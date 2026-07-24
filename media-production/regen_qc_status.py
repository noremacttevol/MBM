#!/usr/bin/env python3
"""Regenerate media-production/QC-STATUS.json from REALITY so the review board
shows every genuinely-done video (the old file was a stale Jul-22 scan that
marked 192 fail and hid them). A build PASSES = its video plays AND it has the
new ElevenLabs voice AND it has no narrator echo. gen_site_index only shows
passing (or approved) videos, so this file decides what Cameron sees.

Run `git fetch origin` first (new-voice check reads origin commit times)."""
import glob, json, os, re, subprocess, sys

MP = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(MP)

# --- new-voice set: mp4 on origin committed at/after its ElevenLabs audio ------
tree = subprocess.run(["git", "ls-tree", "-r", "--name-only", "origin/main", "--", "media-production"],
                      cwd=REPO, capture_output=True, text=True).stdout.splitlines()
def ctime(p):
    o = subprocess.run(["git", "log", "-1", "--format=%ct", "origin/main", "--", p],
                       cwd=REPO, capture_output=True, text=True).stdout.strip()
    return int(o) if o else 0
newvoice = set()
dirs = sorted(set(re.match(r"(media-production/build-\d+-[^/]+)/", p).group(1)
                  for p in tree if re.match(r"media-production/build-\d+-[^/]+/", p)))
for d in dirs:
    num = int(re.search(r"build-(\d+)-", d).group(1))
    mp4 = next((p for p in tree if re.match(rf"{re.escape(d)}/[0-9a-z]+-\d+_[^/]+\.mp4$", p)), None)
    if not mp4: continue
    if not any(p.startswith(f"{d}/audio/") and p.endswith(".mp3") for p in tree): continue
    if ctime(mp4) >= ctime(f"{d}/audio"):
        newvoice.add(num)

# --- echo set (working tree): builds echo_scan still flags ---------------------
echo = set()
out = subprocess.run([sys.executable, os.path.join(MP, "echo_scan.py")],
                     capture_output=True, text=True).stdout
for m in re.finditer(r"^## build-0*(\d+)-", out, re.M):
    echo.add(int(m.group(1)))

# --- plays: verify-mp4 on the working-tree mp4 (skip = treat as fail) ----------
status = {}
for bd in sorted(glob.glob(os.path.join(MP, "build-[0-9]*"))):
    m = re.match(r"build-(\d+)-", os.path.basename(bd))
    if not m: continue
    num = int(m.group(1))
    mp4s = [p for p in glob.glob(os.path.join(bd, "*.mp4"))]
    mp4 = mp4s[0] if mp4s else None
    reasons = []
    plays = bool(mp4) and subprocess.run(["bash", os.path.join(MP, "..", "admin", "verify-mp4.sh"), mp4],
                                         capture_output=True).returncode == 0 if mp4 else False
    if not plays: reasons.append("does not play / no mp4")
    if num not in newvoice: reasons.append("old voice (not rebuilt with ElevenLabs audio)")
    if num in echo: reasons.append("narrator echo")
    status[str(num)] = {"pass": not reasons, "reasons": reasons}

passed = sum(1 for v in status.values() if v["pass"])
tmp = os.path.join(MP, "QC-STATUS.json.tmp")
json.dump(status, open(tmp, "w"), indent=1)
os.replace(tmp, os.path.join(MP, "QC-STATUS.json"))
print(f"QC-STATUS regenerated: {passed} pass / {len(status)} total "
      f"(newvoice={len(newvoice)}, echo={len(echo)})")
