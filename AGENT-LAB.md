# AGENT-LAB — 写码台失败与自救记录

> 纪律（R1-④ 立规）：每次失败记四要素——现象 / 根因 / 自救动作 / 是否升级 codex 会诊。R2 起审核台查账。

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
