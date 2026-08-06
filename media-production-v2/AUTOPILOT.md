# AUTOPILOT — the loop that builds until all 200 are done

Installed 2026-08-06 on Machine A (`Dev`) after Cameron: "is there any way we
can make this into a loop process until its done?" This replaces the old
media-production/SCHEDULER.md idea — V2 has NO Chrome/Flow step, so the loop
runs the ENTIRE build unattended: generate → QC → assemble → ship → deploy.

## How it works

- A crontab line ticks `media-production-v2/autopilot.sh` at :11 and :41 every
  hour. Each tick: if a build is already running, do nothing (PID lock);
  otherwise pull, find the lowest **Ready ✅ / Audio OK / unclaimed** row, and
  start a FRESH headless Claude session on PROMPT-OPUS-RUNNER.md (model:
  opus, 2-hour timeout). Fresh session per run = clean context = the "one
  video per chat" law.
- If no Ready rows remain but NEEDS-BEATS rows exist, the tick runs an AUTHOR
  session (PROMPT-FABLE5-AUTHOR.md) instead, so the board keeps refilling.
- Claim-by-push keeps autopilot and any interactive chat off each other's rows.
- Every law travels with it: learning law (complaint ledger), cost law (reroll
  budget, $/row logging), deploy + live verification. New videos just appear on
  https://milk-b4-meat.web.app/review.html — Cameron only watches / approves /
  complains.
- Throughput ≈ one row per 1–2 h while the machine is on ≈ 8–12 rows/day ≈
  $50–80/day on the Gemini meter, finishing the remaining board in ~2 weeks of
  uptime. The machine must be ON (sleep pauses it; it resumes on wake).

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
( crontab -l 2>/dev/null | grep -v 'autopilot.sh'; echo '11,41 * * * * /home/noremacttevol/Desktop/MBM/media-production-v2/autopilot.sh >> /home/noremacttevol/Desktop/MBM/media-production-v2/autopilot-logs/cron.log 2>&1' ) | crontab -
```

## When it's done

When every row is BUILT the ticks log "ALL ROWS BUILT" and do nothing. Remove
the cron line with the stop command above.
