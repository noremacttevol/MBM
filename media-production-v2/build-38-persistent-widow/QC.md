# Story 38 Realistic V2 QC — The Persistent Widow (Luke 18:1-8)

Final: `luke-18_persistent-widow.mp4` — 1080×1920 H.264, 30 fps, **180.100 s**, 21,859,309 bytes.

- 46 realistic 9:16 pictures at native 2K (1536×2752), against V1's **SEVEN** used
  (an eighth, `s7b-heard-at-once.jpeg`, was generated and never placed at all).
- **AUDIO LOCK PASS, verified independently of the assembler's own report.** The finished
  cut's audio stream MD5 (`342818e9f3a8bede951e5d6b3121cd38`) is byte-identical to the V1
  MP4's. Nothing re-voiced, re-timed or shortened; V1 never written to.
- **30 windows of true digital silence below −60 dB** — a measured inter-segment gap
  (6.3–7.4 s) reads mean −90.3 dB / max −64.7 dB against −16.8 dB mean during speech.
  Narration plus intentional silence, no music or tone bed.

## What V1 actually did (verified from the artefact, not the prose)

- `s7-the-good-father.jpeg` held **50.0 s** — 121.781 s to the card at 171.743 s. The whole
  of the red-letter Luke 18:8 ("I tell you that he will avenge them speedily… shall he find
  faith on the earth?"), the quiet closing question, **and the entire two-segment closing
  application the video exists to deliver**, all on one image. Nearly a third of the running
  time on a single frame.
- `s1-widow-alone.jpeg` held **29.4 s** (0.000–29.448): Luke's stated purpose, the
  narrator's framing, and the whole introduction of the widow.
- `s6-praying-heard.jpeg` held **25.2 s**, swallowing the entire "how much more will your
  Father" contrast the parable turns on.
- `s5` held 24.1 s, `s2` 13.6 s, `s4` 13.0 s, `s3` 10.6 s.

All fifteen spoken segments now have their own pictures: 46 over 171.743 s =
**3.73 s/picture**, shortest 2.72 s, longest 4.85 s.

The inherited scaffold was discarded (kept as `beats_v2.py.inherited-scaffold`): 29 pictures
at 5.7 s each, windows **not contiguous and not even in time order** (its sixth entry
declared 58.13–59.46 between windows ending 27.80 and starting 28.41), and it covered only
to 164.94 s of the 171.743 s that need pictures.

## The sourcing trap on this row — checked and clear

By GIT CONTENT DATE (mtimes are worthless here), `make_narration.py` is 2026-07-23T04:35:31
and every one of the sixteen mp3s **and** the delivered MP4 share one later commit,
2026-07-27T23:15:18 ("REDO #38: new voice + pacing"). The script PRE-dates its own audio,
which is the safe direction — but all sixteen segments were transcribed with faster-whisper
anyway and every one matches the live script. One apparent difference and it is whisper's:
n7 "Here is the whole point" came back as "Here's the whole point", the contraction family
rows 29 and 31 both chased down. **No TEXT_OVERRIDES, no SPEAKER_OVERRIDES.**

## Windows

Rebuilt from scratch from `extract_beats` plus measured whisper word timings, never from the
`.timing.json` sidecars. Contiguous **0.000 → 171.743** (the card's own start), zero gaps,
and every one of the fifteen speech onsets lands inside the window written for it. Each
interior split sits 0.15 s before the onset of the word it belongs to.

## Who carries which red-letter line — this row's sharpest content question

There are four red-letter segments and they do **not** all belong on Jesus's face:

- **jv2 (18:2-3)** is Jesus setting the scene, and its last clause is **the widow's own
  sentence**. Staged inside the parable: the judge carries "which feared not God", and
  **"Avenge me of mine adversary" is on the widow saying it**.
- **j1 (18:4-5)** is **the unjust judge talking to himself**. Putting Jesus's face under a
  caption of a godless man admitting he fears no God would invert the line completely — all
  three of its pictures are the judge, alone in his own chamber.
- **j2 (18:6-7)** and **jv8 (18:8)** *are* Jesus speaking as himself, so those are his.

Jesus is on screen only in the nine frames the narration or the verse puts him in, and he
never appears inside the parable.

## Content care

Luke 18:1-8 narrates no heaven, hell, angel, soul, death or punishment, so none is painted.
**God is never depicted** as any figure, face, form, light or presence — the contrast is an
ordinary Judean village father in his own doorway, in daylight, with no light coming off him
and a lock that forbids long loose hair so he can never read as Jesus either. The husband is
dead before the story opens and stays off camera: he is present only as one folded mantle
she keeps. The judge is **cold, never a grotesque** — a caricature would let the viewer off
the hook. The widow is **dignity itself**: worn, steady, never cowering, never weeping on
camera.

## Staging — four places, none repeating the wave

An **olive-press yard** where Jesus tells it (row 37 used a fig court, 36 a rooftop, 35 a
Pharisee's dining room, 34 a lone terebinth, 33 a rock-cut stair) — a *working* yard with a
stone crushing basin, an edge-runner stone, a beam press and oil-stained clay jars, dust and
crushed olive on the listeners' hands; the **city-gate judgment chamber** and the sunlit
square outside it; the **widow's one bare room**; and the **good father's doorway**.

**The row's visual engine:** the four n4 beats are ONE composition at FOUR HOURS of the same
day-after-day — first light, hard midday, a dust-wind afternoon, and the last of the light
going all the way down to the threshold stone her feet have worn hollow. The camera never
moves; only the light, the shadow direction and the dust change. That repetition IS the
picture, and it is the one thing V1's single still could not do.

## Rerolls and the cures — 7 of 53 = 13.2%

All seven were regenerated **composition-level (delete file + fresh generation), never
`--redo`**.

1. **b03 — Jesus backlit into a bright hair fringe.** The prompt said the sun sat behind the
   camera's shoulder; the render put it behind *him*, which is the rim-light/halo law. Cured
   by stating the light geometry as a second governing rule — sun in front, wall behind him
   darker than he is — rather than by re-forbidding the halo.
2. **b10 — the worst frame in the row, four violations at once.** The widow came back as a
   *different woman*: young, pale, European-looking, in a tailored floor-length cloak with a
   shawl collar, **looking straight down the lens**, under an **arch of dressed voussoirs**,
   with a hinged door and a modern rendered building beyond. The char_ref alone did not hold
   her at that distance. Cured by **geometry, not prohibition**: the camera was moved to
   **right angles to the judge–widow axis** so the two face each other across the frame and
   both are in strict profile — which kills the lens gaze structurally — plus a full identity
   restatement in the beat's own text and a positive statement of the square-topped, empty
   opening.
3. **b11 — setting drift.** "Avenge me of mine adversary" was rendered in her own
   mud-plastered house instead of the court. Cured by stating the chamber positively (dressed
   limestone blocks, worn flags) and naming the domestic objects that must not appear.
4. **and 5. b17 and b19 — the montage broke its own premise.** The four returns are supposed
   to be one fixed composition, but b18 and b16 rendered the opening in **dressed limestone**
   while b17 and b19 rendered it in **mud plaster with a timber door frame**. Cured by
   pinning the opening's material positively and saying in the beat text that it is *the same
   opening in all four pictures*. b19 additionally had **her pupils dead on the lens**; cured
   by re-staging it as a strict side-on profile with the far eye hidden behind the bridge of
   the nose, so the pose itself makes the lens gaze impossible.
6. **b32 — a brass frame buckle on a sandal**, the exact row-35 defect, invisible until
   cropped in. The shared SANDAL-CONSTRUCTION lock already states how a strap fastens and
   still lost. **The object was deleted instead of described again**: he is barefoot in his
   own house, which his lock already allowed.
7. **b46 — the closing image inverted its own line.** The door rendered half-shut across the
   opening (with iron nail heads and a handle) under the caption "he has been waiting to hear
   from you all along". **The door leaf was deleted entirely** (the row-36/37 rule) — the
   doorway is now a clear rectangle with the first light lying through it on the floor
   inside.

Per the row-35 lesson, the frames generated *before* each cure were re-inspected in the same
pass; the montage cure is beat-local to b17/b19 and the b18/b16 frames it had to match were
the ones already correct.

## New shared lock added to `v2_prompt.py`

- **JUDGMENT-SEAT** — "judge", "court", "courtroom" and "hearing" are among the most
  modern-loaded nouns in English and pull an English or American courtroom: a panelled bench,
  a gavel, a wig and gown, a dock, a jury box, a blindfolded statue of Justice. **Nothing in
  the shared recipe reached it**, for exactly the reason a road surface, a prison cell and a
  barn slip through — a courtroom is *architecture and furniture*, not an object a household
  makes by hand, and ANCIENT-PRISON covers where a man is *held*, not where he is *heard*.
  States the gate chamber, the plain stone seat and the standing petitioners positively:
  the judge sits and everyone else stands on the same floor with nothing between them, which
  is the whole social picture the parable turns on. Judgment recurs across the 200 (the woman
  taken in adultery, Pilate's judgment seat, the Sanhedrin, "agree with thine adversary
  quickly").

## Captions

Extracted 24 real frames from the delivered file and looked at them. Captions are drawn in
the **bottom band only**, never over the art and never clipped: **light blue** for the Luke
18:1 scripture framing, **white** for the narrator, **red** for every parable speech — and
each red line sits on the person who actually says it. The closing card carries its words
inside the frame on the cream card.
