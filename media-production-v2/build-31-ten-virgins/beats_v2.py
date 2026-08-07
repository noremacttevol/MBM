#!/usr/bin/env python3
"""V2 beat map — row 31, build-31-ten-virgins (Matthew 25:1-13), realistic.

COVERAGE: 40 pictures against V1's SEVEN stills, over 140.835 s of story =
3.52 s/picture (rows 24-30 shipped at 3.1-4.9). V1's holds and REUSES:
  * `s5.jpeg` covered n8, j3, n9, j4 AND n10 — 52.006 s -> 85.001 s, THIRTY-THREE
    SECONDS on ONE picture, and that stretch contains BOTH of the middle red-letter
    verses (25:8 "Give us of your oil" and the whole of 25:9 "Not so; lest there be
    not enough for us and you") plus the entire refusal, which is the hinge the
    parable turns on.
  * `s7.jpeg` covered j5, j6, n13 AND n14 — 95.243 -> 114.886, NINETEEN AND A HALF
    SECONDS, i.e. "Lord, Lord, open to us", "I know you not", and the knocking.
  * `s4.jpeg` covered j2, n6 AND n7 (16.2 s) and was then REUSED at j1, the closing
    red-letter verse 25:13, the one line the whole passage exists to deliver.
  * `s1.jpeg` covered n0, n1 AND n2 (16.1 s).
  * THE CLOSING APPLICATION RAN ENTIRELY ON RECYCLED PICTURES: n15 (9.55 s, "the oil
    is the one thing you cannot borrow") reused `s2.jpeg` from n3/n4, and n16 (6.80 s,
    "the door is still open now. Tonight, your lamp can be filled") reused `s6.jpeg`
    from n11/n12. The reason the video exists got no picture of its own at all.

⚠️ THE INHERITED beats_v2.py WAS DISCARDED (git history keeps it). It planned 25
pictures across the same 148.3 s cut = 5.93 s/picture and called that the library
density. It is not: rows 24-30 shipped at 3.1-4.9 s/picture, and row 30 — the
immediately preceding row, and the wave's best at a 2.4% reroll rate — shipped at
3.68. A 5.93 s scaffold is the V1 hold problem in a smaller size.

AUDIO IS CLEAN AND LOCKED (checked from the FILES, not from prose):
  * `matthew-25_ten-virgins.mp4` and EVERY one of the twenty-four `audio/*.mp3` last
    changed bytes at the SAME commit, 2026-07-27T22:53:38 (git CONTENT dates — mtimes
    are worthless in this repo, four machines pull it). No placed mp3 is newer than the
    MP4, so `assert_v1_final_is_current()`'s recency tripwire has nothing to refuse,
    and the V1 stream runs 148.306 s against the summed timeline (148.302 s), inside
    the 0.75 s guard. Nothing is re-voiced and V1 is never written to.
  * SOURCING TRAP CHECKED AND CLEARED. All TWENTY-FOUR segments were transcribed with
    faster-whisper `word_timestamps=True` and every one matches the LIVE
    `make_narration.py` word for word. FIVE apparent differences were chased down and
    every one is whisper's, not the audio's:
      - n2  "into the dusk" heard as "into the dust", and "meet him" as "meet them"
            on small.en — the dropped/flipped final consonant family (row 30 saw
            fishermen->fisherman, the bad->the bat).
      - n4  base.en heard "their lamps — but no extra oil" as "their lamps ON but";
            small.en returns "their lamps, but", so the "on" was base.en filling the
            em-dash pause. The script text is what is spoken.
      - n14 base.en heard "told THEM why he had shared THIS story" as "told HIM ... THE
            story"; small.en returns the script exactly, word for word.
      - j4  "not enough for us AND you" heard as "for us IN you" on BOTH models — an
            unstressed "and" reduced to a schwa. The KJV text is what is spoken.
      - n16 "And here IS the good news" heard as "here's" on BOTH models. Row 29 hit
            this identical contraction and reached the same conclusion; the caption
            law renders the script text either way.
    So NO `TEXT_OVERRIDES` are needed on this row and `AUDIO_FROM_V1_SEGMENTS` stays
    off.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with `extract_beats.py` reading the V1
build, then split inside each segment on WORD timings measured from that segment's own
mp3 with faster-whisper. THE `.timing.json` SIDECARS WERE NOT TRUSTED and could not
have been used anyway — every one of the twenty-four holds exactly ONE phrase spanning
its whole segment, so no interior split exists in them (the identical trap row 30
documented). Windows are SEGMENT-BOUNDARY CONTIGUOUS (`seg_start` -> the NEXT segment's
`seg_start`, never `audio_start` -> `spoken_end`), so there is no dead gap at any of the
twenty-two segment joins: contiguous 0.280 s -> 141.115 s (the card start), zero gaps,
zero overlaps, shortest window 2.00 s, longest 4.91 s. Every split lands on a clause
head or a sentence boundary and none falls inside a word.

SCRIPTURE (Matthew 25:1-13 KJV, the verses the cut actually voices):
  v6   "And at midnight there was a cry made, Behold, the bridegroom cometh; go ye
        out to meet him."                                                      -> j2
  v8   "And the foolish said unto the wise, Give us of your oil; for our lamps are
        gone out."                                                             -> j3
  v9   "But the wise answered, saying, Not so; lest there be not enough for us and
        you: but go ye rather to them that sell, and buy for yourselves."      -> j4
  v11  "Afterward came also the other virgins, saying, Lord, Lord, open to us." -> j5
  v12  "But he answered and said, Verily I say unto you, I know you not."      -> j6
  v13  "Watch therefore, for ye know neither the day nor the hour wherein the Son
        of man cometh."                                                        -> j1

CAMERON'S OWN STANDING NOTE ON THIS ROW, from the V1 approval in QUEUE.md, is treated
here as a build law rather than a nicety: *"should be exactly 10 virgins in every
picture (5 with extra oil vases, 5 without)"*. So in EVERY beat where the group
appears, exactly ten young women stand in the frame and no eleventh, each separated by
a clear gap of dark ground so all ten can be counted, and THE JAR IS THE SIGNAL: each
of the five wise carries a small round clay oil jar in her free hand or slung at her
hip, and each of the five foolish has a visibly EMPTY free hand and no second vessel
anywhere on her. That single geometric difference is what lets a viewer tell the two
groups apart with no caption, and it is why the TEN lock enumerates all ten women
individually — age, face, hair, head cloth and tunic — rather than describing "five
wise and five foolish" as two interchangeable blocks.

⚠️ THE LIGHTING IS THE HARD PROBLEM ON THIS ROW AND IT IS WHY A NEW SHARED LOCK EXISTS.
Matthew 25:6 is MIDNIGHT and the only light in the parable is the thing the parable is
about, so TIME-OF-DAY LAW and the no-halo/no-rim-light law collide in literally every
frame: a flame carried near a face is the single most reliable way to get a bright ring
of light around a head, and it arrives by PHYSICS rather than by the prompt asking for
it. A prohibition does not beat physics. `NIGHT-LAMPLIGHT` (promoted into
`v2_prompt.py` SHARED_SETTING_LOCKS by this row) beats it with GEOMETRY instead, per
the row-10/row-14 lesson: every flame is LOW AND IN FRONT of the person it lights,
below the chin and NEARER THE CAMERA THAN THE HEAD, so light can only travel upward
onto the front planes of the face while the crown, the back of the head and the
shoulders stay unlit and merge into the night. It also pins the fixture — a shallow
closed terracotta lamp with a pinched spout and one bare wick, small enough to sit in a
cupped palm — because when the lamp is the SUBJECT rather than set dressing the model
reaches for a glass hurricane lantern or a candle, and PERIOD-MATERIALS' one clause on
flames is not loud enough to stop it.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  rows 2, 8, 21 (Luke 15)      courtyard table / low wall under a fig / house meal
  row 11 (the storm)           an open boat at NIGHT in a gale
  row 16 (Mary & Martha)       a lamplit evening INTERIOR
  row 19 (breakfast on shore)  a Galilee beach at FIRST LIGHT with a charcoal fire
  row 22 (unmerciful servant)  a black basalt Capernaum doorstep and street
  row 23 (vineyard workers)    a terraced hillside above a vineyard
  row 24 (the sower)           a MOORED fishing boat off a daylit SHINGLE beach
  row 25 (wheat and tares)     an open grain plain and a round threshing floor
  row 26 (mustard seed)        a small walled kitchen garden
  row 27 (the leaven)          a synagogue-wall stone bench and a walled baking yard
  row 28 (hidden treasure)     an olive grove / a walled stony field / a mud-brick yard
  row 29 (the pearl)           a limestone shelf above a dry wadi / a caravan road /
                               a quayside market / a dressed-stone courtyard
  row 30 (the net)             a boulder breakwater / open deep water / a sand strand
The two rows this could collide with are 11 and 16, the wave's only other night and
lamplight rows, and both were checked deliberately. Row 11 is a NIGHT GALE on OPEN
WATER — weather, spray and a boat. Row 16 is an INTERIOR, indoors, walls on four sides.
This row is staged in FOUR places, none of them used above and none of them either of
those:
  * THE FRAME — a bare rocky shoulder of the MOUNT OF OLIVES, in CLEAR LATE AFTERNOON,
    with a deep dry valley falling away below and bare tawny hillside rising beyond
    it. NO CITY IS SHOWN (see the re-stage note below). This is
    scripturally exact rather than decorative: Matthew 24:3 seats him on that mountain
    privately with the disciples, and chapter 25 runs straight on from it. It is
    distinguished from row 23's terraced hillside (defined by cultivation and vine
    terraces) and from row 29's limestone shelf (defined by an empty dry wadi) by being
    a HIGH OPEN SHOULDER above a deep dry valley with bare tawny hill rising beyond it —
    no vines, no terraces, no wadi floor, and deliberately no grove, because row 28 owns
    the olive canopy.
    ⚠️ NO CITY IS SHOWN, AND THAT IS A DELIBERATE RE-STAGE, NOT AN OVERSIGHT. The frame
    was first written with Jerusalem hazed across the valley, which is scripturally
    exact (Matthew 24:3) and was the thing that made this staging unique. It had to go.
    Naming "Jerusalem", "city wall" and "temple platform" while standing on the Mount of
    Olives reproduces the modern tourist photograph taken from that exact viewpoint, and
    the model rendered PRESENT-DAY Jerusalem twice: the Al-Aqsa dome, a minaret, Ottoman
    crenellated battlements and modern multi-storey blocks along the ridge. The lock had
    already forbidden every one of those BY NAME and lost, and a second attempt that
    beat it with geometry (pushing the ridge so far off that no building could be
    resolved) still came back with the dome, the minaret and the crenellations. Two
    failures is the stop rule: the object was DELETED from the lock and from every frame
    beat's prose rather than described a third time, and the far side of the valley is
    now bare hillside with nothing built on it anywhere.
  * THE FORECOURT — a wide open packed-earth forecourt outside the bridegroom's house,
    a low dry-laid limestone wall down one side and the blank windowless mud-brick
    backs of village houses closing the other, at DUSK and then in FULL NIGHT. It is
    outdoors, unroofed and unlit except by the ten lamps, so it is neither row 16's
    interior nor row 22's dressed black basalt street.
  * THE GATEWAY — a deep timber-lintelled gateway in the courtyard wall with heavy
    double leaves of adzed plank, the wedding courtyard beyond it warm with lamplight
    while everything outside it is black; and then the same gateway SHUT.
  * THE LANE — the empty packed-earth village track the foolish run down looking for
    oil, shuttered houses either side, at midnight (`ANCIENT-ROAD`, `MARKET-TOWN`).

THE CLOCK IS THE PLOT AND IT IS ON THE SCREEN. The parable's light only ever moves
forward, from last light down into full midnight dark; the frame's hour NEVER changes:
  b01 b33 b34 b35 b37 b40   THE FRAME — CLEAR LATE AFTERNOON on the Olivet shoulder,
                            the sun still well up and OUT OF FRAME, warm but NOT
                            golden-hour and NEVER a sunset. Identical in all six.
  b02-b08                   DUSK in the village — the last cold blue light draining
                            from a clear sky, no sun disc, no orange horizon, the ten
                            lamps just lit and already the brightest thing in frame.
  b09-b10                   EARLY NIGHT — the sky fully dark and starred, lamps set
                            down on the ground burning low beside the sleepers.
  b11-b27                   MIDNIGHT — the deepest dark in the video. Only the lamps,
                            and at b26/b27 the wedding party's pitch torches and the
                            warm spill from the open gateway.
  b28-b32                   MIDNIGHT, outside the SHUT gateway — the five foolish now
                            carrying freshly-lit lamps (they did reach the sellers;
                            that is the whole grief of it) plus one thin line of warm
                            light escaping under the shut door at ground level.
  b36 b38 b39               MIDNIGHT emblem beats and the gateway standing open again.

REVERENCE — THE BRIDEGROOM IS NOT PAINTED AS CHRIST (the row-21/row-30 precedent, that
the symbol is rendered concretely and the meaning is left to land). He is a real
first-century bridegroom of about thirty-five with his own locked face, in DARK
saturated wool, and he is never given Jesus's face, never dressed in cream, and never
lit or framed like him. Jesus appears ONLY in the six frame beats, always with the
JESUS-V2-REF image attached and LOCK v5 in the prompt, and he never enters the parable.
"""

LOCKS = {
    # ------------------------------------------------------------- places ----
    "OLIVET": (
        "OLIVET LOCK: this is the bare western shoulder of the Mount of Olives and it "
        "is IDENTICAL in every frame-story picture. Underfoot is a broad ledge of pale "
        "grey weathered limestone breaking through thin dry ground, tufted with "
        "bleached summer grass and small stones, with a few low grey boulders worn "
        "smooth enough to sit on. There is NO tree, NO grove, NO canopy, NO vine, NO "
        "terrace wall and NO building anywhere on this slope — it is open bare rock and "
        "dry grass, and the sky is wide above it. The ground falls away steeply beyond "
        "the ledge into a deep dry valley, and the far side of that valley rises again "
        "as BARE OPEN HILLSIDE: pale tawny rock, thin dry summer grass, scattered low "
        "scrub and loose stone, hazed with distance. THERE IS NO CITY IN THIS PICTURE "
        "AND NO BUILT THING OF ANY KIND ANYWHERE IN IT. Across the valley and along "
        "every ridge there is only bare hill and empty sky: no town, no village, no "
        "city, no wall, no rampart, no battlement, no crenellation, no gate, no tower, "
        "no temple, no dome, no minaret, no spire, no roof, no house, no ruin, no road, "
        "no terrace, no wire and no pole — the horizon is an unbroken line of empty "
        "hillside against an empty sky. "
        "always OUT OF FRAME, the light warm and directional from the low right, "
        "shadows long but not raking, the far city and hills slightly hazed. IT IS "
        "NEVER SUNSET AND NEVER SUNRISE — there is no sun disc, no orange or pink or "
        "red sky, no golden-hour blaze, no colour band along the horizon and no night."
    ),
    "FORECOURT": (
        "FORECOURT LOCK: the open packed-earth forecourt outside the bridegroom's house "
        "in a small Judean village, and it is the SAME ground in every picture that "
        "uses it. It is a wide flat unpaved yard of hard pale dust scuffed by feet, "
        "open to the sky with NO roof, NO ceiling, NO beam and NO room of any kind — "
        "this is OUTDOORS. Down one side runs a LOW DRY-LAID WALL of rough unmortared "
        "limestone field stones about knee to waist high, with dust and dry weed at its "
        "foot. Closing the far side stand the blank windowless backs of village houses "
        "in tan mud brick and rough stone, FLAT-ROOFED, with plain rectangular door "
        "openings and no glass in anything. A few large fired-clay storage jars stand "
        "against the wall and there is a hand-woven reed basket or two on the ground. "
        "AGAINST THE SKY THERE IS ONLY FLAT ROOFLINE: no dome, no minaret, no bell "
        "tower, no spire, no pitched roof, no roof tile, no shingle, no chimney, no "
        "gable, no half-timbering, no arch of dressed voussoirs, no column with a "
        "carved capital, no corrugated or sheet metal, no aerial, no wire and no cable. "
        "There is no furniture, no bench, no table, no chair and no step of cut stone."
    ),
    "GATEWAY": (
        "GATEWAY LOCK: the entrance to the wedding courtyard, the SAME structure every "
        "time. It is a deep rectangular opening in a thick wall of tan mud brick over a "
        "rough limestone footing, spanned by ONE massive squared timber lintel of "
        "adzed, unpainted, unvarnished wood — a plain post-and-lintel opening, never an "
        "arch, never a keystone, never a moulding, never a carved jamb. Filling it hang "
        "TWO heavy door leaves built of wide vertical adzed planks pegged to three "
        "cross battens, the wood grey and split with age, swinging on hand-cut wooden "
        "pivot posts set into stone sockets top and bottom. THERE IS NO METAL HARDWARE "
        "ANYWHERE ON THE DOOR: no hinge, no strap, no stud, no nail head, no boss, no "
        "handle, no knocker, no lock, no latch plate, no ring and no bolt of "
        "manufactured metal; the only fastening is a plain squared timber drawbar "
        "resting in wooden brackets on the inside face. The threshold is one worn slab "
        "of limestone. Nothing is carved, painted, inscribed or lettered."
    ),
    "LANE": (
        "LANE LOCK: a narrow village track running away between houses, the SAME lane "
        "every time. It is bare packed earth and pale dust worn hollow down the middle "
        "by feet and hooves, with loose stones kicked to the sides and bedrock breaking "
        "through in places. Either side stand the blank tan mud-brick and rough-stone "
        "walls of FLAT-ROOFED village houses, their plain rectangular door openings "
        "shut with plank doors and their window openings small, high and unglazed. The "
        "lane bends out of sight so its far end is lost in darkness. AGAINST THE SKY "
        "THERE IS ONLY FLAT ROOFLINE: no dome, no minaret, no bell tower, no spire, no "
        "pitched roof, no tile, no chimney, no gable, no aerial, no wire, no cable and "
        "no pole of any kind."
    ),
    # ------------------------------------------------------------- people ----
    "TEN": (
        "TEN-VIRGINS LOCK: EXACTLY TEN YOUNG WOMEN AND NO ELEVENTH PERSON stand in this "
        "frame. They are unmarried village girls and young women of first-century "
        "Judea, aged roughly sixteen to thirty, each a DIFFERENT individual human being "
        "with her own face, age, build, hair and colours — no two share a face, no face "
        "is cloned or repeated, and not one of them is a generic bystander. They are "
        "spaced with a clear gap of dark ground between them so that all ten can be counted one by one. THE COUNT IS THE WHOLE POINT OF THIS PICTURE, SO IT IS BUILT AS FIVE PLUS FIVE AND NEVER AS ONE UNDIFFERENTIATED TEN. The women stand in TWO CLEARLY SEPARATE GROUPS OF FIVE with a band of empty dark ground between the two groups: FIVE women in one group, FIVE women in the other group, five and five, ten in all. Count the first group — one, two, three, four, five, and no sixth. Count the second group — one, two, three, four, five, and no sixth. Within each group of five the women are staggered at clearly different distances from the camera, some nearer and larger and some further and smaller, so each of the five is separated from her neighbours by visible dark ground and none overlaps or hides another. THE PICTURE IS TALL AND NARROW, so the two groups are placed one nearer the camera and one further away, up into the depth of the frame, and the ten are NEVER strung out in a single straight horizontal line across the narrow width. THE WHOLE GROUP FITS COMFORTABLY INSIDE THE FRAME WITH ROOM TO SPARE: there is clear empty ground beyond both ends of it, and NOT ONE WOMAN IS CUT, CLIPPED, SLICED OR RUN OFF BY ANY EDGE OF THE PICTURE. ALL TEN ARE GROWN YOUNG WOMEN between about sixteen and thirty — there is NO CHILD, no little girl, no boy, no man and no older woman anywhere in the frame, and no eleventh person of any kind at any edge, in the background, behind a figure or out of focus. EXACTLY TEN LIT LAMPS: every single one of the ten has her own clay lamp with its own flame, so there are ten separate flames in the picture and nobody is empty-handed. EXACTLY FIVE CLAY OIL JARS AND NO SIXTH — all five jars belong to the five wise, and not one jar appears anywhere near the other five women. EVERY ONE OF THE TEN CARRIES HER OWN SMALL CLAY OIL LAMP, and the ONE "
        "difference a viewer must be able to see at a glance is THE SECOND VESSEL: each "
        "of the FIVE WISE also carries a SMALL ROUND FIRED-CLAY OIL JAR, about the size "
        "of two fists, with a narrow neck and a stopper of rolled cloth, held in her "
        "free hand or slung against her hip on a twisted cord — five jars, plainly "
        "visible and individually countable. Each of the FIVE FOOLISH has a VISIBLY "
        "EMPTY FREE HAND and carries NO second vessel of any kind, no jar, no flask, no "
        "skin and no pot, anywhere on her body or at her feet. "
        "EVERY SEPARATE PIECE OF CLOTH ON ALL TEN IS A DARK SATURATED COLOUR — tunic, "
        "sleeves, sash, head cloth and any wrap or shawl alike — and NOTHING ANY OF "
        "THEM WEARS IS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE "
        "OR PALE. Each wears an ankle-length straight woven wool tunic with straight "
        "sleeves, a twisted cord or folded-cloth sash at the waist, and a head cloth "
        "whose LOOSE END IS DOING SOMETHING VISIBLE so it can never be dropped from the "
        "picture. All are barefoot or in plain leather sandals. "
        "THE FIVE WISE, each with a lamp AND a jar: (1) the eldest of the wise, about "
        "thirty, a strong square face and steady dark eyes, black hair pinned up off "
        "her neck, a DARK INDIGO head cloth with its loose end knotted under her chin, "
        "a DARK CHOCOLATE-BROWN tunic. (2) a calm, still young woman of about twenty "
        "with a long oval face, warm brown eyes and thick dark brown hair in ONE heavy "
        "plait falling forward over her LEFT shoulder, a DEEP RUST-RED head cloth with "
        "its loose end thrown back over her right shoulder and hanging down her back, a "
        "DARK OLIVE-GREEN tunic. (3) about seventeen, round-faced and soft-jawed, mid "
        "brown hair loose to her shoulders, a DEEP PLUM head cloth pinned at the left "
        "temple with its end falling to her elbow, a DARK TEAL-BLUE tunic. (4) about "
        "twenty-five, tall and thin with high cheekbones and a long neck, black hair in "
        "TWO plaits, a DARK WALNUT-BROWN head cloth wound close and tucked at the nape, "
        "a DEEP MAROON tunic. (5) about nineteen, a broad freckled face and reddish "
        "brown hair, a DARK OCHRE-GOLD head cloth with its end wrapped once round her "
        "throat, a DARK INDIGO tunic. "
        "THE FIVE FOOLISH, each with a lamp and an EMPTY free hand: (6) about eighteen, "
        "a small heart-shaped face with wide-set dark eyes and a full mouth, black "
        "curly hair escaping in loose coils at her temples, a DARK MOSS-GREEN head "
        "cloth slipping back off the crown of her head with its end over her left "
        "forearm, a DEEP RUST-BROWN tunic. (7) about twenty-two, sharp-featured with a "
        "thin straight nose and a narrow chin, straight dark brown hair, a DEEP "
        "BURGUNDY head cloth drawn close over the brow, a DARK GREY-BROWN tunic. (8) "
        "the youngest of the ten, about sixteen, small and slight with a round "
        "childlike face, black hair, a DARK SLATE-BLUE head cloth with its end held "
        "bunched in her fist, a DARK OLIVE tunic. (9) about twenty-four, broad-faced "
        "and heavy-browed with thick mid-brown hair, a DARK CHARCOAL head cloth folded "
        "flat across the top of her head, a DEEP TERRACOTTA-BROWN tunic. (10) about "
        "twenty, a long neck and a narrow face, black hair in a low knot at the nape, a "
        "DARK BROWN-PURPLE head cloth with its long end hanging straight down her "
        "front, a DARK BRONZE-GREEN tunic."
    ),
    "WISE-LEAD": (
        "WISE-LEAD LOCK: she is the SAME young woman as the attached reference "
        "photograph of her, and these are invariants that hold even when she is small, "
        "distant, in shadow or out of focus — she is woman (2) of the five wise. A calm, "
        "still Judean young woman of about twenty. Her face is a long clean oval with a "
        "smooth broad forehead, level dark brows, warm brown eyes set wide apart, a "
        "straight narrow nose and a soft unsmiling mouth; her skin is warm light olive, "
        "clear, with a faint sunburn across the nose and cheekbones. Her hair is thick "
        "dark brown, parted in the centre and drawn into ONE heavy plait that falls "
        "FORWARD over her LEFT shoulder to below the collarbone, with a few loose "
        "strands at the temple. Her hands are small, brown and work-roughened, the "
        "nails short. EVERY SEPARATE PIECE OF CLOTH ON HER IS DARK AND SATURATED: an "
        "ankle-length DARK OLIVE-GREEN smooth flat close-woven wool tunic with straight "
        "sleeves to the wrist, a twisted DARK BROWN cord sash at the waist, and a DEEP "
        "RUST-RED head cloth whose LOOSE END IS THROWN BACK OVER HER RIGHT SHOULDER and "
        "hangs down her back. She wears no scarf, stole, shawl, wrap or mantle of any "
        "other colour, and nothing she wears is cream, off-white, ivory, buff, beige, "
        "taupe, sand, khaki, white or pale. She carries a small clay oil lamp, and a "
        "small round clay oil jar with a rolled-cloth stopper. HER CLOTH IS THIN, FLAT AND SMOOTH-SURFACED, a fine close plain weave that hangs in soft limp folds and shows only a faint over-and-under thread grid at very close range. IT IS NOT A KNITTED OR CHUNKY FABRIC: no knit or purl stitch, no rib, no cable, no bouclé, no nubbly or bumpy surface, no thick spongy pile, no ribbed or banded collar, cuff or neckline, and nothing on her anywhere resembles a sweater, jumper or hand-knitted garment. Her neck opening is a plain cut slit in the cloth with no band, binding or collar of any kind. "
    ),
    "FOOLISH-LEAD": (
        "FOOLISH-LEAD LOCK: she is the SAME young woman as the attached reference "
        "photograph of her, and these are invariants that hold even when she is small, "
        "distant, in shadow or out of focus — she is woman (6) of the five foolish. A "
        "quick, open-faced Judean girl of about eighteen. Her face is small and "
        "heart-shaped, wide at the cheekbones and narrow at the chin, with large "
        "wide-set very dark brown eyes under fine arched brows, a short straight nose "
        "and a full mouth; her skin is warm mid-brown, smooth, still childlike at the "
        "jaw. Her hair is black and tightly curling and escapes her head cloth in loose "
        "coils at both temples and at the nape. Her hands are small and thin. EVERY "
        "SEPARATE PIECE OF CLOTH ON HER IS DARK AND SATURATED: an ankle-length DEEP "
        "RUST-BROWN smooth flat close-woven wool tunic with straight sleeves, a folded DARK "
        "BROWN cloth sash at the waist, and a DARK MOSS-GREEN head cloth that has "
        "SLIPPED BACK OFF THE CROWN OF HER HEAD, its loose end lying over her LEFT "
        "FOREARM. She wears no scarf, stole, shawl, wrap or mantle of any other colour, "
        "and nothing she wears is cream, off-white, ivory, buff, beige, taupe, sand, "
        "khaki, white or pale. HER CLOTH IS THIN, FLAT AND SMOOTH-SURFACED, a fine close plain weave that hangs in soft limp folds and shows only a faint over-and-under thread grid at very close range. IT IS NOT A KNITTED OR CHUNKY FABRIC: no knit or purl stitch, no rib, no cable, no bouclé, no nubbly or bumpy surface, no thick spongy pile, no ribbed or banded collar, cuff or neckline, and nothing on her anywhere resembles a sweater, jumper or hand-knitted garment. Her neck opening is a plain cut slit in the cloth with no band, binding or collar of any kind. She carries a small clay oil lamp and NOTHING ELSE — her "
        "other hand is EMPTY and there is no jar, flask, skin or second vessel anywhere "
        "on her or at her feet."
    ),
    "BRIDEGROOM": (
        "BRIDEGROOM LOCK: he is the SAME man as the attached reference photograph of "
        "him, and these are invariants that hold even when he is small, distant, in "
        "shadow or out of focus. HE IS NOT JESUS AND MUST NOT RESEMBLE HIM: a "
        "broad-shouldered Judean householder of about thirty-five with a SQUARE "
        "heavy-jawed face, a short blunt nose, deep-set dark brown eyes under thick "
        "straight brows, and weathered mid-brown skin. His hair is black, THICK AND CUT "
        "SHORT at the nape and above the ears, pushed back off a low forehead — never "
        "long, never loose, never falling to the shoulders. His beard is black and "
        "CROPPED CLOSE to the jaw, never long and never flowing. EVERY SEPARATE PIECE "
        "OF CLOTH ON HIM IS DARK AND SATURATED: a knee-length DEEP BURGUNDY-RED "
        "hand-woven wool tunic with straight sleeves, a broad folded DARK BROWN cloth "
        "sash wound twice at the waist, and a DARK INDIGO mantle over ONE shoulder "
        "whose loose end is caught up under the sash. On his head is a plain woven "
        "DARK INDIGO head cloth wound close over his short black hair with its loose end falling over his left shoulder. HIS HEAD CARRIES NO WREATH, GARLAND, CIRCLET, DIADEM, BAND, CROWN OR HEADPIECE OF ANY KIND, and nothing of leaves, twigs, branches, briar or thorn is on or near his head anywhere. NOTHING HE "
        "WEARS IS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE OR "
        "PALE, and he has no halo, no glow, no rim-light and no light coming off him."
    ),
    "PARTY": (
        "WEDDING-PARTY LOCK: the bridegroom's companions are ordinary village men and "
        "women walking with him, six to ten of them, of mixed ages, every one a "
        "different face. EVERY SEPARATE PIECE OF CLOTH ON EVERY ONE OF THEM — tunic, "
        "sleeves, sash, head cloth, mantle, wrap or shawl — IS A DARK SATURATED COLOUR "
        "drawn from deep indigo, dark brown, deep rust, dark olive, charcoal, deep "
        "maroon and dark teal. EVERY SCARF, WRAP, STOLE AND HEAD CLOTH IS AS DARK AS THE TUNIC UNDER IT — there is no light olive, sage, pale grey, grey-green, oatmeal, stone or bleached scarf, wrap, stole or head cloth on anybody. NOT ONE PERSON IN THE PARTY WEARS CREAM, OFF-WHITE, "
        "IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE OR ANY PALE CLOTH, including at "
        "the blurred edges of the frame and on figures out of focus. Two or three of "
        "them carry PITCH TORCHES: a rough wooden stave bound at the head with resinous "
        "rag and fibre, burning with one ragged smoky orange flame, carried LOW and at "
        "arm's length OUT TO THE SIDE, never raised above anybody's head."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the listeners are a small closed circle of ordinary "
        "first-century Galilean working men, weathered and sun-darkened, of mixed ages "
        "from about twenty to about fifty-five, each with his own distinct face, build, "
        "hair and beard — no two alike and no face cloned. EVERY SEPARATE PIECE OF "
        "CLOTH ON EVERY ONE OF THEM — tunic, sleeves, sash, head cloth, mantle, wrap, "
        "shawl or stole — IS A DARK SATURATED COLOUR drawn from deep indigo, dark "
        "umber-brown, deep rust, dark olive-drab, charcoal and deep maroon, and NOT ONE "
        "OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE "
        "OR ANY PALE CLOTH ANYWHERE, including on figures at the blurred edges of the "
        "frame and out of focus. Jesus is the only person in the picture in a pale "
        "garment. They sit low on the rock, listening, and none of them is haloed, "
        "rim-lit or glowing."
    ),
}

OUTPUT_ASSET_DIR = "assets"

# C-FIX 2026-08-07 (Machine A) — flipped to True. Cameron's OPEN complaint: the
# shipped mp4 "stops playing and will not play through the 1:59 mark ... i can skip
# past it and it will play but its not playing correctly." Diagnosis: the shipped
# mp4's muxed AAC stream carries a corrupt packet ("channel element 1.4 is not
# allocated / Invalid data") that stalls browser playback exactly as described; the
# video stream and every source audio/*.mp3 decode CLEAN. Separately the current
# summed timeline is 141.0 s while the mp4 runs 148.3 s (shared gap constants
# shortened since the 2026-08-02 render), so the packet-copy AUDIO LOCK would refuse
# on the >1.0 s guard anyway. The sanctioned remedy (row 25 / row 61) is to rebuild
# the authoritative track from THIS build's own clean mp3s at the extract_beats
# offsets — nothing is re-voiced, re-timed, or resynthesised, so the narration is
# byte-identical in content; only the corrupt AAC encode is replaced with a clean one.
AUDIO_FROM_V1_SEGMENTS = True

REF = True

# Filled in AFTER the three anchor beats are generated in their own run. v2_gen_api
# builds this cache once per invocation, so an anchor cannot be referenced by a beat
# generated in the same run as itself. ANCHOR ORDER: b15 (WISE-LEAD), b17
# (FOOLISH-LEAD), b26 (BRIDEGROOM) — each a face-showing beat that is itself a real
# placed picture on the timeline, so the anchors cost nothing extra.
REFS = {
    "WISE-LEAD": "assets/s15-they-burned-warm-and-bright.jpeg",
    "FOOLISH-LEAD": "assets/s17-they-had-no-oil-left.jpeg",
    "BRIDEGROOM": "assets/s26-the-bridegroom-arrived.jpeg",
}

_NO_JESUS = ("no Jesus in this frame; no bare rocky hillside, no open dry valley and "
             "no late-afternoon daylight; ")
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white or "
             "pale garment, cloth, shawl, wrap, stole or head covering on anybody "
             "anywhere in the frame including the blurred edges; ")
_NO_DAY = ("no sun, no sun disc, no daylight, no sunrise, no sunset, no dawn, no dusk "
           "band, no orange or pink horizon and no warm glow along any skyline; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no glow, no rim-light, no bright "
            "outline, edge or contour around any head, hair, shoulder or body, and no "
            "light source of any kind standing behind, above or beyond anyone's head; ")
_NO_MODERN_LAMP = ("no candle, wax or taper, no glass, chimney, globe or shade, no "
                   "hurricane lamp, storm lantern, kerosene lamp or oil lantern, no "
                   "metal lamp, no hanging fixture, no ring handle, and no electric "
                   "light of any kind; ")
_GAZE = "nobody's pupils centred on the lens."

_NIGHT = ["NIGHT-LAMPLIGHT"]

BEATS = [
    # ============ FRAME — the Olivet shoulder, clear late afternoon ============
    {
        "id": "v2-r031-b01", "out": "s01-a-story-about-ten.jpeg",
        "seg": "n0", "window": "0.280-3.853", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "Jesus told a story about ten young women waiting for a wedding.",
        "must_show": "Jesus seated on a low limestone boulder on the bare Olivet shoulder with his small closed circle of disciples sitting low on the rock around him, the dry valley falling away behind and the bare tawny far hillside rising beyond it, with no town or building anywhere in the picture, in clear late-afternoon light.",
        "must_not_show": _NO_HALO + "no night, no lamp, no flame, no fire, no sunset, no sunrise and no golden low sun; no tree, no grove, no canopy, no vine, no terrace and no building on the slope; no woman, no lamp and no wedding anywhere in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, clear late-afternoon light warm and directional "
            "from the low right, the sun well up and OUT OF FRAME, long soft shadows "
            "reaching left across the pale rock, the far valley and hills slightly hazed, "
            "fine film grain. THE CAMERA IS PLACED COMPLETELY SIDE-ON TO THE WHOLE "
            "CIRCLE, STANDING OUT ON THE ROCK WELL TO ONE SIDE AND SHOOTING ACROSS THE "
            "GROUP AT RIGHT ANGLES TO EVERY EYELINE IN THE PICTURE. Jesus sits at the "
            "RIGHT of the frame on a low grey boulder and the disciples are ranged along "
            "the ledge to the LEFT of him, so the whole conversation runs HORIZONTALLY "
            "ACROSS THE FRAME: his gaze travels leftward into the seated men and exits "
            "through the LEFT EDGE, and every disciple is seen in profile or "
            "three-quarter from behind with a gaze travelling rightward and out through "
            "the RIGHT EDGE. NOT ONE MAN'S FACE IS SQUARED UP TO THE CAMERA AND NOT ONE "
            "PAIR OF PUPILS IS CENTRED ON THE LENS. THIS IS A WIDE FULL-LENGTH GROUP "
            "PHOTOGRAPH AND NOT A PORTRAIT: the camera is far enough back that Jesus AND "
            "at least six seated disciples are in frame together, head to feet, with the "
            "valley and the bare far hillside behind them; Jesus occupies only a "
            "modest part of the picture and is never framed from the chest up. EXACTLY "
            "TWO out-of-focus seated BACKS fill the near bottom corners and they are the "
            "only foreground objects: a DEEP INDIGO shouldered back with a dark indigo "
            "head cloth at the near LEFT and a DARK UMBER back with a dark brown head "
            "cloth at the near RIGHT, BOTH OF THEM A SOLID DARK SATURATED MASS FROM EDGE "
            "TO EDGE. THERE IS NO PALE, IVORY, BEIGE, TAUPE, BUFF, SAND OR LIGHT-TAN "
            "SHAPE, SHOULDER, BACK, SLEEVE, DRAPE OR BLURRED MASS ANYWHERE IN THE "
            "FOREGROUND OR AT ANY EDGE OF THIS PICTURE — the ONLY pale thing in the "
            "whole frame is the wool of Jesus's own robe. Sharp in the middle distance "
            "Jesus sits seen from his left side, forearms on his knees, one hand "
            "beginning to open as he starts to speak."
        ),
    },
    # ================= THE VILLAGE AT DUSK — the custom (n1) ===================
    {
        "id": "v2-r031-b02", "out": "s02-a-whole-village-would-wait.jpeg",
        "seg": "n1", "window": "3.853-7.813", "wide": True, "jesus": False,
        "locks": ["FORECOURT", "MARKET-TOWN"] + _NIGHT,
        "narration": "In those days, a whole village would wait for the bridegroom to come late",
        "must_show": "the whole village waiting in the open forecourt at last light — perhaps twenty villagers of all ages standing and sitting about in loose groups, faces turned toward the dark mouth of the lane the bridegroom will come from, a few small clay lamps already lit among them.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no bride, no bridegroom and no wedding party arriving yet; no torch, no bonfire and no hearth; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, LAST LIGHT — the sky a deep cold blue-grey "
            "draining to near black at the top of the frame with the first stars in it, "
            "the mud-brick walls and the ground read almost entirely as dark shape and "
            "silhouette, and the only warm colour in the picture is the handful of small "
            "lamp flames down among the people. Fine film grain, deep shadow, true "
            "night-photography falloff into black at the edges. THE CAMERA STANDS BEHIND "
            "THE WAITING VILLAGERS, LOW AND CLOSE TO THE GROUND, AND SHOOTS PAST THEM "
            "down the forecourt toward the dark mouth of the lane, so the near people "
            "are seen entirely FROM BEHIND as dark backs, shoulders and head cloths "
            "against the faint light beyond, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "The forecourt opens away from the camera: the low dry-laid limestone wall "
            "runs down the LEFT of the frame, the blank flat-roofed mud-brick house "
            "backs close the RIGHT, and dead ahead at the far end the lane runs out into "
            "total darkness — every villager's body and gaze is aimed that way, into the "
            "depth of the frame and away from the camera. About twenty villagers of all "
            "ages stand and sit in loose scattered groups across the dust, every one of "
            "them in DARK SATURATED wool — deep indigo, dark umber, deep rust, dark "
            "olive, charcoal, deep maroon — with no pale cloth on anyone anywhere. Four "
            "or five small clay oil lamps are held low at waist height or set down on "
            "the ground among the groups, each one a small soft yellow flame that lights "
            "the underside of a jaw, a forearm, a fold of dark wool and a small circle "
            "of pale dust, and NOTHING ELSE — every head in the picture stays dark and "
            "unlit and merges into the night. The sky occupies the top third and is "
            "empty, deep blue-black and starred."
        ),
    },
    {
        "id": "v2-r031-b03", "out": "s03-lead-everyone-in-to-the-feast.jpeg",
        "seg": "n1", "window": "7.813-11.554", "wide": True, "jesus": False,
        "locks": ["GATEWAY", "FORECOURT"] + _NIGHT,
        "narration": "in the evening and lead everyone into the feast.",
        "must_show": "the wedding courtyard being made ready behind the open gateway — warm lamplight spilling out of the deep timber-lintelled opening across the dark threshold and onto the dust outside, two or three villagers carrying jars and baskets in through it, everything outside the doorway black.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no bridegroom and no wedding party yet; no arch, no keystone, no carved jamb, no metal hinge, strap, stud, handle, knocker or ring on the doors; no torch and no bonfire; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep night outside and warm lamplight within. THE "
            "CAMERA STANDS OUT IN THE DARK FORECOURT SEVERAL PACES BACK FROM THE GATEWAY "
            "AND A LITTLE TO ITS LEFT, SHOOTING ACROSS AND SLIGHTLY PAST THE OPENING, so "
            "the two villagers carrying goods in are seen from BEHIND and in three-quarter "
            "from behind as they walk AWAY from the camera into the light, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. The deep rectangular gateway with its one "
            "massive squared timber lintel fills the right-centre of the frame, its two "
            "plank leaves standing open inward. Beyond the threshold the courtyard is "
            "warm and soft with the light of several small clay lamps set LOW on the "
            "ground and on a waist-high mud-brick ledge inside, all of them well below "
            "head height, so the light rakes across the packed floor and up the lower "
            "walls and leaves the upper courtyard and every head in shadow. That warm "
            "light spills out through the opening in one clean wedge across the worn "
            "limestone threshold and onto perhaps two paces of pale dust outside, and "
            "then stops: everything else in the picture — the mud-brick wall, the "
            "forecourt, the sky — is deep blue-black night with stars, lit by nothing. "
            "Two villagers in dark saturated wool, one carrying a large fired-clay jar "
            "against the hip and one a hand-woven reed basket, are walking in through the "
            "opening, their backs to the camera and their bodies dark silhouettes cut "
            "against the warm doorway. No pale garment, cloth or shape appears on anyone "
            "anywhere in the frame. The near foreground is bare dark dust and one low "
            "unmortared limestone wall stone, out of focus."
        ),
    },
    # ============== THE TEN COME OUT — dusk (n2), and the split ================
    {
        "id": "v2-r031-b04", "out": "s04-ten-took-their-lamps.jpeg",
        "seg": "n2", "window": "11.554-16.386", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "So ten young women took their oil lamps and went out into the dusk to meet him.",
        "must_show": "EXACTLY TEN young women walking out across the forecourt into the failing light, each carrying her own small lit clay lamp held low, five of them also carrying a small round clay oil jar and five with an empty free hand, all ten separated so they can be counted.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman and no ninth or twelfth — exactly ten and no other person in the frame; no man, no child, no bridegroom and no villager; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the last cold blue light almost gone from a clear "
            "starred sky, the ground and walls reading as dark shape, the ten small lamp "
            "flames already the brightest things in the picture. Fine film grain, deep "
            "falloff to black. THE CAMERA STANDS OUT IN THE FORECOURT AHEAD OF THE GROUP "
            "AND WELL OFF TO THEIR RIGHT, SHOOTING ACROSS THEIR LINE OF TRAVEL AT RIGHT "
            "ANGLES, so all ten are seen in near PROFILE moving from the RIGHT of the "
            "frame toward the LEFT, every gaze travelling forward along that line and out "
            "through the LEFT EDGE, and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A "
            "WIDE FULL-LENGTH PHOTOGRAPH: the camera is far enough back that all ten "
            "women are in the frame together head to feet. THEY ARE STRUNG OUT IN A LOOSE "
            "UNEVEN LINE ACROSS THE FRAME WITH A CLEAR GAP OF DARK GROUND BETWEEN EACH "
            "WOMAN AND THE NEXT, none overlapping another, so a viewer can count TEN "
            "SEPARATE FIGURES one by one — EXACTLY TEN AND NO ELEVENTH. Each carries her "
            "own small clay oil lamp in one hand, held LOW at waist height and slightly "
            "OUT IN FRONT of her, so each flame lights the underside of that woman's chin "
            "and cheek, her near forearm, and a small pool of pale dust at her feet, while "
            "the crown and back of every head stays completely unlit and dark against the "
            "night. FIVE of the ten also carry a small round fired-clay oil jar with a "
            "rolled-cloth stopper — three held in the free hand, two slung against the hip "
            "on a twisted cord — five jars plainly visible and individually countable; the "
            "OTHER FIVE have a visibly EMPTY free hand swinging at their side and no "
            "second vessel anywhere on them. Every garment in the picture is dark and "
            "saturated. Behind them the low dry-laid limestone wall and the blank "
            "flat-roofed house backs are near-black silhouettes under a deep blue-black "
            "starred sky."
        ),
    },
    {
        "id": "v2-r031-b05", "out": "s05-five-of-them-were-wise.jpeg",
        "seg": "n3", "window": "16.386-19.546", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "Five of them were wise. Along with their lamps,",
        "must_show": "the five wise gathered together on one side of the frame, countable as five, each with her lit lamp low in front of her and her small clay oil jar plainly in hand or at her hip.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no sixth woman in this group — exactly five; no empty-handed woman among these five, every one of them has her jar; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 40mm lens, full dusk gone to night, a deep blue-black starred "
            "sky behind, the five lamp flames the only light. THE CAMERA STANDS TO THE "
            "GROUP'S LEFT AND SLIGHTLY BELOW THEM AND SHOOTS ACROSS THE ARC AT RIGHT "
            "ANGLES TO EVERY EYELINE, so the five are seen in profile and three-quarter "
            "from behind, their attention aimed together toward the dark mouth of the "
            "lane off the RIGHT of the frame, every gaze exiting through the RIGHT EDGE, "
            "and NOT ONE FACE IS SQUARED UP TO THE LENS. THIS IS A WIDE FULL-LENGTH "
            "PHOTOGRAPH: all five stand in the frame head to feet, arranged in a shallow "
            "arc with A CLEAR GAP OF DARK GROUND BETWEEN EACH ONE so a viewer counts "
            "EXACTLY FIVE SEPARATE WOMEN AND NO SIXTH. Each holds her small clay oil lamp "
            "LOW, at waist height and out in front of her body and nearer the camera than "
            "her own head, so the light travels upward onto the front planes of her face "
            "— the underside of the brow, the nose, the chin — and the crown and back of "
            "every head stays dark and merges into the night behind. EVERY ONE OF THE "
            "FIVE ALSO HAS HER SMALL ROUND FIRED-CLAY OIL JAR CLEARLY VISIBLE: two carry "
            "it cradled in the free hand at chest height where the lamplight catches its "
            "curved side, two have it slung against the hip on a twisted cord, one holds "
            "it low against her thigh — five jars, separated and individually countable. "
            "Their garments are dark saturated wool and no pale cloth appears anywhere. "
            "The low limestone wall runs behind them as a near-black line."
        ),
    },
    {
        "id": "v2-r031-b06", "out": "s06-a-small-jar-of-extra-oil.jpeg",
        "seg": "n3", "window": "19.546-22.630", "wide": False, "jesus": False,
        "locks": ["WISE-LEAD"] + _NIGHT,
        "narration": "they each carried a small jar of extra oil.",
        "must_show": "close on the wise lead's hands — her lit clay lamp in one hand and the small round clay oil jar with its rolled-cloth stopper held in the other, the jar's weight and fullness readable.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no glass jar, no bottle, no metal vessel, no cork and no printed or lettered label; no face squared up to the lens; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, very shallow depth of field, deep night with "
            "everything beyond the hands falling away into soft black. A TIGHT WAIST-UP "
            "COMPOSITION FROM HER LEFT SIDE: the camera stands close and low, shooting "
            "ACROSS her body at right angles, so her head is turned well off the camera "
            "axis, seen in near profile with her nose pointed toward the LEFT EDGE and "
            "her gaze travelling down and left onto her own hands and out through that "
            "LEFT EDGE — her pupils never come near the lens. Sharp in the centre of the "
            "frame are HER TWO HANDS, brown, small and work-roughened. The RIGHT hand "
            "holds the small clay oil lamp LOW, at the bottom of the frame and NEARER THE "
            "CAMERA THAN HER FACE, its single small soft yellow flame standing at the "
            "pinched spout, so all the light in the picture climbs UPWARD from below onto "
            "the underside of her wrist, her forearm, her jaw and her cheekbone, and the "
            "top of her head and her hair stay unlit and dark. The LEFT hand is cradled "
            "round a SMALL ROUND FIRED-CLAY OIL JAR about the size of two fists, plain "
            "unglazed terracotta with a narrow neck plugged by a twist of rolled cloth, "
            "held steady against her body, the lamplight raking across its curved "
            "shoulder and showing the faint throwing rings in the clay and a smear of "
            "old oil down one side. Her thick dark brown plait falls forward over her "
            "left shoulder into the frame, dark against dark. Her dark olive-green wool "
            "sleeve and deep rust-red head cloth read as smooth flat close-woven cloth in the "
            "raking light. Everything behind her is unlit black night with two or three "
            "small far lamp flames as tiny soft out-of-focus points."
        ),
    },
    {
        "id": "v2-r031-b07", "out": "s07-the-other-five-were-foolish.jpeg",
        "seg": "n4", "window": "22.630-24.630", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "The other five were foolish.",
        "must_show": "the five foolish gathered on the other side, countable as five, each with her lit lamp low in front of her and every free hand plainly EMPTY — no jar anywhere among them.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no sixth woman in this group — exactly five; NO OIL JAR, FLASK, SKIN OR SECOND VESSEL OF ANY KIND anywhere in this frame, in any hand, at any hip, on the ground or in the background; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 40mm lens, deep night, a blue-black starred sky behind, the "
            "five lamp flames the only light. THE CAMERA STANDS TO THIS GROUP'S RIGHT AND "
            "SLIGHTLY BELOW AND SHOOTS ACROSS THEM AT RIGHT ANGLES TO EVERY EYELINE, so "
            "the five are seen in profile and three-quarter from behind, easy and "
            "unbothered, some looking off toward the lane and some at each other, every "
            "gaze exiting through a side edge of the frame, and NOT ONE FACE IS SQUARED UP "
            "TO THE LENS. THIS IS A WIDE FULL-LENGTH PHOTOGRAPH: all five stand in frame "
            "head to feet in a loose cluster with A CLEAR GAP OF DARK GROUND BETWEEN EACH "
            "ONE so a viewer counts EXACTLY FIVE SEPARATE WOMEN AND NO SIXTH. Each holds "
            "her small clay oil lamp LOW at waist height and out in front of her body, "
            "nearer the camera than her own head, so the light climbs upward onto the "
            "front planes of her face while the crown and back of every head stays unlit "
            "and dark against the night. THE OTHER HAND OF EVERY ONE OF THE FIVE IS OPEN "
            "AND PLAINLY EMPTY — one rests on a hip, one hangs loose at the side, one is "
            "tucked into a sash, one gestures lightly as she talks, one holds the end of "
            "her own head cloth — and THERE IS NO JAR, FLASK, SKIN, POT OR SECOND VESSEL "
            "OF ANY KIND ANYWHERE IN THIS PICTURE, not in a hand, not at a hip, not on a "
            "cord, not on the ground and not in the background. Their garments are dark "
            "saturated wool and no pale cloth appears anywhere. The blank flat-roofed "
            "house backs stand behind them as near-black silhouettes."
        ),
    },
    {
        "id": "v2-r031-b08", "out": "s08-but-no-extra-oil-at-all.jpeg",
        "seg": "n4", "window": "24.630-28.021", "wide": False, "jesus": False,
        "locks": ["FOOLISH-LEAD"] + _NIGHT,
        "narration": "They brought their lamps — but no extra oil at all.",
        "must_show": "close on the foolish lead — her lit clay lamp held low in one hand and her other hand hanging open and unmistakably empty, nothing else with her.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "NO OIL JAR, FLASK, SKIN, POT OR SECOND VESSEL anywhere in the frame, in her hand, at her hip, on a cord, on the ground or out of focus behind her; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, deep night falling away to "
            "soft black behind her. A TIGHT WAIST-UP COMPOSITION FROM HER RIGHT SIDE: the "
            "camera stands close and low and shoots ACROSS her body at right angles, her "
            "head turned well off the camera axis in near profile with her nose pointed "
            "toward the RIGHT EDGE and her gaze travelling out through that RIGHT EDGE "
            "toward the dark lane — her pupils never come near the lens. Her LEFT hand "
            "holds the small clay oil lamp LOW at the bottom of the frame and NEARER THE "
            "CAMERA THAN HER FACE, one small soft yellow flame at the pinched spout, so "
            "the light climbs upward onto the underside of her jaw, her full mouth, the "
            "tip of her nose and the ridge of one cheekbone, catching a few escaped black "
            "curls at her temple from beneath, while the crown and back of her head and "
            "the whole mass of her hair stay UNLIT AND DARK and merge into the night. "
            "Her RIGHT hand hangs open and relaxed at her side, sharp in the frame, the "
            "fingers loose and the palm turned a little forward — EMPTY, carrying "
            "nothing, with no jar, flask, skin, pot, cord or second vessel of any kind "
            "anywhere in the picture, on her body, at her feet or behind her. Her dark "
            "moss-green head cloth has slipped back off the crown of her head and its "
            "loose end lies over her left forearm. Her expression is easy and "
            "untroubled, a young woman with no idea anything is wrong. Her deep "
            "rust-brown wool sleeve reads as smooth flat close-woven cloth in the raking "
            "upward light."
        ),
    },
    # ================= THE DELAY AND THE SLEEP — early night ===================
    {
        "id": "v2-r031-b09", "out": "s09-the-bridegroom-was-delayed.jpeg",
        "seg": "n5", "window": "28.021-31.841", "wide": True, "jesus": False,
        "locks": ["FORECOURT", "LANE"] + _NIGHT,
        "narration": "The bridegroom was delayed, hour after hour slipped by, and",
        "must_show": "the empty dark mouth of the lane with nobody coming — the ten waiting figures small and slumped at the edge of the frame, the night grown long, the sky fully dark and starred.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no bridegroom, no wedding party, no torch and no approaching light in the lane — the lane is empty and black; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, full night now, the sky deep blue-black and thick "
            "with stars, the village walls pure silhouette. THE CAMERA STANDS BEHIND AND "
            "ABOVE THE WAITING WOMEN, LOOKING OVER THEM AND PAST THEM STRAIGHT DOWN THE "
            "LANE, so they are seen entirely FROM BEHIND as dark seated and standing "
            "backs, shoulders and head cloths low across the bottom third of the frame, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. THE SUBJECT OF THE PICTURE IS "
            "THE EMPTINESS: the lane runs away from the camera between the blank "
            "flat-roofed mud-brick house walls and disappears into total black, and there "
            "is NOTHING in it — no figure, no torch, no approaching light, no movement, "
            "just packed dust going grey then going dark then going nowhere. The waiting "
            "women's few lamps are down among them at ground level, small and low, each a "
            "little yellow flame lighting one patch of dust, one hem, one dark forearm "
            "and nothing above shoulder height, so every head in the picture is unlit and "
            "dark. Their postures have gone slack with the hours — one sitting with her "
            "back against the low limestone wall, one with her chin propped on her fist, "
            "one lying on her side. Everything they wear is dark saturated wool and there "
            "is no pale cloth anywhere in the frame. The upper half of the picture is "
            "empty starred sky over a black roofline."
        ),
    },
    {
        "id": "v2-r031-b10", "out": "s10-all-ten-fell-asleep.jpeg",
        "seg": "n5", "window": "31.841-35.760", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "and one by one all 10 women grew drowsy and fell asleep.",
        "must_show": "all TEN women asleep on the ground of the forecourt, countable as ten, their lamps SET DOWN ON THE GROUND beside them burning low, the five wise each with her clay oil jar resting on the dust beside her and the five foolish with nothing beside them.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman — exactly ten; NO LAMP RESTING ON, FIXED TO, HANGING FROM OR STANDING AGAINST ANY WALL — every lamp is on the ground; no bed, no cot, no mattress, no pillow and no furniture; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, a HIGH camera looking DOWN into the forecourt from "
            "about standing head height and off to one side, angled steeply enough that "
            "the flat dust floor fills most of the frame and the sleeping women are laid "
            "out across it like objects on a table. Deep night, the sky reduced to a "
            "narrow starred band at the very top, the walls black. NOT ONE FACE IS "
            "SQUARED UP TO THE CAMERA: every woman is asleep, lying on her side or curled "
            "with her head on her own folded arm or on a rolled fold of her mantle, so "
            "the faces are turned down into the ground, away, or hidden behind an arm, "
            "and EVERY PAIR OF EYES IN THE PICTURE IS CLOSED. THEY ARE LAID OUT ACROSS "
            "THE OPEN DUST WITH A CLEAR GAP OF BARE GROUND BETWEEN EACH SLEEPING BODY so "
            "a viewer counts EXACTLY TEN SEPARATE WOMEN AND NO ELEVENTH. Beside each "
            "woman her small clay oil lamp SITS DIRECTLY ON THE PACKED EARTH, none of "
            "them touching a wall or raised on anything, each burning very low now — ten "
            "small separate yellow flames scattered across the dark floor, each lighting "
            "a little circle of dust, a sleeping hand, a hem of dark wool and the "
            "underside of one cheek, and nothing higher; the tops and backs of all ten "
            "heads are unlit and dark, and there is no rim, edge or outline of light "
            "around any head or shoulder anywhere. Beside FIVE of the sleepers, and only "
            "five, a small round fired-clay oil jar rests on the dust within reach — five "
            "jars, separated and countable; beside the other five there is nothing at all "
            "on the ground but their lamp. Every garment is dark saturated wool and no "
            "pale cloth appears anywhere in the frame. The low limestone wall runs black "
            "along the top of the composition."
        ),
    },
    # ================== MIDNIGHT — the cry (j2, Matthew 25:6) ==================
    {
        "id": "v2-r031-b11", "out": "s11-behold-the-bridegroom-cometh.jpeg",
        "seg": "j2", "window": "35.760-40.605", "wide": True, "jesus": False,
        "locks": ["LANE", "MARKET-TOWN", "ANCIENT-ROAD"] + _NIGHT,
        "narration": "Behold, the bridegroom cometh, go ye out to meet him.",
        "must_show": "the cry going up at midnight — a single runner well down the dark lane, seen from behind, one arm flung up as he shouts ahead of him toward the forecourt, his lamp low in his other hand, the lane black around him.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no crowd, no wedding party and no bridegroom in this frame — one runner only; no torch, no bonfire; no tarmac, kerb, painted line, pole, wire or signpost on the lane; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, THE DEEPEST DARK IN THE STORY — a black midnight "
            "sky heavy with stars, the mud-brick walls of the lane no more than edges "
            "against it, the ground barely readable. THE CAMERA STANDS IN THE LANE BEHIND "
            "THE RUNNER AND SHOOTS PAST HIM: he is seen entirely FROM BEHIND, a dark "
            "back and shoulders and a dark head cloth, running AWAY from the camera into "
            "the depth of the frame, so his face is not visible at all and nothing is "
            "turned toward the lens. He is a village man in dark saturated wool, "
            "mid-stride, his right arm flung UP AND FORWARD in the direction he is "
            "running as he shouts ahead of himself, his head tipped back a little with "
            "the effort. In his LEFT hand, carried LOW and swinging beside his knee — well "
            "below his own head and nearer the camera than it — is a small clay oil lamp "
            "with one whipping yellow flame, and that flame is the only light in the "
            "entire picture: it throws a moving smear of warm light down onto the packed "
            "dust of the lane, up the lower two feet of the wall beside him and onto the "
            "backs of his own calves, and reaches nothing else. His head, his shoulders "
            "and his upper body are UNLIT AND DARK, silhouetted against nothing, with no "
            "bright rim, edge or outline anywhere around them. Far ahead of him the lane "
            "opens into the forecourt, where two or three tiny distant lamp flames sit "
            "small and low and out of focus. The lane surface is bare packed earth and "
            "pale dust with loose stones at the sides. Everything above the lower wall "
            "line is black."
        ),
    },
    {
        "id": "v2-r031-b12", "out": "s12-then-at-midnight-a-cry.jpeg",
        "seg": "n6", "window": "40.605-43.165", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "Then at midnight, a cry rang out.",
        "must_show": "the sleeping women jolted awake by the shout — heads coming up off the ground, eyes opening, bodies still half down, ten of them across the dark forecourt floor.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman — exactly ten; nobody standing yet, they are all still down on the ground; no bridegroom and no wedding party in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, a LOW camera down almost at the level of the dust "
            "and off to one side of the sleeping row, shooting ALONG the line of bodies "
            "rather than at them, so the near women are seen from behind and in profile "
            "and the far ones recede across the frame — NOT ONE FACE IS SQUARED UP TO THE "
            "LENS and every waking gaze is aimed off toward the dark lane mouth at the "
            "LEFT of the frame, exiting through that LEFT EDGE. Deep midnight, the sky a "
            "black starred band at the top. THE MOMENT IS THE JOLT: heads are coming up "
            "off folded arms, one woman is propped on a stiff elbow with her head turned "
            "hard toward the sound, one is half-risen onto one knee, one is still flat "
            "with only her face lifted, several are blinking with their hair loose and "
            "their head cloths slipped — none of them is on her feet yet, every body is "
            "still down on the ground. TEN SEPARATE WOMEN with a clear gap of bare dust "
            "between each and no eleventh. Their ten small clay lamps still sit ON THE "
            "PACKED EARTH beside them, burning very low, each flame lighting a hand, a "
            "jaw from beneath, a fold of dark wool and a circle of dust — the light is "
            "all at floor level and rises no higher, so the tops and backs of all ten "
            "heads stay unlit and dark, with no bright rim or outline around any head, "
            "hair or shoulder. Every garment is dark saturated wool and there is no pale "
            "cloth anywhere. Beside five of them, and only five, a small round clay oil "
            "jar sits on the dust."
        ),
    },
    {
        "id": "v2-r031-b13", "out": "s13-come-out-to-meet-him.jpeg",
        "seg": "n6", "window": "43.165-46.229", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "The bridegroom is coming. Come out to meet him.",
        "must_show": "the ten getting to their feet in a hurry — women rising, gathering skirts, snatching lamps up off the ground, all of them turning toward the dark lane mouth.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman — exactly ten; no bridegroom and no wedding party in this frame yet; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, deep midnight, black starred sky above a black "
            "roofline. THE CAMERA STANDS BEHIND THE WOMEN AND SLIGHTLY TO ONE SIDE AND "
            "SHOOTS PAST THEM toward the dark mouth of the lane, so the whole group is "
            "seen from BEHIND and in three-quarter from behind as they rise and turn away "
            "from the camera, and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE "
            "FULL-LENGTH PHOTOGRAPH with all ten women in the frame head to feet, spread "
            "across the forecourt with A CLEAR GAP OF DARK GROUND BETWEEN EACH so a "
            "viewer counts EXACTLY TEN AND NO ELEVENTH. The action is mid-scramble and "
            "every figure is caught in a different phase of it: one is bent double "
            "reaching down for her lamp on the dust, one is straightening with her lamp "
            "already up at her waist, one has a fistful of her own skirt lifted clear of "
            "her feet, one is pushing herself up off one knee, one is already turned and "
            "taking her first step toward the lane. The lamps are all LOW — in hands at "
            "waist and hip height or still on the ground being reached for, every one of "
            "them below its owner's chin and none above anyone's head — so the light "
            "moves across the dust, up the fronts of skirts and along forearms, and every "
            "head in the picture stays unlit and dark against the night, with no bright "
            "rim, edge, ring or outline around any head, hair or shoulder anywhere in the "
            "frame. Five of the ten also have a small round clay oil jar in hand or being "
            "caught up off the ground. Every garment is dark saturated wool; no pale "
            "cloth appears anywhere."
        ),
    },
    # ============== THE LAMPS — the wise burn, the foolish die =================
    {
        "id": "v2-r031-b14", "out": "s14-reached-for-their-lamps.jpeg",
        "seg": "n7", "window": "46.229-48.829", "wide": False, "jesus": False,
        "locks": ["FORECOURT"] + _NIGHT,
        "narration": "They all woke and reached for their lamps.",
        "must_show": "close and low on the ground — several hands coming down into frame to snatch small clay lamps up off the packed dust, caught mid-reach.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no face, head, beard, chin or shoulder in this frame at all — women's hands, lamps and ground only; NO MAN AND NO MALE FIGURE anywhere in the picture, no male hand, no male forearm, no bare male leg, no trousers, breeches or leg wrapping of any kind; " + _NO_CREAM,
        "scene": (
            "One photograph, 50mm lens, THE CAMERA IS DOWN ON THE PACKED EARTH ITSELF, "
            "lens an inch or two above the dust and looking along it, very shallow depth "
            "of field. This is a picture of HANDS AND LAMPS AND GROUND and there is no "
            "face anywhere in it — the frame is cut off at wrist and forearm height, with "
            "the dark blurred masses of bodies rising out of focus above and behind. "
            "Sharp in the middle of the frame, three small fired-clay oil lamps sit "
            "directly on the pale packed dust, each a shallow closed oval of plain "
            "terracotta with a round filling hole and a pinched spout, each with one "
            "small soft yellow flame standing at the spout and guttering sideways in the "
            "movement of the air. Coming down into the frame from above are four or five "
            "YOUNG WOMEN'S HANDS — slim, brown and work-worn, with slender wrists and "
            "short nails, each emerging from the straight woven sleeve of a woman's "
            "ankle-length tunic — caught MID-REACH at different distances: one has "
            "already closed round the body of a lamp and is lifting it, tilting it a "
            "little so the flame leans; one is an inch from touching; one is splayed flat "
            "on the dust taking a woman's weight as she pushes herself up; one is just "
            "entering the frame at the very edge, still blurred with movement. The light "
            "is entirely from the three flames, at ground level, raking low and hard "
            "ACROSS the dust so every grain, scuff and pebble throws a long shadow, "
            "climbing the undersides of the wrists and forearms and dying out completely "
            "a foot above the ground — the top of the frame is pure black. Dark saturated "
            "wool sleeves and the long ankle-length SKIRT HEMS of women's tunics pass "
            "through the edges of the frame, covering the legs completely so no bare leg "
            "is visible anywhere; no pale cloth appears anywhere. Fine film grain."
        ),
    },
    # ---------------- ANCHOR: WISE-LEAD (generated in its own run) -------------
    {
        "id": "v2-r031-b15", "out": "s15-they-burned-warm-and-bright.jpeg",
        "seg": "n7", "window": "48.829-52.006", "wide": False, "jesus": False,
        "locks": ["WISE-LEAD"] + _NIGHT,
        "narration": "The wise trimmed theirs and they burned warm and bright.",
        "must_show": "the wise lead trimming her wick — her fingers pinching the charred tip of the bare wick at the lamp's spout, the flame standing up clean and strong, her face lit warm from below.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no scissors, snuffer, tongs or manufactured tool; no dying or sputtering flame — this lamp is burning strongly; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, deep midnight falling away "
            "to black behind her. A TIGHT CHEST-UP COMPOSITION SHOT STRICTLY SIDE-ON FROM "
            "HER LEFT: the camera stands close, low and exactly at her side, at right "
            "angles to the way she is facing, so she is seen in FULL PROFILE — her far "
            "cheek and her far eye are hidden behind the bridge of her own nose and the "
            "mass of her head, only the near side of her face is visible, and her gaze "
            "travels forward and DOWN onto her own hands and out through the RIGHT EDGE "
            "of the frame. A LENS GAZE IS GEOMETRICALLY IMPOSSIBLE IN THIS COMPOSITION. "
            "Her hands are raised in front of her chest, BELOW HER CHIN AND NEARER THE "
            "CAMERA THAN HER HEAD: the left palm cups the small terracotta lamp, and the "
            "thumb and forefinger of the right hand are pinching off the black charred "
            "tip of the bare fibre wick where it stands at the pinched spout. The flame "
            "has just taken hold and stands UP CLEAN AND STRONG, a small steady "
            "yellow-orange teardrop with a blue root, brighter than any other light in "
            "the video so far. It lights her from BELOW AND IN FRONT: the undersides of "
            "her fingers and wrists, the underside of her jaw and chin, her lower lip, "
            "the underside of her nose, the front planes of her cheekbones and the "
            "underside of her brow ridge, with her eyes catching one small sharp point of "
            "reflected flame each. THE CROWN AND BACK OF HER HEAD, THE WHOLE MASS OF HER "
            "HAIR AND HER SHOULDERS ARE UNLIT AND DARK and merge into the black behind "
            "her, and there is NO bright rim, edge, ring, contour or outline of light "
            "anywhere around her head, hair or shoulders. Her thick dark brown plait "
            "falls forward over her LEFT shoulder. Her expression is calm, absorbed and "
            "practical. Her dark olive-green wool sleeve and deep rust-red head cloth "
            "read as smooth flat close-woven cloth. The background is pure unlit black with one "
            "tiny distant out-of-focus flame."
        ),
    },
    {
        "id": "v2-r031-b16", "out": "s16-looked-down-in-dismay.jpeg",
        "seg": "n8", "window": "52.006-54.946", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "But the foolish look down in dismay,",
        "must_show": "the five foolish standing with their heads bent down over their own failing lamps, the light on their faces visibly weaker and redder than the strong clean flames of the wise standing apart from them.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman — exactly ten; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 40mm lens, deep midnight. THE CAMERA STANDS OFF TO THE SIDE "
            "OF BOTH GROUPS AND SHOOTS ACROSS THE GAP BETWEEN THEM AT RIGHT ANGLES TO "
            "EVERY EYELINE, so every woman is seen FROM THE SIDE in profile or in "
            "three-quarter from behind, nobody is squared up to the lens and NOT ONE "
            "PAIR OF PUPILS IS CENTRED ON IT — every one of the ten is looking DOWN at a lamp or "
            "sideways at another woman. THIS IS A WIDE FULL-LENGTH PHOTOGRAPH with all "
            "ten women in the frame head to feet, and THE COMPOSITION SPLITS THE FRAME: "
            "the FIVE FOOLISH stand clustered in the NEAR LEFT half, the FIVE WISE stand "
            "apart in the FAR RIGHT half, with a clear band of empty dark dust between the "
            "two groups, and a clear gap of ground between every individual woman so a "
            "viewer counts five and five, EXACTLY TEN AND NO ELEVENTH. THE DIFFERENCE IS "
            "IN THE LIGHT AND IT IS THE POINT OF THE PICTURE: each of the five wise holds "
            "a lamp low in front of her with a CLEAN STRONG YELLOW-WHITE FLAME that lights "
            "her hands and the front of her face warmly and firmly, and each has her small "
            "round clay jar in her free hand or at her hip. Each of the five foolish "
            "stands with her head BENT DOWN over her own lamp, held low at waist height "
            "and out in front of her, and those five flames are visibly DYING — small, "
            "low, dull orange-red, shrunk down onto the wick with a thread of dark smoke "
            "lifting off each one — so their faces are lit only faintly and redly from "
            "beneath, barely emerging from the dark, and their free hands are empty. In "
            "every case the flame is below the chin and nearer the camera than the head, "
            "so the crown and back of all ten heads stay UNLIT AND DARK against the "
            "night, with no bright rim, edge, ring or outline of light around any head, "
            "hair or shoulder anywhere in the frame. Every garment is dark saturated wool "
            "and no pale cloth appears anywhere."
        ),
    },
    # -------------- ANCHOR: FOOLISH-LEAD (generated in its own run) ------------
    {
        "id": "v2-r031-b17", "out": "s17-they-had-no-oil-left.jpeg",
        "seg": "n8", "window": "54.946-59.026", "wide": False, "jesus": False,
        "locks": ["FOOLISH-LEAD"] + _NIGHT,
        "narration": "their lamps were sputtering out, they had no oil left.",
        "must_show": "the foolish lead's lamp guttering out in her cupped hands — the flame shrunk to a dull red bead on a smoking wick, the dry empty bowl of the lamp tipped toward her, her face falling as she realises.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no strong clean flame — this lamp is nearly out; no oil jar, flask or second vessel anywhere in the frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, deep midnight going to "
            "black. A TIGHT CHEST-UP COMPOSITION SHOT STRICTLY SIDE-ON FROM HER RIGHT: "
            "the camera stands close, low and exactly at her side, at right angles to the "
            "way she is facing, so she is seen in FULL PROFILE — her far cheek and her far "
            "eye are hidden behind the bridge of her own nose and the mass of her head, "
            "only the near side of her face is visible, and her gaze travels forward and "
            "sharply DOWN into her own cupped hands and out through the LEFT EDGE of the "
            "frame. A LENS GAZE IS GEOMETRICALLY IMPOSSIBLE IN THIS COMPOSITION. Both her "
            "hands are cupped round the small terracotta lamp and held LOW in front of her "
            "chest, BELOW HER CHIN AND NEARER THE CAMERA THAN HER HEAD, the lamp tipped a "
            "little toward her so the shallow bowl shows DRY — bare fired clay with only a "
            "dark ring of old oil stain round the inside and no liquid left in it at all. "
            "The flame has shrunk to a DULL RED-ORANGE BEAD barely bigger than a "
            "fingertip, crouched down on the charred wick and about to go, with a thin "
            "thread of grey smoke rising off it and bending away. THAT FAILING BEAD IS "
            "THE ONLY LIGHT IN THE PICTURE and it is weak: it reaches the undersides of "
            "her fingers, a small warm patch under her chin and lower lip, the underside "
            "of her nose and one cheekbone, and DIES THERE — her brow is already in "
            "shadow, and the crown and back of her head, the whole mass of her black "
            "curling hair and her shoulders are UNLIT AND DARK, merging completely into "
            "the black behind her, with NO bright rim, edge, ring, contour or outline of "
            "light anywhere around her head, hair or shoulders. Her mouth has come open a "
            "little and her brows have drawn together — the exact moment the easy face "
            "from earlier falls. Her dark moss-green head cloth is slipped back off the "
            "crown of her head. Deep rust-brown smooth flat close-woven wool at her shoulder. "
            "The background is pure unlit black."
        ),
    },
    # ============ j3 — Matthew 25:8, and the plea (n9) =========================
    {
        "id": "v2-r031-b18", "out": "s18-give-us-of-your-oil.jpeg",
        "seg": "j3", "window": "59.026-63.941", "wide": True, "jesus": False,
        "locks": ["TEN", "FOOLISH-LEAD", "FORECOURT"] + _NIGHT,
        "narration": "Give us of your oil, for our lamps are gone out.",
        "must_show": "the foolish crossing the dark ground to the wise with their dead lamps held out — hands extended toward the wise women's clay jars, the asking plain in the bodies.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman — exactly ten; no oil actually being poured or handed over in this frame — it is the asking, not the giving; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep midnight. THE CAMERA STANDS BEHIND AND "
            "SLIGHTLY TO THE LEFT OF THE FIVE FOOLISH AND SHOOTS PAST THEM toward the "
            "wise, so the near five are seen from BEHIND and in three-quarter from behind "
            "— dark backs, shoulders and head cloths across the near half of the frame — "
            "and the five wise stand facing this way in the middle distance, their heads "
            "turned in three-quarter toward the askers so their gazes cross the frame "
            "diagonally and exit through its side edges. NOT ONE FACE IS SQUARED UP TO "
            "THE LENS AND NOT ONE PAIR OF PUPILS IS CENTRED ON IT. THIS IS A WIDE "
            "FULL-LENGTH PHOTOGRAPH with all ten women in frame head to feet, five near "
            "and five beyond, each separated by a clear gap of dark ground so a viewer "
            "counts EXACTLY TEN AND NO ELEVENTH. THE ACTION IS THE ASKING: the five "
            "foolish have crossed the dust and are pressing close, each holding her DEAD "
            "OR DYING lamp OUT AND FORWARD on an extended arm toward the wise — cold dark "
            "clay bowls with no flame or a last red bead and a thread of smoke — and "
            "several have the other hand open and reaching toward the small round clay "
            "jars the wise are holding. The foolish lead is nearest the camera at the "
            "left, seen in three-quarter from behind, her dark moss-green head cloth "
            "slipped off the crown of her head and her lamp thrust out. The five wise "
            "each hold a clean strong low flame in front of them and each has her jar, and "
            "several have drawn the jar back and IN toward the body. ALL THE LIGHT IN THE "
            "PICTURE COMES FROM THE FIVE WISE LAMPS, held low at waist height in front of "
            "their bodies, so it travels forward and upward across the gap onto the "
            "foolish women's outstretched forearms and the undersides of their jaws and "
            "no higher — every head in the frame is unlit and dark on top and behind, "
            "with no bright rim, edge, ring or outline around any head, hair or shoulder "
            "anywhere. Every garment is dark saturated wool; no pale cloth appears "
            "anywhere. No oil is being poured and nothing has changed hands."
        ),
    },
    {
        "id": "v2-r031-b19", "out": "s19-give-us-some-of-your-oil.jpeg",
        "seg": "n9", "window": "63.941-68.357", "wide": False, "jesus": False,
        "locks": ["FOOLISH-LEAD", "WISE-LEAD"] + _NIGHT,
        "narration": "Please, they cried out to the others. Give us some of your oil.",
        "must_show": "a tight two-shot in profile — the foolish lead's open reaching hand almost touching the clay jar the wise lead is holding, the small gap between hand and jar the whole subject of the picture.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "the hand does NOT touch the jar and the jar is not handed over; no oil pouring; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm lens, very shallow depth of field, deep midnight going "
            "to black behind. A TIGHT TWO-SHOT SHOT STRICTLY SIDE-ON: the camera stands "
            "at right angles to the line between the two women, so BOTH are seen in FULL "
            "PROFILE facing each other across the frame — the foolish lead entering from "
            "the LEFT facing right, the wise lead at the RIGHT facing left, each woman's "
            "far cheek and far eye hidden behind her own nose and head, and both gazes "
            "running horizontally along the axis between them and out through the side "
            "edges. A LENS GAZE IS GEOMETRICALLY IMPOSSIBLE IN THIS COMPOSITION. The "
            "SUBJECT OF THE PICTURE IS THE GAP IN THE MIDDLE: sharp in the centre of the "
            "frame the foolish lead's small thin hand is stretched out flat, palm up, "
            "fingers open, reaching — and the small round fired-clay oil jar cradled "
            "against the wise lead's body is a hand's breadth away from it, NOT TOUCHING, "
            "with a clear band of dark air between the fingertips and the clay. The wise "
            "lead's own hand is closed round the jar's neck and drawn slightly back "
            "toward herself. Her lamp burns low in her other hand at the bottom of the "
            "frame, BELOW BOTH CHINS AND NEARER THE CAMERA THAN EITHER HEAD, and it is "
            "the only light: it climbs upward onto the reaching palm and fingers, the "
            "curved shoulder of the jar, the undersides of both jaws and both noses, and "
            "reaches no further — the crowns and backs of both heads, both women's hair "
            "and both sets of shoulders are UNLIT AND DARK and merge into the black, with "
            "NO bright rim, edge, ring, contour or outline around either head. The foolish "
            "lead's mouth is open on the word and her brows are up in appeal; the wise "
            "lead's jaw is set and her eyes are down toward the jar. Dark moss-green and "
            "deep rust-red head cloths, deep rust-brown and dark olive-green wool. The "
            "background is unlit black."
        ),
    },
    # ============= j4 — Matthew 25:9, the refusal, in three beats ==============
    {
        "id": "v2-r031-b20", "out": "s20-not-so-lest-there-be-not-enough.jpeg",
        "seg": "j4", "window": "68.357-72.537", "wide": False, "jesus": False,
        "locks": ["WISE-LEAD"] + _NIGHT,
        "narration": "not so, lest there be not enough for us and you,",
        "must_show": "the wise lead in profile, her small clay jar drawn in and held close against her body with both the lamp and the jar low, her face grave — a refusal that costs her, not a hard one.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no sneer, no scorn and no cruelty in the face; no jar being handed over; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, deep midnight going to "
            "black. A TIGHT CHEST-UP COMPOSITION SHOT STRICTLY SIDE-ON FROM HER RIGHT: "
            "the camera stands close and exactly at her side at right angles to the way "
            "she faces, so she is seen in FULL PROFILE — her far cheek and far eye hidden "
            "behind the bridge of her own nose and the mass of her head — and her gaze "
            "travels level and forward, out through the LEFT EDGE of the frame toward the "
            "woman she is answering. A LENS GAZE IS GEOMETRICALLY IMPOSSIBLE IN THIS "
            "COMPOSITION. The small round fired-clay oil jar is held IN AND CLOSE against "
            "her ribs in her far hand, half hidden by her own forearm, and her near hand "
            "holds the burning lamp LOW at the bottom of the frame, BELOW HER CHIN AND "
            "NEARER THE CAMERA THAN HER HEAD. That single clean yellow flame is the only "
            "light: it climbs upward onto the underside of her wrist and forearm, the "
            "curve of the jar, the underside of her jaw and chin, her lower lip, the "
            "underside of her nose and the front plane of her cheekbone, and thins out "
            "before it reaches her brow. THE CROWN AND BACK OF HER HEAD, THE WHOLE MASS "
            "OF HER HAIR AND HER SHOULDERS ARE UNLIT AND DARK, merging into the black "
            "behind her, with NO bright rim, edge, ring, contour or outline of light "
            "anywhere around her head, hair or shoulders. HER FACE IS THE POINT: her jaw "
            "is set and her mouth is closed and level, her brows drawn slightly together, "
            "her eyes steady and unhappy — this is a grave, sorry, immovable answer and "
            "there is no scorn, no sneer, no triumph and no cruelty in it anywhere. Her "
            "thick dark brown plait falls forward over her left shoulder. Dark "
            "olive-green wool and a deep rust-red head cloth. The background is unlit "
            "black with one small distant out-of-focus flame."
        ),
    },
    {
        "id": "v2-r031-b21", "out": "s21-go-ye-rather-to-them-that-sell.jpeg",
        "seg": "j4", "window": "72.537-75.537", "wide": False, "jesus": False,
        "locks": ["WISE-LEAD", "LANE"] + _NIGHT,
        "narration": "but go ye rather to them that sell and",
        "must_show": "the wise lead's arm carried out level, pointing away down the dark lane toward the sellers, the black depth of the lane filling the space her hand sends them into.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no shop, no stall, no market and no lit building at the end of the lane — it is black; no tarmac, kerb, painted line, pole, wire or signpost; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, deep midnight, shallow depth of field with the "
            "lane soft behind. THE CAMERA STANDS CLOSE AT HER SIDE AND SHOOTS ACROSS HER "
            "AT RIGHT ANGLES, so her head is turned well off the camera axis, seen in "
            "near profile with her nose pointed toward the RIGHT EDGE and her gaze "
            "travelling out level along her own arm and clean out through that RIGHT EDGE "
            "— her pupils never come near the lens. Her near arm is raised and carried "
            "OUT AND LEVEL from the shoulder, the hand open and the fingers together, "
            "aimed away into the depth of the frame; it is a sending gesture, firm, not a "
            "jab. THE SPACE HER HAND POINTS INTO IS THE OTHER HALF OF THE PICTURE and it "
            "is BLACK: the village lane runs away between the blank flat-roofed mud-brick "
            "walls, its packed dust going grey then going dark, and its far end is lost "
            "in total unlit darkness with no shop, no stall, no lit window, no lamp and "
            "no figure in it at all. Her own lamp is in her other hand, carried LOW at "
            "waist height and near the bottom of the frame, BELOW HER CHIN AND NEARER "
            "THE CAMERA THAN HER HEAD, and it is the only light source: it lights the "
            "underside of her raised forearm, the front of her body, her jaw from "
            "beneath and about two paces of dust in front of her, and the rest of the "
            "picture falls away to night. The crown and back of her head and her hair "
            "are unlit and dark, with no bright rim, edge or outline anywhere around "
            "them. Dark olive-green wool sleeve, deep rust-red head cloth with its loose "
            "end down her back. Above the black roofline a deep blue-black starred sky."
        ),
    },
    {
        "id": "v2-r031-b22", "out": "s22-buy-for-yourselves.jpeg",
        "seg": "j4", "window": "75.537-78.486", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT"] + _NIGHT,
        "narration": "buy for yourselves.",
        "must_show": "the two groups now visibly separate across a band of empty dark ground — five wise with burning lamps and jars on one side, five foolish with dead lamps on the other, nobody touching.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman — exactly ten; no oil changing hands; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep midnight. THE CAMERA STANDS WELL OFF TO ONE "
            "SIDE OF BOTH GROUPS AND SHOOTS ACROSS THE EMPTY GROUND BETWEEN THEM AT RIGHT "
            "ANGLES TO EVERY EYELINE, so both groups are seen in profile and "
            "three-quarter, facing each other across the frame, and NOT ONE FACE IS "
            "SQUARED UP TO THE LENS. THIS IS A WIDE FULL-LENGTH PHOTOGRAPH with all ten "
            "women in frame head to feet. THE SUBJECT IS THE SEPARATION: a clear band of "
            "empty dark dust now runs down the middle of the picture. On the RIGHT stand "
            "the FIVE WISE, each with a clean strong low flame and her small round clay "
            "jar held close, already half turned away toward the lane mouth. On the LEFT "
            "stand the FIVE FOOLISH, each holding a dark cold lamp with no flame or a "
            "last red bead and a thread of smoke, their free hands empty and fallen to "
            "their sides, one with her head down. A clear gap of ground separates every "
            "individual woman from the next so a viewer counts five and five, EXACTLY TEN "
            "AND NO ELEVENTH. Nobody is touching anybody and nothing is passing between "
            "the groups. ALL THE LIGHT COMES FROM THE FIVE WISE LAMPS held low at waist "
            "height in front of their bodies: it falls warm on their own hands and the "
            "fronts of their faces, reaches across the empty band as a thinning wash onto "
            "the near shoulders and lowered faces of the foolish, and dies. Every head in "
            "the picture is unlit and dark on top and behind, with no bright rim, edge, "
            "ring or outline around any head, hair or shoulder anywhere in the frame. "
            "Every garment is dark saturated wool and there is no pale cloth anywhere. "
            "Behind them the black roofline and a deep blue-black starred sky."
        ),
    },
    {
        "id": "v2-r031-b23", "out": "s23-there-isnt-enough-for-all.jpeg",
        "seg": "n10", "window": "78.486-81.686", "wide": False, "jesus": False,
        "locks": ["WISE-LEAD", "FOOLISH-LEAD"] + _NIGHT,
        "narration": "but the wise couldn't. There isn't enough for all of us,",
        "must_show": "the wise lead's small clay jar held up between the two women in the lamplight, plainly and honestly small — the jar's size the whole argument of the picture.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no large jar, amphora, cask or barrel — this vessel is small enough to hold in one hand; no pouring; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm lens, very shallow depth of field, deep midnight. THE "
            "CAMERA STANDS AT RIGHT ANGLES TO BOTH WOMEN so both are seen in near PROFILE "
            "across the frame, each far cheek and far eye hidden behind her own nose and "
            "head, both gazes running along the axis between them and out through the "
            "side edges — a lens gaze is geometrically impossible here. Sharp and dead "
            "centre, filling the middle of the frame, is THE SMALL ROUND FIRED-CLAY OIL "
            "JAR, lifted a little in the wise lead's hand into the light between them: "
            "plain unglazed terracotta, unmistakably SMALL — her fingers wrap right round "
            "its body and her thumb nearly meets them, its narrow neck plugged with a "
            "twist of rolled cloth, its curved side showing the faint throwing rings of "
            "the wheel and one old dark oil smear. Her other hand tips it very slightly "
            "so the weight of the little that is inside reads. Both women's faces are "
            "soft-focus at the left and right edges of the frame, hers set and sorry, the "
            "foolish lead's turned down toward the jar with her mouth open. The lamp "
            "burns at the very bottom of the frame, BELOW BOTH CHINS AND NEARER THE "
            "CAMERA THAN EITHER HEAD, and is the only light: it climbs upward onto the "
            "underside of the jar, the fingers holding it, and the undersides of both "
            "jaws, and goes no higher — both heads are unlit and dark on top and behind, "
            "with no bright rim, edge, ring or outline anywhere around either head, hair "
            "or shoulders. Behind them is unlit black night. Dark olive-green and deep "
            "rust-brown wool at the edges of the frame; no pale cloth anywhere."
        ),
    },
    {
        "id": "v2-r031-b24", "out": "s24-hurry-go-and-buy-your-own.jpeg",
        "seg": "n10", "window": "81.686-85.001", "wide": True, "jesus": False,
        "locks": ["TEN", "FORECOURT", "LANE"] + _NIGHT,
        "narration": "they said. Hurry, go and buy your own.",
        "must_show": "the wise urging the foolish away — arms out toward the black lane mouth, the foolish already beginning to turn, the whole group's movement breaking apart.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no eleventh woman — exactly ten; no anger and no shoving; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, deep midnight. THE CAMERA STANDS BEHIND THE FIVE "
            "WISE AND SHOOTS PAST THEM toward the foolish and the black lane mouth beyond, "
            "so the near wise are seen entirely FROM BEHIND — dark backs, shoulders and "
            "head cloths, one arm from each raised and extended AWAY from the camera into "
            "the depth of the frame — and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS "
            "A WIDE FULL-LENGTH PHOTOGRAPH with all ten women in frame head to feet: five "
            "near backs and five figures beyond them, each separated by a clear gap of "
            "dark ground so a viewer counts EXACTLY TEN AND NO ELEVENTH. The five foolish "
            "in the middle distance are seen in three-quarter and in profile, already "
            "breaking and turning away toward the lane, one caught mid-pivot with her "
            "skirt swinging, one still looking back over her shoulder with her dead lamp "
            "hanging at her side, one taking her first running step, their gazes aimed "
            "away toward the lane and out through the far edges. Behind them the mouth of "
            "the lane is a black rectangle between the mud-brick walls with nothing in it. "
            "ALL THE LIGHT COMES FROM THE FIVE WISE LAMPS carried LOW at waist height in "
            "front of their bodies, nearer the camera than any head: it throws the near "
            "backs into near-silhouette, reaches across onto the turning foolish women's "
            "sleeves and lowered faces, and dies before the lane mouth. Every head in the "
            "picture is unlit and dark on top and behind, with no bright rim, edge, ring "
            "or outline around any head, hair or shoulder. Every garment is dark "
            "saturated wool and no pale cloth appears anywhere. The gesture is urgent and "
            "kind, not angry — no fist, no shove, no snarl."
        ),
    },
    # ============= THE FOOLISH RUN — and the bridegroom arrives ================
    {
        "id": "v2-r031-b25", "out": "s25-rushed-off-into-the-dark.jpeg",
        "seg": "n11", "window": "85.001-87.821", "wide": True, "jesus": False,
        "locks": ["FOOLISH-LEAD", "LANE", "ANCIENT-ROAD", "MARKET-TOWN"] + _NIGHT,
        "narration": "And while the foolish rushed off into the dark to find",
        "must_show": "the five foolish running away down the black lane, seen from behind, small against the depth of it, carrying dead unlit lamps — nothing ahead of them but darkness.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no sixth runner — exactly five; NO LIT LAMP IN ANY OF THEIR HANDS, every lamp is dark and out; no shop, stall or lit window ahead; no tarmac, kerb, painted line, pole, wire or signpost; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, THE DEEPEST DARK IN THE VIDEO. THE CAMERA STANDS "
            "IN THE LANE BEHIND THE RUNNERS AND SHOOTS STRAIGHT PAST THEM into its depth, "
            "so all five are seen entirely FROM BEHIND, running AWAY from the camera, "
            "their faces not visible at all and nothing turned toward the lens. THIS IS A "
            "WIDE FULL-LENGTH PHOTOGRAPH: the camera is far enough back that all five "
            "women are in frame head to feet, strung out unevenly down the lane with a "
            "clear gap between each so a viewer counts EXACTLY FIVE AND NO SIXTH, the "
            "nearest large and the furthest already small and half swallowed by the dark. "
            "Each is caught mid-stride, skirts lifted in one fist, head cloths blown "
            "back, and EACH CARRIES HER SMALL CLAY LAMP DARK AND UNLIT, swinging in her "
            "hand with no flame on it at all. ALL FIVE ARE GROWN YOUNG WOMEN, not "
            "children, and EVERY SEPARATE PIECE OF CLOTH ON EVERY ONE OF THEM IS A DARK "
            "SATURATED COLOUR: their five tunics are DEEP RUST-BROWN, DARK GREY-BROWN, "
            "DARK OLIVE, DEEP TERRACOTTA-BROWN and DARK BRONZE-GREEN, and their head "
            "cloths are DARK MOSS-GREEN, DEEP BURGUNDY, DARK SLATE-BLUE, DARK CHARCOAL "
            "and DARK BROWN-PURPLE. NOT ONE OF THE FIVE WEARS ANY WHITE, CREAM, "
            "OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, OATMEAL, STONE, PALE TAN OR "
            "LIGHT-COLOURED GARMENT, TUNIC, SLEEVE, SASH, HEAD CLOTH OR HEM ANYWHERE — "
            "every one of them reads as a dark shape against the pale dust. AHEAD OF THEM THERE IS NOTHING: the lane's "
            "packed dust runs on between the blank flat-roofed mud-brick walls, going "
            "grey, going dim, and ending in total black — no shop, no stall, no lit "
            "window, no lamp, no torch, no figure. THE ONLY LIGHT IN THE PICTURE COMES "
            "FROM BEHIND THE CAMERA, the distant forecourt lamps out of frame, and it is "
            "weak and low: it lays a thin cold wash along the lane floor and the bottom "
            "two feet of the walls and picks out the backs of the nearest runner's heels "
            "and hem, and it reaches no head, no shoulder and nothing above waist height "
            "anywhere in the frame. There is no bright rim, edge, ring or outline of "
            "light around any head, hair or shoulder. Every garment is dark saturated "
            "wool; no pale cloth appears anywhere. Above the black roofline, a deep "
            "blue-black starred sky."
        ),
    },
    # ------------- ANCHOR: BRIDEGROOM (generated in its own run) ---------------
    {
        "id": "v2-r031-b26", "out": "s26-the-bridegroom-arrived.jpeg",
        "seg": "n11", "window": "87.821-90.445", "wide": True, "jesus": False,
        "locks": ["BRIDEGROOM", "PARTY", "LANE"] + _NIGHT,
        "narration": "oil, the bridegroom arrived.",
        "must_show": "the bridegroom coming up the lane at the head of his party, his face visible and lit warm from below by a companion's torch carried low beside him, the party's dark figures crowding behind.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no cream, white or pale garment on the bridegroom or anyone in the party; no crown, no wreath, no garland, no circlet, no diadem and NOTHING OF LEAVES, TWIGS, BRANCHES, BRIAR OR THORN on or near his head — absolutely no crown of thorns and nothing that resembles one; no jewels, no gold, no rich embroidery and no royal or priestly costume — he is a village bridegroom; no torch raised above anyone's head; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, deep midnight, shallow depth of field with the "
            "party behind him soft. THE CAMERA STANDS IN THE LANE OFF TO THE BRIDEGROOM'S "
            "LEFT AND SHOOTS ACROSS HIM AT RIGHT ANGLES AS HE PASSES, so his head is "
            "turned well off the camera axis, seen in three-quarter with his nose pointed "
            "toward the RIGHT EDGE and his gaze travelling forward up the lane and out "
            "through that RIGHT EDGE toward the courtyard — his pupils never come near "
            "the lens. He is sharp in the middle of the frame from the knees up, walking "
            "at an easy unhurried pace, his weight on the forward foot, the deep "
            "burgundy-red wool of his tunic and the dark indigo mantle over one shoulder "
            "moving with the stride, his dark indigo head cloth wound close over his short black hair with its loose end down his left shoulder. "
            "short black hair. His face is broad and square-jawed with a close-cropped "
            "black beard, and his expression is warm and glad. Walking a half pace ahead "
            "of him and NEARER THE CAMERA, a companion carries a PITCH TORCH — a rough "
            "wooden stave bound at the head with resinous rag, one ragged smoky orange "
            "flame — held LOW at the companion's hip and OUT to the side, WELL BELOW "
            "EVERY CHIN IN THE PICTURE and nearer the camera than the bridegroom's head. "
            "That torch is the only strong light: it climbs UPWARD onto the front of the "
            "bridegroom's tunic, the underside of his jaw and beard, his lower lip, the "
            "underside of his nose and the front planes of his cheekbones, and thins out "
            "at his brow. THE TOP AND BACK OF HIS HEAD, HIS HAIR, HIS CIRCLET AND HIS "
            "SHOULDERS ARE UNLIT AND DARK against the black lane behind him, and there is "
            "NO bright rim, edge, ring, contour, corona or outline of light anywhere "
            "around his head, hair or shoulders, and nothing about him gives off light of "
            "its own. Six or eight companions in dark saturated wool crowd behind and "
            "beside him, out of focus, their faces dim and turned forward up the lane, "
            "one more low torch among them. No pale cloth appears on anyone anywhere in "
            "the frame."
        ),
    },
    {
        "id": "v2-r031-b27", "out": "s27-and-the-door-was-shut.jpeg",
        "seg": "n12", "window": "90.445-95.243", "wide": True, "jesus": False,
        "locks": ["GATEWAY", "BRIDEGROOM", "PARTY", "WISE-LEAD"] + _NIGHT,
        "narration": "The ones who were ready went in with him to the wedding feast, and the door was shut.",
        "must_show": "the heavy timber doors swinging closed across the warm lit gateway, the last of the five wise and the party already inside, the wedge of warm light narrowing to a thin line as the leaves come together.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no metal hinge, strap, stud, nail head, boss, handle, knocker, ring, lock or bolt on the doors; no arch, keystone or carved jamb; no foolish woman in this frame — all five are away in the lane; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep midnight. THE CAMERA STANDS OUTSIDE IN THE "
            "DARK FORECOURT, SEVERAL PACES BACK FROM THE GATEWAY AND OFF TO ITS LEFT, "
            "SHOOTING ACROSS THE OPENING AT AN ANGLE — so the few figures still visible in "
            "the narrowing gap are seen from BEHIND and in three-quarter from behind as "
            "they move AWAY into the courtyard, and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. THE ACTION IS THE CLOSING: the two heavy leaves of wide adzed vertical "
            "plank, grey and split with age, are swinging IN toward each other on their "
            "wooden pivot posts and are most of the way shut, leaving a tall narrowing "
            "wedge of warm light between them perhaps a forearm wide, with one villager's "
            "dark hand and shoulder on the inner face of the near leaf pushing it. THROUGH "
            "THAT NARROWING GAP, warm and soft and already half cut off: the packed floor "
            "of the courtyard, several small clay lamps set LOW on the ground and on a "
            "waist-high mud-brick ledge, the dark backs of the wedding party, the "
            "bridegroom's deep burgundy tunic and dark indigo mantle among them, and the "
            "last of the wise women — a dark olive-green tunic and a deep rust-red head "
            "cloth with its end down her back — stepping in, her small lamp still burning "
            "low in her hand. EVERYTHING OUTSIDE THE GAP IS BLACK NIGHT: the mud-brick "
            "wall, the worn limestone threshold, the forecourt dust and the deep "
            "blue-black starred sky above the flat roofline are lit by nothing but the "
            "closing wedge of light, which lays one narrowing blade of warm illumination "
            "across the threshold and two paces of dust and stops. Every lamp in the "
            "picture is below head height, no light stands behind anybody's head, and "
            "there is no bright rim, edge, ring or outline around any head, hair or "
            "shoulder anywhere in the frame. No pale garment appears on anyone."
        ),
    },
    # =========== OUTSIDE THE SHUT DOOR — j5, j6, n13 (Matthew 25:11-12) ========
    {
        "id": "v2-r031-b28", "out": "s28-lord-lord-open-to-us.jpeg",
        "seg": "j5", "window": "95.243-98.684", "wide": True, "jesus": False,
        "locks": ["GATEWAY", "FOOLISH-LEAD"] + _NIGHT,
        "narration": "Lord, Lord, open to us.",
        "must_show": "the five foolish outside the shut timber doors in the dark, their lamps now freshly lit and burning, hands flat on the planks, faces turned up to the wood — one thin line of warm light escaping under the door at ground level.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no sixth woman — exactly five; the doors do NOT open and there is no gap between the leaves; no metal hinge, strap, stud, handle, knocker, ring, lock or bolt; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep midnight. THE CAMERA STANDS OUT IN THE DARK "
            "BEHIND THE FIVE WOMEN AND SHOOTS PAST THEM AT THE SHUT DOORS, so all five "
            "are seen entirely FROM BEHIND and in three-quarter from behind — dark backs, "
            "shoulders, head cloths and lifted arms — facing INTO the depth of the frame, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH "
            "PHOTOGRAPH: all five are in frame head to feet, strung along the closed "
            "gateway with a clear gap of dark ground between each so a viewer counts "
            "EXACTLY FIVE AND NO SIXTH. THE TWO HEAVY PLANK LEAVES ARE FULLY SHUT AND "
            "TIGHT TOGETHER, filling the centre of the frame, grey split adzed wood under "
            "the one massive squared timber lintel, with no gap between them and nothing "
            "of the courtyard visible. Three of the women have both palms flat on the "
            "planks, one has a fist raised mid-knock, one has her forehead nearly against "
            "the wood; every face is tipped UP toward the top of the doors. EACH OF THE "
            "FIVE NOW CARRIES A FRESHLY LIT LAMP — they reached the sellers, and that is "
            "the grief of the picture — each held LOW at waist height and out in front of "
            "her body, nearer the camera than her own head, with a clean small yellow "
            "flame. That lamplight climbs the lower planks of the doors, the women's "
            "sleeves and the undersides of their raised forearms, and reaches no head: "
            "every crown, every head cloth and every set of shoulders stays UNLIT AND "
            "DARK, and there is no bright rim, edge, ring or outline around any head, "
            "hair or shoulder. ALONG THE VERY BOTTOM OF THE DOORS, at the worn limestone "
            "threshold, ONE THIN UNBROKEN LINE OF WARM LIGHT escapes from the feast "
            "inside — a bright horizontal thread at ground level, no wider than a finger, "
            "lying across the dust in front of their feet. Above the wall, a deep "
            "blue-black starred sky. No pale cloth appears on anyone anywhere."
        ),
    },
    {
        "id": "v2-r031-b29", "out": "s29-i-know-you-not.jpeg",
        "seg": "j6", "window": "98.684-102.596", "wide": False, "jesus": False,
        "locks": ["GATEWAY"] + _NIGHT,
        "narration": "Verily I say unto you, I know you not.",
        "must_show": "the shut doors themselves close and head-on — grey split plank, the drawbar's shadow, the thin line of warm light along the threshold, and no person visible at all.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "NO PERSON, no face, no hand and no figure anywhere in this frame; the doors do not open; no metal hinge, strap, stud, nail head, handle, knocker, ring, lock or bolt; no writing, lettering, carving or symbol on the wood; ",
        "scene": (
            "One photograph, 50mm lens, deep midnight, and THERE IS NOBODY IN THIS "
            "PICTURE. The camera stands close and square to the SHUT double doors, a "
            "little below centre, looking slightly UP the face of them. The frame is "
            "almost entirely the two leaves: wide vertical planks of adzed timber, grey "
            "and silvered with age, split along the grain, the cross battens showing as "
            "raised horizontal bands, the joint between the leaves a single tight dark "
            "vertical line straight up the middle. The wood is plain — nothing carved, "
            "painted, inscribed or lettered on it, and no hinge, strap, stud, nail head, "
            "boss, handle, knocker, ring, lock or bolt of metal anywhere. THE ONLY LIGHT "
            "IN THE PICTURE IS ONE THIN UNBROKEN HORIZONTAL LINE OF WARM YELLOW ESCAPING "
            "UNDER THE BOTTOM EDGE OF THE DOORS, no wider than a finger, lying along the "
            "worn limestone threshold and spilling a shallow soft wash of light a hand's breadth "
            "out onto the dust in the near foreground — and it lights nothing else. It "
            "rakes upward along the very bottom of the planks, catching the splinters and "
            "the grain there, and above about knee height the whole picture falls away "
            "into deep unlit black, the lintel and the mud-brick wall barely readable as "
            "shape. There is no bright ring, corona, contour or outline of light anywhere in the "
            "feeling is finality: a shut solid thing, warm on the other side of it, cold "
            "and dark on this one. Fine film grain, deep true blacks."
        ),
    },
    {
        "id": "v2-r031-b30", "out": "s30-came-back-knocking.jpeg",
        "seg": "n13", "window": "102.596-105.536", "wide": False, "jesus": False,
        "locks": ["GATEWAY", "FOOLISH-LEAD"] + _NIGHT,
        "narration": "Later the others came back, knocking.",
        "must_show": "close on a fist striking the plank door, the knuckles flattened against the grey wood, the freshly lit lamp low in the other hand throwing the light upward.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no metal knocker, ring, handle, hinge, strap or stud on the door; no face squared up to the lens; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, very shallow depth of field, deep midnight. A "
            "TIGHT COMPOSITION ON THE DOOR AND ONE HAND: the camera stands close and at a "
            "steep angle along the face of the doors, so the grey split planks run away "
            "across the frame in raking perspective. Sharp and dominant in the centre is "
            "a woman's FIST, small and thin and brown, caught at the instant of impact — "
            "the knuckles flattened white-pale against the timber, the wrist braced, a "
            "faint blur of movement behind it. The plank under it shows every split, "
            "splinter and grain line in the raking light. Below and nearer the camera "
            "than the fist, held LOW and out in front of her body, her freshly lit clay "
            "lamp burns with a clean small yellow flame, and it is the only light in the "
            "frame: it climbs UPWARD along the door planks, onto the underside of her "
            "forearm and the back of her striking hand, and dies out a foot above. Her "
            "face is present only at the very edge of the frame, soft and out of focus, "
            "turned in near profile UP toward the top of the doors with her nose pointed "
            "out of the frame — no part of her gaze comes near the lens, and the crown "
            "and back of her head and her dark moss-green head cloth are unlit and merge "
            "into the black, with no bright rim, edge or outline around them. Her deep "
            "rust-brown wool sleeve reads as smooth flat close-woven cloth. The rest of the "
            "picture is unlit black timber and night."
        ),
    },
    {
        "id": "v2-r031-b31", "out": "s31-open-the-door-for-us.jpeg",
        "seg": "n13", "window": "105.536-108.096", "wide": True, "jesus": False,
        "locks": ["GATEWAY", "FOOLISH-LEAD"] + _NIGHT,
        "narration": "Lord, they called, open the door for us.",
        "must_show": "the five calling at the shut doors — mouths open, one woman's cheek pressed to the plank listening, hands spread on the wood, their lit lamps low.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no sixth woman — exactly five; the doors do not open; no metal hardware on the door; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep midnight. THE CAMERA STANDS CLOSE ALONGSIDE "
            "THE DOORS AND SHOOTS ALONG THEIR FACE AT A STEEP RAKING ANGLE rather than at "
            "the women, so the five are seen in PROFILE and three-quarter from behind, "
            "strung along the timber and receding away from the camera, every face turned "
            "toward the wood and every gaze exiting through the far edge of the frame — "
            "NOT ONE FACE IS SQUARED UP TO THE LENS. All five are in frame with a clear "
            "gap between each so a viewer counts EXACTLY FIVE AND NO SIXTH. The two heavy "
            "plank leaves are FULLY SHUT and fill the left of the frame as a wall of grey "
            "split adzed timber with no gap and no metal on it anywhere. The nearest "
            "woman has her CHEEK AND EAR PRESSED FLAT TO THE PLANK, listening, her eyes "
            "shut; the next has both palms spread wide on the wood and her mouth open on "
            "a call; the third is up on the balls of her feet calling toward the lintel; "
            "the two beyond stand back a pace with their heads tipped up. Each holds her "
            "freshly lit clay lamp LOW at waist height and out in front of her body, "
            "nearer the camera than her own head, so the light climbs the lower door "
            "planks and the undersides of their forearms and jaws and reaches no crown — "
            "every head, head cloth and set of shoulders in the picture stays UNLIT AND "
            "DARK, with no bright rim, edge, ring or outline around any of them. The thin "
            "unbroken line of warm light still escapes under the bottom of the doors "
            "along the limestone threshold. Above, deep blue-black starred sky over the "
            "black wall top. Every garment is dark saturated wool; no pale cloth appears "
            "anywhere."
        ),
    },
    {
        "id": "v2-r031-b32", "out": "s32-i-do-not-know-you.jpeg",
        "seg": "n13", "window": "108.096-111.663", "wide": True, "jesus": False,
        "locks": ["GATEWAY", "FOOLISH-LEAD"] + _NIGHT,
        "narration": "But the answer came from inside. I do not know you.",
        "must_show": "the answer landing — the five gone still and silent at the unmoved doors, hands sliding off the wood, heads dropping, the doors exactly as shut as before.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no sixth woman — exactly five; the doors do NOT move, open or crack; nobody visible inside; no metal hardware on the door; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep midnight. THE CAMERA STANDS OUT IN THE DARK "
            "BEHIND THE FIVE WOMEN AND SHOOTS PAST THEM at the shut doors, so all five "
            "are seen entirely FROM BEHIND — dark backs, dropped shoulders and head "
            "cloths — facing away into the depth of the frame, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH PHOTOGRAPH with all five in "
            "frame head to feet and a clear gap of dark ground between each, so a viewer "
            "counts EXACTLY FIVE AND NO SIXTH. THE PICTURE IS STILLNESS AFTER NOISE: the "
            "raised hands have come down, one woman's palm is sliding slowly off the "
            "plank, one arm hangs dead at a side, two heads have dropped forward, one "
            "woman has taken half a step back from the door; nobody is knocking and "
            "nobody is calling. THE DOORS ARE EXACTLY AS SHUT AS BEFORE — the same two "
            "grey split plank leaves under the same squared timber lintel, tight together "
            "with no gap, unmoved, with nothing of the inside visible and nobody standing "
            "in them. Their five lamps still burn LOW at waist height in front of their "
            "bodies, nearer the camera than their heads, laying warm light on the bottom "
            "of the doors, the dust and their own forearms, and reaching no head — every "
            "crown and set of shoulders stays UNLIT AND DARK, with no bright rim, edge, "
            "ring or outline anywhere around any head, hair or shoulder. The one thin "
            "unbroken line of warm light still lies along the threshold under the doors, "
            "unchanged and indifferent. Above the wall, a deep blue-black starred sky. "
            "Every garment is dark saturated wool; no pale cloth appears anywhere."
        ),
    },
    # ============ BACK TO THE FRAME — the explanation (n14, j1) ================
    {
        "id": "v2-r031-b33", "out": "s33-why-he-had-shared-this-story.jpeg",
        "seg": "n14", "window": "111.663-114.886", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "Then Jesus told them why he had shared this story.",
        "must_show": "Jesus on the Olivet ledge turning back to the disciples as the parable ends, in clear late-afternoon light, the bare far hillside across the valley behind him.",
        "must_not_show": _NO_HALO + "no night, no lamp, no flame, no fire, no sunset, no sunrise and no golden low sun; no tree, no grove, no canopy and no building on the slope; no woman, no lamp and no door anywhere in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 40mm lens, clear late-afternoon light warm and directional "
            "from the low right, the sun well up and OUT OF FRAME, long soft shadows on "
            "the pale limestone, the far valley and the bare far hills hazed, fine film "
            "grain. THE CAMERA IS PLACED SIDE-ON TO THE CIRCLE, STANDING OUT ON THE ROCK "
            "TO ONE SIDE AND SHOOTING ACROSS THE GROUP AT RIGHT ANGLES TO EVERY EYELINE. "
            "Jesus is at the RIGHT of the frame, still seated on the low boulder but "
            "turned back now toward the disciples ranged along the ledge to the LEFT of "
            "him: his head is round in three-quarter with his nose pointed toward the "
            "LEFT EDGE and his gaze travelling into the seated men and out through that "
            "LEFT EDGE, and every disciple is seen in profile or three-quarter from "
            "behind with his gaze travelling rightward and out through the RIGHT EDGE. "
            "NOT ONE FACE IS SQUARED UP TO THE CAMERA AND NOT ONE PAIR OF PUPILS IS "
            "CENTRED ON THE LENS. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A "
            "PORTRAIT: the camera is far enough back that Jesus AND at least five seated "
            "disciples are in frame together head to feet, with the valley and the small "
            "hazed bare hillside low behind them. The men have come forward on the rock — one "
            "has shifted up onto his knees, one has leaned in with his forearms on his "
            "thighs, one has turned his whole body round — the whole circle tightened by "
            "the end of the story. Jesus's near hand rests open on his knee. EXACTLY ONE "
            "out-of-focus DARK UMBER shouldered back with a dark brown head cloth sits at "
            "the near bottom-left corner as the only foreground object, a solid dark "
            "saturated mass. THERE IS NO PALE, IVORY, BEIGE, TAUPE, BUFF OR SAND SHAPE, "
            "SHOULDER, SLEEVE, DRAPE OR BLURRED MASS ANYWHERE IN THE FOREGROUND OR AT ANY "
            "EDGE — the only pale thing in the whole frame is the wool of Jesus's own robe."
        ),
    },
    {
        "id": "v2-r031-b34", "out": "s34-watch-therefore.jpeg",
        "seg": "j1", "window": "114.886-119.386", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": "Watch, therefore, for ye know neither the day nor the hour,",
        "must_show": "Jesus close, in strict side-on profile against the bare rock and the far hazed valley, speaking the warning — grave, warm, unhurried.",
        "must_not_show": _NO_HALO + "no night, no lamp, no flame, no sunset, no sunrise and no golden low sun; no other person in this frame; no tree, no grove and no building; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, clear late-afternoon light "
            "warm and directional from the low right, the sun well up and OUT OF FRAME. A "
            "TIGHT CHEST-UP COMPOSITION SHOT STRICTLY SIDE-ON FROM HIS LEFT: the camera "
            "stands close and exactly at his side, at right angles to the way he is "
            "facing, so he is seen in FULL PROFILE — his far cheek and his far eye are "
            "hidden behind the bridge of his own nose and the mass of his head, only the "
            "near side of his face is visible, and his gaze travels level and forward out "
            "through the LEFT EDGE of the frame toward the men he is speaking to. A LENS "
            "GAZE IS GEOMETRICALLY IMPOSSIBLE IN THIS COMPOSITION. He is speaking: the "
            "jaw open a little on the word, the near brow level, the whole face grave and "
            "warm rather than stern. His one plain undyed off-white cream wool robe and "
            "mantle read as smooth flat close-woven cloth in the clear side light, the weave "
            "visible at the shoulder. He is the only person in the frame. Behind him, "
            "thrown well out of focus, are the pale grey weathered limestone of the ledge, "
            "the dry bleached grass, and low in the background the hazed far side of the "
            "valley, bare tawny rock and dry grass with no building anywhere in it. The "
            "daylight falls on him from the front right, modelling "
            "the near cheek and brow; NOTHING stands behind his head, there is no bright "
            "rim, edge, ring, corona, aura or outline of light around his head, hair, "
            "beard or shoulders, and no light comes off him. Fine film grain."
        ),
    },
    {
        "id": "v2-r031-b35", "out": "s35-wherein-the-son-of-man-cometh.jpeg",
        "seg": "j1", "window": "119.386-122.902", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "wherein the Son of Man cometh.",
        "must_show": "Jesus and the disciples on the ledge with the whole wide empty valley and the bare far hills open beyond them, the words landing in the silence — a wide, quiet, spacious frame.",
        "must_not_show": _NO_HALO + "no night, no lamp, no flame, no sunset, no sunrise and no golden low sun; no tree, no grove, no canopy and no building on the slope; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens, clear late-afternoon light from the low right, the "
            "sun well up and OUT OF FRAME, long soft shadows reaching across the pale rock, "
            "the far distance hazed. THE CAMERA STANDS WELL BACK AND OFF TO ONE SIDE ON "
            "THE LEDGE, BEHIND AND BESIDE THE SEATED DISCIPLES, AND SHOOTS PAST THEM "
            "ACROSS THE GROUP AND OUT OVER THE VALLEY, so the near disciples are seen "
            "entirely FROM BEHIND as small dark seated backs and head cloths low in the "
            "frame, and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE "
            "FULL-LENGTH PHOTOGRAPH AND THE PEOPLE ARE SMALL IN IT: Jesus sits at the "
            "right on his low boulder, seen from behind and in three-quarter from behind, "
            "his gaze out across the valley and away from the camera through the far "
            "edge of the frame; five or six disciples sit lower and nearer, all facing "
            "the same way. THE SUBJECT IS THE SPACE: the bare grey limestone ledge and "
            "dry bleached grass run out to the lip, the ground drops away into the deep "
            "dry valley, and beyond it the far side rises again as BARE TAWNY HILLSIDE, pale "
            "rock and thin dry grass, hazed along the far ridge, with the wide clear sky "
            "above taking the whole upper half of the picture. AGAINST THAT SKY THERE IS "
            "ONLY BARE EMPTY RIDGE AND NOTHING ELSE — no town, no city, no wall, no "
            "battlement, no tower, no temple, no dome, no minaret, no spire, no roof, no "
            "house, no ruin, no aerial, no wire, no cable and no pole. Everything the disciples "
            "wear is dark saturated wool; the only pale thing in the frame is the wool of "
            "Jesus's own robe. Nobody is edge-lit or outlined in light, and nothing "
            "stands behind any head."
        ),
    },
    # ================== THE APPLICATION — n15 and n16 =========================
    {
        "id": "v2-r031-b36", "out": "s36-you-cannot-borrow.jpeg",
        "seg": "n15", "window": "122.902-127.142", "wide": False, "jesus": False,
        "locks": ["WISE-LEAD", "FOOLISH-LEAD"] + _NIGHT,
        "narration": "The oil is the one thing you cannot borrow at the last minute.",
        "must_show": "the emblem of the whole parable — one empty dark lamp bowl and one small clay oil jar held apart in two different hands with dark air between them, nothing passing across.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no oil pouring, no vessel touching another, nothing changing hands; no face squared up to the lens; " + _NO_CREAM,
        "scene": (
            "One photograph, 100mm macro lens, extremely shallow depth of field, deep "
            "midnight with everything beyond the hands falling to pure black. THIS IS A "
            "PICTURE OF TWO HANDS AND TWO CLAY VESSELS and the faces are out of the frame "
            "entirely, cut off above the wrists — no face appears anywhere in it. BOTH HANDS IN THIS PICTURE ARE YOUNG WOMEN'S HANDS — slim and small with "
            "narrow wrists, slender fingers and short nails, NOT a man's hand: no large "
            "broad palm, no thick knuckle, no heavy or hairy forearm anywhere. Entering "
            "from the LEFT, the foolish girl's small thin brown hand holds a SMALL "
            "FIRED-CLAY OIL LAMP "
            "tipped up toward the camera so its shallow bowl is visible and DRY: bare "
            "unglazed terracotta, a dark ring of old oil stain inside, the charred wick "
            "lying dead in the spout with no flame on it at all. Entering from the RIGHT, "
            "the wise woman's second slim brown hand holds a SMALL ROUND FIRED-CLAY OIL JAR with a "
            "rolled-cloth stopper, drawn back and held close and steady. BETWEEN THE TWO "
            "VESSELS RUNS A CLEAR BAND OF DARK EMPTY AIR — they do not touch, nothing is "
            "being poured, nothing is passing across, and the gap is the subject of the "
            "photograph. The only light is one small warm flame BELOW the bottom edge of "
            "the frame and NEARER THE CAMERA than either hand, so the light climbs upward "
            "onto the undersides of both wrists, the rim of the dead lamp and the curved "
            "shoulder of the jar, showing the throwing rings in the clay and the grain of "
            "the fired terracotta, and dies away completely toward the top of the picture, "
            "which is solid unlit black. Dark olive-green and deep rust-brown coarse "
            "hand-woven wool sleeves at the two edges of the frame; no pale cloth "
            "anywhere. Fine film grain, deep true blacks."
        ),
    },
    {
        "id": "v2-r031-b37", "out": "s37-a-heart-that-is-truly-ready.jpeg",
        "seg": "n15", "window": "127.142-129.142", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": "A heart that is truly ready,",
        "must_show": "Jesus quiet on the Olivet ledge in strict side-on profile, not speaking now, the late-afternoon light clear on him.",
        "must_not_show": _NO_HALO + "no night, no lamp, no flame, no sunset, no sunrise and no golden low sun; no other person in this frame; no tree, no grove and no building; " + _GAZE,
        "scene": (
            "One photograph, 105mm lens, very shallow depth of field, clear late-afternoon "
            "light warm and directional from the low right, the sun well up and OUT OF "
            "FRAME. A TIGHT HEAD-AND-SHOULDERS COMPOSITION SHOT STRICTLY SIDE-ON FROM HIS "
            "RIGHT: the camera stands close and exactly at his side at right angles to the "
            "way he faces, so he is seen in FULL PROFILE — his far cheek and his far eye "
            "are hidden behind the bridge of his own nose and the mass of his head, only "
            "the near side of his face is visible, and his gaze travels level and forward "
            "out through the RIGHT EDGE of the frame. A LENS GAZE IS GEOMETRICALLY "
            "IMPOSSIBLE IN THIS COMPOSITION. He is NOT speaking: the mouth is closed and "
            "soft, the near brow relaxed, the expression quiet, attentive and unguarded — "
            "a moment of stillness after the words. The cream wool of his robe and mantle "
            "sits at the bottom of the frame with its hand-woven weave visible in the "
            "clear side light. He is the only person in the frame. Behind him, thrown far "
            "out of focus into soft bands, are the pale grey limestone of the ledge, the "
            "bleached dry grass, and the hazed far valley wall. The daylight falls on him "
            "from the front right and models the near cheekbone, the brow and the line of "
            "the nose; NOTHING stands behind his head, there is NO bright rim, edge, ring, "
            "corona, aura, nimbus or outline of light around his head, hair, beard or "
            "shoulders, and no light comes off him or out of him. Fine film grain."
        ),
    },
    {
        "id": "v2-r031-b38", "out": "s38-a-lamp-you-have-kept-burning.jpeg",
        "seg": "n15", "window": "129.142-133.387", "wide": False, "jesus": False,
        "locks": [] + _NIGHT,
        "narration": "a faith that is really your own, a lamp you have kept burning.",
        "must_show": "one small clay lamp burning steadily in a pair of cupped hands in the dark, well-tended, the flame clean and strong and unhurried — the emblem of a kept faith.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "no face in this frame at all — hands and lamp only; no dying, sputtering or smoking flame; " + _NO_CREAM,
        "scene": (
            "One photograph, 100mm macro lens, extremely shallow depth of field, deep "
            "midnight, everything beyond the hands falling to pure unlit black. THIS IS A "
            "PICTURE OF ONE LAMP AND TWO HANDS and there is no face anywhere in it — the "
            "frame is cut off at the wrists. Sharp and centred, cupped in two brown, "
            "work-worn, slightly cracked hands held together as a shallow bowl, sits a "
            "SMALL FIRST-CENTURY CLAY OIL LAMP: a shallow closed oval of plain unglazed "
            "terracotta small enough to fit in a palm, a round filling hole in the top, a "
            "pinched spout at one end, faint throwing rings in the clay and a dark smear "
            "of oil down one side. Standing at the spout on a bare fibre wick is ONE small "
            "flame, CLEAN AND STEADY AND STRONG — a still yellow-orange teardrop with a "
            "blue root, upright and unwavering, not guttering, not shrunken and not "
            "smoking. Through the filling hole a glint of oil shows: the lamp is full. THE "
            "FLAME IS THE ONLY LIGHT IN THE PICTURE and it sits BELOW AND NEARER THE "
            "CAMERA THAN EVERYTHING ELSE, so the light climbs UPWARD onto the undersides "
            "of the fingers and thumbs, spills warm THROUGH the thin webbing between them, "
            "picks out the cracked skin, the short nails and the grain of the terracotta, "
            "and then falls away to nothing — the whole background and the top of the "
            "frame are solid unlit black with no rim, edge, outline, ring or corona "
            "anywhere. A dark saturated wool sleeve enters at one corner, out of focus; no "
            "pale cloth appears anywhere. Fine film grain, deep true blacks."
        ),
    },
    {
        "id": "v2-r031-b39", "out": "s39-the-door-is-still-open-now.jpeg",
        "seg": "n16", "window": "133.387-137.027", "wide": False, "jesus": False,
        "locks": ["GATEWAY"] + _NIGHT,
        "narration": "And here's the good news. The door is still open now.",
        "must_show": "the same gateway STANDING OPEN — both plank leaves swung wide, warm lamplight pouring out through the whole opening across the threshold and far out onto the dark dust, and nobody blocking the way in.",
        "must_not_show": _NO_JESUS + _NO_DAY + _NO_HALO + _NO_MODERN_LAMP + "the doors are NOT shut and NOT closing — they stand wide open; no person standing in the opening or barring it; no metal hinge, strap, stud, handle, knocker, ring, lock or bolt; no arch, keystone or carved jamb; " + _NO_CREAM,
        "scene": (
            "One photograph, 28mm lens, deep midnight outside and warm light within — and "
            "it is the SAME gateway as before, deliberately the same camera position as "
            "the closing shot, now reversed. THE CAMERA STANDS OUT IN THE DARK FORECOURT "
            "SEVERAL PACES BACK FROM THE GATEWAY AND A LITTLE TO ITS LEFT, shooting "
            "toward the opening. THE TWO HEAVY PLANK LEAVES STAND SWUNG FULLY WIDE ON "
            "THEIR WOODEN PIVOTS, flat back against the inner faces of the wall, and THE "
            "WHOLE DEEP OPENING IS CLEAR — nobody stands in it, nobody bars it, nothing "
            "blocks it, and there is no person anywhere in the frame. Through it the "
            "wedding courtyard is warm and full of light: a dozen small clay lamps set LOW "
            "on the packed floor and along a waist-high mud-brick ledge, all of them well "
            "below head height, so the light rakes across the floor and up the lower walls "
            "and the far side of the courtyard stays soft and dim. THAT LIGHT POURS OUT "
            "THROUGH THE FULL WIDTH OF THE OPENING in one broad clean wedge, over the worn "
            "limestone threshold and far out across the dark packed dust of the forecourt "
            "toward the camera, reaching almost to the bottom edge of the frame — an "
            "invitation laid on the ground. Beyond that wedge, on both sides, the "
            "mud-brick wall and the forecourt and the deep blue-black starred sky above "
            "the flat roofline are unlit night. There is no corona, ring, contour or "
            "outline of light anywhere in the picture and no light source stands above head height. Fine "
            "film grain, deep true blacks, warm true amber in the doorway."
        ),
    },
    {
        "id": "v2-r031-b40", "out": "s40-worth-being-ready-for.jpeg",
        "seg": "n16", "window": "137.027-141.115", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "Tonight your lamp can be filled. He is worth being ready for.",
        "must_show": "Jesus on the Olivet ledge in the clear late afternoon, the story finished, his face open and warm toward the men in front of him — the last picture returns to where the video began.",
        "must_not_show": _NO_HALO + "no night, no lamp, no flame, no fire, no sunset, no sunrise and no golden low sun; no tree, no grove, no canopy and no building on the slope; no woman and no door anywhere in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, clear late-afternoon light warm and directional "
            "from the low right, the sun well up and OUT OF FRAME, the far valley and the "
            "bare far hills hazed, fine film grain. THE CAMERA STANDS OUT ON THE ROCK "
            "TO ONE SIDE AND SHOOTS ACROSS THE GROUP AT RIGHT ANGLES TO EVERY EYELINE, "
            "the same side-on geometry the video opened with. Jesus is seated on the low "
            "grey boulder at the RIGHT of the frame, seen from his left in three-quarter "
            "with his head turned well off the camera axis, his nose pointed toward the "
            "LEFT EDGE and his gaze travelling into the seated men and clean out through "
            "that LEFT EDGE — his pupils never come near the lens. THIS IS A WIDE "
            "FULL-LENGTH PHOTOGRAPH AND NOT A PORTRAIT: the camera is far enough back "
            "that Jesus AND at least four seated disciples are in frame together head to "
            "feet, with the ledge, the valley and the bare hazed far hillside behind them; "
            "he is never framed from the chest up. The story is finished: his hands have "
            "come to rest open on his knees, his shoulders have eased, and his face is "
            "open, warm and unhurried toward the men in front of him. The disciples are "
            "seen in profile and three-quarter from behind, still and quiet, their gazes "
            "travelling rightward and out through the RIGHT EDGE. His one plain undyed "
            "off-white cream wool robe is the ONLY pale thing anywhere in the picture; "
            "every disciple wears dark saturated wool, and there is NO pale, ivory, "
            "beige, taupe, buff or sand shape, shoulder, sleeve, drape or blurred mass "
            "anywhere in the foreground or at any edge. The clear daylight falls on him "
            "from the front right; nothing stands behind his head, and there is no bright "
            "rim, edge, ring, corona, aura or outline of light around his head, hair, "
            "beard or shoulders, and no light comes off him."
        ),
    },
]
