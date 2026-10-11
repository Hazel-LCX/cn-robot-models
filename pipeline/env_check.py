#!/usr/bin/env python
"""env_check.py — M0 动手前的环境体检。

把"能不能开工"从口头感觉变成一张可复现的检查单：
逐项给出 PASS / WARN / FAIL，并给出环境路线建议（venv 或 conda py3.12）。

用法：
    python env_check.py            # 人读报告
    python env_check.py --json     # 机读报告（供管道后续步骤引用）

退出码：0 = 无阻塞项；1 = 存在 FAIL。WARN 均有兜底路径，不算阻塞。
"""

import argparse
import importlib.util
import json
import platform
import shutil
import subprocess
import sys
import urllib.request

ALIYUN_INDEX = "https://mirrors.aliyun.com/pypi/simple/"

# (import 名, 用途, 缺失是否阻塞)。阻塞=FAIL（必须有），否则 WARN（装上才算齐）。
REQUIRED_IMPORTS = [
    ("numpy",    "矩阵与惯量计算（S2、S3）",      True),
    ("scipy",    "旋转矩阵与四元数换算",          False),
    ("lxml",     "URDF/MJCF 的 XML 解析",         True),
    ("trimesh",  "网格读取与包围盒（S2、S3）",    True),
    ("yourdfpy", "URDF 解析器（S2 主校验）",      True),
    ("mujoco",   "MJCF 编译校验与 S6 基准",       True),
]

# (名称, URL, 不通时的定级)。网络三项都为 S1 拉取选路服务。
NET_PROBES = [
    ("pypi-阿里镜像", ALIYUN_INDEX,                        "FAIL"),
    ("github-api",    "https://api.github.com",            "WARN"),
    ("github-raw",    "https://raw.githubusercontent.com", "WARN"),
]


def check_python():
    ok = sys.version_info >= (3, 10)
    detail = f"{platform.python_version()} @ {sys.executable}"
    return ("python", "PASS" if ok else "FAIL", detail)


def check_git():
    path = shutil.which("git")
    if path is None:
        return ("git", "WARN", "未找到 git——S1 可走 API 兜底，但仓库版本化需要它")
    ver = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
    return ("git", "PASS", f"{ver} @ {path}")


def check_imports():
    results = []
    for name, purpose, blocking in REQUIRED_IMPORTS:
        if importlib.util.find_spec(name) is not None:
            results.append((f"import:{name}", "PASS", purpose))
        else:
            status = "FAIL" if blocking else "WARN"
            results.append((f"import:{name}", status, f"未安装——{purpose}"))
    return results


def check_mujoco_wheel():
    """mujoco 尚未安装时，用 pip --dry-run 探当前解释器能否解析到匹配 wheel。

    这一步决定环境路线：解析得动 → venv；解析不动 → conda 建 py3.12。
    """
    if importlib.util.find_spec("mujoco") is not None:
        import mujoco
        return ("mujoco-wheel", "SKIP", f"已安装 {mujoco.__version__}，无需探测")
    cmd = [
        sys.executable, "-m", "pip", "install", "--dry-run", "--ignore-installed",
        "--quiet", "mujoco", "-i", ALIYUN_INDEX, "--timeout", "20",
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return ("mujoco-wheel", "FAIL", "pip --dry-run 超时（180s），镜像或网络异常")
    if proc.returncode == 0:
        return ("mujoco-wheel", "PASS", "当前解释器可解析 mujoco wheel → 走 venv")
    err_tail = (proc.stderr or "").strip().splitlines()
    tail = err_tail[-1] if err_tail else "（无 stderr）"
    return ("mujoco-wheel", "FAIL", f"解析不到 wheel → 走 conda py3.12；pip 尾行：{tail}")


def check_net(name, url, level):
    """拿到任何 HTTP 响应都算"通"（状态码本身留给 S1 关心）；连接错误/超时算不通。"""
    req = urllib.request.Request(url, headers={"User-Agent": "cn-robot-models/env_check"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            return (f"net:{name}", "PASS", f"HTTP {resp.status}")
    except Exception as exc:
        kind = type(exc).__name__
        note = "pip 装不了依赖" if level == "FAIL" else "有兜底路径，不阻塞"
        return (f"net:{name}", level, f"不通（{kind}）——{note}")


def suggest_route(checks):
    if importlib.util.find_spec("mujoco") is not None:
        return "当前解释器已可用；项目仍走独立环境（隔离、可复现），venv 即可"
    wheel_ok = any(n == "mujoco-wheel" and s == "PASS" for n, s, _ in checks)
    if wheel_ok:
        return "venv：python -m venv .venv（mujoco wheel 可解析）"
    return "conda：create -n cnrobot python=3.12（当前版本无 mujoco wheel）"


def main():
    parser = argparse.ArgumentParser(description="M0 环境体检")
    parser.add_argument("--json", action="store_true", help="输出机读 JSON")
    args = parser.parse_args()

    checks = [check_python(), check_git()]
    checks += check_imports()
    checks.append(check_mujoco_wheel())
    checks += [check_net(name, url, level) for name, url, level in NET_PROBES]

    route = suggest_route(checks)
    n_pass = sum(s == "PASS" for _, s, _ in checks)
    n_warn = sum(s == "WARN" for _, s, _ in checks)
    n_fail = sum(s == "FAIL" for _, s, _ in checks)

    if args.json:
        print(json.dumps({
            "python": platform.python_version(),
            "executable": sys.executable,
            "checks": [{"name": n, "status": s, "detail": d} for n, s, d in checks],
            "route": route,
            "blocked": n_fail > 0,
        }, ensure_ascii=False, indent=2))
    else:
        width = max(len(n) for n, _, _ in checks)
        for name, status, detail in checks:
            print(f"[{status}] {name:<{width}}  {detail}")
        print(f"\n汇总：PASS {n_pass} / WARN {n_warn} / FAIL {n_fail}")
        print(f"路线建议：{route}")

    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
