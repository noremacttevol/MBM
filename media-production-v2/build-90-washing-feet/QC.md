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
