# S4 入库对账报告 — deeprobotics_m20（2026-10-24 16:47）

**物理文件口径（终审 F1 修正）**：入库物理文件 36 = raw 溯源件 36（URDF 引用 17 处 → 网格物理文件 17，引用行 ≠ 文件数） + 质检自产件 0[]；**总 23.9 MB（raw 溯源件 23,908,273 B + 质检自产件 0 B，G1 口径注明）**（不含 reports/evidence/文档）。字节级复制，raw 未动。

**对账即事实（R7-H1 规则）**：凡变更 `models/` 下任何文件（含质检自产件），必重跑本脚本刷新对账——本报告必须始终等于当前磁盘事实。

## 分类汇总

asset 17 · mesh 17 · mjcf 1 · urdf 1

## 检查矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `s4:traceability` | PASS | 36 个 raw 源入库件三锚全过（SHA256 命中 manifest 同路径行 + hash-object 命中上游 ls-tree@pin blob id） |
| `s4:mesh-split-decision` | PASS | URDF 侧 17 处引用 → 17 个物理网格 vs MJCF 侧 17 个，两侧同哈希（同源同内容，STL 同格式）——分目录落位以保持各自引用协议结构（不改官方一字节，保持官方 meshdir/相对引用结构，记录在案） |
| `s4:dae-dir-parity` | SKIP | 本模型 urdf 无 dae/ 与 meshes/ 双目录结构（G1 为 meshes/ 单池），R3-D3 判定不适用 |
| `s4:coverage` | PASS | raw 全量 45（除 .git/manifest）= 根级及中间层 4 + 目标子目录 41；子目录 41 全覆盖 = 入库唯一源 36 + 排除 5（其中 meshes/ 冗余 0）（未覆盖：无）——算式按源件口径平账（F1 教训） |
| `s4:recheck-mjcf` | PASS | 入库后 mjcf/M20.xml 编译通过：nbody=18 ngeom=45 nmesh=17（官方相对引用结构保持） |
| `s4:recheck-urdf` | PASS | 入库后 URDF yourdfpy 解析通过：21 links（relative（./ 前缀）——meshes/ 与 urdf 同目录（分目录形态）） |

## 逐文件对账（raw 溯源件 36）

| 入库位置 | 上游路径（raw 相对） | SHA256 | manifest 溯源 |
|---|---|---|---|
| mjcf/M20.xml | deep_robotics_model/M20/mjcf/M20.xml | `25a3a09677d9…` | ✓ |
| mjcf/meshes/base_link.STL | deep_robotics_model/M20/mjcf/meshes/base_link.STL | `a7984137d067…` | ✓ |
| mjcf/meshes/fl_hipx.STL | deep_robotics_model/M20/mjcf/meshes/fl_hipx.STL | `179c63492907…` | ✓ |
| mjcf/meshes/fl_hipy.STL | deep_robotics_model/M20/mjcf/meshes/fl_hipy.STL | `c895052a02cc…` | ✓ |
| mjcf/meshes/fl_knee.STL | deep_robotics_model/M20/mjcf/meshes/fl_knee.STL | `c2ac2f2c9664…` | ✓ |
| mjcf/meshes/fl_wheel.STL | deep_robotics_model/M20/mjcf/meshes/fl_wheel.STL | `bcfca68aeeb8…` | ✓ |
| mjcf/meshes/fr_hipx.STL | deep_robotics_model/M20/mjcf/meshes/fr_hipx.STL | `350a5bca1df6…` | ✓ |
| mjcf/meshes/fr_hipy.STL | deep_robotics_model/M20/mjcf/meshes/fr_hipy.STL | `6a776a1637c7…` | ✓ |
| mjcf/meshes/fr_knee.STL | deep_robotics_model/M20/mjcf/meshes/fr_knee.STL | `e158a0ca5a5e…` | ✓ |
| mjcf/meshes/fr_wheel.STL | deep_robotics_model/M20/mjcf/meshes/fr_wheel.STL | `2773ffcac685…` | ✓ |
| mjcf/meshes/hl_hipx.STL | deep_robotics_model/M20/mjcf/meshes/hl_hipx.STL | `3c20e792611b…` | ✓ |
| mjcf/meshes/hl_hipy.STL | deep_robotics_model/M20/mjcf/meshes/hl_hipy.STL | `d2c9efec9bfc…` | ✓ |
| mjcf/meshes/hl_knee.STL | deep_robotics_model/M20/mjcf/meshes/hl_knee.STL | `f6897fb23e4f…` | ✓ |
| mjcf/meshes/hl_wheel.STL | deep_robotics_model/M20/mjcf/meshes/hl_wheel.STL | `d61d98f986e9…` | ✓ |
| mjcf/meshes/hr_hipx.STL | deep_robotics_model/M20/mjcf/meshes/hr_hipx.STL | `b49f8992cc84…` | ✓ |
| mjcf/meshes/hr_hipy.STL | deep_robotics_model/M20/mjcf/meshes/hr_hipy.STL | `70332110c7bc…` | ✓ |
| mjcf/meshes/hr_knee.STL | deep_robotics_model/M20/mjcf/meshes/hr_knee.STL | `2fcf688c3059…` | ✓ |
| mjcf/meshes/hr_wheel.STL | deep_robotics_model/M20/mjcf/meshes/hr_wheel.STL | `88b2fca83119…` | ✓ |
| urdf/M20.urdf | deep_robotics_model/M20/urdf/M20.urdf | `1643c65b3992…` | ✓ |
| urdf/meshes/base_link.STL | deep_robotics_model/M20/urdf/meshes/base_link.STL | `a7984137d067…` | ✓ |
| urdf/meshes/fl_hipx.STL | deep_robotics_model/M20/urdf/meshes/fl_hipx.STL | `179c63492907…` | ✓ |
| urdf/meshes/fl_hipy.STL | deep_robotics_model/M20/urdf/meshes/fl_hipy.STL | `c895052a02cc…` | ✓ |
| urdf/meshes/fl_knee.STL | deep_robotics_model/M20/urdf/meshes/fl_knee.STL | `c2ac2f2c9664…` | ✓ |
| urdf/meshes/fl_wheel.STL | deep_robotics_model/M20/urdf/meshes/fl_wheel.STL | `bcfca68aeeb8…` | ✓ |
| urdf/meshes/fr_hipx.STL | deep_robotics_model/M20/urdf/meshes/fr_hipx.STL | `350a5bca1df6…` | ✓ |
| urdf/meshes/fr_hipy.STL | deep_robotics_model/M20/urdf/meshes/fr_hipy.STL | `6a776a1637c7…` | ✓ |
| urdf/meshes/fr_knee.STL | deep_robotics_model/M20/urdf/meshes/fr_knee.STL | `e158a0ca5a5e…` | ✓ |
| urdf/meshes/fr_wheel.STL | deep_robotics_model/M20/urdf/meshes/fr_wheel.STL | `2773ffcac685…` | ✓ |
| urdf/meshes/hl_hipx.STL | deep_robotics_model/M20/urdf/meshes/hl_hipx.STL | `3c20e792611b…` | ✓ |
| urdf/meshes/hl_hipy.STL | deep_robotics_model/M20/urdf/meshes/hl_hipy.STL | `d2c9efec9bfc…` | ✓ |
| urdf/meshes/hl_knee.STL | deep_robotics_model/M20/urdf/meshes/hl_knee.STL | `f6897fb23e4f…` | ✓ |
| urdf/meshes/hl_wheel.STL | deep_robotics_model/M20/urdf/meshes/hl_wheel.STL | `d61d98f986e9…` | ✓ |
| urdf/meshes/hr_hipx.STL | deep_robotics_model/M20/urdf/meshes/hr_hipx.STL | `b49f8992cc84…` | ✓ |
| urdf/meshes/hr_hipy.STL | deep_robotics_model/M20/urdf/meshes/hr_hipy.STL | `70332110c7bc…` | ✓ |
| urdf/meshes/hr_knee.STL | deep_robotics_model/M20/urdf/meshes/hr_knee.STL | `2fcf688c3059…` | ✓ |
| urdf/meshes/hr_wheel.STL | deep_robotics_model/M20/urdf/meshes/hr_wheel.STL | `88b2fca83119…` | ✓ |

## 排除清单（config s4.excluded）

- `deep_robotics_model/M20/usd/M20.usd` — USD 格式件——锚点=URDF/MJCF 双格式，USD 不入库只记录（Lite3 M2 usd/ excluded 先例；上游 README 自述 USD 传感器层无传感器定义等格式差异）
- `deep_robotics_model/M20/usd/configuration/M20_base.usd` — USD 配套件——同上
- `deep_robotics_model/M20/usd/configuration/M20_physics.usd` — USD 配套件——同上
- `deep_robotics_model/M20/usd/configuration/M20_robot.usd` — USD 配套件——同上
- `deep_robotics_model/M20/usd/configuration/M20_sensor.usd` — USD 配套件——同上

**结论**：入库完成，可进 S5/S6（FAIL 0 / WARN 0）
