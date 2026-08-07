#!/usr/bin/env python3
"""make-post-kit.py — build site/post-kit.html, Cameron's one-tap posting page.

Cameron (2026-08-07): "i need copy and paste sections for every words that
should go with each video and where it goes to and if its more than 3 minutes
or whatever idk how to deal with each platform different so you need to help
me with that."

So: ONE page, one card per approved video in posting order. Every platform
gets its own labeled box with a COPY button — the box already contains the
complete text for that platform (caption + the right hashtags), and the label
says exactly where to paste it. The over-3:00 rule is baked in: those videos
show a SKIP banner on Instagram instead of a box. Nothing to assemble,
nothing to remember.

Sources (regenerate any time approvals change — run from repo root):
  social/postable.json          the byte-verified approved list (order + files)
  social/POST-QUEUE.md          captions, YouTube titles, per-platform hashtags
  social/YOUTUBE-UPLOAD-SHEET.md  YouTube descriptions + tag lists

Output: site/post-kit.html  (deploy with `firebase deploy --only hosting`)
"""
import html
import json
import re

POSTABLE = "social/postable.json"
QUEUE = "social/POST-QUEUE.md"
YTSHEET = "social/YOUTUBE-UPLOAD-SHEET.md"
OUT = "site/post-kit.html"

BASE_TAGS = "#Jesus #BibleStories #Scripture #KJV #Faith"


def parse_queue():
    text = open(QUEUE, encoding="utf-8").read()
    entries = {}
    for block in re.split(r"(?=^### Row )", text, flags=re.M)[1:]:
        num = int(re.match(r"### Row (\d+)", block).group(1))
        title_m = re.search(r"^\*\*YouTube title:\*\* (.+)$", block, re.M)
        cap_m = re.search(r"^\*\*Caption:\*\*\n(.*?)(?=^\*\*Story tags)", block,
                          re.M | re.S)
        ig_m = re.search(r"^\*\*Instagram hashtags:\*\* `([^`]+)`", block, re.M)
        tk_m = re.search(r"^\*\*TikTok hashtags:\*\* `([^`]+)`", block, re.M)
        entries[num] = {
            "yt_title": title_m.group(1).strip() if title_m else "",
            "caption": cap_m.group(1).strip() if cap_m else "",
            "ig_tags": ig_m.group(1).strip() if ig_m else None,  # None = skip IG
            "tk_tags": tk_m.group(1).strip() if tk_m else BASE_TAGS,
            "fits_all": "fits all four" in block,
        }
    return entries


def parse_ytsheet():
    text = open(YTSHEET, encoding="utf-8").read()
    entries = {}
    for block in re.split(r"(?=^## \d+ — )", text, flags=re.M)[1:]:
        num = int(re.match(r"## (\d+) —", block).group(1))
        desc_m = re.search(r"\*\*Description:\*\*\n```\n(.*?)\n```", block, re.S)
        tags_m = re.search(r"\*\*Tags:\*\*\n```\n(.*?)\n```", block, re.S)
        entries[num] = {
            "yt_desc": desc_m.group(1).strip() if desc_m else "",
            "yt_tags": tags_m.group(1).strip() if tags_m else "",
        }
    return entries


def esc(s):
    return html.escape(s, quote=False)


def block(label, where, text, bid):
    return f"""
<div class="box">
  <div class="boxhead"><span class="lbl">{esc(label)}</span>
    <span class="where">{esc(where)}</span>
    <button class="copy" data-t="{bid}">COPY</button></div>
  <pre id="{bid}">{esc(text)}</pre>
</div>"""


def main():
    postable = json.load(open(POSTABLE))["postable"]
    queue = parse_queue()
    yts = parse_ytsheet()

    cards = []
    for p in postable:
        n = p["row"]
        q = queue.get(n)
        y = yts.get(n, {"yt_desc": "", "yt_tags": ""})
        if not q:
            continue
        dur = p.get("duration", "")
        short = q["fits_all"]
        fname = p["exportPath"].split("/")[-1]
        fb_text = q["caption"] + "\n\n" + BASE_TAGS
        tk_text = q["caption"] + "\n\n" + q["tk_tags"]

        boxes = []
        boxes.append(block("YouTube — Title",
                           "YouTube Studio → Details → Title box",
                           q["yt_title"], f"v{n}yt_t"))
        boxes.append(block("YouTube — Description",
                           "YouTube Studio → Details → Description box",
                           y["yt_desc"], f"v{n}yt_d"))
        boxes.append(block("YouTube — Tags",
                           "YouTube Studio → Show more → Tags box",
                           y["yt_tags"], f"v{n}yt_g"))
        boxes.append(block("Facebook — the whole post",
                           "Facebook → Create Reel/Post → text box (one paste)",
                           fb_text, f"v{n}fb"))
        boxes.append(block("TikTok — the whole caption",
                           "TikTok → Post → caption box (one paste)",
                           tk_text, f"v{n}tk"))
        # Instagram takes every video (20-min Reel limit, verified 2026-08-07).
        # Over 3:00 the only difference is reach: IG shows those mostly to
        # existing followers, so the card says that instead of skipping.
        ig_text = q["caption"] + "\n\n" + (q["ig_tags"] or BASE_TAGS +
                                           " #Christian #Bible")
        boxes.append(block("Instagram — the whole caption",
                           "Instagram → New Reel → caption box (one paste)",
                           ig_text, f"v{n}ig"))
        ig_note = "" if short else (
            '<div class="note">⏱ Over 3:00 — Instagram allows it (Reels go up '
            'to 20 minutes now), but IG only recommends Reels over 3:00 to '
            'people who already follow you. Post it anyway — new-viewer '
            'discovery comes from the short videos.</div>')

        kind = ("YouTube Short" if short
                else "YouTube regular upload (SET THE THUMBNAIL — it matters)")
        thumb_note = (f"Video file: <b>{esc(fname)}</b> (in social/exports/) "
                      f"&nbsp;·&nbsp; YouTube thumbnail: <b>row-{n:03d}.jpg</b> "
                      f"(social/thumbs/yt/) &nbsp;·&nbsp; TikTok/IG cover: "
                      f"<b>row-{n:03d}.jpg</b> (social/thumbs/vertical/)")

        cards.append(f"""
<details class="card" id="row{n}">
<summary><span class="num">{n:02d}</span> {esc(p['title'])}
  <span class="meta">{esc(p.get('scripture',''))} · {esc(dur)} · {esc(kind)}</span></summary>
<div class="files">{thumb_note}</div>
{ig_note}
{''.join(boxes)}
<div class="donebar">When all posted: tick this video's chips on the
<a href="review.html#social">live tracker</a>.</div>
</details>""")

    page = f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MBM Post Kit — copy &amp; paste for every video</title>
<style>
 body{{font-family:system-ui,sans-serif;margin:0;background:#111;color:#eee;
      padding:12px;max-width:760px;margin:0 auto}}
 h1{{font-size:1.3em}} .sub{{color:#aaa;font-size:.95em;line-height:1.5}}
 .card{{background:#1c1c1e;border:1px solid #333;border-radius:10px;
       margin:10px 0;padding:0 12px}}
 summary{{cursor:pointer;padding:12px 0;font-weight:600;font-size:1.05em}}
 .num{{display:inline-block;background:#2e5c2e;color:#fff;border-radius:6px;
      padding:1px 8px;margin-right:6px}}
 .meta{{display:block;font-weight:400;color:#9a9;font-size:.85em;margin-top:2px}}
 .files{{font-size:.85em;color:#bbb;background:#222;border-radius:8px;
        padding:8px;margin-bottom:8px;line-height:1.6}}
 .box{{margin:10px 0}}
 .boxhead{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
 .lbl{{font-weight:700}}
 .where{{color:#8ab;font-size:.8em;flex:1}}
 .copy{{background:#2563eb;color:#fff;border:0;border-radius:8px;
       padding:8px 18px;font-size:1em;font-weight:700;cursor:pointer}}
 .copy.ok{{background:#16a34a}}
 pre{{white-space:pre-wrap;background:#0c0c0d;border:1px solid #2a2a2c;
     border-radius:8px;padding:10px;font-size:.9em;line-height:1.45;
     font-family:inherit;margin:6px 0 0}}
 .skip{{background:#4a1d1d;border:1px solid #7f1d1d;color:#fecaca;
       border-radius:8px;padding:10px;margin:10px 0;font-weight:600}}
 .note{{background:#3a2f10;border:1px solid #7a5c1a;color:#fde68a;
       border-radius:8px;padding:10px;margin:10px 0}}
 .donebar{{color:#9a9;font-size:.85em;padding:10px 0 14px}}
 a{{color:#7ab7ff}}
</style></head><body>
<h1>📤 MBM Post Kit — every video, ready to paste</h1>
<p class="sub">Work top to bottom — the number is the posting order. Tap a video
to open it. Every box has a <b>COPY</b> button and says exactly where the text
goes. Every video posts to all four platforms; on videos over 3:00 the card
carries a heads-up about Instagram reach — you never have to figure out
platform rules. Upload files live on the computer
in <b>social/exports/</b>; thumbnails in <b>social/thumbs/</b>. After posting,
tick the chips on the <a href="review.html#social">live tracker</a>.</p>
{''.join(cards)}
<script>
document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',async()=>{{
  const t=document.getElementById(b.dataset.t).textContent;
  try{{await navigator.clipboard.writeText(t);}}
  catch(e){{const ta=document.createElement('textarea');ta.value=t;
    document.body.appendChild(ta);ta.select();document.execCommand('copy');
    ta.remove();}}
  b.textContent='COPIED ✓';b.classList.add('ok');
  setTimeout(()=>{{b.textContent='COPY';b.classList.remove('ok');}},1600);
}}));
</script></body></html>"""
    open(OUT, "w", encoding="utf-8").write(page)
    print(f"wrote {OUT}: {len(cards)} video cards")


if __name__ == "__main__":
    main()
