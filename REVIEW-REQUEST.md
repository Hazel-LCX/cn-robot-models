# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-11 审毕：**R13 = 协议⑤完成，M1 含开源更新全流程闭环**（收尾 push `03444af` 已上线，审计链补全至 R13）。

【送审类型】**协议②（M2 选型定案 + S0 license 核对结论确认）**——M2 首个送审件，触发即停手，S1 未动。

【背景：在做什么】M1 闭环后启动 **M2**。按 R13 裁定，M2 的真正考题 = **异厂 license/结构泛化**（blob-parity 门与三锚对账迎自动化首战）。四家异厂候选已深查（GitHub trees API + license 端点 + 两官网域抓取，原件在 `workspace/m2_recon/` 与 `models/deeprobotics_lite3/evidence/`）：

| 厂商/仓库 | 双格式 | license | 裁定 |
|---|---|---|---|
| **云深处 DeepRoboticsLab/deep_robotics_model** | **单仓 URDF×9 + MJCF×8**（DR02/Lite3/M20/M20S/M20_Piper 多机型）、STL×286 | **BSD-3-Clause**（端点+原文双证） | **推荐** |
| 加速进化 BoosterRobotics/booster_assets | URDF×10（K1/T1/T2 人形）、STL×440，**本仓无 MJCF**（跨仓 booster_gym 需再核） | BSD-3-Clause | 备选（双格式需跨仓配对，多一跳） |
| 众擎 engineai-robotics/engineai_robotics_description | URDF×5、STL/DAE 各 164 | **无 LICENSE 文件（端点 404）** | **出局**——license 不明不收录（红线） |
| 智元 AgibotTech/genie_sim | 平台仓（内嵌 URDF 为**宇树 G1** 非自家机型） | **NOASSERTION**（自定义 license 需人工定性） | **出局**——license 非标准 + 收平台副本无增量 |

**推荐定案候选：云深处 Lite3（四足）**，配对 `Lite3/urdf/Lite3.urdf` + `Lite3/mjcf/Lite3.xml`（各带 4 件同名 STL，两侧独立目录非共享池）。理由三条：①**单仓双格式是新形态**——unitree 是 ros/mujoco 分仓，本仓同仓双子目录，S1/S4 双源逻辑按"同仓两子目录"适配，正是结构泛化的考题本体；②**一次只引入一个新变量**——M1 已验人形拓扑（G1），M2 选同形态四足（对照 M0 Go2），使"厂商"成为唯一新变量，归因干净；③体量小而干净（Lite3 全目录 21 项，usd/ 超范围 excluded）。DR02/M20 等多机型留 M3+。

**S0 已产出**：`models/deeprobotics_lite3/SOURCE.md`（状态行=待审）+ license 原文快照（1502 B，contents base64 = blob 正本，sha256 `6bc5967b1cfb…`）+ evidence 6 件（org/repo/head API 原件 + 两官网域抓取件 + 首轮探测件）。

【决策点：需要拍板的具体选项】

1. **M2 选型定案 = 云深处 Lite3**（`deeprobotics_lite3`，单仓双格式配对，usd/ excluded）。
2. **S0 license 三条结论确认**（BSD-3-Clause：再分发=是/修改=是/保留声明=是，网格二进制随仓库 license）→ S0 门关闭放行 S1。
3. **A4 证据强度裁定**：**路径①未命中**（deeprobotics.cn/.us 两官网域全文均无 github 字样，原件在案）、**路径②成立**（org name/blog=deeprobotics.us/twitter/email 四字段品牌互指 + fork:false + org 下 28 仓与官网产品线生态互证）——比 M0 unitree 双路径全中弱一层。请裁定路径②单证是否足以关闭官方性结论，或需补强（如公众号/文档站/邮件确认等线下证据）。

【我的倾向+理由】三项均按上述定案。选 Lite3 的核心理由：M2 的含金量不在"又一个模型"，而在**管道对非 unitree 生态的一览无余的适配性检验**——同仓双格式、BSD-3 文本差异（1502 B vs unitree 1558/1559 B，版权行与措辞必然不同）、STL 网格（非 dae/obj）、无 xacro/、独立 meshes 目录——每一步都会遇到"config 里没有的字段怎么填"。A4 路径②单证如实分层呈现：org 四字段互指 + 28 仓生态佐证在开源机器人厂商里属常见形态（unitree 官网直链反而是少数派），倾向按"路径②成立"关门；若审核台认为需补强，建议补"云深处官方文档站/公众号对 GitHub 的指引"类线上证据再议。

【相关文件路径】
- `models/deeprobotics_lite3/SOURCE.md`（S0 产物，状态行=待审核台确认）
- `models/deeprobotics_lite3/LICENSE-upstream-deep_robotics_model.txt`（1502 B 原文快照）
- `models/deeprobotics_lite3/evidence/` ×6（org/repo/head API 原件 + 两官网域抓取件）
- 侦察原始数据：`workspace/m2_recon/`（m2_{booster,engineai,deeprobotics,agibot}_tree.json + m2_summary.json + 脚本，gitignored 可本地复查）
