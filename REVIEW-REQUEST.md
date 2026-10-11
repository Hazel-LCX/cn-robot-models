# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审（S7 终审）已于 2026-10-11 审毕：**R5 = M0 有条件收官**（E1 过/干净环境实测过/门面过；F1 数字失真必修 + F2 轻残留），详见 REVIEW.md R5。

【送审类型】**终审 F1/F2 修复回报**（R5 收官条件：审核台复核 F1 数字一致即回写"M0 正式收官"，无需全量送审）

【背景：在做什么】按 R5 待修清单执行完毕：
- **F1 修复三件**：①`build_plan` 网格闭包按 dest 去重 + `assert` 防回归（URDF 17 处 visual 引用 → 7 个物理 dae，**引用行 ≠ 文件数**）；②体积/对账/冗余判定全改**物理文件口径**（冗余判定 17/0 → **7/0**）；③coverage 算式写平（`root_level` 改两段路径判定）：**raw 62 = 两仓库根级 8 + 目标子目录 54；54 = 入库 33 + meshes 冗余 7 + 排除 13，未覆盖 0**。
- **扩散 4 处更正**：S4-package.{md,json}（源头重跑刷新）、SOURCE.md §4、顶层 README 汇总表、模型页 Provenance 表——全部改为 **34 个物理文件（33 个 raw 溯源件 + 1 个质检截图）/ 56.2 MB（磁盘实测 56,186,xxx bytes ≈ 53.9 MiB）**。
- **F2**：s3_physics.py C1 模板中 png 提示文本移 config（`notes['upstream_png']`），S3 重跑 8/4/0/SKIP1 不变。
- 修复过程中额外抓到并修掉：S4 骨架每次重跑会覆盖 S7 全文模型页（改为**仅缺失时写** + git 历史恢复全文）；重跑 rm 误删质检截图（已恢复）。
- 自查三源对齐：脚本输出 = 磁盘 `find` = `git ls-files` = **54**（34 资产+截图 + 10 reports + 6 evidence + 4 根级文档）；正文文档 "43 文件/81.4" 残留清零（DEVLOG 历史条目与 REVIEW/REVIEW-REQUEST 审核原文按留痕纪律保留）。

【决策点：需要拍板的具体选项】复核 F1 终值数字一致——**入库物理文件 34（raw 溯源 33 + 质检自产 1）/ 资产 56.1 MB、目录全量 54 文件 56.2 MB**；冗余判定 **7/0**（物理文件口径）；coverage **62 = 8 + 54 = 33 + 7 + 13**——一致即按 R5 裁定回写"**M0 正式收官**"。用户已按收官流程直接复核本清单数字。

【我的倾向+理由】数字已三源对齐、算式闭合、残留清零，倾向回写收官。

【相关文件路径】
- models/unitree_go2/reports/S4-package.{md,json}（源头，重跑刷新）
- models/unitree_go2/SOURCE.md §4、README.md（顶层汇总表）、models/unitree_go2/README.md（Provenance 行）
- pipeline/s4_package.py（F1 主修 + 断言 + 骨架仅缺失时写）、pipeline/s3_physics.py（F2）
- DEVLOG.md（会话 10）
