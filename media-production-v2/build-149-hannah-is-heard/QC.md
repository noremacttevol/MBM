# QC / RUNNER HANDOFF — build-149-hannah-is-heard (1 Samuel 1)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 22 beats, ~126 s.

## 🅿️ COMPLAINT LEDGER — OPEN complaint ROOT-CAUSED to the dead-tail class (2026-08-07, Machine A `Dev`, $0 Fable-5 author lane)

- **OPEN Cameron complaint (`v2_outline.py 149`): "Wrong caption at 2:06."** ROOT CAUSE =
  the **trailing dead-tail / frozen-caption** family (same class as rows 83 & 86 — "13 extra
  seconds on the end... cut off as soon as the voice stops"). **Measured:** the live V1 mp4
  (`media-production/build-149-.../1-samuel-1_hannah-is-heard.mp4`) runs **139.62 s**, but the
  narration + card content ends at **126.2 s = exactly 2:06** — Cameron's timestamp lands on the
  narration-end point. So a **13.4 s dead tail** freezes the final caption on screen past the
  voice; that lingering/mis-timed caption at 2:06 is what he flagged.
- **Source is CORRECT — no author text error:** every caption text matches KJV/narration and the
  2-voice colouring is right (Hannah's prayer = WOMAN pink; Eli's blessing s1 = SCRIPTURE light
  blue; card = narrator). Nothing in beats_v2.py / make_narration.py reproduces a *wrong* caption;
  the fault is purely the over-long V1 render's tail.
- **🅿️ RUNNER — do this (this row has 0 stills → you BUILD the fresh V2):** the V2 assembler's
  **TAIL GATE** (row-74/86 lesson) fixes this automatically — the picture ends when the closing
  card begins and the final mp4 ends on the last word (rendered mp4 tail ≈ the standard TAIL
  constant, NOT +13 s). **VERIFY at assembly:** captioned.mp4 duration ≈ card seg_start (±0.2 s)
  and final mp4 duration = audio total exactly (no trailing dead-air); then eyeball the closing
  caption at the 2:06 narration→card boundary (w4 "…as long as he liveth…" light-blue → card).
  Ship with a card telling Cameron the end was trimmed to the last word (no more frozen caption).
  If, once built, a *specific* caption is still wrong at 2:06 (not just the tail), localize it
  against the delivered mp4 and fix that segment — but the measured evidence is the dead tail.

## Hannah's dignity (rows 44/74 class, strictly)

Barrenness = the empty lap + the yearly ache — never abject, never
hysterical. The silent prayer (b03/b04) is the row's centre: LIPS
MOVING, NO SOUND, tears bright — no wailing gestures ever.
Tear-tracks stay UNWIPED in b15.

## The vow's gesture-language (the row's signature)

Asking hand drawn IN at the chest / giving hand open OUT toward the
sanctuary — b05 (in), b06 (the turn out), b09 (BOTH at once), b10
(the whole posture). Check the hands across these four as a set.

## Order-of-events gates

- b17's eased face comes BEFORE any answer — NO child, NO sign in
  frame; faith's receipt only. A child in b17 is a reject.
- Samuel's ages: newborn (b18) → toddler (b19) → small boy ~4
  (b21/b22). Face-board the ageing; his little olive tunic is the
  mother's yearly gift.

## Eli's arc

Weary error (b11, never malice) → focusing (b12) → compassion
(b14) → full blessing (b16, hand raised) → gentle hand on Samuel's
shoulder (b22). One old man, five registers.

## The leaving (b22, direction law exact)

Hannah walks AWAY down the morning road, back straight, steps even,
tears allowed; Samuel at the door under Eli's hand, both watching
her go. Broken AND at peace — both must read.

## Other gates

- The other wife: ONE frame (b02), a smug glance — not cartoon
  cruelty.
- b20's brow-on-the-doorpost intimacy — tears on the wood.
- Dusk lamps physical (deliberate dusk for the prayer sequence).

## Coverage shape

One true wide with stated geometry: b01 (camera across the court
past the milling families' backs). No Jesus beats (OT row). File
order ≠ story order (b09 at 47s before b10's 42s, b20 at 40.92s) —
build by WINDOW.

- Plates: none auto-matched (clean). SHILOH promote-first from b03.
