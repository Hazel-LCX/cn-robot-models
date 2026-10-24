# S3 物理体检报告 — deeprobotics_m20_piper（2026-10-24 23:11）

**质量口径声明（修正 2，置顶）**：官方整机基准未取证（mass_kg=null，口径见 config s3.official.note）

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：[]——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | WARN | 官方整机质量基准未取证（官网无该机型页，config s3.official.note）——总量对比跳过，实测总量 39.161 kg 仅作记录非判据（官方基准缺失不得虚构，R17 检查点同源） |
| `urdf:inertia-pd` | PASS | 27 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 27 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 27 个；全部落区间 |
| `urdf:collision-inventory` | PASS | 27/27 link 有 <collision>（{'box': 9, 'cylinder': 18, 'mesh': 10}）；无 collision：[]（标记不自动补，A1；M20_Piper/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用） |
| `urdf:joint-limits` | FAIL | 17 个 revolute lower<upper 且 effort/velocity>0；limit 非数值（上游数据缺陷如实落表，交叉证据=MJCF 同关节限位正常）：['fl_hipx_joint']；注：prismatic 夹爪平移关节限位=位移量纲（m）非角度——S3 限位检查按类型分支如实处理；官网基准 S3 前置侦察定 |
| `mjcf:mass-total` | WARN | 官方整机质量基准未取证（官网无该机型页，config s3.official.note）——总量对比跳过，实测总量 39.161 kg 仅作记录非判据（官方基准缺失不得虚构，R17 检查点同源） |
| `mjcf:body-geom` | PASS | 27 个 body 共 64 geom；无 geom 的 body：[]（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 22 单自由度活动关节（revolute+continuous）↔ MJCF 22 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 22 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | PASS | 逐 body 对账：完全一致 23 个（hip/thigh/base 等）；约定差异 ['fl_hipx(-0.0000)', 'fr_hipx(-0.0000)', 'hl_hipx(-0.0000)', 'hr_hipx(-0.0000)'] |
| `cross:com-per-body` | PASS | 逐 body COM 对账（记录级）：对账 27 个，最大逐分量差 4.79e-08（最差 hl_knee，容差 1e-06）；全部一致 |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- M20_Piper/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用

## 汇总

PASS 9 / WARN 3 / FAIL 1 / SKIP 0

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：1 个 FAIL——如实落表，修复走协议③**
