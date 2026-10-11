# S3 物理体检报告 — unitree_g1（2026-10-11 18:28）

**质量口径声明（修正 2，置顶）**：官网原文「带电池重量 约35kg」（unitree.com/cn/g1 规格表，2026-10-11 浏览器渲染，截图 4 张 evidence/official-g1-spec-page-screenshot-{1..4}.png + 渲染文本 official-g1-spec-page.txt 互证）；顺带实证：总自由度 23 个关节电机（↔ URDF 23 revolute 精确一致）、膝关节最大扭矩 90N.m（脚注[1]：整机口径下最大关节电机的最大扭矩；EDU 版 120N.m，页面宣传区取 120 同口径自洽）、单腿 6+腰 1+单臂 5（6×2+1+5×2=23 数学自洽）、运动空间 腰 Z±155°/膝 0~165°/髋 P±154°、R-30~+170°、Y±158°（↔ S3 限位对账素材） 官网标称口径=带电池整机（原文实证）；URDF/MJCF 均无电池 link——严格口径不可比，总量对比仅作 sanity，不作逐 link 真值依据（M0 同法）

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：['imu_in_torso', 'imu_in_pelvis', 'd435_link', 'mid360_link']——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | PASS | 34.134 kg vs 官方 35.0 kg（-2.5%，容差 ±10%）；口径：官网标称口径=带电池整机（原文实证）；URDF/MJCF 均无电池 link——严格口径不可比，总量对比仅作 sanity，不作逐 link 真值依据（M0 同法） |
| `urdf:inertia-pd` | PASS | 29 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 29 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 33 个；全部落区间 |
| `urdf:collision-inventory` | WARN | 27/33 link 有 <collision>（{'mesh': 21, 'sphere': 8, 'cylinder': 4}）；无 collision：['pelvis', 'waist_yaw_fixed_link', 'imu_in_torso', 'imu_in_pelvis', 'd435_link', 'mid360_link']（标记不自动补，A1；上游对照素材：images/g1_23dof.png（23dof 配置官方渲染图，配图候选）；images/ 下另有 29dof/29dof_with_hand/dual_arm 三张属未收配置） |
| `urdf:joint-limits` | PASS | 23 个 revolute 全部 lower<upper 且 effort/velocity>0；注：官网「超大关节运动空间」对账基准——腰 Z±155°、膝 0~165°、髋 P±154°/R-30~+170°/Y±158°（规格表原文，evidence/official-g1-spec-page.txt）；URDF 限位逐关节对账见体检表 |
| `mjcf:mass-total` | PASS | 34.137 kg vs 官方 35.0 kg（-2.5%，容差 ±10%）；口径：官网标称口径=带电池整机（原文实证）；URDF/MJCF 均无电池 link——严格口径不可比，总量对比仅作 sanity，不作逐 link 真值依据（M0 同法） |
| `mjcf:body-geom` | WARN | 30 个 body 共 62 geom；无 geom 的 body：['waist_roll', 'waist_pitch', 'left_wrist_pitch', 'left_wrist_yaw', 'right_wrist_pitch', 'right_wrist_yaw']（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | WARN | URDF 23 revolute ↔ MJCF 29 hinge；仅 URDF：[]；仅 MJCF：['left_wrist_pitch_joint', 'left_wrist_yaw_joint', 'right_wrist_pitch_joint', 'right_wrist_yaw_joint', 'waist_pitch_joint', 'waist_roll_joint'] |
| `cross:joint-axes` | PASS | 23 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | WARN | 逐 body 对账：完全一致 21 个（hip/thigh/base 等）；约定差异 ['head_link(urdf独有 1.036kg)', 'left_wrist_roll_rubber_hand(-0.0000)', 'logo_link(urdf独有 0.001kg)', 'pelvis_contour_link(urdf独有 0.001kg)', 'right_wrist_roll_rubber_hand(-0.0000)', 'waist_support_link(urdf独有 0.001kg)', 'waist_yaw_fixed_link(urdf独有 0.244kg)']；真值分歧 ['torso_link(8.5620 vs 9.8420, -1.2800)']——MJCF 更贴官方总量，分歧≠错误，M0 不修（修正 6），送审拍板 |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- 上游对照素材：images/g1_23dof.png（23dof 配置官方渲染图，配图候选）；images/ 下另有 29dof/29dof_with_hand/dual_arm 三张属未收配置

## 汇总

PASS 7 / WARN 5 / FAIL 0 / SKIP 0

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审**
