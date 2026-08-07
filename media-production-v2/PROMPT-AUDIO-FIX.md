# AUDIO-FIX SESSION — close Cameron's audio complaints on NEEDS-AUDIO rows

Created 2026-08-06 after Cameron: "i dont know why it hasent already fixed the
ones i turned down and complained about." 28+ rows are parked NEEDS-AUDIO
because their open complaints are AUDIO defects (mispronunciations, wrong
voice, stale/mismatched V1 renders) that the picture runner is forbidden to
touch. THIS job fixes them. It spends $0 on Gemini — ElevenLabs (only for
re-voiced segments) + ffmpeg only.

## Hard rails

- NEVER generate images. No v2_gen_api, no v2_story_cast. The row's stills are
  either already generated (ship them) or not needed yet (the picture runner
  builds them after your audio fix flips the row's Audio to OK).
- Touch ONLY the audio chain: `make_narration.py` (respell/SPOKEN dicts),
  narration segment mp3s, the V1 final render, `v2_assemble.py` runs, captions
  if the park note says so. Never scene text, locks, or beat structure.
- **KNOW WHICH TTS ENGINE ACTUALLY SHIPS BEFORE YOU RE-VOICE (2026-08-07, row 18).**
  Many builds migrated to ElevenLabs (2026-07-23) but still carry the OLD
  edge-tts `make_narration.py` scaffold — so a park note that says "set SPOKEN
  and run `make_narration.py`" will re-voice the segment in the WRONG engine
  (edge-tts AndrewNeural, 24 kHz) and swap the voice mid-video. **ffprobe the
  segment first:** `44100 Hz / 128 k = ElevenLabs` (VOICE_ELEVEN — narrator
  "Brian"), `24000 Hz / 48 k = edge-tts`. Re-voice through the SAME engine the
  rest of the row uses. For ElevenLabs, render ONE segment with
  `mbm_eleven.render_segment(spoken, speaker, out, key=...)` (the shared key
  file now holds an extra cloudflare token — grep out just the `sk_...`), then
  **pitch-preserving atempo-match the new take back to the original segment
  duration** so NO downstream still-window in `beats_v2.py` has to move. The
  possessive "'s" can't be expressed in a SPOKEN key (the override regex splits
  on the apostrophe); respell "Jesus's" → "Jesuses" directly in the spoken
  string — the caption comes from SEGMENTS s[2] and stays "Jesus's".
- Shared-file discipline (PARALLEL-LANES LAW in PROMPT-OPUS-RUNNER.md):
  pull-rebase immediately before editing QUEUE/AUTHOR-BOARD/review.html/
  SESSION-LOG, push immediately after. NEVER git clean / reset --hard / delete
  files you did not create.
- HEADLESS: run everything foreground to completion; never background, never
  wait for notifications. **This includes encodes: run ffmpeg/v2_assemble as a
  plain foreground command and let it block until it exits — a session that
  ends its turn "waiting for the encode" is DEAD and strands the row
  (2026-08-07, row 18: the encode finished as the session died; only the
  unclaimed board row let the next lane rescue it). Ship (deploy + verify)
  in the SAME turn the encode finishes.**

## The loop, per row (lowest NEEDS-AUDIO row first)

1. `git pull --rebase --autostash origin main`. Open AUTHOR-BOARD.md, pick the
   lowest **NEEDS-AUDIO** row whose Claim does not contain `AUDIO-FIX`.
   Claim-by-push: append `AUDIO-FIX <date> LIVE` to that row's Claim cell,
   commit, push (rejected push = taken, next row).
2. **Read the row's per-row authority, in order:** the build's `QC.md`
   "RUNNER PARK" note (it names the exact defect and the exact fix), then
   `python3 media-production-v2/v2_outline.py <row>` (the open complaints in
   Cameron's words), then `media-production/COMPLAINT-FIX-PLAN.md` (the
   pronunciation doctrine: SPREAD_TO_ALL_VOICES, the words Cameron gave exact
   phonetics for, A/B rules).
3. **Fix by class:**
   - **STALE-V1 / duration-mismatch** (park says "re-render V1 mp4" or "set
     AUDIO_FROM_V1_SEGMENTS=True"): do exactly what the park note says — these
     need NO new TTS and cost $0. Re-render, then `v2_assemble.py <row>` must
     pass its audio gate.
   - **PRON / VOICE re-voice** (park quotes a mispronunciation complaint): add
     the respelling to the dict per COMPLAINT-FIX-PLAN (spread to every voice
     without a measured entry — the SAY_BY_VOICE single-voice bug is the root
     cause of Cameron's repeats). Regenerate ONLY the affected segment(s) via
     ElevenLabs with the SAME locked voice, re-render the final audio, then
     re-assemble. **Verify the fix**: transcribe or ear-check the regenerated
     segment and note the timestamp + what it now says in QC.md. Never
     regenerate segments that carry no complaint.
4. **The audio hash will change — that is the POINT.** The V2 audio-immutability
   law protects against ACCIDENTAL audio drift; a Cameron-ordered re-voice is
   the sanctioned exception. Document the new audio baseline in QC.md
   (old hash → new hash, which segments changed and why, quoting his
   complaint). Never silently change anything else: same voices, same wording,
   same timing outside the fixed segments.
5. **Ship exactly like the runner** (PROMPT-OPUS-RUNNER.md step 7): commit the
   mp4, update the row's review card — the "🛠" flag MUST answer the complaint
   in Cameron's own words ("Your complaint 'Cana → Kane-a' — Cana now says
   KAY-nuh at 0:41; nothing else in the audio changed") — then
   `firebase deploy --only hosting` and VERIFY on the live URL (a push is not
   a delivery). If the row has no V2 stills yet, ship nothing visual: flip the
   board row to **AUTHORED / Audio OK / Ready ✅** with claim cleared so the
   picture runner builds it on the fixed audio, and note the fix in QC.md.
   If stills exist (rows parked mid-build), re-assemble and ship the full cut.
6. Board: NEEDS-AUDIO → BUILT (if shipped) or AUTHORED+Ready (if handed to the
   picture runner). SESSION-LOG entry (which complaints closed, $ spent,
   segments re-voiced), commit, push. Next row.

## Money truth

Gemini: $0 — always. ElevenLabs: only the complained-about segments are
regenerated (typically 1–3 short segments per row). Log every re-voiced
segment in QC.md. If ElevenLabs itself refuses (credits/quota), write the
blocker + resume into QC.md, mark the claim `AUDIO-FIX BLOCKED`, push, move
to the next row — never park silently.
