#!/usr/bin/env python3
"""Scan every build's narration for the 'echo' Cameron hates: two ADJACENT lines
that say the same thing almost word-for-word (a character/scripture line then the
narrator repeating it, or narrator then scripture). Flags high word-overlap pairs."""
import glob, os, re, subprocess, sys, importlib.util

MP = "/home/noremacttevol/Desktop/MBM/media-production"
STOP = set("the a an and or of to in on for his her he she it they them was were is are be "
           "that this with as at by from i you me my thy thee thou shall will would had have has "
           "did do not no but so her him he she they said told out over into her his".split())

def words(t):
    return [w for w in re.findall(r"[a-z]+", t.lower()) if w not in STOP and len(w) > 2]

def sentences(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s.strip()]

def echo_sentences(char_line, narr_text):
    """Return the narrator SENTENCES that restate the character line — a sentence
    that contains >=55% of the character line's content words (>=2 words). This
    catches a paraphrase repeat ('touch his clothes ... I will be well' echoing
    'touch but his clothes, I shall be whole') without flagging an action sentence
    that merely reuses one word ('reached out to touch the edge of his cloak')."""
    cw = set(words(char_line))
    if len(cw) < 2: return []
    hits = []
    for s in sentences(narr_text):
        sw = set(words(s))
        shared = len(cw & sw)
        if shared >= 2 and shared / len(cw) >= 0.55:
            hits.append(s)
    return hits

def overlap(a, b):
    # 'a' is the character/scripture line, 'b' the adjacent narrator text.
    return 1.0 if echo_sentences(a, b) else 0.0

def load_segments(bdir):
    code = ("import make_narration as m,json;"
            "print(json.dumps([[s[0],s[1],s[2]] for s in m.SEGMENTS]))")
    r = subprocess.run([sys.executable, "-c", code], cwd=bdir,
                       capture_output=True, text=True)
    import json
    try: return json.loads(r.stdout.strip().splitlines()[-1])
    except Exception: return None

hits = {}
for bdir in sorted(glob.glob(os.path.join(MP, "build-[0-9]*"))):
    if not os.path.exists(os.path.join(bdir, "make_narration.py")): continue
    segs = load_segments(bdir)
    if not segs: continue
    b = os.path.basename(bdir)
    for i in range(len(segs) - 1):
        (id1, sp1, t1), (id2, sp2, t2) = segs[i], segs[i + 1]
        # echo = a character/scripture line adjacent to a narrator line (either order)
        speakers = {sp1, sp2}
        if "narrator" not in speakers: continue
        if speakers == {"narrator"}: continue
        # character/scripture line = the non-narrator one; narrator = the repeat side
        if sp1 == "narrator": char_line, narr_id, narr_txt = t2, id1, t1
        else:                 char_line, narr_id, narr_txt = t1, id2, t2
        bad = echo_sentences(char_line, narr_txt)
        if bad:
            hits.setdefault(b, []).append((round(overlap(char_line, narr_txt), 2),
                                           "char", char_line, narr_id, narr_txt, bad))

print(f"builds with echo hits: {len(hits)}\n")
total = 0
for b in sorted(hits, key=lambda x: int(re.search(r'\d+', x).group())):
    print(f"## {b}")
    for ov, _c, char_line, narr_id, narr_txt, bad in hits[b]:
        total += 1
        print(f"  char: {char_line[:78]}")
        print(f"  narr[{narr_id}] REPEAT SENTENCE(S) to cut:")
        for s in bad:
            print(f"     - {s[:80]}")
    print()
print(f"TOTAL echo pairs: {total} across {len(hits)} builds")
