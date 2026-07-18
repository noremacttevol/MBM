#!/usr/bin/env python3
"""Regenerate the GitHub Pages landing page (repo-root index.html) so every
finished story video is watchable at https://noremacttevol.github.io/MBM/ .

It scans media-production/build-NN-*/ for the one scripture-named .mp4 at the
build-folder root (not the per-segment files under segs/ or the raw clips under
assets/), reads its real duration with ffprobe, and reads the approval state
straight out of media-production/QUEUE.md so the page is split into sections:

  🟡 NEEDS YOUR REVIEW  — built, waiting on Cameron's yes  (shown FIRST, on top)
  ✅ APPROVED           — Cameron said yes, not yet posted
  🌐 LIVE IN THE APP    — already shipped (Post ✅)
  🔧 BEING REWORKED     — rejected / in the fix queue

The approval monitor chat runs this after every approve/reject and pushes, so
the live site always matches the board.  Run from the repo root:
  python3 media-production/gen_site_index.py
"""
import glob
import json
import os
import re
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Videos stream straight from GitHub instead of being re-published by Pages, so
# the published site stays tiny (just this HTML) and always deploys. This is the
# same direct-link pattern used by the watch links in STATUS.md.
RAW_BASE = "https://github.com/noremacttevol/MBM/raw/main/"

# The review gallery is hosted on Firebase (milk-b4-meat.web.app/review.html),
# not GitHub Pages — the repo is far over Pages' 1 GB limit, but Firebase only
# uploads the small site/ folder. Videos stream from GitHub (RAW_BASE), so this
# page stays tiny. Deploy with:  firebase deploy --only hosting
OUT_DIR = os.path.join(REPO, "site")
OUT_NAME = "review.html"

# GitHub repo behind the Report-a-problem button + complaint display. Public, so
# the page reads open/closed complaint issues with no token.
GH_OWNER, GH_REPO = "noremacttevol", "MBM"

# Version-lock: Cameron's approval is tied to the EXACT video he watched. We store
# the git blob hash of the mp4 he approved. When a machine rebuilds that video the
# hash changes, the approval auto-falls-off, and it returns to the review list
# flagged "NEW cut." This file is written ONLY by the approval monitor (monitor.py)
# so build machines never conflict on it.
APPROVALS_FILE = os.path.join(REPO, "media-production", "approvals.json")

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
    45: "The Wicked Tenants", 46: "The Seed Growing Secretly",
    47: "Houses on Rock and Sand", 48: "New Wine, Old Bottles",
    49: "Water to Wine at Cana", 50: "The Nobleman's Son",
    51: "The First Catch of Fish", 52: "The Demoniac in the Synagogue",
    53: "Peter's Mother-in-Law", 54: "The Leper Made Clean",
    55: "The Withered Hand", 56: "The Widow of Nain's Son",
    57: "Jairus's Daughter", 58: "Feeding the Five Thousand",
    59: "Feeding the Four Thousand", 60: "The Gerasene Demoniac", 61: "The Syrophoenician Woman", 62: "Ephphatha: the Deaf Man", 63: "The Man Born Blind", 64: "The Pool of Bethesda",
    70: "The Temptations",
    71: "Calling the Fishermen", 72: "Calling Matthew",
    81: "Render Unto Caesar",
    73: "This Day Fulfilled", 74: "The Woman Who Washed His Feet",
    75: "The Woman Taken in Adultery",
    76: "Suffer the Little Children",
    84: "No Room: the Manger", 91: "Gethsemane",
    101: "The Still Small Voice", 102: "Jacob's Ladder", 103: "Peter's Confession", 104: "The Boy Samuel", 105: "Face to Face, as a Friend", 106: "God Spake by the Prophets", 107: "John the Baptist's Doubt", 108: "My Sheep Hear My Voice", 109: "Ask, Seek, Knock", 110: "The Lord's Prayer", 111: "Lilies and Sparrows", 112: "The Beatitudes", 113: "Where Art Thou?", 114: "Abraham Pleads for Sodom", 115: "The Ram in the Thicket", 116: "Graven on His Palms", 117: "Hosea Buys Her Back",
    118: "Jonah and the God Who Relents",
    119: "The Fourth Man in the Fire",
    120: "Job Answered from the Whirlwind",
    121: "Salt and Light", 122: "The Mote and the Beam",
    123: "The Golden Rule",
    124: "Love Your Enemies",
    135: "The Rainbow Covenant",
    151: "If Any of You Lack Wisdom",
    152: "He Revealeth His Secret to the Prophets",
    153: "The Restitution of All Things",
    154: "The Angel with the Everlasting Gospel",
    155: "A Falling Away First",
    156: "A Famine of Hearing the Word",
    157: "A Marvellous Work and a Wonder",
    158: "The Stick of Judah and Joseph",
    159: "Other Sheep I Have",
    162: "The Keys of the Kingdom",
    160: "The Stone Cut Without Hands",
    161: "Called of God, as was Aaron",
    163: "Built on Apostles and Prophets",
    164: "Till We All Come in the Unity of the Faith",
    165: "Laying On of Hands for the Holy Ghost",
    166: "Baptized Again, Properly",
    167: "I Have Chosen You, and Ordained You",
    168: "Born of Water and of the Spirit",
    169: "To Fulfil All Righteousness",
    170: "The Sacrament, Worthily",
}

SMALL = {"of", "and", "the", "a", "an", "in", "on", "to", "his", "her"}


def derive_title(slug):
    words = slug.replace("-", " ").split()
    out = []
    for i, w in enumerate(words):
        out.append(w if (w in SMALL and i) else w.capitalize())
    return " ".join(out)


def scripture(book_chap):
    # "mark-5" -> "Mark 5"; "matthew-13" -> "Matthew 13";
    # numbered books: "1kings-19" -> "1 Kings 19", "2samuel-7" -> "2 Samuel 7"
    book, chap = book_chap.rsplit("-", 1)
    m = re.match(r"^(\d+)([a-z]+)$", book)
    if m:
        book = f"{m.group(1)} {m.group(2).capitalize()}"
    else:
        book = book.capitalize()
    return f"{book} {chap}"


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
            if re.match(r"^[0-9a-z]+-\d+_", os.path.basename(p))]
    return hits[0] if hits else None


def load_approvals():
    """{num(str): {"hash": blob, "date": "YYYY-MM-DD"}} — what Cameron approved
    and which exact cut. Missing/broken file = nothing approved (fresh slate)."""
    try:
        with open(APPROVALS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}


def mp4_hashes():
    """build number -> git blob hash of its finished mp4 (committed). Reads the
    git tree, not the file bytes, so it's instant even for 15 GB of video."""
    out = subprocess.run(
        ["git", "ls-tree", "-r", "HEAD", "--", "media-production"],
        cwd=REPO, capture_output=True, text=True).stdout
    hashes = {}
    for line in out.splitlines():
        try:
            meta, path = line.split("\t", 1)
            _, _typ, h = meta.split()
        except ValueError:
            continue
        m = re.match(r"media-production/build-(\d+)-.*/[0-9a-z]+-\d+_.*\.mp4$", path)
        if m:
            hashes[int(m.group(1))] = h
    return hashes


def parse_queue():
    """Read state from QUEUE.md.

    Returns (appr, post, rejected, reasons):
      appr[num]     -> True if that row's Appr column is ✅ (legacy; page now uses
                       approvals.json for approval + version)
      post[num]     -> True if that row's Post column is ✅
      rejected      -> set of numbers sitting in the Fix queue
      reasons[num]  -> the "What's wrong" text for a rejected video
    """
    path = os.path.join(REPO, "media-production", "QUEUE.md")
    appr, post, rejected, reasons = {}, {}, set(), {}
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return appr, post, rejected, reasons

    section = None
    for line in lines:
        s = line.strip()
        if s.startswith("## "):
            low = s.lower()
            if "fix queue" in low:
                section = "fix"
            elif low.startswith("## the 200"):
                section = "200"
            else:
                section = "other"
            continue
        if not s.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        # parts[0] is '' (before first pipe); real columns start at parts[1]
        if len(parts) < 3 or not re.match(r"^\d+$", parts[1]):
            continue  # skips header + separator rows
        num = int(parts[1])
        if section == "fix":
            rejected.add(num)
            # fix-queue row: '' | # | Story | What's wrong | Claimed by | ''
            if len(parts) > 3 and num not in reasons:
                reasons[num] = parts[3]
        elif section == "200" and len(parts) >= 9:
            # '' | # | Story | Ref | Prep | Built | Appr | Post | notes | ''
            appr[num] = (parts[6] == "✅")
            post[num] = (parts[7] == "✅")
    return appr, post, rejected, reasons


def card_html(num, title, scrip, length, rel, badge="", reason=""):
    meta = f" · {scrip}" + (f" · {length}" if length else "")
    badge_html = f'<p class="badge">{badge}</p>\n' if badge else ""
    reason_html = f'<p class="reason">{reason}</p>\n' if reason else ""
    return (
        f'<div class="card" id="v{num}" data-num="{num}">'
        f'<p class="title">{num:02d} — {title}<span class="meta">{meta}</span></p>\n'
        f'{badge_html}{reason_html}'
        f'<video controls preload="metadata" playsinline src="{RAW_BASE}{rel}"></video>\n'
        f'<div class="complaints" data-num="{num}"></div>\n'
        f'<button class="report" onclick="report({num}, this)">🚩 Report a problem</button>'
        f'</div>')


def section_html(heading, blurb, cards):
    if not cards:
        return ""
    body = "\n".join(card_html(*c) for c in cards)
    intro = f'<p class="note">{blurb}</p>\n' if blurb else ""
    return f'<h2>{heading} ({len(cards)})</h2>\n{intro}{body}'


def details_section_html(heading, blurb, cards):
    """Collapsed drop-down — keeps the good/done videos off the review view but
    one click away. Separates 'the good from the bad' on the page."""
    if not cards:
        return ""
    body = "\n".join(card_html(*c) for c in cards)
    intro = f'<p class="note">{blurb}</p>\n' if blurb else ""
    return (f'<details><summary>{heading} ({len(cards)})</summary>\n'
            f'{intro}{body}\n</details>')


def main():
    builds = sorted(glob.glob(os.path.join(REPO, "media-production", "build-*")))
    cards = []
    for bd in builds:
        m = re.match(r"build-(\d+)-", os.path.basename(bd))
        if not m:
            continue
        num = int(m.group(1))
        mp4 = find_main_mp4(bd)
        if not mp4:
            continue
        rel = os.path.relpath(mp4, REPO).replace(os.sep, "/")
        fname = os.path.basename(mp4)
        book_chap = fname.split("_", 1)[0]
        slug = fname.rsplit("_", 1)[1].rsplit(".", 1)[0]
        title = TITLES.get(num, derive_title(slug))
        cards.append((num, title, scripture(book_chap), dur(mp4), rel))

    cards.sort(key=lambda c: c[0])
    appr, post, rejected, reasons = parse_queue()
    approvals = load_approvals()
    hashes = mp4_hashes()

    # Approval is tied to the EXACT cut Cameron watched (its git blob hash). A
    # rebuilt video no longer matches its approved hash, so it falls out of
    # Approved and back into review flagged "NEW cut." Rejected videos (fix queue)
    # show their complaint. Live-in-app means nothing here — only Cameron's yes.
    review, approved, rework = [], [], []
    for num, title, scrip, length, rel in cards:
        ap = approvals.get(str(num))
        if num in rejected:
            rework.append((num, title, scrip, length, rel, "", reasons.get(num, "")))
        elif ap and hashes.get(num) == ap.get("hash"):
            approved.append((num, title, scrip, length, rel, "", ""))
        elif ap:  # approved before, but the video was rebuilt since
            review.append((num, title, scrip, length, rel,
                           f"🔁 NEW cut — this changed since you approved it "
                           f"({ap.get('date','')}). Re-watch to confirm.", ""))
        else:
            review.append((num, title, scrip, length, rel, "", ""))

    count = len(cards)
    # Only the review list is open on load. The good/done/reworking ones fold
    # into collapsed drop-downs so Cameron opens straight to what needs his yes.
    sections = "\n".join(s for s in [
        section_html(
            "🟡 Needs your review",
            "Built and waiting on your yes. Watch these, then tell the monitor "
            "which are good — they drop into Approved and leave this list.",
            review),
        '<h2 class="done-head">Done — tap to open</h2>',
        details_section_html(
            "✅ Approved",
            "You said yes. Queued to post to the app.",
            approved),
        details_section_html(
            "🔧 Being reworked",
            "You flagged something — a build machine is remaking these.",
            rework),
    ] if s)

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
       color: #8ab; margin: 32px 0 6px; border-bottom: 1px solid #2a2a30;
       padding-bottom: 6px; }}
  .card {{ background: #16161b; border: 1px solid #26262e; border-radius: 14px;
          padding: 12px; margin: 0 0 18px; }}
  .title {{ font-weight: 600; font-size: 16px; margin: 0 0 8px; }}
  .meta {{ color: #889; font-size: 13px; font-weight: 400; }}
  video {{ width: 100%; border-radius: 10px; background: #000; display: block; }}
  .note {{ color: #778; font-size: 13px; margin: 0 0 12px; }}
  .done-head {{ color: #667; border-bottom-color: #202028; }}
  details {{ margin: 0 0 10px; }}
  summary {{ cursor: pointer; list-style: none; user-select: none;
             font-size: 15px; font-weight: 600; color: #7c9;
             background: #14140f; border: 1px solid #26262e; border-radius: 12px;
             padding: 12px 14px; }}
  summary::-webkit-details-marker {{ display: none; }}
  summary::before {{ content: "▸ "; color: #567; }}
  details[open] > summary::before {{ content: "▾ "; }}
  details[open] > summary {{ margin-bottom: 14px; }}
  .badge {{ background: #2a2410; border: 1px solid #6a5a1e; color: #e8cf7a;
            border-radius: 8px; padding: 8px 10px; margin: 0 0 8px;
            font-size: 13px; font-weight: 600; }}
  .reason {{ background: #2a1414; border: 1px solid #6a2a2a; color: #f0b4b4;
             border-radius: 8px; padding: 8px 10px; margin: 0 0 8px;
             font-size: 13px; }}
  .report {{ margin-top: 10px; width: 100%; cursor: pointer;
             background: #201014; color: #f0a9b8; font-size: 14px; font-weight: 600;
             border: 1px solid #52242e; border-radius: 10px; padding: 10px; }}
  .report:hover {{ background: #2a1218; }}
  .complaint {{ border-radius: 8px; padding: 8px 10px; margin: 8px 0 0;
                font-size: 13px; }}
  .complaint.open {{ background: #2a1414; border: 1px solid #6a2a2a; color: #f0b4b4; }}
  .complaint.fixed {{ background: #14210f; border: 1px solid #2e5a24; color: #b6e6a4; }}
  .complaint a {{ color: inherit; opacity: .7; }}
</style>
</head>
<body>
<header>
  <h1>Milk Before Meat — Story Videos</h1>
  <p class="sub">Watch the ones waiting on your yes. Something wrong? Tap
  <b>Report a problem</b> — it saves to GitHub and stays on the video until a
  newer version fixes it.</p>
  <p class="sub">{count} videos · {len(review)} waiting on your review · {len(approved)} approved.</p>
</header>
<div class="wrap">
{sections}
</div>
<script>
var GH = "{GH_OWNER}/{GH_REPO}";
function esc(s){{ var d=document.createElement('div'); d.textContent=s||""; return d.innerHTML; }}
function report(num, btn){{
  var card = btn.closest('.card');
  var title = card.querySelector('.title').textContent.split('·')[0].replace(/^[0-9]+\\s*—\\s*/, '').trim();
  var what = window.prompt("What's wrong with #" + num + " (" + title + ")? Keep it short.");
  if(!what) return;
  var url = "https://github.com/" + GH + "/issues/new?labels=complaint"
    + "&title=" + encodeURIComponent("Video #" + num + " — " + title)
    + "&body=" + encodeURIComponent(what + "\\n\\n(filed from the review page — stands until a newer cut fixes it)");
  window.open(url, "_blank");
}}
// Pull Cameron's complaints straight from GitHub and pin them to each video.
fetch("https://api.github.com/repos/" + GH + "/issues?state=all&labels=complaint&per_page=100")
 .then(function(r){{ return r.ok ? r.json() : []; }})
 .then(function(issues){{
   if(!Array.isArray(issues)) return;
   issues.forEach(function(is){{
     var m = /#(\\d+)/.exec(is.title || "");
     if(!m) return;
     var slot = document.querySelector('.complaints[data-num="' + m[1] + '"]');
     if(!slot) return;
     var first = (is.body || "").split("\\n")[0].trim();
     var open = is.state === "open";
     var div = document.createElement('div');
     div.className = 'complaint ' + (open ? 'open' : 'fixed');
     div.innerHTML = (open ? "🚩 Complaint: " : "✅ Fixed: ") + esc(first)
       + ' <a href="' + is.html_url + '" target="_blank">#' + is.number + '</a>';
     slot.appendChild(div);
   }});
 }})
 .catch(function(){{}});
</script>
</body>
</html>
"""
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, OUT_NAME)
    with open(out, "w") as f:
        f.write(html)
    print(f"wrote {out} with {count} videos")
    print(f"  review={len(review)} approved={len(approved)} "
          f"rework={len(rework)}")


if __name__ == "__main__":
    main()
