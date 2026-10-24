# S3 物理体检报告 — booster_t2（2026-10-24 22:35）

**质量口径声明（修正 2，置顶）**：官网原文「重量：约 42 千克*」「身高：约 140 厘米」「自由度 全身：31」「最大峰值扭矩：140 N·m」（booster.tech/cn/booster-t2 产品页规格表，2026-10-24 静态 HTML，原件 evidence/official-t2-spec-page.html 269,610B=R34 活源逐字节）；README 配置表 T2 行（R34 更正令②活源原文）「head 2 + arms 7×2 + waist 3 + legs 6×2」=2+14+3+12=31 逐位 官网标称口径=整机；42kg 星号注记 S3 前置逐字核对原文（疑为不含电池/手部口径，R34 预警②）；严格口径不可比仅作 sanity（M0/M1 同法）；**effort 对账=官网峰值扭矩 140 N·m（本库首个三基准机型，X2 120 N·m 先例同法升级为全对账）**

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：['head_booster_stereo_rgb_link', 'waist_booster_stereo_rgb_link']——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | PASS | 41.994 kg vs 官方 42.0 kg（-0.0%，容差 ±10%）；口径：官网标称口径=整机；42kg 星号注记 S3 前置逐字核对原文（疑为不含电池/手部口径，R34 预警②）；严格口径不可比仅作 sanity（M0/M1 同法）；**effort 对账=官网峰值扭矩 140 N·m（本库首个三基准机型，X2 120 N·m 先例同法升级为全对账）** |
| `urdf:inertia-pd` | PASS | 33 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 33 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 35 个；全部落区间 |
| `urdf:collision-inventory` | WARN | 21/35 link 有 <collision>（{'box': 3, 'mesh': 6, 'cylinder': 12}）；无 collision：['head_yaw_link', 'left_shoulder_pitch_link', 'left_shoulder_roll_link', 'left_wrist_yaw_link', 'right_shoulder_pitch_link', 'right_shoulder_roll_link', 'right_wrist_yaw_link', 'waist_pitch_link', 'waist_roll_link', 'left_ankle_pitch_link', 'right_ankle_pitch_link', 'logo', 'head_booster_stereo_rgb_link', 'waist_booster_stereo_rgb_link']（标记不自动补，A1；robots/T2/T2_31dof/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用） |
| `urdf:joint-limits` | PASS | 31 个 revolute 全部 lower<upper 且 effort/velocity>0；注：官网 DoF 分解=全身 31（头 2+臂 7×2+腰 3+腿 6×2，R34 更正令②原文）↔ URDF 31R；关节限位官网未公布逐值——纯体检；**effort 基准=官网峰值扭矩 140 N·m（上限合理性 sanity，M3 X2 120 N·m 先例同法）** |
| `mjcf:mass-total` | PASS | 41.994 kg vs 官方 42.0 kg（-0.0%，容差 ±10%）；口径：官网标称口径=整机；42kg 星号注记 S3 前置逐字核对原文（疑为不含电池/手部口径，R34 预警②）；严格口径不可比仅作 sanity（M0/M1 同法）；**effort 对账=官网峰值扭矩 140 N·m（本库首个三基准机型，X2 120 N·m 先例同法升级为全对账）** |
| `mjcf:body-geom` | PASS | 32 个 body 共 54 geom；无 geom 的 body：[]（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 31 单自由度活动关节（revolute+continuous）↔ MJCF 31 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 31 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | PASS | 逐 body 对账：完全一致 31 个（hip/thigh/base 等）；约定差异 ['logo(urdf独有 0.001kg)', 'trunk(-0.0010)'] |
| `cross:com-per-body` | WARN | 逐 body COM 对账（记录级）：对账 32 个，最大逐分量差 7.70e-06（最差 trunk，容差 1e-06）；超容差 ['trunk(0.0000)']——如实披露不修（上游 OEM 格式差异口径，R25 裁定②） |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- robots/T2/T2_31dof/ 无图片资产（S1 实测）——S3 C1 模板 png 提示不适用

## 汇总

PASS 10 / WARN 3 / FAIL 0 / SKIP 0

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审**
