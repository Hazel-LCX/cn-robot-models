# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> **已审 2026-10-24 · R24 结论：协议⑤执行回执终查通过——M4 含发布全流程闭环，四厂商五模型（Go2/G1/Lite3/X2/T1）全量在线，项目回维护态。回执数字全独立复测零出入：ref 四观测=6511dfa 逐位（本地/tracking/ls-remote/API 活源）、计数双路 55（rev-list+API Link=R23 预言 53+2 命中）、R13 专项闭合（远端含 R22 节无 R23 节，活源 blob 359911c 同物双证）、booster_t1 八件套在线、08ae1ba 恰 4 件纯台账+瑕疵①更正恰 1 行（74 行内容不动）、瑕疵②记档完毕。遗留常态：08ae1ba 下次随队（纯台账无需新审）、M4+ 候选动前协议②、无新增挂账。详见 REVIEW.md R24。**
> 上一次送审已于 2026-10-24 审毕：**R23 = 协议⑤通过——T1 硬数字全过硬，三决策点全批（S7 验收 ✓ / 基准缺失处置定案 / push 放行）**；R20 深度口径差观察项关闭。

【送审类型】**协议⑤执行回执**（R23 裁定 push 放行：首选 a 用户亲自、b 可接受需回执——用户令"继续"，按 **路径 b 工作台代推**执行，本回执如实在案，R20 路径 b 先例同款）——请审核台回写 R24 一行收尾，M4 至此闭环

【背景：在做什么】R23 读毕即执行 push（路径 b）。工作台实测回执验证（全程序化）：

- **三源逐位一致**：本地 HEAD = origin/main（fetch 后）= ls-remote（GitHub 实时）= `6511dfa94585124671b95d66c6e418bfe2104d45`；push 输出 `8195c20..6511dfa main -> main`，推前实测工作区仅审核台手迹 2 件（REVIEW.md R23 节 + 本件待覆写），push 本身不涉工作区；
- **远端 commit 总数 = 55**（`rev-list --count origin/main` 实测 = R23 预言 53+2 逐位命中）；
- **上线链 2 条逐条对上 R23 放行清单**：`9c3fab9` 协议②/S0（booster_assets 正本源修正 + BSD-3 定性 + S0 落档）→ `6511dfa` M4 S1–S7 全链（52 件三锚/基准/披露/台账随队）；
- **R13 专项 ✓**：远端 REVIEW.md grep `^## R22` 命中原节标题（`git show origin/main:REVIEW.md`）；另实测远端**无 R23 节**（grep `^## R23` = 0）——与计划一致：R23 节随本回执 commit 首次落库；
- **瑕疵①更正随队**：`models/booster_t1/reports/S1-manifest.sha256` 头注释 `unitree_go2`→`booster_t1`（R23 裁定"下个 commit 顺手更正"，随本回执 commit 落库；内容 74 行本就全对）；瑕疵②按裁定口径记档入 DEVLOG（算式正确分解 = manifest 74 = 5 根级 + T1 域 69 = 27+4+38）；
- **M4 全量上线**：github.com/Hazel-LCX/cn-robot-models 的 main 现含 `models/booster_t1/`（52 物理件三锚 + 模型页披露 5 节 + 五步报告）、`pipeline/configs/booster_t1.json`、s3 mass_kg=null 分支（N2 追认）、LICENSES/LICENSE/顶层 README 四厂商五模型口径——**五模型（Go2/G1/Lite3/X2/T1）全上线**；
- 本 leg `pipeline/` 零 diff（push+回执纯执行，manifest 头注释系 reports/ 件非 pipeline——N2 备案行不适用，如实声明）。

【决策点】确认回执 → 回写 **R24"协议⑤完成，M4 含发布全流程闭环"**。如无异议，M4 至此全部闭环（第五厂商入库+官方基准缺失首例处置定案+R20 观察项关闭），项目回维护态；M4+ 候选（云深处同仓多机型=维护态填充件随时可做/booster K1、T2 线）未被要求启动，动前先送协议②。

【我的倾向+理由】回执三源一致、上线链 2 条逐条对上 R23 放行清单、总数 55 与预言逐位命中、R13 专项闭合、瑕疵①已随手更正随队，无其他遗留项，倾向直接闭环。本件不枚举自身哈希（清单至 `6511dfa` + 本件随批，回执 rev-list 实测为准）。

【相关文件路径】
- 远端：github.com/Hazel-LCX/cn-robot-models（main @ `6511dfa`，55 commit）
- 本件、REVIEW.md（R23 节随本 commit 落库）、DEVLOG.md（回执记录+瑕疵②口径记档）、models/booster_t1/reports/S1-manifest.sha256（瑕疵①更正随队）
