# S1 拉取记录（unitree_g1）· 2026-10-11 17:36

```json
{
  "model": "unitree_g1",
  "repos": [
    {
      "repo": "unitreerobotics/unitree_ros",
      "pin": "5994d4faef0a9cadd3287f8de0199a67eeb2a259",
      "resolved_head": "5994d4faef0a9cadd3287f8de0199a67eeb2a259",
      "method": "直连",
      "files": 223,
      "bytes": 120713077
    },
    {
      "repo": "unitreerobotics/unitree_mujoco",
      "pin": "1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d",
      "resolved_head": "1eb6642e3f3fdfb7fb13a9794fd6a2dd93ea0e7d",
      "method": "直连",
      "files": 76,
      "bytes": 37110384
    }
  ],
  "license": [
    {
      "repo": "unitree_ros",
      "status": "MATCH",
      "sha256": "84aac59fd3246e3ddc49d1387644e8fcf43b0def4f0b9fe687f372e90446df2d"
    },
    {
      "repo": "unitree_mujoco",
      "status": "MATCH",
      "sha256": "a5d73fc4aca9074e3e6fe0b1a0ba763cf9514b2249b7390ed20fe8d53630bf25"
    }
  ],
  "manifest": {
    "files": 299,
    "bytes": 157823461,
    "sample3_ok": true
  }
}
```

## 人读补充（2026-10-11 · S1 收尾侦察，workspace/m1_recon/s1_inspect.py 可重放）

- **J1 计数重放（raw 实测，非引用送审件）**：ros 侧顶层模型文件 = **23 urdf + 10 xml = 33 文件**，按 stem 去重 **23 配置**（23dof 系 3、29dof 系 17、特殊基底 g1_comp/g1_dual_arm/g1_pl 3）。与 R10-J1 逐位一致。本库收 g1_23dof 配对，其余 32 文件不入库（S4 excluded 逐件列）。
- **A2 子目录声明复查（S0 §4 待办闭环）**：`g1_description/README.md`、`g1_description/motor_info.md`、`unitree_robots/g1/g1_joint_index_dds.md` 三个上游文档**许可关键词全无**（license/BSD/Apache/MIT/copyright/版权）——无需快照许可声明，按上游文档件 excluded 归档。
- **A2 license 快照 MATCH**：两仓 raw LICENSE sha256 = `84aac59f…` / `a5d73fc4…`，与 S0 blob-exact 快照逐字节一致——**L8 正本检出铁律生效的实证**（新克隆 autocrlf=false，检出件天然 = blob，A2 一次通过；对比 M0 同步骤抓到 CRLF 失真）。
- **格式差异 #3（M1 新事实，S2/S4 改码点报备）**：g1_23dof.urdf 的网格引用 **50/50 全为相对路径 `meshes/xxx.STL`**（urdf 位于包根，相对自身解析）——与 Go2 的 `package://go2_description/dae/…` 协议不同。影响：S2 网格引用校验、S4 网格闭包解析需按"引用协议"分支（config 字段化：`ref_style: package|relative`），S2/S4 实现时报备。
- **MJCF 闭包面（S4 整拷/闭包决策输入）**：g1_23dof.xml 的 `<mesh file=…>` 引用 **29 件**（去重后）；meshes/ 池 60 件中其余 **31 件为 29dof/手部/腰部约束网格**（left/right_hand_*、waist_*、torso_constraint_*、*_rubber_hand——23dof 无手无腰，件数自洽）。**S4 决策：闭包拷贝 29 件**（整拷将冗余 31 件/约 16 MB，否决）。
- **ros meshes/ 池**：173 件 STL / 110.4 MB 全变体共享；23dof.urdf 引用 50 处 → 去重物理件数在 S2 解析后精确化（预估 ~25 件）。
- raw 只读：299 文件 / 157.8 MB（ros 223 + mujoco 76），manifest.sha256 真身 workspace/raw/unitree_g1/（gitignored），副本上方 JSON。
