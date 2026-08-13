# build-179-stephens-witness — QC / runner handoff (Acts 7)

**AUTHORED 2026-08-07, Machine A `Dev` (Fable-5 author lane, $0).** 14-beat V2 map,
`v2_prompt.py --check` PASS, windows contiguous+monotonic 0.400→56.831 (=card_start),
onsets in-window, audio OK. Picture-only rebuild — do NOT re-voice.

---

## COMPLAINT LEDGER (LEARNING LAW — one line per open complaint, what fixes it)

**OPEN complaint (the whole spec):** *"Regenerate this video about Stephen in Acts 7
from a Latter-day Saint perspective. The vision scene (Acts 7:55-56) must clearly
show two distinct glorified personages in radiant heavenly light: God the Father and
His Son Jesus Christ standing at the Father's right hand... separate embodied beings...
not one figure, not Jesus only, no dove or Trinitarian symbol... reverent, luminous
style like official Latter-day Saint gospel art... keep it simple, milk-level,
Christ-centered... focus on Stephen full of the Holy Ghost, his bold testimony, the
vision of the Father and Son, his martyrdom, and his forgiving prayers."*

**What in this cut fixes it:**
- **The vision (b05 + b07)** now shows **TWO distinct, separate, embodied, glorified
  personages** — God the Father AND His Son Jesus Christ **STANDING at the Father's
  right hand** — in brilliant radiant white light, reverent and luminous like the
  Latter-day Saint Gospel Art Book. `GLORIFIED-FATHER` and `GLORIFIED-SON` are locked
  as two separate men (Father: white hair/beard, radiant white robe; Son: the
  canonical warm Middle-Eastern face, dark hair/beard, radiant white robe, on his own
  feet at the Father's right). **NO merged figure, NO Jesus-only, NO Father-only, NO
  dove/triangle/eye/cross/Trinitarian symbol** — hard-banned in every vision
  `must_not_show`. b04 builds to it (Stephen looks up), b06 lands on Stephen declaring.
- **Milk, simple, Christ-centered:** the map follows the exact arc Cameron named —
  full of the Holy Ghost + testimony (b01-b02), looks up (b03-b04), the vision
  (b05-b07), rejected/rushed out (b08-b09), face of an angel (b10), martyrdom by
  restraint (b11), and the two forgiving prayers (b12 "lay not this sin to their
  charge", b13-b14). No extra doctrine, no heavy emphasis.
- **Reverent LDS art feel:** radiant white robes, brilliant heavenly radiance (worded
  as "radiant/luminous/brilliant white light" — the drift-word gate bans the literal
  words halo/glow, so the light is in the SKY, never a ring around a head).

**The review card MUST tell Cameron, in plain words:** *"The vision now shows the
Father and the Son as two separate glorified beings, the Son standing at the Father's
right hand — done in the reverent Latter-day Saint gospel-art style you asked for."*

---

## ⚠️ AUTHOR NOTE — DELIBERATE FATHER EMBODIMENT (do not "correct")

This row is the ONE deliberate exception to the "God/the Father is never embodied"
gate, by Cameron's explicit filed instruction. The Father IS shown (glorified,
embodied, radiant) in b05/b07 — because that is exactly what Stephen saw and exactly
what Cameron asked for. **Un-embodying the vision, merging the two, showing Jesus
only, or adding a dove RE-OPENS the complaint.** Logged as numbered lesson 15 in
V2-REBUILD-RUBRIC.md this session so no future pass reverts it. (CONTENT-CARE.md's
numeric table is the THE-200 catalog, where #179 is the fiery furnace — a different
story — so it is left untouched.) Everywhere ELSE in this row there is no divine
figure.

---

## 🅿️ RUNNER — do this (picture-only build on the locked audio)

1. **Audio:** default AUDIO LOCK stream-copy (V1 mp4 2026-07-29 already carries the
   speaker-law voices; all segs 44100/128k new-voice). No `AUDIO_FROM_V1_SEGMENTS`,
   no re-voice.
2. **Places are NEW — promote-first (lesson 11):**
   - `COUNCIL-CHAMBER` → generate **b01** first, QC it, then
     `v2_stash.py --promote build-179-stephens-witness COUNCIL-CHAMBER <b01 frame>`,
     and generate b02/b03/b04/b06/b08 with the plate attached.
   - `OUTSIDE-WALLS` → generate **b09** first, QC it, then
     `--promote ... OUTSIDE-WALLS <b09 frame>`, generate b10-b14 with the plate.
   - **IGNORE the `--wire` "NEW PLACE" suggestion for `THE-MOB`** — it is a CAST/crowd
     text lock, NOT a location (same as row 175's NATIONS-PILGRIMS). Do not promote a
     place plate for it.
3. **The vision (b05, b07)** carries no plate and no image REF — it is the two
   glorified figures by text lock. Generate carefully; the pass bar is Cameron's
   complaint: two plainly SEPARATE glorified persons, Son standing at the Father's
   right, radiant white, no dove/symbol. Reroll here first if any frame merges them,
   drops one, or reads as one figure.
4. **RESTRAINT LAW on b09-b14 (martyrdom):** parent test every frame — no stone
   striking, no wound, no blood, no gore. Weight on Stephen's peaceful/forgiving face.
   If a reroll starts adding a struck body or blood, that frame fails.
5. **Face/beard/scale boards** (lessons 2/10/13/14): STEPHEN is the same young
   short-dark-bearded man in all 11 of his frames; the SANHEDRIN elders are distinct
   individuals (not twins) and the same men across b01/b02/b08; the two vision figures
   are ordinary-sized beside each other. Identity-edit drift, then recheck the frame.
6. Assemble (`v2_assemble.py`, AUDIO REBUILD/LOCK must pass), verify captioned length
   ≈ card_start and the two SCRIPTURE captions (s1 b07, s60 b12) render **light-blue**
   (Stephen's words — NOT red, there is no red-letter in this row). Ship with the
   review card above.

---

## Inherited caption/audio desyncs (do NOT try to fix — audio is locked)
- **n3a** delivered audio opens with an extra recap line ("Look, he told them — heaven
  is open, and the Son of man is standing at God's right hand.") not in the caption.
  b08 (council refusing) reads true against both.
- **n3b** delivered audio speaks only the first sentence ("...face of an angel — at
  peace, not afraid."); the caption's second sentence has no audio. b10 pictures the
  first sentence.
These existed in the V1 cut Cameron reviewed; he complained only about the vision.

## Coverage / windows
14 beats, ~4.0 s/pic. Contiguous window starts: b01 0.400 · b02 5.261 · b03 10.304 ·
b04 12.266 · b05 15.734 · b06 20.262 · b07 22.854 · b08 28.918 · b09 34.096 ·
b10 37.334 · b11 42.059 · b12 48.912 · b13 52.842 · b14 54.711 · (hold to card 56.831).

---

## 🅿️ RUNNER PARK → NEEDS-REBUILD (2026-08-13, Opus runner resume, Machine A `Dev`) — STEPHEN IDENTITY/WARDROBE DRIFT across the interior→exterior change. $0, 0 rerolls.

**Already-shipped check FIRST (RUNNER-LESSONS):** no committed V2 mp4; live review card v179 still carries the OLD 2026-07-24 cut (`data-hash e3156507`, no `realistic-v2` wave). Genuine resume, not shipped.

**State at resume:** the dead session had FINISHED generation — all 14 stills (~3 MB each), 3 story_cast portraits (glorified-father / glorified-son / stephen), and both place plates (COUNCIL-CHAMBER, OUTSIDE-WALLS) present + wired. `v2_gen_api --dry-run` = 0 shots pending. It died before assemble/gate/ship.

**FULL-CUT GATE (per-source-frame, all 14) — BLOCKED on identity, NOT shipped.** Two visibly different Stephens across the video (Stephen is the human spine, so this reads immediately):
- **On-lock-ish YOUNG cluster (council interior):** s01, s02, s03, s04, s05(kneeling), s06, s08, s14 — ~20 yo, short/patchy LIGHT beard, plain oatmeal one-piece tunic, no clear mantle.
- **OFF-LOCK OLDER cluster (outdoor martyrdom):** s09, s10, s11, s12, s13 — ~30 yo, FULL dark beard, **CREAM tunic + brown mantle**. The cream tunic directly violates the STEPHEN LOCK ("oatmeal-and-brown … NEVER cream") and the per-beat `must_not_show: no cream robe`.
- Net: age (~20 vs ~30), beard (light-patchy vs full-dark), and wardrobe (oatmeal one-piece vs cream+brown-mantle) all flip at the s08→s09 location change, and the CLOSING shot s14 flips back to the young look — a face-board failure Cameron would flag ("that's not the same man"). FACE-BOARD LAW = blocks reviewer publication.

**Root cause:** `REFS = {}` — Stephen is TEXT-LOCK ONLY (no image ref wired to any beat). The committed `CAST-REF-V2/stephen.jpeg` was made by `v2_story_cast` but never attached, and the portrait itself is ~30 in a CREAM tunic (also off the "young/never-cream" lock). With no image anchor, the model rendered a young oatmeal Stephen indoors and an older cream+mantle Stephen outdoors. Blind `--redo` of the same beat text would re-drift (RUNNER-LESSONS continuity lesson) — this is a BEAT/LOCK fix, not a generation fluke, and pinning a ref is an author-lane edit the runner may not make. Consistent regen = 5–8 frames, far over the 15% COST-LAW reroll budget.

**WHAT IS GOOD — DO NOT TOUCH ON REBUILD (preserve, save credits):**
- **The vision (s05, s07) NAILS Cameron's open complaint** — TWO plainly separate glorified personages: God the Father (white hair/beard, radiant white robe) on the left, the Son (canonical V2 Jesus face: dark wavy hair, full dark beard, warm olive skin, radiant white robe) STANDING at his side; NO merge, NO Jesus-only, NO Father-only, NO dove/triangle/symbol; radiant light in the sky (no head-halo); reverent LDS gospel-art feel. Keep both frames exactly.
- s01–s06, s08 (council) + s14 (fell asleep) are the YOUNG cluster and are internally consistent + on the wardrobe color — treat the young look as canonical.
- Restraint held on martyrdom (s09–s13): stones in hand / raised fists at a distance, NO stone striking, NO wound, NO blood, NO gore.
- Realistic/photoreal throughout, no modern objects, elders distinct (no twins), no lens-stare, scale ordinary.

**AUTHOR-LANE FIX (minimal-cost, touch-once):**
1. Generate ONE on-lock STEPHEN reference — ~30, warm olive-tan, short dark brown hair + SHORT dark beard, undyed **oatmeal-and-brown** rough-wool tunic AND mantle, **NEVER cream** — and wire it into `REFS` for every STEPHEN beat (or add a committed CAST sheet so the token auto-attaches). Reconcile the lock's "young" vs "about thirty" wording so the ref is unambiguous.
2. Delete ONLY the off-model outdoor stills **s09, s10, s11, s12, s13** (bring them to the young/oatmeal canonical Stephen: age down to match the council, kill the CREAM tunic → oatmeal, keep the brown mantle, keep restraint). Keep s01–s08, s14 and BOTH vision frames.
3. Re-run the plain runner (skips the kept frames), FULL-CUT GATE the regens against the council Stephen as the face-board anchor, then assemble + ship.

**Audio untouched** (default stream-copy from the 2026-07-29 V1 mp4). **Board:** State RUNNING → NEEDS-REBUILD, claim cleared for the author lane. No card change (old cut stays where it is; the redo is not ready).

---

## ✅ AUTHOR-LANE FIX DONE (2026-08-13, Fable-5 author lane resume, Machine A `Dev`, $0) → row set AUTHORED + Ready ✅ for the picture runner

**Full FACE-BOARD (viewed every Stephen frame) — the drift was WORSE than the park logged: at least THREE Stephens.**
- **On-lock (warm olive-tan, dark hair/eyes, short dark beard, oatmeal — canonical):** s03, s10, s14 (and the small-in-frame wides s01/s08). KEPT.
- **Pale drift (light/European skin, light or blue eyes, minimal beard — violates "warm olive-tan, NEVER fair"):** s02, s04, s06.
- **Cream-wardrobe violation (cream robe + brown mantle, some also pale or older):** s09, s11, s12, s13.
- **Vision (s05/s07):** GOOD — the two separate glorified personages that answer Cameron's complaint. KEPT untouched.

**Author fix applied ($0, no generation):**
1. **Pinned an on-lock STEPHEN image ref** — root cause was `REFS = {}`. Cropped two head-and-shoulders portraits from the delivered on-model frames — `STEPHEN-REF/stephen-front.jpeg` (from s10, frontal) + `STEPHEN-REF/stephen-quarter.jpeg` (from s03, three-quarter): warm olive-tan skin, dark hair, dark eyes, short dark beard, oatmeal-and-brown tunic. Wired into `REFS["STEPHEN"]` (a list = two angles). `cast_refs_for()` now attaches this face to every beat whose `locks` name STEPHEN, so every regen converges on ONE man. Committed (force-added; `assets/` + `CAST-REF-V2/` are gitignored).
2. **Tightened the STEPHEN lock** — reconciled the age to "about thirty," added hard bans the drift needed: NEVER pale/fair/European complexion, NEVER blue/grey/green/light eyes, NEVER cream/white/bleached cloth; "the reference portrait IS his face and outranks these words."
3. **Deleted ONLY the 7 off-model stills** for regen — s02, s04, s06, s09, s11, s12, s13. Kept the 7 on-lock frames (s01, s03, s05, s07, s08, s10, s14) + both place plates + the vision.

**`v2_prompt.py --check` = PASS (14 beats).** `v2_gen_api --dry-run` = exactly **7 shots pending, est ~$0.94** (kept frames skipped, COST LAW). Audio still default stream-copy (untouched).

### 🅿️ RUNNER — remaining work (fresh runner lane, complaint-first)
1. `v2_gen_api build-179-stephens-witness` regenerates the 7 deleted frames ONLY — the STEPHEN ref auto-attaches (`[+char ref: STEPHEN:...]` in the log). Reroll any regen that still drifts off the ref face/wardrobe or breaks RESTRAINT (b09-b13 martyrdom: no stone striking, no wound, no blood).
2. **FULL-CUT GATE** the whole cut against the pinned ref as the face-board anchor — all 14 Stephen frames must read as the SAME olive-tan short-dark-bearded man in oatmeal-and-brown (never cream), the vision two-personages preserved, the two SCRIPTURE captions (s1 b07, s60 b12) light-blue not red.
3. Assemble (AUDIO LOCK), deploy, live-verify. **Review card MUST tell Cameron:** *"The vision now shows the Father and the Son as two separate glorified beings, the Son standing at the Father's right hand — done in the reverent Latter-day Saint gospel-art style you asked for."* (Stephen is now one consistent man across the whole video.)
