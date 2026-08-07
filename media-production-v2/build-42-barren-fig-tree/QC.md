# QC / RUNNER HANDOFF — build-42-barren-fig-tree (Luke 13:6-9)

Lesson-12 pass done 2026-08-05 (Machine A). `--check` PASSES, zero WARNs.
35 beats, 200.3 s. Audio OK on AUTHOR-BOARD. No open reviewer complaint
on this row.

## Coverage shape (lesson 12)

Three true wides with stated camera geometry: b01 (square establish),
b13 (the axe order — owner, gardener, tree side-on in profile), b18 (THE
INTERCESSION — the camera holds the line owner → gardener → trunk in
profile so the stepping-BETWEEN reads at a glance). Fifteen former wides
are now tighter shots — most were single figures or empty landscapes
where the multi-people wide block would have INJECTED people (the row-11
"someone climbing the mast / pouring water into the boat" complaint
class: extra people doing wrong things because the prompt demanded a
crowd the story doesn't have).

## Place plates (lesson 11) — both places are PROMOTE-FIRST

| Token | Promote from | Then covers |
|---|---|---|
| FIGTREE | b05 `assets/s05-the-privilege-mapped...` (person-free landscape of the corner: tree + wall + vine rows — the ideal plate) | every FIGTREE beat (b04-b30, b35) |
| SQUARE | b01 `assets/s01-he-told-them-a-short.jpeg` | b02 b03 b17 b27 b32 b33 b34 |

Generate b05 FIRST (before b04) so the tree exists before anyone stands
under it, promote it, then do the rest.

## Complaint-corpus checks (from Cameron's 77-row review history — apply
to every frame of this build)

- **Direction anchored (row-83 class: "walking the wrong way"):** b10 the
  owner walks AWAY and the tree must be visible behind him so the
  direction reads; b25 the gardener carries the axe AWAY down the path.
  Ask of every frame: does each figure's travel/gaze line point at the
  thing the narration says it points at, with that thing IN FRAME or its
  direction unmistakable?
- **No giants (rows 56/69/83/107/112 class):** in every square frame,
  Jesus's height is compared against the nearest standing adult before
  accepting. Same check for owner vs gardener at the tree.
- **Beard/identity drift (rows 32/62/91/102 class — Cameron ordered a
  beard QC):** the OWNER's clipped grey beard and the GARDENER's soft
  dark beard must survive every frame including small/distant renders.
  Face-board both men across all their frames before assembly.
- **Same-tree law (row-11 "different boat every picture" class):** the
  fig's forked grey trunk, the wall two paces behind, the vine rows
  downhill — identical in every tree frame. That is what the b05 plate
  is for; reroll any frame where the tree reads as a different tree.
- **Count law (row-135 class):** b04/b09 "no fruit, not one" — zero figs
  visible under any leaf; b35 buds only, still NO figs (the ending is
  open — a fruited tree breaks the parable).

## Row-specific traps

- The AXE never swings and never touches wood — carried, leaned, carried
  away. Any chopping/felling frame is an automatic reject (mercy law).
- Season arc must run one direction: late-summer (b04-b16) → hard noon
  (b13/b18) → autumn digging (b20-b25) → winter's edge (b26-b29) →
  next spring (b35). No season may flash back after its window.
- The dung/feeding beats (b22) are earthy but clean — baskets and dark
  soil, nothing gross.
- b30's detail: the gardener's mattock lies at the ring's edge — his
  tool, not the owner's axe. Do not swap them.
- Only Jesus wears cream (square beats); owner walnut-brown, gardener
  moss-green throughout.
- Person-free frames: b05 b06 b07 b09 b12 b16 b26 b28 b30 b35 — do not
  let the model add figures.

## RUNNER QC LOG — first-attempt V2 cut (Machine A, 2026-08-05)
35/35 at 2K. Portraits OWNER+GARDENER wired via REFS; FIGTREE (b05, person-free
landscape) and SQUARE (b01) promoted as plates before any other beat.
REROLLED 2: b04 and b22 both came back as MULTI-PANEL COLLAGES (4-up and 3-up
grids inside one 9:16 frame) instead of a single picture — obvious garbage, cured.
PASSED: intercession staged side-on so gardener-between-owner-and-tree reads;
tree state follows the story (leafy → bare → the green shoot at the end); only
Jesus in cream; no phantom people in the wides; no modern objects.
Row ~$4.9; meter 236.64.

## COMPLAINT LEDGER
- **OPEN (reportedAgainst b35fd2a17, the 2026-08-05 cut): "the captions are
  messed up multiple times match them up to the words, the correct wordage."**
  FIXED in this C-FIX re-cut (2026-08-07, Machine A). ROOT CAUSE: this was NOT a
  wording defect — every caption's TEXT already matched the spoken audio (verified
  caption text == each segment's timing.json). It was a whole-video TIMING drift.
  The `beats_v2.py` still-windows were scaffolded from a STALE `beats.json`
  (a 200 s narration timeline, timeline "A") written BEFORE the Jul-29 "REDO #42:
  new voice + pacing" re-voice lengthened the real audio to 223 s (timeline "B").
  The assembler places captions on the LIVE `extract_beats` timeline (B, correct)
  but places the STILLS on `beats_v2.py` windows (A, stale). Result: pictures ran
  progressively AHEAD of the words — 0 s early, ~12 s by the climax — and the last
  still froze ~19 s while two narrators played under it. Measured proof of the
  anomaly: good rows 45/41 have `beats_v2 last-window-end` within 0.1 s of
  `extract card_start`; row 42 was off by +12.56 s.
  THE FIX (assembly-only, audio untouched): built a monotonic piecewise-linear
  A→B time map anchored on the 18 stable segment boundaries (audio_start +
  spoken_end) and remapped all 35 window values in `beats_v2.py` to timeline B
  (e.g. jv9 s25 138.24-143.81 → 146.61-152.11, matching audio jv9 at 146.33-151.76).
  Re-assembled: **AUDIO LOCK PASS** (SHA256 f46238109083…cace335 — the narration is
  byte-identical to the cut Cameron already has). Re-verified 7 timeline points +
  the card from the RENDERED mp4: still + caption + spoken word now agree at
  t=100 (jv8), 140 (n8), 150 (jv9), 175 (n10), 200 (n11), 210 (n12), 219 (card).
  NO pictures rerolled, NO re-voice, $0.00 Gemini spend, 0 rerolls.
