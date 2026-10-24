# S4 入库对账报告 — deeprobotics_m20_piper（2026-10-24 23:11）

**物理文件口径（终审 F1 修正）**：入库物理文件 56 = raw 溯源件 56（URDF 引用 37 处 → 网格物理文件 27，引用行 ≠ 文件数） + 质检自产件 0[]；**总 42.3 MB（raw 溯源件 42,296,431 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 27 · mesh 27 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 56 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 37 处引用 → 27 个物理网格 vs MJCF 侧 27 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | WARN | raw 全量 65（除 .git/manifest）= 根级及中间层 4 + 目标子目录 61；子目录 61 全覆盖 = 入库唯一源 56 + 排除 0（其中 meshes/ 冗余 0）（未覆盖：['deep_robotics_model/M20_Piper/usd/M20_Piper.usd', 'deep_robotics_model/M20_Piper/usd/configuration/M20_Piper_base.usd', 'deep_robotics_model/M20_Piper/usd/configuration/M20_Piper_physics.usd', 'deep_robotics_model/M20_Piper/usd/configuration/M20_Piper_robot.usd', 'deep_robotics_model/M20_Piper/usd/configuration/M20_Piper_sensor.usd']）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/M20_Piper.xml 编译通过：nbody=28 ngeom=64 nmesh=27（官方相对引用结构保持） |
| `s4:recheck-urdf` | FAIL | ValueError: could not convert string to float: '0。611' |

## 逐文件对账（raw 溯源件 56）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/M20_Piper.xml | deep_robotics_model/M20_Piper/mjcf/M20_Piper.xml | `e768e7ed5d66…` | ✓ |
| mjcf/meshes/arm_base_link.STL | deep_robotics_model/M20_Piper/mjcf/meshes/arm_base_link.STL | `fd4a3d6d0266…` | ✓ |
| mjcf/meshes/base_link.STL | deep_robotics_model/M20_Piper/mjcf/meshes/base_link.STL | `a7984137d067…` | ✓ |
| mjcf/meshes/fl_hipx.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fl_hipx.STL | `179c63492907…` | ✓ |
| mjcf/meshes/fl_hipy.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fl_hipy.STL | `c895052a02cc…` | ✓ |
| mjcf/meshes/fl_knee.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fl_knee.STL | `c2ac2f2c9664…` | ✓ |
| mjcf/meshes/fl_wheel.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fl_wheel.STL | `bcfca68aeeb8…` | ✓ |
| mjcf/meshes/fr_hipx.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fr_hipx.STL | `350a5bca1df6…` | ✓ |
| mjcf/meshes/fr_hipy.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fr_hipy.STL | `6a776a1637c7…` | ✓ |
| mjcf/meshes/fr_knee.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fr_knee.STL | `e158a0ca5a5e…` | ✓ |
| mjcf/meshes/fr_wheel.STL | deep_robotics_model/M20_Piper/mjcf/meshes/fr_wheel.STL | `2773ffcac685…` | ✓ |
| mjcf/meshes/gripper_base.STL | deep_robotics_model/M20_Piper/mjcf/meshes/gripper_base.STL | `2895bfa6f1ee…` | ✓ |
| mjcf/meshes/hl_hipx.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hl_hipx.STL | `3c20e792611b…` | ✓ |
| mjcf/meshes/hl_hipy.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hl_hipy.STL | `d2c9efec9bfc…` | ✓ |
| mjcf/meshes/hl_knee.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hl_knee.STL | `f6897fb23e4f…` | ✓ |
| mjcf/meshes/hl_wheel.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hl_wheel.STL | `d61d98f986e9…` | ✓ |
| mjcf/meshes/hr_hipx.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hr_hipx.STL | `b49f8992cc84…` | ✓ |
| mjcf/meshes/hr_hipy.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hr_hipy.STL | `70332110c7bc…` | ✓ |
| mjcf/meshes/hr_knee.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hr_knee.STL | `2fcf688c3059…` | ✓ |
| mjcf/meshes/hr_wheel.STL | deep_robotics_model/M20_Piper/mjcf/meshes/hr_wheel.STL | `88b2fca83119…` | ✓ |
| mjcf/meshes/link1.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link1.STL | `9ee6e1d67c02…` | ✓ |
| mjcf/meshes/link2.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link2.STL | `0d37675b699b…` | ✓ |
| mjcf/meshes/link3.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link3.STL | `e8ae51f17c0c…` | ✓ |
| mjcf/meshes/link4.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link4.STL | `efa330229762…` | ✓ |
| mjcf/meshes/link5.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link5.STL | `a1c69d1c7f6f…` | ✓ |
| mjcf/meshes/link6.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link6.STL | `88374973bc3b…` | ✓ |
| mjcf/meshes/link7.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link7.STL | `475a7d8db056…` | ✓ |
| mjcf/meshes/link8.STL | deep_robotics_model/M20_Piper/mjcf/meshes/link8.STL | `3f88d534a85e…` | ✓ |
| urdf/M20_Piper.urdf | deep_robotics_model/M20_Piper/urdf/M20_Piper.urdf | `68a655fe16c1…` | ✓ |
| urdf/meshes/arm_base_link.STL | deep_robotics_model/M20_Piper/urdf/meshes/arm_base_link.STL | `fd4a3d6d0266…` | ✓ |
| urdf/meshes/base_link.STL | deep_robotics_model/M20_Piper/urdf/meshes/base_link.STL | `a7984137d067…` | ✓ |
| urdf/meshes/fl_hipx.STL | deep_robotics_model/M20_Piper/urdf/meshes/fl_hipx.STL | `179c63492907…` | ✓ |
| urdf/meshes/fl_hipy.STL | deep_robotics_model/M20_Piper/urdf/meshes/fl_hipy.STL | `c895052a02cc…` | ✓ |
| urdf/meshes/fl_knee.STL | deep_robotics_model/M20_Piper/urdf/meshes/fl_knee.STL | `c2ac2f2c9664…` | ✓ |
| urdf/meshes/fl_wheel.STL | deep_robotics_model/M20_Piper/urdf/meshes/fl_wheel.STL | `bcfca68aeeb8…` | ✓ |
| urdf/meshes/fr_hipx.STL | deep_robotics_model/M20_Piper/urdf/meshes/fr_hipx.STL | `350a5bca1df6…` | ✓ |
| urdf/meshes/fr_hipy.STL | deep_robotics_model/M20_Piper/urdf/meshes/fr_hipy.STL | `6a776a1637c7…` | ✓ |
| urdf/meshes/fr_knee.STL | deep_robotics_model/M20_Piper/urdf/meshes/fr_knee.STL | `e158a0ca5a5e…` | ✓ |
| urdf/meshes/fr_wheel.STL | deep_robotics_model/M20_Piper/urdf/meshes/fr_wheel.STL | `2773ffcac685…` | ✓ |
| urdf/meshes/gripper_base.STL | deep_robotics_model/M20_Piper/urdf/meshes/gripper_base.STL | `2895bfa6f1ee…` | ✓ |
| urdf/meshes/hl_hipx.STL | deep_robotics_model/M20_Piper/urdf/meshes/hl_hipx.STL | `3c20e792611b…` | ✓ |
| urdf/meshes/hl_hipy.STL | deep_robotics_model/M20_Piper/urdf/meshes/hl_hipy.STL | `d2c9efec9bfc…` | ✓ |
| urdf/meshes/hl_knee.STL | deep_robotics_model/M20_Piper/urdf/meshes/hl_knee.STL | `f6897fb23e4f…` | ✓ |
| urdf/meshes/hl_wheel.STL | deep_robotics_model/M20_Piper/urdf/meshes/hl_wheel.STL | `d61d98f986e9…` | ✓ |
| urdf/meshes/hr_hipx.STL | deep_robotics_model/M20_Piper/urdf/meshes/hr_hipx.STL | `b49f8992cc84…` | ✓ |
| urdf/meshes/hr_hipy.STL | deep_robotics_model/M20_Piper/urdf/meshes/hr_hipy.STL | `70332110c7bc…` | ✓ |
| urdf/meshes/hr_knee.STL | deep_robotics_model/M20_Piper/urdf/meshes/hr_knee.STL | `2fcf688c3059…` | ✓ |
| urdf/meshes/hr_wheel.STL | deep_robotics_model/M20_Piper/urdf/meshes/hr_wheel.STL | `88b2fca83119…` | ✓ |
| urdf/meshes/link1.STL | deep_robotics_model/M20_Piper/urdf/meshes/link1.STL | `9ee6e1d67c02…` | ✓ |
| urdf/meshes/link2.STL | deep_robotics_model/M20_Piper/urdf/meshes/link2.STL | `0d37675b699b…` | ✓ |
| urdf/meshes/link3.STL | deep_robotics_model/M20_Piper/urdf/meshes/link3.STL | `e8ae51f17c0c…` | ✓ |
| urdf/meshes/link4.STL | deep_robotics_model/M20_Piper/urdf/meshes/link4.STL | `efa330229762…` | ✓ |
| urdf/meshes/link5.STL | deep_robotics_model/M20_Piper/urdf/meshes/link5.STL | `a1c69d1c7f6f…` | ✓ |
| urdf/meshes/link6.STL | deep_robotics_model/M20_Piper/urdf/meshes/link6.STL | `88374973bc3b…` | ✓ |
| urdf/meshes/link7.STL | deep_robotics_model/M20_Piper/urdf/meshes/link7.STL | `475a7d8db056…` | ✓ |
| urdf/meshes/link8.STL | deep_robotics_model/M20_Piper/urdf/meshes/link8.STL | `3f88d534a85e…` | ✓ |

## 排除清单（config s4.excluded）



**结论**：存在 FAIL，停手处置（FAIL 1 / WARN 1）
