# QC / RUNNER HANDOFF — build-97-the-empty-tomb (Luke 24:1-8)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 97`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 13 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 12 beats, ~65 s.

## THE TOMB — Jesus's own (row 71's law)

This is JESUS's garden tomb: NOT the Lazarus/parable cave (rows
17/37). Take row 71's promoted TOMB frame if it exists (its b12 sealed
frame is the same tomb one row earlier in time); else promote-first
here from b03's first good rock-face frame — and rows 96/98 share it.
NEVER --take the build-37 tomb the stash will offer by token name.

## The empty tomb (rendering laws)

- The stone stands ROLLED ASIDE from b05 on; the interior holds the
  FOLDED grave clothes (the linen lying, the napkin apart — if an
  interior frame renders, those two items and nothing else).
- NO risen Jesus appears in this row (Luke 24:1-8 — the absence IS
  the message; his appearing belongs to row 98). Any Jesus figure in
  a render is an automatic reject.
- The TWO in shining garments follow row 85's angel canon EXACTLY:
  real plain-robed figures, silver-grey shining like dawn cloth —
  wingless, unhaloed, feet on ground.

## Coverage shape

Three true wides with stated geometry: b01 (the dark walk in
profile), b04 (the disproportion — camera behind the three climbing
backs toward the rock face; the stone problem stated as scale), b12
(the emergence into the risen morning from the side). Four flips.

## Other checks

- THREE women (count law), spice jars in hand on the walk IN —
  and still carried, forgotten, on the run OUT (the detail that
  sells the turn).
- Arc of light: pre-dawn dark → first grey → risen morning — one
  direction, the light itself telling the story.
- Direction (row-83): up the path IN; out of the mouth and DOWN the
  path OUT — b12's emergence vector opposes b01's approach.
- WOMEN: distinct (Magdalene among them — her canonical face, if row
  98 builds first, anchors here; the three-Marys law holds: she is
  neither Bethany-Mary nor the mother).


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=1.92s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.

## ✅ RUNNER BUILT + SHIPPED — realistic-V2 first cut (2026-08-07, Opus runner, Machine A `Dev`, UNATTENDED/HEADLESS)

**COMPLAINT LEDGER: none open** (`v2_outline.py 97` shows no Cameron complaint on this row). QUEUE row 97 cross-checked = still "The empty tomb" (Luke 24) — NOT swapped, safe to build.

**Build:** 12 realistic stills, no portraits (all cast reused from library, $0). TOMB is a PROSE place lock (`[+1 place: TOMB]`), not an image plate. **PLATE DECISION — declined the single TOMB image plate (rubric §372/§374 + row 50/51 precedent):** the TOMB token spans exterior-approach (dark), the rolled-stone reveal (dawn-rose), the interior chamber, AND the risen-morning emergence — a token spanning different scenes AND a deliberate time-of-day arc ("pre-dawn dark → first grey → risen morning — the light itself telling the story," per this QC). A single promoted plate would bleed one scene's light/interior-vs-exterior across all 9 beats and fight the arc. Also cleared the `--wire` auto-suggestion `TOMB ← build-37-rich-man-lazarus` (this QC forbids it; rubric §356) back to `{}`. Each beat rendered its own tomb on the shared TOMB prose; uniformity QC'd by eye.

**Row-specific sacred laws — all held:** NO risen Jesus in any frame (the absence IS the message; verified all 12); THREE women throughout, distinct + consistent (library WOMEN refs held — red older / blue tall / green young across every beat); folded grave clothes present in every interior (linen lying, the napkin apart — s06/s09/s11); the two angels follow row-85 canon (real plain-robed, wingless, unhaloed, feet on ground); only-cream-is-Jesus held trivially (no cream anywhere; angels in white/silver-grey, not cream); light arc reads pre-dawn → dawn-rose reveal (s05) → risen-gold morning emergence (s12); direction up-the-path IN (s01) vs out-the-mouth (s12).

**Rerolls: 2/12 = 16.7%** (b03, b04) — both genuine defects. **≈$1.88 row** (12 stills $1.61 + 2 rerolls $0.27; 0 portraits). Meter $485.08 → $489.37. Under the $6.10/row running average → COST-LAW trend DOWN holds; the 16.7% reroll is ~1 frame over the 15% budget, justified (two beats each carried a genuine defect) and explained.

**AUDIO REBUILD PASS SHA256=1bbcdd2019ebd1e5** (rebuilt byte-identical from the 13 V1-dir mp3s via AUDIO_FROM_V1_SEGMENTS — nothing re-voiced), 73.6s / 19.4 MB. **STALE-V1 stale-window check (rubric §417/§433, row 97 is in the 86–100 batch): PASS** — all 12 stills placed (no dropped beat), final mp4 73.6s == extract total 73.575s (card 65.51→73.575), decode 0 errors. Caption QC on the rendered mp4 (output-seek 5s/35s/69s): bottom-band white serif only, question card clean beige with margins, no squares.

### FIX-WAVE (author beat-text — NOT runner-rerollable; probe rerolls confirmed structural)
1. **b03 (s03) + b04 (s04) — tomb renders OPEN before the reveal.** The rock-cut tomb renders with the disc stone rolled aside and a dark open doorway, despite b03's `must_not_show` "the stone NOT yet visible as moved" (and b04's implied seated stone). The model's iconic "empty-tomb-open" prior overrides the beat text; ONE probe reroll each did NOT seal it (kept the better-composed/better-lit takes). This spoils the b05 reveal ("the huge stone that had sealed the tomb was rolled away"). AUTHOR: add to b03 & b04 `must_show` an explicit "the great disc stone SEALS the low doorway, tomb still CLOSED, NO dark opening visible," then regenerate ONLY those two.
2. **b04 (s04) — full DAYLIGHT despite narration "walking up that hill in the dark."** The beat text ("wide grey frame," "dark limestone shoulder") doesn't lock the pre-dawn SKY, so the resurrection wide defaults to bright daylight (rubric §477/§85 lone-wide-loses-night). Reroll didn't fix (text-weak, not a seed fluke). AUTHOR: add "pre-dawn darkness / night sky before sunrise / no daylight" to b04's `must_show`/`scene`.
3. **Angel look drift — s07 fair-haired luminous white vs s08/s10 dark-haired grey/white.** The two angels are a PROSE lock (TWO, no REF image), so they drift shot-to-shot (same class as the row-52/55 face-flip, but for the two messengers, and not a filed complaint). AUTHOR/fix-wave: promote a TWO-angel anchor + wire `REFS`, or accept — s08/s10 already agree (dark), s07 is the outlier.
