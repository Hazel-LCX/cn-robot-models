# S2 格式校验报告 — deeprobotics_lite3（2026-10-11 19:43）

环境：yourdfpy 0.0.60 · trimesh 5.1.1 · mujoco 3.15.0 · Python 3.14.6

## 校验矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:xml-wellformed` | PASS | lxml 解析成功（15495 字节） |
| `urdf:names-unique` | PASS | 17 links / 16 joints，无重名 |
| `urdf:tree` | PASS | 根=TORSO，全树可达，无环无菱形 |
| `urdf:mesh-refs` | PASS | 13 处引用（ref_style=relative）→ 解析出 4 个文件，缺失 0，越界/外包 0，大小写失配 0；visual 引 4 个文件、collision 引 0 个，集合不同（素材归 S3-A1 清点） |
| `urdf:mesh-loadable` | PASS | 4 个网格 trimesh 全部读通，最小顶点数 19560 |
| `urdf:joint-limits` | PASS | 关节类型 {'revolute': 12, 'fixed': 4}；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3） |
| `urdf:yourdfpy-parse` | PASS | yourdfpy 0.0.60 解析成功：17 links / 16 joints |
| `mjcf:xml-wellformed` | PASS | lxml 解析成功（14445 字节） |
| `mjcf:compile-model` | PASS | nbody=18 njnt=13 ngeom=35 nmesh=13 nu=12 nq=19 timestep=0.0020（73 ms） |
| `mjcf:compile-scene` | PASS | 场景包装（Lite3.xml）编译成功 |

## 汇总

PASS 10 / WARN 0 / FAIL 0

**结论：全部通过，可进 S3**
