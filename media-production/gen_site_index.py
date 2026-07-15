#!/usr/bin/env python3
"""Regenerate the GitHub Pages landing page (repo-root index.html) so every
finished story video is watchable at https://noremacttevol.github.io/MBM/ .

It scans media-production/build-NN-*/ for the one scripture-named .mp4 at the
build-folder root (not the per-segment files under segs/ or the raw clips under
assets/), reads its real duration with ffprobe, and writes a clean, phone-first
video gallery in numerical order. Run from the repo root:  python3
media-production/gen_site_index.py
"""
import glob
import os
import re
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Nice display titles keyed by build number (the folder slug drives discovery;
# this map only supplies the human-facing name). Anything not listed falls back
# to a title derived from the filename slug.
TITLES = {
    1: "Woman Who Touched His Cloak", 2: "The Prodigal Son", 3: "Zacchaeus",
    4: "Nicodemus at Night", 5: "The Bent-Over Woman", 6: "The Two Sons",
    7: "Peter Walks on Water", 8: "The Lost Coin", 9: "The Rich Young Ruler",
    10: "The Woman at the Well", 11: "Calming the Storm", 12: "Blind Bartimaeus",
    13: "The Man Through the Roof", 14: "The Ten Lepers",
    15: "The Centurion's Servant", 16: "Mary and Martha", 17: "Lazarus",
    18: "The Road to Emmaus", 19: "Breakfast on the Shore",
    20: "The Good Samaritan", 21: "The Lost Sheep",
    22: "The Unmerciful Servant", 23: "The Workers in the Vineyard",
    24: "The Sower", 25: "The Wheat and the Tares", 26: "The Mustard Seed",
    27: "The Leaven", 28: "The Hidden Treasure", 29: "The Pearl of Great Price",
    30: "The Net", 31: "The Ten Virgins", 32: "The Talents",
    33: "The Sheep and the Goats", 34: "The Rich Fool", 35: "The Great Banquet",
    36: "The Shrewd Steward", 37: "The Rich Man and Lazarus", 38: "The Persistent Widow", 39: "The Pharisee and the Publican",
    40: "The Friend at Midnight", 43: "The Wedding Garment",
    41: "Counting the Cost", 42: "The Barren Fig Tree Spared",
    45: "The Wicked Tenants",
    47: "Houses on Rock and Sand", 48: "New Wine, Old Bottles",
    84: "Calling the Fishermen", 124: "Gethsemane",
}

SMALL = {"of", "and", "the", "a", "an", "in", "on", "to", "his", "her"}


def derive_title(slug):
    words = slug.replace("-", " ").split()
    out = []
    for i, w in enumerate(words):
        out.append(w if (w in SMALL and i) else w.capitalize())
    return " ".join(out)


def scripture(book_chap):
    # "mark-5" -> "Mark 5"; "matthew-13" -> "Matthew 13"
    book, chap = book_chap.rsplit("-", 1)
    return f"{book.capitalize()} {chap}"


def dur(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        s = int(round(float(out.stdout.strip())))
        return f"{s // 60}:{s % 60:02d}"
    except ValueError:
        return ""


def find_main_mp4(build_dir):
    # the finished cut is the single scripture-named mp4 sitting directly in the
    # build folder (book-chap_slug.mp4), never inside segs/ or assets/
    hits = [p for p in glob.glob(os.path.join(build_dir, "*.mp4"))
            if re.match(r"^[a-z]+-\d+_", os.path.basename(p))]
    return hits[0] if hits else None


def main():
    builds = sorted(glob.glob(os.path.join(REPO, "media-production", "build-*")))
    cards = []
    count = 0
    for bd in builds:
        m = re.match(r"build-(\d+)-", os.path.basename(bd))
        if not m:
            continue
        num = int(m.group(1))
        mp4 = find_main_mp4(bd)
        if not mp4:
            continue
        rel = os.path.relpath(mp4, REPO)
        fname = os.path.basename(mp4)
        book_chap = fname.split("_", 1)[0]
        slug = fname.rsplit("_", 1)[1].rsplit(".", 1)[0]
        title = TITLES.get(num, derive_title(slug))
        cards.append((num, title, scripture(book_chap), dur(mp4), rel))
        count += 1

    cards.sort(key=lambda c: c[0])
    rows = []
    for num, title, scrip, length, rel in cards:
        meta = f" · {scrip}" + (f" · {length}" if length else "")
        rows.append(
            f'<div class="card"><p class="title">{num:02d} — {title}'
            f'<span class="meta">{meta}</span></p>\n'
            f'<video controls preload="metadata" playsinline '
            f'src="{rel}"></video></div>')

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MBM — Story Videos</title>
<style>
  :root {{ color-scheme: dark; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 0 16px 64px;
    background: #0f0f12; color: #eee;
    font-family: -apple-system, system-ui, "Segoe UI", Roboto, sans-serif;
    line-height: 1.4;
  }}
  header {{ padding: 24px 0 8px; max-width: 780px; margin: 0 auto; }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  .sub {{ color: #9aa; font-size: 14px; margin: 0 0 4px; }}
  .wrap {{ max-width: 780px; margin: 0 auto; }}
  h2 {{ font-size: 15px; text-transform: uppercase; letter-spacing: .06em;
       color: #8ab; margin: 32px 0 12px; border-bottom: 1px solid #2a2a30;
       padding-bottom: 6px; }}
  .card {{ background: #16161b; border: 1px solid #26262e; border-radius: 14px;
          padding: 12px; margin: 0 0 18px; }}
  .title {{ font-weight: 600; font-size: 16px; margin: 0 0 8px; }}
  .meta {{ color: #889; font-size: 13px; font-weight: 400; }}
  video {{ width: 100%; border-radius: 10px; background: #000; display: block; }}
  .note {{ color: #778; font-size: 13px; margin-top: 8px; }}
</style>
</head>
<body>
<header>
  <h1>Milk Before Meat — Story Videos</h1>
  <p class="sub">Every finished story video. Tap play on any of them — they
  stream on phone or desktop. Stills-only, and the Lord's face is never
  shown (seen only from behind, at a distance, or off-frame).</p>
  <p class="sub">{count} videos.</p>
</header>
<div class="wrap">
<h2>All Story Videos ({count})</h2>
{chr(10).join(rows)}
</div>
</body>
</html>
"""
    out = os.path.join(REPO, "index.html")
    with open(out, "w") as f:
        f.write(html)
    print(f"wrote {out} with {count} videos")
    for num, title, scrip, length, rel in cards:
        print(f"  {num:02d} {title} ({scrip}) {length}")


if __name__ == "__main__":
    main()
