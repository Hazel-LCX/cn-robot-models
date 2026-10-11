# SOURCE — deeprobotics_lite3 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-11）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-11 · 取证方式 = GitHub API + 两官网域全文抓取实测；M2 选型背景与四家对比见 REVIEW-REQUEST.md（本次送审件）。

## 1. 数据源（单仓双格式——与 unitree 分仓模式不同的新形态）

| 项 | DeepRoboticsLab/deep_robotics_model（云深处） |
|---|---|
| 仓库 | https://github.com/DeepRoboticsLab/deep_robotics_model |
| 拉取锚点（2026-10-11 实测 head） | 分支 `main` @ `75824b516ecc8fa3f8f7ce5d6577e1e86d6b614f`（2026-09-28） |
| 目标子目录 | `Lite3/`（**单仓含 urdf/ + mjcf/ 双格式**——unitree 是 ros/mujoco 分仓，本仓同仓双格式为 M2 新形态，S1/S4 的双源逻辑按同仓两子目录适配） |
| 配对选定（待审） | `Lite3/urdf/Lite3.urdf` + `Lite3/mjcf/Lite3.xml` |
| 网格 | `urdf/meshes/` 4 件 STL + `mjcf/meshes/` 4 件同名 STL（两侧独立目录非共享池；两侧同哈希与否 S1 实测——G1 先例 28/29） |
| 引用协议 | 待 S1 实测（package:// 或 relative，config ref_style 留待实证） |
| 不入库 | `Lite3/usd/`（USD 格式，超出本库 URDF/MJCF 双格式范围，excluded 逐件记录） |

**机型选择（待审）**：本仓含 DR02/Lite3/M20/M20S/M20_Piper 多机型（URDF×9/MJCF×8）。推荐 **Lite3**（四足）——M1 已验人形拓扑（G1），M2 考题是**异厂 license/结构泛化**，选同形态（对照 M0 Go2 四足）使"厂商"成为唯一新变量；机型多收留 M3+。

## 2. 官方性验证（A4 证据链——强度分层如实呈现）

**双路径全中（R14 复核升级，按 M0 同强度关闭）**：

- **路径①命中（R14 行动项②更正）**：官网**支持页** `https://www.deeprobotics.cn/robot/index/support` 含 **"DeepRoboticsLab(点击跳转GitHub)" 直链 → github.com/DeepRoboticsLab/**（原件 `evidence/deeprobotics-support-page.html.txt`，2026-10-11 实抓；审核台 R14 一手复核发现——工作台首轮仅抓首页属欠采样，`deeprobotics-homepage-link.html.txt` 已留痕更正不删原文）；
- **路径②成立**：org API 原件（`evidence/github-org-DeepRoboticsLab.json`）多字段品牌互指——org name `DEEPRoboticsLab`、blog `https://www.deeprobotics.us/`（官网域）、twitter `DeepRobotics_CN`、email `info@deeprobotics.us`、location China；repo API 原件 `fork: false, archived: false`；org 下 28 仓（Lite3_rl_deploy/Lite3_MotionSDK/deep-robotics-sdk2 等）与官网产品线（Lite3/M20/DR02）互为生态佐证。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| deep_robotics_model | **BSD-3-Clause**（SPDX 端点复核一致） | **Copyright (c) 2024, DeepRoboticsLab**（快照原文逐字引用，N1；公司主体关联见 §2 官方性佐证） | `LICENSE-upstream-deep_robotics_model.txt`（1502 B，contents base64 = blob 正本） |

**三条结论**（BSD-3 逐条对应，与 unitree 同判）：

1. **允许再分发：是**（第 1 条）；
2. **允许修改：是**（第 1、2 条：修改版须随附声明性 notice）；
3. **须保留版权声明：是**（第 2 条 + 第 3 条不得背书条款 → S7 商标声明义务："Deep Robotics / Lite3"为云深处科技商标，本项目非官方、无关联、无背书）。

**网格等二进制跟随仓库同一 license 的假设**：与 M0/M1 记录方式相同——仓库根级单 LICENSE.txt 覆盖全仓（Lite3/ 子目录无独立 license 文件，见 §4）；STL 二进制按 BSD-3 再分发。

## 4. 子目录声明检查（A2）

2026-10-11 git trees API 实测 `Lite3/` 全量 21 项（mjcf/urdf/usd 三子目录）：**无 LICENSE/COPYING 文件**。repo 根级仅 `LICENSE.txt` 一份。`Lite3/` 内无 README（usd/configuration 为 USD 组件），无待复查正文项。

## 5. 对本库的义务（入库时落 LICENSES.md）

- BSD-3 单仓库：模型页 README 保留版权与许可声明；根级 `LICENSES.md` 增 deeprobotics_lite3 一行（S4 入库随对账更新，S7 定稿）；
- 商标声明沿用 B3；本库 MIT 不覆盖上游文件（双层结构不变）。
