# SOURCE — deeprobotics_x30 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-24）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-24 · 取证方式 = GitHub API 活源 + 解析器口径结构侦察（R29/R34 规程）+ 官网 X30 产品页复核；M10 选型背景见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓多机型，同仓第五机型——scale 实战线）

| 项 | DeepRoboticsLab/deep_robotics_model（云深处模型仓，八机型） |
|---|---|
| 仓库 | https://github.com/DeepRoboticsLab/deep_robotics_model |
| 拉取锚点（2026-10-24 实测 head） | `main` @ `530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（**与 M5/M6/M9 同 HEAD 零漂移**；树 422 件 truncated=False） |
| 目标子目录 | `X30/`（21 目录项：1 urdf + 1 xml + 8 mesh + usd 5 件——本库最小资产池） |
| 配对选定（待审） | `X30/urdf/X30.urdf`（21 link / **12 revolute + 8 fixed**，13 引 `./meshes/` 前缀 → **4 唯一**网格，**scale 5 处**）↔ `X30/mjcf/X30.xml`（8 引→4 唯一，**MJCF scale 4 处**——跨格式 scale 对账首例素材） |
| 网格 | `X30/meshes/` 8 件（torso/hip/thigh 等基础件复用——**极简池 L12 实战线**） |
| 引用协议 | URDF `./meshes/` 显式前缀（Lite3/M20/DR02/M20_Piper 同款第四形态）；MJCF `meshdir="./meshes/"` 相对（S1 实测细化） |
| **scale 逐处定位（解析器口径，本件核心侦察资产）** | URDF 5 处全为**镜像技巧**（共用网格翻转，Lite3 R19 案例同族）：FR_HIP/FR_THIGH（`1 -1 1`）、HL_HIP（`-1 1 1`）、HR_HIP（`-1 -1 1`）、HR_THIGH（`1 -1 1`）——四腿 hip/thigh 两两共用 hip.STL/thigh.STL 翻转；**MJCF 侧另有 4 处 scale**（跨格式 scale 对账首例素材，S1 逐处定位） |
| 不入库（记录口径，S1 实测细化） | `usd/` 5 件（M20/M9 先例）、其余机型目录/根级仓级件 |

**机型背景（待审）**：X30 = 云深处**工业级四足**（绝影系列旗舰，官网"绝影X30"），整机重量（含电池）**约 56 kg**（官网产品页 M9 落档复核）、持续负载 20 kg——**本库最大质量四足**（vs Go2 8.2/Lite3 12 档），S3 质量基准可得。**选型核心叙事=scale 实战线**：镜像技巧 5 处（URDF）+4 处（MJCF）为管道 scale 应用能力（R18 修复后 preview.js）的第一次成规模实战检验，且薄池（4 唯一网格）极简闭包。

## 2. 官方性验证（A4——同仓链条第五机型继承）

- **M2/M5/M6/M9 同仓同 org**：双路径先例四轮在案——**第五机型直接沿用，无新增阴性项**；
- 官网 X30 产品页（detail/6.html，141,310 B 二进制原件落 evidence，R29 范式**脱敏 1 处 token**）；README 八机型表含 X30 行；
- S3 前置侦察：官网 X30 规格表（整机重量约 56 kg/持续负载 20 kg/防护等级等）在档可提取——质量基准可得（非 T1/Piper 式缺失）。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| DeepRoboticsLab/deep_robotics_model（整仓单 license，M2 已定性） | **BSD-3-Clause**（M2/R14/R22/R25/R28/R37 六轮先例） | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，blob `cdc6c065…`，hash-object MATCH，**与 M2/M5/M6/M9 快照逐字节同物**——同仓第五机型零漂移断言过） |

**定性论证**：与 M2/M5/M6/M9 完全同源（同仓同 license），**无新定性考题**——S0 license 门作业 = 零漂移断言 + 快照随件分发；LICENSES.md 复指口径同前行式样（S7 落笔）。

## 4. 选型对比备案（M10 候选线）

- **X30（本件）**：scale 实战线（5+4 处跨格式）+ 官网 56 kg 基准（四足大机型档）+ 薄池极简闭包（4 网格）——质检叙事与管道实战双价值；
- 同仓 DR02 Standard（21R/68kg 平替）/M20S/S10（同构轮足变体）维持"加 config 即加模型"档案；
- booster T2 四手部变体双锚题/其余跨仓候选维持 M10+ 专项档案。

## 5. 快照与锚点

- license 快照：blob `cdc6c065…` → `git hash-object --no-filters` MATCH + 与 M2/M5/M6/M9 同物断言双过（L8 立规执行）。
- pin：`530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（与 M5/M6/M9 同 HEAD，S1 时对账）；树快照 `workspace/m10_recon/deep_robotics_model_tree_v4.json`（侦察件，不入库）。
- 上游漂移监控：活跃仓（pushed 2026-10-23），S1 对账 head；pin 机制免疫后续上游变动。
