# QC / RUNNER HANDOFF — build-90-washing-feet

## ✅ AUDIO FIX DONE — STALE-V1-FINAL lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL, BOTH tripwires, no open Cameron complaint (`v2_outline.py 90`).
Parked on the AUDIO LOCK: the V1 mp4 (107.433s) runs +31.215s LONGER than the 76.218s
timeline AND 13 mp3s are newer than the V1 mp4 (it carries deleted/old audio). Fix ($0, no
new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from
this build's own 13 mp3 segments (present in the V1 audio/ dir) at the timeline offsets
instead of copying the stale/oversized V1 mp4 AAC. 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, ship nothing visual: board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture
runner assembles on the corrected audio. No Gemini spend.

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before build

"Why does every disciple look the fucking same."
HUMAN-VARIETY GATE (rubric lesson 3): the Twelve are TWELVE DISTINCT
men — different ages, builds, hairlines, beard shapes, skin
weathering. Before assembly, tile all disciple faces from every
frame on one board: if any two read as the same man (other than the
same man twice), regenerate. Named disciples must match their canon
sheets; the rest must differ from each other visibly.


## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 76.218s vs authoritative V1 mp4 `john-13_washing-the-disciples-feet.mp4` = 107.433s.
Tripwire(s): RUNTIME |Δ|=31.215s > 1.0 (line 531); RECENCY 13 mp3(s) newer than V1 mp4. V1 mp4 LONGER than timeline (excess audio not in build).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (and note: the {newer}-mp3 recency tripwire also needs a re-rendered V1 mp4 OR the segment-rebuild path, which the flag provides) then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-90-washing-feet --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-90-washing-feet --ceiling <c>
python3 media-production-v2/v2_assemble.py 90
```

---

## PICTURE RUNNER BUILD — 2026-08-07 (Opus runner, Machine A `Dev`, resumed stranded RUNNING row)

Resumed the stranded row (State RUNNING / Claim A-auto; a prior autopilot lane died after 6 stills).
Already-shipped check: no committed mp4, live card was the OLD 2026-07-28 build → not shipped, built it.
Audio: `AUDIO_FROM_V1_SEGMENTS=True` present (audio-fix done 2026-08-06). Portraits: 0 (cast reused, $0).
Generated the remaining 6 stills; light-QC'd all 12 against must_show/must_not_show + RUNNER-LESSONS.

### COMPLAINT LEDGER
- **OPEN (rubric lesson 3 / HUMAN-VARIETY GATE): "Why does every disciple look the fucking same."**
  FIXED in this cut. The Twelve read as twelve distinct men across every multi-figure frame —
  s01 (supper wide), s03 (washing wide), s09/s10 (teaching wides), s11, s12: visibly different
  ages, beard shapes/lengths, hairlines, skin weathering, one head-covering, a young beardless
  John vs a grey elder being washed. No two disciples read as the same man (other than the same
  man across frames). Peter held consistent by REF (dark curly hair + full dark beard + blue-grey
  tunic + rope belt) across s04/s05/s06/s07/s08/s11. Review card answers the complaint in his words.

### REROLLS (4 of 12 beats = 33% — OVER the 15% COST-LAW budget; all mandatory-class, explained)
- **s02/b02 ×2** — take 1: kerosene/hurricane GLASS-CHIMNEY wall lamps (modern-object, RUNNER-LESSONS
  b41) + daylight window in a night supper. Reroll take 1 cleared the lamps+daylight but returned a
  3-panel COLLAGE (the must_show "close on the SEQUENCE: robe aside… towel knotted… water arcing" is
  a structural collage trigger, row-66/114). Reroll take 2 landed a CLEAN single night frame: clay jar
  → clay basin, towel girded, period oil lamp, no daylight. KEPT take 2.
- **s09/b09 ×1** — daylight doorway in a night supper (time-of-day). b09 locks ROOM (="window open on the
  night") so the reroll landed night: closed door, warm oil lamps, clay basin. KEPT. Clean fix.
- **s06/b06 ×1** — bright daylight window in a night supper. Reroll fixed the lamp (clay) + basin (clay)
  but the DAYLIGHT WINDOW PERSISTS. Root cause is structural (row-103): b06 `locks` = [BASIN, PETER],
  it OMITS ROOM, so it never receives the "window open on the night" cue. A reroll re-runs the same
  gamble — per row-103 I did NOT burn a 2nd reroll. KEPT the better take, logged FIX-WAVE below.

Cost: 12 stills + 4 rerolls = 16 × $0.134 ≈ **$2.14 this row** (0 portraits). Still ~1/3 of the $6.10
baseline even at 33% rerolls — the overage is 4 MANDATORY defects (modern-object, time-of-day ×2,
collage), not subtle-drift chasing, and every one is root-caused to an author gap below so it is
fixed structurally, not re-rolled every session.

### FIX-WAVE / AUTHOR HANDOFF (do NOT re-roll — structural, needs beat-text/lock edits)
- **b06 `locks`: add "ROOM".** Currently [BASIN, PETER] → renders daylight in a night story. Adding
  ROOM (the night+oil-lamp setting lock) fixes the residual daylight window. Then regenerate ONLY b06.
- **b02 `locks`: add "ROOM"; and de-sequence the must_show.** b02 = [BASIN] only (that is why the first
  take invented kerosene lamps + daylight), and its must_show "close on the SEQUENCE …" (3 enumerated
  steps) is a collage magnet. Author: add ROOM, and rewrite must_show to ONE moment (the pour), so the
  beat stops needing 2 rerolls to land a single night frame. (Take 2 is clean now; this hardens it.)
- **s05/b05** close Jesus↔Peter two-shot is near forehead-to-forehead — watch for a row-49 "romantic/too
  close" read; author could state an arm's-length + must_not_show "faces not close." Non-blocking.
- **s10** floor basin rendered white/glazed vs the clay BASIN lock (minor prop tint). Non-blocking.

Audio untouched (AUDIO_FROM_V1_SEGMENTS). STALE-V1 batch → verify captioned≈card_start after assemble.
