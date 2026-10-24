# S6 基准报告 — booster_t2（2026-10-24 22:38）

**场景**：固定 qpos0、纯重力、无控制器（人形站立初始姿态，测引擎步进吞吐，不掺控制变量）；**展幅验收执行 R32 处置先例：首轮超线则三轮复跑+负载源核查+取干净轮（K1 先例）**。**基准对象**：models/ 入库件。

## 基准矩阵

| 指标 | 数值 |
|---|---|
| `mjcf:load-time` | 229.03 ms（5 次中位数；min 224.67 / max 301.22） |
| `mjcf:step-rate` | 27,583 steps/s（10,000 步 × 5 次、预热 100 丢弃；µs/step 中位 36.3；场景：固定 qpos0、纯重力、无控制器（人形站立初始姿态，测引擎步进吞吐，不掺控制变量）；**展幅验收执行 R32 处置先例：首轮超线则三轮复跑+负载源核查+取干净轮（K1 先例）**） |
| `mjcf:stability` | steps/s 展幅 2,808（10.2%，验收 <20%） |
| `urdf:parse-time` | 4.62 ms（5 次中位数）——URDF 无物理引擎，只测加载，如实标注 |

## 机器与版本

platform: Windows 11 · processor: Intel64 Family 6 Model 197 Stepping 2, GenuineIntel · python: 3.14.6 · mujoco: 3.15.0 · yourdfpy: 0.0.60 · note: 数字仅在本机同口径内可比；跨机对比无意义

**一句话结论**：MuJoCo 步进 27,583 steps/s（36.3 µs/step），加载 229.0 ms；URDF 解析 4.6 ms
