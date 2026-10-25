# S4 入库对账报告 — booster_t2_wujihand（2026-10-25 20:35）

**物理文件口径（终审 F1 修正）**：入库物理文件 176 = raw 溯源件 176（URDF 引用 141 处 → 网格物理文件 87，引用行 ≠ 文件数） + 质检自产件 0[]；**总 104.9 MB（raw 溯源件 104,926,694 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 87 · mesh 87 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 176 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 141 处引用 → 87 个物理网格 vs MJCF 侧 87 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | WARN | raw 全量 96（除 .git/manifest）= 根级及中间层 5 + 目标子目录 91；子目录 91 全覆盖 = 入库唯一源 89；物理落位 176 件（87 件为双侧同源网格重复落位，同源同内容、两侧引用协议各自独立目录） + 排除 0（其中 meshes/ 冗余 0）（未覆盖：['booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_wrist_roll_link_collision.STL', 'booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_wrist_roll_link_collision.STL']）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/T2_31dof_WujiHand.xml 编译通过：nbody=73 ngeom=157 nmesh=87（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：87 links（relative（meshes/ 前缀）——meshes/ 与 urdf 同目录） |

## 逐文件对账（raw 溯源件 176）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/T2_31dof_WujiHand.xml | booster_assets/robots/T2/T2_31dof_WujiHand/T2_31dof_WujiHand.xml | `8aecc568185c…` | ✓ |
| mjcf/meshes/head_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/head_pitch_link.STL | `f1f59dab47d9…` | ✓ |
| mjcf/meshes/head_pitch_link_collision.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/head_pitch_link_collision.STL | `3ee342ea15b2…` | ✓ |
| mjcf/meshes/head_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/head_yaw_link.STL | `82837cb3b7d1…` | ✓ |
| mjcf/meshes/left_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_ankle_pitch_link.STL | `68e0ea886e54…` | ✓ |
| mjcf/meshes/left_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_ankle_roll_link.STL | `feeb92e5ff35…` | ✓ |
| mjcf/meshes/left_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_elbow_pitch_link.STL | `7a629fe2ce05…` | ✓ |
| mjcf/meshes/left_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_elbow_yaw_link.STL | `35afa050a21f…` | ✓ |
| mjcf/meshes/left_finger1_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link1.STL | `ef6226834aaf…` | ✓ |
| mjcf/meshes/left_finger1_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link2.STL | `4b95c67bfb2d…` | ✓ |
| mjcf/meshes/left_finger1_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link3.STL | `2a6ba5a4d292…` | ✓ |
| mjcf/meshes/left_finger1_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link4.STL | `bcb512d59797…` | ✓ |
| mjcf/meshes/left_finger1_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_tip_link.STL | `83c92a6c07f7…` | ✓ |
| mjcf/meshes/left_finger2_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link1.STL | `afb3cd29a430…` | ✓ |
| mjcf/meshes/left_finger2_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link2.STL | `02c12143eabd…` | ✓ |
| mjcf/meshes/left_finger2_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link3.STL | `764426f6623a…` | ✓ |
| mjcf/meshes/left_finger2_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link4.STL | `324194485051…` | ✓ |
| mjcf/meshes/left_finger2_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_tip_link.STL | `ef47c5b83594…` | ✓ |
| mjcf/meshes/left_finger3_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link1.STL | `92839a1448fa…` | ✓ |
| mjcf/meshes/left_finger3_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link2.STL | `b538ab9ce27e…` | ✓ |
| mjcf/meshes/left_finger3_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link3.STL | `795ecf9b1fe6…` | ✓ |
| mjcf/meshes/left_finger3_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link4.STL | `e2428e5723d8…` | ✓ |
| mjcf/meshes/left_finger3_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_tip_link.STL | `36b33404458a…` | ✓ |
| mjcf/meshes/left_finger4_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link1.STL | `34372b6d907d…` | ✓ |
| mjcf/meshes/left_finger4_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link2.STL | `d51b96912a9e…` | ✓ |
| mjcf/meshes/left_finger4_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link3.STL | `18d23d11f4b8…` | ✓ |
| mjcf/meshes/left_finger4_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link4.STL | `592c269cd9a4…` | ✓ |
| mjcf/meshes/left_finger4_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_tip_link.STL | `67995957f508…` | ✓ |
| mjcf/meshes/left_finger5_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link1.STL | `2ddd53a41d44…` | ✓ |
| mjcf/meshes/left_finger5_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link2.STL | `09f0d2e932c4…` | ✓ |
| mjcf/meshes/left_finger5_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link3.STL | `2550cb770eba…` | ✓ |
| mjcf/meshes/left_finger5_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link4.STL | `3f095a1ca173…` | ✓ |
| mjcf/meshes/left_finger5_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_tip_link.STL | `6955f23515b6…` | ✓ |
| mjcf/meshes/left_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_hip_pitch_link.STL | `75e86c93f4f3…` | ✓ |
| mjcf/meshes/left_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_hip_roll_link.STL | `a712069ff473…` | ✓ |
| mjcf/meshes/left_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_hip_yaw_link.STL | `1a48820e718a…` | ✓ |
| mjcf/meshes/left_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_knee_pitch_link.STL | `ee66d048f415…` | ✓ |
| mjcf/meshes/left_palm_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_palm_link.STL | `5a16d3510b49…` | ✓ |
| mjcf/meshes/left_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_shoulder_pitch_link.STL | `37a19783477a…` | ✓ |
| mjcf/meshes/left_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_shoulder_roll_link.STL | `d10c4f38c0fd…` | ✓ |
| mjcf/meshes/left_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_wrist_pitch_link.STL | `85085ba79d4c…` | ✓ |
| mjcf/meshes/left_wrist_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_wrist_roll_link.STL | `ea4e1ad6f296…` | ✓ |
| mjcf/meshes/left_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_wrist_yaw_link.STL | `bfc1d2685458…` | ✓ |
| mjcf/meshes/logo.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/logo.STL | `58edab292a58…` | ✓ |
| mjcf/meshes/right_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_ankle_pitch_link.STL | `c65638beb7e0…` | ✓ |
| mjcf/meshes/right_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_ankle_roll_link.STL | `a61e8f7879fd…` | ✓ |
| mjcf/meshes/right_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_elbow_pitch_link.STL | `1d8d06a76e0f…` | ✓ |
| mjcf/meshes/right_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_elbow_yaw_link.STL | `d6600efeefb0…` | ✓ |
| mjcf/meshes/right_finger1_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link1.STL | `0e32302a46cd…` | ✓ |
| mjcf/meshes/right_finger1_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link2.STL | `080015cce41d…` | ✓ |
| mjcf/meshes/right_finger1_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link3.STL | `52eef283d29c…` | ✓ |
| mjcf/meshes/right_finger1_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link4.STL | `f0fb321c4abf…` | ✓ |
| mjcf/meshes/right_finger1_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_tip_link.STL | `25929e0c28a5…` | ✓ |
| mjcf/meshes/right_finger2_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link1.STL | `36e0471a0373…` | ✓ |
| mjcf/meshes/right_finger2_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link2.STL | `56bb1972b8cb…` | ✓ |
| mjcf/meshes/right_finger2_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link3.STL | `48d70e865e2b…` | ✓ |
| mjcf/meshes/right_finger2_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link4.STL | `3eede2c8e1eb…` | ✓ |
| mjcf/meshes/right_finger2_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_tip_link.STL | `496039ce3f4f…` | ✓ |
| mjcf/meshes/right_finger3_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link1.STL | `558fac18be21…` | ✓ |
| mjcf/meshes/right_finger3_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link2.STL | `338db71e2c1e…` | ✓ |
| mjcf/meshes/right_finger3_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link3.STL | `3af337085d5f…` | ✓ |
| mjcf/meshes/right_finger3_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link4.STL | `3b8efa21bafc…` | ✓ |
| mjcf/meshes/right_finger3_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_tip_link.STL | `7a99f65a6a47…` | ✓ |
| mjcf/meshes/right_finger4_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link1.STL | `508321fefaea…` | ✓ |
| mjcf/meshes/right_finger4_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link2.STL | `e0b28769389c…` | ✓ |
| mjcf/meshes/right_finger4_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link3.STL | `b01668bab452…` | ✓ |
| mjcf/meshes/right_finger4_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link4.STL | `d673bf02761f…` | ✓ |
| mjcf/meshes/right_finger4_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_tip_link.STL | `e8b1fbee8e01…` | ✓ |
| mjcf/meshes/right_finger5_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link1.STL | `85ce22b8285a…` | ✓ |
| mjcf/meshes/right_finger5_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link2.STL | `9245362396a1…` | ✓ |
| mjcf/meshes/right_finger5_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link3.STL | `1083dcec6df5…` | ✓ |
| mjcf/meshes/right_finger5_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link4.STL | `6342d4562a8b…` | ✓ |
| mjcf/meshes/right_finger5_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_tip_link.STL | `ebbf48ca7ba3…` | ✓ |
| mjcf/meshes/right_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_hip_pitch_link.STL | `9ba846267032…` | ✓ |
| mjcf/meshes/right_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_hip_roll_link.STL | `1aacf29649c0…` | ✓ |
| mjcf/meshes/right_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_hip_yaw_link.STL | `5bfda02be110…` | ✓ |
| mjcf/meshes/right_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_knee_pitch_link.STL | `a04304cce3fe…` | ✓ |
| mjcf/meshes/right_palm_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_palm_link.STL | `1ba4495e3b7a…` | ✓ |
| mjcf/meshes/right_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_shoulder_pitch_link.STL | `0e4ca045ba6d…` | ✓ |
| mjcf/meshes/right_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_shoulder_roll_link.STL | `0c3b6f453e93…` | ✓ |
| mjcf/meshes/right_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_wrist_pitch_link.STL | `25538e72b962…` | ✓ |
| mjcf/meshes/right_wrist_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_wrist_roll_link.STL | `e48d25ea4be3…` | ✓ |
| mjcf/meshes/right_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_wrist_yaw_link.STL | `2b6ce1d4710e…` | ✓ |
| mjcf/meshes/trunk.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/trunk.STL | `52afacf37b33…` | ✓ |
| mjcf/meshes/waist_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_pitch_link.STL | `ba2d7dd2d4c8…` | ✓ |
| mjcf/meshes/waist_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_roll_link.STL | `2196475c282f…` | ✓ |
| mjcf/meshes/waist_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_yaw_link.STL | `c0950ebf894f…` | ✓ |
| mjcf/meshes/waist_yaw_link_collision.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_yaw_link_collision.STL | `3767612763d5…` | ✓ |
| urdf/T2_31dof_WujiHand.urdf | booster_assets/robots/T2/T2_31dof_WujiHand/T2_31dof_WujiHand.urdf | `864c674a6f56…` | ✓ |
| urdf/meshes/head_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/head_pitch_link.STL | `f1f59dab47d9…` | ✓ |
| urdf/meshes/head_pitch_link_collision.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/head_pitch_link_collision.STL | `3ee342ea15b2…` | ✓ |
| urdf/meshes/head_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/head_yaw_link.STL | `82837cb3b7d1…` | ✓ |
| urdf/meshes/left_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_ankle_pitch_link.STL | `68e0ea886e54…` | ✓ |
| urdf/meshes/left_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_ankle_roll_link.STL | `feeb92e5ff35…` | ✓ |
| urdf/meshes/left_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_elbow_pitch_link.STL | `7a629fe2ce05…` | ✓ |
| urdf/meshes/left_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_elbow_yaw_link.STL | `35afa050a21f…` | ✓ |
| urdf/meshes/left_finger1_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link1.STL | `ef6226834aaf…` | ✓ |
| urdf/meshes/left_finger1_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link2.STL | `4b95c67bfb2d…` | ✓ |
| urdf/meshes/left_finger1_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link3.STL | `2a6ba5a4d292…` | ✓ |
| urdf/meshes/left_finger1_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_link4.STL | `bcb512d59797…` | ✓ |
| urdf/meshes/left_finger1_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger1_tip_link.STL | `83c92a6c07f7…` | ✓ |
| urdf/meshes/left_finger2_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link1.STL | `afb3cd29a430…` | ✓ |
| urdf/meshes/left_finger2_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link2.STL | `02c12143eabd…` | ✓ |
| urdf/meshes/left_finger2_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link3.STL | `764426f6623a…` | ✓ |
| urdf/meshes/left_finger2_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_link4.STL | `324194485051…` | ✓ |
| urdf/meshes/left_finger2_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger2_tip_link.STL | `ef47c5b83594…` | ✓ |
| urdf/meshes/left_finger3_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link1.STL | `92839a1448fa…` | ✓ |
| urdf/meshes/left_finger3_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link2.STL | `b538ab9ce27e…` | ✓ |
| urdf/meshes/left_finger3_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link3.STL | `795ecf9b1fe6…` | ✓ |
| urdf/meshes/left_finger3_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_link4.STL | `e2428e5723d8…` | ✓ |
| urdf/meshes/left_finger3_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger3_tip_link.STL | `36b33404458a…` | ✓ |
| urdf/meshes/left_finger4_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link1.STL | `34372b6d907d…` | ✓ |
| urdf/meshes/left_finger4_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link2.STL | `d51b96912a9e…` | ✓ |
| urdf/meshes/left_finger4_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link3.STL | `18d23d11f4b8…` | ✓ |
| urdf/meshes/left_finger4_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_link4.STL | `592c269cd9a4…` | ✓ |
| urdf/meshes/left_finger4_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger4_tip_link.STL | `67995957f508…` | ✓ |
| urdf/meshes/left_finger5_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link1.STL | `2ddd53a41d44…` | ✓ |
| urdf/meshes/left_finger5_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link2.STL | `09f0d2e932c4…` | ✓ |
| urdf/meshes/left_finger5_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link3.STL | `2550cb770eba…` | ✓ |
| urdf/meshes/left_finger5_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_link4.STL | `3f095a1ca173…` | ✓ |
| urdf/meshes/left_finger5_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_finger5_tip_link.STL | `6955f23515b6…` | ✓ |
| urdf/meshes/left_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_hip_pitch_link.STL | `75e86c93f4f3…` | ✓ |
| urdf/meshes/left_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_hip_roll_link.STL | `a712069ff473…` | ✓ |
| urdf/meshes/left_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_hip_yaw_link.STL | `1a48820e718a…` | ✓ |
| urdf/meshes/left_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_knee_pitch_link.STL | `ee66d048f415…` | ✓ |
| urdf/meshes/left_palm_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_palm_link.STL | `5a16d3510b49…` | ✓ |
| urdf/meshes/left_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_shoulder_pitch_link.STL | `37a19783477a…` | ✓ |
| urdf/meshes/left_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_shoulder_roll_link.STL | `d10c4f38c0fd…` | ✓ |
| urdf/meshes/left_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_wrist_pitch_link.STL | `85085ba79d4c…` | ✓ |
| urdf/meshes/left_wrist_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_wrist_roll_link.STL | `ea4e1ad6f296…` | ✓ |
| urdf/meshes/left_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/left_wrist_yaw_link.STL | `bfc1d2685458…` | ✓ |
| urdf/meshes/logo.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/logo.STL | `58edab292a58…` | ✓ |
| urdf/meshes/right_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_ankle_pitch_link.STL | `c65638beb7e0…` | ✓ |
| urdf/meshes/right_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_ankle_roll_link.STL | `a61e8f7879fd…` | ✓ |
| urdf/meshes/right_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_elbow_pitch_link.STL | `1d8d06a76e0f…` | ✓ |
| urdf/meshes/right_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_elbow_yaw_link.STL | `d6600efeefb0…` | ✓ |
| urdf/meshes/right_finger1_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link1.STL | `0e32302a46cd…` | ✓ |
| urdf/meshes/right_finger1_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link2.STL | `080015cce41d…` | ✓ |
| urdf/meshes/right_finger1_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link3.STL | `52eef283d29c…` | ✓ |
| urdf/meshes/right_finger1_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_link4.STL | `f0fb321c4abf…` | ✓ |
| urdf/meshes/right_finger1_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger1_tip_link.STL | `25929e0c28a5…` | ✓ |
| urdf/meshes/right_finger2_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link1.STL | `36e0471a0373…` | ✓ |
| urdf/meshes/right_finger2_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link2.STL | `56bb1972b8cb…` | ✓ |
| urdf/meshes/right_finger2_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link3.STL | `48d70e865e2b…` | ✓ |
| urdf/meshes/right_finger2_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_link4.STL | `3eede2c8e1eb…` | ✓ |
| urdf/meshes/right_finger2_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger2_tip_link.STL | `496039ce3f4f…` | ✓ |
| urdf/meshes/right_finger3_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link1.STL | `558fac18be21…` | ✓ |
| urdf/meshes/right_finger3_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link2.STL | `338db71e2c1e…` | ✓ |
| urdf/meshes/right_finger3_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link3.STL | `3af337085d5f…` | ✓ |
| urdf/meshes/right_finger3_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_link4.STL | `3b8efa21bafc…` | ✓ |
| urdf/meshes/right_finger3_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger3_tip_link.STL | `7a99f65a6a47…` | ✓ |
| urdf/meshes/right_finger4_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link1.STL | `508321fefaea…` | ✓ |
| urdf/meshes/right_finger4_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link2.STL | `e0b28769389c…` | ✓ |
| urdf/meshes/right_finger4_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link3.STL | `b01668bab452…` | ✓ |
| urdf/meshes/right_finger4_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_link4.STL | `d673bf02761f…` | ✓ |
| urdf/meshes/right_finger4_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger4_tip_link.STL | `e8b1fbee8e01…` | ✓ |
| urdf/meshes/right_finger5_link1.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link1.STL | `85ce22b8285a…` | ✓ |
| urdf/meshes/right_finger5_link2.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link2.STL | `9245362396a1…` | ✓ |
| urdf/meshes/right_finger5_link3.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link3.STL | `1083dcec6df5…` | ✓ |
| urdf/meshes/right_finger5_link4.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_link4.STL | `6342d4562a8b…` | ✓ |
| urdf/meshes/right_finger5_tip_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_finger5_tip_link.STL | `ebbf48ca7ba3…` | ✓ |
| urdf/meshes/right_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_hip_pitch_link.STL | `9ba846267032…` | ✓ |
| urdf/meshes/right_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_hip_roll_link.STL | `1aacf29649c0…` | ✓ |
| urdf/meshes/right_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_hip_yaw_link.STL | `5bfda02be110…` | ✓ |
| urdf/meshes/right_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_knee_pitch_link.STL | `a04304cce3fe…` | ✓ |
| urdf/meshes/right_palm_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_palm_link.STL | `1ba4495e3b7a…` | ✓ |
| urdf/meshes/right_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_shoulder_pitch_link.STL | `0e4ca045ba6d…` | ✓ |
| urdf/meshes/right_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_shoulder_roll_link.STL | `0c3b6f453e93…` | ✓ |
| urdf/meshes/right_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_wrist_pitch_link.STL | `25538e72b962…` | ✓ |
| urdf/meshes/right_wrist_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_wrist_roll_link.STL | `e48d25ea4be3…` | ✓ |
| urdf/meshes/right_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/right_wrist_yaw_link.STL | `2b6ce1d4710e…` | ✓ |
| urdf/meshes/trunk.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/trunk.STL | `52afacf37b33…` | ✓ |
| urdf/meshes/waist_pitch_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_pitch_link.STL | `ba2d7dd2d4c8…` | ✓ |
| urdf/meshes/waist_roll_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_roll_link.STL | `2196475c282f…` | ✓ |
| urdf/meshes/waist_yaw_link.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_yaw_link.STL | `c0950ebf894f…` | ✓ |
| urdf/meshes/waist_yaw_link_collision.STL | booster_assets/robots/T2/T2_31dof_WujiHand/meshes/waist_yaw_link_collision.STL | `3767612763d5…` | ✓ |

## 排除清单（config s4.excluded）



**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 1）
