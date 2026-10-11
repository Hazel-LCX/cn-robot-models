# PIPELINE — 国产机器人仿真模型库 · 质检管道设计

> **版本** v0.2（2026-10-11）— 落实 R1 必修 A1–A4、吸收建议 B1–B6、四问答复落档、增补审核点协议
> **状态** R1 有条件通过 → v0.2 已送轻复审（REVIEW-REQUEST.md）→ 放行后才动手
> **M0 范围** 宇树 Go2 一个模型走通全管道。含金量在质检工程，不在收集数量。
> **红线** 只收录官方开源发布的模型文件；每个模型先核对并记录 license，再动手。

---

## 0. 写死的设计决策

1. **全程原生 Windows**（Git Bash + Anaconda）。mujoco / trimesh / yourdfpy 均支持 Windows，M0 不碰 WSL，与 C++/ROS 学习线完全隔离。
2. **前端零 node 依赖**（实测机器无 node）：预览是纯静态页 + 本地 three.js（ESM + import map），无构建、无 CDN、离线可用。即便以后装了 node 也不用——单页静态物无构建必要。
3. **管道脚本模型无关**：每步读 `pipeline/configs/<model>.json`，不写死 Go2。M1+ 加模型 = 加配置不改代码。config 含 `format_source: official|converted` 字段（转换件钩子，M0 零转换代码，见 §7-4）。
4. **raw 只读**：`workspace/raw/` 是上游原始快照，之后一切处理只读它；修改稿写 `workspace/patched/`；只有过检文件才进 `models/`。
5. **fail 不静默**：校验失败必须落报告；任何"修复"必须 changelog（文件/位置/改前→改后/理由）+ 用户逐条确认 + 回归重跑（S2+S3 双跑，见 §2）。禁止顺手改设计。
6. **质检报告本身就是产品**：哪怕一个参数都不用修，S2/S3 体检报告就是本项目的主产出。**备两套叙事**：有异常→质检故事；全绿→"管道可复现 + 双格式对账 + 基准数字"同样成立（R1-附 风险2）。
7. **数据源红线**：只用 unitreerobotics 官方 org 的仓库。mujoco_menagerie 等第三方整理库只做交叉参照，不做数据源。
8. **license 优先于一切**：S0 是门，不过门不拉取。license 不明 = 不收录。
9. **完成度 > 规模（铁律，R1-附）**：M0 必须完整闭环出模型页 README；任何情况下不许 M0 做一半就去收第二个模型——那是两头空。
10. **门面立位（R1-附）**：顶层 README 与作品集介绍以"仿真模型质检管道"为主体，模型库是管道的副产品。叙事立错会被归到"资源收集"类，恰是要避开的定位。

## 1. 环境侦察结论（2026-10-11 实测）

| 项 | 结果 | 对设计的影响 |
|---|---|---|
| 项目目录 | 全新开始 | — |
| node | 无 | 预览走纯静态 + 本地 three.js |
| git | 2.55.0.windows.5 | 可用 |
| Python | D:/Anaconda base = **3.14.6（太新）** | mujoco cp314 wheel 存疑 → env_check 第一查；兜底=建 py3.12 专用环境 |
| numpy/scipy/lxml | 已有 | — |
| mujoco/trimesh/yourdfpy | 未装 | S2 前装齐（阿里源） |
| raw.githubusercontent | **不通（被墙）** | 拉取不以 raw 为路径 |
| api.github.com | **通** | 拉取主路径 git clone，兜底 API 逐文件（blob API 支持 >1MB 二进制） |
| jsDelivr | 404 | 不预设可用，S1 现场实测 |

**Go2 官方源（已证实存在，均为官方 org + BSD-3-Clause）**：
- URDF：`unitreerobotics/unitree_ros` → `robots/go2_description/`（`urdf/go2_description.urdf` + `dae/` + `meshes/` + `xacro/`）
- MJCF：`unitreerobotics/unitree_mujoco` → `unitree_robots/go2/`（MJCF xml + **.obj 网格**）
- 注意：两源网格格式不同（dae/stl vs obj），必然不是同一套文件 → 入库时分目录，S4 以 SHA256 实测确认。

## 2. 管道总览

```
S0 license核对(门) → S1 拉取 → S2 格式校验 → S3 物理体检/修复(门:回归) → S4 双格式入库 → S5 3D预览 → S6 基准 → S7 报告收尾
```

两道硬门：**S0 license 门**（不过不拉取）；**S3 回归门**——任何 S3 修复后 **S2 与 S3 双重跑**（S2 验"能加载"，S3 验"物理不超差"，修复本身可能引入新超差；S3 体检表全绿或每项有处置记录才过门）（A3）。

## 3. 分步设计

### S0 License 核对（人工步骤，红线门）
- **定位**：动手前把"能不能收、怎么收"钉死。这步不写代码，用户亲自读 license。
- **输入**：`unitree_ros`、`unitree_mujoco`（已证实 = unitreerobotics 官方 org，SPDX = BSD-3-Clause）
- **输出**：`models/unitree_go2/SOURCE.md`（仓库、commit hash、抓取日期、结论）；`LICENSE-upstream`（license 原文快照，初版可由网页/API 生成）；`LICENSES.md` 索引一行
- **官方 org 验证方法（A4，证据链落字）**：满足其一并记档——
  1. 宇树官网 unitree.com 开发者页/官方文档中链接到 unitreerobotics GitHub org 的证据（URL + 截图 + 日期）；
  2. org 主页自述（官方描述字段）+ 仓库非 fork 状态（GitHub 页面 "forked from" 缺失）截图。
- **子目录声明检查（A2）**：顺带检查 `robots/go2_description/` 与 `unitree_robots/go2/` 内有无独立 LICENSE/README 许可声明，有则一并快照进 SOURCE.md 记录。
- **验收**：
  - [ ] 仓库属 unitreerobotics 官方组织，**按 A4 证据链验证并留痕**（URL + 截图日期）
  - [ ] 两仓库 license 原文快照进模型目录
  - [ ] 三条结论写明：允许再分发？允许修改？是否须保留版权声明？（BSD-3 = 是/是/是）
  - [ ] 网格等二进制跟随仓库同一 license 的假设已记录
  - [ ] 子目录独立声明检查完毕并记录
  - [ ] 用户过目后 SOURCE.md 标"已确认"（**协议②：结论确认走审核台**）

### S1 拉取
- **定位**：拿到干净、可溯源的上游原始件。宁慢勿脏。
- **输入**：S0 定下的 repo + 固定 commit；网络路径链（git clone → GitHub API 逐文件 → 代理，实测选路）
- **输出**：`workspace/raw/unitree_go2/`（所需内容：go2_description + unitree_robots/go2 + **两仓库 LICENSE 及子目录声明文件**）；`manifest.sha256`（逐文件 SHA256/体积/上游路径）；实际路径与 commit 回写 SOURCE.md
- **license 快照复核（A2）**：`models/…/LICENSE-upstream` 最终以 **raw 内同一 commit 的文件为准**生成；SOURCE.md 记录"license 文件 commit hash = 模型文件 commit hash"
- **验收**：
  - [ ] 所有文件出自同一 commit（两仓库各记各的 hash）
  - [ ] manifest 生成，随机抽 3 个文件哈希复算一致
  - [ ] 实际网络路径记录在案
  - [ ] license 快照与模型件同 commit 已复核（A2）
  - [ ] raw 此后只读

### S2 格式校验
- **定位**：证明"文件合法、完整、能加载"。MJCF 的最强校验就是让 MuJoCo 真编译一遍。
- **输入**：raw 快照；环境就绪（mujoco、trimesh、yourdfpy、numpy——`env_check.py` 先行，py3.14 无 wheel 就建 py3.12 专用环境）
- **输出**：`models/unitree_go2/reports/S2-validation.md` + JSON 明细，逐项 pass/warn/fail
- **检查项**：
  - URDF：XML 合法；yourdfpy 解析成功；link/joint 名唯一；关节树无环、单根；网格引用 100% 可解析（**package:// 是 ROS 包路径，脱 ROS 打不开是常态——校验器把包名重映射到本地目录，这是第一坑**）；网格非零字节且 trimesh 能读出顶点数
  - MJCF：XML 合法；`mujoco.MjModel.from_xml_path()` 编译零 error（warning 逐条记录）
- **验收**：
  - [ ] URDF 解析零 error；MJCF 编译零 error
  - [ ] 网格引用 100% 解析
  - [ ] 全部 warning 列表化；fail 不许静默跳过（修复留 S3，先如实记录）

### S3 物理参数核对 / 修复
- **定位**：证明"物理参数是真的、自洽的"。修不修是结论，体检本身就是产出。
- **输入**：S2 通过的模型；官方标称来源（宇树官网 Go2 页面，抓取时存档链接；整备质量 ≈15 kg 量级，以官网页面实测为准）
- **输出**：`reports/S3-physics.md` 体检表；若有修复：`CHANGELOG.md`（文件/位置/改前→改后/理由/证据）+ 修复稿放 `workspace/patched/`
- **检查项**：
  - 每个 link 质量 > 0
  - 总质量 vs 官方标称（容差 ±10%，超差只标记不自动改）
  - 惯量张量：正定（特征值全 >0）+ 三角不等式（Ixx+Iyy≥Izz 等）
  - **惯量数量级 sanity（B1）**：主惯量 vs m·L²（L = 该 link 网格包围盒特征长度）的比值落合理区间（0.01–1 起步，容差实测后定）——抓"正定但整体错 100 倍"这类正定+三角不等式抓不住的错
  - **碰撞体检查（A1，三件）**：
    1. URDF：逐 link 清点 `<collision>` 存在性，无 collision 的 link 列表化（**只标记，不自动补**）；
    2. collision 引用的网格 trimesh 可加载、顶点数 > 0；visual 与 collision 网格差异记录在案（官方源常见 collision 低模/visual 高模，差异本身就是质检素材）；
    3. MJCF：逐 body 清点 geom，无 geom 的 body 列表化。
    定位同其他项：**清点 + 记录 + 异常标记**，M0 无官方对照物故不要求修复。
  - 12 个旋转关节（每腿 3：髋外展/大腿/小腿 × 4）全部有位置限位；力矩/速度限位字段存在
  - URDF vs MJCF 交叉对账：同名关节、质量/轴向一致（容差实测后定）
- **验收**：
  - [ ] 体检表全绿，或每个问题有处置记录
  - [ ] 每处修复一条 changelog + 用户逐条确认（**协议③：改物理参数走审核台，附改动值+依据**）
  - [ ] **回归门（A3）：修复稿重跑 S2 与 S3 双通过**，S3 全绿或每项有处置记录
  - [ ] 碰撞体清点表已入报告（无 collision 的 link 清单 + visual/collision 差异表 + 无 geom 的 body 清单）（C1）
  - [ ] 无"顺手优化"——不改任何非必要参数

### S4 双格式入库
- **定位**：把过检文件按最终结构入库，每个文件可溯源。
- **输入**：raw（官方原件）+ S3 修复稿（若有，替换对应文件）；config `format_source: official`（M0 两源皆官方件）
- **输出**：`models/unitree_go2/{urdf/, mjcf/, urdf_meshes/, mjcf_meshes/}`；provenance 写入模型 README；SOURCE.md 补齐文件对账
- **网格策略**：两源网格逐文件 SHA256 对比，完全相同才合并共享；预期不同（dae/stl vs obj）则分目录，决策与仓库总体积记录在案
- **验收**：
  - [ ] 两格式各自能再被加载器读取（复跑 S2 最小版）
  - [ ] 目录与 manifest 对账：无多文件、无缺文件
  - [ ] 每个文件可溯源（上游路径 + commit）
  - [ ] 网格分/合决策 + 总体积已记录

### S5 Three.js 在线 3D 预览
- **定位**：让"看模型"零门槛——打开浏览器就能转着看。
- **输入**：入库后的 URDF + 网格；three.js 本地库文件（镜像/代理下载进 `pipeline/s5_preview/libs/` 并随仓库提交，保证离线）
- **输出**：`pipeline/s5_preview/`（index.html + preview.js + libs/）；`python -m http.server` 起本地服务
- **功能**：加载入库真实文件；轨道控制（旋转/缩放/平移）；显示链接/关节结构（点击高亮可选）
- **实现路径**：优先 vendor 现成 URDFLoader；若依赖链受阻，退路 = 自写 URDF→three 场景加载器。**退路边界（B6）：自写部分只限 URDF XML 解析 + 坐标变换，DAE/STL 解析不自写——ColladaLoader/STLLoader 随 three 一并本地 vendor，不把工作量烧在胶水格式上。**走哪条必记 AGENT-LAB.md。
- **验收**：
  - [ ] 断网可开：页面零外网请求（浏览器 Network 面板核对，这本身就是质检动作）
  - [ ] 拓扑正确：四腿、站姿正常、无网格缺失发黑
  - [ ] 页面读取的就是 models/ 入库文件（相对路径可核对）
  - [ ] 用户截图确认

### S6 加载 / 步速基准
- **定位**：用数字说话，可复现的跑法。
- **输入**：入库模型；本机信息
- **输出**：`reports/S6-benchmark.md` + `benchmark.json`；README 表格数据
- **指标**：
  - MJCF：MuJoCo 加载耗时；`mj_step` **先预热 ≥100 步丢弃再计时（B2）**，计时段 ≥10⁴ 步或分多轮循环取中位数（固定初始姿态、纯重力、无控制器——姿态会倒是预期，测的是引擎步进吞吐）；重复 ≥5 次取中位数
  - URDF：yourdfpy 解析耗时（如实标注：URDF 无物理引擎，只测加载）
  - 预览页：首帧加载耗时（performance API）
- **验收**：
  - [ ] bench 脚本可重复运行；两次运行中位数差 < 20%（超了记录波动原因）
  - [ ] 报告含 CPU/内存/Python/MuJoCo 版本
  - [ ] 一句话结论写进模型 README

### S7 README 质检报告 + 收尾
- **定位**：一站式闭环——陌生人 clone 下来照 README 就能用。
- **输入**：S0–S6 全部产物
- **输出**：
  - `models/unitree_go2/README.md`（模型页：截图、来源、license、质检结论、基准表、5 行 mujoco 加载示例、**MJCF 查看命令（B4）**：`python -m mujoco.viewer --mjcf=models/unitree_go2/mjcf/go2.xml`）
  - 顶层 `README.md`（**以"仿真模型质检管道"为主体，模型库是副产品（R1-附）**：管道图、质检汇总表、模型索引；两套叙事见 §0-6）
  - **商标声明（B3，必写）**：README 注明"Unitree / Go2 为宇树科技商标，本项目非官方、无关联、无背书"。BSD-3 授版权不授商标。
  - LICENSES.md 双层结构：本库 MIT + 逐模型上游 BSD-3 原文与版权声明随行（models/ 内上游文件属再分发，义务随文件走）
- **验收**：
  - [ ] README 每个数字可指到某个 report 文件
  - [ ] 干净环境实测：删 workspace 重跑验证脚本 + 照模型页示例加载成功（近似"新 clone 体验"）
  - [ ] 商标声明在位（B3）
  - [ ] MJCF 查看命令实测可用（B4）
  - [ ] LICENSES.md 与各 SOURCE.md 一致

## 4. 文件结构

```
cn-robot-models/
├── DEVLOG.md                  # 滚动日志（已建）
├── PIPELINE.md                # 本文档（已建）
├── AGENT-LAB.md               # 写码台失败与自救记录（首次失败时建）
├── REVIEW.md                  # 审核台地盘，只读禁改
├── REVIEW-REQUEST.md          # 送审材料（协议触发时由工作台写，审核台标注已审）
├── incident.md                # 同一问题第 3 次未解决时的复盘档案（协议④）
├── README.md                  # S7 产出：质检管道为主体 + 质检汇总
├── LICENSES.md                # S0 起：双层结构（本库 MIT + 逐模型上游声明）
├── .gitignore                 # 动手第0步建
├── pipeline/
│   ├── requirements.txt       # 依赖清单
│   ├── env_check.py           # 动手第0步：环境体检（完成后送代码首审）
│   ├── configs/
│   │   └── unitree_go2.json   # 模型配置：来源/路径/容差/format_source
│   ├── s1_fetch.py
│   ├── s2_validate.py
│   ├── s3_physics.py
│   ├── s4_package.py
│   ├── s6_bench.py
│   ├── run_all.py             # 串联各步，门处停下等确认
│   └── s5_preview/
│       ├── index.html
│       ├── preview.js
│       └── libs/              # 本地 three.js（随仓库提交，保证离线）
├── models/
│   └── unitree_go2/
│       ├── SOURCE.md          # S0 产出
│       ├── LICENSE-upstream   # 上游 license 原文快照（以 raw 同 commit 文件为准）
│       ├── urdf/              # 入库 URDF
│       ├── mjcf/              # 入库 MJCF
│       ├── urdf_meshes/       # 预期分目录（dae/stl）
│       ├── mjcf_meshes/       # （obj）
│       ├── reports/           # S2/S3/S6 报告
│       └── README.md          # S7 产出：模型页
└── workspace/                 # 可丢弃中间态（gitignore）
    ├── raw/unitree_go2/       # 上游原始快照，只读
    └── patched/unitree_go2/   # S3 修复稿
```

## 5. 节奏与讲解映射（作品工作台模式）

每步脚本 = 一个"模块"：写完逐段讲解 → 用户复述确认 → 才算完成、进下一步。

- 会话 A（动手第0步）：git init + .gitignore + **独立环境**（env_check 定：mujoco 有 cp314 wheel 则 venv，否则 conda py3.12）+ requirements.txt + env_check.py（顺带讲：为什么环境隔离）。**env_check.py 完成后送代码首审（R1 ⑤，立风格基线）**。
- 会话 B：S0 你读 license 陪跑 + s1_fetch.py
- 会话 C：s2_validate.py（重头戏一：package:// 坑）
- 会话 D：s3_physics.py（重头戏二：惯量数学 + 碰撞体清点）
- 会话 E：s4_package.py（薄，和 S3 复盘一起过）
- 会话 F：s5_preview（html + js 逐段讲）
- 会话 G：s6_bench.py
- 会话 H：S7 收尾 + 干净环境实测

预估 7–8 个会话。

**AGENT-LAB 记档规矩（R1 ④）**：每次失败记四要素——现象 / 根因 / 自救动作 / 是否升级 codex 会诊；S5 实现路径选择（vendor URDFLoader vs 自写）必须记档。R2 起审核台查账。

## 6. 风险

1. Python 3.14 太新，mujoco 可能无 cp314 wheel → 兜底：conda 建 py3.12 专用环境（env_check 现场定）
2. git clone github.com 可能也被墙（api.github.com 通不等于 git 协议通）→ 兜底：GitHub API blob 逐文件（支持 >1MB 二进制）
3. yourdfpy 非 ROS 官方解析器，极端写法可能误判 → 记录局限；WSL 侧 check_urdf 可作仲裁（M0 默认不启用）
4. jsDelivr 实测 404 → 不预设可用，S1 以实测为准
5. go2 官方件可能全绿无异常 → "报告即产品"两套叙事预案（§0-6），README 都要能讲

## 7. 已拍板事项（R1 答复落档）

1. **本库 license = MIT**。附加：B3 商标声明必写；LICENSES.md 双层结构（本库 MIT + 逐模型上游 BSD-3 原文与版权声明随行，义务随文件走）。
2. **M0 不加 PyBullet**：多一个引擎多一套依赖面与解释成本，且两引擎步速数字互不可比，对"用数字说话"反而掺沙。
3. **网格 SHA256 实测定，默认保守分目录**。
4. **URDF→MJCF 转换仅配置层留钩子**：config 加 `format_source: official|converted` 字段，provenance 标"转换件"。M0 一行转换代码都不写。

## 8. 审核点协议（2026-10-11 用户补充，原文照抄）

> 以下情况触发时，你必须立即停手，不再写任何代码：
> ①管道设计/文件结构/技术选型要改动；②任何模型的 license 核对结论；
> ③要修改模型物理参数时（改动值+依据）；④同一问题第 3 次未解决（配合
> incident.md）；⑤git push 公开仓库、README 定稿、部署上线。
>
> 触发后的固定动作，一步不能少：
> 1. 停止当前任务；
> 2. 在项目根写 REVIEW-REQUEST.md，五段格式：
>    【送审类型】【背景：在做什么】【决策点：需要拍板的具体选项】
>    【我的倾向+理由】【相关文件路径】；
> 3. 对我说这句固定话术："⛔ 审核点已触发，送审材料在 REVIEW-REQUEST.md，
>    请转审核台，审完我会从 REVIEW.md 读结论再继续。"
>
> 另外每次会话开始，先读 REVIEW.md 里有没有新审核结论、DEVLOG.md 最后
> 一条恢复现场，再开始干活。

## 9. 版本记录

- **v0.1**（2026-10-11）：设计稿，零代码，环境侦察 + S0–S7 全设计。
- **v0.2**（2026-10-11）：R1 有条件通过后修订——A1 S3 补碰撞体检查三件；A2 license 快照同 commit + 子目录声明检查；A3 回归门改 S2+S3 双跑；A4 官方 org 证据链落字；B1 惯量数量级 sanity；B2 基准预热 + ≥10⁴ 步；B3 商标声明；B4 MJCF 查看命令；B5 会话 A 独立环境口径；B6 自写加载器边界；四问答复落档 §7；§0 增完成度铁律与门面立位；§8 增审核点协议（原文）。
- **v0.3**（2026-10-11）：R2 通过放行后吸收执行提示 C1——S3 验收增"碰撞体清点表入报告"勾选项；C2（修复项批量送审）、C3（S0 结论天然触发协议②）为流程行为，不改文档。
