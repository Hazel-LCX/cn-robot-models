# SOURCE — booster_t1 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-24）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-24 · 取证方式 = GitHub API + 官网双页实测 + SPDX 官方名录程序化核验；M4 选型背景与两候选线对比见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓双格式，M1 G1 同款形态）

| 项 | BoosterRobotics/booster_assets（加速进化机器人描述资产仓） |
|---|---|
| 仓库 | https://github.com/BoosterRobotics/booster_assets |
| 拉取锚点（2026-10-24 实测 head） | `main` @ `12a97516f57469078707afb587a5f84c1cb110d1`（2026-09-26 push，45.4 MB，494 树件 truncated=False） |
| 目标子目录 | `robots/T1/`（URDF+MJCF 同目录直配，Lite3/G1 同款形态） |
| 配对选定（待审） | `T1_23dof.urdf` + `T1_23dof.xml`（官方 README 配置表列名的 23 自由度标准版） |
| 网格 | `robots/T1/meshes/` 63 件（Mesh 两侧引用闭包关系 S1 实测） |
| 引用协议 | S1 实测（侦察仅确认文件在位；`T1_23dof.xml` 与 urdf 同目录配对关系由官方 README 配置表背书） |
| 不入库（记录口径，S1 实测细化） | `T1_29dof.urdf`（29 自由度变体，**无 xml 配对**——树扫描实测 T1 线 xml 仅 23dof/23dof_parallel/locomotion 三件）、`T1_locomotion.urdf`+`T1_locomotion.xml`（头/臂/腰固化的行走裁剪变体）、`T1_23dof_parallel.xml`（并联变体，**R22 已裁不入库**——用途特化副本，X2 simple_collision 先例同款）、`robots/K1/` `robots/T2/` 整线（M4+ 候选）、`motions/` `src/` `pyproject.toml` `setup.cfg`（仓级非模型件） |

**机型背景（待审）**：T1 = 加速进化（Booster Robotics）双足人形，官方 README 配置表自述 23 DoF = head 2 + arms 4×2 + waist 1 + legs 6×2（**算术自洽 2+8+1+12=23**，锚点选择有官方文档背书，强于 M3 的推断式选型）。同仓 K1（22 DoF）与 T2（31 DoF + 四种手部/夹爪变体）整线留 M4+ 候选；本库四机型序列将获**第四厂商**（宇树/云深处/智元之后），且首次引入"专用资产仓为正本源"的 Booster 生态位（gym 训练仓降为旁证）。

## 2. 官方性验证（A4 证据链——强度分层如实呈现）

- **路径②成立（多件互证）**：①账户官方字段自指官方域——`users/BoosterRobotics` API 原件 blog=`https://www.boosterobotics.com/`（`evidence/github-users-BoosterRobotics.json`；**账户类型=User 非 org**，与 M1 L11 发现同款事实，本仓沿用）；②正本仓 README 官方自述+机型配置表（`evidence/official-readme-booster_assets.txt`，含 Booster 官方机器人描述定位与逐机型 DoF 表）；③生态仓互链——gym 仓 README 官方署名"developed by [Booster Robotics](https://boosterobotics.com/)"并列 Booster Train/Deploy/Assets 三官方仓互链（`workspace/m4_recon/archive_gym_s0/evidence/official-readme-booster_gym.txt` 侦察件）；④license 版权行公司主体 `Copyright (c) 2025, BoosterRobotics`（快照原文）。
- **路径①阴性（如实记录）**：官网→GitHub 直链未命中——静态双页实测：首页 227,886 B 零 github 链接零 "T1" 字样、T2 产品页 `/cn/booster-t2` 263,184 B 同样双零（JS 渲染站，侦察件 `workspace/m4_recon/boosterobotics-home.html` / `booster-t2-page.html`）。**官网产品线现主打 T2，无 T1 独立产品页**——强度低于 M2 双路径全中，与 M1/M3 分层口径相当。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| BoosterRobotics/booster_assets（整仓单 license，robots/ 子目录无独立 LICENSE——树扫描 494 件仅根级 LICENSE 一件） | **BSD-3-Clause**（GitHub 端点直接识别，全文在仓） | BoosterRobotics（`Copyright (c) 2025, BoosterRobotics`，快照原文逐字） | `LICENSE-upstream-booster_assets.txt`（1,502 B，blob `d7a14af35ecb…`，hash-object 比对 MATCH） |

**定性论证**：
1. **BSD-3-Clause 与 M0（unitree_ros）/M2（deep_robotics_model）同族**，三锚先例充分（SPDX 命中 `evidence/spdx-BSD-3-Clause.json`：`isOsiApproved: True`、未弃用）；义务=保留版权行与免责声明，未修改分发官方件+模型页保留声明即满足。
2. **同账户 gym 仓 license 事实（侦察档案，非本仓门槛）**：`BoosterRobotics/booster_gym` 根 LICENSE 为 916 B 短格式声明（"Licensed under the Apache License, Version 2.0"+四项上游基础库清单，**非全文**），GitHub 端点 NOASSERTION 系方括号版权行 `[2024] [Booster Robotics Technology Co., Ltd]` 格式所致——M3 侦察已识别其真身（`workspace/m3_recon/booster_gym_LICENSE.txt`，blob `c9e19b34` 2026-10-24 复测零漂移）。**该仓仅作官方生态旁证，不作正本源**，其 license 考题随源修正消解。
3. **与本库兼容性**：本库 MIT 主体+第三方声明层不变，新增 booster_assets（BSD-3）行即可；快照随件分发即履行声明保留义务。

## 4. 源修正记录（M3 时代预设 → 侦察实测修正，如实落档）

- M3 会话 19 送审件曾按"加速进化=跨仓配对（双仓双 license 三锚，S1/S4 结构扩展）"预设 M4 方向。**侦察修正**：①booster_train 仓 81 件全为训练代码零 T1 资产；②booster_gym 仓 `resources/T1/` 单仓即含 URDF↔MJCF 配对（M3 侦察已见）；③**专用描述仓 `booster_assets` 存在且形态最优**（BSD-3 全文、三机型线、官方配置表）——"跨仓结构扩展"预设不成立，M4 实际形态=**单仓单 license 直配**，管道预判零结构改动（与 M3 会话 19"管道预判零结构改动"口径一致）。
- gym 仓 S0 取证 v1（Apache-2.0 短格式定性件）已撤至 `workspace/m4_recon/archive_gym_s0/`（侦察件不入库）——源修正后 evidence 不混用两正本（L12 教训：互证前提=证据链触达同一 source of truth）。

## 5. 快照与锚点

- license 快照：blob `d7a14af35ecb…`（license 端点 `_links.git` 直取）→ 本地 `git hash-object --no-filters` 比对 MATCH（L8 立规执行）。
- pin：`12a97516f57469078707afb587a5f84c1cb110d1`（2026-10-24 实测，`evidence/github-head-booster_assets.json`）；树快照 `workspace/m4_recon/booster_assets_tree.json`（侦察件，不入库）。
- 上游漂移监控：S1 时对账 head；本仓最近 push 2026-09-26（repo meta pushed_at 实测），活跃但速率温和。
