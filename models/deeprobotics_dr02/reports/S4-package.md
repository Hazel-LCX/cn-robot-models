# S4 入库对账报告 — deeprobotics_dr02（2026-10-24 17:32）

**物理文件口径（终审 F1 修正）**：入库物理文件 70 = raw 溯源件 70（URDF 引用 36 处 → 网格物理文件 34，引用行 ≠ 文件数） + 质检自产件 0[]；**总 59.8 MB（raw 溯源件 59,814,966 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 34 · mesh 34 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 70 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 36 处引用 → 34 个物理网格 vs MJCF 侧 34 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | WARN | raw 全量 133（除 .git/manifest）= 根级及中间层 4 + 目标子目录 129；子目录 129 全覆盖 = 入库唯一源 70 + 排除 3（其中 meshes/ 冗余 0）（未覆盖：['deep_robotics_model/DR02/mjcf/standard/meshes/base_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/body.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_ankle_x_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_ankle_y_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_elbow_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_hip_x_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_hip_y_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_hip_z_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_knee_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_shoulder_x_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_shoulder_y_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/left_shoulder_z_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_ankle_x_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_ankle_y_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_elbow_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_hip_x_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_hip_y_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_hip_z_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_knee_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_shoulder_x_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_shoulder_y_link.STL', 'deep_robotics_model/DR02/mjcf/standard/meshes/right_shoulder_z_link.STL', 'deep_robotics_model/DR02/urdf/pro/meshes/left_wrist_x_link_simplified.STL', 'deep_robotics_model/DR02/urdf/pro/meshes/right_wrist_x_link_simplified.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/base_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/body.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_ankle_x_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_ankle_y_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_elbow_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_hip_x_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_hip_y_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_hip_z_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_knee_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_shoulder_x_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_shoulder_y_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/left_shoulder_z_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_ankle_x_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_ankle_y_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_elbow_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_hip_x_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_hip_y_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_hip_z_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_knee_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_shoulder_x_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_shoulder_y_link.STL', 'deep_robotics_model/DR02/urdf/standard/meshes/right_shoulder_z_link.STL', 'deep_robotics_model/DR02/usd/pro/DR02-pro.usd', 'deep_robotics_model/DR02/usd/pro/configuration/DR02-pro_base.usd', 'deep_robotics_model/DR02/usd/pro/configuration/DR02-pro_physics.usd', 'deep_robotics_model/DR02/usd/pro/configuration/DR02-pro_robot.usd', 'deep_robotics_model/DR02/usd/pro/configuration/DR02-pro_sensor.usd', 'deep_robotics_model/DR02/usd/standard/DR02-std.usd', 'deep_robotics_model/DR02/usd/standard/configuration/DR02-std_base.usd', 'deep_robotics_model/DR02/usd/standard/configuration/DR02-std_physics.usd', 'deep_robotics_model/DR02/usd/standard/configuration/DR02-std_robot.usd', 'deep_robotics_model/DR02/usd/standard/configuration/DR02-std_sensor.usd']）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/DR02_pro.xml 编译通过：nbody=41 ngeom=70 nmesh=34（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：40 links（relative（./ 前缀）——meshes/ 与 urdf 同目录（分目录形态）） |

## 逐文件对账（raw 溯源件 70）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/DR02_pro.xml | deep_robotics_model/DR02/mjcf/pro/DR02_pro.xml | `ee53516d4727…` | ✓ |
| mjcf/meshes/base_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/base_link.STL | `8fee7a61ae3a…` | ✓ |
| mjcf/meshes/body.STL | deep_robotics_model/DR02/mjcf/pro/meshes/body.STL | `0065326f3bad…` | ✓ |
| mjcf/meshes/head_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/head_link.STL | `5dcf25e6d2f5…` | ✓ |
| mjcf/meshes/left_ankle_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_ankle_x_link.STL | `933f1df1cde7…` | ✓ |
| mjcf/meshes/left_ankle_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_ankle_y_link.STL | `c09d127aaea4…` | ✓ |
| mjcf/meshes/left_elbow_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_elbow_link.STL | `38211d6b0d0a…` | ✓ |
| mjcf/meshes/left_hand_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_hand_link.STL | `d414b4e78039…` | ✓ |
| mjcf/meshes/left_hip_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_hip_x_link.STL | `427367a500f0…` | ✓ |
| mjcf/meshes/left_hip_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_hip_y_link.STL | `17f51f44097a…` | ✓ |
| mjcf/meshes/left_hip_z_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_hip_z_link.STL | `f7dbd864b55c…` | ✓ |
| mjcf/meshes/left_knee_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_knee_link.STL | `a77ad7e00be1…` | ✓ |
| mjcf/meshes/left_shoulder_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_shoulder_x_link.STL | `91d993c72032…` | ✓ |
| mjcf/meshes/left_shoulder_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_shoulder_y_link.STL | `5da423fdac9d…` | ✓ |
| mjcf/meshes/left_shoulder_z_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_shoulder_z_link.STL | `f8aa526e7d84…` | ✓ |
| mjcf/meshes/left_wrist_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_wrist_x_link.STL | `d8787e6d6d9f…` | ✓ |
| mjcf/meshes/left_wrist_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_wrist_y_link.STL | `9acc97064e54…` | ✓ |
| mjcf/meshes/left_wrist_z_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/left_wrist_z_link.STL | `69a19089f4da…` | ✓ |
| mjcf/meshes/neck_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/neck_link.STL | `fcc5b16a2d10…` | ✓ |
| mjcf/meshes/right_ankle_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_ankle_x_link.STL | `7423f09810dc…` | ✓ |
| mjcf/meshes/right_ankle_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_ankle_y_link.STL | `daf92711d667…` | ✓ |
| mjcf/meshes/right_elbow_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_elbow_link.STL | `16e60de1c1f4…` | ✓ |
| mjcf/meshes/right_hand_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_hand_link.STL | `87ca2b391635…` | ✓ |
| mjcf/meshes/right_hip_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_hip_x_link.STL | `8f8e6ed5af6b…` | ✓ |
| mjcf/meshes/right_hip_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_hip_y_link.STL | `e81d9cf6c396…` | ✓ |
| mjcf/meshes/right_hip_z_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_hip_z_link.STL | `b8510af591e3…` | ✓ |
| mjcf/meshes/right_knee_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_knee_link.STL | `3865e57db0dd…` | ✓ |
| mjcf/meshes/right_shoulder_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_shoulder_x_link.STL | `8194e2a4893e…` | ✓ |
| mjcf/meshes/right_shoulder_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_shoulder_y_link.STL | `441c0bb194fc…` | ✓ |
| mjcf/meshes/right_shoulder_z_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_shoulder_z_link.STL | `2153a032199c…` | ✓ |
| mjcf/meshes/right_wrist_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_wrist_x_link.STL | `5754566feb9c…` | ✓ |
| mjcf/meshes/right_wrist_y_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_wrist_y_link.STL | `5af9ef5145a9…` | ✓ |
| mjcf/meshes/right_wrist_z_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/right_wrist_z_link.STL | `2c4d7c2267e4…` | ✓ |
| mjcf/meshes/waist_x_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/waist_x_link.STL | `361668ebd468…` | ✓ |
| mjcf/meshes/waist_z_link.STL | deep_robotics_model/DR02/mjcf/pro/meshes/waist_z_link.STL | `273d64aef6b8…` | ✓ |
| urdf/DR02-pro.urdf | deep_robotics_model/DR02/urdf/pro/DR02-pro.urdf | `7d926201951d…` | ✓ |
| urdf/meshes/base_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/base_link.STL | `8fee7a61ae3a…` | ✓ |
| urdf/meshes/body.STL | deep_robotics_model/DR02/urdf/pro/meshes/body.STL | `0065326f3bad…` | ✓ |
| urdf/meshes/head_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/head_link.STL | `5dcf25e6d2f5…` | ✓ |
| urdf/meshes/left_ankle_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_ankle_x_link.STL | `933f1df1cde7…` | ✓ |
| urdf/meshes/left_ankle_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_ankle_y_link.STL | `c09d127aaea4…` | ✓ |
| urdf/meshes/left_elbow_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_elbow_link.STL | `38211d6b0d0a…` | ✓ |
| urdf/meshes/left_hand_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_hand_link.STL | `d414b4e78039…` | ✓ |
| urdf/meshes/left_hip_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_hip_x_link.STL | `427367a500f0…` | ✓ |
| urdf/meshes/left_hip_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_hip_y_link.STL | `17f51f44097a…` | ✓ |
| urdf/meshes/left_hip_z_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_hip_z_link.STL | `f7dbd864b55c…` | ✓ |
| urdf/meshes/left_knee_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_knee_link.STL | `a77ad7e00be1…` | ✓ |
| urdf/meshes/left_shoulder_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_shoulder_x_link.STL | `91d993c72032…` | ✓ |
| urdf/meshes/left_shoulder_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_shoulder_y_link.STL | `5da423fdac9d…` | ✓ |
| urdf/meshes/left_shoulder_z_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_shoulder_z_link.STL | `f8aa526e7d84…` | ✓ |
| urdf/meshes/left_wrist_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_wrist_x_link.STL | `d8787e6d6d9f…` | ✓ |
| urdf/meshes/left_wrist_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_wrist_y_link.STL | `9acc97064e54…` | ✓ |
| urdf/meshes/left_wrist_z_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/left_wrist_z_link.STL | `69a19089f4da…` | ✓ |
| urdf/meshes/neck_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/neck_link.STL | `fcc5b16a2d10…` | ✓ |
| urdf/meshes/right_ankle_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_ankle_x_link.STL | `7423f09810dc…` | ✓ |
| urdf/meshes/right_ankle_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_ankle_y_link.STL | `daf92711d667…` | ✓ |
| urdf/meshes/right_elbow_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_elbow_link.STL | `16e60de1c1f4…` | ✓ |
| urdf/meshes/right_hand_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_hand_link.STL | `87ca2b391635…` | ✓ |
| urdf/meshes/right_hip_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_hip_x_link.STL | `8f8e6ed5af6b…` | ✓ |
| urdf/meshes/right_hip_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_hip_y_link.STL | `e81d9cf6c396…` | ✓ |
| urdf/meshes/right_hip_z_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_hip_z_link.STL | `b8510af591e3…` | ✓ |
| urdf/meshes/right_knee_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_knee_link.STL | `3865e57db0dd…` | ✓ |
| urdf/meshes/right_shoulder_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_shoulder_x_link.STL | `8194e2a4893e…` | ✓ |
| urdf/meshes/right_shoulder_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_shoulder_y_link.STL | `441c0bb194fc…` | ✓ |
| urdf/meshes/right_shoulder_z_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_shoulder_z_link.STL | `2153a032199c…` | ✓ |
| urdf/meshes/right_wrist_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_wrist_x_link.STL | `5754566feb9c…` | ✓ |
| urdf/meshes/right_wrist_y_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_wrist_y_link.STL | `5af9ef5145a9…` | ✓ |
| urdf/meshes/right_wrist_z_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/right_wrist_z_link.STL | `2c4d7c2267e4…` | ✓ |
| urdf/meshes/waist_x_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/waist_x_link.STL | `361668ebd468…` | ✓ |
| urdf/meshes/waist_z_link.STL | deep_robotics_model/DR02/urdf/pro/meshes/waist_z_link.STL | `273d64aef6b8…` | ✓ |

## 排除清单（config s4.excluded）

- `deep_robotics_model/DR02/urdf/pro/DR02-pro_fix_joints.urdf` — 锁死变体（同 40 link、10 关节固化为 fixed=21R+18F）——R28 锚点=Pro 主配对，不入库只记录（T1_locomotion 同类）
- `deep_robotics_model/DR02/urdf/standard/DR02-std.urdf` — Standard 平替配对 URDF 侧（21R/68kg）——R28 裁定整组留 M6+ 维护态填充，不入库只记录
- `deep_robotics_model/DR02/mjcf/standard/DR02_std.xml` — Standard 平替配对 MJCF 侧——R28 裁定整组留 M6+，不入库只记录

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 1）
