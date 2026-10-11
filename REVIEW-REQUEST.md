# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-11 审毕：**R11 = 期中稽查**（K1 关闭/K2 立案/S1–S4 清算），K2 六步已完成（44754af）。

【送审类型】**协议⑤（M1 全量 push 公开仓库）**——S1–S6 + K2 共 7 个本地 commit 一并上线申请 + S7 验收。

【背景：在做什么】M1（宇树 G1 人形）全管道完成：S1 拉取（blob-parity 门）、S2 校验（10/0/0，含大小写核验）、S3 体检（7/5/0，torso−1.28kg 逐克闭环 + head_link.STL 网格证据链）、S4 入库（62 件/40.5MB 三锚全过，excluded 228 件逐件 why）、S5 预览（v4 config 驱动 + STL 支路，R10 五条件全落）、S6 基准（50,809 steps/s，展幅 2.3%）；K2（R11 立案）六步修复完毕并根治落码（s1 blob-parity 门 + s4 三锚 traceability，290/290 实测）。S7 收尾三件已完成：`models/unitree_g1/README.md` 全文（披露链：①官方 `g1_23dof.xml` 实为 29 hinge——两格式动作空间 23/29 维不可互换；②torso −1.28kg 与 head_link.STL 网格差异同根闭环；③官网 35kg 口径 evidence 5 件）、`LICENSES.md` 增 G1 两行 + 商标补 G1 + go2 过期状态行更正、顶层 README 增"G1 质检结果"表 + 叙事/商标/复现命令更新。

**数字速览（全部可重放）**：G1 = URDF 33 links/32 joints/23 revolute ↔ 官网 23 自由度精确自洽；总质量 URDF 34.134 / MJCF 34.137（差 0.003 kg）；MJCF nbody=31 nmesh=29；两侧网格 28/29 同哈希（唯一异哈希 = head_link.STL，与 S3 分歧同根）；包围盒顶 1.323 m ↔ 官网 1320 mm；Go2 回归 17 mesh 完整渲染（抬升 0.245/包围盒 0.334）。

【决策点：需要拍板的具体选项】
1. **push 放行**：`main` 本地领先远端 8 commit（22113d5 S1 → 407c0c5 S2 → 7fd618b S3 → edbfdc8 S4 → 44754af K2 → 3de2ffe S5 → 7ebd8bd S6 → 本件 S7 commit）。执行方式照旧：首选 a（用户亲自 `git push origin main`）；b（授权工作台）可接受（push 前贴 status 确认 + push 后贴哈希回执）。
2. **S7 验收**：模型页两套叙事（G1 披露链是否达到 M0 E1 同等披露标准）、LICENSES/顶层 README 一致性、K2 证据（blob-parity 门 + 三锚 290/290）随件复核。
3. **K2 六步完成确认**（R11 指定项逐项）：①raw 299 件归正 ✓（export 复验失配 0）②S4 重跑 manifest/报告刷新 ✓ ③S2/S3 回归全绿 ✓ ④根治落码 s1 门+s4 三锚 ✓ ⑤L9 记档 ✓ ⑥S1 报告 L48 划线更正 ✓。

【我的倾向+理由】三项均按上述定案。理由：①G1 全管道数字自洽且全部可重放，披露链（29-hinge 命名不符 + torso/head 网格证据）比 M0 的 calf 案例更深一层——官方文件名与内容不符是下游真金白银的坑；②K2 根治把正本性从"克隆卫生"升级为"程序化对账"，同型缺陷结构性挡死；③S5 v4 config 驱动后，M2+ 全管道（含预览）零改码路径已通——M1 的工程目标（验证管道普适性）达成。

【相关文件路径】
- 模型页：`models/unitree_g1/README.md`（S7 全文）· 顶层 `README.md`（G1 表 + 叙事）· `LICENSES.md`（G1 两行）
- 报告：`models/unitree_g1/reports/`（S1-fetch 含 K2 附更正 / S2 / S3 含 forensics / S4 含补记 / S6）
- K2 证据：`workspace/k1_fix/export_all_detected.py`（g1 归正 299/299）、s1 `verify_blob_parity`（290/290）、s4 三锚 traceability（62/62）、AGENT-LAB L9
- 预览：`pipeline/s5_preview/`（v4 + STLLoader 0.160.0）、截图 `models/unitree_g1/images/preview-g1-v4.png`、`models/unitree_go2/images/preview-v4-regression.png`
