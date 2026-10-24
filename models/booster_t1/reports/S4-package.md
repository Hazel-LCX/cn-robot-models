# S4 入库对账报告 — booster_t1（2026-10-24 15:43）

**物理文件口径（终审 F1 修正）**：入库物理文件 52 = raw 溯源件 52（URDF 引用 25 处 → 网格物理文件 25，引用行 ≠ 文件数） + 质检自产件 0[]；**总 17.4 MB（raw 溯源件 17,359,815 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 25 · mesh 25 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 52 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 25 处引用 → 25 个物理网格 vs MJCF 侧 25 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | WARN | raw 全量 74（除 .git/manifest）= 根级及中间层 5 + 目标子目录 69；子目录 69 全覆盖 = 入库唯一源 27；物理落位 52 件（25 件为双侧同源网格重复落位，同源同内容、两侧引用协议各自独立目录） + 排除 4（其中 meshes/ 冗余 0）（未覆盖：['booster_assets/robots/T1/meshes/AL4.STL', 'booster_assets/robots/T1/meshes/AL5.STL', 'booster_assets/robots/T1/meshes/AL6.STL', 'booster_assets/robots/T1/meshes/AL7.STL', 'booster_assets/robots/T1/meshes/AR4.STL', 'booster_assets/robots/T1/meshes/AR5.STL', 'booster_assets/robots/T1/meshes/AR6.STL', 'booster_assets/robots/T1/meshes/AR7.STL', 'booster_assets/robots/T1/meshes/Crank_Down_Left.STL', 'booster_assets/robots/T1/meshes/Crank_Down_Right.STL', 'booster_assets/robots/T1/meshes/Crank_Up_Left.STL', 'booster_assets/robots/T1/meshes/Crank_Up_Right.STL', 'booster_assets/robots/T1/meshes/Down_Left_XX_Ball.STL', 'booster_assets/robots/T1/meshes/Down_Left_X_Ball.STL', 'booster_assets/robots/T1/meshes/Down_Left_Y_Ball.STL', 'booster_assets/robots/T1/meshes/Down_Right_XX_Ball.STL', 'booster_assets/robots/T1/meshes/Down_Right_X_Ball.STL', 'booster_assets/robots/T1/meshes/Down_Right_Y_Ball.STL', 'booster_assets/robots/T1/meshes/Link_Long_Left.STL', 'booster_assets/robots/T1/meshes/Link_Long_Right.STL', 'booster_assets/robots/T1/meshes/Link_Short_Left.STL', 'booster_assets/robots/T1/meshes/Link_Short_Right.STL', 'booster_assets/robots/T1/meshes/Up_Left_XX_Ball.STL', 'booster_assets/robots/T1/meshes/Up_Left_X_Ball.STL', 'booster_assets/robots/T1/meshes/Up_Left_Y_Ball.STL', 'booster_assets/robots/T1/meshes/Up_Right_XX_Ball.STL', 'booster_assets/robots/T1/meshes/Up_Right_X_Ball.STL', 'booster_assets/robots/T1/meshes/Up_Right_Y_Ball.STL', 'booster_assets/robots/T1/meshes/left_Link1.STL', 'booster_assets/robots/T1/meshes/left_Link11.STL', 'booster_assets/robots/T1/meshes/left_Link2.STL', 'booster_assets/robots/T1/meshes/left_Link22.STL', 'booster_assets/robots/T1/meshes/left_base_link.STL', 'booster_assets/robots/T1/meshes/right_Link1.STL', 'booster_assets/robots/T1/meshes/right_Link11.STL', 'booster_assets/robots/T1/meshes/right_Link2.STL', 'booster_assets/robots/T1/meshes/right_Link22.STL', 'booster_assets/robots/T1/meshes/right_base_link.STL']）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/T1_23dof.xml 编译通过：nbody=26 ngeom=48 nmesh=25（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：25 links（relative（meshes/ 前缀）——meshes/ 与 urdf 同目录） |

## 逐文件对账（raw 溯源件 52）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/T1_23dof.xml | booster_assets/robots/T1/T1_23dof.xml | `f00e3410362b…` | ✓ |
| mjcf/meshes/AL1.STL | booster_assets/robots/T1/meshes/AL1.STL | `43f5d268152b…` | ✓ |
| mjcf/meshes/AL2.STL | booster_assets/robots/T1/meshes/AL2.STL | `4bca60adb29c…` | ✓ |
| mjcf/meshes/AL3.STL | booster_assets/robots/T1/meshes/AL3.STL | `bfdf5611dfe9…` | ✓ |
| mjcf/meshes/AR1.STL | booster_assets/robots/T1/meshes/AR1.STL | `6dbbd3dab448…` | ✓ |
| mjcf/meshes/AR2.STL | booster_assets/robots/T1/meshes/AR2.STL | `0499136785fe…` | ✓ |
| mjcf/meshes/AR3.STL | booster_assets/robots/T1/meshes/AR3.STL | `92330bd8286f…` | ✓ |
| mjcf/meshes/Ankle_Cross_Left.STL | booster_assets/robots/T1/meshes/Ankle_Cross_Left.STL | `e6ec38741838…` | ✓ |
| mjcf/meshes/Ankle_Cross_Right.STL | booster_assets/robots/T1/meshes/Ankle_Cross_Right.STL | `b15d91f0f247…` | ✓ |
| mjcf/meshes/H1.STL | booster_assets/robots/T1/meshes/H1.STL | `527a2e426db4…` | ✓ |
| mjcf/meshes/H2.STL | booster_assets/robots/T1/meshes/H2.STL | `9cbf4fe83a72…` | ✓ |
| mjcf/meshes/Hip_Pitch_Left.STL | booster_assets/robots/T1/meshes/Hip_Pitch_Left.STL | `7bcb8be569ae…` | ✓ |
| mjcf/meshes/Hip_Pitch_Right.STL | booster_assets/robots/T1/meshes/Hip_Pitch_Right.STL | `054d579c3c6c…` | ✓ |
| mjcf/meshes/Hip_Roll_Left.STL | booster_assets/robots/T1/meshes/Hip_Roll_Left.STL | `72dbd65bdb4e…` | ✓ |
| mjcf/meshes/Hip_Roll_Right.STL | booster_assets/robots/T1/meshes/Hip_Roll_Right.STL | `d715a7649ea4…` | ✓ |
| mjcf/meshes/Hip_Yaw_Left.STL | booster_assets/robots/T1/meshes/Hip_Yaw_Left.STL | `8d7de83ab403…` | ✓ |
| mjcf/meshes/Hip_Yaw_Right.STL | booster_assets/robots/T1/meshes/Hip_Yaw_Right.STL | `1a7d98e02188…` | ✓ |
| mjcf/meshes/Logo.STL | booster_assets/robots/T1/meshes/Logo.STL | `221b00d090fd…` | ✓ |
| mjcf/meshes/Shank_Left.STL | booster_assets/robots/T1/meshes/Shank_Left.STL | `6ae8dd7f88cb…` | ✓ |
| mjcf/meshes/Shank_Right.STL | booster_assets/robots/T1/meshes/Shank_Right.STL | `dc66a8a0e2e3…` | ✓ |
| mjcf/meshes/Trunk.STL | booster_assets/robots/T1/meshes/Trunk.STL | `39d9610b23ef…` | ✓ |
| mjcf/meshes/Waist.STL | booster_assets/robots/T1/meshes/Waist.STL | `2fe0a9ccfc28…` | ✓ |
| mjcf/meshes/left_foot_link.STL | booster_assets/robots/T1/meshes/left_foot_link.STL | `2de026f2269f…` | ✓ |
| mjcf/meshes/left_hand_link.STL | booster_assets/robots/T1/meshes/left_hand_link.STL | `34df992aed43…` | ✓ |
| mjcf/meshes/right_foot_link.STL | booster_assets/robots/T1/meshes/right_foot_link.STL | `313a9ff2f95d…` | ✓ |
| mjcf/meshes/right_hand_link.STL | booster_assets/robots/T1/meshes/right_hand_link.STL | `c5a73e493e17…` | ✓ |
| urdf/T1_23dof.urdf | booster_assets/robots/T1/T1_23dof.urdf | `757337c2c8f4…` | ✓ |
| urdf/meshes/AL1.STL | booster_assets/robots/T1/meshes/AL1.STL | `43f5d268152b…` | ✓ |
| urdf/meshes/AL2.STL | booster_assets/robots/T1/meshes/AL2.STL | `4bca60adb29c…` | ✓ |
| urdf/meshes/AL3.STL | booster_assets/robots/T1/meshes/AL3.STL | `bfdf5611dfe9…` | ✓ |
| urdf/meshes/AR1.STL | booster_assets/robots/T1/meshes/AR1.STL | `6dbbd3dab448…` | ✓ |
| urdf/meshes/AR2.STL | booster_assets/robots/T1/meshes/AR2.STL | `0499136785fe…` | ✓ |
| urdf/meshes/AR3.STL | booster_assets/robots/T1/meshes/AR3.STL | `92330bd8286f…` | ✓ |
| urdf/meshes/Ankle_Cross_Left.STL | booster_assets/robots/T1/meshes/Ankle_Cross_Left.STL | `e6ec38741838…` | ✓ |
| urdf/meshes/Ankle_Cross_Right.STL | booster_assets/robots/T1/meshes/Ankle_Cross_Right.STL | `b15d91f0f247…` | ✓ |
| urdf/meshes/H1.STL | booster_assets/robots/T1/meshes/H1.STL | `527a2e426db4…` | ✓ |
| urdf/meshes/H2.STL | booster_assets/robots/T1/meshes/H2.STL | `9cbf4fe83a72…` | ✓ |
| urdf/meshes/Hip_Pitch_Left.STL | booster_assets/robots/T1/meshes/Hip_Pitch_Left.STL | `7bcb8be569ae…` | ✓ |
| urdf/meshes/Hip_Pitch_Right.STL | booster_assets/robots/T1/meshes/Hip_Pitch_Right.STL | `054d579c3c6c…` | ✓ |
| urdf/meshes/Hip_Roll_Left.STL | booster_assets/robots/T1/meshes/Hip_Roll_Left.STL | `72dbd65bdb4e…` | ✓ |
| urdf/meshes/Hip_Roll_Right.STL | booster_assets/robots/T1/meshes/Hip_Roll_Right.STL | `d715a7649ea4…` | ✓ |
| urdf/meshes/Hip_Yaw_Left.STL | booster_assets/robots/T1/meshes/Hip_Yaw_Left.STL | `8d7de83ab403…` | ✓ |
| urdf/meshes/Hip_Yaw_Right.STL | booster_assets/robots/T1/meshes/Hip_Yaw_Right.STL | `1a7d98e02188…` | ✓ |
| urdf/meshes/Logo.STL | booster_assets/robots/T1/meshes/Logo.STL | `221b00d090fd…` | ✓ |
| urdf/meshes/Shank_Left.STL | booster_assets/robots/T1/meshes/Shank_Left.STL | `6ae8dd7f88cb…` | ✓ |
| urdf/meshes/Shank_Right.STL | booster_assets/robots/T1/meshes/Shank_Right.STL | `dc66a8a0e2e3…` | ✓ |
| urdf/meshes/Trunk.STL | booster_assets/robots/T1/meshes/Trunk.STL | `39d9610b23ef…` | ✓ |
| urdf/meshes/Waist.STL | booster_assets/robots/T1/meshes/Waist.STL | `2fe0a9ccfc28…` | ✓ |
| urdf/meshes/left_foot_link.STL | booster_assets/robots/T1/meshes/left_foot_link.STL | `2de026f2269f…` | ✓ |
| urdf/meshes/left_hand_link.STL | booster_assets/robots/T1/meshes/left_hand_link.STL | `34df992aed43…` | ✓ |
| urdf/meshes/right_foot_link.STL | booster_assets/robots/T1/meshes/right_foot_link.STL | `313a9ff2f95d…` | ✓ |
| urdf/meshes/right_hand_link.STL | booster_assets/robots/T1/meshes/right_hand_link.STL | `c5a73e493e17…` | ✓ |

## 排除清单（config s4.excluded）

- `booster_assets/robots/T1/T1_29dof.urdf` — 29 自由度变体无 xml 配对（树扫描实测 T1 线唯一无配对件）——R22 锚点=T1_23dof，不入库只记录
- `booster_assets/robots/T1/T1_locomotion.urdf` — 头/臂/腰固化行走裁剪变体——R22 锚点=T1_23dof，不入库只记录
- `booster_assets/robots/T1/T1_locomotion.xml` — 行走裁剪变体 MJCF 侧——R22 锚点=T1_23dof，不入库只记录
- `booster_assets/robots/T1/T1_23dof_parallel.xml` — 并联变体 MJCF（踝关节并联机构表征副本）——R22 已裁不入库，X2 simple_collision 先例同款

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 1）
