#!/usr/bin/env python
"""s6_bench.py — S6 加载/步速基准：用可复现的跑法拿数字。

MJCF：MuJoCo 加载耗时（中位数）+ 预热 ≥100 步丢弃后计 mj_step ×10⁴
      （B2：预热丢启动噪声，10⁴ 步对 12 关节才有意义），重复 5 次取中位数；
      场景 = 固定 qpos0、纯重力、无控制器（不掺控制变量）。
URDF：yourdfpy 解析耗时（中位数）——如实标注：URDF 无物理引擎，只测加载。
稳定性：steps/s 的 min-max 展幅 < 20% 才算稳（S6 验收）。
基准对象 = models/ 入库件（不是 raw）。输出 reports/S6-benchmark.{md,json}。
"""

import json
import platform
import statistics
import sys
import time
from pathlib import Path

import mujoco
import yourdfpy

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "pipeline" / "configs" / "unitree_go2.json"
MODEL = ROOT / "models" / "unitree_go2"
REPORTS = MODEL / "reports"


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    s2, s6 = config["s2"], config["s6"]
    mjcf = MODEL / "mjcf" / "go2.xml"      # 基准测入库件
    urdf = MODEL / "urdf" / "go2_description.urdf"
    mesh_dir = MODEL / "urdf_meshes"
    results = []

    def add(name, value, detail):
        results.append({"check": name, "value": value, "detail": detail})
        print(f"  {name:<22} {detail}")

    print("== MJCF（MuJoCo，入库件）==")
    loads = []
    for _ in range(s6["repeats"]):
        t0 = time.perf_counter()
        mujoco.MjModel.from_xml_path(str(mjcf))
        loads.append((time.perf_counter() - t0) * 1000)
    med_load = statistics.median(loads)
    add("mjcf:load-time", round(med_load, 2),
        f"{med_load:.2f} ms（{s6['repeats']} 次中位数；min {min(loads):.2f} / max {max(loads):.2f}）")

    model = mujoco.MjModel.from_xml_path(str(mjcf))
    data = mujoco.MjData(model)
    for _ in range(s6["warmup_steps"]):
        mujoco.mj_step(model, data)
    rates, us_per = [], []
    for _ in range(s6["repeats"]):
        t0 = time.perf_counter()
        for _ in range(s6["bench_steps"]):
            mujoco.mj_step(model, data)
        dt = time.perf_counter() - t0
        rates.append(s6["bench_steps"] / dt)
        us_per.append(dt / s6["bench_steps"] * 1e6)
    med_rate = statistics.median(rates)
    spread = (max(rates) - min(rates)) / med_rate
    add("mjcf:step-rate", round(med_rate),
        f"{med_rate:,.0f} steps/s（{s6['bench_steps']:,} 步 × {s6['repeats']} 次、预热 {s6['warmup_steps']} 丢弃；"
        f"µs/step 中位 {statistics.median(us_per):.1f}；场景：{s6['scenario']}）")
    add("mjcf:stability", "PASS" if spread < 0.20 else "WARN",
        f"steps/s 展幅 {(max(rates) - min(rates)):,.0f}（{spread * 100:.1f}%，验收 <20%）")

    print("== URDF（yourdfpy，入库件）==")
    parses = []
    for _ in range(s6["repeats"]):
        t0 = time.perf_counter()
        yourdfpy.URDF.load(str(urdf), mesh_dir=str(mesh_dir), load_meshes=False)
        parses.append((time.perf_counter() - t0) * 1000)
    med_parse = statistics.median(parses)
    add("urdf:parse-time", round(med_parse, 2),
        f"{med_parse:.2f} ms（{s6['repeats']} 次中位数）——URDF 无物理引擎，只测加载，如实标注")

    machine = {
        "platform": f"{platform.system()} {platform.release()}",
        "processor": platform.processor(),
        "python": platform.python_version(),
        "mujoco": mujoco.__version__,
        "yourdfpy": yourdfpy.__version__,
        "note": "数字仅在本机同口径内可比；跨机对比无意义",
    }
    n_warn = sum(1 for r in results if "WARN" in str(r.get("value", "")))
    summary = {"model": config["model"], "date": time.strftime("%Y-%m-%d %H:%M"),
               "scenario": s6["scenario"], "results": results, "machine": machine,
               "headline": f"MuJoCo 步进 {med_rate:,.0f} steps/s（{statistics.median(us_per):.1f} µs/step），"
                           f"加载 {med_load:.1f} ms；URDF 解析 {med_parse:.1f} ms"}
    REPORTS.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(f"| `{r['check']}` | {r['detail']} |" for r in results)
    md = (f"# S6 基准报告 — {config['model']}（{summary['date']}）\n\n"
          f"**场景**：{s6['scenario']}。**基准对象**：models/ 入库件。\n\n"
          f"## 基准矩阵\n\n| 指标 | 数值 |\n|---|---|\n{rows}\n\n"
          f"## 机器与版本\n\n" + " · ".join(f"{k}: {v}" for k, v in machine.items()) + "\n\n"
          f"**一句话结论**：{summary['headline']}\n")
    (REPORTS / "S6-benchmark.md").write_text(md, encoding="utf-8")
    (REPORTS / "S6-benchmark.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n一句话结论：{summary['headline']}")
    sys.exit(1 if n_warn else 0)


if __name__ == "__main__":
    main()
