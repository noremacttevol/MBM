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
