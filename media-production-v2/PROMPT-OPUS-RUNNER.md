# OPUS RUNNER SESSION — generate, assemble, and ship first-attempt V2 cuts

> **To start a session, paste exactly this into a new Opus chat on Machine A
> (`Dev` — the ONLY production machine, Cameron 2026-08-05):**
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
- Claim-by-push in `media-production/QUEUE.md` BEFORE generating: pull, write
  your machine + date in the row's Claim, commit, push; a rejected push means
  the row is taken — move on. (One machine now — Cameron, 2026-08-05 — but the
  claim stays: it is free protection against a crashed or parallel chat
  double-building a row.)
- **THE LEARNING LAW (Cameron, 2026-08-05).** Before the first credit of a row:
  read the TWO META-LAWS + ALL numbered lessons in V2-REBUILD-RUBRIC.md, and run
  `python3 media-production-v2/v2_outline.py <row>` — the complaints shown on
  top are Cameron's own words about THIS row. You may not ship a cut whose
  QC.md lacks a **COMPLAINT LEDGER**: one line per open complaint stating
  exactly what in this cut fixes it (frame number / caption / gate). No open
  complaints → write "COMPLAINT LEDGER: none open." A shipped cut that repeats
  a filed complaint is the worst failure this pipeline can produce.
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
   `must_show` / `must_not_show`, the row's open complaints, and the quick
   mechanical lessons (beards — lesson 13; figure scale — lesson 14; modern
   objects; anatomy). Reroll ONLY obvious garbage: missing named subject, a
   second cream-robed figure, a modern object, someone staring into the lens,
   anatomy visibly wrong, wrong count the narration names, a frame that repeats
   an open complaint. Max TWO rerolls per frame (`--only <beat> --redo
   --ceiling …`); still bad → log the beat in QC.md under "FIX-WAVE" and keep
   the best take. Do not chase subtle drift; that is the fix wave's job.
   **COST LAW: total rerolls ≤15% of the row's beats. If you hit the budget,
   stop rerolling, FIX-WAVE the rest, and say so in QC.md.**
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
      byte-identical to the cut you already have." **If the row had open
      complaints, the flag must also answer them in Cameron's terms — e.g.
      "Your complaint 'Jesus was a giant' — every multi-figure frame now passes
      the scale gate" — so he can verify his own fix in one look.** Add a
      SESSION-LOG entry, commit, push both commits.
   c. **DEPLOY — a push is NOT a delivery (Cameron, 2026-08-05: "i still
      dont have any of that on my reviewer").** The reviewer is Firebase
      hosting, project `milk-b4-meat`, serving `site/`. Git is only the
      warehouse; until you deploy, Cameron sees the OLD page and your row
      does not exist to him. Run:
      `firebase deploy --only hosting`
      (if it 429s on the storage quota, run
      `python3 media-production/prune_hosting_versions.py` and deploy again).
      Then VERIFY on the live URL, never assume:
      `curl -s https://milk-b4-meat.web.app/review.html | grep -o 'id="vNN"[^>]*data-hash="[^"]*"'`
      and confirm the mp4 URL returns HTTP 200 with a real content-length.
      A row is not shipped until the live page carries the new hash.
8. Tick `Built` on the QUEUE row. Clear nothing else. Next row.

## Session pacing

Rows until context runs low (typically 1–2 rows — the frame views are the bulk).
Chain out: SESSION-LOG entry, commit, push. Never leave a claimed row without a
QC.md note saying exactly where it stopped and the resume command.

## Money truth (so nobody is surprised) — and THE COST LAW

Measured baseline (2026-08-05, first 41 rows): **$6.10/row average, 19% of all
spend was rerolls** ($44.62 of $236.64 — build-07 pulled one beat SEVEN times;
that is what the ≤15% reroll budget exists to kill). A typical row ≈ 45 stills
+ 3 portraits ≈ **$6–8**. The remaining rows ≈ **$1,000–1,200 total** on the
Gemini key, spread across sessions, every run under its own ceiling, every
image on the shared meter (api-spend.jsonl). Cameron approved the API for all
200 (2026-07-30) — do not stop to re-ask; the ceilings and the meter are the
protection.

**THE COST LAW (Cameron, 2026-08-05: "the cost should get cheaper"):** the
trend must go DOWN as lessons accumulate. Each session's SESSION-LOG entry
states its $/row and reroll % against the running average and explains any
overage. Reuse before regenerate (plates, promoted anchors, passing frames are
never re-pulled). Touch each row ONCE — batch every known fix into one re-cut;
every re-cut voids Cameron's approval and re-queues the row on his reviewer.
