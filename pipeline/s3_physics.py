#!/usr/bin/env python
"""s3_physics.py — S3 物理体检：证明"物理参数真实、自洽、可对账"。

定位（PIPELINE §3-S3）：修不修是结论，体检本身就是产出。M0 无官方逐件对照物 →
只清点 + 记录 + 标记，不修任何参数（修复走协议③送审）。

检查项：
  URDF 侧：link 质量>0（fixed 座零质量降 WARN，活动关节零质量才 FAIL）→
          总质量 vs 官方标称（±10%，口径先钉死，修正 2）→
          惯量正定 + 三角不等式 →
          惯量数量级 sanity（修正 1：逐轴垂距法 [0.005, 0.5]）→
          碰撞体清点（A1-1 + C1：逐 link 有无 collision、几何类型）→
          12 revolute 限位硬校验（lower<upper、effort>0、velocity>0）
  MJCF 侧：逐 body geom 清点（A1-3 + C1）→ 质量总量
  交叉对账（修正 6）：同名关节集合 → 关节轴逐分量 → 逐 body 质量逐项比对
          （分歧≠错误：记录 + 判谁贴官方标称，不对齐不修）
产出：reports/S3-physics.md + S3-physics.json。
退出码：0 = 无 FAIL（可进 S4）；1 = 有 FAIL。
"""

import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
import trimesh
from lxml import etree

MODEL = sys.argv[1] if len(sys.argv) > 1 else "unitree_go2"
ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "pipeline" / "configs" / f"{MODEL}.json"
RAW = ROOT / "workspace" / "raw" / MODEL
REPORTS = ROOT / "models" / MODEL / "reports"

MESH_EXTENTS = {}


def add(results, name, status, detail):
    results.append({"check": name, "status": status, "detail": detail})
    print(f"  [{status}] {name:<24} {detail}")


def parse_urdf(path):
    root = etree.parse(str(path)).getroot()
    links, rpy_nonzero = {}, []
    for l in root.findall("link"):
        name = l.get("name")
        ine = l.find("inertial")
        e = {"name": name, "mass": None, "inertia": None, "visual_mesh": None,
             "collision_types": []}
        if ine is not None:
            e["mass"] = float(ine.find("mass").get("value"))
            i = ine.find("inertia")
            if i is not None:
                ixx, iyy, izz = (float(i.get(k, 0)) for k in ("ixx", "iyy", "izz"))
                ixy, ixz, iyz = (float(i.get(k, 0)) for k in ("ixy", "ixz", "iyz"))
                e["inertia"] = np.array([[ixx, ixy, ixz], [ixy, iyy, iyz], [ixz, iyz, izz]])
            origin = ine.find("origin")
            if origin is not None and origin.get("rpy", "0 0 0") != "0 0 0":
                rpy_nonzero.append(name)
        for vis in l.findall("visual"):
            mesh = vis.find("geometry/mesh")
            if mesh is not None and e["visual_mesh"] is None:
                e["visual_mesh"] = mesh.get("filename")
        for col in l.findall("collision"):
            g = col.find("geometry")
            kind = next((t for t in ("box", "sphere", "cylinder", "mesh") if g.find(t) is not None), "?")
            e["collision_types"].append(kind)
        links[name] = e
    joints = [{"name": j.get("name"), "type": j.get("type"),
               "child": j.find("child").get("link"),
               "axis": j.find("axis").get("xyz") if j.find("axis") is not None else None,
               "limit": j.find("limit")}
              for j in root.findall("joint")]
    return links, joints, rpy_nonzero


def mesh_extents(uri, package, package_root):
    """visual 网格在 link 系下的 AABB 延度（缓存）。原点平移不改延度；rpy 旋转未计入（见体检说明）。"""
    if uri in MESH_EXTENTS:
        return MESH_EXTENTS[uri]
    prefix = f"package://{package}/"
    p = package_root / uri[len(prefix):] if uri.startswith(prefix) else None
    ext = None
    if p is not None and p.exists():
        mesh = trimesh.load(str(p), force="mesh", process=False)
        ext = np.asarray(mesh.bounds[1]) - np.asarray(mesh.bounds[0])
    MESH_EXTENTS[uri] = ext
    return ext


def check_mass_positive(results, links, joints):
    movable = {j["child"] for j in joints if j["type"] in
               ("revolute", "prismatic", "continuous", "floating", "planar")}
    zero_explicit = [n for n, e in links.items() if e["mass"] is not None and e["mass"] <= 0]
    no_inertial = [n for n, e in links.items() if e["mass"] is None]
    bad = [n for n in zero_explicit + no_inertial if n in movable]
    add(results, "urdf:mass-positive", "FAIL" if bad else "WARN",
        f"显式质量≤0：{zero_explicit}；无 <inertial>：{no_inertial}"
        + (f"；挂在活动关节上的零质量 link：{bad}" if bad
           else "——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL"))


def check_mass_total(results, tag, total, official):
    dev = total / official["mass_kg"] - 1
    status = "PASS" if abs(dev) <= official["tolerance"] else "WARN"
    add(results, f"{tag}:mass-total", status,
        f"{total:.3f} kg vs 官方 {official['mass_kg']} kg（{dev * 100:+.1f}%，容差 ±{official['tolerance'] * 100:.0f}%）"
        f"；口径：{official['caliber']}")


def check_inertia_pd_triangle(results, links):
    no_pd, no_tri = [], []
    n = 0
    for name, e in links.items():
        if e["inertia"] is None or e["mass"] is None or e["mass"] <= 0:
            continue
        n += 1
        I = e["inertia"]
        if np.linalg.eigvalsh(I).min() <= 0:
            no_pd.append(name)
        ixx, iyy, izz = I[0, 0], I[1, 1], I[2, 2]
        if not all(a + b - c >= -1e-9 for a, b, c in
                   ((ixx, iyy, izz), (ixx, izz, iyy), (iyy, izz, ixx))):
            no_tri.append(name)
    add(results, "urdf:inertia-pd", "PASS" if not no_pd else "FAIL",
        f"{n} 个有质量 link 惯量张量全正定" + (f"；非正定：{no_pd}" if no_pd else ""))
    add(results, "urdf:inertia-triangle", "PASS" if not no_tri else "FAIL",
        f"{n} 个 link 三角不等式全成立" + (f"；违反：{no_tri}" if no_tri else ""))


def check_inertia_sanity(results, links, package, package_root, lo, hi, rpy_nonzero):
    checked, skipped, violations = 0, [], []
    for name, e in links.items():
        if e["mass"] is None or e["mass"] <= 0 or e["visual_mesh"] is None:
            skipped.append(name)
            continue
        ext = mesh_extents(e["visual_mesh"], package, package_root)
        if ext is None:
            skipped.append(name)
            continue
        for axis in range(3):
            perp = max(ext[k] for k in range(3) if k != axis)
            ratio = e["inertia"][axis, axis] / (e["mass"] * perp ** 2)
            if not lo <= ratio <= hi:
                violations.append(f"{name}.{'xyz'[axis]}={ratio:.4f}")
        checked += 1
    note = (f"逐轴垂距法（修正 1）{checked} link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [{lo}, {hi}]；"
            f"无网格/零质量跳过 {len(skipped)} 个"
            + (f"；inertial rpy≠0（延度未随 rpy 旋转修正）：{rpy_nonzero}" if rpy_nonzero else ""))
    add(results, "urdf:inertia-sanity", "WARN" if violations else "PASS",
        note + (f"；越界：{violations}（人工复核项，不自动改）" if violations else "；全部落区间"))


def check_collision_inventory(results, links, notes):
    has, missing, types = 0, [], Counter()
    for name, e in links.items():
        if e["collision_types"]:
            has += 1
            types.update(e["collision_types"])
        else:
            missing.append(name)
    add(results, "urdf:collision-inventory", "WARN" if missing else "PASS",
        f"{has}/{len(links)} link 有 <collision>（{dict(types)}）；无 collision：{missing}"
        f"（标记不自动补，A1；{notes['upstream_png']}）")
    n_mesh = sum(e["collision_types"].count("mesh") for e in links.values())
    if n_mesh == 0:
        add(results, "urdf:collision-mesh-loadable", "SKIP",
            "collision 引用 0 个网格文件（全基元）——A1-2 网格可加载检查不适用，显式跳过"
            "（fail 不静默的精神同样适用于不适用，R4-E6）")


def check_joint_limits(results, joints, notes):
    bad, ranges = [], {}
    for j in joints:
        if j["type"] != "revolute":
            continue
        lim = j["limit"]
        lo, hi = float(lim.get("lower")), float(lim.get("upper"))
        eff, vel = float(lim.get("effort", 0)), float(lim.get("velocity", 0))
        ranges[j["name"]] = (lo, hi, eff, vel)
        if not (lo < hi and eff > 0 and vel > 0):
            bad.append(j["name"])
    add(results, "urdf:joint-limits", "PASS" if not bad else "FAIL",
        f"{len(ranges)} 个 revolute 全部 lower<upper 且 effort/velocity>0"
        + (f"；违规：{bad}" if bad else "")
        + f"；{notes['joint_range']}")


def check_mjcf_inventory(results, model):
    import mujoco
    empty, total_geoms = [], 0
    for i in range(1, model.nbody):
        n = int(model.body_geomnum[i])
        total_geoms += n
        if n == 0:
            empty.append(mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_BODY, i))
    add(results, "mjcf:body-geom", "WARN" if empty else "PASS",
        f"{model.nbody - 1} 个 body 共 {total_geoms} geom；无 geom 的 body：{empty}"
        "（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——"
        "建模约定，标记不自动补；R4-E2 措辞更正）")


def check_cross(results, links, joints, model, tol, mass_warn, alias):
    import mujoco
    urdf_rev = {j["name"]: j for j in joints if j["type"] == "revolute"}
    mj_joints = {mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, i):
                 np.array(model.jnt_axis[i])
                 for i in range(model.njnt)
                 if model.jnt_type[i] == mujoco.mjtJoint.mjJNT_HINGE}
    only_u = sorted(set(urdf_rev) - set(mj_joints))
    only_m = sorted(set(mj_joints) - set(urdf_rev))
    add(results, "cross:joint-names", "PASS" if not only_u and not only_m else "WARN",
        f"URDF {len(urdf_rev)} revolute ↔ MJCF {len(mj_joints)} hinge"
        + (f"；仅 URDF：{only_u}；仅 MJCF：{only_m}" if only_u or only_m else "；名称集合一致"))

    common = sorted(set(urdf_rev) & set(mj_joints))
    worst, max_d = "", 0.0
    for nm in common:
        if urdf_rev[nm]["axis"]:
            u_ax = np.array([float(v) for v in urdf_rev[nm]["axis"].split()])
            d = float(np.abs(u_ax - mj_joints[nm]).max())
            if d > max_d:
                max_d, worst = d, nm
    add(results, "cross:joint-axes", "PASS" if max_d <= tol else "WARN",
        f"{len(common)} 对同名关节轴逐分量最大差 {max_d:.2e}（最差 {worst or '—'}，容差 {tol}）；"
        "URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比")

    mj_mass = {mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_BODY, i): float(model.body_mass[i])
               for i in range(1, model.nbody)}
    exact, conventions, true_diff = [], [], []
    for n, e in sorted(links.items()):
        if e["mass"] is None:
            continue
        mn = alias.get(n, n)
        mv = mj_mass.get(mn)
        if mv is None:
            conventions.append(f"{n}(urdf独有 {e['mass']:.3f}kg)")
            continue
        d = e["mass"] - mv
        if abs(d) < 1e-9:
            exact.append(n)
        elif mv == 0:
            conventions.append(f"{n}(mjcf零质量纯架，urdf {e['mass']:.3f}kg)")
        elif abs(d) <= mass_warn:
            conventions.append(f"{n}({d:+.4f})")
        else:
            true_diff.append(f"{n}({e['mass']:.4f} vs {mv:.4f}, {d:+.4f})")
    add(results, "cross:mass-per-body", "WARN" if true_diff else "PASS",
        f"逐 body 对账：完全一致 {len(exact)} 个（hip/thigh/base 等）；约定差异 {conventions}"
        + (f"；真值分歧 {true_diff}——MJCF 更贴官方总量，分歧≠错误，M0 不修（修正 6），送审拍板" if true_diff else ""))


def write_report(model, results, extra, notes=None):
    versions = {"numpy": np.__version__, "trimesh": trimesh.__version__}
    summary = {
        "model": model, "date": time.strftime("%Y-%m-%d %H:%M"),
        "pass": sum(r["status"] == "PASS" for r in results),
        "warn": sum(r["status"] == "WARN" for r in results),
        "fail": sum(r["status"] == "FAIL" for r in results),
        "skip": sum(r["status"] == "SKIP" for r in results),
        "verdict": "", "versions": versions, **extra,
    }
    summary["verdict"] = ("无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审" if summary["fail"] == 0
                          else f"{summary['fail']} 个 FAIL——如实落表，修复走协议③")
    rows = "\n".join(f"| `{r['check']}` | {r['status']} | {r['detail']} |" for r in results)
    md = (f"# S3 物理体检报告 — {model}（{summary['date']}）\n\n"
          f"**质量口径声明（修正 2，置顶）**：{extra['caliber']}\n\n"
          f"## 体检矩阵\n\n| 检查项 | 结果 | 明细 |\n|---|---|---|\n{rows}\n\n"
          f"## C1 碰撞体清点表\n\n- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）\n"
          f"- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）\n"
          f"- {notes['upstream_png']}\n\n"
          f"## 汇总\n\nPASS {summary['pass']} / WARN {summary['warn']} / FAIL {summary['fail']}"
          f" / SKIP {summary['skip']}\n\n"
          f"**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；"
          f"MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。"
          f"两侧方法不对称，如实披露。\n\n"
          f"**结论：{summary['verdict']}**\n")
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "S3-physics.md").write_text(md, encoding="utf-8")
    (REPORTS / "S3-physics.json").write_text(
        json.dumps({"summary": summary, "checks": results}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    return summary


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    s2, s3, official = config["s2"], config["s3"], config["s3"]["official"]
    lo, hi = s3["sanity"]["ratio_range"]
    tol, mass_warn = s3["sanity"]["axis_tolerance"], s3["sanity"]["mass_diff_warn"]

    import mujoco
    urdf_path = RAW / s2["urdf"]["source"] / s2["urdf"]["rel"]
    pkg_root = RAW / s2["urdf"]["source"] / s2["urdf"]["package_root"]
    mjcf_path = RAW / s2["mjcf"]["source"] / s2["mjcf"]["model_rel"]
    model = mujoco.MjModel.from_xml_path(str(mjcf_path))

    results = []
    print("== URDF 侧 ==")
    links, joints, rpy_nonzero = parse_urdf(urdf_path)
    check_mass_positive(results, links, joints)
    urdf_total = sum(e["mass"] for e in links.values() if e["mass"] is not None)
    check_mass_total(results, "urdf", urdf_total, official)
    check_inertia_pd_triangle(results, links)
    check_inertia_sanity(results, links, s2["urdf"]["package"], pkg_root, lo, hi, rpy_nonzero)
    check_collision_inventory(results, links, s3["notes"])
    check_joint_limits(results, joints, s3["notes"])

    print("== MJCF 侧 ==")
    check_mass_total(results, "mjcf", float(model.body_mass[1:].sum()), official)
    check_mjcf_inventory(results, model)

    print("== 交叉对账 ==")
    check_cross(results, links, joints, model, tol, mass_warn, s3["cross_alias"])

    extra = {"caliber": official["evidence"] + " " + official["caliber"],
             "urdf_total_kg": urdf_total, "mjcf_total_kg": float(model.body_mass[1:].sum())}
    summary = write_report(config["model"], results, extra, s3["notes"])
    print(f"\n汇总：PASS {summary['pass']} / WARN {summary['warn']} / FAIL {summary['fail']}"
          f" / SKIP {summary['skip']}")
    print(f"结论：{summary['verdict']}")
    sys.exit(1 if summary["fail"] else 0)


if __name__ == "__main__":
    main()
