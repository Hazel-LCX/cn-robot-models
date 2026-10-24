# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R24 = 协议⑤执行回执终查通过——M4 含发布全流程闭环，四厂商五模型全量在线，项目回维护态**（回执数字四路活证零出入）。

【送审类型】**协议②（M5 选型定案 + S0 license 门确认）**——触发即停手，S1 未动。（背景：M4 收官后用户立"跨 leg 续航令"——没到审核点直接继续，本件为续航令下首个自动推进里程碑，R24 点名的 M4+ 方向。）

【背景：在做什么】按 R24 遗留"云深处同仓多机型=M4+ 候选"方向启动 **M5（第六个模型）**。M4 侦察已扫全仓六机型，本会话定向补扫（`workspace/m5_recon/`，gitignore 不入库：fresh HEAD 树 v2 + 根 README 原件 + 逐机型配对/引用/关节程序化汇总）。

**六机型侦察事实（全程序化，head `530e01a5`）**：

- **M20**（47 件，1 urdf+1 xml+34 mesh）：17 引 `./meshes/` 前缀（Lite3 同款已验风格）→ 17 唯一网格，scale 0；关节 **12 revolute + 4 continuous + 4 fixed**——**管道首个 continuous 关节模型**（轮足形态 4 轮关节）；
- **M20S / S10**（各 47 件，1+1）：与 M20 同构（12R+4C，fixed 数差 1），M20 系变体；
- **M20_Piper**（67 件，1+1）：M20+Piper 臂复合体（18R+4C+2**prismatic**+2F），复合产品口径题（质量/基准归属）；
- **DR02**（144 件，3 urdf+2 xml+114 mesh）：Pro/Standard 双配置 + pro_fix_joints 变体（31R+8F，39 引→34 唯一，scale 0）——本仓最大最重，双配置选型题（g1/X2 先例同款）；
- **X30**（21 件，1+1）：**13 引用仅 4 唯一 mesh + 5 处 scale 属性**——模型薄 + L12 雷区叠加，若收录需闭包+scale 专项核（如实预警）；
- 上游根 README 自述八机型 + Lite3 更新注记（2026-08-21 OEM 版：**URDF 与 MJCF/USD 的 thigh 质心存在差异**——本库 M2 已对账质量总量与逐 body mass 17/17，COM 不在当期范围；本条如实转述备案进 SOURCE.md §4，不动 M2 已闭环记录）。

**S0 已按推荐源落档**（`models/deeprobotics_m20/`，状态=待审）：SOURCE.md + license 快照（blob `cdc6c065` hash-object MATCH + **与 M2 Lite3 快照逐字节同物断言**——同仓单 license 零漂移，无新定性考题）+ evidence ×4（repo/license 端点/HEAD/官方根 README）。

【决策点】

1. **M5 选型定案 = 云深处 M20（`DeepRoboticsLab/deep_robotics_model`，`M20/`）**——同仓第二机型（Lite3 之后），轮足形态 + 管道首个 continuous 关节拓扑（S2 关节类型覆盖/S5 滑条语义/S6 场景设定三处真实新覆盖点）；确认或改选 DR02（最大最重+双配置选型题，M5+ 替补）/M20_Piper（prismatic 夹爪拓扑，复合体口径题）/其他；
2. **锚点 = `M20/urdf/M20.urdf` ↔ `M20/mjcf/M20.xml`** + 不入库清单（同仓其余七机型目录=M5+ 候选、根级仓级件、USD 外链件不收——README 自述 high-res 走 Google Drive，**只收本仓发布件红线**）；确认或改锚；
3. **license 门确认 = 同仓单 license BSD-3-Clause 零漂移**（快照与 M2 逐字节同物 `cdc6c065`，无新定性；LICENSES.md 无新增 license 行、仅 deeprobotics_m20 行复指同仓口径 S7 落笔）；确认或推翻；
4. **A4 继承确认**：M2 已证双路径全中（官网支持页直链+org 互证）直接沿用，无新增阴性项；M20 官网规格侦察留 S3 前置（官方质量对账有望恢复——T1 缺失能力，S3 前置实测为准不做预断）。

【倾向 + 理由】**推荐四项全按上述定案**。理由：①M20 在审核台点名的填充方向内做出真实增量——不是 Lite3 形态复读，continuous 关节是管道五个模型均未覆盖的拓扑（轮足转位在 S6 场景设定、S5 滑条无限位语义、S2 yourdfpy/mujoco 类型映射上都有实测题，预判零结构改动但如实留 S1–S2 定案空间）；②1+1 干净配对+47 件轻量+scale 0+已验引用风格——填充件的管道风险最低档；③license 零新考题（同物快照断言），S0 成本极小而 A4 链条完整继承；④六机型事实全部落档（DR02/X30/M20_Piper 的价值与风险各有着落），后续维护态填充可按需取用。本件不枚举自身哈希（清单至 R24 收官 `6a1c02a` + 本件随批）。

【文件路径】送审核心：`models/deeprobotics_m20/SOURCE.md`（状态=待审）+ `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，与 M2 快照同物）+ `evidence/` ×4。侦察原件（不入库）：`workspace/m5_recon/`（recon 脚本 + S0 生成器 + 树 v2 JSON + dr_model_facts.json + 官方 README 档）。管道 diff=0（本会话零改码）。
