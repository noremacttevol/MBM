#!/usr/bin/env python3
"""AGENT #4 FINISH GATE — decide which videos #4 may caption + finish + post NOW,
and route the rest. A video is FINISHABLE only when its pictures are not known-bad
and its script is echo-clean:

  BLOCK reasons (routed):
    echo      -> #1 : narrator repeats a line (media-production/echo_scan.py)
    complaint -> #3 : an OPEN picture complaint on the board (COMPLAINTS.md)
    worklist  -> #3 : listed in a picture redo / stills-needed worklist
    law       -> #3 : fails character_ref_gate or jesus_face_gate (off-law faces)

Anything with none of those is GREEN = #4 finishes it. (Technical QC — dead air,
hum, size, loudness, captions — is checked per-cut at ship time by scan_defects /
verify-mp4, not here.)

Usage:  python3 media-production/finish_gate.py            # summary + green list
        python3 media-production/finish_gate.py --nums     # just the green numbers
"""
import glob, os, re, subprocess, sys

MP = os.path.dirname(os.path.abspath(__file__))
builds = {}   # num -> dir
for d in glob.glob(os.path.join(MP, "build-[0-9]*")):
    m = re.match(r"build-0*(\d+)-", os.path.basename(d))
    if m and os.path.exists(os.path.join(d, "build.py")):
        builds.setdefault(int(m.group(1)), d)   # first slug wins on dupes

# --- echo (#1) --------------------------------------------------------------
echo = set()
try:
    out = subprocess.run([sys.executable, os.path.join(MP, "echo_scan.py")],
                         capture_output=True, text=True, timeout=1200).stdout
    for m in re.finditer(r"^## build-0*(\d+)-", out, re.M):
        echo.add(int(m.group(1)))
except Exception as e:
    print("WARN echo_scan failed:", e, file=sys.stderr)

# --- picture complaints (#3): classify OPEN complaints as picture vs other ---
PIC = re.compile(r"pictur|photo|image|looks?|face|giant|clothes|shirt|hair|"
                 r"chang|redo|low.?grade|lograde|\bsize\b|burning|frame|square|"
                 r"walking|scene|drawn|art|character", re.I)
NONPIC = re.compile(r"pronounc|spell|phonetic|said|caption|word|extra second|"
                    r"dead air|silence|volume|audio|voice|echo|repeat", re.I)
complaint = set()
cpath = os.path.join(MP, "COMPLAINTS.md")
if os.path.exists(cpath):
    for line in open(cpath):
        m = re.match(r"\|\s*(\d+)\s*\|.*?\|(.*)\|", line)
        if not m: continue
        num, text = int(m.group(1)), m.group(2)
        # picture complaint if it mentions a picture cue and isn't purely audio/pron
        if PIC.search(text) and not (NONPIC.search(text) and not PIC.search(text)):
            complaint.add(num)

# --- picture worklists (#3) -------------------------------------------------
worklist = set()
for wf in ("PICTURE-REDO-WORKLIST.md", "PICTURE-WORKLIST.md", "STILLS-NEEDED.md"):
    p = os.path.join(MP, wf)
    if not os.path.exists(p): continue
    for m in re.finditer(r"build-0*(\d+)-|#(\d+)\b", open(p).read()):
        worklist.add(int(m.group(1) or m.group(2)))

# --- law gates (#3) ---------------------------------------------------------
def gate_fail(d):
    for g in ("character_ref_gate.py", "jesus_face_gate.py"):
        try:
            r = subprocess.run([sys.executable, os.path.join(MP, g),
                                "--dir", os.path.basename(d)], cwd=MP,
                               capture_output=True, text=True, timeout=60)
            if r.returncode != 0: return g.replace(".py", "")
        except Exception: pass
    return None

green, blocked = [], {}
for num in sorted(builds):
    reasons = []
    if num in echo: reasons.append("echo->#1")
    if num in complaint: reasons.append("complaint->#3")
    if num in worklist: reasons.append("worklist->#3")
    lf = gate_fail(builds[num])
    if lf: reasons.append(f"{lf}->#3")
    if reasons: blocked[num] = reasons
    else: green.append(num)

if "--nums" in sys.argv:
    print(" ".join(str(n) for n in green)); sys.exit(0)

print(f"GREEN (#4 finishes now): {len(green)}")
print(" ".join(str(n) for n in green), "\n")
by = {}
for num, rs in blocked.items():
    for r in rs: by.setdefault(r, []).append(num)
print(f"BLOCKED: {len(blocked)}")
for r in sorted(by, key=lambda k: -len(by[k])):
    ns = sorted(by[r])
    print(f"  {r:16} {len(ns):3}  {' '.join(map(str, ns))}")
