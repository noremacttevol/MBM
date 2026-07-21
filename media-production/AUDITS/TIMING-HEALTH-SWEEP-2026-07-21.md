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

## Full table (values at sweep time; fixed videos show their FIXED values)
| # | verify | len s | tail s | LUFS | MB | origin | status |
|---|--------|-------|--------|------|----|--------|--------|
| 1 | OK | 127 | 1.97 | -14.9 | 18.3 | MATCH | PASS [APPROVED-LOCKED] |
| 2 | OK | 191 | 1.47 | -14.7 | 22.9 | MATCH | PASS |
| 3 | OK | 260 | 1.97 | -14.8 | 19.4 | MATCH | PASS |
| 4 | OK | 386 | 1.99 | -14.7 | 22.9 | MATCH | PASS [APPROVED-LOCKED] |
| 5 | OK | 289 | 1.97 | -14.8 | 19.0 | MATCH | PASS [APPROVED-LOCKED] |
| 6 | OK | 149 | 1.89 | -14.8 | 18.9 | MATCH | PASS [APPROVED-LOCKED] |
| 7 | OK | 260 | 1.48 | -14.8 | 18.6 | MATCH | PASS |
| 8 | OK | 83 | 1.52 | -14.7 | 13.3 | MATCH | FIXED |
| 9 | OK | 272 | 1.47 | -14.8 | 15.2 | DIFF | PASS |
| 10 | OK | 344 | 1.49 | -14.8 | 18.8 | DIFF | PASS |
| 11 | OK | 270 | 4.66 | -14.7 | 19.0 | MATCH | PASS [APPROVED-LOCKED] |
| 12 | OK | 318 | 1.49 | -14.8 | 17.9 | MATCH | PASS [APPROVED-LOCKED] |
| 13 | OK | 334 | 1.07 | -14.8 | 19.6 | MATCH | PASS |
| 14 | OK | 262 | 1.55 | -14.8 | 18.0 | DIFF | PASS |
| 15 | OK | 354 | 1.92 | -14.7 | 23.8 | MATCH | PASS [APPROVED-LOCKED] |
| 16 | OK | 195 | 4.62 | -14.8 | 18.3 | MATCH | PASS [APPROVED-LOCKED] |
| 17 | - | - | - | - | - | - | SKIPPED (standing instruction) |
| 18 | OK | 281 | 1.48 | -14.8 | 19.6 | DIFF | PASS |
| 19 | OK | 218 | 1.97 | -14.8 | 19.6 | MATCH | PASS |
| 20 | OK | 202 | 4.64 | -14.8 | 20.1 | MATCH | PASS |
| 21 | OK | 167 | 4.67 | -14.8 | 19.4 | MATCH | PASS |
| 22 | OK | 245 | 2.46 | -14.7 | 20.3 | MATCH | PASS |
| 23 | OK | 203 | 4.64 | -14.8 | 20.2 | MATCH | PASS |
| 24 | OK | 176 | 4.63 | -14.8 | 19.6 | MATCH | PASS |
| 25 | OK | 196 | 4.66 | -14.8 | 19.9 | MATCH | PASS |
| 26 | OK | 103 | 1.73 | -14.8 | 19.3 | MATCH | PASS |
| 27 | OK | 125 | 4.63 | -14.8 | 18.9 | MATCH | PASS |
| 28 | OK | 117 | 1.7 | -14.8 | 19.1 | MATCH | PASS |
| 29 | OK | 152 | 4.67 | -14.7 | 19.3 | MATCH | PASS |
| 30 | OK | 182 | 4.68 | -14.8 | 19.4 | MATCH | PASS |
| 31 | OK | 148 | 1.77 | -14.7 | 20.4 | MATCH | PASS |
| 32 | OK | 165 | 4.65 | -14.8 | 19.4 | MATCH | PASS |
| 33 | OK | 182 | 4.67 | -14.8 | 18.8 | MATCH | PASS |
| 34 | OK | 132 | 1.68 | -14.8 | 19.9 | MATCH | PASS |
| 35 | OK | 155 | 4.64 | -14.8 | 19.3 | MATCH | PASS |
| 36 | OK | 190 | 4.64 | -14.8 | 19.0 | MATCH | PASS |
| 37 | OK | 166 | 1.33 | -14.8 | 19.6 | MATCH | PASS |
| 38 | OK | 158 | 4.66 | -14.7 | 18.9 | MATCH | PASS |
| 39 | OK | 273 | 4.16 | -14.8 | 20.3 | MATCH | PASS |
| 40 | OK | 356 | 4.17 | -14.8 | 19.7 | MATCH | PASS |
| 41 | OK | 377 | 4.17 | -14.8 | 24.0 | MATCH | PASS |
| 42 | OK | 256 | 4.17 | -14.8 | 23.1 | MATCH | PASS |
| 43 | OK | 285 | 4.17 | -14.8 | 19.6 | MATCH | PASS |
| 44 | OK | 258 | 4.18 | -14.8 | 18.2 | MATCH | PASS |
| 45 | OK | 326 | 4.16 | -14.8 | 22.5 | MATCH | PASS |
| 46 | OK | 228 | 4.19 | -14.8 | 21.8 | MATCH | PASS |
| 47 | OK | 236 | 4.16 | -14.8 | 17.8 | MATCH | PASS |
| 48 | OK | 231 | 4.16 | -14.8 | 17.8 | MATCH | PASS |
| 49 | OK | 243 | 4.16 | -14.7 | 21.6 | MATCH | PASS |
| 50 | OK | 172 | 4.22 | -14.7 | 21.7 | MATCH | PASS |
| 51 | OK | 165 | 4.18 | -14.8 | 20.5 | MATCH | PASS |
| 52 | OK | 156 | 4.18 | -14.7 | 20.0 | MATCH | PASS |
| 53 | OK | 125 | 4.18 | -14.8 | 20.4 | MATCH | PASS |
| 54 | OK | 149 | 4.2 | -14.7 | 20.1 | MATCH | PASS |
| 55 | OK | 161 | 4.09 | -14.8 | 19.7 | MATCH | PASS |
| 56 | OK | 151 | 4.16 | -14.7 | 19.4 | MATCH | PASS |
| 57 | OK | 149 | 4.16 | -14.8 | 20.1 | MATCH | PASS |
| 58 | OK | 162 | 4.19 | -14.8 | 20.1 | MATCH | PASS |
| 59 | OK | 157 | 4.19 | -14.7 | 20.2 | MATCH | PASS |
| 60 | OK | 237 | 4.62 | -14.8 | 17.3 | MATCH | PASS |
| 61 | OK | 195 | 4.59 | -14.9 | 17.9 | MATCH | PASS |
| 62 | OK | 204 | 4.65 | -14.8 | 16.9 | MATCH | PASS |
| 63 | OK | 241 | 4.63 | -14.8 | 17.9 | MATCH | PASS |
| 64 | OK | 215 | 4.62 | -14.8 | 17.2 | MATCH | PASS |
| 65 | OK | 214 | 4.6 | -14.8 | 17.5 | MATCH | PASS |
| 66 | OK | 195 | 4.67 | -14.8 | 17.0 | MATCH | PASS |
| 67 | OK | 131 | 1.95 | -14.9 | 18.2 | DIFF | FIXED (rebuilt by batch) |
| 68 | OK | 197 | 4.68 | -14.8 | 17.0 | MATCH | PASS |
| 69 | OK | 200 | 4.62 | -14.8 | 17.4 | MATCH | PASS |
| 70 | OK | 235 | 5.0 | -14.9 | 24.0 | DIFF | FIXED |
| 71 | OK | 222 | 4.2 | -14.7 | 20.6 | MATCH | PASS |
| 72 | OK | 249 | 4.18 | -14.8 | 21.2 | MATCH | PASS |
| 73 | OK | 78 | 4.97 | -14.9 | 16.6 | MATCH | PASS |
| 74 | OK | 128 | 4.98 | -14.8 | 22.4 | MATCH | PASS |
| 75 | OK | 91 | 4.98 | -14.8 | 19.8 | MATCH | PASS |
| 76 | OK | 80 | 4.99 | -14.8 | 17.1 | MATCH | PASS |
| 77 | OK | 70 | 4.18 | -14.8 | 15.1 | MATCH | PASS |
| 78 | OK | 71 | 4.21 | -14.8 | 15.0 | MATCH | PASS |
| 79 | OK | 78 | 4.18 | -14.9 | 16.3 | MATCH | PASS |
| 80 | OK | 66 | 2.21 | -14.8 | 12.0 | DIFF | FIXED |
| 81 | OK | 81 | 4.99 | -14.9 | 16.8 | MATCH | PASS |
| 82 | OK | 105 | 4.19 | -14.9 | 18.6 | MATCH | PASS |
| 83 | OK | 65 | 2.39 | -14.8 | 13.4 | MATCH | PASS |
| 84 | OK | 260 | 4.2 | -14.8 | 20.8 | MATCH | PASS |
| 85 | OK | 112 | 4.2 | -14.9 | 17.8 | MATCH | PASS |
| 86 | OK | 82 | 2.41 | -14.8 | 17.8 | MATCH | PASS |
| 87 | OK | 66 | 4.22 | -14.8 | 13.5 | MATCH | PASS |
| 88 | OK | 78 | 4.19 | -14.9 | 16.4 | MATCH | PASS |
| 89 | OK | 74 | 2.22 | -14.8 | 13.7 | DIFF | FIXED |
| 90 | OK | 76 | 4.21 | -14.8 | 16.7 | MATCH | PASS |
| 91 | OK | 294 | 4.18 | -14.8 | 21.2 | MATCH | PASS |
| 92 | OK | 70 | 4.97 | -14.9 | 14.4 | MATCH | PASS [APPROVED-LOCKED] |
| 93 | OK | 73 | 4.98 | -14.8 | 14.8 | MATCH | PASS |
| 94 | OK | 62 | 4.98 | -14.9 | 12.6 | MATCH | PASS |
| 95 | OK | 65 | 4.98 | -14.9 | 13.5 | MATCH | PASS |
| 96 | OK | 68 | 4.98 | -14.8 | 14.0 | MATCH | PASS |
| 97 | OK | 67 | 4.98 | -14.8 | 13.0 | MATCH | PASS |
| 98 | OK | 61 | 5.0 | -14.8 | 12.4 | MATCH | PASS |
| 99 | OK | 79 | 5.02 | -14.9 | 16.8 | MATCH | PASS [APPROVED-LOCKED] |
| 100 | OK | 116 | 1.46 | -14.8 | 23.1 | MATCH | PASS [APPROVED-LOCKED] |
| 101 | OK | 211 | 1.47 | -14.8 | 20.9 | MATCH | PASS [APPROVED-LOCKED] |
| 102 | OK | 207 | 1.51 | -14.8 | 20.3 | MATCH | PASS [APPROVED-LOCKED] |
| 103 | OK | 160 | 1.48 | -14.9 | 21.7 | MATCH | PASS [APPROVED-LOCKED] |
| 104 | OK | 179 | 1.52 | -14.8 | 21.1 | MATCH | PASS [APPROVED-LOCKED] |
| 105 | OK | 202 | 1.47 | -14.9 | 21.4 | MATCH | PASS [APPROVED-LOCKED] |
| 106 | OK | 179 | 1.49 | -14.9 | 21.3 | MATCH | PASS [APPROVED-LOCKED] |
| 107 | OK | 175 | 1.49 | -14.8 | 20.9 | MATCH | PASS |
| 108 | OK | 185 | 1.55 | -14.8 | 20.7 | MATCH | PASS |
| 109 | OK | 155 | 4.19 | -14.9 | 21.0 | MATCH | PASS |
| 110 | OK | 162 | 4.19 | -14.9 | 20.4 | MATCH | PASS [APPROVED-LOCKED] |
| 111 | OK | 167 | 4.18 | -14.8 | 20.5 | MATCH | PASS |
| 112 | OK | 171 | 4.17 | -14.9 | 20.4 | MATCH | PASS |
| 113 | OK | 193 | 1.55 | -14.8 | 20.5 | MATCH | PASS |
| 114 | OK | 177 | 1.48 | -14.8 | 21.3 | MATCH | PASS [APPROVED-LOCKED] |
| 115 | OK | 237 | 1.54 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 116 | OK | 156 | 1.52 | -14.8 | 21.3 | MATCH | PASS [APPROVED-LOCKED] |
| 117 | OK | 274 | 1.49 | -14.8 | 20.8 | MATCH | PASS [APPROVED-LOCKED] |
| 118 | OK | 334 | 1.46 | -14.8 | 21.8 | MATCH | PASS [APPROVED-LOCKED] |
| 119 | OK | 276 | 1.51 | -14.8 | 22.3 | MATCH | PASS |
| 120 | OK | 325 | 1.49 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 121 | OK | 217 | 4.21 | -14.8 | 20.5 | MATCH | PASS |
| 122 | OK | 150 | 4.23 | -14.8 | 20.1 | MATCH | PASS |
| 123 | OK | 156 | 4.18 | -14.7 | 20.5 | MATCH | PASS |
| 124 | OK | 201 | 4.18 | -14.8 | 20.5 | MATCH | PASS |
| 125 | OK | 79 | 4.23 | -14.8 | 17.0 | MATCH | PASS |
| 126 | OK | 74 | 4.97 | -15.0 | 14.5 | MATCH | PASS |
| 127 | OK | 69 | 4.18 | -14.9 | 14.2 | MATCH | PASS |
| 128 | OK | 73 | 1.49 | -14.9 | 16.3 | MATCH | PASS [APPROVED-LOCKED] |
| 129 | OK | 63 | 4.19 | -14.7 | 12.8 | MATCH | PASS |
| 130 | OK | 64 | 4.21 | -14.8 | 12.8 | MATCH | PASS |
| 131 | OK | 61 | 4.19 | -14.8 | 12.3 | MATCH | PASS |
| 132 | OK | 69 | 4.17 | -14.8 | 14.5 | MATCH | PASS |
| 133 | OK | 70 | 4.17 | -14.8 | 14.9 | MATCH | PASS |
| 134 | OK | 63 | 4.17 | -14.8 | 13.1 | MATCH | PASS |
| 135 | OK | 306 | 1.48 | -14.8 | 21.7 | MATCH | PASS |
| 136 | OK | 62 | 4.21 | -14.8 | 12.9 | MATCH | PASS [APPROVED-LOCKED] |
| 137 | OK | 93 | 1.46 | -14.9 | 20.2 | MATCH | PASS (real #137 = John 17 build; see note 5) |
| 138 | OK | 70 | 4.19 | -14.7 | 15.4 | MATCH | PASS [APPROVED-LOCKED] |
| 139 | OK | 66 | 4.17 | -14.9 | 14.2 | MATCH | PASS [APPROVED-LOCKED] |
| 140 | OK | 88 | 4.22 | -14.9 | 17.4 | MATCH | PASS |
| 141 | OK | 69 | 4.18 | -15.0 | 14.8 | MATCH | PASS [APPROVED-LOCKED] |
| 142 | OK | 61 | 12.78 | -14.8 | 11.0 | MATCH | FAIL - LOCKED (approved) - FIX-LATER |
| 143 | OK | 61 | 8.99 | -14.9 | 12.0 | MATCH | FAIL - LOCKED (approved) - FIX-LATER |
| 144 | OK | 62 | 4.65 | -14.8 | 12.7 | MATCH | PASS [APPROVED-LOCKED] |
| 145 | OK | 61 | 9.6 | -14.8 | 12.0 | MATCH | FAIL - LOCKED (approved) - FIX-LATER |
| 146 | OK | 97 | 1.89 | -14.9 | 18.2 | MATCH | PASS |
| 147 | OK | 127 | 1.89 | -14.7 | 18.9 | MATCH | PASS |
| 148 | OK | 208 | 1.92 | -14.7 | 17.7 | MATCH | PASS |
| 149 | OK | 173 | 1.91 | -14.7 | 18.2 | MATCH | PASS |
| 150 | OK | 156 | 1.93 | -14.7 | 18.1 | MATCH | PASS |
| 151 | OK | 176 | 1.54 | -14.8 | 21.2 | MATCH | PASS |
| 152 | OK | 163 | 1.52 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 153 | OK | 204 | 1.48 | -14.8 | 21.2 | MATCH | PASS |
| 154 | OK | 179 | 1.47 | -14.8 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 155 | OK | 176 | 4.18 | -14.9 | 20.2 | MATCH | PASS |
| 156 | OK | 162 | 1.49 | -14.9 | 21.2 | MATCH | PASS [APPROVED-LOCKED] |
| 157 | OK | 210 | 1.48 | -14.8 | 20.6 | MATCH | PASS |
| 158 | OK | 198 | 1.47 | -14.9 | 20.8 | MATCH | PASS [APPROVED-LOCKED] |
| 159 | OK | 171 | 4.17 | -14.8 | 20.6 | MATCH | PASS |
| 160 | OK | 201 | 1.51 | -14.8 | 20.4 | MATCH | PASS |
| 161 | OK | 188 | 1.48 | -14.8 | 20.8 | MATCH | PASS |
| 162 | OK | 188 | 4.18 | -14.8 | 20.5 | MATCH | PASS |
| 163 | OK | 163 | 1.48 | -14.8 | 21.1 | MATCH | PASS |
| 164 | OK | 170 | 1.5 | -14.7 | 20.9 | MATCH | PASS |
| 165 | OK | 166 | 1.5 | -14.8 | 21.6 | MATCH | PASS |
| 166 | OK | 175 | 1.51 | -14.8 | 20.9 | MATCH | PASS |
| 167 | OK | 155 | 4.18 | -14.9 | 21.0 | MATCH | PASS |
| 168 | OK | 166 | 4.23 | -14.8 | 20.3 | MATCH | PASS |
| 169 | OK | 167 | 4.19 | -14.8 | 20.4 | MATCH | PASS |
| 170 | OK | 168 | 1.52 | -14.8 | 21.6 | MATCH | PASS |
| 171 | OK | 94 | 1.91 | -14.8 | 18.0 | MATCH | PASS |
| 172 | OK | 71 | 1.89 | -14.8 | 15.4 | MATCH | PASS |
| 173 | OK | 49 | 2.22 | -14.8 | 8.3 | DIFF | FIXED |
| 174 | OK | 61 | 2.22 | -14.9 | 11.3 | DIFF | FIXED |
| 175 | OK | 76 | 2.21 | -15.0 | 14.3 | DIFF | FIXED |
| 176 | OK | 108 | 1.94 | -14.7 | 18.5 | MATCH | PASS |
| 177 | OK | 66 | 2.22 | -14.8 | 12.2 | DIFF | FIXED |
| 178 | OK | 91 | 2.22 | -14.8 | 15.1 | DIFF | FIXED |
| 179 | OK | 81 | 1.53 | -14.7 | 17.5 | MATCH | PASS |
| 180 | OK | 85 | 4.97 | -14.8 | 18.1 | MATCH | PASS |
| 181 | OK | 57 | 2.23 | -14.8 | 11.1 | DIFF | FIXED |
| 182 | OK | 92 | 1.48 | -14.8 | 20.6 | MATCH | PASS |
| 183 | OK | 88 | 1.48 | -14.8 | 19.5 | MATCH | PASS |
| 184 | OK | 91 | 1.47 | -14.7 | 19.2 | MATCH | PASS |
| 185 | OK | 66 | 4.98 | -14.8 | 13.7 | MATCH | PASS |
| 186 | OK | 73 | 1.48 | -14.8 | 16.2 | MATCH | PASS |
| 187 | OK | 53 | 2.21 | -14.7 | 9.9 | DIFF | FIXED |
| 188 | OK | 84 | 4.97 | -15.0 | 17.6 | MATCH | PASS |
| 189 | OK | 67 | 4.97 | -14.9 | 14.0 | MATCH | PASS |
| 190 | OK | 69 | 1.53 | -14.9 | 14.5 | MATCH | PASS |
| 191 | OK | 63 | 4.99 | -14.8 | 13.0 | MATCH | PASS |
| 192 | OK | 69 | 4.98 | -14.9 | 14.2 | MATCH | PASS |
| 193 | OK | 62 | 4.99 | -14.9 | 12.8 | MATCH | PASS |
| 194 | OK | 62 | 1.5 | -14.9 | 13.4 | MATCH | PASS |
| 195 | OK | 56 | 2.22 | -14.9 | 10.8 | DIFF | FIXED |
| 196 | OK | 88 | 4.97 | -14.8 | 18.3 | MATCH | PASS |
| 197 | OK | 81 | 4.98 | -14.9 | 16.6 | MATCH | PASS |
| 198 | OK | 76 | 4.98 | -14.9 | 16.1 | MATCH | PASS |
| 199 | OK | 82 | 4.98 | -14.9 | 17.0 | MATCH | PASS |
| 200 | OK | 66 | 4.96 | -14.9 | 13.2 | MATCH | PASS [APPROVED-LOCKED] |
