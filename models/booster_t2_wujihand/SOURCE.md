# SOURCE — booster_t2_wujihand 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-25）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-25 · 取证方式 = GitHub API 活源（两仓树 JSON + 变体 urdf/xml 原件 base64 落 recon）+ lxml 解析器权威口径（R34 规程：结构断言一律解析器生成）；M11 选型背景与四候选对比见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓多机型，booster_assets 第四件——T2 变体矩阵首件入库）

| 项 | BoosterRobotics/booster_assets（加速进化机器人描述资产仓） |
|---|---|
| 仓库 | https://github.com/BoosterRobotics/booster_assets |
| 拉取锚点（2026-10-25 实测） | `main` @ `12a97516f57469078707afb587a5f84c1cb110d1`（**与 M4/M7/M8 同 HEAD 四战零漂移**；树 494 件 truncated=False 今日复测同数） |
| 目标子目录 | `robots/T2/T2_31dof_WujiHand/`（变体自包含：urdf 96,175 B + xml 67,503 B + meshes/ 89 件 52.4 MB；URDF 141 mesh 引 → 87 唯一全 `meshes/` 前缀，**无跨目录引用**，S1 范围=变体目录整组） |
| 配对（待审） | `T2_31dof_WujiHand.urdf`（**lxml 权威：87 link / 86 joint = 71 revolute + 15 fixed，无 floating**——正则侦察口径 88/87/1 floating 系注释混计，K1/T2 world 块同族陷阱，R34 规程第三次实战）↔ `T2_31dof_WujiHand.xml`（**72 body / 72 joint = 1 free + 71 hinge**；72 = 87 − 15 fixed 融合自洽，两侧 71R 逐位对应） |
| 变体语义 | 基座 31R（与在库 booster_t2 同构，官网"全身 31"锚定沿用 M8）+ 双手 5 指 × 4 关节 × 2 = **71R**（M8 在档"Wuji +40"今日逐位复现）；**71R = 本库首个 70R 量级模型**（现役 11 模型 S2 报告 revolute 最大 31：x2/t2/dr02 三并列） |
| 质量 | URDF 85 mass 段，min **0.001 kg** / max 9.7137 kg，零质量段 0——手指小质量段=S3 惯量 sanity 新样本（Lite3 足端零惯量 FAIL 先例的对照组） |
| 网格 | `T2_31dof_WujiHand/meshes/` 89 件（URDF 87 唯一 ↔ MJCF 87 唯一，未收 2 件 S4 平账）；闭包与 identity S1 实测 |
| 引用协议 | URDF `meshes/` 前缀（T1/T2 同款已验风格）；MJCF `meshdir="meshes/"` |

## 2. 官方性验证（A4 同仓链条第四件继承）

- 同 org 同仓同 README（M4 四件互证沿用）；变体目录即官方发布形态（上游全量发布无筛选，官方语义）；
- 官网 T2 页"末端执行器：默认/夹爪/灵巧手"选项明示（M8 在档原文）=变体矩阵官方背书；
- 官方基准沿 M8 三可得（42 kg\* + 31 DoF + 140 N·m，主版口径）——**变体整机质量与主版的差异**（手部替换）S3 前置如实披露，不虚构变体专属基准（官方基准缺失不虚构先例 M4）。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| BoosterRobotics/booster_assets（整仓单 license，M4 已定性） | **BSD-3-Clause**（M4/R22/R31 三轮先例） | **Copyright (c) 2025, BoosterRobotics**（M4/R22 快照逐字） | **同仓复指**：`models/booster_t2/LICENSE-upstream-booster_assets.txt`（blob `d7a14af35ecb678236db590d77e29232aed10cdd`，1,502 B——2026-10-25 树实测逐位同物，四战零漂移）；本模型目录按同仓复指口径不重复落快照，S1 时 A2 对账；LICENSES.md 于 S7 加复指行 |

## 4. 选型对比备案（M11 候选池四路，全同仓复指）

| 候选 | 上仓@pin | 格式 | 关键数 | 本件倾向 |
|---|---|---|---|---|
| **D. T2_31dof_WujiHand** | booster_assets@12a97516 | urdf+xml 全 | 71R（+40 指节）| **推荐试点**（理由五条见送审件） |
| A. DR02 Standard | deep_robotics_model@530e01a5 | urdf+xml 全 | 21R/68kg（M6 取证在档） | 合格替补（最低成本） |
| B. M20S | 同上 | urdf+xml 全 | 轮足四足 | 池尾（拓扑与 M20 重复） |
| C. S10 | 同上 | urdf+xml 全（usd 排除先例） | 轮足四足 | 池尾（同上） |

## 5. 快照与锚点

- pin：`12a97516f57469078707afb587a5f84c1cb110d1`（S1 时对账，四战零漂移预期）；上游 DR 仓对照 pin `530e01a5d2ceb6007f8790f1a7e11ee7389fb981`（树 422 件今日实测同数）。
- 树快照与变体原件：`workspace/m11_recon/`（{dr,booster}_tree.json、wujihand.urdf/.xml、解析脚本——侦察件不入库）。
- 关联：主版 `models/booster_t2/`（M8 五变体对比在档其 SOURCE §1；R43 裁定②③本件启动门）。
