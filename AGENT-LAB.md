# AGENT-LAB — 写码台失败与自救记录

> 纪律（R1-④ 立规）：每次失败记四要素——现象 / 根因 / 自救动作 / 是否升级 codex 会诊。R2 起审核台查账。

## 2026-10-11 · L5 · 预览模型"半截沉在网格下"→两轮修复（用户反馈抓出，F1 修复同期）

- **现象**：①用户首报"大半个身子在地平线以下"；②第一版修复后用户再报"没有踏地，悬空了"。
- **根因（两层）**：第一层——URDF base 原点在髋部、足端 z≈−0.32，Z-up 转换只修方向没修位置；第二层（真根因）——落地抬升的包围盒在**初次渲染前**计算，three.js 场景图组装后父级 `matrixWorld` 尚未更新，`Box3.setFromObject`/`expandByObject`（内部 `updateWorldMatrix(false,false)`）拿到陈旧矩阵 → 算出抬升 0.097m（真实需要 0.245m），差值即悬浮量。
- **自救**：v3 = 落地计算挪到滑条初始化之后 + `model.updateMatrixWorld(true)` 强制刷新 + 只按可见网格 bbox；面板上屏"载入版本/抬升量/包围盒"自证；逐 mesh 实测世界 min.y = 0（足端踏地）。
- **是否升级**：否。**教训**：①three.js 在首次渲染前手动算世界包围盒必须先 `updateMatrixWorld(true)`；②连诊断脚本都踩了同一个陈旧矩阵坑——两轮测量互相打脸，最终以"逐 mesh 分解 + updateMatrixWorld"定案。


## 2026-10-11 · L4 · 干净环境实测抓到 autocrlf 破坏哈希承诺（S7，本项目最有价值的一次自查）

- **现象**：git clone 后 six 项哈希抽查 5/6——`three.module.js` 与工作区不一致；它是唯一以 LF 行尾入库的资产，git autocrlf 在 checkout 时把它转成了 CRLF。
- **根因**：Git for Windows 的 autocrlf 对文本文件做行尾转换；上游模型件全为 CRLF，入库起就从未暴露此雷。
- **自救**：`.gitattributes` 对 `models/**`、`pipeline/s5_preview/libs/**`、`workspace/**` 锁 `-text`（凡哈希被报告引用的资产，字节级稳定）+ `git add --renormalize` + 重 clone 复测 **6/6 ✓** 且 clone 内 MJCF 加载 OK。
- **是否升级**：否。**教训**：对承诺"逐哈希溯源"的项目，`.gitattributes` 是第一天就该有的配置——是 S7 干净环境实测（近似新 clone 体验）逼出来的，不是想出来的。
- **顺带**：首跑还抓到"模型页引用的截图忘了 commit"——干净环境实测的价值一晚兑现两次。

## 2026-10-11 · L2 · S5 实现路径决策（R1-④ 必记档）

- **决策点**：vendor 现成 URDFLoader vs B6 退路自写。
- **现象**：jsDelivr npm 路径超时（继 raw 之后第二个被证实的封锁面）；npmmirror registry API 通，但 urdf-loader 的 `latest` 标签停在 0.13.1（真 latest 2.x 未同步/不可验证），依赖链（three 版本匹配 + three-mesh-bvh）在镜像上无法闭合验证。
- **自救/决策**：走 B6 退路——自写 URDF→three 加载器 ~180 行（边界内：XML 解析 + 坐标变换 + 关节交互），DAE 解析 vendor 官方 ColladaLoader/TGALoader + OrbitControls；npmmirror **files API**（`registry.npmmirror.com/<pkg>/<ver>/files/<path>`）单文件拉取，比 tgz 精准且实测可靠。
- **是否升级**：否。

## 2026-10-11 · L3 · 预览页首版三连 bug（浏览器截图自验收抓出）

- **现象**：①calf 滑条初值 0 被浏览器钳位到 -0.44 且标红——calf 的 URDF 限位 [-2.72, -0.84] **不含 0**，零位本身就是非法姿态；②整机侧躺——URDF 是 Z-up、three 是 Y-up，未做坐标转换；③rpy 四元数分量序写反（Euler(p,r,y) 应为 (r,p,y)）。
- **根因**：①默认"0 是合法初值"没查限位；②坐标系惯性思维；③Euler 顺序语义记混。
- **自救**：①初值 clamp(0,lo,hi)，不在限位内取限位中点；②model.rotation.x = -π/2；③分量序修正——两轮浏览器截图复验，站姿正确、红标清零。
- **是否升级**：否。附注：滑条越限标红机制被 bug 意外自证有效（calf 0.00→-0.44 红标亮起即质检元素工作）。


## 2026-10-11 · L1 侦察脚本 TypeError（S3 侦察第一波）

- **现象**：抓官网规格页的 heredoc 脚本在第 9 行抛 `TypeError: 'enumerate' object is not subscriptable`，脚本中断，后续质量对比没跑到。
- **根因**：对 `enumerate()` 生成器直接切片（`enumerate(...)[:10]`）——生成器不支持下标，低级失误。
- **自救**：改为 `list(...)[:10]`（先物化再切片），重跑成功。
- **是否升级**：否。一行修复，无复发风险。
- **顺带记录**：Git Bash 的 grep 是 ugrep，`.{0,160}` 上下文正则触发 "exceeds complexity limits"——同类抓取任务改用 python re，不再用 ugrep 复杂正则（已两次踩到）。
