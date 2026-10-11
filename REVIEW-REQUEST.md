# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-11 审毕：**R14 = M2 选型定案（Lite3）+ S0 license 关门 + A4 双路径全中升级**。

【送审类型】**协议⑤（M2 全量 push 公开仓库）**——M2 启动 + S1–S6 + S7 共 6 个本地 commit 一并上线申请 + S7 验收。

【背景：在做什么】M2（云深处 Lite3，异厂首录）全管道完成：S1 拉取（**blob-parity 门自动化首战拦截 CRLF 失真 → clone 后写 local config 根治**，15/15 正本）、S2 校验（10/0/0，第三种引用协议变体 `./meshes/` 兼容）、S3 体检（**10/1/1/1——本库首个 FAIL 级发现**：4×FOOT 零惯量占位，零修复披露 + 下游提示；两侧质量 17/17 全一致、vs 官网 12kg 仅 −0.5% 三模型最贴）、S4 入库（10 件/7.0MB 三锚全过，**异厂首战零人工干预**——K1/K2 教训自动化红利兑现）、S5 预览（**零改码首跑**：v4 config 驱动直接吃新 config，完整四足渲染）、S6 基准（47,966 steps/s，展幅 4.9%；同 DOF 异厂商差 2.2× 的 geom 复杂度注记）。S7 三件完成：`models/deeprobotics_lite3/README.md` 全文（披露链：①FAIL 四足端零惯量占位；②MJCF mesh 元素重复定义 13 引 4；③碰撞全基元厂商风格）、`LICENSES.md` 增 Lite3 行（N1 版权逐字）+ 商标补云深处、顶层 README 收录表/叙事/复现命令。

**数字速览（全部可重放）**：URDF 17 links/16 joints/12 revolute（↔ Go2 同 12 关节四足对照）；两侧网格 4/4 全同哈希；总量 11.938 kg vs 官网 12kg（−0.5%）；MJCF nbody=18 nmesh=13（重复定义虚胖如实披露）；包围盒 y [0.000, 0.298]；官网无关节级参数（限位对账无基准，如实记录）。

【决策点：需要拍板的具体选项】
1. **push 放行**：`main` 本地领先远端 **6 commit**（4107fed M2 启动/S0 → 9223c68 S1/S2 → 1787a47 S3 → 8486f0a S4/S5 → 9f235e6 S6 → 本件 S7 commit）。执行照旧：首选 a（用户亲自 push）；b（授权工作台）可接受（push 前贴 status + 后贴哈希回执）。push 后回执 → R15 一行收尾（M2 含发布闭环）。
2. **S7 验收**：Lite3 模型页披露链（首个 FAIL 级发现的处置是否达 M0 E1/M1 同等标准）、LICENSES/顶层 README 一致性。
3. **S3 FAIL 处置确认**：四足端零惯量占位按"零修复披露 + 下游提示"处置（改官方文件违反本库立场），S3 门按"有处置记录"放行——请裁定此处置是否成立，或需升级专项送审。

【我的倾向+理由】三项均按上述定案。理由：①M2 的工程目标（异厂泛化）全部达成且**管道零改码**（s1–s6 全参数化吃新 config、预览 v4 直接工作、blob-parity 门与三锚自动化首战零人工干预）——"加配置即加模型"从承诺变事实；②FAIL 级发现（零惯量占位）是质检价值的直接体现：正是"不静默、不修复、如实披露"立场的第一次实战检验；③同 DOF 步速差 2.2× 的 geom 复杂度发现进一步夯实"跨模型数字不可比"的叙事纪律。

【相关文件路径】
- 模型页：`models/deeprobotics_lite3/README.md`（S7 全文）· 顶层 `README.md`（M2 收录表）· `LICENSES.md`（Lite3 行）
- 报告：`models/deeprobotics_lite3/reports/`（S1-fetch / S2 / S3 含 forensics / S4 / S6 含对照注记）
- 预览：截图 `models/deeprobotics_lite3/images/preview-lite3-v4.png`；官网口径证据 `evidence/official-lite3-spec-page-screenshot-{1..4}.png`
- R14 行动项：`evidence/deeprobotics-support-page.html.txt`（A4 双路径）+ note 件留痕更正
