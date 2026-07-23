#!/usr/bin/env python3
"""ElevenLabs re-voice sweep — regenerate a video's narration on the new engine,
ear-check it, and (optionally) reassemble the mp4. See ELEVENLABS-SETUP.md.

For each selected build it runs, in the build's own folder:
  1. make_narration.py   -> regenerates audio/*.mp3 (routes through ElevenLabs
                            when eleven_config.json is set; edge-tts otherwise)
  2. qc_narration.py      -> whisper ear-check; nonzero exit = a segment failed
  3. build.py  (only with --build) -> reassemble the mp4 with the new audio

It NO-OPS with a clear message if ElevenLabs is not configured, so it can't
silently ship edge-tts audio while pretending it re-voiced.

Selection:
  --range 1-10        rows 1..10 (by build-folder number)
  --rows 5,18,140     explicit rows
  --all               every build folder
Flags:
  --build             also run build.py to reassemble the mp4
  --dry-run           list what would run, do nothing
  --force-edge        run even without a key (regenerate on edge-tts) — for
                      testing the harness only; NOT a re-voice

Claim law: this touches specific videos. Claim their QUEUE.md rows and push the
claim BEFORE running a real sweep (the kickoff's claim-first rule).
"""
import argparse
import glob
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Engine modules pushed into each build just before it runs, so a build's local
# copies never lag the canonical media-production/ versions during a sweep.
SYNC_MODULES = ["mbm_caption_timing.py", "mbm_eleven.py"]


def sync_modules(folder):
    for mod in SYNC_MODULES:
        src = os.path.join(HERE, mod)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(folder, mod))


def build_map():
    """{row_number: folder_path} from build-<N>-slug names."""
    out = {}
    for b in sorted(glob.glob(os.path.join(HERE, "build-*"))):
        if not os.path.isdir(b):
            continue
        m = re.match(r"build-(\d+)-", os.path.basename(b))
        if m:
            out.setdefault(int(m.group(1)), b)
    return out


def parse_selection(args, bmap):
    rows = []
    if args.all:
        rows = sorted(bmap)
    if args.range:
        m = re.match(r"(\d+)-(\d+)$", args.range)
        if not m:
            sys.exit(f"bad --range {args.range!r}; want e.g. 1-10")
        rows += [n for n in range(int(m.group(1)), int(m.group(2)) + 1) if n in bmap]
    if args.rows:
        for tok in args.rows.split(","):
            tok = tok.strip()
            if tok.isdigit() and int(tok) in bmap:
                rows.append(int(tok))
            elif tok:
                print(f"  (skip {tok!r}: no build folder)")
    # de-dup, keep order
    seen, ordered = set(), []
    for n in rows:
        if n not in seen:
            seen.add(n)
            ordered.append(n)
    return ordered


def run(folder, script, dry):
    if not os.path.exists(os.path.join(folder, script)):
        return None  # build has no such script
    if dry:
        print(f"    would run: {script}")
        return 0
    r = subprocess.run([sys.executable, script], cwd=folder)
    return r.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--range")
    ap.add_argument("--rows")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force-edge", action="store_true")
    args = ap.parse_args()

    # Readiness gate.
    sys.path.insert(0, HERE)
    try:
        import mbm_eleven
        configured = mbm_eleven.is_configured()
    except Exception as e:                                  # pragma: no cover
        print(f"ElevenLabs adapter not importable: {e}")
        configured = False
    if not configured and not args.force_edge:
        print("ElevenLabs is NOT configured — nothing to re-voice.\n")
        print(mbm_eleven.check() if "mbm_eleven" in sys.modules else
              "eleven_config.json missing")
        print("\nFill api_key + voices in eleven_config.json, then re-run.")
        print("(Or pass --force-edge to exercise the harness on edge-tts.)")
        return
    engine = "ElevenLabs" if configured else "edge-tts (FORCED — not a re-voice)"

    bmap = build_map()
    rows = parse_selection(args, bmap)
    if not rows:
        sys.exit("no rows selected — use --range / --rows / --all")

    print(f"Engine: {engine}")
    print(f"Sweeping {len(rows)} video(s): {rows}\n")
    passed, failed, qc_fail = [], [], []
    for n in rows:
        folder = bmap[n]
        print(f"#{n}  {os.path.basename(folder)}")
        if not args.dry_run:
            sync_modules(folder)  # ensure current engine code in this build
        rc = run(folder, "make_narration.py", args.dry_run)
        if rc is None:
            print("    ! no make_narration.py — skipped")
            failed.append(n)
            continue
        if rc != 0:
            print(f"    ! narration generation FAILED (rc={rc})")
            failed.append(n)
            continue
        qc = run(folder, "qc_narration.py", args.dry_run)
        if qc not in (0, None):
            print(f"    ! ear-check FAILED (rc={qc}) — fix before shipping")
            qc_fail.append(n)
            continue
        if args.build:
            rb = run(folder, "build.py", args.dry_run)
            if rb not in (0, None):
                print(f"    ! build.py FAILED (rc={rb})")
                failed.append(n)
                continue
        print("    ok")
        passed.append(n)

    print(f"\n=== sweep done ===\n  passed:   {passed}")
    print(f"  ear-check fails: {qc_fail}")
    print(f"  errors:   {failed}")
    if qc_fail or failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
