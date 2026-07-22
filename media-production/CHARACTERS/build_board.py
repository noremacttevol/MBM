#!/usr/bin/env python3
"""build_board.py — regenerate Cameron's character approval board.

    python3 CHARACTERS/build_board.py     # writes site/characters.html + web jpgs
    (then, from the repo root:)
    python3 media-production/prune_hosting_versions.py
    FIREBASE_HOSTING_UPLOAD_CONCURRENCY=4 npx firebase deploy --only hosting

Reads every CHARACTERS/<slug>/ that has a SPEC.md and all three views. A sheet
whose SPEC says it is LOCKED renders as approved; anything still pending shows
in a "NEEDS YOUR YES" band at the top, so Cameron always lands on the new ones
first instead of scrolling past 60 he has already approved.
"""
import html
import re
from pathlib import Path

from PIL import Image

CH = Path(__file__).resolve().parent
ROOT = CH.parent.parent
OUT = ROOT / "site" / "characters"
VIEWS = ("face-front", "three-quarter", "full-body")
WEB_H = 760

THE_TWELVE = ("peter", "andrew", "james", "john-beloved", "philip",
              "bartholomew", "matthew", "thomas", "james-son-of-alphaeus",
              "thaddaeus", "simon-the-zealot", "judas-iscariot")


def sheets():
    for d in sorted(CH.iterdir()):
        if not d.is_dir() or not (d / "SPEC.md").is_file():
            continue
        if all((d / f"{v}.jpeg").exists() for v in VIEWS):
            yield d.name


def locked(slug):
    return "LOCKED" in (CH / slug / "SPEC.md").read_text()[:400]


def blurb(slug):
    spec = (CH / slug / "SPEC.md").read_text()
    m = re.search(r"## Written description\n(.*?)\n\n", spec, re.S)
    if not m:
        return ""
    t = " ".join(m.group(1).split())
    t = re.sub(r"\(Adopts?[^)]*\)\s*", "", t)
    return t[:220] + ("…" if len(t) > 220 else "")


def publish_images(slugs):
    OUT.mkdir(parents=True, exist_ok=True)
    for slug in slugs:
        for v in VIEWS:
            im = Image.open(CH / slug / f"{v}.jpeg")
            if im.height > WEB_H:
                im = im.resize((int(im.width * WEB_H / im.height), WEB_H))
            im.save(OUT / f"{slug}--{v}.jpg", quality=78)


def cards(slugs):
    out = []
    for s in slugs:
        name = s.replace("-", " ").title()
        tag = ' <span class="tw">apostle</span>' if s in THE_TWELVE else ""
        imgs = "".join(
            f'<a href="characters/{s}--{v}.jpg" target="_blank">'
            f'<img loading="lazy" src="characters/{s}--{v}.jpg" alt="{name} {v}"></a>'
            for v in VIEWS)
        out.append(f'<div class="card" id="{s}"><h3>{name}{tag}</h3>'
                   f'<div class="views">{imgs}</div>'
                   f'<p class="d">{html.escape(blurb(s))}</p></div>')
    return "\n".join(out)


CSS = """body{background:#17181c;color:#eee;font-family:Georgia,serif;margin:0;padding:16px}
h1{font-size:1.5em}h2{border-bottom:1px solid #444;padding-bottom:4px;margin-top:32px}
.note{background:#243024;border-left:4px solid #6abf69;padding:12px 16px;border-radius:8px;line-height:1.5}
.ask{background:#3a2f1c;border-left:4px solid #e0a83a}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:14px;margin-top:14px}
.card{background:#202127;border-radius:10px;padding:10px}
.card h3{margin:2px 0 8px;font-size:1.05em;color:#ffd98a}
.tw{font-size:.62em;color:#9fd39c;border:1px solid #4a6b48;border-radius:99px;padding:1px 7px;vertical-align:middle}
.views{display:flex;gap:4px}.views img{width:33%;border-radius:6px;display:block}
.d{font-size:.8em;color:#aaa;line-height:1.4}"""


def main():
    all_slugs = list(sheets())
    pending = [s for s in all_slugs if not locked(s)]
    done = [s for s in all_slugs if locked(s)]
    publish_images(all_slugs)

    parts = [f"<!DOCTYPE html><html><head><meta charset='utf-8'>",
             "<meta name='viewport' content='width=device-width,initial-scale=1'>",
             "<title>MBM Character Sheets</title>", f"<style>{CSS}</style>",
             "</head><body>",
             f"<h1>Character Reference Sheets — {len(done)} locked"
             + (f", {len(pending)} awaiting your yes" if pending else "") + "</h1>"]

    if pending:
        parts.append(
            '<div class="note ask"><b>NEW — these need your yes.</b> '
            'Say "characters approved" to lock them, or name the ones to redo '
            'and what is wrong ("older", "different colour"). '
            'Nothing goes into a video until you approve it.</div>'
            f'<div class="grid">{cards(pending)}</div>')

    parts.append(
        '<div class="note">Locked sheets below are binding: every new still that '
        'shows one of these people is generated with their sheet attached, and a '
        'build that skips it fails <code>character_ref_gate.py</code> before any '
        'credit is spent. A locked look only changes if you say so.</div>')

    twelve = [s for s in done if s in THE_TWELVE]
    rest = [s for s in done if s not in THE_TWELVE]
    if twelve:
        parts.append(f"<h2>The Twelve Apostles ({len(twelve)}/12 locked)</h2>"
                     f'<div class="grid">{cards(twelve)}</div>')
    parts.append(f"<h2>Everyone else ({len(rest)})</h2>"
                 f'<div class="grid">{cards(rest)}</div>')
    parts.append("</body></html>")

    (ROOT / "site" / "characters.html").write_text("\n".join(parts))
    print(f"characters.html — {len(done)} locked, {len(pending)} pending, "
          f"{len(all_slugs) * 3} images published")
    if pending:
        print("pending:", ", ".join(pending))


if __name__ == "__main__":
    main()
