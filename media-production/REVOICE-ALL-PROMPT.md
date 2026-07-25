# PROMPT — Re-voice ALL 200 videos with the new voices + Jesus's pauses

Paste into a session on the MBM machine (`~/Desktop/MBM`).

---

Re-voice every one of the 200 Milk Before Meat videos with the new voice cast and ship
each rebuilt video, one at a time, to the standard in `media-production/CRITIQUE-LAW.md`.

Everything is already configured — you are RUNNING it, not deciding it:
- **Jesus = Alexander** (`mbm_eleven.py` VOICE_ELEVEN[JESUS], id `UMnEnzK9QLLdRwnUyxMW`) —
  warm, grounded, a man not a boy.
- **Pacing is slowed** for every speaker (VOICE_SETTINGS: `speed` 0.86–0.92, higher
  stability) so no one rushes or blows through commas.
- **Jesus PAUSES like Jesus would** — `jesus_pauses()` in `mbm_eleven.py` inserts a longer
  reverent breath after each sentence and a gentle breath after each comma/colon (ElevenLabs
  `<break>` tags in ms; caption timing stays clean). This is applied automatically to every
  Jesus line — do not remove it.
- **Credits are plentiful** (growing_business tier, ~1.8M chars). Re-voice freely.

## Run it
```
bash admin/redo_loop.sh
```
The loop, for each build 1→200 (resumable — skips ones already in `REDO-PROGRESS.txt`):
1. deletes the old clips and re-voices from the canonical `TRANSCRIPTS/*.json` (new cast +
   pacing + Jesus pauses),
2. wipes `segs/` and re-renders the video,
3. gates it with `admin/qc_gate.py` (new voice + render-fresh + complete + no echo),
4. ships the passer via a small worktree commit on origin/main, and records it done.

Do a batch to sanity-check first if you want: `bash admin/redo_loop.sh 1 2 3` — WATCH/whisper
those three to confirm Alexander's Jesus sounds right and the pauses land, THEN let the full
run go. Verify against the ACTUAL shipped mp4 (ffprobe + faster-whisper), never a marker.

When Cameron gives a NEW critique, add it to `CRITIQUE-LAW.md` as a numbered law and it
applies to every remaining video automatically — that is the whole point of the loop.
