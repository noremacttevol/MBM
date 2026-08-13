#!/usr/bin/env python3
"""regen_stories_page.py — keep the public website in sync with the approved library.

Rebuilds the site/stories.html card grid and the "N of 200" counts on
stories.html + index.html from PUBLISH-LEDGER.json (the approval truth).
Run this in the SAME session whenever a newly approved row is published to the
app gallery, then `firebase deploy --only hosting` and re-run
scripts/audit_public_videos.py --live.

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

CARD = '''      <figure class="story">
        <div class="frame">
          <a class="tap" href="/story-videos/{id}.mp4" data-video="/story-videos/{id}.mp4" aria-label="Play: {t}">
            <img src="/story-videos/thumbs/{id}.jpg" alt="{t}" loading="lazy" width="640" height="1138">
            <span class="play"><svg width="18" height="20" viewBox="0 0 18 20" aria-hidden="true"><path d="M0 0 L18 10 L0 20 Z" fill="#f3ede0"/></svg></span>
          </a>
        </div>
        <figcaption>{t}</figcaption>
      </figure>'''
cards = "\n\n".join(CARD.format(id=i, t=H.escape(t, quote=True)) for i, t in rows)

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
      f"Now: firebase deploy --only hosting && python3 scripts/audit_public_videos.py --live")
