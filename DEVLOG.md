# DEVLOG — 滚动日志

> 纪律：每次会话结束追加一条，新的在上。

## 2026-10-11（会话 2：会话 A · 环境就位）

- 仪式：读 REVIEW.md → **R2 通过，放行动手**（A1–A4/B1–B6/四问逐项核验 ✓；越界监察零条目；执行提示 C1–C3）。现场恢复 = v0.2 已送审待放行。
- 吸收 C1：S3 验收补"碰撞体清点表入报告"勾选项，PIPELINE.md 升 **v0.3**；C2（修复项批量送审）、C3（S0 结论天然触发协议②）记入流程，不改文档。
- 动手（会话 A）：git init（main）+ .gitignore + pipeline/requirements.txt + pipeline/env_check.py。
- 体检两轮：base（py3.14.6）→ mujoco cp314 wheel 可解析 → 定 **venv** 路线；.venv 装齐（mujoco 3.15.0 / yourdfpy 0.0.60 / trimesh 5.1.1 / numpy 2.5.3 / scipy 1.18.1 / lxml 6.1.3，阿里镜像）；venv 内复跑全绿（PASS 10 / WARN 1 / FAIL 0，WARN=raw 被墙有兜底）。**py3.14 无 wheel 的风险正式解除，py3.12 兜底方案作废。**
- 状态：env_check.py 待用户复述确认 → 确认后写 REVIEW-REQUEST.md 送**代码首审**（R1 ⑤，立风格基线）→ 会话 B（S0+S1）。git 尚无 commit（等用户发话）。

## 2026-10-11（会话 1：设计）

- 项目启动：M0 = 宇树 Go2 走通全管道。**本会话零代码**，仅环境侦察 + 产出 PIPELINE.md v0.1。
- 侦察结论：无 node（预览走纯静态）；base Anaconda = py3.14.6（mujoco wheel 存疑，env_check 第一查）；raw.githubusercontent 被墙但 api.github.com 通；jsDelivr 404 不预设可用。
- 官方源已证实：URDF = `unitree_ros/robots/go2_description`，MJCF = `unitree_mujoco/unitree_robots/go2`；两仓库均 BSD-3-Clause；两源网格格式不同（dae/stl vs obj），入库预期分目录。
- 状态：设计待用户确认 → 送审核台过审（REVIEW.md）→ 回来从会话 A（动手第0步）开始。
- 会话中段：用户补充**审核点协议**（5 类硬触发 + 固定动作 + 会话开始仪式），原文照抄进 PIPELINE.md §8；自此每次会话开始先读 REVIEW.md 新结论 + DEVLOG 最后一条恢复现场。
- 会话开始仪式首跑：读 REVIEW.md → **R1 有条件通过**（A1–A4 必修、B1–B6 吸收、四问答复、R1-附方向放行 + 三条导航风险）。
- 按待修清单升 v0.2：A1 S3 补碰撞体三件（只标记不自动补）；A2 license 快照同 commit + 子目录声明检查；A3 回归门改 S2+S3 双跑；A4 官方 org 证据链落字；B1 惯量数量级 sanity；B2 基准预热 ≥100 步 + ≥10⁴ 步；B3 商标声明；B4 MJCF 查看命令；B5 独立环境口径；B6 自写加载器边界；四问落档 §7（MIT / 不加 PyBullet / 网格默认分目录 / format_source 钩子）；完成度铁律 + 门面立位入 §0。
- **协议①触发**（管道设计改动）：REVIEW-REQUEST.md 已写，送 v0.2 轻复审，停手等放行。
