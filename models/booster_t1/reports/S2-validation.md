# S2 格式校验报告 — booster_t1（2026-10-24 15:39）

环境：yourdfpy 0.0.60 · trimesh 5.1.1 · mujoco 3.15.0 · Python 3.14.6

## 校验矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:xml-wellformed` | PASS | lxml 解析成功（29733 字节） |
| `urdf:names-unique` | PASS | 25 links / 24 joints，无重名 |
| `urdf:tree` | PASS | 根=trunk，全树可达，无环无菱形 |
| `urdf:mesh-refs` | PASS | 25 处引用（ref_style=relative）→ 解析出 25 个文件，缺失 0，越界/外包 0，大小写失配 0；visual 引 25 个文件、collision 引 0 个，集合不同（素材归 S3-A1 清点） |
| `urdf:mesh-loadable` | PASS | 25 个网格 trimesh 全部读通，最小顶点数 3462 |
| `urdf:joint-limits` | PASS | 关节类型 {'revolute': 23, 'fixed': 1}；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3） |
| `urdf:yourdfpy-parse` | PASS | yourdfpy 0.0.60 解析成功：25 links / 24 joints |
| `mjcf:xml-wellformed` | PASS | lxml 解析成功（18682 字节） |
| `mjcf:compile-model` | PASS | nbody=26 njnt=24 ngeom=48 nmesh=25 nu=23 nq=30 timestep=0.0020（83 ms） |
| `mjcf:compile-scene` | PASS | 场景包装（T1_23dof.xml）编译成功 |

## 汇总

PASS 10 / WARN 0 / FAIL 0

**结论：全部通过，可进 S3**
