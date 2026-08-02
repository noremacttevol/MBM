#!/usr/bin/env python3
"""V2 beat map — row 28, build-28-hidden-treasure (Matthew 13:44), realistic.

COVERAGE: 29 pictures against V1's SEVEN, over 90.08 s of story = 3.11 s/picture.
V1 held `s7.jpeg` on screen from 67.75 s to 90.36 s — TWENTY-TWO AND A HALF SECONDS
across n9, n10 AND n11, which is the entire application of the parable including
"once you truly see who Jesus is, nothing else even compares" and the whole closing
turn about joy. `s1.jpeg` covered n0 and n1 (9.8 s), `s4.jpeg` covered n4 and the
first half of the KJV verse, `s5.jpeg` covered j1b, n5 and n6 (12.9 s) and `s6.jpeg`
covered n7 and n8 (11.8 s). Seven pictures for a ninety-second story.

⚠️ THE INHERITED beats_v2.py WAS DISCARDED, and this is why (measured, not assumed).
It planned 16 pictures at 5.6 s each and called that density a match for the library,
which it no longer is — rows 24-27 shipped at 3.1-4.9 s/picture. Worse, two of its
premises were wrong:
  * IT STAGED THE FRAME IN A HOUSE INTERIOR (Matthew 13:36), arguing that row 25 had
    already used a wide interior so a close one was "no repeat". Row 16 is already
    the wave's lamplit interior and the frame beats here run five times across the
    video; a second interior is the repeat, not the cure. Restaged in an OLIVE GROVE
    (see STAGING below), which no row in this wave has.
  * ITS TREASURE LOCK DESCRIBED "a small iron-banded wooden chest, its lid split
    with age". A hinged, iron-banded strongbox is a mediaeval object and it violates
    the shared PERIOD-MATERIALS lock outright (no machined fitting, no hinge). A
    first-century Judean hoard is a sealed fired-clay jar in the ground, which is
    also what makes the parable's law work — see PERIOD FACT below.

AUDIO IS CLEAN AND LOCKED (checked from the FILES, not from prose):
  * `matthew-13_hidden-treasure.mp4` last changed bytes 2026-07-27T22:44:25 and
    EVERY `audio/*.mp3` last changed bytes at that same commit (git CONTENT dates —
    mtimes are worthless in this repo, four machines pull it). No placed mp3 is
    newer than the MP4, so `assert_v1_final_is_current()`'s recency tripwire has
    nothing to refuse.
  * V1 MP4 runs 98.824 s, inside the guard's 0.75 s excess tripwire on the summed
    timeline.
  * SOURCING TRAP CHECKED AND CLEARED. All FIFTEEN segments (n0-n11, j1, j1b, card)
    were transcribed with faster-whisper `word_timestamps=True` and every one
    matches the LIVE `make_narration.py` word for word (whisper's own misspellings
    aside: "hidden a field" for "hid in a field", "witch" for "which", "heideth"
    for "hideth", "byeth" for "buyeth", plus a hallucinated repeat of its own first
    clause on the tail of n2 after the real speech ends at 13.71 s). NO
    `TEXT_OVERRIDES` are needed on this row and `AUDIO_FROM_V1_SEGMENTS` stays off.
  * The `.pre-speaker` sibling differs from the live script only in the docstring
    and the voice constants — not in one word of narration — so on this row the two
    sources do not disagree, and the audio confirms the live script independently.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with `extract_beats.py` reading the V1
build, then split inside each segment on WORD timings measured from that segment's
own mp3 with faster-whisper. THE `.timing.json` SIDECARS WERE NOT TRUSTED, and this
row's V1 audio folder carries no `.mp3.words.json` files at all (rows 26 and 27
proved both sidecar families unusable). Windows are SEGMENT-BOUNDARY CONTIGUOUS
(`seg_start` -> the next segment's `seg_start`, never `audio_start` -> `spoken_end`),
so there is no dead gap at any of the fourteen segment joins: contiguous 0.280 s ->
90.360 s (the card start), zero gaps, zero overlaps, shortest window 1.46 s, longest
5.27 s. Every split lands on a clause head or a sentence boundary and none falls
inside a word.

SCRIPTURE FACTS (Matthew 13:44 KJV — the whole parable is ONE VERSE):
  "Again, the kingdom of heaven is like unto treasure hid in a field; the which when
   a man hath found, he hideth, and for joy thereof goeth and selleth all that he
   hath, and buyeth that field."
Three things have to be readable in the pictures or the parable does not land:
  1. THE FIELD IS NOT HIS. He is a hired man breaking stony ground for wages on
     somebody else's land — so the treasure he finds he cannot keep, which is the
     entire reason he has to buy the field instead of simply taking the jar.
  2. HE HIDES IT AGAIN. The covering-back-over is an ACT, deliberate and careful,
     not an accident; the ground has to end up reading as untouched.
  3. THE JOY IS THE POINT. "For joy thereof" — the selling is not a sacrifice he
     grits his teeth through. Every selling frame carries a face that is GLAD, and
     the closing frames are open, loose and laughing, never grieving. The narration
     says it outright in n11 and V1 gave that whole idea no picture of its own.

PERIOD FACT THE STORY TURNS ON: in first-century Judea buried hoards were ordinary.
With no banks and repeated wars a household hid its silver in a sealed clay jar in
the ground, and if the family was killed or driven out the jar simply stayed there.
The law of the period held that such a find belonged to the OWNER OF THE LAND, which
is exactly why a labourer who found one bought the ground rather than the pot. So
the hoard is a fired-clay storage jar, its shoulder cracked by the tool, holding
irregular hand-struck silver coins and a few twisted gold ornaments — never a chest.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  rows 2, 8, 21 (Luke 15)      courtyard table / low wall under a fig / house meal
  row 11 (the storm)           an open boat at NIGHT in a gale
  row 16 (Mary & Martha)       a lamplit evening interior
  row 19 (breakfast on shore)  a Galilee beach at FIRST LIGHT with a charcoal fire
  row 22 (unmerciful servant)  a black basalt Capernaum doorstep and street
  row 23 (vineyard workers)    a terraced hillside above a vineyard
  row 24 (the sower)           a moored fishing boat off a daylit shingle beach
  row 25 (wheat and tares)     an open grain plain and a round threshing floor
  row 26 (mustard seed)        a small walled kitchen garden
  row 27 (the leaven)          a synagogue-wall stone bench and a walled baking yard
So this row is staged in THREE places, none of them used anywhere above:
  * THE FRAME — an OLIVE GROVE on the edge of the village, Jesus seated on the
    exposed roots of an ancient olive with the disciples low on the roots and stones
    around him, in warm level late-afternoon light broken into DAPPLE by the
    silver-green canopy. Matthew 13:36 has him leave the crowd and speak to the
    disciples alone and 13:44 opens "AGAIN", so this is a small closed circle
    mid-sequence — which the grove gives without borrowing row 27's synagogue bench,
    row 24's boat, or a second lamplit interior after row 16. No other row in this
    wave has a canopy, dappled light or olive trunks in it.
  * THE FIELD — a SMALL ENCLOSED STONY FIELD on the floor of a narrow side valley,
    walled all round with dry-stone field walls, a white chalk bank cut along one
    side, one dead terebinth stump, thistles in the corners. Deliberately NOT an
    open plain (row 25) and NOT cultivated crop ground (rows 24, 26): it is rough
    fallow being broken for the first time in years, which is why a landowner hires
    a man to swing a mattock at it, and the walls make it one saleable parcel a poor
    man could actually buy.
  * THE DOORYARD — bare beaten earth in front of a poor one-room mud-brick hut on
    the village edge, with a thorn-brush pen. Distinct from row 22's dressed BLACK
    BASALT doorstep and paved street in material, colour and scale, and it is a
    slope of dirt rather than a street.

THE CLOCK IS THE PLOT AND IT IS ON THE SCREEN. The parable is one day's turn plus
the morning after, and the light only ever moves FORWARD:
  b02-b12          HARD HIGH MIDDAY SUN in the field, short black shadows, white
                   glare off the chalk bank (hired work in the worst heat = poverty)
  b14-b18, b27     LOW WARM LATE-AFTERNOON sun, long shadows (he goes and sells)
  b19-b22          CLEAN EARLY-MORNING sun the next day (he buys; it is his)
  b24-b25          FLAT BRIGHT OVERCAST DAYLIGHT, no shadow (the "ordinary field")
  b28-b29          BRIGHT FULL MORNING SUN
The FRAME beats (b01, b11, b13, b23, b26) are ALL warm low late-afternoon dapple in
the grove and never change, because the frame is one continuous conversation.

TERRAIN IS THE INVARIANT (the rule rows 24/25/26/27 established). The field's four
walls, the tumbled gap in the near wall, the white chalk bank, the dead terebinth
stump and the ridge with the owner's house on it are described identically in every
frame; only the light and the state of the dug ground ever change.

CAST NOTE — ANCHOR-FIRST (the rows 20-27 lesson that has held the reroll rate at
3-15%). This row needs exactly TWO new faces, so exactly TWO beats are anchors and
they are generated in their OWN run before anything else, each composed so the face
is large, lit and unobstructed:
  b08  the MAN, kneeling over the open hoard, lit from the open sky
  b15  the OWNER, across the field wall, striking the bargain
`v2_gen_api` builds its REFS cache ONCE per run, so an anchor generated in the same
run as its dependants does not exist yet when they are built — it MUST be a separate
invocation. Jesus is held by JESUS-V2-REF as always.

A FACE SHEET ALONE DOES NOT HOLD A CHARACTER WHO IS SMALL IN FRAME (rows 19, 22-27).
So the MAN and OWNER locks state age, build, hair and dress as explicit invariants,
and every beat naming either of them RESTATES him positively in its own scene text —
including in the wides where he is a distant figure.

CREAM: only Jesus. THE TRAP ON THIS ROW IS THAT THE HERO IS A POOR LABOURER, which
is precisely the figure a model dresses in undyed off-white homespun linen — a
second, unlocked Jesus in every frame of his own story. So he is pinned ENTIRELY to
DARK UMBER-BROWN with a DARK RUSSET-RED head cloth, and the word "undyed" appears
nowhere in this file outside the Jesus lock itself, because on row 21 "undyed
grey-brown wool" rendered near-white every single time. Every near foreground is
stated POSITIVELY and DARK, because the single reroll on row 24 and one on row 25
were both an out-of-focus CREAM shoulder filling the near foreground beside Jesus.

THE SECOND TRAP ON THIS ROW IS THE TOOL. The story's hinge is "his spade struck
something hard", and a spade is the one object a model renders as a present-day
pressed-steel garden shovel with a D-handle and a foot tread — an object from a
garden centre that still satisfies PERIOD-MATERIALS' "hand-forged iron showing
hammer marks". It is also the largest, sharpest, most central thing in a digging
frame, so it cannot be missed. A new shared HAND-TOOLS lock was added to
`v2_prompt.py` for it and every working beat here opts into it by name.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER name a
# character. Clothing colours are stated POSITIVELY and DARK.
LOCKS = {
    # ------------------------------------------------------------- people ----
    "MAN": (
        "MAN LOCK: the hired labourer who finds the treasure is the SAME man in "
        "every shot, and these are invariants that hold even when he is small, "
        "distant, in shadow or out of focus: a working man of about thirty, lean and "
        "hard through the shoulders and forearms from digging, of middling height, "
        "with deeply sun-darkened olive-brown skin, a narrow weathered face with a "
        "strong straight nose, a short-cropped black beard, close-cut black hair, and "
        "quick dark brown eyes set under heavy black brows. There is a pale old scar "
        "about a finger long across the back of his right hand. His clothing NEVER "
        "changes: a DARK UMBER-BROWN coarse wool tunic to mid-calf with straight "
        "unshaped sleeves pushed up above the elbow, worn thin and patched at one "
        "shoulder with a DARK RUSSET-RED patch, a twisted DARK BROWN cord knotted at "
        "the waist, a DARK RUSSET-RED woven head cloth bound over his hair with a "
        "dark cord, and bare feet or plain dark leather sandals. Dust and dry pale "
        "soil on his dark sleeves, shins and face is correct and expected and is not "
        "clothing. EVERY PIECE OF CLOTH ON HIM IS COARSE WOOL WOVEN ON A LOOM and "
        "shows a visible over-and-under grid of warp and weft threads with a flat "
        "matte surface — never knitted, ribbed, cabled, jersey, fleeced, brushed or "
        "napped, and never a sweater or sweatshirt texture, including at the rolled "
        "sleeve, the neck opening, the hem and any blurred edge. He is NEVER dressed "
        "in cream, off-white, white, ivory, ecru, "
        "oatmeal, beige, taupe or pale linen and NEVER in any light-coloured garment "
        "of any kind anywhere in any frame; he never wears a mantle, cloak or shawl; "
        "and he is never old, never a boy, never fair-skinned and never long-haired."
    ),
    "OWNER": (
        "OWNER LOCK: the man who owns the field is the SAME man in every shot, and "
        "these are invariants that hold even when he is small, distant or out of "
        "focus: a settled landholder of about fifty-five, heavier and softer built "
        "than the labourer and a hand shorter, with lighter olive skin that has not "
        "been worked brown, a broad fleshy face with deep lines from the nose to the "
        "mouth corners, a full IRON-GREY beard cut square, iron-grey hair, and shrewd "
        "narrow brown eyes. He wears a DEEP INDIGO wool tunic to the ankle with "
        "straight unshaped sleeves worn down to the wrist, a heavy DARK MADDER-RED "
        "mantle of one rectangle of cloth over his left shoulder, a wide folded DARK "
        "BROWN cloth sash, a DEEP INDIGO head cloth bound with a dark cord, and good "
        "dark leather sandals. EVERY PIECE OF CLOTH ON HIM IS COARSE WOOL WOVEN ON A "
        "LOOM and shows a visible over-and-under grid of warp and weft threads with a "
        "flat matte surface — never knitted, ribbed, cabled, jersey, fleeced, brushed "
        "or napped, and never a sweater, jumper or sweatshirt texture, including at "
        "the cuff, the neck opening, the mantle edge and any blurred edge. He is "
        "NEVER dressed in cream, off-white, white, ivory, "
        "beige or pale linen and NEVER in any light-coloured garment anywhere in any "
        "frame; his hands are clean and uncallused and he never carries or uses a "
        "tool; and he is never young, never lean, never black-bearded."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the men gathered around Jesus in the olive grove are a small "
        "closed circle of eight to ten of his own disciples and NOBODY ELSE — no "
        "crowd, no women, no children, no passing stranger. They are Galilean working "
        "men between twenty-five and fifty, each with a distinct face, build and "
        "beard, none of them repeated or cloned, all seated low on the ground, the "
        "olive roots and loose stones. They wear DEEP INDIGO, DARK UMBER, DARK "
        "OLIVE-DRAB and RUSSET-RED coarse wool with head cloths of the same dark "
        "cloth. NOT ONE of them wears cream, off-white, white, ivory, beige or pale "
        "linen or any light-coloured garment anywhere in the frame, including blurred "
        "figures at the edges, because a pale garment on anyone but Jesus reads as a "
        "second, unlocked Jesus and fails the picture."
    ),
    "NEIGHBOURS": (
        "NEIGHBOURS LOCK: the villagers who come to buy his goods are people of this "
        "same poor place — three or four working men, two women and one old man "
        "leaning on a staff — each with a distinct face and none repeated, all of "
        "them at believable human scale beside the labourer. They wear DEEP INDIGO, "
        "DARK UMBER, RUSSET-RED and dark olive-drab coarse wool with dark head "
        "cloths. NOT ONE of them wears cream, off-white, white, ivory, beige or pale "
        "linen or any light-coloured garment anywhere in the frame, including blurred "
        "figures at the edges."
    ),
    # ------------------------------------------------------------ settings ----
    "GROVE": (
        "OLIVE-GROVE LOCK — this place is IDENTICAL in every frame it appears in and "
        "nothing about it ever changes: a small old OLIVE GROVE on the edge of a "
        "village, perhaps twenty trees standing in loose rows on a gently sloping "
        "floor of dry pale-brown earth and loose limestone. The trees are ancient — "
        "thick fissured trunks a man cannot reach around, hollowed and twisted with "
        "age, their bark silver-grey and deeply grooved, standing on knuckled roots "
        "that break out of the ground and make natural seats. The canopy is fine "
        "narrow SILVER-GREEN leaves that break the light into moving DAPPLE across "
        "the ground and across every person under it. One long low field wall of "
        "dry-laid unmortared limestone runs along the upper edge of the grove. Beyond "
        "the trees the ground falls away to low tawny bare hills. The light in every "
        "frame here is WARM LOW LATE-AFTERNOON SUN coming in almost level beneath the "
        "canopy from one side, throwing long soft-edged shadows. There is no "
        "building, no roof, no wire, no cable, no pipe, no fence post, no cut timber "
        "and no straight manufactured line anywhere in this grove; every trunk, root, "
        "stone and wall is irregular and either hand-laid or grown."
    ),
    "FIELD": (
        "FIELD LOCK — this place is IDENTICAL in every frame it appears in and only "
        "the light and the state of the dug ground ever change: ONE small enclosed "
        "field, roughly forty paces by twenty-five, lying on the flat floor of a "
        "narrow side valley. It is ENCLOSED ON ALL FOUR SIDES by DRY-STONE FIELD "
        "WALLS about waist high, built of unmortared rough limestone blocks stacked "
        "by hand and uneven along the top, with ONE GAP the width of a man in the "
        "near wall where the wall has tumbled. The ground inside is rough stony "
        "fallow — hard pale-tan sun-baked soil thick with loose flat stones, dry grey "
        "thistles standing in the corners, and one broad worked patch in the middle "
        "where the soil has been broken and turned to a darker crumbled brown. On the "
        "left side of the field a WHITE CHALK BANK about twice the height of a man is "
        "cut back into the valley side, glaring and bright. ONE DEAD TEREBINTH STUMP, "
        "grey, split and barkless, stands near the far wall. Beyond the far wall the "
        "valley side rises to a low ridge, and on that ridge stands ONE flat-roofed "
        "mud-brick house with a walled yard — the owner's house — always in the same "
        "place and always small in the distance. Every wall, stump, thistle and stone "
        "in this field is irregular and either hand-laid or natural; there is NO "
        "fence, no post, no wire, no rail, no gate, no hedge, no track of laid stone, "
        "no pipe, no cable and no straight manufactured line anywhere in the field, "
        "along its walls, or against the sky. THIS VALLEY IS BARE AND TREELESS: there "
        "is NO olive tree, no olive grove, no orchard, no terraced planting and no "
        "tree, trunk, canopy or green foliage of any kind inside this field, beside "
        "its walls, on the valley sides or on the ridge — the only woody thing "
        "anywhere in it is the one dead grey barkless terebinth stump."
    ),
    "YARD": (
        "DOORYARD LOCK — this place is IDENTICAL in every frame it appears in and "
        "only the light and what is lying on the ground ever change: the bare beaten "
        "earth DOORYARD of a poor one-room hut on the outer edge of a village, set on "
        "a gentle dirt slope. The hut is built of rough tan MUD BRICK with mud "
        "plaster falling away in patches at the corners, has a FLAT roof of poles and "
        "packed earth with a rough wooden roller lying on it, and ONE low doorway of "
        "three hewn planks with a worn stone threshold. There is ONE small square "
        "window opening with no glass and no shutter. Against the hut wall stands a "
        "large fired-clay water jar on a flat stone. To one side a small pen is "
        "fenced with piled dry thorn brush. The ground is hard swept dirt with a few "
        "loose stones. Beyond the yard the dirt slope falls away toward the other "
        "flat mud roofs of the village and low tawny bare hills close the horizon. "
        "Every building surface here is mud brick or mud plaster with a FLAT roof; "
        "there is no dome, no tower, no minaret, no bell tower, no arch of dressed "
        "voussoirs, no tiled or pitched roof, no column, no glass, no shutter, no "
        "corrugated or sheet metal, no pipe, no wire and no cable anywhere on any "
        "building or against the sky."
    ),
    "TREASURE": (
        "TREASURE LOCK: the treasure is ONE buried hoard and it is always the same "
        "one. It is a round-bellied FIRED-CLAY STORAGE JAR about the size of a man's "
        "head, buff-grey and gritty, its neck sealed long ago with a flat clay "
        "stopper and its SHOULDER FRESHLY CRACKED OPEN in one jagged break where the "
        "iron struck it, the broken edges pale and sharp against the weathered "
        "outside. Spilling from that break are IRREGULAR HAND-STRUCK SILVER COINS, "
        "each a small uneven lump of dull tarnished grey-white metal with a crude "
        "off-centre device beaten into one face and a plain rough rim, no two exactly "
        "alike, together with a few twisted GOLD ornaments — two open bangles, a "
        "heavy ring and a coil of gold wire — soft warm yellow and dented with age. "
        "The coins and gold are DULL and matte with earth still on them and they "
        "never glitter, sparkle, shine like new metal, emit light or glow. THERE IS "
        "NO milled, ridged, reeded or knurled edge on any coin, no perfectly round "
        "disc, no printing, lettering, numerals, date or portrait of any modern kind, "
        "no stacked or rolled coins, no gemstone, no crown, no chest, no casket, no "
        "hinge, no lock, no metal box and no wooden strongbox anywhere in the picture."
    ),
}

OUTPUT_ASSET_DIR = "assets"

# Every V1 mp3 and the V1 MP4 share ONE git content date (2026-07-27T22:44:25) and the
# MP4's runtime sits inside the guard's tripwire, so the finished V1 audio stream is
# current and the normal packet-copy AUDIO LOCK applies. Nothing is re-voiced and V1
# is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Filled in AFTER the two anchor beats are generated in their own run. v2_gen_api
# builds this cache once per invocation, so an anchor cannot be referenced by a beat
# generated in the same run as itself.
REFS = {
    "MAN": "assets/s08-worth-more-than-he-had-ever-seen.jpeg",
    "OWNER": "assets/s15-and-buyeth-that-field.jpeg",
}

BEATS = [
    # ================= FRAME — the olive grove, warm low late afternoon ========
    {
        "id": "v2-r028-b01", "out": "s01-jesus-told-a-very-short-story.jpeg",
        "seg": "n0", "window": "0.280-2.120", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": "Jesus once told a very short story",
        "must_show": "Jesus seated on the knuckled exposed roots of an ancient olive in a grove, beginning to speak, with his small closed circle of disciples seated low on the roots and stones around him in warm low late-afternoon dapple.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no midday overhead glare, no overcast; no field, no dry-stone field wall, no chalk bank, no dead stump, no mattock, no clay jar, no coins, no mud-brick hut and no dooryard anywhere in this frame; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming in almost "
            "level beneath the olive canopy from the left and broken into moving "
            "dapple across the ground and across every man under it, fine film grain. "
            "THE CAMERA IS PLACED COMPLETELY SIDE-ON TO THE WHOLE CIRCLE, STANDING OUT "
            "AMONG THE TRUNKS WELL TO ONE SIDE AND SHOOTING ACROSS THE GROUP AT RIGHT "
            "ANGLES TO EVERY EYELINE IN THE PICTURE. Jesus sits at the LEFT of the "
            "frame on the exposed roots of a thick fissured olive trunk and the "
            "disciples are ranged on the ground to the RIGHT of him, so the whole "
            "conversation runs HORIZONTALLY ACROSS THE FRAME: his gaze travels "
            "rightward into the seated men and exits through the RIGHT EDGE, and every "
            "disciple is seen in profile or three-quarter from behind with a gaze "
            "travelling leftward and out through the LEFT EDGE. NOT ONE MAN'S FACE IS "
            "SQUARED UP TO THE CAMERA AND NOT ONE PAIR OF PUPILS IS CENTRED ON THE "
            "LENS. Two seated backs fill the near bottom corners, soft and out of "
            "focus, a DEEP INDIGO shouldered back and dark indigo head cloth at the "
            "near left and a DARK UMBER back and dark brown head cloth at the near "
            "right, with nothing pale, grey, beige, taupe, ivory or off-white anywhere "
            "on either of them. Sharp in the middle distance Jesus sits on the root "
            "with his back half against the silver-grey grooved trunk, seen from his "
            "left side, leaning forward with his forearms on his knees and one hand "
            "opening as he begins to speak. Around him the disciples sit low on roots "
            "and loose limestone in dark indigo, umber, olive-drab and russet wool, "
            "all of them turned toward him in profile. Behind them the grove's trunks "
            "recede and the long low dry-laid limestone wall runs along the upper edge "
            "under silver-green leaves."
        ),
    },
    {
        "id": "v2-r028-b02", "out": "s02-about-a-man-and-a-field.jpeg",
        "seg": "n0", "window": "2.120-5.400", "wide": True,
        "locks": ["FIELD", "HAND-IRRIGATION"],
        "narration": "about a man, and a field.",
        "must_show": "a wide establishing photograph of the small enclosed stony field on the floor of the narrow side valley, empty of people, under hard high midday sun — its dry-stone walls on all four sides, the one tumbled gap in the near wall, the white chalk bank on the left, the dead terebinth stump, and the owner's flat-roofed house small on the ridge beyond.",
        "must_not_show": "no person anywhere in this frame; no Jesus; no olive grove, no olive trees, no dappled light, no late-afternoon or golden light; no mud-brick hut and no dooryard; no clay jar, no coins, no mattock; no dug hole and no dark turned soil heaped anywhere; nothing lying on the ground in a straight dark line.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, HARD HIGH MIDDAY SUN "
            "almost straight overhead so every stone throws a short black shadow "
            "directly beneath itself and the white chalk bank glares, a thin heat "
            "shimmer above the far wall, fine film grain. THE CAMERA STANDS OUTSIDE "
            "THE FIELD AT THE TUMBLED GAP IN THE NEAR WALL, at chest height, LOOKING "
            "STRAIGHT ACROSS THE WHOLE ENCLOSURE toward the far wall and the ridge "
            "beyond. The near foreground across the bottom of the frame is the rough "
            "grey unmortared limestone top of the near wall itself, sharp and close, "
            "with a dry grey thistle growing at its foot, and there is nobody and "
            "nothing between the camera and the field. Beyond it the hard pale-tan "
            "sun-baked ground runs away from the camera, thick with loose flat stones, dry grey "
            "thistles standing in the corners. The white chalk bank is cut back into "
            "the valley side along the left, twice the height of a man and brilliant "
            "in the overhead light. The grey split barkless terebinth stump stands "
            "near the far wall. Beyond the far wall the valley side rises to a low "
            "ridge where one small flat-roofed mud-brick house with a walled yard "
            "stands against a bleached pale-blue sky. The whole picture is empty, hot, "
            "ordinary and worth nothing to look at."
        ),
    },
    {
        "id": "v2-r028-b03", "out": "s03-he-was-a-hired-worker.jpeg",
        "seg": "n1", "window": "5.400-6.860",
        "locks": ["MAN", "FIELD", "HAND-TOOLS", "HAND-IRRIGATION"],
        "narration": "He was a hired worker,",
        "must_show": "the labourer caught at the top of his swing with the mattock, seen from the side, breaking the stony ground of the field under hard high midday sun, sweat and dust on him.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no late-afternoon or golden light; no other person anywhere in the frame; no clay jar, no coins and no treasure yet; no steel spade or shovel, no D-handle, no foot tread on any blade; no cream, off-white, ivory, beige or pale garment on him; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, HARD HIGH MIDDAY SUN almost straight overhead "
            "throwing a short black shadow directly under him, fine film grain. THE "
            "CAMERA STANDS INSIDE THE FIELD WELL TO HIS LEFT AND SLIGHTLY LOW, "
            "SHOOTING HIM IN CLEAN SIDE PROFILE ACROSS THE FRAME. HIS GAZE HAS A NAMED "
            "TARGET INSIDE THE PICTURE: the patch of broken stony ground directly "
            "under the mattock head at the lower right of the frame, so his head is "
            "down and his eyeline runs steeply down and to the right, leaving the "
            "picture through the BOTTOM RIGHT and nowhere near the lens. He is framed "
            "from the knees up, caught at the very top of the swing with the mattock "
            "haft up and back behind his right shoulder and both arms extended, his "
            "whole body wound and about to come down — a lean hard-shouldered working "
            "man of about thirty with deeply sun-darkened olive-brown skin, a narrow "
            "weathered face, a short-cropped black beard, close-cut black hair under a "
            "DARK RUSSET-RED head cloth bound with a dark cord, and a DARK UMBER-BROWN "
            "coarse wool tunic to mid-calf with the sleeves pushed up above the elbow "
            "and a DARK RUSSET-RED patch at one shoulder, a twisted dark brown cord at "
            "his waist. Sweat runs at his temple and pale dust films his dark sleeves "
            "and shins. The near foreground along the bottom edge is broken dark-brown "
            "turned soil and loose flat stones, with nobody between the camera and "
            "him. Behind him the white chalk bank glares out of focus and the "
            "dry-stone far wall runs level under a bleached sky."
        ),
    },
    {
        "id": "v2-r028-b04", "out": "s04-a-field-that-wasnt-even-his-own.jpeg",
        "seg": "n1", "window": "6.860-10.070", "wide": True,
        "locks": ["MAN", "FIELD", "HAND-TOOLS", "HAND-IRRIGATION"],
        "narration": "out digging in a field that wasn't even his own.",
        "must_show": "a wide photograph in which the labourer is ONE SMALL DARK FIGURE bent over his mattock alone in the middle of the big walled field, with the owner's flat-roofed house standing on the ridge above him — the whole picture saying the ground is not his.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no golden or late-afternoon light; no second person anywhere in the field; no clay jar, no coins and no treasure yet; no steel spade or shovel, no D-handle, no foot tread; no cream, off-white, ivory, beige or pale garment on him; his face is too far away to read and his pupils are never centred on the lens.",
        "scene": (
            "One photograph, 35mm lens, deep depth of field, HARD HIGH MIDDAY SUN "
            "straight overhead, short black shadows, the white chalk bank glaring, "
            "fine film grain. THE CAMERA STANDS UP ON THE LOW RIDGE BESIDE THE OWNER'S "
            "HOUSE AND LOOKS DOWN ACROSS THE VALLEY FLOOR INTO THE FIELD, so the man "
            "is seen from BEHIND AND ABOVE and not one part of his face is turned "
            "toward the lens. The near foreground across the bottom of the frame is "
            "the corner of the owner's own walled yard — rough tan mud-brick wall and "
            "hard swept dirt, sharp and close — with nobody between the camera and the "
            "drop. Small in the middle distance, alone on the pale stony floor of the "
            "walled field, the labourer is bent over his mattock mid-stroke, "
            "unmistakably the same man: a lean working man in a DARK UMBER-BROWN "
            "coarse wool tunic with a DARK RUSSET-RED patch at one shoulder and a DARK "
            "RUSSET-RED head cloth, his dark shape the only thing moving in the "
            "enclosure. He is small enough that all four of the field's dry-stone "
            "walls fit around him inside the frame, and the tumbled gap in the near "
            "wall, the dry thistles in the corners, the grey split terebinth stump and "
            "the white chalk bank cut into the valley side are all clearly larger than "
            "he is. The valley sides close in on both sides and low tawny bare hills "
            "stand beyond under a bleached pale-blue sky."
        ),
    },
    {
        "id": "v2-r028-b05", "out": "s05-his-spade-struck-something-hard.jpeg",
        "seg": "n2", "window": "10.070-15.060",
        "locks": ["MAN", "FIELD", "TREASURE", "HAND-TOOLS", "HAND-IRRIGATION"],
        "narration": "And on one ordinary day, his spade struck something hard, buried in the ground.",
        "must_show": "a close low photograph of the moment of contact — the pitted hand-forged iron mattock blade stopped dead against the buff-grey shoulder of a buried fired-clay jar in the broken soil, one fresh jagged crack opening across the jar, dust jumping off the impact.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no golden or late-afternoon light; no other person in the frame and no face anywhere; no coins visible yet and no gold visible yet; no steel spade or shovel, no D-handle, no foot tread, no chromed or painted metal; no cream, off-white, ivory, beige or pale garment anywhere; nobody looking into the lens.",
        "scene": (
            "One photograph, 85mm macro lens, shallow depth of field, HARD HIGH MIDDAY "
            "SUN straight overhead so the crack throws a hard black line and the dust "
            "in the air catches the light, fine film grain. THE CAMERA IS SET DOWN ON "
            "THE STONY GROUND OF THE FIELD AT SOIL LEVEL, A HAND'S BREADTH ABOVE THE "
            "DIRT, LOOKING ALONG THE FLOOR OF THE FIELD, AND IT IS TILTED UP JUST "
            "ENOUGH THAT A CLEAR BAND OF THE FIELD RUNS ACROSS THE UPPER QUARTER OF "
            "THE FRAME: the unmortared rough limestone of the dry-stone wall, a dry "
            "grey thistle, the glare of the white chalk bank and a strip of bleached "
            "sky, all thrown far out of focus, so the picture is unmistakably outdoors "
            "in this valley and in this century. Sharp and filling the lower two "
            "thirds: the heavy hand-forged iron mattock blade, dark grey, uneven, "
            "pitted and hammer-marked with its worn bright edge, driven into the "
            "broken dark-brown soil and STOPPED DEAD against the round buff-grey "
            "gritty shoulder of a buried fired-clay jar, with ONE FRESH JAGGED CRACK "
            "running away from the point of contact and its broken edges showing pale "
            "against the weathered outside. Dry pale dust jumps off the impact and "
            "hangs in the overhead light. The straight rough-hewn unpainted wooden "
            "haft runs up out of the top of the frame, and a single strong "
            "sun-darkened hand with a pale old scar across the back of it grips the "
            "haft low down at the very edge of the picture, the DARK UMBER-BROWN "
            "sleeve pushed above the elbow. No face is in the frame at all."
        ),
    },
    {
        "id": "v2-r028-b06", "out": "s06-he-cleared-away-the-dirt.jpeg",
        "seg": "n3", "window": "15.060-17.840",
        "locks": ["MAN", "FIELD", "TREASURE", "HAND-IRRIGATION"],
        "narration": "He cleared away the dirt — and there it was.",
        "must_show": "the labourer's two bare hands scraping and sweeping loose earth back off the cracked shoulder of the buried clay jar, uncovering it in the bottom of a shallow scooped hole in the field floor.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no golden or late-afternoon light; no other person in the frame; no gold and no spilled coins yet; no steel spade or shovel; no cream, off-white, ivory, beige or pale garment anywhere; nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, HARD HIGH MIDDAY SUN "
            "straight overhead dropping his own short shadow across the lip of the "
            "hole, fine film grain. THE CAMERA IS SET LOW AND WELL TO HIS RIGHT, AT "
            "THE LIP OF THE SHALLOW HOLE, LOOKING ACROSS AND DOWN INTO IT, AND TILTED "
            "SO A BAND OF THE FIELD — stony pale-tan ground, the grey unmortared "
            "limestone of the far dry-stone wall and the glare of the white chalk bank "
            "— RUNS ACROSS THE TOP OF THE FRAME OUT OF FOCUS. Sharp and filling the "
            "centre are two strong sun-darkened working hands with a pale old scar "
            "across the back of the right one, DARK UMBER-BROWN sleeves pushed above "
            "the elbow, dragging and sweeping the loose dry earth back off the "
            "buff-grey gritty shoulder of the buried fired-clay jar in the bottom of "
            "the scooped hole, the jagged fresh crack across it now clear, soil "
            "falling from between his fingers. The near foreground along the bottom "
            "edge is the dark-brown turned soil heaped at the hole's rim with loose "
            "flat stones on it, and there is nobody between the camera and his hands. "
            "His face is entirely outside the top of the frame and he is the only "
            "person in the picture."
        ),
    },
    {
        "id": "v2-r028-b07", "out": "s07-a-treasure-hidden-forgotten.jpeg",
        "seg": "n3", "window": "17.840-21.060",
        "locks": ["FIELD", "TREASURE", "HAND-IRRIGATION"],
        "narration": "A treasure. Hidden, forgotten,",
        "must_show": "a close photograph looking straight down into the opened hole at the hoard itself — the cracked fired-clay jar on its side with irregular hand-struck silver coins and a few twisted gold ornaments spilling out of the break into the dark soil, earth still clinging to them.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no golden or late-afternoon light; no person, no hand, no arm and no face anywhere in this frame; no glitter, no sparkle, no light coming off the metal, no glow; no perfectly round coin, no milled or reeded edge, no lettering, numerals or date; no chest, casket, hinge, lock, gemstone or crown; no steel spade or shovel.",
        "scene": (
            "One photograph, 85mm macro lens, shallow depth of field, HARD HIGH MIDDAY "
            "SUN straight overhead falling directly into the open hole, fine film "
            "grain. THE CAMERA IS HELD DIRECTLY ABOVE THE SHALLOW HOLE IN THE FLOOR OF "
            "THE FIELD LOOKING STRAIGHT DOWN, AND IT IS FRAMED WIDE ENOUGH THAT A BAND "
            "OF THE FIELD ITSELF RUNS AROUND THE OUTSIDE OF THE FRAME: hard pale-tan "
            "sun-baked stony ground, loose flat limestone, dry grey thistle stalks and "
            "the heaped dark-brown turned soil at the hole's rim, all softly out of "
            "focus, so the picture is unmistakably outdoors on this ground. Sharp in "
            "the middle of the frame lies the hoard: the round-bellied buff-grey "
            "fired-clay jar tipped on its side in the dark soil, its shoulder broken "
            "open in one jagged crack with the broken edges pale against the weathered "
            "outside, and out of that break a slide of IRREGULAR HAND-STRUCK SILVER "
            "COINS — small uneven lumps of dull tarnished grey-white metal, each with "
            "a crude off-centre device beaten into one face and a plain rough rim, no "
            "two alike — mixed with two open twisted gold bangles, a heavy gold ring "
            "and a coil of gold wire, soft warm yellow and dented with age. Dry earth "
            "still clings in every hollow and every coin is DULL and matte. Nothing in "
            "the picture shines, glitters or gives off light."
        ),
    },
    {
        "id": "v2-r028-b08", "out": "s08-worth-more-than-he-had-ever-seen.jpeg",
        "seg": "n3", "window": "21.060-24.550",
        "locks": ["MAN", "FIELD", "TREASURE", "HAND-IRRIGATION"],
        "narration": "and worth more than he had ever seen in his life.",
        "must_show": "THE LABOURER'S OWN FACE, large and clearly lit, as he kneels over the open hoard — the whole picture is his face and what is happening in it: disbelief and dawning understanding, mouth slightly open, dust and sweat on him.",
        "must_not_show": "no Jesus in this frame; no olive grove, no olive tree, no trunk and no green canopy anywhere; no dappled light, no golden or late-afternoon light; no second person anywhere in the frame; no wide view of the whole field, no distant ridge house and no view looking straight down into the hole; no perfectly round machine-made coin, no milled or reeded edge, no lettering or numerals; no steel spade or shovel; no knitted, ribbed or fleece fabric on him; no cream, off-white, ivory, beige or pale garment on him; his face is never squared to the camera and his pupils are never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, HARD HIGH "
            "MIDDAY SUN almost straight overhead with strong clean bounce light coming "
            "back up off the pale stony ground and the white chalk bank so his face is "
            "fully and evenly lit with no part of it lost in shadow, fine film grain. "
            "THE CAMERA IS SET LOW ON THE FIELD FLOOR COMPLETELY SIDE-ON TO HIM, OUT "
            "AT HIS LEFT SHOULDER AND AT RIGHT ANGLES TO THE WAY HE IS FACING, "
            "LOOKING SLIGHTLY UP. HIS WHOLE HEAD IS TURNED AWAY FROM THE CAMERA AXIS "
            "AND HIS FACE IS SEEN IN CLEAN THREE-QUARTER PROFILE FROM HIS LEFT SIDE, "
            "THE LINE OF HIS NOSE POINTING TOWARD THE RIGHT EDGE OF THE FRAME AND "
            "DOWNWARD, SO THE CAMERA SEES HIS CHEEK, HIS JAW AND THE OUTER CORNER OF "
            "HIS FAR EYE RATHER THAN THE FRONT OF HIS FACE. HIS GAZE HAS A NAMED "
            "TARGET INSIDE THE PICTURE: the spilled silver lying at the bottom of the "
            "hole in the LOWER RIGHT of the frame, well away from the camera, so his "
            "eyeline runs down and to the right across the picture and exits through "
            "the BOTTOM RIGHT CORNER. NEITHER OF HIS PUPILS IS CENTRED ON THE LENS AND "
            "HE IS NOT FACING THE CAMERA AT ALL. He fills the frame from the chest up "
            "and he is the only person in "
            "the picture — a lean hard-shouldered working man of about thirty, deeply "
            "sun-darkened olive-brown skin, a narrow weathered face with a strong "
            "straight nose, a short-cropped black beard, close-cut black hair under a "
            "DARK RUSSET-RED head cloth bound with a dark cord, heavy black brows over "
            "quick dark brown eyes now wide, his lips parted, his breath stopped. Pale "
            "dust films his cheek and a bead of sweat runs at his temple. He wears the "
            "DARK UMBER-BROWN coarse wool tunic with the sleeves pushed above the "
            "elbow and the DARK RUSSET-RED patch at one shoulder, and one strong hand "
            "with a pale old scar across its back rests on the rim of the hole. The "
            "near foreground at the bottom edge is the dark heaped soil of the hole's "
            "rim with one dull tarnished silver coin lying on it, and there is nobody "
            "between the camera and him. The stony field, the dry-stone wall and the "
            "bleached sky fall completely out of focus behind him."
        ),
    },
    {
        "id": "v2-r028-b09", "out": "s09-his-heart-pounded.jpeg",
        "seg": "n4", "window": "24.550-27.330",
        "locks": ["MAN", "FIELD", "HAND-IRRIGATION"],
        "narration": "His heart pounded. Quickly, quietly,",
        "must_show": "the labourer risen off his knees into a tight crouch beside the open hole and looking sharply away across the field toward the tumbled gap in the near wall, checking that he is alone, his whole body held and listening.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no golden or late-afternoon light; no second person anywhere in the frame; no close portrait of his face filling the frame and no view looking straight down into the hole; no coins spilled loose across the ground; no steel spade or shovel; no cream, off-white, ivory, beige or pale garment on him; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, HARD HIGH MIDDAY SUN straight overhead, a "
            "short hard black shadow directly under him, fine film grain. THE CAMERA "
            "STANDS INSIDE THE FIELD BEHIND HIM AND TO HIS RIGHT, SHOOTING PAST HIS "
            "SHOULDER FROM THREE-QUARTERS BEHIND, so most of his back is toward the "
            "lens and only the edge of his cheekbone and brow is visible. HIS GAZE HAS "
            "A NAMED TARGET INSIDE THE PICTURE: the tumbled gap in the dry-stone near "
            "wall away at the far left of the frame, so his head is turned hard left "
            "and his eyeline runs horizontally across the picture and exits through "
            "the LEFT EDGE, at right angles to the camera. He is framed from the "
            "thighs up, risen off his knees into a tight crouch beside the open hole, "
            "one hand flat on the stony ground and the other still on the hole's rim, "
            "everything about him held and listening — a lean working man of about "
            "thirty in a DARK UMBER-BROWN coarse wool tunic with the sleeves above the "
            "elbow and a DARK RUSSET-RED patch at one shoulder, a DARK RUSSET-RED head "
            "cloth over close-cut black hair, a short black beard on the visible edge "
            "of his jaw. The near foreground at the bottom right is his own dark "
            "shoulder and the heaped dark-brown soil at the hole's rim, out of focus, "
            "and there is nobody between the camera and him. Beyond him the empty "
            "stony field runs away to the dry-stone walls, the grey terebinth stump, "
            "the glaring white chalk bank and the ridge house tiny in the distance. He "
            "is the only person in the picture."
        ),
    },
    {
        "id": "v2-r028-b10", "out": "s10-he-covered-it-back-over.jpeg",
        "seg": "n4", "window": "27.330-30.480",
        "locks": ["MAN", "FIELD", "HAND-IRRIGATION"],
        "narration": "he covered it back over — and told no one.",
        "must_show": "the labourer's two bare hands pushing and pressing the loose dark soil back down flat over the filled hole, tamping it with the heels of his palms so the ground reads as untouched again.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no golden or late-afternoon light; no second person in the frame; no clay jar and no coins visible any more, nothing of the hoard showing; no open hole; no steel spade or shovel; no cream, off-white, ivory, beige or pale garment anywhere; nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, HARD HIGH MIDDAY SUN "
            "straight overhead raking the pressed soil so every palm print throws its "
            "own tiny shadow, fine film grain. THE CAMERA IS SET LOW ON THE FIELD "
            "FLOOR JUST BEYOND THE FILLED PATCH AND WELL TO HIS LEFT, LOOKING ACROSS "
            "AND DOWN AT THE GROUND, AND TILTED SO A BAND OF THE FIELD — pale-tan "
            "stony ground, dry grey thistles and the grey unmortared limestone of the "
            "far dry-stone wall — RUNS ACROSS THE TOP OF THE FRAME OUT OF FOCUS. Sharp "
            "in the centre are two strong sun-darkened hands with a pale old scar "
            "across the back of the right one, DARK UMBER-BROWN sleeves pushed above "
            "the elbow, pressing down hard with the heels of both palms on a broad "
            "patch of dark-brown crumbled soil, smoothing and tamping it level with "
            "the pale stony ground around it, loose flat stones already scattered back "
            "across the top of it. Nothing of the jar, the silver or the gold is "
            "visible anywhere. His forearms run up out of the top of the frame and his "
            "face is entirely outside it; he is the only person in the picture. The "
            "near foreground along the bottom edge is undisturbed pale stony field "
            "floor with nobody between the camera and his hands."
        ),
    },
    # ==================== KJV — Matthew 13:44, Jesus speaking ==================
    {
        "id": "v2-r028-b11", "out": "s11-like-unto-treasure-hid-in-a-field.jpeg",
        "seg": "j1", "window": "30.480-32.580", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": "Again, the kingdom of heaven is like unto",
        "must_show": "a wide photograph along the olive grove as Jesus speaks the parable, one hand turned palm-up in front of him, the disciples seated low on the roots and stones leaning in toward him in warm low late-afternoon dapple.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no midday overhead glare, no overcast; no field, no dry-stone field wall, no chalk bank, no dead stump, no mattock, no clay jar, no coins, no mud-brick hut and no dooryard anywhere in this frame; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming in almost "
            "level beneath the olive canopy from the left and broken into moving "
            "dapple, fine film grain. THE CAMERA IS PLACED COMPLETELY SIDE-ON TO THE "
            "WHOLE CIRCLE, STANDING AMONG THE TRUNKS WELL TO ONE SIDE AND SHOOTING "
            "ACROSS THE GROUP AT RIGHT ANGLES TO EVERY EYELINE, so the conversation "
            "runs HORIZONTALLY ACROSS THE FRAME. Jesus sits at the RIGHT of the frame "
            "SEEN FROM HIS LEFT SIDE IN CLEAN PROFILE on the knuckled roots of the "
            "thick fissured olive, and the disciples are ranged on the ground to the "
            "LEFT of him. HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: those seated "
            "men at the left of the frame, so his eyeline travels leftward across the "
            "picture and exits through the LEFT EDGE, while every disciple is seen in "
            "profile or three-quarter from behind with an eyeline travelling rightward "
            "and out through the RIGHT EDGE. NOT ONE MAN'S FACE IS SQUARED UP TO THE "
            "CAMERA AND NOT ONE PAIR OF PUPILS IS CENTRED ON THE LENS. Two seated "
            "backs fill the near bottom corners, soft and out of focus, a DARK "
            "OLIVE-DRAB shouldered back at the near left and a DEEP INDIGO back at the "
            "near right, with nothing pale, grey, beige, taupe, ivory or off-white on "
            "either of them. Sharp in the middle distance Jesus sits with his back "
            "half against the silver-grey grooved trunk, his near hand lifted and "
            "turned palm-up in the explaining gesture, his lips parted mid-word. The "
            "other disciples sit low on roots and loose limestone in dark indigo, "
            "umber, olive-drab and russet wool. The grove's ancient trunks recede "
            "behind them and the long low dry-laid limestone wall runs along the upper "
            "edge under the silver-green canopy, with low tawny hills beyond."
        ),
    },
    {
        "id": "v2-r028-b12", "out": "s12-the-ground-looks-untouched.jpeg",
        "seg": "j1", "window": "32.580-35.000",
        "locks": ["FIELD", "HAND-IRRIGATION"],
        "narration": "treasure hid in a field;",
        "must_show": "a close photograph of the flat tamped patch of ground in the field with ONE flat limestone stone laid deliberately on it as a private mark — a piece of ordinary dirt that gives away nothing, with the empty field running away beyond it.",
        "must_not_show": "no Jesus in this frame; no olive grove, no dappled light, no golden or late-afternoon light; no person, no hand, no arm and no face anywhere in this frame; no clay jar, no coins and no gold visible; no open hole and no loose heaped soil; no steel spade or shovel; nothing lying on the ground in a straight dark line.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, HARD HIGH MIDDAY SUN "
            "straight overhead so the single laid stone throws one short hard black "
            "shadow, fine film grain. THE CAMERA IS SET DOWN ON THE FLOOR OF THE FIELD "
            "AT SOIL LEVEL A SHORT WAY FROM THE PATCH, LOOKING ALONG THE GROUND, AND "
            "IT IS TILTED UP JUST ENOUGH THAT THE WHOLE UPPER THIRD OF THE FRAME "
            "CARRIES THE FIELD AND THE VALLEY: the grey unmortared limestone of the "
            "far dry-stone wall, the grey split barkless terebinth stump, the glaring "
            "white chalk bank cut into the valley side and the low ridge with the "
            "small flat-roofed mud-brick house on it under a bleached pale-blue sky, "
            "all softly out of focus. Sharp in the near middle of the frame is a broad "
            "flat patch of dark-brown soil pressed smooth and level into the pale-tan "
            "stony ground, loose flat stones scattered across it so it reads as "
            "ordinary, with ONE hand-sized flat piece of grey limestone laid squarely "
            "in the centre of it — placed, not fallen. The near foreground along the "
            "bottom edge is undisturbed pale stony ground and a dry grey thistle, with "
            "nobody and nothing between the camera and the patch. There is no person "
            "anywhere in the picture."
        ),
    },
    {
        "id": "v2-r028-b13", "out": "s13-when-a-man-hath-found-he-hideth.jpeg",
        "seg": "j1", "window": "35.000-39.510", "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": "the which when a man hath found, he hideth,",
        "must_show": "a closer photograph of Jesus on the olive roots, his near hand turning over palm-down in the air as he describes the hiding, with a seated disciple's dark back close in the near frame.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no midday overhead glare, no overcast; no field, no dry-stone field wall, no chalk bank, no dead stump, no mattock, no clay jar, no coins, no mud-brick hut and no dooryard anywhere in this frame; no wide view of the whole circle of disciples; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, warm low "
            "late-afternoon sun coming in almost level beneath the olive canopy from "
            "the left and broken into moving dapple across his face and shoulders, "
            "fine film grain. THE CAMERA SHOOTS PAST THE SHOULDER OF A SEATED "
            "DISCIPLE, whose ENTIRE back, shoulder, sleeve and head cloth are DEEP "
            "INDIGO — a single dark navy mass filling the near right of the frame out "
            "of focus, with NOTHING pale, grey, beige, taupe, ivory, cream or "
            "off-white anywhere on him — SO THAT JESUS'S GAZE HAS A NAMED TARGET "
            "INSIDE THE PICTURE: he is looking directly at that seated man, his "
            "eyeline running horizontally across the frame to the right and never "
            "toward the lens. Sharp in the middle, Jesus is framed from the waist up, "
            "seated on the knuckled exposed roots with his back half against the "
            "silver-grey fissured olive trunk and his body turned three-quarters "
            "toward that disciple, his near hand lifted and TURNING OVER PALM-DOWN in "
            "the air in the gesture of covering something, his lips parted mid-word, "
            "his expression quiet and warm. The grove's trunks, the silver-green "
            "canopy and the long dry-laid limestone wall fall away behind him into "
            "soft dappled blur."
        ),
    },
    {
        "id": "v2-r028-b14", "out": "s14-for-joy-thereof-goeth-and-selleth.jpeg",
        "seg": "j1b", "window": "39.510-43.250", "wide": True,
        "locks": ["MAN", "FIELD", "HAND-IRRIGATION"],
        "narration": "and for joy thereof goeth and selleth all that he hath,",
        "must_show": "the labourer striding fast away from the field up the valley track toward the village, seen from directly behind, his whole body loose and driving with joy, the walled field and its ridge house left small behind him in low warm late-afternoon light.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no midday overhead glare; no second person anywhere in the frame; no face turned toward the lens; no clay jar, no coins, no gold and no mattock in his hands; no dooryard, no mud-brick hut and no goods laid out; no cream, off-white, ivory, beige or pale garment on him.",
        "scene": (
            "One photograph, 35mm lens, deep depth of field, LOW WARM LATE-AFTERNOON "
            "SUN coming in almost level from the left so his shadow runs long and "
            "raking across the ground beside him and the warm level light lies along "
            "the valley side, fine "
            "film grain. THE CAMERA STANDS DOWN ON THE VALLEY FLOOR BEHIND HIM AND "
            "SHOOTS STRAIGHT UP THE TRACK PAST HIM: his BACK fills the near middle of "
            "the frame and he is walking directly AWAY from the camera toward the "
            "village, so not one part of his face is turned toward the lens and his "
            "eyeline is entirely out of view up the slope ahead of him. He is framed "
            "full length from behind, striding hard and fast with his arms swinging "
            "loose and one heel kicked up mid-stride — a lean hard-shouldered working "
            "man of about thirty in a DARK UMBER-BROWN coarse wool tunic to mid-calf "
            "with a DARK RUSSET-RED patch at one shoulder, a twisted dark brown cord "
            "at the waist and a DARK RUSSET-RED head cloth over close-cut black hair. "
            "His hands are empty. The near foreground along the bottom edge is the "
            "hard pale-tan dirt of the track and loose flat stones with nobody between "
            "the camera and him. Behind and below him at the left the small enclosed "
            "field lies inside its four dry-stone walls with the grey terebinth stump "
            "and the white chalk bank, and the low ridge with the owner's small "
            "flat-roofed mud-brick house stands beyond, all of it warm and gold in the "
            "level light under a deepening sky. He is the only person in the picture."
        ),
    },
    {
        "id": "v2-r028-b15", "out": "s15-and-buyeth-that-field.jpeg",
        "seg": "j1b", "window": "43.250-46.410",
        "locks": ["MAN", "OWNER", "FIELD", "HAND-IRRIGATION"],
        "narration": "and buyeth that field.",
        "must_show": "THE OWNER'S OWN FACE, large and clearly lit, across the dry-stone field wall as the two men strike the bargain — the settled iron-grey landholder weighing the lean dark labourer, their right hands closing together over the top of the wall.",
        "must_not_show": "no Jesus in this frame; no olive grove, no olive tree, no trunk, no canopy and no green foliage anywhere including the blurred background; no dappled light; no midday overhead glare; no third person anywhere in the frame; no coins, no purse, no clay jar, no gold and no treasure of any kind visible in this frame; no wide view of the whole valley and no view down from the ridge; no third hand, no extra arm and no hand without an arm attached to it anywhere in the frame; no bare uncovered head on the owner and no visible loose hair; no collar, placket, button, henley neck or waffle texture on any garment; no knitted, ribbed, fleece or sweater fabric on either man; no cream, off-white, ivory, beige or pale garment on either man; neither man's pupils centred on the lens and neither man facing the camera.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, LOW WARM "
            "LATE-AFTERNOON SUN coming in almost level from the left and lighting the "
            "owner's face fully and evenly from the side with clean warm bounce off "
            "the pale limestone wall filling the shadow side, fine film grain. THE "
            "CAMERA STANDS INSIDE THE FIELD COMPLETELY SIDE-ON TO BOTH MEN, OUT TO ONE "
            "SIDE OF THE LINE BETWEEN THEM AND AT RIGHT ANGLES TO IT, LOOKING ACROSS "
            "THE WALL. THE OWNER'S WHOLE HEAD IS TURNED AWAY FROM THE CAMERA AXIS AND "
            "HIS FACE IS SEEN IN CLEAN THREE-QUARTER PROFILE, THE LINE OF HIS NOSE "
            "POINTING TOWARD THE RIGHT EDGE OF THE FRAME, SO THE CAMERA SEES HIS "
            "CHEEK, HIS BEARD IN PROFILE AND THE OUTER CORNER OF HIS FAR EYE RATHER "
            "THAN THE FRONT OF HIS FACE. HIS GAZE HAS A NAMED TARGET INSIDE THE "
            "PICTURE: the labourer's face at the near right edge of the frame, so his "
            "eyeline runs horizontally across the picture to the right and exits "
            "through the RIGHT EDGE, at right angles to the camera. NEITHER MAN'S "
            "PUPILS ARE CENTRED ON THE LENS AND NEITHER OF THEM FACES THE CAMERA. "
            "Sharp and filling the frame from the chest up is the owner — "
            "a settled landholder of about fifty-five, heavier and softer built, "
            "lighter olive skin not worked brown, a broad fleshy face with deep lines "
            "from nose to mouth corners, a full IRON-GREY beard cut square, iron-grey "
            "hair under a DEEP INDIGO head cloth bound with a dark cord, shrewd narrow "
            "brown eyes weighing what he has just been offered, one eyebrow up. He "
            "WEARS THE DEEP INDIGO WOVEN HEAD CLOTH BOUND OVER HIS HAIR WITH A DARK "
            "CORD — his head is COVERED and no bare scalp or loose grey hair shows "
            "anywhere — with a DEEP INDIGO tunic whose neck is ONE PLAIN SLIT CUT "
            "STRAIGHT IN THE WOVEN CLOTH, with no collar, no placket, no button, no "
            "hook and no fastening of any kind, its sleeves straight and unshaped to "
            "the wrist, and a heavy "
            "DARK MADDER-RED mantle over his left shoulder, BOTH OF THEM COARSE "
            "HAND-WOVEN WOOL showing a clear over-and-under grid of warp and weft "
            "threads with a flat matte surface — no knit stitch, no rib, no cable, no "
            "jersey, no fleece and no sweater texture anywhere on him, at the cuff, "
            "the neck or any blurred edge. Behind him this valley is BARE AND "
            "TREELESS, with no olive tree, no trunk and no green canopy anywhere. "
            "Along the bottom of "
            "the frame the rough unmortared limestone top of the dry-stone field wall "
            "runs across, and on it their two RIGHT HANDS are closing together in a "
            "clasp. EXACTLY TWO HANDS ARE VISIBLE ANYWHERE IN THIS PICTURE AND THERE IS "
            "NO THIRD HAND, NO SPARE ARM AND NO WRIST WITHOUT AN ARM ATTACHED TO IT: "
            "the owner's ONE clean uncallused right hand, reaching in from the left "
            "with his indigo sleeve and his whole arm visibly joined to his shoulder, "
            "and the labourer's ONE hard sun-darkened right hand coming in from the "
            "near right with a pale old scar across the back of it and a DARK "
            "UMBER-BROWN sleeve, its arm likewise running unbroken out of the right "
            "edge of the frame. Nothing else rests on, leans on or lies along the top "
            "of the wall. Of the labourer only that one hand, "
            "his dark shoulder and the out-of-focus edge of his DARK RUSSET-RED head "
            "cloth are in the frame at the near right. Behind the owner the stony "
            "field, the grey split terebinth stump and the warm-lit valley side fall "
            "out of focus."
        ),
    },
    # ==================== the retelling — selling everything ===================
    {
        "id": "v2-r028-b16", "out": "s16-he-sold-everything-he-owned.jpeg",
        "seg": "n5", "window": "46.410-50.970", "wide": True,
        "locks": ["MAN", "NEIGHBOURS", "YARD"],
        "narration": "Did you catch what he did? He went home and sold everything he owned.",
        "must_show": "everything the labourer owns carried out of his one-room hut and laid out on the bare dirt of his dooryard in low warm late-afternoon light, with village neighbours standing over the goods picking them up, and the man himself handing a clay jar across.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no field, no dry-stone field wall, no chalk bank, no dead stump and no ridge house; no midday overhead glare and no morning light; no clay jar of treasure, no silver coins spilled and no gold ornaments; no cream, off-white, ivory, beige or pale garment on anybody; not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, LOW WARM LATE-AFTERNOON SUN coming in almost "
            "level from the right, long raking shadows stretching across the swept "
            "dirt, fine film grain. THE CAMERA STANDS OUT ON THE DIRT SLOPE BELOW THE "
            "YARD AND WELL TO ONE SIDE, SHOOTING UP AND ACROSS THE WHOLE SCENE AT "
            "RIGHT ANGLES TO EVERY EYELINE, so every person is seen in profile or "
            "three-quarter from behind and NOT ONE FACE IS SQUARED UP TO THE LENS. Two "
            "standing backs fill the near bottom corners, soft and out of focus, a "
            "DEEP INDIGO shouldered back at the near left and a DARK UMBER back with a "
            "dark brown head cloth at the near right, with nothing pale, grey, beige, "
            "taupe, ivory or off-white on either of them. Sharp in the middle "
            "distance, laid out in rows directly on the hard swept dirt in front of "
            "the low plank doorway of the rough tan mud-brick hut, is everything one "
            "poor man owns: two rolled sleeping mats of woven reed, a folded dark "
            "brown wool blanket, three fired-clay jars and a shallow clay bowl, a "
            "hand-woven reed basket, a coil of twisted flax rope, a wooden yoke, and a "
            "goat standing tethered to a stake at the edge of the thorn-brush pen. "
            "Standing over the goods, four villagers in DEEP INDIGO, DARK UMBER, "
            "RUSSET-RED and dark olive-drab wool with dark head cloths bend and lift "
            "and turn things over, all of them in profile. At the right of the group, "
            "seen from his left side, the labourer holds out a clay jar into a "
            "neighbour's hands — a lean working man of about thirty in the DARK "
            "UMBER-BROWN tunic with the DARK RUSSET-RED shoulder patch and DARK "
            "RUSSET-RED head cloth, his gaze on the neighbour's hands at the centre of "
            "the frame. The hut's flat earth roof, its one small unglazed window "
            "opening, the big clay water jar on its flat stone and the thorn-brush pen "
            "stand behind, and the village's flat mud roofs fall away beyond under low "
            "tawny hills."
        ),
    },
    {
        "id": "v2-r028-b17", "out": "s17-his-house-his-tools.jpeg",
        "seg": "n6", "window": "50.970-53.170",
        "locks": ["YARD", "HAND-TOOLS"],
        "narration": "His house. His tools. All of it —",
        "must_show": "a close photograph of the emptied plank doorway of the mud-brick hut with its worn stone threshold, and on the swept dirt in front of it the man's few hand tools laid out separately and countable — the mattock, a hand-forged sickle, an adze and a wooden mallet.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no field, no dry-stone field wall, no chalk bank and no ridge house; no person, no hand, no arm and no face anywhere in this frame; no midday overhead glare and no morning light; no steel spade or shovel, no D-handle, no foot tread, no chromed, painted or stainless metal, no tubular metal shaft, no rivets or stamped fittings; no coins, no gold and no treasure.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, LOW WARM "
            "LATE-AFTERNOON SUN coming in almost level from the right and raking hard "
            "across the swept dirt so every tool throws a long shadow of its own, fine "
            "film grain. THE CAMERA IS SET LOW IN THE DOORYARD ON THE HARD SWEPT DIRT "
            "A FEW PACES OUT FROM THE HUT, LOOKING ACROSS THE GROUND AND SLIGHTLY UP, "
            "SO THE UPPER THIRD OF THE FRAME CARRIES THE HUT ITSELF: the rough tan "
            "mud-brick wall with its mud plaster fallen away at the corner, the low "
            "doorway of three hewn planks standing open and empty on its worn stone "
            "threshold with nothing but darkness inside, and the big fired-clay water "
            "jar on its flat stone against the wall, all softly out of focus. Sharp "
            "across the near middle of the frame, laid out separately on the bare dirt "
            "with clear space between each one so all FOUR can be counted "
            "individually, are the man's hand tools: the MATTOCK with its straight "
            "rough-hewn unpainted wooden haft and its single heavy dark grey pitted "
            "hammer-marked iron blade wedged onto the head at an angle, a hand-forged "
            "iron sickle with a curved dark blade and a plain wooden grip, a small "
            "adze, and a wooden mallet worn round at the striking face. Every iron "
            "surface is dark, uneven and pitted with a bright worn working edge. There "
            "is no person anywhere in the picture and the near foreground along the "
            "bottom edge is swept dirt with two loose stones on it."
        ),
    },
    {
        "id": "v2-r028-b18", "out": "s18-all-of-it-gladly.jpeg",
        "seg": "n6", "window": "53.170-55.990",
        "locks": ["MAN", "NEIGHBOURS", "YARD", "HAND-TOOLS"],
        "narration": "gladly, without a second thought.",
        "must_show": "THE LABOURER'S FACE, unmistakably GLAD, as he hands his own mattock across into a neighbour's hands — no hesitation, no grief, the corners of his mouth clearly up.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no field, no dry-stone field wall, no chalk bank and no ridge house; no midday overhead glare and no morning light; no wide view of the goods laid out in rows on the ground; no sorrow, no reluctance, no backward look and no tears; no steel spade or shovel, no D-handle, no foot tread; no cream, off-white, ivory, beige or pale garment on anybody; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, LOW WARM "
            "LATE-AFTERNOON SUN coming in almost level from the right and lighting the "
            "side of his face fully and warmly with clean bounce off the tan mud-brick "
            "wall filling the shadow side, fine film grain. THE CAMERA STANDS IN THE "
            "DOORYARD WELL TO HIS RIGHT, SHOOTING HIM IN THREE-QUARTER VIEW ACROSS THE "
            "FRAME. HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: the neighbour's "
            "hands taking the mattock haft at the near left of the frame, so his head "
            "is turned down and to his own left and his eyeline runs across and out "
            "through the LEFT EDGE, well clear of the lens. Sharp and framed from the "
            "chest up is the labourer — a lean hard-shouldered working man of about "
            "thirty with deeply sun-darkened olive-brown skin, a narrow weathered "
            "face, a short-cropped black beard, close-cut black hair under a DARK "
            "RUSSET-RED head cloth, quick dark brown eyes under heavy black brows, "
            "wearing the DARK UMBER-BROWN coarse wool tunic with sleeves above the "
            "elbow and the DARK RUSSET-RED patch at one shoulder. HIS EXPRESSION IS "
            "OPEN AND GLAD — the corners of his mouth clearly up, his brows raised and "
            "relaxed, his whole face light — as both his hands push the straight "
            "rough-hewn wooden haft of the mattock, its dark pitted iron blade "
            "hanging, across into a pair of hands coming in from the near left. Of the "
            "neighbour only those hands and a DEEP INDIGO out-of-focus shoulder are in "
            "the frame. The rough tan mud-brick hut wall and the thorn-brush pen fall "
            "out of focus behind him."
        ),
    },
    {
        "id": "v2-r028-b19", "out": "s19-with-every-coin-he-had.jpeg",
        "seg": "n7", "window": "55.990-60.640",
        "locks": ["MAN", "OWNER", "FIELD", "HAND-IRRIGATION"],
        "narration": "And with every coin he had, he bought that one field for himself.",
        "must_show": "a close photograph over the dry-stone field wall of the labourer tipping a coarse dark cloth purse upside down and emptying every last coin out of it into the owner's two cupped hands, the purse held so it is visibly and completely empty.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no midday overhead glare and no late-afternoon golden light; no third person anywhere in the frame; no buried clay jar, no spilled hoard and no gold ornaments from the treasure; no chest, casket, hinge, lock or metal box; no milled or reeded coin edge, no lettering, numerals or date on any coin; no cream, off-white, ivory, beige or pale garment on either man; neither man's pupils centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, CLEAN EARLY-MORNING "
            "SUN low from the left, cool and clear with long soft shadows and no heat "
            "haze, fine film grain. THE CAMERA STANDS BESIDE THE TWO MEN AT THE "
            "DRY-STONE FIELD WALL AND WELL TO ONE SIDE, LOOKING ACROSS THE WALL "
            "BETWEEN THEM AT CHEST HEIGHT, AND IT IS FRAMED WIDE ENOUGH THAT THE UPPER "
            "THIRD CARRIES THE FIELD BEHIND THEM: pale-tan stony ground, the grey "
            "split barkless terebinth stump and the low ridge with the small "
            "flat-roofed mud-brick house on it, softly out of focus. BOTH MEN'S GAZES "
            "HAVE THE SAME NAMED TARGET INSIDE THE PICTURE: the falling coins at the "
            "centre of the frame, so both heads are bowed and both eyelines run "
            "steeply down into the middle of the picture and out through the BOTTOM "
            "EDGE, nowhere near the lens. Sharp in the centre, a pair of hard "
            "sun-darkened working hands with a pale old scar across the back of the "
            "right one, DARK UMBER-BROWN sleeves pushed above the elbow, hold a coarse "
            "DARK BROWN cloth purse UPSIDE DOWN and squeeze its flattened empty sides, "
            "the last irregular hand-struck silver coins falling in a thin stream out "
            "of it — small uneven lumps of dull tarnished grey-white metal with crude "
            "off-centre devices, no two alike — down into the owner's two cupped hands "
            "held together beneath, already heaped with them. The purse is visibly "
            "slack and empty. Above the hands, out of focus at the top of the frame, "
            "are the labourer's dark shoulder and DARK RUSSET-RED head cloth at the "
            "right and the owner's DEEP INDIGO shoulder, DARK MADDER-RED mantle and "
            "iron-grey square-cut beard at the left, both heads bent over the "
            "transaction. The rough unmortared limestone top of the field wall runs "
            "across the bottom of the frame."
        ),
    },
    {
        "id": "v2-r028-b20", "out": "s20-he-knew-what-was-waiting.jpeg",
        "seg": "n8", "window": "60.640-63.120",
        "locks": ["MAN", "FIELD", "HAND-IRRIGATION"],
        "narration": "Because he knew what was waiting under the soil.",
        "must_show": "the labourer alone in the field in clean early-morning light, down on one knee with one open palm resting flat on the tamped patch of ground where the hoard lies, looking down at it, calm and certain.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no midday overhead glare and no late-afternoon golden light; no second person anywhere in the frame; no owner; no purse, no coins, no gold and no open hole — nothing of the hoard is visible; no wide view of the whole field from outside its wall; no steel spade or shovel; no cream, off-white, ivory, beige or pale garment on him; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, CLEAN EARLY-MORNING "
            "SUN low from the left laying a long soft shadow of him across the pale "
            "stony ground, cool clear air, fine film grain. THE CAMERA IS SET LOW ON "
            "THE FIELD FLOOR WELL TO HIS RIGHT, LOOKING ACROSS HIM IN THREE-QUARTER "
            "PROFILE AND SLIGHTLY UP. HIS GAZE HAS A NAMED TARGET INSIDE THE PICTURE: "
            "his own open palm flat on the tamped patch of ground at the lower left of "
            "the frame, so his head is bowed and turned down and to his own left and "
            "his eyeline leaves the picture through the BOTTOM LEFT CORNER, far from "
            "the lens. He is framed from the thighs up, down on one knee with his "
            "weight easy, one forearm across his raised knee and the other hand laid "
            "flat and open on the smooth dark-brown patch of pressed soil with the "
            "single flat grey limestone marker beside it — a lean hard-shouldered "
            "working man of about thirty with deeply sun-darkened olive-brown skin, a "
            "narrow weathered face, a short-cropped black beard, close-cut black hair "
            "under a DARK RUSSET-RED head cloth, in the DARK UMBER-BROWN coarse wool "
            "tunic with the DARK RUSSET-RED patch at one shoulder. His expression is "
            "settled and certain, the faintest smile at the corner of his mouth. The "
            "near foreground along the bottom edge is pale-tan stony field floor with "
            "loose flat stones, and there is nobody between the camera and him. Behind "
            "him the empty field, the grey unmortared dry-stone wall and the white "
            "chalk bank fall out of focus under a clear early sky. He is the only "
            "person in the picture."
        ),
    },
    {
        "id": "v2-r028-b21", "out": "s21-that-field-was-worth-more.jpeg",
        "seg": "n8", "window": "63.120-65.360", "wide": True,
        "locks": ["MAN", "FIELD", "HAND-IRRIGATION"],
        "narration": "That field was worth more",
        "must_show": "a wide photograph of the whole enclosed field in clean early-morning light with the labourer standing small and alone in the middle of it, seen squarely from behind, the four dry-stone walls closing the whole parcel around him — it is all his now.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no midday overhead glare and no late-afternoon golden light; no second person anywhere in the field; no owner; no face turned toward the lens; no coins, no gold, no clay jar and no open hole; no dooryard, no mud-brick hut and no goods laid out; no steel spade or shovel; no cream, off-white, ivory, beige or pale garment on him.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, CLEAN EARLY-MORNING SUN "
            "low from the left throwing one long shadow of him right across the stony "
            "ground, cool clear air with no heat haze, fine film grain. THE CAMERA "
            "STANDS OUTSIDE THE FIELD AT THE TUMBLED GAP IN THE NEAR WALL, at chest "
            "height, LOOKING STRAIGHT ACROSS THE WHOLE ENCLOSURE, so the man is seen "
            "SQUARELY FROM BEHIND and not one part of his face is turned toward the "
            "lens; his own gaze is out across the field away from the camera. The near "
            "foreground across the bottom of the frame is the rough grey unmortared "
            "limestone top of the near wall itself, sharp and close, with a dry grey "
            "thistle at its foot and nobody between the camera and the field. Standing "
            "small and alone out in the middle of the pale-tan stony ground, his back "
            "to the camera and his arms hanging loose and open at his sides, is the "
            "labourer — a lean working man in a DARK UMBER-BROWN coarse wool tunic "
            "with a DARK RUSSET-RED patch at one shoulder and a DARK RUSSET-RED head "
            "cloth over close-cut black hair, his dark shape the only figure in the "
            "enclosure. All four dry-stone walls close the parcel around him inside "
            "the frame; the dry grey thistles stand in the corners, the grey split "
            "barkless terebinth stump stands near the far wall, the white chalk bank "
            "is cut into the valley side at the left, and the low ridge with the small "
            "flat-roofed mud-brick house rises beyond under a clear pale morning sky."
        ),
    },
    {
        "id": "v2-r028-b22", "out": "s22-than-everything-else-he-owned.jpeg",
        "seg": "n8", "window": "65.360-67.750",
        "locks": ["YARD"],
        "narration": "than everything else he owned, put together.",
        "must_show": "the emptied dooryard in clean early-morning light — the plank doorway standing open on nothing, the swept dirt completely bare where the goods were laid out, the thorn-brush pen empty, and pale rectangles in the dust where the mats and jars stood.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no field, no dry-stone field wall, no chalk bank, no dead stump and no ridge house; no person, no hand, no arm and no face anywhere in this frame; no midday overhead glare and no late-afternoon golden light; no goods, no tools, no jars, no mats, no basket, no rope and no goat; no coins, no gold and no treasure.",
        "scene": (
            "One photograph, 35mm lens, CLEAN EARLY-MORNING SUN low from the right "
            "laying long soft shadows across the swept dirt, cool clear air, fine film "
            "grain. THE CAMERA STANDS OUT ON THE DIRT SLOPE BELOW THE YARD AT CHEST "
            "HEIGHT, LOOKING UP AND ACROSS THE WHOLE EMPTY DOORYARD toward the hut. "
            "The near foreground across the bottom of the frame is bare hard swept "
            "dirt with two loose stones and a scatter of dry straw on it, and there is "
            "nobody and nothing between the camera and the hut. The rough tan "
            "mud-brick hut stands with its mud plaster fallen away at the corners, its "
            "flat roof of poles and packed earth with the rough wooden roller lying on "
            "it, its one small unglazed window opening dark, and its low doorway of "
            "three hewn planks standing OPEN on nothing but darkness above the worn "
            "stone threshold. The swept dirt in front of it is completely bare — only "
            "the faint pale rectangles in the dust where mats and jars stood, and one "
            "shallow round depression where the big water jar sat on its flat stone, "
            "the stone itself now empty. The thorn-brush pen at the side is empty with "
            "its stake standing alone and its tether gone. Beyond the yard the dirt "
            "slope falls away to the other flat mud roofs of the village and low tawny "
            "bare hills close the horizon under a clear pale morning sky. There is no "
            "person anywhere in the picture."
        ),
    },
    # ================ the turn — back to the grove, then the meaning ===========
    {
        "id": "v2-r028-b23", "out": "s23-that-is-what-gods-kingdom-is-like.jpeg",
        "seg": "n9", "window": "67.750-71.370", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES"],
        "narration": "That, Jesus said, is what God's kingdom is like.",
        "must_show": "Jesus in the olive grove having just finished, his hands come to rest open on his knees, the disciples around him quiet and still working it out, in warm low late-afternoon dapple.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no midday overhead glare, no overcast; no field, no dry-stone field wall, no chalk bank, no dead stump, no mattock, no clay jar, no coins, no mud-brick hut and no dooryard anywhere in this frame; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming in almost "
            "level beneath the olive canopy from the left and broken into moving "
            "dapple, fine film grain. THE CAMERA IS PLACED COMPLETELY SIDE-ON TO THE "
            "CIRCLE, LOW DOWN AMONG THE ROOTS AND WELL TO ONE SIDE, SHOOTING ACROSS "
            "THE GROUP AT RIGHT ANGLES TO EVERY EYELINE, so the whole picture reads "
            "HORIZONTALLY ACROSS THE FRAME. Jesus sits at the left of the frame on the "
            "knuckled exposed roots, seen from his right side in three-quarter, and "
            "the disciples are ranged on the ground to the right of him. HIS GAZE HAS "
            "A NAMED TARGET INSIDE THE PICTURE: a disciple seated low at the right of "
            "the frame, so his eyeline travels rightward and exits through the RIGHT "
            "EDGE; the disciples' own gazes are down at the ground in front of them or "
            "across at one another, and NOT ONE PAIR OF PUPILS IS CENTRED ON THE LENS. "
            "One seated back fills the near bottom right corner, soft and out of "
            "focus, DARK OLIVE-DRAB shoulder and dark brown head cloth, with nothing "
            "pale, grey, beige, taupe, ivory or off-white on him. Sharp in the middle "
            "distance Jesus has come to rest — his back half against the silver-grey "
            "fissured trunk, both hands open and still on his knees, his mouth closed, "
            "his expression warm and unhurried, letting it land. Around him the "
            "disciples sit low in dark indigo, umber, olive-drab and russet wool, one "
            "with his chin on his fist, one looking down at a stone he is turning "
            "over, all of them quiet. The ancient trunks recede behind them and the "
            "dry-laid limestone wall runs along the upper edge under the silver-green "
            "canopy."
        ),
    },
    {
        "id": "v2-r028-b24", "out": "s24-it-can-look-like-an-ordinary-field.jpeg",
        "seg": "n10", "window": "71.370-74.270", "wide": True,
        "locks": ["FIELD", "HAND-IRRIGATION"],
        "narration": "At first it can look like an ordinary field.",
        "must_show": "a wide photograph of the same enclosed field under flat bright overcast daylight with no shadow at all — the most ordinary, unremarkable, worthless-looking piece of ground imaginable, empty of people.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no person anywhere in the frame; no direct sunlight, no shadows, no golden light, no morning or evening colouring; no clay jar, no coins, no gold and no open hole; no dooryard and no mud-brick hut; nothing lying on the ground in a straight dark line.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, FLAT BRIGHT OVERCAST "
            "DAYLIGHT under a high even white sky so there is NO shadow anywhere in "
            "the picture and every colour is muted and grey-tan, fine film grain. THE "
            "CAMERA STANDS OUTSIDE THE FIELD ON THE VALLEY FLOOR AT THE TUMBLED GAP IN "
            "THE NEAR WALL, at chest height, LOOKING STRAIGHT ACROSS THE WHOLE "
            "ENCLOSURE toward the far wall and the ridge. The near foreground across "
            "the bottom of the frame is the rough grey unmortared limestone top of the "
            "near wall, sharp and close, with a dry grey thistle at its foot and "
            "nobody between the camera and the field. Beyond it the hard pale-tan "
            "stony ground runs away from the camera, flat and dull and littered with loose stones, dry "
            "grey thistles in the corners, the broad tamped patch in the middle now "
            "weathered down until it barely reads as different from the rest. The "
            "white chalk bank is cut into the valley side at the left, its glare gone "
            "in the flat light. The grey split barkless terebinth stump stands near "
            "the far wall. Beyond the far wall the ridge rises with the small "
            "flat-roofed mud-brick house on it under a blank white sky. Nothing in the "
            "picture is beautiful or interesting and nothing in it suggests that "
            "anything is buried there."
        ),
    },
    {
        "id": "v2-r028-b25", "out": "s25-once-you-catch-sight-of-the-treasure.jpeg",
        "seg": "n10", "window": "74.270-76.750",
        "locks": ["FIELD", "TREASURE", "HAND-IRRIGATION"],
        "narration": "But once you catch sight of the treasure in it,",
        "must_show": "a close photograph low in the same field where a narrow break in the soil has opened and ONE dull tarnished silver coin and the curve of the buried buff-grey clay jar show through the dirt — the one thing in the whole ordinary field that changes what it is worth.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no person, no hand, no arm and no face anywhere in this frame; no direct sunlight and no shadows, no golden light; no glitter, no sparkle, no shining metal, no light coming off the coin, no glow; no wide view of the whole field and no distant ridge house; no chest, casket, hinge, lock or gemstone; no milled or reeded coin edge, no lettering or numerals.",
        "scene": (
            "One photograph, 85mm macro lens, very shallow depth of field, FLAT BRIGHT "
            "OVERCAST DAYLIGHT with no shadow anywhere, fine film grain. THE CAMERA IS "
            "SET DOWN ON THE FLOOR OF THE FIELD AT SOIL LEVEL, A HAND'S BREADTH ABOVE "
            "THE DIRT, LOOKING ALONG THE GROUND, AND IT IS TILTED UP JUST ENOUGH THAT "
            "A CLEAR BAND OF THE FIELD RUNS ACROSS THE UPPER QUARTER OF THE FRAME: "
            "pale-tan stony ground running away, dry grey thistle stalks and the grey "
            "unmortared limestone of the dry-stone wall under a blank white sky, "
            "thrown far out of focus, so the picture is unmistakably outdoors on this "
            "ground. Sharp and filling the lower two thirds is a narrow break in the "
            "hard dry soil, its edges crumbled, and in the shadowless light down "
            "inside it: the smooth round buff-grey gritty curve of the buried "
            "fired-clay jar with earth packed against it, and resting in the dirt at "
            "the lip of the break ONE irregular hand-struck silver coin — a small "
            "uneven lump of DULL TARNISHED grey-white metal with a crude off-centre "
            "device beaten into its face and a plain rough rim, matte, with dry earth "
            "still in its hollows. It does not shine, sparkle or give off any light. "
            "There is no person anywhere in the picture."
        ),
    },
    {
        "id": "v2-r028-b26", "out": "s26-once-you-truly-see-who-jesus-is.jpeg",
        "seg": "n10", "window": "76.750-82.020", "jesus": True, "ref": REF,
        "locks": ["GROVE", "DISCIPLES", "PETER"],
        "narration": "once you truly see who Jesus is — nothing else even compares.",
        "must_show": "a close photograph of Jesus's own face in the olive grove, warm and fully lit in the dappled late-afternoon light, looking at Peter seated low beside him — the picture the narration is pointing at when it says once you truly see who he is.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus, and nothing bright behind his head; no night, no lamp, no midday overhead glare, no overcast; no field, no dry-stone field wall, no chalk bank, no dead stump, no mattock, no clay jar, no coins, no mud-brick hut and no dooryard anywhere in this frame; no wide view of the whole circle of disciples; no cream or off-white cloth on anybody but Jesus anywhere in the frame including the blurred edges; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 105mm portrait lens, very shallow depth of field, warm "
            "low late-afternoon sun coming in almost level beneath the olive canopy "
            "from the left and broken into soft moving dapple across his face and "
            "shoulders, with clean warm bounce off the pale dry ground filling the "
            "shadow side so his face is fully readable, fine film grain. THE CAMERA "
            "STANDS AMONG THE TRUNKS WELL TO JESUS'S LEFT AND SLIGHTLY LOW, SHOOTING "
            "HIM IN THREE-QUARTER VIEW ACROSS THE FRAME. HIS GAZE HAS A NAMED TARGET "
            "INSIDE THE PICTURE: Peter, seated low at the near right of the frame with "
            "his broad DARK UMBER back and dark brown head cloth turned to the camera "
            "and thrown out of focus, so Jesus's eyeline runs horizontally across the "
            "picture to the right and exits through the RIGHT EDGE, well clear of the "
            "lens. Sharp and filling the frame from the shoulders up is Jesus, seated "
            "on the knuckled exposed olive roots with the silver-grey fissured trunk "
            "close behind him, his head turned toward Peter, his expression quiet, "
            "warm and completely unguarded, the beginning of a smile at his mouth. The "
            "background is nothing but the dark grooved trunk and dappled silver-green "
            "leaves gone entirely soft, with no bright patch of sky or light behind "
            "his head. There is nothing pale, grey, beige, taupe, ivory or off-white "
            "anywhere in the frame except the wool of his own robe."
        ),
    },
    {
        "id": "v2-r028-b27", "out": "s27-you-dont-give-everything-up-sadly.jpeg",
        "seg": "n11", "window": "82.020-84.540",
        "locks": ["MAN", "NEIGHBOURS", "YARD"],
        "narration": "And you don't give everything up sadly.",
        "must_show": "the labourer in his emptying dooryard handing the last of his goods away with a completely level, un-grieved face — he does not look back at the hut and there is no sorrow anywhere in him.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no field, no dry-stone field wall, no chalk bank and no ridge house; no midday overhead glare and no morning light; no sorrow, no grief, no tears, no hesitation, no clinging and no backward look at the hut; no wide view of the goods laid out in rows; no coins, no gold and no treasure; no cream, off-white, ivory, beige or pale garment on anybody; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm lens, shallow depth of field, LOW WARM "
            "LATE-AFTERNOON SUN coming in almost level from the right, warm bounce off "
            "the tan mud-brick wall filling the shadow side of his face, fine film "
            "grain. THE CAMERA STANDS IN THE DOORYARD WELL TO HIS LEFT, SHOOTING HIM "
            "IN THREE-QUARTER VIEW ACROSS THE FRAME. HIS GAZE HAS A NAMED TARGET "
            "INSIDE THE PICTURE: the folded DARK BROWN wool blanket passing out of his "
            "own hands into a woman's hands at the near right of the frame, so his "
            "head is turned down and to his own right and his eyeline runs across and "
            "out through the RIGHT EDGE, well clear of the lens. Sharp and framed from "
            "the chest up is the labourer — a lean hard-shouldered working man of "
            "about thirty with deeply sun-darkened olive-brown skin, a narrow "
            "weathered face, a short-cropped black beard, close-cut black hair under a "
            "DARK RUSSET-RED head cloth, quick dark brown eyes under heavy black "
            "brows, in the DARK UMBER-BROWN coarse wool tunic with sleeves above the "
            "elbow and the DARK RUSSET-RED patch at one shoulder. HIS FACE IS LEVEL "
            "AND EASY AND ENTIRELY WITHOUT GRIEF — his brow smooth, his jaw relaxed, "
            "no tightness anywhere in it — as he passes the folded dark brown blanket "
            "across. Of the woman only her two hands taking it and a RUSSET-RED "
            "out-of-focus shoulder with a dark madder-brown head cloth are in the "
            "frame at the near right, with nothing pale on her. Behind him the rough "
            "tan mud-brick hut wall and the empty plank doorway fall out of focus."
        ),
    },
    {
        "id": "v2-r028-b28", "out": "s28-you-do-it-out-of-pure-joy.jpeg",
        "seg": "n11", "window": "84.540-87.500",
        "locks": ["MAN", "FIELD", "HAND-IRRIGATION"],
        "narration": "You do it out of pure joy, because you've found",
        "must_show": "THE LABOURER'S FACE OPEN IN UNMISTAKABLE JOY, standing in his own field in bright full morning sun — head back, eyes creased, mouth open in a laugh, his whole face released.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no overcast flat light, no midday overhead glare and no late-afternoon golden light; no second person anywhere in the frame; no sorrow, no restraint and no solemnity; no coins, no gold, no clay jar and no open hole; no dooryard and no mud-brick hut; no steel spade or shovel; no cream, off-white, ivory, beige or pale garment on him; his pupils never centred on the lens.",
        "scene": (
            "One photograph, 85mm portrait lens, shallow depth of field, BRIGHT FULL "
            "MORNING SUN coming in from the left across his face, clean and warm, with "
            "bounce off the pale stony ground filling under his jaw, fine film grain. "
            "THE CAMERA IS SET LOW ON THE FIELD FLOOR WELL TO HIS RIGHT AND LOOKING UP "
            "AT HIM IN THREE-QUARTER VIEW. HIS GAZE HAS A NAMED TARGET INSIDE THE "
            "PICTURE: the open morning sky above the far dry-stone wall at the upper "
            "left of the frame, so his head is tipped back and turned up and to his "
            "own left and his eyeline leaves the picture through the TOP LEFT CORNER, "
            "far above and to the side of the lens. Sharp and filling the frame from "
            "the chest up is the labourer, standing in the middle of his own field — a "
            "lean hard-shouldered working man of about thirty with deeply sun-darkened "
            "olive-brown skin, a narrow weathered face, a short-cropped black beard, "
            "close-cut black hair under a DARK RUSSET-RED head cloth, in the DARK "
            "UMBER-BROWN coarse wool tunic with sleeves above the elbow and the DARK "
            "RUSSET-RED patch at one shoulder. HIS FACE IS OPEN IN A FULL UNGUARDED "
            "LAUGH — head back, eyes creased almost shut, teeth showing, the deep "
            "lines of his cheeks pulled up, both hands lifted loose and open at his "
            "sides — pure released joy with nothing held back and nothing solemn about "
            "it. The near foreground at the bottom edge is pale-tan stony field floor "
            "with loose flat stones, and there is nobody between the camera and him. "
            "The stony field, the grey unmortared dry-stone wall and the clear morning "
            "sky fall completely out of focus behind him. He is the only person in the "
            "picture."
        ),
    },
    {
        "id": "v2-r028-b29", "out": "s29-the-one-thing-worth-having.jpeg",
        "seg": "n11", "window": "87.500-90.360", "wide": True,
        "locks": ["MAN", "FIELD", "HAND-IRRIGATION"],
        "narration": "the one thing worth having everything else.",
        "must_show": "a wide closing photograph of the labourer standing out in the middle of his own field in bright full morning sun, seen squarely from behind and small, arms loose at his sides, the whole walled parcel and the valley open around him — everything gone, everything gained.",
        "must_not_show": "no Jesus in this frame; no olive grove and no dappled light; no overcast flat light, no midday overhead glare and no late-afternoon golden light; no second person anywhere in the field; no face turned toward the lens; no coins, no gold, no clay jar and no open hole; no dooryard, no mud-brick hut and no goods; no steel spade or shovel; no cream, off-white, ivory, beige or pale garment on him.",
        "scene": (
            "One photograph, 24mm lens, deep depth of field, BRIGHT FULL MORNING SUN "
            "from the left throwing his long shadow across the pale stony ground, "
            "clean warm clear air, fine film grain. THE CAMERA STANDS INSIDE THE FIELD "
            "WELL BEHIND HIM AND LOW, SHOOTING PAST HIM UP THE VALLEY, so he is seen "
            "SQUARELY FROM BEHIND and not one part of his face is turned toward the "
            "lens; his own gaze is out across the field away from the camera. The near "
            "foreground across the bottom of the frame is the hard pale-tan stony "
            "ground of the field with loose flat stones and one dry grey thistle, "
            "sharp and close, with nobody between the camera and him. Standing out in "
            "the middle of the enclosure with his back to the camera, his arms hanging "
            "loose and open away from his sides and his head up, is the labourer — a "
            "lean working man in a DARK UMBER-BROWN coarse wool tunic to mid-calf with "
            "a DARK RUSSET-RED patch at one shoulder and a DARK RUSSET-RED head cloth "
            "over close-cut black hair, small enough in the frame that the whole "
            "parcel fits around him. All four dry-stone walls close the field, the dry "
            "grey thistles stand in the corners, the grey split barkless terebinth "
            "stump stands near the far wall, the white chalk bank is cut into the "
            "valley side at the left, and the low ridge with the small flat-roofed "
            "mud-brick house rises beyond, the whole valley opening out under a clear "
            "bright morning sky. He is the only person in the picture."
        ),
    },
]
