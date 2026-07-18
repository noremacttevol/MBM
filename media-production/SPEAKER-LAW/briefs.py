#!/usr/bin/env python3
"""Build a per-video brief: everything a plan author needs, already extracted.

A brief carries the scripture reference, every current segment with its text and
whether it is painted red today, the current BEATS mapping with the still each
beat sits on, and the assets on disk. Plan authors then do only the judgment —
which speaker each line belongs to — instead of re-deriving the mechanics 198
times.
"""
import ast
import glob
import json
import os
import re
import sys

MP = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
    if os.path.basename(os.path.dirname(os.path.abspath(__file__))) == "SPEAKER-LAW" \
    else os.path.expanduser("~/Desktop/MBM/media-production")

BOOKS = {
    "genesis": "Genesis", "exodus": "Exodus", "leviticus": "Leviticus",
    "numbers": "Numbers", "deuteronomy": "Deuteronomy", "joshua": "Joshua",
    "judges": "Judges", "ruth": "Ruth", "1-samuel": "1 Samuel",
    "1samuel": "1 Samuel", "2-samuel": "2 Samuel", "1-kings": "1 Kings",
    "1kings": "1 Kings", "2-kings": "2 Kings", "2kings": "2 Kings",
    "job": "Job", "psalm": "Psalm", "psalms": "Psalms",
    "proverbs": "Proverbs", "ecclesiastes": "Ecclesiastes",
    "isaiah": "Isaiah", "jeremiah": "Jeremiah", "ezekiel": "Ezekiel",
    "daniel": "Daniel", "hosea": "Hosea", "joel": "Joel", "amos": "Amos",
    "jonah": "Jonah", "micah": "Micah", "habakkuk": "Habakkuk",
    "zechariah": "Zechariah", "malachi": "Malachi",
    "matthew": "Matthew", "matt": "Matthew", "mt": "Matthew",
    "mark": "Mark", "luke": "Luke", "john": "John",
    "2-thessalonians": "2 Thessalonians", "2thessalonians": "2 Thessalonians",
    "acts": "Acts", "romans": "Romans", "1-corinthians": "1 Corinthians",
    "1corinthians": "1 Corinthians", "2-corinthians": "2 Corinthians",
    "2corinthians": "2 Corinthians", "galatians": "Galatians",
    "ephesians": "Ephesians", "philippians": "Philippians",
    "colossians": "Colossians", "1-thessalonians": "1 Thessalonians",
    "1thessalonians": "1 Thessalonians", "1-timothy": "1 Timothy",
    "2-timothy": "2 Timothy", "titus": "Titus", "hebrews": "Hebrews",
    "james": "James", "1-peter": "1 Peter", "1peter": "1 Peter",
    "2-peter": "2 Peter", "1-john": "1 John", "1john": "1 John",
    "revelation": "Revelation",
}

# Old Testament: any Deity speech here is the premortal Jehovah -> GOD/green,
# never red. A red-letter KJV prints none of it in red.
OT = {"Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua",
      "Judges", "Ruth", "1 Samuel", "2 Samuel", "1 Kings", "2 Kings", "Job",
      "Psalm", "Psalms", "Proverbs", "Ecclesiastes", "Isaiah", "Jeremiah",
      "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Jonah", "Micah",
      "Habakkuk", "Zechariah", "Malachi"}
# Epistles/Acts/Revelation: the writer is Paul, Peter, James, John, Luke...
# never Jesus, except Revelation's explicit red-letter sayings.
EPISTLE = {"Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians",
           "Ephesians", "Philippians", "Colossians", "1 Thessalonians",
           "1 Timothy", "2 Timothy", "Titus", "Hebrews", "James", "1 Peter",
           "2 Peter", "1 John", "Revelation"}
GOSPEL = {"Matthew", "Mark", "Luke", "John"}


def reference_of(mp4):
    if not mp4:
        return "", ""
    head = mp4.split("_")[0]
    m = re.match(r"([0-9a-z-]+?)-(\d+)$", head)
    if m and m.group(1) in BOOKS:
        return BOOKS[m.group(1)], f"{BOOKS[m.group(1)]} {m.group(2)}"
    for k, v in BOOKS.items():
        if head.startswith(k):
            rest = head[len(k):].strip("-")
            return v, (f"{v} {rest}" if rest.isdigit() else v)
    return "", ""


def beats_of(build_dir):
    """(seg_id, still_var, zoom_dir) plus the still_var -> filename mapping.

    Three BEATS shapes exist across the library:
      A  ("n1", S1, "in")                      — 178 builds
      C  ("n1", [(S1, "in")], gap_override)    — 6 builds; one beat may span
                                                 several stills, cutting at
                                                 caption-chunk boundaries
    (Template B keeps its beats as a 7-tuple inside build.py and is converted
    separately.) A template-C beat is reported with every still it touches.
    """
    src = open(os.path.join(build_dir, "build.py"),
               encoding="utf-8", errors="replace").read()
    # still vars are not uniformly named (S1, ST1, IMG1...) — match any
    # module-level constant bound to an image filename
    stills = dict(re.findall(r'^([A-Z][A-Z0-9_]*)\s*=\s*"([^"]+\.(?:jpe?g|png))"',
                             src, re.M))
    m = re.search(r"^BEATS = \[(.*?)^\]", src, re.M | re.S)
    beats, shape = [], "A"
    if not m:
        return beats, stills, "unparsed"
    body = m.group(1)
    if re.search(r'\(\s*"[^"]+"\s*,\s*\[', body):
        shape = "C"
        # the gap_override third element is optional (build-73 omits it)
        for bm in re.finditer(r'\(\s*"([^"]+)"\s*,\s*\[(.*?)\]\s*[,)]', body, re.S):
            pairs = re.findall(r'\(\s*([A-Za-z_]\w*|"[^"]+")\s*,\s*"([^"]+)"\s*\)',
                               bm.group(2))
            for still, zdir in pairs:
                beats.append([bm.group(1), still.strip('"'), zdir])
    else:
        for bm in re.finditer(
                r'\(\s*"([^"]+)"\s*,\s*([A-Za-z_]\w*|"[^"]+")\s*,\s*"([^"]+)"',
                body):
            beats.append([bm.group(1), bm.group(2).strip('"'), bm.group(3)])
    return beats, stills, shape


def brief(build, survey):
    r = survey[build]
    d = os.path.join(MP, build)
    book, ref = reference_of(r.get("mp4") or "")
    beats, stills, shape = beats_of(d)
    testament = ("OT" if book in OT else
                 "epistle" if book in EPISTLE else
                 "gospel" if book in GOSPEL else "unknown")
    red = set(r["red"])
    return {
        "build": build,
        "template": "B" if r["template"] == "B" else shape,
        "mp4": r.get("mp4"),
        "book": book,
        "reference": ref,
        "testament": testament,
        "card_hold_was": r.get("card_hold"),
        "assets": sorted(os.path.basename(p) for p in
                         glob.glob(os.path.join(d, "assets", "*.jpeg"))),
        "still_vars": stills,
        "beats": beats,
        "segments": [{"id": s["id"], "currently_red": s["id"] in red,
                      "text": s["text"]} for s in r["segments"]],
    }


def main():
    survey = json.load(open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "survey.json")))
    out = {}
    for b in survey:
        try:
            out[b] = brief(b, survey)
        except Exception as e:
            out[b] = {"build": b, "error": f"{type(e).__name__}: {e}"}
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "briefs.json")
    tmp = dest + ".tmp"
    with open(tmp, "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    os.replace(tmp, dest)

    from collections import Counter
    c = Counter(v.get("testament") for v in out.values())
    noref = [b for b, v in out.items() if not v.get("reference")]
    nobeats = [b for b, v in out.items() if not v.get("beats")]
    print(f"briefs: {len(out)}")
    print(f"  by testament: {dict(c)}")
    print(f"  no reference parsed: {len(noref)} {noref[:8]}")
    print(f"  no BEATS parsed:     {len(nobeats)} {nobeats[:8]}")


if __name__ == "__main__":
    main()
