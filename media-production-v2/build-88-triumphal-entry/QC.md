# QC / RUNNER HANDOFF — build-88-triumphal-entry (Matthew 21:1-11)

## ✅ AUDIO FIX DONE — STALE-V1-FINAL lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL, BOTH tripwires, no open Cameron complaint (`v2_outline.py 88`).
Parked on the AUDIO LOCK: timeline 118.564s vs V1 mp4 117.100s (|Δ|=1.464s) AND all 15
mp3s newer than the V1 mp4. Fix ($0, no new TTS): set `AUDIO_FROM_V1_SEGMENTS = True` in
beats_v2.py so the assembler rebuilds from this build's own 15 mp3 segments (present in the
V1 audio/ dir) instead of copying the stale V1 mp4 AAC. 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, ship nothing visual: board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture
runner assembles on the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 20 beats, ~112 s.

## Same occasion as row 83 — different stagings on purpose

Row 83 owns the OVERLOOK vista (the weeping); this row lives at crowd
level: Bethphage lane, the branch-strewn road, the gate. Do not
introduce panorama compositions here — if a render looks like row 83's
valley view, it missed this row's staging. Row 83's approved OVERLOOK
frame may still seed this row's distant-city glimpses if any.

## Coverage shape

Five true wides with stated geometry: b01 (the sending in profile),
b11 (the carpeting — camera low behind the colt's advance), b13 (the
hosanna flood — rider and river of branches in profile), b16 (the
gate — camera INSIDE the city behind the turning heads), b20 (the
closing — meek rider amid it all, in profile). Eight flips.

## THE COLT (the animal laws)

- TWO animals: grey MOTHER DONKEY + darker grey COLT (count law); the
  COLT is ridden, the mother led alongside. If any frame swaps which
  animal carries him, reject (scripture-exactness).
- The colt is SMALL and never-ridden — Jesus on it reads humble-low,
  feet near the ground: meekness as geometry (and the no-giant gate
  matters doubly on a small mount).
- Handled gently in every frame; cloaks-as-saddle (garments, not
  tack — row-7 class: no leather saddle, no bridle hardware).

## Other checks

- The carpeting is CLOAKS + CUT BRANCHES on the road — both visible,
  the road transformed frame by frame (bare → strewn: one direction).
- Direction (row-83's law on its sibling row): the whole procession
  descends TOWARD the in-frame gate/city; nobody walks against it.
- The crowd is joyful, never mob-like; "WHO IS THIS?" plays on
  city faces at windows (b15) vs the procession's answer (b19).
- TWO disciples on the errand (count law) — same two men through
  b01-b07.
- ROAD wired from build-38. COLT is an animal lock — no plate; LANE
  promote-first from b03's lane frame if needed.
- Only Jesus wears cream.


## RUNNER PARK (A-auto Machine A `Dev`, 2026-08-06) — NEEDS-AUDIO / STALE-V1-FINAL — $0 SPENT
Pre-flighted at step 2 BEFORE any credit (no stills generated, nothing to reuse-waste).

**BLOCKER — v2_assemble AUDIO LOCK will fail:** timeline total = 118.564s vs authoritative V1 mp4 `matthew-21_triumphal-entry.mp4` = 117.100s.
Tripwire(s): RUNTIME |Δ|=1.464s > 1.0 (line 531); RECENCY 15 mp3(s) newer than V1 mp4. V1 mp4 SHORTER than timeline (trailing-silence shortfall).
The AUDIO LOCK copies the finished V1 mp4's AAC stream packet-for-packet; it refuses when the mp4 does not match the recomputed timeline.

**Why the runner cannot fix it:** the fix is `AUDIO_FROM_V1_SEGMENTS = True` in this build's beats_v2.py (rebuilds the track from this build's OWN mp3s at the timeline offsets — nothing re-voiced, V1 stays read-only). Editing beats_v2.py is outside the runner's allowed writes (art / QC.md / boards / SESSION-LOG / review card / mp4 only — PROMPT-OPUS-RUNNER.md hard rails). Same class as parked rows 69/74/77/78/80/82/83.

**FIX (author):** set `AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py (and note: the {newer}-mp3 recency tripwire also needs a re-rendered V1 mp4 OR the segment-rebuild path, which the flag provides) then this row builds normally.

**RESUME after fix:**
```
python3 media-production-v2/v2_story_cast.py build-88-triumphal-entry --ceiling <c>
python3 media-production-v2/v2_gen_api.py build-88-triumphal-entry --ceiling <c>
python3 media-production-v2/v2_assemble.py 88
```
