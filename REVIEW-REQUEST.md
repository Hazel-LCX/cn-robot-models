# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。

【送审类型】**协议⑤ S7 送审（M11 全链）**——R44 四决策点全批放行后，booster_t2_wujihand S1–S7 全链完成件（第十二模型）。

【背景：在做什么】
R44 放行后全链一次推进（全数字程序化，与报告 JSON 同源）：
- **S1**：config 程序化生成（以 booster_t2.json 为基、pin 证据注入、预警六条写入 note）；直连命中 `12a97516`（五战零漂移）、96 文件/52.6 MB、**blob-parity 91 件失配 0**（K2 门十战全绿）、license 快照与主版 sha256 逐位同物 `056db8cc`。
- **S2 = 9 PASS / 1 FAIL / 0 WARN**：URDF 87 link/86 joint=**71R+15F**（lxml 权威）、141 引→87 唯一 100% 解析、87 网格全读通；MJCF nbody=73/njnt=72/nq=78/**nu=71**（71 hinge 全驱动）；**FAIL=names-unique `logo` 跨集重名**（link+joint 联合名字空间重名 2，与主版 M8 发现同款同位置=家族遗传；yourdfpy/MuJoCo 双引擎加载实测可，零修复披露走 M8 先例）。
- **S3 = 9 PASS / 4 WARN / 0 FAIL**：两侧总量 **42.4915 kg 逐位同值**（贵台 R44 独立实测预判逐位命中）vs 官网 42 kg\*（+1.2% sanity）；71 对轴差 0；**预警⑤变体对账新形态首例**：非指节 31R 关节名/类型/轴/effort/**origin** 与主版逐位全同（**预警⑥ head 漂移实测=无**），共享 35 link mass/inertial/visual/collision origin 全量对账差异 6 处全集中 wrist_roll 对——**两件真发现**（a）**ankle_pitch 双侧限位主版↔变体文件间分歧**（变体 −0.8378~+0.5760 vs 主版 −0.6458~+0.3316，各自 URDF↔MJCF 内自洽，官网无逐值）；（b）**wrist_roll 轻量化重设计**（变体 0.156254 vs 主版 0.42548，palm 拆分后组件合计 0.3254 仍轻 0.100 kg+COM 重移+主版有 collision 变体无）；**wrist_roll 变体内 URDF↔MJCF"分歧"=fixed 融合精确闭合**（0.156254+0.16914=0.325394↔0.3254——工具"真值分歧"分类口径更正披露）；无惯量 2 link=传感器座主版同款。
- **S4**：**176 物理件/104.9 MB 三锚全过**、87 网格双侧同哈希分目录落位、唯一源 89=91−2（**池外 2 件=left/right_wrist_roll_link_collision.STL 与主版引用件 hash 同物 `fa648fbdc092`=上游模板复制遗留**，与变体 URDF wrist_roll 无 collision 自洽）、recheck 双侧过。
- **S5**（**R44 改码窗口执行=N2 备案**）：preview.js 页头计数标签细化"滑条 N（xR+yC+zP）"+index.html v11（**R26 遗留"revolute 16"清账**，显示层不动 kinematics）；变体页 **71 滑条（31 体+40 指节）**、断网 93 资源 0 外网、**包围盒 y [0.000, 1.413] 与主版逐位同值**（身高对账随主版）、截图存档画面判读合格；**十一模型基线逐位回归 11/11**（0.334/1.323/0.298/1.319/1.180/0.675/1.792/0.955/1.413/0.937/0.520）；测量卫生记档：IAB HTTP 缓存对贵台 R42 期访问过的 URL 吐旧版 index.html——回归加 cache-buster 后确认 v11 全量生效（首轮"bbox 命中但标签旧版"以此解释）。
- **S6**：**4,997 steps/s（200.1 µs/step，加载 262.7 ms）——十二点序列新末位**（主版 27,583 的 5.5× 慢；njnt 32→72/ngeom 55→157、µs 36.3→200.1 **超线性**=接触对规模效应的结构性观察，不作更深归因）；**展幅 3.2% 稳过（预警④ armed 未触发，无需对照实验）**。
- **S7**：模型页全文（**变体谱系首行+主版互链=条件①**；披露 5 节）；主版页三处更新（互链+配对行+披露 5 升格口径）；LICENSES.md 复指行注明**变体首件入库**（**条件②**）；三变体留池（**条件③**）；顶层 README 收录行/披露索引/M11 表/预览链接；SOURCE 状态行 R44 已批（license 快照措辞落笔前自查更正一次："不重复落快照"与在库每模型八件套形态不符）。

【决策点】
1. **S2 FAIL 处置**：`logo` 跨集重名（家族遗传）零修复+披露（M8 先例同款），双引擎加载实测不阻塞——请确认。
2. **S3 两件真发现处置**：ankle_pitch 限位主版↔变体分歧 + wrist_roll 轻量化重设计——均零修复如实披露+下游提示（协议③红线零物理参数修改）——请确认。
3. **S3 口径**：变体无专属官方基准，42 kg\* 主版口径仅 sanity（+1.2% 不作主版基准 PASS/FAIL 依据，M4 不虚构先例）——请确认。
4. **R44 三条件执行核验**：①谱系首行+双向互链 ✓；②LICENSES 变体首件入库口径行 ✓；③JZ/Revo2/YS 留池不自动跟进 ✓。
5. **S6 序列**：4,997 steps/s（展幅 3.2%）入十二点序列为末位，超线性表述为"结构性观察不作深归因"——是否接受。

【倾向+理由】
全部零修复如实披露（协议③）；变体对账（基座逐位+共享 link 全量+池外件身份）建议记为本库新对账形态（R44 预警⑤的实践完成件）；S6 末位数字如实入序列（跨模型不可比 M2 定案不变，序列仅同法同口径记录）。

【文件路径】
- 模型页：`models/booster_t2_wujihand/README.md`（披露 5 节）；主版互链：`models/booster_t2/README.md`（三处）
- SOURCE：`models/booster_t2_wujihand/SOURCE.md`（R44 已批状态+license 复指）；LICENSES.md 复指行
- 报告：`models/booster_t2_wujihand/reports/`（S1/S2/S3/S4/S6 全套）；截图 `images/preview-booster_t2_wujihand-v1.png`
- 改码窗口 diff（N2 备案同日）：`pipeline/s5_preview/preview.js`（页头标签）+`index.html`（v11）+`pipeline/configs/booster_t2_wujihand.json`（新增）
- 顶层 README：收录行/披露索引/M11 表/预览链接
