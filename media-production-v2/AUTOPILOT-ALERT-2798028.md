# AUTOPILOT LANE-COLLISION ALERT — headless runner PID 2798028, 2026-08-06

A headless Opus runner (this session) was launched on `PROMPT-OPUS-RUNNER.md`
to "run the next ready rows." It stopped **without building a new row on
purpose**. Here is exactly what it found, so the next session / Cameron can
fix the autopilot rather than re-discover it.

## What happened this session
1. Session start: HEAD was `21b1f3806`, AUTHOR-BOARD showed row 43
   (wedding-garment) as **RUNNING** with an orphaned `v2_gen_api.py` (PID
   2770018) still producing its stills from a prior dead session. I treated
   row 43 as a stranded row to rescue: waited for the gen to finish (48/48
   stills, only 3 rerolls = 6.25%, under budget), ran full light QC on all 48
   frames via ffmpeg contact sheets (clean — no cream drift, no giants, no
   modern objects, gold-robe/count law held, outer-darkness beats sorrow not
   torture), assembled (**AUDIO LOCK PASS**), and verified the 3 caption
   frames (bottom-band captions, clean question card).
2. **But while I was doing that QC, ANOTHER lane already built AND shipped row
   43**: commits `be3d0654c` (48 stills, AUDIO LOCK PASS) + `336968852`
   (row 43 on the reviewer). HEAD advanced under me to `94fa79298`. My
   re-assembled mp4 (blob `fe592fd2…`) differed from the shipped, live one
   (blob `763a3df5…`), so I **reverted my working-tree mp4 to the committed
   version and deleted my scratch `segs/`** — leaving zero spurious diff.
   No API spend was wasted by me (the stills I watched were the single pass
   that shipped; my only duplicate work was a free local assemble, reverted).
3. **Row 43 is verified DONE and LIVE**: `curl https://milk-b4-meat.web.app/
   review.html` carries `id="v43" … data-hash="be3d0654cef0…"
   data-review-wave="realistic-v2"`. Nothing more to do on it.

## The real problem (cost + corruption hazard) — please fix the autopilot
- **3 live `claude -p` autopilot lanes are all running in the SAME main
  worktree** (`/home/noremacttevol/Desktop/MBM`): PIDs 2798028 (me), 2830023,
  2857242 — all `cwd=main`. Only 2 extra git worktrees exist
  (`peaceful-wright-cbe256`, `pensive-cori-a4c725`), so most lanes are NOT
  isolated.
- Consequences observed / risked:
  - **Duplicate work on the same row**: two lanes both took row 43 (one shipped
    it, one — me — rescued it redundantly). The claim-by-push did not prevent
    it because the orphan's claim looked stranded.
  - **Shared-file clobber risk**: lanes editing the same `review.html`,
    `QUEUE.md`, `AUTHOR-BOARD.md`, `SESSION-LOG.md` in one tree can overwrite
    each other's edits (last-writer-wins on disk) — this can silently drop a
    row's reviewer card or a claim.
  - **Concurrent Gemini gens on one API key** (build-45 active alongside
    leftover waiters) raise 429 risk and make the per-run `--ceiling` race a
    shared meter.
- **Suggested fix**: give every lane its OWN `git worktree` (isolation), or
  serialize lanes with a real cross-lane lock, so no two lanes ever share the
  main tree or touch the same row. The existing `.autopilot.lock` (single PID)
  is not holding — 3 lanes got past it.

## Why I stopped instead of building row 46
Adding a 4th concurrent builder in this shared tree would compound the
clobber risk on `review.html` and add a 3rd concurrent gen for marginal
throughput while the other two lanes already cover the frontier (row 45
in-flight). The safest useful action was to verify row 43 is delivered,
leave no footprint, and surface this alert. This file has a unique name so it
cannot clobber any hot shared file.

— headless runner, 2026-08-06

---

## ANSWERED (main session, 2026-08-06, same night)

Every hazard above is now addressed — future lanes: do NOT stop over these.
1. Lane cap now counts LIVE `timeout 7200 claude -p` processes (pid files
   proved deletable); cap enforced at MBM_LANES=4.
2. PROMPT-OPUS-RUNNER.md now carries the PARALLEL-LANES LAW: claimed/RUNNING
   rows are NEVER touched by sessions (strand rescue is autopilot.sh's resume
   branch only, fires at zero live lanes); shared files get pull-rebase
   immediately before each edit + push immediately after; `git clean`/`reset
   --hard`/deleting files you didn't create is FORBIDDEN (that is what wiped
   the lane pid files); ceilings get a +$25 concurrency allowance.
3. Worktrees rejected deliberately: per-lane branches + api-spend.jsonl and
   board merges across worktrees cost more correctness than they buy; the
   shared-tree rules above close the observed clobber windows.
This file stays as the record; the law lives in the runner brief.
