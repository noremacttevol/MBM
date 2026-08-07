# SCHEDULE — cadence and posting order

## The order (Cameron's call, 2026-08-07)

**Lowest row number first: 01, 02, 03…** The numbers are the order only — they
never go in a title or caption. The full ordered list with per-platform boxes is
the board in `TRACKER.md`; work it top to bottom on every platform.

## The cadence (simple on purpose)

- **YouTube already has the full library** (bulk-uploaded 2026-08-07 from
  `YOUTUBE-UPLOAD-SHEET.md`). This calendar governs Instagram, TikTok, and
  Facebook going forward — and any video the YouTube bulk pass missed.
- **One video per day per platform, in row order, 7:00 PM Eastern.** Daily posting
  is the single biggest lever on these platforms — a page that posts steadily gets
  fed to new people; a page that posts in bursts doesn't. Consistency beats
  clever timing.
- **Instagram skips videos over 3:00** (Reels cap). On those days Instagram simply
  posts nothing — it moves to the next short one the following day. Never trim a
  video to fit; editing a cut voids your approval.
- **Upload the file exactly as it is.** No platform sounds, no filters, no
  auto-captions, no "enhance." The silence is intentional and the captions are
  already burned in.

## The weekly rhythm (about an hour, once a week)

**Sunday afternoon — schedule the whole week (~45–60 min):**
1. **Facebook + Instagram together:** Meta Business Suite → Create Reel → schedule
   the next 7 row numbers for both platforms in one pass.
2. **TikTok:** tiktok.com on the computer → upload → Schedule (up to ~10 days ahead).
3. Tick the boxes in `TRACKER.md` as you schedule.

**Daily — 10 to 15 minutes:** open each app once, reply to comments and DMs (voice
rules in `GROWTH-PLAYBOOK.md`), check the message-requests folders. Replying in the
first hours after posting matters more than any hashtag.

## Day 1 note

Post video 01 — The Woman Who Touched His Cloak — then pin it on every platform
(pin to profile on IG/TikTok, pin to top on Facebook, set as the pinned comment or
channel trailer on YouTube). It's the app's signature story and the front door.

## When new videos are approved

Rerun `python3 social/refresh-postable.py`, add the caption entry in
`POST-QUEUE.md`, add the row to `TRACKER.md` — it slots into the order by its
number automatically.
