# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R21 = 协议⑤执行回执终查通过——M3 含发布全流程闭环，项目回维护态**（四路活证零出入；收官 commit `8195c20` 已随队 push，远端 53 commit）。

【送审类型】**协议②（M4 选型定案 + S0 license 定性结论确认 + 源修正确认）**——触发即停手，S1 未动。

【背景：在做什么】M3 收官后用户令"继续"，启动 **M4（第五个模型）**。侦察两候选线全程序化取证（GitHub API + 官网双页实测 + SPDX 名录，原始数据在 `workspace/m4_recon/`，gitignore 不入库）。

**两候选线侦察事实（全程序化取证）**：

- **候选 A 加速进化（BoosterRobotics，第四厂商）**：账户类型 **User 非 org**（9 仓，M1 L11 同款事实沿用）。**源修正（本件核心侦察成果）**——M3 时代"跨仓配对"预设被三步修正：①`booster_train` 81 件全为训练代码零 T1 资产（M3 档案树扫复证）；②`booster_gym` `resources/T1/` 单仓含 URDF↔MJCF 配对，但根 LICENSE 为 916 B 短格式 Apache-2.0 声明（方括号版权行致 NOASSERTION，M3 已识真身，blob `c9e19b34` 本会话复测**零漂移**）且 44 STL 池 20 件无引用、meshes 非专用；③**专用描述资产仓 `booster_assets` 形态最优**——BSD-3-Clause 全文在仓（1,502 B）、`robots/` 下 K1/T1/T2 三机型线、官方 README 逐机型 DoF 配置表、活跃维护（pushed 2026-09-26，45.4 MB/494 树件 truncated=False）。**历史口径修正（如实记录）**：M3 送审件曾记"T2/K1 等其余 10 URDF 无 MJCF"——本次 `booster_assets` 全树实测 **10 urdf + 11 xml**，K1_22dof 与 T2 全部五变体均有同目录 xml 配对，T1 线唯一无配对件 = `T1_29dof.urdf`。
- **候选 B 云深处同仓多机型**（`DeepRoboticsLab/deep_robotics_model`）：Lite3 之外六机型目录全扫——DR02（144 件/3 urdf+2 xml/114 mesh，变体最多）、M20/M20S/S10（各 47 件 1+1 配对）、M20_Piper（67 件）、**X30（21 件仅 8 mesh，网格异常薄——若选需 S1 闭包先行核，如实预警）**；license 零漂移（M2 快照 blob `cdc6c065` = 上游现值 hash-object 逐位）；仓库活跃（pushed 2026-10-23，HEAD `530e01a5` 相对 M2 Lite3 pin `75824b5` 已漂移——pin 机制对此免疫，M0 先例）。

**S0 已按推荐源落档**（`models/booster_t1/`，状态=待审）：SOURCE.md + license 快照（blob `d7a14af35ecb…` hash-object MATCH）+ evidence ×6（账户/repo/license 端点/HEAD/SPDX-BSD-3/官方 README 声明）。**源修正纪律**：gym 仓 v1 取证件撤至 `workspace/m4_recon/archive_gym_s0/` 不入库——证据链不混用两正本（L12 教训）。

【决策点】

1. **M4 选型定案 = 加速进化 T1（BoosterRobotics/booster_assets，`robots/T1/`）**——确认或改选候选 B；本选型使本库达**四厂商五模型**，且首次引入"专用资产仓正本 + 训练仓旁证"的生态位记录；
2. **锚点 = `T1_23dof.urdf` ↔ `T1_23dof.xml`** + 不入库清单（`T1_29dof.urdf` 无 xml 配对 / `T1_locomotion.*` 裁剪变体 / `T1_23dof_parallel.xml` 并联变体——**我方倾向不入库**（用途特化副本，同 X2 simple_collision 处置先例），待裁 / `robots/K1/`+`robots/T2/` 整线 M4+ 候选 / `motions/`+`src/`+仓级配置件）——确认或改锚 locomotion（若倾向与 gym 训练口径一致）；
3. **license 定性 = booster_assets BSD-3-Clause 可收录**（全文在仓、SPDX `isOsiApproved: True` 未弃用、M0/M2 同族三锚先例、版权行 `Copyright (c) 2025, BoosterRobotics` 快照逐字）；gym 仓 Apache-2.0 短格式定性件降侦察档案、不作本仓门槛——确认或推翻；
4. **A4 分层 + 源修正确认**：路径②成立四件互证（账户 blog 自指官网 / assets README 官方自述+配置表 / gym README 官方署名+三官方仓互链 / 版权行公司主体），**路径①阴性**（官网首页 227,886 B + T2 产品页 263,184 B 双页零 GitHub 直链零 T1——JS 渲染站，官网现主打 T2）；"跨仓配对"预设修正为**单仓同目录直配**，管道预判零结构改动——确认修正记录入 SOURCE.md §4。

【倾向 + 理由】**推荐四项全按上述定案**。理由：①T1 路线带来第四厂商与新生态位事实（User 账户、资产仓+训练仓分工、官网主打 T2 的前代收录），质检叙事增量实在；②锚点选择有官方 README 配置表背书（head 2 + arms 4×2 + waist 1 + legs 6×2 = 23 算术自洽），强于 M3 的推断式选型，且与 M1 `g1_23dof` 命名形态同款；③管道预判零结构改动：单仓同目录配对、MJCF `meshdir` 相对引用（resolve_ref 已覆盖）、侦察 T1 gym 版 URDF 零 scale 属性（assets 版 S1 实测复核）——"加 config 即加模型"范围内；④候选 B 留 **M4+ 维护态填充**（license 零漂移已证、六机型事实在档，随时可做，与 M3 会话 19 分层建议一致）；⑤风险如实列示：assets 版 URDF 引用风格/网格闭包/官方质量参数均 S1–S3 实测定案，本件不做预断。

【文件路径】送审核心：`models/booster_t1/SOURCE.md`（状态=待审）+ `LICENSE-upstream-booster_assets.txt`（blob 正本快照 1,502 B）+ `evidence/` ×6。侦察原件（不入库）：`workspace/m4_recon/`（recon 脚本 ×3 + gym/assets 树扫 JSON + 两仓 license JSON + 官网双页 HTML + `archive_gym_s0/` 撤档）。管道 diff=0（本会话零改码）。
