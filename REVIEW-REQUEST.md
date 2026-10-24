# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R22 = 协议②通过——M4 选型=加速进化 T1 定案（第五模型/第四厂商），四决策点全批，S1 放行**（BSD-3 活源全验四证、pin 零漂移、树事实逐字复现、源修正三步活源复证；parallel 变体随裁不入库；S1 预警三条照单）。

【送审类型】**协议⑤（M4 S1–S7 全链完成 → push 放行 + S7 验收 + 官方基准缺失处置确认）**——触发即停手，本地 commit 未 push。

【背景：在做什么】R22 读毕即执行 S1–S7 全链（M3 会话 20 同款节奏），**零物理参数修改、纯体检+披露**：

- **S1 拉取**：config 程序化生成（pin 从 evidence 注入，s2 补 package/package_root 两键属配置补全非改码）；直连一次命中 pin `12a97516` **零漂移**（R22 预警③闭合）、69 文件/15.9 MB、**blob-parity 69 件失配 0**（K2 门三战全绿）、A2 license MATCH；**R22 预警①闭合**：URDF/MJCF scale 属性各 **0 处**（grep 实测，L12 立规实践）；引用风格=`meshes/` 前缀 relative（G1 同族第五形态）；网格闭包 25/25 零缺失，38 件未收 STL 身份自洽（踝并联 Crank/Link/Ball + 手部 left/right_Link* + 29dof 臂 AL4-7/AR4-7，2+14+1+12=29 算术自洽）；
- **S2 校验 10/0/0 全绿**：URDF 25 link/24 joint（根=trunk；上游 XML 字面 26/25 含显式 world link+floating joint，yourdfpy 规范化口径如实记录）、MJCF 编译 nbody=26/njnt=24/nq=30/**nu=23** 与 URDF 23 revolute 逐数自洽；
- **S3 体检 7/5/0/SKIP1**：**官方整机基准缺失=本库首例**——官网无 T1 产品页（R22 侦察双页阴性）+ 三官方仓（gym/assets/deploy）README 无质量字段穷尽实测；s3 新增 mass_kg=null WARN 分支（跳过对比**不虚构**，R17 检查点同源），实测总量 URDF 31.738 / MJCF 31.740 kg **仅记录非判据**；仍成立的官方对账=DoF 三方逐位（README 配置表 23 ↔ URDF 23 revolute ↔ MJCF nu=23，booster_deploy README 旁证第三件）；两侧逐 body 23/23 一致（trunk −0.0016 kg 约定差容差内）、23 对关节轴逐分量差 0；URDF 碰撞全基元（box5/cylinder14/sphere1，零 mesh 碰撞）披露；
- **S4 入库**：**52 物理件/17.4 MB 三锚全过**（SHA256↔manifest↔hash-object@pin）、唯一源 27（25 网格双侧落位保持官方结构）+ excluded 4 逐件带 why、38 未收网格逐件列名算式平账（69=5 根级+27 唯一源+4 排除+38 未收中子目录口径）、入库后 recheck 双侧通过；
- **S5 预览零改码**：v4 config 驱动直接吃下第五模型（preview.js/index.html 零 diff）；T1 包围盒 y [0.000, **1.180**]、落地抬升 0.687、断网自检 33 资源全本机外网 0、23 关节滑条、截图 `preview-booster_t1-v1.png`（画面判读：零位双臂平展、头部双关节+相机座、整机闭合无幽灵件）；**四模型基线逐位回归** go2 0.334 / g1 1.323 / lite3 0.298 / x2 1.319 全命中；**R20 挂账执行**：bbox 测量法注明落模型页披露 5（three.js Box3 逐 mesh AABB 并集口径；页 y=1.180 与 yourdfpy scene.bounds z=1.180 逐位同值、落地 0.687 与 z_min −0.687 逐位同值——同法双链互证）；
- **S6 基准**：**36,766 steps/s**（27.2 µs/step）、加载 51.6 ms、展幅 15.9% 稳过——五模型序列第五点（Go2 105k/G1 51k/Lite3 48k/X2 39k），26 body/48 geom 复杂度主导，跨模型不可比再实证；
- **S7 报告**：模型页全文（披露 5 节：官方基准缺失居首/碰撞全基元/网格池 63 收 25/world+floating 口径/测量法注明）；LICENSES.md 加 booster_t1 行+商标补 Booster；LICENSE 第三方层补 BoosterRobotics/Booster 商标；顶层 README 收录行/披露索引/M4 表/预览链接/商标行。

**N2 改码备案（本 leg pipeline/ diff 1 文件 2 处，均通用改动零模型特异）**：①`check_mass_total` 增 mass_kg=null 分支（动因=官方基准缺失的缺失处置，未来同类模型受益）；②main 尾部 caliber 拼接 `.get()` 兜底（①的伴生）。**协议③红线核对：零物理参数修改。**

【决策点】

1. **S7 验收**：模型页/LICENSES/LICENSE/顶层 README 四件与报告数字一致性；S5 测量法挂账执行确认（R20 观察项就此关闭与否请裁定）；
2. **官方基准缺失处置确认**：本库首例"无官网基准机型"——质量对比 WARN 跳过+模型自报值如实披露+DoF 官方对账仍成立的三层处置是否定案（含 s3 通用改码 2 处 N2 备案追认）；
3. **push 放行**：通过即按序 push（本地领先 2 = `9c3fab9` 协议②/S0 + 本件 S1–S7+R22 台账随队）。首选 a=用户亲自 push（回执照 M3 先例实测三源/总数/R13 专项），b 可接受需回执。

【倾向 + 理由】**推荐三项全按上述定案**。理由：①全链数字可重放——R22 三条预警逐项闭合（scale 0 处 grep 实测/闭包 25 零缺失/pin 零漂移），blob-parity 门三战全绿证明管道对第五厂商/第五形态的模型无关性；②官方基准缺失处置是"/license 不明不收录"同源的纪律延伸——缺失不虚构、模型自报值显式降级为记录、仍可对账的 DoF 口径逐位锚死，披露 5 节全部可证据化；③基准/预览/回归数字与四存量模型序列自洽（36.8k 落位第五、基线逐位不动、零改码第五形态兼容）。本件不枚举自身哈希（清单至 `9c3fab9` + 本件随批）。

【文件路径】送审核心：`models/booster_t1/`（README 模型页 + reports/×5 步报告 + urdf/mjcf/images 入库件 + SOURCE.md 待裁→已裁更正）+ `pipeline/configs/booster_t1.json`（新 config）+ `pipeline/s3_physics.py`（N2 备案 2 处）+ LICENSES.md/LICENSE/顶层 README（收录与商标）。台账：REVIEW.md R22 节随队 + DEVLOG 会话 23 续。
