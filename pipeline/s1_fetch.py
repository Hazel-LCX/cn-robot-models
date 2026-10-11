#!/usr/bin/env python
"""s1_fetch.py — S1 拉取：按送审锚点把上游原始件取进 workspace/raw/<model>/。

用法：python pipeline/s1_fetch.py [model_name]（缺省 unitree_go2，config =
pipeline/configs/<model_name>.json）。

主路径（修正 5）：blobless 部分克隆 + sparse-checkout，monorepo 只拉目标子目录；
**检出即正本（AGENT-LAB L8 铁律，K1 根治）**：克隆命令全程 -c core.autocrlf=false，
工作区字节 == 上游 blob；
兜底：GitHub API 逐文件 git/blobs base64（字节直写，天然免疫行尾转换）；
代理 socks5h://127.0.0.1:12450 重试一次。
产出：raw 快照、manifest.sha256（同步副本进 models/…/reports/）、
体积/文件数记录（reports/S1-fetch.md）、license 快照同 commit 复核（A2）。
raw 只读原则：目录已存在则拒绝执行，要重拉先手删。
"""

import base64
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

MODEL = sys.argv[1] if len(sys.argv) > 1 else "unitree_go2"
ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "pipeline" / "configs" / f"{MODEL}.json"
RAW = ROOT / "workspace" / "raw" / MODEL
MODEL_DIR = ROOT / "models" / MODEL
REPORTS = MODEL_DIR / "reports"
PROXY = "socks5h://127.0.0.1:12450"
API = "https://api.github.com"


def sh(cmd, cwd=None, timeout=570):
    env = os.environ.copy()
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          timeout=timeout, env=env)
    if proc.returncode != 0:
        raise RuntimeError(f"命令失败（{proc.returncode}）：{' '.join(cmd)}\n{proc.stderr[-600:]}")
    return proc.stdout.strip()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def api_json(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "cn-robot-models/s1_fetch",
        "Accept": "application/vnd.github+json",
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def clone_sparse(name, cfg):
    """blobless + sparse 克隆，锁到送审锚点；返回 (resolved_sha, method)。"""
    repo_dir = RAW / name
    url = f"https://github.com/{cfg['repo']}.git"
    attempts = [
        ("直连", ["-c", "core.autocrlf=false"]),
        ("代理", ["-c", "core.autocrlf=false",
                  "-c", f"http.proxy={PROXY}", "-c", f"https.proxy={PROXY}"]),
    ]
    last_err = ""
    for label, git_cfg in attempts:
        try:
            print(f"  [{label}] git clone --filter=blob:none --sparse --depth 1 {cfg['repo']}")
            sh(["git", *git_cfg, "clone", "--filter=blob:none", "--sparse", "--depth", "1",
                url, str(repo_dir)], timeout=570)
            head = sh(["git", "-C", str(repo_dir), "rev-parse", "HEAD"])
            if head != cfg["pin"]:
                print(f"  分支头 {head[:12]} ≠ 送审锚点 {cfg['pin'][:12]}，改拉锚点")
                sh(["git", *git_cfg, "-C", str(repo_dir), "fetch", "--depth", "1",
                    "origin", cfg["pin"]], timeout=570)
                sh(["git", "-C", str(repo_dir), "checkout", "--detach", "FETCH_HEAD"])
                head = sh(["git", "-C", str(repo_dir), "rev-parse", "HEAD"])
            sh(["git", "-C", str(repo_dir), "sparse-checkout", "set", cfg["subdir"]])
            return head, label
        except Exception as exc:  # noqa: BLE001 —— 记录后换下一条网络路径
            last_err = str(exc)
            print(f"  [{label}] 失败：{exc.splitlines()[-1] if exc else exc}")
    raise RuntimeError(f"{name} 两条网络路径都失败，最后错误：\n{last_err}")


def fetch_via_api(name, cfg):
    """兜底：按锚点树逐文件拉（git/blobs API 任意大小，base64 解码）。"""
    repo_dir = RAW / name
    tree = api_json(f"{API}/repos/{cfg['repo']}/git/trees/{cfg['pin']}?recursive=1")
    if tree.get("truncated"):
        raise RuntimeError("上游目录树被截断，API 兜底不可靠，需人工处理")
    entries = [e for e in tree["tree"]
               if e["type"] == "blob"
               and (e["path"] == cfg["license_path"]
                    or e["path"].startswith(cfg["subdir"] + "/"))]
    print(f"  API 兜底：{len(entries)} 个文件")
    for i, entry in enumerate(entries, 1):
        dest = repo_dir / entry["path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        blob = api_json(f"{API}/repos/{cfg['repo']}/git/blobs/{entry['sha']}")
        dest.write_bytes(base64.b64decode(blob["content"]))
        if i % 20 == 0:
            print(f"    {i}/{len(entries)}")
        time.sleep(0.15)  # 匿名 API 限额礼貌间隔
    return cfg["pin"], "api-fallback"


def write_manifest():
    lines, total = [], 0
    for repo_dir in sorted(RAW.iterdir()):
        if not repo_dir.is_dir():
            continue
        for f in sorted(repo_dir.rglob("*")):
            if not f.is_file() or ".git" in f.parts:
                continue
            rel = f.relative_to(RAW).as_posix()
            total += f.stat().st_size
            lines.append(f"{sha256_file(f)}  {rel}")
    manifest = RAW / "manifest.sha256"
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (REPORTS / "S1-manifest.sha256").write_text(
        "# 副本：真身在 workspace/raw/unitree_go2/manifest.sha256（gitignored）\n"
        + "\n".join(lines) + "\n", encoding="utf-8")
    return len(lines), total


def verify_blob_parity(cfg_list):
    """blob-parity 门（K2-④）：检出件必须与上游 blob 逐字节一致。

    方法：ls-tree -r HEAD 取每仓目标文件的 blob id；`git hash-object --stdin-paths`
    批量计算检出件的 blob id（纯内容 id，不经行尾过滤）——同 id 即同字节。
    机制背景（AGENT-LAB L9）：clone -c 只在该进程生效、不写入 repo config，
    sparse-checkout set 独立进程读全局 autocrlf 会把文本件转 CRLF——
    本门把正本性从"克隆卫生"升级为"程序化对账"，任何一环失真 FAIL 即挡。
    """
    parity = []
    for cfg in cfg_list:
        repo_dir = RAW / cfg["name"]
        ls = sh(["git", "-C", str(repo_dir), "ls-tree", "-r", "HEAD", "--", cfg["subdir"]])
        blobs = {}
        for line in ls.splitlines():
            meta, path = line.split("	", 1)
            parts = meta.split()
            if parts[1] == "blob":
                blobs[path] = parts[2]
        targets = [str(repo_dir / rel) for rel in sorted(blobs)]
        # hash-object 一次喂全部路径（--stdin-paths），避免逐件起进程
        # --no-filters：blob id 是纯内容 id——上游原生 CRLF 件（如 g1 urdf）不带此
        # 旗会被全局 autocrlf 清洗 id 而假报失配（门测试首跑实测抓到）
        proc = subprocess.run(
            ["git", "-C", str(repo_dir), "hash-object", "--no-filters", "--stdin-paths"],
            input="\n".join(targets) + "\n", capture_output=True, text=True, check=True)
        ids = proc.stdout.split()
        bad = [blobs[rel] and rel for rel, oid in zip(sorted(blobs), ids)
               if blobs[rel] != oid]
        parity.append({"repo": cfg["name"], "files": len(blobs), "mismatch": bad})
        print(f"  blob-parity [{cfg['name']}]: {len(blobs)} 件，失配 {len(bad)}"
              + (f"：{bad[:5]}" if bad else ""))
    return parity


def verify_license(cfg_list):
    """A2：license 快照以 raw 内同 commit 文件为准复核，不一致则重生成并标记。"""
    results = []
    for cfg in cfg_list:
        raw_lic = RAW / cfg["name"] / cfg["license_path"]
        snap = MODEL_DIR / f"LICENSE-upstream-{cfg['name']}.txt"
        if not raw_lic.exists():
            results.append({"repo": cfg["name"], "status": "MISSING"})
            continue
        h_raw = sha256_file(raw_lic)
        if snap.exists() and sha256_file(snap) == h_raw:
            results.append({"repo": cfg["name"], "status": "MATCH", "sha256": h_raw})
        else:
            snap.write_bytes(raw_lic.read_bytes())
            results.append({"repo": cfg["name"], "status": "REGENERATED-FROM-RAW",
                            "sha256": h_raw})
    return results


def main():
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if RAW.exists():
        sys.exit(f"[拒绝] {RAW} 已存在——raw 只读原则，重拉请先手删该目录")
    RAW.mkdir(parents=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    summary = {"model": config["model"], "repos": [], "license": []}
    for cfg in config["sources"]:
        print(f"== {cfg['repo']} @ {cfg['pin'][:12]}（{cfg['note']}）")
        repo_dir = RAW / cfg["name"]
        try:
            head, method = clone_sparse(cfg["name"], cfg)
        except RuntimeError as exc:
            print(f"  部分克隆失败，转 API 兜底：{exc.splitlines()[0]}")
            if repo_dir.exists():
                shutil.rmtree(repo_dir)
            head, method = fetch_via_api(cfg["name"], cfg)
        files = [f for f in repo_dir.rglob("*") if f.is_file() and ".git" not in f.parts]
        size = sum(f.stat().st_size for f in files)
        print(f"  完成：HEAD={head[:12]} 方法={method} 文件 {len(files)} 个 / {size / 1e6:.1f} MB")
        summary["repos"].append({
            "repo": cfg["repo"], "pin": cfg["pin"], "resolved_head": head,
            "method": method, "files": len(files), "bytes": size,
        })

    n_files, total = write_manifest()
    lines = [l for l in (RAW / "manifest.sha256").read_text(encoding="utf-8").split("\n") if l.strip()]
    step = max(1, n_files // 3)
    sample = lines[::step][:3]
    ok = all(sha256_file(RAW / p) == h for h, p in (l.split("  ", 1) for l in sample))
    summary["manifest"] = {"files": n_files, "bytes": total, "sample3_ok": ok}
    summary["license"] = verify_license(config["sources"])
    summary["blob_parity"] = verify_blob_parity(config["sources"])
    if any(r["mismatch"] for r in summary["blob_parity"]):
        sys.exit("[阻塞] blob-parity 失配——检出件与上游 blob 不一致，K2 类缺陷进门被挡（重拉或按 cat-file 归正后重跑）")

    (REPORTS / "S1-fetch.md").write_text(
        "# S1 拉取记录（" + config["model"] + "）· " + time.strftime("%Y-%m-%d %H:%M") + "\n\n"
        "```json\n" + json.dumps(summary, ensure_ascii=False, indent=2) + "\n```\n",
        encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
