#!/usr/bin/env python3
"""Fix the narrator echo in ONE build: delete the narrator sentence(s) that
restate an adjacent character/scripture line (echo_scan's rule), re-voice the
changed segments via ElevenLabs, and write the sidecars build.py needs. Rebuild
is done by the caller (build.py). Backs up make_narration.py -> .pre-echo.

Usage: python3 media-production/echo_fix.py <build-number-or-dir>
Prints CHANGED:<id> lines and DROPPED:<id> lines; exits 0 if it edited anything,
2 if nothing to fix.
"""
import asyncio, glob, importlib, os, re, sys

MP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MP)
from echo_scan import sentences, echo_sentences   # same rule as the scanner

arg = sys.argv[1]
d = arg if os.path.isdir(arg) else (glob.glob(os.path.join(MP, f"build-{int(arg):02d}-*")) or [None])[0]
if not d or not os.path.exists(os.path.join(d, "make_narration.py")):
    print("no such build", arg); sys.exit(2)
os.chdir(d)

# load SEGMENTS fresh
sys.path.insert(0, d)
import make_narration as m
importlib.reload(m)
segs = list(m.SEGMENTS)

# find narrator segments to trim
changed, dropped = {}, []
for i, (sid, sp, txt) in enumerate(segs):
    if sp != m.NARRATOR: continue
    # adjacent character/scripture lines (either side)
    neigh = []
    if i > 0 and segs[i-1][1] != m.NARRATOR: neigh.append(segs[i-1][2])
    if i+1 < len(segs) and segs[i+1][1] != m.NARRATOR: neigh.append(segs[i+1][2])
    bad = set()
    for cl in neigh:
        bad.update(echo_sentences(cl, txt))
    if not bad: continue
    kept = [s for s in sentences(txt) if s not in bad]
    new = " ".join(kept).strip()
    if new: changed[sid] = (txt, new)
    else:   dropped.append((sid, txt))

if not changed and not dropped:
    print("nothing to fix"); sys.exit(2)

# rewrite make_narration.py (backup once)
if not os.path.exists("make_narration.py.pre-echo"):
    open("make_narration.py.pre-echo", "w").write(open("make_narration.py").read())
src = open("make_narration.py").read()
for sid, (old, new) in changed.items():
    assert old in src, f"seg {sid} text not found"
    src = src.replace(old, new)
    print("CHANGED:" + sid)
for sid, old in dropped:
    # remove the whole ("id", SPEAKER, "...") entry line
    src = re.sub(r'^[ \t]*\(\s*"' + re.escape(sid) + r'".*?\),?[ \t]*\n', "", src, flags=re.M | re.S)
    print("DROPPED:" + sid)
open("make_narration.py", "w").write(src)

# re-voice changed segments (dropped ones: delete their audio)
importlib.reload(m)
seg = {s[0]: (s[1], s[2]) for s in m.SEGMENTS}
async def revoice():
    for sid in changed:
        spk, t = seg[sid]
        await m.save_speaker_narration(m.spoken_text(t, m.SPOKEN, spk), spk, f"audio/{sid}.mp3")
        print("revoiced audio/%s.mp3" % sid)
asyncio.run(revoice())
for sid, _ in dropped:
    for ext in (".mp3", ".timing.json"):
        p = f"audio/{sid}{ext}"
        if os.path.exists(p): os.remove(p)
print(f"done: {len(changed)} trimmed, {len(dropped)} dropped")
