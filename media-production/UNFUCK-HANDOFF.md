# HANDOFF — Fix the MBM videos (paste this into a fresh session)

You are taking over the **Milk Before Meat** project: 200 short vertical Bible-story
videos for spreading the restored gospel of Jesus Christ (Latter-day Saint perspective),
reviewed by Cameron on a private board. A previous AI session (me) got the new ElevenLabs
voice onto all 200 but left real defects. Your job is to **fix them properly** — verify
every fix against the ACTUAL shipped mp4, never a proxy. Cameron sets the vision ("do what
is good for spreading the LDS gospel of the true, good Jesus Christ") and trusts you to
execute. **Do not ask him permission to start or offload decisions onto him — decide and do.**

Repo: `~/Desktop/MBM` (public GitHub `noremacttevol/MBM`). Read `MBM/CLAUDE.md`,
`MBM/AGENT-RULES.md`, and `media-production/FRESH-CHAT-KICKOFF-2026-07-23.md` first.

## Credits — NO LONGER A CONSTRAINT
Cameron upgraded to the **$300 growing_business tier: ~1.8 million characters available.**
Re-voice, fix pronunciation, and restore full-length narration freely. The live API key is
in `media-production/elevenlabs API KEY.txt` (gitignored — NEVER commit it; leaked keys get
auto-revoked). Prefer `recover_from_history.py` (free re-download) before re-voicing text
that already exists in history; re-voice freely when the text is new or corrected.

## THE DEFECTS TO FIX (from the live complaint board + Cameron)
Pull the CURRENT complaints first: `node admin/sync-reviews.mjs` then read
`media-production/COMPLAINTS.md` (it syncs from Firestore — the local copy goes stale, so
re-sync before trusting it). A complaint only clears when **Cameron taps Approve** — fixing
it does NOT remove it, so tell him plainly which are fixed and ready to approve.

1. **Shortened videos** — some narrations were over-trimmed. Example: #10 (woman at the
   well) was a ~5-minute story, now ~68s. The full text lives in `TRANSCRIPTS/*.json`
   (`{row, segments:[{id,speaker,text}]}`) — the planner's source of truth. Restore the
   fuller narration, re-voice, rebuild. Do NOT trim a story down to a stub.
2. **Jesus talks too fast / weird pacing** — `mbm_eleven.py` uses MODEL
   `eleven_multilingual_v2` with `VOICE_SETTINGS` per speaker (stability/similarity/style).
   Slow Jesus (and any rushed voice): raise stability, add a `"speed": 0.9`-ish value to
   his `voice_settings` if the model honors it, and/or insert natural sentence breaks.
   Re-voice a sample and LISTEN (whisper + your own check) before mass-applying.
3. **Weird / wrong pronunciations of archaic words** — calleth, lieth, findeth, liveth,
   maketh, overcometh, abideth, divideth, putteth ("put-uth"), Esaias, Elias (should be
   "ee-LY-us", spelled *Elias* not *Elijah*), Siloam ("si-LOH-uhm"), and homographs
   tear/lead/wound/row/bow/live. Fix in `mbm_eleven.py`'s pronunciation layer:
   `eleven_spoken_text()` applies `PHRASES` (orthographic) + per-build `SPOKEN` overrides,
   OR wire an ElevenLabs **pronunciation dictionary** (the code comments say this is the
   intended path — "one measured lexicon" instead of the old respelling war). Test with
   `check_pronunciation.py`, and **verify by transcribing the FINAL mp4 with whisper**, not
   by ear-guessing. Homographs (tear/lead/row/bow) can't be verified by transcription —
   listen or use the per-build SPOKEN override and spot-check.
4. **Old voice still on some videos** — a gate regression (a check was removed) let ~45
   videos ship with the OLD voice baked into the mp4 even though new clips existed. They
   are being rebuilt now; when you start, RE-VERIFY: `python3 admin/qc_sweep.py` then check
   every build passes `admin/qc_gate.py` (which now enforces new-voice + render-fresh).
5. **Wrong / weird things said** — verify each narration is scripturally accurate and
   "milk-level" (Christ-centered, simple, uplifting, no heavy doctrine). Fix the transcript,
   re-voice, rebuild.

## PICTURES — the OTHER computer is handling these (coordinate, don't collide)
A second machine (Windows + Flow) is steadily regenerating the messed-up stills using the
locked character-reference sheets in `media-production/CHARACTERS/` (aaron, abraham, andrew,
peter, john, mary-magdalene, God, etc.). **Every still must condition on that character's
ref sheet so faces/clothes/size stay consistent across all videos** — that is the rule that
kept getting missed. Your lane is VOICE/SCRIPT/CAPTIONS/TIMING; only touch a picture if the
other machine isn't covering it, and if so use `gen_shots.py --dir <build> --shots <slug>
[--jesus <slug>] --force` (Flow is $0; `flow_driver.py check` = logged_in). Always Read the
regenerated jpeg to QC it before rebuilding.

## THE PIPELINE / TOOLS
- **Re-voice:** `python3 voice_from_transcripts.py TRANSCRIPTS` (real ElevenLabs via
  `mbm_eleven.render_segment`; writes 44100 Hz clips + `<id>.timing.json`). Cast:
  narrator=Brian, Jesus=Chris, God=Bill, scripture=Roger, woman=Matilda.
- **Rebuild a video from its clips:** `rm -rf <build>/segs && (cd <build> && python3 build.py)`.
  Batch: `bash admin/rebuild_survivors.sh <nums…>` (wipes segs, renders 4-parallel, gates,
  bulk-ships via a worktree on origin/main, redeploys the board).
- **QC GATE (never bypass):** `python3 admin/qc_gate.py <build>` — passes only if the FINAL
  mp4 is: new voice (every referenced clip 44100 Hz), render-fresh (mp4 length explained by
  clips+card+gaps, so it was actually rebuilt from the new audio), complete, no script echo.
  **Do NOT remove checks to "simplify" — that is exactly the regression that shipped old
  voice.** `qc_sweep.py [--deep]` writes `QC-STATUS.json`, which the board reads.
- **Board:** `python3 media-production/gen_site_index.py` regenerates `site/review.html`
  (shows only gate-passers); firebase deploy publishes it (429 → `prune_hosting_versions.py`
  then redeploy). Ship via a worktree built on `origin/main` (the repo is huge; big pushes
  500). Watch for stale DUPLICATE build dirs (`build-NN-oldslug` vs `build-NN-newslug`) —
  they cause false gate results; quarantine the stale one to `media-production/_stale-dupes/`
  (confirm canonical via `QUEUE.md`).

## VERIFICATION LAW (why the last session failed Cameron)
Trust ONLY the actual shipped mp4: `ffprobe` the audio, transcribe with faster-whisper,
measure duration. NEVER claim "fixed/done" from a marker, a git timestamp, a sample rate on
the folder clips, or "the text matches." Every one of those lied. When you fix something,
rebuild the mp4, gate it, watch/transcribe it, THEN tell Cameron it's ready to approve.

## MISTAKES THE LAST SESSION MADE — do not repeat
- Removed a gate check to "keep it simple" → 45 old-voice videos shipped as done.
- Reported "pronunciation all fixed" when the board still showed many broken.
- Over-trimmed scripts, shortening real stories to stubs.
- Verified clips instead of the final mp4; trusted timestamps and markers.
- Left stale duplicate build folders that produced false pass/fail.

Work through the complaint board top to bottom, fix each defect at the source, rebuild,
gate, verify the real mp4, and keep the board honest. Credits are plentiful now — do it
right, not cheap.
