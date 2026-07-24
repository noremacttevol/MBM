# Audio Handoff — from Session #2 (audio maker) to the organizing session

**All 200 videos' ElevenLabs narration is done and on GitHub. 2,848/2,848 clips, verified 44100 Hz.**

## Where the audio is
- **Branch: `session-2-audio-clips`** on `github.com/noremacttevol/MBM`.
- Every build's clips live at `media-production/build-<N>-<slug>/audio/*.mp3` (+ `.timing.json`).
- Verified: every segment of every one of the 200 canonical transcripts is present and 44100 Hz
  (the new voices: narrator=Brian, jesus=Chris, god=Bill, scripture=Roger, woman=Matilda).
- It's on a BRANCH, not `main`, because a full push to main dies on the 54GB repo (HTTP 500) and this
  clone is diverged. Pull the audio from the branch, or merge the branch into main if you own that.

## How to pull the audio into your working tree
```
git fetch origin session-2-audio-clips
git checkout origin/session-2-audio-clips -- media-production
# (or cherry-pick just the build audio dirs you need)
```

## CRITICAL — do not repeat these traps
1. **A 44100 mp4 does NOT prove the new voice.** When a build is assembled, ffmpeg outputs 44100 even
   from the OLD 24000 edge-tts audio (it resamples). The ONLY proof a video has the new voice is that
   its SOURCE clips in `audio/` are 44100 AND the mp4 was RE-RENDERED after those clips landed.
2. **Clips revert.** In this shared clone, uncommitted audio gets restored to the old voice by git
   operations. Commit audio immediately, and before assembling a build, verify its clips.
3. **build-06-two-sons has a build-local `.gitignore` that ignores `audio/`.** Use `git add -f`.

## Tools I left you (on the branch)
- `media-production/verify-eleven-audio.sh <build>` — exits non-zero if any clip isn't 44100. GATE the
  assembly/ship on this: never build/ship a video whose clips fail it.
- `media-production/recover_from_history.py <transcripts_dir>` — if any clip reverts or goes missing,
  this re-downloads it FREE from the ElevenLabs account history (NO credits). Always recover, never
  re-voice — re-voicing bills again (that's how the credits got burned: ~8,210 billed generations for
  2,848 needed clips).
- `media-production/voice_from_transcripts.py` — the real ElevenLabs renderer (only use for brand-new
  transcript text not yet in history).

## What is NOT done (your lane)
- The mp4s must be RE-RENDERED from these clips. Correct clips ≠ finished video.
- Merging this branch to main / getting audio into the shipping flow is git-coordination.

Full honest failure account: branch `session-2-audio-report`,
`media-production/AUDITS/SESSION-2-AUDIO-FAILURE-REPORT.md`.
