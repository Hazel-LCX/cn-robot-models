# S6 基准报告 — deeprobotics_lite3（2026-10-11 19:59）

**场景**：固定 qpos0、纯重力、无控制器（四足站立初始姿态，测引擎步进吞吐，不掺控制变量）。**基准对象**：models/ 入库件。

## 基准矩阵

| 指标 | 数值 |
|---|---|
| `mjcf:load-time` | 59.23 ms（5 次中位数；min 58.91 / max 84.87） |
| `mjcf:step-rate` | 47,966 steps/s（10,000 步 × 5 次、预热 100 丢弃；µs/step 中位 20.8；场景：固定 qpos0、纯重力、无控制器（四足站立初始姿态，测引擎步进吞吐，不掺控制变量）） |
| `mjcf:stability` | steps/s 展幅 2,355（4.9%，验收 <20%） |
| `urdf:parse-time` | 1.92 ms（5 次中位数）——URDF 无物理引擎，只测加载，如实标注 |

## 机器与版本

platform: Windows 11 · processor: Intel64 Family 6 Model 197 Stepping 2, GenuineIntel · python: 3.14.6 · mujoco: 3.15.0 · yourdfpy: 0.0.60 · note: 数字仅在本机同口径内可比；跨机对比无意义

**一句话结论**：MuJoCo 步进 47,966 steps/s（20.8 µs/step），加载 59.2 ms；URDF 解析 1.9 ms

## 跨模型对照注记（工作台补记）

Lite3（12 revolute / nbody 18）与 Go2（12 revolute / nbody 18）拓扑同规模，步速却差 2.2 倍（47,966 vs 105,131 steps/s）——引擎单步负载由 **geom 类型与网格复杂度**主导（Lite3 MJCF 含 mesh geom 与高顶点数 STL，Go2 以简单几何为主），**同 DOF 也不可比**——"跨模型数字不可比"的再实证；三模型仅在本机同口径内各自自洽。
