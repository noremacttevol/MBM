#!/usr/bin/env python3
"""Ship rebuilt videos to the review board as they land, in batches.

Cameron approves continuously, so a finished video must not sit on disk waiting
for the whole run. This watches batch-log.json and, every SHIP_EVERY newly
verified builds, commits those specific paths, pushes, regenerates the site index
and deploys.

Deliberate constraints:
  * stages EXPLICIT paths only — never `git add -A`. Four machines share this
    clone and an -A would sweep up another session's work.
  * never touches approvals.json, COMPLAINTS.md or QUEUE.md. Those are Cameron's.
  * a push rejection means another machine got there first: pull --rebase and
    retry rather than forcing.
  * a git push does NOT update the board. gen_site_index.py + firebase deploy do.
    If the deploy 429s, prune_hosting_versions.py runs and the deploy is retried.
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
MP = os.path.dirname(HERE)
REPO = os.path.dirname(MP)
LOG = os.path.join(HERE, "batch-log.json")
STATE = os.path.join(HERE, "shipped-to-board.json")
LOCK = os.path.join(HERE, ".ship.lock")
SHIP_EVERY = 20
POLL = 90


def run(cmd, cwd=REPO, timeout=1800, check=False):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    if check and r.returncode:
        raise RuntimeError(f"{' '.join(cmd[:4])} -> {r.returncode}\n{r.stderr[-800:]}")
    return r


def verified():
    try:
        with open(LOG) as f:
            d = json.load(f)
    except Exception:
        return []
    return sorted(k for k, v in d.items() if v.get("status") == "shipped")


def already():
    if os.path.exists(STATE):
        try:
            with open(STATE) as f:
                return set(json.load(f))
        except Exception:
            pass
    return set()


def remember(s):
    tmp = STATE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(sorted(s), f, indent=1)
    os.replace(tmp, STATE)


def push_with_rebase(tries=4):
    for i in range(tries):
        r = run(["git", "push", "origin", "main"], timeout=3600)
        if r.returncode == 0:
            return True
        print(f"  push rejected ({i+1}/{tries}); pulling --rebase", flush=True)
        run(["git", "pull", "--rebase", "origin", "main"], timeout=1800)
    return False


def deploy():
    r = run(["npx", "firebase", "deploy", "--only", "hosting"], timeout=1800)
    if r.returncode == 0:
        return True
    if "429" in (r.stdout + r.stderr) or "quota" in (r.stdout + r.stderr).lower():
        print("  deploy 429 — pruning hosting versions and retrying", flush=True)
        run([sys.executable, os.path.join(MP, "prune_hosting_versions.py")],
            timeout=1800)
        r = run(["npx", "firebase", "deploy", "--only", "hosting"], timeout=1800)
        return r.returncode == 0
    print(f"  deploy failed: {(r.stderr or r.stdout)[-400:]}", flush=True)
    return False


def ship(batch):
    paths = [f"media-production/{b}" for b in batch]
    run(["git", "add"] + paths, check=True)
    msg = (f"SPEAKER LAW: {len(batch)} more rebuilt videos verified and shipped\n\n"
           + "\n".join(f"  {b}" for b in batch)
           + "\n\nEach decodes clean, ends 1.5s after the last spoken word, and its\n"
             "mp4 mtime advanced. Speaker colours drive both voice and caption.\n\n"
             "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>\n")
    r = subprocess.run(["git", "commit", "-F", "-"], cwd=REPO, input=msg,
                       capture_output=True, text=True)
    if r.returncode and "nothing to commit" not in (r.stdout + r.stderr):
        print(f"  commit failed: {(r.stderr or r.stdout)[-300:]}", flush=True)
        return False
    if not push_with_rebase():
        print("  PUSH FAILED — leaving for the next round", flush=True)
        return False
    run([sys.executable, os.path.join(MP, "gen_site_index.py")], timeout=900)
    run(["git", "add", "site/review.html"])
    subprocess.run(["git", "commit", "-m",
                    f"review board: regenerate for {len(batch)} more rebuilds"],
                   cwd=REPO, capture_output=True, text=True)
    push_with_rebase()
    ok = deploy()
    print(f"  shipped {len(batch)}; board {'updated' if ok else 'NOT updated'}",
          flush=True)
    return True


def main():
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
    except FileExistsError:
        raise SystemExit("a ship loop is already running")
    import atexit
    atexit.register(lambda: os.path.exists(LOCK) and os.unlink(LOCK))

    sent = already()
    idle = 0
    while True:
        pending = [b for b in verified() if b not in sent]
        batch_running = any(
            l.split()[:2] == ["python3", "run_batch.py"]
            for l in subprocess.run(["ps", "-eo", "cmd"], capture_output=True,
                                    text=True).stdout.splitlines())
        if len(pending) >= SHIP_EVERY or (pending and not batch_running):
            print(f"shipping {len(pending)} (batch running: {batch_running})",
                  flush=True)
            if ship(pending):
                sent |= set(pending)
                remember(sent)
            idle = 0
        elif not batch_running:
            idle += 1
            if idle > 3:
                print("batch finished and nothing left to ship — done", flush=True)
                return
        time.sleep(POLL)


if __name__ == "__main__":
    main()
