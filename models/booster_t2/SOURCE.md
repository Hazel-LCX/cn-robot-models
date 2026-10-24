# SOURCE — booster_t2 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-24）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-24 · 取证方式 = GitHub API 活源 + 官网 T2 产品页（新域）结构化提取 + 五变体程序化对比；M8 选型背景见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓多机型，booster_assets 第三机型线——变体矩阵）

| 项 | BoosterRobotics/booster_assets（加速进化机器人描述资产仓） |
|---|---|
| 仓库 | https://github.com/BoosterRobotics/booster_assets |
| 拉取锚点（2026-10-24 实测 head） | `main` @ `12a97516f57469078707afb587a5f84c1cb110d1`（**与 M4/M7 同 HEAD 零漂移**；树 494 件 truncated=False） |
| 目标子目录 | `robots/T2/`（347 目录项：5 urdf + 6 xml + 325 mesh——本库最大变体矩阵） |
| 配对选定（待审） | **主版**：`T2_31dof/T2_31dof.urdf`（36 link / 31 revolute + 3 fixed + 1 floating，39 引 `meshes/` 前缀 → 37 唯一，scale 0）↔ `T2_31dof/T2_31dof.xml`（37 file 引用自洽，joint 标签 32=31+free） |
| 网格 | `T2_31dof/meshes/`（37 件引用池）+ 四变体各自 meshes/（325 物理件总量，分目录形态 M20 同款；闭包关系 S1 实测） |
| 引用协议 | URDF `meshes/` 前缀（T1 同款已验风格）；MJCF meshdir 相对（S1 实测细化） |
| 不入库（记录口径，S1 实测细化） | 四手部变体整组（`T2_31dof_JZgripper` 43R / `T2_31dof_Revo2Hand` 53R / `T2_31dof_WujiHand` 71R / `T2_31dof_YSgripper` 43R——各含 urdf+xml+meshes，末端执行器复合体）、`T2_31dof_parallel.xml`（踝并联变体，R22/M7 先例同款）、其余仓级件 |

**机型背景（待审）**：T2 = 加速进化**旗舰级人形**（官网现主打机型），站立身高**约 140 cm**、整机重量**约 42 kg\***（星号注记原文在页，S3 前置核对——疑为"不含电池/手部"类口径注记）、全身自由度 **31**（单腿 6…）、双臂最大负载 10 kg\*、最大峰值扭矩 **140 N·m**、**官网明示"末端执行器：默认/夹爪/灵巧手"为选项**——与仓内四手部变体矩阵对应。**主版 31R 与官网"全身 31"逐位对应**（变体=31+手部自由度的复合体：JZ/YS +12、Revo2 +22、Wuji +40），**X2-Ultra vs 手部变体先例同构处置**（M3：主版锚定+变体不入库只记录）。

## 2. 官方性验证（A4——同仓链条第三机型线继承 + K1 转正口径沿用）

- **M4/M7 同仓同 org**：DeepRobotics 式双路径先例在 booster 系已由 K1 转正（官网产品页直证）——T2 页同域同形态（`booster.tech/cn/booster-t2`，269,610 B 二进制原件落 evidence，R29 取证范式：本次零 token 无需脱敏）；账户/README/版权行互证四件沿用 M4（`evidence/official-readme-booster_assets.txt` 配置表 T2 行"31-DoF layout: head 2 joints, arms 4 joints ×2, waist 1 joint, legs 6 joints ×2"——**31=2+8+1+12 算术自洽**）；
- **官网 T2 页与 T1/K1 页同模板同规格表结构**（身高/重量/DoF/负载/扭矩五区）——三机型页互为形态佐证；官网 T2 页 DoF 行明列"全身：31/单腿：6…"与 README 配置表逐位一致；
- S3 前置侦察基本完成：官网双基准（42 kg+31 DoF）**+扭矩基准（140 N·m）三可得**——本库首个三基准机型（effort 上限 sanity 可对账，M3 X2 官网 120 N·m 先例同法）；42 kg 星号注记 S3 前置逐字核对原文。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| BoosterRobotics/booster_assets（整仓单 license，M4 已定性） | **BSD-3-Clause**（M4/R22/R31 三轮先例） | **Copyright (c) 2025, BoosterRobotics**（快照逐字，N1） | `LICENSE-upstream-booster_assets.txt`（1,502 B，blob `d7a14af35ecb…`，hash-object MATCH，**与 M4/M7 快照逐字节同物**——同仓第三机型线零漂移断言过） |

**定性论证**：与 M4/M7 完全同源（同仓同 license），**无新定性考题**——S0 license 门作业 = 零漂移断言 + 快照随件分发；LICENSES.md 复指口径同 M5/M6/M7 行式样（S7 落笔）。

## 4. 选型对比备案（M8 候选线）

- **T2 主版（本件）**：官网主打旗舰（140 cm/42 kg 档，介于 K1 0.95 m 与 DR02 1.79 m 之间）、**31R 与官网"全身 31"逐位**（首个人形主版 DoF 直证）、S3 三基准可得（质量+DoF+**扭矩 140 N·m**——effort 对账首个可全对账机型）；变体矩阵叙事（四手部=31+N 复合体）为"加 config 即加模型"的潜在后续填充；
- 变体矩阵若审核台倾向收录某手部版（如 Revo2Hand 灵巧手 53R），主版与变体可同里程碑双锚（管道成本=2×config，结构零改动）——**我方倾向仅收主版**（变体整组 X2 手部先例处置，保持每模型单一锚点纪律），待裁；
- 其余候选（DR02 Standard 平替/X30 薄网格+scale 预警/M20_Piper 复合体）维持档案。

## 5. 快照与锚点

- license 快照：blob `d7a14af35ecb…` → `git hash-object --no-filters` MATCH + 与 M4/M7 同物断言双过（L8 立规执行）。
- pin：`12a97516f57469078707afb587a5f84c1cb110d1`（与 M4/M7 同 HEAD，S1 时对账）；树快照 `workspace/m8_recon/booster_assets_tree_v3.json`（侦察件，不入库）。
- 上游漂移监控：仓库不活跃（pushed 2026-09-26 至今无新 push），漂移风险低；S1 对账 head。
