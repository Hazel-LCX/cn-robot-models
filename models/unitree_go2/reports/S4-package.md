# S4 入库对账报告 — unitree_go2（2026-10-11 17:25）

**物理文件口径（终审 F1 修正）**：入库物理文件 34 = raw 溯源件 33（URDF 引用 17 处 → 网格物理文件 7，引用行 ≠ 文件数） + 质检自产件 1['images/preview-screenshot.png']；**总 55.4 MB（raw 溯源件 55,045,611 B + 质检自产件 312,334 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 16 · image 1 · mesh 7 · mjcf 2 · urdf 1 · xacro 6 · 质检自产 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 33 个 raw 源入库文件 SHA256 全部命中 raw manifest 同路径行（逐文件可溯源） |
| `s4:mesh-split-decision` | PASS | URDF 侧 17 处引用 → 7 个物理网格（dae）vs MJCF 侧 16 个（obj），哈希交集 0 → 决策：分目录；MJCF 网格落位 mjcf/assets/（保持官方 meshdir 相对引用，不改官方一字节——§4 树中 mjcf_meshes/ 的实际形态，记录在案） |
| `s4:dae-dir-parity` | PASS | dae/ 与 meshes/ 同名对比（R3-D3 判定，物理文件口径）：同内容 7，不同 0[]，单侧 0——meshes/ 为同内容冗余目录，不随库分发 |
| `s4:coverage` | PASS | raw 全量 62（除 .git/manifest）= 根级及中间层 9 + 目标子目录 53；子目录 53 全覆盖 = 入库 33 + 排除 20（其中 meshes/ 冗余 7）（未覆盖：无）——算式每行必须平（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/go2.xml 编译通过：nbody=18 ngeom=56（meshdir=assets 相对结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：42 links（package:// 重映射到 urdf_meshes/） |

## 逐文件对账（raw 溯源件 33）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| images/Go2.png | unitree_mujoco/unitree_robots/go2/Go2.png | `78d864b80648…` | ✓ |
| mjcf/assets/base_0.obj | unitree_mujoco/unitree_robots/go2/assets/base_0.obj | `8cdc53719002…` | ✓ |
| mjcf/assets/base_1.obj | unitree_mujoco/unitree_robots/go2/assets/base_1.obj | `39d2f4724ff6…` | ✓ |
| mjcf/assets/base_2.obj | unitree_mujoco/unitree_robots/go2/assets/base_2.obj | `29cae463f95d…` | ✓ |
| mjcf/assets/base_3.obj | unitree_mujoco/unitree_robots/go2/assets/base_3.obj | `f51ba43bf300…` | ✓ |
| mjcf/assets/base_4.obj | unitree_mujoco/unitree_robots/go2/assets/base_4.obj | `49ddec012954…` | ✓ |
| mjcf/assets/calf_0.obj | unitree_mujoco/unitree_robots/go2/assets/calf_0.obj | `4a818cd563c5…` | ✓ |
| mjcf/assets/calf_1.obj | unitree_mujoco/unitree_robots/go2/assets/calf_1.obj | `51950c3a153a…` | ✓ |
| mjcf/assets/calf_mirror_0.obj | unitree_mujoco/unitree_robots/go2/assets/calf_mirror_0.obj | `6dc0406207a1…` | ✓ |
| mjcf/assets/calf_mirror_1.obj | unitree_mujoco/unitree_robots/go2/assets/calf_mirror_1.obj | `f84f5af90b91…` | ✓ |
| mjcf/assets/foot.obj | unitree_mujoco/unitree_robots/go2/assets/foot.obj | `df9e78a7c011…` | ✓ |
| mjcf/assets/hip_0.obj | unitree_mujoco/unitree_robots/go2/assets/hip_0.obj | `cc29932ab4d2…` | ✓ |
| mjcf/assets/hip_1.obj | unitree_mujoco/unitree_robots/go2/assets/hip_1.obj | `3fd5bd9b2ef6…` | ✓ |
| mjcf/assets/thigh_0.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_0.obj | `bb3edfe6a7b0…` | ✓ |
| mjcf/assets/thigh_1.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_1.obj | `3a631822f9f7…` | ✓ |
| mjcf/assets/thigh_mirror_0.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_mirror_0.obj | `07abaedce761…` | ✓ |
| mjcf/assets/thigh_mirror_1.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_mirror_1.obj | `db984a3e983e…` | ✓ |
| mjcf/go2.xml | unitree_mujoco/unitree_robots/go2/go2.xml | `2014a3d76e30…` | ✓ |
| mjcf/scene.xml | unitree_mujoco/unitree_robots/go2/scene.xml | `6c1fda780e78…` | ✓ |
| urdf/go2_description.urdf | unitree_ros/robots/go2_description/urdf/go2_description.urdf | `7d19fe48e2e6…` | ✓ |
| urdf_meshes/dae/base.dae | unitree_ros/robots/go2_description/dae/base.dae | `e52bebbb5c7f…` | ✓ |
| urdf_meshes/dae/calf.dae | unitree_ros/robots/go2_description/dae/calf.dae | `29872fa1a435…` | ✓ |
| urdf_meshes/dae/calf_mirror.dae | unitree_ros/robots/go2_description/dae/calf_mirror.dae | `79c66be7ed06…` | ✓ |
| urdf_meshes/dae/foot.dae | unitree_ros/robots/go2_description/dae/foot.dae | `ffbd95fd6418…` | ✓ |
| urdf_meshes/dae/hip.dae | unitree_ros/robots/go2_description/dae/hip.dae | `8735e10617af…` | ✓ |
| urdf_meshes/dae/thigh.dae | unitree_ros/robots/go2_description/dae/thigh.dae | `a622381ae308…` | ✓ |
| urdf_meshes/dae/thigh_mirror.dae | unitree_ros/robots/go2_description/dae/thigh_mirror.dae | `c7bae0b0565c…` | ✓ |
| xacro/const.xacro | unitree_ros/robots/go2_description/xacro/const.xacro | `c4f4a69c8ea1…` | ✓ |
| xacro/gazebo.xacro | unitree_ros/robots/go2_description/xacro/gazebo.xacro | `958454496b23…` | ✓ |
| xacro/leg.xacro | unitree_ros/robots/go2_description/xacro/leg.xacro | `c26f92bae9ac…` | ✓ |
| xacro/materials.xacro | unitree_ros/robots/go2_description/xacro/materials.xacro | `eb45dfe0751c…` | ✓ |
| xacro/robot.xacro | unitree_ros/robots/go2_description/xacro/robot.xacro | `8cc8dfb8259d…` | ✓ |
| xacro/transmission.xacro | unitree_ros/robots/go2_description/xacro/transmission.xacro | `f4a0fc2c5df4…` | ✓ |

## 排除清单（config s4.excluded）

- `unitree_ros/robots/README.md` — robots 中间层上游文档，非模型件（G2 补桶）
- `unitree_mujoco/unitree_robots/go2/scene_terrain.xml` — 地形演示件，非模型必需
- `unitree_mujoco/unitree_robots/go2/height_field.png` — scene_terrain 专用地形图
- `unitree_mujoco/unitree_robots/go2/unitree_hfield.png` — scene_terrain 专用地形图
- `unitree_ros/robots/go2_description/launch` — ROS 运行件，与模型无关（目录）
- `unitree_ros/robots/go2_description/config` — ROS 运行件，与模型无关（目录）
- `unitree_ros/robots/go2_description/CMakeLists.txt` — ROS 构建件
- `unitree_ros/robots/go2_description/package.xml` — ROS 包清单（license 结论已在 SOURCE.md）
- `unitree_ros/robots/go2_description/README.md` — 上游包文档，不随库分发
- `unitree_ros/robots/go2_description/urdf/Amended_collision_model.png` — 上游碰撞示意图，S3 报告引用名即可
- `unitree_ros/robots/go2_description/urdf/Normal_collision_model.png` — 同上

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 0）
