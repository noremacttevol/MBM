#!/usr/bin/env python3
"""V2 beat map — row 30, build-30-net (Matthew 13:47-50), realistic.

COVERAGE: 40 pictures against V1's SIX PLACED stills, over 147.39 s of story =
3.68 s/picture (rows 24-29 shipped at 3.1-4.9). V1's holds were the worst in the
wave so far:
  * `s5-cast-bad.jpeg` covered n7, j2, j50 AND n8 — 79.991 s -> 115.780 s, THIRTY-FIVE
    AND THREE QUARTER SECONDS on ONE picture, i.e. the entire end-of-the-world turn
    (both red-letter verses AND the "the angels do it, God does it, it was never
    handed to us" line that the whole passage is aimed at).
  * `s6-shore-close.jpeg` covered n9, n10 AND n11 — 115.780 -> 147.672, THIRTY-ONE
    AND NINE-TENTHS SECONDS, which is the ENTIRE closing application, "it was cast
    for you", the reason the video exists.
  * `s1-cast.jpeg` covered n1, j1 AND n2 — 0.280 -> 23.701, TWENTY-THREE AND A HALF.
  * `s5b-cast-away.jpeg` sits in `assets/` and is never placed on the timeline at all.

⚠️ THE INHERITED beats_v2.py WAS DISCARDED (git history keeps it), for measured
reasons, not taste:
  * It planned 25 pictures at 5.7 s each and called that "the library density".
    It is not: rows 24-29 shipped at 3.1-4.9 s/picture.
  * IT STAGED THE FRAME IN A HOUSE INTERIOR ("Jesus at the deep window of the room"),
    arguing from Matthew 13:36. Row 16 already owns this wave's interior and rows 28
    and 29 each examined and rejected exactly this argument for exactly this reason.
    The frame beats recur NINE times here, so a second interior is the repeat, not
    the cure.
  * Its own clock note let the parable beats wander ("bright morning ... midday ...
    dusk ... back to wide bright morning") without pinning the frame's hour at all,
    and the frame is the one thing in the video that must never change.

AUDIO IS CLEAN AND LOCKED (checked from the FILES, not from prose):
  * `matthew-13_the-net.mp4` and EVERY one of the sixteen `audio/*.mp3` last changed
    bytes at the SAME commit, 2026-07-27T22:50:25 (git CONTENT dates — mtimes are
    worthless in this repo, four machines pull it). No placed mp3 is newer than the
    MP4, so `assert_v1_final_is_current()`'s recency tripwire has nothing to refuse,
    and the V1 stream runs 154.933 s against the summed timeline (154.885 s).
  * SOURCING TRAP CHECKED AND CLEARED. All SIXTEEN segments (n1-n11, j1, j48, j2,
    j50, card) were transcribed with faster-whisper `word_timestamps=True` and every
    one matches the LIVE `make_narration.py` word for word. THREE apparent differences
    were chased down and are whisper's, not the audio's, and all three are the same
    family — a dropped or flipped final consonant: "fishermen"->"fisherman" (n2),
    "the bad away"->"the bat away" (j48), "the angels"->"the angel" (j2). So NO
    `TEXT_OVERRIDES` are needed on this row and `AUDIO_FROM_V1_SEGMENTS` stays off.

⚠️ WINDOWS COMPUTED FROM SCRATCH 2026-08-02 with `extract_beats.py` reading the V1
build, then split inside each segment on WORD timings measured from that segment's
own mp3 with faster-whisper. THE `.timing.json` SIDECARS WERE NOT TRUSTED and could
not have been used anyway — every one of the sixteen holds exactly ONE phrase
spanning its whole segment, so no interior split exists in them. The `.mp3.words.json`
siblings were likewise ignored. Windows are SEGMENT-BOUNDARY CONTIGUOUS (`seg_start`
-> the NEXT segment's `seg_start`, never `audio_start` -> `spoken_end`), so there is
no dead gap at any of the fifteen segment joins: contiguous 0.280 s -> 147.672 s (the
card start), zero gaps, zero overlaps, shortest window 1.88 s, longest 4.88 s. Every
split lands on a clause head or a sentence boundary and none falls inside a word.

SCRIPTURE (Matthew 13:47-50 KJV):
  v47  "Again, the kingdom of heaven is like unto a net, that was cast into the sea,
        and gathered of every kind:"
  v48  "Which, when it was full, they drew to shore, and sat down, and gathered the
        good into vessels, but cast the bad away."
  v49  "So shall it be at the end of the world: the angels shall come forth, and
        sever the wicked from among the just,"
  v50  "And shall cast them into the furnace of fire: there shall be wailing and
        gnashing of teeth."
Four things have to be readable in the pictures or the parable does not land:
  1. THE GATHERING IS WIDE AND IT COMES FIRST. The net is a DRAGNET, not a cast net —
     a wall of mesh walked out and hauled, sweeping a whole stretch of water. The
     warmth of the row lives in n3/n4, and those beats must show a genuinely mixed,
     countable, ordinary catch, never a tidy selection.
  2. THE SORTING HAPPENS ASHORE, SEATED, AFTER EVERYONE IS ALREADY IN. v48 says it
     twice — "drew to shore" and "sat down" — and n5 says it in plain words. So the
     sorting beats are all LOW, SEATED, UNHURRIED, and the net is already emptied.
  3. THE ANGELS ARE NOT PAINTED, and neither is heaven or hell (the row-21 precedent).
     v49/v50 stay inside the parable's own fish-and-shore imagery. The furnace beats
     are the set-aside catch carried away at dusk toward a small DISTANT shore fire —
     thin smoke, grave tone, never close flames, never a person or a creature in fire,
     never any suffering depicted.
  4. THE CLOSING TURN IS THE REASON THE VIDEO EXISTS and V1 gave it no picture of its
     own: "it was cast for you. The gathering came first." It is carried by RETURNING
     to the bright morning water and the net going out wide — the same act the video
     opened on, now read as grace.

STAGING ACROSS THE LIBRARY — this row must not repeat a composition already used:
  rows 2, 8, 21 (Luke 15)      courtyard table / low wall under a fig / house meal
  row 11 (the storm)           an open boat at NIGHT in a gale
  row 16 (Mary & Martha)       a lamplit evening interior
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
This row is a water story, so the two rows it could collide with are 11 and 24 and
both were checked deliberately. It is staged in THREE places, none of them used above:
  * THE FRAME — a low man-made BREAKWATER of dry-laid rounded field boulders running
    out from a small harbour into the open lake, water on THREE sides of the stone.
    It is not a beach (19, 24), not a boat (11, 24), not rock in a dry landscape (29).
    n1 says "he set it out on the water", and this is the one place in the library
    where the ground underfoot is stone and the water is all round it.
  * THE OPEN WATER — two working boats on DEEP water with the land a thin far line,
    in daylight. Row 11 is one boat at night in a gale; row 24 is one boat MOORED
    close in off a shingle beach in daylight. Deep water, two boats, and a dragnet
    strung between them is neither.
  * THE STRAND — a wide flat SAND-AND-HARD-MUD strand at the mouth of a stream, ridged
    by the water, with dry reed beds standing back from the waterline. Deliberately
    not row 19's stony beach with its charcoal fire and not row 24's shingle.

THE CLOCK IS THE PLOT AND IT IS ON THE SCREEN. Each thread's light only ever moves
forward, and the frame's hour NEVER changes:
  b01 b02 b23 b30 b31 b32 b33 b37 b40   THE FRAME — high BRIGHT EARLY AFTERNOON on the
                                        boulder mole, hard clean light almost overhead,
                                        short shadows, the lake broken into hard white
                                        glitter. Identical in all nine, always.
  b03-b06                               CLEAR EARLY MORNING on the open water, the sun
                                        low off the left, a long sparkle path
  b07-b13                               HIGH MIDDAY on the open water, sun overhead,
                                        the water dark green-black under it
  b14-b21                               LONG GOLD LATE AFTERNOON on the strand
  b22                                   the gold going flat and cool, first of the dusk
  b24-b29, b34                          GRAVE BLUE DUSK on the strand, a small DISTANT
                                        fire far up the shore, thin smoke
  b35 b36 b38 b39                       BACK TO CLEAR EARLY MORNING on the open water —
                                        deliberate, and it is the point: the closing
                                        grace beats return to the cast that included
                                        everyone

TERRAIN IS THE INVARIANT (the rule rows 24-29 established). Each of the three places
is described identically in every beat it appears in; only the light and what the men
are doing ever change.

CAST NOTE — ANCHOR-FIRST (the rows 20-29 lesson that has held the reroll rate at
3-25%). This row needs exactly TWO new faces, so exactly TWO beats are anchors and
they are generated in their OWN run before anything else, each composed so the face is
large, lit and unobstructed, AND — the rows 28/29 lesson — with the HEAD TURNED OFF
THE CAMERA AXIS and the nose pointed at a named frame corner, because on a
near-frontal portrait naming a gaze target inside the frame was not enough on its own:
  b12  the CREWMAN, the young one, leaning over the gunwale watching the net go down
  b20  the HEADMAN, the old master fisherman, seated over a basket in gold afternoon
`v2_gen_api` builds its REFS cache ONCE per run, so an anchor generated in the same
run as its dependants does not exist yet when they are built — it MUST be a separate
invocation. Jesus is held by JESUS-V2-REF as always.

A FACE SHEET ALONE DOES NOT HOLD A CHARACTER WHO IS SMALL IN FRAME (rows 19, 22-29).
So the HEADMAN and CREWMAN locks state age, build, hair and dress as explicit
invariants, and every beat naming either of them RESTATES him positively in its own
scene text — including in the wides where he is a distant figure.

CREAM: only Jesus. THE TRAP ON THIS ROW IS THE FISHERMAN'S TUNIC, which is exactly
the garment a model renders in undyed bleached homespun — a second, unlocked Jesus in
every working frame. So every man in the parable is pinned ENTIRELY to dark saturated
wool, and — the row 28 lesson, where the leak was the SCARF and not the tunic — EVERY
SEPARATE PIECE OF CLOTH on every non-Jesus figure is enumerated by name (tunic,
sleeves, sash, head cloth, and any scarf, stole, shawl, wrap or mantle) and pinned
dark, with each head cloth given something to DO (its loose end thrown back over a
named shoulder) so the model cannot quietly drop it.

THE SECOND TRAP ON THIS ROW IS THE NET, and it is the row's own new-setting
anachronism: a model asked for a fishing net renders BRIGHT SYNTHETIC MONOFILAMENT in
green or blue, MOULDED PLASTIC FLOATS in orange or white, and a machined metal ring at
every corner. PERIOD-MATERIALS reaches part of this (it names nets and floats), so no
new SHARED lock was needed — but it is restated positively and in detail in the NET
lock below, because the net is the largest and most central object in twenty-five of
these forty frames and there is nowhere for a defect in it to hide.

THE THIRD TRAP is the CATCH. "Every kind" invites a model to paint an aquarium — reef
fish, tropical colour, ocean species, impossible sizes. The FISH lock pins the catch
to the real freshwater species of that lake and states the variety as SIZE and SHAPE
rather than colour, which is what the parable actually means.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER name a
# character. Clothing colours are stated POSITIVELY and DARK, piece by piece.
LOCKS = {
    # ------------------------------------------------------------- people ----
    "HEADMAN": (
        "HEADMAN LOCK: the master fisherman is the SAME man in every shot, and these "
        "are invariants that hold even when he is small, distant, in shadow or out of "
        "focus: a Galilean fisherman of about fifty-five, broad and thick through the "
        "chest, shoulders and forearms from a lifetime on the oars and the hauling "
        "rope, not fat, standing a little stooped. His skin is deeply sun-blackened "
        "red-brown, coarse and creased; his face is broad and flat-planed with a heavy "
        "jaw, a blunt nose broken once and set crooked, deep vertical creases between "
        "the brows and a fan of white lines at the outer corners of the eyes from a "
        "permanent squint into water glare. His beard is short, cut close, and grizzled "
        "IRON-GREY; his hair is thick, grey-shot black, pushed straight back off a high "
        "forehead and cut at the nape. His eyes are small, steady and dark brown. His "
        "hands are enormous, thick-knuckled, scarred across the palms and rope-burned, "
        "with cracked nails. EVERY SEPARATE PIECE OF CLOTH ON HIM IS DARK AND "
        "SATURATED: a knee-length DARK UMBER-BROWN coarse hand-woven wool tunic with "
        "the straight sleeves pushed up above the elbows, a twisted DARK BROWN rope "
        "sash knotted at the waist, and a DEEP INDIGO head cloth whose LOOSE END IS "
        "THROWN BACK OVER HIS LEFT SHOULDER and hangs down his back. He wears no "
        "scarf, stole, shawl, wrap or mantle of any other colour, and nothing he wears "
        "is cream, off-white, ivory, buff, beige, taupe, sand, khaki or pale. He is "
        "barefoot, his feet and shins wet and sand-crusted."
    ),
    "CREWMAN": (
        "CREWMAN LOCK: the young fisherman is the SAME man in every shot, and these "
        "are invariants that hold even when he is small, distant, in shadow or out of "
        "focus: a Galilean of about twenty, lean and long-limbed and quick, narrow "
        "through the waist with wiry forearms, a full head taller than the headman and "
        "half his width. His skin is warm sun-browned olive, smooth, still unlined "
        "except at the eyes. His face is narrow and open with high cheekbones, a "
        "straight nose and a wide mouth; his beard is thin, soft and patchy along the "
        "jaw and has never been cut. His hair is dark brown, thick and springy, cut "
        "roughly at the jaw and pushed behind the ears, salt-stiffened. His eyes are "
        "clear light brown. His hands are long and hard-palmed but unscarred. EVERY "
        "SEPARATE PIECE OF CLOTH ON HIM IS DARK AND SATURATED: a short DARK "
        "OLIVE-DRAB coarse hand-woven wool tunic ending above the knee with straight "
        "sleeves cut off at the shoulder, a RUSSET-RED folded cloth sash knotted at "
        "the hip, and a CHARCOAL-GREY head cloth whose LOOSE END IS THROWN BACK OVER "
        "HIS RIGHT SHOULDER. He wears no scarf, stole, shawl, wrap or mantle of any "
        "other colour, and nothing he wears is cream, off-white, ivory, buff, beige, "
        "taupe, sand, khaki or pale. He is barefoot and his legs are wet to the thigh."
    ),
    "CREW": (
        "CREW LOCK: the rest of the fishing crew are four to six other first-century "
        "Galilean working men between twenty-five and fifty, weathered brown skin, "
        "dark hair, all of them bearded, hard-handed and barefoot, none of them "
        "resembling the headman or the young crewman and no two of them sharing a "
        "face. EVERY SEPARATE PIECE OF CLOTH ON EVERY ONE OF THEM IS A DARK SATURATED "
        "COLOUR — tunic, sleeves, sash, head cloth, and any scarf, stole, shawl, wrap "
        "or mantle — in DEEP INDIGO, DARK UMBER-BROWN, DARK OLIVE-DRAB, RUSSET-RED or "
        "CHARCOAL-GREY coarse hand-woven wool, every one of them plain and undyed-dark, "
        "and each man's head cloth has its LOOSE END THROWN BACK OVER ONE SHOULDER so "
        "it reads as a separate piece of cloth. NOT ONE OF THEM WEARS ANYTHING CREAM, "
        "OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI OR PALE, at any distance, "
        "in focus or out of focus, at any edge of the frame."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the men listening are a small closed circle of eight to ten "
        "first-century Galilean working men between twenty-five and fifty, weathered "
        "brown skin, dark hair, most of them bearded and one of them young and "
        "clean-shaven, no two of them sharing a face. EVERY SEPARATE PIECE OF CLOTH ON "
        "EVERY ONE OF THEM IS A DARK SATURATED COLOUR — tunic, sleeves, sash, head "
        "cloth, and any scarf, stole, shawl, wrap or mantle — in DEEP INDIGO, DARK "
        "UMBER-BROWN, DARK OLIVE-DRAB, RUSSET-RED or CHARCOAL-GREY coarse hand-woven "
        "wool, and each head cloth has its LOOSE END THROWN BACK OVER ONE SHOULDER so "
        "it reads as a separate piece of cloth. NOT ONE OF THEM WEARS ANYTHING CREAM, "
        "OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI OR PALE, at any distance, "
        "in focus or out of focus, at any edge of the frame — the one pale garment in "
        "the whole picture is the robe Jesus himself is wearing. They sit low on the "
        "stone, barefoot or in worn leather sandals, and they carry nothing."
    ),
    # ----------------------------------------------------------- settings ----
    "MOLE": (
        "MOLE LOCK: the frame scene is always the same place and it never changes. It "
        "is a low man-made BREAKWATER built of rough ROUNDED GREY-BROWN FIELD "
        "BOULDERS, dry-laid and packed by hand with no mortar, running out from a small "
        "fishing harbour into the open lake — about four paces wide, its top an uneven "
        "pavement of flat-topped stones with dry salt-bleached weed and pale grit in "
        "the gaps, its sides sloping away into green water that laps and sucks through "
        "the boulders. WATER LIES ON THREE SIDES OF THE STONE and runs out to a clean "
        "far horizon. Low and small and far back at one end stand the flat mud-brick "
        "and pale limestone roofs of the harbour town with bare tawny hills behind "
        "them. THE LIGHT IS IDENTICAL IN EVERY FRAME BEAT: high BRIGHT EARLY-AFTERNOON "
        "sun almost overhead and a little behind the camera, hard clean light, short "
        "dark shadows pooled directly under the seated men, and the lake surface broken "
        "into hard white glitter. There is NO tree, no canopy, no bush, no wall, no "
        "roof and no building anywhere on or near the stone; no boat tied alongside; no "
        "fire, no smoke and no lamp; no net, no basket and no fish anywhere on the "
        "mole; and no mooring post, bollard, ring, chain, rail or rope on it."
    ),
    "DEEPWATER": (
        "DEEP-WATER LOCK: this is the open middle of a large freshwater lake and it is "
        "always the same water. There is no beach, no jetty, no rock and no building "
        "anywhere near — the land is only a THIN FAR LINE of low tawny hills along one "
        "distant edge of the picture, hazy with distance, and everywhere else is open "
        "water to a clean horizon. The boats are TWO open working boats of the same "
        "build: hulls of bare hewn and adzed planks pegged to sawn frames, the wood "
        "weathered grey-brown and unpainted and unvarnished and worn bright along the "
        "gunwale where hands and ropes pass, a single low mast of rough timber, long "
        "hand-shaped wooden oars on twisted fibre loops, and a bilge of wet planking "
        "with coiled flax rope, fired-clay water jars and hand-woven reed baskets lying "
        "in it. THE HULLS CARRY NO PAINT, NO VARNISH, NO STRIPE, NO NAME, NO NUMBER AND "
        "NO LETTERING; there is no metal cleat, screw, bolt, hinge, chain, wire or "
        "sheet metal anywhere on either boat, no engine, motor, propeller or rudder "
        "wheel, no plastic, no rubber fender, no glass, no flag, no buoy of moulded "
        "material and no modern object of any kind."
    ),
    "STRAND": (
        "STRAND LOCK: the shore scene is always the same place. It is a WIDE FLAT "
        "STRAND of grey-brown sand and hard packed mud at the mouth of a small stream "
        "running into the lake, the surface ridged and combed in long shallow ripples "
        "by the water, scattered with dark rounded stones the size of a fist and "
        "streaked with drying green weed and thin white salt lines. Dry pale REED BEDS "
        "stand back from the waterline in a broken wall along one side, and low bare "
        "tawny hills lie behind them. The water shelves so gradually that it runs out "
        "in a long thin sheet across the flat, and one open working boat of hewn "
        "unpainted grey-brown planks lies grounded and canted over on the mud with its "
        "keel in a scoured furrow. THERE IS NO SHINGLE, NO PEBBLE BEACH, NO CLIFF, NO "
        "HARBOUR, NO JETTY, NO STONE MOLE, NO QUAY, NO BUILDING, NO WALL, NO TREE AND "
        "NO TENT anywhere on this shore, and no fire except where the scene itself "
        "places one far off in the distance."
    ),
    # ------------------------------------------------------------- objects ---
    "NET": (
        "NET LOCK: the net is a first-century DRAGNET and it is built entirely by hand. "
        "It is a long wall of hand-knotted cord in a coarse diamond mesh with openings "
        "about the width of two fingers, the cord twisted from natural flax and hemp "
        "fibre and gone unevenly BROWN, GREY AND TAR-DARKENED with use, thick and "
        "slightly furred, sagging heavily and unevenly when it holds anything. Its top "
        "edge is a thick twisted fibre head-rope strung at intervals with floats of "
        "LIGHT BARE WOOD AND CORK-OAK BARK, irregular in shape and undyed; its bottom "
        "edge is a thicker foot-rope weighted at intervals with FLAT DRILLED GREY "
        "STONES and small rings of fired clay. Where it has been mended the repairs are "
        "visibly lighter, newer cord knotted in by hand. THE NET IS NOT MANUFACTURED: "
        "there is no nylon, monofilament, polypropylene or any synthetic cord; no "
        "bright green, blue, orange, red, yellow or fluorescent colour anywhere in it; "
        "no perfectly regular machine-made mesh; no moulded plastic or polystyrene "
        "float; no coloured buoy; no metal ring, clip, swivel, shackle or chain; and no "
        "lettering, tag or label anywhere on it."
    ),
    "FISH": (
        "CATCH LOCK: the fish are the real freshwater fish of a first-century Galilean "
        "lake and the VARIETY IS IN SIZE AND SHAPE, not in colour. There are "
        "broad-bodied deep flat fish the length of a forearm with blunt heads, small "
        "spines along the back and faint dark vertical bars; long slender fish with "
        "smooth heads, trailing barbels at the mouth and heavy shoulders; and drifts of "
        "small slim silver fish the length of a finger. All of them are WET, SLICK AND "
        "HEAVY, in dull silver, olive-grey, brass-brown and greenish black, with clear "
        "wet eyes, open gasping mouths and red gills showing, some still curling and "
        "kicking. THE CATCH IS NOT AN AQUARIUM: there is no tropical or reef fish, no "
        "bright blue, yellow, orange, pink or striped fish, no ocean species, no shark, "
        "ray, eel, octopus, crab, lobster, shellfish or seaweed frond, nothing larger "
        "than a man's arm, and nothing that does not belong in fresh water."
    ),
}

OUTPUT_ASSET_DIR = "assets"

# Every V1 mp3 and the V1 MP4 share ONE git content date (2026-07-27T22:50:25) and the
# MP4's runtime sits inside the guard's tripwire (154.933 s against a 154.885 s summed
# timeline), so the finished V1 audio stream is current and the normal packet-copy
# AUDIO LOCK applies. Nothing is re-voiced and V1 is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Filled in AFTER the two anchor beats are generated in their own run. v2_gen_api
# builds this cache once per invocation, so an anchor cannot be referenced by a beat
# generated in the same run as itself.
REFS = {
    "CREWMAN": "assets/s12-the-gathering-is-wide-open.jpeg",
    "HEADMAN": "assets/s20-into-baskets.jpeg",
}

_NO_JESUS = ("no Jesus in this frame; no boulder breakwater, no harbour town and no "
             "early-afternoon frame-story light; ")
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand or pale garment on "
             "anybody anywhere in the frame including the blurred edges; ")
_NO_MODERN_NET = ("no nylon, monofilament or synthetic net cord, no bright green, "
                  "blue or orange netting, no moulded plastic float, no coloured "
                  "buoy, no metal ring, clip or chain on the net; ")
_GAZE = "nobody's pupils centred on the lens."

BEATS = [
    # =============== FRAME — the boulder mole, bright early afternoon ==========
    {
        "id": "v2-r030-b01", "out": "s01-one-more-short-story.jpeg",
        "seg": "n1", "window": "0.280-3.980", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "Jesus told one more short story about the kingdom of heaven,",
        "must_show": "Jesus seated on the flat-topped boulders of the low breakwater with his small closed circle of disciples sitting low on the stone around him, the open lake on three sides, in high bright early-afternoon sun.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no dusk, no sunset and no golden low sun; no tree, no canopy, no wall, no roof and no building on or near the stone; no boat alongside, no net, no basket, no fish and no fire anywhere in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, high bright early-afternoon sun almost "
            "overhead and a little behind the camera, hard clean light, short dark "
            "shadows pooled directly under the seated men, the lake broken into hard "
            "white glitter on both sides, fine film grain. THE CAMERA IS PLACED "
            "COMPLETELY SIDE-ON TO THE WHOLE CIRCLE, STANDING OUT ON THE STONE WELL TO "
            "ONE SIDE AND SHOOTING ACROSS THE GROUP AT RIGHT ANGLES TO EVERY EYELINE "
            "IN THE PICTURE. Jesus sits at the LEFT of the frame on a flat-topped "
            "boulder and the disciples are ranged along the stone to the RIGHT of him, "
            "so the whole conversation runs HORIZONTALLY ACROSS THE FRAME: his gaze "
            "travels rightward into the seated men and exits through the RIGHT EDGE, "
            "and every disciple is seen in profile or three-quarter from behind with a "
            "gaze travelling leftward and out through the LEFT EDGE. NOT ONE MAN'S "
            "FACE IS SQUARED UP TO THE CAMERA AND NOT ONE PAIR OF PUPILS IS CENTRED ON "
            "THE LENS. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A PORTRAIT: "
            "the camera is far enough back that Jesus AND at least six seated disciples "
            "are in the frame together, head to feet, with the open water and the clean "
            "far horizon behind them; Jesus occupies only a modest part of the picture "
            "and is never framed from the chest up. EXACTLY TWO out-of-focus seated "
            "BACKS fill the near bottom corners and they are the only foreground "
            "objects: a DEEP INDIGO shouldered back with a dark indigo head cloth at "
            "the near LEFT and a DARK UMBER back with a dark brown head cloth at the "
            "near RIGHT, BOTH OF THEM A SOLID DARK SATURATED MASS FROM EDGE TO EDGE. "
            "THERE IS NO PALE, IVORY, BEIGE, TAUPE, BUFF, SAND OR LIGHT-TAN SHAPE, "
            "SHOULDER, BACK, SLEEVE, DRAPE OR BLURRED MASS ANYWHERE IN THE FOREGROUND "
            "OR AT ANY EDGE OF THIS PICTURE — the ONLY pale thing in the whole frame is "
            "the wool of Jesus's own robe. Sharp in the middle distance Jesus sits on "
            "the boulder seen from his left side, forearms on his knees, one hand "
            "beginning to open as he starts to speak."
        ),
    },
    {
        "id": "v2-r030-b02", "out": "s02-out-on-the-water.jpeg",
        "seg": "n1", "window": "3.980-6.747", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "and this time he set it out on the water.",
        "must_show": "Jesus in three-quarter profile on the mole, his open hand carried out level toward the open lake, the water and the far horizon filling the space his hand travels into.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no dusk, no sunset and no golden low sun; no net, no boat, no basket, no fish and no fire anywhere in this frame; no tree, no wall and no building near the stone; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, a medium three-quarter view from Jesus's left "
            "and slightly below, shallow depth of field with the far water soft, high "
            "bright early-afternoon sun almost overhead, hard clean light, the lake "
            "broken into hard white glitter behind him, fine film grain. THE CAMERA "
            "STANDS OUT ON THE STONE TO HIS LEFT AND SHOOTS ACROSS HIM, so his head is "
            "turned well off the camera axis with his nose pointed toward the RIGHT "
            "EDGE of the frame and his gaze travelling out level along his own arm and "
            "clean out through that RIGHT EDGE — his pupils never come near the lens. "
            "He sits on a flat-topped grey-brown boulder in his one plain undyed "
            "off-white cream wool robe, the only pale garment in the picture, and his "
            "near arm is raised and carried OUT AND LEVEL, the palm open and turned "
            "slightly up, the gesture setting something down on the surface of the "
            "water rather than pointing at it. Behind and below his hand the open lake "
            "runs flat and glittering to a clean far horizon and fills the whole right "
            "half of the picture. In the near bottom-left corner, out of focus and dark, "
            "is one seated shoulder and dark indigo head cloth of a listening man, a "
            "solid dark saturated mass, and there is no pale, ivory, beige, buff or "
            "sand-coloured shape anywhere else in the frame. Below him the dry-laid "
            "rounded field boulders of the mole are sharp and close, pale grit and "
            "salt-bleached weed in the gaps."
        ),
    },
    # ================ j1 — Matthew 13:47, the open water, early morning ========
    {
        "id": "v2-r030-b03", "out": "s03-cast-into-the-sea.jpeg",
        "seg": "j1", "window": "6.747-10.547", "wide": True, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREW", "CREWMAN"],
        "narration": "Again, the kingdom of heaven is like unto a net, that was cast into the sea,",
        "must_show": "the dragnet leaving the boat — a heavy brown wall of hand-knotted mesh already half in the water and still paying out over the gunwale, the crew feeding it out, on open water in clear early morning.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no night, no storm, no gale, no breaking waves and no dark sky; no beach, no jetty, no rock and no building near the boats; no painted or white hull, no engine, no metal fitting; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, clear EARLY MORNING with the sun still low off "
            "the LEFT laying a long broken sparkle path across the water, the light "
            "raking and warm-white, the lake a moving blue-green, fine film grain. THE "
            "CAMERA IS IN THE SECOND BOAT, LOW AND WELL BEHIND THE WORKING MEN, AND "
            "SHOOTS PAST THEM ACROSS THE WATER: the two nearest fishermen are seen "
            "entirely FROM BEHIND, their dark backs and working shoulders filling the "
            "near left of the frame, and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS "
            "IS A WIDE FULL-LENGTH WORKING SCENE AND NOT A PORTRAIT: the camera is far "
            "enough back that a whole open boat, four or five men in it head to feet, "
            "and a long stretch of open water are all in the frame together. Sharp in "
            "the middle of the picture the DRAGNET is going over the side — a heavy "
            "brown and grey wall of hand-knotted flax mesh sagging in loose folds, its "
            "float-line of irregular bare wood and cork bark already strung out across "
            "the surface in a curving line running away toward the RIGHT EDGE, its "
            "weighted stone foot-line sinking dark below it. Two men lean out over the "
            "gunwale feeding the mesh out hand over hand, and the young crewman — lean, "
            "long-limbed, about twenty, thick dark brown hair cut roughly at the jaw, "
            "in a short DARK OLIVE-DRAB tunic with a RUSSET-RED sash and a "
            "CHARCOAL-GREY head cloth thrown back over his right shoulder — stands "
            "braced in the bow with the head-rope running through his fists, seen in "
            "hard profile against the water, his gaze down on the rope. Every other man "
            "is in deep indigo, dark umber, dark olive or russet wool with a dark head "
            "cloth. Far off along the LEFT edge the land is only a thin hazy line of "
            "low tawny hills; everywhere else is open water to a clean horizon."
        ),
    },
    {
        "id": "v2-r030-b04", "out": "s04-of-every-kind.jpeg",
        "seg": "j1", "window": "10.547-15.517", "wide": True, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREW"],
        "narration": "and gathered of every kind:",
        "must_show": "the net fully out — a long curving arc of float-line stretched right across the open water between the two boats, the mesh hanging down in the green water beneath it, the sea it encloses enormous.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no night, no storm and no dark sky; no beach, no jetty and no building near the boats; no painted or white hull, no engine, no metal fitting; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, deep depth of field, clear EARLY MORNING with "
            "the sun low off the LEFT and a long broken sparkle path lying across the "
            "water, fine film grain. THE CAMERA IS HIGH IN THE STERN OF THE NEAR BOAT "
            "LOOKING OUT AND DOWN ACROSS THE WATER, WELL BEHIND EVERY MAN IN THE "
            "PICTURE, so the two figures in the near bottom corners are seen only as "
            "dark backs and shoulders from directly behind and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE OPEN-WATER LANDSCAPE AND NOT A PORTRAIT: "
            "the men are small, the water is the subject, and both boats are visible "
            "whole. The float-line of the dragnet runs from the near boat in a long "
            "shallow ARC right across the middle of the picture and away to the "
            "SECOND BOAT lying small in the distance at the far end of the arc — a "
            "line of irregular bare wood and cork-bark floats riding the surface, "
            "hundreds of them, dipping and lifting in the swell. Beneath the line the "
            "brown hand-knotted mesh hangs down into clear green water and fades into "
            "darkness, and the enormous stretch of open water the arc encloses lies "
            "flat and bright between them. In the near bottom-left corner the "
            "weathered grey-brown gunwale of the boat and one dark umber shoulder are "
            "sharp and close; in the near bottom-right corner a coil of twisted flax "
            "rope lies on wet planking. There is no pale, ivory, beige, buff or sand "
            "cloth anywhere in the picture. Far off along the LEFT edge the land is "
            "only a thin hazy line of low tawny hills."
        ),
    },
    # ==================== n2 — the throwing and the sinking ====================
    {
        "id": "v2-r030-b05", "out": "s05-off-the-side-of-the-boat.jpeg",
        "seg": "n2", "window": "15.517-19.537", "wide": False, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREWMAN"],
        "narration": "Picture fishermen throwing a great wide net off the side of the boat,",
        "must_show": "a close mid-action moment of the mesh actually leaving human hands over the gunwale — arms extended, the net in mid-air in a heavy brown fan, water below.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no night, no storm and no dark sky; no beach and no building; no painted or white hull, no engine, no metal fitting; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, shot from LOW AND BEHIND the working man's "
            "right shoulder inside the boat so his back and the back of his head fill "
            "the near left of the frame and his face is never seen, clear EARLY MORNING "
            "light raking in from the LEFT, a fast shutter freezing water drops in the "
            "air, fine film grain. Mid-action and mid-throw: the young crewman — lean, "
            "long-limbed, about twenty, thick dark brown hair cut roughly at the jaw, "
            "in a short DARK OLIVE-DRAB tunic with a RUSSET-RED sash and a "
            "CHARCOAL-GREY head cloth thrown back over his right shoulder — is caught "
            "at the top of the swing with both arms flung out over the gunwale and his "
            "weight thrown forward onto the rail, seen from behind and in "
            "three-quarter, his gaze down and away toward the LOWER RIGHT CORNER of the "
            "frame. The heavy brown and grey hand-knotted mesh is IN MID-AIR in a wide "
            "loose fan between his hands and the water, unfolding as it goes, its bare "
            "wood and cork-bark floats scattered along the top edge and its flat "
            "drilled stone weights swinging below, wet cord flicking bright drops. "
            "Below and beyond, the blue-green water is close and sharp, already dimpled "
            "where the first weights have gone in. The weathered grey-brown adzed "
            "planking of the gunwale, worn bright along its top edge, runs across the "
            "bottom of the frame. There is no pale, ivory, beige, buff or sand cloth "
            "anywhere in the picture."
        ),
    },
    {
        "id": "v2-r030-b06", "out": "s06-sink-down-and-drag.jpeg",
        "seg": "n2", "window": "19.537-23.701", "wide": False, "jesus": False,
        "locks": ["DEEPWATER", "NET"],
        "narration": "letting it sink down and drag through the whole sea.",
        "must_show": "the mesh sinking — the net seen through and under the surface, hanging as a brown curtain going down into green water and fading into the dark below.",
        "must_not_show": _NO_JESUS + _NO_MODERN_NET + "no fish yet in the mesh; no person's face; no night, no storm and no dark sky; no beach, no rock and no building; no coral, no reef and no tropical colour; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, shot from the gunwale looking STRAIGHT DOWN AND "
            "OUT into the water at a shallow angle, clear EARLY MORNING light coming "
            "in from the LEFT and driving down through the surface in moving shafts, "
            "fine film grain, no person's face anywhere in the picture. The upper sixth "
            "of the frame is the bright dimpled surface of the lake with the "
            "float-line of irregular bare wood and cork-bark floats riding it, seen "
            "almost edge-on and running away toward the RIGHT EDGE. Everything below is "
            "UNDERWATER and it is the subject: the brown and grey hand-knotted diamond "
            "mesh hangs as a long curtain from that line, sagging in slow folds, its "
            "wet cord catching the light in short bright dashes where the sun strikes "
            "it, its flat drilled grey stone weights strung along the bottom edge and "
            "pulling it down. The curtain runs away from the camera and DOWN, its lower "
            "reaches going soft and blue-green and finally lost in darkness at the "
            "bottom of the frame, so the depth of the water is legible. Fine particles "
            "drift in the green light. In the near top-left corner the weathered "
            "grey-brown planking of the boat's side is sharp and close and dripping. "
            "There is no fish in the mesh yet, and nothing bright, coloured or "
            "synthetic anywhere in the water."
        ),
    },
    # ============ n3 — the first beautiful thing, high midday, every kind ======
    {
        "id": "v2-r030-b07", "out": "s07-does-not-pick-and-choose.jpeg",
        "seg": "n3", "window": "23.701-28.521", "wide": True, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREW", "HEADMAN"],
        "narration": "And here is the first beautiful thing. That net does not pick and choose.",
        "must_show": "the long haul under high midday sun — the crew leaning back on the head-rope, the net coming in heavy and blind, nobody choosing anything, just pulling.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no night, no storm and no dark sky; no beach and no building near the boats; no painted or white hull, no engine, no metal fitting; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, HIGH MIDDAY sun straight overhead, hard "
            "vertical light, the men's shadows pooled tight under their own feet, the "
            "water gone dark green-black under the sun with a small hard patch of "
            "glitter, fine film grain. THE CAMERA STANDS IN THE STERN OF THE BOAT "
            "BEHIND THE WHOLE HAULING LINE AND SHOOTS FORWARD PAST THEIR BACKS, so "
            "every man is seen from directly behind or in three-quarter from behind and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH "
            "WORKING SCENE AND NOT A PORTRAIT: four men are visible head to feet in a "
            "line down the boat with the open water beyond them. They are hauling: "
            "each man has the thick twisted head-rope over one shoulder and gripped in "
            "both fists, all of them leaning their weight back and away from the "
            "gunwale in the same direction, feet braced wide on wet planking, the rope "
            "hard and straight, water squeezing out of it. Nearest the bow the headman "
            "— broad and thick through the chest, about fifty-five, short grizzled "
            "iron-grey beard, DARK UMBER-BROWN tunic with sleeves pushed above the "
            "elbows, DARK BROWN rope sash, DEEP INDIGO head cloth thrown back over his "
            "left shoulder — hauls in hard profile, his gaze fixed down the rope and "
            "out through the LEFT EDGE. The others are in deep indigo, dark olive-drab "
            "and russet wool with dark head cloths. Over the gunwale the brown "
            "hand-knotted mesh is coming up out of the water in dripping folds, heavy "
            "and shapeless and full, sagging under its own weight. There is no pale, "
            "ivory, beige, buff or sand cloth anywhere in the picture."
        ),
    },
    {
        "id": "v2-r030-b08", "out": "s08-every-kind-of-fish.jpeg",
        "seg": "n3", "window": "28.521-31.241", "wide": False, "jesus": False,
        "locks": ["NET", "FISH"],
        "narration": "It sweeps up every kind of fish there is:",
        "must_show": "a close look into the risen mesh — a genuinely mixed press of real lake fish of different sizes and shapes packed together against the wet cord.",
        "must_not_show": _NO_JESUS + _NO_MODERN_NET + "no tropical, reef or brightly coloured fish, no shark, ray, eel, octopus, crab or shellfish, no seaweed frond; no person's face; no night; no coral and no aquarium glass; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens close in, shallow depth of field with the far "
            "side of the mesh going soft, HIGH MIDDAY sun straight down putting a hard "
            "wet shine on every scale and throwing tight shadows between the fish, fine "
            "film grain, no person's face in the picture. The frame is filled almost "
            "edge to edge by the risen dragnet: the brown, grey and tar-darkened "
            "hand-knotted diamond mesh, thick and slightly furred and streaming water, "
            "pressed and stretched taut by what is inside it. Packed against the cord "
            "and against each other are fish of visibly DIFFERENT KINDS, and the "
            "variety is in size and shape: two or three broad deep flat fish the length "
            "of a forearm with blunt heads and faint dark bars, one long slender fish "
            "with a smooth head and trailing barbels at its mouth lying diagonally "
            "across them, and a packed drift of small slim silver fish the length of a "
            "finger filling every gap between. All of them are wet, slick and dull — "
            "silver, olive-grey, brass-brown and greenish black — with clear wet eyes, "
            "open gasping mouths and red gills showing, one broad tail caught in "
            "mid-kick and blurred. Water runs off the cord in threads. In the top-left "
            "corner, out of focus, one brown hand grips the mesh; no face is visible. "
            "Beyond the net the dark green-black midday water is a soft field of "
            "nothing."
        ),
    },
    {
        "id": "v2-r030-b09", "out": "s09-big-ones-small-ones.jpeg",
        "seg": "n3", "window": "31.241-35.881", "wide": False, "jesus": False,
        "locks": ["FISH", "CREW"],
        "narration": "big ones, small ones, common ones, strange ones,",
        "must_show": "the catch spilling out of the mesh into the bilge of the boat — a countable spread of clearly different fish, big and small and odd, tumbled together on wet planking.",
        "must_not_show": _NO_JESUS + _NO_CREAM + "no tropical, reef or brightly coloured fish, no shark, ray, eel, octopus, crab or shellfish; no face turned toward the lens; no night; no plastic crate, tray or box; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens angled STEEPLY DOWN into the open bilge of the "
            "boat from above and behind the working men, HIGH MIDDAY sun straight "
            "overhead putting a hard bright shine on wet scales and wet planking, fine "
            "film grain. The frame is mostly the boat's floor: weathered grey-brown "
            "adzed planks awash with a shallow film of water, a coil of twisted flax "
            "rope and one hand-woven reed basket in the top corner. Spilled across the "
            "planks in a loose heap that thins out toward the edges, so the individual "
            "fish can be SEEN AND COUNTED rather than read as a mass, is the catch: "
            "three broad deep flat fish the length of a forearm with blunt heads and "
            "faint dark bars lying on their sides, one much longer slender fish with a "
            "smooth head and trailing barbels curved right across them, one very small "
            "and very deep-bodied odd-looking fish on its own, and a scattered drift of "
            "small slim silver fish the length of a finger. They are wet, slick and "
            "dull silver, olive-grey, brass-brown and greenish black, eyes clear, mouths "
            "open, gills red, two tails caught mid-kick and blurred. Entering from the "
            "TOP EDGE of the frame only, and seen from behind, are the bare shins and "
            "one dark-sleeved forearm of a fisherman still holding the mesh open — no "
            "head, no face and no eyes appear anywhere in the picture. The brown "
            "hand-knotted mesh lies slack and emptied along the top of the frame."
        ),
    },
    {
        "id": "v2-r030-b10", "out": "s10-everything-the-sea-has-in-it.jpeg",
        "seg": "n3", "window": "35.881-39.565", "wide": True, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREW"],
        "narration": "everything the sea has in it, gathered in together.",
        "must_show": "the whole scale of it from far off — the two boats small on the enormous midday lake with the loaded net between them, so the gathering reads as the size of the sea, not the size of a catch.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no night, no storm and no dark sky; no beach, no jetty, no rock and no building close to the boats; no painted or white hull, no engine; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, very deep depth of field, HIGH MIDDAY sun "
            "straight overhead, the enormous water gone dark green-black with a small "
            "hard blaze of glitter under the sun, a wide bleached white sky, fine film "
            "grain. THE CAMERA IS FAR OUT ON THE WATER AND WELL BEHIND BOTH BOATS AND "
            "SHOOTS PAST THEM, so every figure aboard is a small distant shape seen "
            "from behind or from the side and NOT ONE FACE IS TURNED TOWARD THE LENS "
            "and no face is even legible. THIS IS A WIDE OPEN-WATER LANDSCAPE AND NOT "
            "A PORTRAIT: the two open boats sit SMALL in the lower third of the frame, "
            "each with four or five dark-clothed men aboard visible head to feet, and "
            "the rest of the picture is water and sky. Between and behind them the "
            "float-line of the dragnet is drawn into a long closing curve of bare wood "
            "and cork-bark floats riding the surface, its enclosed water darker and "
            "boiling faintly where the catch turns beneath it, the loaded brown mesh "
            "just breaking the surface along the near side of the curve. The men are in "
            "deep indigo, dark umber, dark olive-drab and russet wool with dark head "
            "cloths and there is no pale, ivory, beige, buff or sand cloth anywhere in "
            "the picture. The lake runs unbroken to a clean far horizon on every side "
            "except the far LEFT edge, where the land is only a thin hazy line of low "
            "tawny hills."
        ),
    },
    # ==================== n4 — the net is not fussy ============================
    {
        "id": "v2-r030-b11", "out": "s11-not-fussy.jpeg",
        "seg": "n4", "window": "39.565-42.745", "wide": False, "jesus": False,
        "locks": ["NET", "FISH"],
        "narration": "The net is not fussy about who gets caught up in it.",
        "must_show": "a tight look at the mesh's blind indifference — one very ordinary small fish and one large fine one held in the same few knots of the same cord, neither of them treated differently.",
        "must_not_show": _NO_JESUS + _NO_MODERN_NET + "no tropical, reef or brightly coloured fish, no shark, ray, eel, octopus or shellfish; no person's face; no night; no hand sorting or choosing between them; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens very close in, extremely shallow depth of "
            "field with everything past the cord dissolving into soft dark green, HIGH "
            "MIDDAY sun straight down putting a hard wet specular shine on the cord and "
            "the scales, fine film grain, no person anywhere in the picture. The frame "
            "is a few square hands of the DRAGNET seen almost flat on: thick brown and "
            "grey hand-knotted flax cord, furred and slightly frayed, one repair of "
            "newer lighter cord knotted in near the top, water beading and running along "
            "it. Caught in the SAME few diamond openings of that same cord, side by "
            "side and given exactly the same treatment by it, are two fish: on the left "
            "one broad deep flat fish the length of a forearm, a fine heavy fish with a "
            "blunt head and faint dark bars, its gill plate lifted and its eye clear "
            "and wet; on the right one very small, thin, plain silver fish the length "
            "of a finger, hanging by its gills in a single knot. Both are wet and slick "
            "and dull-coloured; both are held identically; nothing distinguishes how "
            "the net treats them. NO HAND, ARM, FACE OR PERSON APPEARS IN THIS "
            "PICTURE, and nothing is choosing between them. Behind the cord the "
            "dark green-black midday water is a soft field of nothing."
        ),
    },
    {
        "id": "v2-r030-b12", "out": "s12-the-gathering-is-wide-open.jpeg",
        "seg": "n4", "window": "42.745-47.145", "wide": False, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREWMAN"],
        "narration": "The gathering is wide open.",
        "must_show": "ANCHOR FOR THE CREWMAN — his face large, lit and unobstructed, leaning over the gunwale and watching the wide net, an open unguarded expression.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no second person's face in the frame; no night, no storm; no beach and no building; no painted or white hull, no engine, no metal fitting; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, a close three-quarter view of ONE man from his "
            "front-left and slightly above, shallow depth of field with the water "
            "beyond him dissolved into soft dark green and hard glitter, HIGH MIDDAY "
            "sun straight overhead lighting the top planes of his face cleanly and "
            "leaving soft shadow under the brow and jaw, fine film grain. THE CAMERA "
            "STANDS INSIDE THE BOAT TO HIS LEFT AND SHOOTS ACROSS HIM. HIS HEAD IS "
            "TURNED WELL OFF THE CAMERA AXIS WITH HIS NOSE POINTED AT THE LOWER-RIGHT "
            "CORNER OF THE FRAME, and his gaze goes down and away along the float-line, "
            "exiting through that RIGHT EDGE — his pupils never come near the lens and "
            "he does not know he is being looked at. He is the young crewman: about "
            "twenty, lean and long-limbed, warm sun-browned olive skin still smooth, a "
            "narrow open face with high cheekbones, a straight nose, a wide mouth, a "
            "thin soft patchy beard along the jaw, thick springy dark brown hair cut "
            "roughly at the jaw and pushed behind his ears, clear light brown eyes. He "
            "is leaning forward with both forearms folded on the weathered grey-brown "
            "gunwale, resting there, watching the water. His expression is open, "
            "unguarded and quietly glad. He wears a short DARK OLIVE-DRAB coarse wool "
            "tunic with the sleeves cut off at the shoulder, a RUSSET-RED folded cloth "
            "sash, and a CHARCOAL-GREY head cloth whose loose end is thrown back over "
            "his right shoulder; nothing on him is pale. Out of focus behind him the "
            "float-line of bare wood and cork-bark floats runs away across the bright "
            "water in a long curve. No other person appears in the frame."
        ),
    },
    {
        "id": "v2-r030-b13", "out": "s13-nobody-too-far-gone.jpeg",
        "seg": "n4", "window": "47.145-51.092", "wide": False, "jesus": False,
        "locks": ["NET", "FISH"],
        "narration": "Nobody swimming in that sea is too ordinary, or too far gone, to be swept up into it.",
        "must_show": "one plain, battered, unremarkable fish held safe in the mesh with the rest — scarred and dull and old, and gathered in exactly like everything else.",
        "must_not_show": _NO_JESUS + _NO_MODERN_NET + "no tropical, reef or brightly coloured fish, no shark, ray, eel, octopus or shellfish; no person's face; no wound, blood or gore; no night; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens close in, very shallow depth of field, "
            "HIGH MIDDAY sun straight down, a hard wet shine on scale and cord, fine "
            "film grain, no person anywhere in the picture. Held in the brown "
            "hand-knotted flax mesh in the middle of the frame and sharp is ONE plain "
            "unremarkable fish: an old, worn, dull olive-grey lake fish about the "
            "length of a hand, its scales rubbed thin and patchy along the flank, one "
            "fin frayed and split at the edge, a pale healed scar line down its side, "
            "its jaw blunt and its eye clouded — an entirely ordinary, entirely "
            "unbeautiful fish, and it is intact and unhurt. It lies cradled in the "
            "diamond openings of the cord with its gills working. Immediately around "
            "and behind it, going soft with the shallow focus, other fish of other "
            "sizes press in against the same mesh — a broad deep-bodied fish above it, "
            "small slim silver fish below it — so it is plainly held in the SAME net, "
            "on the same terms, as everything else. Water runs off the cord in bright "
            "threads. NO HAND, ARM, FACE OR PERSON APPEARS IN THIS PICTURE and nothing "
            "is being pulled out or thrown back. Beyond the mesh the dark green-black "
            "midday water is a soft field of nothing."
        ),
    },
    # ============ j48 — Matthew 13:48, ashore, long gold afternoon =============
    {
        "id": "v2-r030-b14", "out": "s14-they-drew-to-shore.jpeg",
        "seg": "j48", "window": "51.092-54.532", "wide": True, "jesus": False,
        "locks": ["STRAND", "NET", "CREW", "HEADMAN"],
        "narration": "Which, when it was full, they drew to shore, and sat down,",
        "must_show": "the loaded net being dragged up out of the shallows onto the flat sand-and-mud strand in long gold late-afternoon light, the whole crew leaning into it.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no shingle or pebble beach, no cliff, no harbour, no jetty, no stone mole, no quay, no building, no wall and no tree; no fire; no night and no midday overhead sun; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, LONG GOLD LATE-AFTERNOON sun coming in almost "
            "level from the RIGHT across the flat, throwing very long soft-edged "
            "shadows away to the left across ridged wet sand, the light warm and "
            "raking, fine film grain. THE CAMERA STANDS UP THE STRAND WELL BEHIND THE "
            "HAULING MEN AND SHOOTS DOWN THE SLOPE PAST THEIR BACKS TOWARD THE WATER, "
            "so every man is seen from directly behind or in three-quarter from behind, "
            "leaning away from the camera into the drag, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH WORKING SCENE AND NOT A "
            "PORTRAIT: five men are visible head to bare feet, spread across the frame, "
            "with the water and the far horizon beyond them. They are strung out along "
            "the twisted fibre foot-rope, each with it over a shoulder and gripped in "
            "both fists, bodies angled far back, bare heels dug into the wet sand and "
            "leaving deep dragged furrows. Coming up out of the shallows behind them is "
            "the DRAGNET, enormously heavy, a long swollen brown and grey mass of "
            "hand-knotted mesh half in the thin sheet of water and half on the mud, "
            "silver catch showing in bright broken glints all through it, water pouring "
            "out of it. The headman — broad and thick through the chest, about "
            "fifty-five, short grizzled iron-grey beard, DARK UMBER-BROWN tunic with "
            "sleeves pushed above the elbows, DARK BROWN rope sash, DEEP INDIGO head "
            "cloth thrown back over his left shoulder — is nearest the water in hard "
            "profile, both hands on the rope, his gaze down the rope and out through "
            "the RIGHT EDGE. Dry pale reed beds stand back along the LEFT of the "
            "picture and low bare tawny hills lie behind them. There is no pale, ivory, "
            "beige, buff or sand cloth on anyone."
        ),
    },
    {
        "id": "v2-r030-b15", "out": "s15-and-sat-down.jpeg",
        "seg": "j48", "window": "54.532-56.832", "wide": True, "jesus": False,
        "locks": ["STRAND", "NET", "CREW", "HEADMAN"],
        "narration": "and gathered the good into vessels,",
        "must_show": "the crew SEATED on the wet sand along the opened net — down low, unhurried, the work of sorting only beginning now that everything is ashore.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no shingle beach, no cliff, no harbour, no jetty, no quay, no building, no wall and no tree; no fire; no night; nobody still standing and hauling; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, LONG GOLD LATE-AFTERNOON sun almost level from "
            "the RIGHT, very long soft shadows reaching away to the left, warm raking "
            "light on ridged wet sand, fine film grain. THE CAMERA IS DOWN LOW ON THE "
            "SAND WELL TO ONE SIDE OF THE WHOLE LINE OF MEN AND SHOOTS ALONG IT AT "
            "RIGHT ANGLES TO EVERY EYELINE, so the men are seen in profile and "
            "three-quarter from behind and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "THIS IS A WIDE FULL-LENGTH SCENE AND NOT A PORTRAIT: five men are visible "
            "whole, seated, strung out along the frame from left to right with the flat "
            "and the water beyond them. EVERY MAN IS SITTING DOWN on the wet sand — "
            "cross-legged, or on one hip, or on his heels — and not one of them is "
            "standing or hauling. The opened DRAGNET lies spread along the sand in front "
            "of them in a long loose brown and grey heap, its mesh pulled back and its "
            "catch spilled out in a bright silver drift down its length. Hand-woven "
            "reed baskets and shallow fired-clay bowls stand along the line between the "
            "men. Their hands are in the catch, each man working the fish nearest him, "
            "all of their gazes DOWN into the sand at their own feet. The headman — "
            "broad and thick, about fifty-five, short grizzled iron-grey beard, DARK "
            "UMBER-BROWN tunic, DARK BROWN rope sash, DEEP INDIGO head cloth thrown "
            "back over his left shoulder — sits at the RIGHT end of the line in "
            "profile, one huge hand resting on a basket rim. Dry pale reed beds stand "
            "back along the far LEFT; no pale, ivory, beige, buff or sand cloth is on "
            "anyone."
        ),
    },
    {
        "id": "v2-r030-b16", "out": "s16-but-cast-the-bad-away.jpeg",
        "seg": "j48", "window": "56.832-60.045", "wide": False, "jesus": False,
        "locks": ["STRAND", "FISH", "HEADMAN"],
        "narration": "but cast the bad away.",
        "must_show": "a close, unhurried, deliberate two-handed moment — one fish going down into a reed basket and one being laid aside on the sand, done without anger or violence.",
        "must_not_show": _NO_JESUS + _NO_CREAM + "no face turned toward the lens; no throwing, flinging, anger or disgust; no blood, gore or wound; no shingle, no building, no fire; no night; no plastic crate, tray or box; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens close in and angled DOWN over the man's own "
            "shoulder from behind and to his left so his face is not in the picture at "
            "all, shallow depth of field, LONG GOLD LATE-AFTERNOON sun almost level "
            "from the RIGHT laying warm light along wet scales and a long shadow across "
            "the sand, fine film grain. The frame is two enormous scarred brown hands, "
            "thick-knuckled and rope-burned with cracked nails, and the wet ridged sand "
            "and net-cord beneath them — they are the headman's hands and his DARK "
            "UMBER-BROWN sleeve, pushed above the elbow, and the end of his DEEP INDIGO "
            "head cloth hanging down over his left shoulder are visible at the top of "
            "the frame. THE RIGHT HAND is lowering one broad deep flat fish the length "
            "of a forearm, dull silver-olive and wet, gently DOWN into the mouth of a "
            "hand-woven reed basket already half filled with fish, holding it carefully "
            "under the belly. THE LEFT HAND is at the same time laying a second, "
            "clearly spoiled fish — dull, slack, sunken-eyed and grey — flat down onto "
            "the sand to one side, setting it down open-palmed rather than throwing it, "
            "with no anger and no disgust in the gesture. The two actions read at once "
            "and the difference between them is only care and direction. Around the "
            "hands the brown hand-knotted mesh and the ridged wet sand run out of focus "
            "to the edges of the frame. There is nothing bright, coloured, plastic or "
            "manufactured in the picture."
        ),
    },
    # ================= n5 — drawn up, sat down, only then sorting ==============
    {
        "id": "v2-r030-b17", "out": "s17-drag-it-up-onto-the-shore.jpeg",
        "seg": "n5", "window": "60.045-64.705", "wide": True, "jesus": False,
        "locks": ["STRAND", "NET", "CREW"],
        "narration": "When the net is full, the fishermen drag the whole heavy thing up onto the shore,",
        "must_show": "the sheer weight of it — the loaded net now fully out of the water and lying up on the flat, the drag furrow behind it written into the wet sand.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no shingle beach, no cliff, no harbour, no jetty, no quay, no building, no wall and no tree; no fire; no night and no midday overhead sun; " + _GAZE,
        "scene": (
            "One photograph, 28mm lens, deep depth of field, LONG GOLD LATE-AFTERNOON "
            "sun almost level from the RIGHT, very long soft-edged shadows thrown away "
            "to the left, warm raking light picking out every ridge in the wet sand, "
            "fine film grain. THE CAMERA IS LOW ON THE SAND AND WELL BEHIND THE MEN, "
            "SHOOTING ALONG THE DRAG FURROW TOWARD THE WATER PAST THEIR BACKS, so the "
            "nearest figures are seen from directly behind and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE LANDSCAPE SCENE AND NOT A PORTRAIT: the "
            "men are small in the middle distance, visible head to feet, and the strand "
            "and the water fill the rest of the picture. The subject is the DRAGNET, "
            "now fully out of the water and lying up on the flat: an enormous swollen "
            "brown and grey mass of hand-knotted mesh forty feet long, humped and "
            "shapeless, still streaming, silver catch glinting all through it. Running "
            "from it back down the frame to the waterline is the DRAG FURROW — a broad "
            "smooth scar ploughed through the ridged wet sand, water standing in it, "
            "flanked by deep dug heel prints — so the weight of the thing is written "
            "into the ground. Four men in deep indigo, dark umber, dark olive-drab and "
            "russet wool with dark head cloths stand around the near end of it, backs "
            "and profiles to the camera, hands on knees, straightening up and breathing "
            "hard. Beyond them the thin sheet of water runs out flat and gold to a "
            "clean horizon; dry pale reed beds stand back along the LEFT edge with low "
            "bare tawny hills behind. No pale, ivory, beige, buff or sand cloth is on "
            "anyone."
        ),
    },
    {
        "id": "v2-r030-b18", "out": "s18-and-they-sit-down-beside-it.jpeg",
        "seg": "n5", "window": "64.705-67.785", "wide": False, "jesus": False,
        "locks": ["STRAND", "NET", "CREW"],
        "narration": "and they sit down beside it.",
        "must_show": "two fishermen lowering themselves down onto the wet sand beside the beached net, the work stopped, weight coming off their legs.",
        "must_not_show": _NO_JESUS + _NO_CREAM + "no face turned toward the lens; no shingle, no building, no wall, no tree, no fire; no night and no midday overhead sun; nobody hauling or standing over the net; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, a medium view from LOW DOWN ON THE SAND AND "
            "WELL TO THE SIDE of both men, shooting across them at right angles to "
            "their eyelines, shallow depth of field, LONG GOLD LATE-AFTERNOON sun "
            "almost level from the RIGHT, long soft shadows reaching left, warm light "
            "along the tops of shoulders, fine film grain. Two fishermen are caught "
            "mid-movement in the act of SITTING DOWN on the wet ridged sand beside the "
            "beached net — the nearer man already down on one hip with a hand planted "
            "flat in the sand behind him and his legs folding out, the farther man "
            "still half-crouched with both hands on his own knees and his weight "
            "sinking. Both are seen in PROFILE and three-quarter from behind, both "
            "gazes down at the sand in front of them and out through the LEFT EDGE of "
            "the frame; neither face is squared to the camera. They are in DEEP INDIGO "
            "and DARK OLIVE-DRAB coarse wool tunics with dark sashes and dark head "
            "cloths thrown back over their shoulders, barefoot, their shins and "
            "forearms wet and sand-crusted, chests still moving. Sharp along the whole "
            "RIGHT side of the frame lies the swollen brown and grey hand-knotted mesh "
            "of the beached net, huge and close and dripping. Out of focus beyond them "
            "the flat wet strand runs to a thin gold sheet of water. There is no pale, "
            "ivory, beige, buff or sand cloth anywhere in the picture."
        ),
    },
    {
        "id": "v2-r030-b19", "out": "s19-only-then-does-sorting-begin.jpeg",
        "seg": "n5", "window": "67.785-72.173", "wide": True, "jesus": False,
        "locks": ["STRAND", "NET", "CREW", "FISH"],
        "narration": "And only then, once everyone is already gathered in, does any sorting begin.",
        "must_show": "the whole catch lying together, ashore and safe, with the men only now reaching into it — the gathering finished before the sorting starts.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no shingle beach, no cliff, no harbour, no building, no wall and no tree; no fire; no night; no fish being thrown or flung; " + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep depth of field, LONG GOLD LATE-AFTERNOON "
            "sun almost level from the RIGHT, very long soft shadows away to the left, "
            "the wet sand and the whole catch turned warm and bright, fine film grain. "
            "THE CAMERA IS DOWN AT SAND LEVEL AT ONE END OF THE OPENED NET AND SHOOTS "
            "ALONG ITS LENGTH PAST THE SEATED MEN, so they are seen in profile and "
            "three-quarter from behind, ranged away from the camera, and NOT ONE FACE "
            "IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE AND NOT A "
            "PORTRAIT: four seated men are visible whole with the strand and the water "
            "beyond. The near half of the frame, sharp and close, is THE CATCH ITSELF "
            "spilled out along the opened mesh in a long bright drift — broad deep flat "
            "fish the length of a forearm, longer slender fish with trailing barbels, "
            "and packed small silver fish, all wet and dull silver, olive-grey and "
            "brass-brown, lying together in one continuous mass with nothing separated "
            "out of it yet. Seated along the far side of that drift the men have only "
            "just begun: two have their hands into the near edge of the catch, one is "
            "still drawing an empty hand-woven reed basket toward himself, and the "
            "fourth is only turning to reach. Several empty reed baskets and shallow "
            "fired-clay bowls stand upright and unfilled along the sand. The men are in "
            "deep indigo, dark umber, dark olive-drab and russet wool with dark head "
            "cloths; there is no pale, ivory, beige, buff or sand cloth anywhere. "
            "Beyond them the thin sheet of gold water and a clean far horizon."
        ),
    },
    # ======================= n6 — the good into baskets ========================
    {
        "id": "v2-r030-b20", "out": "s20-into-baskets.jpeg",
        "seg": "n6", "window": "72.173-75.113", "wide": False, "jesus": False,
        "locks": ["STRAND", "FISH", "HEADMAN"],
        "narration": "They gather the good fish carefully into baskets,",
        "must_show": "ANCHOR FOR THE HEADMAN — his face large, lit and unobstructed, bent over a reed basket in gold afternoon light, careful and absorbed.",
        "must_not_show": _NO_JESUS + _NO_CREAM + "no second person's face in the frame; no shingle, no building, no wall, no tree, no fire; no night and no midday overhead sun; no plastic crate, tray or box; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, a close three-quarter view of ONE seated man "
            "from his front-right and slightly above, shallow depth of field with the "
            "strand behind him dissolved into warm soft gold, LONG GOLD LATE-AFTERNOON "
            "sun almost level from the RIGHT raking across the side of his face and "
            "picking out every crease in it, fine film grain. THE CAMERA IS DOWN ON THE "
            "SAND TO HIS RIGHT AND SHOOTS ACROSS HIM. HIS HEAD IS TURNED WELL OFF THE "
            "CAMERA AXIS AND BOWED, HIS NOSE POINTED DOWN AT THE LOWER-LEFT CORNER OF "
            "THE FRAME, and his gaze is down into the basket between his knees and out "
            "through that LEFT EDGE — his pupils never come near the lens and he does "
            "not know he is being looked at. He is the headman: about fifty-five, broad "
            "and thick through the chest and shoulders, deeply sun-blackened red-brown "
            "creased skin, a broad flat-planed face with a heavy jaw and a blunt nose "
            "broken once and set crooked, deep vertical creases between the brows, a "
            "fan of white squint lines at the outer corners, a short close-cut grizzled "
            "IRON-GREY beard, thick grey-shot black hair pushed straight back off a "
            "high forehead, small steady dark brown eyes. He sits on his heels with a "
            "hand-woven reed basket between his knees, and his enormous scarred "
            "thick-knuckled hands are lowering one broad silver-olive fish into it with "
            "both palms, unhurried and careful. His expression is absorbed, patient and "
            "gentle — the face of a man handling something he values. He wears a DARK "
            "UMBER-BROWN coarse wool tunic with the sleeves pushed above the elbows, a "
            "DARK BROWN rope sash and a DEEP INDIGO head cloth thrown back over his "
            "left shoulder; nothing on him is pale. No other person appears in the frame."
        ),
    },
    {
        "id": "v2-r030-b21", "out": "s21-not-losing-a-single-one.jpeg",
        "seg": "n6", "window": "75.113-79.991", "wide": False, "jesus": False,
        "locks": ["STRAND", "FISH"],
        "narration": "keeping them, valuing them, not losing a single one.",
        "must_show": "the filled reed baskets standing in a row on the wet sand in gold light, each one packed and cared for — the keeping made visible and countable.",
        "must_not_show": _NO_JESUS + _NO_CREAM + "no person's face; no shingle, no building, no wall, no tree, no fire; no night and no midday overhead sun; no plastic crate, tray, box or bag; no lettering or label; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens down at sand level, shallow depth of field with "
            "the far end of the row going soft, LONG GOLD LATE-AFTERNOON sun almost "
            "level from the RIGHT throwing each basket's long shadow away to the left "
            "across the ridged wet sand, warm light in the weave, fine film grain, no "
            "person's face in the picture. Standing in a row across the frame on the "
            "wet sand are FIVE hand-woven reed baskets, separated from one another by "
            "clear space so each can be seen and counted individually, their split-reed "
            "weave rough and irregular and dark with wet. Each is packed to the rim "
            "with dull silver, olive-grey and brass-brown lake fish laid in neatly "
            "rather than tipped in — broad deep flat fish arranged side by side, "
            "smaller silver fish filling the spaces — wet and heavy and shining in the "
            "low sun. The nearest basket is sharp and close in the bottom-left of the "
            "frame; the others recede in a row toward the upper right, the farthest "
            "soft. Entering from the RIGHT EDGE only, out of focus, are one dark "
            "umber-brown sleeve and one large brown hand still settling a fish into the "
            "second basket; no head, face or eyes appear anywhere in the picture. "
            "Beyond and above the row the flat wet strand runs out to a thin gold sheet "
            "of water and a clean horizon, all of it soft. Nothing plastic, painted, "
            "printed or lettered is anywhere in the frame."
        ),
    },
    # =============== n7 — the ones set aside; then back to the frame ===========
    {
        "id": "v2-r030-b22", "out": "s22-they-set-aside.jpeg",
        "seg": "n7", "window": "79.991-83.751", "wide": False, "jesus": False,
        "locks": ["STRAND", "FISH"],
        "narration": "And the ones that cannot be kept, they set aside.",
        "must_show": "the set-aside fish lying apart on the sand in the last flat cooling light — separated and left, quietly and without violence, no basket for them.",
        "must_not_show": _NO_JESUS + _NO_CREAM + "no person's face; no throwing, flinging, anger or disgust; no blood, gore or wound; no fire close by; no shingle, no building, no wall and no tree; no night-black sky; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens down at sand level looking along the flat, "
            "shallow depth of field, the LONG GOLD LIGHT NOW GONE FLAT AND COOL as the "
            "sun drops — the warmth draining out of it, the shadows lengthened and "
            "grey-blue at the edges, the sky above still pale but the colour going out "
            "of the sand, fine film grain, no person's face in the picture. In the "
            "middle of the frame, sharp, lying directly on the ridged wet sand with NO "
            "basket and NO container of any kind, is a small separate group of set-aside "
            "fish: four or five dull, slack, sunken-eyed grey and dark fish laid out "
            "flat and apart from one another, some of them broken-finned, one lying on "
            "its side with its gill plate open and still. They are laid down neatly, not "
            "flung or heaped, and nothing is damaging them. A clear stretch of empty "
            "sand separates them from the upper-left of the frame, where the row of "
            "filled hand-woven reed baskets stands out of focus and warm — the "
            "separation between the two is the whole subject. Entering from the TOP "
            "EDGE only, out of focus, are the bare heels and the hem of one dark "
            "indigo tunic of a man already turning away; no head, face or eyes appear "
            "anywhere in the picture. Beyond, the thin sheet of water runs out flat and "
            "silver-grey to a clean horizon under a cooling sky."
        ),
    },
    {
        "id": "v2-r030-b23", "out": "s23-how-things-finally-end.jpeg",
        "seg": "n7", "window": "83.751-87.679", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "Jesus said that is a picture of how things finally end.",
        "must_show": "back on the mole — Jesus in three-quarter profile, serious and steady, speaking a hard thing plainly to the men in front of him.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no dusk, no sunset and no golden low sun; no fire, no fish, no net, no basket and no boat in this frame; no tree, no wall and no building near the stone; no anger, no threat and no raised voice; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, a STRICT SIDE-ON PROFILE VIEW of Jesus, shallow "
            "depth of field with the water "
            "behind him dissolved into soft blue and hard white glitter, high BRIGHT "
            "EARLY-AFTERNOON sun almost overhead lighting the top planes of his face "
            "cleanly, short shadow under the brow, fine film grain. THE CAMERA STANDS "
            "OUT ON THE STONE AT A FULL RIGHT ANGLE TO HIS RIGHT SHOULDER AND SHOOTS "
            "STRAIGHT ACROSS HIM, SO ONLY THE RIGHT-HAND SIDE OF HIS FACE IS VISIBLE "
            "AND HIS FAR CHEEK, FAR EYE AND THE FRONT OF HIS FACE ARE HIDDEN FROM THE "
            "CAMERA BY HIS OWN HEAD — a clean silhouette profile of brow, nose, lips, "
            "beard and jaw against the bright water. His head is NOT turned toward the "
            "camera at any point and his single visible eye looks straight ahead along "
            "his own profile line into the face of a man seated below and "
            "left of him, and clean out through that LEFT EDGE — his pupils never come "
            "near the lens and no part of this is a front-facing portrait. He is "
            "seated on a flat-topped grey-brown boulder in his one "
            "plain undyed off-white cream wool robe, the only pale garment in the "
            "picture, leaning slightly forward with his forearms on his knees and both "
            "hands loosely together. His expression is grave, steady and kind — this is "
            "a hard thing said plainly and without anger, not a warning shouted; there "
            "is no threat in his face. In the bottom-left corner, out of focus and "
            "dark, is one listening man's shoulder and dark indigo head cloth, a solid "
            "dark saturated mass, and there is no pale, ivory, beige, buff or sand "
            "shape anywhere else in the frame. Sharp beneath him the dry-laid rounded "
            "field boulders of the mole, pale grit and salt-bleached weed in the gaps."
        ),
    },
    # ============ j2 — Matthew 13:49, grave dusk, no angels painted ============
    {
        "id": "v2-r030-b24", "out": "s24-the-end-of-the-world.jpeg",
        "seg": "j2", "window": "87.679-90.419", "wide": False, "jesus": False,
        "locks": ["STRAND", "NET"],
        "narration": "So shall it be at the end of the world:",
        "must_show": "the strand at the very end of the day — the emptied net lying dark on the sand, the light almost gone, everything finished.",
        "must_not_show": _NO_JESUS + "no angel, no wing, no figure of light, no heaven, no cloud of glory and no vision; no fire close by; no person at all in this frame; no shingle, no building, no wall and no tree; no lamp; " + _NO_MODERN_NET + _GAZE,
        "scene": (
            "One photograph, 35mm lens down at sand level, deep depth of field, GRAVE "
            "BLUE DUSK — the sun gone, a last cold band of dull orange low along the "
            "horizon and everything above it deepening to slate blue, the wet sand "
            "holding a thin sheen of that dying light, the air still, fine film grain. "
            "THERE IS NO PERSON ANYWHERE IN THIS PICTURE. Lying across the middle "
            "distance in a long dark humped line is the emptied DRAGNET — the brown and "
            "grey hand-knotted mesh now slack, spread out and abandoned along the "
            "strand, its bare wood and cork-bark floats scattered along its edge, its "
            "flat drilled stone weights half sunk in the mud, all of it gone almost "
            "black in the failing light with only the wet cord picking up a faint "
            "silver line along its top. In front of it the ridged wet sand runs toward "
            "the camera, its ripples raking hard across the frame, empty of everything. "
            "Behind it the thin sheet of water lies flat and steel-grey out to a clean "
            "far horizon under the cold band of orange. Dry pale reed beds stand back "
            "in a dark broken wall along the LEFT edge with low bare tawny hills behind "
            "them, almost silhouetted. Nothing is burning and nothing is lit."
        ),
    },
    {
        "id": "v2-r030-b25", "out": "s25-the-angels-shall-come-forth.jpeg",
        "seg": "j2", "window": "90.419-92.519", "wide": False, "jesus": False,
        "locks": ["STRAND", "FISH"],
        "narration": "the angels shall come forth,",
        "must_show": "the two groups on the darkening sand seen together and apart — the covered filled baskets on one side, the set-aside fish on the other, and nobody's hands anywhere near either.",
        "must_not_show": _NO_JESUS + "no angel, no wing, no figure of light, no heaven, no vision and no shining being; no person at all in this frame; no fire close by; no shingle, no building, no wall and no tree; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens down at sand level looking straight along the "
            "flat, moderate depth of field, GRAVE BLUE DUSK with the sun gone, a last "
            "cold band of dull orange low on the horizon and slate-blue air above, the "
            "wet ridged sand holding a thin cold sheen, fine film grain. THERE IS NO "
            "PERSON, NO HAND AND NO ARM ANYWHERE IN THIS PICTURE. The frame holds two "
            "things and a wide empty stretch of sand between them, and the emptiness "
            "between them is the subject. On the LEFT, sharp, stand three hand-woven "
            "reed baskets packed to the rim with dull silver and olive-grey lake fish, "
            "each with a square of coarse dark cloth laid over half its mouth as if "
            "just covered, upright and orderly and cared for. On the RIGHT, well "
            "separated and slightly further off, the set-aside fish lie flat and apart "
            "directly on the bare sand with no container of any kind — dull, slack, "
            "sunken-eyed and grey, four or five of them, laid down and left. Between "
            "the two runs a clean unbroken width of ridged wet sand with a single set "
            "of already-filling bare footprints crossing it and going away out of the "
            "TOP of the frame. Beyond, the flat steel-grey water and a clean far "
            "horizon under the dying orange band. Nothing is burning and nothing is lit."
        ),
    },
    {
        "id": "v2-r030-b26", "out": "s26-sever-the-wicked-from-among-the-just.jpeg",
        "seg": "j2", "window": "92.519-96.449", "wide": True, "jesus": False,
        "locks": ["STRAND", "CREW", "FISH"],
        "narration": "and sever the wicked from among the just",
        "must_show": "the two loads leaving in opposite directions across the dusk strand — the covered baskets carried up toward the reeds, the set-aside catch carried the other way toward a small distant fire.",
        "must_not_show": _NO_JESUS + _NO_CREAM + "no angel, no wing, no figure of light and no vision; no close flames, no burning fish, no person or creature in fire and no suffering; no shingle, no building and no tree; " + _GAZE,
        "scene": (
            "One photograph, 28mm lens, deep depth of field, GRAVE BLUE DUSK with the "
            "sun gone, a cold band of dull orange low along the horizon, slate-blue air, "
            "the wet sand holding a thin cold sheen, fine film grain. THE CAMERA STANDS "
            "HIGH UP THE STRAND WELL BEHIND BOTH GROUPS OF MEN AND SHOOTS DOWN ACROSS "
            "THE FLAT PAST THEM, so every figure is seen from behind or in hard side "
            "profile, walking away from the camera, and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS and no face is legible at all. THIS IS A WIDE LANDSCAPE SCENE AND "
            "NOT A PORTRAIT: the figures are small and whole, head to bare feet, and "
            "the strand fills the picture. Two parties are walking APART, and the "
            "widening gap between them is the subject. Going away to the LEFT, up "
            "toward the dark broken wall of dry reed beds, two men carry the packed "
            "hand-woven reed baskets of good fish on their shoulders, cloth squares laid "
            "over the tops. Going away to the RIGHT, far down the open flat, two other "
            "men carry the set-aside catch slung in a coarse dark cloth between them, "
            "walking toward a SMALL DISTANT FIRE burning far off near the waterline at "
            "the very edge of the picture — a low orange point with a thin pale line of "
            "smoke leaning off it, tiny, far away, its flames not readable at this "
            "distance. Nothing is being burned in view and nothing is being thrown. All "
            "four men are in deep indigo, dark umber, dark olive-drab and russet wool "
            "with dark head cloths; no pale, ivory, beige, buff or sand cloth is on "
            "anyone. Their footprints run back toward the camera across the ridged sand."
        ),
    },
    # ============ j50 — Matthew 13:50, restrained; the distant fire ============
    {
        "id": "v2-r030-b27", "out": "s27-the-furnace-of-fire.jpeg",
        "seg": "j50", "window": "96.449-100.129", "wide": False, "jesus": False,
        "locks": ["STRAND"],
        "narration": "And shall cast them into the furnace of fire:",
        "must_show": "the small distant shore fire alone at the far end of the dark strand — grave and remote, a point of orange and a column of smoke, seen from a long way off.",
        "must_not_show": _NO_JESUS + "no close flames, no fire filling the frame, no burning fish, animal, creature or person, no body, no face and no figure in or near the fire; no suffering, no torment, no screaming and no pain; no demon, devil, horns, skull or bone; no angel and no wing; no shingle, no building and no tree; " + _GAZE,
        "scene": (
            "One photograph, 135mm lens compressing a very long distance, shallow depth "
            "of field, GRAVE BLUE DUSK almost gone to night — the last cold orange band "
            "reduced to a thin line on the horizon, the air deep slate blue, the wet "
            "sand a dark sheen, fine film grain. THERE IS NO PERSON, NO ANIMAL AND NO "
            "CREATURE ANYWHERE IN THIS PICTURE. The frame is mostly empty dark strand "
            "and dark water. Far away at the very end of the flat, SMALL in the frame "
            "and no taller than a thumbnail, burns one low shore fire of driftwood and "
            "dry reed: a compact dull orange core, its individual flames not resolvable "
            "at this distance, throwing a short soft orange smear across the wet sand "
            "in front of it and a faint orange line out along the water. Rising from it "
            "and leaning slowly away to the LEFT is a thin pale column of smoke that "
            "spreads and dissolves into the blue air, and this smoke — not the fire — "
            "is the largest thing in the picture. The near foreground, sharp and close "
            "along the bottom, is bare ridged wet sand and two dark rounded stones, "
            "cold and untouched by the light. Nothing else in the frame is lit. The "
            "mood is grave and quiet and final, never violent and never lurid."
        ),
    },
    {
        "id": "v2-r030-b28", "out": "s28-wailing-and-gnashing.jpeg",
        "seg": "j50", "window": "100.129-104.096", "wide": False, "jesus": False,
        "locks": ["STRAND", "NET"],
        "narration": "there shall be wailing and gnashing of teeth.",
        "must_show": "the emptied strand at last light with the sorted places both gone — bare sand where the set-aside fish lay, the net dark and slack, absolute stillness and loss carried by emptiness alone.",
        "must_not_show": _NO_JESUS + "no person, face, body or figure of any kind; no fire close by, no flames and nothing burning in view; no suffering, torment, screaming, pain, demon, devil, skull or bone; no angel and no wing; no shingle, no building and no tree; " + _NO_MODERN_NET + _GAZE,
        "scene": (
            "One photograph, 35mm lens down at sand level, deep depth of field, LAST "
            "LIGHT gone almost to night — the horizon band reduced to a cold thin ember "
            "line, the air deep slate blue, everything nearly monochrome, fine film "
            "grain. THERE IS NO PERSON, FACE, BODY OR FIGURE ANYWHERE IN THIS PICTURE. "
            "Sharp and close across the whole bottom of the frame is the bare patch of "
            "ridged wet sand where the set-aside fish had been laid out — now empty, "
            "holding only their shallow pressed outlines and a few scattered scales "
            "catching the last of the light, and the dragged marks of the cloth that "
            "took them away leading off toward the RIGHT EDGE. Behind it, running across "
            "the middle distance, the emptied DRAGNET lies slack and abandoned, a long "
            "low black humped line of hand-knotted mesh with its bare wood floats and "
            "flat stone weights just readable against the sand. Far off at the very edge "
            "of the picture the small shore fire is now only a dull dying orange point "
            "with a thin pale thread of smoke standing above it, tiny and remote and not "
            "the subject. Beyond, the flat water lies dead calm and steel-dark to a "
            "clean far horizon. Nothing moves. The whole picture carries loss by "
            "emptiness alone."
        ),
    },
    # ============ n8 — whose job it is; the strand, then the frame =============
    {
        "id": "v2-r030-b29", "out": "s29-a-real-end-a-real-sorting.jpeg",
        "seg": "n8", "window": "104.096-107.136", "wide": False, "jesus": False,
        "locks": ["STRAND", "FISH"],
        "narration": "There is a real end, and a real sorting.",
        "must_show": "the covered baskets standing alone on the dark strand at last light — the keeping is real, and it is over and settled, with no hand on it.",
        "must_not_show": _NO_JESUS + "no person, hand, arm or face; no fire close by; no shingle, no building, no wall and no tree; no plastic crate, tray, box or bag; no lettering or label; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens down at sand level, shallow depth of field, LAST "
            "LIGHT gone almost to night — a cold ember line on the horizon, deep "
            "slate-blue air, the wet sand a dark sheen, fine film grain. THERE IS NO "
            "PERSON, HAND, ARM OR FACE ANYWHERE IN THIS PICTURE. Standing sharp and "
            "close in the near frame, up above the waterline on dry darker sand, are "
            "FOUR hand-woven reed baskets, clearly separated from one another so each "
            "can be counted, packed to the rim with dull silver and olive-grey lake "
            "fish and each with a square of coarse dark cloth laid over its mouth and "
            "tucked down at the sides — finished, closed, put by. The rough split-reed "
            "weave and the coarse dark cloth are legible in the last of the light. "
            "Their four shadows have gone and only a faint cold sheen on the sand marks "
            "where they stand. Behind them, running away out of focus, is the long "
            "black humped line of the emptied dragnet and the flat steel-dark water to "
            "a clean far horizon under the ember line. Far off at the very edge, a dull "
            "dying orange point of fire and a thin thread of smoke, small and remote. "
            "Nothing plastic, painted, printed or lettered is anywhere in the frame."
        ),
    },
    {
        "id": "v2-r030-b30", "out": "s30-the-angels-do-it.jpeg",
        "seg": "n8", "window": "107.136-111.616", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "But notice whose job it is. The angels do it. God does it.",
        "must_show": "Jesus on the mole in the bright afternoon, one hand turned up and away from himself as he names whose work it is — the gesture handing it off, not claiming it.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no angel, no wing, no figure of light, no heaven and no vision; no night, no lamp, no dusk and no sunset; no fire, no fish, no net and no boat in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, a medium three-quarter view of Jesus from his "
            "left and slightly below, shallow depth of field with the water behind him "
            "soft blue and hard white glitter, high BRIGHT EARLY-AFTERNOON sun almost "
            "overhead, hard clean light, fine film grain. THE CAMERA STANDS OUT ON THE "
            "STONE TO HIS LEFT AND SHOOTS ACROSS HIM, so his head is turned well off "
            "the camera axis with his nose pointed toward the UPPER RIGHT of the frame "
            "and his gaze travelling up and away past his own lifted hand and out "
            "through the RIGHT EDGE — his pupils never come near the lens. He sits on a "
            "flat-topped grey-brown boulder in his one plain undyed off-white cream "
            "wool robe, the only pale garment in the picture. His near hand is lifted "
            "open at about shoulder height with the palm turned UP AND AWAY from his own "
            "body, the fingers loose — a gesture that hands something over to someone "
            "else rather than claiming it, plainly directed away from himself and away "
            "from the men in front of him. His expression is calm and matter-of-fact. "
            "Above and beyond his hand there is only open sky and the far horizon of "
            "the lake, empty — nothing is depicted there. In the bottom-left corner, "
            "out of focus and dark, one seated shoulder and dark indigo head cloth, a "
            "solid dark saturated mass; no pale, ivory, beige, buff or sand shape "
            "anywhere else in the frame. Sharp below him the dry-laid rounded field "
            "boulders of the mole."
        ),
    },
    {
        "id": "v2-r030-b31", "out": "s31-never-handed-to-us.jpeg",
        "seg": "n8", "window": "111.616-115.780", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "At the very end, it was never handed to us to do.",
        "must_show": "the wide frame on the mole — Jesus and the seated circle small on the stone with the open water all round, the listening men's empty open hands resting on their knees.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no angel, no wing and no vision; no night, no lamp, no dusk and no sunset; no fire, no fish, no net, no basket and no boat in this frame; no tree, no wall, no roof and no building on the stone; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 28mm lens, deep depth of field, high BRIGHT "
            "EARLY-AFTERNOON sun almost overhead and a little behind the camera, hard "
            "clean light, short dark shadows pooled directly under the seated men, the "
            "lake broken into hard white glitter on both sides, fine film grain. THE "
            "CAMERA STANDS FAR BACK ALONG THE MOLE AND WELL TO ONE SIDE OF THE WHOLE "
            "GROUP AND SHOOTS ACROSS THEM AT RIGHT ANGLES TO EVERY EYELINE, so the "
            "near men are seen from behind and in profile and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND NOT A "
            "PORTRAIT: the whole seated circle sits SMALL in the lower third of the "
            "picture, everyone visible head to feet, with the open lake and the clean "
            "far horizon filling the rest. The near foreground across the bottom is the "
            "dry-laid rounded grey-brown field boulders of the mole, sharp and close, "
            "pale grit and salt-bleached weed in the gaps, with nobody between the "
            "camera and the group. Seated on and around the flat-topped stones are "
            "Jesus and eight or nine disciples in DEEP INDIGO, DARK UMBER, DARK "
            "OLIVE-DRAB and RUSSET-RED wool with dark head cloths and no pale scarf, "
            "stole or shawl anywhere among them, all of them turned in toward Jesus in "
            "profile or three-quarter from behind. Several of them sit with their own "
            "hands resting open and empty, palms up, on their knees. Jesus sits among "
            "them on a boulder in his one plain undyed off-white cream wool robe, seen "
            "from the side, leaning forward with one hand open — the ONLY pale thing in "
            "the whole picture. Beyond and below the stone the water runs out flat and "
            "glittering on both sides to a clean far horizon, with the flat roofs of "
            "the little harbour town small and low at the far end of the mole."
        ),
    },
    # ================= n9 — you do not have to do the sorting ==================
    {
        "id": "v2-r030-b32", "out": "s32-what-the-story-leaves-you-with.jpeg",
        "seg": "n9", "window": "115.780-118.760", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "So here is what the little story leaves you with.",
        "must_show": "Jesus on the mole, quiet and finished with the telling, looking steadily into the face of one of the men in front of him.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no dusk and no sunset; no fire, no fish, no net, no basket and no boat in this frame; no tree, no wall and no building near the stone; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, a close three-quarter view of Jesus from his "
            "left and level with him, shallow depth of field with the water behind him "
            "dissolved to soft blue and hard white glitter, high BRIGHT EARLY-AFTERNOON "
            "sun almost overhead, clean light on the top planes of his face, fine film "
            "grain. THE CAMERA STANDS OUT ON THE STONE TO HIS LEFT AND SHOOTS ACROSS "
            "HIM, so his head is turned well off the camera axis with his nose pointed "
            "toward the LOWER RIGHT of the frame, and his gaze goes down and level into "
            "the upturned face of a man seated on the stone below him and out through "
            "that RIGHT EDGE — his pupils never come near the lens. He sits on a "
            "flat-topped grey-brown boulder in his one plain undyed off-white cream "
            "wool robe, the only pale garment in the picture, his shoulders relaxed and "
            "his hands come to rest loosely in his lap, the telling finished. His "
            "expression is quiet, warm and attentive — waiting for it to land rather "
            "than pressing it. In the bottom-right of the frame, out of focus, the back "
            "of the listening man's head and his dark umber shoulder and dark head "
            "cloth rise into the picture as a solid dark saturated mass; there is no "
            "pale, ivory, beige, buff or sand shape anywhere else in the frame. Sharp "
            "beneath him the dry-laid rounded field boulders of the mole with pale grit "
            "and salt-bleached weed in the gaps."
        ),
    },
    {
        "id": "v2-r030-b33", "out": "s33-not-yours-to-decide.jpeg",
        "seg": "n9", "window": "118.760-122.680", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "You do not have to spend your life deciding who belongs and who does not.",
        "must_show": "the listening men on the mole with the weight visibly going off them — shoulders dropping, open empty hands, one man exhaling as it lands.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no dusk and no sunset; no fire, no fish, no net, no basket and no boat in this frame; no tree, no wall and no building on the stone; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 35mm lens, high BRIGHT EARLY-AFTERNOON sun almost overhead "
            "and a little behind the camera, hard clean light, short dark shadows "
            "pooled under the men, the lake in hard white glitter beyond, fine film "
            "grain. THE CAMERA IS DOWN LOW ON THE STONE COMPLETELY SIDE-ON TO THE ROW "
            "OF SEATED MEN AND SHOOTS ALONG IT AT RIGHT ANGLES TO EVERY EYELINE, so "
            "every man is seen in hard profile or three-quarter from behind, all their "
            "gazes travelling in the same direction across the frame toward Jesus and "
            "out through the LEFT EDGE, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "THIS IS A WIDE FULL-LENGTH SCENE AND NOT A PORTRAIT: four disciples are "
            "visible whole, head to feet, seated along the boulders with the water "
            "behind them, and Jesus is present only as an out-of-focus cream shoulder "
            "and forearm entering the frame at the far LEFT EDGE, small and partial. "
            "THE SUBJECT IS THE MEN AND WHAT IS LEAVING THEM: the nearest sits with his "
            "shoulders visibly dropped and both hands fallen open and empty, palms up, "
            "on his crossed knees; the next has let his head tip forward and is "
            "breathing out, his jaw loosened; the third has unclenched one fist and is "
            "looking down at his own open palm; the fourth simply sits back on his "
            "hands. Nobody is arguing and nobody is tense. They are in DEEP INDIGO, "
            "DARK UMBER, DARK OLIVE-DRAB and RUSSET-RED wool with dark head cloths and "
            "no pale scarf, stole or shawl among them. Sharp under them the dry-laid "
            "rounded field boulders of the mole, pale grit and weed in the gaps; beyond "
            "them the open water to a clean far horizon."
        ),
    },
    {
        "id": "v2-r030-b34", "out": "s34-not-your-net.jpeg",
        "seg": "n9", "window": "122.680-126.655", "wide": False, "jesus": False,
        "locks": ["STRAND", "NET"],
        "narration": "That is not your net, and it is not your sorting.",
        "must_show": "the net itself lying alone on the empty dusk strand with no person anywhere near it — it plainly belongs to nobody in the frame.",
        "must_not_show": _NO_JESUS + "no person, hand, arm, face or figure of any kind; no fish being sorted; no fire close by; no shingle, no building, no wall and no tree; " + _NO_MODERN_NET + _GAZE,
        "scene": (
            "One photograph, 35mm lens down at sand level and close to the mesh, "
            "shallow depth of field with the far end of the net dissolving, GRAVE BLUE "
            "DUSK — the sun gone, a cold thin band of dull orange on the horizon, "
            "slate-blue air, the wet sand holding a faint cold sheen, fine film grain. "
            "THERE IS NO PERSON, HAND, ARM, FACE OR FIGURE ANYWHERE IN THIS PICTURE and "
            "nobody is anywhere near the net. Filling the near frame, sharp and very "
            "close, is the emptied DRAGNET: thick brown, grey and tar-darkened "
            "hand-knotted flax cord in a coarse diamond mesh, furred and slightly "
            "frayed, one repair of newer lighter cord knotted in, lying slack in loose "
            "folds directly on the ridged wet sand with a few dull scales caught in it "
            "and a thin line of cold light along the top of each wet strand. Its bare "
            "wood and cork-bark floats lie scattered along one edge and its flat "
            "drilled grey stone weights are half sunk in the mud along the other. The "
            "mesh runs away from the camera and out of focus into the blue distance, "
            "enormous and untended, and the strand around it in every direction is bare "
            "empty sand with no basket, no fish and no footprint near it. Beyond, the "
            "flat steel-grey water to a clean far horizon under the dying orange band."
        ),
    },
    # ============ n10 — the net was cast for you; back to the morning ==========
    {
        "id": "v2-r030-b35", "out": "s35-cast-for-the-whole-sea.jpeg",
        "seg": "n10", "window": "126.655-130.155", "wide": True, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREW"],
        "narration": "Your part is simply this: the net was cast for the whole sea,",
        "must_show": "back to the bright early morning water — the float-line seen from high above closing an enormous circle on the surface, the scale of the cast made plain.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no night, no dusk, no storm and no dark sky; no beach, no jetty, no strand, no reed bed and no building; no painted or white hull, no engine; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens from HIGH ABOVE AND BEHIND the near boat looking "
            "steeply down and out across the water, very deep depth of field, clear "
            "EARLY MORNING with the sun low off the LEFT laying a long broken sparkle "
            "path across the surface, warm-white raking light, fine film grain. THE "
            "CAMERA IS HIGH AND WELL BEHIND EVERY MAN IN THE PICTURE, so the two "
            "figures in the near boat are seen from directly above and behind as dark "
            "backs and the tops of dark head cloths, and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS and no face is legible. THIS IS A WIDE OPEN-WATER LANDSCAPE AND "
            "NOT A PORTRAIT: the boats are small, the water is the subject and fills "
            "almost the whole frame. From the near boat in the bottom corner the "
            "float-line of the dragnet sweeps out in an ENORMOUS shallow CIRCLE of "
            "irregular bare wood and cork-bark floats riding the bright surface, curving "
            "right across the middle of the picture and back to the second boat lying "
            "small and far off, so the whole ring and the vast stretch of water it "
            "encloses are visible at once. The enclosed water is a slightly darker "
            "green than the water outside it and it is enormous — the ring takes in far "
            "more sea than either boat could ever hold. The men are in deep indigo, "
            "dark umber and dark olive-drab wool with dark head cloths and there is no "
            "pale, ivory, beige, buff or sand cloth anywhere in the picture. Along the "
            "far LEFT edge the land is only a thin hazy line of low tawny hills; "
            "everywhere else is open water to a clean horizon."
        ),
    },
    {
        "id": "v2-r030-b36", "out": "s36-and-it-was-cast-for-you.jpeg",
        "seg": "n10", "window": "130.155-134.115", "wide": False, "jesus": False,
        "locks": ["NET"],
        "narration": "and it was cast for you. The gathering came first.",
        "must_show": "the mesh coming toward the camera from below the surface, wide and open and unhurried — the net arriving for whoever is here, seen from inside the water it is sweeping.",
        "must_not_show": _NO_JESUS + _NO_MODERN_NET + "no person, hand, arm or face; no fish trapped or struggling in distress; no coral, reef or tropical colour; no night; no boat hull filling the frame; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens HELD UNDER THE SURFACE OF THE WATER looking "
            "back up and out, so the top quarter of the frame is the bright rippled "
            "underside of the surface with the early morning sun burning through it "
            "from the LEFT in long moving shafts, and everything below is clear "
            "green-blue water, fine film grain. THERE IS NO PERSON, HAND, ARM OR FACE "
            "ANYWHERE IN THIS PICTURE. Coming toward the camera out of the soft blue "
            "distance is the DRAGNET, seen head-on: a wide curtain of brown, grey and "
            "tar-darkened hand-knotted diamond mesh hanging from its float-line at the "
            "surface down into the dark below, its bare wood and cork-bark floats "
            "visible along the top pushing a small wake, its flat drilled grey stone "
            "weights swinging along the bottom edge, the whole wall of it sagging in "
            "slow folds and moving unhurriedly toward the viewer with its openings wide "
            "and clear. Sunlight from the surface strikes the wet cord in short bright "
            "dashes. The mesh spreads far wider than the frame can hold, running out "
            "past both edges of the picture, and it is coming on gently, not sweeping "
            "or snapping. Small drifting particles hang in the green light. No fish is "
            "caught in it and nothing is struggling."
        ),
    },
    {
        "id": "v2-r030-b37", "out": "s37-grace-reached-out-wide-enough.jpeg",
        "seg": "n10", "window": "134.115-137.529", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "Grace reached out wide enough to catch you up in it.",
        "must_show": "Jesus on the mole with both arms opening wide and low over the water — the reach itself, warm and unhurried, the water filling the space between his hands.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no cross, no crucifix and no crucifixion pose; no night, no lamp, no dusk and no sunset; no fire, no fish, no net and no boat in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, a medium view of Jesus from his RIGHT SIDE and "
            "slightly below, shallow depth of field with the water behind him soft blue "
            "and hard white glitter, high BRIGHT EARLY-AFTERNOON sun almost overhead, "
            "hard clean light, fine film grain. THE CAMERA STANDS OUT ON THE STONE WELL "
            "TO HIS RIGHT AND SHOOTS ACROSS HIM AT RIGHT ANGLES TO HIS EYELINE, so he "
            "is seen in three-quarter profile with his head turned well off the camera "
            "axis, his nose pointed toward the LEFT EDGE of the frame and his gaze "
            "travelling level out across the water and clean out through that LEFT EDGE "
            "— his pupils never come near the lens. He is seated forward on a "
            "flat-topped grey-brown boulder in his one plain undyed off-white cream "
            "wool robe, the only pale garment in the picture. BOTH ARMS ARE OPENING "
            "WIDE AND LOW, held out at little more than waist height with the elbows "
            "soft and both palms turned up and open — a gathering-in gesture, unhurried "
            "and warm, the arms low and never lifted level with the shoulders and never "
            "held straight out to the sides. His expression is glad and open. Between "
            "and beyond his two hands the open lake runs flat and glittering to a clean "
            "far horizon and fills the space they enclose. In the near bottom-left "
            "corner, out of focus and dark, one seated shoulder and dark indigo head "
            "cloth, a solid dark saturated mass; no pale, ivory, beige, buff or sand "
            "shape anywhere else in the frame. Sharp beneath him the dry-laid rounded "
            "field boulders of the mole."
        ),
    },
    # ================== n11 — the whole ocean of us; the close ==================
    {
        "id": "v2-r030-b38", "out": "s38-that-is-how-good-he-is.jpeg",
        "seg": "n11", "window": "137.529-139.729", "wide": True, "jesus": False,
        "locks": ["DEEPWATER", "NET", "CREW"],
        "narration": "That is how good he is.",
        "must_show": "the widest possible morning view — the whole lake, the two small boats and the thread of the float-line lost in the size of the water.",
        "must_not_show": _NO_JESUS + _NO_CREAM + _NO_MODERN_NET + "no night, no dusk, no storm and no dark sky; no beach, no jetty, no strand and no building; no painted or white hull, no engine; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, very deep depth of field, clear EARLY MORNING "
            "with the sun low off the LEFT and a long broken sparkle path lying right "
            "across the water, warm-white light, a wide clean sky going from warm pale "
            "gold at the horizon to soft blue above, fine film grain. THE CAMERA IS FAR "
            "OUT ON THE WATER AND WELL BEHIND BOTH BOATS AND SHOOTS PAST THEM, so the "
            "few figures aboard are tiny dark shapes seen from behind or side-on, NOT "
            "ONE FACE IS TURNED TOWARD THE LENS and no face is legible at all. THIS IS "
            "A WIDE OPEN-WATER LANDSCAPE AND NOT A PORTRAIT: the two open working "
            "boats of hewn unpainted grey-brown planks sit VERY SMALL and low in the "
            "bottom third of the frame, and the water and sky take everything else. "
            "Strung faintly between them and away across the surface is the float-line "
            "of the dragnet, reduced by distance to a thin broken thread of bare wood "
            "and cork-bark floats on the bright water. In every direction the lake runs "
            "unbroken to a clean far horizon; along the far LEFT edge the land is only "
            "a thin hazy line of low tawny hills. The picture is mostly water and light "
            "and the boats are almost lost in it. There is no pale, ivory, beige, buff "
            "or sand cloth anywhere in the picture, and no object in the frame is "
            "painted, moulded or manufactured."
        ),
    },
    {
        "id": "v2-r030-b39", "out": "s39-the-whole-ocean-of-us.jpeg",
        "seg": "n11", "window": "139.729-143.329", "wide": False, "jesus": False,
        "locks": ["NET", "FISH"],
        "narration": "He threw the net over the whole ocean of us, of every kind,",
        "must_show": "the loaded mesh breaking the surface in the morning sun, teeming and mixed — every kind together, alive and safe and coming up.",
        "must_not_show": _NO_JESUS + _NO_MODERN_NET + "no tropical, reef or brightly coloured fish, no shark, ray, eel, octopus, crab or shellfish; no face turned toward the lens; no night, no dusk; no fish dead, injured, bleeding or crushed; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens close in and angled slightly down at the water's "
            "edge beside the boat, shallow depth of field with the far water dissolved "
            "to bright sparkle, clear EARLY MORNING with the sun low off the LEFT "
            "throwing hard warm-white highlights along every wet surface, a fast "
            "shutter freezing flung droplets in the air, fine film grain. Filling the "
            "middle of the frame and BREAKING THE SURFACE from below is the loaded "
            "DRAGNET — a great bulging shoulder of brown, grey and tar-darkened "
            "hand-knotted diamond mesh rising out of the blue-green water, water "
            "sheeting and pouring off it in bright ropes, its bare wood and cork-bark "
            "floats riding up along its top edge. Packed inside and pressed against the "
            "cord is a teeming, visibly MIXED catch — broad deep flat fish the length "
            "of a forearm with blunt heads and faint dark bars, longer slender fish "
            "with smooth heads and trailing barbels, and drifts of small slim silver "
            "fish the length of a finger — all of them wet, slick and alive, dull "
            "silver, olive-grey, brass-brown and greenish black, tails kicking and "
            "blurred, gills red and working, none of them injured. Entering from the "
            "TOP-RIGHT EDGE only, out of focus, is one dark olive-drab sleeve and one "
            "brown hand on the head-rope; no head, face or eyes appear anywhere in the "
            "picture. Beyond, the bright morning water and the long sparkle path run "
            "out of focus to the edges."
        ),
    },
    {
        "id": "v2-r030-b40", "out": "s40-not-one-soul-missed.jpeg",
        "seg": "n11", "window": "143.329-147.672", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOLE", "DISCIPLES"],
        "narration": "so that not one soul who wanted to be found would be missed.",
        "must_show": "the wide closing photograph — Jesus and his circle small together on the boulder mole with the open water running out all round them to a clean far horizon.",
        "must_not_show": "no halo, no glow, no rim-light and no light coming off Jesus; no night, no lamp, no dusk and no sunset; no fire, no fish, no net, no basket and no boat in this frame; no tree, no canopy, no wall, no roof and no building on the stone; " + _NO_CREAM + "not one face turned toward the lens.",
        "scene": (
            "One photograph, 24mm lens, very deep depth of field, high BRIGHT "
            "EARLY-AFTERNOON sun almost overhead and a little behind the camera, hard "
            "clean light, short dark shadows pooled directly under the seated men, the "
            "whole lake broken into hard white glitter on both sides, fine film grain. "
            "THE CAMERA STANDS FAR BACK ALONG THE MOLE AND WELL TO ONE SIDE OF THE "
            "WHOLE GROUP AND SHOOTS ACROSS THEM AT RIGHT ANGLES TO EVERY EYELINE, so "
            "the near men are seen from behind and in profile and NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. THIS IS A WIDE LANDSCAPE SCENE AND NOT A "
            "PORTRAIT: the whole seated circle is small in the lower third of the "
            "frame, everyone visible head to feet, and the open water and sky fill the "
            "rest of the picture. The near foreground across the bottom is the "
            "dry-laid rounded grey-brown field boulders of the breakwater, sharp and "
            "close, pale grit and salt-bleached weed in the gaps, with nobody between "
            "the camera and the group. Seated together on and around the flat-topped "
            "stones in the middle distance are Jesus and eight or nine of his "
            "disciples, the men low on the boulders in DEEP INDIGO, DARK UMBER, DARK "
            "OLIVE-DRAB and RUSSET-RED wool with dark head cloths and no pale scarf, "
            "stole or shawl anywhere among them, all of them turned in toward Jesus in "
            "profile or three-quarter from behind. Jesus sits among them on a boulder "
            "in his one plain undyed off-white cream wool robe, seen from the side, "
            "leaning slightly forward with one hand open — the ONLY pale thing in the "
            "whole picture. The water runs away on THREE sides of the stone, flat and "
            "glittering, out to a clean far horizon, with the low flat roofs of the "
            "little harbour town small and far off at the landward end of the mole and "
            "bare tawny hills behind them."
        ),
    },
]
