# S2 格式校验报告 — deeprobotics_dr02（2026-10-24 17:29）

环境：yourdfpy 0.0.60 · trimesh 5.1.1 · mujoco 3.15.0 · Python 3.14.6

## 校验矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:xml-wellformed` | PASS | lxml 解析成功（38879 字节） |
| `urdf:names-unique` | PASS | 40 links / 39 joints，无重名 |
| `urdf:tree` | PASS | 根=base_link，全树可达，无环无菱形 |
| `urdf:mesh-refs` | PASS | 36 处引用（ref_style=relative）→ 解析出 34 个文件，缺失 0，越界/外包 0，大小写失配 0；visual 引 34 个文件、collision 引 2 个，集合不同（素材归 S3-A1 清点） |
| `urdf:mesh-loadable` | PASS | 34 个网格 trimesh 全部读通，最小顶点数 14976 |
| `urdf:joint-limits` | PASS | 关节类型 {'revolute': 31, 'fixed': 8}；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3） |
| `urdf:yourdfpy-parse` | PASS | yourdfpy 0.0.60 解析成功：40 links / 39 joints |
| `mjcf:xml-wellformed` | PASS | lxml 解析成功（32475 字节） |
| `mjcf:compile-model` | PASS | nbody=41 njnt=32 ngeom=70 nmesh=34 nu=31 nq=38 timestep=0.0020（274 ms） |
| `mjcf:compile-scene` | PASS | 场景包装（DR02_pro.xml）编译成功 |

## 汇总

PASS 10 / WARN 0 / FAIL 0

**结论：全部通过，可进 S3**
