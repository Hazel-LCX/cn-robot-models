# SOURCE — deeprobotics_m20 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-24）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-24 · 取证方式 = GitHub API 活源 + 逐机型引用/关节程序化扫描；M5 选型背景与六机型对比见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓多机型，M2 Lite3 同仓第二机型）

| 项 | DeepRoboticsLab/deep_robotics_model（云深处模型仓，八机型） |
|---|---|
| 仓库 | https://github.com/DeepRoboticsLab/deep_robotics_model |
| 拉取锚点（2026-10-24 实测 head） | `main` @ `530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（2026-10-23 push，活跃仓；树 422 件 truncated=False；相对 M2 Lite3 pin `75824b5` 已漂移——pin 机制免疫，M0 先例） |
| 目标子目录 | `M20/`（单机型 47 件：1 urdf + 1 xml + 34 mesh + 杂件） |
| 配对选定（待审） | `M20/urdf/M20.urdf` + `M20/mjcf/M20.xml`（同名直配，1+1 干净形态） |
| 网格 | `M20/meshes/` 34 件（URDF 17 引用 → 17 唯一网格，闭包关系 S1 实测复核） |
| 引用协议 | URDF `./meshes/` 显式前缀（**Lite3 同款已验风格**，m5_recon 引用样本 `./meshes/base_link.STL` 实测）；MJCF 结构 S1 实测 |
| 关节拓扑（侦察实测） | **12 revolute + 4 continuous + 4 fixed = 管道首个 continuous 关节模型**（轮足形态：4 轮转向/驱动连续旋转关节，无限位）——S2 关节类型覆盖 / S5 滑条语义 / S6 场景设定均是新覆盖点，S1–S2 实测定案如实送审预警 |
| 不入库（记录口径，S1 实测细化） | 同仓其余七机型目录（`Lite3/` 已收录、`M20S/` `S10/` `M20_Piper/` `X30/` `DR02/` M4+ 候选）、根级 `images/` `Contributors.md` `LICENSE.txt` `README.md` `.gitattributes`（仓级件）；USD 格式本仓未含（README 自述 high-res 走 Google Drive 外链，**不入库不引外链**——只收本仓发布件红线） |

**机型背景（待审）**：M20 = 云深处轮足四足（官方根 README 机型表列名；12 腿关节 + 4 轮关节拓扑侦察实测）。同仓 M20S（同构 1+1）、S10（同构 1+1）、M20_Piper（M20+Piper 臂复合体，含 2 prismatic 夹爪关节）、DR02（Pro/Standard 双配置 3 urdf，31R+8F，114 网格池）、X30（薄网格：13 引用仅 4 唯一 mesh + **5 处 scale 属性**——L12 雷区，若收录需闭包+scale 专项核）均为 M5+ 候选。

## 2. 官方性验证（A4——复用 M2 已证链条）

- **M2 Lite3 同仓同 org**：DeepRoboticsLab 官方性与 A4 双路径（官网支持页直链 + org 互证）已于 M2 全中（R14 复核升级），本仓同 org 同 license 同仓——A4 链条直接继承，无新增阴性项；
- 官方根 README 机型叙事（`evidence/official-readme-deep_robotics_model.txt`：八机型表 + viewer/Drive 外链口径）；M20 官网产品页规格侦察留 S3 前置（Lite3 支持页路径同厂可复用，**S3 基准可得性大概率恢复**——M4 T1 缺失的官方质量对账在 M20 上有望补回，S3 前置实测为准不做预断）。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| DeepRoboticsLab/deep_robotics_model（整仓单 license，M2 已定性） | **BSD-3-Clause**（M2 先例，R14/R22 两轮活源核验） | **Copyright (c) 2024, DeepRoboticsLab**（快照逐字，N1） | `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，blob `cdc6c065…`，hash-object MATCH，**与 M2 Lite3 快照逐字节同物**——同仓单 license 零漂移，S0 断言通过） |

**定性论证**：与 M2 Lite3 完全同源（同仓同 license 同版权行），**无新定性考题**——本 S0 的 license 门作业 = 零漂移断言 + 快照随件分发（义务履行同 M2 口径）。同仓第二机型使 LICENSES.md 无新增 license 行（仅 deeprobotics_m20 行复指同仓条目口径，S7 时按表结构落笔）。

## 4. 背景备案（如实转述上游披露）

- 上游根 README"Lite3 model update (2026-08-21)"注记：**Lite3 URDF 与 MJCF/USD 的 thigh 质心存在差异**（OEM 格式特有数据）。本库 M2 已对账质量总量与逐 body mass 一致性（17/17），**COM 不在 M2 对账范围**——本条为上游自述的如实转述备案，不动 M2 已闭环记录；如审核台认为需要补对账，属新增质检项走 S3 前置裁定。

## 5. 快照与锚点

- license 快照：blob `cdc6c065…`（license 端点 `_links.git` 直取）→ `git hash-object --no-filters` MATCH + 与 M2 快照同物断言双过（L8 立规执行）。
- pin：`530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（2026-10-24 实测，`evidence/github-head-deep_robotics_model.json`）；树快照 `workspace/m5_recon/deep_robotics_model_tree_v2.json`（侦察件，不入库）。
- 上游漂移监控：**活跃仓（pushed 2026-10-23）**——S1 时对账 head；本 pin 锚定后上游再动不影响入库件（M0 先例）。
