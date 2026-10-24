# SOURCE — deeprobotics_dr02 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-24）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-24 · 取证方式 = GitHub API 活源 + 官网规格页结构化提取 + 双配置程序化对比；M6 选型背景见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓多机型，同仓第三机型）

| 项 | DeepRoboticsLab/deep_robotics_model（云深处模型仓，八机型） |
|---|---|
| 仓库 | https://github.com/DeepRoboticsLab/deep_robotics_model |
| 拉取锚点（2026-10-24 实测 head） | `main` @ `530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（与 M5 同 HEAD——M5 S1 后上游未动；树 422 件 truncated=False） |
| 目标子目录 | `DR02/`（144 目录项：3 urdf + 2 xml + 114 物理 mesh 分 pro/standard 两侧 + usd 等仓级件，S1 实测细化） |
| 配对选定（待审） | **Pro 配置**：`DR02/urdf/pro/DR02-pro.urdf`（40 link / 31 revolute + 8 fixed，39 引→34 唯一，scale 0）↔ `DR02/mjcf/pro/DR02_pro.xml`（model=DR02_pro，meshdir=meshes/，31 关节——双侧自洽） |
| 网格 | `DR02/mjcf/pro/meshes/` 等分目录池（114 物理件跨两配置，闭包关系 S1 实测） |
| 引用协议 | URDF `./meshes/` 显式前缀（Lite3/M20 同款已验风格）；MJCF `meshdir` 相对引用（S1 实测细化） |
| 不入库（记录口径，S1 实测细化） | `DR02/urdf/pro/DR02-pro_fix_joints.urdf`（锁死变体：同 40 link 但 10 关节固化为 fixed，21R+18F——T1_locomotion/M2 usd 同类处置）、`DR02/urdf/standard/DR02-std.urdf` + `DR02/mjcf/standard/DR02_std.xml`（Standard 配对整组——审核台裁定不入库则随组记录）、两配置各自 usd/ 件（如有，M20/M2 先例）、根级仓级件 |

**机型背景（待审）**：DR02 = 云深处**人形机器人**（官网"全球首款行业级全天候人形机器人"，detail/5.html），站立尺寸约 1800×558×400 mm（**1.8 m 级**，本库最高模型）。**官网规格页逐部位 DoF 分解与仓库两配置逐位对上**（强于 T1 README 表背书的选型证据）：
- **Pro（31 DoF）**：单臂 7×2 + 单腿 6×2 + 腰 3 + **头 2** = 31 ✓ ↔ DR02-pro.urdf 31R ↔ DR02_pro.xml 31 关节；整机重量（含电池）**约 78 kg**；
- **Standard（21 DoF）**：单臂 4×2 + 单腿 6×2 + 腰 1 = 21 ✓ ↔ DR02-std.urdf 21R ↔ DR02_std.xml 21 关节；**约 68 kg**。
本库锚定 **Pro**（完整自由度上位配置，X2-Ultra 旗舰先例同款）；Standard 为平替（管道成本相同）。

## 2. 官方性验证（A4——同仓链条第三机型继承）

- **M2/M5 同仓同 org**：DeepRoboticsLab 官方性与 A4 双路径（官网支持页直链 + org 互证）M2 全中（R14）、M5 继承（R25）——**第三机型直接沿用，无新增阴性项**；
- 官网 DR02 产品页（detail/5.html，静态 HTML 可提取，原件 `evidence/official-dr02-spec-page.html` 150,548 B）：产品叙事 + 双版本参数表（整机/运动/环境/接口/技术五区）+ **逐部位 DoF 分解**（选型算术证据）；
- S3 前置侦察基本完成：官网 Pro 口径 **78 kg（含电池）**已在案（S3 回填 config 时逐字核对原件），自由度分项官方明示（质量/DoF 对账双基准可得——M4 T1 缺失能力在云深处系全线恢复）。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| DeepRoboticsLab/deep_robotics_model（整仓单 license，M2 已定性） | **BSD-3-Clause**（M2/R14/R22/R25 四轮先例） | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，blob `cdc6c065…`，hash-object MATCH，**与 M2/M5 快照逐字节同物**——同仓第三机型零漂移断言过） |

**定性论证**：与 M2/M5 完全同源（同仓同 license），**无新定性考题**——S0 license 门作业 = 零漂移断言 + 快照随件分发；LICENSES.md 复指口径同 M5 行式样（S7 落笔）。

## 4. 选型对比备案（M6 候选线）

- **DR02（本件）**：本库**第 4 个人形机型**（G1/X2/T1 之后）与**云深处首个人形**，1.8 m 级为库内最高；官方逐部位 DoF 分解证据为历次选型最强；S3 双基准（质量 78 kg+DoF 分项）可得；
- 同仓其余（M20S/S10 轮足变体、M20_Piper 复合体、X30 薄网格+scale 预警）维持 M6+ 档案；
- booster K1/T2 线（booster_assets 仓）：K1 22dof 有官方 README 表，T2 为官网主打（31dof+四手部变体）——跨厂商 M7+ 候选。

## 5. 快照与锚点

- license 快照：blob `cdc6c065…` → `git hash-object --no-filters` MATCH + 与 M2/M5 同物断言双过（L8 立规执行）。
- pin：`530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（与 M5 同 HEAD，活跃仓 S1 时对账）；树快照 `workspace/m6_recon/`（侦察件，不入库）。
- 上游漂移监控：活跃仓（pushed 2026-10-23），S1 对账 head；pin 机制免疫后续上游变动。
