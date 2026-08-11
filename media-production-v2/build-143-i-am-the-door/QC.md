## ✅ AUDIO-FIX DONE → AUTHORED / Audio OK / Ready (2026-08-11, Machine A `Dev`, audio lane)

STALE-V1 class, resolved at **$0, zero Gemini, zero re-voice** — no stills exist
yet, so this hands back to the picture runner (prompt step 5, "no V2 stills" case).

- **Voice-ID:** all segments are 44100 Hz / 128 kbps / mono = ElevenLabs new-voice
  spec (edge-tts would be 24000/48k). NOT the dead old edge-tts — no re-voice.
- **Fix:** `AUDIO_FROM_V1_SEGMENTS = True` added to `beats_v2.py` (timeline 63.16s vs stale 66.15s render, gap 3.00s). When the
  picture runner assembles, the track rebuilds from the segment mp3s instead of the
  stale V1 render, so `v2_assemble.py 143` passes the audio lock.
- **Board:** NEEDS-AUDIO → **AUTHORED / Audio OK / Ready ✅**, claim cleared.

---

## 🅿️ RUNNER $0 PRE-FLIGHT PARK → NEEDS-AUDIO (2026-08-11, Machine A `Dev`, Opus runner)

**Parked at $0 BEFORE any still was generated (row-141 lesson: pre-flight the AUDIO
LOCK even when the board says Audio OK).** This row is STALE-V1: the current V2
audio segments no longer match the old V1 render.

- extract_beats timeline (current `audio/*.mp3` segments) = **63.156s**
- authoritative V1 final mp4 = **66.153s** → gap **2.997s** (past the 0.75s guard); `AUDIO_FROM_V1_SEGMENTS` is NOT set.
- 7 segments, spec 44100/128000/mono = the new-voice ElevenLabs cast spec (Brian narrator / Chris Jesus) — so a re-voice is probably NOT needed, only the flag.

**AUDIO LANE — RESUME (row-200/118/22 template, expected $0/no re-voice):**
1. Voice-ID the segments to confirm they are the new ElevenLabs cast (not old edge-tts); re-voice ONLY any wrong seg first.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `build-143-i-am-the-door/beats_v2.py`.
3. Hand back to the picture runner: `v2_prompt.py build-143-i-am-the-door --check` (PASS) → generate the beats → `v2_assemble.py 143` must print **AUDIO REBUILD PASS** (~63.2s) → FULL-CUT GATE → ship + deploy + live-verify.

The runner does NOT set the flag itself (beats_v2.py is off the runner's allowed-write
list; the runner-prompt step 6 says an AUDIO-LOCK failure = stop the row, log, do not ship).

---

# QC / RUNNER HANDOFF — build-143-i-am-the-door (John 10:1-9)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~55 s. Third I AM row.

## The shepherd IS build-21's shepherd (new cross-video identity)

SHEPHERD lock copied byte-identical from build-21 (lost-sheep) plus
a same-man clause — ONE parable shepherd across both rows. The FOLD
plate (build-21 b12) was ACCEPTED for exactly this reason: the frame
IS the row's picture (gateless gap, shepherd standing in it, flock,
dusk) and the man in it is now this row's locked character.
Face-board 143's shepherd against build-21's frames.

## The gap law

Exactly ONE opening, NO gate, NO bars, ever — the open gap is the
doctrine. A rendered gate is an automatic reject. b07: JESUS himself
stands framed in the gap (the only jesus-in-fold frame — the claim
embodied). b10: the shepherd LYING ACROSS the opening under stars.

## The wall-climber (b04, row-126 unease pattern)

Dark figure over the FAR wall, sheep stirring away — NO attack, NO
struggle. The lit opening visibly avoided.

## Direction law

b06: flock files IN at violet dusk, each under the shepherd's hand.
b08: flock streams OUT at bright morning to green pasture. The
two directions are the verse ("go in and out").

## Coverage shape

One true wide with stated geometry: b01 (camera low on the slope,
fold from the side). Two Jesus beats (b03 teaching slope with the
fold beyond; b07 in the opening). Night/dusk fold frames BY DESIGN.
File order = story order.

- Plates: FOLD accepted (build-21 b12 — see identity note above).
  HILLSIDE promote-first from b03.
- b09: the nuzzle close — nothing transactional in frame.
