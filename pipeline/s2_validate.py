#!/usr/bin/env python
"""s2_validate.py — S2 格式校验：证明"文件合法、完整、能加载"。

URDF 侧：XML 合法 → link/joint 名唯一 → 关节树单根无环 → 网格引用 100% 解析
        （package:// 按包名重映射到本地目录——S2 第一坑）→ 网格非零字节且
        trimesh 读得动（顶点数 > 0）→ yourdfpy 结构化解析交叉确认。
MJCF 侧：XML 合法 → MuJoCo 真编译（最强校验：模型本体 + 场景包装各编一遍）。
产出：reports/S2-validation.md + S2-validation.json。
退出码：0 = 无 FAIL（可进 S3）；1 = 有 FAIL（fail 不静默，全部落报告，修复留 S3）。
"""

import json
import platform
import sys
import time
from collections import Counter, deque
from pathlib import Path

import trimesh
from lxml import etree

import yourdfpy

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "pipeline" / "configs" / "unitree_go2.json"
RAW = ROOT / "workspace" / "raw" / "unitree_go2"
REPORTS = ROOT / "models" / "unitree_go2" / "reports"

# 四态语义（R3 风格基线）：PASS / WARN（有兜底、不阻塞）/ FAIL（阻塞）/ SKIP（不适用）。


def add(results, name, status, detail):
    results.append({"check": name, "status": status, "detail": detail})
    print(f"  [{status}] {name:<30} {detail}")


def resolve_pkg(uri, package, package_root):
    """package://<pkg>/rest → package_root/rest；非本包 URI 返回 None（调用方计失败）。"""
    prefix = f"package://{package}/"
    if uri.startswith(prefix):
        return package_root / uri[len(prefix):]
    return None


def check_urdf_structural(path, package, package_root):
    """lxml 自查：合法、名唯一、单根无环、网格引用、网格可读。返回 (results, root)。"""
    results = []
    try:
        tree = etree.parse(str(path))
        add(results, "urdf:xml-wellformed", "PASS", f"lxml 解析成功（{path.stat().st_size} 字节）")
    except etree.XMLSyntaxError as exc:
        add(results, "urdf:xml-wellformed", "FAIL", f"XML 语法错误：{exc}")
        return results, None
    root = tree.getroot()

    links = root.findall("link")
    joints = root.findall("joint")
    link_names = [l.get("name") for l in links]
    joint_names = [j.get("name") for j in joints]
    dup = [n for n, c in Counter(link_names + joint_names).items() if c > 1]
    add(results, "urdf:names-unique", "PASS" if not dup else "FAIL",
        f"{len(link_names)} links / {len(joints)} joints" + (f"；重名：{dup}" if dup else "，无重名"))

    children = {j.find("child").get("link") for j in joints}
    adjacency = {j.find("parent").get("link"): [] for j in joints}
    for j in joints:
        adjacency[j.find("parent").get("link")].append(j.find("child").get("link"))
    roots = [n for n in link_names if n not in children]
    tree_root = roots[0] if len(roots) == 1 else None
    if tree_root is None:
        add(results, "urdf:tree", "FAIL", f"根节点数 {len(roots)}（应恰为 1）：{roots}")
    else:
        seen, queue = set(), deque([tree_root])
        revisit = False
        while queue:
            node = queue.popleft()
            if node in seen:
                revisit = True
                break
            seen.add(node)
            queue.extend(adjacency.get(node, []))
        if revisit or len(seen) != len(link_names):
            add(results, "urdf:tree", "FAIL",
                f"根={tree_root}；{'重复访问（环/菱形）' if revisit else f'存在不可达 link（{len(seen)}/{len(link_names)}）'}")
        else:
            add(results, "urdf:tree", "PASS", f"根={tree_root}，全树可达，无环无菱形")

    mesh_refs = []
    for link in links:
        for usage in ("visual", "collision"):
            for mesh in link.findall(f"{usage}/geometry/mesh"):
                uri = mesh.get("filename")
                if uri:
                    mesh_refs.append((uri, usage, link.get("name")))
    resolved, missing, foreign = {}, [], []
    for uri, usage, link_name in mesh_refs:
        target = resolve_pkg(uri, package, package_root)
        if target is None:
            foreign.append(f"{uri} @ {link_name}")
        elif target.exists():
            resolved.setdefault(target, []).append(usage)
        else:
            missing.append(f"{uri} @ {link_name}")
    visual_uris = {u for u, usage, _ in mesh_refs if usage == "visual"}
    collision_uris = {u for u, usage, _ in mesh_refs if usage == "collision"}
    add(results, "urdf:mesh-refs", "PASS" if not missing and not foreign else "FAIL",
        f"{len(mesh_refs)} 处引用 → 解析出 {len(resolved)} 个文件，缺失 {len(missing)}，非本包 {len(foreign)}；"
        f"visual 引 {len(visual_uris)} 个文件、collision 引 {len(collision_uris)} 个"
        + ("，集合不同（素材归 S3-A1 清点）" if visual_uris != collision_uris else "，集合相同")
        + (f"；失败明细：{missing[:4] + foreign[:4]}" if missing or foreign else ""))

    bad, v_min = [], None
    for p in sorted(resolved):
        try:
            if p.stat().st_size == 0:
                bad.append(f"{p.name}（0 字节）")
                continue
            mesh = trimesh.load(str(p), force="mesh", process=False)
            v = len(mesh.vertices)
            if v == 0:
                bad.append(f"{p.name}（0 顶点）")
            v_min = v if v_min is None else min(v_min, v)
        except Exception as exc:
            bad.append(f"{p.name}（{type(exc).__name__}: {exc}）")
    add(results, "urdf:mesh-loadable", "PASS" if not bad else "FAIL",
        f"{len(resolved)} 个网格 trimesh 全部读通，最小顶点数 {v_min}" if not bad
        else f"网格读取失败 {len(bad)} 个：{bad[:5]}")

    jtypes = Counter(j.get("type") for j in joints)
    no_limit = [j.get("name") for j in joints
                if j.get("type") in ("revolute", "prismatic") and j.find("limit") is None]
    add(results, "urdf:joint-limits", "PASS" if not no_limit else "FAIL",
        f"关节类型 {dict(jtypes)}"
        + (f"；活动关节缺 <limit>：{no_limit}" if no_limit else
           "；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3）"))
    return results, tree_root


def check_urdf_yourdfpy(path, package_root):
    """yourdfpy 结构化解析交叉确认（load_meshes=False 只验结构，网格已由自查覆盖）。"""
    results = []
    try:
        urdf = yourdfpy.URDF.load(str(path), mesh_dir=str(package_root), load_meshes=False)
        add(results, "urdf:yourdfpy-parse", "PASS",
            f"yourdfpy {yourdfpy.__version__} 解析成功：{len(urdf.link_map)} links / {len(urdf.joint_map)} joints")
    except Exception as exc:
        try:  # 旧签名兜底：不带 load_meshes 再试一次
            urdf = yourdfpy.URDF.load(str(path), mesh_dir=str(package_root))
            add(results, "urdf:yourdfpy-parse", "PASS",
                f"yourdfpy 解析成功（回退签名）：{len(urdf.link_map)} links / {len(urdf.joint_map)} joints")
        except Exception as exc2:
            add(results, "urdf:yourdfpy-parse", "FAIL",
                f"{type(exc).__name__}: {exc}；回退亦败 {type(exc2).__name__}: {exc2}")
    return results


def check_mjcf(path_model, path_scene):
    import mujoco
    results = []
    try:
        etree.parse(str(path_model))
        add(results, "mjcf:xml-wellformed", "PASS", f"lxml 解析成功（{path_model.stat().st_size} 字节）")
    except etree.XMLSyntaxError as exc:
        add(results, "mjcf:xml-wellformed", "FAIL", f"XML 语法错误：{exc}")
        return results
    try:
        t0 = time.perf_counter()
        model = mujoco.MjModel.from_xml_path(str(path_model))
        dt_ms = (time.perf_counter() - t0) * 1000
        add(results, "mjcf:compile-model", "PASS",
            f"nbody={model.nbody} njnt={model.njnt} ngeom={model.ngeom} nmesh={model.nmesh} "
            f"nu={model.nu} nq={model.nq} timestep={model.opt.timestep:.4f}（{dt_ms:.0f} ms）")
    except Exception as exc:
        add(results, "mjcf:compile-model", "FAIL", f"MuJoCo 编译失败——{type(exc).__name__}: {exc}")
    try:
        mujoco.MjModel.from_xml_path(str(path_scene))
        add(results, "mjcf:compile-scene", "PASS", "scene.xml（模型 + 地形 + 光照）编译成功")
    except Exception as exc:
        add(results, "mjcf:compile-scene", "FAIL", f"场景编译失败——{type(exc).__name__}: {exc}")
    return results


def write_report(model, results):
    versions = {
        "yourdfpy": yourdfpy.__version__,
        "trimesh": trimesh.__version__,
        "mujoco": __import__("mujoco").__version__,
        "python": platform.python_version(),
    }
    summary = {
        "model": model,
        "date": time.strftime("%Y-%m-%d %H:%M"),
        "pass": sum(r["status"] == "PASS" for r in results),
        "warn": sum(r["status"] == "WARN" for r in results),
        "fail": sum(r["status"] == "FAIL" for r in results),
        "versions": versions,
    }
    summary["verdict"] = ("全部通过，可进 S3" if summary["fail"] == 0
                          else f"{summary['fail']} 个阻塞项——fail 已如实落表，处置走 S3/送审")
    rows = "\n".join(f"| `{r['check']}` | {r['status']} | {r['detail']} |" for r in results)
    md = (f"# S2 格式校验报告 — {model}（{summary['date']}）\n\n"
          f"环境：yourdfpy {versions['yourdfpy']} · trimesh {versions['trimesh']} · "
          f"mujoco {versions['mujoco']} · Python {versions['python']}\n\n"
          f"## 校验矩阵\n\n| 检查项 | 结果 | 明细 |\n|---|---|---|\n{rows}\n\n"
          f"## 汇总\n\nPASS {summary['pass']} / "
          f"WARN {summary['warn']} / FAIL {summary['fail']}\n\n**结论：{summary['verdict']}**\n")
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "S2-validation.md").write_text(md, encoding="utf-8")
    (REPORTS / "S2-validation.json").write_text(
        json.dumps({"summary": summary, "checks": results}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    return summary


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    s2 = config["s2"]
    print("== URDF 侧 ==")
    u = s2["urdf"]
    urdf_path = RAW / u["source"] / u["rel"]
    pkg_root = RAW / u["source"] / u["package_root"]
    if not urdf_path.exists():
        sys.exit(f"[阻塞] URDF 不存在：{urdf_path}")
    results, _ = check_urdf_structural(urdf_path, u["package"], pkg_root)
    results += check_urdf_yourdfpy(urdf_path, pkg_root)

    print("== MJCF 侧 ==")
    m = s2["mjcf"]
    results += check_mjcf(RAW / m["source"] / m["model_rel"], RAW / m["source"] / m["scene_rel"])

    summary = write_report(config["model"], results)
    print(f"\n汇总：PASS {summary['pass']} / "
          f"WARN {summary['warn']} / FAIL {summary['fail']}")
    print(f"结论：{summary['verdict']}")
    sys.exit(1 if summary["fail"] else 0)


if __name__ == "__main__":
    main()
