# REVIEW-REQUEST — 送审材料

> 审核台审毕请在本文件顶部标注"已审 + 日期"，结论追加进 REVIEW.md。本文件由工作台写入，审毕留痕（历次送审全文可在 git 历史回溯）。
> 上一次送审（代码首审 + 协议② license 结论批量件）已于 2026-10-11 审毕：**R3 通过**（代码首审过立五件套基线 / S0 门关闭 / 修正 1–8 核验 8/8 / 放行 S2），详见 REVIEW.md R3。

【送审类型】**物理质检专项审**（R1 后续送审点 3）· 按 R3 约定合并 pipeline/ 全脚本代码细审

【背景：在做什么】S0 门关闭 → S1 拉取（62 文件锚点锁定）→ S2 全绿 → **S3 体检完成：PASS 8 / WARN 4 / FAIL 0，零修复纯体检**（M0 定位：体检本身就是产出）。核心成果是质量分歧 forensics 闭环：URDF 总质量 16.087kg vs MJCF 15.206kg，差 0.881kg 逐项解释——rotors 12×0.089kg（URDF 独立建 rotor link，**约定差异**）− calf 4×0.0874kg（**真值分歧**）+ foot 4×0.04kg（MJCF 零质量纯 site 架，**约定差异**）+ head 0.002kg。hip/thigh/base 逐项完全一致；**12 对同名关节轴逐分量差 0.00e+00**（两模型运动学同源实锤）。修正 1（逐轴垂距法）实战首战：17 link × 3 轴全部落 [0.005, 0.5]——旧全长法会误报 4 条 calf 长轴，审核台预判命中。

【决策点：需要拍板的具体选项】
1. **体检矩阵与 WARN 处置记录**是否认可——WARN①：URDF 11 个 fixed 座零质量/无 inertial（imu/radar 显式 0kg + calflower×8/front_camera 无 inertial），规则精化为"挂在活动关节上的零质量才 FAIL"，全为 fixed 座降 WARN；WARN②：URDF 15 个 link 无 collision（12 rotor + imu/radar/camera，rotor 无碰撞合理），碰撞几何全基元（box 5 / cylinder 17 / sphere 5，无网格）；WARN③：MJCF 4 个 foot body 零 geom（纯 site 架）；WARN④：calf 真值分歧（见决策点 2）。
2. **calf 真值分歧处置**：0.154（URDF）vs 0.2414（MJCF），差 -87.4g×4。建议 **M0 不修 + 模型页如实披露**——理由：无官方分件标称，无法判定谁对；MJCF 总量 +1.4% 更贴官方是间接证据而非直接证据；社区有"unitree_ros URDF 参数沿袭自 Go1"的传闻但无官方文书支撑。修复需协议③（改动值+依据），现在改=编造依据。
3. **官方标称口径存证现状**：unitree.com/go2 为 JS 渲染，静态页无重量数字（片段已存 evidence/official-go2-spec-page.html.txt）；15kg 取官方公开规格表，报告口径栏注明"是否含电池未证实、双方模型均无电池 link，总量对比仅作 sanity"。是否接受，或要求 S7 收尾前用浏览器补一张规格页截图入 evidence/（A4 框架认可截图为补充证据形式）？
4. **pipeline/ 全脚本代码细审**（R3 约定合并至本次）：s1_fetch.py（R3 曾裁定"实跑背书可不逐行审"，本次按约定合并细审）、s2_validate.py（含 INFO 态→四态收敛的声明）、s3_physics.py（新增；自查修正两处：joints 缺 child 键、foot 从"真值分歧"重归类为"约定差异"后重跑）、env_check.py。AGENT-LAB.md 已建档（L1：enumerate 切片 TypeError + ugrep 复杂正则两次踩坑，均自救未升级）。
5. 若 1–4 过：**放行 S4 双格式入库**（网格 SHA256 分/合决策 + provenance 落档 + 仓库总体积记录）。

【我的倾向+理由】倾向 1 认可、2 不修+披露（编造依据比留下已解释的分歧更伤质检公信力——这正是"分歧≠错误"规则的意义）、3 接受现状且我承诺 S7 收尾前补截图、4 欢迎细审（脚本全部可重跑验证）、5 放行。理由：体检零 FAIL；全部 WARN 有处置记录且分类经自查修正；forensics 把"两个模型为什么不一样"回答到了每一个克。

【相关文件路径】
- models/unitree_go2/reports/S3-physics.md + S3-physics.json（体检报告 + 机器可读版，含 C1 双清点表）
- models/unitree_go2/evidence/official-go2-spec-page.html.txt（标称口径存证现状）
- pipeline/s3_physics.py（新增）、pipeline/s2_validate.py、pipeline/s1_fetch.py、pipeline/env_check.py（细审对象）
- AGENT-LAB.md（L1）、PIPELINE.md（v0.5）、DEVLOG.md（会话 6）、本文件
