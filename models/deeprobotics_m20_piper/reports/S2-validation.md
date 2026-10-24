# S2 格式校验报告 — deeprobotics_m20_piper（2026-10-24 23:09）

环境：yourdfpy 0.0.60 · trimesh 5.1.1 · mujoco 3.15.0 · Python 3.14.6

## 校验矩阵

| 检查项 | 结果 | 明细 |
|---|---|---|
| `urdf:xml-wellformed` | PASS | lxml 解析成功（29325 字节） |
| `urdf:names-unique` | PASS | 27 links / 26 joints，无重名 |
| `urdf:tree` | PASS | 根=base_link，全树可达，无环无菱形 |
| `urdf:mesh-refs` | PASS | 37 处引用（ref_style=relative）→ 解析出 27 个文件，缺失 0，越界/外包 0，大小写失配 0；visual 引 27 个文件、collision 引 10 个，集合不同（素材归 S3-A1 清点） |
| `urdf:mesh-loadable` | PASS | 27 个网格 trimesh 全部读通，最小顶点数 3528 |
| `urdf:joint-limits` | PASS | 关节类型 {'revolute': 18, 'continuous': 4, 'fixed': 2, 'prismatic': 2}；活动关节全带 <limit>（effort/velocity 数值硬校验留 S3） |
| `urdf:yourdfpy-parse` | FAIL | ValueError: could not convert string to float: '0。611'；回退亦败 ValueError: could not convert string to float: '0。611' |
| `mjcf:xml-wellformed` | PASS | lxml 解析成功（24170 字节） |
| `mjcf:compile-model` | PASS | nbody=28 njnt=25 ngeom=64 nmesh=27 nu=24 nq=31 timestep=0.0020（165 ms） |
| `mjcf:compile-scene` | PASS | 场景包装（M20_Piper.xml）编译成功 |

## 汇总

PASS 9 / WARN 0 / FAIL 1

**结论：1 个阻塞项——fail 已如实落表，处置走 S3/送审**
