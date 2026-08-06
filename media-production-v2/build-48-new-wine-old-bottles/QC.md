# QC / RUNNER HANDOFF — build-48-new-wine-old-bottles (Luke 5:33-39)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 35 beats, ~196 s. Audio OK. No open complaint.

## Coverage shape

Two true wides with stated geometry: b01 (courtyard establish — the
three fasting men approaching, in profile) and b06 (the wedding at full
joy, camera behind the nearest dancers). Nine former wides re-flagged,
including the two object-frames the flag would have ruined: b18 (the
puckered patch on the washed coat) and b26 (the burst wineskin aftermath)
are PERSON-FREE — phantom people in either kills the frame.

## Place plates — all promote-first (stash had no honest match)

| Token | Promote from | Then covers |
|---|---|---|
| COURTYARD | b01 `assets/s01-...jpeg` | b05 b08 b11 b15 b31 b34 + other courtyard beats |
| WEDDING | b06 `assets/s06-...jpeg` | b09 and the other wedding beats |
| WORKSHOP | first workshop beat's good frame | the cloth/patch beats |
| CELLAR | first cellar beat's good frame | the wineskin beats |

The stash suggested COURTYARD from build-34 (rich fool) — DECLINED, same
reason as row 42: that is a wealthy estate's flagstoned courtyard, wrong
world for this ordinary public courtyard. Do not --take it.

## Complaint-corpus checks

- **Identity (32/62/91/102):** the THREE askers stay the same three men
  in every courtyard beat — face-board them; count is exactly three
  (row-135 class).
- **Gaze convergence (row-83):** b09 the wedding faces orient to the
  groom like plants to sun — the groom must be IN frame or his direction
  unmistakable.
- **Object truth (rows 7/11 class):** the wineskins are PERIOD goatskin
  vessels, never glass bottles (the KJV word "bottles" means skins — any
  glass in frame is the row-7 modern-object defect). The patch/coat
  beats show hand-woven wool, the tear worse AFTER washing (b18).
- **RESTRAINED burst (b26):** aftermath only — split skin, spilled wine
  on the cellar floor; no explosion drama, and wine reads as wine,
  never as blood (frame it dark-red on stone, not spattered).
- **Two-mood law:** courtyard beats carry Jesus's joy→shadow→joy arc
  (b11 is the bridegroom-taken-away verse — the one solemn frame; do
  not brighten it). Wedding = lamplit night joy; workshop/cellar =
  plain working light. Palettes must not bleed between worlds.
- Only Jesus wears cream anywhere.

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (37th resume attempt, headless)

Fresh headless resume (direct user instruction to resume row 48, not a cron tick). Pulled clean
(Already up to date, autostash). `--check` PASSES (35 beats, v4 PASS).
11/35 stills intact (assets/ s01-s09, s16, s22), 4 plates present, 0 portraits outstanding.
Meter unchanged at $409.64. Recomputed ceiling
439.46 (meter $409.64 + 24 remaining × 0.134 × 1.5 + 25 concurrency). Ran
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10 → s10)**, `prepayment credits are depleted`. **$0 spent.** Thirty-seventh
consecutive resume blocked by the identical empty-prepayment state — a HARD billing block, not a
rate limit; no automated resume can refill an empty prepayment balance (the script's internal
retry already fired before surfacing the 429; foreground sleep is blocked in this headless shell,
so the honored retry stands). Row is HARD-BLOCKED on Cameron and cannot advance headless. ONLY a
billing top-up at https://ai.studio/projects unblocks it; then re-run the resume command below
(resumes free — the 11 passing frames are never re-pulled) and the runner finishes the row
unattended through assemble → ship → firebase deploy → BUILT. Row left State RUNNING / Claim
A-auto. (Note updated in place across the 21st→35th probe to avoid unbounded QC growth — full
park history preserved below. Circuit breaker in autopilot.sh, shipped on the 34th probe, is what
stops the cron from spawning further $0 paid ticks while billing is empty; it self-heals on top-up.)

**ROOT-CAUSE FIX THIS SESSION (stop the $0 session bleed):** 30 prior park notes asked Cameron to
pause the cron by hand; that never happened, so the 10-min autopilot kept spawning fresh Opus
`claude -p` sessions that ALL hit the same depleted-prepayment wall and burned tokens for $0. This
session added a **fail-safe billing circuit breaker to `autopilot.sh`**: before spawning a PAID
(runner/resume) tick it checks whether any runner/resume log in the last 25 min reported
`prepayment credits are depleted` / `RESOURCE_EXHAUSTED`, and if so skips the tick (author/$0 ticks
are never blocked). It **self-heals** — the moment Cameron tops up, a run succeeds, leaves no fresh
depletion log, and the loop resumes with no crontab edit and no manual re-enable. Verified with
`bash -n` + `./autopilot.sh --dry-run` (breaker correctly skipped the next paid tick). This does
NOT unblock row 48 — only a top-up does — it just stops the board from wasting Opus sessions while
billing is empty.

**⚠️ THE BLOCK IS GLOBAL, NOT ROW-48-SPECIFIC. Every V2 row's generation returns the same
depleted-prepayment 429.** The ONLY action that moves this row — and unblocks the whole board — is
topping up the Gemini prepayment balance at https://ai.studio/projects. After that, one run of the
resume command below finishes the row unattended (assemble → ship → firebase deploy → BUILT), and
the new circuit breaker lets the cron resume the rest of the board automatically.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (19th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date — autostash), `--check` PASSES
(35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4 plates present
(courtyard/wedding/workshop/cellar). Meter unchanged at $409.64 (api-spend.jsonl last line
is still build-116 at 08:29). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted` (the script's own single retry fired
internally before surfacing the 429). **$0 spent, meter unchanged at $409.64.** Nineteenth
consecutive resume blocked by the same empty-prepayment state — a hard billing block, NOT a
rate limit; no wait can refill an empty prepayment balance. Only Cameron can clear it: top up
billing at https://ai.studio/projects, then re-run the resume command below (resumes free —
the 11 passing frames are never re-pulled). Row left State RUNNING / Claim A-auto.

**This row is HARD-BLOCKED on Cameron and cannot advance headless** — 19 identical
attempts prove that only a billing top-up (not another automated resume) will move it.
Every future headless resume will produce the same 429 until the prepayment balance is
refilled at https://ai.studio/projects. Nothing else is wrong with the build.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (16th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date — autostash), `--check` PASSES
(35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4 plates present
(courtyard/wedding/workshop/cellar). Meter unchanged at $409.64 (api-spend.jsonl last line
is still build-116 at 08:29). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted` (the script's own single retry fired
internally before surfacing the 429). **$0 spent, meter unchanged at $409.64.** Sixteenth
consecutive resume blocked by the same empty-prepayment state — a hard billing block, NOT a
rate limit; no wait can refill an empty prepayment balance. Only Cameron can clear it: top up
billing at https://ai.studio/projects, then re-run the resume command below (resumes free —
the 11 passing frames are never re-pulled). Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (15th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date — autostash), `--check` PASSES
(35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4 plates present
(courtyard/wedding/workshop/cellar). Meter unchanged at $409.64 (api-spend.jsonl last line
is still build-116 at 08:29). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted` (the script's own single retry fired
internally before surfacing the 429). **$0 spent, meter unchanged at $409.64.** Fifteenth
consecutive resume blocked by the same empty-prepayment state — a hard billing block, NOT a
rate limit; no wait can refill an empty prepayment balance (the foreground-sleep retry is also
blocked by the headless shell, so the script's internal retry stands as the honored retry).
Only Cameron can clear it: top up billing at https://ai.studio/projects, then re-run the resume
command below (resumes free — the 11 passing frames are never re-pulled). Row left State
RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (14th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date — autostash), `--check` PASSES
(35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4 plates present
(courtyard/wedding/workshop/cellar). Meter unchanged at $409.64 (api-spend.jsonl last line
is still build-116 at 08:29). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted` (the script's own single retry fired
internally before surfacing the 429). **$0 spent, meter unchanged at $409.64.** Fourteenth
consecutive resume blocked by the same empty-prepayment state — a hard billing block, NOT a
rate limit; no wait can refill an empty prepayment balance. Only Cameron can clear it: top up
billing at https://ai.studio/projects, then re-run the resume command below (resumes free —
the 11 passing frames are never re-pulled). Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (13th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date — autostash), `--check` PASSES
(35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4 plates present
(courtyard/wedding/workshop/cellar). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted` (the script's own single 60 s retry
already fired internally before surfacing the 429). **$0 spent, meter unchanged at $409.64.**
Thirteenth consecutive resume blocked by the same empty-prepayment state — a hard billing
block, NOT a rate limit; a 60 s wait cannot refill an empty prepayment balance. Only Cameron
can clear it: top up billing at https://ai.studio/projects, then re-run the resume command
below (resumes free — the 11 passing frames are never re-pulled). Row left State RUNNING /
Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (12th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date — autostash), `--check` PASSES
(35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4 plates present
(courtyard/wedding/workshop/cellar). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted`. Honored the 429 rule: waited 60 s,
retried once → identical 429 on b10. **$0 spent, meter unchanged at $409.64.** Twelfth
consecutive resume blocked by the same empty-prepayment state — a hard billing block, not a
rate limit. Only Cameron can clear it: top up billing at https://ai.studio/projects, then
re-run the resume command below (resumes free — the 11 passing frames are never re-pulled).
Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (11th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date — autostash), `--check` PASSES
(35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4 plates present
(courtyard/wedding/workshop/cellar). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted`. This is a hard billing block, not a
rate limit — 10 prior resumes confirm a 60 s wait cannot refill an empty prepayment balance,
so the single retry is not repeated in place of Cameron's top-up. **$0 spent, meter unchanged
at $409.64.** (Note: api-spend.jsonl's last line is build-116 at 08:29 today — a brief top-up
window opened and closed before this resume; the balance is empty NOW.) Only Cameron can clear
it: top up billing at https://ai.studio/projects, then re-run the resume command below (resumes
free — the 11 passing frames are never re-pulled). Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (10th resume attempt, headless)

Fresh headless resume. Pulled clean (autostash — other lanes' in-progress files present),
`--check` PASSES (35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4
plates present (courtyard/wedding/workshop/cellar). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted`. Honored the 429 rule: waited 60 s,
retried once → identical 429 on b10. **$0 spent, meter unchanged at $409.64.** Tenth
consecutive resume blocked by the same empty-prepayment state — a hard billing block, not a
rate limit. Only Cameron can clear it: top up billing at https://ai.studio/projects, then
re-run the resume command below (resumes free — the 11 passing frames are never re-pulled).
Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (9th resume attempt, headless)

Fresh headless resume. Pulled clean (autostash — other lanes' in-progress files present),
`--check` PASSES (35 beats, v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). 4
plates present (courtyard/wedding/workshop/cellar). Note: api-spend.jsonl shows build-116
recorded frames at 08:29 today, but the prepayment balance is empty NOW — any brief top-up
window closed before this resume. Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED on
the FIRST shot (b10)**, `prepayment credits are depleted`. Honored the 429 rule: waited 60 s,
retried once → identical 429 on b10. **$0 spent, meter unchanged at $409.64.** Ninth
consecutive resume blocked by the same empty-prepayment state — a hard billing block, not a
rate limit. Only Cameron can clear it: top up billing at https://ai.studio/projects, then
re-run the resume command below (resumes free — the 11 passing frames are never re-pulled).
Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (8th resume attempt, headless)

Fresh headless resume. Pulled clean, `--check` PASSES (35 beats, v4 PASS). 11/35 stills
intact (assets/ s01-s09, s16, s22). 4 plates present (courtyard/wedding/workshop/cellar).
Ran the resume command `v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46`
→ **429 RESOURCE_EXHAUSTED on the FIRST shot (b10)**, `prepayment credits are depleted`.
Honored the 429 rule: waited 60 s, retried once → identical 429 on b10. **$0 spent, meter
unchanged at $409.64.** Eighth consecutive resume blocked by the same empty-prepayment
state — a hard billing block, not a rate limit. Only Cameron can clear it: top up billing
at https://ai.studio/projects, then re-run the resume command below (resumes free — the 11
passing frames are never re-pulled). Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (7th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date), `--check` PASSES (35 beats,
v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED
on the FIRST shot (b10)**, `prepayment credits are depleted`. Honored the 429 rule: waited
60 s, retried once → identical 429 on b10. **$0 spent, meter unchanged at $409.64.**
Seventh consecutive resume blocked by the same empty-prepayment state — a hard billing
block, not a rate limit. Only Cameron can clear it: top up billing at
https://ai.studio/projects, then re-run the resume command below (resumes free — the 11
passing frames are never re-pulled). Row left State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (6th resume attempt, headless)

Fresh headless resume. Pulled clean (Already up to date), `--check` PASSES (35 beats,
v4 PASS). 11/35 stills intact (assets/ s01-s09, s16, s22). Ran the resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED
on the FIRST shot (b10)**, `prepayment credits are depleted`. Honored the 429 rule: retried
once → identical 429 on b10. **$0 spent, meter unchanged at $409.64.** Sixth consecutive
resume blocked by the same empty-prepayment state — a hard billing block, not a rate limit.
Only Cameron can clear it: top up billing at https://ai.studio/projects, then re-run the
resume command below (resumes free — the 11 passing frames are never re-pulled). Row left
State RUNNING / Claim A-auto.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (5th resume attempt, headless)

Fresh headless resume session. Pulled clean (Already up to date), `--check` PASSES
(35 beats, v4 checklist PASS). 11/35 stills still intact (assets/ s01-s09, s16, s22).
Ran the exact resume command `v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46`
→ **429 RESOURCE_EXHAUSTED on the FIRST shot (b10)** — `prepayment credits are depleted`.
Honored the 429 rule: waited 60 s, retried once → identical 429 on b10. **$0 spent, meter
unchanged at $409.64.** Fifth consecutive resume blocked by the same empty-prepayment state.
A 60 s wait cannot refill an empty balance — this is a hard billing block, not a rate limit.

**ACTION FOR CAMERON (the ONLY thing that unblocks this row):** top up billing at
https://ai.studio/projects (billing). Then re-run the resume command below — it resumes
free (the 11 passing frames are never re-pulled) and the runner finishes the row unattended.

Row left State RUNNING / Claim A-auto for post-top-up resume.

**EXACT RESUME COMMAND (after top-up):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING STILL DEPLETED (4th resume attempt, headless)

Fresh headless resume session. Pulled clean (Already up to date), `--check` PASSES
(35 beats, v4 checklist PASS). 11/35 stills still intact (assets/ s01-s09, s16, s22).
Ran the exact resume command `v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46`
→ **429 RESOURCE_EXHAUSTED on the FIRST shot (b10)** — `prepayment credits are depleted`.
Honored the 429 rule: retried once → identical 429 on b10. **$0 spent, meter unchanged
at $409.64.** The prepayment balance is STILL empty; only Cameron can refill it. This is
now the 4th consecutive resume attempt blocked by the same depleted-prepayment state
(not a transient rate limit — a 60 s wait cannot refill an empty balance).

**ACTION FOR CAMERON:** top up billing at https://ai.studio/projects (billing), then
re-run the resume command below (resumes free — the 11 passing frames are never re-pulled).

Row left State RUNNING / Claim A-auto for post-top-up resume.

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING DEPLETED (3rd resume attempt, headless)

Fresh headless resume session. Pulled clean (Already up to date), `--check` PASSES.
11/35 stills still intact (assets/ s01-s09, s16, s22). Ran the exact resume command
`v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46` → **429 RESOURCE_EXHAUSTED
on the FIRST shot (b10)** — `prepayment credits are depleted`. Honored the 429 rule:
waited 60 s, retried once → identical 429 on b10. **$0 spent, meter unchanged at
$409.64.** The prepayment balance is still empty; only Cameron can refill it.

**ACTION FOR CAMERON:** top up billing at https://ai.studio/projects (billing), then
re-run the resume command below (resumes free — the 11 passing frames are never re-pulled).

Row left State RUNNING / Claim A-auto for post-top-up resume.

---

## RUNNER PARK — 2026-08-06 (A-auto Machine A) — BILLING DEPLETED (2nd resume attempt)

Resumed row 48 per direct instruction (was State RUNNING, Claim A-auto). Portraits
DONE (0 to make). Plates present (courtyard/wedding/workshop/cellar in PLACE-REF).
**11 of 35 stills already generated** (assets/ s01-s09, s16, s22).

**STILL BLOCKED: Gemini prepayment credits DEPLETED — global 429 RESOURCE_EXHAUSTED.**
Same persistent billing block that parked rows 114 and 116 and the first row-48
resume. This session (2026-08-06, headless resume) tried the exact resume command,
got 429 on the FIRST shot (b10), waited 60 s, retried once per the 429 rule — 429
again on b10, identical `prepayment credits are depleted` message. **$0 spent this
session** — meter unchanged at $409.64. This is NOT a transient rate limit; the
prepayment balance is empty and only Cameron can refill it.

**ACTION FOR CAMERON:** top up billing at https://ai.studio/projects (billing).

**EXACT RESUME COMMAND (after top-up — resumes free, the 11 passing frames are
never re-pulled):**
```
cd /home/noremacttevol/Desktop/MBM/media-production-v2
python3 v2_gen_api.py build-48-new-wine-old-bottles --ceiling 439.46
```
Then continue the loop from step 5: light QC the 24 new frames + the 11 existing
(QC the promote-first COURTYARD/WEDDING plate frames hardest), assemble
(`python3 v2_assemble.py 48` — must print AUDIO LOCK PASS), ship two commits,
`firebase deploy --only hosting`, verify the live hash, stash-scan, tick BUILT.
Row left State RUNNING / Claim A-auto for post-top-up resume.
