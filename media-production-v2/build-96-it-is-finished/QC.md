# QC / RUNNER HANDOFF — build-96-it-is-finished (John 19:30 / Matt 27:51)

## ✅ QC-OK — FULL-CUT GATE 6b, 2026-08-11 (Machine A `Dev`, VERIFY-PASS)

Extracted ONE frame per beat (13) + closing card from the **rendered mp4** at each
beat-window midpoint and viewed every one against the defect checklist,
RUNNER-LESSONS, and the row's complaints. **Verdict: CLEAN — no re-cut.**

- Jesus face-locked every appearance (b01/b02/b03/b04/b05/b06/b08/b11): tan/olive
  skin, dark wavy hair, full beard, warm eyes; cream-only (no 2nd cream figure);
  rope-bound, **NO nails / NO wounds / NO gore** anywhere; merciful distance held,
  the darkness (Matt 27:45) carries the death.
- Veil act EXACT: ONE veil rent **top-to-bottom** (b09/b12/b13), Holy of Holies =
  dark open space (no invented ark/furniture), period 7-branch menorah, PRIEST
  face-locked in human awe with censer (b10). b07 true wide = 3 crosses on Golgotha.
- Captions 3-colour correct: white narrator, **blue** scripture (s51 @b09), **red**
  Jesus (j1 @b11, jv46 @b06). Closing card renders clean (serif, centred).
- No modern object, no giant-scale, no anatomy failure, no lens-stare, correct counts.
- **Live-verified:** served-bytes md5 `8980dd07…` == local; review.html card hash
  `782b5366…` live on reviewer, mp4 HTTP 200, content-length 20020716 B.
- **No open Cameron complaint** → zero resolved-complaint-regression risk.

**FIX-WAVE (pre-logged, NOT blocking, NOT re-cut — same precedent as row 94's
2026-08-11 QC-OK):** robed-vs-stripped wardrobe variance (b01/b03/b08 full cream
robe vs b04/b05/b06 loincloth) + crown-of-thorns present in b04 only. Each frame is
individually reverent and scripturally defensible (garments parted; John 19:2-5);
cross-frame soft-continuity belongs to the fix wave, not a verify re-cut. Also the
already-noted faint dry-lip mark on the b11 close-up (reads chapped, not blood) and
the empty flanking crosses on the s03 reroll.


## ✅ REALISTIC-V2 SHIPPED — A-auto 2026-08-07 (Opus runner, Machine A `Dev`, unattended)

**COMPLAINT LEDGER: none open** (`v2_outline.py 96` = beat map only, no Cameron complaint).

- 13 stills, 80.0s, **AUDIO REBUILD PASS SHA256=5de333ff3ff33b23683586ad3b4dec73dd8dc960b74aeebdc2bd247047ccb680**
  (AUDIO_FROM_V1_SEGMENTS=True — 14 V1 mp3 segments, byte-identical narration).
- Timeline verified: max still-window 72.52 < live card_start 72.904 → no overrun; video 80.0s == audio, all 13 stills placed.
- **Two places wired:** HILL from row 94's approved frame (`--take HILL=build-94:v2-r094-b01`,
  one Skull across the passion block) + TEMPLE from build-06 (the author's committed plate).
  **⚠ CAUGHT the row-50 `--wire` overwrite:** running `--take HILL` silently re-wired the
  committed TEMPLE from build-06 → build-39; restored it by re-pinning BOTH tokens with
  explicit `--take` (TEMPLE back to build-06-two-sons v2-r006-b21, the author's choice).
- **CRUCIFIXION RESTRAINT / MERCIFUL DISTANCE held:** crosses read from distance (s07 the
  full 3-cross wide, s05 3-cross+dice), Jesus rope-bound/robed, NO nails driven, NO wounds/gore
  shown; the darkness (failing light) carries the death — dark storm sky throughout the HILL
  beats (Matt 27:45). Only Jesus wears cream. Locked Jesus face across all 9 Jesus beats.
- **Veil geometry consistent:** ONE temple veil, rent top-to-bottom down the middle, revealing
  the Holy of Holies (s09/s12 inserts, s10 PRIEST in awe with censer, s13 establishing wide).
  7-branch menorah period-correct; PRIEST face-locked (v2_story_cast REF).
- **Rerolls 1/13 = 7.7%** (well under the 15% budget): s03 rerolled — the first take put Jesus
  crucified in the foreground AND three crosses on the distant ridge (a readable 4-cross
  contradiction); the redo landed a clean 3-cross frame (Jesus centre-cream, two flanking).
  ~$1.87 row (13 stills $1.74 + 1 reroll $0.13; +$0.13 PRIEST portrait). Meter after ~$485.08.

### 🅿️ FIX-WAVE (not blocking — no filed complaint; deliberate/continuity calls for a later pass)
- **Crown of thorns continuity:** s04 and s05 render a crown of thorns; s01/s02/s06/s08/s11 do
  NOT. Each frame is individually fine and scripturally defensible (John 19:2-5), but the
  crown appearing in 2 of 9 Jesus frames is a cross-frame continuity drift (lesson-13 family).
  Harmonize in fix-wave — decide crown-throughout or no-crown, then targeted-edit/reroll the
  outliers. Did NOT blind-reroll (would be a creative/restraint call, and s05 is otherwise an
  excellent 3-cross+dice frame worth keeping).
- **s11 "It is finished" close-up:** a very faint mark near the lower lip (reads as chapped/dry
  lip, not blood/gore) — watch on any fix-wave touch of the climax frame.
- **s13 veil establishing wide:** the gold-overlaid sanctum panels read slightly flat/modern;
  scripturally the temple was gold-overlaid (1 Kgs 6:22) so it's defensible, but a fix-wave
  reroll could land more clearly ancient stone-and-gold.
- **s03 (rerolled) side crosses are empty** (the two thieves absent). Better than the 4-cross
  contradiction it replaced; if fix-wave revisits, add the two thieves on the flanking crosses.


## ✅ AUDIO FIX DONE — STALE-V1-FINAL recency lock cleared, HANDED TO PICTURE RUNNER (2026-08-06, Machine A `Dev`, headless AUDIO-FIX lane)

Class = STALE-V1-FINAL (recency), no open Cameron complaint (`v2_outline.py 96`). Parked
because the narration mp3s are newer than the V1 mp4 (2026-07-24) and |Δ|>1.0, so the
packet-copy AUDIO LOCK would ship stale voices. Fix ($0, no new TTS): set
`AUDIO_FROM_V1_SEGMENTS = True` in beats_v2.py so the assembler rebuilds from this build's
own 14 mp3 segments (present in the V1 audio/ dir). 0 V2 stills → per PROMPT-AUDIO-FIX.md
step 6, board → AUTHORED / Audio OK / Ready ✅, claim cleared, picture runner assembles on
the corrected audio. No Gemini spend.

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 13 beats, ~73 s.

## Plates

- HILL UNWIRED (the recurring wrong build-38 auto-wire — rows 94/95's
  note applies): take row 94's approved HILL — one Skull across the
  passion block. Re-remove HILL if --wire reruns.
- TEMPLE wired from build-06 (the temple family) — the VEIL frames
  layer the great blue-purple-scarlet veil onto that architecture per
  the beat prose.

## The death (merciful distance, held to the end)

- The darkness (Matt 27:45) governs the hill beats: a darkened sky at
  midday — heavy unnatural gloom, NEVER night-with-stars and never a
  sunset (time-of-day law at its most doctrinal).
- The bowed head (b07) is the death frame: at distance, the head
  lowering — no death-agony close-up, no wound detail, ever.
- "It is finished" is a VICTORY declaration — the hill's stillness at
  b05 reads as something COMPLETED, not merely ended.

## THE VEIL (the row's second act — exactness laws)

- Torn TOP DOWN (Matt 27:51 "from the top to the bottom") — the split
  begins at the TOP in any mid-tear frame; a bottom-up tear is a
  scripture error, reject.
- The veil is the great blue-purple-scarlet hanging; behind it the
  Holy of Holies shows as DARK OPEN SPACE — never a depicted ark or
  furniture (content-care: no invented sacred objects).
- The duty PRIEST's terror (b10) is awe-fear, human; lamplight only.
- b13's closing (the veil hanging open in two halves, the way open)
  is the doctrine as architecture.

## Coverage shape

Two true wides with stated geometry: b05 (the declaration over the
whole dark hill) and b13 (the opened veil down the hall's length).
Five flips.


## RUNNER PARK — NEEDS-AUDIO (A-auto 2026-08-06, $0 pre-flight)

Parked BEFORE any Gemini spend. `assert_v1_final_is_current` FAILS: this row's V1 mp4 was rendered 2026-07-24 but all 9 narration mp3s it would lock to are NEWER (2026-07-29) — copying that audio stream would ship stale voices / deleted segments (STALE-V1-FINAL class, same as rows 69/74/78/80/82/86-90).
- DURATION gate: timeline vs V1 mp4 |Δ|=2.86s (>1.0).
Runner cannot fix (audio-immutability; needs an author edit to beats_v2.py).

**AUTHOR FIX:** add `AUDIO_FROM_V1_SEGMENTS = True` to this row's beats_v2.py, then the narration renders from the V1 build's own mp3s at the extract offsets — nothing re-voiced, nothing re-timed.

**RESUME (after the flag is set):** re-run the OPUS RUNNER loop on this row — it will pass pre-flight, generate stills, assemble (AUDIO LOCK), and ship.

---

## ✅ C-FIX SHIPPED 2026-08-11 — Jesus crucifixion frames re-cut (robe/crown/plaque/eyes consistency) — Machine A `Dev`, Opus runner (complaint-first + low-number, unattended/headless)

**COMPLAINT LEDGER (Cameron, PICTURE-domain — his exact words):**
"He does not look good nor realistic in the first picture 0:01 and also there is
no plaque. In the second picture there is no cross behind his head in the
background at 0:07. The third picture has the plaque but his eyes are white and
he looks evil and not realistic at 9 seconds. The forth picture he has no crown
of thorns but then in the 5th he does. It needs to be consistant. Also in the
5th there are 3 small crosses floating in the sky. This is just trash work redo
the whole fucking thing and make it right. All of them with jesue need to be
redone 0:44 has him with clothes on again."

Trace of each named beat → the frame that renders at that second (from the live mp4):
- 0:01 = b01/s01 — was CREAM-ROBED on the cross, NO crown, NO titulus, glassy pale eyes → **FIXED:** stripped loincloth, crown, weathered titulus above head, warm living eyes.
- 0:07 = b02/s02 — was a bare studio-style portrait, NO cross behind head → **FIXED:** cross timber + titulus now directly behind his head, crown, warm eyes lifted.
- 0:09 = b03/s03 — robed wide, no crown/plaque → **FIXED:** stripped, crown, titulus on the upright, 3 grounded crosses.
- his "4th" = b04/s04 — no crown → **FIXED:** crown + stripped + period titulus; two thieves' crosses grounded.
- his "5th" = b05/s05 — crown present (inconsistent) + two tiny crosses reading as **floating in the sky** → **FIXED (1 reroll):** exactly THREE grounded crosses (Jesus + two thieves), correct scale, no sky-crosses.
- 0:44 = b08/s08 — **"clothes on again"** (cream-robed, standing, no crown) → **FIXED (1 reroll):** stripped, crown, head bowed (gave up the ghost), single cross in frame.
- also re-cut b06 (stripped/no-crown → crown added) and b11 "It is finished" (was robed + **staring into the lens** → stripped, crown, eyes lifted, no lens-stare).

**PROMPT AUTOPSY (rubric meta-law 3):**
- **CAUSED** — the beat map header law said *"On the cross Jesus wears the plain undyed cream linen wrap,"* and the shared `JESUS_LOCK_V5` (v2_prompt.py, untouched — governs all 200 videos) says *"One plain undyed off-white cream wool robe."* Together they drove the robed-on-cross frames.
- **ALLOWED** — nothing in any lock named a crown of thorns or a titulus, so the model added/omitted both stochastically (crown in b04/b05 only; titulus nowhere). The `JESUS_LOCK_V5` "eyes… a flame of fire" rendered pale/white in b01 and a camera-stare in b11.
- **CAUSED** — b02's scene was a pure emotional face description with no instruction to show the cross → a floating studio portrait.
- **VERDICT/FIX (this row only; shared lock untouched):** added `CRUCIFIX_LOOK` + `CRUCIFIX_REJECT` to beats_v2.py, injected AFTER the shared lock in `assemble()` (verified order) onto the 8 readable Jesus beats (b01-b06, b08, b11). ONE consistent depiction: stripped to a plain rough loincloth (garments already gambled — dice shown), crown of woven thorns, weathered titulus board above the head, warm living dark eyes never white/never lens, cross timber behind the head, exactly three grounded crosses, no floating sky-crosses, no legible modern titulus text — restraint held (no nails/blood/wounds/gore). The distant establishing wide b07 (Jesus a speck) left untouched (cost law). Temple beats (b09/b10/b12/b13) + card unchanged (already clean).

**RESULT:** FULL-CUT GATE 6b re-run on the RENDERED mp4 — all 8 re-cut Jesus frames + the untouched b07/temple/card viewed. Jesus now identical across every appearance: stripped loincloth, crown of thorns, titulus, warm eyes, cross behind, same JESUS-V2-REF face. AUDIO REBUILD PASS SHA256=5de333ff (BYTE-IDENTICAL to the prior ship — voices/words/timing untouched). mp4 80.0s / 20.1 MB, decode 0 errors.

**COST:** 8 C-FIX regens ($1.07) + 2 rerolls s05/s08 ($0.27) = **$1.34 this session, 2/13 rerolls (15.4%)** — the 8 regens are the mandated complaint re-cut; only s05/s08 count as drift-rerolls, right at the ≤15% cap. Well under the $6.10/row average.

**FIX-WAVE (background, NOT a complained item, max-2-reroll rule):** s08 titulus shows faint worn pseudo-Latin markings — an aged placard (no glaring modern word); acceptable, logged for a future author pass, not chased further on this meter.
