# S6 基准报告 — unitree_g1（2026-10-11 18:44）

**场景**：固定 qpos0、纯重力、无控制器（人形初始姿态站立，测引擎步进吞吐，不掺控制变量）。**基准对象**：models/ 入库件。

## 基准矩阵

| 指标 | 数值 |
|---|---|
| `mjcf:load-time` | 102.84 ms（5 次中位数；min 102.28 / max 173.03） |
| `mjcf:step-rate` | 50,809 steps/s（10,000 步 × 5 次、预热 100 丢弃；µs/step 中位 19.7；场景：固定 qpos0、纯重力、无控制器（人形初始姿态站立，测引擎步进吞吐，不掺控制变量）） |
| `mjcf:stability` | steps/s 展幅 1,166（2.3%，验收 <20%） |
| `urdf:parse-time` | 4.74 ms（5 次中位数）——URDF 无物理引擎，只测加载，如实标注 |

## 机器与版本

platform: Windows 11 · processor: Intel64 Family 6 Model 197 Stepping 2, GenuineIntel · python: 3.14.6 · mujoco: 3.15.0 · yourdfpy: 0.0.60 · note: 数字仅在本机同口径内可比；跨机对比无意义

**一句话结论**：MuJoCo 步进 50,809 steps/s（19.7 µs/step），加载 102.8 ms；URDF 解析 4.7 ms
