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
from collections import Counter
from pathlib import Path

import mujoco
from lxml import etree
import yourdfpy

MODEL_NAME = sys.argv[1] if len(sys.argv) > 1 else "unitree_go2"
ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "pipeline" / "configs" / f"{MODEL_NAME}.json"
RAW = ROOT / "workspace" / "raw" / MODEL_NAME
MODEL = ROOT / "models" / MODEL_NAME
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
    """[(src_abs, dest_rel, kind)]，字节级复制；网格闭包按 dest 去重
    （URDF 17 处 visual 引用共享 7 个物理 dae——终审 F1 修正：引用行 ≠ 文件数）。"""
    s4, s2 = config["s4"], config["s2"]
    ros_dir = RAW / s2["urdf"]["source"]
    mjm_dir = RAW / s2["mjcf"]["source"]
    plan = []
    for item in s4["urdf"]:
        plan.append((ros_dir / item["src_rel"], item["dest"], "urdf"))
    pkg = s4["urdf_meshes"]["package"]
    pkg_root = ros_dir / s2["urdf"]["package_root"]
    urdf_abs = ros_dir / s2["urdf"]["rel"]
    ref_style = s2["urdf"].get("ref_style", "package")
    tree = etree.parse(str(urdf_abs))
    mesh_refs, seen = 0, set()
    for mesh in tree.getroot().iter("mesh"):
        uri = mesh.get("filename") or ""
        if ref_style == "relative":
            # G1 协议：uri 相对 URDF 自身目录（urdf 位于包根）——dest 必须保持
            # "meshes/ 在 urdf 旁边"的相对关系（dest_root 配 "urdf"）。
            # 越界（../ 逃逸）已由 S2 urdf:mesh-refs 检查（G1 实测 0）。
            if uri.startswith(".."):
                continue
            rel = uri
            src = urdf_abs.parent / rel
        else:
            prefix = f"package://{pkg}/"
            if not uri.startswith(prefix):
                continue
            rel = uri[len(prefix):]
            src = pkg_root / rel
        mesh_refs += 1
        if rel in seen:
            continue
        seen.add(rel)
        plan.append((src, f"{s4['urdf_meshes']['dest_root']}/{rel}", "mesh"))
    xd = s4.get("xacro_dir")
    if xd:
        base = ros_dir / xd["src_rel"]
        for p in sorted(base.rglob("*")):
            if p.is_file():
                plan.append((p, f"{xd['dest']}/{p.relative_to(base).as_posix()}", "xacro"))
    for item in s4["mjcf"]:
        plan.append((mjm_dir / item["src_rel"], item["dest"], "mjcf"))
    ad = s4["mjcf_assets"]
    abase = mjm_dir / ad["src_rel"]
    if ad.get("mode") == "closure":
        # G1：MJCF <mesh file=...> 相对 meshdir 的引用闭包（池含未收配置的网格，整拷冗余）
        mxml = etree.parse(str(mjm_dir / s2["mjcf"]["model_rel"]))
        meshdir = mxml.getroot().find("compiler").get("meshdir") if mxml.getroot().find("compiler") is not None else "."
        for m in mxml.getroot().iter("mesh"):
            f = m.get("file")
            if not f:
                continue
            plan.append((abase / f, f"{ad['dest']}/{f}", "asset"))
    else:
        for p in sorted(abase.rglob("*")):
            if p.is_file():
                plan.append((p, f"{ad['dest']}/{p.relative_to(abase).as_posix()}", "asset"))
    for item in s4["images"]:
        src_dir = RAW / item["source"] if item.get("source") else mjm_dir
        plan.append((src_dir / item["src_rel"], item["dest"], "image"))
    dests = [d for _, d, _ in plan]
    assert len(dests) == len(set(dests)), "入库计划出现重复 dest——F1 回归，立即停"
    plan.sort(key=lambda t: t[1])
    return plan, mesh_refs


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    s4 = config["s4"]
    if (MODEL / "urdf").exists():
        sys.exit(f"[拒绝] {MODEL / 'urdf'} 已存在——防覆盖保护，重入库先手删已落位目录")
    plan, mesh_refs = build_plan(config)
    print(f"入库计划：{len(plan)} 个物理文件"
          f"（URDF 引用 {mesh_refs} 处 → 网格物理文件 {sum(1 for _, _, k in plan if k == 'mesh')}——引用行 ≠ 文件数，F1 修正）")

    results, rows = [], []
    for src, dest_rel, kind in plan:
        dest = MODEL / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        rows.append({"dest": dest_rel, "src": src.relative_to(RAW).as_posix(), "kind": kind})

    # 可溯源对账：每文件 SHA256 必须命中 raw manifest 的同路径行
    manifest = {}
    mf = RAW / "manifest.sha256"
    if mf.exists():
        for line in mf.read_text(encoding="utf-8").splitlines():
            if line.strip():
                h, p = line.split("  ", 1)
                manifest.setdefault(h, set()).add(p)
    for r in rows:
        r["sha256"] = sha256_file(MODEL / r["dest"])
        r["traceable"] = r["src"] in manifest.get(r["sha256"], set())
    n_bad = [r["dest"] for r in rows if not r["traceable"]]
    add(results, "s4:traceability", "PASS" if not n_bad else "FAIL",
        f"{len(rows)} 个 raw 源入库文件 SHA256 全部命中 raw manifest 同路径行（逐文件可溯源）"
        + (f"；未命中：{n_bad}" if n_bad else ""))

    # 两源网格哈希交集 → 分/合决策
    mesh_urdf_prefix = s4["urdf_meshes"]["dest_root"] + ("/meshes/" if s4["urdf_meshes"].get("ref_relative", True) and s4["urdf_meshes"]["dest_root"] == "urdf" else "/")
    mesh_mjcf_prefix = s4["mjcf_assets"]["dest"] + "/"
    urdf_hashes = {r["sha256"] for r in rows if r["dest"].startswith(mesh_urdf_prefix)}
    mjcf_hashes = {r["sha256"] for r in rows if r["dest"].startswith(mesh_mjcf_prefix)}
    overlap = urdf_hashes & mjcf_hashes
    verdict = ("两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构"
               if len(overlap) and overlap == urdf_hashes == mjcf_hashes
               else f"哈希交集 {len(overlap)} → 分目录")
    add(results, "s4:mesh-split-decision", "PASS",
        f"URDF 侧 {mesh_refs} 处引用 → {len(urdf_hashes)} 个物理网格 vs MJCF 侧 {len(mjcf_hashes)} 个，"
        f"{verdict}（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案）")

    # dae/ 与 meshes/ 同内容判定（R3-D3 遗留，Go2 特有；config dae_parity 开关，缺省 SKIP）
    same, diff, single = 0, [], 0
    pkg_root = RAW / config["s2"]["urdf"]["source"] / config["s2"]["urdf"]["package_root"]
    dae_parity = s4.get("dae_parity", False)
    if not dae_parity:
        add(results, "s4:dae-dir-parity", "SKIP",
            "本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用")
        redundant_ok = False
    if dae_parity:
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
          f"dae/ 与 meshes/ 同名对比（R3-D3 判定，物理文件口径）：同内容 {same}，不同 {len(diff)}{diff[:4]}，单侧 {single}"
          + ("——meshes/ 为同内容冗余目录，不随库分发" if redundant_ok else "——两目录存在差异，需送审处置"))

    # 覆盖率对账：raw 两个目标子目录 vs 入库 + 排除清单
    # scope 前缀动态算（原硬编码 unitree_robots/go2 对 M1 假阴性——G1 实测教训）
    scope_prefixes = (f"{config['s2']['urdf']['source']}/{config['s2']['urdf']['package_root']}/",
                      f"{config['s2']['mjcf']['source']}/{config['s4']['mjcf'][0]['src_rel'].rsplit('/', 1)[0]}/")
    scope = scope_prefixes
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
    raw_total = sum(1 for p in RAW.rglob("*")
                    if p.is_file() and ".git" not in p.parts and "manifest" not in p.name)
    # G2：目标子目录 = 完整子目录前缀；robots/README.md 这类中间层归"根级及中间层"桶
    scope_files = sum(1 for p in RAW.rglob("*")
                      if p.is_file() and ".git" not in p.parts and "manifest" not in p.name
                      and p.relative_to(RAW).as_posix().startswith(scope_prefixes))
    root_and_mid = raw_total - scope_files  # 两仓库根级 8 + robots 中间层 1（G2 补桶）
    excluded_scope = {e for e in excluded if e.startswith(scope_prefixes)}  # 排除项按桶归位
    add(results, "s4:coverage", "PASS" if not uncovered else "WARN",
        f"raw 全量 {raw_total}（除 .git/manifest）= 根级及中间层 {root_and_mid} + 目标子目录 {scope_files}；"
        f"子目录 {scope_files} 全覆盖 = 入库 {len(rows)} + 排除 {len(excluded_scope)}（其中 meshes/ 冗余 {same}）"
        f"（未覆盖：{uncovered or '无'}）——算式每行必须平（F1 教训）")

    # 最小复验：均指向入库新路径
    rc = s4["recheck"]
    try:
        m = mujoco.MjModel.from_xml_path(str(MODEL / rc["mjcf"]))
        add(results, "s4:recheck-mjcf", "PASS",
            f"入库后 {rc['mjcf']} 编译通过：nbody={m.nbody} ngeom={m.ngeom} nmesh={m.nmesh}（官方相对引用结构保持）")
    except Exception as exc:
        add(results, "s4:recheck-mjcf", "FAIL", f"{type(exc).__name__}: {exc}")
    try:
        u = yourdfpy.URDF.load(str(MODEL / rc["urdf"]),
                               mesh_dir=str(MODEL / rc["urdf_mesh_dir"]), load_meshes=False)
        add(results, "s4:recheck-urdf", "PASS",
            f"入库后 URDF yourdfpy 解析通过：{len(u.link_map)} links（{rc['note']}）")
    except Exception as exc:
        add(results, "s4:recheck-urdf", "FAIL", f"{type(exc).__name__}: {exc}")

    # 非 raw 源的入库件（质检截图等）——F1：物理文件口径 = raw 溯源件 + 质检自产件
    raw_srcs = {r["dest"] for r in rows}
    known_docs = {"README.md", "SOURCE.md"}
    non_raw = sorted(
        p.relative_to(MODEL).as_posix() for p in MODEL.rglob("*")
        if p.is_file()
        and p.relative_to(MODEL).as_posix() not in raw_srcs
        and not p.relative_to(MODEL).as_posix().startswith(("reports/", "evidence/"))
        and p.relative_to(MODEL).as_posix() not in known_docs
        and not p.name.startswith("LICENSE-upstream"))
    total = sum(p.stat().st_size for p in MODEL.rglob("*")
                if p.is_file()
                and not p.relative_to(MODEL).as_posix().startswith(("reports/", "evidence/"))
                and p.relative_to(MODEL).as_posix() not in known_docs
                and not p.name.startswith("LICENSE-upstream"))
    physical = len(rows) + len(non_raw)
    pins = {s["name"]: s["pin"] for s in config["sources"]}
    model_readme = MODEL / "README.md"
    if not model_readme.exists():  # S4 只补骨架；S7 全文模型页不被重跑覆盖
        model_readme.write_text(
            f"# {MODEL_NAME} — 模型页（S4 入库骨架，S7 补全）\n\n"
            f"> **provenance**：unitreerobotics/unitree_ros@`{pins['unitree_ros']}` + "
            f"unitreerobotics/unitree_mujoco@`{pins['unitree_mujoco']}`；license BSD-3-Clause"
            f"（SOURCE.md / LICENSE-upstream-*）；模型资产+质检截图 {physical} 文件 / {total / 1e6:.1f} MB"
            f"（不含 reports/evidence/文档）。\n"
            f"> **质检**：S2 全绿（reports/S2-validation.md）· S3 体检 8P/4W/0F（reports/S3-physics.md，"
            f"calf 分歧披露待 S7/E1）· 入库对账 reports/S4-package.md（逐文件哈希溯源）。\n",
            encoding="utf-8")

    n_fail = sum(r["status"] == "FAIL" for r in results)
    n_warn = sum(r["status"] == "WARN" for r in results)
    table = "\n".join(f"| {r['dest']} | {r['src']} | `{r['sha256'][:12]}…` | {'✓' if r['traceable'] else '✗'} |"
                      for r in rows)
    checks = "\n".join(f"| `{r['check']}` | {r['status']} | {r['detail']} |" for r in results)
    kind_count = Counter(r["kind"] for r in rows)
    rows_bytes = sum((MODEL / r["dest"]).stat().st_size for r in rows)
    non_raw_bytes = total - rows_bytes
    md = (f"# S4 入库对账报告 — {config['model']}（{time.strftime('%Y-%m-%d %H:%M')}）\n\n"
          f"**物理文件口径（终审 F1 修正）**：入库物理文件 {physical} = raw 溯源件 {len(rows)}"
          f"（URDF 引用 {mesh_refs} 处 → 网格物理文件 {kind_count.get('mesh', 0)}，引用行 ≠ 文件数）"
          f" + 质检自产件 {len(non_raw)}{non_raw}；"
          f"**总 {total / 1e6:.1f} MB（raw 溯源件 {rows_bytes:,} B + 质检自产件 {non_raw_bytes:,} B，G1 口径注明）**"
          f"（不含 reports/evidence/文档）。"
          f"字节级复制，raw 未动。\n\n"
          f"**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——"
          f"本报告必须始终等于当前磁盘事实。\n\n"
          f"## 分类汇总\n\n" + " · ".join(f"{k} {v}" for k, v in sorted(kind_count.items()))
          + (f" · 质检自产 {len(non_raw)}" if non_raw else "") + "\n\n"
          f"## 检查矩阵\n\n| 检查项 | 结果 | 明细 |\n|---|---|---|\n{checks}\n\n"
          f"## 逐文件对账（raw 溯源件 {len(rows)}）\n\n| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |\n|---|---|---|---|\n{table}\n\n"
          f"## 排除清单（config s4.excluded）\n\n"
          + "\n".join(f"- `{e['src']}` — {e['why']}" for e in s4["excluded"])
          + f"\n\n**结论**：{'入库完成，可进 S5/S6' if n_fail == 0 else '存在 FAIL，停手处置'}"
          f"（FAIL {n_fail} / WARN {n_warn}）\n")
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "S4-package.md").write_text(md, encoding="utf-8")
    (REPORTS / "S4-package.json").write_text(
        json.dumps({"rows": rows, "checks": results, "total_bytes": total,
                    "physical_files": physical, "non_raw": non_raw},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n入库完成：物理文件 {physical}（raw 溯源 {len(rows)} + 质检自产 {len(non_raw)}）"
          f" / {total / 1e6:.1f} MB；FAIL {n_fail} / WARN {n_warn}")
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
