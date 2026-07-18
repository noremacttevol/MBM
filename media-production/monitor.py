#!/usr/bin/env python3
"""MBM approval monitor helper — the one place Cameron's approvals get recorded.

Approval is VERSION-LOCKED: it stores the git blob hash of the exact mp4 cut
Cameron approved. When a build machine rebuilds that video the hash changes, the
review page (gen_site_index.py) sees the mismatch, drops it out of Approved, and
puts it back in the review list flagged "NEW cut." So a rebuilt video can never
silently stay in the approved pile.

Usage (run from the repo root):
  python3 media-production/monitor.py approve 5 6 7
  python3 media-production/monitor.py unapprove 6
  python3 media-production/monitor.py list

Approvals are stored in media-production/approvals.json, written ONLY here so the
build machines never conflict on it. After running, regenerate + deploy the page:
  python3 media-production/gen_site_index.py && firebase deploy --only hosting
"""
import json
import os
import re
import subprocess
import sys
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPROVALS_FILE = os.path.join(REPO, "media-production", "approvals.json")
QUEUE = os.path.join(REPO, "media-production", "QUEUE.md")


def mp4_hashes():
    out = subprocess.run(
        ["git", "ls-tree", "-r", "HEAD", "--", "media-production"],
        cwd=REPO, capture_output=True, text=True).stdout
    hashes = {}
    for line in out.splitlines():
        try:
            meta, path = line.split("\t", 1)
            _, _typ, h = meta.split()
        except ValueError:
            continue
        m = re.match(r"media-production/build-(\d+)-.*/[0-9a-z]+-\d+_.*\.mp4$", path)
        if m:
            hashes[int(m.group(1))] = h
    return hashes


def load():
    try:
        with open(APPROVALS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}


def save(data):
    with open(APPROVALS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def set_appr_column(nums, tick):
    """Keep QUEUE.md's Appr column roughly in sync for the machines/humans."""
    with open(QUEUE, encoding="utf-8") as f:
        lines = f.readlines()
    in200 = False
    for i, line in enumerate(lines):
        if line.strip() == "## The 200":
            in200 = True
        p = line.split("|")
        if in200 and len(p) == 10 and re.match(r"^\s*\d+\s*$", p[1]):
            if int(p[1]) in nums and p[5].strip() == "✅":
                p[6] = " ✅ " if tick else " ⬜ "
                lines[i] = "|".join(p)
    with open(QUEUE, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    data = load()

    if cmd == "list":
        h = mp4_hashes()
        for k in sorted(data, key=int):
            cur = h.get(int(k))
            state = "OK" if cur == data[k]["hash"] else "CHANGED since approval"
            print(f"  #{k}: approved {data[k]['date']} — {state}")
        print(f"total approved: {len(data)}")
        return

    nums = [int(x) for x in sys.argv[2:] if x.isdigit()]
    if not nums:
        print("give one or more video numbers")
        return

    if cmd == "approve":
        h = mp4_hashes()
        today = date.today().isoformat()
        done, missing = [], []
        for n in nums:
            if n not in h:
                missing.append(n)
                continue
            data[str(n)] = {"hash": h[n], "date": today}
            done.append(n)
        save(data)
        set_appr_column(set(done), True)
        print(f"approved (version-locked): {done}")
        if missing:
            print(f"  no committed mp4 found for: {missing} (build/commit it first)")
    elif cmd == "unapprove":
        for n in nums:
            data.pop(str(n), None)
        save(data)
        set_appr_column(set(nums), False)
        print(f"unapproved: {nums}")
    else:
        print(f"unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
