# Story 37 Realistic V2 QC — The Rich Man and Lazarus (Luke 16:19-31)

Final: `luke-16_rich-man-lazarus.mp4` — 1080×1920 H.264, 30 fps, **165.372 s**, 22,153,426 bytes.

- 49 realistic 9:16 pictures at native 2K (1536×2752), against V1's **EIGHT** — one of
  which V1 REUSED.
- **AUDIO LOCK PASS, verified independently of the assembler's own report.** The finished
  cut's audio stream MD5 (`634404ebcc21fc6c2c70f514b42d874a`) is byte-identical to the V1
  MP4's. Nothing re-voiced, re-timed or shortened; V1 never written to.
- **44 windows of true digital silence below −60 dB** — narration plus intentional
  silence, no music or tone bed.

## What V1 actually did (verified from the artefact, not the prose)

- `s5.jpeg` held **33.0 s** — 44.708 s to 77.693 s — carrying the rich man's death and
  burial, his waking in torment, the WHOLE red-letter plea of Luke 16:24 ("Father
  Abraham, have mercy on me… for I am tormented in this flame") and the sight across the
  gulf. Four distinct events and the longest red-letter line in the video on one image.
- `s6.jpeg` held **32.0 s** (77.693–109.681) **and was then REUSED** for 133.452–143.640.
  So Abraham's final answer — "neither will they be persuaded, though one rose from the
  dead", the line the whole parable exists to deliver — was shown on a picture the viewer
  had already stared at for half a minute. **The climax had no picture of its own.**
- `s7.jpeg` held **23.8 s** across the five brethren and "They have Moses and the prophets".
- `s8.jpeg` held **21.5 s** — the entire closing application on one image.

All nineteen spoken segments now have their own pictures: 49 over 156.525 s =
**3.19 s/picture**, shortest 1.75 s, longest 4.82 s.

## The sourcing trap on this row — it was live

`make_narration.py` is **newer than its own audio** (2026-07-28, the day after the mp3s)
and that commit says "narration re-recorded". It **rewrote n13**, from three sentences to
"Because the day is still yours — for now." A script that post-dates its audio cannot be
trusted, so all twenty segments were transcribed with faster-whisper and compared against
the LIVE script. **The audio carries the short n13 (2.586 s)** — the live script is the
one that matches the shipped audio. Three apparent differences were chased down and every
one is whisper's:

- n7 "Across a vast divide" came back as "He crossed a vast divide" from **both** small.en
  and medium.en. Settled from the word timings rather than by opinion: whisper's "He"
  spans 0.000–0.140 and "crossed" 0.140–0.380 — one 380 ms word "Across" split in two at
  the unstressed leading schwa.
- n0 "who lived side by side" heard as "who live" (the dropped final -d family).
- n12 "Jesus told this to people" heard as "told us to people".

No TEXT_OVERRIDES, no SPEAKER_OVERRIDES.

## Windows

Rebuilt from scratch from `extract_beats` plus measured word timings, never from the
`.timing.json` sidecars (twelve of twenty hold one phrase spanning the whole segment).
Contiguous **0.000 → 156.525** (the card's own start), zero gaps, and all nineteen speech
onsets land inside the window written for them. Each interior split sits 0.15 s before the
onset of the word it belongs to.

The inherited scaffold was discarded (kept as `beats_v2.py.inherited-scaffold`): 27
pictures at 5.25 s each, **22 dead intervals**, and it covered only 141.750 s of the
156.525 s that need pictures.

## Content care — the one story in the 200 whose narration goes past death

Every other row in this wave was told to paint no heaven, hell, angel, soul or torment
*because the narration does not state it*. Luke 16 states it outright, so the rule became
**stage only what the text says and nothing it does not** — in Latter-day Saint terms, not
medieval Christendom's.

- **The place of torment is separation and thirst, not special effects.** It is the spirit
  world, not the final state: bare cracked sun-baked clay running flat and empty to a far
  horizon under a burning white sky, and **the man is alone in every frame of it**. His
  torment reads on his own face — cracked lips, sweat cutting tracks through dust, eyes
  screwed against the glare. **"I am tormented in this flame" is staged as heat, glare and
  parched air** — a 200 mm shot through boiling heat haze with a false mirage dissolving
  along the horizon — and there is **no fire anywhere in the cut**: no flame, ember, coal,
  smoke, burning ground, molten fissure or red light. No devil, demon, horns, pitchfork,
  chain, cauldron, lake of fire, crowd of the damned, hellmouth, skull or skeleton.
- **Abraham's bosom is nearness and rest**: deep shade under real broad-leaved trees, green
  growing ground, one channel of still clear water, Abraham sitting on a reed mat on the
  ground beside Lazarus — who is whole, clean, mended, his sores simply gone, holding a
  clay cup of water. The comfort of Luke 16:25 is staged as **an old hand resting flat on
  a shoulder**. No clouds, gates, golden streets, harps, wings, haloes, thrones or shafts
  of light. Abraham never sits on a raised seat and never holds a book, key or sceptre.
- **The great gulf is literal geology** — an enormous dry rift of banded limestone dropping
  into shadow with no floor visible, both rims in frame, the far side green and hazy with
  sheer distance. Nothing is built across it: no wall, fence, bridge, stair, rope or veil,
  and no fire in its depths.
- **The angels are two ordinary grown men** in plain indigo and dark umber, carrying
  Lazarus level between them toward the shade. **No wings, no feathers, no haloes, no light
  coming off them.** The risk was removed by geometry rather than prohibition: the camera
  stands behind and above and they walk away from it, so nothing above their shoulders can
  be invented.
- **God is never depicted** as any figure, face, form, light or presence, and **Jesus never
  appears inside the parable** — he is the one telling it.
- **Nobody is a ghost.** Every person in the spirit world is solid, opaque, fully clothed,
  standing on real ground and casting a real shadow.
- **Lazarus keeps his dignity and cannot be mistaken for Christ.** His sores are dry,
  healed-over and confined to shins, calves and knees — never bleeding, and never on the
  hands, wrists, tops of the feet, side or brow — and he wears only dark cloth with short
  hair and a short beard (the row-31 lesson). The rich man is never a fat, jewelled,
  sneering caricature; he is composed and self-assured, which is what makes his
  indifference at the gate land.

## Who carries which red-letter line

**All five** red-letter segments are characters speaking *inside* the parable, not Jesus
speaking as himself: j3 is the RICH MAN, and j1, j4, j5 and j2 are all ABRAHAM. Putting
Jesus's face under a caption of a man begging from torment, or under Abraham's refusal,
would invert the line — so every one is staged where the words are actually said. Jesus is
on screen only in the three frames the narration puts him in (b01, b46, b48).

## Staging — six places, none repeating the wave

The **fig court** where Jesus tells it (row 36 used a rooftop, 33 a rock-cut stair, 34 a
lone terebinth, 35 a Pharisee's dining room); the rich man's **dining room** at his daily
feast; his **gateway** and the dust outside it; the **hillside tombs**; the spirit world's
**place of rest**; and its **place of torment** with the **great gulf**.

## Rerolls and the cures — 4 of 53 = 7.5%

1. **The rich man's anchor came back with a glazed window carrying a timber sash upright.**
   PERIOD-MATERIALS' "no glass of any kind" does not reach it, because a window is
   *architecture*. Cured by front-loading the opening geometry positively in the RICH-HOUSE
   lock and **deleting the opening from the anchor frame entirely** (the row-35/36
   delete-the-object rule), applied preventively to every house beat before they generated.
2. **Abraham's anchor came back on bare arid stony hillside** instead of the place of rest,
   which would have broken continuity against all eight other rest frames. Cured by stating
   the rest region's ground positively in the beat text.
3. **and 4. `s35` and `s42` came back with EIGHT and SIX men** against a narration that says
   "my **five** brothers" — a COUNT-AS-GEOMETRY violation — and s35 also had two men looking
   down the lens. The cause was my own prompt: "the camera shoots past the two nearest men"
   plus "the three beyond" was read as *additive* rather than as the same five. Cured by
   **geometry, not prohibition**: the near side of the table is now stated as empty of
   people, the camera sits behind the bare tabletop so the foreground is filled by wood and
   clay rather than bodies, and all five are ranged along the far side and the two ends with
   a visible gap between each. Both came back correct in one pass, and the lens gaze went
   with the re-stage.

All three anchors were regenerated composition-level (delete + withheld REFS + fresh
generation), **never `--redo`**. Per the row-35 lesson, frames generated before each cure
were re-inspected in the same pass; the house cure landed before any other house beat
generated, and the count cure is beat-local (no other beat names a number).

## New shared locks added to `v2_prompt.py`

- **SPIRIT-WORLD** — states both regions of the Luke 16 spirit world positively and refuses
  both Dante's inferno and painted-heaven kitsch. Nothing above it reaches these, because
  they are *theology*, not furniture. Belongs in the shared recipe because the doctrine
  rules recur even though Lazarus-and-Dives imagery does not.
- **COURTYARD-GATE** — "gate" pulls a wrought-iron estate gate, and row 36 hit the same
  defect from the other side and cured it by *deleting* a gateway, which this story cannot
  do. States the first-century gateway positively: a square-topped rectangle in a mud-brick
  wall, two dressed jambs, one flat lintel, a pivot-socket timber leaf. Gates and doorways
  recur across the 200.

## Captions

Extracted frames inspected: captions drawn in the **bottom band only**, never over the art
and never clipped — **white** for the narrator, **red** for all five parable speeches. This
build has no scripture-framing segment, so no light-blue caption appears. The closing card
carries its words inside the frame on the cream card.
