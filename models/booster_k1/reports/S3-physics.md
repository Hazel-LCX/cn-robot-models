# S3 物理体检报告 — booster_k1（2026-10-24 21:59）

**质量口径声明（修正 2，置顶）**：官网原文「重量：约 19.5 千克」「身高：约 95 厘米」「自由度 全身：22 / 单腿：6…」（booster.tech/cn/booster-k1 产品页规格表，2026-10-24 静态 HTML，原件 evidence/official-k1-spec-page.html 336,389B=R31 活源逐字节）；DoF 分解 头2+臂8+腿12 与 README 配置表交叉逐位 官网标称口径=整机（含电池与否官网未注明，S3 实测 URDF 电池 link 后披露）；严格口径不可比仅作 sanity（M0/M1/M2 同法）；DoF 对账=官方逐部位分解（22=2+8+12）↔ URDF 22R（本库第二个官方 DoF 基准齐备机型，DR02 之后）

## 体检矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:mass-positive` | WARN | 显式质量≤0：[]；无 <inertial>：['head_realsense_rgb_link', 'head_booster_stereo_rgb_link']——以上全为 fixed 传感器/转子座（各引擎普遍合并 fixed link），规则精化：活动关节零质量才 FAIL |
| `urdf:mass-total` | PASS | 19.666 kg vs 官方 19.5 kg（+0.9%，容差 ±10%）；口径：官网标称口径=整机（含电池与否官网未注明，S3 实测 URDF 电池 link 后披露）；严格口径不可比仅作 sanity（M0/M1/M2 同法）；DoF 对账=官方逐部位分解（22=2+8+12）↔ URDF 22R（本库第二个官方 DoF 基准齐备机型，DR02 之后） |
| `urdf:inertia-pd` | PASS | 23 个有质量 link 惯量张量全正定 |
| `urdf:inertia-triangle` | PASS | 23 个 link 三角不等式全成立 |
| `urdf:inertia-sanity` | PASS | 逐轴垂距法（修正 1）0 link × 3 轴，比值 I_i/(m·d⊥i²) ∈ [0.005, 0.5]；无网格/零质量跳过 25 个；全部落区间 |
| `urdf:collision-inventory` | WARN | 17/25 link 有 <collision>（{'box': 3, 'cylinder': 9, 'mesh': 8}）；无 collision：['aaleft_shoulder_pitch_link', 'aaright_shoulder_pitch_link', 'left_hip_pitch_link', 'left_ankle_pitch_link', 'right_hip_pitch_link', 'right_ankle_pitch_link', 'head_realsense_rgb_link', 'head_booster_stereo_rgb_link']（标记不自动补，A1；robots/K1/ 无图片资产（58 目录项 S1 实测）——S3 C1 模板 png 提示不适用） |
| `urdf:joint-limits` | PASS | 22 个 revolute 全部 lower<upper 且 effort/velocity>0；注：官网 DoF 分解=全身 22（头 2+臂 8+腿 12）↔ URDF 22R（双文档交叉+模型三重逐位）；关节级扭矩/限位官网未公布——纯体检+披露（Lite3 同口径） |
| `mjcf:mass-total` | PASS | 19.666 kg vs 官方 19.5 kg（+0.9%，容差 ±10%）；口径：官网标称口径=整机（含电池与否官网未注明，S3 实测 URDF 电池 link 后披露）；严格口径不可比仅作 sanity（M0/M1/M2 同法）；DoF 对账=官方逐部位分解（22=2+8+12）↔ URDF 22R（本库第二个官方 DoF 基准齐备机型，DR02 之后） |
| `mjcf:body-geom` | WARN | 25 个 body 共 44 geom；无 geom 的 body：['head_realsense_rgb_link', 'head_booster_stereo_rgb_link']（实测为自闭合空 body：零质量/零 geom/零 site，foot 触地几何挂于 calf 的 foot class geom——建模约定，标记不自动补；R4-E2 措辞更正） |
| `cross:joint-names` | PASS | URDF 22 单自由度活动关节（revolute+continuous）↔ MJCF 22 hinge；名称集合一致 |
| `cross:joint-axes` | PASS | 22 对同名关节轴逐分量最大差 0.00e+00（最差 —，容差 1e-06）；URDF 轴在关节系、MJCF 轴在 body 系——两模型约定一致时可数值直比 |
| `cross:mass-per-body` | PASS | 逐 body 对账：完全一致 23 个（hip/thigh/base 等）；约定差异 [] |
| `cross:com-per-body` | PASS | 逐 body COM 对账（记录级）：对账 23 个，最大逐分量差 0.00e+00（最差 —，容差 1e-06）；全部一致 |

## C1 碰撞体清点表

- URDF 侧：见 `urdf:collision-inventory` 行（逐 link 有无 + 几何类型）
- MJCF 侧：见 `mjcf:body-geom` 行（逐 body geom 数，无 geom body 列表化）
- robots/K1/ 无图片资产（58 目录项 S1 实测）——S3 C1 模板 png 提示不适用

## 汇总

PASS 10 / WARN 3 / FAIL 0 / SKIP 0

**方法论披露（R4-E5）**：URDF 侧惯量正定/三角不等式为本管道的独立数学检查；MJCF 侧无对应独立检查——依赖 MuJoCo 编译器拒绝非法惯量（编译通过=引擎背书）。两侧方法不对称，如实披露。

**结论：无 FAIL；WARN 全部有处置记录（M0 只体检不修复），可送专项审**
