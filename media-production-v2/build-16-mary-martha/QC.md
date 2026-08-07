# QC / RUNNER HANDOFF — build-16-mary-martha

## 🅿️ NEEDS-REBUILD — NEW open complaint AUTHOR-FIXED (2026-08-07, Machine A `Dev`, $0 Fable-5 lane)

**COMPLAINT LEDGER — SECOND, still-open complaint** (the earlier "headless person at 0:42" was
already C-FIX-shipped; the review board's `latest` is now this one):
> "the picture at 1:31 - 1:32 of jesus standing and looking mean needs to be removed. all the other
> ones are good enough that one for a breif second isnt needed."

- **The 1:31-1:32 frame was `s16-the-room-went-quiet.jpeg` (beat v2-r016-b16, window 91.32-92.76)** —
  a 1.44s wide of Jesus turned toward Martha that rendered stern/"mean." Cameron asked to REMOVE it
  and confirmed the rest are good.
- **AUTHOR FIX ($0, no image gen):** **REMOVED beat b16 entirely.** Its window is absorbed into the
  very next beat **b17 "not-a-scolding"** (the tender close-up of Jesus's warm, fond, NOT-a-scolding
  face), now widened to **91.32-100.53** — so "the whole room went quiet" + "answered her gently"
  both play over the warm face, the exact opposite of the mean read. **26 → 25 beats**, `--check` PASS
  (windows contiguous, no gap at 91.32). Audio UNTOUCHED.
- **🅿️ RUNNER — do this ($0-ish re-cut, no new image):** re-assemble the row WITHOUT `s16` — do NOT
  generate any new still; `s17-not-a-scolding.jpeg` already exists and now covers the extended window.
  **AUDIO LOCK byte-identical**, ship with a card telling Cameron the mean-looking frame was removed.

## COMPLAINT LEDGER
- OPEN complaint (Cameron): "There is a headless person at 42 seconds" → beat
  v2-r016-b07 (`s07-winding-tighter.jpeg`, window 41.52-47.51).
  **FIXED 2026-08-07 (C-FIX, Machine A `Dev`).** The prior take had a figure in
  a rust robe seated back-to-camera dead-center with a dark void where the head
  belonged. Rerolled ONLY b07 (`--only b07 --redo`, 1 shot, $0.13). New take:
  Martha kneads dough at the table, hands working, head turned in a glance
  across the room — every figure (Martha + the two seated men at right) now has
  a complete, visible head. Verified at full res AND in the rendered mp4 at
  0:44. No second cream robe, no Jesus, period-correct oil lamps, realistic.
  Every other frame is byte-identical; audio untouched (AUDIO LOCK PASS
  SHA256=d380ba61…). Touch-once: this was the only open complaint on the row.

## C-FIX record 2026-08-07
- 1 reroll / 26 beats = 3.8% (well under the 15% budget). Row spend this
  session ≈ $0.13. Re-assembled, AUDIO LOCK PASS, 166.8s / 20.3 MB.
