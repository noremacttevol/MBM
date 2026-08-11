## 🅿️ RUNNER $0 PRE-FLIGHT PARK → NEEDS-AUDIO (2026-08-11, Machine A `Dev`, Opus runner)

**Parked at $0 BEFORE any still was generated (row-141 lesson: pre-flight the AUDIO
LOCK even when the board says Audio OK).** This row is STALE-V1: the current V2
audio segments no longer match the old V1 render.

- extract_beats timeline (current `audio/*.mp3` segments) = **47.570s**
- authoritative V1 final mp4 = **43.793s** → gap **3.777s** (past the 0.75s guard); `AUDIO_FROM_V1_SEGMENTS` is NOT set.
- 9 segments, spec 44100/128000/mono = the new-voice ElevenLabs cast spec (Brian narrator / Chris Jesus) — so a re-voice is probably NOT needed, only the flag.

**AUDIO LANE — RESUME (row-200/118/22 template, expected $0/no re-voice):**
1. Voice-ID the segments to confirm they are the new ElevenLabs cast (not old edge-tts); re-voice ONLY any wrong seg first.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `build-145-way-truth-life/beats_v2.py`.
3. Hand back to the picture runner: `v2_prompt.py build-145-way-truth-life --check` (PASS) → generate the beats → `v2_assemble.py 145` must print **AUDIO REBUILD PASS** (~47.6s) → FULL-CUT GATE → ship + deploy + live-verify.

The runner does NOT set the flag itself (beats_v2.py is off the runner's allowed-write
list; the runner-prompt step 6 says an AUDIO-LOCK failure = stop the row, log, do not ship).

---

# QC / RUNNER HANDOFF — build-145-way-truth-life (John 14:1-6)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~43 s. Fifth I AM row.

## Build-89's upper room, byte-identical

ROOM lock = build-89 (last supper chamber: U-shaped table, clay
lamps, plastered walls, one night window). Wire build-89's ROOM
plate here when promoted; the two rows are the same night in the
same room.

## Thomas is the shared cast token

Same thomas face as CAST-V2-REF sheets. His b03 question is HONEST
confusion — the room silently agrees with him; no doubt-villain
framing ever.

## The I AM signature set

b04's hand-flat-at-chest is the series signature (matches 141 b05,
142 b02, 144 b07). b02's raised-ONE-finger is warm precision (a
rescuer naming the rope), never gate-slamming. b06's by-me gesture
is a ROUTE through him, not a barrier.

## Light law

One lamplit night — clay flames only, warm on faces, deep night at
the window. No other light source anywhere.

## Coverage shape

One true wide with stated geometry: b01 (camera up the lamplit
table past the reclining disciples' backs). Nine Jesus beats
(all but b03/b09). b09's route-scroll: unopened, cords tied,
indistinct script. b10 direction: Jesus toward the door, the
Eleven rising to follow. File order ≠ story order (b02 at 24s
before b04's 14.9s neighbors) — build by WINDOW.

- Plates: none auto-matched. ROOM shared with build-89 when
  promoted.
