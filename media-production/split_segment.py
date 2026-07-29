#!/usr/bin/env python3
"""split_segment.py — split one narration segment's EXISTING audio into two, at a
real sentence gap, so a new coverage still can take the second half of a long hold.

Why this exists (assembly lane, 2026-07-29): the coverage-stills law adds art to
long single-beat holds, but an OLD-format build.py can only show one still per
segment. Re-running TTS would change an already ear-checked narration; cutting the
approved mp3 at a sentence boundary keeps the voice byte-identical on both sides.

It NEVER touches make_narration.py or build.py — it prints the exact SEGMENTS lines
and BEATS row the caller must paste in, because those edits carry judgment
(which sentence the new picture illustrates) and must be reviewed by the person
doing the wiring.

Usage, from inside media-production/:
  python3 split_segment.py --dir build-07-peter-water --seg n0 --after 2
  python3 split_segment.py --dir build-07-peter-water --seg n0        # auto: cut nearest the middle

--after K cuts after the K-th sentence (1-based) of audio/<seg>.timing.json.
Writes audio/<seg>b.mp3 (+ .timing.json, + .words.json if present), rewrites the
first half in place, and verifies the two halves' durations sum to the original.
Refuses to run if <seg>b already exists in the build's audio/ folder.
"""
import argparse
import json
import os
import subprocess
import sys

FF = "ffmpeg"


def dur_of(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--seg", required=True)
    ap.add_argument("--after", type=int, default=0,
                    help="cut after this sentence number (1-based); 0 = auto")
    ap.add_argument("--new", default="",
                    help="name of the new second-half segment (default <seg>b)")
    args = ap.parse_args()

    a = os.path.join(args.dir, "audio")
    seg, new = args.seg, (args.new or args.seg + "b")
    mp3 = os.path.join(a, f"{seg}.mp3")
    tj = os.path.join(a, f"{seg}.timing.json")
    if not os.path.exists(mp3) or not os.path.exists(tj):
        sys.exit(f"missing {mp3} or {tj}")
    if os.path.exists(os.path.join(a, f"{new}.mp3")):
        sys.exit(f"{new}.mp3 already exists — pick another name with --new")

    sent = json.load(open(tj))
    if len(sent) < 2:
        sys.exit(f"{seg} has only {len(sent)} sentence(s) — nothing to split at")

    total = dur_of(mp3)
    if args.after:
        k = args.after
        if not 1 <= k < len(sent):
            sys.exit(f"--after must be 1..{len(sent) - 1}")
    else:
        # auto: the sentence boundary nearest the middle of the spoken audio
        k = min(range(1, len(sent)),
                key=lambda i: abs((sent[i - 1]["end"] + sent[i]["start"]) / 2
                                  - total / 2))
    cut = (sent[k - 1]["end"] + sent[k]["start"]) / 2

    # cut the mp3: first half in place (via temp), second half to <new>.mp3.
    # Re-encode (edge-tts mp3s are 24 kHz mono); a copy-cut can only land on
    # frame boundaries and would smear the cut point.
    tmp = os.path.join(a, f"_{seg}.split1.mp3")
    subprocess.run([FF, "-y", "-v", "error", "-i", mp3, "-t", f"{cut:.3f}",
                    "-c:a", "libmp3lame", "-q:a", "2", tmp], check=True)
    subprocess.run([FF, "-y", "-v", "error", "-i", mp3, "-ss", f"{cut:.3f}",
                    "-c:a", "libmp3lame", "-q:a", "2",
                    os.path.join(a, f"{new}.mp3")], check=True)
    os.replace(tmp, mp3)

    # split the sidecars, rebasing the second half to its new zero
    first, second = sent[:k], sent[k:]
    json.dump(first, open(tj, "w"), indent=1)
    json.dump([{**s, "start": round(s["start"] - cut, 3),
                "end": round(s["end"] - cut, 3)} for s in second],
              open(os.path.join(a, f"{new}.timing.json"), "w"), indent=1)
    wj = os.path.join(a, f"{seg}.mp3.words.json")
    if os.path.exists(wj):
        words = json.load(open(wj))
        json.dump([w for w in words if w[2] <= cut + 1e-6], open(wj, "w"))
        json.dump([[w[0], round(w[1] - cut, 3), round(w[2] - cut, 3)]
                   for w in words if w[1] >= cut - 1e-6],
                  open(os.path.join(a, f"{new}.mp3.words.json"), "w"))

    d1 = dur_of(mp3)
    d2 = dur_of(os.path.join(a, f"{new}.mp3"))
    if abs((d1 + d2) - total) > 0.25:
        sys.exit(f"DURATION MISMATCH: {d1:.2f}+{d2:.2f} != {total:.2f} — do not ship")

    t1 = " ".join(s["text"] for s in first)
    t2 = " ".join(s["text"] for s in second)
    print(f"OK  cut {seg} at {cut:.2f}s of {total:.2f}s -> {seg} ({d1:.2f}s) + {new} ({d2:.2f}s)")
    print("\nNow paste into make_narration.py SEGMENTS (replacing the old "
          f"{seg} line, same speaker):")
    print(f'    ("{seg}", <SPEAKER>, {json.dumps(t1)}),')
    print(f'    ("{new}", <SPEAKER>, {json.dumps(t2)}),')
    print(f'\n...and add ("{new}", <NEW-STILL>, "in"/"out") right after {seg} in BEATS.')


if __name__ == "__main__":
    main()
