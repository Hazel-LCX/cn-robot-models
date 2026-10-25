# S2 格式校验报告 — deeprobotics_x30（2026-10-25 18:44）

环境：yourdfpy 0.0.60 · trimesh 5.1.1 · mujoco 3.15.0 · Python 3.14.6

## 校验矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:xml-wellformed` | PASS | lxml 解析成功（15916 字节） |
| `urdf:names-unique` | PASS | 21 links / 20 joints，无重名 |
| `urdf:tree` | PASS | 根=TORSO，全树可达，无环无菱形 |
| `urdf:mesh-refs` | PASS | 13 处引用（ref_style=relative）→ 解析出 4 个文件，缺失 0，越界/外包 0，大小写失配 0；visual 引 4 个文件、collision 引 0 个，集合不同（素材归 S3-A1 清点） |
| `urdf:mesh-loadable` | PASS | 4 个网格 trimesh 全部读通，最小顶点数 31752 |
| `urdf:joint-limits` | PASS | 关节类型 {'revolute': 12, 'fixed': 8}；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3） |
| `urdf:yourdfpy-parse` | PASS | yourdfpy 0.0.60 解析成功：21 links / 20 joints |
| `mjcf:xml-wellformed` | PASS | lxml 解析成功（9771 字节） |
| `mjcf:compile-model` | PASS | nbody=22 njnt=12 ngeom=35 nmesh=8 nu=0 nq=12 timestep=0.0020（146 ms） |
| `mjcf:compile-scene` | PASS | 场景包装（X30.xml）编译成功 |

## 汇总

PASS 10 / WARN 0 / FAIL 0

**结论：全部通过，可进 S3**
