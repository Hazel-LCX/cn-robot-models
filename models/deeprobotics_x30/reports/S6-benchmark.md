# S6 基准报告 — deeprobotics_x30（2026-10-25 18:50）

**场景**：固定 qpos0、纯重力、无控制器（四足站立初始姿态，测引擎步进吞吐，不掺控制变量）；展幅验收执行 R32 处置先例。**基准对象**：models/ 入库件。

## 基准矩阵

| 指标 | 数值 |
|---|---|
| `mjcf:load-time` | 57.23 ms（5 次中位数；min 54.21 / max 67.38） |
| `mjcf:step-rate` | 79,053 steps/s（10,000 步 × 5 次、预热 100 丢弃；µs/step 中位 12.6；场景：固定 qpos0、纯重力、无控制器（四足站立初始姿态，测引擎步进吞吐，不掺控制变量）；展幅验收执行 R32 处置先例） |
| `mjcf:stability` | steps/s 展幅 45,809（57.9%，验收 <20%） |
| `urdf:parse-time` | 2.14 ms（5 次中位数）——URDF 无物理引擎，只测加载，如实标注 |

## 机器与版本

platform: Windows 11 · processor: Intel64 Family 6 Model 197 Stepping 2, GenuineIntel · python: 3.14.6 · mujoco: 3.15.0 · yourdfpy: 0.0.60 · note: 数字仅在本机同口径内可比；跨机对比无意义

**一句话结论**：MuJoCo 步进 79,053 steps/s（12.6 µs/step），加载 57.2 ms；URDF 解析 2.1 ms
