# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> **已审 2026-10-11 · R16 结论：协议⑤完成，M2 含发布全流程闭环（三源 `8a13023`、总数 45=基数 36+9、上线链 9 条 ✓、R13 专项检查过=R15 节确随队、N2 备案首执行在案）。R16 本条+回执 commit `0529d1d` 一并 push 收尾（R13 先例，无需新送审），push 后回维护态。详见 REVIEW.md R16。**
> 上一次送审已于 2026-10-11 审毕：**R15 = 协议⑤ M2 push 放行**（S7 验收通过 + S3 FAIL 处置立先例 + N2 立规）。

【送审类型】**协议②（M3 选型定案 + S0 license 定性结论确认）**——MulanPSL-2.0 定性即 R16 预设的前置考题，本件正面接题；触发即停手，S1 未动。

【背景：在做什么】M2 收官后用户令"继续"，启动 **M3（第四个模型）**。选型侦察按 M1/M2 先例做全：三路线候选实测（GitHub API + 官方域四站 + SPDX 官方名录，原始数据在 `workspace/m3_recon/`，gitignore 不入库）。

**三路线侦察事实（全程序化取证）**：

- **路线 A 云深处同仓多机型**（DR02/M20/S10/X30）：同仓 BSD-3 已在 M2 定性（S0 最省）；URDF 均为 SolidWorks 导出 + 内嵌 mujoco compiler 块，MJCF 兄弟件同在（6 个 URDF∩MJCF 新配对）；但同仓同风格同格式，管道新覆盖少。
- **路线 B 加速进化跨仓配对**：`BoosterRobotics` 实为**个人账户非 org**（9 仓）——M1 期 org 扫描失败真因即此（记 AGENT-LAB L11）；**关键新事实：`booster_gym`（Apache-2.0，方括号版权行骗过检测器显 NOASSERTION）内 resources/T1/ 已有 URDF↔MJCF 同仓配对**——"跨仓配对"非必需；若坚持跨仓（assets URDF 正本 + gym MJCF）则是 S1/S4 双仓双 license 三锚结构性扩展。T2/K1 等其余 10 URDF 无 MJCF。
- **路线 C 智元**：`genie_sim`（NOASSERTION，平台仓非模型库）与 `genie_sim_robot_model`（Apache-2.0，**仅 xacro 源 0 成品 URDF**——收源生成为派生，撞"只收官方发布件"红线精神）均否决；**`agibot_x2_urdf` 可行**：NOASSERTION 真身 = **木兰宽松许可证第 2 版（MulanPSL-2.0）**，URDF↔MJCF 同目录直接配对（v1.4.0），STL 网格。
- **MulanPSL-2.0 定性核心证据**：SPDX 官方名录 740 项程序化命中——`MulanPSL-2.0`，`isOsiApproved: True`（OSI 认证）、未弃用；官方 README 明文声明采用；原文快照 blob `adf05533…` hash-object 比对 MATCH。

【决策点】

1. **M3 选型定案 = 智元灵犀 X2（AgibotTech/agibot_x2_urdf）**——确认或改选路线 A/B；
2. **MulanPSL-2.0 定性结论 = 可收录**——确认或推翻（红线："license 不明=不收录"的正确执行是拿原文定性，非跟随 GitHub 检测器空白）；
3. **锚点 = v1.4.0 X2-Ultra 配对** + 不入库清单（v1.3.0 整套 / X2-EDU 配对 / omnihand+omnipicker 手部变体 / simple_collision / scene.xml / x2_fist）——确认或改锚 EDU；
4. **A4 强度如实分层**：路径②成立（org 官方字段自指 agibot.com + 23 仓生态互证 + README_CN 官方声明 + 官网页脚生态仓直链含 Agibot-World 品牌互指），**路径①阴性**（官网→AgibotTech org 直链四站探测未命中：agibot.com.cn / open.agibot.com / openloong.org.cn / agibot.com）——强度低于 M2、与 M1 相当，S0 收尾补强方向 = 官网新闻/公告页深挖。

【倾向 + 理由】**推荐四项全按上述定案**。理由：①X2 路线正面接审核台预设考题——S0 门要在 GitHub 检测器失效处拿出程序化证据链（原文快照 → SPDX 名录核验 → 义务清单 → 兼容性分析），这是"质检工程含金量"的最硬一集，且智元=第三家厂商+国产开源许可证第一例，与"国产机器人仿真模型库"主题同频；②管道预判零结构改动：单仓、Lite3 同款 `./meshes/` 显式前缀（72 引实测）、MJCF meshdir 相对引用（resolve_ref 已覆盖）、STL 网格——"加 config 即加模型"范围内；③跨仓配对（路线 B）是 S1/S4 结构性专项（双仓双 license 三锚），值得单独里程碑专心做，建议 M4；同仓多机型（路线 A）是随时可做的填充件，建议 M4+/维护态演示"一站式覆盖"叙事用。

【文件路径】送审核心：`models/agibot_x2/SOURCE.md`（状态=待审）+ `LICENSE-upstream-mulanpsl2.txt`（blob 正本快照）+ `evidence/` ×6（org/repo/license 端点/HEAD commit/SPDX 记录/README 官方声明）。侦察原件（不入库）：`workspace/m3_recon/`（scan 脚本 ×3 + 四仓树/license JSON + 四站 HTML）。管道 diff=0（本会话零改码）。
