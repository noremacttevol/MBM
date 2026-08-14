# QC / COMPLAINT HANDOFF — build-44-pentecost

## C-FIX — Codex `Dev`, 2026-08-13

### COMPLAINT LEDGER

- OPEN, reported twice against Reviewer hash
  `102f1cbbd06fc5843fd9791a90d7ee5c154bf7e5`: **"1:38 picture needs to be
  redone there are buildings in the sky. Same problem again. Replace that
  picture."**
- Exact trace: 1:38 is b17 / `s17-cut-to-the-heart.jpeg`, window
  95.17–101.70. Rendered samples at 96, 98 and 100 seconds all prove the defect
  is in the source still: a second row of Jerusalem buildings floats in open
  sky above the real ground-level city.

### Prompt autopsy — ALLOWED

The emotional beat requested a close but did not bound the background. Its
`JERUSALEM-COURT` place lock also names houses and temple walls beyond, which
allowed the model to combine the close crowd, the plate's ground-level city,
and another incompatible upper skyline. The old prompt did not explicitly ban
floating/duplicated architecture, a mist seam, or a second vertical perspective.

Author repair before any paid pull:

- b17 is now a tight eye-level chest-to-head close of exactly three adults.
- No sky can appear. One continuous softly blurred limestone wall fills the
  entire background edge to edge at ground level.
- The negative gate bans all skyline, rooftops, towers, distant/duplicated or
  floating buildings, architecture above heads, fog seams, panels, collage,
  and a second perspective.
- Only b17 will be regenerated. The other 23 accepted stills and every byte of
  the existing audio remain untouched.

Before ship: prompt/face gates, inspect the native source at full resolution,
assemble, prove the audio packet hash unchanged, view all 24 rendered beats plus
captions/card, run exact-byte receipt and full project QC, publish a new Reviewer
hash as Unwatched with this complaint retained.

### Replacement source gate — PASS

- One successful Gemini 2K generation, approximately **$0.13**. The endpoint timed
  out twice before the successful retry; only the saved result was entered in the
  spend ledger.
- Full-resolution source inspected at 1536×2752. Exactly three separate grieving
  adults fill the frame chest-to-head; the first man's hand is naturally attached
  with five digits, the other bodies and faces are clean, and first-century clothing
  is coherent.
- Background is one continuous softly blurred pale-limestone wall. No visible sky,
  skyline, roof, tower, floating/duplicated architecture, fog seam, panel, collage,
  or second perspective. Cameron's 1:38 complaint is visually absent in the source.

Next gate: assemble against the unchanged existing audio, then inspect the rendered
replacement at 96/98/100 seconds and the full 24-beat cut.

### Final rendered full-cut gate — PASS

- Reassembled all 24 still beats with the existing 11-segment audio. Old complained
  cut and new cut have the identical encoded-audio packet SHA-256
  `954a7f75990aedbf47d98313f1ef8c3c487407af38d8f376b17b2ab2a13d5d14`:
  no voice, word, pause, or timing changed.
- Rendered b17 inspected at 96, 98 and 100 seconds. The slow crop remains entirely on
  the three grieving adults and one continuous wall; no sky or floating architecture
  enters at any point. Caption is synchronized and inside the bottom band.
- Extracted and viewed one midpoint frame from every rendered beat, 1–24, in story
  order. Realistic-only, Peter/cast continuity, flame-not-burning law, anatomy,
  period setting, actions, captions, and scene logic all PASS. No unrelated still was
  regenerated.
- Closing card viewed at 139, 142 and 145 seconds: stable full frame, clean serif text,
  no crop/jump/typo-square. Question/invitation remains readable.
- Narration ear/transcript check PASS for all 11 existing source segments (nine at
  1.00 match, s2 at 0.97, n6 at 0.98). `verify-mp4.sh` PASS and full ffmpeg decode
  PASS. Final MP4: 1080×1920 H.264/AAC mono, 146.300s video / 146.283s audio,
  20,937,218 bytes; standard MP4 SHA-256
  `6216228a2fc822908e4f45a69af780be0b75aa36094b468832a116349dac7a88`.

Exact-byte render receipt recorded for the final 20,937,218-byte MP4. Final
`admin/qc_gate.py` PASS with Whisper enabled and zero reasons. Ready for Reviewer
publication as a new Unwatched revision with Cameron's prior complaint retained.
