# S4 入库对账报告 — booster_k1（2026-10-24 22:00）

**物理文件口径（终审 F1 修正）**：入库物理文件 50 = raw 溯源件 50（URDF 引用 32 处 → 网格物理文件 24，引用行 ≠ 文件数） + 质检自产件 0[]；**总 24.0 MB（raw 溯源件 24,002,868 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 24 · mesh 24 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 50 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 32 处引用 → 24 个物理网格 vs MJCF 侧 24 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | WARN | raw 全量 61（除 .git/manifest）= 根级及中间层 5 + 目标子目录 56；子目录 56 全覆盖 = 入库唯一源 26；物理落位 50 件（24 件为双侧同源网格重复落位，同源同内容、两侧引用协议各自独立目录） + 排除 2（其中 meshes/ 冗余 0）（未覆盖：['booster_assets/robots/K1/meshes/Head_2_Collision.STL', 'booster_assets/robots/K1/meshes/Head_2_ZED.STL', 'booster_assets/robots/K1/meshes/K1_left_foot.STL', 'booster_assets/robots/K1/meshes/L1_XX_Ball.STL', 'booster_assets/robots/K1/meshes/L1_X_Ball.STL', 'booster_assets/robots/K1/meshes/L1_Y_Ball.STL', 'booster_assets/robots/K1/meshes/L2_XX_Ball.STL', 'booster_assets/robots/K1/meshes/L2_X_Ball.STL', 'booster_assets/robots/K1/meshes/L2_Y_Ball.STL', 'booster_assets/robots/K1/meshes/Left_Crank_Down.STL', 'booster_assets/robots/K1/meshes/Left_Crank_Up.STL', 'booster_assets/robots/K1/meshes/Left_Foot_Collision.STL', 'booster_assets/robots/K1/meshes/Left_Foot_old.STL', 'booster_assets/robots/K1/meshes/Left_Link_Long.STL', 'booster_assets/robots/K1/meshes/Left_Link_Short.STL', 'booster_assets/robots/K1/meshes/R1_XX_Ball.STL', 'booster_assets/robots/K1/meshes/R1_X_Ball.STL', 'booster_assets/robots/K1/meshes/R1_Y_Ball.STL', 'booster_assets/robots/K1/meshes/R2_XX_Ball.STL', 'booster_assets/robots/K1/meshes/R2_X_Ball.STL', 'booster_assets/robots/K1/meshes/R2_Y_Ball.STL', 'booster_assets/robots/K1/meshes/Right_Crank_Down.STL', 'booster_assets/robots/K1/meshes/Right_Crank_Up.STL', 'booster_assets/robots/K1/meshes/Right_Foot_Collision.STL', 'booster_assets/robots/K1/meshes/Right_Foot_old.STL', 'booster_assets/robots/K1/meshes/Right_Link_Long.STL', 'booster_assets/robots/K1/meshes/Right_Link_Short.STL', 'booster_assets/robots/K1/meshes/Trunk_Collision.STL']）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/K1_22dof.xml 编译通过：nbody=26 ngeom=45 nmesh=24（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：25 links（relative（meshes/ 前缀）——meshes/ 与 urdf 同目录） |

## 逐文件对账（raw 溯源件 50）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/K1_22dof.xml | booster_assets/robots/K1/K1_22dof.xml | `1f1a1cdd451f…` | ✓ |
| mjcf/meshes/Head_1.STL | booster_assets/robots/K1/meshes/Head_1.STL | `9ab00ca2c2ae…` | ✓ |
| mjcf/meshes/Head_2.STL | booster_assets/robots/K1/meshes/Head_2.STL | `ae8f81b864fd…` | ✓ |
| mjcf/meshes/K1logo.STL | booster_assets/robots/K1/meshes/K1logo.STL | `93aab425a2e9…` | ✓ |
| mjcf/meshes/Left_Ankle_Cross.STL | booster_assets/robots/K1/meshes/Left_Ankle_Cross.STL | `1798cb3b9721…` | ✓ |
| mjcf/meshes/Left_Arm_1.STL | booster_assets/robots/K1/meshes/Left_Arm_1.STL | `e1a6de4b34f1…` | ✓ |
| mjcf/meshes/Left_Arm_2.STL | booster_assets/robots/K1/meshes/Left_Arm_2.STL | `b5861bc9f611…` | ✓ |
| mjcf/meshes/Left_Arm_3.STL | booster_assets/robots/K1/meshes/Left_Arm_3.STL | `5424bdfedad4…` | ✓ |
| mjcf/meshes/Left_Arm_4.STL | booster_assets/robots/K1/meshes/Left_Arm_4.STL | `e7de1dc79b85…` | ✓ |
| mjcf/meshes/Left_Foot.STL | booster_assets/robots/K1/meshes/Left_Foot.STL | `1a391f4b3b87…` | ✓ |
| mjcf/meshes/Left_Hip_Pitch.STL | booster_assets/robots/K1/meshes/Left_Hip_Pitch.STL | `ca604e643aaf…` | ✓ |
| mjcf/meshes/Left_Hip_Roll.STL | booster_assets/robots/K1/meshes/Left_Hip_Roll.STL | `aa278205ca75…` | ✓ |
| mjcf/meshes/Left_Hip_Yaw.STL | booster_assets/robots/K1/meshes/Left_Hip_Yaw.STL | `2d8ed37c3a7c…` | ✓ |
| mjcf/meshes/Left_Shank.STL | booster_assets/robots/K1/meshes/Left_Shank.STL | `0e99f5850ba7…` | ✓ |
| mjcf/meshes/Right_Ankle_Cross.STL | booster_assets/robots/K1/meshes/Right_Ankle_Cross.STL | `fd59798e9b4b…` | ✓ |
| mjcf/meshes/Right_Arm_1.STL | booster_assets/robots/K1/meshes/Right_Arm_1.STL | `1dc1518437d0…` | ✓ |
| mjcf/meshes/Right_Arm_2.STL | booster_assets/robots/K1/meshes/Right_Arm_2.STL | `2f7f4bf14aac…` | ✓ |
| mjcf/meshes/Right_Arm_3.STL | booster_assets/robots/K1/meshes/Right_Arm_3.STL | `e3ae9cbd2073…` | ✓ |
| mjcf/meshes/Right_Arm_4.STL | booster_assets/robots/K1/meshes/Right_Arm_4.STL | `4a70e0006cc8…` | ✓ |
| mjcf/meshes/Right_Foot.STL | booster_assets/robots/K1/meshes/Right_Foot.STL | `059b969922a9…` | ✓ |
| mjcf/meshes/Right_Hip_Pitch.STL | booster_assets/robots/K1/meshes/Right_Hip_Pitch.STL | `ab6052ca8f6a…` | ✓ |
| mjcf/meshes/Right_Hip_Roll.STL | booster_assets/robots/K1/meshes/Right_Hip_Roll.STL | `9655e49b0ae1…` | ✓ |
| mjcf/meshes/Right_Hip_Yaw.STL | booster_assets/robots/K1/meshes/Right_Hip_Yaw.STL | `dd54f3cd1cdb…` | ✓ |
| mjcf/meshes/Right_Shank.STL | booster_assets/robots/K1/meshes/Right_Shank.STL | `6a7e83105514…` | ✓ |
| mjcf/meshes/Trunk.STL | booster_assets/robots/K1/meshes/Trunk.STL | `6c2fc1adb1d3…` | ✓ |
| urdf/K1_22dof.urdf | booster_assets/robots/K1/K1_22dof.urdf | `834e17faf468…` | ✓ |
| urdf/meshes/Head_1.STL | booster_assets/robots/K1/meshes/Head_1.STL | `9ab00ca2c2ae…` | ✓ |
| urdf/meshes/Head_2.STL | booster_assets/robots/K1/meshes/Head_2.STL | `ae8f81b864fd…` | ✓ |
| urdf/meshes/K1logo.STL | booster_assets/robots/K1/meshes/K1logo.STL | `93aab425a2e9…` | ✓ |
| urdf/meshes/Left_Ankle_Cross.STL | booster_assets/robots/K1/meshes/Left_Ankle_Cross.STL | `1798cb3b9721…` | ✓ |
| urdf/meshes/Left_Arm_1.STL | booster_assets/robots/K1/meshes/Left_Arm_1.STL | `e1a6de4b34f1…` | ✓ |
| urdf/meshes/Left_Arm_2.STL | booster_assets/robots/K1/meshes/Left_Arm_2.STL | `b5861bc9f611…` | ✓ |
| urdf/meshes/Left_Arm_3.STL | booster_assets/robots/K1/meshes/Left_Arm_3.STL | `5424bdfedad4…` | ✓ |
| urdf/meshes/Left_Arm_4.STL | booster_assets/robots/K1/meshes/Left_Arm_4.STL | `e7de1dc79b85…` | ✓ |
| urdf/meshes/Left_Foot.STL | booster_assets/robots/K1/meshes/Left_Foot.STL | `1a391f4b3b87…` | ✓ |
| urdf/meshes/Left_Hip_Pitch.STL | booster_assets/robots/K1/meshes/Left_Hip_Pitch.STL | `ca604e643aaf…` | ✓ |
| urdf/meshes/Left_Hip_Roll.STL | booster_assets/robots/K1/meshes/Left_Hip_Roll.STL | `aa278205ca75…` | ✓ |
| urdf/meshes/Left_Hip_Yaw.STL | booster_assets/robots/K1/meshes/Left_Hip_Yaw.STL | `2d8ed37c3a7c…` | ✓ |
| urdf/meshes/Left_Shank.STL | booster_assets/robots/K1/meshes/Left_Shank.STL | `0e99f5850ba7…` | ✓ |
| urdf/meshes/Right_Ankle_Cross.STL | booster_assets/robots/K1/meshes/Right_Ankle_Cross.STL | `fd59798e9b4b…` | ✓ |
| urdf/meshes/Right_Arm_1.STL | booster_assets/robots/K1/meshes/Right_Arm_1.STL | `1dc1518437d0…` | ✓ |
| urdf/meshes/Right_Arm_2.STL | booster_assets/robots/K1/meshes/Right_Arm_2.STL | `2f7f4bf14aac…` | ✓ |
| urdf/meshes/Right_Arm_3.STL | booster_assets/robots/K1/meshes/Right_Arm_3.STL | `e3ae9cbd2073…` | ✓ |
| urdf/meshes/Right_Arm_4.STL | booster_assets/robots/K1/meshes/Right_Arm_4.STL | `4a70e0006cc8…` | ✓ |
| urdf/meshes/Right_Foot.STL | booster_assets/robots/K1/meshes/Right_Foot.STL | `059b969922a9…` | ✓ |
| urdf/meshes/Right_Hip_Pitch.STL | booster_assets/robots/K1/meshes/Right_Hip_Pitch.STL | `ab6052ca8f6a…` | ✓ |
| urdf/meshes/Right_Hip_Roll.STL | booster_assets/robots/K1/meshes/Right_Hip_Roll.STL | `9655e49b0ae1…` | ✓ |
| urdf/meshes/Right_Hip_Yaw.STL | booster_assets/robots/K1/meshes/Right_Hip_Yaw.STL | `dd54f3cd1cdb…` | ✓ |
| urdf/meshes/Right_Shank.STL | booster_assets/robots/K1/meshes/Right_Shank.STL | `6a7e83105514…` | ✓ |
| urdf/meshes/Trunk.STL | booster_assets/robots/K1/meshes/Trunk.STL | `6c2fc1adb1d3…` | ✓ |

## 排除清单（config s4.excluded）

- `booster_assets/robots/K1/K1_locomotion.urdf` — 行走裁剪变体（23 link/12R+10F）——R31 锚点=K1_22dof，不入库只记录（T1_locomotion 同类）
- `booster_assets/robots/K1/K1_22dof_parallel.xml` — 并联踝变体 MJCF——R31 锚点=K1_22dof，R22 parallel 已裁先例同款

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 1）
