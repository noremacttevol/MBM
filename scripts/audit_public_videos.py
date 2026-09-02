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
  E3. (--live) the LIVE WEBSITE milkb4meat.org: stories.html's card set ==
     approved set, every card points at the release host, and every
     thumbnail referenced by stories.html + the homepage serves 200.
     (Added 2026-09-01 after Cameron found every card 404ing — the site
     moved to GitHub Pages 2026-08-29 without story-videos/, and this gate
     "PASSED all 8" because it never once looked at what the site served.)

Usage: python3 scripts/audit_public_videos.py [--live]
"""
import hashlib, json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "media-production-v2", "PUBLISH-LEDGER.json")
VIDEOS_TS = os.path.join(ROOT, "mobile", "src", "data", "videos.ts")
GALLERY = os.path.join(ROOT, "site", "story-videos")
# VIDEO HOSTING MOVED OFF FIREBASE (2026-08-24): Firebase Hosting's free tier
# allows 10 GB egress/month, which at ~20.6 MB per clip is only ~486 views a
# month for ALL users combined; the quota was exhausted and every video began
# returning HTTP 509. The app now streams from GitHub release assets, which
# are CDN-served with unmetered bandwidth. Release assets are a FLAT
# namespace, so thumbnails are `thumb-<id>.jpg`, not `thumbs/<id>.jpg`.
HOST = "https://github.com/noremacttevol/MBM/releases/download/videos-v1"

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

# G. social exports — every approved row must sit byte-verified in
#    social/exports/ (Cameron posts ONLY from there; 2026-09-01: "i cant find
#    44 in exports but its approved in the reviewer this shouldnt happen to
#    any of them"). Fix on FAIL: python3 social/refresh-postable.py
import glob as _glob
import json as _json
try:
    _POSTED = set(_json.load(open("social/POSTED.json"))["posted_all_socials"])
except Exception:
    _POSTED = set()
def _tier(_n):
    # posted rows keep their kit in the archive; GP rows stage in gp-queue
    if _n in _POSTED: return "social/posted-1-100"
    if _n >= 301: return "social/gp-queue"
    return "social"
_exp = {}
for _f in _glob.glob("social/exports/row-*.mp4") + _glob.glob("social/posted-1-100/exports/row-*.mp4") + _glob.glob("social/gp-queue/exports/row-*.mp4"):
    _m = re.match(r"row-(\d+)-.+?\.mp4$", os.path.basename(_f))
    if _m and not _f.endswith("-yt.mp4"):
        _exp[int(_m.group(1))] = _f
_exp_missing = [r for r in sorted(approved) if r not in _exp]
# full posting kit (2026-09-01: "i need all posting needs made for each one
# when i approve the videos") — cover + both branded thumbs + per-video page.
# Fix on FAIL: bash social/refresh-all.sh
_kit_missing = []
for _r in sorted(approved):
    _td = _tier(_r)
    _pv = f"{_td}/per-video/{_r:03d}.md" if _r in _POSTED else f"social/per-video/{_r:03d}.md"
    for _p in (f"{_td}/covers/row-{_r:03d}.jpg",
               f"{_td}/thumbs/yt/row-{_r:03d}.jpg",
               f"{_td}/thumbs/vertical/row-{_r:03d}.jpg",
               _pv):
        if not os.path.exists(_p):
            _kit_missing.append(f"{_r}:{_p.split('/')[-2]}")
_exp_drift = []
for _r in sorted(approved):
    if _r in _exp and _r in ledger_sha:
        _h = hashlib.sha1(open(_exp[_r], "rb").read()).hexdigest()
        if _h != ledger_sha[_r]:
            _exp_drift.append(_r)
check(not _exp_missing and not _exp_drift and not _kit_missing,
      "G: every approved row has its FULL posting kit (export + cover + thumbs + per-video)",
      f"missing: {_exp_missing} drifted: {_exp_drift} kit: {_kit_missing[:12]}"
      + ("  ->  run: bash social/refresh-all.sh" if (_exp_missing or _exp_drift or _kit_missing) else ""))

# F. website hygiene — the site may hold NO video file outside the approved
#    gallery, and public marketing pages may reference only approved ids.
SITE = os.path.join(ROOT, "site")
stray = []
for dirpath, dirnames, filenames in os.walk(SITE):
    for fn in filenames:
        if fn.lower().endswith(".mp4"):
            rel = os.path.relpath(os.path.join(dirpath, fn), SITE)
            ok = (os.path.dirname(rel) == "story-videos"
                  and fn[:-4].isdigit() and int(fn[:-4]) in approved)
            if not ok:
                stray.append(rel)
check(not stray, "F1: no mp4 on the site outside the approved gallery", f"stray: {stray}")

PUBLIC_PAGES = ["index.html", "stories.html", "roadmap.html", "support.html", "privacy.html"]
bad_refs = []
for page in PUBLIC_PAGES:
    path = os.path.join(SITE, page)
    if not os.path.exists(path):
        continue
    html = open(path, encoding="utf-8", errors="replace").read()
    page_ids = set(int(x) for x in re.findall(r"/story-videos/(?:thumbs/)?(\d+)\.(?:mp4|jpg)", html))
    page_ids |= set(int(x) for x in re.findall(r"releases/download/videos-v1/(\d+)\.mp4", html))
    for rid in page_ids:
        if rid not in approved:
            bad_refs.append(f"{page}→{rid}")
    for pat in ("fixed/", "Explainer.mp4", "img/walk/"):
        if pat in html:
            bad_refs.append(f"{page}→{pat}")
check(not bad_refs, "F2: public pages reference only approved stories", f"bad: {bad_refs}")

# E. live
if "--live" in sys.argv:
    def head(url):
        req = urllib.request.Request(url, method="HEAD")
        for attempt in (1, 2, 3):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    return r.status, int(r.headers.get("Content-Length") or -1)
            except urllib.error.HTTPError as e:
                if e.code >= 500 and attempt < 3:
                    continue  # transient CDN/hosting wobble — retry
                return e.code, -1
            except (TimeoutError, OSError):
                if attempt == 3:
                    return -1, -1  # network dead ≠ file wrong, but still fails the check honestly
        return -1, -1
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

    # E3: the LIVE WEBSITE. The site is GitHub Pages (repo milkb4meat-site);
    # cards stream from the release host, thumbs are same-origin files.
    def get(url):
        for attempt in (1, 2, 3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url), timeout=60) as r:
                    return r.status, r.read()
            except urllib.error.HTTPError as e:
                if e.code >= 500 and attempt < 3:
                    continue
                return e.code, b""
            except (TimeoutError, OSError):
                if attempt == 3:
                    return -1, b""
        return -1, b""
    SITE_URL = "https://milkb4meat.org"
    web_bad = []
    st, body = get(f"{SITE_URL}/stories.html")
    if st != 200:
        web_bad.append(f"stories.html HTTP {st}")
    else:
        live_html = body.decode("utf-8", "replace")
        live_vids = re.findall(r'data-video="([^"]+?/(\d+)\.mp4)"', live_html)
        live_ids = set(int(i) for _, i in live_vids)
        if live_ids != approved:
            web_bad.append(f"live card set != approved (extra {sorted(live_ids - approved)}, "
                           f"missing {sorted(approved - live_ids)})")
        off_host = [u for u, _ in live_vids if not u.startswith(HOST + "/")]
        if off_host:
            web_bad.append(f"{len(off_host)} cards not on the release host, e.g. {off_host[:3]}")
        thumb_paths = set(re.findall(r'(?:src|poster)="(/story-videos/thumbs/\d+\.jpg)"', live_html))
        st2, body2 = get(f"{SITE_URL}/")
        if st2 != 200:
            web_bad.append(f"homepage HTTP {st2}")
        else:
            thumb_paths |= set(re.findall(r'(?:src|poster)="(/story-videos/thumbs/\d+\.jpg)"',
                                          body2.decode("utf-8", "replace")))
        dead = []
        for t in sorted(thumb_paths):
            s, _ln = head(SITE_URL + t)
            if s != 200:
                dead.append(f"{t}:{s}")
        if dead:
            web_bad.append(f"{len(dead)} thumbnails dead on the site, e.g. {dead[:5]}")
    check(not web_bad, "E3: milkb4meat.org serves the approved set (cards + thumbs live)",
          "; ".join(web_bad))

for w in warns:
    print("  warn:", w)
print("\n" + ("✅ PUBLIC-VIDEO GATE: PASS — the public sees exactly the approved realistic set."
              if not fails else f"❌ PUBLIC-VIDEO GATE: FAIL ({len(fails)}): {fails}"))
sys.exit(1 if fails else 0)
