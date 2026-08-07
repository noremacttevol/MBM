# QC — build-22-unmerciful-servant (row 22)

## ✅ RESOLVED — AUDIO-FIX 2026-08-07 (Machine A `Dev`): "shouldest" → "should-est" SHIPPED

**Cameron's complaint (now CLOSED):** "2:46 Jesus mispronounces shouldest it should
be should-est."

**Fix (audio-only, $0 — edge-tts, no Gemini):**
- Added `SPOKEN.update({"shouldest": "should-est"})` to BOTH the authoritative V1
  `make_narration.py` (`media-production/build-22-unmerciful-servant/`) and the V2
  copy. Regenerated **only** `audio/j5.mp3` (targeted regen, not a full re-run) in
  the V1 dir — the other 24 segment mp3s are byte-identical (verified by hash diff).
- A/B in the JESUS/Eric voice, in-context (plain vs `should-est` vs `should est`):
  plain rendered the mashed word Cameron rejected; `should-est` broke cleanly into
  "should" + "est" (faster-whisper heard "should" + a separate est), no unnatural
  gap (raw 12.617s→13.512s), mirroring the measured `shewest`→`show-est` -est-family
  winner + COMPLAINT-FIX-PLAN row 22. Caption keeps KJV "Shouldest".
- **Audio baseline changed (sanctioned re-voice):** j5 SHA256
  `085d2c08…` → `4a6da5a2…`. Rebuilt narration track (AUDIO_FROM_V1_SEGMENTS=True)
  hash `20a6ef72…`, 225.174s.
- **Timeline coupling:** extract_beats measures spoken (trimmed) duration, so the
  real shift after j5 is only **+0.17s** (card 216.10→216.275, total 225.003→225.174),
  NOT the raw +0.895s. Remapped the still-windows in `beats_v2.py` (s38→s48) through a
  piecewise-linear old→new segment-start map so every picture stays phrase-synced.
- **AUDIO_FROM_V1_SEGMENTS = True** added to `beats_v2.py` so assembly rebuilds the
  track from the (fixed) V1 mp3s instead of muxing the stale V1 final MP4.

**Verified in the RENDERED V2 mp4** (`matthew-18_unmerciful-servant.mp4`, sha1
`6e6943d8c0dc`, 225.2s, decodes 0 errors): j5 region transcribes the full KJV line
with the re-voiced "should-est"; frame at 2:46 shows the realistic wicked-servant
scene with the red KJV caption in sync. Realistic V2 pictures (48) UNCHANGED — no
Gemini spend, 0 rerolls.

**Shipped:** reviewer card (`site/review.html` v22) updated with a 🛠 flag answering
the complaint in Cameron's words + new cache-buster `?v=6e6943d8c0dc`; committed +
pushed to main (GitHub raw serves the video); `firebase deploy --only hosting` +
live-verified. Board row 22 NEEDS-AUDIO → BUILT, Audio CHECK → OK.

---

## §0 RUNNER PARK — C-FIX 2026-08-07 → NEEDS-AUDIO (audio-pronunciation, out of runner scope) [CLOSED — see RESOLVED above]

**Cameron's OPEN complaint on the shipped cut:**
> "2:46 Jesus mispronounces shouldest it should be should-est"

**Domain: AUDIO (pronunciation).** The word is in spoken segment **j5** (the king's
rebuke, KJV Matthew 18:32-33): *"O thou wicked servant, I forgave thee all that debt,
because thou desiredst me: **Shouldest** not thou also have had compassion on thy
fellowservant, even as I had pity on thee?"* — window **159.95–172.53 s**; "Shouldest"
lands at ~2:46. Beat `v2-r022-b39` / `s39-shouldest-not-thou-also.jpeg`.

**Why this is a PARK, not a ship:**
- The complaint is a mispronunciation of a spoken word. The only fix is a **re-voice**
  (add a SPOKEN respelling for "shouldest" + regenerate `j5.mp3` + re-assemble). The
  picture-runner is FORBIDDEN to re-voice (audio-immutability; AUDIO LOCK is its only
  proof of a clean cut). RUNNER-LESSONS: audio-pronunciation complaints are OUT of
  runner scope — park NEEDS-AUDIO, do not touch pictures.
- **Not the "already baked in → ship" exception (RUNNER-LESSONS row 57).** Checked
  `make_narration.py`: `SPOKEN = {"owest": "owesst"}` only — there is **NO override for
  "shouldest"**, so the mispronunciation is live in the current mp4
  (`matthew-18_unmerciful-servant.mp4`, j5.mp3 dated Jul 28). The fix is not yet
  rendered → park, don't ship.
- **No picture defect** is in the complaint, so nothing to reroll and nothing to batch
  (touch-once). $0 spent — no pictures touched.

**AUTHOR RESUME (audio lane):**
1. In `build-22-unmerciful-servant/make_narration.py`, add a per-segment override:
   `SPOKEN.update({"shouldest": "should-est"})` — mirror the measured `-est` winners
   already in `mbm_pronounce.py` (`"shewest": "show-est"`, `"sheweth": "show-eth"`), but
   A/B-test in the JESUS voice first (PRONUNCIATION-LAW Trap 2: hyphen forms can read as
   two words; pick the spelling that round-trips "should-est" clean). Caption keeps KJV
   "Shouldest".
2. `python3 make_narration.py` to regenerate `audio/j5.mp3` (only j5 changed).
3. `python3 media-production-v2/v2_assemble.py 22` — AUDIO LOCK will change (expected;
   the audio legitimately changed). Verify the new j5 says "should-est".
4. Ship the re-cut through the normal C-FIX flow (deploy + live-verify + review-card
   flag answering the complaint in Cameron's words). This re-cut voids the prior
   approval and re-queues the row — that is correct for an audio re-voice.

## COMPLAINT LEDGER
- **OPEN — [2:46 "shouldest" mispronunciation]** → AUDIO-domain re-voice; PARKED
  NEEDS-AUDIO for the author lane (see §0). NOT fixed in this session — runner cannot
  re-voice. No other open complaints on this row.

**Reviewer:** still shows the existing shipped cut (unchanged — a park does not ship,
no deploy). Board row 22 flipped BUILT→NEEDS-AUDIO, Audio OK→CHECK.
