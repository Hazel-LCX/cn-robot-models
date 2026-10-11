# S4 入库对账报告 — unitree_go2（2026-10-11 15:56）

**物理文件口径（终审 F1 修正）**：入库物理文件 34 = raw 溯源件 33（URDF 引用 17 处 → 网格物理文件 7，引用行 ≠ 文件数） + 质检自产件 1['images/preview-screenshot.png']；**总 56.1 MB（raw 溯源件 55,807,233 B + 质检自产件 312,334 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

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
| mjcf/assets/base_0.obj | unitree_mujoco/unitree_robots/go2/assets/base_0.obj | `25134a5dc51a…` | ✓ |
| mjcf/assets/base_1.obj | unitree_mujoco/unitree_robots/go2/assets/base_1.obj | `119384942f6f…` | ✓ |
| mjcf/assets/base_2.obj | unitree_mujoco/unitree_robots/go2/assets/base_2.obj | `08c84b27583b…` | ✓ |
| mjcf/assets/base_3.obj | unitree_mujoco/unitree_robots/go2/assets/base_3.obj | `c485dee967b8…` | ✓ |
| mjcf/assets/base_4.obj | unitree_mujoco/unitree_robots/go2/assets/base_4.obj | `7930e5f66140…` | ✓ |
| mjcf/assets/calf_0.obj | unitree_mujoco/unitree_robots/go2/assets/calf_0.obj | `cf31a09f9720…` | ✓ |
| mjcf/assets/calf_1.obj | unitree_mujoco/unitree_robots/go2/assets/calf_1.obj | `8c586d682059…` | ✓ |
| mjcf/assets/calf_mirror_0.obj | unitree_mujoco/unitree_robots/go2/assets/calf_mirror_0.obj | `5ed525542abd…` | ✓ |
| mjcf/assets/calf_mirror_1.obj | unitree_mujoco/unitree_robots/go2/assets/calf_mirror_1.obj | `28bbdc6311f0…` | ✓ |
| mjcf/assets/foot.obj | unitree_mujoco/unitree_robots/go2/assets/foot.obj | `228f80ff74ca…` | ✓ |
| mjcf/assets/hip_0.obj | unitree_mujoco/unitree_robots/go2/assets/hip_0.obj | `2df3b24a0012…` | ✓ |
| mjcf/assets/hip_1.obj | unitree_mujoco/unitree_robots/go2/assets/hip_1.obj | `c456392ad509…` | ✓ |
| mjcf/assets/thigh_0.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_0.obj | `201b41523863…` | ✓ |
| mjcf/assets/thigh_1.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_1.obj | `a363dd76e33e…` | ✓ |
| mjcf/assets/thigh_mirror_0.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_mirror_0.obj | `80b96e40faf2…` | ✓ |
| mjcf/assets/thigh_mirror_1.obj | unitree_mujoco/unitree_robots/go2/assets/thigh_mirror_1.obj | `3d2cf7d14ee1…` | ✓ |
| mjcf/go2.xml | unitree_mujoco/unitree_robots/go2/go2.xml | `08e3993fb258…` | ✓ |
| mjcf/scene.xml | unitree_mujoco/unitree_robots/go2/scene.xml | `e23eadbbb091…` | ✓ |
| urdf/go2_description.urdf | unitree_ros/robots/go2_description/urdf/go2_description.urdf | `252809b6d3ca…` | ✓ |
| urdf_meshes/dae/base.dae | unitree_ros/robots/go2_description/dae/base.dae | `f777940215d5…` | ✓ |
| urdf_meshes/dae/calf.dae | unitree_ros/robots/go2_description/dae/calf.dae | `a875e0e2bb24…` | ✓ |
| urdf_meshes/dae/calf_mirror.dae | unitree_ros/robots/go2_description/dae/calf_mirror.dae | `c65ac56ddfca…` | ✓ |
| urdf_meshes/dae/foot.dae | unitree_ros/robots/go2_description/dae/foot.dae | `f37a2d16dd2e…` | ✓ |
| urdf_meshes/dae/hip.dae | unitree_ros/robots/go2_description/dae/hip.dae | `1f1a02068305…` | ✓ |
| urdf_meshes/dae/thigh.dae | unitree_ros/robots/go2_description/dae/thigh.dae | `167a6c6545f7…` | ✓ |
| urdf_meshes/dae/thigh_mirror.dae | unitree_ros/robots/go2_description/dae/thigh_mirror.dae | `ab1d3b0ef118…` | ✓ |
| xacro/const.xacro | unitree_ros/robots/go2_description/xacro/const.xacro | `fec485669d74…` | ✓ |
| xacro/gazebo.xacro | unitree_ros/robots/go2_description/xacro/gazebo.xacro | `6a5663dc0be1…` | ✓ |
| xacro/leg.xacro | unitree_ros/robots/go2_description/xacro/leg.xacro | `5f2e1b5f5da2…` | ✓ |
| xacro/materials.xacro | unitree_ros/robots/go2_description/xacro/materials.xacro | `5335e8a1c02e…` | ✓ |
| xacro/robot.xacro | unitree_ros/robots/go2_description/xacro/robot.xacro | `82931c266f08…` | ✓ |
| xacro/transmission.xacro | unitree_ros/robots/go2_description/xacro/transmission.xacro | `aa297bf9bc39…` | ✓ |

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
