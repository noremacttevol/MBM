# QC / RUNNER HANDOFF — build-96-it-is-finished (John 19:30 / Matt 27:51)

## ✅ QC-OK — FULL-CUT GATE 6b, 2026-08-11 (Machine A `Dev`, VERIFY-PASS)

Extracted ONE frame per beat (13) + closing card from the **rendered mp4** at each
beat-window midpoint and viewed every one against the defect checklist,
RUNNER-LESSONS, and the row's complaints. **Verdict: CLEAN — no re-cut.**

- Jesus face-locked every appearance (b01/b02/b03/b04/b05/b06/b08/b11): tan/olive
  skin, dark wavy hair, full beard, warm eyes; cream-only (no 2nd cream figure);
  rope-bound, **NO nails / NO wounds / NO gore** anywhere; merciful distance held,
  the darkness (Matt 27:45) carries the death.
- Veil act EXACT: ONE veil rent **top-to-bottom** (b09/b12/b13), Holy of Holies =
  dark open space (no invented ark/furniture), period 7-branch menorah, PRIEST
  face-locked in human awe with censer (b10). b07 true wide = 3 crosses on Golgotha.
- Captions 3-colour correct: white narrator, **blue** scripture (s51 @b09), **red**
  Jesus (j1 @b11, jv46 @b06). Closing card renders clean (serif, centred).
- No modern object, no giant-scale, no anatomy failure, no lens-stare, correct counts.
- **Live-verified:** served-bytes md5 `8980dd07…` == local; review.html card hash
  `782b5366…` live on reviewer, mp4 HTTP 200, content-length 20020716 B.
- **No open Cameron complaint** → zero resolved-complaint-regression risk.

**FIX-WAVE (pre-logged, NOT blocking, NOT re-cut — same precedent as row 94's
2026-08-11 QC-OK):** robed-vs-stripped wardrobe variance (b01/b03/b08 full cream
robe vs b04/b05/b06 loincloth) + crown-of-thorns present in b04 only. Each frame is
individually reverent and scripturally defensible (garments parted; John 19:2-5);
cross-frame soft-continuity belongs to the fix wave, not a verify re-cut. Also the
already-noted faint dry-lip mark on the b11 close-up (reads chapped, not blood) and
the empty flanking crosses on the s03 reroll.


## ✅ REALISTIC-V2 SHIPPED — A-auto 2026-08-07 (Opus runner, Machine A `Dev`, unattended)

**COMPLAINT LEDGER: none open** (`v2_outline.py 96` = beat map only, no Cameron complaint).

- 13 stills, 80.0s, **AUDIO REBUILD PASS SHA256=5de333ff3ff33b23683586ad3b4dec73dd8dc960b74aeebdc2bd247047ccb680**
  (AUDIO_FROM_V1_SEGMENTS=True — 14 V1 mp3 segments, byte-identical narration).
- Timeline verified: max still-window 72.52 < live card_start 72.904 → no overrun; video 80.0s == audio, all 13 stills placed.
- **Two places wired:** HILL from row 94's approved frame (`--take HILL=build-94:v2-r094-b01`,
  one Skull across the passion block) + TEMPLE from build-06 (the author's committed plate).
  **⚠ CAUGHT the row-50 `--wire` overwrite:** running `--take HILL` silently re-wired the
  committed TEMPLE from build-06 → build-39; restored it by re-pinning BOTH tokens with
  explicit `--take` (TEMPLE back to build-06-two-sons v2-r006-b21, the author's choice).
- **CRUCIFIXION RESTRAINT / MERCIFUL DISTANCE held:** crosses read from distance (s07 the
  full 3-cross wide, s05 3-cross+dice), Jesus rope-bound/robed, NO nails driven, NO wounds/gore
  shown; the darkness (failing light) carries the death — dark storm sky throughout the HILL
  beats (Matt 27:45). Only Jesus wears cream. Locked Jesus face across all 9 Jesus beats.
- **Veil geometry consistent:** ONE temple veil, rent top-to-bottom down the middle, revealing
  the Holy of Holies (s09/s12 inserts, s10 PRIEST in awe with censer, s13 establishing wide).
  7-branch menorah period-correct; PRIEST face-locked (v2_story_cast REF).
- **Rerolls 1/13 = 7.7%** (well under the 15% budget): s03 rerolled — the first take put Jesus
  crucified in the foreground AND three crosses on the distant ridge (a readable 4-cross
  contradiction); the redo landed a clean 3-cross frame (Jesus centre-cream, two flanking).
  ~$1.87 row (13 stills $1.74 + 1 reroll $0.13; +$0.13 PRIEST portrait). Meter after ~$485.08.

### 🅿️ FIX-WAVE (not blocking — no filed complaint; deliberate/continuity calls for a later pass)
- **Crown of thorns continuity:** s04 and s05 render a crown of thorns; s01/s02/s06/s08/s11 do
  NOT. Each frame is individually fine and scripturally defensible (John 19:2-5), but the
  crown appearing in 2 of 9 Jesus frames is a cross-frame continuity drift (lesson-13 family).
  Harmonize in fix-wave — decide crown-throughout or no-crown, then targeted-edit/reroll the
  outliers. Did NOT blind-reroll (would be a creative/restraint call, and s05 is otherwise an
  excellent 3-cross+dice frame worth keeping).
- **s11 "It is finished" close-up:** a very faint mark near the lower lip (reads as chapped/dry
  lip, not blood/gore) — watch on any fix-wave touch of the climax frame.
- **s13 veil establishing wide:** the gold-overlaid sanctum panels read slightly flat/modern;
  scripturally the temple was gold-overlaid (1 Kgs 6:22) so it's defensible, but a fix-wave
  reroll could land more clearly ancient stone-and-gold.
- **s03 (rerolled) side crosses are empty** (the two thieves absent). Better than the 4-cross
  contradiction it replaced; if fix-wave revisits, add the two thieves on the flanking crosses.


## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 96`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 14 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 13 beats, ~73 s.

## Plates

- HILL UNWIRED (the recurring wrong build-38 auto-wire — rows 94/95's
  note applies): take row 94's approved HILL — one Skull across the
  passion block. Re-remove HILL if --wire reruns.
- TEMPLE wired from build-06 (the temple family) — the VEIL frames
  layer the great blue-purple-scarlet veil onto that architecture per
  the beat prose.

## The death (merciful distance, held to the end)

- The darkness (Matt 27:45) governs the hill beats: a darkened sky at
  midday — heavy unnatural gloom, NEVER night-with-stars and never a
  sunset (time-of-day law at its most doctrinal).
- The bowed head (b07) is the death frame: at distance, the head
  lowering — no death-agony close-up, no wound detail, ever.
- "It is finished" is a VICTORY declaration — the hill's stillness at
  b05 reads as something COMPLETED, not merely ended.

## THE VEIL (the row's second act — exactness laws)

- Torn TOP DOWN (Matt 27:51 "from the top to the bottom") — the split
  begins at the TOP in any mid-tear frame; a bottom-up tear is a
  scripture error, reject.
- The veil is the great blue-purple-scarlet hanging; behind it the
  Holy of Holies shows as DARK OPEN SPACE — never a depicted ark or
  furniture (content-care: no invented sacred objects).
- The duty PRIEST's terror (b10) is awe-fear, human; lamplight only.
- b13's closing (the veil hanging open in two halves, the way open)
  is the doctrine as architecture.

## Coverage shape

Two true wides with stated geometry: b05 (the declaration over the
whole dark hill) and b13 (the opened veil down the hall's length).
Five flips.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=2.86s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
