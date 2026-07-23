# AUTO-FIX LOOP — kickoff for the OTHER computer (Claude Code desktop)

**Paste this whole file's intent to the desktop machine that is logged into Flow.**
Goal: fix the videos Cameron complains about **without a human pasting prompts**.
Cameron only does the FINAL yes on the board. Nobody hand-drives Flow.

The tools to do this ALREADY EXIST in `media-production/`. Do NOT rebuild them.
Your job is to CHAIN them into one loop and run it.

## The pieces (all already here)
- `admin/sync-reviews.mjs` → pulls Cameron's live complaints into `COMPLAINTS.md`.
- `flow_driver.py gen --prompt "…" --out assets/sX-slug.jpeg --ref a.jpeg b.jpeg`
  → makes ONE Flow still from the command line, no extension. This is why no human
  has to paste prompts.
  **CREDIT LAW (do not restate the old "0 credits/free" myth):** Cameron's Flow
  credits are PREPAID and EXPIRE MONTHLY. Do NOT hoard them and do NOT default to
  the cheapest model to "save money" — spend them on the model that gets it right.
  Use **Nano Banana Pro** for anything that needs to hold (faces, Jesus, crowds,
  fewer rerolls); ordinary stills can use Nano Banana 2. The ONLY thing banned is
  the paid Gemini API. Never call Flow generations "0 credits," "$0," or "free."
- `CHARACTERS/character_refs.py` → `refs('peter')` gives the 3 ref jpegs,
  `lock_text('peter')` gives the exact paragraph to put in the shot.
- `character_ref_gate.py` / `jesus_face_gate.py` → run BEFORE generating; must
  exit 0 (prompt-sheet check, NOT a video check — see WHAT THE GATES MEAN).
- each `build-NN/build.py` → assembles the mp4 from stills + narration.
- `check_pronunciation.py --build build-NN` → render+transcribe audit for words.
- `admin/verify-mp4.sh <mp4>` → truncated-file gate.
- `admin/ship-fixes.sh` → approved-lock check + commit + push + board refresh.

## The loop (run this repeatedly)
For each OPEN complaint in `COMPLAINTS.md` (skip any number `dump-approvals.mjs`
marks approved — NEVER ship over an approved cut):

1. **Classify the defect** from Cameron's text + the build:
   - **pronunciation** ("mispronounced X", "X is pronounced …") → deterministic.
   - **timing / dead air** ("extra seconds at the end") → deterministic.
   - **caption color / red-letter / blue scripture** → deterministic.
   - **still / character** ("looks bad", "redo the picture", "characters change",
     "Jesus is a giant", "wrong number of people") → needs a new picture.
   - **story / doctrine** ("duplicate story", "show the Father AND the Son") →
     STOP, leave for Cameron. Do not guess doctrine.

2. **Deterministic fixes** (do them yourself, no Flow):
   - pronunciation: edit that build's `make_narration.py` `SPOKEN` dict. A/B every
     candidate through `check_pronunciation.py` (render both, keep the one that
     transcribes back clean). One continuous lowercase word, NO hyphens/CAPS.
   - timing: `build.py` derives the tail from the last spoken word — rebuild fixes
     stray end seconds; never hand-set.
   - caption color: the color comes from the segment's SPEAKER in `make_narration`
     (narrator=white, jesus=red, scripture=light-blue, god=green, woman=pink).
     Rebuild picks it up.

3. **Still fixes** (auto-drive Flow — no human):
   - open the build's `PROMPTS.md`, find the shot named in the complaint.
   - wire it for real: for every rostered character in the shot, put
     `lock_text(name)` into the shot text and collect `refs(name)` jpegs.
     For Jesus: the byte-identical JESUS LOCK v3 block + `REF: jesus-master-ref`.
   - `python3 character_ref_gate.py --dir build-NN` and `jesus_face_gate.py` must
     exit 0. (Passing by pasting a bare "NAME LOCK" string is CHEATING and is
     banned — the real lock paragraph + the ref jpegs must be there.)
   - generate: `flow_driver.py gen --prompt "<style block + wired shot>"
     --out assets/sX-slug.jpeg --ref <each ref jpeg>`. STALE-PART TRAP: also
     delete `segs/<seg>*` so the rebuild can't reuse the old picture.
   - **Hermes checks the NEW jpeg** (face hidden if Jesus; characters match the
     sheet; right count of people; not a giant; reverent painted style). If Hermes
     says bad → regenerate. Only a Hermes-passed jpeg moves on.

4. **Rebuild + verify:** `python3 build.py`; `verify-mp4.sh` on the output;
   for pronunciation, transcribe the final mp4 window to confirm the word.

5. **Ship:** drop a one-line `build-NN/FIXNOTE.txt` in plain English, then let
   `admin/ship-fixes.sh` push it to the board. It refuses approved cuts and
   truncated files by itself.

6. Cameron reviews on the board and approves. His approval is the ONLY thing that
   clears a complaint.

## WHAT THE GATES MEAN (do not repeat Hermes's mistake)
Both gates read the PROMPT SHEET, not the finished video. Gate-red does NOT mean a
shipped video is broken; gate-green does NOT mean it's fixed. Use them ONLY as the
pre-flight check right before generating a still. Judge finished videos by looking
at frames and listening to audio — that is Hermes's job, below.

## What stays human
- Cameron's final approval on every cut (by design).
- Doctrine/story calls (#140 duplicate story, #179 Father+Son vision, etc.).
- Which respelling "sounds right" when the A/B is close — flag it, don't guess.
