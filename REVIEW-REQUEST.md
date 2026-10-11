# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。本文件由工作台写入，审毕留痕（历次送审全文可在 git 历史回溯）。
> 上一次送审（PIPELINE.md v0.2 轻复审）已于 2026-10-11 审毕：**R2 通过放行**，详见 REVIEW.md R2。

【送审类型】批量送审（C2 精神）：① **代码首审**（env_check.py，R1 ⑤ 后续送审点 2）＋ ② **协议② license 核对结论**（S0 门，R2-C3）

【背景：在做什么】用户修订工作模式（2026-10-11）：免复述确认、直接推进+讲解，审核点协议硬门不变。R2 放行后会话 A 完成：git init（main）+ .gitignore + requirements.txt + env_check.py + .venv 体检全绿（exit=0，mujoco 3.15.0 cp314 wheel 实测可装，py3.12 兜底作废），PIPELINE.md 已按 C1 升 v0.3 并打首个 commit。随即执行 S0 license 门：两仓库取证完毕，按 C3 触发协议②停手送审。

【决策点：需要拍板的具体选项】
1. **代码首审（立风格基线）**：env_check.py 的命名（snake_case 函数 + 元组表驱动）、注释密度（中文用途注释 + docstring 定位）、输出格式（人读表 + --json 机读）、退出码契约（0=无阻塞 / 1=有 FAIL）、四态语义（PASS/WARN/FAIL/SKIP，WARN=有兜底）是否作为本库基线。
2. **license 结论**：两仓库均 BSD-3-Clause（版权方 = 宇树本体 HangZhou YuShu Technology）；三条结论 允许再分发/允许修改/须保留声明 = 是/是/是；子目录独立声明检查完毕（go2_description/package.xml `<license>BSD</license>` 与仓库级一致；unitree_robots/go2/ 无独立声明随仓库级）；"二进制网格随仓库 license"假设是否放行。
3. **A4 官方性证据链**：路径① unitree.com 首页 HTML 含 github.com/unitreerobotics 链接；路径② org 自述 + blog=unitree.com + 两仓库 fork=false。双路径互证、API/HTML 实测留痕（2026-10-11），是否认可（验收原文写"截图"，本记录以实测输出为证据原件，截图可补）。
4. **放行 S1 拉取**：按固定锚点 unitree_ros@master `5994d4fa…a259`、unitree_mujoco@main `1eb6642e…ea0e7d` 拉取，raw 内同 commit 复核 license 快照（A2 闭环）。

【我的倾向+理由】倾向 1–3 确认、4 放行。理由：env_check.py 两轮实测闭环（base 探路定 venv → venv 全绿验证），退出码/三态语义有明确契约；license 三条结论逐条对应 BSD-3 原文条款且原文快照已入库；证据链双路径互证且均留痕；S1 锚点为实测 HEAD SHA，拉取后按 A2 复核闭环。

【相关文件路径】
- pipeline/env_check.py（代码首审对象；两轮体检输出见 DEVLOG 会话 2/3）
- models/unitree_go2/SOURCE.md（S0 全记录：来源/证据链/三条结论/子目录检查）
- models/unitree_go2/LICENSE-upstream-unitree_ros.txt、LICENSE-upstream-unitree_mujoco.txt（license 原文快照）
- LICENSES.md（双层索引首版）
- PIPELINE.md（v0.3）、DEVLOG.md（会话 3）、本文件
