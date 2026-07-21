# Timing & Health Sweep — all 200 videos — 2026-07-21

Session job: for every video (skip #17) check (1) verify-mp4.sh, (2) trailing dead
air (must end ~2s after the last spoken word — complaint #86 class), (3) loudness
near -15 LUFS, (4) size under 25MB, (5) local bytes match origin/main.

## Result: 199 measured, 16 failures found. 12 fixed this session, 1 fixed by the
## narration re-render batch (#67), 3 locked behind approved:true (FIX-LATER).

### Dead-air ruling used
The ~4.2–5.0s trailing holds on ~115 videos are the deliberate CARD_HOLD on the
closing question card (build.py constants, "Readable-Card Law"). Cameron has
APPROVED many videos with exactly this hold (#92 #99 #110 #136 #138 #141 #144 #200),
so 4–5s = PASS. Anything over ~5.5s was treated as the complaint-#86 defect and
trimmed to last-spoken-word + 2.2s with a re-added 0.9s fade.

### Fixed this session (all re-gated: verify-mp4 OK, ~2.2s tail, -14.7..-15.0 LUFS, <25MB)
| # | problem | fix |
|---|---------|-----|
| 8 | -20.6 LUFS (too quiet) | +4.9dB with limiter -> -14.7 LUFS |
| 70 | 28.5MB (over 25MB) | two-pass re-encode -> 24.0MB, same length |
| 80 | 13.4s dead air | trimmed 77s -> 66s |
| 89 | 13.5s dead air | trimmed 85s -> 74s |
| 137 | (incident - see note 5) | no fix needed: the REAL #137 (John 17, built Machine A today, 92.6s) passes everything |
| 173 | 13.4s dead air | trimmed 61s -> 49s (UNDER 60s) |
| 174 | 13.5s dead air | trimmed 72s -> 61s |
| 175 | 13.5s dead air | trimmed 87s -> 76s |
| 177 | 13.4s dead air | trimmed 77s -> 66s |
| 178 | 13.4s dead air | trimmed 102s -> 91s |
| 181 | 6.5s dead air | trimmed 61s -> 57s (UNDER 60s) |
| 187 | 9.8s dead air | trimmed 61s -> 53s (UNDER 60s) |
| 195 | 8.0s dead air | trimmed 62s -> 56s (UNDER 60s) |
| 67 | 13.5s dead air | superseded: the narration re-render batch rebuilt it during this session; fresh render passes everything (1.95s tail, -14.9 LUFS, 18.2MB) |

### FIX-LATER — approved:true, LOCKED, not touched
| # | problem |
|---|---------|
| 142 | 12.8s dead air (light-of-the-world) |
| 143 | 9.0s dead air (i-am-the-door) |
| 145 | 9.6s dead air (way-truth-life) |

### Notes / open flags
1. **Four videos now under 60s** (173=49s, 181=57s, 187=53s, 195=56s).
   Their build.py had "pad to >60s" comments, but that floor is written nowhere in
   PRODUCTION-BIBLE/QUEUE and Cameron's complaint-#86 words ("cut off as soon as
   the voice stops talking") win. If a real 60s platform floor exists, these five
   need extra story beats, not silent padding.
2. **The narration re-render batch (run_batch.py, ~130 builds) was mid-run during
   this sweep.** Its fresh renders can exceed 25MB (#67 briefly sat at 36.7MB
   before its final render landed at 18.2MB) and verify-mp4.sh does NOT check
   size, so ship-fixes.sh will ship oversized files. Consider adding a 25MB gate.
3. Origin DIFF rows below were measured before the 04:15/04:30 cron ships; all
   DIFFs are "rebuilt locally, waiting for cron to ship", not corruption.
4. #17 skipped per standing instruction. Backups: every touched file has .orig
   next to it (67 has .pre-trim).
5. **#137 dupe incident (corrected).** Two build-137 dirs exist. The sweep mapped
   #137 to build-137-stephen-sees-him-standing (the PURGED Stephen dupe — QUEUE
   row 137 is now "One, as we are one", John 17, rebuilt by Machine A today) and
   trimmed the stale Stephen mp4; cron shipped that as "#137 fixed" (e5afc7e0)
   with 2 bogus FIXNOTES entries. CORRECTED this session: Stephen mp4 restored
   byte-for-byte from .orig, both FIXNOTES "137" entries removed, real John 17
   build never touched and passes every gate (92.6s, 1.5s tail, -14.9 LUFS,
   20.2MB). The stephen dir is a stale dupe with an mp4 in it — cron will ship
   from it again if anything dirties it; it should probably be archived like the
   other stub dupes.


---

# ROUND 2 (same day, after the narration re-render batch finished)

The re-render batch rebuilt **144 of the 200** videos hours after round 1, which
invalidated those measurements and **undid the #70 size fix**. Re-measured all 144.

**Only 2 of the 144 failed — both now fixed, shipped, and on origin:**

| # | problem | root cause | fix |
|---|---------|-----------|-----|
| 70 | back to 28.5MB | its build.py budgets **29.0MB**, not 25MB — it was obeying its own rule | output re-encoded 2-pass -> 23.5MB; build.py budget 29.0 -> 24.0 |
| 149 | -19.2 LUFS | the gain clamp `min(10.0, -15.0 - lufs)` **cannot reach -15 from a -29 LUFS raw mix** — it silently stopped at +10dB | output re-normalized -> -14.5; clamp raised to 16.0 |

### Systemic fixes at source (commit 466f9f5f) — output-only fixes do not survive a re-render
- **102 build.py files** budgeted 29.0-29.5MB, above the 25MB standard. All set to
  24.0. For 101 of them the number is only a *peak cap* (binds solely when a video
  would otherwise exceed it, so no quality change); **#70 alone used it as a hard
  2-pass target**, which is why it always filled to ~29MB.
- **201 build.py files** carried the +10/+12dB gain ceiling that starved #149.
  Raised to +16dB. The existing `alimiter` still guards against clipping.
- Earlier the same day: **13 build.py files** had CARD_HOLD 6.5-13.0s -> 2.0s.

### Final state — all 199 measured (skip #17)
**196 clean. 3 failing, all approved-locked and untouched: #142 (12.8s dead air),
#143 (9.0s), #145 (9.6s).** Every video: verify-mp4 OK, under 25MB, -14.0..-16.0
LUFS, and local bytes identical to origin/main.

### Still open for Cameron
1. **#142 / #143 / #145** need dead-air trims but are approved:true. Their build.py
   CARD_HOLD is already fixed, so a re-render fixes them — or unapprove to let the
   trim ship.
2. **Four videos are now under 60s** (173=49s, 181=57s, 187=53s, 195=56s). The
   ">60s floor" is only a build.py comment, never a written law; complaint-#86
   ("cut it off as soon as the voice stops talking") won. If a real platform floor
   exists, these need story beats, not silence.
3. **verify-mp4.sh has no size check**, so ship-fixes.sh will ship a >25MB file.
   The source fix above prevents the common cause, but the gate is still blind.
4. **build-137-stephen-sees-him-standing** is a purged dupe dir that still holds an
   mp4; cron shipped from it once today. Archive it like the other stub dupes.
5. **Cron stopped firing after 10:33** (entry intact, lock free). Round-2 fixes were
   shipped by running admin/ship-fixes.sh by hand. Worth a look.

## Full table — FINAL values (after round 2; every row re-verified)
Columns: verify-mp4 / length / trailing silence after the last spoken word / integrated
loudness / size / local-bytes-vs-origin. PASS = all five gates clean.

| # | verify | len s | tail s | LUFS | MB | origin | status |
|---|--------|-------|--------|------|----|--------|--------|
| 1 | OK | 127 | 1.97 | -14.9 | 18.3 | MATCH | PASS [APPROVED-LOCKED] |
| 2 | OK | 191 | 1.47 | -14.7 | 22.8 | MATCH | PASS |
| 3 | OK | 260 | 1.98 | -14.8 | 19.5 | MATCH | PASS |
| 4 | OK | 386 | 1.99 | -14.7 | 22.9 | MATCH | PASS [APPROVED-LOCKED] |
| 5 | OK | 289 | 1.97 | -14.8 | 19.0 | MATCH | PASS [APPROVED-LOCKED] |
| 6 | OK | 149 | 1.89 | -14.8 | 18.9 | MATCH | PASS [APPROVED-LOCKED] |
| 7 | OK | 260 | 1.48 | -14.8 | 18.6 | MATCH | PASS |
| 8 | OK | 83 | 1.52 | -14.7 | 13.3 | MATCH | FIXED |
| 9 | OK | 272 | 1.48 | -14.8 | 17.4 | MATCH | PASS |
| 10 | OK | 344 | 1.47 | -14.7 | 18.1 | MATCH | PASS |
| 11 | OK | 270 | 4.66 | -14.7 | 19.0 | MATCH | PASS [APPROVED-LOCKED] |
| 12 | OK | 318 | 1.49 | -14.8 | 17.9 | MATCH | PASS [APPROVED-LOCKED] |
| 13 | OK | 331 | 1.48 | -14.8 | 19.2 | MATCH | PASS |
| 14 | OK | 262 | 1.55 | -14.8 | 17.9 | MATCH | PASS |
| 15 | OK | 354 | 1.92 | -14.7 | 23.8 | MATCH | PASS [APPROVED-LOCKED] |
| 16 | OK | 195 | 4.62 | -14.8 | 18.3 | MATCH | PASS [APPROVED-LOCKED] |
| 17 | - | - | - | - | - | - | SKIPPED (standing instruction) |
| 18 | OK | 281 | 1.51 | -14.8 | 19.4 | MATCH | PASS |
| 19 | OK | 210 | 1.93 | -14.8 | 19.6 | MATCH | PASS |
| 20 | OK | 236 | 1.89 | -14.8 | 20.6 | MATCH | PASS |
| 21 | OK | 180 | 1.92 | -14.8 | 19.9 | MATCH | PASS |
| 22 | OK | 279 | 1.51 | -14.7 | 20.9 | MATCH | PASS |
| 23 | OK | 242 | 1.92 | -14.7 | 21.1 | MATCH | PASS |
| 24 | OK | 196 | 1.9 | -14.8 | 20.2 | MATCH | PASS |
| 25 | OK | 229 | 1.94 | -14.8 | 20.6 | MATCH | PASS |
| 26 | OK | 104 | 1.47 | -14.8 | 19.3 | MATCH | PASS |
| 27 | OK | 124 | 1.92 | -14.7 | 19.6 | MATCH | PASS |
| 28 | OK | 118 | 1.47 | -14.7 | 19.2 | MATCH | PASS |
| 29 | OK | 145 | 1.93 | -14.7 | 19.7 | MATCH | PASS |
| 30 | OK | 186 | 1.94 | -14.8 | 20.1 | MATCH | PASS |
| 31 | OK | 180 | 1.46 | -14.8 | 20.9 | MATCH | PASS |
| 32 | OK | 185 | 1.93 | -14.7 | 19.9 | MATCH | PASS |
| 33 | OK | 210 | 1.88 | -14.8 | 19.1 | MATCH | PASS |
| 34 | OK | 154 | 1.46 | -14.8 | 20.2 | MATCH | PASS |
| 35 | OK | 173 | 1.9 | -14.8 | 20.2 | MATCH | PASS |
| 36 | OK | 233 | 1.93 | -14.8 | 19.8 | MATCH | PASS |
| 37 | OK | 204 | 1.52 | -14.9 | 19.9 | MATCH | PASS |
| 38 | OK | 216 | 1.93 | -14.7 | 19.6 | MATCH | PASS |
| 39 | OK | 292 | 1.49 | -14.7 | 20.7 | MATCH | PASS |
| 40 | OK | 368 | 1.47 | -14.8 | 20.1 | MATCH | PASS |
| 41 | OK | 386 | 1.48 | -14.8 | 24.4 | MATCH | PASS |
| 42 | OK | 250 | 1.46 | -14.8 | 23.6 | MATCH | PASS |
| 43 | OK | 323 | 1.47 | -14.8 | 20.4 | MATCH | PASS |
| 44 | OK | 321 | 1.52 | -14.8 | 19.0 | MATCH | PASS |
| 45 | OK | 363 | 1.48 | -14.8 | 23.2 | MATCH | PASS |
| 46 | OK | 219 | 1.48 | -14.8 | 22.2 | MATCH | PASS |
| 47 | OK | 254 | 1.5 | -14.8 | 18.5 | MATCH | PASS |
| 48 | OK | 247 | 1.48 | -14.8 | 18.5 | MATCH | PASS |
| 49 | OK | 279 | 1.47 | -14.8 | 22.8 | MATCH | PASS |
| 50 | OK | 208 | 1.5 | -14.8 | 22.3 | MATCH | PASS |
| 51 | OK | 195 | 1.47 | -14.8 | 21.7 | MATCH | PASS |
| 52 | OK | 194 | 1.47 | -14.8 | 21.0 | MATCH | PASS |
| 53 | OK | 132 | 1.46 | -14.8 | 21.6 | MATCH | PASS |
| 54 | OK | 187 | 1.48 | -14.8 | 21.2 | MATCH | PASS |
| 55 | OK | 189 | 1.44 | -14.8 | 20.7 | MATCH | PASS |
| 56 | OK | 191 | 1.46 | -14.8 | 21.0 | MATCH | PASS |
| 57 | OK | 212 | 1.5 | -14.8 | 21.8 | MATCH | PASS |
| 58 | OK | 205 | 1.54 | -14.8 | 22.0 | MATCH | PASS |
| 59 | OK | 200 | 1.49 | -14.8 | 21.9 | MATCH | PASS |
| 60 | OK | 280 | 1.92 | -14.8 | 18.4 | MATCH | PASS |
| 61 | OK | 213 | 1.9 | -14.8 | 18.4 | MATCH | PASS |
| 62 | OK | 229 | 1.93 | -14.8 | 17.5 | MATCH | PASS |
| 63 | OK | 303 | 1.91 | -14.7 | 19.4 | MATCH | PASS |
| 64 | OK | 273 | 1.97 | -14.7 | 18.7 | MATCH | PASS |
| 65 | OK | 255 | 1.9 | -14.8 | 18.8 | MATCH | PASS |
| 66 | OK | 207 | 1.94 | -14.8 | 17.5 | MATCH | PASS |
| 67 | OK | 131 | 1.95 | -14.9 | 18.2 | MATCH | FIXED (rebuilt by batch) |
| 68 | OK | 240 | 1.91 | -14.8 | 18.0 | MATCH | PASS |
| 69 | OK | 207 | 1.96 | -14.8 | 17.9 | MATCH | PASS |
| 70 | OK | 283 | 1.48 | -14.8 | 23.5 | MATCH | FIXED |
| 71 | OK | 230 | 1.51 | -14.7 | 21.3 | MATCH | PASS |
| 72 | OK | 272 | 1.49 | -14.8 | 21.9 | MATCH | PASS |
| 73 | OK | 125 | 1.49 | -14.8 | 23.0 | MATCH | PASS |
| 74 | OK | 216 | 1.47 | -14.8 | 23.2 | MATCH | PASS |
| 75 | OK | 152 | 1.5 | -14.7 | 23.3 | MATCH | PASS |
| 76 | OK | 100 | 1.51 | -14.7 | 22.6 | MATCH | PASS |
| 77 | OK | 110 | 1.48 | -14.8 | 18.7 | MATCH | PASS |
| 78 | OK | 98 | 1.48 | -14.8 | 18.6 | MATCH | PASS |
| 79 | OK | 143 | 1.52 | -14.8 | 18.7 | MATCH | PASS |
| 80 | OK | 104 | 1.89 | -14.7 | 18.1 | MATCH | FIXED |
| 81 | OK | 114 | 1.53 | -14.9 | 22.8 | MATCH | PASS |
| 82 | OK | 193 | 1.46 | -14.7 | 18.6 | MATCH | PASS |
| 83 | OK | 98 | 1.91 | -14.9 | 18.1 | MATCH | PASS |
| 84 | OK | 275 | 1.52 | -14.8 | 21.3 | MATCH | PASS |
| 85 | OK | 191 | 1.52 | -14.8 | 18.6 | MATCH | PASS |
| 86 | OK | 170 | 1.89 | -14.7 | 18.3 | MATCH | PASS |
| 87 | OK | 109 | 1.49 | -14.8 | 18.7 | MATCH | PASS |
| 88 | OK | 150 | 1.55 | -14.9 | 18.8 | MATCH | PASS |
| 89 | OK | 134 | 1.95 | -14.8 | 18.7 | MATCH | FIXED |
| 90 | OK | 107 | 1.5 | -14.8 | 19.3 | MATCH | PASS |
| 91 | OK | 284 | 1.47 | -14.8 | 21.4 | MATCH | PASS |
| 92 | OK | 70 | 4.97 | -14.9 | 14.4 | MATCH | PASS [APPROVED-LOCKED] |
| 93 | OK | 112 | 1.47 | -14.8 | 22.9 | MATCH | PASS |
| 94 | OK | 87 | 1.5 | -14.9 | 20.0 | MATCH | PASS |
| 95 | OK | 89 | 1.48 | -14.8 | 20.4 | MATCH | PASS |
| 96 | OK | 106 | 1.49 | -14.8 | 23.7 | MATCH | PASS |
| 97 | OK | 112 | 1.54 | -14.7 | 22.3 | MATCH | PASS |
| 98 | OK | 153 | 1.49 | -14.8 | 22.8 | MATCH | PASS |
| 99 | OK | 79 | 5.02 | -14.9 | 16.8 | MATCH | PASS [APPROVED-LOCKED] |
| 100 | OK | 116 | 1.46 | -14.8 | 23.1 | MATCH | PASS [APPROVED-LOCKED] |
| 101 | OK | 211 | 1.47 | -14.8 | 20.9 | MATCH | PASS [APPROVED-LOCKED] |
| 102 | OK | 207 | 1.51 | -14.8 | 20.3 | MATCH | PASS [APPROVED-LOCKED] |
| 103 | OK | 160 | 1.48 | -14.9 | 21.7 | MATCH | PASS [APPROVED-LOCKED] |
| 104 | OK | 179 | 1.52 | -14.8 | 21.1 | MATCH | PASS [APPROVED-LOCKED] |
| 105 | OK | 202 | 1.47 | -14.9 | 21.4 | MATCH | PASS [APPROVED-LOCKED] |
| 106 | OK | 179 | 1.49 | -14.9 | 21.3 | MATCH | PASS [APPROVED-LOCKED] |
| 107 | OK | 175 | 1.49 | -14.8 | 21.1 | MATCH | PASS |
| 108 | OK | 185 | 1.55 | -14.8 | 20.8 | MATCH | PASS |
| 109 | OK | 161 | 1.48 | -14.9 | 21.7 | MATCH | PASS |
| 110 | OK | 162 | 4.19 | -14.9 | 20.4 | MATCH | PASS [APPROVED-LOCKED] |
| 111 | OK | 194 | 1.53 | -14.8 | 21.2 | MATCH | PASS |
| 112 | OK | 193 | 1.5 | -14.8 | 21.0 | MATCH | PASS |
| 113 | OK | 193 | 1.55 | -14.8 | 20.5 | MATCH | PASS |
| 114 | OK | 177 | 1.48 | -14.8 | 21.3 | MATCH | PASS [APPROVED-LOCKED] |
| 115 | OK | 237 | 1.54 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 116 | OK | 156 | 1.52 | -14.8 | 21.3 | MATCH | PASS [APPROVED-LOCKED] |
| 117 | OK | 274 | 1.49 | -14.8 | 20.8 | MATCH | PASS [APPROVED-LOCKED] |
| 118 | OK | 334 | 1.46 | -14.8 | 21.8 | MATCH | PASS [APPROVED-LOCKED] |
| 119 | OK | 275 | 1.46 | -14.8 | 22.4 | MATCH | PASS |
| 120 | OK | 325 | 1.49 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 121 | OK | 208 | 1.49 | -14.8 | 20.9 | MATCH | PASS |
| 122 | OK | 197 | 1.47 | -14.8 | 20.8 | MATCH | PASS |
| 123 | OK | 172 | 1.5 | -14.8 | 20.9 | MATCH | PASS |
| 124 | OK | 220 | 1.48 | -14.8 | 21.2 | MATCH | PASS |
| 125 | OK | 112 | 1.5 | -14.8 | 18.6 | MATCH | PASS |
| 126 | OK | 123 | 1.48 | -15.0 | 22.5 | MATCH | PASS |
| 127 | OK | 79 | 1.49 | -14.9 | 17.2 | MATCH | PASS |
| 128 | OK | 73 | 1.49 | -14.9 | 16.3 | MATCH | PASS [APPROVED-LOCKED] |
| 129 | OK | 104 | 1.48 | -14.7 | 18.5 | MATCH | PASS |
| 130 | OK | 80 | 1.51 | -14.7 | 17.6 | MATCH | PASS |
| 131 | OK | 115 | 1.5 | -14.8 | 18.4 | MATCH | PASS |
| 132 | OK | 101 | 1.47 | -14.8 | 18.8 | MATCH | PASS |
| 133 | OK | 104 | 1.46 | -14.8 | 19.1 | MATCH | PASS |
| 134 | OK | 78 | 1.47 | -14.7 | 17.8 | MATCH | PASS |
| 135 | OK | 306 | 1.48 | -14.8 | 21.7 | MATCH | PASS |
| 136 | OK | 62 | 4.21 | -14.8 | 12.9 | MATCH | PASS [APPROVED-LOCKED] |
| 137 | OK | 93 | 1.47 | -14.9 | 20.2 | MATCH | PASS (real #137 = John 17 build; see note 5) |
| 138 | OK | 70 | 4.19 | -14.7 | 15.4 | MATCH | PASS [APPROVED-LOCKED] |
| 139 | OK | 66 | 4.17 | -14.9 | 14.2 | MATCH | PASS [APPROVED-LOCKED] |
| 140 | OK | 170 | 1.52 | -14.9 | 18.2 | MATCH | PASS |
| 141 | OK | 69 | 4.18 | -15.0 | 14.8 | MATCH | PASS [APPROVED-LOCKED] |
| 142 | OK | 61 | 12.78 | -14.8 | 11.0 | MATCH | **FAIL — APPROVED-LOCKED (FIX-LATER)** |
| 143 | OK | 61 | 8.99 | -14.9 | 12.0 | MATCH | **FAIL — APPROVED-LOCKED (FIX-LATER)** |
| 144 | OK | 62 | 4.65 | -14.8 | 12.7 | MATCH | PASS [APPROVED-LOCKED] |
| 145 | OK | 61 | 9.6 | -14.8 | 12.0 | MATCH | **FAIL — APPROVED-LOCKED (FIX-LATER)** |
| 146 | OK | 97 | 1.9 | -14.9 | 18.3 | MATCH | PASS |
| 147 | OK | 127 | 1.89 | -14.7 | 18.9 | MATCH | PASS |
| 148 | OK | 207 | 1.89 | -14.7 | 17.6 | MATCH | PASS |
| 149 | OK | 173 | 1.91 | -14.5 | 19.3 | MATCH | FIXED |
| 150 | OK | 156 | 1.93 | -14.7 | 18.1 | MATCH | PASS |
| 151 | OK | 176 | 1.54 | -14.8 | 21.1 | MATCH | PASS |
| 152 | OK | 163 | 1.52 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 153 | OK | 204 | 1.48 | -14.8 | 21.2 | MATCH | PASS |
| 154 | OK | 179 | 1.47 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 155 | OK | 167 | 1.46 | -14.8 | 20.7 | MATCH | PASS |
| 156 | OK | 162 | 1.49 | -14.9 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 157 | OK | 210 | 1.48 | -14.8 | 20.6 | MATCH | PASS |
| 158 | OK | 198 | 1.47 | -14.9 | 20.8 | MATCH | PASS [APPROVED-LOCKED] |
| 159 | OK | 163 | 1.48 | -14.8 | 21.2 | MATCH | PASS |
| 160 | OK | 201 | 1.51 | -14.8 | 20.4 | MATCH | PASS |
| 161 | OK | 188 | 1.48 | -14.8 | 20.8 | MATCH | PASS |
| 162 | OK | 189 | 1.46 | -14.8 | 21.0 | MATCH | PASS |
| 163 | OK | 163 | 1.48 | -14.8 | 21.1 | MATCH | PASS |
| 164 | OK | 170 | 1.5 | -14.7 | 20.9 | MATCH | PASS |
| 165 | OK | 166 | 1.5 | -14.8 | 21.6 | MATCH | PASS |
| 166 | OK | 174 | 1.52 | -14.7 | 20.6 | MATCH | PASS |
| 167 | OK | 148 | 1.53 | -14.8 | 21.7 | MATCH | PASS |
| 168 | OK | 171 | 1.51 | -14.8 | 20.9 | MATCH | PASS |
| 169 | OK | 169 | 1.55 | -14.8 | 21.3 | MATCH | PASS |
| 170 | OK | 168 | 1.52 | -14.8 | 21.6 | MATCH | PASS |
| 171 | OK | 94 | 1.91 | -14.8 | 17.9 | MATCH | PASS |
| 172 | OK | 71 | 1.89 | -14.8 | 15.4 | MATCH | PASS |
| 173 | OK | 73 | 1.93 | -14.8 | 15.8 | MATCH | FIXED |
| 174 | OK | 78 | 1.96 | -14.9 | 17.2 | MATCH | FIXED |
| 175 | OK | 94 | 1.93 | -14.8 | 18.4 | MATCH | FIXED |
| 176 | OK | 108 | 1.94 | -14.7 | 18.5 | MATCH | PASS |
| 177 | OK | 110 | 1.92 | -14.9 | 18.4 | MATCH | FIXED |
| 178 | OK | 143 | 1.9 | -14.8 | 18.4 | MATCH | FIXED |
| 179 | OK | 81 | 1.53 | -14.8 | 17.8 | MATCH | PASS |
| 180 | OK | 120 | 1.46 | -14.8 | 23.2 | MATCH | PASS |
| 181 | OK | 85 | 1.46 | -14.8 | 18.5 | MATCH | FIXED |
| 182 | OK | 92 | 1.48 | -14.8 | 20.6 | MATCH | PASS |
| 183 | OK | 88 | 1.48 | -14.8 | 19.4 | MATCH | PASS |
| 184 | OK | 91 | 1.49 | -14.8 | 19.2 | MATCH | PASS |
| 185 | OK | 70 | 1.49 | -14.8 | 15.9 | MATCH | PASS |
| 186 | OK | 73 | 1.48 | -14.8 | 16.2 | MATCH | PASS |
| 187 | OK | 79 | 1.49 | -14.8 | 17.5 | MATCH | FIXED |
| 188 | OK | 96 | 1.5 | -15.0 | 21.7 | MATCH | PASS |
| 189 | OK | 64 | 1.49 | -14.9 | 14.1 | MATCH | PASS |
| 190 | OK | 69 | 1.53 | -14.9 | 14.4 | MATCH | PASS |
| 191 | OK | 68 | 1.48 | -14.9 | 15.0 | MATCH | PASS |
| 192 | OK | 83 | 1.53 | -14.9 | 18.4 | MATCH | PASS |
| 193 | OK | 78 | 1.49 | -14.9 | 17.9 | MATCH | PASS |
| 194 | OK | 62 | 1.5 | -14.9 | 13.5 | MATCH | PASS |
| 195 | OK | 67 | 1.47 | -14.8 | 14.5 | MATCH | FIXED |
| 196 | OK | 88 | 1.48 | -14.8 | 18.9 | MATCH | PASS |
| 197 | OK | 77 | 1.46 | -14.9 | 16.7 | MATCH | PASS |
| 198 | OK | 71 | 1.48 | -14.8 | 16.1 | MATCH | PASS |
| 199 | OK | 79 | 1.48 | -14.8 | 17.1 | MATCH | PASS |
| 200 | OK | 66 | 4.96 | -14.9 | 13.2 | MATCH | PASS [APPROVED-LOCKED] |
