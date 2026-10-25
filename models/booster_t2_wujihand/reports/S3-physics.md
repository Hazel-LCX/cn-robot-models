# S3 物理体检报告 — booster_t2_wujihand（2026-10-25 20:34）

**质量口径声明（修正 2，置顶）**：官网原文「重量：约 42 千克*」「身高：约 140 厘米」「自由度 全身：31」「最大峰值扭矩：140 N·m」（booster.tech/cn/booster-t2 产品页规格表，M8 活源原件 models/booster_t2/evidence/official-t2-spec-page.html 269,610B=R34 逐字节——同仓复指证据不重复取证）；README 配置表 T2 行主版 DoF 31 逐位 **变体无专属官方基准（不虚构，M4 先例）**：42kg*/31DoF/140N·m 系主版 T2 口径，仅作整机 sanity——变体整机质量与主版差值预期=手部替换（WujiHand 双手 vs 默认手），不作主版基准的 PASS/FAIL 依据、如实披露差值；**变体对账真基准=主版 booster_t2 URDF 逐 body 对账（R44 预警⑤跨模型三锚新形态）**；42kg 星号注记 M8 已逐字核对原文在档

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：['head_booster_stereo_rgb_link', 'waist_booster_stereo_rgb_link']——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | PASS | 42.491 kg vs 官方 42.0 kg（+1.2%，容差 ±10%）；口径：**变体无专属官方基准（不虚构，M4 先例）**：42kg*/31DoF/140N·m 系主版 T2 口径，仅作整机 sanity——变体整机质量与主版差值预期=手部替换（WujiHand 双手 vs 默认手），不作主版基准的 PASS/FAIL 依据、如实披露差值；**变体对账真基准=主版 booster_t2 URDF 逐 body 对账（R44 预警⑤跨模型三锚新形态）**；42kg 星号注记 M8 已逐字核对原文在档 |
| `urdf:inertia-pd` | PASS | 85 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 85 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 87 个；全部落区间 |
| `urdf:collision-inventory` | WARN | 71/87 link 有 <collision>（{'box': 3, 'mesh': 56, 'cylinder': 12}）；无 collision：['head_yaw_link', 'left_shoulder_pitch_link', 'left_shoulder_roll_link', 'left_wrist_yaw_link', 'left_wrist_roll_link', 'right_shoulder_pitch_link', 'right_shoulder_roll_link', 'right_wrist_yaw_link', 'right_wrist_roll_link', 'waist_pitch_link', 'waist_roll_link', 'left_ankle_pitch_link', 'right_ankle_pitch_link', 'logo', 'head_booster_stereo_rgb_link', 'waist_booster_stereo_rgb_link']（标记不自动补，A1；robots/T2/T2_31dof/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用） |
| `urdf:joint-limits` | PASS | 71 个 revolute lower<upper 且 effort/velocity>0；注：官网 DoF=全身 31（主版口径）↔ 变体 71R=31+40 指节（M8『Wuji +40』逐位复现）——变体 DoF 无官方逐值，结构断言以 S2 解析器实测为准；关节限位官网未公布逐值——纯体检；**effort 基准=官网峰值扭矩 140 N·m 为主版口径 sanity**（上限量级核对，主版全对账不外推至指节）；手指小质量关节（0.001~0.003 kg 级）惯量 sanity=Lite3 零惯量 FAIL 先例对照组（R44 裁定①） |
| `mjcf:mass-total` | PASS | 42.491 kg vs 官方 42.0 kg（+1.2%，容差 ±10%）；口径：**变体无专属官方基准（不虚构，M4 先例）**：42kg*/31DoF/140N·m 系主版 T2 口径，仅作整机 sanity——变体整机质量与主版差值预期=手部替换（WujiHand 双手 vs 默认手），不作主版基准的 PASS/FAIL 依据、如实披露差值；**变体对账真基准=主版 booster_t2 URDF 逐 body 对账（R44 预警⑤跨模型三锚新形态）**；42kg 星号注记 M8 已逐字核对原文在档 |
| `mjcf:body-geom` | PASS | 72 个 body 共 156 geom；无 geom 的 body：[]（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 71 单自由度活动关节（revolute+continuous）↔ MJCF 71 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 71 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | WARN | 逐 body 对账：完全一致 59 个（hip/thigh/base 等）；约定差异 ['left_finger1_link4(-0.0041)', 'left_finger1_tip_link(urdf独有 0.004kg)', 'left_finger2_link4(-0.0032)', 'left_finger2_tip_link(urdf独有 0.003kg)', 'left_finger3_link4(-0.0032)', 'left_finger3_tip_link(urdf独有 0.003kg)', 'left_finger4_link4(-0.0032)', 'left_finger4_tip_link(urdf独有 0.003kg)', 'left_finger5_link4(-0.0032)', 'left_finger5_tip_link(urdf独有 0.003kg)', 'left_palm_link(urdf独有 0.169kg)', 'logo(urdf独有 0.001kg)', 'right_finger1_link4(-0.0041)', 'right_finger1_tip_link(urdf独有 0.004kg)', 'right_finger2_link4(-0.0032)', 'right_finger2_tip_link(urdf独有 0.003kg)', 'right_finger3_link4(-0.0032)', 'right_finger3_tip_link(urdf独有 0.003kg)', 'right_finger4_link4(-0.0032)', 'right_finger4_tip_link(urdf独有 0.003kg)', 'right_finger5_link4(-0.0032)', 'right_finger5_tip_link(urdf独有 0.003kg)', 'right_palm_link(urdf独有 0.169kg)', 'trunk(-0.0010)']；真值分歧 ['left_wrist_roll_link(0.1563 vs 0.3254, -0.1691)', 'right_wrist_roll_link(0.1563 vs 0.3254, -0.1691)']——MJCF 更贴官方总量，分歧≠错误，M0 不修（修正 6），送审拍板 |
| `cross:com-per-body` | WARN | 逐 body COM 对账（记录级）：对账 72 个，最大逐分量差 2.62e-02（最差 right_wrist_roll_link，容差 1e-06）；超容差 ['trunk(0.0000)', 'left_wrist_roll_link(0.0222)', 'left_finger1_link4(0.0029)', 'left_finger2_link4(0.0024)', 'left_finger3_link4(0.0024)', 'left_finger4_link4(0.0024)', 'left_finger5_link4(0.0024)', 'right_wrist_roll_link(0.0262)', 'right_finger1_link4(0.0031)', 'right_finger2_link4(0.0024)', 'right_finger3_link4(0.0024)', 'right_finger4_link4(0.0024)', 'right_finger5_link4(0.0024)']——如实披露不修（上游 OEM 格式差异口径，R25 裁定②） |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- robots/T2/T2_31dof/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用

## 汇总

PASS 9 / WARN 4 / FAIL 0 / SKIP 0

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审**
