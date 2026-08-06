# QC / RUNNER HANDOFF — build-87-boy-in-the-temple (Luke 2:41-52)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 15 beats, ~86 s.

## THE BOY JESUS (identity law — one of a kind)

- Jesus at TWELVE per his lock: a BOY (child scale — never a small
  adult), warm olive-brown, wavy dark hair, warm brown eyes, in cream
  (only he wears cream — the law holds at every age). The ADULT face
  ref does NOT apply; story-cast the boy and face-board him across
  his frames. He is earnest and luminous-natured, never precocious-
  smug.
- Scale-gate BOTH ways (row-56/69 class): a twelve-year-old beside
  seated elders — child-sized, and no giant elders.

## Nativity-block continuity

MARY here is ~30 (aged from 84-86's eighteen) and JOSEPH ~42 — FAMILY
RESEMBLANCE to the young canon, aged: same features older. If the
84-86 canon exists at build time, use it as the resemblance reference;
note the aging explicitly to the generator.

## Coverage shape

Three true wides with stated geometry: b01 (the festival road in
profile), b03 (the finding — camera behind the haggard parents toward
the seated circle: the reveal is THEIRS), b15 (the road home, camera
behind the three — subject-unto-them as a walking-away frame). Five
flips including b12 — the small cream figure amid great columns is a
SINGLE (phantom trap; the scale lives in prose).

## Other checks

- The DOCTORS: seated learned elders, listening AND asking (v46-47 —
  "both hearing them, and asking them questions... astonished at his
  understanding"): their faces carry genuine astonishment, not
  indulgence. Distinct men (90/107).
- Mary's line lands as a mother's three-days terror + relief; the
  boy's answer is earnest, not corrective. Both dignified.
- Direction (row-83): festival flow one way (b01); the urgent
  backtrack the other (b02); home again at the close (b15) — three
  road beats, three distinct readable directions.
- PORCH is temple-family — promote-first from b03 or --take the
  build-06 temple frame for family continuity (runner's choice; note
  which in the build log).
- Only the boy wears cream.


## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 94.422s vs authoritative V1 mp4 `luke-2_boy-in-the-temple.mp4` = 93.000s.
Tripwire(s): RUNTIME |Δ|=1.422s > 1.0 (line 531). V1 mp4 SHORTER than timeline (trailing-silence shortfall).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py  then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-87-boy-in-the-temple --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-87-boy-in-the-temple --ceiling <c>
python3 media-production-v2/v2_assemble.py 87
```
