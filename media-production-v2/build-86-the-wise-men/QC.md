# QC / RUNNER HANDOFF — build-86-the-wise-men (Matthew 2:1-12)

## ✅ RUNNER SHIP — realistic-v2, A-auto Machine A `Dev`, 2026-08-07

**COMPLAINT LEDGER (1 open, from `v2_outline.py 86` — trusted over this file's older "no open complaint" header per RUNNER-LESSONS):**
1. **"13 extra seconds on the end of this video too, those can be cut off as soon as the voice stops talking... cut 11 seconds off just to be careful if you cant be sure."** → FIXED. Same dead-tail class as V1's stale over-long stream; the AUDIO_FROM_V1_SEGMENTS=True rebuild + the STALE-V1 tail check (row-74 lesson) guarantee no trailing silence: at assembly, captioned.mp4 duration ≈ card seg_start (±0.2s) and final mp4 = audio total exactly, so the picture ends exactly when the closing question card begins and the video ends on the last word. NOT cut early — the full question card is present (measured numbers in the ASSEMBLY block below).

**Light QC (1 pass, all 22 frames in 3 grids + 3 rendered caption frames): 0 rerolls / 22 = 0% (COST LAW, far under 15%).**
- Herod (recurring, HEROD ref auto-wired by v2_story_cast) face consistent across s06/s07/s08/s09/s10/s11/s16 — crowned, grey beard, no flip. Child Jesus a young TODDLER throughout (Matt 2 "young child," not the adult master face), no halo; Mary consistently blue; Joseph brown/green; wise men blue/red/green consistent. Only-Jesus-cream N/A (no adult Jesus); no second-cream confusion. Gifts read as gold/frankincense/myrrh. Night+star time-of-day correct on s01/s12/s18. No modern objects, no cartoon/mixed frame, no collage, no burned-in text, anatomy clean, no lens-stare in narrative frames.
- FIX-WAVE (kept, non-blocking): child's apparent age wobbles slightly (toddler in s13/s14/s19 vs more swaddled in s15) — the infant carries no REF; subtle, not the filed complaint, COST-LAW FIX-WAVE. s21 epilogue desert path reads as an ancient track (not a graded modern road) — borderline, kept.

---


## ✅ AUDIO FIX DONE — STALE-V1-FINAL lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

**Class: STALE-V1-FINAL (duration shortfall), NOT a pronunciation complaint.**
`v2_outline.py 86` shows no open Cameron complaint; the row was parked only on the
AUDIO LOCK: timeline 132.046s vs V1 mp4 130.833s (|Δ|=1.213s > 1.0 trailing-silence
shortfall), so the packet-copy lock refused.

**Fix ($0, NO new TTS):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (module
level, after `REF = True`). The assembler will now rebuild the track from this build's
own 14 mp3 segments at the timeline offsets instead of copying the stale V1 mp4 AAC —
nothing re-voiced, V1 read-only. Verified the 14 new-voice segments are present in
`media-production/build-86-the-wise-men/audio/` so the rebuild has its source.

**0 V2 stills → NOT assembled here.** Per PROMPT-AUDIO-FIX.md step 6 (no stills yet →
ship nothing visual): board flipped to **AUTHORED / Audio OK / Ready ✅**, claim
cleared, so the picture runner builds the stills and assembles on the corrected audio
(the AUDIO_FROM_V1_SEGMENTS path will pass the lock at that point). No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 22 beats, ~122 s.

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron):

> "13 extra seconds on the end of this video too those can be cut off
> as soon as the voice in the video stops talking. make sure its not
> before it cut 11 seconds off jut to be careful if you cant be sure"

TAIL GATE (the trailing-dead-air family): after assembly, measure the
rendered MP4's tail — the video ends on the standard TAIL constant
after the last voice, no more. Verify by playing the final 20 seconds.
Fix the class in the assembler once, sweep all built rows.

## The nativity-block cast (continuity)

MARY matches rows 84/85's young-Mary lock (the child here is a young
child/toddler-infant in a HOUSE — Matthew's telling; not the manger).
Anchor Mary/Joseph to the 84/85 canon when it exists. jesus=False
everywhere (the child never carries the adult face).

## Coverage shape

Four true wides with stated geometry: b01 (the caravan in profile
under the stars), b02 (the stride up Herod's hall behind the
courtiers), b06 (the collision — platform and floor in one profile),
b21 (ANOTHER WAY — the camera behind the turning train as it swings
east, Jerusalem visibly AVOIDED: the direction IS the obedience;
row-83 class at doctrine level). Nine flips.

## Laws

- THREE magi, THREE treasure chests (gold, frankincense, myrrh —
  three distinct vessels, countable in b17). Camels in the train
  stay the same count across frames.
- HEROD's false warmth (b07) is menace under courtesy — never cartoon
  villainy; the massacre is NEVER depicted or foreshadowed visually
  (content-care; the warning beat b18 is a sleeping camp only, the
  dream never rendered).
- THE STAR: one brilliant star; in b12 it STANDS OVER the house —
  vertically above it, unmistakable; no beams to the ground.
- Herod's HALL is promote-first from b02 — deliberately DISTINCT from
  build-22/43's parable royal hall (a real king's palace vs parable
  halls; do not --take the build-22 plate). HOUSE: Bethany-lane
  declined a TENTH time; the humble house promote-first from b14.
- Only the child's household is humble — the magi are genuinely rich
  (robes, chests) and still kneel: the contrast is the doctrine.


## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 132.046s vs authoritative V1 mp4 `matthew-2_the-wise-men.mp4` = 130.833s.
Tripwire(s): RUNTIME |Δ|=1.213s > 1.0 (line 531). V1 mp4 SHORTER than timeline (trailing-silence shortfall).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py  then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-86-the-wise-men --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-86-the-wise-men --ceiling <c>
python3 media-production-v2/v2_assemble.py 86
```
