# QC — build-22-unmerciful-servant (row 22)

## §0 RUNNER PARK — C-FIX 2026-08-07 → NEEDS-AUDIO (audio-pronunciation, out of runner scope)

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
