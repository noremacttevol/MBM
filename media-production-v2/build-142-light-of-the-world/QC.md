## 🅿️ RUNNER $0 PRE-FLIGHT PARK → NEEDS-AUDIO (2026-08-11, Machine A `Dev`, Opus runner)

**Parked at $0 BEFORE any still was generated (row-141 lesson: pre-flight the AUDIO
LOCK even when the board says Audio OK).** This row is STALE-V1: the current V2
audio segments no longer match the old V1 render.

- extract_beats timeline (current `audio/*.mp3` segments) = **59.409s**
- authoritative V1 final mp4 = **63.067s** → gap **3.658s** (past the 0.75s guard); `AUDIO_FROM_V1_SEGMENTS` is NOT set.
- 7 segments, spec 44100/128000/mono = the new-voice ElevenLabs cast spec (Brian narrator / Chris Jesus) — so a re-voice is probably NOT needed, only the flag.

**AUDIO LANE — RESUME (row-200/118/22 template, expected $0/no re-voice):**
1. Voice-ID the segments to confirm they are the new ElevenLabs cast (not old edge-tts); re-voice ONLY any wrong seg first.
2. Set `AUDIO_FROM_V1_SEGMENTS = True` in `build-142-light-of-the-world/beats_v2.py`.
3. Hand back to the picture runner: `v2_prompt.py build-142-light-of-the-world --check` (PASS) → generate the beats → `v2_assemble.py 142` must print **AUDIO REBUILD PASS** (~59.4s) → FULL-CUT GATE → ship + deploy + live-verify.

The runner does NOT set the flag itself (beats_v2.py is off the runner's allowed-write
list; the runner-prompt step 6 says an AUDIO-LOCK failure = stop the row, log, do not ship).

---

# QC / RUNNER HANDOFF — build-142-light-of-the-world (John 8:12; John 9)

AUTHORED FROM SCRATCH, 2026-08-05 (Machine A). `--check` PASSES, zero
WARNs. 10 beats, ~53 s. Second I AM row.

## Light law (doubly binding)

Every light physical: festival lampstand flames, the guttering lamp,
the lantern, the sunrise. NO light effect on any person — b03's
lamps burn BESIDE Jesus, never from him. Automatic reject.

## The born-blind man is ROW 63's man

BLINDMAN lock is BYTE-IDENTICAL to build-63 — same face, patched
rust-brown tunic; eyes MILK-PALE in b07/b08, CLEAR DEEP BROWN from
b09. Face-board against build-63's frames. Eye-state is per-beat —
a pale eye after b09 or a brown eye before is a reject.

## Discreet anointing (b08, the row-136 pattern)

Posture only: fingertips (earth-dusted) at the closed lids, head
bent. Nothing clinical, no fluid.

## The casting-out (b09)

COLD, not violent: turned receding backs, a distant dismissing
gesture. The frame's weight is Jesus ARRIVING at his side — found,
not abandoned.

## Real dark (b05/b06)

The night genuinely dark beyond the lantern ring — the light does
not pretend the night is harmless. b06 direction: bearer AHEAD,
follower stepping into the lit footprints.

## Coverage shape

One true wide with stated geometry: b01 (camera past the moving
crowd's backs into the treasury). Eight Jesus beats. b10 closes on
the healed man's FIRST sunrise, walked beside its maker. File
order = story order.

- Plates: TEMPLE accepted (the build-06 b21 family anchor, same as
  43/75/131 — architecture only; identity-edit the frame's
  foreground trio if they leak). NIGHTROAD promote-first from b05.
