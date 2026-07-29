# V2-PICTURE-SESSION — paste this to start a pictures-only session

> Cameron: open a new Claude Code session on this repo, set the model to OPUS 5,
> and paste the block below. Nothing else.

```
Read V2-NEXT-SESSION-PROMPT.md and execute it. Start now.

PICTURES ONLY. Do not touch git beyond commit+push of your own work. Never
merge, rebase, or repair history unless I ask.

WATCHDOG — do this every 10 minutes, all session:
  ls -t media-production-v2/build-*/assets/*.jpeg | head -1 | xargs stat -c '%y'
If that timestamp is more than 8 minutes old, generation is DEAD. A live
v2_run_all process proves nothing — it walks beats and logs progress while
producing zero pictures. Diagnose from the newest *.FAILED.txt beside the
intended output, fix the cause, confirm a new jpeg lands, then continue.

Exactly ONE runner. Check `pgrep -af v2_run_all` before starting one, and never
start a second. A runner with --first N is worthless if rows N+ have no
beats_v2.py — it idles forever.

Between watchdog checks, author beat maps for the lowest-numbered rows lacking
one. Use v2_scaffold.py for the mechanical half, then write every scene by hand.
Skip row 17 (deferred). Commit each row as it passes --check.

Report only: pictures on disk, rows authored, and any stall with its cause.
```

## Why each line is there

- **Pictures only / hands off git.** 2026-07-29: a session spent hours merging a
  6-day divergence that Cameron had not asked for, while the generator sat dead.
- **The watchdog.** The same session reported "runner alive, 220 on disk" twice
  while generation had been stopped for hours. `pgrep` proves the process exists,
  not that pictures are landing. Only the newest file's timestamp proves that.
- **Exactly one runner.** A racy `pgrep` read "dead" when the runner was alive; a
  second was started and two processes briefly fought over the same Chrome.
- **--first N warning.** A `--first 50` runner idled for over an hour because
  every row in its range was unauthored, while 300 finished pictures waited.
- **Scaffold then hand-write.** `v2_scaffold.py` does the bookkeeping half. Its
  output deliberately fails `--check` until every scene is written, so it can
  never reach Flow half-done.
