# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R26 = 协议⑤通过——M20 硬数字全过硬，三决策点全批（S7 验收 ✓ / 质量分布分歧处置定案 / push 放行）**；口径小注（页头"revolute 16"系 12R+4C 合计展示标签）不阻塞。

【送审类型】**协议⑤执行回执**（R26 裁定 push 放行：首选 a 用户亲自、b 可接受需回执——用户令"继续"，按 **路径 b 工作台代推**执行，本回执如实在案，R20/R23 连续先例）——请审核台回写 R27 一行收尾，M5 至此闭环

【背景：在做什么】R26 读毕即执行 push（路径 b）。工作台实测回执验证（全程序化）：

- **三源逐位一致**：本地 HEAD = origin/main（fetch 后）= ls-remote（GitHub 实时）= `6603094546dafbf580700f133279d4c719aaca64`；push 输出 `6a1c02a..6603094 main -> main`，推前实测工作区仅审核台手迹 2 件（REVIEW.md R26 节 + 本件待覆写），push 本身不涉工作区；
- **远端 commit 总数 = 59**（`rev-list --count origin/main` 实测 = R26 预言 57+2 逐位命中）；
- **上线链 2 条逐条对上 R26 放行清单**：`4224e52` 协议②/S0（M20 选型+同仓 license 零漂移+S0 落档）→ `6603094` M5 S1–S7 全链（36 件三锚/官方基准恢复/质量分布分歧披露/continuous 三覆盖点落码/R25 台账随队）；
- **R13 专项 ✓**：远端 REVIEW.md grep `^## R25` 命中原节标题（=1）；另实测远端**无 R26 节**（=0）——与计划一致：R26 节随本回执 commit 首次落库；
- **M5 全量上线**：github.com/Hazel-LCX/cn-robot-models 的 main 现含 `models/deeprobotics_m20/`（36 物理件三锚+模型页披露 5 节+五步报告+官网规格页原件）、`pipeline/configs/deeprobotics_m20.json`、s3 COM 对账+continuous 纳入、preview.js 轮滑条 v9、LICENSES 复指行、Lite3 页转述注记（裁定③）、顶层 README M5 表——**六模型（Go2/G1/Lite3/X2/T1/M20）全量在线**；
- **R26 口径小注（revolute 16 展示标签）处置**：预览页 meta 行的"revolute 16"系 preview.js 滑条计数标签（12R+4C 合计），标注可细化不阻塞——按裁定留待下次 pipeline 改码窗口顺手细化（如审核台认为需立即改，回执注明即改）；
- 本 leg `pipeline/` 零 diff（push+回执纯执行——N2 备案行不适用，如实声明）。

【决策点】确认回执 → 回写 **R27"协议⑤完成，M5 含发布全流程闭环"**。如无异议，M5 至此全部闭环（同仓第二机型+continuous 拓扑首覆盖+质量分布分歧处置定案+官方基准恢复），项目回维护态；M5+ 候选（DR02 云深处人形=M5+ 替补/M20S、S10、M20_Piper、X30 各有档案与预警/booster K1、T2 线）未被要求启动，动前先送协议②。

【我的倾向+理由】回执三源一致、上线链 2 条逐条对上 R26 放行清单、总数 59 与预言逐位命中、R13 专项闭合、无其他遗留项，倾向直接闭环。本件不枚举自身哈希（清单至 `6603094` + 本件随批，回执 rev-list 实测为准）。

【相关文件路径】
- 远端：github.com/Hazel-LCX/cn-robot-models（main @ `6603094`，59 commit）
- 本件、REVIEW.md（R26 节随本 commit 落库）、DEVLOG.md（回执记录）
