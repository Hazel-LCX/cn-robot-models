# SOURCE — booster_k1 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-24）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-24 · 取证方式 = GitHub API 活源 + 官网 K1 产品页结构化提取；M7 选型背景见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓多机型，booster_assets 第二机型线）

| 项 | BoosterRobotics/booster_assets（加速进化机器人描述资产仓） |
|---|---|
| 仓库 | https://github.com/BoosterRobotics/booster_assets |
| 拉取锚点（2026-10-24 实测 head） | `main` @ `12a97516f57469078707afb587a5f84c1cb110d1`（**与 M4 T1 同 HEAD 零漂移**——M4 S1 后上游未动；树 494 件 truncated=False） |
| 目标子目录 | `robots/K1/`（58 目录项：2 urdf + 2 xml + 52 mesh） |
| 配对选定（待审） | `K1_22dof.urdf`（26 link / 22 revolute + 2 fixed + 1 floating，32 引 `meshes/` 前缀 → 24 唯一，scale 0）↔ `K1_22dof.xml`（meshdir=meshes/，24 file 引用=24 唯一） |
| 网格 | `robots/K1/meshes/` 52 件（两侧引用闭包关系 S1 实测） |
| 引用协议 | URDF `meshes/` 前缀（T1 同款已验风格）；MJCF meshdir 相对（S1 实测细化） |
| 不入库（记录口径，S1 实测细化） | `K1_locomotion.urdf`（行走裁剪变体：23 link/12R+10F，T1_locomotion 同类处置）、`K1_22dof_parallel.xml`（并联踝变体 MJCF，R22 已裁先例同款）、`robots/T1/`（已收录）`robots/T2/` 整线（M7+ 候选）、`motions/` `src/` 仓级件 |

**机型背景（待审）**：K1 = 加速进化 **教育/开发平台级人形**（官网定位"探索教育、展演、机器人足球及真实场景应用"），站立身高**约 95 cm**、整机重量**约 19.5 kg**、全身自由度 **22 = 头部 2 + 双臂 8 + 双腿 12**——**官网产品页 DoF 分解与 assets README 配置表逐位一致**（双官方文档交叉背书，DR02 之后的第二强选型证据）；本库最小型机型（0.95 m 级，与 DR02 1.79 m 构成尺度带两极）。

## 2. 官方性验证（A4——**M4"路径①阴性"结论被推翻，升级为双路径全中**）

- **路径①转正（本 S0 核心侦察成果）**：M4 侦察时官网首页无 K1 内容（"官网现主打 T2，无 T1 独立产品页"）——本次复测**官网首页 meta 描述明列 "Booster K1、T2 人形机器人"且存在 K1 产品链接 `/cn/booster-k1`**（M4 首页快照与当前页内容不同——官网改版或 M4 快照采样偏差，如实记录）。K1 产品页（336,389 B 二进制原件落 evidence，R29 取证范式：本次扫描零 token 无需脱敏）含完整规格表（身高/重量/DoF 分解/应用场景）；
- **路径②成立（M4 四件互证沿用）**：账户 blog 自指官网 + assets README 官方自述与 DoF 配置表（`evidence/official-readme-booster_assets.txt`）+ gym README 官方署名与三官方仓互链 + 版权行公司主体 `Copyright (c) 2025, BoosterRobotics`；
- **A4 强度升级**：K1 成为本库**首个官网产品页直证机型**（DR02/M20 为云深处系产品页、X2/T1 无产品页——K1 页实存且双文档交叉）——详见 [SOURCE.md 对比注记]。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| BoosterRobotics/booster_assets（整仓单 license，M4 已定性） | **BSD-3-Clause**（M4/R22 两轮先例） | **Copyright (c) 2025, BoosterRobotics**（快照逐字，N1） | `LICENSE-upstream-booster_assets.txt`（1,502 B，blob `d7a14af35ecb…`，hash-object MATCH，**与 M4 T1 快照逐字节同物**——同仓第二机型线零漂移断言过） |

**定性论证**：与 M4 完全同源（同仓同 license），**无新定性考题**——S0 license 门作业 = 零漂移断言 + 快照随件分发；LICENSES.md 复指口径同 M5/M6 行式样（S7 落笔）。

## 4. 选型对比备案（M7 候选线）

- **K1（本件）**：同仓第二机型线，官方双文档 DoF 交叉背书 + 官网产品页实存（A4 升级）+ 小尺寸档（0.95 m/19.5 kg 与 DR02 1.79 m/78 kg 构成尺度带两极，S3/S6 序列新数据点）；S3 双基准可得（质量+DoF）；
- 同仓 T2 线（31DoF+四手部变体，官网主打）：变体矩阵大（JZgripper/Revo2Hand/WujiHand/YSgripper），M7+ 跨变体选型专项；
- 同仓 Standard（DR02 平替）/X30/M20_Piper 等维持档案；"跨仓配对"预设已废（M4 源修正），booster 全系单仓。

## 5. 快照与锚点

- license 快照：blob `d7a14af35ecb…` → `git hash-object --no-filters` MATCH + 与 M4 同物断言双过（L8 立规执行）。
- pin：`12a97516f57469078707afb587a5f84c1cb110d1`（与 M4 同 HEAD，S1 时对账）；树快照 `workspace/m7_recon/booster_assets_tree_v2.json`（侦察件，不入库）。
- 上游漂移监控：仓库不活跃（pushed 2026-09-26 至今无新 push），漂移风险低；S1 对账 head。
