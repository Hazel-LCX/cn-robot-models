# S3 物理体检报告 — unitree_go2（2026-10-11 14:44）

**质量口径声明（修正 2，置顶）**：官网 unitree.com/go2 为 JS 渲染，静态页无重量数字（片段已存 evidence/official-go2-spec-page.html.txt）；数值取官方公开规格表约 15kg，建议人工补规格页截图入 evidence/ 官网标称口径（是否含电池）未证实；双方模型均无电池 link——总量对比仅作 sanity，不作为逐 link 真值依据

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：['imu', 'radar']；无 <inertial>：['FL_calflower', 'FL_calflower1', 'FR_calflower', 'FR_calflower1', 'RL_calflower', 'RL_calflower1', 'RR_calflower', 'RR_calflower1', 'front_camera']——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | PASS | 16.087 kg vs 官方 15.0 kg（+7.2%，容差 ±10%）；口径：官网标称口径（是否含电池）未证实；双方模型均无电池 link——总量对比仅作 sanity，不作为逐 link 真值依据 |
| `urdf:inertia-pd` | PASS | 31 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 31 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）17 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 25 个；全部落区间 |
| `urdf:collision-inventory` | WARN | 27/42 link 有 <collision>（{'box': 5, 'cylinder': 17, 'sphere': 5}）；无 collision：['FL_hip_rotor', 'FL_thigh_rotor', 'FL_calf_rotor', 'FR_hip_rotor', 'FR_thigh_rotor', 'FR_calf_rotor', 'RL_hip_rotor', 'RL_thigh_rotor', 'RL_calf_rotor', 'RR_hip_rotor', 'RR_thigh_rotor', 'RR_calf_rotor', 'imu', 'radar', 'front_camera']（标记不自动补，A1；上游对照素材：urdf/ 目录自带 Amended_collision_model.png / Normal_collision_model.png（R4-E3 已 config 化）） |
| `urdf:collision-mesh-loadable` | SKIP | collision 引用 0 个网格文件（全基元）——A1-2 网格可加载检查不适用，显式跳过（fail 不静默的精神同样适用于不适用，R4-E6） |
| `urdf:joint-limits` | PASS | 12 个 revolute 全部 lower<upper 且 effort/velocity>0；注：RL/RR_thigh 行程与 FL/FR 不同（[-0.5236,4.5379] vs [-1.5708,3.4907]，后腿反装镜像，如实记录）（R4-E3 已 config 化） |
| `mjcf:mass-total` | PASS | 15.206 kg vs 官方 15.0 kg（+1.4%，容差 ±10%）；口径：官网标称口径（是否含电池）未证实；双方模型均无电池 link——总量对比仅作 sanity，不作为逐 link 真值依据 |
| `mjcf:body-geom` | WARN | 17 个 body 共 56 geom；无 geom 的 body：['FL_foot', 'FR_foot', 'RL_foot', 'RR_foot']（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 12 revolute ↔ MJCF 12 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 12 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | WARN | 逐 body 对账：完全一致 9 个（hip/thigh/base 等）；约定差异 ['FL_calf_rotor(urdf独有 0.089kg)', 'FL_foot(mjcf零质量纯架，urdf 0.040kg)', 'FL_hip_rotor(urdf独有 0.089kg)', 'FL_thigh_rotor(urdf独有 0.089kg)', 'FR_calf_rotor(urdf独有 0.089kg)', 'FR_foot(mjcf零质量纯架，urdf 0.040kg)', 'FR_hip_rotor(urdf独有 0.089kg)', 'FR_thigh_rotor(urdf独有 0.089kg)', 'Head_lower(urdf独有 0.001kg)', 'Head_upper(urdf独有 0.001kg)', 'RL_calf_rotor(urdf独有 0.089kg)', 'RL_foot(mjcf零质量纯架，urdf 0.040kg)', 'RL_hip_rotor(urdf独有 0.089kg)', 'RL_thigh_rotor(urdf独有 0.089kg)', 'RR_calf_rotor(urdf独有 0.089kg)', 'RR_foot(mjcf零质量纯架，urdf 0.040kg)', 'RR_hip_rotor(urdf独有 0.089kg)', 'RR_thigh_rotor(urdf独有 0.089kg)', 'imu(urdf独有 0.000kg)', 'radar(urdf独有 0.000kg)']；真值分歧 ['FL_calf(0.1540 vs 0.2414, -0.0874)', 'FR_calf(0.1540 vs 0.2414, -0.0874)', 'RL_calf(0.1540 vs 0.2414, -0.0874)', 'RR_calf(0.1540 vs 0.2414, -0.0874)']——MJCF 更贴官方总量，分歧≠错误，M0 不修（修正 6），送审拍板 |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- 上游对照素材：urdf/ 目录自带 Amended_collision_model.png / Normal_collision_model.png

## 汇总

PASS 8 / WARN 4 / FAIL 0 / SKIP 1

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审**
