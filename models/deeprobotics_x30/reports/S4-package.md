# S4 入库对账报告 — deeprobotics_x30（2026-10-25 18:45）

**物理文件口径（终审 F1 修正）**：入库物理文件 10 = raw 溯源件 10（URDF 引用 13 处 → 网格物理文件 4，引用行 ≠ 文件数） + 质检自产件 0[]；**总 8.4 MB（raw 溯源件 8,423,759 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 4 · mesh 4 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 10 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 13 处引用 → 4 个物理网格 vs MJCF 侧 4 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | WARN | raw 全量 19（除 .git/manifest）= 根级及中间层 4 + 目标子目录 15；子目录 15 全覆盖 = 入库唯一源 10 + 排除 0（其中 meshes/ 冗余 0）（未覆盖：['deep_robotics_model/X30/usd/X30.usd', 'deep_robotics_model/X30/usd/configuration/X30_base.usd', 'deep_robotics_model/X30/usd/configuration/X30_physics.usd', 'deep_robotics_model/X30/usd/configuration/X30_robot.usd', 'deep_robotics_model/X30/usd/configuration/X30_sensor.usd']）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/X30.xml 编译通过：nbody=22 ngeom=35 nmesh=8（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：21 links（relative（./ 前缀）——meshes/ 与 urdf 同目录） |

## 逐文件对账（raw 溯源件 10）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/X30.xml | deep_robotics_model/X30/mjcf/X30.xml | `1573299d7477…` | ✓ |
| mjcf/meshes/hip.STL | deep_robotics_model/X30/mjcf/meshes/hip.STL | `a943a6359982…` | ✓ |
| mjcf/meshes/shank.STL | deep_robotics_model/X30/mjcf/meshes/shank.STL | `c61f6fa87a12…` | ✓ |
| mjcf/meshes/thigh.STL | deep_robotics_model/X30/mjcf/meshes/thigh.STL | `40acfaff81d2…` | ✓ |
| mjcf/meshes/torso.STL | deep_robotics_model/X30/mjcf/meshes/torso.STL | `d44d38c10db3…` | ✓ |
| urdf/X30.urdf | deep_robotics_model/X30/urdf/X30.urdf | `e69196c62c15…` | ✓ |
| urdf/meshes/hip.STL | deep_robotics_model/X30/urdf/meshes/hip.STL | `a943a6359982…` | ✓ |
| urdf/meshes/shank.STL | deep_robotics_model/X30/urdf/meshes/shank.STL | `c61f6fa87a12…` | ✓ |
| urdf/meshes/thigh.STL | deep_robotics_model/X30/urdf/meshes/thigh.STL | `40acfaff81d2…` | ✓ |
| urdf/meshes/torso.STL | deep_robotics_model/X30/urdf/meshes/torso.STL | `d44d38c10db3…` | ✓ |

## 排除清单（config s4.excluded）



**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 1）
