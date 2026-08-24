# build-183-sun-moon-and-stars — QC / runner handoff (1 Corinthians 15:40-42)

**AUTHORED 2026-08-07, Machine A `Dev` (Fable-5 author lane, $0).** 17-beat V2 map,
`v2_prompt.py --check` PASS (0 warnings), windows contiguous+monotonic 0.400→64.419
(=card_start), every segment onset in-window, audio OK. Picture-only rebuild — do
NOT re-voice.

---

## COMPLAINT LEDGER (LEARNING LAW)

**No open Cameron complaint on file** (`v2_outline.py 183` shows none). Built to the
full rubric (all 15 lessons) and the laws below.

**Review card:** e.g. *"Paul's answer to 'with what body do the dead rise?' — the sun,
the moon and the differing stars, each with its own glory, as a picture of the
resurrection: sown in corruption, raised in incorruption; a brightness God is
preparing for you."*

---

## 🅿️ RUNNER — do this (picture-only build on the locked audio)

1. **Audio:** default AUDIO LOCK stream-copy (board Audio = OK). No re-voice, no flag.
2. **Places — promote-first (lesson 11), but the SKY is NOT plate-locked:**
   - `PAUL-COURT` → generate **b01** (establishing wide of the portico) first, QC it,
     `--promote build-183-sun-moon-and-stars PAUL-COURT <b01 frame>`, then b02, b10.
   - `RESURRECTION-DAWN` → generate **b11** (establishing wide of the dawn field)
     first, QC it, `--promote ... RESURRECTION-DAWN <b11 frame>`, then b12, b13, b14,
     b17.
   - **IGNORE the `--wire` "NEW PLACE" suggestions for `HEAVENS-DAY`, `HEAVENS-NIGHT`
     and `RISEN-ONES`.** HEAVENS-DAY (sun/day) and HEAVENS-NIGHT (moon+stars/night)
     are DIFFERENT times of day BY DESIGN — a single plate would bleed the wrong
     time-of-day (row-50/101 lesson). RISEN-ONES is a people text-lock. Do NOT
     promote a plate for any of the three; the text lock carries them.
3. **SPEAKER LAW — SCRIPTURE, not red-letter, not God-voice.** Only s1 (b05/b06/b07)
   and s2 (b11/b12) are scripture → **light-blue** captions; every other beat is the
   NARRATOR → **white**. NO red-letter and NO GREEN God-voice (Paul's epistle, quoted
   as his written words). NO Jesus and NO cream anywhere.
4. **HARD GATE — GOD IS NEVER EMBODIED (default gate).** b17 "the same God who hung
   the sun..." shows NO figure/face/hand/beam — the heavens carry it. Drift-word gate
   bans halo/glow/rim-light; sun/moon/stars are natural lights, NEVER faces or ringed
   discs.
5. **CONTENT-CARE — resurrection of the DEAD by RESTRAINT (rows 171/173).** The risen
   (b11, b13, b14) are WHOLE, solid, living, fully-clothed, healthy, glad men and
   women rising into the golden dawn — NEVER corpses, skeletons, bones, decaying/
   wounded flesh, zombies, translucent ghosts or mist-figures, and never gore. If a
   reroll produces any corpse/skeleton/ghost, reject it.
6. **"Sown in corruption... raised in incorruption" (b12) = Paul's SEED metaphor** —
   a spent seed in dark earth breaking open into a green shoot rising to the light.
   NO rotting body. b14's "husk" is a spent seed-husk, not a body.
7. **Face / scale board (lessons 2/10/14):** PAUL is the SAME wiry ~50 balding
   dark-bearded man (byte-identical to builds 138/155/166/171) on all his beats
   (b01/b02/b10). RISEN-ONES are distinct individuals, ordinary-sized, one ground
   plane. Identity-edit drift, recheck the whole frame.
8. **Time of day (intentional):** SUN beats (b05/b08) = brilliant clear DAY; MOON/STAR
   beats (b03/b04/b06/b07/b09/b15/b16) = deep luminous NIGHT; PAUL beats = daytime
   court; RESURRECTION beats (b11-b14/b17) = golden DAWN. Keep them distinct.
9. **Assemble** with `v2_assemble.py` (AUDIO LOCK stream-copy must pass), verify
   captioned length ≈ card_start (64.419) + card, decodes 0 errors, realistic-only
   (Law 14) on all 17. Ship to the reviewer.

## Coverage / windows
17 beats, ~3.8 s/pic. Contiguous window starts: b01 0.400 · b02 5.640 · b03 8.286 ·
b04 12.530 · b05 16.365 · b06 19.800 · b07 22.800 · b08 26.561 · b09 28.370 ·
b10 30.640 · b11 33.586 · b12 36.520 · b13 41.291 · b14 43.770 · b15 48.900 ·
b16 51.530 · b17 58.630 · (hold to card_start 64.419).
Arc: Paul asked what body the dead rise with → he points at the sky → the varied
lights → sun's glory / moon's glory / stars differ → the astonishing point → "so also
is the resurrection of the dead" → sown/raised (seed→shoot) → what rising is like →
what goes in breaks down / what returns never will → not one flat outcome → glories
plural, each a gift of light → the God who hung them is preparing a brightness for you.

---

## ✅ RUNNER SHIPPED (2026-08-24, Machine A `Dev`, Claude session)

**FIRST ROW BUILT UNDER RUBRIC LESSON 26 (clone prevention) — and it worked.**
Before the first paid roll, every same-place beat in the three big families
(HEAVENS-NIGHT ×7, RESURRECTION-DAWN ×5, PAUL-COURT ×3) was given an explicit
contrasting camera plus a "NOT the <earlier> framing" negative. Result: **2
rerolls / 17 stills = 11.8%, $2.55** — against 28-38% on the rows built earlier
tonight without the pre-authoring. The night sky came back genuinely varied
(moon+stars wide, telephoto cluster, low large moon over a ridge, diagonal milky
way, close colour starfield, ground-level silhouette, panoramic arc).
- The ONE clone (s05/s08, 0.968) was in HEAVENS-DAY — the only family I did NOT
  pre-contrast. Fixed by contrasting b08 to a low raking horizon sun over a lit
  landscape → 0.674. That is a clean natural experiment confirming lesson 26.
- b01 rerolled once: `v2_story_cast` reported "no REFS" and left `REFS = {}`
  even though paul.jpeg was copied in from build-138, so Paul generated
  unanchored. **Wire REFS by hand whenever the cast sheet is copied rather than
  generated** — verified against the canon sheet after the fix.

**FULL-CUT GATE — 17 beats + card viewed on the ENCODED mp4: PASS.** SPEAKER
LAW: s1/s2 LIGHT-BLUE (Paul's epistle, quoted); narrator white; no red, no
green; no Jesus, no cream. GOD NEVER EMBODIED (b17). CONTENT-CARE: the risen are
WHOLE living clothed people walking into dawn — never corpse, skeleton, zombie
or ghost; "sown/raised" uses Paul's own seed metaphor (split seed → green
shoot), no rotting body. PAUL byte-identical to 138/155/166 (md5 b200a21d).
Intentional day/night/dawn registers preserved (sky deliberately not
plate-locked). Encoded similarity: no pair >0.92. Card clean.

**AUDIO:** guard fix `AUDIO_FROM_V1_SEGMENTS` (V1 72.701s vs extract 71.738s —
0.963s stale trailing take; 8 ElevenLabs mp3s) — **AUDIO REBUILD PASS
SHA256=f28ba0db4f…**, 71.7s, 20.0 MB.
