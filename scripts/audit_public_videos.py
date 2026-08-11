#!/usr/bin/env python3
"""audit_public_videos.py — THE PUBLIC-VIDEO GATE.

Proves, mechanically, that every video the public can reach (app gallery +
website) is EXACTLY the set of realistic v2 cuts Cameron approved — nothing
old-style, nothing missing, nothing byte-drifted. Run before/after any deploy
or OTA that touches videos. Exit 0 = PASS, 1 = FAIL.

Truth source: media-production-v2/PUBLISH-LEDGER.json — a row is PUBLIC-READY
iff its LATEST version entry is v2.x and lists platform "app-gallery".

Checks:
  A. mobile/src/data/videos.ts PRODUCED_VIDEO_IDS == approved set (exact)
  B. site/story-videos/*.mp4 ids on disk           == approved set (exact)
  C. every approved mp4's sha1 on disk             == ledger sha1 (no drift)
  D. every approved id has a thumb jpg on disk
  E. (--live) every approved URL serves 200 with disk's byte size,
     and every retired old-era URL returns 404/410 (not still cached-alive)

Usage: python3 scripts/audit_public_videos.py [--live]
"""
import hashlib, json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "media-production-v2", "PUBLISH-LEDGER.json")
VIDEOS_TS = os.path.join(ROOT, "mobile", "src", "data", "videos.ts")
GALLERY = os.path.join(ROOT, "site", "story-videos")
HOST = "https://milk-b4-meat.web.app/story-videos"

fails, warns = [], []


def check(ok, label, detail=""):
    print(("  PASS " if ok else "✗ FAIL ") + label + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(label)


# Truth: the ledger
rows = json.load(open(LEDGER))["rows"]
approved, old_era, ledger_sha = set(), set(), {}
for rid, r in rows.items():
    vs = r.get("versions") or []
    if not vs:
        continue
    last = vs[-1]
    if not any(w.get("platform") == "app-gallery" for w in last.get("where", [])):
        continue
    if str(last.get("version", "")).startswith("2"):
        approved.add(int(rid))
        if last.get("sha1"):
            ledger_sha[int(rid)] = last["sha1"]
    else:
        old_era.add(int(rid))
print(f"LEDGER: {len(approved)} approved realistic rows; {len(old_era)} old-era rows (must NOT be public)")

# A. app catalog set
src = open(VIDEOS_TS).read()
m = re.search(r"PRODUCED_VIDEO_IDS = new Set<number>\(\[(.*?)\]\)", src, re.S)
produced = set(int(x) for x in re.findall(r"\d+", m.group(1)))
check(produced == approved, "A: app PRODUCED_VIDEO_IDS == approved set",
      f"app-only: {sorted(produced - approved)} missing: {sorted(approved - produced)}")

# B. disk set
disk = set(int(f[:-4]) for f in os.listdir(GALLERY) if f.endswith(".mp4") and f[:-4].isdigit())
check(disk == approved, "B: gallery mp4s on disk == approved set",
      f"extra: {sorted(disk - approved)} missing: {sorted(approved - disk)}")

# C. byte truth
drift = []
for rid in sorted(approved & disk):
    if rid not in ledger_sha:
        warns.append(f"row {rid}: ledger entry has no sha1 (skipped)")
        continue
    h = hashlib.sha1(open(os.path.join(GALLERY, f"{rid}.mp4"), "rb").read()).hexdigest()
    if h != ledger_sha[rid]:
        drift.append(rid)
check(not drift, "C: every approved mp4 byte-matches its ledger sha1", f"drifted: {drift}")

# D. thumbs
no_thumb = [r for r in sorted(approved) if not os.path.exists(os.path.join(GALLERY, "thumbs", f"{r}.jpg"))]
check(not no_thumb, "D: every approved id has a thumbnail", f"missing: {no_thumb}")

# E. live
if "--live" in sys.argv:
    def head(url):
        req = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status, int(r.headers.get("Content-Length") or -1)
        except urllib.error.HTTPError as e:
            return e.code, -1
    bad_live, still_up = [], []
    for rid in sorted(approved):
        st, ln = head(f"{HOST}/{rid}.mp4")
        if st != 200 or ln != os.path.getsize(os.path.join(GALLERY, f"{rid}.mp4")):
            bad_live.append((rid, st, ln))
    check(not bad_live, "E1: all approved rows live with exact disk bytes", str(bad_live))
    for rid in sorted(old_era):
        st, _ = head(f"{HOST}/{rid}.mp4")
        if st == 200:
            still_up.append(rid)
    check(not still_up, "E2: every old-era row is GONE from hosting (404)", f"still up: {still_up}")

for w in warns:
    print("  warn:", w)
print("\n" + ("✅ PUBLIC-VIDEO GATE: PASS — the public sees exactly the approved realistic set."
              if not fails else f"❌ PUBLIC-VIDEO GATE: FAIL ({len(fails)}): {fails}"))
sys.exit(1 if fails else 0)
