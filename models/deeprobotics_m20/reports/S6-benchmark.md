# S6 基准报告 — deeprobotics_m20（2026-10-24 16:50）

**场景**：固定 qpos0、纯重力、无控制器（轮足站立初始姿态，测引擎步进吞吐，不掺控制变量——continuous 关节 qpos0 语义 S6 前实测校准）。**基准对象**：models/ 入库件。

## 基准矩阵

| 指标 | 数值 |
|---|---|
| `mjcf:load-time` | 62.34 ms（5 次中位数；min 57.51 / max 75.60） |
| `mjcf:step-rate` | 43,867 steps/s（10,000 步 × 5 次、预热 100 丢弃；µs/step 中位 22.8；场景：固定 qpos0、纯重力、无控制器（轮足站立初始姿态，测引擎步进吞吐，不掺控制变量——continuous 关节 qpos0 语义 S6 前实测校准）） |
| `mjcf:stability` | steps/s 展幅 5,249（12.0%，验收 <20%） |
| `urdf:parse-time` | 2.37 ms（5 次中位数）——URDF 无物理引擎，只测加载，如实标注 |

## 机器与版本

platform: Windows 11 · processor: Intel64 Family 6 Model 197 Stepping 2, GenuineIntel · python: 3.14.6 · mujoco: 3.15.0 · yourdfpy: 0.0.60 · note: 数字仅在本机同口径内可比；跨机对比无意义

**一句话结论**：MuJoCo 步进 43,867 steps/s（22.8 µs/step），加载 62.3 ms；URDF 解析 2.4 ms
