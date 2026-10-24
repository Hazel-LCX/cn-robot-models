# LICENSES — 全库 License 索引

> 双层结构（R1 四问已批）：**本库 MIT** + 逐模型上游声明随行——models/ 内上游文件属再分发，义务随文件走。

## 本库

| 项 | 值 |
|---|---|
| License | MIT（LICENSE 已落位，含第三方声明：上游 BSD-3/MulanPSL-2.0 随模型、three.js MIT 随 libs/） |
| 商标声明 | Unitree / Go2 / G1 为宇树科技商标、Deep Robotics / 绝影 / Lite3 为云深处科技商标、AgiBot / 灵犀 X2 为智元机器人商标、Booster / T1 为加速进化（Booster Robotics）商标；本项目非官方、无关联、无背书（S7 必写，B3） |

## 逐模型上游

| 模型 | 上游仓库 | License | 版权方 | 快照位置 | commit 锚点 | 核对日期 |
|---|---|---|---|---|---|---|
| unitree_go2 | unitreerobotics/unitree_ros（URDF 源） | BSD-3-Clause | HangZhou YuShu Technology CO.,LTD. ("Unitree Robotics") © 2016–2022 | models/unitree_go2/LICENSE-upstream-unitree_ros.txt | `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 2026-10-11 |
| unitree_go2 | unitreerobotics/unitree_mujoco（MJCF 源） | BSD-3-Clause | 同上 © 2016–2024 | models/unitree_go2/LICENSE-upstream-unitree_mujoco.txt | `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` | 2026-10-11 |
| unitree_g1 | unitreerobotics/unitree_ros（URDF 源） | BSD-3-Clause | HangZhou YuShu Technology CO.,LTD. ("Unitree Robotics") © 2016–2022 | models/unitree_g1/LICENSE-upstream-unitree_ros.txt | `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 2026-10-11 |
| unitree_g1 | unitreerobotics/unitree_mujoco（MJCF 源） | BSD-3-Clause | 同上 © 2016–2024 | models/unitree_g1/LICENSE-upstream-unitree_mujoco.txt | `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` | 2026-10-11 |
| deeprobotics_lite3 | DeepRoboticsLab/deep_robotics_model（单仓双格式） | BSD-3-Clause | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | models/deeprobotics_lite3/LICENSE-upstream-deep_robotics_model.txt | `75824b516ecc8fa3f8f7ce5d6577e1e86d6b614f` | 2026-10-11 |
| agibot_x2 | AgibotTech/agibot_x2_urdf（单仓双格式） | **MulanPSL-2.0**（R17 人工定性=可收录：blob `adf05533` + SPDX 名录 `isOsiApproved=true` + 义务清单三件套——GitHub NOASSERTION=检测器盲区） | 智元机器人（AgibotTech org 官方主体）——**上游 LICENSE 为许可模板、未含逐字版权主体行，如实注记不虚构（R17 检查点）**；官方声明=「本项目采用木兰宽松许可证，第2版（Mulan PSL v2）开源」（evidence/official-readme-declaration.txt） | models/agibot_x2/LICENSE-upstream-agibot_x2_urdf.txt | `575cc6b988f976c23550e0db85aa1e5475d3652d` | 2026-10-11 |
| booster_t1 | BoosterRobotics/booster_assets（单仓双格式） | BSD-3-Clause（GitHub 端点直接识别；R22 活源全验——全文 1,502 B 通读三条款完整+活源 blob 同物+全树仅根级 LICENSE） | **Copyright (c) 2025, BoosterRobotics**（快照逐字，N1） | models/booster_t1/LICENSE-upstream-booster_assets.txt | `12a97516f57469078707afb587a5f84c1cb110d1` | 2026-10-24 |
| deeprobotics_m20 | DeepRoboticsLab/deep_robotics_model（单仓多机型，Lite3 同仓） | BSD-3-Clause（**与 Lite3 行同仓同快照逐字节同物 `cdc6c065`**，R25 三重同物全验——同仓单 license 复指口径，无新增 license 行语义） | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | models/deeprobotics_m20/LICENSE-upstream-deep_robotics_model.txt | `530e01a5d2ceb6007f8790f1a7e11ee7389fb981` | 2026-10-24 |
| deeprobotics_dr02 | DeepRoboticsLab/deep_robotics_model（单仓多机型，Lite3/M20 同仓） | BSD-3-Clause（**与 Lite3/M20 行同仓同快照逐字节同物 `cdc6c065`**，R28 三重同物全验——复指口径同上） | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | models/deeprobotics_dr02/LICENSE-upstream-deep_robotics_model.txt | `530e01a5d2ceb6007f8790f1a7e11ee7389fb981` | 2026-10-24 |
| booster_k1 | BoosterRobotics/booster_assets（单仓多机型，T1 同仓） | BSD-3-Clause（**与 T1 行同仓同快照逐字节同物 `d7a14af35ecb`**，R31 双重同物全验——复指口径同上） | **Copyright (c) 2025, BoosterRobotics**（快照逐字，N1） | models/booster_k1/LICENSE-upstream-booster_assets.txt | `12a97516f57469078707afb587a5f84c1cb110d1` | 2026-10-24 |
| booster_t2 | BoosterRobotics/booster_assets（单仓多机型，T1/K1 同仓） | BSD-3-Clause（**与 T1/K1 行同仓同快照逐字节同物 `d7a14af35ecb`**，R34 三重同物全验——复指口径同上） | **Copyright (c) 2025, BoosterRobotics**（快照逐字，N1） | models/booster_t2/LICENSE-upstream-booster_assets.txt | `12a97516f57469078707afb587a5f84c1cb110d1` | 2026-10-24 |

详细核对过程与三条结论见各模型 SOURCE.md（go2：已确认 R3；g1：已确认 R10，M1 选型 + S0 同件审）。

> G1 与 Go2 同上游两仓库、同锚点（head 零漂移，check_anchors.py 三源裁决在案）——license 快照逐字节相同（`84aac59f…`/`a5d73fc4…`，K2 后均为 blob 正本）。
> Lite3 为异厂首录（单仓双格式新形态）：官网**支持页**含 GitHub 直链（A4 双路径全中，R14 复核升级——首页欠采样的教训在案）；版权方按快照逐字引用。
> agibot_x2 为**国产开源许可证首例**：MulanPSL-2.0 义务 = 分发向接收者提供许可证副本 + 保留版权/商标/专利及免责声明（§4）、无商标许可（§3）、中英同效中文优先（§6）——快照随文件入库即义务履行；双 license 并存后本表逐模型行口径保持一致（BSD-3 逐字版权行 ∥ MulanPSL 模板无版权行如实注记）。
> booster_t1 为**第四厂商首录**（专用资产仓正本 + 训练仓旁证生态位，M3 时代"跨仓配对"预设经侦察修正）：同账户 gym 仓 Apache-2.0 短格式声明（NOASSERTION=方括号版权行盲区，M3 已识真身）降为生态旁证不作本仓门槛；BSD-3 与 M0/M2 同族三锚先例，快照随文件入库即义务履行。
