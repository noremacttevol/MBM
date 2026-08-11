# QC / RUNNER HANDOFF — build-84-no-room-manger (Luke 2:1-7)

Lesson-12 + complaint-corpus pass done 2026-08-05 (Machine A). `--check`
PASSES, zero WARNs. 34 beats, ~191 s.

## THE NATIVITY CAST — anchors for the whole block (84-87)

- MARY here is ~18 (her lock) — the YOUNG mother. She must NOT use row
  49's mother-Mary canon (that Mary is ~50). This row's approved young
  Mary becomes the NATIVITY-BLOCK canon: rows 85 (shepherds), 86 (wise
  men) and 87 (boy in temple, Mary ~30 — aged between, family
  resemblance) anchor to her. Note her canonical frame here when
  approved.
- JOSEPH likewise seeds 85/86/87.
- THE CHILD is a NEWBORN: jesus=False on every beat (already authored
  so) — the adult face ref never applies; no halo on the child, ever.

## Coverage shape

Four true wides with stated geometry: b01 (the imperial decree hall),
b05 (the journey's true size — the tiny pair on the switchback), b08
(the town's fullness in profile), b29 (the two facts — dark hill, one
lit cave, from the side). Fourteen flips including FIVE person-free
frames (b13 stable inventory, b27 rooftops, b31 star sky, b34 closing
cave mouth, b25 cave-at-edge) — phantom people in the star frames
would be uninvited angels.

## Laws

- NO ANGELS in this row (the narration doesn't summon them — they
  belong to row 85). "Heaven's answer" is the brilliant star + deep
  starfield only.
- The birth is never depicted — the row cuts to the already-swaddled
  child (content-care, already authored).
- The MANGER is a wooden feed-trough on legs — never a crib, never
  decorative (row-7 class).
- Direction (row-83): Nazareth → Bethlehem southward journey one
  direction; the door-search works DOWN the lane; the pointing arm
  (b11) aims at the town's edge where the cave is.
- The donkey and ox are the SAME animals across frames (row-11
  same-boat class, barnyard edition).
- Time arc: day → dusk → lamplit night → deep night, one direction.
- TOWN wired from build-38 (generic limestone hill town, light-
  compatible). STABLE promote-first from b13 — its approved frame
  seeds ROW 85's stable scenes directly.

---

## RUNNER QC + SHIP (2026-08-07, Machine A `Dev`, resumed stranded row)

**COMPLAINT LEDGER: none open.** `v2_outline.py 84` shows NO Cameron complaint
on this row (AUTHOR-BOARD Compl=0). Nothing to answer; this is a fresh
first-attempt V2 cut.

**Resume:** prior lane died at 13/34 stills (s01–s13). This session generated
b14–b34 (v2_gen_api resumes automatically; s01–s13 never re-pulled — COST LAW).

**Light-QC pass (all 34 frames viewed once against must_show/RUNNER-LESSONS):**
- Row gates all held: NO angels (s31 shows only the brilliant star = heaven's
  answer); birth never depicted (cuts to the already-swaddled child); manger is
  a wooden feed-trough on legs in every frame (never a crib); newborn child
  jesus=False with NO halo anywhere; same ox + grey donkey across frames; time
  arc day→dusk→lamplit→deep night reads correctly; lamps sit on wicks; only Mary
  (blue) + Joseph (brown/wool) — no second cream robe (Jesus is the newborn, not
  shown as an adult, so no cream in the row).
- **3 rerolls (8.8% of 34 beats — under the 15% COST-LAW budget), all
  modern-object fails (RUNNER-LESSONS row-71 modern-road + modern-town class):**
  - **s05** journey wide — reroll: original had a prominent graded modern
    switchback road cutting the hills. New take = a worn desert footpath, period.
  - **s27** "the town slept on" (person-free rooftops) — reroll: original was a
    present-day town (rooftop plastic/black water tanks + solar heater panels).
    New take = a period limestone stone-block town at night, no modern gear.
  - **s29** "every crowded house" — reroll: original was a modern hillside town
    (concrete block houses, rooftop water tanks, a garage door). New take = a
    period adobe/mud-brick Bethlehem hillside above the cave, clay jars, no
    modern objects.
- No collage, no cartoon/CGI-mix frame, no burned-in text, no lens-stare, no
  giant/shrunken figures, no extra limbs. Plate frames (TOWN, STABLE) QC'd
  first — period-correct on the kept frames (s14/s25) and on the two rerolls.

**Spend this session:** 21 stills + 3 rerolls = 24 images ≈ **$3.21**
(meter 426.79 → 430.01). Under the $6.10/row average even counting the resume.

---

## QC-VERIFY → QC-FIX 2026-08-11 (Machine A `Dev`) — caption/audio mismatch + still-window drift

**FULL-CUT GATE** (PROMPT-OPUS-RUNNER §6b) run before Cameron's eyes: extracted one
frame per beat from the RENDERED mp4 (per-beat window midpoints) + caption-band crops.

**COMPLAINT LEDGER: none open** (`v2_outline.py 84` shows no filed complaint).

**PICTURES: all 34 stills + question card CLEAN** — realistic biblical photography
throughout, no cartoon/mixed frame, Mary (blue) and Joseph (brown) locked and
consistent, newborn wears no halo, no second cream robe (no grown Jesus in this row),
period oil-lamps only, correct night lighting, correct anatomy, no modern objects, no
lens-stare, no collage. Scripture captions blue (sv1, v7), narrator white. **Zero
picture rerolls needed.**

**TWO ASSEMBLY DEFECTS found and fixed (assembly-only, $0, audio byte-identical):**

1. **Caption text did not match the spoken audio on n1, n6, n7.** The V1
   `make_narration.py` script was TIGHTENED after the ElevenLabs voices were cut, so
   `extract_beats` fed the caption filter the newer, shorter script while the shipped
   mp3s speak the older, fuller take. Transcription-confirmed (faster-whisper small.en):
   - n1 caption showed *"A command issued in a distant palace reached all the way into
     two ordinary lives in Nazareth"* but the audio speaks *"In those days a decree went
     out from Caesar Augustus, the emperor in far-off Rome, that the whole known world
     should be counted and taxed. And so every family in the land had to pack up and
     travel to the town their ancestors came from, to be registered."*
   - n6 and n7 the same class (audio richer than the tightened script).
   All three were the ONLY mismatched segments (n2–n5, n8–n12, sv1, v7 verified matching).
   FIX: declared `TEXT_OVERRIDES = {"n1":…, "n6":…, "n7":…}` in beats_v2.py with the
   genuinely-spoken text (the assembler's sanctioned mechanism; V1 never edited).

2. **Still-windows were scaffolded on the stale/short (tightened-script) timeline.**
   beats_v2 windows ended at 190.68 s but the live audio's card_start is 217.408 s
   (~27 s short) → the picture track ran ahead of the narration and s34 froze ~33 s
   while n10/n11/n12 played. AUDIO REBUILD/LOCK PASS never checks video length (row-74
   lesson). FIX: remapped all 34 `window` values onto the live extract_beats per-segment
   slices (preserved intra-segment split ratios; last beat → card_start), row-42/89 method.

**Re-assembled:** AUDIO LOCK PASS `SHA256=af5b5cbcd414aec40488adfb7d487cdce4894984146bd36a537dc47f556f4961`
— **byte-identical to the shipped audio** (no re-voice; all segments are the same
ElevenLabs batch, confirmed via audio-eleven.log + identical mtimes). New mp4 md5
`4dc426f29e7bda26d5767c06edd54a7e`, total 229.63 s, video_silent 229.70 s (no tail truncation).

**Re-gated the rendered mp4** at sv1/n1/n2/n4/n6/v7/n7/n8/n10/n11/n12 + card: every
still + caption + spoken word now agree; the s34 freeze is gone; the question card is
clean. **Cost: 0 rerolls, 0 images, $0** (assembly-only).
