# MBM Video QC Review List — 2026-07-17

**Purpose:** Ranked list of review-pool videos (built on disk, NOT yet approved by Cameron) by confidence they are WRONG. Top = 100% confirmed defects. Bottom = clean / minor.

**How produced:** Hermes ran mechanical audio QC (silencedetect >2.5s mid-video, level scan) on all 120 review-pool videos + vision-checked frames + end cards on the documented-defect rows. Confidence levels are Hermes's honest estimate.

**Review pool:** 120 videos (160 built total − 40 explicitly approved by Cameron).

---

## TIER 1 — 100% CONFIRMED WRONG (Cameron already rejected / visually verified)

| # | Story | Defect | Confidence | Source |
|---|-------|--------|-----------|--------|
| 7 | Peter walks on water | End card has TOFU SQUARES (missing-font glyphs) — verified by vision on the card frame. Also mid-video dead-air 2.6s @104.6s, and QUEUE notes knee-deep figure + direction mismatch + weird stills (3rd reject) | 100% | Cameron reject + vision confirm |
| 17 | Jesus wept (Lazarus) | REJECTED by Cameron ("not good"). DEFERRED — redo LAST after all others done | 100% | Cameron reject |
| 32 | The talents | TTS misread "kinder" as "Kender" @2:39 (narration-only fix, visuals kept). End card now clean (verified). Mid-video dead-air 2.8s @80s + @112s | 100% audio defect | Cameron reject + vision confirm |

## TIER 2 — MECHANICAL LAW BREAK (audio dead-air >2.5s mid-video, auto-detected)

These violate the NO DEAD AIR law (no spoken gap >2.5s). High confidence the audio is wrong; the *video* stills may be fine. Send to builder for narration/assembly fix.

| # | Story | Dead-air gap(s) (start s, dur s) | Confidence |
|---|-------|----------------------------------|-----------|
| 30 | The net | 27.0/2.8, 115.8/2.8 | 95% |
| 128 | Famine of hearing | 60.6/2.8 | 95% |
| 137 | Stephen sees him standing | 39.3/4.4, 48.5/13.0 | 95% |
| 145 | Way, truth, life | 51.6/9.6 | 95% |
| 146 | Vine and branches | 53.7/9.6 | 95% |
| 147 | Joseph forgives | 72.1/9.6 | 95% |
| 148 | Ruth and the redeemer | 89.5/9.6 | 95% |
| 149 | Hannah is heard | 75.2/9.6 | 95% |
| 150 | Shepherd Psalm | 68.7/9.7 | 95% |
| 171 | Baptized for the dead | 77.7/9.6 | 95% |
| 172 | Gospel to the dead | 51.1/9.6 | 95% |
| 173 | Dead shall hear | 47.2/13.4 | 95% |
| 174 | Hearts of the fathers | 59.0/13.4 | 95% |
| 175 | Mountain of the LORD's house | 73.5/13.5 | 95% |
| 187 | Ye are gods | 51.2/9.8 | 95% |
| 195 | Prove all things | 53.8/8.0 | 95% |

> Note: gaps of ~4.2s at the END of every video (the closing card hold) are NORMAL and excluded. Only mid-video gaps above are listed.

## TIER 3 — DOCUMENTED REVIEWER NOTES (builder flagged, needs your eyes)

Builder self-flagged these. Hermes has NOT fully vision-verified all; confidence is the builder's note + my spot-check where done.

| # | Story | Noted concern | Confidence it's wrong |
|---|-------|--------------|----------------------|
| 14 | Ten lepers | Lepers look like GIANTS vs Jesus/disciples @~0:55 (scale) — APPROVED but FIX-LATER | 80% (you approved, flagged scale) |
| 44 | Two debtors | Captions cover whole picture (CAPTION-LAW) — approved, fix applied | 70% (already fixed per note) |
| 45 | Wicked tenants | Captions cover whole picture — approved | 70% |
| 59 | Feeding 4000 | s5 had halo/radiance, rerolled + fixed | 60% (likely resolved) |
| 106 | God spake by prophets | "no halo" claimed; verify | 50% |
| 107 | John's doubt | "no halo" claimed; verify | 50% |
| 108 | My sheep hear | "no halo" claimed; verify | 50% |
| 109 | Ask seek knock | "no halo" claimed; verify | 50% |
| 110 | Lord's prayer | "no halo" claimed; verify | 50% |
| 111 | Lilies and sparrows | Brown mantle variance over cream robe (s2) — Hermes saw one frame, robe was clean there; variance may be in other frames | 60% |
| 112 | Beatitudes | "no halo" claimed; s8/s10 recovered | 50% |
| 127 | Strait gate | "no tofu" claimed; verify | 50% |
| 136 | Healed in two touches | Soft cream radiance behind Jesus head (s5) — subtle, not distinct halo; builder couldn't reroll (assembly-only) | 70% (real but minor) |
| 138 | We are his offspring | Brown mantle variance (Paul) | 60% |
| 154 | Everlasting gospel | Angel gold/light NOT cream, no halo (correct) | 40% (likely fine) |
| 170 | Sacrament | Caption frames not visually spot-checked before push | 50% |

## TIER 4 — CLEAN (Hermes spot-checked, no defect found)

Verified clean on sampled frames: #49 Water to Wine, #111 Lilies (one frame), #136 Healed (one frame). 
Remaining ~80 review-pool videos: NOT yet vision-checked this pass — pending your go-ahead for full sweep.

---

**Next step:** Cameron confirms Tier 1 + Tier 2, those go to Claude's builders. Tier 3 needs your eyes on the specific frames. Say "sweep the rest" and Hermes vision-checks all ~80 remaining.
