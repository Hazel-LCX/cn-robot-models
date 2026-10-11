# S2 格式校验报告 — unitree_go2（2026-10-11 13:11）

环境：yourdfpy 0.0.60 · trimesh 5.1.1 · mujoco 3.15.0 · Python 3.14.6

## 校验矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:xml-wellformed` | PASS | lxml 解析成功（28201 字节） |
| `urdf:names-unique` | PASS | 42 links / 41 joints，无重名 |
| `urdf:tree` | PASS | 根=base，全树可达，无环无菱形 |
| `urdf:mesh-refs` | PASS | 17 处引用 → 解析出 7 个文件，缺失 0，非本包 0；visual 引 7 个文件、collision 引 0 个，集合不同（素材归 S3-A1 清点） |
| `urdf:mesh-loadable` | PASS | 7 个网格 trimesh 全部读通，最小顶点数 7703 |
| `urdf:joint-limits` | PASS | 关节类型 {'fixed': 29, 'revolute': 12}；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3） |
| `urdf:yourdfpy-parse` | PASS | yourdfpy 0.0.60 解析成功：42 links / 41 joints |
| `mjcf:xml-wellformed` | PASS | lxml 解析成功（15169 字节） |
| `mjcf:compile-model` | PASS | nbody=18 njnt=13 ngeom=56 nmesh=16 nu=12 nq=19 timestep=0.0020（161 ms） |
| `mjcf:compile-scene` | PASS | scene.xml（模型 + 地形 + 光照）编译成功 |

## 汇总

PASS 10 / WARN 0 / FAIL 0

**结论：全部通过，可进 S3**
