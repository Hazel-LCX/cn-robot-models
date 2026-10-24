# SOURCE — deeprobotics_m20_piper 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-24）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-24 · 取证方式 = GitHub API 活源 + 双候选对比侦察（X30 对照线数据在档）+ 官网组件页取证；M9 选型背景见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓多机型，同仓第四机型——复合体形态）

| 项 | DeepRoboticsLab/deep_robotics_model（云深处模型仓，八机型） |
|---|---|
| 仓库 | https://github.com/DeepRoboticsLab/deep_robotics_model |
| 拉取锚点（2026-10-24 实测 head） | `main` @ `530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（**与 M5/M6 同 HEAD 零漂移**；树 422 件 truncated=False） |
| 目标子目录 | `M20_Piper/`（67 目录项：1 urdf + 1 xml + 54 mesh + usd 5 件） |
| 配对选定（待审） | `M20_Piper/urdf/M20_Piper.urdf`（27 link / **18 revolute + 4 continuous + 2 prismatic** + 2 fixed，37 引 `./meshes/` 前缀 → 27 唯一，scale 0）↔ `M20_Piper/mjcf/M20_Piper.xml`（27 file 引用=27 唯一，24 joint=**22 hinge + 2 slide**） |
| 网格 | `M20_Piper/meshes/` 54 件（两侧引用闭包 27，其余 27 件 S1 实测身份——M20 底盘共用池可能性待核） |
| 引用协议 | URDF `./meshes/` 显式前缀（Lite3/M20/DR02 同款第四形态）；MJCF `meshdir` 相对（M20 同款） |
| 关节拓扑（侦察实测，**管道六拓扑补全**） | **18 revolute + 4 continuous + 2 prismatic + 2 fixed**——MJCF 侧 22 hinge + **2 slide**：**prismatic↔slide 映射=管道关节拓扑最后一块拼图**（M5 continuous 之后第二个新拓扑实战：S2 类型映射/S5 滑条位移单位 m 非 rad（真实改码点，N2 预备）/S6 场景三处覆盖） |
| 不入库（记录口径，S1 实测细化） | `usd/` 5 件（M20/M2 先例）、其余机型目录（`DR02/` Standard 线、`M20S/` `S10/` `X30/` 等 M9+ 档案）、根级仓级件 |

**机型背景（待审）**：M20_Piper = 云深处 **M20 轮足底盘 + Piper 臂移动操作复合体**（M20 底盘 18R+4C 轮足 + Piper 臂末端 2 prismatic 夹爪平移关节）——**移动操作（loco-manipulation）形态为本库首例**（四足/轮足/人形/复合体第四谱系）。官网组件产品线独立页（`evidence/official-piper-component-page.html` 60,233 B 落档——组件列表页，Piper 臂详细规格在独立产品页，S3 前置侦察深挖如实记录）。**S3 质量基准预判**：复合体重量大概率=M20 底盘 35 kg + Piper 臂自重（官网组件页/产品页 S3 前置实测，不做预断）。

## 2. 官方性验证（A4——同仓链条第四机型继承）

- **M2/M5/M6 同仓同 org**：双路径先例四轮在案（R14/R25/R28）——**第四机型直接沿用，无新增阴性项**；
- 官网组件产品线（Piper 臂为云深处独立组件产品，`products/index/4.html` 组件分类在导航——M9 侦察实测）；README 八机型表含 M20_Piper 行（`evidence/official-readme-deep_robotics_model.txt`）；**R37 轻度口径处置（S1 落档）**：①evidence 原件改名 `official-robot-component-index-page.html`（通用分类列表页零 Piper 字样，原"piper-component-page"关联性过强）；②**Piper 独立产品页确认无**（组件分类页 detail 链接 1/2/5/6/7/8/9 全为整机与 J 系列关节，零 Piper 字样，S1 实测在案）——S3 整机基准按 M4 T1 式 mass_kg=null WARN 处置定案；
- S3 前置侦察留待：Piper 臂独立产品页深挖（质量/负载/DoF 基准可得性实测——组件页 60,233 B 无整机参数，复合体整机基准可能无官网页=M4 T1 式处置预备，如实定案）。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| DeepRoboticsLab/deep_robotics_model（整仓单 license，M2 已定性） | **BSD-3-Clause**（M2/R14/R22/R25/R28 五轮先例） | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，blob `cdc6c065…`，hash-object MATCH，**与 M2/M5/M6 快照逐字节同物**——同仓第四机型零漂移断言过） |

**定性论证**：与 M2/M5/M6 完全同源（同仓同 license），**无新定性考题**——S0 license 门作业 = 零漂移断言 + 快照随件分发；LICENSES.md 复指口径同 M5/M6/M7 行式样（S7 落笔）。

## 4. 选型对比备案（M9 候选线）

- **M20_Piper（本件）**：prismatic 拓扑补全（六关节类型全覆盖收官）+ 复合体谱系首例（loco-manipulation）+ 27 引=27 唯一干净闭包 + scale 0；S5 prismatic 滑条改码点已预判（N2 预备）；
- **X30 对照线（数据在档，M9+ 档案）**：21 件薄池（13 引→4 唯一+5 scale——L12 家族实战叙事强）+ 官网 56 kg 基准可得（四足大机型档）；短板=模型几何极简（4 网格）质检面窄；
- 其余（DR02 Standard/fix_joints、M20S/S10 同构变体、booster T2 手部双锚题）维持档案。

## 5. 快照与锚点

- license 快照：blob `cdc6c065…` → `git hash-object --no-filters` MATCH + 与 M2/M5/M6 同物断言双过（L8 立规执行）。
- pin：`530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（与 M5/M6 同 HEAD，S1 时对账）；树快照 `workspace/m9_recon/deep_robotics_model_tree_v3.json`（侦察件，不入库）。
- 上游漂移监控：活跃仓（pushed 2026-10-23），S1 对账 head；pin 机制免疫后续上游变动。
