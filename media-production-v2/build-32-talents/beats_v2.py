#!/usr/bin/env python3
"""V2 beat map — row 32, build-32-talents (Matthew 25:14-30). REALISTIC V2.

THE INHERITED SCAFFOLD WAS DISCARDED. It proposed 25 pictures at 5.8 s each,
far outside the wave's measured 3.1-4.9 s band, and it kept V1's Jerusalem
skyline in the OLIVET lock — the exact object row 31 had to DELETE after the
model returned the modern tourist photograph (Al-Aqsa dome, minaret, Ottoman
crenellations) twice in a row. Jerusalem is deleted here before the first paid
image rather than after.

WHAT V1 ACTUALLY DID (verified against the artefact, not the prose):
  SEVEN stills for 157.3 s, and two of them carry the whole video.
    * `s1-entrusting.jpeg` covers j14 + n1 + n2 — 0.28 s to 32.05 s, THIRTY-ONE
      AND A HALF SECONDS on ONE picture, containing the opening red-letter verse
      (25:14) and the entire setup.
    * `s7-buried-returned.jpeg` covers n8 + j24 + j2 + n9 — 88.12 s to 128.04 s,
      FORTY SECONDS on ONE picture, containing BOTH of the parable's closing
      red-letter verses (25:24 and 25:25) AND the retelling the whole story
      turns on.
    * `s6-well-done.jpeg` covers j1 + n7 and is then REUSED for n10 — so the
      NINETEEN-SECOND closing application, the reason the video exists, had no
      picture of its own.
  V2 gives every one of the 14 spoken segments its own pictures: 46 pictures over
  149.62 s = 3.25 s/picture.

AUDIO: LOCKED, never re-voiced. The V1 MP4 and all fifteen mp3s share ONE git
content date (2026-07-27T22:56:44), so the normal packet-copy AUDIO LOCK applies.

SOURCING TRAP CHECKED AND CLEARED: all 15 segments transcribed with faster-whisper
(small.en, word_timestamps=True) against the LIVE make_narration.py. Four apparent
differences were chased down and every one is whisper's, not the script's:
"travelling"->"traveling" (spelling only), "listen to why"->"listened to why"
(the final-consonant mis-hear this wave keeps producing), "strawed"->"strawd",
and "the hard man THAT servant"->"the hard man THE servant". No TEXT_OVERRIDES.

WINDOWS: rebuilt from scratch from extract_beats plus the measured word timings.
Every `.timing.json` sidecar in this build holds ONE phrase spanning its whole
segment and could not supply an interior split. Contiguous 0.280 -> 149.900
(the card's own start), ZERO gaps, shortest 1.98 s, longest 5.09 s.

SCRIPTURE FACTS (Matthew 25:14-30 KJV):
  v14-15 "delivered unto them his goods ... to every man according to his several
        ability; and straightway took his journey" — trust proportioned, then a
        real departure and real freedom.
  v16-17 the five and the two both "went and traded" and DOUBLED what they held.
  v18   the one-talent servant "digged in the earth, and hid his lord's money" —
        a night burial. Fear works in the dark; that is correct, not a defect.
  v19-23 the reckoning: the identical words to BOTH faithful servants — "Well
        done ... enter thou into the joy of thy lord."
  v24-25 "I knew thee that thou art an hard man ... I was afraid." The buried
        talent came out of a LIE about the master's character.
  v30 (outer darkness) is NOT in this narration. No punishment is painted. The
        third servant walks out into the evening and the row ends on the master's
        longing to say "well done."

CONTENT CARE: the fearful servant is anxious and pitiable in every frame, never
villainous, never mocked, never punished on screen. The master is warm, generous
and finally grieved — never cold, never cruel — because the whole point of the
narration is that the servant was WRONG about him.

STAGING — five places, none of them used elsewhere in the wave: a shaded OLIVE
CANOPY on the Olivet terrace (row 31's Olivet was an open boulder shoulder shot
side-on in clear late afternoon; this is under a tree, shot from behind the
seated men, and carries no city); the master's PAVED ESTATE COURTYARD and
COLONNADED PORCH; his stone COUNTING HALL with an iron-fitted strongbox; a
MERCHANTS' WEIGHING COLONNADE and caravan yard; and a NIGHT OLIVE ORCHARD with
a threshing floor beyond it.
"""

OUTPUT_ASSET_DIR = "assets"

# The V1 MP4 (157.300 s) and all fifteen mp3s share ONE git content date
# (2026-07-27T22:56:44), and the summed V1 timeline is 157.25 s, well inside the
# guard's 0.75 s tripwire. The normal packet-copy AUDIO LOCK applies. Nothing is
# re-voiced and V1 is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Filled in AFTER the four anchor beats are generated in their own run, so the
# REFS cache (built once per v2_gen_api invocation) cannot make an anchor
# reference itself. ANCHOR ORDER: b21 (MASTER), b11 (SERV5), b13 (SERV2),
# b27 (SERV1) — every one of them is a real placed picture on the timeline and a
# daylight or lamplit face-showing shot, so the anchors cost nothing extra.
REFS = {
    "MASTER": "assets/ref-master.jpeg",
    "SERV5": "assets/ref-serv5.jpeg",
    "SERV2": "assets/ref-serv2.jpeg",
    "SERV1": "assets/ref-serv1.jpeg",
}

_NO_JESUS = ("no Jesus in this frame; no olive-shaded hillside terrace and no "
             "group of seated listening men; ")
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering "
             "on anybody anywhere in the frame including the blurred edges; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no bright outline, edge or "
            "contour around any head, hair, shoulder or body, and no light source "
            "of any kind standing behind, above or beyond anyone's head; ")
_NO_MODERN_LAMP = ("no candle, wax or taper, no glass, chimney, globe or shade, "
                   "no hurricane lamp, storm lantern, kerosene lamp or oil "
                   "lantern, no metal lamp, no hanging fixture, no ring handle, "
                   "and no electric light of any kind; ")
_NO_MODERN_TOOL = ("no steel spade or shovel, no flat pressed-steel blade, no "
                   "D-handle or T-handle, no foot tread on any blade, no painted "
                   "or chromed metal and no maker's stamp on any tool; ")
_NO_NIGHT = ("no night, no darkness, no stars, no lamp and no flame anywhere in "
             "this frame; ")
_GAZE = "nobody's pupils centred on the lens."

_NIGHT = ["NIGHT-LAMPLIGHT"]

LOCKS = {
    "MASTER": (
        "MASTER LOCK: the master is the SAME MAN in every picture he appears in — "
        "a MALE landowner of about fifty-five, broad-shouldered and heavy through "
        "the chest, with thick greying dark hair cut to the nape, a full dark "
        "beard shot through with grey at the chin, deep smile creases beside warm "
        "brown eyes, and a wide open weathered face. HIS CLOTHING IS EXACTLY "
        "THREE SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) a long DEEP "
        "FOREST-GREEN wool robe woven on a loom, its over-and-under grid of warp "
        "and weft threads plainly visible, with a narrow DARK GOLD-BROWN woven "
        "border at the neck opening and along the hem; (2) a DARK "
        "CHOCOLATE-BROWN under-tunic showing at the wrists and below the robe "
        "hem; and (3) one wide plain OXBLOOD-RED folded-cloth sash wound twice "
        "around his waist and tucked. He also wears one pair of worn brown "
        "leather sandals. NOTHING HE WEARS IS CREAM, IVORY, WHITE, BEIGE OR PALE, "
        "and he wears no head covering. HIS DEFAULT EXPRESSION IS WARMTH: he is "
        "generous, delighted, open-handed, and when he is finally grieved his "
        "face stays kind and sorrowing — never cold, never stern, never cruel, "
        "never angry."
    ),
    "SERV5": (
        "FIVE-TALENT SERVANT LOCK: the first servant is the SAME MAN in every "
        "picture he appears in — a MALE steward of about thirty-five, lean and "
        "quick, with close-cropped black hair, a short neat black beard, bright "
        "dark eyes and a ready open smile. HIS CLOTHING IS EXACTLY TWO SEPARATE "
        "PIECES OF CLOTH AND NOTHING ELSE: (1) a knee-length DEEP RUSSET-RED wool "
        "tunic woven on a loom with its warp and weft grid plainly visible, its "
        "straight sleeves pushed up above the elbows so his bare forearms show; "
        "and (2) one narrow DARK BROWN leather belt at the waist. He also wears "
        "one pair of leather sandals. HIS HEAD IS BARE — he wears no head cloth "
        "and no cap. Nothing he wears is cream, ivory, white, beige or pale."
    ),
    "SERV2": (
        "TWO-TALENT SERVANT LOCK: the second servant is the SAME MAN in every "
        "picture he appears in — a MALE steward of about forty-five, thickset and "
        "steady, with a heavy dark-brown beard, a square weathered face, and calm "
        "patient eyes. HIS CLOTHING IS EXACTLY THREE SEPARATE PIECES OF CLOTH AND "
        "NOTHING ELSE: (1) a knee-length DARK OLIVE-GREEN wool tunic woven on a "
        "loom with its warp and weft grid plainly visible; (2) one twisted "
        "natural-fibre rope belt at the waist; and (3) one DARK RUST-BROWN cloth "
        "wound over his hair as a simple head cloth and KNOTTED AT THE BACK OF "
        "HIS NECK, which he is forever shoving back off his brow with the back of "
        "his wrist as he works. He also wears one pair of leather sandals. "
        "Nothing he wears is cream, ivory, white, beige or pale."
    ),
    "SERV1": (
        "ONE-TALENT SERVANT LOCK: the third servant is the SAME MAN in every "
        "picture he appears in — a MALE household servant in his late twenties, "
        "slight and narrow-shouldered, with unkempt dark hair a little too long, "
        "a thin patchy dark beard, and hollow anxious eyes that never quite "
        "settle on anything. HIS CLOTHING IS EXACTLY TWO SEPARATE PIECES OF CLOTH "
        "AND NOTHING ELSE: (1) a knee-length DARK SLATE-GREY wool tunic woven on "
        "a loom with its warp and weft grid plainly visible, worn thin and frayed "
        "along the hem; and (2) one frayed twisted-fibre rope belt knotted twice "
        "at the waist. He also wears one pair of worn sandals. HIS HEAD IS BARE. "
        "Nothing he wears is cream, ivory, white, beige or pale. HE IS ANXIOUS "
        "AND PITIABLE AND THE PICTURE IS ON HIS SIDE — frightened, ashamed, small; "
        "never sneering, never scheming, never villainous, never comic."
    ),
    "ESTATE": (
        "ESTATE LOCK: the master's country estate is the SAME PLACE in every "
        "picture of it. A square courtyard of worn limestone paving stands behind "
        "one deep rectangular gateway spanned by a single massive squared timber "
        "lintel, its two plank leaves standing open. Along the courtyard's north "
        "side runs a low covered porch carried on six plain round stone columns "
        "with square untouched capitals. Behind the porch is the counting hall: "
        "one long room of dressed limestone blocks with a flat roof of poles and "
        "packed earth, a heavy adzed-oak table down its middle, and one big "
        "hand-forged iron-banded wooden strongbox standing against the far wall. "
        "Two dark cypresses stand at the courtyard's outer wall and an old olive "
        "orchard of gnarled short trees slopes away behind the buildings. Every "
        "built thing here is dressed limestone, tan mud brick, hewn timber and "
        "packed earth; the roofs are FLAT; the window and door openings are plain "
        "rectangles with no glass in them."
    ),
    "TRADE": (
        "TRADING-COLONNADE LOCK: the working town of the trading beats is the "
        "SAME PLACE in every picture of it — a merchants' colonnade of squat "
        "square limestone piers roofed with hewn beams, its floor of packed "
        "earth, holding two long plank weighing benches on stone blocks. On the "
        "benches stand hand-forged bronze balance scales with two shallow pans on "
        "twisted fibre cords, small stone weights, fired-clay bowls and "
        "hand-woven reed baskets. Behind the colonnade is an open caravan yard of "
        "packed dust where laden donkeys and roped bales of dyed wool stand "
        "waiting. THE BACKGROUND POPULATION OF THIS PLACE IS STATED POSITIVELY AND "
        "IS CAPPED: at most THREE other people are ever visible behind the named "
        "figures, all of them MEN, every one of them dressed head to foot in ONE "
        "SOLID DARK SATURATED EARTH COLOUR — DARK UMBER, CHARCOAL, DEEP RUST, DARK "
        "OLIVE, DEEP INDIGO or DEEP MAROON — so that every human shape in the "
        "background of the picture, in focus or out of focus, near or far, is a "
        "DARK MASS from edge to edge. NOT ONE PERSON IN THE BACKGROUND WEARS "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE, PALE "
        "GREY OR ANY LIGHT-TONED CLOTH, DRAPE, MANTLE, SHAWL, TUNIC OR HEAD "
        "COVERING, and no blurred pale figure stands among the animals or in any "
        "doorway. The only light-toned things anywhere in the picture are stone, "
        "dust, reed basketry and bare skin."
    ),
    "ORCHARD": (
        "OLIVE-ORCHARD LOCK: the orchard behind the estate is the SAME PLACE in "
        "every picture of it — perhaps twenty short gnarled old olive trees on a "
        "gentle slope of dry stony red-brown earth, their trunks split and "
        "hollowed with age, their small grey-green leaves thin enough to see the "
        "sky through. Between the trunks the ground is bare worked soil and loose "
        "field stones, with one low dry-laid limestone retaining wall running "
        "across the slope. There is nothing else on this ground: no tube, hose, "
        "pipe, line, cord, wire, cable, tape, stake or fitting of any kind lying "
        "along or across it, and nothing black or glossy running in a straight "
        "line anywhere."
    ),
    "OLIVET": (
        "OLIVET-TERRACE LOCK: the teaching place is a narrow dry earth terrace "
        "high on the Mount of Olives, under the low spreading canopy of one very "
        "old olive tree whose split grey trunk leans out over the ledge. The "
        "ground is dry pale dust and grey outcropping rock with a few thin dry "
        "grasses. Beyond the ledge the land falls away into a deep dry valley of "
        "bare tawny rock and thorn scrub, and a bare tawny hillside rises again "
        "on the far side of it. THERE IS NO TOWN, NO CITY, NO WALL, NO TOWER, NO "
        "DOME, NO ROOFLINE AND NO BUILDING OF ANY KIND ANYWHERE IN THE PICTURE — "
        "the far side of the valley is empty bare hill from edge to edge."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the listeners are a small closed group of MEN, first-"
        "century Galilean labourers and fishermen between about twenty-five and "
        "fifty, weathered and sun-darkened, most of them bearded, sitting low on "
        "the dust and rock. Each man wears a plain loom-woven wool tunic in ONE "
        "SATURATED DARK COLOUR — deep indigo, dark umber, deep rust, dark olive, "
        "charcoal or deep maroon — with a rope or folded-cloth belt, and several "
        "of them have a DARK head cloth of the same saturated family wound over "
        "the hair and tucked behind an ear. NOT ONE OF THEM WEARS CREAM, IVORY, "
        "OFF-WHITE, BEIGE, BUFF, SAND OR ANY PALE CLOTH — the only pale wool in "
        "any picture is Jesus's own robe. No woman and no child is among them."
    ),
}

BEATS = [
    # ================== FRAME + THE ENTRUSTING (j14, 25:14) ==================
    {
        "id": "v2-r032-b01", "out": "s01-for-the-kingdom-of-heaven.jpeg",
        "seg": "j14", "window": "0.280-4.000", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "For the kingdom of heaven is as a man travelling into a far country,",
        "must_show": "Jesus sitting on the dry terrace under the old olive canopy with his small group of male disciples sitting low on the dust around him, the empty dry valley and the bare far hillside behind, in clear afternoon light broken by the leaves.",
        "must_not_show": _NO_HALO + "no town, city, wall, tower, dome, minaret, roofline or building anywhere; no night, no lamp, no flame, no sunset and no sunrise; no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, clear afternoon light coming from high on the "
            "left and broken into soft moving patches by the olive leaves, the sun well "
            "up and OUT OF FRAME, fine film grain, true depth of field. THE CAMERA IS "
            "SET LOW AND BEHIND THE SEATED DISCIPLES AND SHOOTS PAST THEM toward Jesus, "
            "so the four nearest men are seen entirely FROM BEHIND as dark backs, "
            "shoulders and dark head cloths filling the lower third of the frame, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. Jesus sits on the bare dust with "
            "his back against the leaning split olive trunk, slightly left of centre in "
            "the middle distance, seen in three-quarter view; his forearms rest on his "
            "raised knees and one hand is opening as he begins to speak, and his gaze "
            "travels down and to the LEFT into the seated men and exits through the "
            "LEFT EDGE of the picture. THIS IS A WIDE FULL-LENGTH GROUP PHOTOGRAPH AND "
            "NOT A PORTRAIT: the camera is far enough back that Jesus and at least six "
            "seated men appear together head to sandals, with the tree above them and "
            "the empty dry valley and the bare tawny far hillside beyond. Jesus occupies "
            "only a modest part of the frame. THE ONLY PALE WOOL IN THE WHOLE PICTURE IS "
            "HIS OWN ROBE; every disciple's back, shoulder and head cloth is a solid "
            "dark saturated mass of indigo, umber, rust, olive or charcoal from edge to "
            "edge, in focus and out of focus alike."
        ),
    },
    {
        "id": "v2-r032-b02", "out": "s02-who-called-his-own-servants.jpeg",
        "seg": "j14", "window": "4.000-6.730", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "SERV2", "SERV1", "ESTATE"],
        "narration": "who called his own servants,",
        "must_show": "the master standing in the doorway of his counting hall in bright morning light with one arm raised, calling; his three named male servants crossing the sunlit paved courtyard toward him.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no money-bag, coin or strongbox visible yet; no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, hard bright morning sun from the low left "
            "throwing long crisp shadows across the pale limestone paving, deep clean "
            "shade under the porch, fine film grain. THE CAMERA STANDS BEHIND THE THREE "
            "SERVANTS AT SHOULDER HEIGHT AND SHOOTS PAST THEM up the courtyard, so all "
            "three men are seen FROM BEHIND and in three-quarter from behind as they "
            "walk AWAY from the camera toward the hall doorway, and NOT ONE OF THEIR "
            "FACES IS TURNED TOWARD THE LENS. The russet-tunicked first servant walks "
            "ahead at the left, the olive-tunicked head-clothed second servant a pace "
            "behind him at the centre, and the slate-grey third servant hangs back "
            "rightmost and slowest of the three. Beyond them, small in the middle "
            "distance and sharp, the master stands in the plain rectangular doorway of "
            "the counting hall under the porch columns, his deep green robe bright in "
            "the doorway shade, his right arm lifted and open in a summoning gesture and "
            "his face turned down the courtyard toward the approaching men, his gaze "
            "travelling toward the bottom left of the frame. The two dark cypresses "
            "stand against the far wall on the right. THE NEAR FOREGROUND IS BARE SUNLIT "
            "LIMESTONE PAVING AND THE THREE MEN'S OWN LONG SHADOWS AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b03", "out": "s03-delivered-unto-them-his-goods.jpeg",
        "seg": "j14", "window": "6.730-10.490", "wide": False, "jesus": False,
        "locks": ["MASTER", "ESTATE"],
        "narration": "and delivered unto them his goods.",
        "must_show": "the open iron-banded strongbox and the master's two male hands lifting a heavy drawstring leather money-bag out of it and setting it down on the adzed-oak table.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no printed lettering, numerals or maker's stamp on the box, the bags or the table; no machined hinge, screw, bolt or padlock; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a shallow aperture, bright morning daylight "
            "raking in from a plain rectangular window opening on the left across the "
            "adzed-oak table, dust hanging in the light, deep shadow at the back of the "
            "hall, fine film grain. THE CAMERA IS LOW AND CLOSE AT TABLE HEIGHT, FRAMING "
            "ONLY THE HANDS, THE TABLE AND THE BOX — no complete face appears in this "
            "picture at all. The master's two broad weathered MALE hands, with the dark "
            "gold-brown woven border of his deep forest-green sleeve showing at each "
            "wrist, are lowering one heavy brown drawstring leather money-bag onto the "
            "worn tabletop, the bag sagging under its weight and the twisted flax "
            "drawstring hanging loose. The heavy hand-forged iron-banded wooden "
            "strongbox stands open at the right of the frame with its plank lid tipped "
            "back, three more identical bags visible inside it. Sharp on the near table "
            "are a few loose struck silver coins, each correctly bearing a ruler's head "
            "in profile and a worn rim legend. THE NEAR FOREGROUND IS THE BARE WORN OAK "
            "OF THE TABLE, ITS ADZE MARKS AND ITS GRAIN, OUT OF FOCUS, AND NOTHING ELSE."
        ),
    },
    # ============================ n1 — the setup ============================
    {
        "id": "v2-r032-b04", "out": "s04-a-wealthy-man-before-a-journey.jpeg",
        "seg": "n1", "window": "10.490-14.810", "wide": True, "jesus": False,
        "locks": ["MASTER", "ESTATE", "ANCIENT-ROAD"],
        "narration": "Jesus told a story about a wealthy man who, before a long journey,",
        "must_show": "the master's travel donkeys standing loaded in the sunlit courtyard by the open gateway, two male grooms cinching the packs, and the master pulling his oxblood sash tight as he checks the load.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no servant of the three named men in this frame; no cart with a pneumatic tyre, no metal buckle, clip or webbing strap on any pack; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, bright mid-morning sun from the right, hard "
            "shadows on the limestone paving, hazy tan hills visible through the open "
            "gateway, fine film grain. THE CAMERA STANDS AT THE BACK OF THE COURTYARD "
            "BEHIND AND SLIGHTLY LEFT OF THE ANIMALS AND SHOOTS PAST THEM toward the "
            "open gateway, so the two grooms are seen from the side and from behind at "
            "work and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH "
            "SCENE: two laden donkeys stand side-on across the middle of the frame with "
            "roped bundles of dark wool cloth and two fired-clay water jars lashed over "
            "their backs with twisted fibre cord, and two MALE grooms in dark umber and "
            "charcoal tunics lean into the cinches on the far side of them. At the right, "
            "seen in full length and in three-quarter from behind, the master stands "
            "pulling his wide oxblood-red folded-cloth sash tight around the waist of his "
            "deep forest-green robe, his head turned away from the camera toward the "
            "donkeys, his gaze exiting the frame through the LEFT EDGE. Beyond the deep "
            "timber-lintelled gateway the bare packed-earth road runs away between "
            "stones into the hills, with nothing lining it. THE NEAR FOREGROUND IS ONE "
            "COIL OF TWISTED FIBRE ROPE LYING ON THE PAVING, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b05", "out": "s05-entrusted-his-own-fortune.jpeg",
        "seg": "n1", "window": "14.810-17.510", "wide": False, "jesus": False,
        "locks": ["MASTER", "SERV5", "ESTATE"],
        "narration": "entrusted his servants with his own fortune.",
        "must_show": "the master pressing one heavy leather money-bag into the first servant's two open male hands, the two men close and facing each other in strict profile.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no other person in the frame; no female hand or figure; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a shallow aperture, warm morning daylight from "
            "the left, the counting hall soft and dark behind, fine film grain. THE "
            "CAMERA IS STRICTLY SIDE-ON TO BOTH MEN AND SHOOTS ACROSS THEM AT RIGHT "
            "ANGLES, SO EACH MAN IS SEEN IN FULL PROFILE WITH HIS FAR CHEEK AND FAR EYE "
            "COMPLETELY HIDDEN BEHIND HIS OWN HEAD — a gaze into the lens is impossible "
            "from either position. The master, the grey-bearded man in the deep "
            "forest-green robe with the dark gold-brown border, stands at the LEFT of "
            "the frame in profile facing right; the first servant, the lean "
            "black-bearded man in the deep russet-red tunic with his sleeves pushed above "
            "the elbows and his head bare, stands at the RIGHT in profile facing left. "
            "Their eyelines are exactly horizontal and meet in the middle of the picture. "
            "Between them, sharp and central at chest height, the master's two broad MALE "
            "hands are pressing one heavy brown drawstring leather money-bag down into "
            "the servant's two upturned MALE hands, both pairs of hands taking the weight "
            "at once. The master's expression is confiding and glad; the servant's is "
            "surprised and steady. THE NEAR FOREGROUND IS THE OUT-OF-FOCUS DARK GREEN "
            "SHOULDER OF THE MASTER'S OWN ROBE AT THE BOTTOM LEFT CORNER AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b06", "out": "s06-five-bags-of-silver.jpeg",
        "seg": "n1", "window": "17.510-20.190", "wide": False, "jesus": False,
        "locks": ["MASTER", "SERV5", "ESTATE"],
        "narration": "To one he gave five bags of silver,",
        "must_show": "EXACTLY FIVE heavy leather money-bags standing separated in one straight row along the oak table, countable one by one, with the first servant's hands resting at the near end of the row.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no sixth bag, no heap, no pile and no vague cluster of bags; no numerals or lettering on any bag; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, bright morning daylight raking from the left "
            "across the adzed-oak table, deep shade behind, fine film grain. THE CAMERA "
            "LOOKS DOWN THE LENGTH OF THE TABLE FROM SLIGHTLY ABOVE AND SLIGHTLY TO ONE "
            "SIDE, so the row of bags recedes across the frame and each one is fully "
            "separated from its neighbours against the bare wood. COUNTABLE AND EXACT: "
            "FIVE heavy brown drawstring leather money-bags stand in ONE STRAIGHT ROW "
            "along the table, spaced a clear hand's width apart, each one plainly "
            "distinct, each sagging under the weight of coin, each with its twisted flax "
            "drawstring knotted at the neck — one, two, three, four, five, and NO SIXTH "
            "BAG anywhere in the picture. The nearest bag stands open with struck silver "
            "coins spilled beside it, each coin correctly bearing a ruler's head in "
            "profile and a worn rim legend. At the near right edge, cropped at the "
            "forearms, the first servant's two bare MALE forearms and hands rest on the "
            "table beside the nearest bag, the pushed-up sleeve of his deep russet-red "
            "tunic visible at the elbow; no complete face appears in this picture. THE "
            "NEAR FOREGROUND IS THE OUT-OF-FOCUS GRAIN OF THE OAK TABLETOP AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b07", "out": "s07-to-another-two-and-another-one.jpeg",
        "seg": "n1", "window": "20.190-23.330", "wide": True, "jesus": False,
        "locks": ["SERV2", "SERV1", "ESTATE"],
        "narration": "to another two, and to another one,",
        "must_show": "the second servant standing behind EXACTLY TWO money-bags set apart on the table, and the third servant standing behind EXACTLY ONE money-bag, the three bags clearly separated so the two and the one can be counted.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no fourth bag anywhere; no master and no first servant in this frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, bright morning daylight from a plain rectangular "
            "window opening on the left, the far end of the hall in deep shade, fine "
            "film grain. THE CAMERA STANDS AT THE END OF THE TABLE AND SHOOTS ALONG IT "
            "FROM THE SIDE, so both men are seen in three-quarter view turned toward "
            "their own bags and NEITHER FACE IS SQUARED UP TO THE LENS; each man's gaze "
            "travels down onto the wood in front of him. THIS IS A WIDE FULL-LENGTH "
            "SCENE with both men visible from head to sandals. At the LEFT stands the "
            "second servant, the thickset dark-bearded man in the DARK OLIVE-GREEN tunic "
            "with the rope belt and the DARK RUST-BROWN head cloth knotted at the back "
            "of his neck, one hand pushing the cloth back off his brow; on the table "
            "before him stand EXACTLY TWO heavy brown leather money-bags, a clear hand's "
            "width apart. At the RIGHT, a full pace further down the table and standing "
            "apart from him, is the third servant, the slight anxious man in the DARK "
            "SLATE-GREY tunic with the frayed rope belt and his head bare, his shoulders "
            "drawn in; on the table before him stands EXACTLY ONE heavy brown leather "
            "money-bag and nothing beside it. THREE BAGS TOTAL IN THE WHOLE PICTURE — "
            "two here, one there, countable at a glance. THE NEAR FOREGROUND IS BARE "
            "OAK TABLETOP, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b08", "out": "s08-according-to-what-he-could-handle.jpeg",
        "seg": "n1", "window": "23.330-26.610", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "SERV2", "SERV1", "ESTATE"],
        "narration": "each according to what he could handle.",
        "must_show": "the master looking along the line of his three named servants, weighing each of them, his face warm and considering — four men in the hall and no fifth.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no fifth person anywhere in the frame; nobody stern, accusing or suspicious; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, morning daylight from the left, the hall warm "
            "and dim beyond, fine film grain. THE CAMERA IS PLACED COMPLETELY SIDE-ON TO "
            "THE WHOLE GROUP AND SHOOTS ACROSS THEM AT RIGHT ANGLES TO EVERY EYELINE IN "
            "THE PICTURE, so the conversation runs HORIZONTALLY ACROSS THE FRAME and NOT "
            "ONE FACE IS SQUARED UP TO THE LENS. EXACTLY FOUR MEN ARE IN THIS PICTURE "
            "AND NO FIFTH. The master stands at the RIGHT in his deep forest-green robe "
            "and oxblood sash, seen in profile, his head turned leftward along the line "
            "and his gaze travelling out through the LEFT EDGE of the frame. Ranged "
            "along to the LEFT of him and clearly separated stand his three servants, "
            "each seen in profile or three-quarter from behind and each holding his own "
            "bags against his chest: nearest the master the lean black-bearded first "
            "servant in DEEP RUSSET-RED with five bags stacked in his arms, then the "
            "thickset second servant in DARK OLIVE-GREEN with the DARK RUST-BROWN head "
            "cloth holding two, and furthest away the slight third servant in DARK "
            "SLATE-GREY holding one against his stomach with both arms. All four men are "
            "seen head to sandals. The master's expression is warm and considering, "
            "measuring each man kindly. THE NEAR FOREGROUND IS THE OUT-OF-FOCUS END OF "
            "THE OAK TABLE RUNNING ACROSS THE BOTTOM OF THE FRAME AND NOTHING ELSE."
        ),
    },
    # ============================ n2 — the trust ============================
    {
        "id": "v2-r032-b09", "out": "s09-a-staggering-amount-of-trust.jpeg",
        "seg": "n2", "window": "26.610-29.110", "wide": False, "jesus": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": "It was a staggering amount of trust.",
        "must_show": "a very close view of the third servant's two male hands cupped around his single heavy money-bag, the leather creasing under the weight of the coin inside.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no complete face in the frame; no female hand; no lettering or numerals on the bag; " + _NO_CREAM + _GAZE,
        "scene": (
            "One macro photograph, 100mm lens wide open, warm morning daylight from the "
            "left, the background falling away into soft dark shade, fine film grain. "
            "THE FRAME CONTAINS ONLY HANDS AND A BAG — no complete face appears in this "
            "picture, so no gaze exists in it at all. Filling the centre of the frame, "
            "two thin MALE hands with short bitten nails and dry knuckles are cupped "
            "under and around one heavy brown drawstring leather money-bag, the fingers "
            "spread wide to take the weight, the soft leather bulging and creasing "
            "between them and the twisted flax drawstring hanging down past the wrist. "
            "The frayed sleeve of a DARK SLATE-GREY loom-woven wool tunic shows at each "
            "wrist, its over-and-under grid of warp and weft threads plainly visible at "
            "this distance and unmistakably WOVEN, never knitted. Far behind and "
            "completely out of focus, a dark rectangle of the hall doorway with hard "
            "sunlight beyond it. THE NEAR FOREGROUND IS THE BAG AND THE HANDS THEMSELVES "
            "AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b10", "out": "s10-left-them-free-to-use-it.jpeg",
        "seg": "n2", "window": "29.110-33.490", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "SERV2", "SERV1", "ESTATE", "ANCIENT-ROAD"],
        "narration": "He handed his wealth to his servants and left them free to use it.",
        "must_show": "the master riding away out through the gateway arch onto the bare road with his laden donkeys, and the three servants standing in the courtyard watching him go, seen from behind.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no asphalt, kerb, painted line, tyre rut, pole, wire, fence or signpost along the road; no farewell embrace and no crowd; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, hard late-morning sun from behind the camera's "
            "right shoulder, the courtyard paving bright, the gateway shade deep, dust "
            "raised in the road beyond, fine film grain. THE CAMERA STANDS IN THE "
            "COURTYARD DIRECTLY BEHIND THE THREE SERVANTS AND SHOOTS PAST THEM AND OUT "
            "THROUGH THE GATEWAY, so all three men are seen entirely FROM BEHIND as dark "
            "backs and shoulders in the near frame with their faces completely hidden, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. Left to right in the near frame "
            "stand the DEEP RUSSET-RED back of the first servant, the DARK OLIVE-GREEN "
            "back and DARK RUST-BROWN head cloth of the second, and the DARK SLATE-GREY "
            "back of the third, all three of them a solid dark saturated mass, all three "
            "watching down the road away from the camera. Framed small and sharp in the "
            "gateway opening beyond them, the master rides away from the camera on a "
            "donkey with the two laden pack animals strung behind him on twisted fibre "
            "leads, his deep forest-green back turned to us, already out on the bare "
            "packed-earth road that runs off between loose stones into the tan hills "
            "with NOTHING LINING IT ANYWHERE. THE NEAR FOREGROUND IS THE THREE DARK "
            "BACKS THEMSELVES AND THE SUNLIT LIMESTONE PAVING BETWEEN THEM."
        ),
    },
    # =========================== n3 — the five ==============================
    {
        "id": "v2-r032-b11", "out": "s11-went-straight-to-work.jpeg",
        "seg": "n3", "window": "33.490-36.930", "wide": False, "jesus": False,
        "locks": ["SERV5", "TRADE", "MARKET-TOWN"],
        "narration": "The servant with five bags went straight to work, trading",
        "must_show": "the first servant at the merchants' weighing bench mid-deal, one hand tipping struck silver coins into the balance pan and the other braced on the plank, his face lit and intent — this is the anchor picture of his face.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no folding table, trestle, metal pole, umbrella, printed or striped awning, plastic crate or painted price board; no dome, minaret, bell tower, spire, pitched roof or roof tile against the sky; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a shallow aperture, strong midday sun outside "
            "the colonnade bouncing up off the packed earth into the shade, so the light "
            "on him is warm and comes from BELOW AND IN FRONT, the piers and the yard "
            "behind him falling into soft out-of-focus shade, fine film grain. THE "
            "CAMERA IS SIDE-ON TO HIM AT BENCH HEIGHT AND SHOOTS ACROSS THE BENCH AT "
            "RIGHT ANGLES TO HIS EYELINE: HE IS SEEN IN THREE-QUARTER PROFILE WITH HIS "
            "HEAD TURNED WELL OFF THE CAMERA AXIS, HIS GAZE FIXED DOWN ON THE BALANCE "
            "PAN IN FRONT OF HIM AND EXITING THE FRAME THROUGH THE BOTTOM LEFT CORNER. "
            "The first servant fills the right half of the frame from the hips up — the "
            "lean quick man of about thirty-five with close-cropped black hair, a short "
            "neat black beard and a bare head, in his DEEP RUSSET-RED loom-woven tunic "
            "with the sleeves pushed above his elbows and one narrow dark brown leather "
            "belt at his waist. His right MALE hand tips a stream of struck silver coins "
            "from a leather bag into the shallow bronze pan of the balance scales, each "
            "coin correctly bearing a ruler's head in profile and a worn rim legend; his "
            "left hand is braced flat on the plank bench. His expression is alive, "
            "focused and glad. Sharp beside the scales are small stone weights and one "
            "hand-woven reed basket. THE NEAR FOREGROUND IS THE OUT-OF-FOCUS EDGE OF THE "
            "PLANK BENCH RUNNING ACROSS THE BOTTOM OF THE FRAME AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b12", "out": "s12-doubled-everything-he-was-given.jpeg",
        "seg": "n3", "window": "36.930-41.540", "wide": True, "jesus": False,
        "locks": ["SERV5", "TRADE", "MARKET-TOWN"],
        "narration": "and investing, and doubled everything he had been given.",
        "must_show": "the first servant in the caravan yard receiving the return on his trade — EXACTLY FIVE money-bags standing separated in a row on the bench and his hands setting a fresh sixth bag down beside them, with laden donkeys and roped bales behind.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no vague heap or pile of bags; no plastic crate, printed awning, folding trestle or painted sign; no dome, minaret, bell tower, spire or roof tile against the sky; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hot open afternoon sun from the high right, hard "
            "shadows on the packed dust of the caravan yard, dust hanging in the air, "
            "fine film grain. THE CAMERA STANDS BEHIND AND TO THE LEFT OF THE SERVANT "
            "AND SHOOTS PAST HIS SHOULDER ALONG THE BENCH into the yard, so he is seen "
            "in three-quarter FROM BEHIND with his face turned away down the bench and "
            "HIS GAZE EXITING THE FRAME THROUGH THE RIGHT EDGE; NO FACE IN THIS PICTURE "
            "IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE: the first "
            "servant, the lean black-bearded bare-headed man in the DEEP RUSSET-RED "
            "tunic with pushed-up sleeves, stands at the left of the frame seen head to "
            "sandals, both MALE hands lowering one fresh heavy leather money-bag onto "
            "the plank bench. COUNTABLE AND EXACT: FIVE money-bags already stand in ONE "
            "STRAIGHT ROW along the bench, spaced a clear hand's width apart, each one "
            "plainly separate — one, two, three, four, five — and the bag in his hands "
            "is coming down to start a second row. Behind him in the middle distance two "
            "MALE porters in dark umber and charcoal tunics, seen from behind, are "
            "roping bales of dark dyed wool onto a laden donkey. Against the sky beyond "
            "the yard there is only FLAT ROOFLINE and bare tan hill. THE NEAR FOREGROUND "
            "IS THE OUT-OF-FOCUS END OF THE PLANK BENCH AND ONE HAND-WOVEN REED BASKET."
        ),
    },
    # ============================ n4 — the two ==============================
    {
        "id": "v2-r032-b13", "out": "s13-the-servant-with-two-bags.jpeg",
        "seg": "n4", "window": "41.540-44.100", "wide": False, "jesus": False,
        "locks": ["SERV2", "TRADE", "MARKET-TOWN"],
        "narration": "The servant with two bags did the same,",
        "must_show": "the second servant at the weighing bench with EXACTLY TWO money-bags in front of him, one hand shoving his rust-brown head cloth back off his brow, his face weathered and calm — this is the anchor picture of his face.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no third bag; no folding trestle, metal pole, umbrella, printed awning, plastic crate or painted sign; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a shallow aperture, bright afternoon light "
            "bouncing up off the pale packed earth of the yard into the colonnade shade, "
            "so the light on him comes from BELOW AND IN FRONT, the piers behind him soft "
            "and dark, fine film grain. THE CAMERA IS SIDE-ON AT BENCH HEIGHT AND SHOOTS "
            "ACROSS HIM AT RIGHT ANGLES TO HIS EYELINE: HE IS SEEN IN THREE-QUARTER "
            "PROFILE WITH HIS HEAD TURNED WELL OFF THE CAMERA AXIS, HIS GAZE TRAVELLING "
            "DOWN AND ACROSS ONTO THE TWO BAGS AND EXITING THE FRAME THROUGH THE BOTTOM "
            "RIGHT CORNER. The second servant fills the left half of the frame from the "
            "hips up — the thickset steady man of about forty-five with a heavy "
            "dark-brown beard and a square weathered face, in his DARK OLIVE-GREEN "
            "loom-woven tunic with one twisted rope belt, and his DARK RUST-BROWN head "
            "cloth knotted at the back of his neck. His right MALE hand is lifted and he "
            "is shoving the head cloth back off his brow with the back of his wrist, the "
            "cloth rucked up under his palm; his left hand rests spread on the plank "
            "bench. COUNTABLE AND EXACT: EXACTLY TWO heavy brown leather money-bags "
            "stand on the bench in front of him, a clear hand's width apart, and there "
            "is NO THIRD BAG in the picture. His expression is calm, deliberate and "
            "quietly pleased. THE NEAR FOREGROUND IS THE OUT-OF-FOCUS PLANK EDGE OF THE "
            "BENCH AND ONE SMALL STONE WEIGHT."
        ),
    },
    {
        "id": "v2-r032-b14", "out": "s14-doubled-his-as-well.jpeg",
        "seg": "n4", "window": "44.100-48.140", "wide": True, "jesus": False,
        "locks": ["SERV2", "TRADE", "MARKET-TOWN"],
        "narration": "and doubled his as well. Neither one played it safe.",
        "must_show": "the second servant handing over a roped bale of dyed wool to a trader and taking back EXACTLY FOUR money-bags standing separated in a row on the bench.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no fifth bag, no heap and no vague cluster; no plastic crate, printed awning, folding trestle or painted sign; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm mid-afternoon sun slanting in under the "
            "colonnade beams from the low right, long bars of light and shade across the "
            "packed earth floor, fine film grain. THE CAMERA STANDS BEHIND THE SECOND "
            "SERVANT AND SHOOTS PAST HIS SHOULDER ACROSS THE BENCH, so he is seen from "
            "behind and in three-quarter from behind, his rust-brown head cloth toward "
            "us and his face hidden, and the trader opposite him is seen in strict "
            "PROFILE looking down at the bale — NOT ONE FACE IN THIS PICTURE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE with both men visible "
            "head to sandals. The second servant stands at the near left in his DARK "
            "OLIVE-GREEN tunic, both MALE hands pushing a roped bale of dark indigo dyed "
            "wool across the plank bench; opposite him a MALE trader in a deep umber "
            "tunic and a charcoal head cloth takes it with both hands, his gaze down on "
            "the bale and exiting the frame through the BOTTOM EDGE. COUNTABLE AND "
            "EXACT: FOUR heavy brown leather money-bags stand in ONE STRAIGHT ROW along "
            "the bench beside them, spaced a clear hand's width apart — one, two, three, "
            "four — and there is NO FIFTH BAG anywhere in the picture. Behind them the "
            "caravan yard, laden donkeys and bare tan hill under a FLAT ROOFLINE. THE "
            "NEAR FOREGROUND IS ONE HAND-WOVEN REED BASKET ON THE EARTH FLOOR, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b15", "out": "s15-made-it-grow.jpeg",
        "seg": "n4", "window": "48.140-52.100", "wide": True, "jesus": False,
        "locks": ["SERV5", "SERV2", "TRADE", "MARKET-TOWN"],
        "narration": "They took what they were trusted with and made it grow.",
        "must_show": "the two faithful servants working side by side in the colonnade at the end of a long day, sleeves rolled, sweat-marked, one weighing and one carrying — two men and no third.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no third named servant and no master in this frame; no folding trestle, metal pole, printed awning or plastic crate; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, low warm late-afternoon sun driving straight in "
            "under the colonnade beams from the far left and throwing long shadows back "
            "across the packed earth, dust turning in the light, fine film grain. THE "
            "CAMERA STANDS DEEP INSIDE THE COLONNADE BEHIND BOTH MEN AND SHOOTS PAST "
            "THEM toward the bright yard, so both are seen from behind and from the side "
            "as dark shapes against the outside light and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. EXACTLY TWO MEN ARE IN THIS PICTURE AND NO THIRD. THIS IS A WIDE "
            "FULL-LENGTH SCENE, both men head to sandals. At the left the first servant, "
            "bare-headed in DEEP RUSSET-RED with his sleeves shoved to the elbow, stands "
            "in profile at the bench with one MALE hand steadying the bronze balance "
            "beam and his gaze down on the pans, exiting the frame through the BOTTOM "
            "LEFT. At the right the second servant, in DARK OLIVE-GREEN with his DARK "
            "RUST-BROWN head cloth knotted behind, is walking away from the camera into "
            "the yard with a roped bale up on his shoulder, seen entirely from behind. "
            "Their tunics are dark with sweat between the shoulder blades and their "
            "forearms are dusty. The bench between them carries stone weights, a "
            "fired-clay bowl and one reed basket. THE NEAR FOREGROUND IS ONE SQUAT "
            "SQUARE LIMESTONE PIER AT THE LEFT EDGE, OUT OF FOCUS."
        ),
    },
    # ====================== n5 — the burial, at night ========================
    {
        "id": "v2-r032-b16", "out": "s16-the-servant-with-one-bag-was-afraid.jpeg",
        "seg": "n5", "window": "52.100-54.780", "wide": False, "jesus": False,
        "locks": ["SERV1", "ORCHARD"] + _NIGHT,
        "narration": "But the servant with one bag was afraid.",
        "must_show": "the third servant alone at the edge of the night orchard clutching his one money-bag against his chest with both arms, his small clay lamp standing on the ground in front of him.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no daylight, no sun, no sunrise, no sunset and no bright horizon; no other person anywhere in the frame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens wide open, GENUINE DEEP NIGHT — the sky above the "
            "olive branches deep blue-black and full of stars, the trees and the slope "
            "reading only as shape and silhouette, everything more than three paces away "
            "falling to near black. THE ONE LIGHT IN THE PICTURE is a small shallow "
            "terracotta oil lamp with a pinched spout and one bare fibre wick, standing "
            "ON THE GROUND at the very bottom of the frame, WELL BELOW HIS CHIN AND "
            "NEARER THE CAMERA THAN HIS HEAD, so its small soft yellow flame throws light "
            "only UPWARD AND FORWARD onto the underside of his brow, his nose, his "
            "cheekbones and his chin, while the crown and back of his head, his hair and "
            "his shoulders stay UNLIT AND DARK and merge straight into the night behind "
            "him. THE CAMERA IS SIDE-ON TO HIM AND SHOOTS ACROSS HIM AT RIGHT ANGLES: HE "
            "IS SEEN IN THREE-QUARTER PROFILE WITH HIS HEAD TURNED WELL OFF THE CAMERA "
            "AXIS, HIS GAZE THROWN BACK OVER HIS OWN SHOULDER TOWARD THE DARK BULK OF "
            "THE HOUSE AND EXITING THE FRAME THROUGH THE RIGHT EDGE. The third servant, "
            "the slight anxious man with unkempt hair, a thin patchy beard and a bare "
            "head, in his DARK SLATE-GREY loom-woven tunic and frayed rope belt, is "
            "crouched at the left of the frame with one heavy brown leather money-bag "
            "hugged against his chest inside both MALE arms. His face is frightened and "
            "small — never sly, never comic. THE NEAR FOREGROUND IS THE BARE STONY EARTH "
            "OF THE ORCHARD FLOOR AND THE LAMP ITSELF."
        ),
    },
    {
        "id": "v2-r032-b17", "out": "s17-dug-a-hole-in-the-ground.jpeg",
        "seg": "n5", "window": "54.780-57.660", "wide": False, "jesus": False,
        "locks": ["SERV1", "ORCHARD", "HAND-TOOLS"] + _NIGHT,
        "narration": "So he dug a hole in the ground,",
        "must_show": "the third servant driving a hand-forged iron mattock into the stony earth between two olive roots by lamplight, mid-swing, earth already broken and heaped beside the hole.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + _NO_MODERN_TOOL + "no daylight, no sun and no bright horizon; no other person anywhere; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens wide open, GENUINE DEEP NIGHT — deep blue-black "
            "starred sky through the thin olive leaves, the orchard beyond three paces "
            "falling to near black, no ambient fill from anywhere. THE ONE LIGHT IN THE "
            "PICTURE is a small shallow terracotta oil lamp with a pinched spout and one "
            "bare fibre wick, set DOWN ON THE BROKEN EARTH at the bottom of the frame "
            "AND NEARER THE CAMERA THAN HIS HEAD, so its single soft yellow flame lights "
            "only the turned soil, his sandals, his shins, his forearms and the "
            "underside of his jaw, and the whole top of his head, his hair and his "
            "shoulders stay UNLIT AND DARK against the night. THE CAMERA IS LOW ON THE "
            "GROUND AND STRICTLY SIDE-ON TO HIM, SHOOTING ACROSS HIS BODY AT RIGHT "
            "ANGLES: HE IS SEEN IN FULL PROFILE WITH HIS FAR CHEEK AND FAR EYE HIDDEN "
            "BEHIND HIS OWN HEAD, HIS GAZE DRIVEN STRAIGHT DOWN AT THE HOLE. The third "
            "servant, in his DARK SLATE-GREY loom-woven tunic and frayed rope belt, is "
            "caught MID-SWING: his weight is forward on his front foot, his back is "
            "bent, and both MALE hands grip a MATTOCK — one straight rough-hewn "
            "unpainted wooden haft about an arm and a half long with a single heavy "
            "hand-forged iron blade wedged onto its head at an angle, the iron dark grey "
            "and pitted and showing hammer marks, its edge bright and worn thin — and "
            "the blade is buried in the stony red-brown earth between two humped olive "
            "roots, throwing loose soil forward. A ragged heap of turned earth already "
            "lies beside the hole. THE NEAR FOREGROUND IS THE HEAP OF BROKEN SOIL AND "
            "THE LAMP."
        ),
    },
    {
        "id": "v2-r032-b18", "out": "s18-buried-the-silver.jpeg",
        "seg": "n5", "window": "57.660-60.520", "wide": False, "jesus": False,
        "locks": ["SERV1", "ORCHARD"] + _NIGHT,
        "narration": "buried the silver, and did nothing with it at all.",
        "must_show": "a very close view of the money-bag lying at the bottom of the open hole and the third servant's two male hands pushing loose earth in over it.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no daylight; no complete face in the frame; no female hand; " + _NO_CREAM + _GAZE,
        "scene": (
            "One close photograph, 50mm lens wide open, GENUINE DEEP NIGHT with the "
            "orchard beyond the hole falling completely to black. THE ONE LIGHT IN THE "
            "PICTURE is a small shallow terracotta oil lamp with a pinched spout and one "
            "bare fibre wick standing on the soil at the near edge of the frame, LOW AND "
            "NEARER THE CAMERA THAN ANYTHING ELSE, its single soft yellow flame raking "
            "ACROSS the broken earth from the front so every clod throws a long shadow "
            "away from the camera. THE FRAME CONTAINS ONLY THE HOLE, THE BAG, THE EARTH "
            "AND TWO HANDS — no face appears in this picture at all, so no gaze exists "
            "in it. Looking steeply down into a rough hole scraped in stony red-brown "
            "soil between two humped olive roots, one heavy brown drawstring leather "
            "money-bag lies slumped at the bottom of it, its twisted flax drawstring "
            "flopped across the dirt and one struck silver coin fallen loose beside it. "
            "Two thin MALE hands with dirt driven under the nails are sweeping and "
            "pushing loose earth in from the near rim, half of the bag already covered. "
            "The frayed sleeves of a DARK SLATE-GREY loom-woven wool tunic show at both "
            "wrists, the over-and-under grid of warp and weft threads plainly visible "
            "and unmistakably WOVEN, never knitted. THE NEAR FOREGROUND IS THE CRUMBLING "
            "RIM OF THE HOLE, OUT OF FOCUS."
        ),
    },
    # ================== n6 — the master comes home, the joy ==================
    {
        "id": "v2-r032-b19", "out": "s19-when-the-master-came-home.jpeg",
        "seg": "n6", "window": "60.520-63.400", "wide": True, "jesus": False,
        "locks": ["MASTER", "ESTATE", "ANCIENT-ROAD"],
        "narration": "When the master came home, the first two servants",
        "must_show": "the master riding back in through the estate gateway in clear afternoon light, travel-dusty, with his pack animals behind him and the household turning at the sound.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no asphalt, kerb, painted line, tyre rut, pole, wire, fence or signpost; no cheering crowd and no banner; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, hard clear afternoon sun from the high left, the "
            "gateway throwing a hard black shadow across the limestone paving, hanging "
            "road dust catching the light, fine film grain. THE CAMERA STANDS INSIDE THE "
            "COURTYARD WELL BACK AND TO ONE SIDE AND SHOOTS ACROSS THE GATEWAY AT RIGHT "
            "ANGLES TO THE LINE OF TRAVEL, so the master and his animals move ACROSS the "
            "frame from right to left and he is seen in PROFILE with his gaze forward "
            "along his own direction of travel, exiting the frame through the LEFT EDGE; "
            "NOT ONE FACE IN THIS PICTURE IS TURNED TOWARD THE LENS. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the master rides in under the massive squared timber "
            "lintel on a dusty donkey, seen head to sandals, his DEEP FOREST-GREEN robe "
            "and OXBLOOD-RED sash grey with road dust, his beard and hair dusty, his "
            "face tired and glad. Two laden pack donkeys follow him on twisted fibre "
            "leads. Beyond the gateway the bare packed-earth road runs away between "
            "loose stones into the tan hills with NOTHING LINING IT. At the far right of "
            "the courtyard, small and sharp, two MALE household servants in dark umber "
            "and charcoal tunics are turning toward the gateway at the sound, both seen "
            "from behind. THE NEAR FOREGROUND IS ONE ROUND STONE PORCH COLUMN AT THE "
            "LEFT EDGE, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b20", "out": "s20-and-he-was-overjoyed.jpeg",
        "seg": "n6", "window": "63.400-67.920", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "SERV2", "ESTATE"] + _NIGHT,
        "narration": "showed him what they had made, and he was overjoyed.",
        "must_show": "the two faithful servants setting their money-bags down on the oak table in the lamplit hall and the master coming up off his bench with both arms opening wide, his face full of delight.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no third servant in this frame; nobody stern or suspicious; no daylight and no sun; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, NIGHT INSIDE THE HALL — the plain rectangular "
            "window openings are black, the vault of the roof above is lost in darkness, "
            "and the room reads warm only where the flames reach. THE LIGHT COMES FROM "
            "THREE SMALL SHALLOW TERRACOTTA OIL LAMPS, each with a pinched spout and one "
            "bare fibre wick, STANDING IN A ROW ALONG THE OAK TABLE ITSELF — LOW, WELL "
            "BELOW EVERY CHIN, AND NEARER THE CAMERA THAN ANY HEAD — so their soft "
            "yellow light climbs UPWARD AND FORWARD onto the front planes of the faces "
            "and the hands, and every crown, every head of hair and every shoulder in "
            "the room stays UNLIT AND DARK against the black room behind. THE CAMERA "
            "STANDS BEHIND THE TWO SERVANTS AT THE NEAR END OF THE TABLE AND SHOOTS PAST "
            "THEM at the master, so both servants are seen FROM BEHIND as dark backs "
            "and shoulders and NEITHER OF THEIR FACES IS VISIBLE AT ALL. THIS IS A WIDE "
            "FULL-LENGTH SCENE. In the near frame the DEEP RUSSET-RED back of the first "
            "servant and the DARK OLIVE-GREEN back and DARK RUST-BROWN head cloth of the "
            "second lean in over the table, their MALE hands still on the money-bags "
            "they have just set down in a loose line on the wood. Beyond the table the "
            "master is coming up off his bench, caught mid-movement, both broad arms "
            "thrown wide and open, his head back, his whole face lit from the lamps "
            "below into open helpless delight, his gaze on the two men and exiting the "
            "frame through the BOTTOM EDGE toward them. THE NEAR FOREGROUND IS THE TWO "
            "DARK SERVANTS' BACKS AND THE LAMPLIT TABLETOP BETWEEN THEM."
        ),
    },
    # ===================== j1 — Matthew 25:21, the reward =====================
    {
        "id": "v2-r032-b21", "out": "s21-well-done-good-and-faithful.jpeg",
        "seg": "j1", "window": "67.920-71.060", "wide": False, "jesus": False,
        "locks": ["MASTER", "SERV5", "ESTATE"] + _NIGHT,
        "narration": "Well done, thou good and faithful servant:",
        "must_show": "the master gripping the first servant by both shoulders at arm's length, looking him full in the face and saying it — the master's face warm, creased and delighted. This is the anchor picture of the master's face.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no other person in the frame; nobody stern; no daylight; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a shallow aperture, NIGHT INSIDE THE HALL, the "
            "room behind them falling to soft black. THE LIGHT COMES FROM ONE SMALL "
            "SHALLOW TERRACOTTA OIL LAMP with a pinched spout and one bare fibre wick "
            "STANDING ON THE TABLE AT THE BOTTOM OF THE FRAME, BELOW BOTH MEN'S CHINS "
            "AND NEARER THE CAMERA THAN EITHER HEAD, so its soft yellow light travels "
            "only UPWARD AND FORWARD onto the fronts of both faces — catching the "
            "underside of the brow, the nose, the cheekbones and the chin — while both "
            "crowns, both heads of hair and both sets of shoulders stay UNLIT AND DARK "
            "and merge into the black room behind. THE CAMERA IS STRICTLY SIDE-ON TO "
            "BOTH MEN AND SHOOTS ACROSS THEM AT RIGHT ANGLES, SO EACH MAN IS SEEN IN "
            "FULL PROFILE WITH HIS FAR CHEEK AND FAR EYE COMPLETELY HIDDEN BEHIND HIS "
            "OWN HEAD — a gaze into the lens is geometrically impossible from either "
            "position — and their eyelines are exactly horizontal and meet in the middle "
            "of the picture. The master fills the LEFT of the frame from the chest up, "
            "in profile facing right: the heavy-set man of about fifty-five with thick "
            "greying dark hair, a full grey-shot dark beard and deep smile creases, in "
            "his DEEP FOREST-GREEN robe with the DARK GOLD-BROWN woven border. Both his "
            "broad MALE hands grip the first servant's shoulders at arm's length. The "
            "first servant fills the RIGHT of the frame in profile facing left — the "
            "lean black-bearded bare-headed man in DEEP RUSSET-RED, his chin lifting, "
            "his eyes wet. The master's mouth is open on the words and his whole face is "
            "warm, creased and delighted. THE NEAR FOREGROUND IS THE LAMP AND THE WORN "
            "OAK TABLETOP, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b22", "out": "s22-faithful-over-a-few-things.jpeg",
        "seg": "j1", "window": "71.060-73.960", "wide": False, "jesus": False,
        "locks": ["MASTER", "ESTATE"] + _NIGHT,
        "narration": "thou hast been faithful over a few things,",
        "must_show": "the master's broad male hand laid flat and easy on the small line of money-bags on the table, dismissing their size — the bags read as a modest little heap, not a treasure.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no complete face in the frame; no female hand; no glittering hoard of loose gold; " + _NO_CREAM + _GAZE,
        "scene": (
            "One close photograph, 100mm lens wide open, NIGHT INSIDE THE HALL, "
            "everything past the tabletop falling to black. THE LIGHT COMES FROM ONE "
            "SMALL SHALLOW TERRACOTTA OIL LAMP with a pinched spout and one bare fibre "
            "wick standing on the table at the near left of the frame, LOW AND NEARER "
            "THE CAMERA THAN ANYTHING ELSE, its soft yellow flame raking ACROSS the wood "
            "from the front so the bags throw long shadows away from the camera. THE "
            "FRAME CONTAINS ONLY A HAND, THE BAGS AND THE TABLE — no face appears in "
            "this picture at all, so no gaze exists in it. The master's broad weathered "
            "MALE hand, thick-knuckled and scarred across the back, with the DARK "
            "GOLD-BROWN woven border of his DEEP FOREST-GREEN sleeve at the wrist, lies "
            "flat, open and completely relaxed across the tops of three small brown "
            "drawstring leather money-bags slumped together on the worn oak. The bags "
            "are ordinary, dull and modest — soft brown leather, dusty, nothing "
            "gleaming. A few struck silver coins lie loose beside them, each correctly "
            "bearing a ruler's head in profile and a worn rim legend. THE NEAR "
            "FOREGROUND IS THE ADZE-MARKED GRAIN OF THE OAK TABLETOP, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b23", "out": "s23-ruler-over-many-things.jpeg",
        "seg": "j1", "window": "73.960-77.100", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "ESTATE", "ORCHARD"],
        "narration": "I will make thee ruler over many things:",
        "must_show": "the master out on the colonnaded porch at last light with the first servant beside him, one arm flung out over the whole estate and the olive orchard falling away below.",
        "must_not_show": _NO_JESUS + _NO_HALO + "no crown, circlet, wreath, diadem, ring of leaves or headpiece of any kind on anyone; no throne; no kneeling and no bowing; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, the very last minutes of daylight — a cool "
            "even blue-grey light with the sun already gone below the far ridge and OUT "
            "OF FRAME, no coloured horizon band, the orchard below flattening into soft "
            "shape, fine film grain. THE CAMERA STANDS BEHIND BOTH MEN ON THE PORCH AND "
            "SHOOTS PAST THEM OUT OVER THE LAND, so both are seen entirely FROM BEHIND "
            "as dark backs and shoulders against the wide view, their faces completely "
            "hidden, and NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE "
            "FULL-LENGTH SCENE, both men visible head to sandals between two plain round "
            "stone columns. At the left the master, his DEEP FOREST-GREEN back and "
            "OXBLOOD-RED sash toward us, has his right arm flung straight out and open "
            "across the view; at the right, half a pace back, the first servant in DEEP "
            "RUSSET-RED stands with his own arms loose at his sides, his head following "
            "the line of the master's arm. Below and beyond them the old olive orchard "
            "of short gnarled trees falls away down the slope, one low dry-laid "
            "limestone wall running across it, the two dark cypresses at the courtyard "
            "wall on the right, and bare tan hills behind. THE NEAR FOREGROUND IS THE "
            "WORN LIMESTONE PORCH FLOOR AND THE BASE OF ONE ROUND STONE COLUMN, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b24", "out": "s24-enter-into-the-joy-of-thy-lord.jpeg",
        "seg": "j1", "window": "77.100-80.950", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "ESTATE"] + _NIGHT,
        "narration": "enter thou into the joy of thy lord.",
        "must_show": "the master steering the first servant in through the hall doorway with an arm across his shoulders, toward a lamplit table already laid with bread and bowls inside.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no daylight and no sun; no crowd, no musicians and no dancing; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, DEEP NIGHT OUTSIDE AND WARM LAMPLIGHT WITHIN. "
            "The courtyard, the porch columns and the sky are deep blue-black with stars "
            "and are lit by nothing. Inside the hall, SEVERAL SMALL SHALLOW TERRACOTTA "
            "OIL LAMPS with pinched spouts and single bare fibre wicks stand LOW on the "
            "oak table and on a waist-high stone ledge, ALL OF THEM WELL BELOW HEAD "
            "HEIGHT, so their light rakes across the floor and the tabletop and up the "
            "lower walls and leaves the upper room and every head in shadow. That warm "
            "light spills out through the plain rectangular doorway in one clean wedge "
            "across the threshold and two paces of paving, and then stops. THE CAMERA "
            "STANDS OUT IN THE DARK COURTYARD SEVERAL PACES BACK AND A LITTLE TO THE "
            "LEFT OF THE DOORWAY AND SHOOTS PAST IT, so both men are seen FROM BEHIND as "
            "they walk AWAY from the camera into the light, their bodies dark "
            "silhouettes cut against the warm opening, and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. THIS IS A WIDE FULL-LENGTH SCENE. The master's broad DEEP "
            "FOREST-GREEN back is at the left with his right arm laid across the "
            "shoulders of the first servant in DEEP RUSSET-RED at the right, steering "
            "him over the worn limestone threshold. Inside, sharp beyond them, the long "
            "oak table is laid with round flat loaves, two fired-clay bowls and one clay "
            "jar. THE NEAR FOREGROUND IS THE DARK EMPTY PAVING OF THE COURTYARD."
        ),
    },
    # ===================== n7 — he shared his own joy ========================
    {
        "id": "v2-r032-b25", "out": "s25-shared-his-own-joy-with-them.jpeg",
        "seg": "n7", "window": "80.950-84.270", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "SERV2", "ESTATE"] + _NIGHT,
        "narration": "He did not just reward them, he shared his own joy with them,",
        "must_show": "the master seated at his own table between the two faithful servants, all three eating together and laughing, the master's head thrown back.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no fourth person; no third named servant; no daylight; no wine cup raised in a formal toast; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, NIGHT INSIDE THE HALL with the room beyond the "
            "table falling to black. THE LIGHT COMES FROM THREE SMALL SHALLOW TERRACOTTA "
            "OIL LAMPS with pinched spouts and single bare fibre wicks STANDING IN A LINE "
            "ALONG THE TABLE ITSELF, LOW AND WELL BELOW EVERY CHIN AND NEARER THE CAMERA "
            "THAN ANY HEAD, so the light climbs UPWARD AND FORWARD onto the fronts of "
            "the three faces and the hands and the bread, and every crown, every head of "
            "hair and every shoulder stays UNLIT AND DARK against the black room. THE "
            "CAMERA IS PLACED COMPLETELY SIDE-ON TO THE TABLE AND SHOOTS ALONG IT AT "
            "RIGHT ANGLES TO EVERY EYELINE, so all three men are seen in profile or "
            "three-quarter turned toward each other and the conversation runs "
            "HORIZONTALLY ACROSS THE FRAME; NOT ONE FACE IS SQUARED UP TO THE LENS. "
            "EXACTLY THREE MEN ARE IN THIS PICTURE AND NO FOURTH. The master sits at the "
            "centre on a plain bench in his DEEP FOREST-GREEN robe, his head thrown back "
            "and his mouth open in a broad laugh, one MALE hand flat on the table and "
            "one holding a torn piece of flat bread, his gaze going leftward to the "
            "first servant. The first servant in DEEP RUSSET-RED sits at the left in "
            "profile grinning back at him; the second servant in DARK OLIVE-GREEN with "
            "his DARK RUST-BROWN head cloth sits at the right, seen three-quarter from "
            "behind, laughing down at the table. Torn loaves, two fired-clay bowls and "
            "one clay jar stand between them. THE NEAR FOREGROUND IS THE LAMPLIT EDGE OF "
            "THE OAK TABLE, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b26", "out": "s26-welcomed-them-deeper-in.jpeg",
        "seg": "n7", "window": "84.270-88.120", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV5", "SERV2", "ESTATE"] + _NIGHT,
        "narration": "and welcomed them deeper in.",
        "must_show": "the master walking the two servants through an inner doorway further into the warm house, one hand on the second servant's back, all three moving away from the camera.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no fourth person; no daylight; no face turned back toward the camera; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, NIGHT INSIDE THE HOUSE. THE LIGHT COMES FROM "
            "SMALL SHALLOW TERRACOTTA OIL LAMPS with pinched spouts and single bare "
            "fibre wicks set LOW on a waist-high stone ledge in the inner room BEYOND "
            "the doorway and BELOW every chin, so the three men are lit from LOW AND IN "
            "FRONT as they walk toward it, and every crown, head of hair and shoulder "
            "stays dark. THE CAMERA STANDS BACK IN THE DARK OUTER HALL DIRECTLY BEHIND "
            "ALL THREE MEN AND SHOOTS PAST THEM through the inner doorway, so all three "
            "are seen ENTIRELY FROM BEHIND as dark backs and shoulders walking AWAY from "
            "the camera, their faces completely hidden, and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE with all three men "
            "visible head to sandals. In the middle the master's broad DEEP FOREST-GREEN "
            "back and OXBLOOD-RED sash; at the right his MALE hand is laid flat between "
            "the shoulder blades of the second servant, whose DARK OLIVE-GREEN back and "
            "DARK RUST-BROWN head cloth are turned to us; at the left the first "
            "servant's DEEP RUSSET-RED back. All three are stepping over the low worn "
            "stone sill of a plain rectangular inner doorway into the warmer room "
            "beyond, where a low table and a stone ledge are just visible. THE NEAR "
            "FOREGROUND IS THE DARK EMPTY OUTER HALL FLOOR AND ONE UNLIT OAK BENCH "
            "ACROSS THE BOTTOM OF THE FRAME."
        ),
    },
    # ================== n8 — the third servant comes back ====================
    {
        "id": "v2-r032-b27", "out": "s27-dug-up-his-one-buried-bag.jpeg",
        "seg": "n8", "window": "88.120-91.760", "wide": False, "jesus": False,
        "locks": ["SERV1", "ORCHARD", "HAND-TOOLS"],
        "narration": "Then the last servant came, dug up his one buried bag,",
        "must_show": "the third servant kneeling in the orchard in plain daylight, lifting the one dirt-crusted money-bag out of the reopened hole with both male hands, his face anxious and set — this is the anchor picture of his face.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + _NO_MODERN_TOOL + "no other person anywhere in the frame; nobody sneering or gloating; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens at a shallow aperture, flat overcast morning "
            "daylight with no hard shadows, the orchard behind him soft and out of "
            "focus, fine film grain. THE CAMERA IS DOWN AT GROUND LEVEL AND SIDE-ON TO "
            "HIM, SHOOTING ACROSS HIM AT RIGHT ANGLES TO HIS EYELINE: HE IS SEEN IN "
            "THREE-QUARTER PROFILE WITH HIS HEAD TURNED WELL OFF THE CAMERA AXIS AND HIS "
            "GAZE DRIVEN DOWN ONTO THE BAG IN HIS OWN HANDS, EXITING THE FRAME THROUGH "
            "THE BOTTOM EDGE. The third servant fills the right of the frame, kneeling "
            "on one knee in the turned red-brown soil between two humped olive roots — "
            "the slight narrow-shouldered man of about twenty-eight with unkempt dark "
            "hair a little too long, a thin patchy dark beard, hollow anxious eyes and a "
            "bare head, in his DARK SLATE-GREY loom-woven wool tunic frayed at the hem, "
            "with one frayed twisted-fibre rope belt knotted twice at the waist. Both "
            "his thin MALE hands, dirt under the nails, are lifting one heavy brown "
            "leather money-bag out of the reopened hole, the leather crusted and streaked "
            "with dried earth, soil still falling from it. Lying on the ground beside "
            "the hole is the MATTOCK: one rough-hewn unpainted wooden haft with a single "
            "heavy hand-forged iron blade wedged on at an angle, dark grey, pitted and "
            "hammer-marked. His expression is tight, anxious and braced. THE NEAR "
            "FOREGROUND IS THE HEAP OF LOOSE TURNED EARTH AT THE RIM OF THE HOLE."
        ),
    },
    {
        "id": "v2-r032-b28", "out": "s28-handed-it-back-untouched.jpeg",
        "seg": "n8", "window": "91.760-94.340", "wide": False, "jesus": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": "and handed it back untouched.",
        "must_show": "the third servant holding the dirt-crusted money-bag out flat on both male palms toward the master, and the master's hands still at his sides, not yet reaching for it.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no complete face in the frame; no female hand; nobody snatching, striking or pointing; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 100mm lens wide open, cool daylight coming in from a plain "
            "rectangular window opening on the left, the hall behind falling into soft "
            "shade, fine film grain. THE FRAME IS CROPPED AT CHEST HEIGHT AND CONTAINS "
            "ONLY TORSOS, ARMS AND HANDS — no face appears in this picture at all, so no "
            "gaze exists in it. Filling the left of the frame, the third servant's two "
            "thin MALE hands are held out flat and level, palms up, offering one heavy "
            "brown leather money-bag crusted and streaked with dried earth, its twisted "
            "flax drawstring still knotted exactly as it was tied and one dry olive root "
            "fibre stuck to the leather. The frayed sleeves of his DARK SLATE-GREY "
            "loom-woven wool tunic show at both wrists, the over-and-under grid of warp "
            "and weft plainly visible and unmistakably WOVEN, never knitted. Filling the "
            "right of the frame and slightly further away, the master's DEEP "
            "FOREST-GREEN robe with its DARK GOLD-BROWN woven border and his wide "
            "OXBLOOD-RED sash; both his broad weathered MALE hands hang open and still at "
            "his sides, NOT reaching out, NOT taking it. The small space of air between "
            "the offered bag and the unmoving hands is the centre of the picture. THE "
            "NEAR FOREGROUND IS THE OUT-OF-FOCUS EDGE OF THE OAK TABLE ACROSS THE BOTTOM."
        ),
    },
    {
        "id": "v2-r032-b29", "out": "s29-listen-to-why-he-had-buried-it.jpeg",
        "seg": "n8", "window": "94.340-96.820", "wide": False, "jesus": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": "And listen to why he had buried it.",
        "must_show": "the third servant's face alone, close, in strict side profile, eyes down, working himself up to speak — frightened, ashamed, pitiable.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no other person in the frame; nobody sneering, scheming, sly or comic; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 135mm lens wide open, cool soft daylight from a plain "
            "rectangular window opening at the LEFT of the room falling across the front "
            "of his face, the hall behind him dissolving into deep soft shade, fine film "
            "grain. THE CAMERA IS STRICTLY SIDE-ON TO HIM AND SHOOTS ACROSS HIM AT RIGHT "
            "ANGLES: HE IS SEEN IN FULL PROFILE FACING LEFT, WITH HIS FAR CHEEK AND HIS "
            "FAR EYE COMPLETELY HIDDEN BEHIND HIS OWN HEAD, SO A GAZE INTO THE LENS IS "
            "GEOMETRICALLY IMPOSSIBLE. His single visible eye is cast down and forward "
            "and his gaze exits the frame through the BOTTOM LEFT CORNER. The third "
            "servant fills the frame from the shoulders up — the slight man of about "
            "twenty-eight with unkempt dark hair a little too long over his ear, a thin "
            "patchy dark beard, a hollow cheek and a bare head. His jaw is set hard, his "
            "throat is working, there is dried dirt in the creases of his neck and a "
            "faint sheen of sweat on his temple. The neck of his DARK SLATE-GREY "
            "loom-woven wool tunic shows at the bottom of the frame with its warp and "
            "weft grid plainly visible. He is frightened and ashamed and the picture is "
            "entirely on his side — never sly, never sneering, never comic. THE NEAR "
            "FOREGROUND IS THE OUT-OF-FOCUS DARK SHOULDER OF HIS OWN TUNIC AT THE BOTTOM "
            "RIGHT CORNER AND NOTHING ELSE."
        ),
    },
    # ============= j24 — Matthew 25:24, the lie about the master =============
    {
        "id": "v2-r032-b30", "out": "s30-thou-art-an-hard-man.jpeg",
        "seg": "j24", "window": "96.820-100.000", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": "Lord, I knew thee that thou art an hard man,",
        "must_show": "the third servant standing in front of the seated master saying it, and the master listening — the master's face open and grieved, never angry, because the accusation is not true.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no third person; nobody shouting, threatening, raising a fist or striking; the master is never scowling, sneering or angry; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, cool even daylight from a plain rectangular "
            "window opening on the left, the far end of the hall in deep shade, fine "
            "film grain. THE CAMERA IS PLACED COMPLETELY SIDE-ON TO BOTH MEN AND SHOOTS "
            "ACROSS THEM AT RIGHT ANGLES TO BOTH EYELINES, so the confrontation runs "
            "HORIZONTALLY ACROSS THE FRAME and NOT ONE FACE IS SQUARED UP TO THE LENS. "
            "THIS IS A WIDE FULL-LENGTH SCENE with both men visible head to sandals. "
            "EXACTLY TWO MEN ARE IN THIS PICTURE AND NO THIRD. At the LEFT the third "
            "servant stands in profile facing right in his DARK SLATE-GREY loom-woven "
            "tunic and frayed rope belt, bare-headed, his shoulders hunched high, one "
            "thin MALE hand jabbed out flat toward the seated man and the other still "
            "clutching the dirt-crusted money-bag against his hip; his mouth is open on "
            "the words and his gaze travels rightward and exits the frame through the "
            "RIGHT EDGE. At the RIGHT the master sits on the plain oak bench in profile "
            "facing left, in his DEEP FOREST-GREEN robe and OXBLOOD-RED sash, his broad "
            "hands loose and open on his knees, leaning slightly forward to listen; his "
            "eyebrows are drawn up in the middle and his mouth is closed and soft, and "
            "his whole face is OPEN, HURT AND GRIEVING — not angry, not stern, not "
            "scowling. His gaze travels leftward and exits through the LEFT EDGE. THE "
            "NEAR FOREGROUND IS THE OUT-OF-FOCUS END OF THE OAK TABLE RUNNING ACROSS THE "
            "BOTTOM OF THE FRAME."
        ),
    },
    {
        "id": "v2-r032-b31", "out": "s31-reaping-where-thou-hast-not-sown.jpeg",
        "seg": "j24", "window": "100.000-102.480", "wide": True, "jesus": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": "reaping where thou hast not sown,",
        "must_show": "the third servant's arm flung out through the wide hall doorway toward the master's standing barley beyond it, naming the fields he is accusing him about.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no master in this frame; no tractor, combine, fence, pole, wire or building in the fields; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, the hall interior dim and cool and the land "
            "beyond the doorway blazing in flat late-morning sun, so the doorway is a "
            "hard bright rectangle in a dark wall, fine film grain. THE CAMERA STANDS "
            "BEHIND THE SERVANT AND SLIGHTLY TO HIS LEFT AND SHOOTS PAST HIM OUT THROUGH "
            "THE DOORWAY, so he is seen ENTIRELY FROM BEHIND as a dark back, shoulder "
            "and outflung arm against the bright opening, his face completely hidden and "
            "NOT TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE. He stands at "
            "the near left in his DARK SLATE-GREY loom-woven tunic and frayed rope belt, "
            "seen head to sandals, his right arm flung straight out and level toward the "
            "opening with the fingers spread. Beyond the plain rectangular doorway and "
            "sharp in the bright light, a wide sloping field of ripe standing barley "
            "runs away to a low dry-laid limestone wall and bare tan hills, with nothing "
            "else in it anywhere — no fence, no post, no wire, no pole, no machine and "
            "no building. Two dark specks of MALE reapers with hand sickles work at the "
            "far edge of the barley, tiny and seen from behind. THE NEAR FOREGROUND IS "
            "THE DARK INTERIOR WALL AND THE WORN LIMESTONE THRESHOLD, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b32", "out": "s32-strawing-where-thou-hast-not-strawed.jpeg",
        "seg": "j24", "window": "102.480-106.510", "wide": True, "jesus": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": "and strawing where thou hast not strawed:",
        "must_show": "the master's threshing floor beyond the doorway — a round swept stone floor with heaped straw and men winnowing with wooden forks — with the third servant a dark shape at the near edge of the frame.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no master in this frame; no welded metal pitchfork, no machine, no tractor, no baler, no fence, pole or wire; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, hot flat midday sun outside and deep cool shade "
            "inside the doorway, chaff and dust hanging bright in the air over the "
            "threshing floor, fine film grain. THE CAMERA STANDS WELL BACK IN THE DARK "
            "HALL BEHIND THE SERVANT AND SHOOTS PAST HIS SHOULDER through the plain "
            "rectangular doorway, so he appears only as a dark out-of-focus shoulder and "
            "the back of a bare head at the near right edge, his face completely hidden "
            "and NOT TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE beyond the "
            "opening: a round swept threshing floor of flat laid stone stands in the "
            "sun, with a broad heap of pale broken straw piled at one side of it and a "
            "clean mound of winnowed grain at the other. Three MALE farm workers in dark "
            "umber, charcoal and deep rust tunics work across it, all three seen from "
            "behind or in profile with their gazes down at their own work — two tossing "
            "threshed straw up into the air off wide HAND-CARVED WOODEN WINNOWING FORKS "
            "cut from single pieces of timber, the chaff blowing away to the left on the "
            "wind, and one sweeping grain into a hand-woven reed basket with a bundle of "
            "twigs. Beyond the floor, a low dry-laid limestone wall and bare tan hills, "
            "with no fence, post, wire, pole or machine anywhere. THE NEAR FOREGROUND IS "
            "THE DARK DOORJAMB AT THE RIGHT EDGE, OUT OF FOCUS."
        ),
    },
    # ================ j2 — Matthew 25:25, "I was afraid" =====================
    {
        "id": "v2-r032-b33", "out": "s33-and-i-was-afraid.jpeg",
        "seg": "j2", "window": "106.510-109.290", "wide": False, "jesus": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": "And I was afraid, and went and hid thy talent",
        "must_show": "the third servant standing with his shoulders collapsed and both male hands turned helplessly palm-up, the dirt-crusted bag on the floor between his feet.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no other person in the frame; nobody kneeling in worship, prostrate or grovelling; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens at a shallow aperture, cool soft daylight from a "
            "plain rectangular window opening at the LEFT, the hall behind him falling "
            "into deep soft shade, fine film grain. THE CAMERA IS SIDE-ON TO HIM AND "
            "SHOOTS ACROSS HIM AT RIGHT ANGLES TO HIS EYELINE: HE IS SEEN IN FULL "
            "PROFILE FACING LEFT WITH HIS FAR CHEEK AND FAR EYE HIDDEN BEHIND HIS OWN "
            "HEAD, and his one visible eye is cast down at the floor in front of his own "
            "feet, his gaze exiting the frame through the BOTTOM LEFT CORNER. He is seen "
            "from the knees up, filling the right half of the frame — the slight "
            "narrow-shouldered man with unkempt dark hair, a thin patchy dark beard and "
            "a bare head, in his DARK SLATE-GREY loom-woven wool tunic frayed at the hem "
            "with its warp and weft grid plainly visible, and one frayed twisted-fibre "
            "rope belt knotted twice. HIS SHOULDERS HAVE COLLAPSED FORWARD AND DOWN, his "
            "chin is dropped, and both his thin MALE hands are turned outward and "
            "helplessly PALM-UP at the level of his hips, empty. On the worn stone floor "
            "between his sandalled feet, sharp and low in the frame, sits the one heavy "
            "brown leather money-bag crusted and streaked with dried earth. THE NEAR "
            "FOREGROUND IS THE WORN STONE FLOOR RUNNING AWAY OUT OF FOCUS TOWARD THE "
            "BOTTOM OF THE FRAME."
        ),
    },
    {
        "id": "v2-r032-b34", "out": "s34-hid-thy-talent-in-the-earth.jpeg",
        "seg": "j2", "window": "109.290-111.710", "wide": False, "jesus": False,
        "locks": ["ORCHARD"] + _NIGHT,
        "narration": "in the earth: lo,",
        "must_show": "looking straight down into the black hole in the orchard floor with the money-bag lying at the bottom of it, half covered in soil, seen from directly overhead.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no person, no hand, no face and no figure anywhere in the frame; no daylight; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph taken from DIRECTLY OVERHEAD, 50mm lens, GENUINE DEEP NIGHT "
            "with the orchard beyond the rim of the hole falling completely to black. "
            "THERE IS NO PERSON IN THIS PICTURE AT ALL — no figure, no hand, no face — "
            "so no gaze exists in it. THE ONE LIGHT is a small shallow terracotta oil "
            "lamp with a pinched spout and one bare fibre wick standing on the soil just "
            "outside the frame edge at the near left, so its low soft yellow flame rakes "
            "in ACROSS the ground from one side and every clod and root throws a long "
            "hard shadow across the picture. The camera looks straight down into a rough "
            "hole scraped in stony red-brown earth between two humped grey olive roots. "
            "At the bottom of the hole one heavy brown drawstring leather money-bag lies "
            "slumped on its side, half buried under a fall of loose soil, its twisted "
            "flax drawstring still knotted and one struck silver coin fallen loose in "
            "the dirt beside it, the coin correctly bearing a ruler's head in profile "
            "and a worn rim legend. Around the hole the turned soil is heaped and "
            "cracked and studded with small field stones. Everything beyond the reach of "
            "the flame is total darkness. THE NEAR FOREGROUND IS THE CRUMBLING RIM OF "
            "THE HOLE AND ONE HUMPED OLIVE ROOT, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b35", "out": "s35-there-thou-hast-that-is-thine.jpeg",
        "seg": "j2", "window": "111.710-115.460", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": "there thou hast that is thine.",
        "must_show": "the third servant pushing the dirt-crusted money-bag across the oak table toward the seated master, and the master's hands lying still on the wood, not reaching for it.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no third person; nobody angry, shouting or striking; the master is never scowling or sneering; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, cool even daylight from a plain rectangular "
            "window opening on the left laying a long bar of light across the oak table, "
            "the hall beyond in deep shade, fine film grain. THE CAMERA IS PLACED "
            "COMPLETELY SIDE-ON TO THE TABLE AND SHOOTS ALONG IT AT RIGHT ANGLES TO BOTH "
            "EYELINES, so the exchange runs HORIZONTALLY ACROSS THE FRAME and NOT ONE "
            "FACE IS SQUARED UP TO THE LENS. THIS IS A WIDE FULL-LENGTH SCENE with both "
            "men visible from head to sandals. EXACTLY TWO MEN ARE IN THIS PICTURE AND "
            "NO THIRD. At the LEFT the third servant stands in profile facing right in "
            "his DARK SLATE-GREY loom-woven tunic, bare-headed, both thin MALE hands "
            "pushing the dirt-crusted brown leather money-bag away from himself across "
            "the wood; his chin is down and his gaze follows the bag and exits the frame "
            "through the BOTTOM RIGHT. At the RIGHT the master sits on the oak bench in "
            "profile facing left in his DEEP FOREST-GREEN robe and OXBLOOD-RED sash, "
            "both broad MALE hands lying flat and completely STILL on the tabletop, NOT "
            "reaching, NOT taking; his shoulders have dropped and his face is quiet and "
            "sorrowing. The bag sits alone in the bar of window light in the middle of "
            "the table between them. THE NEAR FOREGROUND IS THE OUT-OF-FOCUS NEAR EDGE "
            "OF THE OAK TABLE ACROSS THE BOTTOM OF THE FRAME."
        ),
    },
    # ===================== n9 — the lie, and what it cost ====================
    {
        "id": "v2-r032-b36", "out": "s36-he-buried-the-gift.jpeg",
        "seg": "n9", "window": "115.460-117.460", "wide": False, "jesus": False,
        "locks": ["ESTATE"],
        "narration": "There it is. He buried the gift",
        "must_show": "the one dirt-crusted money-bag standing alone on the oak table beside two clean, worn, well-handled bags — the contrast between them the whole point of the picture.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no person, no hand, no face and no figure anywhere in the frame; no lettering or numerals on any bag; " + _NO_CREAM + _GAZE,
        "scene": (
            "One still-life photograph, 100mm lens wide open, cool soft daylight coming "
            "in low from a plain rectangular window opening on the LEFT and raking "
            "across the tabletop from the side, so every crease and crumb of dirt throws "
            "a long shadow, the hall behind dissolving into soft dark shade. THERE IS NO "
            "PERSON IN THIS PICTURE AT ALL — no figure, no hand, no shoulder, no face — "
            "so no gaze exists in it. Sharp and central on the worn adze-marked oak "
            "table stands ONE heavy brown drawstring leather money-bag crusted and "
            "streaked all over with dried red-brown earth, a dry olive root fibre stuck "
            "to its side, its twisted flax drawstring still knotted exactly as it was "
            "first tied. A hand's width away to the right, slightly softer in focus, "
            "stand TWO other bags of the same make, both clean, both rubbed smooth and "
            "shiny with handling, both open at the neck with struck silver coins spilled "
            "out beside them, each coin correctly bearing a ruler's head in profile and "
            "a worn rim legend. THREE BAGS IN THE PICTURE AND NO FOURTH. A dusting of "
            "dry soil has fallen from the crusted bag onto the clean wood around it. THE "
            "NEAR FOREGROUND IS THE GRAIN OF THE OAK TABLETOP, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b37", "out": "s37-he-believed-his-master-was-cruel.jpeg",
        "seg": "n9", "window": "117.460-120.820", "wide": False, "jesus": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": "because he believed his master was harsh and cruel.",
        "must_show": "the third servant's frightened face sharp in the near frame and the master soft and out of focus behind him — the master perfectly ordinary and kind, so the fear is visibly in the servant and not in the man.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no third person; the master is never scowling, glaring, looming, sneering or angry; no raised hand, no fist, no whip and no weapon; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens wide open with a very shallow plane of focus, "
            "cool even daylight from a plain rectangular window opening at the LEFT, "
            "fine film grain. THE CAMERA IS SIDE-ON TO THE SERVANT AND SHOOTS ACROSS HIM "
            "AT RIGHT ANGLES: HE IS SEEN IN FULL PROFILE FACING LEFT IN THE NEAR FRAME "
            "WITH HIS FAR CHEEK AND FAR EYE HIDDEN BEHIND HIS OWN HEAD, so a gaze into "
            "the lens is geometrically impossible; his one visible eye is wide and cast "
            "down and away, exiting the frame through the LEFT EDGE. He fills the right "
            "half of the frame from the shoulders up — the slight man with unkempt dark "
            "hair, a thin patchy dark beard and a bare head, the neck of his DARK "
            "SLATE-GREY loom-woven tunic at the bottom of the frame, his jaw tight, a "
            "muscle jumping in his cheek, sweat on his temple. SOFT AND WELL OUT OF "
            "FOCUS in the middle distance behind him at the LEFT sits the master on his "
            "bench, unmistakable by his DEEP FOREST-GREEN robe with the DARK GOLD-BROWN "
            "border, his OXBLOOD-RED sash and his grey-shot dark beard — SEATED, "
            "RELAXED, SMALL IN THE FRAME AND PERFECTLY ORDINARY, both hands open on his "
            "knees, his head tilted a little to one side in patient attention. He is not "
            "standing, not looming, not raising a hand, not scowling. THE NEAR "
            "FOREGROUND IS THE OUT-OF-FOCUS DARK SHOULDER OF THE SERVANT'S OWN TUNIC AT "
            "THE BOTTOM RIGHT CORNER."
        ),
    },
    {
        "id": "v2-r032-b38", "out": "s38-he-was-wrong-about-him.jpeg",
        "seg": "n9", "window": "120.820-123.600", "wide": False, "jesus": False,
        "locks": ["MASTER", "ESTATE"],
        "narration": "He was wrong about him. His fear was built on",
        "must_show": "the master's face alone, close and in profile, looking down at the dirt-crusted bag — grieved, gentle, and completely without anger, which is the whole answer to the accusation.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no other person in the frame; no scowl, no glare, no bared teeth, no clenched jaw and no anger of any kind; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 135mm lens wide open, cool soft daylight from a plain "
            "rectangular window opening at the RIGHT of the room falling across the "
            "front of his face, the hall behind him dissolving into deep soft shade, "
            "fine film grain. THE CAMERA IS STRICTLY SIDE-ON TO HIM AND SHOOTS ACROSS "
            "HIM AT RIGHT ANGLES: HE IS SEEN IN FULL PROFILE FACING RIGHT, WITH HIS FAR "
            "CHEEK AND HIS FAR EYE COMPLETELY HIDDEN BEHIND HIS OWN HEAD, SO A GAZE INTO "
            "THE LENS IS GEOMETRICALLY IMPOSSIBLE, and his one visible eye is lowered "
            "toward the table below and in front of him, his gaze exiting the frame "
            "through the BOTTOM RIGHT CORNER. The master fills the frame from the "
            "shoulders up — the heavy-set man of about fifty-five with thick greying "
            "dark hair, a full dark beard shot with grey at the chin, deep creases "
            "beside a warm brown eye, and a broad weathered brow. The dark gold-brown "
            "woven border and the DEEP FOREST-GREEN wool of his robe show at the bottom "
            "of the frame, the over-and-under grid of warp and weft plainly visible. HIS "
            "EYEBROWS ARE DRAWN UP AND TOGETHER IN THE MIDDLE, his mouth is closed and "
            "soft, and his eye is bright with unshed water: this is GRIEF AND "
            "TENDERNESS, the face of a man who has just been badly misunderstood by "
            "someone he trusted. Blurred and low at the bottom edge, the shape of the "
            "dirt-crusted money-bag on the table. THE NEAR FOREGROUND IS THAT "
            "OUT-OF-FOCUS BAG AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b39", "out": "s39-a-lie-about-who-he-really-was.jpeg",
        "seg": "n9", "window": "123.600-126.440", "wide": True, "jesus": False,
        "locks": ["MASTER", "SERV1", "ESTATE"],
        "narration": "a lie about who his master really was.",
        "must_show": "the whole hall wide: the two men standing far apart down the length of the oak table with the untouched dirt-crusted bag alone on the wood between them — the distance itself is the picture.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no third person; no anger, no shouting and no raised hand; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens from well back, cool even daylight coming in from "
            "two plain rectangular window openings along the left wall and laying two "
            "long bars of light across the stone floor, the roof above lost in shade, "
            "fine film grain. THE CAMERA STANDS AT THE FAR END OF THE HALL WELL BEHIND "
            "THE THIRD SERVANT AND SHOOTS PAST HIM DOWN THE LENGTH OF THE TABLE, so he "
            "is seen ENTIRELY FROM BEHIND as a small dark back and shoulders in the near "
            "frame with his face completely hidden, and the master far beyond him is "
            "seen in three-quarter turned away toward the window; NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE, both men small and "
            "visible head to sandals with a great deal of empty stone floor and empty "
            "table between them. The third servant's DARK SLATE-GREY back stands near "
            "the camera at the left; the master stands far away at the top of the frame "
            "beside the strongbox, his DEEP FOREST-GREEN robe and OXBLOOD-RED sash "
            "unmistakable, his shoulders dropped and his head turned away toward the "
            "light. Exactly halfway between them on the bare oak table, small, alone and "
            "sharply lit in one bar of window light, sits the untouched dirt-crusted "
            "money-bag. THE NEAR FOREGROUND IS THE EMPTY WORN STONE FLOOR RUNNING AWAY "
            "FROM THE CAMERA, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b40", "out": "s40-that-lie-cost-him-everything.jpeg",
        "seg": "n9", "window": "126.440-129.440", "wide": True, "jesus": False,
        "locks": ["SERV1", "ESTATE"] + _NIGHT,
        "narration": "And that lie cost him everything.",
        "must_show": "the third servant walking out alone through the estate gateway into the dark, seen from behind, with the warm lamplit doorway of the hall still open behind him.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no punishment, no binding, no beating, no chains, no guards, no fire and no pit; no other person visible in this frame; no daylight; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, GENUINE NIGHT — the sky above the gateway deep "
            "blue-black and starred, the courtyard paving and the walls reading only as "
            "shape and silhouette, everything away from the doorway falling to near "
            "black. THE LIGHT IN THE PICTURE comes from SMALL SHALLOW TERRACOTTA OIL "
            "LAMPS with pinched spouts and single bare fibre wicks standing LOW INSIDE "
            "the hall on the table and a waist-high stone ledge, WELL BELOW HEAD HEIGHT, "
            "so their warm light spills out of the plain rectangular doorway in one "
            "clean low wedge across the paving and lights nothing above knee height out "
            "in the yard. THE CAMERA STANDS IN THE COURTYARD BETWEEN THE LIT DOORWAY AND "
            "THE GATEWAY, BEHIND THE MAN, AND SHOOTS PAST HIM out through the gateway, "
            "so he is seen ENTIRELY FROM BEHIND, walking AWAY from the camera into the "
            "dark, his face completely hidden and NOT TURNED TOWARD THE LENS. THIS IS A "
            "WIDE FULL-LENGTH SCENE: the third servant, seen head to sandals and small in "
            "the frame, walks under the massive squared timber lintel of the open "
            "gateway, his DARK SLATE-GREY back and bare head a solid dark shape, his "
            "arms empty at his sides and his shoulders rounded. Beyond the gateway there "
            "is only the black road and the starred sky. Behind him at the top left the "
            "warm lamplit doorway of the hall STANDS OPEN AND UNGUARDED. THE NEAR "
            "FOREGROUND IS THE DARK EMPTY LIMESTONE PAVING OF THE COURTYARD."
        ),
    },
    # ==================== n10 — the closing application =====================
    {
        "id": "v2-r032-b41", "out": "s41-the-real-tragedy-of-the-story.jpeg",
        "seg": "n10", "window": "129.440-132.320", "wide": False, "jesus": False,
        "locks": ["ESTATE"] + _NIGHT,
        "narration": "That is the real tragedy of the story.",
        "must_show": "the empty lamplit hall with the dirt-crusted money-bag left standing alone on the oak table and the doorway to the dark courtyard beyond it standing open.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no person, no hand, no figure and no face anywhere in the frame; no daylight; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, NIGHT INSIDE THE HALL, the room quiet and empty. "
            "THERE IS NO PERSON IN THIS PICTURE AT ALL — no figure, no hand, no "
            "shoulder, no face — so no gaze exists in it. THE ONE LIGHT is a small "
            "shallow terracotta oil lamp with a pinched spout and one bare fibre wick "
            "standing ON THE OAK TABLE at the near left of the frame, LOW AND NEARER THE "
            "CAMERA THAN ANYTHING ELSE, its single soft yellow flame raking ACROSS the "
            "tabletop from the front so the bag throws one long shadow away from the "
            "camera and the far end of the hall falls to black. Sharp and central on the "
            "worn adze-marked oak, one heavy brown drawstring leather money-bag stands "
            "alone where it was left, crusted and streaked all over with dried "
            "red-brown earth, its twisted flax drawstring still knotted exactly as it "
            "was first tied. The benches are pushed back and empty. Beyond the table, "
            "small and dim at the top of the frame, the plain rectangular doorway to the "
            "courtyard stands open on deep blue-black night with a few stars in it. THE "
            "NEAR FOREGROUND IS THE LAMP AND THE GRAIN OF THE TABLETOP, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b42", "out": "s42-not-that-he-had-little.jpeg",
        "seg": "n10", "window": "132.320-135.600", "wide": False, "jesus": False,
        "locks": ["SERV1", "ESTATE"],
        "narration": "Not that he had little, but that he so badly",
        "must_show": "one open male hand holding a small quantity of struck silver coins on the palm — an ordinary, modest, entirely sufficient amount, not a fortune and not a pittance.",
        "must_not_show": _NO_JESUS + _NO_NIGHT + _NO_HALO + "no complete face in the frame; no female hand; no glittering treasure hoard and no gold; " + _NO_CREAM + _GAZE,
        "scene": (
            "One macro photograph, 100mm lens wide open, cool soft daylight from the "
            "left, everything past the hand dissolving into soft dark shade, fine film "
            "grain. THE FRAME CONTAINS ONLY ONE HAND AND SOME COINS — no face appears in "
            "this picture at all, so no gaze exists in it. Filling the centre of the "
            "frame, one thin MALE hand with short bitten nails, dry knuckles and dirt "
            "still in the creases is held open and level, palm up. On the palm lie a "
            "small loose handful of struck silver coins, dulled and worn, each one "
            "correctly bearing a ruler's head in profile and a worn rim legend; they are "
            "an ordinary, modest, unglamorous little sum, not gleaming, not heaped, not "
            "a treasure. The frayed sleeve of a DARK SLATE-GREY loom-woven wool tunic "
            "shows at the wrist, the over-and-under grid of warp and weft plainly "
            "visible at this distance and unmistakably WOVEN, never knitted. THE NEAR "
            "FOREGROUND IS THE EDGE OF THE PALM AND THE COINS THEMSELVES AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b43", "out": "s43-misjudged-the-heart-that-trusted-him.jpeg",
        "seg": "n10", "window": "135.600-139.080", "wide": True, "jesus": False,
        "locks": ["MASTER", "ESTATE", "ORCHARD"],
        "narration": "misjudged the heart of the one who trusted him.",
        "must_show": "the master standing alone at the edge of his porch at last light, one hand on a stone column, still looking out toward the empty gateway the servant walked out of.",
        "must_not_show": _NO_JESUS + _NO_HALO + "no other person anywhere in the frame; no anger; no night, no lamp and no flame; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the last cool blue-grey minutes of daylight with "
            "the sun already down behind the ridge and OUT OF FRAME, no coloured horizon "
            "band anywhere, the courtyard flattening into even shadowless shape, fine "
            "film grain. THE CAMERA STANDS BEHIND AND TO THE RIGHT OF THE MASTER, DEEP "
            "UNDER THE PORCH, AND SHOOTS PAST HIM out across the courtyard toward the "
            "gateway, so he is seen ENTIRELY FROM BEHIND and in three-quarter from "
            "behind as a dark back and shoulder against the wider view, his face turned "
            "away and NOT TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE with "
            "the master visible head to sandals and only a modest part of the frame. He "
            "stands at the left between two plain round stone columns, his DEEP "
            "FOREST-GREEN robe and OXBLOOD-RED sash unmistakable, his right MALE hand "
            "resting flat and heavy on the column beside him, his head slightly bowed "
            "and turned out toward the deep empty gateway across the courtyard. THE "
            "COURTYARD IS COMPLETELY EMPTY — bare limestone paving, the two dark "
            "cypresses at the outer wall, the open gateway with its massive squared "
            "timber lintel, and beyond it the bare road and the tan hills going grey. "
            "Behind and below the porch on the right, the old olive orchard falls away "
            "down the slope. THE NEAR FOREGROUND IS THE WORN LIMESTONE PORCH FLOOR AND "
            "THE BASE OF ONE ROUND STONE COLUMN, OUT OF FOCUS."
        ),
    },
    {
        "id": "v2-r032-b44", "out": "s44-god-is-not-the-hard-man.jpeg",
        "seg": "n10", "window": "139.080-141.940", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": "God is not the hard man that servant imagined.",
        "must_show": "Jesus close, in profile under the olive canopy on the Olivet terrace, speaking quietly and gently — this is the correction to the accusation and his face carries it.",
        "must_not_show": _NO_HALO + "no town, city, wall, tower, dome, minaret, roofline or building anywhere; no night, no lamp, no flame, no sunset and no sunrise; no other person in the frame; " + _GAZE,
        "scene": (
            "One photograph, 135mm lens wide open, clear afternoon daylight coming from "
            "high on the LEFT and broken into soft moving patches by the olive leaves "
            "above him, the sun well up and OUT OF FRAME, the dry valley behind him "
            "dissolving into soft hazed shape, fine film grain. THE CAMERA IS STRICTLY "
            "SIDE-ON TO HIM AND SHOOTS ACROSS HIM AT RIGHT ANGLES: HE IS SEEN IN FULL "
            "PROFILE FACING LEFT, WITH HIS FAR CHEEK AND HIS FAR EYE COMPLETELY HIDDEN "
            "BEHIND HIS OWN HEAD, SO A GAZE INTO THE LENS IS GEOMETRICALLY IMPOSSIBLE. "
            "His one visible eye is level and steady and his gaze travels horizontally "
            "out of the frame through the LEFT EDGE, toward the men he is speaking to. "
            "He fills the frame from the chest up, seated, his head and shoulders against "
            "the out-of-focus tawny far hillside. His lips are parted on a quiet word "
            "and his expression is gentle, unhurried and completely without severity. "
            "The wool of his robe shows at the bottom of the frame with its "
            "over-and-under grid of warp and weft plainly visible. THE NEAR FOREGROUND "
            "IS ONE OUT-OF-FOCUS OLIVE BRANCH AND ITS SMALL GREY-GREEN LEAVES CROSSING "
            "THE BOTTOM RIGHT CORNER AND NOTHING ELSE."
        ),
    },
    {
        "id": "v2-r032-b45", "out": "s45-he-trusts-you-with-something-real.jpeg",
        "seg": "n10", "window": "141.940-145.140", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET", "DISCIPLES"],
        "narration": "He trusts you with something real, and he is longing",
        "must_show": "Jesus's hand extended open toward the seated men, and one of the disciples nearest the camera looking down at his own two empty open palms.",
        "must_not_show": _NO_HALO + "no town, city, wall, tower, dome, minaret, roofline or building anywhere; no night, no lamp and no flame; no money-bag, coin or silver in this frame; no woman and no child; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, clear afternoon light from high on the left "
            "broken by the olive leaves, the sun well up and OUT OF FRAME, fine film "
            "grain. THE CAMERA IS SET LOW BESIDE AND SLIGHTLY BEHIND THE SEATED "
            "DISCIPLES AND SHOOTS ACROSS AND PAST THEM toward Jesus, so the nearest men "
            "are seen from behind and from the side as dark backs and shoulders and NOT "
            "ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE, not a "
            "portrait: Jesus and at least four seated men are in frame together with the "
            "olive canopy above and the dry valley and bare tawny far hillside beyond. "
            "Jesus sits at the RIGHT of the frame in three-quarter view, his right hand "
            "reaching out and OPEN, palm up, extended toward the men; his gaze travels "
            "leftward along his own arm into the group and exits the frame through the "
            "LEFT EDGE. Sharp in the near left foreground, seen from behind and over his "
            "own shoulder, one seated disciple in a DEEP INDIGO tunic has both his own "
            "MALE hands turned up and open on his knees and his head bowed to look down "
            "into his empty palms, his gaze exiting through the BOTTOM EDGE. THE ONLY "
            "PALE WOOL IN THE WHOLE PICTURE IS JESUS'S OWN ROBE; every other man's back, "
            "shoulder and head cloth is a solid dark saturated mass of indigo, umber, "
            "rust, olive or charcoal, in focus and out of focus alike. THE NEAR "
            "FOREGROUND IS THAT ONE DARK INDIGO SEATED BACK AND THE DRY PALE DUST OF THE "
            "TERRACE."
        ),
    },
    {
        "id": "v2-r032-b46", "out": "s46-to-share-his-joy.jpeg",
        "seg": "n10", "window": "145.140-149.900", "wide": True, "jesus": False,
        "locks": ["MASTER", "ESTATE"] + _NIGHT,
        "narration": "to say to you, well done, and to share his joy.",
        "must_show": "the master's lamplit table laid for a meal with one place still empty, and the master standing at the open doorway looking out into the dark, waiting for whoever will come.",
        "must_not_show": _NO_JESUS + _NO_HALO + _NO_MODERN_LAMP + "no other person in the frame; no closed or barred door; nobody being turned away; no daylight; " + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, NIGHT — beyond the open doorway the courtyard "
            "and the sky are deep blue-black with stars and are lit by nothing. THE "
            "LIGHT COMES FROM FOUR SMALL SHALLOW TERRACOTTA OIL LAMPS with pinched "
            "spouts and single bare fibre wicks STANDING IN A LINE ALONG THE OAK TABLE "
            "ITSELF AT THE NEAR SIDE OF THE FRAME — LOW, WELL BELOW ANY CHIN, AND NEARER "
            "THE CAMERA THAN THE MAN'S HEAD — so their soft yellow light climbs UPWARD "
            "AND FORWARD across the laid table and the floor and up the lower walls, and "
            "the upper room, the roof and the whole of his head, hair and shoulders stay "
            "UNLIT AND DARK. THE CAMERA STANDS AT THE NEAR END OF THE TABLE BEHIND THE "
            "MASTER AND SHOOTS PAST HIM toward the open doorway, so he is seen ENTIRELY "
            "FROM BEHIND as a dark back and shoulders against the black opening, his "
            "face completely hidden and NOT TURNED TOWARD THE LENS. THIS IS A WIDE "
            "FULL-LENGTH SCENE and he is only a modest part of it. Sharp across the near "
            "foreground the long oak table is laid for a meal: round flat loaves torn "
            "and whole, three fired-clay bowls, one clay jar, and at the near right ONE "
            "PLACE PLAINLY STILL EMPTY — a bare stretch of table, an untouched bowl and "
            "an empty bench drawn up to it. Beyond, the master stands in his DEEP "
            "FOREST-GREEN robe and OXBLOOD-RED sash in the middle of the plain "
            "rectangular doorway, which STANDS WIDE OPEN on the dark, one hand resting "
            "on the jamb, looking out into the night. THE NEAR FOREGROUND IS THE LAMPS "
            "AND THE LAID TABLE."
        ),
    },
]
