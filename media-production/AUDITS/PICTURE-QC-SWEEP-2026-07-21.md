# PICTURE-QC SWEEP — 2026-07-21 (every still, every workable video)

Session mandate: inspect every still in all 200 videos; fix character drift
(Jesus vs JESUS-MASTER-REF, face-law v3) and scene defects (direction, scale,
anatomy, headcount, panels/borders, fake tears, story-fit). Only Jesus has an
approved sheet, so 56 builds with unsheeted rostered characters are BLOCKED —
list lives in QUEUE.md ("CHARACTER-SESSION BLOCK LIST"). Approved (39) locked.
Worklist JSON: scratchpad roster-scan (102 workable rows).

## Complaint videos — RESOLVED this session
| # | complaint | action |
|---|---|---|
| 2 | 0:15 son walking wrong way | shot1-leaving REGENERATED (son now walks away from farm, father behind in gateway); rebuilt |
| 9 | end-card words off-frame | rebuilt with auto-wrap card; ALSO found+fixed video stream that died at 3:38 of 4:32 |
| 18 | Jesus short hair in one picture | s3 REGENERATED (hair past shoulders, disciples per locks); rebuilt |
| 83 | direction/giant/dead-air | already fixed+committed by prior session (verified: 2.4s tail, stills correct) |
| 107 | John inconsistent | s2+s9 REGENERATED to first-still keeper look (dark shaggy hair ~30); s2 also fixed 3→2 messengers (Matt 11:2); rebuilt |
| 112 | giant Jesus 2:11 | already fixed; THIS session found+fixed: s2 was 3-panel collage (+gold sash), s4+s8 painted borders; rebuilt |
| 181 | pictures don't fit story | s3 (stars now visibly sing) + s4 (foundations/cornerstone light) REGENERATED; rebuilt |
| 3,19,90,113,135,153,157 | — | BLOCKED on character sheets (QUEUE.md block list) |

## Full-still sweep results (workable list, audit-score order)
| build | verdict | notes |
|---|---|---|
| 60-gerasene-demoniac | CLEAN | 9/9 pass; healed man consistent s7–s9 |
| 64-pool-of-bethesda | CLEAN | 9/9 pass; infirm man consistent |
| 45-wicked-tenants | CLEAN | 13/13 pass; owner/son/tenants consistent; care-beats correct |
| 44-two-debtors | 2 DEFECTS | s3: painted tear streaks on woman's cheeks (violates no-fake-tears law + its own prompt); s6: teardrop bead on green debtor's cheek. Regen queued. s7 zoom-checked OK (brimming only) |
| 62-ephphatha | CLEAN | 9/9 pass |
| 61-syrophoenician-woman | CLEAN | 9/9 pass; woman consistent every shot |
| 44 fix status | s3+s6 regenerated (dry cheeks), zoom-QC'd, installed, rebuilt |
| 63-man-born-blind | CLEAN | 10/10 pass; man consistent blind→believing; s5 slightly more painterly than the set (watch for style drift if regenerating) |
| 41-counting-the-cost | CLEAN | 16/16 pass; s6-vs-s7 builder difference is BY DESIGN (BUILDER LOCK vs SECOND BUILDER LOCK in PROMPTS.md) |
| 124-love-your-enemies | CLEAN | 10/10 pass; both neighbours consistent s2/s4/s5/s9/s10; Jesus per ref in s1/s3/s7 |
| 20-samaritan | 2 FIXED | s4: victim gained a maroon robe + black hair though he was STRIPPED (lock: torn undertunic, dark brown hair); Samaritan's cloak was rainbow-striped vs locked ochre/rust. s5: painted parchment border + watercolour style break. Both regenerated, rebuilt, verified |
| 38-persistent-widow | CLEAN (mandate) | 7/7 characters consistent (widow, judge). TWO NON-MANDATE OBSERVATIONS for Cameron to rule on: (a) s1–s5 render the judge's hall as GOTHIC — pointed arches, ribbed vaults, medieval capitals — an anachronism in first-century Judea; (b) s6/s7 praying man reads European rather than Middle Eastern and wears cream. Not regenerated: outside this session's defect list. If Cameron wants period-accurate architecture as a standing law, this build needs 5 stills |
| 42-barren-fig-tree | 3 FIXED | s5 had an EXTRA unlocked figure (young beardless man) in a beat the prompt gives to the owner ALONE. s7+s8 showed the tree loaded with ripe figs during "dig about it"/"dung it" — contradicts the barren premise (s9 "if it bear fruit" correctly shows first buds). All 3 regenerated, rebuilt |
| 21-lost-sheep | 4 FIXED | s2 was a STACKED TWO-PANEL image with a white divider (anti-panel violation). Shepherd drift: s2–s5 painted him grey-bearded ~55 while the build's own lock says dark hair/short dark beard (s6/s7 correct). s2,s3,s4,s5 regenerated to the locked look; rebuilt |

## Still to sweep (in priority order)
61, 63, 41, 48(blocked? no—48 blocked), 124, 129, 8, 13(blocked), 20, 21,
23–35 parables, 36, 38, 39, 41, 42, 46, 47, 52, 54, 55, 56, 59, 61, 63, 65,
68, 70, 74, 75, 76, 77, 78, 79, 80, 81, 82, 88, 94, 95, 96, 97, 108, 109,
111, 121–127, 129, 131, 133, 134, 140, 146, 150, 151, 159, 163, 164, 167,
170, 171, 173, 175, 176, 182, 183, 185, 187, 188, 189, 191–195, 198.
(Cross off QUEUE.md-blocked rows; 87/89 also blocked — no prompt files, Mary/Twelve.)

## Process (for resumption)
1. Read every assets/*.jpeg of the build (Read tool renders images).
2. Checks: Jesus vs JESUS-MASTER-REF (long dark hair PAST shoulders, full dark
   beard, warm olive-tan, cream robe, no halo); in-video consistency of every
   recurring figure; walk/look direction vs beat; scale (no giants); anatomy
   (2 arms/hands/legs, 1 head); headcounts vs scripture (enumerate positionally);
   panels/borders/vignettes; fake tears; story-fit of each beat.
3. Defect → regenerate via Flow (Nano Banana 2, 9:16, 2K) with the build's own
   PROMPTS.md prompt + explicit fix clause; zoom-QC the download; install with
   .pre-qc.bak backup; python3 build.py; admin/verify-mp4.sh AND check last
   video packet pts vs duration (verify-mp4 alone missed #9's dead stream);
   FIXNOTE.txt; ship-fixes cron commits.
4. File uploads into Chrome are blocked for this session — edits must be fresh
   regens from prompts, not Gemini image-edits.
