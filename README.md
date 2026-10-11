# 国产机器人仿真模型质检管道（cn-robot-models）

> **这不是模型收集站。** 这是一条可复现的开源仿真模型**质检管道**：
> license 核对 → 拉取 → 格式校验 → 物理体检 → 双格式入库 → 在线预览 → 基准 → 质检报告。
> 模型库是管道的副产品，**每一步的检查报告本身就是产品**。
> 已收录：宇树 Go2（M0 质检样板）· 宇树 G1（M1 · 人形）——官方双源 URDF/MJCF，BSD-3-Clause。

## 为什么是"质检管道"而不是"模型库"

网上流传的机器人 URDF/MJCF 大量来自转手改版，质量无人负责。本管道对每个收录模型做
**可复现、可溯源、留痕**的体检：来源锁定 commit、逐文件哈希对账、惯量正定与数量级双重
数学检查、URDF↔MJCF 交叉对账、官方规格口径核对——发现的每一个分歧都"清点 + 记录 +
披露"，绝不静默修复。**价值不在收了几个模型，而在"能证明这些模型可以被信任地加载"。**

- 如果体检发现分歧（M0 发现 calf 质量分歧，M1 发现更多——见各自模型页披露章节）：
  [Go2 · calf 质量/hip 限位](models/unitree_go2/README.md#-已知分歧披露质检的一部分) ·
  [G1 · 官方文件名与自由度不符（g1_23dof.xml 实为 29 关节，两格式动作空间不可互换）/ torso−1.28kg 网格证据链](models/unitree_g1/README.md#-已知分歧披露质检的一部分)。
- 如果体检全绿：价值落在"管道可复现 + 双格式对账 + 基准数字"——同样的成立。

## 管道

```
S0 license核对(门) → S1 拉取 → S2 格式校验 → S3 物理体检(门:回归) → S4 双格式入库 → S5 3D预览 → S6 基准 → S7 报告
```

- 每步一个脚本（`pipeline/s*.py`），全部 **config 驱动、模型无关**——M1+ 加模型 = 加配置不改代码。
- 每步产出报告（`models/<model>/reports/`），逐项 PASS/WARN/FAIL/SKIP，**fail 不静默**。
- 三份台账：`DEVLOG.md`（滚动日志）、`PIPELINE.md`（管道设计，v0.6a）、`AGENT-LAB.md`（失败与自救档案）。
- 审核协议：管道设计改动 / license 结论 / 物理参数修改等五类事项**停手送审**（PIPELINE.md §8）。

## 已收录模型

### M0 · 宇树 Go2（四足 · 2026-10-11）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | 双仓库 BSD-3-Clause（版权方=宇树本体），官方性双证据链，**已关闭** | [SOURCE.md](models/unitree_go2/SOURCE.md) |
| S1 拉取 | 62 文件锚点锁定（ros@`5994d4fa` + mujoco@`1eb6642e`），逐文件 SHA256 | SOURCE.md §4 |
| S2 格式校验 | **9 PASS / 0 FAIL**：URDF 42 link/41 joint、网格引用 100%、MJCF 真编译 | [S2-validation.md](models/unitree_go2/reports/S2-validation.md) |
| S3 物理体检 | **8 PASS / 4 WARN / 0 FAIL**，零修复纯体检；质量分歧 forensics 闭环到每一克 | [S3-physics.md](models/unitree_go2/reports/S3-physics.md) |
| S4 双格式入库 | 34 文件 / 55.4 MB（33 溯源件 + 1 质检截图 = 55,357,945 B，逐字节 = 上游 blob 正本，K1 行尾归正后口径），dae/meshes 冗余裁决 7/0 | [S4-package.md](models/unitree_go2/reports/S4-package.md) |
| S5 3D 预览 | 断网可开（外网请求 0），12 关节交互滑条（越限标红） | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 105,131 steps/s（9.5 µs/step）**，加载 56 ms，URDF 解析 4.7 ms | [S6-benchmark.md](models/unitree_go2/reports/S6-benchmark.md) |

### M1 · 宇树 G1（人形 · 2026-10-11）

| 步骤 | 结果 | 报告 |
|---|---|---|
| S0 license 门 | 同上游两仓库（与 Go2 同锚点零漂移），BSD-3-Clause，**已关闭（R10）** | [SOURCE.md](models/unitree_g1/SOURCE.md) |
| S1 拉取 | 299 文件锚点锁定（同 go2 锚点），**blob-parity 门**（检出件=上游 blob 逐字节，K2 后硬门） | SOURCE.md / S1-fetch.md |
| S2 格式校验 | **10 PASS / 0 FAIL**：URDF 33 link/32 joint、50 处引用全解析 + **大小写逐字节核验失配 0**、MJCF 真编译 | [S2-validation.md](models/unitree_g1/reports/S2-validation.md) |
| S3 物理体检 | **7 PASS / 5 WARN / 0 FAIL**，零修复纯体检；torso −1.28 kg 分歧逐克闭环 + head_link.STL 网格证据链 | [S3-physics.md](models/unitree_g1/reports/S3-physics.md) |
| S4 双格式入库 | 62 文件 / 40.5 MB **三锚全过**（models↔manifest↔上游 blob id），excluded 228 件逐件带 why | [S4-package.md](models/unitree_g1/reports/S4-package.md) |
| S5 3D 预览 | 29 件 STL 统一中性着色（如实标注），包围盒顶 1.323 m ↔ 官网 1320 mm 吻合；**预览页 v4 config 驱动** | [pipeline/s5_preview/](pipeline/s5_preview/) |
| S6 基准 | **MuJoCo 50,809 steps/s（19.7 µs/step）**，加载 102.8 ms，展幅 2.3% | [S6-benchmark.md](models/unitree_g1/reports/S6-benchmark.md) |

## 快速开始

**在线预览（零依赖，断网可用）**

```bash
python -m http.server 8130
# 浏览器打开 http://127.0.0.1:8130/pipeline/s5_preview/index.html                 # Go2
# 或            http://127.0.0.1:8130/pipeline/s5_preview/index.html?model=unitree_g1  # G1（人形）
```

**MuJoCo 查看 / 加载**

```bash
pip install mujoco
python -m mujoco.viewer --mjcf=models/unitree_go2/mjcf/go2.xml
```

```python
import mujoco
model = mujoco.MjModel.from_xml_path("models/unitree_go2/mjcf/go2.xml")
data = mujoco.MjData(model)
mujoco.mj_step(model, data)   # 模型加载与步进就这么多
```

## 复现管道

```bash
# 环境体检（决定 venv / conda，双镜像兜底）
python pipeline/env_check.py
# 各步（按序；S0 是人工 license 核对，见 PIPELINE.md）；<model> = configs/ 下的模型名
python pipeline/s1_fetch.py unitree_g1   # 拉取 + manifest + blob-parity 门
python pipeline/s2_validate.py unitree_g1   # 格式校验（含引用大小写核验）
python pipeline/s3_physics.py unitree_g1    # 物理体检
python pipeline/s4_package.py unitree_g1    # 入库对账（三锚溯源）
python pipeline/s6_bench.py unitree_g1      # 基准
```

## License（双层结构）

- **本库**：MIT（[LICENSE](LICENSE)）。
- **models/ 内上游文件**：属再分发，BSD-3-Clause 义务随文件走——上游 license 原文随模型入库
  （[models/unitree_go2/LICENSE-upstream-*.txt](models/unitree_go2/)），索引见 [LICENSES.md](LICENSES.md)。
- `pipeline/s5_preview/libs/` 内 vendor 的 three.js（MIT）随附其原版 LICENSE。

**商标声明**：Unitree / Go2 / G1 为宇树科技（杭州宇树科技）商标；本项目非官方、无关联、无背书。

## 目录结构

```
pipeline/        质检脚本（s1–s6 + env_check + configs，模型无关）
models/          入库产物（模型文件 + 报告 + license 快照 + 溯源记录）
workspace/       可丢弃中间态（raw 快照/修复稿，gitignore）
DEVLOG.md        滚动日志    PIPELINE.md 管道设计
AGENT-LAB.md     失败档案    REVIEW.md 审核结论（只读）
```
