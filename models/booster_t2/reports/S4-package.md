# S4 入库对账报告 — booster_t2（2026-10-24 22:36）

**物理文件口径（终审 F1 修正）**：入库物理文件 76 = raw 溯源件 76（URDF 引用 39 处 → 网格物理文件 37，引用行 ≠ 文件数） + 质检自产件 0[]；**总 99.1 MB（raw 溯源件 99,114,849 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 37 · mesh 37 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 76 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 39 处引用 → 37 个物理网格 vs MJCF 侧 37 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | PASS | raw 全量 45（除 .git/manifest）= 根级及中间层 5 + 目标子目录 40；子目录 40 全覆盖 = 入库唯一源 39；物理落位 76 件（37 件为双侧同源网格重复落位，同源同内容、两侧引用协议各自独立目录） + 排除 1（其中 meshes/ 冗余 0）（未覆盖：无）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/T2_31dof.xml 编译通过：nbody=33 ngeom=55 nmesh=37（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：35 links（relative（meshes/ 前缀）——meshes/ 与 urdf 同目录） |

## 逐文件对账（raw 溯源件 76）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/T2_31dof.xml | booster_assets/robots/T2/T2_31dof/T2_31dof.xml | `b147ef5d8c0c…` | ✓ |
| mjcf/meshes/head_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/head_pitch_link.STL | `f1f59dab47d9…` | ✓ |
| mjcf/meshes/head_pitch_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/head_pitch_link_collision.STL | `3ee342ea15b2…` | ✓ |
| mjcf/meshes/head_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/head_yaw_link.STL | `82837cb3b7d1…` | ✓ |
| mjcf/meshes/left_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_ankle_pitch_link.STL | `68e0ea886e54…` | ✓ |
| mjcf/meshes/left_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_ankle_roll_link.STL | `feeb92e5ff35…` | ✓ |
| mjcf/meshes/left_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_elbow_pitch_link.STL | `7a629fe2ce05…` | ✓ |
| mjcf/meshes/left_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_elbow_yaw_link.STL | `35afa050a21f…` | ✓ |
| mjcf/meshes/left_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_hip_pitch_link.STL | `75e86c93f4f3…` | ✓ |
| mjcf/meshes/left_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_hip_roll_link.STL | `a712069ff473…` | ✓ |
| mjcf/meshes/left_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_hip_yaw_link.STL | `1a48820e718a…` | ✓ |
| mjcf/meshes/left_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_knee_pitch_link.STL | `ee66d048f415…` | ✓ |
| mjcf/meshes/left_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_shoulder_pitch_link.STL | `37a19783477a…` | ✓ |
| mjcf/meshes/left_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_shoulder_roll_link.STL | `d10c4f38c0fd…` | ✓ |
| mjcf/meshes/left_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_pitch_link.STL | `85085ba79d4c…` | ✓ |
| mjcf/meshes/left_wrist_roll_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_roll_link_collision.STL | `fa648fbdc092…` | ✓ |
| mjcf/meshes/left_wrist_roll_link_with_hand.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_roll_link_with_hand.STL | `2d866fe2e7e0…` | ✓ |
| mjcf/meshes/left_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_yaw_link.STL | `bfc1d2685458…` | ✓ |
| mjcf/meshes/logo.STL | booster_assets/robots/T2/T2_31dof/meshes/logo.STL | `58edab292a58…` | ✓ |
| mjcf/meshes/right_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_ankle_pitch_link.STL | `c65638beb7e0…` | ✓ |
| mjcf/meshes/right_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_ankle_roll_link.STL | `a61e8f7879fd…` | ✓ |
| mjcf/meshes/right_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_elbow_pitch_link.STL | `1d8d06a76e0f…` | ✓ |
| mjcf/meshes/right_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_elbow_yaw_link.STL | `d6600efeefb0…` | ✓ |
| mjcf/meshes/right_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_hip_pitch_link.STL | `9ba846267032…` | ✓ |
| mjcf/meshes/right_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_hip_roll_link.STL | `1aacf29649c0…` | ✓ |
| mjcf/meshes/right_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_hip_yaw_link.STL | `5bfda02be110…` | ✓ |
| mjcf/meshes/right_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_knee_pitch_link.STL | `a04304cce3fe…` | ✓ |
| mjcf/meshes/right_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_shoulder_pitch_link.STL | `0e4ca045ba6d…` | ✓ |
| mjcf/meshes/right_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_shoulder_roll_link.STL | `0c3b6f453e93…` | ✓ |
| mjcf/meshes/right_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_pitch_link.STL | `25538e72b962…` | ✓ |
| mjcf/meshes/right_wrist_roll_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_roll_link_collision.STL | `a90f223f0a93…` | ✓ |
| mjcf/meshes/right_wrist_roll_link_with_hand.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_roll_link_with_hand.STL | `f5b4955689b6…` | ✓ |
| mjcf/meshes/right_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_yaw_link.STL | `2b6ce1d4710e…` | ✓ |
| mjcf/meshes/trunk.STL | booster_assets/robots/T2/T2_31dof/meshes/trunk.STL | `52afacf37b33…` | ✓ |
| mjcf/meshes/waist_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_pitch_link.STL | `ba2d7dd2d4c8…` | ✓ |
| mjcf/meshes/waist_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_roll_link.STL | `2196475c282f…` | ✓ |
| mjcf/meshes/waist_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_yaw_link.STL | `c0950ebf894f…` | ✓ |
| mjcf/meshes/waist_yaw_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_yaw_link_collision.STL | `3767612763d5…` | ✓ |
| urdf/T2_31dof.urdf | booster_assets/robots/T2/T2_31dof/T2_31dof.urdf | `1833e3e82f23…` | ✓ |
| urdf/meshes/head_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/head_pitch_link.STL | `f1f59dab47d9…` | ✓ |
| urdf/meshes/head_pitch_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/head_pitch_link_collision.STL | `3ee342ea15b2…` | ✓ |
| urdf/meshes/head_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/head_yaw_link.STL | `82837cb3b7d1…` | ✓ |
| urdf/meshes/left_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_ankle_pitch_link.STL | `68e0ea886e54…` | ✓ |
| urdf/meshes/left_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_ankle_roll_link.STL | `feeb92e5ff35…` | ✓ |
| urdf/meshes/left_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_elbow_pitch_link.STL | `7a629fe2ce05…` | ✓ |
| urdf/meshes/left_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_elbow_yaw_link.STL | `35afa050a21f…` | ✓ |
| urdf/meshes/left_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_hip_pitch_link.STL | `75e86c93f4f3…` | ✓ |
| urdf/meshes/left_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_hip_roll_link.STL | `a712069ff473…` | ✓ |
| urdf/meshes/left_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_hip_yaw_link.STL | `1a48820e718a…` | ✓ |
| urdf/meshes/left_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_knee_pitch_link.STL | `ee66d048f415…` | ✓ |
| urdf/meshes/left_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_shoulder_pitch_link.STL | `37a19783477a…` | ✓ |
| urdf/meshes/left_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_shoulder_roll_link.STL | `d10c4f38c0fd…` | ✓ |
| urdf/meshes/left_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_pitch_link.STL | `85085ba79d4c…` | ✓ |
| urdf/meshes/left_wrist_roll_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_roll_link_collision.STL | `fa648fbdc092…` | ✓ |
| urdf/meshes/left_wrist_roll_link_with_hand.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_roll_link_with_hand.STL | `2d866fe2e7e0…` | ✓ |
| urdf/meshes/left_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/left_wrist_yaw_link.STL | `bfc1d2685458…` | ✓ |
| urdf/meshes/logo.STL | booster_assets/robots/T2/T2_31dof/meshes/logo.STL | `58edab292a58…` | ✓ |
| urdf/meshes/right_ankle_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_ankle_pitch_link.STL | `c65638beb7e0…` | ✓ |
| urdf/meshes/right_ankle_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_ankle_roll_link.STL | `a61e8f7879fd…` | ✓ |
| urdf/meshes/right_elbow_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_elbow_pitch_link.STL | `1d8d06a76e0f…` | ✓ |
| urdf/meshes/right_elbow_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_elbow_yaw_link.STL | `d6600efeefb0…` | ✓ |
| urdf/meshes/right_hip_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_hip_pitch_link.STL | `9ba846267032…` | ✓ |
| urdf/meshes/right_hip_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_hip_roll_link.STL | `1aacf29649c0…` | ✓ |
| urdf/meshes/right_hip_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_hip_yaw_link.STL | `5bfda02be110…` | ✓ |
| urdf/meshes/right_knee_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_knee_pitch_link.STL | `a04304cce3fe…` | ✓ |
| urdf/meshes/right_shoulder_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_shoulder_pitch_link.STL | `0e4ca045ba6d…` | ✓ |
| urdf/meshes/right_shoulder_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_shoulder_roll_link.STL | `0c3b6f453e93…` | ✓ |
| urdf/meshes/right_wrist_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_pitch_link.STL | `25538e72b962…` | ✓ |
| urdf/meshes/right_wrist_roll_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_roll_link_collision.STL | `a90f223f0a93…` | ✓ |
| urdf/meshes/right_wrist_roll_link_with_hand.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_roll_link_with_hand.STL | `f5b4955689b6…` | ✓ |
| urdf/meshes/right_wrist_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/right_wrist_yaw_link.STL | `2b6ce1d4710e…` | ✓ |
| urdf/meshes/trunk.STL | booster_assets/robots/T2/T2_31dof/meshes/trunk.STL | `52afacf37b33…` | ✓ |
| urdf/meshes/waist_pitch_link.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_pitch_link.STL | `ba2d7dd2d4c8…` | ✓ |
| urdf/meshes/waist_roll_link.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_roll_link.STL | `2196475c282f…` | ✓ |
| urdf/meshes/waist_yaw_link.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_yaw_link.STL | `c0950ebf894f…` | ✓ |
| urdf/meshes/waist_yaw_link_collision.STL | booster_assets/robots/T2/T2_31dof/meshes/waist_yaw_link_collision.STL | `3767612763d5…` | ✓ |

## 排除清单（config s4.excluded）

- `booster_assets/robots/T2/T2_31dof/T2_31dof_parallel.xml` — 踝并联变体 MJCF——R34 锚点=主版，R22/M7 parallel 已裁先例同款

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 0）
