# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。

【送审类型】**协议②选型送审（M11 启动门）**——M10 闭环（R43）后维护态首个新里程碑，R43 裁定②"M11+ 候选动前先协议②"之执行件。

【背景：在做什么】
M11 候选池四路侦察完毕（全程序化：两仓树 JSON + 变体 urdf/xml 原件 base64 活源实测，侦察件 `workspace/m11_recon/` 不入库）：
- **A. DR02 Standard 平替**（`DeepRoboticsLab/deep_robotics_model@530e01a5`，树 422 件今日实测同数零漂移）：M6 留档"平替整组留后续"，官网 21R/68kg 口径 M6 已取证；`urdf/standard/DR02-std.urdf`（26,125 B）+ `mjcf/standard/DR02_std.xml`（21,705 B）双格式全；拓扑=在库 pro 减配，零新增。
- **B. M20S**（同仓）：urdf 23,032 B + mjcf 18,834 B 双格式全；轮足四足，与在库 M20 同拓扑族。
- **C. S10**（同仓）：urdf 23,134 B + mjcf 15,555 B 双格式全 + usd 仓级件（S1 范围控制排除，Lite3/M20 先例）；轮足四足小机型，同拓扑族。
- **D. T2 手部四变体**（`BoosterRobotics/booster_assets@12a97516`，与 M4/M7/M8 同 HEAD 四战零漂移，树 494 件今日实测同数）：M8 在档 JZ 43R / Revo2 53R / **Wuji 71R** / YS 43R——今日实测 WujiHand 71R 逐位复现；变体**自包含**（meshes/ 89 件 52.4 MB，URDF 141 引 → 87 唯一全 `meshes/` 前缀，无跨目录引用）；**lxml 权威口径 87 link / 86 joint = 71 revolute + 15 fixed，无 floating**（正则侦察 88/87/1 floating 系注释混计——K1/T2 world 块同族陷阱，R34 规程第三次实战，SOURCE 已落解析器口径）；MJCF 72 body / 72 joint = 1 free + 71 hinge（72 = 87 − 15 fixed 融合自洽，两侧 71R 对应）；mass 85 段 min 0.001 / max 9.7137 kg，零质量段 0。

【决策点】
1. **M11 选型**：推荐 **D 试点 = `T2_31dof_WujiHand`（71R 灵巧手）**；备选 A（DR02 Standard，最低成本快速填充）；B/C 不推本轮（拓扑与 M20 重复，边际价值低，列池留档）。
2. **license 口径**：**同仓复指** booster_assets——BSD-3-Clause（M4/R22/R31 三轮先例）；今日树实测 LICENSE blob `d7a14af35ecb678236db590d77e29232aed10cdd`（1,502 B）与 M4/M7/M8 快照同物零漂移。无新定性，请确认复指适用。
3. **双锚/入库口径**：变体以独立模型目录 `models/booster_t2_wujihand/` 入库（目录名直译上游；主版 `booster_t2` 不动）——M8 期"变体不入库只记录"（X2 手部先例）由本件**升格为"变体入库"**请裁；主版页+变体页互链（S7 文档层小改）；S1 范围=变体目录整组（自包含已实测）；后续三变体（JZ/Revo2/YS）随"加 config"填充候选留池。
4. **顺手改码窗口**：R26 遗留"页头 revolute 16 滑条计数标签"（preview.js 计数标签 12R+4C 合计误标 revolute）细化——71 滑条模型入库必然开 S5 窗口，拟随本 leg N2 备案顺手执行，**范围=页头计数标签显示层**（如"滑条 N（xR+yC+zP）"式分解标注），**不动 kinematics/加载逻辑**——请确认范围边界。

【倾向+理由】
倾向 **D（WujiHand 试点）**：①**变体矩阵双锚是质检工程新叙事维度**——基座 31R 与在库 T2 逐位对账 + 末端 40 指节差异 = 三锚对账新形态；②**71R = 本库首个 70R 量级模型**（现役 11 模型 S2 报告 revolute 最大 31，x2/t2/dr02 三并列）——S5 滑条面板（71 个）与 S6 基准压力实测有价值；③**证据成本最低的变体**：M8 五变体对比在档 + 今日实测复现，license 零新定性；④手指 0.001 kg 量级小质量段 = **S3 惯量 sanity 新样本**（Lite3 足端零惯量 FAIL 先例的对照组）；⑤71 滑条倒逼 S5 开窗——R26+R43 两笔遗留标签问题一次清账。若审核台倾向稳妥，A 为合格替补（M6 留档证据现成，M6 时官网口径已取证）。

【文件路径】
- SOURCE：`models/booster_t2_wujihand/SOURCE.md`（S0 产物，状态=待审核台确认）
- 侦察件（不入库）：`workspace/m11_recon/`（两仓树 JSON、wujihand.urdf/.xml 原件、解析脚本）
- 上游：`DeepRoboticsLab/deep_robotics_model@530e01a5`、`BoosterRobotics/booster_assets@12a97516`
- 规程参照：PIPELINE.md §8 协议②；R26 遗留标签（DEVLOG）；R34 解析器规程；R43 裁定②③
