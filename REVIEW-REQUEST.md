# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。历次送审全文可在 git 历史回溯。
> 上一次送审已于 2026-10-24 审毕：**R39 = 协议⑤执行回执终查通过——M9 含发布全流程闭环，四厂商十模型全量在线，管道拓扑能力封顶，项目回维护态**（回执数字四路活证零出入）。

【送审类型】**协议②（M10 选型定案 + S0 license 门确认）**——触发即停手，S1 未动。（续航令下第六个自动推进里程碑：M9 收官后按 R39 候选池首选 X30 方向直接启动。）

【背景：在做什么】启动 **M11 系第 11 个模型 M10（第十一个模型）**。定向侦察（`workspace/m10_recon/`，gitignore 不入库；解析器口径——R29/R34 规程连续第三轮执行）：X30 主配对结构细节 + **scale 逐处定位** + fresh pin。

**X30 侦察事实（全程序化，head 与 M5/M6/M9 锚 `530e01a5` 零漂移）**：

- **配对结构（解析器口径）**：`X30.urdf` **21 link / 12 revolute + 8 fixed**、13 引 `./meshes/` 前缀 → **4 唯一网格**（本库最小资产池：torso/hip/thigh 等基础件复用）、scale **5 处** ↔ `X30.xml`（8 引→4 唯一，meshdir=`./meshes/`，**MJCF scale 4 处**）；
- **scale 逐处定位（本件核心侦察资产——L12 家族实战线）**：URDF 5 处全为**镜像技巧**（共用网格翻转，Lite3 R19 案例同族）：FR_HIP/FR_THIGH（`1 -1 1`）、HL_HIP（`-1 1 1`）、HR_HIP（`-1 -1 1`）、HR_THIGH（`1 -1 1`）——四腿 hip/thigh 两两共用 hip.STL/thigh.STL 翻转；**MJCF 侧另有 4 处 scale**——**跨格式 scale 对账首例素材**（T1 无 scale/DR02 零 scale/M20 零 scale 后首个两侧均有 scale 的模型，S1 逐处对账）；
- **官网基准（M9 档案复核）**：X30 产品页（detail/6.html）整机重量（含电池）**约 56 kg**、持续负载 20 kg——**本库最大质量四足**（vs Go2 8.2/Lite3 12 档），S3 质量基准可得；
- 官方性验证：A4 沿用同仓四轮双路径先例（M2/M5/M6/M9 第五机型）；license 同仓第五机型零漂移断言（`cdc6c065` 与 M2/M5/M6/M9 快照逐字节同物）。

**S0 已按推荐源落档**（`models/deeprobotics_x30/`，状态=待审）：SOURCE.md + license 快照（1,502 B hash-object MATCH + 同物断言五过）+ evidence ×4（repo/license 端点/HEAD/官方 README + **X30 产品页二进制原件 141,318 B**——R29 取证范式，**本次脱敏 1 处 token**=范式实战执行）。

【决策点】

1. **M10 选型定案 = 云深处 X30（`DeepRoboticsLab/deep_robotics_model`，`X30/`）**——**scale 实战线**（URDF 5 处镜像+MJCF 4 处跨格式对账=管道 scale 应用能力首次成规模实战检验）+ **四足大机型档**（56 kg，尺度带新数据点）+ 薄池极简闭包（4 网格）；确认或改选 DR02 Standard/M20S/S10（同构填充档案）等；
2. **锚点 = `X30.urdf` ↔ `X30.xml`** + 不入库清单（usd 5 件先例处置/其余机型目录/仓级件）；确认或改锚；
3. **license 门确认 = 同仓单 license BSD-3-Clause 零漂移**（快照与 M2/M5/M6/M9 逐字节同物 `cdc6c065`，无新定性；LICENSES.md 复指口径同前行式样 S7 落笔）；确认或推翻；
4. **A4 继承确认**：M2/M5/M6/M9 四轮双路径先例第五机型沿用，无新增阴性项；S3 前置侦察基本完成（官网 56 kg 基准在档可提取——非 T1/Piper 式缺失）；确认或推翻。

【倾向 + 理由】**推荐四项全按上述定案**。理由：①X30 是候选池里管道实战价值最高的一枚——**scale 镜像技巧 5 处（URDF）+4 处（MJCF）是 R18 修复 preview.js scale 应用后的第一次成规模实战检验**（Lite3 案例 6 处含 5 镜像同族），且跨格式 scale 对账为九模型以来首例素材；②56 kg 补四足质量档（8.2/12/20→56），S3 基准可得非缺失型；③薄池 4 网格极简闭包——S1–S4 管道面最省；④风险如实列示：MJCF scale 4 处的逐处对账（与 URDF 5 处的跨格式一致性）S1 实测定案、极简池对 collision/惯量检查覆盖面（21 link 结构仍完整）——均 S1–S3 定案不做预断。本件不枚举自身哈希（清单至 R39 收官 `a0254e3` + 本件随批）。

【文件路径】送审核心：`models/deeprobotics_x30/SOURCE.md`（状态=待审）+ `LICENSE-upstream-deep_robotics_model.txt`（1,502 B，与 M2/M5/M6/M9 快照同物）+ `evidence/` ×4（含 X30 产品页二进制原件 141,318 B，脱敏 1 处 token）。侦察原件（不入库）：`workspace/m10_recon/`（recon 脚本 + x30_facts.json + 树 v4 + X30 产品页档）。管道 diff=0（本会话零改码）。
