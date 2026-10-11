# SOURCE — unitree_g1 来源与 License 核对记录（S0 产物）

> **状态：已确认（R10 · 2026-10-11）——S0 license 门关闭，S1 拉取完成（正本检出 / A2 MATCH / J1 计数重放通过），S2 未启动。**
> 核对：写码工作台 · 2026-10-11 · 取证方式 = GitHub API 实测（raw.githubusercontent 不通，未使用）；M1 选型背景与候选对比见 git 历史的 REVIEW-REQUEST.md（协议②送审件，R10 批准）。

## 1. 数据源（两仓库，均官方 org，与 M0 同源）

| 项 | unitree_ros（URDF 源） | unitree_mujoco（MJCF 源） |
|---|---|---|
| 仓库 | https://github.com/unitreerobotics/unitree_ros | https://github.com/unitreerobotics/unitree_mujoco |
| 拉取锚点（2026-10-11 实测 head） | 分支 `master` @ `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 分支 `main` @ `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` |
| **锚点漂移检查** | **= M0 go2 所钉锚点，零漂移** | **= M0 go2 所钉锚点，零漂移** |
| 目标子目录 | `robots/g1_description/` | `unitree_robots/g1/` |
| 配对选定（待审） | `g1_23dof.urdf`（28.8 KB） | `g1_23dof.xml`（31.7 KB）+ `scene_23dof.xml` |
| 网格格式（API 实测 2026-10-11） | `meshes/` = **stl ×173 / 110.4 MB**（全变体共享池，非逐变体独立） | `meshes/` = **stl ×60 / 31.8 MB** |

**M1 新事实（与 Go2 的差异，选型即知；S1 后补实测）**：
1. **网格格式从 dae（Go2-URDF 侧）变为 stl**——S2/S4/S5 面对新格式；S5 预览加载器需**新增 STL 支路**（R10 已裁定：配置边界内管道增强，五条件直进）。
2. **URDF 网格引用协议差异（S1 实测新发现）**：g1_23dof.urdf 引用 **50/50 全为相对路径 `meshes/xxx.STL`**（Go2 走 `package://` 协议）——S2 校验与 S4 闭包按"引用协议"分支处理（config 拟加 `ref_style` 字段），S2/S4 实现时报备。
3. **URDF 变体 33 个模型文件（23 urdf + 10 xml）= 23 去重配置**（J1 口径，S1 raw 重放与 R10 逐位一致）。本库只收 g1_23dof 配对；其余 32 文件 S4 excluded 逐件记录。
4. `inspire_hand/` 子目录（灵巧手模型）不入 M1 范围。

**S1 拉取现态（2026-10-11）**：blobless+sparse+**autocrlf=false（L8 铁律）**直连一次成功；raw = ros 223 件/120.7 MB + mujoco 76 件/37.1 MB，manifest 299 件（K2 归正后重生成 = 150.5 MB；原报告 157.8 MB 为检出失真态字节；真身 gitignored，副本进 reports/S1-fetch.md）；**license 快照 A2 MATCH**（raw 检出件与 S0 blob-exact 快照逐字节一致——正本检出铁律生效实证）；MJCF 侧 23dof.xml 引用池 60 件中 **29 件**（其余 31 件为 29dof/手部网格）→ S4 闭包拷贝 29 件（整拷否决）。明细 reports/S1-fetch.md。

**拉取方法**：沿用 M0 路线——blobless 部分克隆 + sparse-checkout（锚点上表 SHA），API 逐文件兜底，代理 socks5h://127.0.0.1:12450 备用。STL 为二进制，API 兜底路径走 base64（1.37× 膨胀）优先级低于克隆。

## 2. 官方 org 验证（A4 证据链）

**同 org（unitreerobotics）复核，M0 原件仍在档**：`../unitree_go2/evidence/`（官网首页链接片段 + org API 原文，2026-10-11 抓取）。M1 本日独立复核（原件存本目录 `evidence/`，均 2026-10-11 API 实测）：

| 原件文件 | 内容 | 复核结果 |
|---|---|---|
| `evidence/github-org-unitreerobotics.json` | org API 原文 | description/blog/type 与 M0 逐字一致 |
| `evidence/github-repo-unitree_ros.json` | 仓库 API 原文 | `fork: false, archived: false, default_branch: master` |
| `evidence/github-repo-unitree_mujoco.json` | 仓库 API 原文 | `fork: false, archived: false, default_branch: main` |
| `evidence/github-license-unitree_*.json`（×2） | license 端点原文 | 两仓库 `spdx_id: BSD-3-Clause` |
| `evidence/github-head-unitree_*.json`（×2） | head commit 原文 | 锚点 = 上表 SHA，日期 2026-09-30 / 2026-09-07 |

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照（本日 API 抓取） |
|---|---|---|---|
| unitree_ros | **BSD-3-Clause** | HangZhou YuShu Technology CO.,LTD. ("Unitree Robotics")，© 2016–2022 | `LICENSE-upstream-unitree_ros.txt`（1558 B） |
| unitree_mujoco | **BSD-3-Clause** | 同上，© 2016–2024 | `LICENSE-upstream-unitree_mujoco.txt`（1559 B） |

**三条结论**（BSD-3 逐条对应，与 M0 同判）：

1. **允许再分发：是**（第 1 条）；
2. **允许修改：是**（第 1、2 条：修改版须随附声明性 notice）；
3. **须保留版权声明：是**（第 2 条 + 第 3 条不得背书条款 → S7 沿用 B3 商标声明义务）。

**网格等二进制跟随仓库同一 license 的假设**：与 M0 记录方式相同——两仓库根级 LICENSE 覆盖仓库内容，未发现网格目录独立授权声明（见 §4）；stl 二进制按 BSD-3 再分发，入库时保留源头声明文件。

## 4. 子目录声明检查（A2）

2026-10-11 GitHub contents API 实测两个目标子目录文件清单：

- `robots/g1_description/`：39 项，**无 LICENSE 文件**（有 README.md、motor_info.md、merge notebook 与变体 urdf/xml）；
- `unitree_robots/g1/`：10 项，**无 LICENSE 文件**（有 g1_joint_index_dds.md、scene xml、meshes/、images/）。

**S1 复核结论（2026-10-11，A2 待办闭环）**：`g1_description/README.md`、`g1_description/motor_info.md`、`unitree_robots/g1/g1_joint_index_dds.md` 三个上游文档正文**许可关键词全无**（license/BSD/Apache/MIT/copyright/版权 程序化扫描）——无需补快照许可声明，按上游文档件 excluded 归档（明细 reports/S1-fetch.md 人读段）。

## 5. 对本库的义务（入库时落 LICENSES.md）

- BSD-3 双仓库：模型页 README 保留版权与许可声明（S7 模板同 M0）；根级 `LICENSES.md` 增补 unitree_g1 一行（S4 入库时随对账重跑更新，S7 定稿）；
- 商标声明沿用 B3（"Unitree"、"Unitree Robotics"、"G1" 为宇树科技商标，本库为其开源模型文件之再分发与质检整理）；
- 网格再分发随仓库 BSD-3，本库 MIT 不覆盖上游文件（双层结构不变）。
