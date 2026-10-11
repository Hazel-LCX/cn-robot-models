# SOURCE — agibot_x2 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②送审中，2026-10-11）——S0 license 门未关闭，S1 未启动。**
> 核对：写码工作台 · 2026-10-11 · 取证方式 = GitHub API + 官方域四站实测 + SPDX 官方名录程序化核验；M3 选型背景与三路线对比见 REVIEW-REQUEST.md（本次送审件）。**S1 起快照改名对齐管道惯例 `LICENSE-upstream-<name>.txt`（s1 A2 复核路径），字节不变。**

## 1. 数据源（单仓双格式 + 双版本目录）

| 项 | AgibotTech/agibot_x2_urdf（智元灵犀 X2 系列） |
|---|---|
| 仓库 | https://github.com/AgibotTech/agibot_x2_urdf |
| 拉取锚点（2026-10-11 实测 head） | `main` @ `575cc6b988f976c23550e0db85aa1e5475d3652d`（2026-09-21） |
| 目标子目录 | `X2_URDF-v1.4.0/`（**当前最新发布版**；仓内 v1.3.0 为旧版整机一套，双版本目录并存为本库首个多版本仓形态） |
| 配对选定（待审） | `X2-Ultra.urdf` + `X2-Ultra.xml`（旗舰机型新版；URDF 72 mesh 引用实测） |
| 网格 | `meshes/` STL（v1.4 目录内，件数与两侧共享关系 S1 实测） |
| 引用协议 | URDF = 显式 `./meshes/` 前缀（Lite3 同款已验风格，实测 `./meshes/pelvis.stl` 等 72 引）；MJCF = `meshdir="meshes/"` 相对引用（S2 resolve_ref 已覆盖） |
| 不入库（记录口径，M1 先例） | `X2_URDF-v1.3.0/` 整套（旧版）、`X2-EDU.urdf/.xml`（教育版配对）、`X2-Ultra_omnihand/omnipicker*.urdf`（手部变体，无 MJCF 配对）、`*_simple_collision.urdf`（简化碰撞变体）、`scene.xml`（场景件）、`x2_fist*`（虚手件） |

**机型背景（待审）**：X2 = 智元灵犀 X2 系列双足人形（Ultra 旗舰 / EDU 教育版，官方 README 识别指引按颈部铭牌区分）。推荐锚 **X2-Ultra（v1.4.0 新版）**：官方 README 标注"upgraded motors, reinforced structure"为当前在售版；EDU 配对完整亦在 v1.4 内，如审核台倾向教育版可平替（两者管道成本相同）。

## 2. 官方性验证（A4 证据链——强度分层如实呈现）

- **路径②成立（多件互证）**：org 官方字段自指官方域——`users/AgibotTech` API 原件 blog=`https://www.agibot.com/`、location=China（`evidence/github-users-AgibotTech.json`）；repo 原件 `fork:false, archived:false`（`evidence/github-repo-agibot_x2_urdf.json`）；org 23 仓与官方产品/研发线互为生态佐证（genie_sim 官方仿真平台、sonic_for_a3、agibot_x1_infer/train/hardware 等）；README_CN 官方自我声明"智元机器人致力于通用人形机器人研发"+官网链接（`evidence/official-readme-declaration.txt`）；官网 agibot.com.cn 首页页脚直链官方生态 GitHub 仓（AimRT/Link-U-OS/OpenDriveLab/Agibot-World——`OpenDriveLab/Agibot-World` 仓路径即品牌互指），原件 `workspace/m3_recon/agibot-homepage.html`（侦察件不入库）。
- **路径①阴性（如实记录）**：官网→AgibotTech org 直链未命中——四站探测（agibot.com.cn 首页 / open.agibot.com 开源门户 / openloong.org.cn 社区站 / agibot.com 国际站）直链均指向生态仓或无 GitHub 链接。**强度低于 M2 双路径全中、与 M1 相当**；补强方向留 S0 收尾：官网新闻/公告页深挖（M2 是在 support 子页挖到直链的）。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| AgibotTech/agibot_x2_urdf（整仓单 license，子目录无独立 LICENSE——API license 端点 + 树扫描双证） | **MulanPSL-2.0**（木兰宽松许可证，第 2 版） | 智元机器人（AgibotTech org 官方主体；许可模板无逐文件版权行，S7 LICENSES.md 措辞届时一并送审确认） | `LICENSE-upstream-agibot_x2_urdf.txt`（6752 B，blob `adf055335332c2223e5aadc740682b3ba6e4ebab`，hash-object 比对 MATCH） |

**定性论证（本条即协议②送审的 license 定性考题）**：

1. **GitHub 端点显示 NOASSERTION ≠ license 不明**——是 GitHub 检测器对中文头部许可证的识别盲区。本库红线"license 不明=不收录"的正确执行 = 拿原文定性，而非跟随第三方检测器的空白。
2. **SPDX 官方名录程序化核验**（`evidence/spdx-MulanPSL-2.0.json`，2026-10-11 实抓）：`MulanPSL-2.0 = Mulan Permissive Software License, Version 2`，`isOsiApproved: True`（OSI 认证通过）、未弃用；全名录 740 项中 `MulanPSL-1.0` 无 OSI 标记、2.0 有——**v2 是国际认证的宽松型开源许可证**。
3. **义务清单**（原文 `LICENSE-upstream-agibot_x2_urdf.txt`）：①宽松授予复制/使用/修改/分发权（§1/§2 含专利许可）；②**分发义务：向接收者提供许可证副本 + 保留版权/商标/专利及免责声明（§4）**；③无商标许可（§3）——本库商标声明体系（B3）覆盖；④中英双版本同效、歧义以中文为准（§6）。未修改分发官方件 + 保留 license 副本 = 义务满足。
4. **与本库兼容性**：本库 MIT 主体 + 第三方声明层（LICENSES.md 逐仓行）结构不变，新增 MulanPSL-2.0 行即可；快照随件分发 = §4 义务的直接履行。
5. **关联仓排除**（如实记录）：`genie_sim_robot_model`（Apache-2.0）仅 xacro 源无成品 URDF（436 blobs / 0 urdf，树扫描实测）——收源生成为派生，撞"只收官方发布件"红线精神，否决；`genie_sim` 平台仓 license 同为 NOASSERTION 且为仿真平台非模型库，否决。智元路线可行形态 = **agibot_x2_urdf 本仓**。

## 4. 快照与锚点

- license 快照：blob `adf055335332c2223e5aadc740682b3ba6e4ebab`（license 端点 `_links.git` 直取）→ 本地 `git hash-object --no-filters` 比对 MATCH（L8 立规执行）。
- pin：`575cc6b988f976c23550e0db85aa1e5475d3652d`（2026-09-21，`evidence/github-head-agibot_x2_urdf.json`）；树快照 `workspace/m3_recon/agibot_x2_urdf_tree.json`（侦察件，不入库）。
- 上游漂移监控：S1 时对账 head；本仓 2026-09-21 后无新 push（users/AgibotTech repos pushed 字段实测）。
