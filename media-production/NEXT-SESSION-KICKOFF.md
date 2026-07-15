# NEXT-SESSION KICKOFF — Machine A (paste this into a fresh chat)

> Purpose: continue the MBM video factory in a NEW low-context session. Everything needed
> is in the repo; this file just orients you and states the exact resume point.

---

## Paste-into-a-new-chat prompt

```
This is Machine A of the MBM video factory. Work unattended, use my Google Flow / Ultra
subscription for all stills (Nano Banana 2, 9:16, 1x = 0 credits), NEVER the paid API,
and notify me by pushing each finished video to the gallery.

1. cd to the MBM repo (~/Desktop/Brain/MBM), `git pull --rebase origin main`.
2. Read, in order, and follow exactly:
   - media-production/FACTORY-ORDERS.md   (laws, money rule, my range = rows 45–83)
   - media-production/FLOW-BUILD-PLAYBOOK.md  (the fast, low-token how-to — read this!)
3. First check the browser: list connected Chrome browsers. If none, tell me to reopen
   Chrome + the Claude-in-Chrome extension and stop until it's back. If several, ask me
   which ONE to drive (machine-safety), then proceed with no further questions.
4. RESUME POINT: build-49-water-to-wine is claimed by me and half-built (see state below).
   Finish #49 first (generate stills s2–s12 only; s1 is already done), assemble, publish.
   Then take the next lowest ⬜ row in 45–83 and keep going until my range is built.
```

---

## Exact state at handoff (2026-07-15, THE-200 v2)

**My range (Machine A): rows 45–83.**

| Row | Story | State |
|---|---|---|
| 42 | Barren Fig Tree Spared | ✅ built + **APPROVED** |
| 45 | The Wicked Tenants | ✅ built + **APPROVED** |
| 46 | The Seed Growing Secretly | ✅ built — awaiting Cameron's yes |
| 47, 48 | Houses on rock/sand · New wine | ✅ already built (earlier) |
| **49** | **Water to Wine at Cana** | 🔨 **IN FLIGHT — resume here** |
| 50–83 | (Nobleman's son, First catch of fish, …) | ⬜ not started, in my range |

(44 Two Debtors was built by Computer B; its stale row was ticked. #41/#43/#48 already built.)

## #49 resume detail — no rework needed

`build-49-water-to-wine/` already contains, committed to git:
- `PROMPTS.md` — 12 shots, **face gate PASS** (John 2:1-11; Jesus staged from behind in
  s2/s5/s8/s9/s12; only-Jesus-cream; wedding framed around JOY, not drink).
- `make_narration.py` + `audio/` — all 16 clips rendered (two-voice; jv4/jv7/jv8; sacred
  silences on jv7 + jv8).
- `assets/s1-the-wedding-feast.jpeg` — still 1 of 12, done at 2K.

**To finish #49:** open a NEW Flow project, generate shots **s2 … s12** from the PROMPTS.md
bodies (paste STILL STYLE BLOCK + body), 2K-download each to `assets/<slug>.jpeg` (slugs =
the shot headers). Then copy `build-46/build.py` → change OUT=`john-2_water-to-wine.mp4`,
the S1..S12 constants, the BEATS list (below), KJV={jv4,jv7,jv8}, silences=jv7 & jv8.
Assemble, QC 4 frames, tick row 49, add `49: "Water to Wine at Cana"` to gen_site_index
TITLES, push.

BEATS for #49 build.py:
```
("n1", S1, "in"),
("n2", S2, "in"),
("n3", S3, "in"),
("n4", S4, "in"),
("jv4", S5, "in"), ("n5", S5, "out"),
("n6", S6, "in"),
("n7", S7, "in"),
("jv7", S8, "in"), ("n8", S8, "out"),     # SACRED SILENCE 1
("jv8", S9, "in"), ("n9", S9, "out"),     # SACRED SILENCE 2
("n10", S10, "in"),
("n11", S11, "in"),
("n12", S12, "in"),
```
S-constants (asset filenames): s1-the-wedding-feast, s2-the-guest, s3-the-wine-runs-out,
s4-they-have-no-wine, s5-mine-hour, s6-do-whatever-he-says, s7-the-six-waterpots,
s8-fill-them-with-water, s9-draw-out-now, s10-the-good-wine, s11-the-feast-restored,
s12-they-believed. (All 12 shot bodies are in build-49-water-to-wine/PROMPTS.md.)

## The one blocker that stopped the prior session

The Claude-in-Chrome extension on Machine A disconnected (`list_connected_browsers` → `[]`).
Only the operator can fix it: reopen Chrome and ensure the extension is enabled/connected.
Nothing was lost — all WIP is committed.
