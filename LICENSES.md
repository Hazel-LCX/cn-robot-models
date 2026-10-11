# LICENSES — 全库 License 索引

> 双层结构（R1 四问已批）：**本库 MIT** + 逐模型上游声明随行——models/ 内上游文件属再分发，义务随文件走。

## 本库

| 项 | 值 |
|---|---|
| License | MIT（LICENSE 已落位，含第三方声明：上游 BSD-3 随模型、three.js MIT 随 libs/） |
| 商标声明 | Unitree / Go2 / G1 为宇树科技商标、Deep Robotics / 绝影 / Lite3 为云深处科技商标；本项目非官方、无关联、无背书（S7 必写，B3） |

## 逐模型上游

| 模型 | 上游仓库 | License | 版权方 | 快照位置 | commit 锚点 | 核对日期 |
|---|---|---|---|---|---|---|
| unitree_go2 | unitreerobotics/unitree_ros（URDF 源） | BSD-3-Clause | HangZhou YuShu Technology CO.,LTD. ("Unitree Robotics") © 2016–2022 | models/unitree_go2/LICENSE-upstream-unitree_ros.txt | `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 2026-10-11 |
| unitree_go2 | unitreerobotics/unitree_mujoco（MJCF 源） | BSD-3-Clause | 同上 © 2016–2024 | models/unitree_go2/LICENSE-upstream-unitree_mujoco.txt | `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` | 2026-10-11 |
| unitree_g1 | unitreerobotics/unitree_ros（URDF 源） | BSD-3-Clause | HangZhou YuShu Technology CO.,LTD. ("Unitree Robotics") © 2016–2022 | models/unitree_g1/LICENSE-upstream-unitree_ros.txt | `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 2026-10-11 |
| unitree_g1 | unitreerobotics/unitree_mujoco（MJCF 源） | BSD-3-Clause | 同上 © 2016–2024 | models/unitree_g1/LICENSE-upstream-unitree_mujoco.txt | `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` | 2026-10-11 |
| deeprobotics_lite3 | DeepRoboticsLab/deep_robotics_model（单仓双格式） | BSD-3-Clause | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | models/deeprobotics_lite3/LICENSE-upstream-deep_robotics_model.txt | `75824b516ecc8fa3f8f7ce5d6577e1e86d6b614f` | 2026-10-11 |

详细核对过程与三条结论见各模型 SOURCE.md（go2：已确认 R3；g1：已确认 R10，M1 选型 + S0 同件审）。

> G1 与 Go2 同上游两仓库、同锚点（head 零漂移，check_anchors.py 三源裁决在案）——license 快照逐字节相同（`84aac59f…`/`a5d73fc4…`，K2 后均为 blob 正本）。
> Lite3 为异厂首录（单仓双格式新形态）：官网**支持页**含 GitHub 直链（A4 双路径全中，R14 复核升级——首页欠采样的教训在案）；版权方按快照逐字引用。
