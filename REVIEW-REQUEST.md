# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R27 = 协议⑤执行回执终查通过——M5 含发布全流程闭环，三厂商六模型全量在线，项目回维护态**（回执数字四路活证零出入）。

【送审类型】**协议②（M6 选型定案 + S0 license 门确认）**——触发即停手，S1 未动。（续航令下第二个自动推进里程碑：M5 收官后按 R27 点名"M6+ 候选（DR02=云深处人形官网实证）"方向直接启动。）

【背景：在做什么】启动 **M6（第七个模型）**。定向侦察（`workspace/m6_recon/`，gitignore 不入库）：DR02 双配置程序化对比 + 官网规格页结构化提取 + fresh pin。

**DR02 侦察事实（全程序化，head `530e01a5` 与 M5 同——M5 S1 后上游未动）**：

- **双配置官方算术逐位闭合（选型证据为历次最强）**：官网规格页（detail/5.html，静态 HTML 150,548 B 原件落档）明示两版本逐部位 DoF 分解——**Pro：主动 31 = 单臂 7×2 + 单腿 6×2 + 腰 3 + 头 2** ✓↔ `DR02-pro.urdf` 31R ↔ `DR02_pro.xml` 31 关节；**Standard：主动 21 = 单臂 4×2 + 单腿 6×2 + 腰 1** ✓↔ `DR02-std.urdf` 21R ↔ `DR02_std.xml` 21 关节；整机重量（含电池）**Pro 约 78 kg / Standard 约 68 kg**、站立尺寸约 1800×558×400 mm（1.8 m 级，本库最高模型）；
- **Pro 配置细节**：40 link / 31R+8F、39 引 `./meshes/` 前缀（Lite3/M20 同款）→ 34 唯一网格、**scale 0**；MJCF `model=DR02_pro`、meshdir 相对、31 关节——双侧自洽；
- **变体与平替**：`DR02-pro_fix_joints.urdf`（同 40 link、10 关节固化为 fixed=21R+18F，锁死变体——T1_locomotion 同类处置不入库）；`DR02-std.urdf`（24 link/21R+2F，22 引=22 唯一）+ `DR02_std.xml` 为 Standard 平替配对；
- 网格 114 物理件分 pro/standard 两侧（分目录形态，M20 同款已验）；DR02 官网定位"全球首款行业级全天候人形机器人"；
- 同仓其余机型（M20S/S10/M20_Piper/X30）与跨仓候选（booster K1/T2）维持 M7+ 档案。

**S0 已按推荐源落档**（`models/deeprobotics_dr02/`，状态=待审）：SOURCE.md + license 快照（blob `cdc6c065` hash-object MATCH + **与 M2/M5 快照逐字节同物断言**——同仓第三机型零漂移，无新定性）+ evidence ×4（repo/license 端点/HEAD/官网 DR02 规格页原件）。

【决策点】

1. **M6 选型定案 = 云深处 DR02（`DeepRoboticsLab/deep_robotics_model`，`DR02/` Pro 配置）**——本库**第 4 个人形机型**（G1/X2/T1 之后）与**云深处首个人形**、1.8 m 级库内最高；确认或改选 Standard 平替（21R/68kg，管道成本相同）/其他候选；
2. **锚点 = `DR02/urdf/pro/DR02-pro.urdf` ↔ `DR02/mjcf/pro/DR02_pro.xml`** + 不入库清单（`DR02-pro_fix_joints.urdf` 锁死变体 / Standard 配对整组随裁定 / usd 件如有 / 根级仓级件）；确认或改锚 Standard；
3. **license 门确认 = 同仓单 license BSD-3-Clause 零漂移**（快照与 M2/M5 逐字节同物 `cdc6c065`，无新定性；LICENSES.md 复指口径同 M5 行式样 S7 落笔）；确认或推翻；
4. **A4 继承确认**：M2/M5 已证双路径全中第三机型沿用，无新增阴性项；S3 前置侦察基本完成——官方双基准可得（**质量 78 kg（Pro 含电池）+ DoF 逐部位分解**），S3 回填时逐字核对原件。

【倾向 + 理由】**推荐四项全按上述定案**。理由：①选型证据为历次最强——官网逐部位 DoF 分解与仓库配置逐位闭合（31=7×2+6×2+3+2 / 21=4×2+6×2+1），超越 T1 README 表与 X2 推断式证据；②DR02 使本库人形覆盖达四机型（宇树/智元/加速进化/云深处四家人形齐备），1.8 m 级与大质量（78 kg）对 S3 对账和 S6 序列都是新数据点；③同仓第三机型 license/A4/引用协议全部继承已验链条，管道预判零结构改动（fix_joints 变体与 usd 件按既有先例处置）；④风险如实列示：39 引→34 唯一的闭包差（5 件变体共用网格）、分目录网格同 M20 形态、78 kg 大质量 S3 容差口径——均 S1–S3 实测定案不做预断。本件不枚举自身哈希（清单至 R27 收官 `24461b8` + 本件随批）。

【文件路径】送审核心：`models/deeprobotics_dr02/SOURCE.md`（状态=待审）+ `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，与 M2/M5 快照同物）+ `evidence/` ×4（含官网规格页原件 150,548 B）。侦察原件（不入库）：`workspace/m6_recon/`（recon 脚本 + dr02_facts.json + 规格页档）。管道 diff=0（本会话零改码）。
