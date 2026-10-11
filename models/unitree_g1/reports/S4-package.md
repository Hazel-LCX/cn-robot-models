# S4 入库对账报告 — unitree_g1（2026-10-11 18:05）

**物理文件口径（终审 F1 修正）**：入库物理文件 62 = raw 溯源件 62（URDF 引用 50 处 → 网格物理文件 29，引用行 ≠ 文件数） + 质检自产件 0[]；**总 40.5 MB（raw 溯源件 40,516,538 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 29 · image 1 · mesh 29 · mjcf 2 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 62 个 raw 源入库文件 SHA256 全部命中 raw manifest 同路径行（逐文件可溯源） |
| `s4:mesh-split-decision` | PASS | URDF 侧 50 处引用 → 29 个物理网格 vs MJCF 侧 29 个，哈希交集 28 → 分目录（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | PASS | raw 全量 299（除 .git/manifest）= 根级及中间层 9 + 目标子目录 290；子目录 290 全覆盖 = 入库 62 + 排除 228（其中 meshes/ 冗余 0）（未覆盖：无）——算式每行必须平（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/g1_23dof.xml 编译通过：nbody=31 ngeom=62 nmesh=29（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：33 links（relative 引用协议——meshes/ 与 urdf 同目录的相对关系保持） |

## 逐文件对账（raw 溯源件 62）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| images/g1_23dof.png | unitree_ros/robots/g1_description/images/g1_23dof.png | `8cd8db7c7abd…` | ✓ |
| mjcf/g1_23dof.xml | unitree_mujoco/unitree_robots/g1/g1_23dof.xml | `2876f3331af5…` | ✓ |
| mjcf/meshes/head_link.STL | unitree_mujoco/unitree_robots/g1/meshes/head_link.STL | `d297328b3569…` | ✓ |
| mjcf/meshes/left_ankle_pitch_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_ankle_pitch_link.STL | `d49e3abc6f5b…` | ✓ |
| mjcf/meshes/left_ankle_roll_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_ankle_roll_link.STL | `c4092af94314…` | ✓ |
| mjcf/meshes/left_elbow_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_elbow_link.STL | `fa752198accd…` | ✓ |
| mjcf/meshes/left_hip_pitch_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_hip_pitch_link.STL | `4725168105ee…` | ✓ |
| mjcf/meshes/left_hip_roll_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_hip_roll_link.STL | `91f25922ee8a…` | ✓ |
| mjcf/meshes/left_hip_yaw_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_hip_yaw_link.STL | `a16d88aa6dda…` | ✓ |
| mjcf/meshes/left_knee_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_knee_link.STL | `8d92b9e3d3a6…` | ✓ |
| mjcf/meshes/left_shoulder_pitch_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_shoulder_pitch_link.STL | `f0d1cfd02fcf…` | ✓ |
| mjcf/meshes/left_shoulder_roll_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_shoulder_roll_link.STL | `fb9df2168777…` | ✓ |
| mjcf/meshes/left_shoulder_yaw_link.STL | unitree_mujoco/unitree_robots/g1/meshes/left_shoulder_yaw_link.STL | `1aa97e9748e9…` | ✓ |
| mjcf/meshes/left_wrist_roll_rubber_hand.STL | unitree_mujoco/unitree_robots/g1/meshes/left_wrist_roll_rubber_hand.STL | `e81030abd023…` | ✓ |
| mjcf/meshes/logo_link.STL | unitree_mujoco/unitree_robots/g1/meshes/logo_link.STL | `8571a0a19bc4…` | ✓ |
| mjcf/meshes/pelvis.STL | unitree_mujoco/unitree_robots/g1/meshes/pelvis.STL | `5ba6bbc888e6…` | ✓ |
| mjcf/meshes/pelvis_contour_link.STL | unitree_mujoco/unitree_robots/g1/meshes/pelvis_contour_link.STL | `5cc5c2c7a312…` | ✓ |
| mjcf/meshes/right_ankle_pitch_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_ankle_pitch_link.STL | `15be426539ec…` | ✓ |
| mjcf/meshes/right_ankle_roll_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_ankle_roll_link.STL | `4b66222ea566…` | ✓ |
| mjcf/meshes/right_elbow_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_elbow_link.STL | `1be925d7aa26…` | ✓ |
| mjcf/meshes/right_hip_pitch_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_hip_pitch_link.STL | `e4f3c99d7f4a…` | ✓ |
| mjcf/meshes/right_hip_roll_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_hip_roll_link.STL | `4c254ef66a35…` | ✓ |
| mjcf/meshes/right_hip_yaw_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_hip_yaw_link.STL | `e479c2936ca2…` | ✓ |
| mjcf/meshes/right_knee_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_knee_link.STL | `63c4008449c9…` | ✓ |
| mjcf/meshes/right_shoulder_pitch_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_shoulder_pitch_link.STL | `24cdb387e012…` | ✓ |
| mjcf/meshes/right_shoulder_roll_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_shoulder_roll_link.STL | `962b97c48f9c…` | ✓ |
| mjcf/meshes/right_shoulder_yaw_link.STL | unitree_mujoco/unitree_robots/g1/meshes/right_shoulder_yaw_link.STL | `a0b76489271d…` | ✓ |
| mjcf/meshes/right_wrist_roll_rubber_hand.STL | unitree_mujoco/unitree_robots/g1/meshes/right_wrist_roll_rubber_hand.STL | `0729aff1ac43…` | ✓ |
| mjcf/meshes/torso_link.STL | unitree_mujoco/unitree_robots/g1/meshes/torso_link.STL | `e96d023f0368…` | ✓ |
| mjcf/meshes/waist_support_link.STL | unitree_mujoco/unitree_robots/g1/meshes/waist_support_link.STL | `1fae9e1bb609…` | ✓ |
| mjcf/meshes/waist_yaw_link.STL | unitree_mujoco/unitree_robots/g1/meshes/waist_yaw_link.STL | `2883f20e03f0…` | ✓ |
| mjcf/scene_23dof.xml | unitree_mujoco/unitree_robots/g1/scene_23dof.xml | `5582080972f7…` | ✓ |
| urdf/g1_23dof.urdf | unitree_ros/robots/g1_description/g1_23dof.urdf | `5d5a7380ec2f…` | ✓ |
| urdf/meshes/head_link.STL | unitree_ros/robots/g1_description/meshes/head_link.STL | `005fb67fbd3e…` | ✓ |
| urdf/meshes/left_ankle_pitch_link.STL | unitree_ros/robots/g1_description/meshes/left_ankle_pitch_link.STL | `d49e3abc6f5b…` | ✓ |
| urdf/meshes/left_ankle_roll_link.STL | unitree_ros/robots/g1_description/meshes/left_ankle_roll_link.STL | `c4092af94314…` | ✓ |
| urdf/meshes/left_elbow_link.STL | unitree_ros/robots/g1_description/meshes/left_elbow_link.STL | `fa752198accd…` | ✓ |
| urdf/meshes/left_hip_pitch_link.STL | unitree_ros/robots/g1_description/meshes/left_hip_pitch_link.STL | `4725168105ee…` | ✓ |
| urdf/meshes/left_hip_roll_link.STL | unitree_ros/robots/g1_description/meshes/left_hip_roll_link.STL | `91f25922ee8a…` | ✓ |
| urdf/meshes/left_hip_yaw_link.STL | unitree_ros/robots/g1_description/meshes/left_hip_yaw_link.STL | `a16d88aa6dda…` | ✓ |
| urdf/meshes/left_knee_link.STL | unitree_ros/robots/g1_description/meshes/left_knee_link.STL | `8d92b9e3d3a6…` | ✓ |
| urdf/meshes/left_shoulder_pitch_link.STL | unitree_ros/robots/g1_description/meshes/left_shoulder_pitch_link.STL | `f0d1cfd02fcf…` | ✓ |
| urdf/meshes/left_shoulder_roll_link.STL | unitree_ros/robots/g1_description/meshes/left_shoulder_roll_link.STL | `fb9df2168777…` | ✓ |
| urdf/meshes/left_shoulder_yaw_link.STL | unitree_ros/robots/g1_description/meshes/left_shoulder_yaw_link.STL | `1aa97e9748e9…` | ✓ |
| urdf/meshes/left_wrist_roll_rubber_hand.STL | unitree_ros/robots/g1_description/meshes/left_wrist_roll_rubber_hand.STL | `e81030abd023…` | ✓ |
| urdf/meshes/logo_link.STL | unitree_ros/robots/g1_description/meshes/logo_link.STL | `8571a0a19bc4…` | ✓ |
| urdf/meshes/pelvis.STL | unitree_ros/robots/g1_description/meshes/pelvis.STL | `5ba6bbc888e6…` | ✓ |
| urdf/meshes/pelvis_contour_link.STL | unitree_ros/robots/g1_description/meshes/pelvis_contour_link.STL | `5cc5c2c7a312…` | ✓ |
| urdf/meshes/right_ankle_pitch_link.STL | unitree_ros/robots/g1_description/meshes/right_ankle_pitch_link.STL | `15be426539ec…` | ✓ |
| urdf/meshes/right_ankle_roll_link.STL | unitree_ros/robots/g1_description/meshes/right_ankle_roll_link.STL | `4b66222ea566…` | ✓ |
| urdf/meshes/right_elbow_link.STL | unitree_ros/robots/g1_description/meshes/right_elbow_link.STL | `1be925d7aa26…` | ✓ |
| urdf/meshes/right_hip_pitch_link.STL | unitree_ros/robots/g1_description/meshes/right_hip_pitch_link.STL | `e4f3c99d7f4a…` | ✓ |
| urdf/meshes/right_hip_roll_link.STL | unitree_ros/robots/g1_description/meshes/right_hip_roll_link.STL | `4c254ef66a35…` | ✓ |
| urdf/meshes/right_hip_yaw_link.STL | unitree_ros/robots/g1_description/meshes/right_hip_yaw_link.STL | `e479c2936ca2…` | ✓ |
| urdf/meshes/right_knee_link.STL | unitree_ros/robots/g1_description/meshes/right_knee_link.STL | `63c4008449c9…` | ✓ |
| urdf/meshes/right_shoulder_pitch_link.STL | unitree_ros/robots/g1_description/meshes/right_shoulder_pitch_link.STL | `24cdb387e012…` | ✓ |
| urdf/meshes/right_shoulder_roll_link.STL | unitree_ros/robots/g1_description/meshes/right_shoulder_roll_link.STL | `962b97c48f9c…` | ✓ |
| urdf/meshes/right_shoulder_yaw_link.STL | unitree_ros/robots/g1_description/meshes/right_shoulder_yaw_link.STL | `a0b76489271d…` | ✓ |
| urdf/meshes/right_wrist_roll_rubber_hand.STL | unitree_ros/robots/g1_description/meshes/right_wrist_roll_rubber_hand.STL | `0729aff1ac43…` | ✓ |
| urdf/meshes/torso_link.STL | unitree_ros/robots/g1_description/meshes/torso_link.STL | `e96d023f0368…` | ✓ |
| urdf/meshes/waist_support_link.STL | unitree_ros/robots/g1_description/meshes/waist_support_link.STL | `1fae9e1bb609…` | ✓ |
| urdf/meshes/waist_yaw_link.STL | unitree_ros/robots/g1_description/meshes/waist_yaw_link.STL | `2883f20e03f0…` | ✓ |

## 排除清单（config s4.excluded）

- `unitree_ros/robots/g1_description/g1_23dof.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_23dof_mode_10.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_23dof_rev_1_0.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_23dof_rev_1_0.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_lock_waist.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_lock_waist.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_lock_waist_rev_1_0.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_lock_waist_rev_1_0.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_lock_waist_with_hand_rev_1_0.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_lock_waist_with_hand_rev_1_0.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_11.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_12.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_13.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_14.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_15.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_15_with_dex1_1.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_16.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_mode_18.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_rev_1_0.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_rev_1_0.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_rev_1_0_with_inspire_hand_DFQ.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_rev_1_0_with_inspire_hand_FTP.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_with_hand.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_with_hand.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_with_hand_rev_1_0.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_29dof_with_hand_rev_1_0.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_comp.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_dual_arm.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_dual_arm.xml` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/g1_pl.urdf` — J1：23 配置中未收的变体文件（本库收 g1_23dof 配对，29dof 系留 M2+）
- `unitree_ros/robots/g1_description/images/g1_29dof.png` — 上游渲染图（未收配置的图示），配图仅收 g1_23dof.png
- `unitree_ros/robots/g1_description/images/g1_29dof_with_hand.png` — 上游渲染图（未收配置的图示），配图仅收 g1_23dof.png
- `unitree_ros/robots/g1_description/images/g1_dual_arm.png` — 上游渲染图（未收配置的图示），配图仅收 g1_23dof.png
- `unitree_ros/robots/g1_description/inspire_hand/config.yaml` — 灵巧手模型目录，非 23dof 范围
- `unitree_ros/robots/g1_description/inspire_hand/DFQ_left_hand.urdf` — 灵巧手模型目录，非 23dof 范围
- `unitree_ros/robots/g1_description/inspire_hand/DFQ_right_hand.urdf` — 灵巧手模型目录，非 23dof 范围
- `unitree_ros/robots/g1_description/inspire_hand/FTP_left_hand.urdf` — 灵巧手模型目录，非 23dof 范围
- `unitree_ros/robots/g1_description/inspire_hand/FTP_right_hand.urdf` — 灵巧手模型目录，非 23dof 范围
- `unitree_ros/robots/g1_description/merge_g1_29dof_and_inspire_hand.ipynb` — 上游合并工具 notebook，非模型件
- `unitree_ros/robots/g1_description/meshes/backpack_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/d455_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Dex1_base_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/dex1_col_1.stl` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/dex1_col_2.stl` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Dex1_finger_link_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Dex1_finger_link_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/handle_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/head_base_link_with_2dof_head.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/head_link_with_2dof_head.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/head_servo_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/L_hand_base_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_base_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_index_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_index_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_middle_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_middle_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_palm_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_thumb_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_thumb_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_hand_thumb_2_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_index_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_index_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_index_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_index_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_index_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_little_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_little_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_little_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_little_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_little_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_middle_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_middle_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_middle_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_middle_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_middle_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_palm_force_sensor.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_ring_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_ring_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_ring_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_ring_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_ring_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_rubber_hand.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_4.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_force_sensor_4.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_thumb_swing.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_wrist_pitch_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_wrist_pitch_link_5010.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_wrist_roll_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_wrist_roll_link_5010.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_wrist_yaw_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/left_wrist_yaw_link_5010.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link11_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link11_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link12_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link12_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link13_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link13_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link14_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link14_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link15_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link15_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link16_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link16_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link17_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link17_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link18_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link18_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link19_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link19_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link20_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link20_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link21_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link21_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link22_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/Link22_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/neck_pitch_link_with_2dof_head.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/pelvis_ver0529.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/R_hand_base_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_base_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_index_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_index_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_middle_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_middle_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_palm_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_thumb_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_thumb_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_hand_thumb_2_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_index_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_index_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_index_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_index_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_index_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_little_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_little_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_little_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_little_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_little_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_middle_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_middle_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_middle_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_middle_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_middle_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_palm_force_sensor.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_ring_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_ring_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_ring_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_ring_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_ring_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_rubber_hand.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_4.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_force_sensor_1.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_force_sensor_2.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_force_sensor_3.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_thumb_force_sensor_4.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_wrist_pitch_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_wrist_pitch_link_5010.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_wrist_roll_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_wrist_roll_link_5010.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_wrist_yaw_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/right_wrist_yaw_link_5010.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/torso_constraint_L_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/torso_constraint_L_rod_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/torso_constraint_R_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/torso_constraint_R_rod_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/torso_link_23dof_rev_1_0.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/torso_link_rev_1_0.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/torso_link_with_2dof_head.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/waist_constraint_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/waist_constraint_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/waist_roll_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/waist_roll_link_rev_1_0.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/waist_yaw_custom.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/waist_yaw_link_rev_1_0.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/meshes/xl330_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_ros/robots/g1_description/motor_info.md` — 上游包文档（A2 复查无许可声明）
- `unitree_ros/robots/g1_description/README.md` — 上游包文档（A2 复查无许可声明）
- `unitree_mujoco/unitree_robots/g1/g1_29dof.xml` — 未收配置/全场景包装（scene.xml 含地形依赖）
- `unitree_mujoco/unitree_robots/g1/g1_joint_index_dds.md` — 上游 DDS 关节索引文档（A2 复查无许可声明）
- `unitree_mujoco/unitree_robots/g1/height_field.png` — 地形演示专用图
- `unitree_mujoco/unitree_robots/g1/images/g1_23dof.png` — mujoco 侧页面图，非模型件
- `unitree_mujoco/unitree_robots/g1/images/g1_29dof.png` — 上游渲染图（未收配置的图示），配图仅收 g1_23dof.png
- `unitree_mujoco/unitree_robots/g1/images/g1_29dof_with_hand.png` — 上游渲染图（未收配置的图示），配图仅收 g1_23dof.png
- `unitree_mujoco/unitree_robots/g1/images/g1_dual_arm.png` — 上游渲染图（未收配置的图示），配图仅收 g1_23dof.png
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_index_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_index_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_middle_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_middle_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_palm_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_thumb_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_thumb_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_hand_thumb_2_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_rubber_hand.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_wrist_pitch_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_wrist_roll_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/left_wrist_yaw_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_index_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_index_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_middle_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_middle_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_palm_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_thumb_0_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_thumb_1_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_hand_thumb_2_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_rubber_hand.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_wrist_pitch_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_wrist_roll_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/right_wrist_yaw_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/torso_constraint_L_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/torso_constraint_L_rod_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/torso_constraint_R_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/torso_constraint_R_rod_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/waist_constraint_L.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/waist_constraint_R.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/meshes/waist_roll_link.STL` — meshes/ 池中 23dof 引用闭包外的网格（29dof/手部/腰部配置件；ros 池含 2 件小写 .stl 的 Dex1 手网格，后缀大小写混杂如实记录）
- `unitree_mujoco/unitree_robots/g1/scene.xml` — 未收配置/全场景包装（scene.xml 含地形依赖）
- `unitree_mujoco/unitree_robots/g1/scene_29dof.xml` — 未收配置/全场景包装（scene.xml 含地形依赖）
- `unitree_mujoco/unitree_robots/g1/unitree_hfield.png` — 地形演示专用图

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 0）

## 工作台补记（2026-10-11 · 数字可重放）

- **mesh-split 交集 28/29 的一件 = head_link.STL**：URDF 侧 932,784 B vs MJCF 侧 337,584 B（同名不同哈希，其余 28 件两侧同哈希=同源同内容）。**与 S3 forensics 同根闭环**：URDF 把头壳独立建模（head_link，1.036 kg + 精细网格），MJCF 合并进 torso（简化头壳网格）——质量拆分分歧与网格差异是上游同一建模决策的两个侧面，零修复如实披露。
- **入库名录**：62 件 = URDF 1（urdf/g1_23dof.urdf）+ urdf/meshes 29（relative 引用协议，与 urdf 同目录）+ MJCF 2（g1_23dof.xml + scene_23dof.xml）+ mjcf/meshes 29（meshdir 闭包）+ images 1（g1_23dof.png 官方渲染图）；40.5 MB。excluded 228 件逐件带 why（config s4.excluded，程序化生成）。
- **traceability 对账口径升级**：manifest 由"哈希→单路径"改"哈希→路径集合"——G1 两侧网格 28 件同哈希（同源同内容），单路径映射会把 ros 侧件全部误判未命中（本会话实测抓到后修复）；对账语义 = 入库件哈希在 manifest 中存在且 src ∈ 该哈希路径集合。
