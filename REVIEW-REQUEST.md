# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R30 = 协议⑤执行回执终查通过——M6 含发布全流程闭环，四厂商七模型全量在线，项目回维护态**（回执数字四路活证零出入）。

【送审类型】**协议②（M7 选型定案 + S0 license 门确认 + A4 升级确认）**——触发即停手，S1 未动。（续航令下第三个自动推进里程碑：M6 收官后按 R30 候选池首选 booster K1 方向直接启动。）

【背景：在做什么】启动 **M8 系第 8 个模型 M7（第八个模型）**。定向侦察（`workspace/m7_recon/`，gitignore 不入库）：K1 配对细节 + 官网复测 + fresh pin。

**K1 侦察事实（全程序化，head 与 M4 锚 `12a97516` 零漂移——M4 S1 后上游未动）**：

- **配对结构**：`K1_22dof.urdf`（26 link / **22 revolute** + 2 fixed + 1 floating，32 引 `meshes/` 前缀 → 24 唯一，**scale 0**）↔ `K1_22dof.xml`（meshdir=meshes/，24 file 引用=24 唯一）；变体 2 件（`K1_locomotion.urdf` 裁剪版 12R+10F / `K1_22dof_parallel.xml` 并联踝——均 R22/M4 先例同款处置不入库）；网格 52 件单池；
- **官方双文档 DoF 交叉背书**：官网 K1 产品页（`/cn/booster-k1`，336,389 B 二进制原件落 evidence）规格表明示**全身 22 = 头部 2 + 双臂 8 + 双腿 12** ↔ assets README 配置表 K1 行（head 2 + arms 4×2 + legs 6×2）↔ URDF 22R——三方逐位一致；
- **官方质量基准**：官网明示**身高约 95 cm / 重量约 19.5 kg**——K1 成**本库最小型机型**（0.95 m 级，与 DR02 1.79 m/78 kg 构成尺度带两极），S3 双基准（质量+DoF）可得；
- **A4 重大升级（本件核心侦察成果）**：M4 侦察"官网首页无 K1/T1 内容、现主打 T2"——本次复测**官网首页 meta 明列 "Booster K1、T2 人形机器人"且存在 K1 产品链接 `/cn/booster-k1`，产品页完整实存**（含规格表/应用场景）——**M4"路径①阴性"结论被当前官网推翻，K1 升级为本库首个官网产品页直证机型**（M4 快照与当前页不同：官网改版或采样偏差，如实记录于 SOURCE.md §2）；
- license/官方性/引用协议全链条继承 M4（同仓第二机型线）。

**S0 已按推荐源落档**（`models/booster_k1/`，状态=待审）：SOURCE.md + license 快照（blob `d7a14af35ecb…` hash-object MATCH + **与 M4 快照逐字节同物断言**——同仓第二机型线零漂移，无新定性）+ evidence ×6（账户/repo/license 端点/HEAD/官方 README/K1 产品页二进制原件——R29 取证范式执行，本次扫描零 token 无需脱敏）。

【决策点】

1. **M7 选型定案 = 加速进化 K1（`BoosterRobotics/booster_assets`，`robots/K1/`）**——同仓第二机型线（T1 之后），本库最小型机型（0.95 m/19.5 kg 档）+ 官方双文档 DoF 交叉 + **官网产品页直证（A4 路径①升级）**；确认或改选同仓 T2 线（31DoF 四手部变体矩阵，M7+ 专项）/其他；
2. **锚点 = `K1_22dof.urdf` ↔ `K1_22dof.xml`** + 不入库清单（`K1_locomotion.urdf` 裁剪变体 / `K1_22dof_parallel.xml` 并联踝变体——R22 已裁先例同款 / `robots/T2/` 整线 M7+ / `motions/`+`src/` 仓级件）；确认或改锚；
3. **license 门确认 = 同仓单 license BSD-3-Clause 零漂移**（快照与 M4 逐字节同物 `d7a14af35ecb…`，无新定性；LICENSES.md 复指口径同 M5/M6 行式样 S7 落笔）；确认或推翻；
4. **A4 升级确认**：M4"路径①阴性"被当前官网推翻（首页 meta+K1 产品链接+产品页实存）——K1 升级为首个官网产品页直证机型，M4 结论更正如实落 SOURCE.md §2（历史口径修正，R17"46"/M4"10 URDF 无 MJCF"先例同款）；确认或裁定保留原分层口径。

【倾向 + 理由】**推荐四项全按上述定案**。理由：①K1 是候选池里证据链最厚的一枚——官网产品页+README 配置表+URDF 三方 DoF 逐位、质量基准明示、A4 双路径全中（四模型序列里首个"路径①阴性转正"案例，质检叙事增量实在）；②0.95 m/19.5 kg 小尺寸档补全尺度带（0.30 m Go2 ~ 1.79 m DR02），S6 序列第八点；③同仓第二机型线全部继承 M4 已验链条（license 同物/A4 互证/引用协议），管道预判零结构改动（22R 无 continuous/无 prismatic，floating+free 常规口径）；④风险如实列示：32 引→24 唯一的闭包差 8 件（S1 实测）、floating+显式 world 与否（S1 核对 T1 口径）、52 网格单池闭包——均 S1–S3 定案不做预断。本件不枚举自身哈希（清单至 R30 收官 `6f77c9b` + 本件随批）。

【文件路径】送审核心：`models/booster_k1/SOURCE.md`（状态=待审）+ `LICENSE-upstream-booster_assets.txt`（1,502 B，与 M4 快照同物）+ `evidence/` ×6（含官网 K1 产品页二进制原件 336,389 B）。侦察原件（不入库）：`workspace/m7_recon/`（recon 脚本 + k1_facts.json + 树 v2 + 官网双页档）。管道 diff=0（本会话零改码）。
