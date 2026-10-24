# DEVLOG — 滚动日志

> 纪律：每次会话结束追加一条，新的在上。

## 2026-10-24（会话 23：R20 放行执行——路径 b push + 回执三查全过 → 回执落档待 R21）

- 会话开始仪式：读 REVIEW.md（R20）+ DEVLOG（会话 22）+ 记忆专条 → 现场核对与交接一致：本地领先 4 commit（23c165d/6a5b300/bea1309/3dc950b）、审核台手迹 2 件在车上。远端实测未推（origin/main 仍 `9b20289`/47 commit）→ 上轮已给路径 b 选项，用户令"继续"，按 **路径 b（工作台代推）** 执行，R20 裁定 b 可接受需回执。
- **push 执行**：推前实测 `HEAD..origin/main` 为空（纯快进无分叉）、工作区仅审核台手迹 2 件（push 不涉工作区）→ `9b20289..3dc950b main -> main` 一次成功。
- **回执三查全过（全程序化）**：①三源逐位一致——本地 HEAD = fetch 后 origin/main = ls-remote = `3dc950b1363efdec0a84d32d61b14d84fb32def4`；②`rev-list --count origin/main` = **51**（47+4，R20 预言逐位命中——R19 期"50/47+3"口径疑云就此收口）；③R13 专项——远端 REVIEW.md grep `^## R19` 命中原节标题；另实测远端无 R20 节（grep `^## R20` 空，按计划随回执 commit 首次落库，口径自洽）。
- **回执落档**：REVIEW-REQUEST.md 覆写为协议⑤执行回执（M2 会话 18 五段先例，路径 b 如实在案、不枚举自身哈希），同 commit 带上工作区未提交的 REVIEW.md R20 节 + DEVLOG 本条；**回执 commit 不 push**，等审核台 R21 闭环一行后收尾 push（R9/R13/R16 先例）。
- 本会话 `pipeline/` 零 diff（push+回执纯执行，无改码——N2 备案行不适用，如实声明）。
- 状态：**M3 四模型全量上线、回执已落档 → 停手等审核台 R21**；R21 回写后收尾 push，M3 全闭环项目回维护态（M4 候选未被要求启动，动前先送协议②）。
- **R21 读毕 → M3 正式闭环收尾**：审核台四路活证终查零出入（ref 四观测一致 `3dc950b`、计数双路 51、R13 专项双路等证、上线抽查 X2 八件套在线 + v4 缺陷图远端绝迹、回执 commit 恰 3 件纯台账零改码属实）→ **R21 = 协议⑤完成，M3 含发布全流程闭环**。R21 本节 + 标注随本收官 commit 与回执 commit `8bcdd00` 一并 push（M2 `9b20289` 先例，纯台账无需新审）——commit 前 grep 自证 R21/R20 节随队，push 后按例三源复核。M3 全周期五审闭环（R17 选型→R18 决策点退回→R19 暂缓→R20 放行→R21 终查），四模型（Go2/G1/Lite3/X2）全量在线；项目回维护态：深度口径差观察项随下次 S5 注明测量法，M4 候选（加速进化 booster_gym NOASSERTION 人工定性/云深处同仓多机型）动前先送协议②。
- **M4 启动（同会话续）→ 协议②送审**：用户令"继续"，按 M3 会话 19 先例两候选线全程序化侦察（`workspace/m4_recon/`，不入库）。**侦察修正核心成果**：M3 时代"加速进化=跨仓配对"预设三步被修——booster_train 零 T1 资产、booster_gym resources/T1 单仓配对但 license 为 916 B 短格式 Apache-2.0（NOASSERTION 真身，blob `c9e19b34` 零漂移）且 44 STL 池 20 件无引用、**专用资产仓 `booster_assets` 形态最优**（BSD-3 全文 1,502 B、K1/T1/T2 三线、官方 DoF 配置表、活跃维护）——M4 正本源改锚 `booster_assets`，gym 降旁证；历史口径修正如实记录（M3 曾记"T2/K1 等其余 10 URDF 无 MJCF"，实测 10 urdf+11 xml 仅 T1_29dof 无配对）。候选 B 云深处六机型全扫（DR02/M20/M20S/M20_Piper/S10/X30，X30 网格 8 件异常薄预警），license 零漂移（快照 blob `cdc6c065`=上游现值）——留 M4+ 维护态填充。**源修正纪律**：gym 版 S0 取证件撤 `archive_gym_s0/`，证据链不混用两正本（L12 教训）。**S0 落档**（`gen_t1_s0_v2.py`）：`models/booster_t1/` = SOURCE.md（状态=待审）+ `LICENSE-upstream-booster_assets.txt`（1,502 B，blob `d7a14af35ecb…` hash-object MATCH）+ evidence ×6；锚点推荐 `T1_23dof.urdf↔T1_23dof.xml`（官方配置表背书 2+8+1+12=23 算术自洽，M1 g1_23dof 同款形态）；A4 分层如实（路径②成立四件互证/路径①阴性=官网首页+T2 页双零 JS 站）。
- 本会话 `pipeline/` 零 diff（截至 M4-S0 全 leg 纯取证，push/回执/侦察/S0 无改码；**S1–S7 leg 的 2 处 N2 备案见下条**）。
- **R22 读毕（协议②全批、S1 放行）→ M4 S1–S7 全链完成 → 协议⑤送审**：①SOURCE.md"待裁"→"已裁"顺手更正（R22 裁定 2）；②**S1 拉取**：config 程序化生成（pin 从 evidence 注入；s2 补 package/package_root 两键），直连一次命中 pin `12a97516` 零漂移（R22 预警③闭合）、69 文件/15.9 MB、blob-parity 69 件失配 0（K2 门三战全绿）、A2 license MATCH；**R22 预警①②闭合**：URDF/MJCF scale 属性各 0 处（grep 实测）、引用风格 `meshes/` 前缀（G1 同族第五形态）、网格闭包 25/25 零缺失、38 件未收 STL 身份自洽（踝并联/手部/29dof 臂加长 2+14+1+12=29）；③**S2 校验 10/0/0**：URDF 25 link/24 joint（yourdfpy 规范化 world+floating 口径在案）、MJCF nbody=26/njnt=24/nq=30/nu=23 逐数自洽；④**S3 体检 7/5/0/SKIP1**：**官方整机基准缺失=本库首例**（官网无 T1 页+三官方仓 README 无质量字段穷尽实测）——s3 新增 mass_kg=null WARN 分支（官方基准缺失跳过对比不虚构，总量 31.738/31.740 kg 仅记录）、两侧逐 body 23/23 一致、23 轴差 0、trunk −0.0016 kg 约定差容差内、URDF 碰撞全基元（box5/cylinder14/sphere1）披露；⑤**S4 入库**：52 物理件/17.4 MB 三锚全过（SHA256+hash-object@pin）、唯一源 27+excluded 4、38 未收网格逐件列名算式平账、recheck 双侧通过；⑥**S5 预览零改码**（v4 config 驱动吃下第五模型，preview.js/index.html 零 diff）：T1 包围盒 y [0.000, 1.180]、落地 0.687、断网自检 33 资源全本机外网 0、23 滑条、截图 `preview-booster_t1-v1.png` 存档（画面判读合格：零位双臂平展/头部双关节+相机座/整机闭合无幽灵）；**四模型基线逐位回归** go2 0.334/g1 1.323/lite3 0.298/x2 1.319 全命中；**R20 挂账执行**：bbox 测量法注明落模型页披露 5（three.js Box3 逐 mesh AABB 并集口径，页 y=1.180 与 yourdfpy scene.bounds z=1.180 逐位同值互证）；⑦**S6 基准**：36,766 steps/s（27.2 µs/step，加载 51.6 ms，展幅 15.9% 稳过）——五模型序列第五点；⑧**S7 报告**：模型页全文（披露 5 节：官方基准缺失居首）、LICENSES.md 加 booster_t1 行+商标补 Booster、LICENSE 第三方层补 BoosterRobotics/Booster 商标、顶层 README 收录行/披露索引/M4 表/预览链接/商标行。
- **N2 改码备案（S1–S7 leg，pipeline/ diff 1 文件 2 处，均通用改动零模型特异）**：①s3_physics.py `check_mass_total` 增 mass_kg=null 分支（动因=T1 官方整机基准缺失：官网无该机型页+三官方仓 README 无质量字段穷尽实测；官方基准缺失不得虚构——R17 检查点同源；未来无官网基准模型受益）；②s3_physics.py main 尾部 caliber 拼接改 `.get()` 兜底（动因=①的伴生：official 段无 evidence/caliber 键时崩溃）。**协议③红线核对：零物理参数修改（纯体检+披露），改码为体检口径的"缺失处置"非参数改动。**
- 状态：**M4 S1–S7 全链完成 → 协议⑤送审**（REVIEW-REQUEST.md：push 放行 + S7 验收 + 官方基准缺失处置确认三决策点），停手等审核台；本地 commit 未 push（领先 2=9c3fab9 协议②+本件）。
- **R23 读毕（三决策点全批、S7 验收过、R20 观察项关闭、N2 追认、push 放行）→ 路径 b push + 回执落档**：①push `8195c20..6511dfa main -> main`（用户令"继续"，R23 首选 a 但 b 可接受需回执——R20 路径 b 先例同款，本回执如实在案）；②**R24 前置三查全过（全程序化）**：三源逐位一致（本地 HEAD=fetch 后 origin/main=ls-remote=`6511dfa94585124671b95d66c6e418bfe2104d45`）、`rev-list --count`=**55**（53+2，R23 预言逐位命中）、R13 专项过（远端 REVIEW.md 含 R22 节；远端无 R23 节=按计划随回执 commit 首次落库，口径自洽）；③**瑕疵两笔处置**：①manifest 头注释模板残留 `unitree_go2`→`booster_t1` 随本回执 commit 更正（R23 裁定"下个 commit 顺手改"，内容 74 行本就全对）；②送审件算式书写歧义口径记档——正确分解 = manifest 74 = 5 根级 + T1 域 69 = 27 唯一源 + 4 排除 + 38 未收（数字全对、等式写法不成立，R23 判非载荷）；④回执落档：REVIEW-REQUEST.md 覆写为协议⑤执行回执（M2 会话 18 五段先例，路径 b 在案、不枚举自身哈希），同 commit 带上 REVIEW.md R23 节 + DEVLOG 本条 + manifest 更正；**回执 commit 不 push**，等审核台 R24 闭环一行后收尾 push（R9/R13/R16/R21 先例）。
- 本 leg `pipeline/` 零 diff（push+回执纯执行——N2 备案行不适用，如实声明）。
- 状态：**M4 五模型全量上线、回执已落档 → 停手等审核台 R24**；R24 回写后收尾 push，M4 全闭环项目回维护态（M4+ 候选：云深处多机型填充件/booster K1、T2 线，动前先送协议②）。
- **R24 读毕 → M4 正式闭环收尾**：审核台四路活证终查零出入（ref 四观测一致 `6511dfa`、计数双路 55=R23 预言命中、R13 专项双路等证含"远端无 R23 节=计划一致"、booster_t1 八件套在线、回执 commit 恰 4 件纯台账+瑕疵①更正恰 1 行复核）→ **R24 = 协议⑤完成，M4 含发布全流程闭环，四厂商五模型全量在线**。R24 本节 + 标注随本收官 commit 与回执 commit `08ae1ba` 一并 push（M2 `9b20289`/M3 R21 先例连续第三次，纯台账无需新审）——commit 前 grep 自证 R24/R23 节随队，push 后按例三源复核。**M4 三审一次过闭环（R22 协议② → R23 全链 → R24 终查）**，本库里程碑：四厂商五模型（Go2/G1/Lite3/X2/T1）全量在线、"官方基准缺失不虚构"先例与"跨仓配对预设修正"侦察方法论入库；项目回维护态：无新增挂账（R20 观察项已闭），M4+ 候选（云深处六机型，X30 预警在档）动前先送协议②。
- **跨 leg 续航令（用户立规）→ M5 启动（同会话续）→ 协议②送审**：用户令"以后这个任务只要没到审核点就直接继续"——leg 闭环/审核台回写后不再等待，续航令落记忆（项目专条+索引）。M4 收官即按 R24 点名方向启动 **M5（第六个模型）**：M4 侦察已扫全仓六机型，本会话定向补扫（`workspace/m5_recon/`：fresh HEAD `530e01a5` 树 422 件 + 根 README + 逐机型配对/引用/关节程序化汇总）。**六机型事实**：M20/M20S/S10 同构 1+1（12R+4**continuous**+3-4F，`./meshes/` 前缀，scale 0）；M20_Piper 复合体（+Piper 臂，2 prismatic）；DR02 双配置 3 urdf（Pro/Standard，31R+8F，114 mesh 池）；**X30 薄网格 13 引→4 唯一+5 处 scale 属性**（L12 雷区预警）；上游 README 自述 Lite3 thigh COM URDF/MJCF 有差（如实转述备案 SOURCE.md §4，M2 对账范围外不动已闭环记录）。**推荐定案：M5=云深处 M20（轮足四足）**——管道首个 continuous 关节拓扑（S2/S5/S6 三处真实新覆盖点）、1+1 干净配对 47 件、scale 0、同厂官网基准 S3 前置大概率恢复（T1 缺失能力）；DR02=M5+ 替补。**S0 落档**（`gen_m20_s0.py`）：`models/deeprobotics_m20/` = SOURCE.md（状态=待审）+ license 快照（1,502 B，blob `cdc6c065` hash-object MATCH + **与 M2 快照逐字节同物断言**——同仓单 license 零漂移无新考题）+ evidence ×4；A4 链条继承 M2 双路径全中。
- 本会话 `pipeline/` 零 diff（M5 侦察+S0 纯取证，无改码——N2 备案行不适用，如实声明）。
- 状态：**协议②已触发（M5 选型=云深处 M20 + 锚点与不入库清单 + 同仓 license 零漂移确认 + A4 继承确认，四决策点）**，停手等审核台；本地 commit 未 push（push 属协议⑤，随 M5 协议⑤窗口同队）。
- **R25 读毕（四决策点全批、S1 放行、COM 处置三件套裁定）→ M5 S1–S7 全链完成 → 协议⑤送审**：①**S1 拉取**：config 程序化生成，直连一次命中 pin `530e01a5` 零漂移（预警②闭合）、41 文件/41.1 MB、blob-parity 41 件失配 0（K2 门四战全绿）、A2 MATCH；**网格按格式分目录实测修正**（urdf/meshes 17+mjcf/meshes 17，非共享池——config mjcf_assets 随改）；17 引=17 唯一闭包零缺失、scale 0（预警③闭合）、usd/ 5 件 excluded（Lite3 先例）；②**S2 校验 10/0/0**：21 link/20 joint（12R+4C+4F），MJCF nbody=18/njnt=17/nq=23/nu=16 逐数自洽——**continuous↔unlimited hinge 映射定案（预警①覆盖点 1/2）**；③**S3 前置侦察**：官网 M20 产品页静态可提取（deeprobotics.cn/products/detail/1.html，curl 带浏览器 UA 过 CDN 520），**官方基准恢复**——整机重量含电池约 35 kg 回填 config（evidence 原件 160,864 B 落档）；④**S3 体检 10/3/0/SKIP1**：两侧总量 34.491/34.526 kg vs 官网 35（−1.5%/−1.4% 容差内 PASS）；**核心发现=hipy/knee 质量分布两格式分歧 ×四腿**（URDF 2.4930/1.2600 vs MJCF 2.6180/1.1450，每腿合计 −0.01 与总量差自洽）——上游格式间质量重分配，零修复披露；**R25 裁定②落码：cross:com-per-body 逐 body COM 对账（记录级）——17/17 全一致最大差 4.99e-07**（质量分歧而 COM 逐位一致=同仓 Lite3 COM 注记的互补模式）；cross:joint-names WARN 实证检查脚本 continuous 盲区→通用修（continuous 纳入对账集合）后 16↔16 全 PASS（预警①覆盖点 3）；⑤**回归纪律**：s3 改码后重跑三存量模型 S3 确认结论与已闭环记录一致（Lite3 的 1 FAIL=M2 立案足端零惯量非回归），**误覆写的三份已审计 S3 报告文件（.md+.json）即回滚**——已闭环模型记录字节态零触碰；⑥**S4 入库**：36 物理件/23.9 MB 三锚全过、FAIL 0/WARN 0（算式最净：45=4 根级+41 子目录=36 唯一源+5 usd 排除，分目录闭包精确全收零未收）、recheck 双侧通过；⑦**S5 预览**：初载实测 12 滑条（4 轮关节缺失）——**preview.js continuous 滑条落码**（±π 语义，预警①覆盖点 S5 侧）+index.html v9；重载 16 滑条全齐、包围盒 y [0.000, 0.675]、断网 25 资源 0 外网、截图 `preview-deeprobotics_m20-v1.png` 存档（画面判读：轮足四足四腿带轮整机闭合无幽灵）；**五模型基线逐位回归** go2 0.334/g1 1.323/lite3 0.298/x2 1.319/t1 1.180 全命中；⑧**S6 基准**：43,867 steps/s（22.8 µs/step，加载 62.3 ms，展幅 12.0% 稳过）——六模型序列第四点；⑨**S7 报告**：M20 模型页全文（披露 5 节：质量分布分歧居首+COM 互补模式）、LICENSES.md 加 deeprobotics_m20 复指行、**R25 裁定③执行：Lite3 模型页披露区补转述注记（### 4，不动 M2 质检本体）**、顶层 README 收录行/披露索引/M5 表/预览链接。
- **N2 改码备案（S1–S7 leg，pipeline/ diff 3 文件 6 处，均通用改动零模型特异）**：①s3_physics.py parse_urdf 增 COM 原点解析（动因=R25 裁定②载体）；②s3_physics.py check_cross 增 cross:com-per-body 逐 body COM 对账（记录级 WARN 非 FAIL 门，动因=上游 OEM 格式差异先例 + M20 实证质量/COM 分离模式，未来模型受益）；③s3_physics.py check_cross urdf_rev 纳入 continuous（动因=M20 实证检查脚本 continuous 盲区，R25 预警①落码）；④s3_physics.py joint-names 显示口径改"单自由度活动关节"（③伴生）；⑤preview.js 滑条 filter 纳入 continuous（±π 默认域既有 fallback 承接，动因=4 轮关节不可交互）；⑥index.html 缓存 v8→v9（⑤的缓存击穿，既定手法）。**协议③红线核对：零物理参数修改（纯体检+披露）。**
- 状态：**M5 S1–S7 全链完成 → 协议⑤送审**（REVIEW-REQUEST.md：push 放行 + S7 验收 + 质量分布分歧处置确认三决策点），停手等审核台；本地 commit 未 push（领先 2=4224e52 协议②+本件）。
- **R26 读毕（三决策点全批、质量分布分歧处置定案、push 放行）→ 路径 b push + 回执落档**：①push `6a1c02a..6603094 main -> main`（用户令"继续"，R26 首选 a 但 b 可接受需回执——R20/R23 连续先例，本回执如实在案）；②**R27 前置三查全过（全程序化）**：三源逐位一致（本地 HEAD=fetch 后 origin/main=ls-remote=`6603094546dafbf580700f133279d4c719aaca64`）、`rev-list --count`=**59**（57+2，R26 预言逐位命中）、R13 专项过（远端 REVIEW.md 含 R25 节；远端无 R26 节=按计划随回执 commit 首次落库，口径自洽）；③**口径小注处置**：页头"revolute 16"系 preview.js 滑条计数标签（12R+4C 合计），按裁定"可细化不阻塞"留待下次 pipeline 改码窗口顺手细化，回执已声明；④回执落档：REVIEW-REQUEST.md 覆写为协议⑤执行回执（五段先例，路径 b 在案、不枚举自身哈希），同 commit 带上 REVIEW.md R26 节 + DEVLOG 本条；**回执 commit 不 push**，等审核台 R27 闭环一行后收尾 push（R9/R13/R16/R21/R24 先例连续第五次）。
- 本 leg `pipeline/` 零 diff（push+回执纯执行——N2 备案行不适用，如实声明）。
- 状态：**M5 六模型全量上线、回执已落档 → 停手等审核台 R27**；R27 回写后收尾 push，M5 全闭环项目回维护态（M5+ 候选：DR02 云深处人形=M5+ 替补/M20S、S10、M20_Piper、X30/booster K1、T2 线，动前先送协议②）。
- **R27 读毕 → M5 正式闭环收尾**：审核台四路活证终查零出入（ref 四观测一致 `6603094`、计数双路 59=R26 预言命中、R13 专项双路等证、M20 八件套在线、回执 commit 恰 3 件纯台账、口径小注处置一致确认）→ **R27 = 协议⑤完成，M5 含发布全流程闭环，三厂商六模型全量在线**。R27 本节 + 标注随本收官 commit 与回执 commit `92c0dc9` 一并 push（先例连续第四次，纯台账无需新审）——commit 前 grep 自证 R27/R26 节随队，push 后按例三源复核。**M5 两审+终查一次过闭环（R25 协议② → R26 全链 → R27 终查）**，本库现状：三厂商六模型全量在线，管道已消化六种关节拓扑与四种引用形态，"官方基准恢复+质量分布分歧互补模式"两件质检叙事资产上线公开；项目回维护态：口径小注（revolute 16 标签）随下次 pipeline 窗口细化，M6+ 候选（DR02=云深处人形官网实证=M5+ 替补/X30/M20_Piper）动前先送协议②。
- **M6 启动（续航令第二个自动推进里程碑）→ 协议②送审**：M5 收官即按 R27 点名方向启动 **M6（第七个模型）**。定向侦察（`workspace/m6_recon/`）：**DR02 双配置官方算术逐位闭合**——官网规格页（detail/5.html，静态 HTML 150,548 B 原件落档）逐部位 DoF 分解：Pro 31=单臂 7×2+单腿 6×2+腰 3+头 2 ✓↔ DR02-pro.urdf 31R↔DR02_pro.xml 31 关节（78 kg 含电池）；Standard 21=臂 4×2+腿 6×2+腰 1 ✓↔ DR02-std.urdf 21R↔DR02_std.xml（68 kg）——**选型证据历次最强**（超越 T1 README 表与 X2 推断式）；站立 1800×558×400 mm（1.8 m 级库内最高、云深处首个人形、库内第 4 个人形机型）；Pro 细节=40 link/31R+8F、39 引→34 唯一 `./meshes/` 前缀、scale 0、MJCF 31 关节自洽；fix_joints=锁死变体（21R+18F）不入库、Standard 平替；网格 114 件分目录（M20 同款）。**S0 落档**（`gen_dr02_s0.py`）：`models/deeprobotics_dr02/` = SOURCE.md（状态=待审）+ license 快照（1,502 B，blob `cdc6c065` MATCH+与 M2/M5 同物断言——同仓第三机型零漂移无新考题）+ evidence ×4（含官网规格页原件）。A4 继承 M2/M5 双路径全中；S3 双基准可得（质量 78 kg+DoF 分项）。
- 本会话 `pipeline/` 零 diff（M6 侦察+S0 纯取证，无改码——N2 备案行不适用，如实声明）。
- 状态：**协议②已触发（M6 选型=云深处 DR02 Pro + 锚点与不入库清单 + 同仓 license 零漂移确认 + A4 继承确认，四决策点）**，停手等审核台；本地 commit 未 push（push 属协议⑤，随 M6 协议⑤窗口同队）。
- **R28 读毕（四决策点全批、S1 放行、轻度口径处置令）→ M6 S1–S7 全链完成 → 协议⑤送审**：①**S1 拉取**：config 程序化生成，pin `530e01a5` 零漂移（预警④闭合）、129 文件/151.7 MB、blob-parity 129 件失配 0（K2 门五战全绿）、A2 MATCH；**网格 114=36+22+34+22 逐位**（R28 口径复现）、池外 2 件身份=wrist simplified（预警②闭合）、scale 双侧 0（预警⑤闭合）；**轻度口径处置**：规格页重取二进制原件（curl 字节 148,398 B 逐位=R28 活源口径）+ **sessionId 令牌脱敏**（40 位→占位符，−1 B，令牌零残留断言过）——敏感信息红线优先；usd 10 件未收（锚点范围）走 coverage 平账；②**S2 校验 10/0/0**：40 link/39 joint、MJCF nbody=41/njnt=32/nq=38/nu=31 逐数自洽；③**口径钉案（数字可重放）**：S1 正则"39 引"vs S2 lxml"36 处有效引用"——**差 3 处系 URDF 注释块内禁用 mesh**（head_link/ankle_x），lxml 两法（直系路径+iter）互证 36 为权威，唯一集 34 不变、池外身份不变；S1 正则口径如实更正（模型页披露 1=L12 家族活案例）；④**S3 体检 10/3/0/0 SKIP（历次最净）**：两侧总量 **78.085 vs 官网 78 kg（+0.1% 历次最贴）且 URDF/MJCF 同值**；逐 body **34/34 完全一致**（无 M20 式分歧）+ **COM 34/34 差 0.00e+00**；31 轴差 0；**官方 DoF 基准齐备**（本库首个：官网 31 分解↔URDF 31R 逐位）；collision 含 2 处 mesh 碰撞（本库首见，复用 visual 文件）；预警③闭合（78±10% 容差口径 config 在案）；⑤**S4 入库**：70 物理件/59.8 MB 三锚全过、FAIL 0/WARN 1（平账 129=70 唯一源+3 excluded+56 未收：Standard 网格 44+池外 2+usd 10 逐件列名）、recheck 双侧通过；⑥**S5 预览**：humanoid 机位 31 滑条、**包围盒 y [0.000, 1.792] ↔ 官网站立 1800 mm（−8 mm 零位/标称姿态差=人形首个身高官方对账点）**、断网 42 资源 0 外网、截图 `preview-deeprobotics_dr02-v1.png` 存档（画面判读：人形整机闭合双臂弯手张零位、无幽灵）；**六模型基线逐位回归** go2 0.334/g1 1.323/lite3 0.298/x2 1.319/t1 1.180/m20 0.675 全命中；⑦**S6 基准**：**110,257 steps/s（9.1 µs/step）超越 Go2 成七模型序列最快**（41 body 全基元碰撞：几何简单度主导步速，"跨模型不可比"再加固）、加载 153.8 ms、展幅 3.4% 稳过；⑧**S7 报告**：DR02 模型页全文（披露 5 节：口径更正居首+collision-mesh 首见+身高对账口径+sessionId 脱敏）、LICENSES.md 加 deeprobotics_dr02 复指行、顶层 README 收录行/披露索引/M6 表/预览链接。
- 本会话（M6 leg）`pipeline/` 零 diff（侦察/S0/拉取/入库/预览/基准/报告全程无改码——M5 的 COM/continuous 通用能力直接覆盖 DR02，N2 备案行不适用，如实声明）。
- 状态：**M6 S1–S7 全链完成 → 协议⑤送审**（REVIEW-REQUEST.md：push 放行 + S7 验收 + 口径更正与 sessionId 脱敏处置确认三决策点），停手等审核台；本地 commit 未 push（领先 2=fc1b956 协议②+本件）。
- **R29 读毕（三决策点全批、口径更正+脱敏处置双确认、push 放行）→ 路径 b push + 回执落档**：①push `24461b8..d3fd2ac main -> main`（用户令"继续"，R29 首选 a 但 b 可接受需回执——R20/R23/R26 连续先例，本回执如实在案）；②**R30 前置三查全过（全程序化）**：三源逐位一致（本地 HEAD=fetch 后 origin/main=ls-remote=`d3fd2accb8a85efecf3f6417da62f05414062b4b`）、`rev-list --count`=**63**（61+2，R29 预言逐位命中）、R13 专项过（远端 REVIEW.md 含 R28 节；远端无 R29 节=按计划随回执 commit 首次落库，口径自洽）——**七模型全量上线**；③**R29 两项新规随记（流程口径无改码）**：正则计数仅作线索/解析器计数为断言依据入规程（审核台自省+工作台同款口径更正双源合一）；脱敏四要件立为 evidence 网页取证标准范式；④回执落档：REVIEW-REQUEST.md 覆写为协议⑤执行回执（五段先例，路径 b 在案、不枚举自身哈希），同 commit 带上 REVIEW.md R29 节 + DEVLOG 本条；**回执 commit 不 push**，等审核台 R30 闭环一行后收尾 push（R9/R13/R16/R21/R24/R27 先例连续第六次）。
- 本 leg `pipeline/` 零 diff（push+回执纯执行——N2 备案行不适用，如实声明）。
- 状态：**M6 七模型全量上线、回执已落档 → 停手等审核台 R30**；R30 回写后收尾 push，M6 全闭环项目回维护态（M7+ 候选：Standard 平替整组/booster K1、T2 跨仓/X30、M20_Piper/M20S、S10 档案，动前先送协议②）。
- **R30 读毕 → M6 正式闭环收尾**：审核台四路活证终查零出入（ref 四观测一致 `d3fd2ac`、计数双路 63=R29 预言命中、R13 专项双路等证、DR02 八件套在线、回执 commit 恰 3 件纯台账）→ **R30 = 协议⑤完成，M6 含发布全流程闭环，四厂商七模型全量在线**。R30 本节 + 标注随本收官 commit 与回执 commit `3eb7e0a` 一并 push（先例连续第五次，纯台账无需新审）——commit 前 grep 自证 R30/R29 节随队，push 后按例三源复核。**M6 两审+终查一次过闭环（R28 协议② → R29 全链 → R30 终查）**，**库里程碑：四厂商七模型全量在线**——宇树（Go2/G1）、云深处（Lite3/M20/DR02 三机型）、智元（X2）、加速进化（T1），四足/轮足/人形三形态全覆盖、1.8m~0.3m 尺度带、六种关节拓扑；M6 单轮四件叙事资产（S3 史上最净/官方 DoF 基准首个/身高官方对账/collision-mesh 首见）+ 双台互纠正面闭环（正则→解析器口径规程）；项目回维护态：无新增挂账，M7+ 候选池（booster K1/T2 跨仓=协议②侦察起步/同仓 Standard、X30、Piper 等预警在档）动前先送协议②，revolute 16 标签随下次 pipeline 窗口。
- **M7 启动（续航令第三个自动推进里程碑）→ 协议②送审**：M6 收官即按 R30 候选池首选启动 **M7（第八个模型）=加速进化 K1**。定向侦察（`workspace/m7_recon/`）：①head 与 M4 锚 `12a97516` 零漂移（M4 S1 后上游未动）；②配对 `K1_22dof.urdf`（26 link/22R+2F+floating，32 引 `meshes/` 前缀→24 唯一，scale 0）↔ `K1_22dof.xml`（meshdir，24=24）自洽；变体 2 件（locomotion 裁剪 12R+10F/parallel 并联踝）先例处置不入库；网格 52 件单池；③**A4 重大升级（核心侦察成果）**：M4"官网无 K1 页、现主打 T2"被当前官网推翻——首页 meta 明列 "Booster K1、T2"且 `/cn/booster-k1` 产品页完整实存（336,389 B 二进制原件落 evidence，R29 取证范式零 token 无需脱敏），**K1 升级为本库首个官网产品页直证机型**（M4 快照与当前页不同：官网改版或采样偏差，如实记录 SOURCE.md §2）；④官方规格：身高约 95cm/重量约 19.5kg/**全身 22=头 2+双臂 8+双腿 12**——官网页与 assets README 配置表与 URDF 22R 三方逐位（DR02 之后第二强选型证据）；⑤本库最小型机型（0.95m 档，与 DR02 1.79m 构成尺度带两极），S3 双基准（质量+DoF）可得。**S0 落档**（`gen_k1_s0.py`）：`models/booster_k1/` = SOURCE.md（状态=待审）+ license 快照（1,502 B，blob `d7a14af35ecb…` MATCH+与 M4 快照同物断言——同仓第二机型线零漂移无新考题）+ evidence ×6（含 K1 产品页二进制原件）。license/A4/引用协议全链条继承 M4。
- 本会话（M7 leg）`pipeline/` 零 diff（侦察+S0 纯取证，无改码——N2 备案行不适用，如实声明）。
- 状态：**协议②已触发（M7 选型=加速进化 K1 + 锚点与不入库清单 + 同仓 license 零漂移确认 + A4 升级确认，四决策点）**，停手等审核台；本地 commit 未 push（push 属协议⑤，随 M7 协议⑤窗口同队）。
- **R31 读毕（四决策点全批、S1 放行、域名迁移补记令）→ M7 S1–S7 全链完成 → 协议⑤送审**：①**SOURCE §2 补域名迁移**（boosterobotics.com 301→booster.tech，R31 裁定①执行）+ config 程序化生成；②**S1 拉取**：pin `12a97516` 零漂移（预警④闭合）、56 文件/21.7 MB、blob-parity 56 件失配 0（K2 门六战全绿）、A2 MATCH；32 引→24 唯一（预警①：8 处复用）、单池 52 件闭包 28 未收身份自洽（踝并联 Ball×18+Crank/Link×8=parallel 配套/Foot_Collision/Foot_old/Head_2_Collision/ZED）；scale 双侧 0；③**口径钉案（R29 规程第二次实战）**：预警② floating+world——**K1 的 world link+world_joint（floating）整块在 XML 注释内**（上游注释掉的挂载，与 T1 活元素相反）：grep 字面 26 link/25 joint（含 floating）vs lxml 权威 **25 link/24 joint（22R+2F，无 floating 无 world）**，yourdfpy/MuJoCo 行为与解析器一致；R31 沿用的侦察数字即 grep 口径，如实更正；④**S2 校验 10/0/0**：nbody=26/njnt=23/nq=29/nu=22 逐数自洽；⑤**S3 体检 10/3/0/0（连续第二最净档）**：两侧总量 **19.666 vs 官网 19.5 kg（+0.9%）同值**、逐 body 23/23 一致、COM 23/23 差 0、22 轴差 0、**官方 DoF 三方逐位**（官网+README+URDF）；collision **mesh 8 处**（本库第二例，DR02 之后）；⑥**S4 入库**：50 物理件/24.0 MB 三锚全过、FAIL 0/WARN 1（平账 56=26+2+28 逐件列名）、recheck 双侧通过；⑦**S5 预览**：humanoid 机位 22 滑条、**包围盒 y [0.000, 0.955] ↔ 官网"身高约 95 厘米"逐位命中（+5mm 姿态差，身高官方对账第二例）**、断网 32 资源 0 外网、截图 `preview-booster_k1-v1.png` 存档（画面判读：小尺寸人形双臂平展整机闭合无幽灵）；**七模型基线逐位回归** go2 0.334/g1 1.323/lite3 0.298/x2 1.319/t1 1.180/m20 0.675/dr02 1.792 全命中；⑧**S6 基准（展幅超线首例+处置定案）**：首轮展幅 **22.4% 超验收线 20%（本库首次）**——三轮复跑：中位三轮一致（39,544/39,132/40,549，±1.8%），**负载源假设实证**（浏览器 three.js 标签渲染循环抢占 CPU，关闭后第三轮 19.2% 过线）——**取干净环境第三轮 40,549 steps/s 为正式数字**，前两轮超线与处置如实记档（模型页披露 5）；⑨**S7 报告**：K1 模型页全文（披露 5 节：域名迁移+路径①转正居首/注释 world 块/单池 52 收 24/传感器座+mesh 碰撞第二例/身高对账+S6 处置）、LICENSES.md 加 booster_k1 复指行、顶层 README 收录行/披露索引/M7 表/预览链接。
- 本会话（M7 S1–S7 leg）`pipeline/` 零 diff（拉取/入库/预览/基准/报告全程无改码——M5/M6 通用能力直接覆盖，N2 备案行不适用，如实声明）。
- 状态：**M7 S1–S7 全链完成 → 协议⑤送审**（REVIEW-REQUEST.md：push 放行 + S7 验收 + 展幅处置与域名迁移补记确认三决策点），停手等审核台；本地 commit 未 push（领先 2=223cd0a 协议②+本件）。

## 2026-10-11（会话 22：R19 读毕 → 三小件返工（DoubleSide/lite3 换图/口径更正）→ 增量重送）

- 会话开始仪式：读 REVIEW.md → **R19 已回写：返工五项四过一补**——X2 scale 修复实测有效（1.319 逐位命中+徽标 12cm 渲染正确）、披露 1/L12/N2/敏感扫描全过；但 **lite3 镜像腿渲染缺陷新发现**：本会话送审件"三模型 URDF 无 scale 属性"断言未跑 grep 即落笔（lite3 实有 6 处 scale 含 5 镜像——hip/thigh 左右腿共用 STL 的镜像技巧），**L12 立规当天在断言里复发**（连续第三次同类：R18-决策点3/R17-台账46/本次），记轻度越界；负 scale 翻三角形绕向 + STL_MATERIAL FrontSide → 镜像腿内翻缺面，M2 公开 lite3 截图系缺陷渲染产物需换图；另深度口径差（0.681 AABB 保守并集 vs 0.643 FK 逐点）记观察项。
- **三小件执行**：①`STL_MATERIAL` 补 `side: THREE.DoubleSide`（负 scale 镜像翻绕向的标准修复；闭合实体背面被深度测试遮挡，双面渲染对无镜像模型零观感代价）+ index.html v8；②lite3 截图重渲染替换：新官方图 `images/preview-lite3-v8.png`（四腿实心、左右镜像正确），v4 旧图（缺陷渲染产物）删除，模型页加换版说明；③口径更正（grep 证据随送审件）：**go2/g1 URDF 0 处 scale（`grep -c` 实测）、lite3 6 处含 5 镜像**（L44 恒等；L149/L175/L379 `1 -1 1`、L252 `-1 1 1`、L354 `-1 -1 1`——hip/thigh 左右腿共用 STL 镜像）。
- **验证数字**：lite3 高 0.298 不变、宽（three z=URDF y）0.436→0.372=镜像应用后正确值（R19 消融实验预测一致）；**镜像判据程序化闭合**：三组腿网格（hip/thigh/calf 指纹分组）世界包围盒在左右轴 z 严格成对镜像（±0.159/±0.127/±0.045），x 差值=前后腿位置非失真；X2 回归 1.319/徽标不变、go2 0.334/g1 1.323 不变、四模型 loadFail 0、断网自检全 0；画面判据 lite3 四腿实心对称。
- **N2 改码备案（本会话 pipeline/ diff 2 处，均通用改动零模型特异）**：①preview.js STL_MATERIAL 增 DoubleSide（动因=R19 镜像腿缺面：负 scale 翻绕向需材质配套，全部镜像网格受益）；②s5_preview/index.html v7→v8（动因=①缓存击穿，既定手法）。
- 状态：**三小件完成 → 增量重送**（REVIEW-REQUEST.md：三小件证据 + 请轻量复核放行 push），停手等审核台；本地 commit 未 push。

## 2026-10-11（会话 21：R18 读毕 → 决策点 3 事实前提被推翻 → P1 返工五项 → 增量重送）

- 会话开始仪式：读 REVIEW.md → **R18 已回写：M3 首次决策点级退回**——硬数字全过（四链三锚 83/83、物理全复现、N2 备案合规、R17 检查点 ✓），但**决策点 3"跨格式 visual 缩放分歧"事实前提被推翻**：URDF L478 本就有 `scale="0.03 0.05 0.11"` + 半透明黑，上游两格式完全一致；4 m 幽灵 = preview.js 零处处理 `<mesh scale>` 的**本库渲染缺陷**；本会话送审件另记轻度口径缺陷（枚举 amend 前死哈希 `105b8f7`）。审核台预言"应用 scale 后含徽标仍 ≈1.319"。
- **P1 返工五项执行**：①preview.js 补 scale 应用（`scaleAttr → obj.scale.set`，通用健壮性）+ index.html 缓存 v7；重测：**X2 含徽标包围盒 1.319 m ↔ 官网 1.31 m 逐位命中 R18 预言**，go2 0.334/g1 1.323/lite3 0.298 三基线逐位不变（无 scale 属性模型零副作用），断网自检 0 外网；重渲染默认视图单截图 v6（徽标 12 cm 半透明，两视图在修复后无差异，合并为单张——M1/M2 单图先例），v5 双截图（缺陷渲染产物）删除；②模型页披露 1 重写（上游一致 + 本库踩坑史 + 下游"必读 mesh@scale"提示；0.453 m 宽度对比一并更正——那也是幽灵撑出来的巧合）；③顶层 README 披露索引行 + M3 表 S5 行同步改口径；④**AGENT-LAB L12 记档**（工具中间表示被当原文/循环验证/立规三条：先读属性再定性、跨格式分歧两侧读同类属性、互证前提=两条证据链各自触达 source of truth）；⑤增量送审件（本件，**不枚举自身哈希**——M2 口径，R18 轻度缺陷不再犯）。
- **N2 改码备案（本会话 pipeline/ diff 2 处，均通用改动零模型特异）**：①preview.js 增 URDF `<mesh scale>` 应用（动因=R18-L12 返工：忽略 scale 把缩放网格按原生渲染；全部模型的 scale 网格受益）；②s5_preview/index.html 缓存版本号 v6→v7（动因=①的缓存击穿，既定手法）。
- 状态：**P1 返工完成 → 增量重送**（REVIEW-REQUEST.md：返工五项证据 + 请复核放行 push），停手等审核台；本地 commit 未 push。

## 2026-10-11（会话 20：R17 读毕 → M3 S1–S7 全链完成 → 协议⑤送审）

- 会话开始仪式：读 REVIEW.md → **R17 已回写：协议②全项批准零退回（连续第三个一次过）**——选型定案智元灵犀 X2（v1.4.0 X2-Ultra 配对）、MulanPSL-2.0 定性=可收录并**立人工定性三件套先例**（blob 正本+SPDX 名录+义务清单）、锚点确认（x2_fist 单列冗余=无害口径小瑕）、A4 接受（路径①阴性审核台亲手复核成立）；**S7 新检查点=上游 LICENSE 无逐字版权行不得虚构**；S1 即刻解禁。
- **S1（拉取）**：config 程序化生成（pin 从 evidence 注入；license 快照改名对齐管道惯例 `LICENSE-upstream-agibot_x2_urdf.txt`，字节不变 A2 MATCH sha256 `d5777bea…`）。直连一次命中锚点 `575cc6b9`，raw 82 件/125.0 MB，**blob-parity 门 78 件失配 0**（K2 门第二次实战全绿）。**审核台实测数独立复现逐项全中**：72 引全显式 `./meshes/` 前缀/40 唯一 STL/39 link/38 joint（31 revolute+7 fixed）/65 stl 全小写；引用↔磁盘双向对账零缺失零大小写失配；65−40=25 件为变体共用网格池（G1 先例同构）。新事实：MJCF 32 body/32 joint 与 URDF 39 link 自洽（7 fixed 融合+free 根）。
- **S2（校验）10/0/0 全绿**：根=pelvis、72 引→40 件、40 网格 trimesh 全读通（最小 29304 顶点）、MJCF 编译 nbody=33/njnt=32/nq=38/**nu=31**（31 revolute↔31 hinge↔31 执行器逐数自洽）。
- **S3（体检）8/4/0 无 FAIL**：两侧质量逐 body **32/32 完全一致**（44.801 kg 同值）、31 对关节轴逐分量差 0；WARN×4 全有处置——①总量 44.801 vs 官网 39kg（+14.9% 超 ±10%：官网未注明含电池/换电单列/焕新电机更重，口径披露不修）②7 个 fixed 传感器座无 inertial（普遍约定）③32/39 有 collision（同源）④MJCF 同总量。**S3 前置侦察**：官网 X2 参数表静态 HTML 可提取（evidence/official-x2-spec-page.html）——39kg 旗舰版口径、身高 1.31m、主动自由度 25/30、**关节峰值扭矩 120 N·m**（effort 基准）、500Wh 换电；DOF 披露点=URDF 31 = 官网 30 + head_pitch（URDF 头 2 自由度 vs 官网颈 1）。
- **S4（入库）FAIL 0 / WARN 0**：83 溯源件/158.0 MB 三锚全过；唯一源 43（40 网格双侧落位保持官方引用结构）+ excluded 35 逐件带 why（程序化生成 25 件变体网格 + 2 README + 1 上游杂件 `meshes/meshes`=1 字节 "."——xxd 实证）；官方渲染图 png 走 s4.images 入库；算式按源件口径平账（78=43+35）。
- **S5（预览）config 驱动 + 质检发现**：X2 走 `s5.viewport="humanoid"` 新键（preview.js 改 1 行 config 化+G1 回退兼容）；40 STL/31 滑条/断网自检 0 外网；go2/lite3 数字+画面回归全过（go2 包围盒 0.334=L10 完整基线逐位一致）。**核心发现=跨格式 visual 缩放分歧**：品牌徽标件 `agibot.stl`（"agibot" 字母飘带，native 3.959×0.809×0.389 m，trimesh+浏览器双实测）URDF 侧 1:1（无 scale）撑爆包围盒至 1.519m/3.959m；MJCF 侧 `scale="0.03 0.05 0.11"`（全场唯一带 scale mesh）+半透明黑收为 12cm 徽标——**剔除该件后机身 1.319m ↔ 官网 1.31m 逐位吻合**。定位链：包围盒异常→逐件世界坐标→29304 顶点件→二进制 STL 三角数 9768 反查文件名→urdf/xml 双侧归属比对。零修复+双截图（默认如实/机身特写）+下游提示（本库首个跨格式 visual 分歧）。
- **S6（基准）**：39,086 steps/s（25.6 µs/step，加载 454.5 ms，展幅 4.5% 稳过）——四模型序列第四点（Go2 105k/G1 51k/Lite3 48k），33 body/99 geom 复杂度主导，跨模型不可比再实证。
- **S7（报告）**：模型页全文（披露块 5 节：跨格式缩放分歧居首）；LICENSES.md 加 MulanPSL-2.0 行（R17 检查点：版权主体行缺失如实注记不虚构；双 license 并存口径一致）+商标补智元；顶层 README 收录行/披露索引/M3 表/预览链接/license 双层措辞；**本库 LICENSE 第三方声明层同步全厂商口径**（顺手修 M0 时代欠账——该层此前只提宇树，M2 云深处商标未同步）。
- **N2 改码备案（本会话 pipeline/ diff 共 3 处，均通用改动零模型特异）**：①s4_package.py coverage 打印改源件口径（动因=X2 双侧共享池致 dest 件数算式永不平，撞 F1"算式必须平"；PASS/FAIL 判据不变仍按 src 集合）；②preview.js isHumanoid 改 config `s5.viewport` 驱动+G1 硬编码回退（动因=X2 人形需人形机位，模型名硬编码违背 v4 config 驱动精神）；③s5_preview/index.html 缓存版本号 v5→v6（动因=②的缓存击穿，M2 既定手法）。
- 状态：**S1–S7 全链完成 → 协议⑤送审**（REVIEW-REQUEST.md：push 放行 + S7 验收 + 跨格式分歧处置确认三决策点），停手等审核台；本地 commit 未 push。

## 2026-10-11（会话 19：M3 启动——三路线选型侦察 + 智元 X2 S0 落档 → 协议②送审）

- 会话开始仪式：读 REVIEW.md → **R16 已回写：协议⑤完成，M2 含发布全流程闭环**（R15 节随队上线实证 + N2 立规首执行在案）。按 R16 尾注启动 M3，三路线候选（同仓多机型 / 加速进化跨仓配对 / 智元 license 定性）选型侦察。
- **侦察三波全程序化**（`workspace/m3_recon/`，gitignore 不入库）：①`scan_m3.py` org/账户扫描——**BoosterRobotics 实为个人账户非 org**（M1 期 `/orgs/` 404 真因，记 L11）；②`scan_trees.py` 四仓树扫——**booster_gym 内 resources/T1/ 已有 URDF↔MJCF 同仓配对**（"跨仓配对"非必需）、`genie_sim_robot_model`（Apache-2.0 新仓）**仅 xacro 源 0 成品 URDF**（收源生成=派生，撞红线精神）、`agibot_x2_urdf` URDF↔MJCF 同目录直接配对（v1.4.0）；③`fetch_licenses.py` license 原文三份落档——booster_gym NOASSERTION 真身=Apache-2.0（方括号版权行骗过检测器）、**agibot_x2_urdf NOASSERTION 真身=木兰宽松许可证第 2 版（MulanPSL-2.0）**。
- **MulanPSL-2.0 程序化定性**：SPDX 官方名录 740 项命中——`MulanPSL-2.0`，`isOsiApproved: True`、未弃用（MulanPSL-1.0 无 OSI 标记）；义务=分发附许可证副本+保留版权/商标/专利及免责声明（§4）、无商标许可（§3）、中英同效中文优先（§6）——未修改分发官方件+保留副本即义务满足，与本库 MIT+第三方声明层兼容。
- **S0 落档**（`gen_x2_s0.py`）：`models/agibot_x2/` = SOURCE.md（状态=待审）+ `LICENSE-upstream-mulanpsl2.txt`（blob `adf05533…`，`git hash-object --no-filters` 比对 MATCH，L8 立规执行）+ evidence ×6（org/repo/license 端点/HEAD/SPDX/README 官方声明）。锚点 v1.4.0 X2-Ultra 配对（72 mesh 引实测 `./meshes/` 显式前缀，Lite3 同款风格）；不入库清单按 M1 先例（v1.3.0 整套/EDU/手部变体/simple_collision/scene.xml/x2_fist）。
- **A4 强度如实分层**：路径②成立（org 官方字段自指 agibot.com + 23 仓生态互证 + README_CN 官方声明 + 官网页脚生态仓直链含 Agibot-World 品牌互指）；**路径①阴性**——官网→AgibotTech 直链四站探测未命中（agibot.com.cn / open.agibot.com / openloong.org.cn / agibot.com，原件存 m3_recon），强度与 M1 相当低于 M2，S0 收尾补强方向=官网新闻/公告页。
- **推荐定案：M3 = 智元灵犀 X2**（正面接审核台预设 license 考题 = 质检含金量最硬一集；管道预判零结构改动）。跨仓配对建议 M4 专项（双仓双 license 三锚是 S1/S4 结构扩展）；同仓多机型建议 M4+/维护态填充件。
- 本会话 `pipeline/` 零 diff（侦察+S0 纯取证，无改码——N2 备案行不适用，如实声明）。
- 状态：**协议②已触发**（M3 选型定案 + MulanPSL-2.0 定性确认 + 锚点与不入库清单 + A4 分层四决策点），停手等审核台；本地 commit 未 push（push 属协议⑤）。

## 2026-10-11（会话 15：R10 读毕 → K1 七步修复完成 + 准备 S1）

- 会话开始仪式：读 REVIEW.md → **R10 已回写**：①M1 选型定案 = 宇树 G1（g1_23dof 配对）**批准**；②S0 license 门关闭放行 S1（前置 = K1）；③**J1**：M1 送审件"30 变体"计数不实，实测 33 文件（23 urdf + 10 xml）= 23 去重配置，S1 报告按准确计数记档（"数字必须能被重放"）；④**K1 P0**：autocrlf 第二幕——上游 blob 全 LF，M0 检出件被转 CRLF 入库，公开仓库 34 件文本件行尾失真（内容级零差异）；正本判据修正 = **git blob（cat-file/contents base64），永不采信工作区检出件**；⑤S5 STL 支路 = 配置边界内管道增强，带五条件直进。
- **K1 七步全部完成**：①两克隆 autocrlf=false + **检出区 62 件 cat-file 全量导出**（`checkout -f` 不可信——autocrlf 混乱时 status 报 clean 且不重写行尾；cat-file 直写免疫；5 件 PNG 的"CRLF"系二进制随机字节，逐件判明上游原生）；②models/ 34 件 blob-exact 替换（35 件终验全 PASS，含 license 快照 2 件）；③S4 重跑 **traceability 33/33、FAIL 0**（manifest 重生成 62 件/77.7 MB）；④S2（10/0/0）+S3（8/4/0/SKIP1，WARN 均既有处置）回归门重跑；⑤SOURCE.md §4（快照 v3 = blob-exact，R10 预言哈希 84aac59f/a5d73fc4 逐位命中三重验证）+ 模型页/顶层 README 同刷（56,119,567→**55,357,945 B**，差 = ~500 万行尾归正）；⑥**L8 记档**（autocrlf 两幕 + 三条新立规：哈希肉眼比对禁止/CRLF 判二进制/拉取一律正本检出）；⑦commit+push 见下。
- 疑点排除记：M0 报告 82.3 MB vs 现测 77.7 MB——分仓实测定位 = dae/obj 逐行几何 ~500 万行尾累计，件数 62 前后一致，非文件增删；S1-fetch.md 历史正文不刷，末尾加 K1 附注保审计链。
- **S1（G1 拉取）同会话完成**：s1_fetch.py 参数化（model 名入参，"脚本模型无关"设计承诺的实现补课，非设计改动）+ clone 命令 `-c core.autocrlf=false`（L8 铁律落码）；configs/unitree_g1.json 落盘（pin 从 evidence 原件程序化注入，杜绝手打；s3/s4 段骨架待 S2/S3 实证回填）。拉取直连一次成功：ros 223 件/120.7 MB + mujoco 76 件/37.1 MB，manifest 299 件/157.8 MB。**license 快照 A2 MATCH 一次过**（检出件=blob 正本，对比 M0 同步骤抓到 CRLF 失真——K1 根治的对照实证）；**J1 计数 raw 重放通过**（23 urdf+10 xml=33 文件=23 配置）；A2 三个上游 md 许可关键词全零（待办闭环）。**新发现两枚**：①URDF 引用协议差异——g1_23dof.urdf 网格引用 50/50 相对路径（Go2 走 package://），S2/S4 按 ref_style 分支（改码点，S4 前报备）；②MJCF 池 60 件中 23dof.xml 仅引 29 件（31 件为 29dof/手部网格）→ S4 闭包拷贝 29 件，整拷否决。S1 报告人读段落 reports/S1-fetch.md。
- 状态：**K1 闭环 + S1 完成**，commit 本地（push 留下一个协议窗口）；下一步 S2（校验，含 ref_style 分支实现与 STL 大小写核验）。

## 2026-10-11（会话 14：M1 启动——选型侦察 + S0 license 核对 → 协议②送审）

- M0 闭环后用户令"继续"，启动 **M1（第二个模型）**。选型侦察：五家国产厂商官方 org 全景扫描（GitHub API 实测）——宇树 URDF∩MJCF 交集 11 模型；智元（genie_sim 平台重）、加速进化/众擎/云深处（license 未核）、逐际（文件未定位）。
- **推荐定案候选：宇树 G1（人形）**，配对 `g1_23dof.urdf` ↔ `g1_23dof.xml`；29dof 系留 M2+；30 变体不入库只记录。四条理由见送审件（形态跨越证管道普适性 / S0 门最干净 / 配对名对齐 / 作品叙事）。
- S0 产出备齐：SOURCE.md（状态=待审）+ license 原文快照 ×2（1558/1559 B，BSD-3）+ evidence ×7（org/两仓库/license 端点/head）。**上游零漂移**：head = M0 所钉锚点，check_anchors.py 三源程序化裁决 OK。
- **新事实两枚**：网格格式 stl（URDF 侧池 173 件/110.4 MB 全变体共享，MJCF 侧 60 件/31.8 MB）——S5 需新增 STL 支路（M0 加载器只覆盖 dae+TGA），"加配置不改码"边界如实进送审件请裁定；两目标子目录无独立 LICENSE（A2 过）。
- 排障记 **AGENT-LAB L7**（python 商店 stub exit 49 / Windows 反斜杠 glob / 内联转义穿墙）+ 立规：**哈希与长串一律程序化比对**。
- 状态：**协议②已触发**（M1 选型 + S0 结论确认 + S5 增量裁定三决策点），停手等审核台；本地 commit 未 push（push 属协议⑤）。

## 2026-10-11（会话 13：R9 读毕 → M0 正式收官收尾）

- 会话开始仪式：读 REVIEW.md → **R9 已回写：协议⑤完成，M0 含开源发布全流程闭环**（审核台独立实证：三源一致 + 匿名访问 Public 确认 + 目录齐）。
- R9 抓到回执错数一处并要求更正：**"12 个 commit" 实为 21**。工作台按规矩先实测复核（`rev-list --count 5e1785a` = 21，与审核台、GitHub 页面三方一致）→ 回执件正文已更正并注明。
- 按 R9 授权执行收官同步（R8 放行范围内，无需新送审）：R9 结论 + 回执更正 + 本条记档一并 commit/push。
- **M0 宣告正式关闭**：S0 license 门 → S1–S7 管道 → 九轮审核（R1–R9）→ 开源上线，零越界收官。项目进入维护态（M1+ 加模型 = 加 config；凡动 models/ 必重跑 S4）。

## 2026-10-11（会话 12：协议⑤执行回执 → M0 全流程闭环）

- 用户按 R8 首选路径 a 完成 push：GitHub `Hazel-LCX/cn-robot-models`（public）。**回执实测：本地 main = origin/main = ls-remote = `5e1785a` 逐位一致，M0 全部 12 个 commit 上线**（含审计链台账随库公开）。
- R8 落档提交（`5e1785a` 本身）含 REVIEW/REVIEW-REQUEST 的 R8 标注与结论。
- 状态：**M0 全流程（设计→八轮审核→实现→收官→开源发布）闭环**，REVIEW-REQUEST.md 回执件待审核台回写 R9 一行收尾。后续 M1+ 按常规流程另起。

## 2026-10-11（会话 11：R7 清算（G1/G2/H1）+ R5 三项自查 → 协议⑤送审）

- **G1**：S4 报告头部体积口径注明分解（raw 溯源件 B 数 + 质检自产件 B 数 = 总 MB）。
- **G2**：coverage 补桶——`robots/README.md` 归"根级及中间层"（9 = 根级 8 + 中间层 1），目标子目录口径改完整前缀（53），算式写平：**62 = 9 + 53；53 = 入库 33 + 排除 20（其中 meshes/ 冗余 7），未覆盖 0**。
- **H1**：s4_package.py 重跑刷新对账，**total_bytes = 56,119,567 与磁盘 34 资产件逐字节一致（终验 True）**；README 两处同步 56.1 MB 口径；**"对账即事实"规则落 PIPELINE v0.6**（§3-S4：凡变更 models/ 下任何文件必重跑 S4）。
- R5 三项自查：README 定稿（终值口径）✓；LICENSES/SOURCE 一致性（BSD-3/双锚点双文件在案）✓；.gitattributes clone 抽查 5/5 + clone 内加载 ✓。
- 过程失误两连记 AGENT-LAB L6（短变量 NameError 被 grep 滤错线索、sed 写出占位符），均当场自纠。
- 状态：**R7 清单全清 → 协议⑤送审**（REVIEW-REQUEST.md：push 前检查清单执行证据 + 请裁定 push 执行方式），停手等终查。

## 2026-10-11（会话 10 补记：预览落地对齐修复）

- 用户反馈预览页"机器人半截身子在地平线以下"——根因：URDF base 原点在髋部、足端 z≈−0.32，Z-up 转换只修了方向没修位置，网格面（y=0）拦腰切过整机。修复 = 加载后按包围盒自动抬升至足端贴网格面 + 相机目标对准几何中心；浏览器复验通过（断网自检/红标照旧全绿）。记 AGENT-LAB L5；模型页配图同步换落地版截图。

## 2026-10-11（会话 10：终审 F1/F2 修复 → 数字复核）

- **F1 修复**：s4_package.py 计数改**物理文件口径**——网格闭包按 dest 去重 + `assert` 防回归（URDF 17 处引用 → 7 个物理 dae）；体积实求和；冗余判定 17/0 → **7/0**；coverage 算式写平（root_level 改两段路径判定）：**raw 62 = 根级 8 + 子目录 54 = 入库 33 + meshes 冗余 7 + 排除 13，未覆盖 0**。重跑刷新 S4 报告，**终值：物理文件 34（33 个 raw 溯源件 + 1 个质检截图）/ 56.2 MB（磁盘 56,186,xxx bytes ≈ 53.9 MiB）**。扩散 4 处更正：SOURCE.md §4 / 顶层 README / 模型页 Provenance / S4 报告源头。
- **F2**：s3 C1 模板 png 提示移 config（notes['upstream_png']），S3 重跑 8/4/0/SKIP1 不变。
- 修复过程自抓两尾巴：S4 骨架每次重跑覆盖 S7 全文模型页（改"仅缺失时写" + git 历史恢复全文）；重跑 rm 误删质检截图（恢复重跑，清落位清单不再含 images/ 误删风险）。
- 自查：脚本 = 磁盘 find = git ls-files = **54** 三源对齐；正文文档 "43/81.4" 残留清零（DEVLOG 历史与 REVIEW 原文合规保留）。
- 状态：F1/F2 修复回报已写 REVIEW-REQUEST.md；**等用户复核数字 → 审核台回写"M0 正式收官"**。push 公开仓库按协议⑤另触发。

## 2026-10-11（会话 9：S7 收尾完成 → 终审送审）

- **E1 全清**：①官网规格页截图入 evidence/（浏览器实测）——顺带挖出**口径定案**（官网原文"带电池重量 约15kg"）+ 三个旁证（扭矩 45N·m ↔ calf effort 45.43、电机 12 个 ↔ 12 revolute、运动空间 thigh/calf 与 URDF 符号镜像等宽）+ **一个新分歧：hip 限位 URDF ±60° vs 官网 ±48°**（披露不修，已入模型页）；②calf 披露块全文进模型页（两源数值/−87.4g×4/归因/RL 下游影响提示）。S3 口径证据升级后重跑，数字不变（8/4/0/SKIP1）。
- **S7 产物**：顶层 README（**以"仿真模型质检管道"为主体**，库是副产品；两套叙事；质检汇总表；B3 商标声明）；模型页 README 全文（provenance/使用/质检结论/披露块/口径/文件清单）；本库 MIT LICENSE（含第三方声明三层：上游 BSD-3/three.js MIT/商标）。
- **干净环境实测（近似新 clone）**：首跑抓两个真问题——①模型页引用截图忘了 commit；②**autocrlf 把 three.module.js 转 CRLF 破坏哈希承诺** → `.gitattributes` 锁资产字节稳定 + renormalize → 复测 **6/6 哈希一致 + clone 内 MJCF 加载 OK**。记 AGENT-LAB L4。
- 状态：**S0–S7 全部完成，M0 闭环** → 终审送审（REVIEW-REQUEST.md：E1 查验/数字溯源/干净环境见证/门面叙事/M0 收官五决策点），停手等审核台。收官后 push 公开仓库需按协议⑤另行触发。

## 2026-10-11（会话 8：S5 预览 + S6 基准收官）

- **S5 预览**：B6 退路决策记 AGENT-LAB L2（URDFLoader 版本轮盘不值得赌 + jsDelivr npm 路径证实超时）——**自写 URDF→three 加载器 ~180 行**，vendor three 0.160.0 三件（ColladaLoader/TGALoader/OrbitControls）+ **原版 MIT LICENSE**（修正 3 验收项），npmmirror files API 单文件拉取。**浏览器实测验收（工作台自验 + 截图存档）**：断网自检 13 资源全本机、外网请求 0；42 links / 41 joints / 12 关节滑条（滑条范围比 URDF 限位宽 0.4rad，越限标红=质检元素）/ 17 visual 网格；站姿正确；读取的就是 models/ 入库件（../../models/ 相对路径）。三连 bug 修复记 L3：滑条初值（calf 限位不含 0 → 初值取限位中点）、Z-up/Y-up 坐标转换、rpy 分量序。
- **S6 基准（入库件）**：**MuJoCo 步进 105,131 steps/s（9.5 µs/step）**、加载 56.0 ms、URDF 解析 4.7 ms；预热 100 步丢弃 + 10⁴ 步 × 5 次取中位数（B2 落实）；稳定性展幅 3.0%（<20% PASS）；机器/版本全记录。
- 状态：S5+S6 过（无送审点）→ **S7 收尾**：顶层 README（"仿真模型质检管道"主体 + 两套叙事）+ 模型页（E1 calf 披露块 + 官网规格页截图）+ 本库 MIT LICENSE 文件 + LICENSES.md 定稿 + 干净环境实测 → 终审。预览页本地常驻：http://127.0.0.1:8130/pipeline/s5_preview/index.html（用户可直接玩）。

## 2026-10-11（会话 7：R4 消化 + S4 入库全绿）

- R4 回写读取：**S3 认可（审核台独立复核 raw 数字，forensics 数学自洽）/ calf 不修+披露批准 / 四脚本细审通过 / AGENT-LAB 首查账通过 / 零越界 / 放行 S4**；E1–E6 领取（E1 留 S7 查验）。
- **E2/E3/E5/E6 随本轮落实**：foot 措辞更正（"自闭合空 body：零质量/零 geom/零 site，触地几何挂于 calf 的 foot class geom"）；三处 Go2 硬编码 config 化（alias/行程注/png 注）；MJCF 惯量方法论披露写入 S3 报告（URDF 独立数学检查 vs MJCF 编译器背书，不对称如实披露）；collision 网格检查显式 SKIP 行 + enumerate 冗余清理。**S3 重跑 PASS 8 / WARN 4 / FAIL 0 / SKIP 1——数字与 R4 预期完全一致**。
- **S4 入库（s4_package.py + config s4 段）：43 文件 / 81.4 MB，PASS 6 / FAIL 0 / WARN 0**——traceability 43/43 命中 manifest 同路径行；两源网格哈希交集 0 → 分目录，MJCF 网格落 `mjcf/assets/`（保持官方 meshdir，不改官方一字节）；**R3-D3 遗留裁决：dae/ vs meshes/ 同内容 17 / 不同 0 → meshes/ 为冗余目录不随库分发**；coverage 未覆盖=无；入库路径 MJCF 编译 + yourdfpy 双复验通过。
- s4 自查两处修复后重跑：meshes/ 冗余排除逻辑（原从 rows 筛——rows 里根本没有未入库文件；改为从 dae rel 拼路径）、raw_count 排除 .git。
- 待核小账（下会话顺手，不阻塞）：coverage 算术 43+20 vs 62 的口径差 + find 40 vs 43 的 .md 过滤口径——traceability 43/43 与 uncovered=无 两个硬判据已过。
- 状态：S4 过 → S5 预览 + S6 基准（无送审点挡路，连做）；E1（calf 披露块 + 规格页截图）在 S7 收尾查验 → 终审。

## 2026-10-11（会话 6：S3 物理体检 · 零修复纯体检 → 专项审送审）

- s3_physics.py 上线（质量口径声明置顶 + 体检矩阵 + C1 双清点表 + URDF↔MJCF 交叉对账）。结果 **PASS 8 / WARN 4 / FAIL 0**，零修复纯体检。
- **质量分歧 forensics 闭环**：URDF 16.087 vs MJCF 15.206，差 0.881kg 逐项解释 = rotors 12×0.089（URDF 独立 rotor link，约定差异）− calf 4×0.0874（真值分歧）+ foot 4×0.04（MJCF 零质量纯 site 架，约定差异）+ head 0.002；hip/thigh/base 逐项完全一致；**12 对同名关节轴逐分量差 0.00e+00**（运动学同源实锤）。
- **修正 1（逐轴垂距法）实战首战**：17 link×3 轴全部落 [0.005, 0.5]——旧全长法会误报 4 条 calf 长轴，审核台预判命中。
- 官网标称存证：unitree.com/go2 JS 渲染、静态页无重量数字，片段已存 evidence/；15kg 取公开规格表 + 口径栏如实注明"是否含电池未证实"；送审决策点 3 提出收尾前补截图。
- 体检器自查修正两处：joints 字典缺 child 键（跑前自查修复）；foot 从"真值分歧"重归类为"约定差异"（MJCF 零质量纯架）后重跑。
- AGENT-LAB.md 建档（L1：enumerate 切片 TypeError + ugrep 复杂正则两次踩坑，四要素已记，未升级）。
- 协议检查：零修复 → 协议③未触发；S3 报告产出 → 按 R1 送审点 3 送**专项审**（REVIEW-REQUEST.md 已写，含 pipeline/ 全脚本细审请求），停手等审核台；放行后进 S4 入库打包。

## 2026-10-11（会话 5：S2 格式校验全绿）

- s2_validate.py 上线（lxml 自查为权威 + yourdfpy 交叉确认 + MuJoCo 真编译为最强校验），config 增 s2 段；yourdfpy 探针确认 0.0.60 的 filename_handler 机制（默认剥 package://+包名再拼 mesh_dir，正好覆盖重映射）。
- 结果 **PASS 9 / INFO 2 / WARN 0 / FAIL 0**：URDF 42 links / 41 joints（29 fixed + 12 revolute），根=base，单根无环无菱形；17 处网格引用 → 7 个文件全解析、trimesh 全读通（最小 7703 顶点）；MJCF 真编译通过——nbody=18 njnt=13 ngeom=56 nmesh=16 nu=12 nq=19 timestep=0.002，scene.xml 场景包装也编过。
- **质检素材两条**：①URDF collision 不引用任何网格文件（17 处引用全为 visual 的 dae）——碰撞几何全是基元，S3 的 A1 清点要按"基元存在性"查而非网格；②URDF 12 revolute ↔ MJCF nu=12 电机数对上，S3 对账的现成钩子。
- 报告：reports/S2-validation.{md,json}。状态：S2 过 → 下一步 S3 物理体检（垂距法惯量首战 + 质量口径钉死 + 碰撞体清点）。
- **R3 回写对齐**（审核台正式落 REVIEW.md）：代码首审过（五件套基线立定）、S0 门关闭（A4 认可"可复现实测输出"为证据原件形式，截图不再必要）、修正 1–8 核验 8/8、S1 放行 S2；附带发现：上游 urdf/ 自带 Amended/Normal_collision_model.png 两张碰撞示意图 → S3 清点作上游对照素材。
- **D1–D3 清账（v0.5）**：SOURCE.md 状态行改"已确认（R3）"；PIPELINE.md 头部版本号补齐（原停 v0.2 与 §9 矛盾）；网格格式记录全改实测（URDF 源 dae/ 与 meshes/ 均 .dae、无 stl）。
- **自查收敛**：s2_validate.py 原引入 INFO 第五态，违反刚立的四态基线——观察并入检查明细（mesh-refs / joint-limits），重跑 PASS 10 / FAIL 0，四态纯。S3 专项审送审时主动声明此收敛。

## 2026-10-11（会话 4：审核台修正 1–8 落实 + S1 拉取完成）

- 修正 1–8 经用户转达落实（REVIEW.md 尚无 R3 回写，待审核台补记，工作台不代写）：①惯量 sanity 改逐轴垂距取法 [0.005, 0.5]（修"细杆长轴必误报"的方法错）；②S3 总质量对比口径先钉死（官网含电池 vs URDF 不含电池）；③S5 验收增 vendor 库随附原版 LICENSE；④A4 证据原件入 evidence/（org/仓库 API JSON 全文 + 官网首页 HTML 原文片段，实测命中 1 处导航链接）；⑤S1 主路径改 blobless+sparse；⑥URDF↔MJCF 对账增分歧处置（分歧≠错误，不对齐不修）；⑦env_check pypi 双镜像兜底（**实测**：模拟阿里挂→清华接管 PASS，全挂才 FAIL）；⑧xacro/urdf 权威关系记档（urdf 为准、xacro 溯源）。PIPELINE.md 升 **v0.4**。
- S1 拉取（pipeline/s1_fetch.py + configs/unitree_go2.json）：**直连** blobless+sparse 一次成功——ros @ `5994d4fa`（36 文件 52.4 MB）+ mujoco @ `1eb6642e`（26 文件 29.9 MB）；manifest 62 文件 82.3 MB、抽 3 复算一致；raw 只读生效。
- **A2 复核抓到真问题**：S0 快照 v1（`/license` API 端点）与 raw 字节不一致，实证原因 = 端点规范化行尾（LF）≠ 仓库原件（CRLF）；快照 v2 已按规则从 raw 重生成。质检素材 +1。
- 状态：S1 完成 → 下一步 S2 校验器（s2_validate.py，package:// 重映射是第一坑）。下一送审点 = S3 专项审。

## 2026-10-11（会话 3：S0 license 门 · 协议②触发）

- **模式修订**（用户指示）：免复述确认，直接推进+讲解；审核点协议硬门不变。
- 会话 A 收尾：**首个 commit**（设计文档 v0.3 + 骨架，git 身份现成）。
- S0 取证（GitHub API + 官网 HTML，raw 未用）：两仓库 LICENSE 原文快照入库，均 **BSD-3-Clause**、版权方=宇树本体；A4 双证据链成立（官网首页含 org 链接 HTTP 200 + org 自述 blog=unitree.com + 两仓库 fork=false）；go2_description/package.xml `<license>BSD</license>` 与仓库级一致（maintainer=TODO 占位，记为质检素材）；unitree_robots/go2/ 无独立声明随仓库级；HEAD 锚点固定 ros@**master**=5994d4fa…a259、mujoco@main=1eb6642e…ea0e7d。
- **协议②触发**（license 核对结论）：REVIEW-REQUEST.md 批量送审（代码首审 + S0 结论，C2 精神），停手等审核台；放行后进 S1 拉取。

## 2026-10-11（会话 2：会话 A · 环境就位）

- 仪式：读 REVIEW.md → **R2 通过，放行动手**（A1–A4/B1–B6/四问逐项核验 ✓；越界监察零条目；执行提示 C1–C3）。现场恢复 = v0.2 已送审待放行。
- 吸收 C1：S3 验收补"碰撞体清点表入报告"勾选项，PIPELINE.md 升 **v0.3**；C2（修复项批量送审）、C3（S0 结论天然触发协议②）记入流程，不改文档。
- 动手（会话 A）：git init（main）+ .gitignore + pipeline/requirements.txt + pipeline/env_check.py。
- 体检两轮：base（py3.14.6）→ mujoco cp314 wheel 可解析 → 定 **venv** 路线；.venv 装齐（mujoco 3.15.0 / yourdfpy 0.0.60 / trimesh 5.1.1 / numpy 2.5.3 / scipy 1.18.1 / lxml 6.1.3，阿里镜像）；venv 内复跑全绿（PASS 10 / WARN 1 / FAIL 0，WARN=raw 被墙有兜底）。**py3.14 无 wheel 的风险正式解除，py3.12 兜底方案作废。**
- 状态：env_check.py 待用户复述确认 → 确认后写 REVIEW-REQUEST.md 送**代码首审**（R1 ⑤，立风格基线）→ 会话 B（S0+S1）。git 尚无 commit（等用户发话）。

## 2026-10-11（会话 1：设计）

- 项目启动：M0 = 宇树 Go2 走通全管道。**本会话零代码**，仅环境侦察 + 产出 PIPELINE.md v0.1。
- 侦察结论：无 node（预览走纯静态）；base Anaconda = py3.14.6（mujoco wheel 存疑，env_check 第一查）；raw.githubusercontent 被墙但 api.github.com 通；jsDelivr 404 不预设可用。
- 官方源已证实：URDF = `unitree_ros/robots/go2_description`，MJCF = `unitree_mujoco/unitree_robots/go2`；两仓库均 BSD-3-Clause；两源网格格式不同（dae/stl vs obj），入库预期分目录。
- 状态：设计待用户确认 → 送审核台过审（REVIEW.md）→ 回来从会话 A（动手第0步）开始。
- 会话中段：用户补充**审核点协议**（5 类硬触发 + 固定动作 + 会话开始仪式），原文照抄进 PIPELINE.md §8；自此每次会话开始先读 REVIEW.md 新结论 + DEVLOG 最后一条恢复现场。
- 会话开始仪式首跑：读 REVIEW.md → **R1 有条件通过**（A1–A4 必修、B1–B6 吸收、四问答复、R1-附方向放行 + 三条导航风险）。
- 按待修清单升 v0.2：A1 S3 补碰撞体三件（只标记不自动补）；A2 license 快照同 commit + 子目录声明检查；A3 回归门改 S2+S3 双跑；A4 官方 org 证据链落字；B1 惯量数量级 sanity；B2 基准预热 ≥100 步 + ≥10⁴ 步；B3 商标声明；B4 MJCF 查看命令；B5 独立环境口径；B6 自写加载器边界；四问落档 §7（MIT / 不加 PyBullet / 网格默认分目录 / format_source 钩子）；完成度铁律 + 门面立位入 §0。
- **协议①触发**（管道设计改动）：REVIEW-REQUEST.md 已写，送 v0.2 轻复审，停手等放行。
- **S2（G1 格式校验）同会话完成**：s2_validate.py 模型参数化 + **ref_style 分支实现**（package:// 重映射 ∥ relative 相对解析+包根逃逸检查——G1 的 50/50 相对路径引用协议）+ **网格引用名 vs 磁盘真名大小写逐字节核验**（Windows exists() 不分大小写会放行，入库 GitHub/Linux 即 404——G1 实测 50 处 .STL 引用失配 0，R10 提醒的坑安全通过）；MJCF 场景文案中性化。**全矩阵 10 PASS / 0 WARN / 0 FAIL**：URDF 33 links/32 joints（23 revolute ↔ 官方 23dof 命名自洽）、50 引用 → 29 物理件、trimesh 29/29 读通（最小 4,266 顶点）、yourdfpy 交叉确认、MJCF 真编译 nbody=31/njnt=30/nq=36/nmesh=29——**URDF 网格 29 件 == MJCF nmesh 29**，两侧素材数对上（S3 交叉对账好兆头）；visual 29/collision 21 集合不同（素材清点归 S3-A1，M0 C1 同类）。报告 reports/S2-validation.{md,json}。
- 状态：**S2 闭环**；下一步 S3（官网侦察补 official 口径——config 骨架 pending 占位拒跑生效，零编造）→ 物理体检。S1/S2 两 commit 本地累计 ahead 1，push 留协议窗口。
- **S3（G1 物理体检）同会话完成**：s3_physics.py 参数化；官网侦察补 official 口径——unitree.com/cn/g1 规格表浏览器渲染，**截图 4 张 + 渲染文本证据件落 evidence/**（SPA 懒加载坑：fullPage 截图伪影 7 次重复，改滚动+视口分段；规格数据 curl 源码不可得）。官方口径落 config（零编造）：**带电池约 35kg / 总自由度 23 ↔ URDF 23 revolute 精确自洽 / 膝扭矩 90N.m（脚注[1] 整机最大关节电机口径）**。**体检 7 PASS / 5 WARN / 0 FAIL**：总质量 URDF 34.134 vs MJCF 34.137（**两侧仅差 0.003kg**，均 −2.5% ↔ 官方 35 无电池口径）——比 Go2 的 0.881kg 差干净一个量级；惯量 29 link 正定+三角+sanity 全过。**两大 forensics 闭环进报告**：①torso −1.28kg = URDF 独有件拆分（head 1.036+waist_yaw_fixed 0.244+零星）合计 1.283 解释闭环，建模拆分差异非真值错误；②**官方 g1_23dof.xml 实测 29 hinge（+腰 pitch/roll+双腕 pitch/yaw），文件名与内容不符**——RL 下游两格式动作空间 23/29 维不可互换，模型页将披露（M1 最硬质检素材）。五 WARN 全有处置索引。
- 状态：**S1/S2/S3 三步闭环**（本地 commit ×3，ahead 2，push 留协议窗口）；下一步 S4（入库对账——闭包拷贝 29 件 STL+32 变体 excluded+ref_style relative 闭包解析改码报备）→ S5 STL 支路（R10 五条件）→ S6/S7。
- **S4（G1 入库对账）同会话完成**：s4_package.py 六处改造（参数化；ref_style relative 闭包——dest_root=urdf 保持"meshes/ 与 urdf 同目录"相对关系；mjcf_assets closure 模式按 meshdir 解析 29 件；images 支持 source 键；recheck 参数化；**coverage 假阴性修复**——uncovered 原硬编码 unitree_robots/go2 使 G1 的 mujoco 侧漏检）。**FAIL 3→0 全清过程**：traceability 33 件误判未命中=**G1 两侧网格 28/29 同哈希（同源同内容，与 Go2 交集 0 相反）**+manifest 单路径映射"被代表"→改哈希→路径集合对账；dae-parity 对 G1 不适用→config 开关 SKIP；recheck go2 文件名硬编码→参数化。**S4 终态 FAIL 0 / WARN 0 / SKIP 1**：62 件全溯源、coverage 299=9+290=62+228 每行平（excluded 228 件逐件 why 程序化生成）、MJCF 编译 nmesh=29、URDF relative 关系保持、40.5 MB。**补记 forensics**：唯一不同哈希件 = head_link.STL（URDF 933KB 精细 vs MJCF 338KB 简化）= S3 torso 分歧同根（URDF 独立头壳建模）——两步的披露闭环成一条线。
- 状态：**S1–S4 四步闭环**（本地 commit ×4，ahead 3，push 留协议窗口）；下一步 S5（STL 支路，R10 五条件：vendor STLLoader+MIT/Go2 回归门/着色如实/坑记 LAB/PIPELINE 注记）→ S6 → S7。
- **R11 期中稽查读毕 → K2 六步全部完成（审核台首抓，S5 动工前置已清）**：审核台 95 件独立对账——go2 33/33 正本（K1 关闭），**g1 入库 62 件中 2 件 MJCF xml CRLF 失真（K1 复发）**。**根因实测（修正审核台推测）**：`git clone -c core.autocrlf=false` 只在 clone 进程内生效**不写入 local config**（实测），后续 sparse-checkout set 独立进程读全局 autocrlf=true → sparse 检出文本件全 CRLF；**意外反转**：g1_23dof.urdf 上游 blob 原生 CRLF（851 CR）——检出=blob 正本纯靠侥幸，"正本"="字节=blob 原样"而非"全库 LF"。**修复**：①raw 299 件 cat-file 归正+manifest 重生成（157.8→150.5 MB）；②S4 重拷重跑；③S2（10/0/0）S3（7/5/0）回归全绿；④**根治落码**：s1 blob-parity 门 + s4 traceability 三锚（models↔manifest↔blob，**hash-object 一律 --no-filters**——过程抓到工具自身过滤语义两连坑：主仓 autocrlf 清洗 models 件 id、门首跑 25 件假阳性，门先测门再上岗，终测 290/290）；⑤AGENT-LAB L9 记档；⑥S1 报告 L48"铁律生效实证"声明划线更正（A2 MATCH 只覆盖 2 件，外推过宽）+ SOURCE.md 同步。
- 状态：**K2 闭环，S5 解禁**（R11：完成后 S5 按 R10-⑤ 五条件直进）；本地 commit ahead 4+K2 批次，push 留协议⑤窗口（R11 明示 K2 修复与 S1–S4 四 commit 一并）。
- **S5（STL 支路 + 预览模型无关化）同会话完成（R10 五条件全落）**：①vendor 官方 STLLoader（three **0.160.0 配套版**——首拉 0.180 版本错配重拉，npmmirror files API，同受 libs/LICENSE 覆盖）；②**Go2 回归门**：17 mesh 全挂 + 完整四足渲染 + 抬升 0.245/包围盒 [0.000, 0.334]（完整模型口径——首跑 0.186 系丢段态假基线，判据升级后重验）截图存证 models/unitree_go2/images/preview-v4-regression.png；③**STL 29 件统一中性着色 + 页面如实标注**（"无 UV/材质为格式天性，非上游外观"），断网 0；④AGENT-LAB **L10**（v4 重写丢挂接段——两模型同症：G1 只剩 pelvis 盆、go2 丢四腿；回归判据升级"数字+traverse 计数+画面截图"三判据；G1 包围盒顶 1.323m ↔ 官网 1320mm 逐位吻合的交叉验证；缓存旧 html + 新 js 组合崩 → 动态 DOM 引用 ?. 兜底）；⑤PIPELINE §3-S5 格式清单注记 + §9 v0.6a 修订行（不升大版本）。**preview.js v4 = config 驱动模型无关**（?model= 读 configs/<model>.json，入库路径按 s4 对账表、引用协议 package∥relative 分流）——M2+ 预览零改码。G1 截图 models/unitree_g1/images/preview-g1-v4.png。
- 状态：**S1–S5 五步闭环**（本地 commit，push 留协议⑤窗口）；下一步 S6 基准（G1）→ S7 收尾（LICENSES.md 增行/模型页 README 含 29-hinge + head/torso 披露链/两套叙事）。
- **S6（G1 基准）同会话完成**：s6_bench.py 参数化 + 路径改读 config s4.recheck 键（K2 落的键直接复用）；qpos0 用模型默认（G1 零位=直腿站立，纯重力倾倒是预期口径，与 Go2 同法）。**结果**：MuJoCo 步进 **50,809 steps/s（19.7 µs/step）**、加载 102.8 ms（G1 nmesh 29 件 STL 比 Go2 重，合理）、稳定性展幅 2.3% 稳过、URDF 解析 4.7 ms。**跨模型解读**：步速恰为 Go2（105,131 steps/s）一半——23 关节+nbody 31 对 12 关节+nbody 18，物理量翻倍步速减半，数字自洽；S7 叙事将注明"跨模型数字不可比，本机同口径内自洽"。
- 状态：**S1–S6 六步闭环**（本地 commit，push 留协议⑤窗口）；下一步 **S7 收尾**（LICENSES.md 增 G1 行/模型页 README 全文含 29-hinge 动作空间不可互换 + head/torso 分歧链披露/顶层 README 汇总与两套叙事）→ **协议⑤送审 push**（含 S1–S6+K2 七 commit 一并）。

## 2026-10-11（会话 16：S7 收尾 → 协议⑤送审）

- **S7 三件完成**：①`models/unitree_g1/README.md` 全文——披露链核心 = **官方 `g1_23dof.xml` 实为 29 hinge（文件名与自由度不符，两格式动作空间 23/29 维不可互换）** + torso −1.28kg 与 head_link.STL 网格差异同根闭环（逐克 + 逐字节双证据）+ 官网 35kg/23 自由度口径（evidence 5 件）；②`LICENSES.md` 增 G1 两行（同锚点零漂移注明）+ 商标补 G1 + go2 过期状态行更正；③顶层 README 增"M1 · 宇树 G1"质检结果表（7 行）+ 分歧叙事链接双模型 + 商标/复现命令更新。顺手修 s4_package.py 骨架模板 go2 硬编码残留（S3 数字/calf 文案中性化，M2+ 复用防线）。
- **协议⑤送审**（REVIEW-REQUEST.md）：push 放行（ahead 8：S1–S6 + K2 + S7）+ S7 验收 + K2 六步确认三决策点，停手等审核台。
- 状态：**M1 全管道（S1–S7）完成，协议⑤触发停手**——审完 push 即 M1 含开源更新全流程闭环。
- **协议⑤执行回执（第二次实测生效）**：首次报"好了"实测远端未动（origin/main 仍 8e0a33d，9 commit 未上）——如实回报未写成功回执；用户重试后 **三源逐位一致（本地=origin/main=ls-remote=`6783901`），工作树 clean**。
- **R13 读毕 → 收尾 push**：协议⑤完成，M1 含开源更新全流程闭环。R13 更正一处名不副实：`6783901` message 称"台账随队"但仅含送审件标注一行——**REVIEW.md 的 R12 节当时未 add**（工作区状态被 head -2 截断漏看），远端审计链暂止 R11、"详见 REVIEW.md R12"悬空。本条修正：R12+R13 节 + R13 标注一并 commit/push，**commit 后先 grep 验证内容再推**（message 与内容对账，R9"12≠21"同族教训落法）。

## 2026-10-11（会话 17：M2 启动——异厂选型侦察 + S0 license 核对 → 协议②送审）

- R13 读毕（M1 闭环）后用户令开 **M2**。四家异厂深查（trees API + license 端点 + 官网抓取）：**云深处 deep_robotics_model 推荐**（BSD-3 + **单仓双格式** URDF×9/MJCF×8 多机型——unitree 分仓模式之外的新形态）；众擎出局（**无 LICENSE 文件**，红线）；智元出局（license NOASSERTION + 平台内嵌宇树 G1 非自家机型）；加速进化备选（BSD-3 但本仓纯 URDF，双格式需跨仓配 gym）。
- **推荐定案候选：Lite3（四足）**——M1 已验人形，M2 选同形态使"厂商"成唯一新变量；配对 urdf/mjcf 各 4 件同名 STL；usd/ excluded。**S0 产出**：SOURCE.md（状态=待审）+ license 快照（1502B，sha256 `6bc5967b1cfb`，blob 正本）+ evidence 6 件。**A4 强度分层如实呈现**：路径①未命中（两官网域均无 github 字样）、路径②成立（org 四字段品牌互指 + 非 fork + 28 仓生态互证）——比 M0 弱一层，请审核台裁定是否足闭门。
- 状态：**协议②已触发**（选型定案 + license 结论确认 + A4 证据强度裁定三决策点），停手等审核台；本地 commit 未 push。
- **S1（Lite3 拉取）完成——blob-parity 门自动化首战告捷**：首拉门拦截 `Lite3/mjcf/Lite3.xml` CRLF 失真（L9 根因复现：sparse set 独立进程读全局 autocrlf）→ **根治落码补全**：clone 后显式写 local config（一处写处处生效）→ 重拉 **15/15 失配 0**；license 快照 MATCH 一次过（`6bc5967b…` blob 正本）。**引用协议第三变体**：`./meshes/x.STL` 显式相对前缀（go2 package://、g1 无前缀、Lite3 带./），MJCF 无 meshdir file 相对 xml 目录——build_plan 相对路径规范化（防 dest 污染）。**两侧网格 4/4 全同哈希**。
- **S2（Lite3）全绿 10/0/0**：URDF 17 links/16 joints（**12 revolute ↔ Go2 同为 12 关节四足**，同形态对照成立）、大小写失配 0、MJCF 编译 nbody=18/njnt=13/nmesh=13。**closure 去重补丁**（F1 同哲学）：MJCF asset 段 13 个 mesh 元素引 4 物理件（重复定义 MuJoCo 不报错，nmesh 虚胖——入库 xml 原样保留，披露素材）；collision 全缺（visual 4/collision 0，S3 清点素材）。
- 状态：S1/S2 commit 待批；下一步官网侦察（Lite3 规格口径）→ S3 → S4 → S5 回归 → S6/S7。
- **S4（Lite3 入库）完成——三锚异厂首战全过**：10 件/7.0MB（urdf 1 + urdf/meshes 4 + mjcf 1 + mjcf/meshes 4），excluded 5（usd/），coverage 19=4+15=10+5 平；**K1/K2 教训自动化红利兑现**（blob-parity 门 15/15 + 三锚 10/10 零人工干预）；mesh-split 口径修正（按 kind 过滤——前缀匹配曾把 mjcf 主件 xml 混入网格集合 5=4+1 虚胖）；s4_package 最后两处 go2 硬编码清零（provenance 通用化）。
- **S5（Lite3 预览）完成——M2 零改码承诺兑现**：v4 config 驱动直接吃 deeprobotics_lite3.json，首跑即完整四足渲染（13 处引用全挂、抬升 0.225/包围盒 [0.000, 0.298]、断网 0、12 滑条）；STL 计数口径修正（唯一 URL=4 物理件，引用 13 处）；**缓存三连课**（module 缓存键需 index.html 引用参数化 ?v=5、html 自身缓存需 URL 参数击穿——L10 同族）。
- 状态：**S1–S5 五步闭环**（本地 commit）；下一步 S6 基准 → S7 收尾 → 协议⑤送审。

## 2026-10-11（会话 18：S6/S7 → 协议⑤送审）

- **S6（Lite3 基准）完成**：47,966 steps/s（20.8 µs）、加载 59.2 ms、展幅 4.9% 稳过；**同 DOF 异厂商对照发现**——与 Go2 同 12 关节/nbody 18 却差 2.2×，引擎负载由 geom 类型与网格复杂度主导（Lite3 mesh geom + 高顶点 STL），"跨模型数字不可比"再实证（报告注记）。
- **S7 三件完成**：①Lite3 模型页全文（披露链：FAIL 四足端零惯量占位【本库首个 FAIL 级】/ MJCF mesh 重复定义 13 引 4 / 碰撞全基元厂商风格）；②LICENSES.md 增 Lite3 行（N1 版权逐字）+ 商标补云深处；③顶层 README M2 收录表（7 行）+ 分歧链接三模型 + 复现命令 + 商标。
- **协议⑤送审**（REVIEW-REQUEST.md）：push 放行（ahead 5）+ S7 验收 + **S3 FAIL 处置确认**（零修复披露制 vs 升级专项送审）三决策点，停手等审核台。
- 状态：**M2 全管道（S1–S7）完成，协议⑤触发停手**——审完 push 即 M2 含发布闭环。
- **R15 读毕 → N2 改码备案（立规首执行）**：M2 全程 `pipeline/` 通用改动 4 处，逐处备案——①s1_fetch +4 行（K2 根治落码补全：clone 后写 local core.autocrlf=false，blob-parity 门首战拦截 Lite3.xml 后修）——**非模型特异**；②s4_package `./` 路径规范化 +1 行（Lite3 第三种引用协议变体）——**非模型特异**（通用相对路径卫生）；③s4_package mesh 元素去重 +3 行（Lite3 asset 段 13 引 4 实测触发，F1 同哲学）——**非模型特异**；④s4_package kind 过滤修口径虚胖 + preview.js STL 唯一 URL 计数 + index.html 缓存版本号——**非模型特异**。**口径修正**："管道零改码"准确表述 = **"零模型特异改码"**（4 处均为通用健壮性落码，M0/M1 模型跑回归不受影响——S3/S2 回归全绿旁证）。N2 立规自本条起执行：凡 pipeline/ diff>0 当日备案。
- **协议⑤执行回执（一次生效）**：用户 push 后三源逐位一致 `8a13023`（本地=origin/main=ls-remote），工作树 clean；**远端 45 commit**（M1 收官 36 + M2 九件）；上线链 9 条逐条对上 R15 放行清单（4107fed 启动 → 8a13023 R15 台账/N2 备案）。回执件落档（本地 ahead 1），**停手等 R16 一行收尾 → M2 含发布闭环**。M1 首次"好了"未生效的教训已在 M2 回执流程前置（先实测后说话，一次过）。
- **R16 读毕 → M2 正式闭环收尾**：协议⑤完成（三源 `8a13023`、总数 45=基数 36+9、上线链 9 条逐条核对、R13 专项检查过=R15 节确随队、N2 备案首执行在案）。R16 本条 + 回执 commit 一并 push 收尾（R13 先例，无需新送审）——commit 前 grep 自证 R16 节随队。项目回维护态；M3+ 候选=同仓多机型（DR02/M20 系）/加速进化跨仓配对/智元 NOASSERTION 人工定性（license 定性是前置考题，动前先送）。
