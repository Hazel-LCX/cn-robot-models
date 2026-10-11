# DEVLOG — 滚动日志

> 纪律：每次会话结束追加一条，新的在上。

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
