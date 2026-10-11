# SOURCE — unitree_go2 来源与 License 核对记录（S0 产物）

> **状态：待审核台确认（协议②触发，REVIEW-REQUEST.md 已送审）。确认前不拉取、不处理任何模型文件。**
> 核对：写码工作台 · 2026-10-11 · 取证方式 = GitHub API / 官网 HTML 实测（raw.githubusercontent 不通，未使用）

## 1. 数据源（两仓库，均官方 org）

| 项 | unitree_ros（URDF 源） | unitree_mujoco（MJCF 源） |
|---|---|---|
| 仓库 | https://github.com/unitreerobotics/unitree_ros | https://github.com/unitreerobotics/unitree_mujoco |
| 拉取锚点 | 分支 `master` @ `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 分支 `main` @ `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` |
| 目标子目录 | `robots/go2_description/` | `unitree_robots/go2/` |
| 模型内容 | `urdf/go2_description.urdf` + `dae/` + `meshes/`（stl）+ `xacro/` | `go2.xml` + `scene.xml` + `assets/`（obj 网格） |

注意：unitree_ros 默认分支是 **master** 不是 main，S1 命令按此执行。

## 2. 官方 org 验证（A4 证据链，两条路径均成立）

- **路径①官网链接（强证据）**：unitree.com 官网首页 HTML 含 `github.com/unitreerobotics` 链接（HTTP 200 实测于 2026-10-11）。
- **路径②org 自述 + 非 fork**：GitHub org `unitreerobotics` 自述 "High performance civilian robot manufacturer"，`blog` 字段 = https://www.unitree.com（官网与 org 互指）；两仓库 API 返回 `"fork": false, "archived": false`（2026-10-11 实测）。
- 备注：PIPELINE 验收原文写"URL 与截图日期"；本记录以实测输出为证据原件，如审核台要求补截图再补。

## 3. License 核对结论

| 仓库 | License | 版权方 | 原文快照 |
|---|---|---|---|
| unitree_ros | **BSD-3-Clause** | HangZhou YuShu Technology CO.,LTD. ("Unitree Robotics")，© 2016–2022 | `LICENSE-upstream-unitree_ros.txt` |
| unitree_mujoco | **BSD-3-Clause** | 同上，© 2016–2024 | `LICENSE-upstream-unitree_mujoco.txt` |

**三条结论**（BSD-3 逐条对应）：

1. **允许再分发：是**（第 1 条：源码与二进制形式再分发均许可）；
2. **允许修改：是**（第 1、2 条：修改版须随附声明性 notice）；
3. **须保留版权声明：是**（第 2 条：再分发必须保留版权声明、条件清单与免责声明；第 3 条：未经许可不得以版权方名义背书衍生产品——对应 S7 的 B3 商标声明义务）。

**子目录独立声明检查（A2）**：

- `robots/go2_description/package.xml`：`<license>BSD</license>`，与仓库级一致。附带质检发现：`<maintainer email="TODO@email.com"/>` 是占位符，上游工程卫生问题，记录为素材。
- `unitree_robots/go2/`：目录内无独立 LICENSE/README 声明 → 随仓库级 BSD-3。

**二进制文件假设**：dae/stl/obj 网格跟随仓库同一 license。依据 = 仓库无单独 media license 文件、无 NOTICE 排除声明。此假设已记录，审核台如认为不足可打回。

## 4. 快照一致性（A2，S1 复核项）

S0 快照经 GitHub API 在上表锚点取到。**S1 拉取后必须以 raw 内同一 commit 的 LICENSE 文件复核重生成快照**，并在本文件补记"license 文件 commit hash = 模型文件 commit hash"复核结论。

## 5. 对本库的义务（已落 LICENSES.md）

- 再分发保留版权声明与三条款文本 → 已随快照入库；
- 不得以 Unitree 名义背书本项目 → S7 商标声明（B3）落实；
- 本库自身 MIT（R1 四问已批），与上游 BSD-3 兼容，义务随文件走。
