# 国产机器人仿真模型质检管道（cn-robot-models）

> **这不是模型收集站。** 这是一条可复现的开源仿真模型**质检管道**：
> license 核对 → 拉取 → 格式校验 → 物理体检 → 双格式入库 → 在线预览 → 基准 → 质检报告。
> 模型库是管道的副产品，**每一步的检查报告本身就是产品**。
> 已收录：宇树 Go2（M0 质检样板）· 宇树 G1（M1 · 人形）· 云深处 Lite3（M2 · 异厂首录）· 智元灵犀 X2（M3 · 国产开源许可证首例）· 加速进化 T1（M4 · 第四厂商）· 云深处山猫 M20（M5 · 轮足 · continuous 拓扑首覆盖）· 云深处 DR02 Pro（M6 · 人形 1.8 m · 官方 DoF 基准齐备）· 加速进化 K1（M7 · 0.95 m 最小型 · 首个官网产品页直证机型）· 加速进化 T2（M8 · 官网旗舰 · S3 三基准机型）· 云深处 M20_Piper（M9 · 移动操作复合体 · prismatic 拓扑收官）——官方双源 URDF/MJCF（BSD-3-Clause / MulanPSL-2.0）。

## 为什么是"质检管道"而不是"模型库"

网上流传的机器人 URDF/MJCF 大量来自转手改版，质量无人负责。本管道对每个收录模型做
**可复现、可溯源、留痕**的体检：来源锁定 commit、逐文件哈希对账、惯量正定与数量级双重
数学检查、URDF↔MJCF 交叉对账、官方规格口径核对——发现的每一个分歧都"清点 + 记录 +
披露"，绝不静默修复。**价值不在收了几个模型，而在"能证明这些模型可以被信任地加载"。**

- 如果体检发现分歧（M0 发现 calf 质量分歧，M1 发现更多——见各自模型页披露章节）：
  [Go2 · calf 质量/hip 限位](models/unitree_go2/README.md#-已知分歧披露质检的一部分) ·
  [G1 · 官方文件名与自由度不符（g1_23dof.xml 实为 29 关节，两格式动作空间不可互换）/ torso−1.28kg 网格证据链](models/unitree_g1/README.md#-已知分歧披露质检的一部分) ·
  [Lite3 · 四足端零惯量占位（本库首个 FAIL 级发现）/ MJCF mesh 重复定义](models/deeprobotics_lite3/README.md#-已知分歧披露质检的一部分) ·
  [X2 · 徽标件 scale 陷阱（native 3.96 m 大件，上游两格式一致缩放为 12 cm——忽略 scale 的查看器得幽灵几何，本库预览器曾踩坑已修，L12）](models/agibot_x2/README.md#1--agibotstl-徽标件与-scale-陷阱上游两格式一致本库预览器曾踩坑已修) ·
  [T1 · 官方整机基准缺失（本库首例无官网基准机型，质量对比 WARN 披露不虚构）/ 网格池 63 收 25（38 件未收身份自洽）/ URDF 显式 world+floating joint](models/booster_t1/README.md#1--官方整机基准缺失本库首例无官网基准的机型) ·
  [M20 · URDF↔MJCF 腿部质量分布分歧（hipy −0.125/knee +0.115 kg ×四腿，COM 却逐位一致——同仓 Lite3 互补模式）/ continuous 关节拓扑首覆盖](models/deeprobotics_m20/README.md#1--urdfmjcf-腿部质量分布分歧hipy--0125kg--knee--0115kg-四腿本模型核心质检发现) ·
  [DR02 · 引用计数口径更正（grep 39→解析器 36：注释内元素虚增计数）/ 本库首个 collision-mesh 模型 / 身高官方对账 −8mm 姿态差](models/deeprobotics_dr02/README.md#1--引用计数口径更正grep-39--解析器-36l12-家族活案例) ·
  [K1 · 官网域名迁移实证与路径①转正（boosterobotics.com→booster.tech 301，"快照会过期活源才有效"活教材）/ URDF 注释内 world 块虚增结构断言](models/booster_k1/README.md#1--官网域名迁移与-a4-路径①转正本模型核心侦察成果) ·
  [T2 · link/joint 重名 logo（本库第二个 FAIL 级发现，names-unique 首触发，fail 不静默）/ 三基准全对账（质量+DoF+扭矩 140 N·m 本库首个）](models/booster_t2/README.md#1--faillink-与-joint-重名-logo本库第二个-fail-级发现names-unique-首触发) ·
  [M20_Piper · URDF 限位全角句号 `0。611`（本库第三个 FAIL 级发现：上游数据缺陷 yourdfpy 加载即败，MJCF 交叉证据 / 管道容错如实点名）](models/deeprobotics_m20_piper/README.md#1--failurdf-限位含全角句号-0611本库第三个-fail-级发现上游数据缺陷引用前必读)。
- 如果体检全绿：价值落在"管道可复现 + 双格式对账 + 基准数字"——同样的成立。

## 管道

```
S0 license核对(门) → S1 拉取 → S2 格式校验 → S3 物理体检(门:回归) → S4 双格式入库 → S5 3D预览 → S6 基准 → S7 报告
```

- 每步一个脚本（`pipeline/s*.py`），全部 **config 驱动、模型无关**——M1+ 加模型 = 加配置不改代码。
- 每步产出报告（`models/<model>/reports/`），逐项 PASS/WARN/FAIL/SKIP，**fail 不静默**。
- 三份台账：`DEVLOG.md`（滚动日志）、`PIPELINE.md`（管道设计，v0.6a）、`AGENT-LAB.md`（失败与自救档案）。
- 审核协议：管道设计改动 / license 结论 / 物理参数修改等五类事项**停手送审**（PIPELINE.md §8）。

## 已收录模型

### M0 · 宇树 Go2（四足 · 2026-10-11）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | 双仓库 BSD-3-Clause（版权方=宇树本体），官方性双证据链，**已关闭** | [SOURCE.md](models/unitree_go2/SOURCE.md) |
| S1 拉取 | 62 文件锚点锁定（ros@`5994d4fa` + mujoco@`1eb6642e`），逐文件 SHA256 | SOURCE.md §4 |
| S2 格式校验 | **9 PASS / 0 FAIL**：URDF 42 link/41 joint、网格引用 100%、MJCF 真编译 | [S2-validation.md](models/unitree_go2/reports/S2-validation.md) |
| S3 物理体检 | **8 PASS / 4 WARN / 0 FAIL**，零修复纯体检；质量分歧 forensics 闭环到每一克 | [S3-physics.md](models/unitree_go2/reports/S3-physics.md) |
| S4 双格式入库 | 34 文件 / 55.4 MB（33 溯源件 + 1 质检截图 = 55,357,945 B，逐字节 = 上游 blob 正本，K1 行尾归正后口径），dae/meshes 冗余裁决 7/0 | [S4-package.md](models/unitree_go2/reports/S4-package.md) |
| S5 3D 预览 | 断网可开（外网请求 0），12 关节交互滑条（越限标红） | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 105,131 steps/s（9.5 µs/step）**，加载 56 ms，URDF 解析 4.7 ms | [S6-benchmark.md](models/unitree_go2/reports/S6-benchmark.md) |

### M2 · 云深处 绝影 Lite3（四足 · 异厂首录 · 2026-10-11）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | BSD-3-Clause（版权方按快照逐字），**双路径全中**（官网支持页直链 + org 互证，R14 复核升级） | [SOURCE.md](models/deeprobotics_lite3/SOURCE.md) |
| S1 拉取 | 19 文件锚点锁定（`75824b51`），**blob-parity 门首战拦截 CRLF 失真** → clone 后写 local config 根治，15/15 正本 | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 17 link/16 joint、13 处引用（`./meshes/` 第三种协议变体）全解析、MJCF 编译（mesh 元素重复定义如实披露） | [S2-validation.md](models/deeprobotics_lite3/reports/S2-validation.md) |
| S3 物理体检 | **10 PASS / 1 WARN / 1 FAIL / 1 SKIP**：首个 FAIL = 四足端零惯量占位（零修复披露）；两侧质量 17/17 全一致、vs 官网 12kg 仅 −0.5% | [S3-physics.md](models/deeprobotics_lite3/reports/S3-physics.md) |
| S4 双格式入库 | 10 文件 / 7.0 MB **三锚全过**（异厂首战零人工干预），excluded 5 件（usd/） | [S4-package.md](models/deeprobotics_lite3/reports/S4-package.md) |
| S5 3D 预览 | **零改码首跑**（v4 config 驱动直接吃新 config）；STL 4 物理件/13 引用统一着色 | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 47,966 steps/s（20.8 µs/step）**，加载 59.2 ms，展幅 4.9%（同 DOF 异厂商差 2.2× 的 geom 复杂度注记） | [S6-benchmark.md](models/deeprobotics_lite3/reports/S6-benchmark.md) |

### M1 · 宇树 G1（人形 · 2026-10-11）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | 同上游两仓库（与 Go2 同锚点零漂移），BSD-3-Clause，**已关闭（R10）** | [SOURCE.md](models/unitree_g1/SOURCE.md) |
| S1 拉取 | 299 文件锚点锁定（同 go2 锚点），**blob-parity 门**（检出件=上游 blob 逐字节，K2 后硬门） | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 33 link/32 joint、50 处引用全解析 + **大小写逐字节核验失配 0**、MJCF 真编译 | [S2-validation.md](models/unitree_g1/reports/S2-validation.md) |
| S3 物理体检 | **7 PASS / 5 WARN / 0 FAIL**，零修复纯体检；torso −1.28 kg 分歧逐克闭环 + head_link.STL 网格证据链 | [S3-physics.md](models/unitree_g1/reports/S3-physics.md) |
| S4 双格式入库 | 62 文件 / 40.5 MB **三锚全过**（models↔manifest↔上游 blob id），excluded 228 件逐件带 why | [S4-package.md](models/unitree_g1/reports/S4-package.md) |
| S5 3D 预览 | 29 件 STL 统一中性着色（如实标注），包围盒顶 1.323 m ↔ 官网 1320 mm 吻合；**预览页 v4 config 驱动** | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 50,809 steps/s（19.7 µs/step）**，加载 102.8 ms，展幅 2.3% | [S6-benchmark.md](models/unitree_g1/reports/S6-benchmark.md) |

### M3 · 智元灵犀 X2（双足人形 · 国产开源许可证首例 · 2026-10-11）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | **MulanPSL-2.0 人工定性=可收录（R17）**——GitHub NOASSERTION=检测器盲区，按原文定性三件套（blob `adf05533` + SPDX 名录 OSI 认证 + 义务清单），立为本库先例；版权主体行缺失如实注记不虚构 | [SOURCE.md](models/agibot_x2/SOURCE.md) |
| S1 拉取 | 82 文件锚点锁定（`575cc6b9`），**blob-parity 门 78 件失配 0**（K2 门第二次实战全绿）；审核台实测数（72 引/40 唯一/39 link/38 joint/65 stl）独立复现逐项全中 | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 39 link/38 joint（根=pelvis）、72 处引用（`./meshes/` 第四形态确认）全解析 + 大小写失配 0、MJCF 编译 nq=38/nu=31 与 URDF 31 revolute 逐数自洽 | [S2-validation.md](models/agibot_x2/reports/S2-validation.md) |
| S3 物理体检 | **8 PASS / 4 WARN / 0 FAIL**：两侧质量逐 body 32/32 全一致（44.801 kg 同值，vs 官网 39kg +14.9% 口径披露）、31 关节轴逐分量差 0、effort 基准=官网 120 N·m | [S3-physics.md](models/agibot_x2/reports/S3-physics.md) |
| S4 双格式入库 | **83 溯源件 / 158.0 MB 三锚全过** + 2 质检截图；唯一源 43（40 网格双侧落位保持官方 meshdir 结构，MJCF `meshdir`+裸文件名首例零改码兼容）+ excluded 35 逐件带 why | [S4-package.md](models/agibot_x2/reports/S4-package.md) |
| S5 3D 预览 | 31 关节滑条（含头部双关节）；**发现并修复本库预览器 scale 缺陷（AGENT-LAB L12，R18 审核台抓出）**——徽标件 native 3.96 m 曾被按原生渲染成幽灵（URDF/MJCF 实为同 scale 12 cm 徽标，上游无分歧）；修复后含徽标包围盒 **1.319 m ↔ 官网 1.31 m 吻合**，go2/g1/lite3 基线逐位不变 | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 39,086 steps/s（25.6 µs/step）**，加载 454.5 ms，展幅 4.5%（四模型序列第四点，跨模型不可比再实证） | [S6-benchmark.md](models/agibot_x2/reports/S6-benchmark.md) |

### M4 · 加速进化 T1（双足人形 · 第四厂商 · 2026-10-24）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | **BSD-3-Clause 全文在仓=可收录（R22 活源全验）**——专用资产仓 booster_assets 正本（M3 时代"跨仓配对"预设经侦察修正：train 零资产/gym 短格式 Apache 降旁证/assets 最优）；版权行快照逐字 | [SOURCE.md](models/booster_t1/SOURCE.md) |
| S1 拉取 | 69 文件锚点锁定（`12a97516`，直连零漂移），**blob-parity 门 69 件失配 0**（K2 门第三次实战全绿）；引用风格 `meshes/` 前缀（G1 同族）、**URDF/MJCF scale 属性 0 处（R22 预警 grep 实测）**、网格闭包 25/25 零缺失 | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 25 link/24 joint（根=trunk，yourdfpy 规范化 world+floating 口径在案）、25 引用全解析、MJCF 编译 nq=30/**nu=23** 与 URDF 23 revolute 逐数自洽 | [S2-validation.md](models/booster_t1/reports/S2-validation.md) |
| S3 物理体检 | **7 PASS / 5 WARN / 0 FAIL / 1 SKIP**：**官方整机基准缺失=本库首例**（官网无 T1 页，三官方仓 README 无质量字段——mass 对比 WARN 跳过不虚构，总量 31.738/31.740 kg 仅记录）；两侧逐 body 23/23 一致、23 轴差 0；URDF 碰撞全基元披露 | [S3-physics.md](models/booster_t1/reports/S3-physics.md) |
| S4 双格式入库 | **52 物理件 / 17.4 MB 三锚全过** + 1 质检截图；唯一源 27（25 网格双侧落位保持官方结构）+ excluded 4 逐件带 why；38 件未收网格逐件列名身份自洽（踝并联/手部/29dof 配套） | [S4-package.md](models/booster_t1/reports/S4-package.md) |
| S5 3D 预览 | **零改码首跑**（v4 config 驱动吃下第五模型，preview.js/index.html 零 diff）；23 滑条、包围盒 y [0.000, 1.180] 与 yourdfpy 同法互证逐位同值（**测量法注明挂账在此执行**：three.js Box3 逐 mesh AABB 并集口径）；go2/g1/lite3/x2 基线逐位不变 | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 36,766 steps/s（27.2 µs/step）**，加载 51.6 ms，展幅 15.9%（五模型序列第五点，跨模型不可比再实证） | [S6-benchmark.md](models/booster_t1/reports/S6-benchmark.md) |

### M5 · 云深处 山猫 M20（轮足 · 同仓第二机型 · 2026-10-24）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | **同仓单 license 零漂移（R25 三重同物全验）**——快照与 M2 Lite3 逐字节同物 `cdc6c065`，无新定性；A4 继承 M2 双路径全中；官网产品页静态可提取 | [SOURCE.md](models/deeprobotics_m20/SOURCE.md) |
| S1 拉取 | 41 文件锚点锁定（`530e01a5`，活跃仓零漂移），**blob-parity 41 件失配 0**（K2 门四战全绿）；17 引=17 唯一闭包零缺失、scale 0、**网格按格式分目录**（urdf/mjcf 各 17 件） | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 21 link/20 joint（12R+**4 continuous**+4F）、MJCF nq=23/**nu=16** 逐数自洽——**continuous↔unlimited hinge 映射定案（R25 预警①）** | [S2-validation.md](models/deeprobotics_m20/reports/S2-validation.md) |
| S3 物理体检 | **10 PASS / 3 WARN / 0 FAIL / 1 SKIP**：**官方基准恢复**（官网 35 kg，两侧 −1.5%/−1.4% 容差内）；**核心发现=hipy/knee 质量分布两格式分歧（×四腿）而 COM 逐位一致**（R25 裁定②新增 COM 对账 17/17）；16 轴差 0 | [S3-physics.md](models/deeprobotics_m20/reports/S3-physics.md) |
| S4 双格式入库 | **36 物理件 / 23.9 MB 三锚全过** + 1 质检截图；分目录闭包精确全收零未收、excluded 5（usd/ Lite3 先例）；算式最净（41=36+5） | [S4-package.md](models/deeprobotics_m20/reports/S4-package.md) |
| S5 3D 预览 | **continuous 滑条落码**（4 轮关节 ±π 语义，16 滑条；N2 备案）；包围盒 y [0.000, 0.675]；**五模型基线逐位回归全命中**（0.334/1.323/0.298/1.319/1.180） | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 43,867 steps/s（22.8 µs/step）**，加载 62.3 ms，展幅 12.0%（六模型序列第四点，跨模型不可比再实证） | [S6-benchmark.md](models/deeprobotics_m20/reports/S6-benchmark.md) |

### M6 · 云深处 DR02 Pro（人形 1.8 m · 同仓第三机型 · 2026-10-24）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | **同仓单 license 零漂移（R28 三重同物全验）**——快照与 M2/M5 逐字节同物 `cdc6c065`；A4 继承双路径；官网双基准（78 kg + 逐部位 DoF 分解）在案 | [SOURCE.md](models/deeprobotics_dr02/SOURCE.md) |
| S1 拉取 | 129 文件锚点锁定（`530e01a5` 零漂移），**blob-parity 129 件失配 0**（K2 门五战全绿）；网格 114=36+22+34+22 逐位、池外 2 件身份（wrist simplified）、scale 双侧 0；**R28 轻度口径处置：规格页重取二进制原件+sessionId 脱敏** | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 40 link/39 joint（根=base_link）、36 处有效引用全解析（**grep 39 系注释内元素——口径更正在案**）、MJCF nq=38/**nu=31** 与 URDF 31R 逐数自洽 | [S2-validation.md](models/deeprobotics_dr02/reports/S2-validation.md) |
| S3 物理体检 | **10 PASS / 3 WARN / 0 FAIL / 0 SKIP（历次最净）**：**78.085 vs 官网 78 kg（+0.1% 历次最贴）两侧同值**；逐 body 34/34 一致 + COM 34/34 差 0（无 M20 式分歧）；**官方 DoF 基准齐备**（本库首个）；collision-mesh 2 处首见 | [S3-physics.md](models/deeprobotics_dr02/reports/S3-physics.md) |
| S4 双格式入库 | **70 物理件 / 59.8 MB 三锚全过** + 1 质检截图；Pro 侧分目录闭包（36+34 两侧同哈希）；excluded 3（fix_joints+Standard 整组）+未收 56 逐件列名（Standard 网格 44/池外 2/usd 10） | [S4-package.md](models/deeprobotics_dr02/reports/S4-package.md) |
| S5 3D 预览 | 31 滑条、**包围盒 y [0.000, 1.792] ↔ 官网站立 1800 mm（−8 mm 姿态差，人形首个身高官方对账点）**；**六模型基线逐位回归全命中**（0.334/1.323/0.298/1.319/1.180/0.675） | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 110,257 steps/s（9.1 µs/step）——超越 Go2 成序列最快**（全基元碰撞几何简单度主导，"跨模型不可比"再加固），加载 153.8 ms，展幅 3.4% | [S6-benchmark.md](models/deeprobotics_dr02/reports/S6-benchmark.md) |

### M7 · 加速进化 K1（人形 0.95 m · 同仓第二机型线 · 2026-10-24）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | **同仓单 license 零漂移（R31 双重同物全验）**——快照与 M4 T1 逐字节同物 `d7a14af3`；**A4 路径①转正**（官网域名迁移 boosterobotics.com→booster.tech 实证，K1 产品页 336,389 B 逐字节直证=首个官网直证机型） | [SOURCE.md](models/booster_k1/SOURCE.md) |
| S1 拉取 | 56 文件锚点锁定（`12a97516` 与 M4 同 HEAD 零漂移），**blob-parity 56 件失配 0**（K2 门六战全绿）；32 引→24 唯一（8 处复用）、scale 双侧 0、单池 52 件闭包 28 未收身份自洽；**R31 预警②闭合：world+floating 系注释内块（非活元素，与 T1 相反）** | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 25 link/24 joint（根=trunk，22R+2F）、32 处引用全解析、MJCF 编译 nq=29/**nu=22** 与 URDF 22R 逐数自洽 | [S2-validation.md](models/booster_k1/reports/S2-validation.md) |
| S3 物理体检 | **10 PASS / 3 WARN / 0 FAIL / 0 SKIP（连续第二最净档）**：**19.666 vs 官网 19.5 kg（+0.9%）两侧同值**；逐 body 23/23 一致 + COM 23/23 差 0；22 轴差 0；**官方 DoF 三方逐位**（官网+README+URDF）；collision mesh 8 处（第二例） | [S3-physics.md](models/booster_k1/reports/S3-physics.md) |
| S4 双格式入库 | **50 物理件 / 24.0 MB 三锚全过** + 1 质检截图；单池闭包（24×2 两侧落位同哈希）；excluded 2（locomotion+parallel）+未收 28 逐件列名身份自洽 | [S4-package.md](models/booster_k1/reports/S4-package.md) |
| S5 3D 预览 | 22 滑条、**包围盒 y [0.000, 0.955] ↔ 官网"身高约 95 厘米"逐位命中（+5mm 姿态差，身高官方对账第二例）**；**七模型基线逐位回归全命中**（0.334/1.323/0.298/1.319/1.180/0.675/1.792） | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 40,549 steps/s（24.7 µs/step）**，加载 64.8 ms，展幅 19.2%（八模型序列第六点；**首轮展幅 22.4% 超线=本库首次，三轮复跑定案取干净环境轮**，负载源假设如实记档） | [S6-benchmark.md](models/booster_k1/reports/S6-benchmark.md) |

### M8 · 加速进化 T2（人形 1.40 m · 官网旗舰 · S3 三基准机型 · 2026-10-24）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | **同仓单 license 零漂移（R34 三重同物全验）**——快照与 M4/M7 逐字节同物 `d7a14af3`；A4 沿用 K1 转正口径（同域同模板三机型页互证）；**R34 双更正令随 S1 落档**（floating 口径+README 引文失真=断言类轻度两笔在案，规程升级：结构断言与引文必须解析器/活源原文生成） | [SOURCE.md](models/booster_t2/SOURCE.md) |
| S1 拉取 | 40 文件锚点锁定（subdir 直指主版子目录，`12a97516` 零漂移），**blob-parity 40 件失配 0**（K2 门七战全绿）；39 引→37 唯一（2 处复用）、scale 双侧 0、**world 注释块解析器口径验证成立（更正令①管道侧）** | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **9 PASS / 1 FAIL / 0 WARN**：URDF 35 link/34 joint（根=trunk，31R+3F）、39 处引用全解析、MJCF nq=38/**nu=31** 与 URDF 31R 逐数自洽——**names-unique FAIL=link/joint 重名 `logo`（本库第二个 FAIL 级发现，fail 不静默）** | [S2-validation.md](models/booster_t2/reports/S2-validation.md) |
| S3 物理体检 | **10 PASS / 3 WARN / 0 FAIL / 0 SKIP**：**41.994 vs 官网 42 kg（−0.0% 本库最贴逐位）两侧同值**；逐 body 31/31 一致 + COM trunk 7.7e-06 记录级；**三基准全对账**（42kg 星号脚注逐字核对=版本/选配口径） | [S3-physics.md](models/booster_t2/reports/S3-physics.md) |
| S4 双格式入库 | **76 物理件 / 99.1 MB 三锚全过，FAIL 0 / WARN 0（历史最净）**；subdir 直取主版（四手部变体整组天然隔离）+parallel excluded 1；平账全绿 40=39+1 未收为零 | [S4-package.md](models/booster_t2/reports/S4-package.md) |
| S5 3D 预览 | 31 滑条、**包围盒 y [0.000, 1.413] ↔ 官网"身高约 140 厘米"逐位命中（+13mm 姿态差，身高官方对账第三例）**；**八模型基线逐位回归全命中**（0.334/1.323/0.298/1.319/1.180/0.675/1.792/0.955） | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 27,583 steps/s（36.3 µs/step）——九模型序列最慢点**（33 body/55 geom 最复杂，复杂度主导叙事闭环），加载 229.0 ms，展幅 10.2% 一次过 | [S6-benchmark.md](models/booster_t2/reports/S6-benchmark.md) |

### M9 · 云深处 M20_Piper（移动操作复合体 · prismatic 拓扑收官 · 2026-10-24）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | **同仓单 license 零漂移（R37 四重同物全验）**——快照与 M2/M5/M6 逐字节同物 `cdc6c065`；A4 继承三轮双路径；**R37 轻度口径处置在案**（组件页实为通用分类页已更名+Piper 独立整机页确认无） | [SOURCE.md](models/deeprobotics_m20_piper/SOURCE.md) |
| S1 拉取 | 61 文件锚点锁定（`530e01a5` 与 M5/M6 同 HEAD 零漂移），**blob-parity 61 件失配 0**（K2 门八战全绿）；分目录网格 27+27 各自全收零未收、scale 双侧 0 | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **9 PASS / 1 FAIL / 0 WARN**：URDF 27 link/26 joint（根=base_link，18R+4C+**2P**+2F）、37 处引用全解析、MJCF nq=31/**nu=24**（22 hinge+2 slide）逐数自洽——**yourdfpy-parse FAIL=全角句号 typo（本库第三个 FAIL 级发现，披露 1）** | [S2-validation.md](models/deeprobotics_m20_piper/reports/S2-validation.md) |
| S3 物理体检 | **9 PASS / 3 WARN / 1 FAIL / 0 SKIP**：**官方整机基准缺失=T1 式处置第二例**（复合体无整机页，39.161 kg 仅记录）；joint-limits FAIL 同根如实点名（其余 17 关节正常）；**COM 27/27 全一致**、逐 body 23+4 舍入级、22 轴差 0；27/27 collision 全覆盖（九模型首个） | [S3-physics.md](models/deeprobotics_m20_piper/reports/S3-physics.md) |
| S4 双格式入库 | **56 物理件 / 42.3 MB 三锚全过** + 1 质检截图；分目录闭包（27×2 同哈希）；usd 5 件 excluded；**recheck-urdf FAIL 如实保留**（加载验证对象即失败行为，不做容错） | [S4-package.md](models/deeprobotics_m20_piper/reports/S4-package.md) |
| S5 3D 预览 | **prismatic 滑条落码**（joint7/8 夹爪位移单位 m，24 滑条=22 rad+2 m；N2 备案）；包围盒 y [0.000, 0.937]；**九模型基线逐位回归全命中**（0.334/1.323/0.298/1.319/1.180/0.675/1.792/0.955/1.413） | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 93,447 steps/s（10.7 µs/step）——序列第三**（28 body 碰撞结构简单），加载 105.5 ms，展幅 10.3% 一次过 | [S6-benchmark.md](models/deeprobotics_m20_piper/reports/S6-benchmark.md) |

## 快速开始

**在线预览（零依赖，断网可用）**

```bash
python -m http.server 8130
# 浏览器打开 http://127.0.0.1:8130/pipeline/s5_preview/index.html                 # Go2
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=unitree_g1           # G1（人形）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=deeprobotics_lite3  # Lite3（云深处四足）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=agibot_x2            # X2（智元人形；默认视图含上游徽标件——见模型页披露）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=booster_t1           # T1（加速进化人形）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=deeprobotics_m20    # M20（云深处轮足，含 4 轮 continuous 滑条）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=deeprobotics_dr02   # DR02（云深处人形 1.8 m，31 滑条）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=booster_k1           # K1（加速进化教育人形 0.95 m，22 滑条）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=booster_t2           # T2（加速进化旗舰人形 1.40 m，31 滑条）
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=deeprobotics_m20_piper  # M20_Piper（云深处移动操作复合体，22 rad+2 m 滑条）
```

**MuJoCo 查看 / 加载**

```bash
pip install mujoco
python -m mujoco.viewer --mjcf=models/unitree_go2/mjcf/go2.xml
```

```python
import mujoco
model = mujoco.MjModel.from_xml_path("models/unitree_go2/mjcf/go2.xml")
data = mujoco.MjData(model)
mujoco.mj_step(model, data)   # 模型加载与步进就这么多
```

## 复现管道

```bash
# 环境体检（决定 venv / conda，双镜像兜底）
python pipeline/env_check.py
# 各步（按序；S0 是人工 license 核对，见 PIPELINE.md）；<model> = configs/ 下的模型名
python pipeline/s1_fetch.py unitree_g1   # 拉取 + manifest + blob-parity 门
python pipeline/s2_validate.py unitree_g1   # 格式校验（含引用大小写核验）
python pipeline/s3_physics.py unitree_g1    # 物理体检
python pipeline/s4_package.py unitree_g1    # 入库对账（三锚溯源）
python pipeline/s6_bench.py unitree_g1      # 基准
```

## License（双层结构）

- **本库**：MIT（[LICENSE](LICENSE)）。
- **models/ 内上游文件**：属再分发，上游 license 义务随文件走（BSD-3-Clause / MulanPSL-2.0，逐模型见 [LICENSES.md](LICENSES.md)）
  ——上游 license 原文随模型入库（[models/unitree_go2/LICENSE-upstream-*.txt](models/unitree_go2/)）。
- `pipeline/s5_preview/libs/` 内 vendor 的 three.js（MIT）随附其原版 LICENSE。

**商标声明**：Unitree / Go2 / G1 为宇树科技（杭州宇树科技）商标，Deep Robotics / 绝影 / Lite3 为云深处科技商标，AgiBot / 灵犀 X2 为智元机器人商标，Booster / T1 为加速进化（Booster Robotics）商标；本项目非官方、无关联、无背书。

## 目录结构

```
pipeline/        质检脚本（s1–s6 + env_check + configs，模型无关）
models/          入库产物（模型文件 + 报告 + license 快照 + 溯源记录）
workspace/       可丢弃中间态（raw 快照/修复稿，gitignore）
DEVLOG.md        滚动日志    PIPELINE.md 管道设计
AGENT-LAB.md     失败档案    REVIEW.md 审核结论（只读）
```
