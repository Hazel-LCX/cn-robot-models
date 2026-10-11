# REVIEW-REQUEST — 送审材料

> **已审 2026-10-11 · R8 结论：协议⑤ push 放行**——G1/G2/H1 清算全过（S4 头部分解=磁盘逐字节、coverage 每行平、json=56,119,567=真值、对账即事实入 v0.6）；R5 三项全过（含审核台独立 clone 5/5 哈希一致 + clone 内 MJCF 编译 OK）；公开内容快评无敏感。**执行方式：首选 a 用户亲自 push（GitHub 建空仓 + remote add + push -u origin main）；b 授权工作台可接受（status 确认+回执）**。push 后报回执，审核台追加 R9 收尾。详见 REVIEW.md R8。

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-11 审毕：**R6 = F1/F2 验收通过，M0 正式收官**（G1/G2 为 push 前必清脚注），随后 R7 增补 H1 与 push 前检查清单有效版，详见 REVIEW.md R6–R7。

【送审类型】**协议⑤：git push 公开仓库**——push 前检查清单（R7 版：R5 三项 + G1 + G2 + H1）已全部执行，请终查后放行

【背景：在做什么】R7 清单三项随一次 s4_package.py 重跑全清：
- **G1**：S4 报告头部体积口径注明分解——`总 56.1 MB（raw 溯源件 56,002,074 B + 质检自产件 117,493 B，G1 口径注明）`。
- **G2**：coverage 补桶写平——`robots/README.md` 归"根级及中间层"，目标子目录口径改完整前缀：**raw 62 = 根级及中间层 9 + 目标子目录 53；53 = 入库 33 + 排除 20（其中 meshes/ 冗余 7），未覆盖 0**。
- **H1**：重跑 S4 刷新对账——**total_bytes = 56,119,567 与磁盘 34 资产件之和逐字节一致（终验 True）**；README 两处（顶层汇总表 / 模型页 Provenance）同步 56.1 MB 口径；**"对账即事实"规则落 PIPELINE v0.6**（§3-S4：凡变更 models/ 下任何文件，必重跑 S4）。
- 过程失误两连（coverage 段短变量 NameError 被 grep 滤错线索、sed 写出占位符）已自纠并记 AGENT-LAB L6。

【决策点：需要拍板的具体选项】
1. **R5 三项终查**：①README 定稿状态——顶层与模型页数字均为终值口径（34 / 56.1 MB / 7-0 / 62=9+53）；②LICENSES/SOURCE 一致性——BSD-3 与双 commit 锚点（5994d4fa / 1eb6642e）在两文件均在案（grep 实证）；③.gitattributes 生效——换图后重 clone 抽查 5/5 + clone 内 MJCF 加载 OK。
2. **G1/G2/H1 清算确认**（证据在 S4-package.md 头部与 coverage 行、json total_bytes）。
3. **放行 git push 公开仓库**。**执行方式请一并裁定**：a) 用户自行执行 push（工作台不动 git remote）；b) 授权工作台执行（需提供 remote URL 与分支名，push 前我会再列一次 `git status` 干净确认 + push 后贴 commit 哈希回执）。
4. push 后收尾：回写 R8"协议⑤完成"，M0 全流程（含开源发布）闭环。

【我的倾向+理由】倾向 1–2 确认、3 放行（执行方式 b 优先）。理由：R7 三项全部落在 S4 一个报告内且算式逐行可验；数字三源对齐（脚本/磁盘/git ls-files）；预览页可交互演示（本地 8130 常驻），push 后任何评审者 clone 即得全套断网可用产物。

【相关文件路径】
- models/unitree_go2/reports/S4-package.{md,json}（G1 头部口径 / G2 coverage 行 / H1 total_bytes）
- README.md、models/unitree_go2/README.md（56.1 MB 终值口径）
- PIPELINE.md（v0.6，§3-S4 "对账即事实"规则）
- LICENSES.md、models/unitree_go2/SOURCE.md（一致性自查对象）
- AGENT-LAB.md（L6）、DEVLOG.md（会话 11）、本文件
