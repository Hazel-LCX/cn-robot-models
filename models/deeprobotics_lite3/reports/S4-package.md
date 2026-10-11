# S4 入库对账报告 — deeprobotics_lite3（2026-10-11 19:50）

**物理文件口径（终审 F1 修正）**：入库物理文件 10 = raw 溯源件 10（URDF 引用 13 处 → 网格物理文件 4，引用行 ≠ 文件数） + 质检自产件 0[]；**总 7.0 MB（raw 溯源件 7,021,712 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 4 · mesh 4 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 10 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 13 处引用 → 4 个物理网格 vs MJCF 侧 4 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | PASS | raw 全量 19（除 .git/manifest）= 根级及中间层 4 + 目标子目录 15；子目录 15 全覆盖 = 入库 10 + 排除 5（其中 meshes/ 冗余 0）（未覆盖：无）——算式每行必须平（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/Lite3.xml 编译通过：nbody=18 ngeom=35 nmesh=13（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：17 links（relative（./ 前缀）——meshes/ 与 urdf 同目录） |

## 逐文件对账（raw 溯源件 10）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/Lite3.xml | deep_robotics_model/Lite3/mjcf/Lite3.xml | `512a93c353e1…` | ✓ |
| mjcf/meshes/hip.STL | deep_robotics_model/Lite3/mjcf/meshes/hip.STL | `3386fa94992d…` | ✓ |
| mjcf/meshes/shank.STL | deep_robotics_model/Lite3/mjcf/meshes/shank.STL | `5410bae3b9b1…` | ✓ |
| mjcf/meshes/thigh.STL | deep_robotics_model/Lite3/mjcf/meshes/thigh.STL | `f29ea97407a9…` | ✓ |
| mjcf/meshes/torso.STL | deep_robotics_model/Lite3/mjcf/meshes/torso.STL | `6f3f5fc4b998…` | ✓ |
| urdf/Lite3.urdf | deep_robotics_model/Lite3/urdf/Lite3.urdf | `ff71ca27f756…` | ✓ |
| urdf/meshes/hip.STL | deep_robotics_model/Lite3/urdf/meshes/hip.STL | `3386fa94992d…` | ✓ |
| urdf/meshes/shank.STL | deep_robotics_model/Lite3/urdf/meshes/shank.STL | `5410bae3b9b1…` | ✓ |
| urdf/meshes/thigh.STL | deep_robotics_model/Lite3/urdf/meshes/thigh.STL | `f29ea97407a9…` | ✓ |
| urdf/meshes/torso.STL | deep_robotics_model/Lite3/urdf/meshes/torso.STL | `6f3f5fc4b998…` | ✓ |

## 排除清单（config s4.excluded）

- `deep_robotics_model/Lite3/usd/configuration/Lite3_base.usd` — USD 格式件，超出本库 URDF/MJCF 双格式范围（R14 送审件已声明 excluded）
- `deep_robotics_model/Lite3/usd/configuration/Lite3_physics.usd` — USD 格式件，超出本库 URDF/MJCF 双格式范围（R14 送审件已声明 excluded）
- `deep_robotics_model/Lite3/usd/configuration/Lite3_robot.usd` — USD 格式件，超出本库 URDF/MJCF 双格式范围（R14 送审件已声明 excluded）
- `deep_robotics_model/Lite3/usd/configuration/Lite3_sensor.usd` — USD 格式件，超出本库 URDF/MJCF 双格式范围（R14 送审件已声明 excluded）
- `deep_robotics_model/Lite3/usd/Lite3.usd` — USD 格式件，超出本库 URDF/MJCF 双格式范围（R14 送审件已声明 excluded）

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 0）
