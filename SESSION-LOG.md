## 2026-08-13 (Opus runner, complaint-first, unattended/headless) — Row 95 Thief on the Cross: NEW complaint "1:03 they are facing each other" FIXED + shipped touch-once — Machine A `Dev`

**Commit:** `3b971e9d3` (build: mp4 + s11 + QC + beats_v2 + AUTHOR-BOARD + RUNNER-LESSONS + api-spend); review.html + this log follow.

Complaint-first + low-number dispatched me to AUTHOR-BOARD row 95 (lowest waiting complained row). Cameron's NEW open complaint on the reshipped cut: **"1:03 they are facing each other again and that is wrong replace it."**
- **Frame trace (from the rendered mp4, not guessed):** clip time-map c000–c010 → **1:03 (63s) = c010 = s11** (`s11-today-the-faith-of-a.jpeg`). Extracted the live frame: Jesus's + the penitent thief's crosses were **angled inward, both men in a mutual profile gaze**.
- **PROMPT AUTOPSY = CAUSED.** b11's must_not_show already forbade "crosses angled toward each other," but the positive scene prose commanded **"the two faces turned each other's way along the row"** — the model obeyed the positive line and angled both crosses inward to make the eye-line work. Rewrote b11 scene/must_show/must_not_show → both crosses straight PARALLEL uprights seen from the FRONT, both bodies squared to the viewer, never facing each other (pattern proven in b05/b07).
- **Built touch-once:** regen b11 → parallel-forward achieved but the HILL/overlook look spawned a **modern metal guardrail + bolt** → added "NO modern fence/railing/bolts" to b11 must_not_show and **rerolled once** → clean (natural rocky hillside, distant city wall, small watchers). **$0.26, 1/11 = 9% rerolls (≤15%), meter $634.36→$634.62** — well under the $6.10 baseline (single-beat C-FIX).
- **FULL-CUT GATE 6b PASS** on all 11 rendered beats + 3 caption frames + card (every other beat already clean; only s11 changed). **AUDIO REBUILD PASS `e5ba558a` byte-identical** (narration/voices/timing untouched); new mp4 md5 `6f372e7e`.
- **Ops note:** the first b11 reroll HTTP call hung ~9 min (socket sleeping, 0% CPU, no read-timeout, billing healthy) — killed it (nothing partial), retried under `timeout 240` → success. Logged as a RUNNER-LESSON (wrap paid gens in `timeout`).

Deployed to Firebase + live-verified; card v95 back in Unwatched, data-hash + ?v = ship commit, "what changed" answers his complaint in his words.
## 2026-08-13 (cont. 95) — CHURN KILLED: 25-min per-(job,row) cooldown + row-stamped session logs + escalation counter actually counting — Cameron's "wasting my tokens" complaint root-caused with numbers — Machine A `Dev`, process-engineer session

Cameron (04:00): "i feel like you are wasting my time and tokens... trash work compiling up... almost no new approved videos." Facts pulled before answering: since full-throttle start (01:30) — 23 sessions, 8 complaint-fix ships, 2 fresh BUILT (+3 RUNNING mid-build), 128 images / $17.15. **Zero complaints filed by Cameron tonight — yet rows 95, 147, 135 each got 3 sessions and 117 got 2.** Root cause: ship -> CDN + review-sync lag (minutes) -> next 5-min tick still sees the old live hash matching reportedAgainst -> re-fires the SAME row. The 10-min cadence had been masking it; my 5-min throttle exposed it. ~1/3 of tonight's sessions were this waste.

- **CHURN COOLDOWN:** after any session completes, `cool-<job>-<row>` is touched; the picker skips that (job,row) for 25 min and falls through to the NEXT candidate (emit() now returns on cooled rows instead of exiting). Seeded cooldowns for tonight's repeat rows so the very next tick moves to fresh work (dry-run: audio row 155).
- **Row-stamped logs:** session logs now named `<ts>-<job>-r<row>.log` — required because logs hold session OUTPUT which doesn't reliably echo the row.
- **ESCALATION FIXED (2nd bug):** yesterday's Opus->Fable escalation counted rows by grepping log CONTENT — always ~0, never fired (rows 95/147 should have escalated tonight and didn't). Now counts by filename.
- Honest picture for Cameron: fresh-build rate was also throttled by complaint-class work legitimately outranking builds; with churn dead, lanes go to the 62 ready builds.

---

