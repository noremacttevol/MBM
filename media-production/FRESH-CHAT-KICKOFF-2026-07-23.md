# FRESH-CHAT KICKOFF — 2026-07-23 (paste-and-go for a new low-context session)

Cameron wants a NEW chat to carry the work with fresh context but full understanding of
what's already going. This file is that understanding. Read it, then read the three law
files it points to, claim a lane, and go. Nothing here needs re-deciding.

---

## THE QC GATE LAW (Cameron, 2026-07-24) — NON-NEGOTIABLE, top priority

Cameron's hardest rule: **he must NEVER be shown a video that is told "good" but is
actually bad.** He wasted hours reviewing cuts that still had the OLD voice or still
had the narrator echoing the scripture, because the board decided "ready" from a git
TIMESTAMP (any touch flipped it green). That is banned forever.

- **The gate is `admin/qc_gate.py <build-dir>`.** It reads the ACTUAL video, never a
  date/marker/another session's word. A build passes ONLY if ALL hold: (1) plays start
  to finish (moov + full audio), (2) real NEW voice — every spoken clip it uses is
  44100 Hz ElevenLabs, never the 24000 Hz old edge-tts, (3) every segment has its audio
  clip, (4) transcript has zero narrator-repeats-scripture echoes, (5) faster-whisper
  hears no spoken echo in the finished audio.
- **Nothing ships without it.** It is wired into `admin/ship-fixes.sh` AND
  `media-production/caption-and-ship.sh` right after verify-mp4. A blocked build is
  logged with the reason and NOT posted. Do not remove or bypass these calls.
- **The board obeys it.** `gen_site_index.py` reads `media-production/QC-STATUS.json`
  (written by `admin/qc_sweep.py`) and shows a video ONLY if it passed. Held-back
  videos are counted on the page so Cameron sees the truth. Never revert the board to
  the old `new_voice_set()` timestamp logic.
- **After changing any video's audio/render, refresh its status:**
  `python3 admin/qc_sweep.py <num>` (or a full `python3 admin/qc_sweep.py` sweep), then
  regenerate + deploy the board. A build re-enters the board automatically once it
  passes — no manual re-adding.
- **Current state (2026-07-24 sweep): 168 PASS, 32 BLOCKED** (23 still old voice, 5
  missing audio clips, 4 unplayable). The 32 blocked numbers are the real re-voice
  worklist — get them to pass the gate, don't hand-wave them onto the board.

---

## THE UNIFY ORDER (Cameron, 2026-07-23) — obey exactly

- **One source of truth for STORIES:** `AUDITS/2026-07-20-repeat-audit.md` (authoritative
  dedup — already finished, 6 repeats fixed) + `STORY-INTEGRITY-LAW.md` (rules going
  forward). `STORY-LEDGER.md` is SUBORDINATE; its "only 1 dup" and "merge #44" calls are
  RETRACTED — ignore them.
- **Do NOT re-run the dedup. It is finished. The 200 is full and clean.** No more
  story-hunting.
- **Pronunciation respellings are DEAD.** ElevenLabs owns pronunciation now (better voice
  + a lexicon for the old-English words). Do not add or fix respellings; do not run
  `check_pronunciation` A/Bs. `mbm_pronounce.py` tinkering is over.
- **Nothing Cameron approved gets rebuilt without his word.**
- **Split by CLAIM (existing queue law):** before touching ANY video, claim its row in
  `QUEUE.md` (write your machine + date in the Claim column), commit, and **push the claim
  FIRST**. If the push is rejected, another session took it — pull and take the next row.
  Never touch a row another session has claimed. Push every decision to origin/main
  immediately so all four machines agree.

## The real work now (in priority order)

1. **Transcript trim → ElevenLabs re-voice + full re-approval of all 200 (the fast
   priority).** Every video is being re-voiced with ElevenLabs and re-approved. Before
   re-voicing, TRIM each narration per `STORY-INTEGRITY-LAW.md` Rule 4: drop the old habit
   of saying a scripture line in old English and then repeating it in modern English —
   only restate when the old English is genuinely hard to follow. Tighter, cleaner scripts
   → hand to ElevenLabs. (Set up the ElevenLabs path; edge-tts is being retired.)
2. **Pictures / Flow from ALL complaints (parallel lane).** Keep working `COMPLAINTS.md`
   picture defects through Flow. Pattern that works: contact-sheet the build's stills →
   spot the defect → fix the prompt (scale guard, only-Jesus-cream, dark robes for
   scribes, grounded perspective) → `gen_shots.py` / `flow_driver.py gen` → Read the jpeg
   to QC → clear `segs/` cache → rebuild → verify-mp4 → ship. Flow is LIVE on Machine C
   (`flow_driver.py check` = logged_in).
3. **Character auto-finder (after/with the above).** Build a pass that checks EVERY video's
   characters against the new cast rules (`CAST-REF/CAST-BIBLE.md`: the Twelve + recurring
   cast locked to one face each; only-Jesus-cream; God embodied & consistent) across the
   whole project, and flags drift for regeneration.
4. **New approved stories.** `Pentecost — Acts 2` is APPROVED (Cameron 2026-07-23) as the
   next NEW story; then the bench in `STORY-INTEGRITY-LAW.md` (Damascus road, the Ethiopian,
   Daniel's lions' den). NOTE: the 200 is full — Pentecost needs a slot; that is Cameron's
   pick (do not cut an approved story unasked). Natural moment = the first row that fails
   the ElevenLabs re-review.

**Suggested lane split (claims are the real guard):** one session owns the re-voice sweep
(lowest open rows upward); another owns pictures/Flow from complaints; new-stories can ride
with either once a slot is confirmed. Claim before touching.

## What the 2026-07-23 Machine C session already did (so it isn't redone)

- **Fixed a silent blocker:** this box's git was an ORPHAN lineage (no common ancestor with
  origin) — it literally could not push. Reconciled non-destructively; it is a normal peer
  now and ships fine. (If a Machine C pull ever "hangs," it's the large media history —
  commits are durable locally; see SESSION-LOG.)
- **Shipped word/text fixes:** #109 findeth, #50 Cana, #52 "six words" (these are now moot
  under ElevenLabs but the cuts are correct).
- **Shipped picture fixes:** #13 (pharisees out of cream → dark robes), #112 (giant Jesus),
  #157 (giant scribe), #153 (cleaner), #181 (regenerated grounded in Job per Cameron).
- **Verified already-good (awaiting Cameron's APPROVAL only, do NOT rebuild):** #46 #57 #62
  #67 #83 #86 #90 #108 #146 #150 #171 #184 #188 (words/captions) and #56 #107 #19 #113 #135
  (pictures). Big lever for Cameron: APPROVE these on the board and the complaints clear.
- **Left for Cameron (doctrine):** #140 already Naaman; #179 already the two-personage vision.
- **Authored + pushed** `STORY-INTEGRITY-LAW.md` and reconciled it with the Jul-20 audit.

## Law files to read before working
`STORY-INTEGRITY-LAW.md` · `AUDITS/2026-07-20-repeat-audit.md` · `PRODUCTION-BIBLE.md` ·
`CAST-REF/CAST-BIBLE.md` · `STORY-COVERAGE-LAW.md` · `CLAIM-LAW.md` · `QUEUE.md`.
