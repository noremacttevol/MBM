#!/usr/bin/env python3
"""Mechanically check a speaker plan before it is allowed anywhere near a render.

Catches the failure classes that actually cost time on this project: dropped
segment ids that orphan the music beds, beats pointing at stills that do not
exist, non-narrator lines written in modern English instead of verbatim KJV, and
Old Testament passages still marked `jesus`.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPEAKERS = {"narrator", "jesus", "god", "scripture", "woman"}

OT_BOOKS = {"Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua",
            "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings",
            "Job", "Psalm", "Psalms", "Proverbs", "Ecclesiastes", "Isaiah",
            "Jeremiah", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Jonah",
            "Micah", "Habakkuk", "Zechariah", "Malachi"}
EPISTLES = {"Romans", "1 Corinthians", "2 Corinthians", "Galatians",
            "Ephesians", "Philippians", "Colossians", "1 Thessalonians",
            "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Hebrews",
            "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John"}

# Outside the Gospels, a red-letter KJV still inks Christ's own words in these
# places. Everything else in an epistle or in Acts is the writer.
RED_LETTER_EPISTLE = {
    "Acts": [(9, 4, 6), (18, 9, 10), (22, 7, 8), (22, 18, 21), (23, 11), (26, 14, 18)],
    "1 Corinthians": [(11, 24, 25)],          # "Take, eat: this is my body"
    "2 Corinthians": [(12, 9)],               # "My grace is sufficient for thee"
    "Revelation": [(1, 8), (1, 11), (1, 17, 20), (2, 1, 29), (3, 1, 22),
                   (16, 15), (22, 7), (22, 12, 16), (22, 20)],
}


def red_lettered_epistle(verse):
    """Does a red-letter KJV ink this epistle/Acts reference? `verse` like 'Acts 9:4'."""
    m = re.match(r"^\s*((?:[1-3]\s)?[A-Za-z]+)\s+(\d+):(\d+)", verse or "")
    if not m:
        return False
    book, ch, v = m.group(1), int(m.group(2)), int(m.group(3))
    for rng in RED_LETTER_EPISTLE.get(book, []):
        if rng[0] != ch:
            continue
        lo = rng[1]
        hi = rng[2] if len(rng) > 2 else rng[1]
        if lo <= v <= hi:
            return True
    return False


ARCHAIC = re.compile(
    r"\b(thou|thee|thy|thine|ye|hath|doth|saith|spake|unto|shalt|wilt|art|"
    r"cometh|giveth|verily|behold|shew|whither|wherefore|peradventure|"
    r"beseech|goeth|maketh|liveth|knoweth|hearken|nay|yea)\b", re.I)


def check(plan, brief):
    errs, warns = [], []
    b = plan.get("build")

    seg_ids = [s["id"] for s in plan.get("segments", [])]
    if len(seg_ids) != len(set(seg_ids)):
        dupes = {i for i in seg_ids if seg_ids.count(i) > 1}
        errs.append(f"duplicate segment ids: {sorted(dupes)}")

    # 1. original ids preserved — dropping one orphans start_of[]/music beds
    old = {s["id"] for s in brief["segments"]}
    dropped = sorted(old - set(seg_ids))
    if dropped:
        errs.append(f"dropped original segment id(s) {dropped} — keep them and ADD new ones")

    # 2. speakers valid
    for s in plan.get("segments", []):
        if s.get("speaker") not in SPEAKERS:
            errs.append(f"{s.get('id')}: bad speaker {s.get('speaker')!r}")

    # 3. beats reference real segments and real stills
    beat_ids = [x[0] for x in plan.get("beats", [])]
    for bid in beat_ids:
        if bid not in seg_ids:
            errs.append(f"beat {bid!r} has no matching segment")
    # The closing card is narrated but is NOT a beat — build.py places its audio
    # itself (`audio/<id>.mp3` + CARD_HOLD/TAIL). Most builds call that segment
    # `card`, but plenty of the early ones just let it be the last `nN`. Treat any
    # segment the ORIGINAL build also kept out of BEATS as the card; putting it in
    # `beats` would render the card text twice.
    brief_beat_ids = {x[0] for x in brief.get("beats", [])}
    card_ids = {"card"} | {s["id"] for s in brief["segments"]
                           if s["id"] not in brief_beat_ids}
    for s in plan.get("segments", []):
        if s["id"] not in card_ids and s["id"] not in beat_ids:
            errs.append(f"segment {s['id']!r} never appears in beats")
    sv = set(brief.get("still_vars", {}))
    for x in plan.get("beats", []):
        if len(x) != 3:
            errs.append(f"beat {x} must be [id, still_var, zoom_dir]")
        elif x[1] not in sv:
            errs.append(f"beat {x[0]}: unknown still var {x[1]!r}")
        elif x[2] not in ("in", "out"):
            errs.append(f"beat {x[0]}: zoom must be 'in' or 'out', got {x[2]!r}")

    if seg_ids and seg_ids[-1] not in card_ids:
        warns.append("the card should be the last segment")

    # 4. doctrine: the Old Testament is never `jesus`. Epistles and Acts are the
    #    writer — EXCEPT the handful of places a red-letter KJV really does ink
    #    Christ's own words, which are listed rather than banned outright.
    book = brief.get("book", "")
    for s in plan.get("segments", []):
        if s.get("speaker") == "jesus":
            verse = (s.get("verse") or "").replace("–", "-")
            if book in OT_BOOKS:
                errs.append(f"{s['id']}: marked `jesus` but {book} is Old Testament "
                            f"— premortal Jehovah is `god` (green), never red")
            elif book in EPISTLES and not red_lettered_epistle(verse):
                errs.append(
                    f"{s['id']}: marked `jesus` but {book} is an epistle — that is "
                    f"the writer, so `scripture`. (If this really is one of the "
                    f"passages a red-letter KJV inks, give the exact `verse` and "
                    f"add it to RED_LETTER_EPISTLE.)")

    # 5. non-narrator lines must read as verbatim KJV
    for s in plan.get("segments", []):
        if s.get("speaker") in ("jesus", "god", "scripture", "woman"):
            t = s.get("text", "")
            if not ARCHAIC.search(t) and len(t.split()) > 4:
                warns.append(f"{s['id']} [{s['speaker']}]: no archaic KJV markers — "
                             f"is this verbatim? {t[:70]!r}")
            if not s.get("verse"):
                warns.append(f"{s['id']} [{s['speaker']}]: no verse reference given")

    # 6. the retelling rule
    order = [s["id"] for s in plan.get("segments", [])]
    spk = {s["id"]: s["speaker"] for s in plan.get("segments", [])}
    for i, sid in enumerate(order[:-1]):
        if spk[sid] in ("god", "jesus", "scripture", "woman"):
            nxt = order[i + 1]
            if spk[nxt] not in ("narrator",) and nxt != "card":
                warns.append(f"{sid} [{spk[sid]}] is not followed by a narrator "
                             f"retelling (next is {nxt} [{spk[nxt]}])")
    return errs, warns


def main():
    briefs = json.load(open(os.path.join(HERE, "briefs.json")))
    names = sys.argv[1:] or [f[:-5] for f in sorted(
        os.listdir(os.path.join(HERE, "plans"))) if f.endswith(".json")]
    bad = 0
    tot_w = 0
    for n in names:
        p = os.path.join(HERE, "plans", f"{n}.json")
        if not os.path.exists(p):
            print(f"{n}: NO PLAN")
            bad += 1
            continue
        try:
            plan = json.load(open(p))
        except Exception as e:
            print(f"{n}: UNREADABLE — {e}")
            bad += 1
            continue
        errs, warns = check(plan, briefs[n])
        tot_w += len(warns)
        if errs:
            bad += 1
            print(f"\n{n}: {len(errs)} ERROR(S)")
            for e in errs:
                print(f"   ✗ {e}")
            for w in warns[:4]:
                print(f"   · {w}")
        elif warns:
            print(f"{n}: ok ({len(warns)} warning(s))")
            for w in warns[:3]:
                print(f"   · {w}")
        else:
            print(f"{n}: ok")
    print(f"\n{len(names) - bad}/{len(names)} plans valid; {tot_w} warnings")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
