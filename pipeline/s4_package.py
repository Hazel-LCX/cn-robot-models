#!/usr/bin/env python
"""s4_package.py — S4 双格式入库：把过检文件按最终结构落 models/，每个文件可溯源。

入库范围（config s4 段驱动）：URDF + 引用闭包网格（urdf_meshes/，保留包内相对路径）+
xacro/ 存档（修正 8）+ MJCF 双件 + assets/（保持官方 meshdir 相对引用，不改官方一字节）+
产品图 images/。排除清单逐项记 why（对账"无多无缺"的"缺"侧依据）。
动作：字节级复制 → 每文件 SHA256 + 在 raw manifest 中对账（可溯源）→ 两源网格哈希交集
（分/合决策）→ dae/ 与 meshes/ 同内容判定（R3-D3 遗留）→ 覆盖率对账 → 最小复验
（MJCF 编译 + yourdfpy 加载，均指向入库新路径）→ 总体积 → provenance README 骨架。
产出：models/unitree_go2/** + reports/S4-package.{md,json}。raw 永不被写。
幂等保护：models/unitree_go2/urdf 已存在则拒绝（防覆盖，重入库先手删）。
"""

import hashlib
import json
import shutil
import sys
import time
from pathlib import Path

import mujoco
from lxml import etree
import yourdfpy

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "pipeline" / "configs" / "unitree_go2.json"
RAW = ROOT / "workspace" / "raw" / "unitree_go2"
MODEL = ROOT / "models" / "unitree_go2"
REPORTS = MODEL / "reports"


def add(results, name, status, detail):
    results.append({"check": name, "status": status, "detail": detail})
    print(f"  [{status}] {name:<24} {detail}")


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build_plan(config):
    """[(src_abs, dest_rel)]，全部为字节级复制；网格闭包从 raw URDF 解析。"""
    s4, s2 = config["s4"], config["s2"]
    ros_dir = RAW / s2["urdf"]["source"]
    mjm_dir = RAW / s2["mjcf"]["source"]
    plan = []
    for item in s4["urdf"]:
        plan.append((ros_dir / item["src_rel"], item["dest"]))
    pkg = s4["urdf_meshes"]["package"]
    pkg_root = ros_dir / s2["urdf"]["package_root"]
    tree = etree.parse(str(ros_dir / s2["urdf"]["rel"]))
    for mesh in tree.getroot().iter("mesh"):
        uri = mesh.get("filename") or ""
        prefix = f"package://{pkg}/"
        if uri.startswith(prefix):
            rel = uri[len(prefix):]
            plan.append((pkg_root / rel, f"{s4['urdf_meshes']['dest_root']}/{rel}"))
    xd = s4["xacro_dir"]
    base = ros_dir / xd["src_rel"]
    for p in sorted(base.rglob("*")):
        if p.is_file():
            plan.append((p, f"{xd['dest']}/{p.relative_to(base).as_posix()}"))
    for item in s4["mjcf"]:
        plan.append((mjm_dir / item["src_rel"], item["dest"]))
    ad = s4["mjcf_assets"]
    abase = mjm_dir / ad["src_rel"]
    for p in sorted(abase.rglob("*")):
        if p.is_file():
            plan.append((p, f"{ad['dest']}/{p.relative_to(abase).as_posix()}"))
    for item in s4["images"]:
        plan.append((mjm_dir / item["src_rel"], item["dest"]))
    return plan


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    s4 = config["s4"]
    if (MODEL / "urdf").exists():
        sys.exit(f"[拒绝] {MODEL / 'urdf'} 已存在——防覆盖保护，重入库先手删已落位目录")
    plan = build_plan(config)
    print(f"入库计划：{len(plan)} 个文件（URDF 1 + 网格闭包 + xacro + MJCF 2 + assets + 产品图）")

    results, rows = [], []
    for src, dest_rel in plan:
        dest = MODEL / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        rows.append({"dest": dest_rel, "src": src.relative_to(RAW).as_posix()})

    # 可溯源对账：每文件 SHA256 必须命中 raw manifest 的同路径行
    manifest = {}
    mf = RAW / "manifest.sha256"
    if mf.exists():
        for line in mf.read_text(encoding="utf-8").splitlines():
            if line.strip():
                h, p = line.split("  ", 1)
                manifest.setdefault(h, p)
    for r in rows:
        r["sha256"] = sha256_file(MODEL / r["dest"])
        r["traceable"] = manifest.get(r["sha256"]) == r["src"]
    n_bad = [r["dest"] for r in rows if not r["traceable"]]
    add(results, "s4:traceability", "PASS" if not n_bad else "FAIL",
        f"{len(rows)} 个入库文件 SHA256 全部命中 raw manifest 同路径行（逐文件可溯源）"
        + (f"；未命中：{n_bad}" if n_bad else ""))

    # 两源网格哈希交集 → 分/合决策
    urdf_hashes = {r["sha256"] for r in rows if r["dest"].startswith("urdf_meshes/")}
    mjcf_hashes = {r["sha256"] for r in rows if r["dest"].startswith("mjcf/assets/")}
    overlap = urdf_hashes & mjcf_hashes
    add(results, "s4:mesh-split-decision", "PASS",
        f"URDF 侧 {len(urdf_hashes)} 个网格（dae）vs MJCF 侧 {len(mjcf_hashes)} 个（obj），"
        f"哈希交集 {len(overlap)} → 决策：分目录；MJCF 网格落位 mjcf/assets/"
        "（保持官方 meshdir 相对引用，不改官方一字节——§4 树中 mjcf_meshes/ 的实际形态，记录在案）")

    # dae/ 与 meshes/ 同内容判定（R3-D3 遗留）
    pkg_root = RAW / config["s2"]["urdf"]["source"] / config["s2"]["urdf"]["package_root"]
    same, diff, single = 0, [], 0
    for r in rows:
        if r["dest"].startswith("urdf_meshes/dae/"):
            rel = r["dest"][len("urdf_meshes/dae/"):]
            a, b = pkg_root / "dae" / rel, pkg_root / "meshes" / rel
            if a.exists() and b.exists():
                if sha256_file(a) == sha256_file(b):
                    same += 1
                else:
                    diff.append(rel)
            else:
                single += 1
    redundant_ok = same > 0 and not diff
    add(results, "s4:dae-dir-parity", "PASS" if redundant_ok else "WARN",
        f"dae/ 与 meshes/ 同名对比（R3-D3 判定）：同内容 {same}，不同 {len(diff)}{diff[:4]}，单侧 {single}"
        + ("——meshes/ 为同内容冗余目录，不随库分发" if redundant_ok else "——两目录存在差异，需送审处置"))

    # 覆盖率对账：raw 两个目标子目录 vs 入库 + 排除清单
    scope = (f"{config['s2']['urdf']['source']}/{config['s2']['urdf']['package_root']}/",
             f"{config['s2']['mjcf']['source']}/unitree_robots/go2/")
    excluded = set()
    for item in s4["excluded"]:
        p = RAW / item["src"]
        if p.is_dir():
            excluded.update(q.relative_to(RAW).as_posix() for q in p.rglob("*") if q.is_file())
        else:
            excluded.add(item["src"])
    if redundant_ok:  # meshes/ 冗余目录按判定排除：dae/<rel> 同内容 → meshes/<rel> 一并排除
        excluded.update(
            f"{config['s2']['urdf']['source']}/{config['s2']['urdf']['package_root']}/meshes/"
            + r["dest"][len("urdf_meshes/dae/"):]
            for r in rows if r["dest"].startswith("urdf_meshes/dae/"))
    covered = {r["src"] for r in rows} | excluded
    uncovered = sorted(
        p.relative_to(RAW).as_posix() for p in RAW.rglob("*")
        if p.is_file() and ".git" not in p.parts and "manifest" not in p.name
        and any(p.relative_to(RAW).as_posix().startswith(s) for s in scope)
        and p.relative_to(RAW).as_posix() not in covered)
    raw_count = sum(1 for p in RAW.rglob("*")
                    if p.is_file() and ".git" not in p.parts and "manifest" not in p.name)
    add(results, "s4:coverage", "PASS" if not uncovered else "WARN",
        f"raw 目标子目录内 {raw_count} 文件（不含 .git），"
        f"入库 {len(rows)} + 排除 {len(excluded)}（含 meshes/ 冗余 {same}）；未覆盖：{uncovered or '无'}")

    # 最小复验：均指向入库新路径
    try:
        m = mujoco.MjModel.from_xml_path(str(MODEL / "mjcf" / "go2.xml"))
        add(results, "s4:recheck-mjcf", "PASS",
            f"入库后 mjcf/go2.xml 编译通过：nbody={m.nbody} ngeom={m.ngeom}（meshdir=assets 相对结构保持）")
    except Exception as exc:
        add(results, "s4:recheck-mjcf", "FAIL", f"{type(exc).__name__}: {exc}")
    try:
        u = yourdfpy.URDF.load(str(MODEL / "urdf" / "go2_description.urdf"),
                               mesh_dir=str(MODEL / "urdf_meshes"), load_meshes=False)
        add(results, "s4:recheck-urdf", "PASS",
            f"入库后 URDF yourdfpy 解析通过：{len(u.link_map)} links（package:// 重映射到 urdf_meshes/）")
    except Exception as exc:
        add(results, "s4:recheck-urdf", "FAIL", f"{type(exc).__name__}: {exc}")

    total = sum((MODEL / r["dest"]).stat().st_size for r in rows)
    pins = {s["name"]: s["pin"] for s in config["sources"]}
    (MODEL / "README.md").write_text(
        f"# unitree_go2 — 模型页（S4 入库骨架，S7 补全）\n\n"
        f"> **provenance**：unitreerobotics/unitree_ros@`{pins['unitree_ros']}` + "
        f"unitreerobotics/unitree_mujoco@`{pins['unitree_mujoco']}`；license BSD-3-Clause"
        f"（SOURCE.md / LICENSE-upstream-*）；总体积 {total / 1e6:.1f} MB / {len(rows)} 文件。\n"
        f"> **质检**：S2 全绿（reports/S2-validation.md）· S3 体检 8P/4W/0F（reports/S3-physics.md，"
        f"calf 分歧披露待 S7/E1）· 入库对账 reports/S4-package.md（逐文件哈希溯源）。\n",
        encoding="utf-8")

    n_fail = sum(r["status"] == "FAIL" for r in results)
    n_warn = sum(r["status"] == "WARN" for r in results)
    table = "\n".join(f"| {r['dest']} | {r['src']} | `{r['sha256'][:12]}…` | {'✓' if r['traceable'] else '✗'} |"
                      for r in rows)
    checks = "\n".join(f"| `{r['check']}` | {r['status']} | {r['detail']} |" for r in results)
    md = (f"# S4 入库对账报告 — {config['model']}（{time.strftime('%Y-%m-%d %H:%M')}）\n\n"
          f"入库 {len(rows)} 文件 / {total / 1e6:.1f} MB（字节级复制，raw 未动）。\n\n"
          f"## 检查矩阵\n\n| 检查项 | 结果 | 明细 |\n|---|---|---|\n{checks}\n\n"
          f"## 逐文件对账\n\n| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |\n|---|---|---|---|\n{table}\n\n"
          f"## 排除清单（config s4.excluded）\n\n"
          + "\n".join(f"- `{e['src']}` — {e['why']}" for e in s4["excluded"])
          + f"\n\n**结论**：{'入库完成，可进 S5/S6' if n_fail == 0 else '存在 FAIL，停手处置'}"
          f"（FAIL {n_fail} / WARN {n_warn}）\n")
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "S4-package.md").write_text(md, encoding="utf-8")
    (REPORTS / "S4-package.json").write_text(
        json.dumps({"rows": rows, "checks": results, "total_bytes": total},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n入库完成：{len(rows)} 文件 / {total / 1e6:.1f} MB；FAIL {n_fail} / WARN {n_warn}")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
