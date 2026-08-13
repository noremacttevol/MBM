#!/usr/bin/env python3
"""make-per-video.py — one publish-info file per video, all 200, numbered names.

Cameron (2026-08-07): "make it a file for the 200 and the number as the file
title only and then in there give me the info for each video in a file that i
can open when publishing each video."

Output: social/per-video/001.md ... 200.md — each file carries EVERYTHING that
posts with that video on all four platforms, in fenced blocks he can copy:
  YouTube title / YouTube description / YouTube tags
  Facebook post (caption + base hashtags, one paste)
  TikTok caption (caption + TikTok hashtags, one paste)
  Instagram caption (caption + Instagram hashtags, one paste)
Every description carries the milkb4meat.org link (the only link, ever).

Content sources, in order of authority:
  1. APPROVED rows — the exact text already used on the first publishes:
     social/POST-QUEUE.md (captions/titles/hashtag lines) +
     social/YOUTUBE-UPLOAD-SHEET.md (YouTube descriptions + tag lists).
  2. Everything else — social/captions-authored.json (written 2026-08-07 in the
     same voice; each file says DRAFT until the row is approved, because a
     story swap before approval voids its captions).

Caption laws baked in: never "word for word"; no hype; one honest mirror
question; milkb4meat.org is the only link. Rerun after new approvals (the
refresh loop) — approved rows automatically switch from DRAFT to APPROVED text.
"""
import json
import os
import re

QUEUE_MD = "media-production/QUEUE.md"
POST_QUEUE = "social/POST-QUEUE.md"
YTSHEET = "social/YOUTUBE-UPLOAD-SHEET.md"
AUTHORED = "social/captions-authored.json"
POSTABLE = "social/postable.json"
OUTDIR = "social/per-video"

BASE = "#Jesus #BibleStories #Scripture #KJV #Faith"
YT_BASE_TAGS = "Jesus, Bible stories, KJV, scripture, faith, Christian"
APP_LINE_URL = ("Download the free Milk Before Meat app for every story and "
                "more:\nhttps://milkb4meat.org")
APP_LINE_BIO = ("Download the free Milk Before Meat app for every story and "
                "more — link in bio.")


def the200():
    t = open(QUEUE_MD, encoding="utf-8").read()
    start = t.index("| # | Story | Ref | Prep |")
    rows = {}
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
                         t[start:], re.M):
        n = int(m.group(1))
        if 1 <= n <= 200 and n not in rows:
            rows[n] = {"title": m.group(2).strip(), "ref": m.group(3).strip()}
    return rows


def parse_post_queue():
    text = open(POST_QUEUE, encoding="utf-8").read()
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
            "ig_tags": ig_m.group(1).strip() if ig_m else BASE + " #Christian #Bible",
            "tk_tags": tk_m.group(1).strip() if tk_m else BASE + " #ChristianTikTok #Bible",
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


def from_authored(a):
    """Build the four platform texts from an authored caption set."""
    caption = "%s\n%s\n%s, from the KJV. %s" % (
        a["body"], a["question"], a["ref_line"], APP_LINE_BIO)
    yt_desc = "%s\n\n%s\n\n%s, from the KJV.\n\n%s" % (
        a["body"], a["question"], a["ref_line"], APP_LINE_URL)
    story = " ".join(a.get("story_tags", []))
    return {
        "yt_title": a["yt_title"],
        "yt_desc": yt_desc,
        "yt_tags": (YT_BASE_TAGS + ", " + a["yt_tags_extra"]).strip(", "),
        "caption": caption,
        "ig_tags": (BASE + " #Christian #Bible " + story).strip(),
        "tk_tags": (BASE + " #ChristianTikTok #Bible " + story).strip(),
    }


def fence(text):
    return "```\n" + text.strip() + "\n```"


def main():
    rows = the200()
    pq = parse_post_queue()
    yts = parse_ytsheet()
    authored = {a["row"]: a for a in json.load(open(AUTHORED))} \
        if os.path.exists(AUTHORED) else {}
    try:
        postable = {p["row"]: p for p in json.load(open(POSTABLE))["postable"]}
    except (OSError, ValueError):
        postable = {}

    os.makedirs(OUTDIR, exist_ok=True)
    n_appr = n_draft = n_missing = 0
    for n in sorted(rows):
        meta = rows[n]
        if n in pq and n in yts:
            c = {**pq[n], **yts[n]}
            status = ("APPROVED — post the byte-verified file "
                      "`social/exports/%s`" %
                      postable[n]["exportPath"].split("/")[-1]
                      if n in postable else
                      "APPROVED text (re-run refresh-postable.py for the file)")
            n_appr += 1
        elif n in authored:
            c = from_authored(authored[n])
            status = ("DRAFT — video not approved yet. When Cameron approves "
                      "it, rerun `python3 social/make-per-video.py` (the text "
                      "below is ready; a story swap before approval would "
                      "void it).")
            n_draft += 1
        else:
            n_missing += 1
            continue

        fb = c["caption"] + "\n\n" + BASE
        tk = c["caption"] + "\n\n" + c["tk_tags"]
        ig = c["caption"] + "\n\n" + c["ig_tags"]

        body = f"""# {n:03d} — {meta['title']} ({meta['ref']})

**Status:** {status}
**Thumbnails:** YouTube `social/thumbs/yt/row-{n:03d}.jpg` · TikTok/IG cover `social/thumbs/vertical/row-{n:03d}.jpg` (exist once approved)
**Rule of thumb:** 3:00 or less = YouTube Short. Over 3:00 = regular YouTube upload — set the thumbnail. Instagram takes any length (over 3:00 reaches mostly followers — post it anyway). Facebook: any upload becomes a Reel automatically.
**After posting:** tick this video's chips on the reviewer (milk-b4-meat.web.app/review.html, bottom).

## YouTube — Title
{fence(c['yt_title'])}

## YouTube — Description
{fence(c['yt_desc'])}

## YouTube — Tags (Studio → Show more → Tags)
{fence(c['yt_tags'])}

## Facebook — the whole post (one paste)
{fence(fb)}

## TikTok — the whole caption (one paste)
{fence(tk)}

## Instagram — the whole caption (one paste)
{fence(ig)}
"""
        open(os.path.join(OUTDIR, "%03d.md" % n), "w", encoding="utf-8").write(body)

    print("per-video files: %d approved, %d draft, %d missing captions"
          % (n_appr, n_draft, n_missing))


if __name__ == "__main__":
    main()
