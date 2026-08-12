# AUTOPILOT — the loop that builds until all 200 are done

Installed 2026-08-06 on Machine A (`Dev`) after Cameron: "is there any way we
can make this into a loop process until its done?" This replaces the old
media-production/SCHEDULER.md idea — V2 has NO Chrome/Flow step, so the loop
runs the ENTIRE build unattended: generate → QC → assemble → ship → deploy.

## How it works

- A crontab line ticks `media-production-v2/autopilot.sh` every 10 minutes.
  Each tick: if all lanes are busy, do nothing; otherwise start ONE new lane —
  a FRESH headless Claude session on PROMPT-OPUS-RUNNER.md (model: opus,
  2-hour timeout) on the lowest **Ready ✅ / Audio OK / unclaimed** row. Up to
  **6 builds run in parallel** (Cameron, 2026-08-06: "it should take less than
  24 hours" — override with MBM_LANES). Claim-by-push keeps lanes off each
  other's rows. Fresh session per run = clean context = the "one video per
  chat" law.
- **Five job types, in priority order** (THE COMPLAINT-FIRST LAW, Cameron
  2026-08-06): **COMPLAINT-FIX** (re-cut a shipped row Cameron complained
  about — his complaint outranks everything) → stranded-resume → **AUDIO-FIX**
  (PROMPT-AUDIO-FIX.md — closes audio complaints on NEEDS-AUDIO rows; $0
  Gemini; max one lane) → ready-build → author (PROMPT-FABLE5-AUTHOR.md,
  refills the board from NEEDS-BEATS **and picks up NEEDS-REBUILD parks like
  row 11's boat-lock**). Within every queue: complained-about rows first, then
  the LOWEST row number (Cameron's viewing order — THE LOW-NUMBER LAW,
  2026-08-07); the loop re-syncs his live complaints each tick.
- **Billing breaker with fallback:** when the Gemini prepayment is depleted,
  paid jobs (resume/build) are blocked but the loop does NOT idle — audio and
  author work continue free. Top up at https://ai.studio/projects and paid
  builds resume on their own within ~25 min.
- Claim-by-push keeps autopilot and any interactive chat off each other's rows.
- Every law travels with it: learning law (complaint ledger), cost law (reroll
  budget, $/row logging), deploy + live verification. New videos just appear on
  https://milk-b4-meat.web.app/review.html — Cameron only watches / approves /
  complains.
- Throughput at 6 lanes ≈ 4–8 rows/hour: the ~115 already-authored Ready rows
  finish in roughly **15–24 hours** of uptime. The ~39 not-yet-authored rows
  (162–200) queue behind author lanes and follow. Same total Gemini cost —
  just compressed. Rate-limit 429s on either API slow it gracefully (sessions
  park with a resume note; the stranded-resume branch picks them up). The
  machine must be ON (sleep pauses it; it resumes on wake).
- **Cross-session learning:** every session must read `RUNNER-LESSONS.md`
  (shared defect memory) before QC and append any new defect class it finds;
  after every ship it re-runs `v2_stash.py --scan` so finished pictures are
  reused by later rows instead of re-bought.

## Check on it

```bash
tail -20 ~/Desktop/MBM/media-production-v2/autopilot-logs/autopilot.log
```

```bash
crontab -l | grep autopilot
```

## Pause / stop it

```bash
crontab -l | grep -v 'autopilot.sh' | crontab -
```

(That stops future ticks; a build already running finishes its row and stops.)

## Turn it (back) on

```bash
( crontab -l 2>/dev/null | grep -v 'autopilot.sh'; echo '3,18,33,48 * * * * /home/noremacttevol/Desktop/MBM/media-production-v2/autopilot.sh >> /home/noremacttevol/Desktop/MBM/media-production-v2/autopilot-logs/cron.log 2>&1' ) | crontab -
```

## When it's done

When every row is BUILT the ticks log "ALL ROWS BUILT" and do nothing. Remove
the cron line with the stop command above.

## Loop lessons (permanent — each was a live failure)

- **2026-08-11 — QC stamps count from EITHER board cell.** Verify sessions
  appended `QC-OK` stamps into the **Ready** cell while the picker only read
  the **Claim** cell, so row 117 looked forever-unverified and ate every
  verify tick (9 re-fires) while 12 genuinely unverified BUILT rows waited.
  The picker now checks Claim + Ready for `QC-OK`/`QC-FIX`. Never make a
  session hand-count Markdown columns and a parser read only one of them.
- **2026-08-11 — the loop execs a /tmp copy of itself.** A session inside a
  tick committed a new autopilot.sh while the outer bash was still executing
  it; bash reads scripts incrementally, so the running copy died with a
  phantom "line 290" syntax error and lost its `tick done`. Every run now
  copies itself to /tmp and execs the copy before doing anything else.
- **2026-08-11 — COMPLAINT-FIRST inside the build queue too.** The runner
  pass built AUTHORED+Ready rows purely lowest-first, so re-authored
  complaint rows (149, 171, …) waited behind uncomplained fresh builds.
  Complained ready rows now build first, then the rest, lowest-first in both.
