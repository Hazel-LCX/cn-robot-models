# S2 格式校验报告 — booster_t2_wujihand（2026-10-25 20:33）

环境：yourdfpy 0.0.60 · trimesh 5.1.1 · mujoco 3.15.0 · Python 3.14.6

## 校验矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:xml-wellformed` | PASS | lxml 解析成功（96175 字节） |
| `urdf:names-unique` | FAIL | 87 links / 86 joints；重名：['logo'] |
| `urdf:tree` | PASS | 根=trunk，全树可达，无环无菱形 |
| `urdf:mesh-refs` | PASS | 141 处引用（ref_style=relative）→ 解析出 87 个文件，缺失 0，越界/外包 0，大小写失配 0；visual 引 85 个文件、collision 引 56 个，集合不同（素材归 S3-A1 清点） |
| `urdf:mesh-loadable` | PASS | 87 个网格 trimesh 全部读通，最小顶点数 756 |
| `urdf:joint-limits` | PASS | 关节类型 {'revolute': 71, 'fixed': 15}；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3） |
| `urdf:yourdfpy-parse` | PASS | yourdfpy 0.0.60 解析成功：87 links / 86 joints |
| `mjcf:xml-wellformed` | PASS | lxml 解析成功（67503 字节） |
| `mjcf:compile-model` | PASS | nbody=73 njnt=72 ngeom=157 nmesh=87 nu=71 nq=78 timestep=0.0010（396 ms） |
| `mjcf:compile-scene` | PASS | 场景包装（T2_31dof_WujiHand.xml）编译成功 |

## 汇总

PASS 9 / WARN 0 / FAIL 1

**结论：1 个阻塞项——fail 已如实落表，处置走 S3/送审**
