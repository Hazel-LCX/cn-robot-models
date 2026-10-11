# AGENT-LAB — 写码台失败与自救记录

> 纪律（R1-④ 立规）：每次失败记四要素——现象 / 根因 / 自救动作 / 是否升级 codex 会诊。R2 起审核台查账。

## 2026-10-11 · L9 · K2：blob 正本承诺复发于 M1-S1（审核台首抓）+ 根因实测修正

- **现象**：R11 期中稽查（审核台 95 件独立对账）——go2 33/33 正本 ✓，**g1 入库 62 件中 2 件 CRLF 失真**（mjcf/g1_23dof.xml 32214B/CR×481、scene_23dof.xml 895B/CR×23，上游 blob 31733/872B 全 LF）。K1 刚根治的同类缺陷在 S1 复发。
- **根因（工作台实测修正审核台推测）**：①`git clone -c core.autocrlf=false` **只在 clone 进程内生效、不写入新仓 local config**（实测两仓 local 均未设置）——S1 时"clone -c 持久化"的假设错误；②后续 `sparse-checkout set` 是**独立进程**，读全局 autocrlf=true → sparse 检出的文本件全部 CRLF（mujoco xml×5+md、ros README/motor_info；binary STL/PNG 免疫）；③**意外反转**：g1_23dof.urdf 的上游 blob **原生 CRLF**（851 CR）——检出件=blob 正本纯靠上游原生行尾侥幸，"正本"承诺的本质是"字节=blob 原样"而非"全库 LF"。
- **自救（R11-K2 六步）**：①raw 299 件 cat-file 全量归正（复用 K1 export 脚本参数化）；②manifest 重生成（157.8→150.5 MB，差 = 文本件行尾归正）+ models 两 xml 经 S4 重拷；③S2（10/0/0）+S3（7/5/0）回归全绿；④**根治落码**：s1_fetch 增 blob-parity 门（ls-tree@pin blob id ↔ hash-object --no-filters 批量比对，FAIL 即挡）+ S4 traceability 三锚（models 件 hash-object --no-filters ∈ 上游 blob id 集合）；⑤本条；⑥S1 报告 L48 声明更正。
- **过程新增两课**：①三锚首跑把**已是正本的两 xml 判 FAIL**——manifest 过期（raw 归正后未重生成）与 **hash-object 缺 --no-filters**（主仓 autocrlf 清洗 models 件 id；上游原生 CRLF 件被"合法地"改 id）叠加——**对账工具自身的过滤语义也要对账**；②blob-parity 门首跑自测抓到自家同款缺 --no-filters 假阳性（ros 25 件假失配）——门先测门，再上岗。
- **是否升级**：否。审核台 R11 已给修复清单，全部执行完毕且门落码验证 290/290。
- **立规**：凡 git id 对账一律 `--no-filters`；`clone -c` 的生效范围永远实测（本例：进程内）；S1 拉取后 blob-parity 门是硬门（fail 即挡，不再依赖"克隆卫生"自觉）。

## 2026-10-11 · L8 · autocrlf 第二幕：源头检出失真入库（R10-K1，M0 回溯缺陷）

- **现象**：R10 终裁——上游 blob 全 LF，M0 S1 检出时两克隆 `core.autocrlf=true` 把 62 件检出件转 CRLF，S4 字节复制入库，公开仓库分发 34 件行尾被改文本件（内容级零差异；与本库"不改官方一字节"承诺冲突，非 license 违约）。
- **根因**：L4（第一幕）只修了**库内传播**（.gitattributes 锁 -text，防 clone 再转换），**检出处未关转换**——失真在 M0 第一次检出时就发生了，之后全部对账（manifest/S4/README）锚在衍生物上，"对账即事实"的锚点本身错了，对账错得整整齐齐。
- **自救（R10 七步）**：①两克隆 autocrlf=false + 检出区 62 件按 `cat-file` 全量导出（62/62 == blob 复验；期间发现 `checkout -f` 在 autocrlf 状态混乱时**不重写行尾**且 status 报 clean——git 行尾机制不可信，cat-file 直写才是免疫路径；5 件 PNG 报"CRLF"系二进制数据随机字节，verify 脚本逐件判为上游原生）；②models/ 34 件 blob-exact 替换（逐件前后 SHA256 记档 blob_exact.json，35 件终验全 PASS）；③S4 重跑 traceability 33/33、④S2+S3 回归门重跑无 FAIL（S3 的 4 WARN 均既有处置记录）；⑤SOURCE.md §4 与两处 README 同刷（56,119,567→55,357,945 B）；⑥本条 L8 记档；⑦commit+push（R10 授权）。
- **是否升级**：否。修复全程有 R10 判据与预言（快照哈希 84aac59f/a5d73fc4 逐位命中）背书。
- **顺带立规**：①**哈希/长串肉眼比对从此禁止**（本会话肉眼对锚点连续得出矛盾结论，check_anchors.py 三源裁决一次定案；R9 抓回执错数同根）——数字和长串，机器说了算；②**自产对账脚本发现"CRLF 残留"先判二进制**（`b"\r\n" in data` 对 PNG 无意义）；③K1 后新增铁律：**M1+ 拉取一律 cat-file/检出即正本**，G1 的 S1 按此法执行。

## 2026-10-11 · L7 · M1 侦察 Windows 三连坑（python stub / 反斜杠路径 / 内联转义穿墙变形）

- **现象**：①`curl | python -c` 管道整体 exit 49、零输出；②glob 结果按 `'m1_recon/'` 切分报 IndexError；③`python -c` 内联脚本里 `'\\\\'` 经 bash 双引号穿墙后变成 `'\'`，SyntaxError。
- **根因**：①裸 `python` 命中 WindowsApps 商店占位 stub（真解释器在项目 `.venv`，stub 退出码 49）；②Windows 下 glob 返回反斜杠分隔路径，按正斜杠切分失配；③重演 L6 教训——复杂逻辑内联必死于转义层。
- **自救**：①改用 `.venv/Scripts/python.exe` 显式路径；②路径先归一化反斜杠再切分；③落脚本文件（scan_assets.py / check_anchors.py）不再内联。
- **是否升级**：否。三个均为环境层，无逻辑风险。
- **顺带立规**：**哈希/长串比对自本条起一律程序化**——本会话肉眼比对锚点哈希连续几遍"结果"互相矛盾，改 check_anchors.py 三源裁决（M0 config pin ↔ evidence head 原件 ↔ SOURCE.md 手写值）一次定案全部一致；R9 抓回执错数与本次肉眼错觉同根：数字和长串，机器说了算。

## 2026-10-11 · L6 · R7 清算中的两连小失误（均当场自纠）

- **现象**：①coverage 段重构用了 `s2`/`s4` 短变量——它们只存在于 `build_plan` 作用域，`main` 里 NameError 崩在 coverage，报告停留上轮版本；而排查命令 `2>&1 | grep 关键词` 把 NameError 的 stderr 滤掉了，一度误判"报告没刷新"。②用 sed 修顶层 README 时替换串写错，正文留下 `<?SQL?` 占位符。
- **根因**：①跨作用域改计数逻辑没先 grep 变量定义；②`| grep` 管道会滤掉不含关键词的报错行——排查期不该用过滤管道；③复杂 sed 应换 python 精确替换。
- **自救**：①`grep -n` 定位现文改用 `config["s2"]/["s4"]` 全名重跑；②python `assert in` 替换修复占位符；③coverage 算式终版写平（62 = 9 + 53；53 = 33 + 20，其中 meshes 7）。
- **是否升级**：否。


## 2026-10-11 · L5 · 预览模型"半截沉在网格下"→两轮修复（用户反馈抓出，F1 修复同期）

- **现象**：①用户首报"大半个身子在地平线以下"；②第一版修复后用户再报"没有踏地，悬空了"。
- **根因（两层）**：第一层——URDF base 原点在髋部、足端 z≈−0.32，Z-up 转换只修方向没修位置；第二层（真根因）——落地抬升的包围盒在**初次渲染前**计算，three.js 场景图组装后父级 `matrixWorld` 尚未更新，`Box3.setFromObject`/`expandByObject`（内部 `updateWorldMatrix(false,false)`）拿到陈旧矩阵 → 算出抬升 0.097m（真实需要 0.245m），差值即悬浮量。
- **自救**：v3 = 落地计算挪到滑条初始化之后 + `model.updateMatrixWorld(true)` 强制刷新 + 只按可见网格 bbox；面板上屏"载入版本/抬升量/包围盒"自证；逐 mesh 实测世界 min.y = 0（足端踏地）。
- **是否升级**：否。**教训**：①three.js 在首次渲染前手动算世界包围盒必须先 `updateMatrixWorld(true)`；②连诊断脚本都踩了同一个陈旧矩阵坑——两轮测量互相打脸，最终以"逐 mesh 分解 + updateMatrixWorld"定案。


## 2026-10-11 · L4 · 干净环境实测抓到 autocrlf 破坏哈希承诺（S7，本项目最有价值的一次自查）

- **现象**：git clone 后 six 项哈希抽查 5/6——`three.module.js` 与工作区不一致；它是唯一以 LF 行尾入库的资产，git autocrlf 在 checkout 时把它转成了 CRLF。
- **根因**：Git for Windows 的 autocrlf 对文本文件做行尾转换；上游模型件全为 CRLF，入库起就从未暴露此雷。
- **自救**：`.gitattributes` 对 `models/**`、`pipeline/s5_preview/libs/**`、`workspace/**` 锁 `-text`（凡哈希被报告引用的资产，字节级稳定）+ `git add --renormalize` + 重 clone 复测 **6/6 ✓** 且 clone 内 MJCF 加载 OK。
- **是否升级**：否。**教训**：对承诺"逐哈希溯源"的项目，`.gitattributes` 是第一天就该有的配置——是 S7 干净环境实测（近似新 clone 体验）逼出来的，不是想出来的。
- **顺带**：首跑还抓到"模型页引用的截图忘了 commit"——干净环境实测的价值一晚兑现两次。

## 2026-10-11 · L2 · S5 实现路径决策（R1-④ 必记档）

- **决策点**：vendor 现成 URDFLoader vs B6 退路自写。
- **现象**：jsDelivr npm 路径超时（继 raw 之后第二个被证实的封锁面）；npmmirror registry API 通，但 urdf-loader 的 `latest` 标签停在 0.13.1（真 latest 2.x 未同步/不可验证），依赖链（three 版本匹配 + three-mesh-bvh）在镜像上无法闭合验证。
- **自救/决策**：走 B6 退路——自写 URDF→three 加载器 ~180 行（边界内：XML 解析 + 坐标变换 + 关节交互），DAE 解析 vendor 官方 ColladaLoader/TGALoader + OrbitControls；npmmirror **files API**（`registry.npmmirror.com/<pkg>/<ver>/files/<path>`）单文件拉取，比 tgz 精准且实测可靠。
- **是否升级**：否。

## 2026-10-11 · L3 · 预览页首版三连 bug（浏览器截图自验收抓出）

- **现象**：①calf 滑条初值 0 被浏览器钳位到 -0.44 且标红——calf 的 URDF 限位 [-2.72, -0.84] **不含 0**，零位本身就是非法姿态；②整机侧躺——URDF 是 Z-up、three 是 Y-up，未做坐标转换；③rpy 四元数分量序写反（Euler(p,r,y) 应为 (r,p,y)）。
- **根因**：①默认"0 是合法初值"没查限位；②坐标系惯性思维；③Euler 顺序语义记混。
- **自救**：①初值 clamp(0,lo,hi)，不在限位内取限位中点；②model.rotation.x = -π/2；③分量序修正——两轮浏览器截图复验，站姿正确、红标清零。
- **是否升级**：否。附注：滑条越限标红机制被 bug 意外自证有效（calf 0.00→-0.44 红标亮起即质检元素工作）。


## 2026-10-11 · L1 侦察脚本 TypeError（S3 侦察第一波）

- **现象**：抓官网规格页的 heredoc 脚本在第 9 行抛 `TypeError: 'enumerate' object is not subscriptable`，脚本中断，后续质量对比没跑到。
- **根因**：对 `enumerate()` 生成器直接切片（`enumerate(...)[:10]`）——生成器不支持下标，低级失误。
- **自救**：改为 `list(...)[:10]`（先物化再切片），重跑成功。
- **是否升级**：否。一行修复，无复发风险。
- **顺带记录**：Git Bash 的 grep 是 ugrep，`.{0,160}` 上下文正则触发 "exceeds complexity limits"——同类抓取任务改用 python re，不再用 ugrep 复杂正则（已两次踩到）。
