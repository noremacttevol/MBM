## 2026-08-13 (Opus runner, unattended/headless) — Row 146 VINE & BRANCHES C-FIX#2: REPEAT complaint, prior fix's "14/14 PASS" was FALSE — Machine A `Dev`, ~$0.67 Gemini

Complaint-first + low-number: row 146 was the lowest waiting row with an OPEN complaint. Cameron, against the LIVE C-FIX#1 cut (commit d4b437a00): *"0:47 man has multiple arms / 0:40 some bystanders have white faces / 1:19 Jesus missing a hand… all three problems are still there you fixed nothing and wasted my time and credits."* He was right — I extracted every frame from the live mp4 and confirmed all three defects survived; C-FIX#1's "14/14 PASS, verified in the rendered mp4" was never actually checked against the render (the row-11 failure class).

- **TRACE (live mp4, not beat names):** 0:40 → b04 (back-row faces still cool/ashen in moonlight); 0:47 → b09 (three hands STACKED + over-long forearm = "extra arm"); 1:19 → b14 (Jesus behind the trunk, forearm-tangle hid a hand) and the 79.0s fade-to-black (brightness 6.9) into the card.
- **AUTOPSY:** b04 = **IGNORED** (skin-tone words maxed but no warm fill → back faces drained) → added in-frame oil-lamp warm fill + shallow ring + PHOTOREAL clause. b09 = **ALLOWED** ("2–3 hands on one branch" invited stacking) → EXACTLY 3 hands, one per man, clear GAPS, no overlap. b14 = **ALLOWED** ("against the trunk" occluded a hand) → Jesus CLEAR of trunk, both hands cupping the disciple's hand, five fingers each, bright.
- **5 rerolls** (b04×2 — first drifted painterly; b09×1; b14×2 — first left 2nd hand at side), all mandatory complaint-fixes, ≤2/frame, ~**$0.67**, meter $639.85→$641.99. 11 beats reused untouched. **Audio byte-identical** — AUDIO REBUILD PASS SHA256 `ae063a39`, nothing re-voiced.
- **FULL-CUT GATE — re-verified in the NEW rendered mp4 (what C-FIX#1 skipped):** 14/14 beats extracted at mid-window + 3 caption/card frames viewed. 0:40 warm lamplit ring, no white faces, photoreal; 0:47 three separated hands; 1:16 Jesus clear of trunk, both hands, lit. Jesus locked face + cream-only + no halo (b01/b02/b07/b10), green-cut vs withered pair, captions bottom-band (RED Jesus KJV/WHITE narrator), card clean. **14/14 + card PASS.**
- **Ship:** commit `38f237b16787` (mp4 force-added, QC.md #2 entry, beats_v2 hardened prompts, s04/s09/s14, AUTHOR-BOARD SHIPPED, QUEUE). Reviewer card repointed (data-hash `38f237b16787…`, ?v=38f237b16787, flag admits the prior false-pass and answers each complaint in Cameron's words) + SESSION-LOG. **Deployed to Firebase + LIVE-VERIFIED.** Appr stays ⬜ (Cameron's alone). RUNNER-LESSONS: warm crowds need a practical fill light; hands-on-one-branch need explicit N + gaps; never put Jesus behind a trunk for a clasp; cozy-lamp scenes drift painterly without a photoreal clause; **META — never claim FULL-CUT PASS without looking at the RENDERED frame.**

Commit: 38f237b1678723f530afaa343f251d4451c976f4 (ship) / 19189bb1b (card+log)

---

## 2026-08-13 (Opus runner, unattended/headless) — Row 140 THE BRONZE SERPENT V2 FIRST CUT SHIPPED: b17 MOSES-lock cleared, Naaman-dupe complaint RESOLVED by story replacement — Machine A `Dev`, ~$0.26 Gemini

Ran AUTHOR-BOARD row 140 (lowest Ready ✅, complaint-first). Cross-checked QUEUE.md FIRST: the row was legitimately REPLACED by Cameron (Naaman → Bronze Serpent, approved 2026-08-13, old build archived) — building it IS the resolution to his story-dupe complaint, not an unauthorized swap. Resumed the author's park: the author had built 24 stills (23 PASS) and cleared the b17 identity block by adding `"MOSES"` to b17 `locks`.

- **b17 regen ($0.13):** `--only b17 --redo` → gen log `[+1 char ref: MOSES]` now attaches → hero frame renders the OLD white-bearded canonical Moses (matches every other beat). Pole stayed byte-consistent via the SERPENT-POLE plate; young-Moses did NOT bleed through, so no plate re-promote.
- **Assembly gap the author left, fixed by runner:** new-story row has no rendered V1 mp4, so `v2_assemble` needs `AUDIO_FROM_V1_SEGMENTS = True` (its own FIX message says so) + `OUTPUT_VIDEO_NAME`. Set both (module-level assembly config, established production-lane action — cf. rows 44/155/156). Also `git mv` the archived `build-140-naaman-washes/beats_v2.py` → `.RETIRED.py` (untracked locally) so the row resolver finds exactly one build. Audio REBUILT from 15 V1 segment mp3s, 139.4s, hash `90d6b582`.
- **1 reroll (b21, 4.2% ≤15% budget):** the ~7.6s dying-man close-up had vivid blue eyes → rerolled to a muted grey-hazel man reaching toward the distant pole (reads "a dying man" better). ~$0.26 total; 23 banked frames untouched (touch-once/COST LAW).
- **FULL-CUT GATE 24/24 + card PASS** (per-rendered-frame): Moses identity consistent, no Jesus/cream (OT era), realistic-only, snakes-no-gore, dignified death shroud, period blacksmith, hands/scale/anatomy correct, captions bottom-band 4-voice, question card clean. FIX-WAVE (non-blocking): s06 bg speck, s24 faint vision-crowd overlay.
- **Reviewer cleanup:** row 140 had TWO stale duplicate `id="v140"` cards (Naaman + Road-Runs-Both-Ways, both Prodigal-Son dupes — the exact complaint). Converted one to The Bronze Serpent (hash `f5ce6766`, `data-review-wave="realistic-v2"`, flag answers the complaint in Cameron's words) and DELETED the duplicate so the reviewer serves exactly one, correct card.
- **Ship:** commit `f5ce6766` (mp4 force-added, QC.md, beats_v2, s17/s21, boards, QUEUE); reviewer card + SESSION-LOG `2784a482c`. **Deployed to Firebase (`milk-b4-meat`) + LIVE-VERIFIED:** live review.html carries `data-hash="f5ce6766a8d7dcc44ff0a989e4d507579f636458"` and the mp4 returns HTTP 200, content-length 21,077,336. RUNNER-LESSONS + STASH-INDEX (3740 stills) fed; publish_ledger synced. Appr stays ⬜ (Cameron's alone).

Commit: f5ce6766a8d7dcc44ff0a989e4d507579f636458 (ship) / 2784a482c (card+log)



**Commit:** `dd088a574`

Dispatched as the cfix lane on row 117 (lowest open complaint). Complaint is AUDIO-domain — Cameron: *"it was all good until the very end where you miss pronounced 'Dramatized' — fix that audio at the very end."* Per the audio-domain rail I did NOT re-cut pictures. But this is the SECOND pass: a RUNNER PARK already diagnosed it and an "AUDIO-FIX SHIPPED" (07:34, commit `33b7d3ba1`) claimed to fix it — Cameron re-filed the identical complaint 22 min later (07:56 UTC) against that exact hash. Re-parking the same way = the loop he hates, so I root-caused instead.

- **The 07:34 "fix" was a NULL RE-ROLL — git-proven.** Commit `33b7d3ba1` touched no `.py`; `SPOKEN` is still `{}`. It re-rendered the identical plain word "dramatized" (new md5, same pronunciation) and claimed a stress change without applying a respell or validating. A/B: pre-fix vs post-fix card word envelopes are near-identical. (Its board note's "mp4 SHA256 358dd0f3" is also wrong; real is `dd0e4fb2`.)
- **The shipped word is OBJECTIVELY CORRECT — three independent measures.** Round-trips to "dramatized"; F0 thirds `[158,119,106]` = front-stress (DRAM, not druh-MAT); first-syllable formants F1=599/F2=1650 = canonical /æ/. Live serve == local (`dd0e4fb2`), so Cameron heard exactly this.
- **Rendered 11 ElevenLabs-Brian alternatives — EVERY one is worse** (over-segments, shifts stress off S1, moves the vowel off /æ/, or changes the word to "dramatizes"/"dramatize"). ElevenLabs cannot voice it better; any re-voice is a regression; a blind re-roll = the row-27 8-pass "ear-blocked" trap (RUNNER-LESSONS:27).
- **Resolution: genuine fork, only Cameron can decide.** Parked row State `BUILT → AWAITING-CAMERON` (matches no autopilot picker, so no lane re-dispatches and burns sessions) and escalated to Cameron's Brain inbox with three options: (a) approve as-is, (b) describe what he hears for a targeted attempt, (c) authorize an AUTHOR reword of the deliberate climax word (not done autonomously). Full evidence in the build's QC.md §C-FIX INVESTIGATION 2026-08-13.

**COST:** $0 Gemini, 0 rerolls, pictures untouched. ElevenLabs used only for throwaway A/B candidates. Video stays on the reviewer (still watchable); only the auto-fix loop is stopped.

## 2026-08-13 (AUDIO-FIX lane, unattended/headless) — Rows 155 / 156 / 157 STALE-V1 cleared, all handed to picture runner AUTHORED — Machine A `Dev`, $0

**Commit:** `4f95704b9` (row 157 done→AUTHORED); rows 155/156 shipped in `2d77f05c5` / `fcc8a99ca`; this log entry follows.

THE LOW-NUMBER LAW ran the audio lane down every remaining NEEDS-AUDIO row, lowest first. All three were the SAME class — STALE-V1: the V1 mp4 (old-voice or stale-longer) predates the build's own re-recorded ElevenLabs mp3s, so `v2_assemble`'s AUDIO LOCK / STALE-V1-FINAL guard refused the packet-copy. None had any V2 stills, so per PROMPT-AUDIO-FIX step 5 the deliverable was a $0 hand-off to the picture runner, not a shipped cut.

- **Row 155 falling-away (row-147 class):** voice-ID'd all 11 V1-dir mp3s = 44100/128k ElevenLabs new-voice (audio-eleven.log confirms all 11 cast). Set `AUDIO_FROM_V1_SEGMENTS = True`. Timeline reads 123.1s clean; assemble now clears the audio lock and stops only at missing stills.
- **Row 156 famine-of-hearing (row-147 class):** all 11 mp3s ElevenLabs new-voice (incl. kv11/kv12 [god]); flag set; timeline 122.6s clean. The log's "undecided homograph 'does'" notes are pre-existing render notes, NOT a Cameron complaint — left untouched.
- **Row 157 marvellous-work (row-141 class, BOTH tripwires):** V1 mp4 stale-longer (209.8s vs ~159-174s current timeline = carrying deleted segments) AND all 13 mp3s newer. All 13 ElevenLabs new-voice; flag set so the rebuild uses the mp3s and never touches the stale mp4; timeline 159.3s / 28 phrases clean.

**COST:** $0 total — no Gemini, no ElevenLabs (STALE-V1 is a pure re-point to the build's existing new-voice mp3s; no segment re-voiced). V1 dirs read-only throughout. Each row: board State NEEDS-AUDIO → AUTHORED, Ready ✅, Claim cleared; QC.md carries old→fix note. The picture runner picks all three up (complaint-first/low-number) and builds the stills on the fixed new-voice audio.

---

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

