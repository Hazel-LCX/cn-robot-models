# AGENT-LAB — 写码台失败与自救记录

> 纪律（R1-④ 立规）：每次失败记四要素——现象 / 根因 / 自救动作 / 是否升级 codex 会诊。R2 起审核台查账。

## 2026-10-11 · L1 侦察脚本 TypeError（S3 侦察第一波）

- **现象**：抓官网规格页的 heredoc 脚本在第 9 行抛 `TypeError: 'enumerate' object is not subscriptable`，脚本中断，后续质量对比没跑到。
- **根因**：对 `enumerate()` 生成器直接切片（`enumerate(...)[:10]`）——生成器不支持下标，低级失误。
- **自救**：改为 `list(...)[:10]`（先物化再切片），重跑成功。
- **是否升级**：否。一行修复，无复发风险。
- **顺带记录**：Git Bash 的 grep 是 ugrep，`.{0,160}` 上下文正则触发 "exceeds complexity limits"——同类抓取任务改用 python re，不再用 ugrep 复杂正则（已两次踩到）。
