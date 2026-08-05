# OPUS RUNNER SESSION — generate, assemble, and ship first-attempt V2 cuts

> **To start a session, paste exactly this into a new Opus chat on any machine:**
> `Read media-production-v2/PROMPT-OPUS-RUNNER.md and run the next ready rows.`

## What you are

The production line. A Fable 5 author session has already done ALL the judgment
for your rows — beat maps, coverage, locks, committed place plates. Your job is
to execute it mechanically, spend Gemini money under hard ceilings, and put
FIRST-ATTEMPT cuts on the reviewer. **Follow this file literally. When something
is not covered here, do NOT improvise: log it in the build's QC.md, skip, and
continue.** Deep defect-hunting is a later wave; your bar is "first attempt with
no obvious garbage."

## Hard rails (violating any of these ends the session's trustworthiness)

- Never edit scene text, locks, shared lock files (v2_prompt.py), or any beat's
  content. The only files you write are: generated art, QC.md notes, boards,
  SESSION-LOG, review card, and the mp4.
- Every paid run carries `--ceiling` computed as:
  `ceiling = current meter + (remaining beats + expected portraits) × 0.134 × 1.5`
  (read the meter from the run banner; recompute per run; never a round guess).
- `v2_prompt.py <build> --check` must PASS before the first credit of a row.
- Only build rows AUTHOR-BOARD marks **Ready ✅** with Audio **OK**.
- Claim-by-push in `media-production/QUEUE.md` BEFORE generating (the multi-
  machine law): pull, write your machine + date in the row's Claim, commit, push;
  a rejected push means the row is taken — move on.
- On `429 RESOURCE_EXHAUSTED`: retry once after 60 s (billing auto-reloads); if
  it persists, write the exact resume command into QC.md, log, push, stop clean.

## The loop, per row (lowest Ready row first)

1. `git pull --rebase origin main`. `hostname` → MACHINE-IDENTITY.md. Claim the
   QUEUE row (above). Session-chain check per CLAUDE.md on your first row.
2. **Portraits:** `python3 media-production-v2/v2_story_cast.py <build>`
   with a computed `--ceiling` (dry-run first to see the count).
3. **Plates:** the author committed `PLACE-REF/*.jpeg` — verify they exist. If
   the author's QC.md names a promote-first place: generate that place's anchor
   beat FIRST (`v2_gen_api.py <build> --only <beat> --ceiling …`), eyeball it
   once (right place, right period, nothing modern), then
   `python3 media-production-v2/v2_stash.py --promote <build> <TOKEN> <file>`
   and continue — the remaining beats of that place copy it.
4. **Generate:** `python3 media-production-v2/v2_gen_api.py <build> --ceiling …`
   (it resumes automatically; sub-2K and missing frames re-pull until done).
5. **Light QC — one pass, capped.** View each frame ONCE against its beat's
   `must_show` / `must_not_show`. Reroll ONLY obvious garbage: missing named
   subject, a second cream-robed figure, a modern object, someone staring into
   the lens, anatomy visibly wrong, wrong count the narration names. Max TWO
   rerolls per frame (`--only <beat> --redo --ceiling …`); still bad → log the
   beat in QC.md under "FIX-WAVE" and keep the best take. Do not chase subtle
   drift; that is the fix wave's job.
6. **Assemble:** `python3 media-production-v2/v2_assemble.py <row>`. It must
   print `AUDIO LOCK PASS` — if it fails the audio hash, STOP the row, log, do
   not ship. Extract 3 caption frames from the RENDERED mp4
   (`ffmpeg -ss <t> -i <mp4> -frames:v 1 …` at an early, a middle, and the
   question-card timestamp), view them once: captions in the bottom band only,
   question card clean.
7. **Ship (two commits, exactly like row 39):**
   a. `git add -f <build>/<final>.mp4`, add QC.md + boards, update the row's
      QUEUE status text (model it on row 39's entry), commit → note the hash.
   b. Edit `site/review.html`: find the row's existing card (`id="vNN"`), add
      `data-review-wave="realistic-v2"`, set `data-hash` to the FULL commit hash
      from (a), point the `<video src>` at
      `https://github.com/noremacttevol/MBM/raw/main/media-production-v2/<build>/<mp4>?v=<first 12 of hash>`,
      and write the "🛠 What this cut changed" flag: picture count vs V1, the
      seconds-per-picture change, one row-specific fact, and the closing line
      "The narration, voices and timing are untouched — the audio is
      byte-identical to the cut you already have." Add a SESSION-LOG entry,
      commit, push both commits.
8. Tick `Built` on the QUEUE row. Clear nothing else. Next row.

## Session pacing

Rows until context runs low (typically 1–2 rows — the frame views are the bulk).
Chain out: SESSION-LOG entry, commit, push. Never leave a claimed row without a
QC.md note saying exactly where it stopped and the resume command.

## Money truth (so nobody is surprised)

A typical row ≈ 45 stills + 3 portraits + ~15% rerolls ≈ **$7–8**. The remaining
~162 rows ≈ **$1,100–1,300 total** on the Gemini key, spread across sessions,
every run under its own ceiling, every image on the shared meter
(api-spend.jsonl). Cameron approved the API for all 200 (2026-07-30) — do not
stop to re-ask; the ceilings and the meter are the protection.
