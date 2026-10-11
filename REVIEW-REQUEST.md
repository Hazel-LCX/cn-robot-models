# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-11 审毕：**R9 = 协议⑤完成，M0 含开源发布全流程闭环**（回执计数 12→21 已更正并 push，本地=远端=d0c2c3a）。

【送审类型】**协议②（M1 选型定案 + S0 license 核对结论确认）**——M1 首个送审件，触发即停手，S1 未动。

【背景：在做什么】M0 闭环后用户令"继续"，启动 **M1（第二个模型）**。选型侦察已做：五家国产厂商官方 org 全景扫描（GitHub API 实测，原始数据在 `workspace/m1_recon/`，gitignore 不入库）。S0 产出已备齐：`models/unitree_g1/SOURCE.md`（状态行=待审）+ license 原文快照 ×2 + evidence 原件 ×7（org/两仓库/license 端点/head commits）。

**候选全景（API 实测，非转述）**：

| 厂商/org | 双格式状态 | license | 备注 |
|---|---|---|---|
| 宇树 unitreerobotics | **URDF∩MJCF 交集 11 个模型**（g1/h1/h1_2/h2/r1/a2/as2/b2/b2w/go2w…） | **两仓库 BSD-3（M0 已核，本日复核一致）** | 形态覆盖最全，license 框架已验证 |
| 智元 AgibotTech | genie_sim 仿真平台（★1416），X1 模型文件未独立定位 | 待核 | 平台重、文件散，S1 成本高 |
| 加速进化 BoosterRobotics | booster_assets（"robot descriptions"）+ booster_gym | 待核 | 描述库形态好，license 未核 |
| 众擎 engineai-robotics | engineai_robotics_description 独立库 | 待核 | 可作 M2+ 候选 |
| 云深处 DeepRoboticsLab | deep_robotics_model（URDF）+ rl_deploy | 待核 | 同上 |
| 逐际 limxdynamics | 模型文件未定位 | 待核 | 暂出局 |

**G1 关键实测事实**（送审依据，全 API 实测）：`g1_description/` URDF/xml 变体 **30 个**（23dof/29dof/with_hand/rev_1_0/mode_10–18）；MJCF 侧官方两版 `g1_23dof.xml` / `g1_29dof.xml`；网格 **stl**（URDF 侧池 173 件/110.4 MB 全变体共享、MJCF 侧 60 件/31.8 MB）；**上游零漂移**（head = M0 所钉锚点 `5994d4fa` / `1eb6642e`，程序化三源比对 OK）。

【决策点：需要拍板的具体选项】

1. **M1 选型定案 = 宇树 G1（人形），配对 = `g1_23dof.urdf` ↔ `g1_23dof.xml`**。29dof 系（含腰部/手）留 M2+ 作"同机器人多配置"质检深水区素材；其余 28 变体不入库，S1 报告记录"存在未收"。
2. **S0 license 三条结论确认**（BSD-3 双仓库：再分发=是/修改=是/保留声明=是，网格二进制随仓库 license）→ S0 门关闭，放行 S1。
3. **S5 增量处置**：网格从 dae 变 **stl**，M0 自写预览加载器只覆盖 dae+TGA——S1–S4、S6 预期纯配置零改码，**S5 需新增 STL 支路**（vendor 官方 STLLoader，同 ColladaLoader 待遇：随附原版 MIT LICENSE）。请裁定：这属"配置边界内的管道增强"（工作台直进，PIPELINE 不升版）还是需升版送审。

【我的倾向+理由】三项均按上表定案。选 G1 的四条理由：①**形态跨越**（四足→人形）是管道普适性的最硬证据——S2/S3/S5/S6 全链面对 23 DOF 人形拓扑（腿+臂混合运动学），质检含金量远超再加一只四足；②**S0 门最干净**——同 org license 框架 M0 已核并本日复核一致，锚点零漂移程序化验证过，M1 把工程风险集中在管道验证而非 license 侦察；③双格式官方齐且 23dof 配对名完全对齐，交叉对账基线干净；④作品叙事最强——Go2（四足旗舰）+ G1（人形顶流）覆盖国产机器人两个最受关注的形态。异厂候选的增量价值主要在 license 多样性，但其 license 均未核、模型文件散，把不确定性前置违背"宁慢勿脏"；建议 **M2 走异厂**（届时 M1 已证管道，M2 证 license 流程泛化），两步合起来比一步到位更稳。

【相关文件路径】
- `models/unitree_g1/SOURCE.md`（S0 产物，状态行=待审核台确认）
- `models/unitree_g1/LICENSE-upstream-unitree_ros.txt`、`LICENSE-upstream-unitree_mujoco.txt`（1558/1559 B 原文快照）
- `models/unitree_g1/evidence/` ×7（org / 两仓库 / license 端点 ×2 / head ×2，均 2026-10-11 API 原件）
- `workspace/m1_recon/`（侦察原始 JSON + 锚点裁决脚本 check_anchors.py，不入库可本地复查）
- M0 同 org 证据原件：`models/unitree_go2/evidence/`（官网链接片段 + org API，本日引用复核）
