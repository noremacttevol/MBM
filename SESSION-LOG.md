## 2026-08-13 (cont. 95) — CHURN KILLED: 25-min per-(job,row) cooldown + row-stamped session logs + escalation counter actually counting — Cameron's "wasting my tokens" complaint root-caused with numbers — Machine A `Dev`, process-engineer session

Cameron (04:00): "i feel like you are wasting my time and tokens... trash work compiling up... almost no new approved videos." Facts pulled before answering: since full-throttle start (01:30) — 23 sessions, 8 complaint-fix ships, 2 fresh BUILT (+3 RUNNING mid-build), 128 images / $17.15. **Zero complaints filed by Cameron tonight — yet rows 95, 147, 135 each got 3 sessions and 117 got 2.** Root cause: ship -> CDN + review-sync lag (minutes) -> next 5-min tick still sees the old live hash matching reportedAgainst -> re-fires the SAME row. The 10-min cadence had been masking it; my 5-min throttle exposed it. ~1/3 of tonight's sessions were this waste.

- **CHURN COOLDOWN:** after any session completes, `cool-<job>-<row>` is touched; the picker skips that (job,row) for 25 min and falls through to the NEXT candidate (emit() now returns on cooled rows instead of exiting). Seeded cooldowns for tonight's repeat rows so the very next tick moves to fresh work (dry-run: audio row 155).
- **Row-stamped logs:** session logs now named `<ts>-<job>-r<row>.log` — required because logs hold session OUTPUT which doesn't reliably echo the row.
- **ESCALATION FIXED (2nd bug):** yesterday's Opus->Fable escalation counted rows by grepping log CONTENT — always ~0, never fired (rows 95/147 should have escalated tonight and didn't). Now counts by filename.
- Honest picture for Cameron: fresh-build rate was also throttled by complaint-class work legitimately outranking builds; with churn dead, lanes go to the 62 ready builds.

---

