# SWEEP ALL 200 — the machine's marching order (Cameron, 2026-07-23)

**Goal:** bring every finished video up to today's locked laws WITHOUT Cameron
hunting defects by hand. He only approves the results. You do the finding and the
fixing. Hermes verifies. Run this on the machine logged into Flow.

First: `git pull --rebase --autostash origin main`. Read AUTO-LOOP-KICKOFF.md for
the per-fix mechanics; this file is the full-library plan that feeds it.

---

## THE HARD RULES (each exists because it already bit us)
1. **Never ship over an APPROVED cut.** `node admin/dump-approvals.mjs` → skip any
   number with `approved`. Approved-lock outranks everything.
2. **Verify in the FINAL mp4, never the cache.** Transcribe the shipped mp4's audio
   / grab its frames. A report row or a fresh re-render is NOT proof.
3. **Real defect vs whisper noise.** `sweep_final_audio.py` flags ~150 rows that are
   whisper mis-hearing itself (Trap 1: hath→has, alignment drift, homophones). Only
   act on the archaic-word and character rows you can HEAR/SEE. When unsure, leave
   the true word alone.
4. **Never add a respelling you haven't A/B tested** through `check_pronunciation.py`
   (render both, keep the one that transcribes back clean; one lowercase word, no
   hyphens/CAPS).
5. **Resync shared modules before every rebuild.** Builds carry their OWN copy of
   `mbm_pronounce.py` / `mbm_caption_timing.py` / `mbm_speakers.py`; a stale copy is
   why build-124 still says "mocketh" though the central fix exists. Run
   `bash admin/sync-shared-libs.sh` (or copy the central modules in) so the build
   renders with the current laws.
6. **Stale-part trap:** when a still changes, delete `segs/<seg>*` too, or the old
   picture gets re-muxed.

---

## PASS 1 — PRONUNCIATION (deterministic, do it yourself, no Flow)
1. `python3 sweep_final_audio.py` → SWEEP/FINAL-AUDIO-AUDIT.md (worst-first).
2. Work the REAL archaic-word suspects (maketh, liveth, cumbereth, calleth,
   findeth, abideth, putteth, Siloam, Elias…). For each build:
   - resync modules (rule 5), confirm the fix is in the central dict OR add a
     tested SPOKEN entry (rule 4).
   - `python3 make_narration.py && python3 build.py`.
   - transcribe the fixed line from the FINAL mp4 (rule 2).
   - `admin/verify-mp4.sh`, drop `FIXNOTE.txt`, ship (Pass 4).

## PASS 2 — CHARACTERS & FACES (pictures → Flow via flow_driver, no human clicks)
For each build: `character_ref_gate.py --dir` + `jesus_face_gate.py --dir`.
Where a rostered character appears, wire the real `lock_text()` + attach `refs()`
jpegs into the shot, gates exit 0, then
`flow_driver.py gen --prompt "<style+shot>" --out assets/sX.jpeg --ref <refs>`.
Nano Banana **Pro** for faces/Jesus/crowds (credits are prepaid & expire — spend
them). **Hermes checks each new jpeg** (face hidden if Jesus, characters on-model,
right count of people, not a giant, painted style). Only a Hermes-passed jpeg gets
built in. Delete stale segs, rebuild.

## PASS 3 — CAPTIONS / TIMING (deterministic)
Scripture blue / Jesus red / narrator white comes from the segment SPEAKER — a
rebuild with current modules fixes old white-scripture cuts. Dead air at the end is
derived from the last spoken word — a rebuild trims it. No hand-setting.

## PASS 4 — SHIP
`bash admin/ship-fixes.sh` — it re-checks approved-lock + verify-mp4, commits one
small cut at a time, writes the plain-English FIXNOTE to the board, refreshes it.
Cameron reviews and approves. His yes is the ONLY thing that clears a complaint.

---

## WHAT STAYS WITH CAMERON (flag, don't guess)
- Doctrine / story calls (duplicate story, which vision to show, a name choice).
- A respelling or a picture that's genuinely close — flag it, he decides.
- Anything you can't verify — say so, don't ship it as "fixed."

## PROGRESS (resumable)
Keep a checklist in SWEEP/SWEEP-STATUS.md: build number, pass done, shipped y/n,
flagged-for-Cameron y/n. Log anything you deliberately skipped — a silent skip
reads as "covered" when it wasn't. Work worst-first; don't stop at the first pass
being "mostly done" — the tail is where the misses hide.
