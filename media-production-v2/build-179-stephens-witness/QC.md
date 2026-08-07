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
