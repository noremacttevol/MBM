# QC / RUNNER HANDOFF — build-94-father-forgive-them (Luke 23:33-34)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 94`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24), so the packet-copy AUDIO
LOCK would ship stale voices. Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in
beats_v2.py so the assembler rebuilds from this build's own 11 mp3 segments (present in the
V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md step 6, board → AUTHORED / Audio OK /
Ready ✅, claim cleared, picture runner assembles on the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 12 beats, ~66 s.

## ⚠ HILL plate UNWIRED (fourth wrong-plate catch) — do NOT re-wire

The stash matched build-38's warm golden village frame by token name —
wrong world for Golgotha's bare rise under cold grey sky. IMPORTANT
TOOL TRAP: every `--wire` invocation RE-RUNS auto-wiring and will
re-add HILL from build-38 — if you run --wire on this build again,
re-remove HILL afterward (it is deliberately absent from PLACE_REFS).
HILL is promote-first from b01; its approved frame seeds rows 95/96 —
ONE Skull across the passion block.

## MERCIFUL DISTANCE (the row's rendering law — absolute)

The crucifixion is shown the way this build authored it: the three
crosses at DISTANCE, figures small, under a cold grey sky. NO close-up
of wounds, no nails driven, no blood detail, ever — the nearest
approach is the lifted face at mid-distance for the prayer. Any render
that closes in on gore is an automatic reject. The horror lives in the
dice game's obscene casualness (b06), not in wounds.

## The prayer (the row's center)

"Father, forgive them; for they know not what they do" — spoken OVER
the ones dividing his garments: the words and the dice game share the
geometry (b06/b09/b11: the reach of the prayer measured across every
figure on the hill — soldiers, mockers, watchers; the wide must hold
them all beneath it).

## Other checks

- SOLDIERS group ref wired from build-15 (the centurion's Romans —
  named recurring group exception, same legion look across the
  library; face-board the dice players against it).
- Garments: the CREAM robe among the divided clothing at the cross's
  foot — the one cream item, in the soldiers' hands (only-Jesus-
  wears-cream carried to its terrible endpoint).
- Cold grey light throughout; the sky heavy but not yet the darkness
  (that belongs to row 96).
- Direction: the watchers' gazes UP the rise; the dice players' DOWN
  at the dust — the contrast is the sermon.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: within 1.0s (recency is the blocker).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.

## ✅ REALISTIC-V2 SHIPPED (Opus runner, Machine A `Dev`, 2026-08-07, UNATTENDED/HEADLESS) — RESUMED stranded RUNNING row

**COMPLAINT LEDGER: none open.** `v2_outline.py 94` shows no filed Cameron complaint on this row (only the beat map). Nothing to answer; nothing regressed.

**Resume context:** prior autopilot lane died after 8 of 12 stills (s01-s08 on disk, no committed mp4, live card was OLD V1). Already-shipped check: no mp4 commit, no realistic-v2 card → NOT shipped, resumed. No live sibling gen (ps clean). Generated the remaining 4 (b09-b12), no re-pull of the 8 passing frames (COST LAW).

**Light QC (one pass):** plate s01 (HILL, promote-first, seeds 95/96) QC'd first — cold grey sky, crosses at distance, MERCIFUL DISTANCE held, no gore/modern/lens-stare/2nd-cream. PASS. All Jesus close-ups (s02/s08) locked-look, reverent, eyes-up (green/hazel = baked V2 ref, NOT rerolled per lesson). Dice-game inserts (s05/s06/s07) read the obscene casualness; only-Jesus-cream held (the divided cream garment in soldiers' hands). j1 prayer s09 = the row's center, prayer over the ones dividing his garments — the authored geometry lands.

**2 rerolls / 12 beats = 16.7%** (marginally over the 15% target; both were MANDATORY row-45-class composite garbage, NOT subtle drift):
- s03 (b03) — double-perspective composite: misty horizontal seam splitting two scenes, three crosses DUPLICATED (top hill + bottom). Reroll → single coherent wide (crosses at distance, soldiers dividing garments). FIXED.
- s10 (b10) — same composite/seam defect + giant foreground Jesus over a background duplicate of the crosses. Reroll → single frame, Jesus robed & bound (not nailed — merciful restraint), soldiers casting lots on the cream garment below. FIXED.

**FIX-WAVE (kept, not rerolled — COST LAW):** s05 has a faint sea backdrop behind the dice insert (tight insert, not a place plate); s06 titulus board carries period-appropriate but gibberish lettering (on-board where an inscription belongs, not a bottom-band caption). Neither is garbage; both are fix-wave polish.

**Assembly:** AUDIO_FROM_V1_SEGMENTS=True → AUDIO REBUILD PASS SHA256=80ff9897e4aedbc63ffc5dbe619d44ed1d01a026da6e0e61e4361d1386bc4ae3, 73.767s (new voice at source — 11 V1-dir segment mp3s). Stale-window check (row-74/89 trap): video_silent 73.73s ≈ card_start-based total, all 12 stills placed, final 73.77s — no overrun/drop. Caption frames verified: scripture blue + Jesus-voice j1 RED, bottom band only, question card clean.

**Cost:** 4 fresh stills + 2 rerolls = 6 gens ≈ $0.80 this session (prior lane already spent ~$1.07 on s01-s08). Row total ≈ $1.87. Meter $480.93.

---
## C-FIX 2026-08-11 (Machine A `Dev`, Opus runner) — Cameron's 2 complaints CLOSED, touch-once

**COMPLAINT LEDGER (open at start, now fixed):**
1. **"In 0:54 he is smiling, i dont think he smiled on the cross its offputting, fix it."**
   → 0:54 = beat **b10** (window 50.41–56.38s, s10). FIXED: face re-cut to solemn,
   lifted, heavy with pain — NO smile / no bared teeth. Verified in the RENDERED mp4 at 54s.
2. **"The picture at 0:48 does not have the plaque over his head and his eyes look weird fix it."**
   → 0:48 = beat **b09** (window 46.08–50.41s, s09). FIXED: (a) a weathered wooden titulus
   placard is now fixed to the top of the upright beam directly above his head; (b) eyes re-cut
   open/calm/lifted to heaven, no longer rolled back / whites-showing. Verified at 48s.

**PROMPT AUTOPSY (rubric meta-law 3):**
- b09 titulus → **IGNORED**: the original scene never named a titulus, though Luke 23:38 has a
  superscription and the sibling frame b06 already carried one — presence-inconsistency. FIX =
  added the placard to must_show + scene (worn/indistinct lettering; not demanding legible text
  the model botches into gibberish).
- b09 eyes → **ALLOWED**: scene said "the lifted face high" with no gaze constraint, so at
  distance the eyes rolled back. FIX = must_show/scene now specify eyes open, calm, upward.
- b10 smile → **ALLOWED**: scene said "the praying face … words still moving on the lips" with
  no expression constraint. FIX = must_not_show now forbids smile/grin/bared teeth; scene states
  solemn, sorrowful, never smiling.
- b10 wardrobe (batched, touch-once) → **ALLOWED**: b10 locked only HILL, so it drifted to a full
  cream robe while b06/b09 are stripped — jarring continuity. FIX = stripped to a plain loincloth
  to match, so the three cross frames are consistent.

**FULL-CUT GATE (6b):** all 12 stills + closing card extracted from the rendered mp4 and viewed.
Only b09/b10 changed; every other frame byte-identical (unchanged asset). No other complaint-worthy
defect (row-11 lesson satisfied): b01/b03/b04/b11/b12 distant/merciful, b02/b08 solemn Jesus,
b05/b07 dice-lots no gore, b06 has titulus. No 2nd cream figure, no giant scale, anatomy clean,
realistic throughout, captions bottom-band (blue scripture / white narrator / RED Jesus j1).

**Audio:** AUDIO REBUILD PASS SHA256=80ff9897… — byte-identical to the prior ship; nothing re-voiced.
**Cost:** 2 rerolls (b09/b10) = the two complaint frames, ~$0.27 this run, 0 extra rerolls. Meter 600.72.
