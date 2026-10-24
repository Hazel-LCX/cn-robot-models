# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R37 = 协议②通过——M9 选型=M20_Piper 定案，四决策点全批，S1 放行**（A4 四重同物、解析器口径逐字全中=R35 新规正面生效、组件页改名/补页令、S1 预警四条）。

【送审类型】**协议⑤（M9 S1–S7 全链完成 → push 放行 + S7 验收 + 全角句号 FAIL 处置与容错改码确认）**——触发即停手，本地 commit 未 push。

【背景：在做什么】R37 读毕即执行轻度口径处置与 S1–S7 全链（本 leg `pipeline/` 改码 2 文件 3 处，N2 备案）：

- **R37 轻度口径处置**：evidence 更名 `official-robot-component-index-page.html`（原"piper-component-page"关联性过强——页面实为通用分类列表页）+ **Piper 独立整机页确认无**（组件分类页 detail 链接 1/2/5/6/7/8/9 全为整机与 J 系列关节、零 Piper 字样，S1 实测）→ SOURCE 补记落档；
- **S1 拉取**：pin `530e01a5` 零漂移（预警④闭合）、61 文件/133.1 MB、**blob-parity 61 件失配 0**（K2 门八战全绿）、A2 MATCH；**分目录网格 27+27 各自全收零未收**（预警①闭合——"闭包差 27"实为两侧分目录各自全收的口径差，非未收）；scale 双侧 0；
- **S2 校验 9 PASS / 1 FAIL / 0 WARN——抓到本库第三个 FAIL 级发现（性质最重：上游数据缺陷）**：**yourdfpy-parse FAIL = URDF L70 `fl_hipx_joint`（左前腿髋侧摆）limit `upper="0。611"` 全角句号 typo**（全文件仅此 1 处；**交叉证据：MJCF 侧同值限位为正常半角 `-0.436 0.611`**——上游两格式独立书写实锤）；**影响面：yourdfpy 用户加载整个 URDF 即抛 ValueError**；MJCF 侧完全不受影响（编译 nbody=28/njnt=25/nq=31/**nu=24**=22 hinge+2 slide 逐数自洽——**prismatic↔slide 映射定案，预警②前半**）；
- **S3 管道容错改码（N2 备案①，模型文件一字不动）**：原 check_joint_limits 的 `float("0。611")` 抛异常中断整条管道——改**逐关节容错**（非数值记 FAIL 点名继续，fail 不静默），重跑 **9 PASS / 3 WARN / 1 FAIL / 0 SKIP**：joint-limits FAIL 如实点名 `fl_hipx_joint`（其余 17 关节正常检查）；**官方整机基准缺失=T1 式处置第二例**（复合体无整机页，实测 39.161 kg 仅记录非判据）；**COM 27/27 全一致**（4.79e-08）+ 逐 body 23/23 一致（四 hipx 舍入级）+ 22 轴差 0 + **collision 27/27 全覆盖（九模型首个）**；
- **S4 入库**：**56 物理件/42.3 MB 三锚全过**、分目录闭包（27×2 两侧同哈希）、usd 5 件 excluded、平账 61=56+5 零未收；**recheck-urdf FAIL 如实保留**（验证对象即加载行为本身，不做容错——同根 typo 第三处检查点表现）；
- **S5 prismatic 滑条落码（N2 备案②③，预警②后半）**：preview.js filter 纳入 prismatic+单位 m（非 rad）+**平移运动学分支**（沿 axis 位移非旋转）+index.html v10；**首载暴露编辑事故即修复**（重复 for 行花括号不平衡 module 解析失败页面卡死——花括号平衡快检定位修复，事故记档 DEVLOG）；重载 **24 滑条全齐**（22 rad + 2 夹爪 "0.00 m"）、包围盒 y [0.000, 0.937]、断网 35 资源 0 外网、截图存档（画面判读：轮足底盘+臂复合体整机闭合无幽灵）；**九模型基线逐位回归全命中**（go2 0.334/g1 1.323/lite3 0.298/x2 1.319/t1 1.180/m20 0.675/dr02 1.792/k1 0.955/t2 1.413）；
- **S6 基准一次过**：**93,447 steps/s**（10.7 µs/step）、加载 105.5 ms、展幅 10.3% 稳过——**序列第三**（28 body/64 geom 碰撞结构简单，复杂度主导再实证）；
- **S7 报告**：M20_Piper 模型页全文（披露 5 节：全角句号 FAIL 居首含下游必读/prismatic 收官/基准分层 T1 式/collision 全覆盖/身高对账既定口径）、LICENSES.md 加 deeprobotics_m20_piper 复指行、顶层 README 收录行/披露索引/M9 表/预览链接。

**N2 改码备案（本 leg pipeline/ diff 2 文件 3 处，均通用改动零模型特异）**：①s3 check_joint_limits limit 非数值容错（未来任何上游数据缺陷不再炸管道）；②preview.js prismatic 支持（filter+单位 m+平移运动学一体）；③index.html v10（②缓存击穿）。**协议③红线核对：零物理参数修改（模型文件一字不动）。**

【决策点】

1. **S7 验收**：模型页/LICENSES 复指行/顶层 README 与报告数字一致性；
2. **全角句号 FAIL 处置与容错改码确认**：①三检查点表现（S2 yourdfpy-parse/S3 joint-limits/S4 recheck-urdf）零修复+交叉证据（MJCF 正常半角）+下游必读提示是否定案（本库第三个 FAIL 级发现，性质最重=加载失败级）；②s3 容错改码（逐关节容错点名继续）是否追认为管道规程（未来上游数据缺陷处置先例）；
3. **push 放行**：通过即按序 push（本地领先 2 = `5f167a6` 协议②/S0 + 本件 S1–S7+R37 台账随队）。首选 a=用户亲自 push（回执照连续先例实测三源/总数/R13 专项），b 可接受需回执。

【倾向 + 理由】**推荐三项全按上述定案**。理由：①R37 四条预警逐项闭合且产生本库最重要的 FAIL 级发现——全角句号 typo 是"上游数据缺陷"类首例（前两例为建模约定/命名冲突），yourdfpy 加载即败的影响面使"质检报告即产品"的价值主张最直观；②s3 容错改码让管道对上游数据缺陷免疫（点名继续不炸），且模型文件一字未动（零修复红线）；③prismatic 拓扑收官+复合体谱系首例+S4 零未收平账，M9 单轮三项结构性资产；④S5 编辑事故未上线即修复+记档，九模型回归逐位不变证明 v10 改码零副作用。本件不枚举自身哈希（清单至 `5f167a6` + 本件随批）。

【文件路径】送审核心：`models/deeprobotics_m20_piper/`（README 模型页 + reports/×5 + urdf/mjcf/images 入库件 + SOURCE.md 含 R37 处置补记 + evidence ×4）+ `pipeline/configs/deeprobotics_m20_piper.json` + `pipeline/s3_physics.py`/`pipeline/s5_preview/preview.js`/`index.html`（N2 备案 3 处）+ LICENSES.md/顶层 README。台账：REVIEW.md R37 节随队 + DEVLOG 会话 23 续（含编辑事故记档）。
