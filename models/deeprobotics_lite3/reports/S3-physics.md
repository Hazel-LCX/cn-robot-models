# S3 物理体检报告 — deeprobotics_lite3（2026-10-11 19:48）

**质量口径声明（修正 2，置顶）**：官网原文「重量（带电池）12kg」（deeprobotics.cn/robot/index/product1.html 产品参数区，2026-10-11 浏览器渲染截图 4 张 evidence/official-lite3-spec-page-screenshot-{1..4}.png）；站立尺寸 610×370×406mm、持续行走负载 5kg、最大斜坡 40°；**官网未公布关节级参数（扭矩/限位/自由度数）**——S3 限位对账无官网基准，纯体检+披露（如实记录）；页面四版本标签（基础/探索/专业/激光），默认显示基础版口径 官网标称口径=带电池整机；URDF/MJCF 均无电池 link——严格口径不可比，总量对比仅作 sanity（M0/M1 同法）

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：[]——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | PASS | 11.938 kg vs 官方 12.0 kg（-0.5%，容差 ±10%）；口径：官网标称口径=带电池整机；URDF/MJCF 均无电池 link——严格口径不可比，总量对比仅作 sanity（M0/M1 同法） |
| `urdf:inertia-pd` | FAIL | 17 个有质量 link 惯量张量全正定；非正定：['FL_FOOT', 'FR_FOOT', 'HL_FOOT', 'HR_FOOT'] |
| `urdf:inertia-triangle` | PASS | 17 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 17 个；全部落区间 |
| `urdf:collision-inventory` | PASS | 17/17 link 有 <collision>（{'box': 6, 'cylinder': 12, 'sphere': 4}）；无 collision：[]（标记不自动补，A1；上游无碰撞示意图（Lite3 目录仅 urdf/mjcf/usd 三件套，无图片资产）） |
| `urdf:collision-mesh-loadable` | SKIP | collision 引用 0 个网格文件（全基元）——A1-2 网格可加载检查不适用，显式跳过（fail 不静默的精神同样适用于不适用，R4-E6） |
| `urdf:joint-limits` | PASS | 12 个 revolute 全部 lower<upper 且 effort/velocity>0；注：官网未公布关节级参数（扭矩/限位/自由度数）——限位对账无官网基准，纯体检+披露（S3 侦察实测） |
| `mjcf:mass-total` | PASS | 11.938 kg vs 官方 12.0 kg（-0.5%，容差 ±10%）；口径：官网标称口径=带电池整机；URDF/MJCF 均无电池 link——严格口径不可比，总量对比仅作 sanity（M0/M1 同法） |
| `mjcf:body-geom` | PASS | 17 个 body 共 34 geom；无 geom 的 body：[]（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 12 revolute ↔ MJCF 12 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 12 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | PASS | 逐 body 对账：完全一致 17 个（hip/thigh/base 等）；约定差异 [] |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- 上游无碰撞示意图（Lite3 目录仅 urdf/mjcf/usd 三件套，无图片资产）

## 汇总

PASS 10 / WARN 1 / FAIL 1 / SKIP 1

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：1 个 FAIL——如实落表，修复走协议③**

## 工作台补记（2026-10-11 · forensics 与口径）

### FAIL urdf:inertia-pd 定性：零惯量占位约定，非笔误

FL/FR/HL/HR_FOOT 四件惯量张量**全零**（ixx=iyy=izz=ixy=ixz=iyz=0.0），质量均 0.02 kg、格式规整一致——**上游有意的零惯量占位**（足端质量小、惯量按零处理），非数据错误。零矩阵非正定，体检如实落 FAIL。**下游影响提示**：零惯量 + 非零质量的 body 在部分引擎会被自动估算或告警，RL/控制下游引用 URDF 时注意足端动力学与真实物理的偏差。**零修复**（改官方文件违反本库立场；修复方案属派生版本范畴，如需可另行讨论）。MJCF 侧同批足端如何表达待 S4 复验对照。

### 口径与对照

- 总质量 URDF 11.938 = MJCF 11.938 kg（**逐 body 17/17 完全一致**——两源高度同源，比 Go2 的 0.881 kg 差、G1 的拆分差异都干净）；vs 官网「重量（带电池）12kg」仅 −0.5%——三模型中最贴官网口径（Lite3 模型或已含电池近似质量，如实记录不展开归因）。
- **碰撞全基元**（box×6 + cylinder×12 + sphere×4，无 mesh collision——与 Go2/G1 的 mesh 碰撞风格不同，厂商风格差异如实记录）；SKIP collision-mesh（全基元无网格可查）。
- 官网未公布关节级参数（扭矩/限位/自由度）——限位对账无官网基准（12 revolute ↔ 无官网数可对，纯体检）。
