# build-27-leaven — QC

## §0 RUNNER PARK (2026-08-07, Machine A Dev) — NEEDS-AUDIO

**COMPLAINT LEDGER (open, from `v2_outline.py 27`):**
- Cameron: **"Audio is messed up on this one."** — AUDIO-domain complaint.

**Why parked, not shipped:** The complaint is about the AUDIO itself, not the
pictures. The runner is forbidden to re-voice (audio-immutability). Per
RUNNER-LESSONS ("PACING/rushed/messed-up delivery complaints are audio-domain —
park them the same as a mispronunciation"), a generic "audio is messed up"
complaint is a re-voice / narration-regeneration job that lives one stage
upstream with the FABLE 5 author. Shipping a picture re-cut over an open audio
complaint would leave the audio unchanged and repeat the complaint — the worst
failure this pipeline can produce. **$0 spent, no pictures touched.**

**Runner diagnostics (for the author — narrowing, not a fix):**
- Board Audio column = OK only means the AUDIO LOCK hash matches V1; it is NOT a
  statement that the audio is *correct*. The complaint is that the delivery/audio
  is wrong, which AUDIO LOCK cannot catch.
- All 11 segments render and their durations line up with the outline
  (n1 6.30s, s33 2.40s, j1 8.07s, n2 8.91s, n3 6.82s, n4 7.97s, n5 9.43s,
  n6 9.74s, n7 12.98s, n8 12.02s, card 7.13s). mp4 = 104.47s A/V aligned. So it
  is not a truncated/missing segment or an A/V length mismatch — the defect is
  inside the spoken delivery of one or more segments (glitch, stutter, wrong
  voice, clipping, doubled/garbled word, or bad pacing). The author must LISTEN
  to matthew-13_leaven.mp4 to localize which segment(s).

**AUTHOR resume (FABLE 5):**
1. Listen to `build-27-leaven/matthew-13_leaven.mp4` end to end, identify the
   exact segment(s) where the audio is wrong (n1, s33, j1, n2–n8, or card).
2. Fix at the narration source — `make_narration.py` (SPOKEN/PHRASE_SPOKEN
   respell for a mispronounced/garbled word, or bump stability / re-render for a
   glitchy TTS take; use a modern American Jesus voice for j1, never Multilingual).
3. Regenerate ONLY the offending segment mp3(s), re-assemble
   (`v2_assemble.py 27`, AUDIO LOCK will re-hash to the new audio), verify by ear
   (`qc_narration.py`), then ship via C-FIX so the review card answers Cameron's
   complaint in his own words ("Your complaint 'audio is messed up' — the
   <segment> was re-voiced and re-checked by ear").
4. No picture defect was found or filed — do NOT re-cut stills; touch audio only.
</content>
</invoke>
