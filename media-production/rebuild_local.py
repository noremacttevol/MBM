#!/usr/bin/env python3
"""Safely rebuild canonical MBM videos without git, publishing, or deployment.

The previous unattended shell loop mutated git and the review board.  This runner
does one job only: run each canonical build locally, preserve the previous MP4 if
the render fails, verify the replacement, and write a content-hash receipt.
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass

from corpus import canonical_builds, find_main_mp4
from render_receipt import record


HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
VERIFY = os.path.join(REPO, "admin", "verify-mp4.sh")
LOG_DIR = "/tmp/mbm-local-rebuild-logs"


@dataclass(frozen=True)
class Result:
    row: int
    build: str
    ok: bool
    detail: str


def rebuild(row: int, build_dir: str, timeout: int) -> Result:
    name = os.path.basename(build_dir)
    os.makedirs(LOG_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"{row:03d}-{name}.log")
    before = find_main_mp4(build_dir)
    backup = os.path.join(build_dir, ".mbm-final-backup.mp4")
    if os.path.exists(backup):
        os.remove(backup)
    if before:
        shutil.copy2(before, backup)
    try:
        with open(log_path, "w", encoding="utf-8") as log:
            process = subprocess.run(
                [sys.executable, "build.py"],
                cwd=build_dir,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=timeout,
            )
        after = find_main_mp4(build_dir)
        if process.returncode != 0 or not after:
            raise RuntimeError(f"build.py exit {process.returncode}")
        checked = subprocess.run(
            ["bash", VERIFY, after],
            capture_output=True,
            text=True,
        )
        if checked.returncode != 0:
            raise RuntimeError(
                checked.stdout.strip() or checked.stderr.strip() or "verify-mp4 failed"
            )
        record(build_dir, after)
        if os.path.exists(backup):
            os.remove(backup)
        size_mb = os.path.getsize(after) / 1_000_000
        return Result(row, name, True, f"{os.path.basename(after)} {size_mb:.1f} MB")
    except Exception as exc:
        if os.path.exists(backup):
            target = before or find_main_mp4(build_dir)
            if target:
                os.replace(backup, target)
        return Result(row, name, False, f"{exc}; log={log_path}")
    finally:
        if os.path.exists(backup):
            os.remove(backup)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rows", nargs="*", type=int)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()

    builds = canonical_builds(HERE)
    if args.all:
        selected = sorted(builds)
    elif args.rows:
        selected = sorted(set(args.rows))
    else:
        parser.error("provide row numbers or --all")
    missing = [row for row in selected if row not in builds]
    if missing:
        print("missing canonical builds: " + ",".join(map(str, missing)))
        return 2

    print(
        f"local-only rebuild: {len(selected)} canonical video(s), "
        f"workers={args.workers}, logs={LOG_DIR}",
        flush=True,
    )
    ok = failed = 0
    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {
            pool.submit(rebuild, row, builds[row], args.timeout): row
            for row in selected
        }
        for job in futures.as_completed(jobs):
            result = job.result()
            label = "OK" if result.ok else "FAIL"
            print(
                f"{label:4} #{result.row:03d} {result.build}: {result.detail}",
                flush=True,
            )
            ok += result.ok
            failed += not result.ok
    print(f"\nrebuild complete: OK={ok} FAIL={failed}", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
