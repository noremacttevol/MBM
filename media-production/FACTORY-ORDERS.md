# FACTORY ORDERS — the single source of truth for the MBM video factory

> Written 2026-07-14. Every Claude Code session on every computer reads THIS file
> after pulling the latest repo, then does its job with no further questions.
> This supersedes any older ad-hoc kickoff prompt. If anything elsewhere conflicts
> with this file, this file wins.

---

## MONEY RULE #1 — never break it

Make every still in **Google Flow** using Cameron's **Ultra** subscription:
**Nano Banana 2, 9:16, 1x — 0 credits.** Flow is logged in at
`labs.google/fx/tools/flow`; drive it with your Chrome browser tools.

**NEVER run `gen_stills.py`. NEVER call the paid Gemini image API.** That spends real
money Cameron did not authorize. (The local/free tools are fine and required:
`jesus_face_gate.py`, `make_narration.py` (edge-tts), `build.py`, `gen_site_index.py`.)

---

## ✅ THE-200 v2 IS LIVE (approved by Cameron 2026-07-15). ALL MACHINES GO.

The catalog is now three shelves: rows 1–100 EVERYONE · 101–150 BRIDGE · 151–200
MEMBER (see THE-200.md). QUEUE.md is regenerated to match. All holds are lifted.

**Migration notes (one-time):**
- Old row 84 (Calling the Fishermen, built) is now row 71 — folder renamed.
- Old row 85 (Calling Matthew) is now row 72 — Machine B: finish your in-flight
  build and tick ROW 72; name the folder build-72-calling-matthew.
- Old row 124 (Gethsemane, REJECTED — hair changes length in one scene) is now
  row 91 — folder renamed build-91-gethsemane. Fix the one scene, rebuild, tick 91.
- Old row 164 (Rainbow covenant) is now row 135 — Machine D: finish your in-flight
  build and tick ROW 135; name the folder build-135-rainbow-covenant.
- MEMBER rows (151–200) are verse-videos: same style block, same laws, same feed
  card; the closing card also carries a one-line pointer to the matching Gospel
  Library topic named in THE-200.md. No church logos, footage, or manual text ever.

## MACHINE ASSIGNMENTS (v2)

| Machine | Rows (in QUEUE.md) |
|---|---|
| **A** | 45–83 |
| **B** | 84–120 (plus finishing 72; plus the row-91 Gethsemane fix) |
| **C** | 121–160 (skip 135 while Machine D's claim is on it) |
| **D** | 161–200 (plus finishing 135) |

Your NEXT job = the lowest-numbered row **in your range** where `Built` is ⬜ and
`Claim` is empty. Never touch a row outside your range or one another machine claimed.
(#41 and #48 are already built — the queue tells you what's left; just skip built rows.)

---

## RUN UNATTENDED

Do NOT ask Cameron questions. Make sensible defaults, keep going until every row in
your range is built and pushed. Only stop for a real technical blocker you cannot
solve — and then say it in one line. Standing decisions already made (do not re-ask):
- Over-length videos: **30MB size cap**, keep every word (don't trim, don't starve).
- Style/look: locked. Use the Master Style Block byte-identical.

---

## READ ONCE, THEN NEVER AGAIN (save Claude tokens)

Read whole big files at most once; use `grep`/`sed` for single lines; copy templates
instead of re-inventing. Do NOT read SESSION-LOG.md, other builds' logs, or history
prose.
1. `media-production/CREW-GUIDE.md`
2. `media-production/PRODUCTION-BIBLE.md` — LAW sections only (§0 Three Laws, Standing
   Laws, §4b Pre-Flight, §5 QC, §5b Failure Log). Skip history/money/mission prose.
3. `media-production/build-47-houses-on-rock-and-sand/BUILD-STATUS.md` — the exact
   $0 FLOW procedure.
4. Use `build-48-new-wine-old-bottles/` and `build-41-counting-the-cost/` as your
   PROMPTS.md + make_narration.py + build.py **templates**. Change only story content;
   build-41 also shows the 30MB-cap build.py.
5. `media-production/FLOW-BUILD-PLAYBOOK.md` — the distilled fast/low-token procedure:
   the exact Flow $0 settings, the reliable JS download (skip screenshots), panel/face
   reroll rules, the bundled-ffmpeg + PATH gotchas, caption-box tuning, and the routine
   `gen_site_index.py`/`index.html` rebase-conflict fix. Read this and you can build a
   video in far less context.

## BINDING LAWS (don't re-derive)

Jesus's face is NEVER shown or prompted (camera behind / over-shoulder / at distance);
**only Jesus wears cream/off-white** — dress everyone else in darker earth colors, in
every prompt; two-voice (narrator `en-US-AndrewNeural`, modern paraphrase; Jesus
`en-US-ChristopherNeural`, EXACT KJV only, no Multilingual voice); Phase-1
**STILLS-ONLY**, no motion clips; Master Style Block byte-identical in every prompt;
character/wardrobe locks written into every prompt the character appears in; no spoken
gap over 2.5s; tell the whole story to the final verse; closing card is an invitation,
never a fear-question. File name = `book-chapter_story-name.mp4`.

---

## PER-VIDEO LOOP (repeat until your range is empty)

1. `git pull --rebase`. In QUEUE.md find the lowest row in YOUR range with Built ⬜ and
   Claim empty. Stamp Claim `CLAIMED Machine <letter> <date>`, commit + push NOW.
2. Read the KJV passage in full context. Storyboard 8–16 beats, one still each.
3. Write `build-NN-<slug>/PROMPTS.md` from the template (Master Style Block
   byte-identical; character/wardrobe locks in every prompt a character appears in).
4. `python3 media-production/jesus_face_gate.py --dir <dir>` MUST exit 0. Fix prompts
   and re-run until it passes. NO art before it passes.
5. In Flow: New project → **Image → Nano Banana 2 → 9:16 → 1x** → paste the FULL prompt
   (style block + body) → generate → download the **2K** image → save as
   `<dir>/assets/<slug>.jpeg`. One still per beat. (Downloads: Chrome "ask where to
   save" OFF so files land on disk; see build-47 BUILD-STATUS for the download detail.)
6. QC every still: face never visible, count anatomy, action reads, time-of-day matches
   scripture, style matches template, no baked-in text, only-Jesus-in-cream. Regenerate
   misses in Flow.
7. `python3 make_narration.py` (edge-tts). Then `python3 build.py` to assemble (Ken
   Burns drift, serif captions, cream-italic KJV, closing card). Export 9:16
   1080x1920 H.264 **under 30MB**, named `book-chapter_story-name.mp4`.
8. Full QC pass: face-audit sampled frames, verify KJV captions are exact, no dead air.
9. Tick **Prep + Built** ✅ for the row in QUEUE.md (leave **Appr** blank — see below).
   Add the title to the TITLES map in `media-production/gen_site_index.py`, then
   `python3 media-production/gen_site_index.py`.
10. **PUBLISH = your notification to Cameron:** `git add -A`, commit, `git pull
    --rebase`, `git push origin main`. That publishes the finished video to the gallery
    at **https://noremacttevol.github.io/MBM/** — Cameron watches new videos appear
    there one by one. Cameron never touches git.
11. Next row. Repeat.

---

## APPROVAL — who sets the final checkmark

The **building machines set `Built` ✅ only. They NEVER set `Appr`.**

The **`Appr` ✅ checkmark is set only by the approval-monitor session**, after Cameron
watches a video and says yes. That is a separate Claude chat Cameron runs. Its job:
- When Cameron says a video number is **approved**: `git pull --rebase`, tick that
  row's **Appr** column ✅ in QUEUE.md, commit, push.
- When Cameron says a video is **rejected**: leave Appr blank, write his reason in that
  row's Claim/notes column, and set Built back to ⬜ so a building machine remakes it.
- The monitor NEVER builds videos and NEVER touches the paid API. It only moves the
  approval checkmark.

So the lifecycle of one row is:
`⬜ → Machine X builds + pushes (Built ✅) → appears on the gallery → Cameron watches →
Cameron tells the monitor yes/no → monitor sets Appr ✅ (or bounces it back).`
