# Story 1 Realistic V3 QC — The Woman Who Touched His Cloak

Final candidate: `mark-5_woman-touches-his-cloak-realistic-v3.mp4`

## Delivery proof

- 20 realistic 9:16 source pictures in `assets-realistic-v3/`.
- 17 pictures received identity-only repairs; `s08`, `s09`, and `s19`
  remain byte-for-byte identical to the existing realistic draft.
- Final: 1080×1920 H.264, 30 fps, AAC mono 44.1 kHz,
  108.833333 seconds, 20,309,268 bytes.
- Final Git blob SHA-1: `ce61e1856757c0370d1acd14e4ea022903f54add`.
- Final SHA-256: `f32d742ff644deb6c9cc222482cbd45fa7f076b25816e623a9dc376324053c25`.
- Encoded-audio packet SHA-256:
  `d88c1fe8beb1dabcbea63b8664e41d4173d8a84345a386a95a8be3e1a32097b9`.
- `v2_prompt.py --check`: PASS for all 20 beats under the V4 checklist.
- `v2_identity_board.py --check`: PASS for both recurring identities and all
  25 configured face appearances.
- `admin/verify-mp4.sh`: PASS; video is 108.833333 seconds, audio is
  108.831995 seconds, and the moov atom is readable.
- One decoded frame from every beat plus the closing card was inspected in
  `DECODED-QC-V3.jpg`. The longest detected silence is 1.90848 seconds.

## Audio and script fidelity

- Cameron's open complaint on the V1 hash is: “Back ground sound problem again
  when Jesus was talking.” The defect is real: pauses in both original Jesus
  sources register as silence at −45 dB but not at −50 dB, unlike the narrator.
- Both Jesus sources are confirmed **Alexander**, voice ID
  `UMnEnzK9QLLdRwnUyxMW`, by the ElevenLabs history entries and the exact source
  hashes recorded in `AUDIO-SOURCE-MANIFEST.json`.
- No narration was generated, rewritten, shortened, reordered, or retimed. The
  complete authoritative V1 audio is the base; only `j0` at 62.120–63.740 and
  `j1` at 85.072–90.505 are muted and replaced by those same source files after
  `highpass=f=75,afftdn=nf=-32:nt=w`.
- The repaired encoded pauses now register as silence at −50 dB. Mean loudness
  remains within 0.4 dB of the original Jesus windows.
- The audio packet hash intentionally differs from V1 because this complaint
  authorized a selective denoise. `repair_alexander_room_tone.py` fails closed
  if either Alexander source hash changes and makes no network or TTS request.

## Visual continuity and action

- The existing realistic compositions were preserved instead of reinvented.
  Every identity edit prompt locked camera, crop, lighting, bodies, poses,
  hands, feet, clothing, props, people count, spacing, and story action.
- Jesus is compared to one canonical portrait across 11 clear appearances; the
  woman is compared to one canonical portrait across 14 appearances. The final
  hash-backed face boards are saved in `identity-boards-v3/`.
- The physicians/money exchange, woman entering from the crowd edge, and Jesus
  remaining ahead of her all read in sequence.
- The hinge frame `s11` visibly keeps her fingertips at the lower hem from
  behind—no grabbing, extra fingers, moved garment, or face-on approach.
- The disciple-response frame retains the same principal foreground group. The
  woman remains kneeling when found; Jesus crouches at her level without an
  artificial worship circle. The last picture has her departing peacefully
  through the crowd while Jesus remains behind her.
- Captions retain their speaker colors and are readable on the decoded sheet;
  the full closing invitation is present.

Publishing this new hash returns Story 1 to **Unwatched** while retaining the
old background-noise complaint for comparison. The mobile app and app-feed
video remain unchanged.

## OPEN CAMERON COMPLAINT (2026-08-01) — gate before rebuild

"1:10 picture has Jesus's eyes looking weird" → beat v2-r001-b15
(64.73-77.21). Jesus's eyes must be natural, symmetrical, both open
and aligned on the same point; inspect at full resolution. Any
wall-eye / cross-eye / mismatched-pupil / dead-stare read = reject
and reroll. Face-board Jesus hardest at this beat.
