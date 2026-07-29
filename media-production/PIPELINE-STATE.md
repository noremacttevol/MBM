# MBM PIPELINE STATE — the durable record (2026-07-16, Hermes)

> Filed so any machine/session can pick the factory up cold and so the setup is
> reusable for the next batch after the 200 are done. The repo is the memory.

## THE 3-ROLE FACTORY (all eat off GitHub)
1. **Hermes (draft feeder)** — writes `DRAFTS/row-NNN.md` (narration + storyboard).
2. **BRAIN (Linux + Claude)** — draft -> gate-passed `PROMPTS.md` + `make_narration.py`
   + empty `STILLS-WANTED` marker in `build-NN-*`. Template: `build-70-temptations/`.
3. **PAINTER (Windows + Flow)** — sees `STILLS-WANTED` -> paints stills -> pushes.

## THE DURABLE DRAFT FEEDER (leave running / reuse next batch)
- Cron job **"MBM draft feeder"**, id **`8eec9c594d02`**, every **15 min**.
- Each run: pull -> find rows with no `DRAFTS/row-NNN.md` -> write next 4 -> push.
- When every row is drafted it prints "ALL ROWS DRAFTED — nothing to feed" and
  idles harmlessly (no waste, no spam). SAFE to leave running through completion.
- To pause when the 200 are fully done:  `hermes cron pause 8eec9c594d02`
  To resume for the next batch:          `hermes cron resume 8eec9c594d02`

## THE APPROVAL GATE (Hermes) — runs BEFORE any video is built
- `media-production/contact_sheet.py <build-folder>` -> tiles that folder's stills
  into one `<folder>/_review.jpg` for at-a-glance review.
- Hermes vision-reviews each `_review.jpg`, flags bad stills (face law, anatomy,
  baked-in text, off-script, duplicate-in-frame) and hands Cameron the flagged list.
- **No video is assembled until Cameron approves the stills.**

## THE ASSEMBLER (after approval)
- `media-production/generic_build.py <build-folder>` (or run from inside it) turns any
  build-NN folder's stills + `make_narration.py` into a finished captioned video:
  two-voice narration, Ken Burns, caption-v2 wide-bottom, No-Dead-Air, no music bed
  (HUM PURGE), <25 MB H.264 1080x1920, scripture-name output. No per-video tuning.
  PROVEN end-to-end on build-73 (luke-4_this-day-fulfilled.mp4, 18 MB).

## HARD LAWS (tripwires)
- MONEY IS NOT A CONSTRAINT (Cameron, 2026-07-28 — ban LIFTED). Never refuse a
  model/tier/resolution to save money. A paid API still needs a KEY from Cameron.
  See FACTORY-ORDERS.md MONEY RULE #1.
  Flow ULTRA credits are prepaid — spend freely.
- Never make Cameron the machine's hands — his only task is a Google login/CAPTCHA.
- Finish what you start. 2 failed browser attempts = stop and switch.
- ONLY ONE Flow account: run ONE painter, never 4-5 at once (they trip each other's
  CAPTCHA and can lock the account).
- CLAIM-LAW: claim a row (push the folder+marker) BEFORE painting; dedup on the
  build-NN number, one folder per row. See CLAIM-LAW.md.

## REPO IS A PARTIAL CLONE
`~/Desktop/MBM` is a `blob:none` partial clone. To materialize stills locally:
clear skip-worktree flags, then `git checkout HEAD -- media-production/`.

## STATE AT FILING
~1,467 stills materialized; rows 73-170 mostly painted. Reviewed clean so far:
build-73, build-74 (minor soft flags on 74 s6/s7). NEXT SESSION: "run the stills
review report" -> full 90-folder vision pass -> flagged list for Cameron -> approve
-> assemble.
