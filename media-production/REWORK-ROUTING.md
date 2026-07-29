# REWORK ROUTING — who does what on every flagged video (#1 Planner, 2026-07-23)

Cameron asked why the "needs reworked" videos aren't moving. Straight answer at the
bottom. This routes every currently-flagged video to the session that owns the fix, so
#1/#2/#3/#4 can each take their slice.

## ⛔ THE ONE THING BLOCKING ALL OF IT
**0 of 200 videos have new audio** (`ls build-*/.audio-eleven-done` = 0). #2 (ElevenLabs)
has never run because it needs the **ElevenLabs API key**, which has not been provided.
Every video that "still needs the audio" — including #1 — is waiting on this. Under the
REDO-ALL law every video must be re-voiced and re-approved, so until #2 can run, the
rework queue physically cannot drain. **Give #2 the key and the biggest bucket clears.**

A transcript fix by #1 (trim, dedup) or a still fix by #3 does NOT change the shipped
video until #2 re-voices and #4 reassembles the mp4. That is why finished-looking work
"didn't get put in there" yet.

## Bucket 1 — still OLD voice → #2 re-voice (23 flagged; really ALL 200)
5, 6, 9, 10, 13, 14, 15, 16, 18, 20, 23, 24, 25, 29, 30, 31, 36, 37, 39, 86, 89, 137, 140
— plus #1 and every other approved-on-old-voice row. Transcripts are ready in
`TRANSCRIPTS/`. **Owner: #2** (needs the API key). Then **#4** reassembles + resubmits.

## Bucket 2 — no finished mp4 → build + assemble (4)
- **#65, #67** — have narration; need voice (#2) + assemble (#4).
- **#71** Great Commission — transcript + 8 stills ready; **#4 assemble** (after #2 voices).
- **#128** Mark 7 — new transcript + stills ready (build-128-heart-far-from-me); #2 voice → #4 assemble.

## Bucket 3 — audio gaps from #1's echo sweep → NOW CLEANED, need re-voice + rebuild (5)
100, 134, 172, 176, 181. My echo trim DELETED a pure-restatement narrator segment in each
but left the old audio clip orphaned (QC read it as "segment has no audio clip"). **#1 has
removed the 24 orphan files** so the folders now match the trimmed transcript. **Owner:
#2 re-voice → #4 rebuild.**

## Bucket 4 — Cameron's open complaints (COMPLAINTS.md UNFIXED, 9), by owner
- **Pronunciation → #2 (ElevenLabs lexicon owns this now, no respellings):**
  #46 putteth, #51 tear→"tare", #63 Siloam, #73 Esaias, #127 leadeth. (Seeds already in
  `eleven_config.json` lexicon; #2 tunes by ear on the new voice.)
- **Pictures → #3:** #19 (boat: clothes/faces changing, AI-looking — redo the set),
  #56 (children's clothes + scale, giant Jesus in one).
- **Captions → #4:** #171 (scripture caption must be BLUE, not white).
- **Word sense → #2/#1:** #62 "Mark records" must read as the verb (past tense of record),
  not a name — #2 handles in voice; #1 can add a comma/rephrase in the transcript if needed.

## What #1 (me) has already done toward this
- Transcripts trimmed + echo-swept to 0, deduped, 200 exported to `TRANSCRIPTS/`.
- Created the two missing swap transcripts (#44 Pentecost, #128 Mark 7).
- Cleaned the 5 orphan-audio messes above.
- #1's remaining lane work: transcript-side pronunciation notes and the dup-candidate
  cluster — small next to the audio blocker.
