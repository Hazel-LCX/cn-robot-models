# S4 入库对账报告 — agibot_x2（2026-10-11 21:38）

**物理文件口径（终审 F1 修正）**：入库物理文件 83 = raw 溯源件 83（URDF 引用 72 处 → 网格物理文件 40，引用行 ≠ 文件数） + 质检自产件 0[]；**总 158.0 MB（raw 溯源件 157,985,610 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 40 · image 1 · mesh 40 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 83 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 72 处引用 → 40 个物理网格 vs MJCF 侧 40 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | PASS | raw 全量 82（除 .git/manifest）= 根级及中间层 4 + 目标子目录 78；子目录 78 全覆盖 = 入库唯一源 43；物理落位 83 件（40 件为双侧同源网格重复落位，同源同内容、两侧引用协议各自独立目录） + 排除 35（其中 meshes/ 冗余 0）（未覆盖：无）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/X2-Ultra.xml 编译通过：nbody=33 ngeom=99 nmesh=40（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：39 links（relative（./ 前缀）——meshes/ 与 urdf 同目录） |

## 逐文件对账（raw 溯源件 83）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| images/x2_ultra_new_version.png | agibot_x2_urdf/X2_URDF-v1.4.0/visual/x2_ultra_new_version.png | `0be303c8b6ce…` | ✓ |
| mjcf/X2-Ultra.xml | agibot_x2_urdf/X2_URDF-v1.4.0/X2-Ultra.xml | `20119fc61f43…` | ✓ |
| mjcf/meshes/agibot.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/agibot.stl | `a9465b48bc12…` | ✓ |
| mjcf/meshes/head_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/head_pitch_link.stl | `765cd7690f86…` | ✓ |
| mjcf/meshes/head_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/head_yaw_link.stl | `06060e2d2c61…` | ✓ |
| mjcf/meshes/imu_in_pelvis_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/imu_in_pelvis_link.stl | `0ff4fb344761…` | ✓ |
| mjcf/meshes/imu_in_torso_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/imu_in_torso_link.stl | `06a95800f316…` | ✓ |
| mjcf/meshes/left_ankle_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_ankle_pitch_link.stl | `7b9171cb1d41…` | ✓ |
| mjcf/meshes/left_ankle_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_ankle_roll_link.stl | `89f4c318ec03…` | ✓ |
| mjcf/meshes/left_elbow_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_elbow_link.stl | `49346d3f616b…` | ✓ |
| mjcf/meshes/left_hip_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_hip_pitch_link.stl | `3248cfcb160a…` | ✓ |
| mjcf/meshes/left_hip_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_hip_roll_link.stl | `d3fbaa7ac96d…` | ✓ |
| mjcf/meshes/left_hip_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_hip_yaw_link.stl | `cb99a65a4beb…` | ✓ |
| mjcf/meshes/left_knee_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_knee_link.stl | `79437cc841ab…` | ✓ |
| mjcf/meshes/left_shoulder_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_shoulder_pitch_link.stl | `bc6faae5931e…` | ✓ |
| mjcf/meshes/left_shoulder_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_shoulder_roll_link.stl | `607ca0c704eb…` | ✓ |
| mjcf/meshes/left_shoulder_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_shoulder_yaw_link.stl | `8448bbfe7e22…` | ✓ |
| mjcf/meshes/left_wrist_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_pitch_link.stl | `e788de51902a…` | ✓ |
| mjcf/meshes/left_wrist_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_roll_link.stl | `690c3d6199b9…` | ✓ |
| mjcf/meshes/left_wrist_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_yaw_link.stl | `f12fd39300f5…` | ✓ |
| mjcf/meshes/lidar_chest_front_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/lidar_chest_front_link.stl | `c17ad52f27c3…` | ✓ |
| mjcf/meshes/pelvis.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/pelvis.stl | `19a02d072eb3…` | ✓ |
| mjcf/meshes/rgb_head_center_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/rgb_head_center_link.stl | `b101df14d774…` | ✓ |
| mjcf/meshes/rgb_head_rear_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/rgb_head_rear_link.stl | `d65da262f1b8…` | ✓ |
| mjcf/meshes/rgbd_head_front_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/rgbd_head_front_link.stl | `74012dc6ccef…` | ✓ |
| mjcf/meshes/right_ankle_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_ankle_pitch_link.stl | `f7c4377a6b27…` | ✓ |
| mjcf/meshes/right_ankle_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_ankle_roll_link.stl | `39049286d27d…` | ✓ |
| mjcf/meshes/right_elbow_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_elbow_link.stl | `d874d0305577…` | ✓ |
| mjcf/meshes/right_hip_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_hip_pitch_link.stl | `9ca2c8d8b1a6…` | ✓ |
| mjcf/meshes/right_hip_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_hip_roll_link.stl | `5ca3e69d45bf…` | ✓ |
| mjcf/meshes/right_hip_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_hip_yaw_link.stl | `ab21ff019f81…` | ✓ |
| mjcf/meshes/right_knee_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_knee_link.stl | `0205f0d01727…` | ✓ |
| mjcf/meshes/right_shoulder_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_shoulder_pitch_link.stl | `3d7a48fd4724…` | ✓ |
| mjcf/meshes/right_shoulder_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_shoulder_roll_link.stl | `97e0353794f2…` | ✓ |
| mjcf/meshes/right_shoulder_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_shoulder_yaw_link.stl | `3cc9bcf54a77…` | ✓ |
| mjcf/meshes/right_wrist_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_pitch_link.stl | `6b443af3e4c1…` | ✓ |
| mjcf/meshes/right_wrist_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_roll_link.stl | `f6ed0a2a0140…` | ✓ |
| mjcf/meshes/right_wrist_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_yaw_link.stl | `4cb4c932f96f…` | ✓ |
| mjcf/meshes/stereo_head_front_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/stereo_head_front_link.stl | `3959f7521b50…` | ✓ |
| mjcf/meshes/torso_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/torso_link.stl | `5f179c78e9ec…` | ✓ |
| mjcf/meshes/waist_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/waist_pitch_link.stl | `23e9c15ec385…` | ✓ |
| mjcf/meshes/waist_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/waist_yaw_link.stl | `72eb27c1384f…` | ✓ |
| urdf/X2-Ultra.urdf | agibot_x2_urdf/X2_URDF-v1.4.0/X2-Ultra.urdf | `5973626d3639…` | ✓ |
| urdf/meshes/agibot.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/agibot.stl | `a9465b48bc12…` | ✓ |
| urdf/meshes/head_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/head_pitch_link.stl | `765cd7690f86…` | ✓ |
| urdf/meshes/head_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/head_yaw_link.stl | `06060e2d2c61…` | ✓ |
| urdf/meshes/imu_in_pelvis_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/imu_in_pelvis_link.stl | `0ff4fb344761…` | ✓ |
| urdf/meshes/imu_in_torso_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/imu_in_torso_link.stl | `06a95800f316…` | ✓ |
| urdf/meshes/left_ankle_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_ankle_pitch_link.stl | `7b9171cb1d41…` | ✓ |
| urdf/meshes/left_ankle_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_ankle_roll_link.stl | `89f4c318ec03…` | ✓ |
| urdf/meshes/left_elbow_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_elbow_link.stl | `49346d3f616b…` | ✓ |
| urdf/meshes/left_hip_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_hip_pitch_link.stl | `3248cfcb160a…` | ✓ |
| urdf/meshes/left_hip_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_hip_roll_link.stl | `d3fbaa7ac96d…` | ✓ |
| urdf/meshes/left_hip_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_hip_yaw_link.stl | `cb99a65a4beb…` | ✓ |
| urdf/meshes/left_knee_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_knee_link.stl | `79437cc841ab…` | ✓ |
| urdf/meshes/left_shoulder_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_shoulder_pitch_link.stl | `bc6faae5931e…` | ✓ |
| urdf/meshes/left_shoulder_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_shoulder_roll_link.stl | `607ca0c704eb…` | ✓ |
| urdf/meshes/left_shoulder_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_shoulder_yaw_link.stl | `8448bbfe7e22…` | ✓ |
| urdf/meshes/left_wrist_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_pitch_link.stl | `e788de51902a…` | ✓ |
| urdf/meshes/left_wrist_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_roll_link.stl | `690c3d6199b9…` | ✓ |
| urdf/meshes/left_wrist_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_yaw_link.stl | `f12fd39300f5…` | ✓ |
| urdf/meshes/lidar_chest_front_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/lidar_chest_front_link.stl | `c17ad52f27c3…` | ✓ |
| urdf/meshes/pelvis.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/pelvis.stl | `19a02d072eb3…` | ✓ |
| urdf/meshes/rgb_head_center_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/rgb_head_center_link.stl | `b101df14d774…` | ✓ |
| urdf/meshes/rgb_head_rear_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/rgb_head_rear_link.stl | `d65da262f1b8…` | ✓ |
| urdf/meshes/rgbd_head_front_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/rgbd_head_front_link.stl | `74012dc6ccef…` | ✓ |
| urdf/meshes/right_ankle_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_ankle_pitch_link.stl | `f7c4377a6b27…` | ✓ |
| urdf/meshes/right_ankle_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_ankle_roll_link.stl | `39049286d27d…` | ✓ |
| urdf/meshes/right_elbow_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_elbow_link.stl | `d874d0305577…` | ✓ |
| urdf/meshes/right_hip_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_hip_pitch_link.stl | `9ca2c8d8b1a6…` | ✓ |
| urdf/meshes/right_hip_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_hip_roll_link.stl | `5ca3e69d45bf…` | ✓ |
| urdf/meshes/right_hip_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_hip_yaw_link.stl | `ab21ff019f81…` | ✓ |
| urdf/meshes/right_knee_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_knee_link.stl | `0205f0d01727…` | ✓ |
| urdf/meshes/right_shoulder_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_shoulder_pitch_link.stl | `3d7a48fd4724…` | ✓ |
| urdf/meshes/right_shoulder_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_shoulder_roll_link.stl | `97e0353794f2…` | ✓ |
| urdf/meshes/right_shoulder_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_shoulder_yaw_link.stl | `3cc9bcf54a77…` | ✓ |
| urdf/meshes/right_wrist_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_pitch_link.stl | `6b443af3e4c1…` | ✓ |
| urdf/meshes/right_wrist_roll_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_roll_link.stl | `f6ed0a2a0140…` | ✓ |
| urdf/meshes/right_wrist_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_yaw_link.stl | `4cb4c932f96f…` | ✓ |
| urdf/meshes/stereo_head_front_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/stereo_head_front_link.stl | `3959f7521b50…` | ✓ |
| urdf/meshes/torso_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/torso_link.stl | `5f179c78e9ec…` | ✓ |
| urdf/meshes/waist_pitch_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/waist_pitch_link.stl | `23e9c15ec385…` | ✓ |
| urdf/meshes/waist_yaw_link.stl | agibot_x2_urdf/X2_URDF-v1.4.0/meshes/waist_yaw_link.stl | `72eb27c1384f…` | ✓ |

## 排除清单（config s4.excluded）

- `agibot_x2_urdf/X2_URDF-v1.4.0/X2-EDU.urdf` — EDU 教育版配对成员——R17 锚点=X2-Ultra，不入库只记录
- `agibot_x2_urdf/X2_URDF-v1.4.0/X2-EDU.xml` — EDU 教育版配对成员——R17 锚点=X2-Ultra，不入库只记录
- `agibot_x2_urdf/X2_URDF-v1.4.0/X2-EDU_simple_collision.urdf` — 简化碰撞变体，不入库只记录
- `agibot_x2_urdf/X2_URDF-v1.4.0/X2-Ultra_omnihand.urdf` — 灵巧手变体 URDF-only 无 MJCF 配对，不入库只记录
- `agibot_x2_urdf/X2_URDF-v1.4.0/X2-Ultra_omnipicker.urdf` — 夹爪变体 URDF-only 无 MJCF 配对，不入库只记录
- `agibot_x2_urdf/X2_URDF-v1.4.0/X2-Ultra_simple_collision.urdf` — 简化碰撞变体，不入库只记录
- `agibot_x2_urdf/X2_URDF-v1.4.0/scene.xml` — 场景件非机器人模型，不入库只记录
- `agibot_x2_urdf/X2_URDF-v1.4.0/README.md` — 子目录内说明文档（非模型资产；根级 README/官方声明已走 evidence 流程）
- `agibot_x2_urdf/X2_URDF-v1.4.0/README_CN.md` — 子目录内说明文档（非模型资产）
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/meshes` — 上游杂件：内容为单字节 '.'（0x2e，xxd 实证）——上游打包事故残留非模型资产；系正经上游 blob（blob-parity 在册），不入库只留痕
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/base_link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/finger_abad.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/finger_dip.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/finger_pip.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/l_palm.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/l_thumb_roll.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_roll_extend_link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/left_wrist_roll_link10.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/narrow1_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/narrow2_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/narrow3_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/narrow_loop_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/r_palm.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/r_thumb_roll.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_roll_extend_link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/right_wrist_roll_link2.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/thumb_abad.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/thumb_dip.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/thumb_mcp.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/thumb_pip.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/torso_lite_link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/wide1_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/wide2_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/wide3_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库
- `agibot_x2_urdf/X2_URDF-v1.4.0/meshes/wide_loop_Link.stl` — 变体网格池：仅被未收录变体（X2-EDU/omnihand/omnipicker/simple_collision 的手/腕/腿变体）引用，X2-Ultra 配对不引用——G1 共享池同构，闭包外不入库

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 0）
