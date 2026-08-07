# QC / RUNNER HANDOFF — build-69-baptism

## ✅ C-FIX SHIPPED 2026-08-07 (Machine A / Dev) — John's hair "changed to orange"

COMPLAINT LEDGER (v2_outline, OPEN → NOW FIXED):
  "Johns hair changed to orange and its not keeping his character to the
   reference we have in multiple pictures please check all and redo ones
   that he doesnt look like what the reference laid out for him."

ROOT CAUSE + WHAT FIXED IT:
- Checked ALL 14 John-bearing frames side-by-side against the locked
  reference CAST-REF-V2/baptist.jpeg (black hair with grey streaks, full
  dark beard, tan skin): s01, s02, s06, s07, s08, s09, s12, s13, s16, s17,
  s19, s21, s26, s29. Thirteen of the fourteen already carry correct
  black/grey hair. The ONE outlier was **s12 (beat b12)** — under the warm
  low side-light John's hair rendered a light sandy grey-gingery tone that
  reads "orange," clearly off the black reference. This is exactly the drift
  the prior FIX-WAVE note (a) flagged ("greyer/lighter in b12"); Cameron's
  complaint escalates it from FIX-WAVE to must-fix.
- FIX: `v2_gen_api.py build-69-baptism --only b12 --redo` — ONE reroll,
  re-anchored to the BAPTIST face-lock ("sun-shot black hair") + the
  reference image. New s12: John's hair is dark black/grey matching the
  reference, full dark beard; Jesus in cream (only cream-wearer), no
  halo/glow, both figures ordinary-sized, action reads (Jesus lowering
  John's protesting hands), anatomy clean, nobody faces the lens.
  Original saved to /tmp/s12-orig-backup.jpeg (not committed).
- Verified in the RENDERED mp4 at t=63s (s12 window 61.04-66.42): the fixed
  black-haired John is on screen; caption in the bottom band; question card
  clean.

TOUCH-ONCE / COST: this was the only open complaint on the row. 1 reroll of
29 beats = 3.4% (well under the 15% budget). Spend this C-FIX ≈ $0.13.

AUDIO UNTOUCHED — byte-identical to the shipped cut: AUDIO REBUILD PASS
SHA256 = 7132e43f637005e1bb774c0635ee7eaf11a3be295ff646d5938fead5c3040684
(same hash as the 2026-08-06 ship), mp4 172.3s. No TTS, no wording, no
timing changed — only the s12 picture.

---

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

## ✅ AUDIO-FIX RESOLVED (2026-08-06 AUDIO-FIX session, Machine A / Dev)

STALE-V1 class — fixed at $0 (no new TTS, no image generation). Root cause was
exactly as the park note below diagnosed: the V1 mp4
`media-production/build-69-baptism/matt-3_baptism-of-jesus.mp4` was rendered
2026-07-29 09:47, BEFORE the REDO-ALL re-voice batch re-rendered every narration
segment at 2026-07-29 23:03. The mp4 therefore carried the stale pre-REDO-ALL
voices; the 14 segment mp3s on disk are the intended NEW voices.

FIX APPLIED: `AUDIO_FROM_V1_SEGMENTS = True` in build-69-baptism/beats_v2.py
(this was already staged uncommitted from a prior parked session; this session
committed it and finished the ship). `v2_assemble.py 69` then rebuilt the
narration track from the 14 new-voice V1 mp3s at the extract_beats offsets —
byte-for-byte the source the V1 build would have used had it been re-rendered.

AUDIO BASELINE CHANGE (sanctioned by the STALE-V1 exception, not accidental drift):
- OLD (stale V1 mp4 audio, pre-REDO-ALL voices) — card hash a6a3921d671f, 206.633s.
- NEW (rebuilt from 14 new-voice 23:03 mp3s): timeline 172.277s, final mp4 172.3s.
  AUDIO REBUILD PASS SHA256 = 7132e43f637005e1bb774c0635ee7eaf11a3be295ff646d5938fead5c3040684.
- Segments re-voiced this session: NONE (the mp3s were already the new voice; the
  only change is which audio source the assembler uses). No wording, timing, or
  voice was altered.
- Verification: ffprobe confirms aac audio, 172.300s, mean_volume -15.5 dB (on the
  -15 LUFS target), not silent. Assembler AUDIO REBUILD gate passed.

Cameron's open complaint on this row was the SCALE complaint — "John is way too
big in the first picture" — which the picture runner had already fixed in the
stills (s01: John is ordinary human scale beside the confessing man, gated in b01).
The row sat NEEDS-AUDIO only because the stale-V1 lock blocked assembly; this
session cleared that so the fixed, new-voice cut could ship.

## 🛑 RUNNER PARK — AUDIO-LOCK BLOCKER (2026-08-06 A-auto, Machine A / Dev) — SUPERSEDED, see RESOLVED note above

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

## ✅ AUDIO FIX DONE — AUDIO_FROM_V1_SEGMENTS (AUDIO-FIX job, A-auto 2026-08-06)
The audio-lock blocker is CLEARED. Root cause was a STALE V1 mp4 (206.633s,
Jul-29 09:47) that predated this build's current narration; the assembler was
copying it instead of the real audio. Fix: set `AUDIO_FROM_V1_SEGMENTS = True`
in beats_v2.py so the track is rebuilt from this build's own 14 SPEAKER-LAW
segment mp3s at the extract_beats offsets.

- **Verified the segments are the intended new-voice cut before flipping:** exact
  14/14 segment-ID parity between make_narration.py's SEGMENTS
  (n0,n1,s14,n1b,n2,j1,n3,n4,n5,s17,jv1,n6,n7,card) and audio/*.mp3 — no missing,
  no extra. make_narration.py imports GOD/JESUS/NARRATOR/SCRIPTURE via
  save_speaker_narration (SPEAKER-LAW = new voices); ear-check jv1 (Father) =
  "This is my beloved Son, in whom I am well pleased." The "Jul-29 23:03" the
  park note flagged was a working-tree mtime, not a SEGMENTS content change.
- **Assembly result:** `v2_assemble.py 69` → `AUDIO REBUILD PASS` /
  `AUDIO LOCK PASS`, mp4 172.277s (was blocked at 206.633s vs 172.277s mismatch).
  No new TTS, $0 — the segments are byte-identical, only the combined track was
  rebuilt from the correct source.
- **NOTE (multi-lane 2026-08-06):** a concurrent audio-fix lane re-assembled row
  69 in the shared tree at the same time; both produce the identical deterministic
  mp4 from the same inputs. Ship is idempotent (pull-rebase + card-hash check).
- COMPLAINT LEDGER: open complaint "John is way too big in the first picture"
  (scale) was already fixed in the 29 realistic stills; this audio fix simply
  unblocks that fixed cut so it can finally reach the reviewer.
