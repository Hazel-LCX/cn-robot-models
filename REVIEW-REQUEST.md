# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R36 = 协议⑤执行回执终查通过——M8 含发布全流程闭环，四厂商九模型全量在线，项目回维护态**（回执数字四路活证零出入；更正件逐字核验三处全执行）。

【送审类型】**协议②（M9 选型定案 + S0 license 门确认）**——触发即停手，S1 未动。（续航令下第五个自动推进里程碑：M8 收官后按 R36 候选池"同仓填充线"方向直接启动，双候选对比侦察后定推荐。）

【背景：在做什么】启动 **M10 系第 10 个模型 M9（第十个模型）**。双候选对比侦察（`workspace/m9_recon/`，gitignore 不入库）：X30（L12 scale 实战场）vs M20_Piper（prismatic 拓扑首覆盖），数据说话定推荐。

**双候选侦察事实（全程序化，head 与 M5/M6 锚 `530e01a5` 零漂移）**：

- **M20_Piper（推荐，67 目录项：1 urdf + 1 xml + 54 mesh + usd 5）**：27 link/**18 revolute + 4 continuous + 2 prismatic + 2 fixed**、37 引 `./meshes/` 前缀→27 唯一（闭包零差，预警面干净）、scale 0 ↔ `M20_Piper.xml`（27 file 引用=27 唯一，24 joint=**22 hinge + 2 slide**）——**prismatic↔slide 映射=管道关节拓扑最后一块拼图**（M5 continuous 之后第二个新拓扑实战；S2 类型映射/S5 滑条位移单位 m 非 rad（真实改码点已预判 N2 预备）/S6 场景三处覆盖）；**复合体谱系首例**（M20 轮足底盘 + Piper 臂 = 移动操作 loco-manipulation 形态，本库四足/轮足/人形之外第四谱系）；
- **X30（对照线，数据在档）**：21 件薄池——X30.urdf 22 link/12R+9F、13 引→**4 唯一**、**scale 5 处**（L12 家族实战叙事强）↔ X30.xml（8 引→4 唯一）；官网 X30 页（141,310 B 落档）**整机重量（含电池）约 56 kg** 基准可得（四足大机型档）；短板=模型几何极简（4 网格）质检面窄——**留 M9+ 档案**（scale 实战随时可做）；
- 上游 pin `530e01a5` 与 M5/M6 零漂移；license 同仓第四机型零漂移断言（`cdc6c065` 与 M2/M5/M6 快照逐字节同物）。

**S0 已按推荐源落档**（`models/deeprobotics_m20_piper/`，状态=待审）：SOURCE.md + license 快照（1,502 B hash-object MATCH + 同物断言）+ evidence ×4（repo/license 端点/HEAD/官方 README + **Piper 组件页二进制原件 60,233 B**——R29 取证范式，**本次脱敏 1 处 token**=范式实战执行）。

【决策点】

1. **M9 选型定案 = 云深处 M20_Piper（`DeepRoboticsLab/deep_robotics_model`，`M20_Piper/`）**——**prismatic 拓扑补全**（管道六关节类型 revolute/continuous/fixed/prismatic/free/floating 全覆盖收官）+ **复合体谱系首例**（M20 轮足底盘+Piper 臂移动操作平台）+ 27 引=27 唯一干净闭包；确认或改选 X30（scale 实战线，M9+ 档案随时可做）/其他；
2. **锚点 = `M20_Piper.urdf` ↔ `M20_Piper.xml`** + 不入库清单（usd 5 件先例处置/其余机型目录/仓级件）；确认或改锚；
3. **license 门确认 = 同仓单 license BSD-3-Clause 零漂移**（快照与 M2/M5/M6 逐字节同物 `cdc6c065`，无新定性；LICENSES.md 复指口径同前 S7 落笔）；确认或推翻；
4. **A4 继承确认**：M2/M5/M6 三轮双路径先例第四机型沿用，无新增阴性项；**S3 前置侦察如实分层**：Piper 臂为云深处组件产品线（组件页 60,233 B 落档但无整机参数）——复合体整机基准可能无官网页（**M4 T1 式"官方基准缺失"处置预备**，Piper 臂独立产品页 S3 前置深挖实测为准）；确认或推翻。

【倾向 + 理由】**推荐四项全按上述定案**。理由：①M20_Piper 补全管道关节拓扑最后一块拼图（prismatic）——六类型全覆盖后管道对任意上游模型的类型映射能力封顶，且 S5 滑条位移单位改码是真实覆盖点（continuous 落码先例同节奏）；②复合体谱系首例（轮足底盘+臂的 loco-manipulation）使本库谱系叙事从三形态扩到四谱系；③27 引=27 唯一+scale 0+同仓同结构——填充件管道风险最低档，S1–S7 预判零结构改动（prismatic 滑条改码除外，已预判 N2 预备）；④X30 两头数据在档（scale 实战+56 kg 基准），M9+ 随时可取。风险如实列示：复合体整机基准可能缺失（T1 式处置预备）、54 件单池闭包差 27 件（底盘共用池假设 S1 实测验证）、prismatic 滑条改码幅度——均 S1–S3/S5 定案不做预断。本件不枚举自身哈希（清单至 R36 收官 `fea300d` + 本件随批）。

【文件路径】送审核心：`models/deeprobotics_m20_piper/SOURCE.md`（状态=待审）+ `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，与 M2/M5/M6 快照同物）+ `evidence/` ×4（含 Piper 组件页二进制原件 60,233 B，脱敏 1 处 token）。侦察原件（不入库）：`workspace/m9_recon/`（recon 脚本 + m9_facts.json + 树 v3 + X30/组件页档）。管道 diff=0（本会话零改码）。
