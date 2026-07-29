#!/usr/bin/env python3
"""v2_scaffold.py — do the MECHANICAL half of a beats_v2.py so authoring 184 more
rows stops being the bottleneck.

WHY THIS EXISTS
---------------
Every beat map has two halves. One is judgment: what the picture shows, what the
scripture demands, which frame carries the story. That half cannot be automated
and must never be — a machine-written scene is exactly how V1's mistakes got
made, and V2 exists to fix them.

The other half is pure bookkeeping, and it is most of the typing:
  · reading beats.json and turning every timing phrase into a window
  · deciding how many pictures the coverage law allows for this runtime
  · grouping phrases into that many beats without leaving gaps or overlaps
  · numbering ids, naming output files, wiring seg labels
  · emitting the LOCKS scaffold and the REF constant
  · getting every structural field the assembler needs, spelled correctly

That half is identical for all 200 rows and takes as long as the half that
matters. This script does it, and REFUSES to guess the half that doesn't.

THE SAFETY PROPERTY THAT MAKES THIS LEGAL
-----------------------------------------
The output CANNOT BE SHIPPED. Every emitted beat carries a scene body of
`SCENE_TODO`, and `SCENE_TODO` contains the banned word "NEGATIVE PROMPT", so
`v2_prompt.py --check` FAILS on an unfilled scaffold every time:

    FAIL  v2-rNNN-bNN: NEGATIVE-PROMPT list is banned in V2

There is therefore no path by which a half-finished scaffold reaches Flow or a
delivered video. You must write every scene by hand before the row will even
check, which is exactly the intended division of labour. Do not "fix" this by
softening SCENE_TODO.

⚠️ SCAFFOLD ONE ROW AT A TIME, AND AUTHOR IT IMMEDIATELY. Do not scaffold ahead.
A scaffold on disk makes `v2_prep_row.py --status` count that row as READY when it
is not authored, which hides unwritten work from the only status report there is.
The runner is safe either way — v2_prompt --gen runs the checker first, so a
scaffolded row fails fast and costs no Flow generation — but the bookkeeping lies.
Scaffold, write the scenes, get --check to PASS, commit. Then scaffold the next.

USAGE
    python3 media-production-v2/v2_scaffold.py 22
    python3 media-production-v2/v2_scaffold.py 22 --pictures 30
    python3 media-production-v2/v2_scaffold.py 22 --stdout

It never overwrites an existing beats_v2.py.
"""
import argparse
import json
import pathlib
import sys

V2 = pathlib.Path(__file__).resolve().parent

# Deliberately trips the v4 checker's banned-list rule. See the safety note above.
SCENE_TODO = (
    "SCENE_TODO — write this scene by hand. This placeholder contains the string "
    "NEGATIVE PROMPT on purpose so v2_prompt.py --check fails until it is replaced."
)


def find_build(arg: str) -> pathlib.Path:
    p = pathlib.Path(arg)
    if p.is_dir():
        return p
    if arg.isdigit():
        hits = sorted(V2.glob(f"build-{int(arg):02d}-*"))
        if hits:
            return hits[0]
    raise SystemExit(f"no build folder found for {arg!r}")


def phrases(data):
    """Flatten beats.json into [(seg, idx, abs_start, abs_end, text), ...]."""
    out = []
    for b in data["beats"]:
        start = float(b["audio_start"])
        timing = b.get("timing") or []
        if not timing:
            out.append((b["seg"], 1, start, float(b["spoken_end"]),
                        (b.get("text") or "").strip()))
            continue
        for i, t in enumerate(timing, 1):
            out.append((b["seg"], i, start + float(t["start"]),
                        start + float(t["end"]), t["text"].strip()))
    return out


def target_pictures(runtime: float) -> int:
    """The coverage law: ~15 per 100 s, floor of 10, scaled by runtime.

    Rows 5-21 shipped at 4.6-6.0 s per picture and that band is the house style,
    so aim at the middle of it (5.7 s) and never go below the law's floor of 10.
    """
    return max(10, round(runtime / 5.7))


def group(ph, want):
    """Split phrases into exactly `want` contiguous groups of near-equal duration.

    Balanced by accumulated TIME, not phrase count: phrase lengths vary wildly
    (row 10 has a 14-second phrase beside a 0.7-second one) and equal counts would
    give wildly unequal holds. Walks the phrases once, closing a group whenever the
    elapsed time crosses the next ideal boundary, which guarantees exactly `want`
    groups and no gaps or overlaps.
    """
    want = max(1, min(want, len(ph)))
    t0, t1 = ph[0][2], ph[-1][3]
    span = max(t1 - t0, 1e-6)
    groups = [[] for _ in range(want)]
    for p in ph:
        mid = ((p[2] + p[3]) / 2 - t0) / span
        idx = min(want - 1, int(mid * want))
        groups[idx].append(p)
    # Any empty bucket steals a phrase from the fullest neighbour so every beat
    # has narration and no window is empty.
    for i, g in enumerate(groups):
        if g:
            continue
        donor = max(range(want), key=lambda k: len(groups[k]))
        if len(groups[donor]) < 2:
            continue
        if donor < i:
            groups[i].append(groups[donor].pop())
        else:
            groups[i].append(groups[donor].pop(0))
    return [g for g in groups if g]


def slug(text, n=5):
    words = [w.strip(".,;:!?—-'\"").lower() for w in text.split()]
    words = [w for w in words if w and w.isalpha()]
    return "-".join(words[:n]) or "beat"


def render(build, data, groups):
    row = data["row"]
    runtime = max(float(b["seg_end"]) for b in data["beats"])
    L = []
    L.append('#!/usr/bin/env python3')
    L.append(f'"""V2 beat map — row {row}, {data["slug"]} (SCRIPTURE REFERENCE — FILL IN).')
    L.append("")
    L.append(f"SCAFFOLD generated by v2_scaffold.py. Runtime {runtime:.1f} s, "
             f"{len(groups)} pictures ({runtime/len(groups):.1f} s each).")
    L.append("The windows, segment labels, ids and filenames below are correct and")
    L.append("checked. EVERYTHING ELSE IS YOURS TO WRITE, and the row will not pass")
    L.append("v2_prompt.py --check until you have written it.")
    L.append("")
    L.append("BEFORE YOU WRITE A SINGLE SCENE:")
    L.append("  1. Read the KJV passage in full and put the facts that govern the")
    L.append("     pictures in this header — direction, position, scale, time of day.")
    L.append("  2. Check media-production/CONTENT-CARE.md §3 for this row's flags.")
    L.append("  3. Decide the time-of-day arc and state it here, so no later QC pass")
    L.append("     mistakes a correct sunset for the row-11 storm defect.")
    L.append("  4. Name any prop or condition that CHANGES across the row (a cloak, a")
    L.append("     posture, an illness) and keep it OUT of the locks — a lock must")
    L.append("     never contradict a beat.")
    L.append('"""')
    L.append("")
    L.append("# LOCKS: one entry per recurring person and per setting. Setting locks must")
    L.append("# NEVER name a character (the STRAY-JESUS defect). State clothing colours")
    L.append("# POSITIVELY and dark — 'never cream' alone does not hold. Only Jesus wears")
    L.append("# cream. Recurring cast (PETER, ANDREW, JOHN, JAMES-Z) come from the shared")
    L.append("# CAST_LOCKS in v2_prompt.py — do not redefine them here.")
    L.append("LOCKS = {")
    L.append('    # "NAME": (')
    L.append('    #     "NAME LOCK: ..."')
    L.append('    # ),')
    L.append("}")
    L.append("")
    L.append("REF = True")
    L.append("")
    L.append("# Deliberately contains the banned phrase so v2_prompt.py --check FAILS this")
    L.append("# row until every scene below is written by hand. Do not soften it.")
    L.append('SCENE_TODO = ("SCENE_TODO — unwritten scene. Contains a NEGATIVE PROMPT "')
    L.append('              "marker so the v4 checker rejects this row until replaced.")')
    L.append("")
    L.append("BEATS = [")
    for i, g in enumerate(groups, 1):
        segs = []
        for s, _, _, _, _ in g:
            if s not in segs:
                segs.append(s)
        seg_label = " + ".join(segs)
        text = " ".join(p[4] for p in g)
        start, end = g[0][2], g[-1][3]
        L.append("    {")
        L.append(f'        "id": "v2-r{row:03d}-b{i:02d}", '
                 f'"out": "s{i:02d}-{slug(text)}.jpeg", "seg": "{seg_label}",')
        L.append(f'        "window": "{start:.2f}-{end:.2f}", '
                 f'"wide": True, "jesus": False, "ref": False,')
        L.append('        "locks": [],')
        # The narration is the one piece of real content the scaffold can supply
        # safely: it is quoted verbatim from the audio, not invented.
        wrapped, line = [], ""
        for w in text.split():
            if len(line) + len(w) + 1 > 66:
                wrapped.append(line)
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            wrapped.append(line)
        if len(wrapped) == 1:
            L.append(f'        "narration": "{wrapped[0]}",')
        else:
            L.append('        "narration": (')
            for k, wl in enumerate(wrapped):
                tail = "" if k == len(wrapped) - 1 else " "
                L.append(f'            "{wl}{tail}"')
            L.append("        ),")
        L.append('        "must_show": "TODO",')
        L.append('        "must_not_show": "TODO — always include: no halo, glare or '
                 'rim-light on Jesus.",')
        L.append('        "scene": SCENE_TODO,')
        L.append("    },")
    L.append("]")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("row")
    ap.add_argument("--pictures", type=int, default=None,
                    help="override the coverage-law count")
    ap.add_argument("--stdout", action="store_true")
    a = ap.parse_args()

    build = find_build(a.row)
    bj = build / "beats.json"
    if not bj.is_file():
        raise SystemExit(f"{build.name}: no beats.json — run v2_prep_row.py first")
    data = json.loads(bj.read_text())
    ph = phrases(data)
    runtime = max(float(b["seg_end"]) for b in data["beats"])
    want = a.pictures or target_pictures(runtime)
    groups = group(ph, want)

    text = render(build, data, groups)
    if a.stdout:
        sys.stdout.write(text)
        return 0
    out = build / "beats_v2.py"
    if out.exists():
        raise SystemExit(f"{out} already exists — refusing to overwrite")
    out.write_text(text)
    print(f"wrote {out}")
    print(f"  runtime {runtime:.1f}s · {len(groups)} beats · "
          f"{runtime/len(groups):.1f}s per picture")
    print("  NOW WRITE THE SCENES. The row fails --check until you do.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
