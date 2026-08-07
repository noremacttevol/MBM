# QC — build-31-ten-virgins (C-FIX 2026-08-07, Machine A Dev)

## COMPLAINT LEDGER (open complaints on this row — Cameron's own words)

- **"The video stops playing and will not play through the 1:59 mark for some
  reason i can skip past it and it will play but its not playing correctly."**
  → **FIXED by clean audio re-encode.** Root cause: the shipped mp4's muxed AAC
  audio stream carried a corrupt packet — `ffmpeg -v error` decode reported
  `channel element 1.4 is not allocated` / `Invalid data found when processing
  input`. A corrupt audio packet stalls browser playback exactly as described
  (stops, can be skipped past, resumes wrong). The **video** stream and **every**
  source `audio/*.mp3` segment decode CLEAN — the corruption was only in the final
  mux. Fix: rebuilt the authoritative narration track from THIS build's own clean
  mp3s at the extract_beats offsets (`AUDIO_FROM_V1_SEGMENTS = True`, the sanctioned
  row-25/row-61 remedy) and re-encoded. **Nothing is re-voiced, re-timed, or
  resynthesised — the narration is byte-identical in content**; only the corrupt AAC
  encode was replaced with a clean one. Proof: `ffmpeg -v error -i <mp4> -f null -`
  on the NEW mp4 returns ZERO errors (was 2). `AUDIO REBUILD PASS`
  SHA256=e9fbe3f8949ba7216c14795a2084735cb9bc71fee98e7efb12b1a8538cff22cc.

## What changed this cut

- Re-assembled only. **No image generation — $0 Gemini spend, 0 rerolls.** All 40
  pictures are byte-identical to the 2026-08-02 realistic-V2 cut.
- Audio track rebuilt from 24 clean source mp3 segments (-22.2 LUFS → +7.2 dB),
  148.302 s. Final mp4: 20.9 MB, 148.3 s, faststart, mono AAC 44100.
- Verification frames (rendered mp4): early (8 s) captions in bottom band; 119 s
  (the exact former failure point) plays and renders clean — Jesus close-up with
  red KJV caption in bottom band; question card clean, no squares.

## Pictures / cast

- Untouched from the approved-style realistic-V2 cut; not re-QC'd frame-by-frame
  this session (pictures were not the complaint and were not regenerated).

RESUME (if interrupted): re-run `python3 media-production-v2/v2_assemble.py 31`
(AUDIO_FROM_V1_SEGMENTS is True → rebuild path), then deploy step 7c.
