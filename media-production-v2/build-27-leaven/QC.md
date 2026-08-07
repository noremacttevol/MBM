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

## §0c AUDIO-FIX lane 2026-08-07 (Machine A `Dev`, 2nd pass) — RE-CONFIRMED BLOCKED

Re-examined while sweeping NEEDS-AUDIO after row 185. Two findings:
- **Engine correction:** the segments are **44100 Hz / 128 k = ElevenLabs**, NOT edge-tts.
  So the earlier "deterministic, re-voice can't help" reasoning is void — an ElevenLabs
  re-render of a *named* segment would differ each take and could clear a subtle glitch.
  But that still needs the segment NAMED first.
- **New diagnostic — per-segment pacing:** chars/sec is uniform across all 10 spoken
  segments (13.1–17.9 cps; fastest n1/n3 ≈17.85, not extreme), so there is NO robotic
  too-fast/too-slow outlier to localize either. Combined with §0b (transcript, encode,
  levels, silencedetect all clean), FOUR independent headless diagnostics now come back
  clean. The defect Cameron heard is a subtle delivery/quality issue no mechanical check
  can name. **Still genuinely BLOCKED on one ear-pass.** $0, nothing changed.
  RESUME (correct engine): ear-identify the bad segment, then re-render ONLY it via
  `mbm_eleven.render_segment(text, speaker, out)` (ElevenLabs, same locked voice),
  atempo-match to its original duration, `AUDIO_FROM_V1_SEGMENTS=True`, re-assemble, C-FIX.

## §0d AUDIO-FIX lane 2026-08-07 (Machine A `Dev`, Fable-5 author lane) — TWO NEW headless diagnostics, still BLOCKED

Sweeping the one open complaint (COMPLAINT-FIRST + LOW-NUMBER laws). Ran two diagnostics
no prior pass had run. Both come back clean — **seven independent headless checks now find
nothing**; the block is real.

1. **Word-level timestamp transcript (stutter/doubled-word detector).** Transcribed every
   segment with `word_timestamps=True` and flagged adjacent duplicate words + words >0.9s.
   n1's transcript again *looked* doubled ("...every week..." then "...every day..."), but
   the word times prove it is the **faster_whisper trailing-silence hallucination**: the
   real speech ends at 5.76s ("...her own hands."), and every "second-pass" word is stamped
   at 5.76–5.94s with **zero duration**. n1.mp3 is 6.30s (single utterance + ~0.5s tail
   silence). NO real doubling. Only benign long word: n4 "hiding"=1.04s (deliberate). NO
   stutter, doubled, or cut word anywhere.
2. **Cross-engine s33 "spake" test (settles §0b/§0c).** §0b's isolated s33 transcribes
   "Another parable **spay key** unto them." I rendered the SAME text with a *totally
   different engine* (edge-tts SteffanNeural −18%/−9Hz, the SCRIPTURE voice) and it
   transcribes **identically** "spay key". Two unrelated engines producing the same
   mis-hearing = it is a **whisper artifact of correctly-pronounced KJV liaison**
   (/speɪk hiː/ ≈ "spay-key"), NOT a TTS mispronunciation. So s33 is fine; a "spake"
   respell is NOT warranted (it would fail its own A/B — the plain word is read correctly).

**Engine correction — §0c was WRONG, this is NOT ElevenLabs.** 44100 Hz / 128 k is the
**universal delivered format across the whole library** — approved rows 22/24/26/32 and
shipped rows 10/18 all measure 44100/128k, and row 22 is a *confirmed edge-tts* AUDIO-FIX
(the "shouldest" respell). Raw edge-tts is 24 kHz; the pipeline re-encodes final segments
to 44100/128k. So row 27's audio is edge-tts, re-encoded, and **byte-indistinguishable from
approved rows in sample-rate, bitrate, LUFS (−15.1), peak (0.0 dB), channels, encode
integrity, per-segment cps, and now word-timing.** It is on the same (new) voices as the
approved rows — this is NOT an old-voice / REDO-ALL case.

**Why still no fix at $0 headless:** every mechanical dimension is clean or matches approved
work; the defect Cameron heard is a subtle delivery-quality issue no check can name. A blind
re-voice of all 11 segments (edge-tts, deterministic) would reproduce the same waveforms OR,
if forced different, change every timing for **zero expected benefit** — the exact worse-than-
an-honest-block failure this QC already warns against. **$0, nothing changed, no pictures
touched.**

**RESUME (unchanged, needs one ear-pass — Cameron or any machine with audio playback):**
play `matthew-13_leaven.mp4` once, note the timestamp where the delivery sounds wrong, map
it to the segment via the outline (n1 0–6.5s, s33 7–9.6s, j1 10.7–18.8s, n2 19.8–28.7s,
n3 29.3–36.1s, n4 36.7–44.7s, n5 45.3–54.6s, n6 55.2–65.0s, n7 65.6–78.6s, n8 79.2–91.2s,
card 91.8s+). Then it is a targeted single-segment edge-tts input fix (respell/punctuation/
rate — A/B via check_pronunciation.py), regen ONLY that mp3, remap only the affected
still-windows for the small duration delta, re-assemble, C-FIX. Everything else is verified
clean seven ways.

## §0e AUDIO-FIX lane 2026-08-07 (Machine A `Dev`, Fable-5 author lane, 4th pass) — 8th diagnostic (voice identity) CLEAN + structural lead

Swept the top open complaint again (COMPLAINT-FIRST + LOW-NUMBER). Ran one diagnostic no
prior pass had run, plus scrutinised the narration TEXT as content (not waveform).

1. **Per-segment voice-identity scan (wrong-voice detector) — NEW, CLEAN.** A segment
   rendered in the WRONG speaker's voice (e.g. the Jesus red-letter j1 coming out in the
   narrator voice, or a narrator line in the Jesus/scripture voice) would sound "messed up"
   yet pass every transcript / level / timing / encode / cps / word-timing check already run.
   Measured median voiced F0 (autocorrelation, numpy) of all 11 segments:
   - **JESUS j1 = 84 Hz** — distinctly the LOWEST (deeper Jesus voice, correct).
   - **NARRATOR n1–n8/card = 88–118 Hz, median 98 Hz** — one consistent male narrator.
   - **SCRIPTURE s33 = 102 Hz** — its own register, between the two.
   Three correct, distinct male voices; no segment is voiced by the wrong speaker. n2's 118 Hz
   is the top of the narrator's normal prosodic range (an emphatic line), not an outlier voice.
   **Eight independent headless diagnostics now find nothing.** The block is real.

2. **Narration TEXT read as content (not waveform).** `make_narration.py` SEGMENTS are clean
   English — no doubled phrase, no stray pause mark, no truncated clause. The n1 "doubling"
   whisper flagged is a hallucination (the word "every day" is NOT in n1's text; n1 says
   "every week … her own hands"). Nothing in the written text is malformed.

**Forward LEAD for the ear-pass (the one structural thing unique to row 27).** Row 27 is the
ONLY build in the library where a mid-sentence KJV attribution clause was split into its own
2.4 s micro-segment in a THIRD voice between the narrator on-ramp and Jesus (the SPEAKER-LAW
rebuild). So in the first ~11 s the ear hears narrator → a 2.4 s formal fragment ending on a
hanging semicolon ("Another parable **spake he** unto them;") → Jesus. Two things there could
read as "messed up" even though every segment is individually clean and no law is violated:
(a) three distinct male voices inside 11 s is a fast switch; (b) as a STANDALONE cut, opening
the retelling with "**Another** parable spake he" is confusing — there was no *first* parable
in this video (it's "another" only in Matthew 13's sequence after the mustard seed). **If the
ear-pass localises the wrongness to 0–11 s, this is the cause, and it is CONTENT not a
waveform artifact** — the fix is scripting, not a re-render: e.g. keep s33 blue/scripture per
SPEAKER-LAW but reconsider whether the standalone cut should lead on the attribution clause at
all, or let n1 flow straight into j1 with s33 folded differently. This is why eight waveform
diagnostics cannot see it. **$0, nothing changed, no pictures/audio touched.** (Scan:
`/tmp/f0scan.py` method — decode each mp3 to 16 kHz mono, autocorrelation F0, median over
voiced frames.)
