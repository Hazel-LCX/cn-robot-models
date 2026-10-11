# SOURCE — unitree_go2 来源与 License 核对记录（S0 产物）

> **状态：已确认（R3 · 2026-10-11）——S0 license 门正式关闭。**
> 核对：写码工作台 · 2026-10-11 · 取证方式 = GitHub API / 官网 HTML 实测（raw.githubusercontent 不通，未使用）；R3 复核结论见 REVIEW.md

## 1. 数据源（两仓库，均官方 org）

| 项 | unitree_ros（URDF 源） | unitree_mujoco（MJCF 源） |
|---|---|---|
| 仓库 | https://github.com/unitreerobotics/unitree_ros | https://github.com/unitreerobotics/unitree_mujoco |
| 拉取锚点 | 分支 `master` @ `5994d4faef0a9cadd3287f8de0199a67eeb2a259` | 分支 `main` @ `1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d` |
| 目标子目录 | `robots/go2_description/` | `unitree_robots/go2/` |
| 模型内容 | `urdf/go2_description.urdf` + `dae/` + `meshes/`（**实测均 .dae，无 stl**——R3-D3 更正）+ `xacro/` | `go2.xml` + `scene.xml` + `assets/`（obj 网格） |

注意：unitree_ros 默认分支是 **master** 不是 main，S1 命令按此执行。

**收录与权威关系（修正 8）**：go2_description 内 `urdf/`（生成物）与 `xacro/`（源）两份都收——**入库与质检以官方 `urdf/` 为准**，`xacro/` 存档供溯源；若发现"xacro 已改、urdf 未重生成"的漂移，记录为质检素材，不代上游重新生成。
**拉取方法（修正 5）**：blobless 部分克隆 + sparse-checkout（monorepo 只拉 go2 子目录），锚点为上表 SHA；API 逐文件兜底，代理 socks5h://127.0.0.1:12450 备用。

## 2. 官方 org 验证（A4 证据链——证据原件存档，修正 4）

结论不变（两条路径均成立），可追溯性升级：**复核看原件，不看转述**。原件存 `evidence/`（均 2026-10-11 实测抓取）：

| 原件文件 | 内容 | 支撑 |
|---|---|---|
| `evidence/unitree-homepage-link.html.txt` | unitree.com 首页 HTML 中指向 `github.com/unitreerobotics` 的原文片段（含前后 200 字节上下文，文件头注明抓取 URL 与日期） | 路径① |
| `evidence/github-org-unitreerobotics.json` | GitHub org API 原始返回全文（description / blog / type 字段在案） | 路径② |
| `evidence/github-repo-unitree_ros.json`、`evidence/github-repo-unitree_mujoco.json` | 两仓库 API 原始返回全文（fork / archived / default_branch 字段在案） | 路径② |

关键摘录（原文引用，非转述）：

```text
官网首页导航链接原文片段（完整上下文见 evidence 文件）：
<a href="https://github.com/unitreerobotics" rel="noopener noreferrer" target="_blank"
```

```text
"description": "High performance civilian robot manufacturer. Please everyone be sure to use the robot in a Friendly and Safe manner.",
"blog": "https://www.unitree.com",
"type": "Organization"
```

```text
"fork": false,        ← unitree_ros 与 unitree_mujoco 两仓库 JSON 原件均含此字段
"archived": false,
```

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

## 4. 快照一致性（A2，S1 复核结论；R10-K1 判据修正后现态）

S0 快照经 GitHub API 取得；S1 以 raw 内同 commit 文件复核；**K1（R10）后以上游 git blob 为正本终裁**。现态（2026-10-11 K1 后）：

| 仓库 | resolved HEAD | 复核状态 | LICENSE SHA256（= blob 正本） |
|---|---|---|---|
| unitree_ros | `5994d4fa…a259`（= 送审锚点） | **快照 v3 = blob-exact**（与 unitree_g1 快照逐字节相同） | `84aac59f…6df2d`（1558 B，0 CR） |
| unitree_mujoco | `1eb6642e…a0e7d`（= 送审锚点） | **快照 v3 = blob-exact**（与 unitree_g1 快照逐字节相同） | `a5d73fc4…0bf25`（1559 B，0 CR） |

- **A2 抓到的真问题（历史，2026-10-11）**：S0 快照 v1（走 GitHub `/license` API 端点）与 raw 检出件**字节不一致**——已查明原因：**当时解释方向判反了**。真相（R10 终裁）：上游 blob 本身即 LF；raw 检出件被本地 autocrlf 转成 CRLF，**检出件才是衍生物**。快照 v2（从 raw 检出件重生成）因此也是 CRLF 件，随 K1 一并归正为 v3 = blob-exact。
- **正本判据（R10 修正，永久生效）**：**上游 git blob（`git cat-file` / contents API base64）为唯一正本，永不采信工作区检出件。**
- **K1 修复七步（2026-10-11，R10 指定，S1 前置已完成）**：①两克隆 autocrlf=false + 检出区 62 件全量 cat-file 导出（62/62 == blob；5 件 PNG 的"CRLF"为二进制数据随机字节，非行尾）；②models/ 34 件替换为 blob-exact（逐件前后 SHA256 记档 workspace/k1_fix/blob_exact.json）；③S4 全量重跑（traceability 33/33，FAIL 0）；④S2+S3 回归门重跑（10/0/0 与 8/4/0/SKIP1，WARN 均既有处置）；⑤本节与两处 README 对账行同刷；⑥AGENT-LAB L8 记档；⑦commit + push（R10 授权，无需新送审）。
- license 文件与模型文件同 commit（resolved HEAD = 送审锚点，两仓库均成立）✓。
- 拉取方法（M0 原始记录保留）：**直连 blobless+sparse 一次成功**（代理/API 兜底未动用）；ros 36 文件、mujoco 26 文件，合计 62 文件。M0 报告的 82.3 MB 为当时 CRLF 检出件现态字节；**K1 后检出区全正本口径 = 77.7 MB**——差 4.6 MB 为 dae/obj 逐行几何数据约 500 万个行尾的累计（非文件增删，62 件数前后一致）。
- **入库对账（S4，K1 后现态）**：**34 个物理文件**（33 个 raw 溯源件逐文件 SHA256 命中 manifest 同路径行 + 1 个质检截图）/ **55,357,945 B（55.4 MB）** 落 `models/unitree_go2/`（reports/S4-package.md）；dae/ 与 meshes/ 判定同内容冗余（**7/0，物理文件口径**——URDF 17 处 visual 引用共享 7 个物理 dae，引用行 ≠ 文件数），meshes/ 不随库分发；两源网格哈希交集 0 → 分目录，MJCF 网格落 `mjcf/assets/`（保持官方 meshdir 相对引用）；入库路径 MJCF 编译 + yourdfpy 双复验通过。

## 5. 对本库的义务（已落 LICENSES.md）

- 再分发保留版权声明与三条款文本 → 已随快照入库；
- 不得以 Unitree 名义背书本项目 → S7 商标声明（B3）落实；
- 本库自身 MIT（R1 四问已批），与上游 BSD-3 兼容，义务随文件走。
