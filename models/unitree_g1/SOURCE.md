# SOURCE — unitree_g1 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-11）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-11 · 取证方式 = GitHub API 实测（raw.githubusercontent 不通，未使用）；M1 选型背景与对比见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（两仓库，均官方 org，与 M0 同源）

| 项 | unitree_ros（URDF 源） | unitree_mujoco（MJCF 源） |
|---|---|---|
| 仓库 | https://github.com/unitreerobotics/unitree_ros | https://github.com/unitreerobotics/unitree_mujoco |
| 拉取锚点（2026-10-11 实测 head） | 分支 `master` @ `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 分支 `main` @ `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` |
| **锚点漂移检查** | **= M0 go2 所钉锚点，零漂移** | **= M0 go2 所钉锚点，零漂移** |
| 目标子目录 | `robots/g1_description/` | `unitree_robots/g1/` |
| 配对选定（待审） | `g1_23dof.urdf`（28.8 KB） | `g1_23dof.xml`（31.7 KB）+ `scene_23dof.xml` |
| 网格格式（API 实测 2026-10-11） | `meshes/` = **stl ×173 / 110.4 MB**（全变体共享池，非逐变体独立） | `meshes/` = **stl ×60 / 31.8 MB** |

**M1 新事实（与 Go2 的差异，选型即知）**：
1. **网格格式从 dae（Go2-URDF 侧）变为 stl**——M1 的 S2/S4/S5 都要面对新格式；S5 预览加载器需**新增 STL 支路**（M0 自写加载器只覆盖 dae+TGA）。这是"加配置不改码"承诺的已知边界：S1–S4、S6 预期纯配置，**S5 有增量**，已在送审件中如实披露，待审核台确认。
2. **URDF 变体 30 个**（23dof/29dof/with_hand/rev_1_0/mode_10–18…），29dof 系带腰部自由度。**本库只收 23dof 配对**（变体池不入库，S1 拉取按 `g1_23dof.urdf` 网格引用闭包定清单——23dof 只引用 173 个 stl 中的一部分，拉取面远小于 110 MB 池值）；其余变体在 S1 报告记录"存在未收"，不拉取。
3. `inspire_hand/` 子目录（灵巧手模型）不入 M1 范围。

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

**待 S1 复核项**：`g1_description/README.md`（6.8 KB）与 `g1_joint_index_dds.md` 快照落库后复查正文是否含许可/署名声明，有则补快照进 SOURCE.md（M0 对 go2 README 同法办理）。

## 5. 对本库的义务（入库时落 LICENSES.md）

- BSD-3 双仓库：模型页 README 保留版权与许可声明（S7 模板同 M0）；根级 `LICENSES.md` 增补 unitree_g1 一行（S4 入库时随对账重跑更新，S7 定稿）；
- 商标声明沿用 B3（"Unitree"、"Unitree Robotics"、"G1" 为宇树科技商标，本库为其开源模型文件之再分发与质检整理）；
- 网格再分发随仓库 BSD-3，本库 MIT 不覆盖上游文件（双层结构不变）。
