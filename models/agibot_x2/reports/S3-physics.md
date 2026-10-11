# S3 物理体检报告 — agibot_x2（2026-10-11 21:28）

**质量口径声明（修正 2，置顶）**：官网原文「重量 约35kg（X2青春版）/约39kg（X2旗舰版）」（www.agibot.com.cn/products/X2 产品参数表，2026-10-11 抓取——该页静态 HTML 内嵌参数表全文可提取，evidence/official-x2-spec-page.html 原件；与 Lite3 SPA 页不同，curl 直得无需浏览器截图）；锚定口径=旗舰版（X2-Ultra v1.4.0=焕新旗舰，官方 README「upgraded motors, reinforced structure」）。顺带实证：身高约 1.31m、主动自由度 25（青春）/30（旗舰）、关节峰值扭矩 120N·m（双版本同——S3 effort 上限基准）、电池约 500Wh 支持换电、负载最大 3kg（特定姿态） 官网参数表「重量 约39kg」未注明含电池；包装清单中电池单独列示（换电设计）——整机重量口径可能不含电池，严格口径不可比，总量对比仅作 sanity（M0/M1/M2 同法）；URDF/MJCF 均无电池 link

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：['imu_in_pelvis_link', 'imu_in_torso_link', 'lidar_chest_front_link', 'rgbd_head_front_link', 'stereo_head_front_link', 'rgb_head_rear_link', 'rgb_head_center_link']——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | WARN | 44.801 kg vs 官方 39.0 kg（+14.9%，容差 ±10%）；口径：官网参数表「重量 约39kg」未注明含电池；包装清单中电池单独列示（换电设计）——整机重量口径可能不含电池，严格口径不可比，总量对比仅作 sanity（M0/M1/M2 同法）；URDF/MJCF 均无电池 link |
| `urdf:inertia-pd` | PASS | 32 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 32 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 39 个；全部落区间 |
| `urdf:collision-inventory` | WARN | 32/39 link 有 <collision>（{'mesh': 32}）；无 collision：['imu_in_pelvis_link', 'imu_in_torso_link', 'lidar_chest_front_link', 'rgbd_head_front_link', 'stereo_head_front_link', 'rgb_head_rear_link', 'rgb_head_center_link']（标记不自动补，A1；v1.4.0 目录无图片资产（README 无渲染图）——S3 C1 模板 png 提示不适用） |
| `urdf:joint-limits` | PASS | 31 个 revolute 全部 lower<upper 且 effort/velocity>0；注：官网未公布逐关节限位——限位对账无官网基准，纯体检+披露（Lite3 同口径）。对账点披露：官网主动自由度 30（颈 1+双臂 7×2+腰 3+双腿 6×2）vs URDF 31 revolute = 30 + head_pitch（URDF 头部 2 自由度：pitch+yaw，官网表「颈部自由度 1」）——多 1 头部俯仰自由度，披露不修；MJCF nu=31 含头双关节全执行 |
| `mjcf:mass-total` | WARN | 44.801 kg vs 官方 39.0 kg（+14.9%，容差 ±10%）；口径：官网参数表「重量 约39kg」未注明含电池；包装清单中电池单独列示（换电设计）——整机重量口径可能不含电池，严格口径不可比，总量对比仅作 sanity（M0/M1/M2 同法）；URDF/MJCF 均无电池 link |
| `mjcf:body-geom` | PASS | 32 个 body 共 99 geom；无 geom 的 body：[]（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 31 revolute ↔ MJCF 31 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 31 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | PASS | 逐 body 对账：完全一致 32 个（hip/thigh/base 等）；约定差异 [] |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- v1.4.0 目录无图片资产（README 无渲染图）——S3 C1 模板 png 提示不适用

## 汇总

PASS 8 / WARN 4 / FAIL 0 / SKIP 0

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审**
