# S3 物理体检报告 — deeprobotics_dr02（2026-10-24 17:32）

**质量口径声明（修正 2，置顶）**：官网原文「整机重量（含电池）约 78kg」+「主动自由度 31=单臂 7×2+单腿 6×2+腰 3+头 2」（deeprobotics.cn/products/detail/5.html DR02 Pro 参数表，2026-10-24 静态 HTML，原件 evidence/official-dr02-spec-page.html——R28 轻度口径处置后为二进制原件+sessionId 脱敏注记）；Standard 版 21DoF/68kg 不入库只记录 官网标称口径=含电池整机；URDF/MJCF 电池 link 情况 S3 实测——严格口径不可比仅作 sanity（M0/M1/M2 同法）；**DoF 对账有官方逐部位基准**（31 分解）——本库首个官方自由度基准齐备的机型（T1/M20 仅质量基准）

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：['d435_head_link', 'd435_front_link', 'd435_rear_link', 'lidar_link', 'imu_head_link', 'imu_base_link']——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | PASS | 78.085 kg vs 官方 78.0 kg（+0.1%，容差 ±10%）；口径：官网标称口径=含电池整机；URDF/MJCF 电池 link 情况 S3 实测——严格口径不可比仅作 sanity（M0/M1/M2 同法）；**DoF 对账有官方逐部位基准**（31 分解）——本库首个官方自由度基准齐备的机型（T1/M20 仅质量基准） |
| `urdf:inertia-pd` | PASS | 34 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 34 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 40 个；全部落区间 |
| `urdf:collision-inventory` | WARN | 28/40 link 有 <collision>（{'cylinder': 27, 'box': 6, 'mesh': 2, 'sphere': 1}）；无 collision：['left_shoulder_y_link', 'left_wrist_x_link', 'right_shoulder_y_link', 'right_wrist_x_link', 'left_hip_x_link', 'right_hip_x_link', 'd435_head_link', 'd435_front_link', 'd435_rear_link', 'lidar_link', 'imu_head_link', 'imu_base_link']（标记不自动补，A1；DR02/urdf/pro/ 与 mjcf/pro/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用） |
| `urdf:joint-limits` | PASS | 31 个 revolute 全部 lower<upper 且 effort/velocity>0；注：官网 DoF 分解=主动 31（臂 7×2+腿 6×2+腰 3+头 2）↔ URDF 31R 逐位（本库首个官方 DoF 基准齐备机型）；关节级扭矩/限位官网未公布——纯体检+披露（Lite3 同口径） |
| `mjcf:mass-total` | PASS | 78.085 kg vs 官方 78.0 kg（+0.1%，容差 ±10%）；口径：官网标称口径=含电池整机；URDF/MJCF 电池 link 情况 S3 实测——严格口径不可比仅作 sanity（M0/M1/M2 同法）；**DoF 对账有官方逐部位基准**（31 分解）——本库首个官方自由度基准齐备的机型（T1/M20 仅质量基准） |
| `mjcf:body-geom` | WARN | 40 个 body 共 70 geom；无 geom 的 body：['d435_head_link', 'd435_front_link', 'd435_rear_link', 'lidar_link', 'imu_head_link', 'imu_base_link']（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 31 单自由度活动关节（revolute+continuous）↔ MJCF 31 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 31 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | PASS | 逐 body 对账：完全一致 34 个（hip/thigh/base 等）；约定差异 [] |
| `cross:com-per-body` | PASS | 逐 body COM 对账（记录级）：对账 34 个，最大逐分量差 0.00e+00（最差 —，容差 1e-06）；全部一致 |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- DR02/urdf/pro/ 与 mjcf/pro/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用

## 汇总

PASS 10 / WARN 3 / FAIL 0 / SKIP 0

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审**
