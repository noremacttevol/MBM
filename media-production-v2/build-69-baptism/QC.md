# QC / RUNNER HANDOFF — build-69-baptism

Complaint-gate addendum, 2026-08-05 (Machine A).

## OPEN CAMERON COMPLAINT — gates before build

"John is way too big in the first picture."
SCALE GATE (rubric lesson 14), gated in b01's must_not_show: John
ordinary-sized against the penitent and the bank crowd in EVERY
frame, not just b01. Check every John-bearing frame side by side.

## COMPLAINT LEDGER (LEARNING LAW — filled by runner, 2026-08-06 A-auto)

- OPEN complaint (v2_outline): "John is way too big in the first picture."
  FIXED. The scale-gate is authored into b01's must_not_show and I
  verified it frame-by-frame: in b01 (s01-down-at-the-jordan-river) John
  baptizing in the water reads the SAME height as the penitent under his
  hands and the bank crowd — an ordinary man, not enlarged. I then checked
  every OTHER John-bearing frame side-by-side (b02, b06, b07, b08, b09,
  b12, b13, b16, b17, b19, b26, b29): John is ordinary-sized against Jesus
  and the crowd in all of them. Jesus is likewise ordinary-sized in every
  multi-figure frame. The review card answers Cameron in his own words.

## RUNNER QC NOTES (2026-08-06 A-auto, Machine A / Dev)

- 29 beats + 1 portrait (BAPTIST). JORDAN promoted from b01 (a clean,
  no-Jesus river frame → 20 beats). DOVE NOT promoted (its anchor b24 is a
  Jesus-bearing frame; rubric lesson 11 forbids handing a Jesus frame to
  place-wiring — DOVE beats carried by text lock + face lock, and the dove
  reads as one consistent real white bird across b20/b21/b22/b24/b26).
- Godhead gate PASS: the Father is shown ONLY as opened-sky light/shaft
  (b18, b20, b21, b22, b26) — never a figure. The Spirit is one real white
  dove. No halo/glow/rim-light on Jesus anywhere. Only Jesus wears cream.
- REROLLS: 1 beat, 2 attempts (b19). First take had a vertical panel/
  collage seam on the right edge + Jesus's robe read tan not cream (collage
  defect, reroll-on-sight per RUNNER-LESSONS). Reroll #1 landed a clean
  single John but drifted indoors; reroll #2 landed the correct river shot
  (John gesturing at himself, Jesus in cream, penitents on bank). Kept #2.
  Reroll rate = 2/29 = 6.9% — under the 15% COST LAW budget.
- FIX-WAVE (subtle drift, NOT rerolled per cost law — do not chase):
  (a) John's hair greyness varies slightly between frames (greyer/lighter
  in b12 vs darker in b02/b06/b07/b09); lesson-2/13 identity drift, minor.
  (b) b03 (s03) distant background baptizer robe reads a muted light-tan
  that could faintly echo cream — but it is a tiny, distant, faceless
  background figure, not a second cream-robed Jesus; b10 covers the same
  beat-type with John clearly in brown.
- Spend this row: ~$4.27 (1 portrait + 29 beats + 2 rerolls). Under the
  $6.10/row baseline. Reroll % 6.9% under 19% baseline. COST LAW: trend down.

## 🛑 RUNNER PARK — AUDIO-LOCK BLOCKER (2026-08-06 A-auto, Machine A / Dev)

ALL 29 stills + BAPTIST portrait are GENERATED, QC'd and PASS (see the
COMPLAINT LEDGER + QC notes above — the scale complaint is fixed). The row
is BLOCKED only at assembly:

`v2_assemble.py 69` FAILS the AUDIO LOCK:
  "extracted timeline is 172.277s but the authoritative V1 final is 206.633s."

ROOT CAUSE (runner diagnosis, not a runner-fixable item):
- V1 mp4 `media-production/build-69-baptism/matt-3_baptism-of-jesus.mp4`
  = 206.633s, rendered Jul 29 09:47.
- That build's `make_narration.py` was edited LATER (Jul 29 23:03), so the
  V1 mp4 predates the current narration script — it is STALE.
- The current V2 narration segments (build-69-baptism/audio/*.mp3, 14 files)
  sum to 161.07s → 172.277s timeline. A 34s gap vs the stale V1 mp4.

WHY THE RUNNER DID NOT FIX IT:
- The assembler's hint is "set AUDIO_FROM_V1_SEGMENTS = True in this row's
  beats_v2.py." Editing beats_v2.py is OUTSIDE the runner's allowed writes
  (art / QC.md / boards / SESSION-LOG / review card / mp4 only) and audio
  is an author decision under the REDO-ALL / audio-immutability law. The
  runner must not improvise on audio (brief step 6: audio-hash fail → STOP,
  log, do not ship).

AUTHOR ACTION NEEDED (Fable 5 author session):
- Decide the authoritative audio: either (a) re-render the V1 mp4 from the
  current (post-Jul-29-23:03) narration so V1 == 172.277s and the lock
  matches, OR (b) set `AUDIO_FROM_V1_SEGMENTS = True` in
  build-69-baptism/beats_v2.py if the current 14 segment mp3s ARE the
  intended byte-identical audio, then re-verify. Confirm the audio is the
  correct NEW-voice cut before flipping either switch.

RESUME COMMAND (after author fixes audio):
  cd media-production-v2 && python3 v2_assemble.py 69   # must print AUDIO LOCK PASS
  # then follow PROMPT-OPUS-RUNNER.md step 7 (ship: two commits + firebase deploy + live verify)
  # stills are already generated — do NOT regenerate; reroll budget already spent 6.9%.
