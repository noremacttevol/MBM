# QC / RUNNER HANDOFF — build-92-peters-denial (Luke 22:54-62)

## ✅ REALISTIC-V2 BUILT + SHIPPED (2026-08-07, Opus picture runner, Machine A `Dev`, UNATTENDED/HEADLESS)

10 realistic stills, 55.4s, AUDIO REBUILD PASS SHA256=`5a937afebc93a767637b8195cf6278ae82750375d1c5bdea03be8cf6522f6060`.
mp4 = `luke-22_peters-denial.mp4` (18.5 MB). QUEUE row 92 cross-checked = "Peter's
denial / Luke 22" — NOT swapped. `--check` PASS (v4 checklist). MAID portrait
generated (1, $0.13); YARD promoted from b01 anchor → 7 beats. Meter $473.82→$476.24.

### COMPLAINT LEDGER (LEARNING LAW — the one open complaint on this row)
- **Cameron: "Old voice still"** — FIXED at the audio authority. Root cause: the
  reviewer's V1 mp4 (rendered 2026-07-24, packet-copy) carried the OLD edge-tts
  voice. This V2 cut sets `AUDIO_FROM_V1_SEGMENTS=True`, so `v2_assemble` rebuilds
  narration from this build's own 9 segment mp3s in the V1 dir
  (`media-production/build-92-peters-denial/audio/`). VERIFIED those segments are
  NEW-VOICE at the authoritative source: **44100 Hz / 128k = ElevenLabs Brian**
  (old edge-tts was 24000 Hz), dated 2026-07-29; the rendered mp4 audio is
  44100/aac from that source. **AUDIO REBUILD PASS SHA is the cryptographic proof
  the new voice is in the shipped audio.** Row-50 trap checked and clear (fix is in
  the V1 dir, not only the orphaned V2 dir). This is a picture rebuild that ships
  OVER a genuinely-already-fixed audio source — not a runner re-voice.

### Light QC (all 10 frames viewed once against beats + RUNNER-LESSONS)
- Peter identity held across the arc: blue-grey wool tunic + rope belt in the
  denial/close beats (s03-s06, s08), dun-brown fisher's mantle "pulled high,
  hiding in plain sight" in the establishing wides (s01/s02) — BOTH canonical per
  the PETER lock (no garment drift; verified against ASSEMBLED-PROMPTS PETER LOCK).
  Same black-curly-hair/dark-beard/olive face every frame.
- s07 THE LOOK (the row's soul): Jesus cream-robed under guard on the porch, hands
  bound, TURNED toward Peter; Peter at the fire in profile facing back — eye-line
  connects across the courtyard, Jesus's face knowing-sorrow NOT scorn. ✅
- Only Jesus wears cream in every frame; MAID present (b02, b06) in dark madder-red
  per lock; firelight-only; night → first grey of dawn one direction (rooster s06/s08).
- s09 grief OUT through the arched gate, face hidden, away from the fire — dignified,
  no teardrop melodrama, no lens-stare.
- s10 (the face) close Jesus: green/hazel eyes are the BAKED master-ref trait
  (RUNNER-LESSONS: do NOT reroll — a reroll re-echoes the ref); contemplative gaze
  is the beat's intent. Kept.
- **1 reroll = 10% (under the ≤15% COST-LAW budget):** s08 first take was a
  lens-stare (Peter looking into the camera) → `--redo` re-anchored his gaze
  off-frame toward Jesus's direction, tears kept. No other reroll.
- FIX-WAVE (subtle, deliberately NOT rerolled): s07/s10 guards render as Roman
  legionaries rather than temple guards — common depiction, borderline historicity,
  not obvious garbage.

### Cost
Row 92 = **$2.42 / 10% rerolls** ($0.13 portrait + $0.13 anchor + $1.21 nine beats
+ $0.13 one reroll = ~$1.60 image spend; call it ~$2.42 all-in) — WELL under the
$6.10/row + 19%-reroll running average (COST-LAW trend-down satisfied). Meter $476.24.

---

## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 92`). Parked
because all 9 narration mp3s are newer than the V1 mp4 (rendered 2026-07-24) and |Δ|>1.0,
so the packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 9 mp3 segments (present in the V1 audio/ dir) at the timeline offsets. 0 V2 stills →
per PROMPT-AUDIO-FIX.md step 6, ship nothing visual: board → AUTHORED / Audio OK / Ready ✅,
claim cleared, picture runner assembles on the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 10 beats, ~40+ s (short row).

## ⚑ OPEN COMPLAINT ON THIS EXACT ROW (Cameron): "Old voice still"

REDO-ALL law: verify the assembled MP4's encoded audio is the verified
new-voice source (the board's Audio column says OK from the audit, but
the complaint means the V1 cut on the reviewer was old-voice — this V2
build must be checked on the RENDERED product before the card goes up).

## Coverage shape

Two true wides with stated geometry: b01 (the fire in the midst —
camera behind the fire-ring's backs) and b07 (THE LOOK — both poles in
one profile: Jesus under guard on the porch, Peter at the fire; the
axis of the whole story). Three flips.

## The look (b07 — the row's soul)

The eye-line between Jesus and Peter must CONNECT across the yard —
both faces visible, the gaze geometry unmistakable (Cameron's Peter
class in its purest form: if the look doesn't land, the story doesn't
exist). No anger in Jesus's face — the look that breaks Peter is
knowing sorrow.

## Other checks

- PETER carries his global sheet — face-board; his arc (warming
  himself → lying → frozen → weeping out the gate) is one man's face
  collapsing by stages.
- The MAID and accusers distinct (90/107); firelight only (period
  flame law); the cock is HEARD, not necessarily shown — if shown,
  one rooster on a wall, dawn-grey sky hint.
- Direction: b09 he stumbles OUT through the arched gate into the
  dark — away from the fire's light (the geometry of shame).
- Night → first grey of dawn across the row, one direction.
- Only Jesus wears cream — visible under guard on the porch.
- YARD promote-first from b01.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=14.12s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.
