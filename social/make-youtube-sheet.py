#!/usr/bin/env python3
"""Regenerate social/YOUTUBE-UPLOAD-SHEET.md from POST-QUEUE.md + postable.json.

Run from the repo root:  python3 social/make-youtube-sheet.py

Order = row number, lowest first (Cameron's law, 2026-08-07).
LINK LAW (Cameron, 2026-08-07): promote the app actively, but the ONLY link in any
caption, bio, or description is https://milkb4meat.org — never a store link. The
site is updated with the current app links as approvals land.
"""
import json
import re

APP_LINE = ('Download the free Milk Before Meat app for every story and more:\n'
            'https://milkb4meat.org')
STRIP = ' Download the free Milk Before Meat app for every story and more — link in bio.'

SPECIAL = {'John316': 'John 3:16', 'FeedingThe5000': 'Feeding the 5000', 'KJV': 'KJV',
           'TenLepers': 'Ten Lepers', 'TheNet': 'The Net', 'TheSeventy': 'The Seventy'}


def tagword(h):
    w = h.lstrip('#')
    return SPECIAL.get(w) or re.sub(r'(?<=[a-z])(?=[A-Z])|(?<=[a-zA-Z])(?=[0-9])', ' ', w)


def main():
    pj = {p['row']: p for p in json.load(open('social/postable.json'))['postable']}
    q = open('social/POST-QUEUE.md').read()
    entries = {}
    for block in re.split(r'(?=^### Row )', q, flags=re.M):
        m = re.match(r'^### Row (\d+) — (.+)$', block, re.M)
        if not m:
            continue
        row = int(m.group(1))
        yt = re.search(r'\*\*YouTube title:\*\* (.+)', block)
        cap = re.search(r'\*\*Caption:\*\*\n(.+?)\n\*\*Story tags', block, re.S)
        tags = re.search(r'\*\*Story tags:\*\* `([^`]+)`', block)
        entries[row] = dict(title=yt.group(1).strip(),
                            caption=[l.strip() for l in cap.group(1).strip().split('\n')],
                            tags=tags.group(1).split())

    out = ["""# YOUTUBE UPLOAD SHEET — every approved video, ready to paste

> **Order = row number, lowest first (01, 02, 03…).** The numbers are the posting
> order only — they never go in a title. Work top to bottom. Every entry has an
> **UPLOAD THESE** box naming the exact files, then the title / description / tags
> to paste (tags box: YouTube Studio → Show more → Tags).
>
> **About thumbnails:** videos 3:00 or shorter become **Shorts** — YouTube picks
> the frame and usually won't offer a thumbnail box for them (that's normal, not a
> mistake; if it does offer one, use the file listed). Videos over 3:00 are regular
> uploads — **set the thumbnail, it matters most there.** The tall cover file is
> for TikTok and Instagram when you post there later.
>
> **The only link in any description is milkb4meat.org** — the site carries the
> current app links as approvals land. Never paste a store link.
>
> **After each upload, tick the YT chip on the live tracker** (reviewer page,
> bottom). New approvals get their own entry, thumbnails included, automatically.
"""]
    for row in sorted(pj):
        p, e = pj[row], entries[row]
        mm, ss = p['duration'].split(':')
        is_short = (int(mm) * 60 + int(ss)) <= 180
        cap = e['caption']
        desc = (f"{cap[0]}\n\n{cap[1]}\n\n{cap[2].replace(STRIP, '')}\n\n{APP_LINE}")
        tags = ', '.join(['Jesus', 'Bible stories', 'KJV', 'scripture', 'faith', 'Christian']
                         + [tagword(t) for t in e['tags']])
        thumb_note = ('(Short — YouTube usually picks its own frame; use this file if the box appears)'
                      if is_short else '← REQUIRED — set this thumbnail')
        out.append(f"""---

## {row:02d} — {p['title']}  ·  {p['duration']}  ·  {'Short' if is_short else 'regular video'}

**UPLOAD THESE:**
- **Video:** `{p['exportPath']}`
- **Thumbnail:** `social/thumbs/yt/row-{row:03d}.jpg` {thumb_note}
- *(later, TikTok/Instagram cover: `social/thumbs/vertical/row-{row:03d}.jpg`)*

**Title:**
```
{e['title']}
```

**Description:**
```
{desc}
```

**Tags:**
```
{tags}
```
""")
    open('social/YOUTUBE-UPLOAD-SHEET.md', 'w').write('\n'.join(out))
    print('sheet regenerated:', len(pj), 'entries')


if __name__ == '__main__':
    main()
