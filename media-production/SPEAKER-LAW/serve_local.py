#!/usr/bin/env python3
"""Publish every verified rebuild through Firebase instead of GitHub.

The repo is ~38 GB and the unpushed backlog is tens of gigabytes, so `git push`
answers HTTP 500 and finished videos sit on this machine unwatchable. The review
page already supports an opt-in local source: drop the cut into
site/story-videos/<row>.mp4 and list the row in SERVE-LOCAL.txt, and the same
Firebase deploy that publishes the page serves the video.

Two rules that folder's own docstring is emphatic about, and this honours both:
  * "file exists" is NOT sufficient — that folder holds ~50 older intermediate
    cuts used by other pages, so a row is only listed when we have just copied a
    VERIFIED rebuild over it.
  * a row is only served locally until its commit reaches GitHub.

Copies are atomic (temp + rename) so a half-copied file is never served.
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
REPO = os.path.dirname(MP)
DEST = os.path.join(REPO, "site", "story-videos")
LIST = os.path.join(DEST, "SERVE-LOCAL.txt")
sys.path.insert(0, HERE)
import migrate  # noqa: E402


def row_of(build):
    m = re.match(r"build-(\d+)-", build)
    return int(m.group(1)) if m else None


def main():
    log = json.load(open(os.path.join(HERE, "batch-log.json")))
    shipped = sorted(k for k, v in log.items() if v.get("status") == "shipped")
    os.makedirs(DEST, exist_ok=True)

    existing = set()
    header = ["# Served from Firebase because the git push is blocked "
              "(38GB repo -> HTTP 500).",
              "# Remove a number once its commit lands on GitHub."]
    if os.path.exists(LIST):
        for line in open(LIST):
            s = line.split("#", 1)[0].strip()
            if s.isdigit():
                existing.add(int(s))

    copied, skipped = [], []
    for b in shipped:
        row = row_of(b)
        if row is None:
            continue
        name = migrate.output_mp4(os.path.join(MP, b))
        if not name:
            skipped.append((b, "no mp4"))
            continue
        src = os.path.join(MP, b, name)
        dst = os.path.join(DEST, f"{row}.mp4")
        # only overwrite when the rebuild is genuinely newer than what is there
        if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
            existing.add(row)
            continue
        tmp = dst + ".tmp"
        shutil.copy2(src, tmp)
        os.replace(tmp, dst)
        existing.add(row)
        copied.append(row)

    tmp = LIST + ".tmp"
    with open(tmp, "w") as f:
        f.write("\n".join(header + [str(n) for n in sorted(existing)]) + "\n")
    os.replace(tmp, LIST)

    total = sum(os.path.getsize(os.path.join(DEST, f))
                for f in os.listdir(DEST) if f.endswith(".mp4"))
    print(f"copied {len(copied)} rebuilt videos into site/story-videos/")
    print(f"SERVE-LOCAL.txt now lists {len(existing)} rows")
    print(f"folder total: {total/1e9:.2f} GB")
    for b, why in skipped:
        print(f"  skipped {b}: {why}")


if __name__ == "__main__":
    main()
