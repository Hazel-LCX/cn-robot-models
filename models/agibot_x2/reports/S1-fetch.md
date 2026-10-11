# S1 拉取记录（agibot_x2）· 2026-10-11 21:24

```json
{
  "model": "agibot_x2",
  "repos": [
    {
      "repo": "AgibotTech/agibot_x2_urdf",
      "pin": "575cc6b988f976c23550e0db85aa1e5475d3652d",
      "resolved_head": "575cc6b988f976c23550e0db85aa1e5475d3652d",
      "method": "直连",
      "files": 82,
      "bytes": 125045298
    }
  ],
  "license": [
    {
      "repo": "agibot_x2_urdf",
      "status": "MATCH",
      "sha256": "d5777bea50dc2cd111845d8a9c51ab990d188ce343b843e5ad3e653b5fa8fdab"
    }
  ],
  "manifest": {
    "files": 82,
    "bytes": 125045298,
    "sample3_ok": true
  },
  "blob_parity": [
    {
      "repo": "agibot_x2_urdf",
      "files": 78,
      "mismatch": []
    }
  ]
}
```


## 人读段（S1 复现审核台实测数 · 2026-10-11 21:24）

- 拉取：直连一次命中锚点 `575cc6b9`（分支头=锚点，无 fetch 漂移）；raw=v1.4.0 子目录 82 件 / 125,045,298 B（blobless+sparse，manifest.sha256 抽样 3 复算 OK）。
- **blob-parity 门 78 件失配 0**（K2 门第二次实战：ls-tree@pin ↔ hash-object --no-filters 全等）；license 快照 A2 MATCH（sha256 `d5777bea…`，改名后字节未变复核）。
- 审核台数独立复现：URDF mesh 引用 72（显式 `./meshes/` 前缀 True，0 例其他形式）、唯一 STL 40、link 39 / joint 38（{'fixed': 7, 'revolute': 31}）、meshes/ .stl 65 件全小写扩展名——R17 实测数（72/40/39/38/31 revolute+7 fixed/65）逐项对上。
- 引用↔磁盘双向对账：URDF 引用缺失 无；磁盘未引用 ['base_link.stl', 'finger_abad.stl', 'finger_dip.stl', 'finger_pip.stl', 'l_palm.stl', 'l_thumb_roll.stl', 'left_wrist_roll_extend_link.stl', 'left_wrist_roll_link10.stl', 'narrow1_Link.stl', 'narrow2_Link.stl', 'narrow3_Link.stl', 'narrow_loop_Link.stl', 'r_palm.stl', 'r_thumb_roll.stl', 'right_wrist_roll_extend_link.stl', 'right_wrist_roll_link2.stl', 'thumb_abad.stl', 'thumb_dip.stl', 'thumb_mcp.stl', 'thumb_pip.stl', 'torso_lite_link.stl', 'wide1_Link.stl', 'wide2_Link.stl', 'wide3_Link.stl', 'wide_loop_Link.stl']（**65−40=25 件为 EDU/omnihand/omnipicker/simple_collision 变体共用网格池，与 G1 共享池先例同构，S4 closure 按引用闭包**）；大小写失配 无。
- MJCF 侧：meshdir=`meshes/`，mesh 元素 40 引 40 唯一件（缺失 无）；body 32 / joint 32（free 悬浮根预计含内，S3 细查）。
- R17 口径小瑕备案执行：x2_fist 仅在 v1.3.0（本 raw 无此件——sparse 隔离实证），不入库清单单列冗余无害。
