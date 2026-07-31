#!/usr/bin/env python3
"""Compact narration outline for a prepped V2 row.

Authoring a beat map means reading the whole narration and every audio window,
and beats.json is far too verbose to read straight (row 5 alone is ~40 KB of
JSON for ~2 minutes of narration). This prints the same information in the form
the beat map is actually written from: one line per timing phrase, with the
absolute audio window each phrase occupies.

    python3 media-production-v2/v2_outline.py 5
    python3 media-production-v2/v2_outline.py media-production-v2/build-05-bent-woman

Columns: seg + phrase index | absolute start-end | speaker | the words.
The absolute window is what a beat's "window" field must sit inside; splitting a
segment across several pictures means giving each picture the sub-window of the
phrases it covers.
"""
import json
import pathlib
import sys

V2 = pathlib.Path(__file__).resolve().parent
REVIEW_LESSONS = V2 / "REVIEW-LESSONS.json"


def find_build(arg: str) -> pathlib.Path:
    p = pathlib.Path(arg)
    if p.is_dir():
        return p
    if arg.isdigit():
        hits = sorted(V2.glob(f"build-{int(arg):02d}-*"))
        if hits:
            return hits[0]
    raise SystemExit(f"no build folder found for {arg!r}")


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    build = find_build(sys.argv[1])
    data = json.loads((build / "beats.json").read_text())

    print(f"row {data['row']}  {data['slug']}")
    print(f"constants: {data['constants']}")
    if REVIEW_LESSONS.is_file():
        lessons = json.loads(REVIEW_LESSONS.read_text())
        lesson = lessons.get(str(data["row"]))
        if lesson:
            state = "OPEN — MUST BE FIXED" if lesson["open"] else "RESOLVED — DO NOT REGRESS"
            print(f"prior reviewer lesson [{state}]: {lesson['latest']}")
    total = 0.0
    n_phrases = 0
    for b in data["beats"]:
        total = max(total, float(b["seg_end"]))
        start = float(b["audio_start"])
        head = f"{b['seg']:>6}  [{b['speaker']}]  v1 still: {b.get('v1_still')}"
        print()
        print(head)
        timing = b.get("timing") or []
        if not timing:
            print(f"    {start:7.2f}-{float(b['spoken_end']):7.2f}  {b.get('text', '')}")
            n_phrases += 1
            continue
        for i, t in enumerate(timing, 1):
            a = start + float(t["start"])
            z = start + float(t["end"])
            print(f"    {b['seg']} p{i}  {a:7.2f}-{z:7.2f}  {t['text']}")
            n_phrases += 1

    print()
    print(f"TOTAL runtime {total:.1f}s ({total/60:.1f} min) over {n_phrases} phrases")
    print("coverage law: ~15 pictures (10-20), scaled by runtime; narration decides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
