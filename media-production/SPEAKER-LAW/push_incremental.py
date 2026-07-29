#!/usr/bin/env python3
"""Push the backlog one commit at a time.

A single `git push` of the whole backlog keeps dying with
"send-pack: unexpected disconnect while reading sideband packet" — the repo is
~38 GiB and each rebuilt video adds a fresh ~20 MB blob, so one push can be
gigabytes over a home uplink. Pushing commit-by-commit keeps each transfer small
enough to finish, and a drop costs one commit instead of the whole run.

Never rebases and never touches the working tree, so it cannot disturb a render
in progress.
"""
import os
import subprocess
import sys
import time

REPO = os.path.expanduser("~/Desktop/MBM")


def git(*args, timeout=5400):
    return subprocess.run(["git"] + list(args), cwd=REPO,
                          capture_output=True, text=True, timeout=timeout)


def pending():
    r = git("log", "origin/main..HEAD", "--format=%H", "--reverse")
    return [l.strip() for l in r.stdout.splitlines() if l.strip()]


def main():
    # a bigger buffer makes each transfer less likely to be cut mid-sideband
    git("config", "http.postBuffer", "524288000")
    todo = pending()
    print(f"{len(todo)} commits to push", flush=True)
    for i, sha in enumerate(todo, 1):
        subj = git("log", "-1", "--format=%s", sha).stdout.strip()[:70]
        for attempt in (1, 2, 3):
            r = git("push", "origin", f"{sha}:main")
            if r.returncode == 0:
                print(f"[{i}/{len(todo)}] pushed {sha[:8]} {subj}", flush=True)
                break
            err = (r.stderr or r.stdout).strip().splitlines()
            print(f"[{i}/{len(todo)}] attempt {attempt} failed: "
                  f"{err[-1][:90] if err else '?'}", flush=True)
            if "non-fast-forward" in (r.stderr + r.stdout):
                print("  another machine moved main — stopping, needs a human",
                      flush=True)
                return 1
            time.sleep(15)
        else:
            print(f"  giving up on {sha[:8]} after 3 attempts", flush=True)
            return 1
    print("backlog pushed", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
