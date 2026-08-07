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

## §0b AUDIO-FIX lane 2026-08-07 (Machine A `Dev`) — HEADLESS DIAGNOSTICS EXHAUSTED → BLOCKED (needs ear-check)

Claimed as the next NEEDS-AUDIO row. Ran every mechanical check available headless
to localize the defect. **The audio is indistinguishable from approved, clean rows —
I could not localize a defect without listening, and blind re-voicing cannot fix it.**

What was checked and RULED OUT (all clean):
- **Words/pronunciation:** full-mp4 faster-whisper transcript is correct end to end,
  including s33 "Another parable **spake he** unto them" (the per-segment "spay key" was
  context-starvation — whisper can't spell archaic "spake" in isolation; in full context
  it spells it right). n1's isolated transcript looked "doubled" but that is a whisper
  loop artifact on a short clip: `silencedetect` shows NO internal gap and n1 is 6.30s =
  single-utterance length, so n1 is a single clean pass. No garbled/doubled/missing word.
- **Encode integrity:** `ffmpeg -map 0:a -f null` decodes the muxed AAC with **0 errors**
  (this is NOT the row-31 corrupt-packet class).
- **Levels:** per-segment mean −25…−27 dB, no source clipping; delivered mp4 measures
  **I=−15.1 LUFS, LRA 5.1, peak 0.0 dB** — IDENTICAL to approved rows 22/24/26/32 (all
  peak 0.0 dB, ~−15 LUFS). Not an outlier; the 0.0 dB peak is the shared limiter output,
  not a row-27 defect.
- **Stream/channels:** one mono audio stream, no phase/L-R/DC issue possible.
- **Timeline:** durations match the outline; A/V aligned at 104.47s.
- **Provenance:** Cameron reported against git-blob `1e389df4` = content-sha1
  `a0193524` = the CURRENT committed cut (not an older render). V2 audio md5
  `e6fffafb` == V1 audio md5 (AUDIO LOCK copy). So he reviewed exactly this cut.

**Why blind re-voicing was NOT done:** edge-tts (Azure neural) is deterministic for a
fixed (text, voice, rate) — regenerating any segment with the same input yields the same
waveform, so it cannot cure a delivery artifact. The row-10 precedent fixed a robotic
take by CHANGING the input (removed ellipsis / adjusted rate) on a KNOWN segment. Without
ears I cannot know which segment or what input change, and re-voicing all 11 blind would
change every timing for zero expected benefit — a worse, cost-ier failure than an honest
block. $0 spent, no pictures touched, no audio changed.

**RESUME (needs one ear-pass — human or a machine with audio playback):**
1. Play `matthew-13_leaven.mp4` once and note the timestamp where the delivery is wrong
   (map it to the segment via the outline: n1 0–6.5s, s33 7–9.6s, j1 10.7–18.8s,
   n2 19.8–28.7s, n3 29.3–36.1s, n4 36.7–44.7s, n5 45.3–54.6s, n6 55.2–65.0s,
   n7 65.6–78.6s, n8 79.2–91.2s, card 91.8s+).
2. Then it is a targeted single-segment input fix (respell / punctuation / rate), regen
   ONLY that mp3, set `AUDIO_FROM_V1_SEGMENTS = True`, remap only the affected still-
   windows for the small duration delta (see row-22 method in SESSION-LOG 2026-08-07),
   re-assemble, ship via C-FIX. Everything upstream of that one segment is verified clean.
</content>
</invoke>
