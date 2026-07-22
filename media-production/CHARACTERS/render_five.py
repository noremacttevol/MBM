#!/usr/bin/env python3
"""render_five.py — render the outstanding apostle sheets, patiently.

The Flow browser profile is shared with the other Claude sessions on this
computer, so a job can sit in the lock queue for a long time behind a whole
video build. This driver therefore:
  * runs the characters one at a time, in order,
  * never hides an error (raw child output goes to the log),
  * retries a character whose sheet came out incomplete.

    python3 -u CHARACTERS/render_five.py philip bartholomew … > log 2>&1 &
"""
import subprocess
import sys
import time
from pathlib import Path

CH = Path(__file__).resolve().parent
VIEWS = ("face-front", "three-quarter", "full-body")


def done(slug):
    return all((CH / slug / f"{v}.jpeg").exists() for v in VIEWS)


def main():
    todo = sys.argv[1:]
    for slug in todo:
        for attempt in range(1, 6):
            if done(slug):
                break
            print(f"=== {slug}: attempt {attempt} "
                  f"({time.strftime('%H:%M:%S')})", flush=True)
            r = subprocess.run(
                ["python3", "-u", str(CH / "render_sheet.py"), slug],
                cwd=str(CH.parent), capture_output=True, text=True)
            for ln in (r.stdout + r.stderr).splitlines():
                if any(k in ln for k in ("saved", "done", "FAILED", "busy",
                                         "Error", "error", "Traceback")):
                    print(f"[{slug}] {ln.strip()}", flush=True)
            if done(slug):
                print(f"=== {slug}: SHEET COMPLETE", flush=True)
                break
        else:
            print(f"=== {slug}: GAVE UP after 5 attempts", flush=True)
    print("ALL REQUESTED SHEETS FINISHED", flush=True)


if __name__ == "__main__":
    main()
