#!/usr/bin/env python3
"""Render every build that has a validated plan, verify it, and log the result.

One bad build must never kill the run, so each is wrapped. A build is only
counted as rebuilt when the mp4's mtime actually advanced — a dark caption band
proves nothing, the old captions drew one too.
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import migrate  # noqa: E402
from deadair import measure  # noqa: E402

LOG = os.path.join(HERE, "batch-log.json")


def load_log():
    if os.path.exists(LOG):
        try:
            with open(LOG) as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_log(d):
    tmp = LOG + ".tmp"
    with open(tmp, "w") as f:
        json.dump(d, f, indent=1)
    os.replace(tmp, LOG)


def decode_errors(path):
    """Fully decode the mp4 and count errors.

    ffprobe reads duration straight out of the container header, so a file whose
    video stream is shredded still reports a plausible duration and sails past a
    metadata-only check. Two concurrent batch processes writing the same output
    did exactly that here — builds 101 and 102 reported OK while carrying 14025
    and 5505 decode errors. Nothing ships without a real decode.
    """
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "null", "-"],
                       capture_output=True, text=True)
    return len([ln for ln in r.stderr.splitlines() if ln.strip()])


def verify(build):
    """Post-render checks that would otherwise only surface on the review board."""
    d = os.path.join(migrate.MP, build)
    out = {}
    name = migrate.output_mp4(d)
    if not name:
        return {"ok": False, "why": "no mp4 to measure"}
    mp4 = os.path.join(d, name)
    m = measure(d, name)
    if not m:
        return {"ok": False, "why": f"could not measure {name}"}
    out.update(total=m["total"], trailing=m["trailing"], mp4=name)
    errs = decode_errors(mp4)
    out["decode_errors"] = errs
    if errs:
        return {"ok": False, "why": f"mp4 is corrupt — {errs} decode errors", **out}
    if m["trailing"] > 3.0:
        return {"ok": False, "why": f"trailing dead air {m['trailing']}s > 3.0s ceiling",
                **out}
    if m["total"] < 60.0:
        return {"ok": False, "why": f"runtime {m['total']}s under the 60s floor", **out}
    src = open(os.path.join(d, "build.py"), encoding="utf-8").read()
    if migrate.leftover_kjv(src):
        return {"ok": False, "why": "build.py still references the retired kjv flag",
                **out}
    out["ok"] = True
    return out


LOCK = os.path.join(HERE, ".batch.lock")


def acquire_lock():
    """Exactly one batch may run. Two concurrent batches rendering the same build
    interleave their writes to segs/ and to the output mp4 and silently corrupt
    it — that is how builds 101 and 102 shipped shredded. O_EXCL makes a second
    batch refuse to start instead of quietly destroying the first one's work."""
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        try:
            with open(LOCK) as f:
                who = f.read().strip()
        except Exception:
            who = "unknown"
        pid = who.split()[0] if who else ""
        if pid.isdigit() and not os.path.exists(f"/proc/{pid}"):
            print(f"stale lock from pid {pid}; taking over", flush=True)
            os.unlink(LOCK)
            return acquire_lock()
        raise SystemExit(f"another batch is already running ({who}). "
                         f"Refusing to start — concurrent batches corrupt mp4s.")
    os.write(fd, f"{os.getpid()} started".encode())
    os.close(fd)
    import atexit
    atexit.register(lambda: os.path.exists(LOCK) and os.unlink(LOCK))


def main():
    acquire_lock()
    names = sys.argv[1:]
    if not names:
        names = sorted(f[:-5] for f in os.listdir(os.path.join(HERE, "plans"))
                       if f.endswith(".json"))
    log = load_log()
    todo = [n for n in names if log.get(n, {}).get("status") != "shipped"]
    print(f"{len(todo)} to build ({len(names) - len(todo)} already done)", flush=True)

    for i, b in enumerate(todo, 1):
        t0 = time.time()
        print(f"\n[{i}/{len(todo)}] {b}", flush=True)
        try:
            migrate.migrate(b)
            v = verify(b)
            log[b] = {"status": "shipped" if v.get("ok") else "failed-verify",
                      "secs": round(time.time() - t0, 1), **v}
            print(f"    {'OK ' if v.get('ok') else 'FAIL'} "
                  f"total={v.get('total')}s trailing={v.get('trailing')}s "
                  f"{v.get('why','')}", flush=True)
        except KeyboardInterrupt:
            raise
        except BaseException as e:
            # BaseException, not Exception: a `raise SystemExit` inside migrate()
            # sails past `except Exception` and killed a 165-video run after 8
            # builds. One bad build must never stop the queue.
            log[b] = {"status": "error", "why": f"{type(e).__name__}: {e}"[:300],
                      "secs": round(time.time() - t0, 1)}
            print(f"    ERROR {type(e).__name__}: {str(e)[:200]}", flush=True)
        save_log(log)

    ok = sum(1 for v in log.values() if v.get("status") == "shipped")
    print(f"\n=== {ok} shipped, "
          f"{sum(1 for v in log.values() if v.get('status') != 'shipped')} not ===",
          flush=True)


if __name__ == "__main__":
    main()
