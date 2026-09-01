#!/usr/bin/env python3
"""regen_stories_page.py — keep the public website in sync with the approved library.

Rebuilds the site/stories.html card grid and the "N of 200" counts on
stories.html + index.html from PUBLISH-LEDGER.json (the approval truth).
Run this in the SAME session whenever a newly approved row is published to the
app gallery, then push stories.html + index.html + any NEW thumbs to the
noremacttevol/milkb4meat-site repo (GitHub Pages serves milkb4meat.org — the
Firebase deploy is DEAD, 2026-08-29) and re-run
scripts/audit_public_videos.py --live.

URL LAW (2026-09-01, after Cameron found every video/thumb 404ing on Pages):
  - videos  -> the videos-v1 GitHub release (same host the app streams from;
               unmetered, already carries every published row)
  - thumbs  -> same-origin /story-videos/thumbs/{id}.jpg, committed INTO the
               milkb4meat-site repo (~70KB each; proper image MIME, no 302
               chain per card). A new publish must copy the new thumb(s) in.
site/review.html + docs/review.html detect WEB presence by regexing
data-video="...{id}.mp4" out of the live stories.html — their regex accepts
any host, so changing VIDEO_HOST here cannot silently break the WEB chips.

Idempotent: safe to run any time; exits 1 if the rebuild would produce a grid
that disagrees with the ledger.
"""
import html as H
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "media-production-v2", "PUBLISH-LEDGER.json")
STORIES = os.path.join(ROOT, "site", "stories.html")
INDEX = os.path.join(ROOT, "site", "index.html")

led = json.load(open(LEDGER))["rows"]
rows = []
for rid, r in led.items():
    vs = r.get("versions") or []
    if not vs:
        continue
    last = vs[-1]
    if (str(last.get("version", "")).startswith("2")
            and any(w.get("platform") == "app-gallery" for w in last.get("where", []))):
        rows.append((int(rid), r["title"]))
rows.sort()
N = len(rows)

VIDEO_HOST = "https://github.com/noremacttevol/MBM/releases/download/videos-v1"

CARD = '''      <figure class="story">
        <div class="frame">
          <a class="tap" href="{host}/{id}.mp4" data-video="{host}/{id}.mp4" aria-label="Play: {t}">
            <img src="/story-videos/thumbs/{id}.jpg" alt="{t}" loading="lazy" width="640" height="1138">
            <span class="play"><svg width="18" height="20" viewBox="0 0 18 20" aria-hidden="true"><path d="M0 0 L18 10 L0 20 Z" fill="#f3ede0"/></svg></span>
          </a>
        </div>
        <figcaption>{t}</figcaption>
      </figure>'''
cards = "\n\n".join(CARD.format(id=i, t=H.escape(t, quote=True), host=VIDEO_HOST) for i, t in rows)

s = open(STORIES).read()
s2 = re.sub(r'(<div class="grid">\n).*?(\n    </div>)',
            lambda m: m.group(1) + "\n" + cards + "\n" + m.group(2), s, flags=re.S)
s2 = re.sub(r"\d+ of 200 stories finished", f"{N} of 200 stories finished", s2)
s2 = re.sub(r"\d+ finished, free to watch", f"{N} finished, free to watch", s2)
if s2.count('<figure class="story">') != N:
    print(f"FATAL: grid rebuild produced {s2.count('<figure class=\"story\">')} cards, ledger says {N}")
    sys.exit(1)
open(STORIES, "w").write(s2)

i = open(INDEX).read()
i = re.sub(r"\d+ of 200 stories finished", f"{N} of 200 stories finished", i)
i = re.sub(r"See all \d+ finished stories", f"See all {N} finished stories", i)
open(INDEX, "w").write(i)

print(f"stories.html: {N} cards; counts synced on stories.html + index.html. "
      f"Now: push stories.html + index.html + new thumbs to noremacttevol/milkb4meat-site, "
      f"then python3 scripts/audit_public_videos.py --live")
