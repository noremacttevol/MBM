# AGENT #4 — Captions, Video Organizer, Submitter, Reviewer-Board Keeper

**Set up 2026-07-23.** Cameron runs a 4-agent line for the ElevenLabs redo of THE-200:

| # | Agent | Job |
|---|-------|-----|
| 1 | Video planner | Transcripts + plans; doctrine check ("what Jesus would want"), checks against all others |
| 2 | Audio maker | Takes #1's transcripts → ElevenLabs → new `audio/*.mp3`; drops `.eleven-done` / `.audio-eleven-done` |
| 3 | Still maker | Reads Cameron's complaints + the auto-scanner; fixes bad pictures in `assets/` per the character/still rules |
| **4** | **This agent** | **Re-caption the video, organize it into its folder, submit it to the reviewer site, keep the board healthy** |

## My lane — do ONLY this
- **Never** touch transcripts (#1), audio (#2), or stills (#3). I consume their output.
- When #2 drops new audio OR #3 fixes a still, the build's captioned `.mp4` is stale. I re-run
  `build.py` (it burns fresh caption timing over the current audio + stills), verify it, and ship it.
- Keep the reviewer website (https://milk-b4-meat.web.app/review.html) accurate and fresh.

## The one command
```bash
bash media-production/caption-and-ship.sh            # re-caption every stale build, ship all
bash media-production/caption-and-ship.sh 6 7 9      # only these build numbers
BATCH=3 bash media-production/caption-and-ship.sh    # cap per run (this is what cron uses)
RENDER_ONLY=1 bash media-production/caption-and-ship.sh   # caption + verify, don't ship
```
**Stale** = a build with an ElevenLabs marker whose newest input (`.eleven-done`/`.audio-eleven-done`,
`audio/*.mp3`, or `assets/` stills) is newer than its finished root `*_*.mp4`. Re-running `build.py`
is safe + idempotent. Each cut is gated by `admin/verify-mp4.sh` (truncated-mp4) before it can ship.

## What ships it + updates the board
`caption-and-ship.sh` hands verified cuts to **`admin/ship-fixes.sh`**, which:
1. checks the **approved-lock** (never ships over a video Cameron approved),
2. makes one small commit per video + pushes to GitHub (videos stream to the board from there),
3. runs `admin/sync-reviews.mjs` (rebuilds `approvals.json` + `COMPLAINTS.md` from Firestore),
4. regenerates `gen_site_index.py` → `site/review.html` and **`firebase deploy`**s the board.

## Automation (installed 2026-07-23)
```
*/15  * * * *  admin/ship-fixes.sh                    # existing: ships any dirty verified mp4 + deploys board
7-59/15 * * *  BATCH=3 media-production/caption-and-ship.sh   # NEW: re-caption 3 stale builds/run
```
Both share flocks; safe to overlap. The board fills steadily as builds get re-captioned.

## The reviewer board (Firestore `reviews` collection)
- **Fresh start done 2026-07-23:** `node admin/reset-approvals.mjs` cleared all 86 old approvals →
  0 approved. The 61 old complaints were **kept** (Cameron's call) so picture-defect notes (#19, #56,
  #107, …) don't get lost; they auto-clear when Cameron approves each new cut.
- Approvals are **version-locked** to the exact mp4 hash: when I ship a new cut, an old approval
  auto-falls-off and it returns to "needs review."
- A complaint stays ACTIVE until Cameron approves — shipping a new cut does NOT clear it (rule since
  2026-07-21). `COMPLAINTS.md` is the machine-readable "what #3/#1 must fix" list.
- To wipe approvals again for a new wave: `node admin/reset-approvals.mjs`. There is no complaint-wipe
  script by design.

## Health checks
```bash
node admin/dump-approvals.mjs | python3 -c "import json,sys;d=json.load(sys.stdin);print('approved',sum(1 for v in d.values() if v['approved']),'complaints',sum(1 for v in d.values() if v['complaint']))"
tail -f media-production/caption-and-ship.log      # my render/ship log
tail -f admin/ship-fixes.log                       # ship + deploy log
```
Requires `node` + `firebase` (both present on this box: `~/.npm-global/bin`). `whisper`, `ffmpeg` present.

## FINISH GATE (added 2026-07-23, Cameron's order: verify pictures, then finish, loop till done)
`finish_gate.py` decides which videos #4 may finish NOW. A build is GREEN only if:
- **echo-clean** (`echo_scan.py` finds no narrator-repeat) — else routed to **#1**,
- **no open picture complaint** on the board — else **#3**,
- **not on** PICTURE-REDO-WORKLIST / PICTURE-WORKLIST / STILLS-NEEDED — else **#3**,
- **passes** `character_ref_gate.py` + `jesus_face_gate.py` (on-law faces) — else **#3**.
No machine can judge "does the picture look good" — that's #3 + Cameron's eyes. This gate
only blocks KNOWN-bad pictures; technical QC (dead air/hum/size/loudness/captions) is checked
per-cut at ship time by scan_defects/verify-mp4.

`finish-loop.sh` = run the gate, then caption-and-ship ONLY the green numbers. Cron runs it
`7-59/15` at BATCH=3, so as #1 clears echoes and #3 fixes pictures, freshly-green builds get
finished automatically — "don't stop until there are no more to make."
- First run 2026-07-23: **40 green** finishing now. Blocked: 125 echo→#1, ~65 picture-worklist→#3,
  39 character_ref→#3, 26 picture-complaint→#3, 18 jesus_face→#3.
- Commands: `python3 media-production/finish_gate.py` (summary), `bash media-production/finish-loop.sh`.
