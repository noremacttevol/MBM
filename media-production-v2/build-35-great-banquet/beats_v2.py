#!/usr/bin/env python3
"""V2 beat map — row 35, build-35-great-banquet (Luke 14:16-24). REALISTIC V2.

THE INHERITED SCAFFOLD WAS DISCARDED for a measured reason and is kept beside
this file as `beats_v2.py.inherited-scaffold` for provenance only: it planned 22
pictures at 5.8 s each and called that "the library density", against the wave's
measured 3.1-4.9 s per picture across rows 24-34. A picture costs about thirteen
cents and regenerates in seconds; a five-and-a-half second hold is the exact
defect V2 exists to remove.

WHAT V1 ACTUALLY DID (verified against the artefact, not the prose):
  SEVEN stills for 141.70 s of finished video. The holds are among the worst in
  the wave:
    * `s3-excuses.jpeg` covers j18 + n3 + n4 — 25.72 s to 52.71 s, TWENTY-SEVEN
      SECONDS on ONE picture, carrying the verbatim first excuse (Luke 14:18),
      the narrator's sweep through ALL THREE excuses, and the whole reflection on
      why they said no. Three different men, three different places, three
      different refusals — one picture.
    * `s7-table-full.jpeg` covers j2 + n9 + n10 — 101.42 s to 132.79 s, THIRTY-ONE
      AND A HALF SECONDS, i.e. the second red-letter command (Luke 14:23), its
      retelling, AND the entire closing application, the reason the video exists.
    * `s6-bringing-them-in.jpeg` covers n7 + j22 + n8 — 81.33 s to 100.04 s,
      NINETEEN SECONDS, including the servant's verbatim report (Luke 14:22).
    * `s1-feast-ready.jpeg` covers s16 + j16 + n1 — 0.28 s to 17.31 s, SEVENTEEN
      SECONDS, including the opening scripture and the opening red-letter line.
    * `s5-to-the-streets.jpeg` covers j1 + n6 — 62.28 s to 79.90 s, SEVENTEEN AND
      A HALF SECONDS, i.e. the longest red-letter line in the story plus its
      retelling.
  V2 gives all sixteen spoken segments their own pictures: 40 pictures over
  134.19 s = 3.35 s/picture.

AUDIO: LOCKED, never re-voiced. The V1 MP4 (141.700 s) and all seventeen mp3s
share ONE git content date (2026-07-27T23:05:57), and `make_narration.py` is
OLDER (2026-07-22T05:26:53), so the shipped audio was rendered after the script
and matches it. The summed V1 timeline is 141.700 s and the V1 audio stream is
141.688 s — 0.012 s INSIDE it, nowhere near the 0.75 s staleness tripwire.
Neither tripwire fires; the normal packet-copy AUDIO LOCK applies.

SOURCING TRAP CHECKED AND CLEARED: all 17 segments transcribed with faster-whisper
(small.en, word_timestamps=True) against the LIVE make_narration.py. Every one
matches word for word. There is not even a whisper mishearing to chase on this
row — the archaic KJV forms here ('bade', 'must needs', 'hither', 'maimed',
'halt', 'thou hast', 'compel') all came back correct, unlike row 33's 'an
hungred' and row 34's 'whose'. No TEXT_OVERRIDES.

WINDOWS: rebuilt from scratch from extract_beats plus the measured word timings.
The `.timing.json` sidecars are the usual trap — every one of the seventeen holds
ONE phrase spanning its whole segment, so not one of them could supply an
interior split. Contiguous 0.000 -> 134.190 (the card's own start), ZERO gaps,
shortest 2.12 s, longest 4.46 s, 3.35 s/picture, and all sixteen speech onsets
land inside the window written for them.

SCRIPTURE FACTS (Luke 14 KJV):
  14:1   The whole chapter happens at a SABBATH DINNER in the house of 'one of the
         chief Pharisees' — Jesus is himself reclining at a table when he tells
         this, answering a man who 'sat at meat with him'. That is why the framing
         beats are staged at a table and not on a hillside, and it is scripturally
         correct rather than invented.
  14:16  'A certain man made a great supper, and bade many' — an evening meal, so
         the parable runs from late golden afternoon into lamplight.
  14:18  'I have bought a piece of ground, and I must needs go and see it' — the
         only excuse quoted verbatim; the oxen (14:19) and the marriage (14:20)
         are retold by the narrator, so all three get their own frames anyway.
  14:21  'the poor, and the maimed, and the halt, and the blind.'
  14:22  'Lord, it is done as thou hast commanded, and yet there is room.'
  14:23  'Go out into the highways and hedges, and compel them to come in.'

WHY JESUS IS ON SCREEN FOR ONLY FOUR FRAMES: s16 and j16 are the frame of the
story, spoken by Jesus himself at the Pharisee's table, so he carries them. j18,
j1, j22 and j2 are red-letter but they are NOT Jesus speaking as himself — they
are the FIRST INVITED GUEST, the HOST and the SERVANT talking inside the parable.
Putting Jesus's face under a caption of a man refusing an invitation would be
worse than putting nothing there. Those are staged inside the parable where the
words are actually said. Jesus returns for the last two frames, where the
narrator's closing application is addressed to the listener.

CONTENT CARE: the remark that provokes this parable is 'Blessed is he that shall
eat bread in the KINGDOM OF GOD' (14:15) — and it is deliberately NOT in this
video's narration, so nothing in this build paints it. There is no heaven, no
throne, no gate, no crown, no cloud, no opening sky, no shaft of light from above
and no depiction of God as any figure, face, form or light. The great supper is a
real supper in a real house and the meaning lands on its own. 'Compel them to
come in' is staged as INSISTENT WELCOME — open hands, a servant crouched down to
a man's own level, a hand held out and taken — never as seizing, dragging,
binding or force, which would invert the verse. The poor, the maimed, the halt
and the blind are painted with dignity: real people, worn and thin, leaning on
hewn staves and crutches, never grotesque, never comic, never pitiable props. No
figure in this build carries a wound, a scar, blood, a glow or cream cloth, so
none can read as the crucified Christ (the row-31 lesson).

STAGING — seven places, none of them used elsewhere in the realistic wave:
  * the SABBATH DINING ROOM of a chief Pharisee where Jesus is reclining as he
    speaks (row 16's interior was a modest village house's living room; this is a
    well-off townsman's severe dining chamber with a low U-shaped table and
    reclining mats, in flat hard sabbath midday light);
  * the HOST'S BANQUET HALL, lit first by low gold afternoon light through open
    doorways and later by clay lamps alone;
  * the HOST'S OUTER COURTYARD and stone gateway;
  * a bought FIELD of stony hill terrace with upright boundary stones (row 25's
    was standing wheat, row 28's was ploughed loam, row 34's was reaped stubble —
    this is bare unworked fallow, and the lock says so positively);
  * an OX YARD with a byre, a yoke and a threshing sledge (deliberately NOT a
    ploughed field, so it cannot collide with row 28);
  * a BRIDE'S HOUSE in broad daylight with a red marriage cloth (row 31's
    bridegroom scene was at NIGHT lit only by hand lamps — this is broad
    afternoon, states 'no lamp, torch, candle or fire' outright, and shares no
    frame with it);
  * the TOWN'S STEPPED LANES and, beyond the wall, the HIGHWAY AND ITS THORN
    HEDGES at night.

NEW SHARED LOCK ADDED BY THIS ROW: BANQUET-HALL in v2_prompt.py. 'Banquet',
'feast', 'supper' and 'table' pull a MEDIEVAL OR VICTORIAN HALL — a long high
trestle with high-backed chairs, a white cloth, goblets, cutlery, a chandelier —
and PERIOD-MATERIALS cannot reach it, because a dining room is ARCHITECTURE AND
FURNISHING, not an object, the same way a road surface (row 29), a prison cell
(row 33) and a barn (row 34) slip through. Nothing anywhere in the shared recipe
says a word about a table's HEIGHT or about CHAIRS. See the comment above the
lock.

LOCK-WORDING AUDIT (the row-34 lesson: read every lock you write as if the model
will build the most modern thing your words permit). Every phrase below was read
back for invitations before the first paid image, and three were rewritten:
'hedges' was pinned to DRY GREY-BROWN PILED THORN because the bare word pulls a
clipped green English hedgerow; 'doorway' was everywhere stated as an opening
closed only by a HANGING PANEL OF CLOTH, because 'door' invites hinges; and the
BOUGHT-FIELD lock says NO CROP GROWS HERE outright, because 'field' invites
standing wheat.

CAST: THREE anchors, all of them pictures that already had to exist on the
timeline, so the anchors cost nothing extra. All three are generated in ONE
anchor run before anything else, and NONE of the three has another anchor in its
frame, so the REFS cache cannot make an anchor reference itself.
  b04 HOST        — face-showing, strict side-on profile, alone in his hall.
  b07 SERVANT     — face-showing, strict side-on profile, alone in the courtyard.
  b09 FIRST-GUEST — face-showing, strict side-on profile, alone on his threshold
                    (the servant he is answering stands OFF-frame to the left).
Jesus needs no anchor: he carries JESUS-V2-REF on every frame he is in.
"""

import os

OUTPUT_ASSET_DIR = "assets"

# The V1 MP4 (141.700 s) and all seventeen mp3s share ONE git content date
# (2026-07-27T23:05:57); make_narration.py is older, so the audio post-dates the
# script. The summed timeline is 141.700 s and the V1 stream is 141.688 s, i.e.
# 0.012 s INSIDE it. Neither staleness tripwire fires; the normal packet-copy
# AUDIO LOCK applies. Nothing is re-voiced and V1 is never written to.
AUDIO_FROM_V1_SEGMENTS = False

REF = True

# Wired in AFTER the three anchor beats are generated in their own run.
A_HOST = "assets/s04-he-made-a-great-supper.jpeg"
A_SERV = "assets/s07-he-sent-his-servant.jpeg"
A_GUEST = "assets/s09-bought-a-piece-of-ground.jpeg"
REFS = {"HOST": A_HOST, "SERVANT": A_SERV, "FIRST-GUEST": A_GUEST}

_HERE = os.path.dirname(os.path.abspath(__file__))


def _have(rel):
    """ANCHOR-FIRST: a character reference attaches only once its anchor exists.

    On the first (anchor-only) run every list below is empty, so `--check` passes
    and no anchor can reference itself through the REFS cache. Every run after it
    wires the accepted anchors into all the later beats automatically.
    """
    return [rel] if os.path.isfile(os.path.join(_HERE, rel)) else []


_HOST = _have(A_HOST)
_SERV = _have(A_SERV)
_GUEST = _have(A_GUEST)
_HOST_SERV = _HOST + _SERV

# ---------------------------------------------------------------- negatives ---
_NO_CREAM = ("no cream, off-white, ivory, buff, beige, taupe, sand, khaki, white "
             "or pale garment, tunic, robe, mantle, sash, wrap or head covering on "
             "anybody anywhere in the frame including the blurred edges; ")
_NO_HALO = ("no halo, no nimbus, no aura, no corona, no bright outline, edge or "
            "contour around any head, hair, shoulder or body, and no light source "
            "of any kind standing behind, above or beyond anyone's head; ")
_NO_HEAVEN = ("no heaven, sky kingdom, throne, seat of judgement, crown, gate of "
              "pearl, golden street, cloud of glory, opening sky, shaft of light "
              "from above, radiance, angel, wing or winged figure anywhere; no "
              "hand, arm or face reaching down from the sky; and no depiction of "
              "God as any figure, face, form, light or presence; ")
_NO_MODERN_DINE = ("no chair, high-backed chair, stool, bench or seat with a back; "
                   "no tall or waist-high table, trestle or refectory board; no "
                   "tablecloth, runner, napkin or placemat; no glass, stemware, "
                   "goblet, chalice or decanter; no silver, pewter, brass or gold "
                   "plate, charger, tray or serving dish; no knife, fork, spoon or "
                   "cutlery laid for a diner; no candle, candlestick, candelabra, "
                   "chandelier or metal hanging fixture; no fireplace, mantel, "
                   "panelling, cornice, moulding, framed picture, mirror or "
                   "pictorial tapestry; ")
_NO_MODERN_TOWN = ("no dome, minaret, bell tower, spire, clock, crenellation, "
                   "pitched roof, roof tile, shingle, chimney, gable or "
                   "half-timbering against any sky; no pole, mast, pylon, wire, "
                   "cable, aerial, guardrail, signpost or painted sign; no "
                   "asphalt, tarmac, concrete, kerb, gutter, drain, grating or "
                   "painted road marking; no vehicle, wheel of pneumatic rubber, "
                   "engine or machine of any kind; ")
_NO_GREEN = ("no green meadow, lawn, turf, pasture, moor, fell, upland, heather, "
             "clipped green hedgerow, deciduous woodland or lush temperate "
             "countryside of any kind, and no soft grey overcast northern European "
             "sky; ")
_NO_NIGHT = ("no night, no darkness, no stars, no lamp and no flame anywhere in "
             "this frame; ")
_NO_MODERN_LAMP = ("no candle, wax or taper, no glass, chimney, globe or shade, no "
                   "hurricane lamp, storm lantern, kerosene lamp or oil lantern, no "
                   "metal lamp, no hanging fixture, no ring handle, and no electric "
                   "light of any kind; ")
_NO_FORCE = ("nobody is seized, grabbed by the clothing, dragged, hauled, pushed, "
             "struck, bound, roped, chained or restrained, and no hand grips any "
             "person against their will — the welcome is insistent and open-handed, "
             "never violent; ")
_NO_MOCK = ("nobody who is poor, lame or blind is drawn grotesque, comic, "
            "monstrous, deformed beyond what the narration says, filthy, ragged to "
            "indecency, cowering or pitiable; each is a real person with dignity; "
            "and no modern wheelchair, walking frame, prosthesis, crutch of "
            "manufactured metal, bandage of white gauze or medical dressing "
            "appears anywhere; ")
_GAZE = "nobody's pupils centred on the lens."

# Common lock stacks.
_HALL_DAY = ["BANQUET-HALL", "HOUSE", "HOST", "BACKGROUND-CAST"]
_HALL_LAMP = ["BANQUET-HALL", "HOUSE", "HOST", "NIGHT-LAMPLIGHT", "BACKGROUND-CAST"]
_TABLE_JESUS = ["BANQUET-HALL", "PHARISEE-HOUSE", "DINNER-COMPANY"]

LOCKS = {
    # ------------------------------------------------------------- people ----
    "HOST": (
        "HOST LOCK: the man who made the great supper is the SAME MAN in every "
        "picture he appears in, and he is a JUDEAN of the first century, born and "
        "weathered in the dry country of that place. He is about fifty, tall and "
        "square-shouldered, still upright, a prosperous householder rather than a "
        "soft idler. HIS SKIN IS WARM SUN-DARKENED OLIVE-BROWN, clearly Middle "
        "Eastern, lined across the forehead and at the outer corners of dark brown "
        "eyes, with a straight strong nose and level dark brows. He has a FULL "
        "BEARD, dark brown going grey at the chin, trimmed neat and square and "
        "reaching the top of his chest. HIS HAIR IS THICK, DARK BROWN AND GREYING "
        "AT THE TEMPLES, waving back off a high forehead to the nape of his neck; "
        "it is never a bare, bald, shaven, cropped or thinning head, and a clear "
        "band of that thick greying hair shows at the front edge, at the temples "
        "and at the nape in EVERY shot of him, INCLUDING EVERY SHOT TAKEN FROM "
        "BEHIND HIM. His hands are broad, clean and steady, with a working man's "
        "knuckles. HE WEARS EXACTLY THREE SEPARATE PIECES OF CLOTH AND NOTHING "
        "ELSE: (1) ONE ankle-length hand-woven wool tunic in DEEP MADDER RED with "
        "straight unshaped sleeves to the wrist; (2) ONE rectangular hand-woven "
        "wool mantle in DEEP INDIGO thrown over the left shoulder and hanging down "
        "his back; and (3) ONE folded cloth sash of DARK UMBER knotted at his "
        "waist. On his feet, good leather sandals. HE NEVER WEARS CREAM, "
        "OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE CLOTH, and "
        "he wears no head covering, no turban, no cap, no crown, no jewellery, no "
        "ring, no brooch, no clasp, no chain and no belt of manufactured metal. He "
        "is a healthy living man in every frame: no wound, no scar, no blood, no "
        "bandage, no glow and no light of any kind coming off him."
    ),
    "SERVANT": (
        "SERVANT LOCK: the servant sent out with the invitations is the SAME MAN in "
        "every picture he appears in, and he is a JUDEAN of the first century. He "
        "is about twenty-eight, lean, wiry and quick, a head shorter and far "
        "slighter than the host, and NOBODY EVER MISTAKES ONE FOR THE OTHER. HIS "
        "SKIN IS WARM SUN-DARKENED OLIVE-BROWN, clearly Middle Eastern, smooth "
        "across the cheeks with the beginnings of lines at the eyes, a narrow "
        "straight nose and quick dark brown eyes. He has a SHORT CLOSE-CROPPED "
        "DARK BEARD following the jaw, and SHORT THICK BLACK CURLY HAIR cut close "
        "to the skull — never long, never to the shoulders, never straight — and a "
        "clear cap of that short black curl is visible at the crown, the temples "
        "and the nape in EVERY shot of him, INCLUDING EVERY SHOT TAKEN FROM BEHIND "
        "HIM. HE WEARS EXACTLY TWO SEPARATE PIECES OF CLOTH AND NOTHING ELSE: "
        "(1) ONE knee-length hand-woven wool work tunic in DARK OLIVE with short "
        "straight unshaped sleeves, hitched up at the thigh and tucked into "
        "(2) ONE twisted cloth belt of DEEP RUST at his waist. He is barefoot or "
        "in worn plain leather sandals. HE NEVER WEARS CREAM, OFF-WHITE, IVORY, "
        "BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE CLOTH, and no head covering, "
        "no cap, no jewellery and no metal ornament of any kind. He is always in "
        "the middle of doing something — walking, calling, stooping, reaching — "
        "and never posing. He carries no wound, scar, blood, bandage or glow."
    ),
    "FIRST-GUEST": (
        "FIRST-GUEST LOCK: the first invited man, the one who says he has bought a "
        "piece of ground, is the SAME MAN in every picture he appears in, and he "
        "is a JUDEAN of the first century. He is about forty, of middling height "
        "and comfortably built, plainly well-off. HIS SKIN IS WARM OLIVE-BROWN, "
        "clearly Middle Eastern, less weathered than a field hand's, with a "
        "rounded nose, full cheeks and dark brown eyes set close under heavy "
        "brows. He has a FULL SOFT BLACK BEARD without grey in it, and THICK BLACK "
        "WAVY HAIR to the middle of the neck, parted and pushed back, with a clear "
        "band of it visible at the temples and the nape in EVERY shot of him, "
        "INCLUDING EVERY SHOT TAKEN FROM BEHIND HIM. HE WEARS EXACTLY THREE "
        "SEPARATE PIECES OF CLOTH AND NOTHING ELSE: (1) ONE ankle-length "
        "hand-woven wool tunic in DARK OLIVE-GREEN; (2) ONE rectangular hand-woven "
        "wool mantle in DEEP MAROON over both shoulders; and (3) ONE folded cloth "
        "sash of CHARCOAL at his waist. Good leather sandals. HE NEVER WEARS "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, WHITE OR ANY PALE "
        "CLOTH, and no head covering, no jewellery and no metal ornament. His "
        "manner is polite and evasive, not angry: the hands make a small "
        "apologetic gesture while the body is already turned away."
    ),
    "OTHER-EXCUSERS": (
        "OTHER-EXCUSERS LOCK: the second and third invited men are two DIFFERENT "
        "Judean men of the first century, each appearing in his own frame, and "
        "neither of them shares a face with the other, with the first guest, with "
        "the host or with the servant. THE OX-BUYER is about thirty-five, big "
        "through the shoulders and heavily muscled, with sun-darkened olive-brown "
        "skin, a broad flat nose, a short thick black beard and short black hair, "
        "wearing ONE calf-length hand-woven wool work tunic in DARK UMBER hitched "
        "into ONE twisted cloth belt of CHARCOAL, and nothing else. THE BRIDEGROOM "
        "is about twenty-two, slim and smooth-faced with only a light young dark "
        "beard just coming in, warm olive-brown skin and short black curling hair, "
        "wearing ONE ankle-length hand-woven wool tunic in DEEP RUST-RED under ONE "
        "rectangular mantle of DARK INDIGO, with ONE sash of dark olive. NEITHER "
        "OF THEM EVER WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, SAND, KHAKI, "
        "WHITE OR ANY PALE CLOTH, and neither wears a crown, jewellery or metal "
        "ornament of any kind."
    ),
    "GUESTS": (
        "INVITED-GUESTS LOCK: the men first invited to the great supper are between "
        "two and five well-off Judean householders of the first century, aged from "
        "about thirty to about sixty, each with weathered warm olive-brown Middle "
        "Eastern skin, dark hair and a dark beard, and no two of them share a face. "
        "Every one of them is dressed head to foot in ONE SOLID DARK SATURATED "
        "EARTH COLOUR — DEEP INDIGO, DARK UMBER, DEEP RUST, DARK OLIVE, CHARCOAL "
        "or DEEP MAROON — so every guest in the frame, in focus or out of focus, "
        "near or far, is a DARK MASS from edge to edge. NOT ONE OF THEM WEARS "
        "CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE OR PALE "
        "GREY CLOTH, DRAPE, MANTLE, SHAWL, TUNIC, SASH OR HEAD COVERING. THE ONLY "
        "LIGHT-TONED THINGS ANYWHERE IN THE FRAME ARE BARE STONE, PLASTER, DUST, "
        "REED BASKETRY, RAW TIMBER, FLAT BREAD AND BARE SKIN."
    ),
    "DINNER-COMPANY": (
        "SABBATH-DINNER-COMPANY LOCK: the men reclining with Jesus at the chief "
        "Pharisee's sabbath table are between three and six Judean men of the "
        "first century, aged from about thirty-five to about sixty-five, learned "
        "and well-off, each with warm olive-brown Middle Eastern skin, a full dark "
        "or greying beard and no two sharing a face. Every one of them is dressed "
        "head to foot in ONE SOLID DARK SATURATED COLOUR — DEEP INDIGO, DARK "
        "UMBER, DEEP RUST, DARK OLIVE, CHARCOAL or DEEP MAROON — so that in this "
        "room THE ONLY PALE WOOL IN THE PICTURE IS JESUS'S OWN ROBE. NOT ONE OF "
        "THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, "
        "WHITE OR PALE GREY CLOTH OF ANY KIND, at any distance and at any focus — "
        "a pale figure at this table reads as a second, unlocked Jesus and fails "
        "the picture. They recline propped on the LEFT elbow around the low table, "
        "listening; they are not arranged for a camera and none of them faces it."
    ),
    "POOR": (
        "POOR-AND-INVITED LOCK: the people the servant brings in are ordinary "
        "first-century Judean poor of that town and that road, and they are "
        "painted with DIGNITY. They are men and women together, from about "
        "eighteen to about seventy, all with warm sun-darkened olive-brown Middle "
        "Eastern skin, dark hair and dark eyes, thin in the face and worn by hard "
        "living but upright and human, and no two of them share a face. EACH WEARS "
        "EXACTLY ONE OR TWO SEPARATE PIECES OF CLOTH AND NOTHING ELSE: one "
        "calf-length hand-woven wool tunic, faded, patched and mended with plainly "
        "visible stitching, and for some ONE rectangular wool mantle over the "
        "shoulders — and every piece is ONE SOLID DARK MUTED EARTH COLOUR: DARK "
        "UMBER, CHARCOAL, DEEP RUST, DARK OLIVE, DEEP INDIGO or DEEP MAROON, faded "
        "but never pale. NOT ONE OF THEM WEARS CREAM, OFF-WHITE, IVORY, BUFF, "
        "BEIGE, TAUPE, SAND, KHAKI, WHITE OR PALE GREY CLOTH. Most are barefoot; a "
        "few have worn leather sandals. HEAD COVERING IS STATED POSITIVELY: where a "
        "woman covers her hair she does it with ONE FOLD OF HER OWN MANTLE drawn up "
        "over the head, in exactly the same dark colour as the rest of her cloth, and "
        "NOBODY IN THIS PICTURE WEARS A SEPARATE SCARF, VEIL, WRAP, SHAWL, TURBAN OR "
        "HEAD CLOTH OF ITS OWN, and least of all a pale one: there is no cream, "
        "off-white, ivory, buff, beige, sand, khaki or pale grey head covering on any "
        "person anywhere in the frame. WHERE THE NARRATION NAMES THEM: a LAME man "
        "leans his weight on ONE SINGLE hand-hewn wooden staff or ONE SINGLE forked "
        "branch tucked under ONE armpit — ONE stick only, never a matched PAIR of "
        "underarm crutches, which reads as a modern hospital crutch and fails the "
        "picture; "
        "and a BLIND man's eyes are simply clouded pale and unfocused, with his "
        "hand out ahead of him reading the air or resting on a companion's "
        "shoulder. NOBODY IS GROTESQUE, COMIC, MONSTROUS OR PITIABLE, nobody is "
        "filthy, nobody is ragged to indecency, and there is no modern wheelchair, "
        "walking frame, prosthesis, metal crutch, white gauze bandage or medical "
        "dressing anywhere in the picture."
    ),
    # ------------------------------------------------------------- places ----
    "HOUSE": (
        "HOST-HOUSE LOCK: the great supper is held in a well-off first-century "
        "JUDEAN townhouse built round a courtyard. Its outer wall is dressed "
        "limestone blocks below and mud brick plastered pale tan above, with a "
        "FLAT roof of poles and packed earth and an outside stone stair climbing "
        "to it. The COURTYARD inside is a square of worn flagstones and beaten "
        "earth with a stone water trough and a fig tree in one corner, entered "
        "through ONE wide gateway of plain squared stone jambs and a plain stone "
        "lintel, closed only by a heavy hanging panel of dark woven goat-hair "
        "cloth. From the courtyard ONE broad plain rectangular opening, also "
        "curtained with the SAME DARK GOAT-HAIR CLOTH, leads into the dining "
        "chamber. EVERY HANGING IN THIS HOUSE IS DARK — deep umber, charcoal or "
        "near-black undyed goat hair, heavy, coarse and matte. NO HANGING, "
        "CURTAIN, DRAPE OR PANEL ANYWHERE IN THIS BUILDING IS CREAM, OFF-WHITE, "
        "IVORY, BUFF, BEIGE, PALE GOLD, LINEN-COLOURED OR ANY LIGHT TONE, and "
        "none of them is a sheer, gathered, pleated or floor-pooling modern "
        "curtain hung on a rail. Everything is "
        "hand-built from the stone, mud brick, timber and cloth of that place. "
        "THERE IS NO ARCH OF DRESSED VOUSSOIRS, no column with a carved capital, "
        "no pediment, no carved stone ornament, no glass in any opening, no hinged "
        "or panelled door, no iron gate, no lock, hasp, latch, bolt, hinge or "
        "metal fitting on any opening, no tiled or pitched roof, no chimney and no "
        "lettering, numeral or sign anywhere on the building."
    ),
    "PHARISEE-HOUSE": (
        "PHARISEE-SABBATH-ROOM LOCK: this is the dining chamber of a CHIEF "
        "PHARISEE on the sabbath, and it is quieter, plainer and more severe than "
        "the great supper's hall — a smaller square room of dressed limestone "
        "washed pale, with a low flat ceiling on three rough hewn beams, ONE plain "
        "rectangular window opening high in one wall with NO GLASS in it, and flat "
        "hard midday sabbath light falling through it in one clean shaft onto the "
        "floor, never onto anybody's head from behind. The floor is worn flagstone "
        "spread with two dark hand-woven wool mats. In the middle stands ONE low "
        "U-shaped table of adzed timber slabs on short hewn legs, KNEE HIGH, with "
        "flat rounds of bread laid straight on the bare wood, a shallow clay bowl "
        "of olives, a fired-clay wine jar and plain unstemmed clay cups, and low "
        "bolsters and folded mats laid on the floor around three sides for "
        "reclining, the fourth side left open. ONE plain undyed woven hanging is "
        "on the wall and NOTHING ELSE: no picture, no mirror, no pictorial "
        "tapestry, no shelf of ornaments, no chair, stool, bench or seat with a "
        "back, no tall table, no cloth on the table, no glass, no metal vessel, no "
        "cutlery and no hanging fixture of any kind."
    ),
    "JUDEAN-LAND": (
        "JUDEAN-LAND LOCK: this is the dry limestone farming country of "
        "first-century JUDEA in the hot part of the year, and the land is stated "
        "positively. The ground is pale chalky limestone breaking through thin "
        "stony soil in bald shelves and slabs, with dry straw-gold grass, thistle, "
        "thorn scrub and dusty grey-green olive, fig and terebinth trees. "
        "Everything is in the colours of drought: bleached gold, straw, tan, pale "
        "ochre and dust grey. Low dry-stone terraces of unmortared limestone step "
        "down every slope. THE SKY BY DAY IS THE HARD CLEAR PALE BLUE OF A HOT DRY "
        "COUNTRY, whitening toward the horizon. THERE IS NO GREEN COUNTRYSIDE "
        "ANYWHERE IN THIS FRAME: no green grass, lawn, turf, meadow, pasture, "
        "moor, fell, upland, heather, bracken, clipped hedge, deciduous wood, oak, "
        "birch, pine forest, fern, ivy, rolling green hill or lush temperate "
        "valley, and no soft grey overcast northern sky. Nothing in this picture "
        "is Britain, Ireland, Scandinavia, the Alps or the American Midwest."
    ),
    "BOUGHT-FIELD": (
        "BOUGHT-FIELD LOCK: the piece of ground the first guest has bought is a "
        "stony hillside FALLOW — bare pale tan and grey stony soil lying unsown "
        "and unploughed, its surface loose with limestone chips and flints, dry "
        "straw-gold weeds and thistles standing in it, and pale bedrock showing "
        "through in shelves. It is held by low unmortared DRY-STONE TERRACE WALLS "
        "of rough field limestone stacked by hand without mortar, and its corners "
        "are marked by upright unworked BOUNDARY STONES — plain rough limestone "
        "slabs set on end in the earth, uncarved and unlettered. NO CROP GROWS "
        "HERE: this ground is bare and unworked, and it is NOT a field of standing "
        "wheat or barley, NOT a ploughed loam of turned dark furrows and NOT cut "
        "stubble. There is NOTHING BUILT ON IT: no fence, post, rail, wire, "
        "netting, gate, stake, marker peg, clipped hedge, concrete ditch, tyre "
        "track or machine of any kind, and no writing, numeral or sign on any "
        "stone anywhere in the frame."
    ),
    "OX-YARD": (
        "OX-YARD LOCK: the yard where the oxen are tried is a flat swept apron of "
        "packed pale tan earth beside a low mud-brick byre with a FLAT roof of "
        "poles and packed earth, ringed by a waist-high unmortared dry-stone wall "
        "with ONE gap for a gateway closed by a single bar of hewn timber dropped "
        "into two stone sockets. In it stand EXACTLY FOUR OXEN AND NO MORE — big "
        "dun-brown and grey humped working cattle with wide horns, two of them "
        "yoked together under ONE hand-hewn wooden neck yoke of a shaped timber "
        "beam with four wooden pegs and twisted flax lashings, and two standing "
        "loose. Around them lies the plain hand-made gear of that work: a "
        "hand-hewn ard plough of a single crooked timber with an iron-shod point, "
        "a threshing sledge of adzed planks studded with flint, coils of twisted "
        "flax rope, hand-woven reed baskets and a fired-clay water trough. THERE "
        "IS NO MACHINE, TRACTOR, TRAILER, CART OF PNEUMATIC TYRES, METAL GATE, "
        "WIRE FENCE, CHAIN, BUCKLE, RIVETED HARNESS, PAINTED SURFACE OR PRINTED "
        "MARK ANYWHERE IN THIS YARD, and no ploughed field of turned dark loam "
        "anywhere in the frame."
    ),
    "BRIDE-HOUSE": (
        "BRIDE-HOUSE LOCK: the newly married man's house is a small first-century "
        "Judean village house of mud brick plastered pale tan on a limestone "
        "footing, with a FLAT roof of poles and packed earth and ONE plain "
        "rectangular opening for a doorway with no door in it. IT IS BROAD "
        "AFTERNOON DAYLIGHT and the scene is lit by the sun alone: there is NO "
        "lamp, torch, candle, flame or fire anywhere in this frame, no night, no "
        "darkness and no stars. Over the doorway hangs ONE rectangle of hand-woven "
        "wool dyed DEEP MADDER RED, the marriage cloth, still fresh, with a plain "
        "twisted flax cord and a few dry wildflowers tied at one corner; ONE "
        "hand-woven reed basket of figs and almonds and ONE fired-clay jar stand "
        "on the doorstep. THERE IS NO PROCESSION, NO LAMP-LIT WAITING, NO CROWD "
        "CARRYING LIGHTS and no torchlit arrival of a bridegroom anywhere in this "
        "picture. There is no glass, no hinged or panelled door, no metal fitting, "
        "no printed or patterned fabric, no flowers arranged in a vase, no ribbon, "
        "no bunting and no lettering anywhere."
    ),
    "TOWN-LANES": (
        "TOWN-LANES LOCK: the streets and lanes are the narrow ways of a small "
        "first-century Judean town, and they are stated positively. A lane is a "
        "gap barely two men wide between plain mud-brick and dressed-limestone "
        "house walls plastered pale tan, its floor bare packed earth and worn "
        "limestone with shallow hand-cut steps where the ground climbs, its sides "
        "littered with a broken clay jar, a pile of swept dust and a coil of flax "
        "rope. Above, the FLAT rooflines of poles and packed earth almost meet, "
        "leaving one ragged strip of sky between them, and outside stone stairs "
        "climb the walls to those roofs. Plain rectangular door and window "
        "openings with NO GLASS are cut into the walls, closed only by hanging "
        "panels of dark woven cloth. EVERY OPENING IN EVERY WALL OF THIS TOWN IS "
        "SPANNED BY ONE PLAIN FLAT LINTEL — a single squared limestone block or one "
        "hewn timber beam laid straight across the top of a plain rectangular gap — "
        "so every doorway, window and passage in the frame is a RECTANGLE, and not "
        "one opening anywhere is curved, rounded, vaulted or arched. THERE IS "
        "NOTHING BUILT OR FITTED THAT IS NOT "
        "STONE, MUD BRICK, TIMBER, CLAY OR CLOTH: no arch of dressed voussoirs, no "
        "carved capital, no dome, minaret, bell tower, spire, clock, crenellation, "
        "pitched roof, roof tile, shingle, chimney or gable; no cobbled setts or "
        "laid regular paving, no kerb, gutter, drain, grating or culvert; no pole, "
        "wire, cable, aerial, rail, gate, hinge or fitting of manufactured metal; "
        "no painted sign, notice, lettering or numeral anywhere; and no modern "
        "person, garment, footwear or object."
    ),
    "HIGHWAY-HEDGES": (
        "HIGHWAY-AND-HEDGES LOCK: outside the town wall the way is a first-century "
        "highway and it is nothing but GROUND — bare packed earth and pale dust "
        "worn hollow by feet and hooves, bedrock breaking through, loose stones "
        "kicked to the sides. THE HEDGES BESIDE IT ARE EXACTLY WHAT THE WORD MEANS "
        "IN THAT COUNTRY: rough banks and low unmortared dry-stone walls topped "
        "with cut and piled THORN — dry grey-brown bramble, boxthorn and "
        "camel-thorn heaped and interlaced as a stock barrier, spiny, irregular, "
        "leafless and half dead, with dry straw-gold grass and thistle at the "
        "foot. THEY ARE NOT A CLIPPED GREEN ENGLISH HEDGEROW, not privet, not box, "
        "not beech, not laurel, not a trimmed garden hedge and not green at all. "
        "In the lee of those thorn banks are the rough sleeping places of people "
        "with nowhere else: a hollow scraped in the earth, a scrap of dark woven "
        "cloth pegged to two hewn sticks, a few stones ringing a dead fire. THERE "
        "IS NOTHING MANUFACTURED BESIDE THIS ROAD: no asphalt, kerb, painted line "
        "or tyre rut; no post, pole, pylon, telegraph pole, wire, cable, fence of "
        "wire or milled rail, guardrail, gate, signpost or milestone board; and no "
        "vehicle of any kind but a hand-built wooden cart on hewn spoked wheels."
    ),
}

BEATS = [
    # ============ s16 — Luke 14:16a, LUKE writing (light blue) ================
    {
        "id": "v2-r035-b01", "out": "s01-then-said-he-unto-him.jpeg",
        "seg": "s16", "window": "0.000-3.277", "wide": True, "jesus": True, "ref": REF,
        "locks": _TABLE_JESUS,
        "narration": "Then said he unto him,",
        "must_show": "Jesus reclining at the low U-shaped table in the chief Pharisee's plain sabbath dining room, turning his head to answer one of the men reclining with him, in flat hard midday light.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, flat hard sabbath midday light falling "
            "through ONE high plain window opening in one clean shaft onto the "
            "flagstone floor and the near edge of the table, the sun itself well "
            "out of frame and NEVER behind any head, fine film grain, true depth "
            "of field. THE CAMERA STANDS BEHIND AND ABOVE THE OPEN FOURTH SIDE OF "
            "THE TABLE AND SHOOTS DOWN AND ACROSS IT: the two nearest reclining "
            "men fill the lower LEFT of the frame as dark heads, shoulders and "
            "backs seen entirely FROM BEHIND, and NOT ONE FACE IS TURNED TOWARD "
            "THE LENS. Jesus reclines on the far side of the table, right of "
            "centre, propped on his LEFT elbow on a low dark bolster with his feet "
            "away from the table behind him, seen in three-quarter view; he has "
            "just turned his head to his own right toward the man beside him, and "
            "his gaze travels level and to the RIGHT and exits the picture through "
            "the RIGHT EDGE. His right hand rests open and low on the table's edge "
            "beside a flat round of barley bread. THIS IS A WIDE FULL-LENGTH GROUP "
            "PHOTOGRAPH AND NOT A PORTRAIT: the camera is far enough back that "
            "five men and the whole low table are in frame together, with the bare "
            "pale limestone walls and the low beamed ceiling above them. THE ONLY "
            "PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; every other man is a "
            "solid dark saturated mass of indigo, umber, rust, olive, charcoal or "
            "maroon from edge to edge, in focus and out of focus alike."
        ),
    },
    # ============ j16 — Luke 14:16b, JESUS speaking (RED) =====================
    {
        "id": "v2-r035-b02", "out": "s02-a-certain-man.jpeg",
        "seg": "j16", "window": "3.277-5.400", "wide": False, "jesus": True, "ref": REF,
        "locks": _TABLE_JESUS,
        "narration": "A certain man made a great supper,",
        "must_show": "A close side-on view of Jesus at the Pharisee's table beginning to tell the parable, one hand lifted low and open at his own chest as he speaks.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 85mm lens, the same flat hard sabbath daylight coming "
            "in almost level from the LEFT and modelling the face from the front, "
            "fine film grain, shallow but honest depth of field. THIS IS A STRICT "
            "SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: Jesus is "
            "seen half-length at the RIGHT of the frame, propped on his left elbow "
            "and turned fully to the LEFT, so the viewer sees ONE cheek, ONE eye, "
            "ONE ear and the clean outline of brow, nose, lips and beard against "
            "the pale limestone wall beyond. THE FAR CHEEK AND THE FAR EYE ARE "
            "COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF HIS "
            "HEAD and cannot be seen at all; his one visible eye looks steadily "
            "and level to the LEFT at the man he is answering and exits the "
            "picture through the LEFT EDGE, so his pupils are nowhere near the "
            "lens. His right hand is lifted low and open at his own chest height, "
            "palm up, in the small gesture of a man beginning a story. Across the "
            "bottom third of the frame, close to the camera and softly out of "
            "focus, runs the near edge of the KNEE-HIGH adzed-timber table with a "
            "flat round of barley bread and a plain unstemmed clay cup on it. "
            "Behind him one dark-clad shoulder of another reclining man is turned "
            "away into the shadow. His hair, beard, eyes and robe are exactly as "
            "locked."
        ),
    },
    {
        "id": "v2-r035-b03", "out": "s03-and-bade-many.jpeg",
        "seg": "j16", "window": "5.400-7.947", "wide": True, "jesus": False,
        "locks": _HALL_DAY + ["SERVANT", "JUDEAN-LAND"], "char_refs": _HOST_SERV,
        "narration": "and bade many:",
        "must_show": "The host standing in his own courtyard gateway having just handed out the invitations, his servant setting off out through the gate with them while the host looks after him.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming in "
            "almost level from the LEFT through the open gateway and lighting both "
            "men from the front, the sun well out of frame and never behind any "
            "head, fine film grain. THE CAMERA STANDS INSIDE THE COURTYARD BEHIND "
            "AND TO THE RIGHT OF THE HOST AND SHOOTS PAST HIM out through the "
            "gateway: the host is in the near RIGHT foreground seen in "
            "three-quarter FROM BEHIND, three-quarter length, only the back and "
            "side of his head in frame, his deep indigo mantle down his back over "
            "his deep madder red tunic, his face turned away toward the gate and "
            "NOT visible to the camera. BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS "
            "HAIR IS THE THING THE VIEWER SEES OF HIM AND IT IS STATED HERE: thick "
            "dark brown hair going iron grey at the temples, waving back off the "
            "crown and curling onto the nape of his neck and the top of his mantle "
            "— it is NOT a bare, bald, shaven, cropped or thinning head, and he "
            "wears nothing on it. In the middle distance his servant is already "
            "three paces out through the gateway, seen from the side and moving "
            "LEFT ACROSS THE FRAME AND AWAY, his short black curls bare, his dark "
            "olive work tunic hitched into its deep rust belt, a small stack of "
            "folded cloth invitation squares held against his chest in one hand. "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH "
            "SCENE: the camera is far enough back that both men are visible head "
            "to sandals, with the plain squared stone jambs and lintel of the "
            "gateway framing the bright dusty lane and dry stony hill country "
            "beyond."
        ),
    },
    # ============ n1 — the feast is prepared ==================================
    {
        # ANCHOR BEAT — HOST. Generated in the anchor run before every other beat,
        # so the REFS cache cannot make this picture reference itself. No char_refs
        # and nobody else in the frame.
        "id": "v2-r035-b04", "out": "s04-he-made-a-great-supper.jpeg",
        "seg": "n1", "window": "7.947-11.370", "wide": False, "jesus": False,
        "locks": ["BANQUET-HALL", "HOUSE", "HOST"],
        "narration": "A man threw a great feast. He prepared everything,",
        "must_show": "The host standing alone in his own dining hall looking over the low U-shaped table he has had laid for a great supper, his face clearly visible in strict side-on profile.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, warm low late-afternoon sun coming in "
            "almost level from the LEFT through a broad open doorway and modelling "
            "the face from the front, fine film grain, shallow but honest depth of "
            "field. THIS IS A STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY "
            "ON HIS LEFT: the host stands three-quarter length at the RIGHT of the "
            "frame turned fully to the LEFT, so the viewer sees ONE cheek, ONE "
            "eye, ONE ear and the clean outline of brow, nose, lips and beard "
            "against the pale plastered wall beyond. THE FAR CHEEK AND THE FAR EYE "
            "ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF "
            "HIS HEAD and cannot be seen at all; his one visible eye looks steadily "
            "down and away to the LEFT along the length of the table and exits the "
            "picture through the LEFT EDGE, so his pupils are nowhere near the "
            "lens. His face is quiet satisfaction, not devotion: the brows easy, "
            "the mouth just short of a smile, one broad hand resting flat on the "
            "adzed timber. His deep madder red tunic, deep indigo shoulder mantle "
            "and dark umber waist sash are all clearly readable, and his thick "
            "dark brown hair, iron grey at the temple, is lit along the top. HE IS "
            "THE ONLY PERSON IN THE PICTURE. Across the lower third, close to the "
            "camera and softly out of focus, runs the KNEE-HIGH adzed-timber table "
            "laid ready: flat rounds of bread straight on the bare wood, shallow "
            "fired-clay bowls of olives and figs, a plain fired-clay wine jar and "
            "unstemmed clay cups, with low dark bolsters and folded wool mats on "
            "the floor beside it. There is no cloth on the table and no chair "
            "anywhere in the room."
        ),
    },
    {
        "id": "v2-r035-b05", "out": "s05-the-finest-food.jpeg",
        "seg": "n1", "window": "11.370-14.230", "wide": False, "jesus": False,
        "locks": ["BANQUET-HALL", "HOUSE"],
        "narration": "the finest food, the tables set,",
        "must_show": "A close view along the laid low table itself — flat bread, clay bowls of olives and figs and lentils, roast lamb on a clay platter, a clay wine jar — with no person in the frame at all.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM + _NO_NIGHT
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, camera low and level with the table top "
            "and looking straight down its length, warm low late-afternoon sun "
            "raking in from the LEFT and glancing off the food, fine film grain, "
            "NO PERSON IN THE PICTURE AT ALL. THE FRAME IS FILLED BY THE LOW TABLE "
            "AND WHAT IS ON IT, running away from the camera into soft focus: flat "
            "torn rounds of barley and wheat bread laid straight on the bare adzed "
            "timber, shallow fired-clay bowls of black olives, of green lentils, "
            "of dried figs and almonds, a joint of roast lamb on a plain "
            "fired-clay platter, a small clay dish of coarse grey salt, and a "
            "fired-clay wine jar with plain unstemmed clay cups set beside it. THE "
            "WOOD OF THE TABLE IS BARE: there is no tablecloth, runner, napkin, "
            "placemat or cloth of any kind under or on the food, no glass, no "
            "metal plate, tray or dish, and no knife, fork or spoon anywhere. THE "
            "TABLE IS KNEE HIGH and the camera's low viewpoint shows the worn "
            "flagstone floor and the dark folded wool bolsters lying on it just "
            "behind. In the soft background stand ONE shallow fired-clay oil lamp, "
            "unlit, on a stone ledge, and the pale plastered wall."
        ),
    },
    {
        "id": "v2-r035-b06", "out": "s06-every-place-ready.jpeg",
        "seg": "n1", "window": "14.230-18.690", "wide": True, "jesus": False,
        "locks": _HALL_DAY, "char_refs": _HOST,
        "narration": "every place ready, and he sent out his invitations.",
        "must_show": "The whole dining hall seen from behind the host as he stands in its opening looking in at the finished room, the low U-shaped table laid and every reclining place made up and empty.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 24mm lens, warm low late-afternoon sun coming from "
            "behind the camera through the courtyard opening and lighting the "
            "whole room in front, the sun well out of frame and never behind any "
            "head, fine film grain, deep focus. THE CAMERA STANDS CLOSE BEHIND THE "
            "HOST IN THE OPENING AND SHOOTS PAST HIM into the room: he is seen "
            "ENTIRELY FROM BEHIND, full length, at the LEFT of the frame, his deep "
            "indigo mantle hanging down his back over his deep madder red tunic, "
            "one broad hand hooked in his dark umber sash, HIS FACE NOT VISIBLE AT "
            "ALL. BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS THE THING THE "
            "VIEWER SEES OF HIM AND IT IS STATED HERE: thick dark brown hair going "
            "iron grey at the temples, waving back off the crown to the nape of "
            "his neck and lying on the top of his mantle — NOT a bare, bald, "
            "shaven, cropped or thinning head, and nothing worn on it. NOT ONE "
            "FACE IS TURNED TOWARD THE LENS AND THERE IS NO OTHER PERSON IN THE "
            "ROOM. Beyond him THIS IS A WIDE FULL-LENGTH SCENE of the whole "
            "chamber: the KNEE-HIGH U-shaped adzed-timber table on its three sides "
            "with the fourth left open, laid with bread, clay bowls, clay jars and "
            "unstemmed clay cups, and around it eight reclining places made up on "
            "the floor with dark folded wool mats and bolsters, EVERY ONE OF THEM "
            "EMPTY. Rough hewn beams cross the low ceiling, dark wool rugs lie on "
            "the flagstones, and one dark cloth hanging covers the far opening. "
            "There is no chair and no cloth on the table anywhere in the room."
        ),
    },
    # ============ n2 — the servant is sent ====================================
    {
        # ANCHOR BEAT — SERVANT. Generated in the anchor run; the host is NOT in
        # this frame, so this anchor cannot reference the host anchor.
        "id": "v2-r035-b07", "out": "s07-he-sent-his-servant.jpeg",
        "seg": "n2", "window": "18.690-22.330", "wide": False, "jesus": False,
        "locks": ["HOUSE", "SERVANT", "JUDEAN-LAND"],
        "narration": "When the feast was ready, he sent his servant to tell the invited guests,",
        "must_show": "The servant alone in the host's courtyard, already turning to go out through the gateway with the folded invitations against his chest, his face clearly visible in strict side-on profile.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, warm low late-afternoon sun coming in "
            "almost level from the RIGHT through the courtyard gateway and "
            "modelling the face from the front, fine film grain, shallow but "
            "honest depth of field. THIS IS A STRICT SIDE-ON PROFILE AND THE "
            "CAMERA SITS EXACTLY ON HIS RIGHT: the servant stands three-quarter "
            "length at the LEFT of the frame turned fully to the RIGHT, so the "
            "viewer sees ONE cheek, ONE eye, ONE ear and the clean outline of "
            "brow, nose, lips and short cropped beard against the sunlit gateway "
            "beyond. THE FAR CHEEK AND THE FAR EYE ARE COMPLETELY HIDDEN BEHIND "
            "THE BRIDGE OF HIS NOSE AND THE MASS OF HIS HEAD and cannot be seen at "
            "all; his one visible eye is already looking out and away to the RIGHT "
            "toward the lane and exits the picture through the RIGHT EDGE, so his "
            "pupils are nowhere near the lens. His expression is willing and "
            "hurried, caught mid-step, the near shoulder dropped and the far foot "
            "already lifting. His SHORT THICK BLACK CURLY HAIR IS CUT CLOSE TO THE "
            "SKULL and lit along the top; his dark olive knee-length work tunic is "
            "hitched at the thigh into its deep rust twisted belt. Against his "
            "chest he holds a small stack of folded cloth invitation squares in "
            "one lean hand. HE IS THE ONLY PERSON IN THE PICTURE. Behind him the "
            "courtyard's worn flagstones, its stone water trough and the plain "
            "squared jambs of the gateway with bright dusty lane beyond."
        ),
    },
    {
        "id": "v2-r035-b08", "out": "s08-everything-is-ready.jpeg",
        "seg": "n2", "window": "22.330-25.724", "wide": True, "jesus": False,
        "locks": ["MARKET-TOWN", "TOWN-LANES", "SERVANT", "GUESTS", "BACKGROUND-CAST"],
        "char_refs": _SERV,
        "narration": "come, for everything is ready now.",
        "must_show": "The servant standing in a narrow stepped town lane at a house opening with one hand lifted in invitation, calling the message in to a well-off householder standing inside it.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun striking down "
            "the lane from the far end so both men are lit from the front and the "
            "sun itself is out of frame above, never behind any head, fine film "
            "grain. THE CAMERA STANDS BEHIND AND SLIGHTLY ABOVE THE SERVANT AND "
            "SHOOTS PAST HIM up the lane: he is in the near LEFT foreground seen "
            "in three-quarter FROM BEHIND, full length, his short black curls bare "
            "and his dark olive tunic and deep rust belt filling the near frame, "
            "his right arm lifted and his open hand held out toward the opening, "
            "HIS FACE NOT VISIBLE to the camera. In the middle distance the "
            "householder stands in a plain rectangular opening two shallow steps "
            "up, seen in three-quarter from the side in deep indigo, one hand "
            "raised palm-out in the small gesture of a man about to decline; his "
            "gaze travels down at the servant and exits the frame through the "
            "LOWER LEFT. NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the camera is far enough back that both men are "
            "visible head to sandals, with the narrow lane of pale plastered "
            "mud-brick walls closing in on both sides, shallow hand-cut steps "
            "underfoot, flat rooflines almost meeting above and one bright ragged "
            "strip of hard pale sky between them. At most one other townsman is "
            "visible far up the lane, a solid dark mass head to foot."
        ),
    },
    # ============ j18 — Luke 14:18, the FIRST GUEST speaking (RED) ============
    {
        # ANCHOR BEAT — FIRST-GUEST. Generated in the anchor run. The servant he
        # answers stands OFF-FRAME to the left, so this anchor has no other anchor
        # in its picture and cannot reference one.
        "id": "v2-r035-b09", "out": "s09-bought-a-piece-of-ground.jpeg",
        "seg": "j18", "window": "25.724-29.940", "wide": False, "jesus": False,
        "locks": ["TOWN-LANES", "FIRST-GUEST"],
        "narration": "I have bought a piece of ground, and I must needs go and see it:",
        "must_show": "The first invited guest standing alone on his own threshold answering the servant who is off-frame to the left, one hand raised in a small apologetic gesture, his face clearly visible in strict side-on profile.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_CREAM + _NO_NIGHT
        + "no other person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, warm low late-afternoon sun coming in "
            "almost level from the LEFT along the lane and modelling the face from "
            "the front, fine film grain, shallow but honest depth of field. THIS "
            "IS A STRICT SIDE-ON PROFILE AND THE CAMERA SITS EXACTLY ON HIS LEFT: "
            "the guest stands three-quarter length at the RIGHT of the frame "
            "turned fully to the LEFT in his own doorway, so the viewer sees ONE "
            "cheek, ONE eye, ONE ear and the clean outline of brow, nose, lips and "
            "full soft black beard against the plastered wall beyond. THE FAR "
            "CHEEK AND THE FAR EYE ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS "
            "NOSE AND THE MASS OF HIS HEAD and cannot be seen at all; his one "
            "visible eye looks level and away to the LEFT at somebody standing "
            "OUTSIDE THE PICTURE and exits the frame through the LEFT EDGE, so his "
            "pupils are nowhere near the lens. HE IS THE ONLY PERSON IN THE "
            "PICTURE and no part of any other person appears in it. His expression "
            "is polite, faintly embarrassed evasion — the brows lifted, the mouth "
            "making an excuse — and his near hand is raised palm-out at chest "
            "height in a small apologetic gesture while his far shoulder and hip "
            "are ALREADY TURNED BACK toward the dark opening behind him, so the "
            "body is leaving while the face is still talking. His THICK BLACK WAVY "
            "HAIR to the middle of the neck is lit along the top; his dark "
            "olive-green tunic, deep maroon mantle and charcoal sash are all "
            "clearly readable. Behind him the plain rectangular opening with its "
            "dark hanging cloth half pushed aside, and the pale plastered lane "
            "wall running away into soft focus."
        ),
    },
    {
        "id": "v2-r035-b10", "out": "s10-have-me-excused.jpeg",
        "seg": "j18", "window": "29.940-33.685", "wide": True, "jesus": False,
        "locks": ["TOWN-LANES", "FIRST-GUEST", "SERVANT", "BACKGROUND-CAST"],
        "char_refs": _GUEST + _SERV,
        "narration": "I pray thee have me excused.",
        "must_show": "The first guest stepping back inside his own opening and letting the dark cloth fall shut behind him while the servant stands below in the lane with the folded invitation still held out in his hand.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun raking along "
            "the lane from the LEFT, the sun out of frame and never behind any "
            "head, fine film grain. THE CAMERA STANDS BEHIND AND BESIDE THE "
            "SERVANT AND SHOOTS PAST HIM up at the opening: the servant is in the "
            "near RIGHT foreground seen in three-quarter FROM BEHIND, full length, "
            "his short black curls bare, his dark olive tunic and deep rust belt "
            "filling the near frame, one lean arm still extended with a small "
            "folded cloth invitation square in his open hand, his shoulders "
            "beginning to drop; HIS FACE IS NOT VISIBLE to the camera. In the "
            "middle distance, two shallow steps up, the first invited guest is "
            "seen ENTIRELY FROM BEHIND AND SLIGHTLY TO THE SIDE as he steps back "
            "in through his own opening — his deep maroon mantle and dark "
            "olive-green tunic, and BECAUSE THE CAMERA IS BEHIND HIS HEAD HIS HAIR "
            "IS STATED HERE: thick black wavy hair to the middle of the neck, "
            "pushed back off the crown and lying on the collar of his mantle, not "
            "cropped, not bald, nothing worn on it. His near hand is releasing the "
            "dark woven hanging so that it swings across the opening behind him. "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH "
            "SCENE: both men are visible head to sandals in the narrow stepped "
            "lane of pale plastered walls, with the flat rooflines almost meeting "
            "above and one bright strip of hard pale sky between them, and the "
            "long shadow of the servant thrown up the steps ahead of him."
        ),
    },
    # ============ n3 — one by one, the three excuses ==========================
    {
        "id": "v2-r035-b11", "out": "s11-one-by-one-excuses.jpeg",
        "seg": "n3", "window": "33.685-36.840", "wide": True, "jesus": False,
        "locks": ["TOWN-LANES", "SERVANT", "BACKGROUND-CAST"], "char_refs": _SERV,
        "narration": "But one by one, they all made excuses.",
        "must_show": "The servant standing alone in the middle of the empty stepped lane between a row of house openings, every one of them now closed by its hanging cloth, the folded invitations still in his hand.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun coming down "
            "the lane from the far end so the servant is lit from the front and "
            "the sun is out of frame above, never behind his head, fine film "
            "grain, deep focus. THE CAMERA STANDS BEHIND THE SERVANT AND SHOOTS "
            "PAST HIM down the length of the lane: he is seen ENTIRELY FROM "
            "BEHIND, small, full length, standing still in the middle of the frame "
            "with his back to the camera, his short black curls bare, his dark "
            "olive tunic and deep rust belt reading clearly, his arms fallen to "
            "his sides and the small stack of folded cloth invitation squares "
            "still gripped in one hand. BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS "
            "HAIR IS STATED HERE: short thick black curly hair cut close to the "
            "skull, a clear cap of dark curl at the crown and the nape, nothing "
            "worn on it. HIS FACE IS NOT VISIBLE AT ALL and NOT ONE FACE IS TURNED "
            "TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE: the narrow lane "
            "runs away from him in shallow hand-cut steps between pale plastered "
            "mud-brick walls, and along both sides FOUR plain rectangular openings "
            "stand separated and individually countable, four and no more, EVERY "
            "ONE OF THEM CLOSED by a hanging panel of dark woven cloth pulled "
            "fully across it. The lane is otherwise completely empty of people. "
            "Flat rooflines almost meet above with one bright ragged strip of hard "
            "pale sky between them."
        ),
    },
    {
        "id": "v2-r035-b12", "out": "s12-bought-a-field.jpeg",
        "seg": "n3", "window": "36.840-39.290", "wide": True, "jesus": False,
        "locks": ["BOUGHT-FIELD", "JUDEAN-LAND", "FIRST-GUEST"], "char_refs": _GUEST,
        "narration": "One had just bought a field and had to go see it.",
        "must_show": "The first guest out on his newly bought stony hillside fallow, standing at its edge along the dry-stone terrace wall with his hand on an upright boundary stone, looking out over the ground he has bought.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 35mm lens, warm low late-afternoon sun from the LEFT "
            "raking across the stony ground and throwing a long shadow off every "
            "stone, the sun out of frame and never behind his head, fine film "
            "grain, deep focus. THE CAMERA STANDS BEHIND AND TO THE LEFT OF THE "
            "MAN AND SHOOTS PAST HIM out over the field: he is in the near LEFT "
            "foreground seen ENTIRELY FROM BEHIND, full length, his deep maroon "
            "mantle across both shoulders over his dark olive-green tunic, his "
            "charcoal sash at the waist, one hand resting flat on the top of an "
            "upright unworked limestone boundary stone. BECAUSE THE CAMERA IS "
            "BEHIND HIS HEAD, HIS HAIR IS THE THING THE VIEWER SEES OF HIM AND IT "
            "IS STATED HERE: thick black wavy hair to the middle of the neck, "
            "parted and pushed back off the crown and lying on the collar of his "
            "mantle — not cropped, not bald, not thinning, and nothing worn on it. "
            "HIS FACE IS NOT VISIBLE AT ALL and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. HE IS THE ONLY PERSON IN THE PICTURE. THIS IS A WIDE "
            "FULL-LENGTH SCENE: beyond him the bought ground runs away — bare pale "
            "tan and grey stony fallow soil loose with limestone chips, dry "
            "straw-gold thistles standing in it, held in steps by low unmortared "
            "dry-stone terrace walls, with two more upright uncarved boundary "
            "stones set far apart along its edge and bare bleached limestone hills "
            "behind under a hard clear pale blue sky. NO CROP GROWS ANYWHERE IN "
            "THIS FRAME."
        ),
    },
    {
        "id": "v2-r035-b13", "out": "s13-bought-oxen.jpeg",
        "seg": "n3", "window": "39.290-41.910", "wide": True, "jesus": False,
        "locks": ["OX-YARD", "JUDEAN-LAND", "OTHER-EXCUSERS", "HAND-TOOLS"],
        "narration": "One had bought oxen and had to try them out.",
        "must_show": "The ox-buyer in his walled yard working with his new cattle — bent at the neck of a yoked pair with both hands on the hand-hewn wooden yoke, settling it down onto their shoulders, while two more oxen stand loose behind.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 40mm lens, warm low late-afternoon sun from the RIGHT "
            "raking across the yard and lighting the animals and the man from the "
            "front, the sun out of frame and never behind any head, fine film "
            "grain, deep focus. THE CAMERA STANDS BEHIND AND TO THE RIGHT OF THE "
            "MAN AND SHOOTS PAST HIM into the work: he is at the LEFT of the frame "
            "seen in three-quarter FROM BEHIND, full length, bent forward from the "
            "waist with BOTH HANDS ON THE HAND-HEWN WOODEN NECK YOKE, pressing it "
            "down and back onto the shoulders of the near ox, his head turned away "
            "down toward the animals' necks and HIS FACE NOT VISIBLE to the "
            "camera; he wears ONE calf-length dark umber work tunic hitched into "
            "ONE charcoal twisted belt, his short black hair bare, and his arms "
            "and shoulders are visibly braced and taking weight. NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. IN THE YARD THERE ARE EXACTLY FOUR OXEN AND "
            "NO MORE, separated far enough to be counted one by one: TWO standing "
            "yoked together side by side under the single timber yoke in the "
            "middle of the frame, heads low, dust round their hooves, and TWO more "
            "standing loose apart from them at the RIGHT, one of those turned "
            "away. THIS IS A WIDE FULL-LENGTH SCENE: the whole yard is in frame — "
            "packed pale tan earth, a waist-high unmortared dry-stone wall, a low "
            "mud-brick byre with a FLAT roof of poles and packed earth, a "
            "hand-hewn ard plough and a flint-studded threshing sledge lying to "
            "one side, and bleached limestone hills beyond."
        ),
    },
    {
        "id": "v2-r035-b14", "out": "s14-had-just-married.jpeg",
        "seg": "n3", "window": "41.910-45.630", "wide": True, "jesus": False,
        "locks": ["BRIDE-HOUSE", "JUDEAN-LAND", "OTHER-EXCUSERS", "SERVANT",
                  "BACKGROUND-CAST"],
        "char_refs": _SERV,
        "narration": "One had just married, and simply would not come.",
        "must_show": "The young bridegroom standing under the fresh red marriage cloth over his own doorway with his back to the lane, waving the servant away over his shoulder without turning round.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _NO_NIGHT + _NO_MODERN_LAMP + _GAZE,
        "scene": (
            "One photograph, 35mm lens, BROAD WARM AFTERNOON DAYLIGHT with the sun "
            "high and to the LEFT and out of frame, lighting the doorway and both "
            "men from the front, fine film grain, deep focus. NO LAMP, TORCH, "
            "CANDLE OR FIRE APPEARS ANYWHERE IN THIS FRAME AND IT IS NOT NIGHT. "
            "THE CAMERA STANDS BEHIND AND BESIDE THE SERVANT DOWN IN THE LANE AND "
            "SHOOTS PAST HIM up at the doorway: the servant is in the near RIGHT "
            "foreground seen in three-quarter FROM BEHIND, three-quarter length, "
            "his short black curls bare and his dark olive tunic and deep rust "
            "belt filling the near frame, one arm still half-raised with a folded "
            "cloth invitation square in it, HIS FACE NOT VISIBLE. In the middle "
            "distance the young bridegroom stands in his own doorway seen ENTIRELY "
            "FROM BEHIND, full length, already stepping in — his deep rust-red "
            "tunic under a dark indigo mantle, his short black curling hair bare — "
            "with his nearer arm thrown back over his own shoulder in a loose "
            "dismissive wave toward the lane WITHOUT HIS HEAD TURNING ROUND. NOT "
            "ONE FACE IS TURNED TOWARD THE LENS AND NEITHER MAN'S FACE IS VISIBLE. "
            "THIS IS A WIDE FULL-LENGTH SCENE: both men are visible head to "
            "sandals against a small pale-plastered mud-brick house with a FLAT "
            "roof of poles and packed earth, ONE rectangle of fresh DEEP MADDER "
            "RED hand-woven wool hung over the doorway with a twisted flax cord "
            "and a few dry wildflowers at one corner, and ONE reed basket of figs "
            "and ONE fired-clay jar standing on the doorstep. Dry stony hill "
            "country and hard pale blue sky behind."
        ),
    },
    # ============ n4 — they were not evil, only busy ==========================
    {
        "id": "v2-r035-b15", "out": "s15-not-evil-just-busy.jpeg",
        "seg": "n4", "window": "45.630-49.070", "wide": True, "jesus": False,
        "locks": ["MARKET-TOWN", "TOWN-LANES", "GUESTS", "BACKGROUND-CAST", "JUDEAN-LAND"],
        "narration": "They were not evil people. They were just busy.",
        "must_show": "Three of the invited householders going about their own separate business in the town at the same hour — one counting figs into a basket, one leading a laden donkey away, one bent over a scroll of accounts on a stone bench — none of them doing anything wrong.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 28mm lens, warm low late-afternoon sun coming from "
            "the LEFT across the open ground at the head of the lane so every "
            "figure is lit from the front and the sun is out of frame, fine film "
            "grain, deep focus. THE CAMERA STANDS HIGH ABOVE AND BEHIND THE WHOLE "
            "SCENE ON AN OUTSIDE ROOF STAIR AND LOOKS DOWN AND ACROSS IT: because "
            "the camera is above and behind every person in the frame, EVERY "
            "FIGURE IS SEEN FROM BEHIND OR IN THREE-QUARTER FROM BEHIND, no face "
            "is turned up toward the lens and a gaze into the lens is "
            "geometrically impossible. THERE ARE EXACTLY THREE MEN IN THE PICTURE, "
            "separated far enough to be counted one by one and each busy with his "
            "own ordinary work: at the LEFT one in deep indigo crouches over a "
            "hand-woven reed basket counting figs into it with both hands; in the "
            "MIDDLE one in dark umber walks away up the lane leading a laden "
            "donkey by a twisted flax halter, seen from directly behind; at the "
            "RIGHT one in deep maroon sits on a low dry-stone bench bent over a "
            "HAND-INKED HEBREW SCROLL spread on his knees, his head down. NONE OF "
            "THEM IS DOING ANYTHING WRONG, cruel, drunken or shameful; they are "
            "simply occupied. THIS IS A WIDE FULL-LENGTH SCENE: all three and the "
            "whole corner of the town are in frame together, with pale plastered "
            "mud-brick walls, flat rooflines of poles and packed earth, packed "
            "pale tan earth underfoot, and dry stony hills under a hard clear pale "
            "sky beyond."
        ),
    },
    {
        "id": "v2-r035-b16", "out": "s16-their-own-plans.jpeg",
        "seg": "n4", "window": "49.070-51.730", "wide": False, "jesus": False,
        "locks": ["TOWN-LANES", "GUESTS"],
        "narration": "Their own plans felt more urgent",
        "must_show": "A close view from behind and above of one invited householder's hands setting the small folded cloth invitation down on a stone ledge and drawing a scroll of his own accounts across on top of it.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_CREAM + _NO_NIGHT
        + "no face, head, eyes or any part of a person above the chest anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, warm low late-afternoon sun raking "
            "in almost level from the LEFT across the stone, fine film grain, "
            "shallow depth of field. THE CAMERA IS DIRECTLY BEHIND AND ABOVE THE "
            "MAN'S OWN SHOULDER AND LOOKS STRAIGHT DOWN AT HIS HANDS: NO FACE, "
            "HEAD, EYE OR ANY PART OF A PERSON ABOVE THE CHEST APPEARS IN THIS "
            "PICTURE AT ALL, so a gaze into the lens is impossible. THE SUBJECT IS "
            "TWO ADULT MEN'S HANDS at true life size — broad, olive-brown, "
            "dark-haired across the back, blunt-fingered, plainly a grown man's "
            "and not a child's or a woman's. The LEFT hand has just laid a SMALL "
            "FOLDED SQUARE OF PLAIN HAND-WOVEN CLOTH flat on a worn pale limestone "
            "ledge; the RIGHT hand is drawing a rolled HAND-INKED HEBREW SCROLL "
            "across and DOWN ON TOP OF IT, so the folded cloth is already half "
            "covered and about to disappear beneath the scroll. The cuff of ONE "
            "deep indigo hand-woven wool sleeve fills the upper LEFT corner: THIS "
            "IS A CLOSE MACRO OF FABRIC AND THE WEAVE IS STATED HERE — a visible "
            "slightly irregular over-and-under grid of warp and weft threads, flat "
            "and matte, with a frayed selvedge, unmistakably coarse hand-woven "
            "wool and NOT knitwear, not a knit stitch, rib, cable or jersey, and "
            "not felted, brushed, napped or fleeced anywhere. The stone below is "
            "pitted, dusty and scored with age."
        ),
    },
    {
        "id": "v2-r035-b17", "out": "s17-the-joy-waiting.jpeg",
        "seg": "n4", "window": "51.730-54.154", "wide": True, "jesus": False,
        "locks": ["BANQUET-HALL", "HOUSE"],
        "narration": "than the joy waiting for them at his table.",
        "must_show": "The laid banquet hall standing entirely empty in the last low gold light, every reclining place made up and untouched, the food waiting on the low table and nobody in the room.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM
        + "no person, figure, hand, arm, shoulder, face or shadow of a person anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 24mm lens, the last low warm gold light of the "
            "afternoon coming in almost level from the RIGHT through a broad open "
            "opening and lying in one long bar across the floor and the table, the "
            "sun itself out of frame, fine film grain, deep focus, NO PERSON IN "
            "THE PICTURE AT ALL AND NOT ONE HUMAN SHADOW. THE CAMERA IS LOW, AT "
            "THE HEIGHT OF THE TABLE ITSELF, standing just inside the doorway and "
            "looking AWAY FROM THE camera-side opening along and across the whole "
            "room, so the empty made-up places are seen from behind and from the "
            "side. THIS IS A WIDE FULL-LENGTH SCENE OF AN EMPTY ROOM: the "
            "KNEE-HIGH U-shaped adzed-timber table stands on three sides with the "
            "fourth left open, laid with flat rounds of bread straight on the bare "
            "wood, shallow fired-clay bowls of olives and figs, a joint of roast "
            "lamb cooling on a clay platter, a fired-clay wine jar and eight plain "
            "unstemmed clay cups set out untouched. Around it, on the worn "
            "flagstones and dark hand-woven wool mats, eight reclining places are "
            "made up with folded wool bolsters, EVERY ONE OF THEM EMPTY and "
            "undisturbed. Rough hewn beams cross the low ceiling; the pale "
            "plastered walls are bare but for ONE plain woven hanging; ONE shallow "
            "fired-clay oil lamp stands unlit on a stone ledge. Dust drifts slowly "
            "in the gold bar of light. There is no chair, no cloth on the table, "
            "no glass and no metal anywhere in the room."
        ),
    },
    # ============ n5 — the servant comes back alone ===========================
    {
        "id": "v2-r035-b18", "out": "s18-came-back-alone.jpeg",
        "seg": "n5", "window": "54.154-58.350", "wide": True, "jesus": False,
        "locks": ["HOUSE", "SERVANT", "JUDEAN-LAND"], "char_refs": _SERV,
        "narration": "The servant came back alone, and here is where you would expect",
        "must_show": "The servant walking back in alone through the host's courtyard gateway at dusk with nobody behind him, the invitations still undelivered in his hand and the long empty lane stretching away beyond.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, the last cool blue-grey light after the "
            "sun has gone off the walls, one weak warm light only from an open "
            "opening deep inside the courtyard and NEVER behind anyone's head, "
            "fine film grain, deep focus. THE CAMERA STANDS INSIDE THE COURTYARD "
            "FACING THE GATEWAY, ABOVE HEAD HEIGHT AND LOOKING DOWN, and the "
            "servant is walking IN toward it and AWAY from the lane, so he is seen "
            "in three-quarter from the side with his head down and HIS FACE TURNED "
            "AWAY toward the flagstones; his gaze goes down and exits the picture "
            "through the BOTTOM EDGE and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "He is full length, small in the frame, his short black curls bare, "
            "his dark olive tunic and deep rust belt dusty at the hem, his "
            "shoulders down and the small stack of folded cloth invitation squares "
            "STILL GRIPPED IN ONE HAND, plainly undelivered. THIS IS A WIDE "
            "FULL-LENGTH SCENE AND THE POINT OF IT IS EMPTINESS: through the plain "
            "squared stone gateway behind him the lane runs away utterly empty of "
            "people to the last pale strip of dusk sky, and there is NOBODY "
            "FOLLOWING HIM — no second figure, no shoulder, no shape at the edge "
            "of the frame, nobody in the gateway and nobody in the lane. The "
            "courtyard around him is bare worn flagstone, a stone water trough and "
            "one dark fig tree in the corner."
        ),
    },
    {
        "id": "v2-r035-b19", "out": "s19-he-did-not.jpeg",
        "seg": "n5", "window": "58.350-62.285", "wide": False, "jesus": False,
        "locks": ["BANQUET-HALL", "HOUSE", "HOST", "NIGHT-LAMPLIGHT"], "char_refs": _HOST,
        "narration": "the host to cancel the feast, hurt and offended. He did not.",
        "must_show": "The host in his lamplit hall taking the news — standing very still beside the laid empty table with his hand resting flat on the wood, grave and thinking, his face in strict side-on profile.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_CREAM
        + "nobody is shouting, snarling, weeping, striking, throwing, sweeping the table clear or overturning anything, and nothing in the room is broken or upset; " + _GAZE,
        "scene": (
            "One photograph, 85mm lens, the room dark and the ONLY light ONE "
            "shallow fired-clay oil lamp with a single small bare-wick flame "
            "standing ON THE LOW TABLE, BELOW HIS CHIN AND NEARER THE CAMERA THAN "
            "HIS HEAD, so its light travels UPWARD AND FORWARD onto the front "
            "planes of his face — the underside of the brow, the nose, the "
            "cheekbone, the chin — while the crown and the back of his head, his "
            "hair and his shoulders stay UNLIT AND DARK and merge into the room "
            "behind. NO LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND HIS HEAD and "
            "there is no bright rim, edge, outline or corona anywhere on him. Fine "
            "film grain, shallow depth of field. THIS IS A STRICT SIDE-ON PROFILE "
            "AND THE CAMERA SITS EXACTLY ON HIS RIGHT: the host stands half-length "
            "at the LEFT of the frame turned fully to the RIGHT, so the viewer "
            "sees ONE cheek, ONE eye, ONE ear and the clean outline of brow, nose, "
            "lips and beard against the dark room. THE FAR CHEEK AND THE FAR EYE "
            "ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF "
            "HIS HEAD; his one visible eye looks down and away to the RIGHT at the "
            "empty places along the table and exits the picture through the RIGHT "
            "EDGE. HIS FACE IS GRAVE AND STILL, NOT RAGING: the brows drawn but "
            "level, the mouth closed, the jaw unclenched — this is a man absorbing "
            "something and deciding what to do, not a man in a temper. One broad "
            "hand rests flat and steady on the bare adzed timber beside an "
            "untouched clay cup. His deep madder red tunic, deep indigo mantle and "
            "dark umber sash read dark and warm in the lamplight. Nothing in the "
            "room is broken, thrown, swept aside or overturned."
        ),
    },
    # ============ j1 — Luke 14:21, the HOST speaking (RED) ====================
    {
        "id": "v2-r035-b20", "out": "s20-streets-and-lanes.jpeg",
        "seg": "j1", "window": "62.285-65.780", "wide": True, "jesus": False,
        "locks": ["HOUSE", "HOST", "SERVANT", "NIGHT-LAMPLIGHT"], "char_refs": _HOST_SERV,
        "narration": "Go out quickly into the streets and lanes of the city,",
        "must_show": "The host in his gateway sending the servant straight back out into the dark, one arm flung out level and pointing down the lane, the servant already turning to run.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep blue night with the last light gone "
            "off the sky and the ONLY light ONE shallow fired-clay oil lamp with a "
            "single small bare-wick flame standing LOW ON THE STONE THRESHOLD "
            "BETWEEN THE TWO MEN, below both their chins and nearer the camera "
            "than either head, so it throws light UPWARD onto the fronts of their "
            "bodies while every crown, back of head and shoulder stays UNLIT AND "
            "DARK. NO LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND ANY HEAD and "
            "there is no bright rim, outline or corona on anyone. Fine film grain. "
            "THE CAMERA STANDS OUT IN THE LANE BEHIND AND BESIDE THE SERVANT AND "
            "SHOOTS PAST HIM back toward the gateway: the servant is in the near "
            "RIGHT foreground seen ENTIRELY FROM BEHIND, full length, his short "
            "black curls a dark cap at the crown and nape, his dark olive tunic "
            "and deep rust belt reading in the low lamplight, his body already "
            "twisting away to the LEFT and one foot lifting to run, HIS FACE NOT "
            "VISIBLE AT ALL. In the gateway the host stands in three-quarter from "
            "the side, full length, leaning forward with his whole right arm flung "
            "out and level, the hand open and pointing hard away down the lane to "
            "the LEFT; his head is turned fully away after his own pointing hand "
            "so his gaze runs LEFT and exits the picture through the LEFT EDGE, "
            "nowhere near the lens. NOT ONE FACE IS TURNED TOWARD THE LENS. THIS "
            "IS A WIDE FULL-LENGTH SCENE: both men head to sandals, the plain "
            "squared stone jambs and lintel of the gateway, and the dark lane "
            "dropping away."
        ),
    },
    {
        "id": "v2-r035-b21", "out": "s21-the-poor-and-the-maimed.jpeg",
        "seg": "j1", "window": "65.780-68.740", "wide": True, "jesus": False,
        "locks": ["TOWN-LANES", "POOR", "BACKGROUND-CAST", "NIGHT-LAMPLIGHT"],
        "narration": "and bring in hither the poor, and the maimed,",
        "must_show": "Two poor townspeople sitting against a wall at the foot of a dark lane — a thin older woman wrapped in her mantle and a man whose left arm ends at the elbow — with nowhere to go and nothing to do.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, deep blue night and the ONLY light ONE "
            "shallow fired-clay oil lamp with a single small bare-wick flame "
            "standing ON THE GROUND in the near foreground between the camera and "
            "the two people, below both their chins and nearer the camera than "
            "either head, so its light travels UPWARD AND FORWARD onto the fronts "
            "of their bodies and the undersides of their faces while every crown, "
            "back of head and shoulder stays UNLIT AND DARK. NO LIGHT SOURCE "
            "STANDS BEHIND, ABOVE OR BEYOND ANY HEAD; there is no rim, outline or "
            "corona on anybody. Fine film grain. THE CAMERA SITS LOW ON THE GROUND "
            "AND WELL TO THE SIDE, SHOOTING ALONG THE WALL RATHER THAN AT THE "
            "PEOPLE, so both are seen in strict side-on profile against the "
            "plastered stone. THERE ARE EXACTLY TWO PEOPLE IN THIS PICTURE and no "
            "third. At the LEFT a thin older woman of about sixty sits with her "
            "back to the wall and her knees drawn up, wrapped in ONE dark umber "
            "wool mantle, her greying dark hair covered by its fold, her one "
            "visible eye looking away LEFT along the ground and out through the "
            "LEFT EDGE. At the RIGHT a man of about forty in ONE patched charcoal "
            "tunic sits with his legs out in front of him, HIS LEFT ARM ENDING "
            "CLEANLY AT THE ELBOW in an old healed limb with no bandage, no gauze, "
            "no blood and no open wound, his good hand flat on his knee, his head "
            "bowed and his one visible eye looking down and out through the BOTTOM "
            "EDGE. NEITHER OF THEM IS GROTESQUE, COMIC OR PITIABLE — they are "
            "worn, quiet, dignified people. NOT ONE FACE IS TURNED TOWARD THE LENS."
        ),
    },
    {
        "id": "v2-r035-b22", "out": "s22-the-halt-and-the-blind.jpeg",
        "seg": "j1", "window": "68.740-71.970", "wide": True, "jesus": False,
        "locks": ["TOWN-LANES", "POOR", "BACKGROUND-CAST", "NIGHT-LAMPLIGHT"],
        "narration": "and the halt, and the blind.",
        "must_show": "Two more poor townspeople further down the same dark lane — a lame man standing with his weight thrown onto one hewn wooden crutch and a blind man beside him with a hand resting on the lame man's shoulder.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, deep blue night and the ONLY light ONE "
            "shallow fired-clay oil lamp with a single small bare-wick flame standing "
            "LOW ON A STONE STEP in the near foreground, below both men's chins and "
            "nearer the camera than either head, throwing its light UPWARD AND FORWARD "
            "onto the fronts of their bodies while every crown, back of head and "
            "shoulder stays UNLIT AND DARK. NO LIGHT SOURCE STANDS BEHIND, ABOVE OR "
            "BEYOND ANY HEAD; there is no rim, outline or corona on anybody. Fine film "
            "grain, shallow depth of field. THE CAMERA SITS LOW AND EXACTLY SIDE-ON TO "
            "THE LINE BETWEEN THE TWO MEN AND SHOOTS ACROSS IT, so BOTH ARE IN STRICT "
            "SIDE-ON PROFILE, each turned fully toward the other and each showing the "
            "camera ONE cheek, ONE eye and ONE ear only, with each man's FAR CHEEK AND "
            "FAR EYE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS OWN NOSE — so neither "
            "of them can look at the lens and a gaze into it is geometrically "
            "impossible. THERE ARE EXACTLY TWO PEOPLE IN THIS PICTURE and no third. At "
            "the LEFT, turned fully RIGHT, a LAME man of about forty-five stands with "
            "his weight thrown hard onto ONE SINGLE HAND-HEWN WOODEN STAFF — one rough "
            "stick of a natural branch as thick as a wrist, gripped high in BOTH his "
            "hands and planted in the ground in front of him, with THE STICK STANDING "
            "ON THE FLOOR BETWEEN HIS OWN TWO FEET AND NOT UNDER HIS ARM. THERE IS ONE "
            "STICK IN THIS PICTURE AND ONLY ONE: no second stick, no matched pair, no "
            "underarm crutch, no padded armrest, no cross-piece, no modern hospital "
            "crutch and no walking frame. His right leg is turned out and takes no "
            "weight, his patched deep rust tunic hangs crooked because of it, and his "
            "one visible eye is level on his companion and exits the frame through the "
            "RIGHT EDGE. At the RIGHT, turned fully LEFT, a BLIND man of about fifty in "
            "ONE dark olive tunic stands with his face lifted and aimed slightly high "
            "and past the other man's shoulder, his clouded pale unfocused eyes plainly "
            "not fixed on anything and exiting the frame through the LEFT EDGE, ONE "
            "hand resting on the lame man's near shoulder and the other out ahead of "
            "him reading the air. BOTH ARE DIGNIFIED AND HUMAN, never grotesque, comic "
            "or pitiable, and there is no metal crutch, walking frame, wheelchair, "
            "prosthesis or white bandage anywhere. Behind them the narrow lane runs "
            "away into black, with plain RECTANGULAR openings under flat stone lintels "
            "and NOT ONE ARCH anywhere."
        ),
    },
    # ============ n6 — the retelling of the command ===========================
    {
        "id": "v2-r035-b23", "out": "s23-go-out-into-the-streets.jpeg",
        "seg": "n6", "window": "71.970-75.370", "wide": True, "jesus": False,
        "locks": ["TOWN-LANES", "SERVANT", "BACKGROUND-CAST", "NIGHT-LAMPLIGHT"],
        "char_refs": _SERV,
        "narration": "Go out into the streets, he said, and bring in the poor,",
        "must_show": "The servant running away down the dark stepped lane with a clay lamp carried low in his hand, going fast, the hem of his tunic flying.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep blue night in the lane and the ONLY "
            "light ONE shallow fired-clay oil lamp with a single small bare-wick "
            "flame CARRIED LOW IN HIS OWN HAND AT HIP HEIGHT, well below his chin "
            "and nearer the camera than his head, so its light throws UPWARD AND "
            "FORWARD onto the steps in front of him and the front of his legs and "
            "body while his crown, the back of his head, his hair and his "
            "shoulders stay UNLIT AND DARK. NO LIGHT SOURCE STANDS BEHIND, ABOVE "
            "OR BEYOND HIS HEAD; there is no rim, outline or corona anywhere "
            "on him, and he gives off no light of his own. Slight motion blur in the trailing hem "
            "and the free hand, everything else sharp. Fine film grain. THE CAMERA "
            "STANDS BEHIND THE SERVANT AND SHOOTS PAST HIM down the lane: he is "
            "seen ENTIRELY FROM BEHIND, full length, mid-stride and running away "
            "from the camera down the shallow hand-cut steps, one arm out for "
            "balance and the lamp low in the other. BECAUSE THE CAMERA IS BEHIND "
            "HIS HEAD, HIS HAIR IS STATED HERE: short thick black curly hair cut "
            "close to the skull, a clear dark cap of curl at the crown and the "
            "nape, nothing worn on it. HIS FACE IS NOT VISIBLE AT ALL. THIS IS A "
            "WIDE FULL-LENGTH SCENE: the narrow lane of pale plastered mud-brick "
            "walls falls away in steps ahead of him into darkness, with flat "
            "rooflines almost meeting above and one strip of deep blue-black star "
            "sky between them. NOT ONE FACE IS TURNED TOWARD THE LENS and there is "
            "nobody else in the lane."
        ),
    },
    {
        "id": "v2-r035-b24", "out": "s24-the-crippled-the-blind.jpeg",
        "seg": "n6", "window": "75.370-78.650", "wide": True, "jesus": False,
        "locks": ["TOWN-LANES", "SERVANT", "POOR", "NIGHT-LAMPLIGHT", "BACKGROUND-CAST"],
        "char_refs": _SERV,
        "narration": "the crippled, the blind, everyone the respectable",
        "must_show": "The servant crouched right down on his heels in the lane to the level of the sitting blind man, both his hands open and offered, telling him he is invited.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 50mm lens, deep blue night and the ONLY light ONE "
            "shallow fired-clay oil lamp with a single small bare-wick flame SET "
            "DOWN ON THE GROUND BETWEEN THE TWO MEN in the near foreground, below "
            "both their chins and nearer the camera than either head, so its light "
            "goes UPWARD AND FORWARD onto the fronts of their faces and hands "
            "while both crowns, the backs of both heads and both sets of shoulders "
            "stay UNLIT AND DARK. NO LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND "
            "ANY HEAD; no rim, outline or corona on anybody. Fine film grain, "
            "shallow depth of field. THE CAMERA SITS LOW AND WELL TO THE SIDE AND "
            "SHOOTS ACROSS BETWEEN THEM, so both men are seen in strict side-on "
            "profile facing each other and neither can look at the lens. THERE ARE "
            "EXACTLY TWO PEOPLE IN THIS PICTURE. At the LEFT the servant is "
            "crouched right down on his heels, knees wide, his dark olive tunic "
            "gathered, BOTH HANDS OPEN AND HELD OUT LOW AND EMPTY, palms up, "
            "toward the other man — he is not touching him, not gripping him and "
            "not pulling him; his one visible eye looks steadily RIGHT into the "
            "other man's face and exits the frame through the RIGHT EDGE. At the "
            "RIGHT the blind man of about fifty sits against the wall in ONE "
            "patched dark olive tunic, his face lifted and turned toward the "
            "sound, his clouded pale unfocused eyes aimed slightly high and past "
            "the servant's shoulder and out through the LEFT EDGE, one hand "
            "halfway up in the air as if to be sure he has heard right. HIS "
            "EXPRESSION IS DAWNING DISBELIEF, not misery. Neither man is "
            "grotesque, comic or pitiable. NOT ONE FACE IS TURNED TOWARD THE LENS."
        ),
    },
    {
        "id": "v2-r035-b25", "out": "s25-never-have-invited.jpeg",
        "seg": "n6", "window": "78.650-81.329", "wide": False, "jesus": False,
        "locks": ["TOWN-LANES", "POOR", "NIGHT-LAMPLIGHT"],
        "narration": "guests would never have invited.",
        "must_show": "A close view from behind and above of the small folded cloth invitation being laid into a poor man's thin open hand by the servant's hand, both hands lit from below by a lamp on the ground.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_CREAM
        + "no face, head, eyes or any part of a person above the chest anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 100mm macro lens, deep night and the ONLY light ONE "
            "shallow fired-clay oil lamp with a single small bare-wick flame "
            "standing ON THE GROUND just outside the near edge of the frame below, "
            "so the light comes UP from beneath onto the backs and knuckles of the "
            "hands, fine film grain, shallow depth of field. THE CAMERA IS "
            "DIRECTLY BEHIND AND ABOVE THE SERVANT'S OWN SHOULDER AND LOOKS "
            "STRAIGHT DOWN AT THE TWO HANDS: NO FACE, HEAD, EYE OR ANY PART OF A "
            "PERSON ABOVE THE CHEST APPEARS IN THIS PICTURE AT ALL, so a gaze into "
            "the lens is impossible. THE SUBJECT IS TWO ADULT MEN'S HANDS at true "
            "life size, and both are plainly grown men's hands and not a child's "
            "or a woman's. From the upper LEFT the servant's lean olive-brown hand "
            "comes down and lays A SMALL FOLDED SQUARE OF PLAIN HAND-WOVEN CLOTH "
            "into the other; from the lower RIGHT the poor man's hand is open and "
            "waiting, thinner, harder, the nails broken, the palm seamed and "
            "grimed, the fingers just beginning to close. NEITHER HAND GRIPS, "
            "SEIZES OR PULLS THE OTHER — it is a thing being given and taken. AT "
            "THE EDGES OF THE FRAME, CLOSE AND SHARP, ARE TWO SLEEVES, AND THIS IS "
            "A CLOSE MACRO OF FABRIC SO THE WEAVE IS STATED HERE: the servant's "
            "dark olive cuff and the poor man's patched deep rust cuff each show a "
            "visible slightly irregular over-and-under grid of warp and weft "
            "threads, flat and matte, with a frayed selvedge and plainly visible "
            "mending stitches — unmistakably coarse hand-woven wool and NOT "
            "knitwear, not a knit stitch, rib, cable or jersey, and not felted, "
            "brushed, napped or fleeced anywhere."
        ),
    },
    # ============ n7 — the servant goes and finds them ========================
    {
        "id": "v2-r035-b26", "out": "s26-the-overlooked.jpeg",
        "seg": "n7", "window": "81.329-85.430", "wide": True, "jesus": False,
        "locks": ["TOWN-LANES", "SERVANT", "POOR", "NIGHT-LAMPLIGHT", "BACKGROUND-CAST"],
        "char_refs": _SERV,
        "narration": "So the servant went and found them, the overlooked and the left out,",
        "must_show": "The servant leading a small line of poor townspeople up the dark lane toward the host's gateway, his lamp low in his hand, the lame man on his crutch and the blind man with a hand on a shoulder following behind.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, deep blue night and the ONLY lights TWO "
            "shallow fired-clay oil lamps with single small bare-wick flames, one "
            "carried LOW AT HIP HEIGHT in the servant's hand at the front and one "
            "LOW IN A WOMAN'S CUPPED HANDS further back, both well below every "
            "chin and both nearer the camera than the heads they light, so the "
            "light goes UPWARD AND FORWARD onto the fronts of the bodies while "
            "every crown, back of head and shoulder in the picture stays UNLIT AND "
            "DARK. NO LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND ANY HEAD; no "
            "rim, outline, corona on anybody. Fine film grain, deep focus. "
            "THE CAMERA STANDS BEHIND AND ABOVE THE WHOLE LINE AND SHOOTS DOWN AND "
            "PAST THEM up the lane, so EVERY PERSON IS SEEN FROM BEHIND and a gaze "
            "into the lens is geometrically impossible. THERE ARE EXACTLY FIVE "
            "PEOPLE IN THIS PICTURE, separated far enough to be counted one by "
            "one: the servant at the front, then the lame man swinging along on "
            "his forked wooden crutch, then the blind man with one hand resting on "
            "the lame man's shoulder, then the thin older woman with the second "
            "lamp cupped in both hands, then one younger man at the back. NOBODY "
            "IS DRAGGED, GRIPPED, PUSHED OR HERDED — they are following willingly, "
            "and one of them has a hand raised to another's back in help. THIS IS "
            "A WIDE FULL-LENGTH SCENE: all five are visible head to sandals in the "
            "narrow stepped lane of pale plastered walls, climbing toward a faint "
            "warm lamplit opening far ahead, with flat rooflines above and one strip "
            "of deep blue-black star sky between them."
        ),
    },
    {
        "id": "v2-r035-b27", "out": "s27-a-seat-with-your-name.jpeg",
        "seg": "n7", "window": "85.430-89.190", "wide": True, "jesus": False,
        "locks": _HALL_LAMP + ["POOR", "SERVANT"], "char_refs": _HOST_SERV,
        "narration": "and told them there was a seat with their name on it. You can imagine their faces.",
        "must_show": "The poor coming in through the opening of the lit hall and stopping dead at the sight of the laid table, the host standing to one side with both arms open in welcome and the servant showing them where to lie down.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, night, and the ONLY light THREE shallow "
            "fired-clay oil lamps with single small bare-wick flames standing LOW ON "
            "THE TABLE ITSELF and on a low stone ledge, all of them below every chin "
            "in the room, so the light travels UPWARD AND FORWARD onto faces, hands "
            "and the front of the table while every crown, back of head and shoulder "
            "stays UNLIT AND DARK and the corners of the room fall away to near black. "
            "NO LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND ANY HEAD; no rim, outline "
            "or corona on anybody. Fine film grain, deep focus. THE CAMERA STANDS OUT "
            "IN THE DARK COURTYARD BEHIND THE PEOPLE WHO HAVE JUST COME IN, AT THEIR "
            "OWN SHOULDER HEIGHT, AND SHOOTS PAST THEIR BACKS THROUGH THE OPENING INTO "
            "THE LIT ROOM. Because every one of the newcomers stands BETWEEN THE "
            "CAMERA AND THE LIGHT with the camera at their backs, THE VIEWER SEES ONLY "
            "THE BACKS OF THEIR HEADS, THEIR SHOULDERS AND THEIR HAIR, not one of their "
            "faces is visible at all, and a gaze into the lens is geometrically "
            "impossible. FOUR of the poor fill the near frame as dark silhouetted "
            "backs, stopped dead just inside the opening — one has halted mid-step, one "
            "has a hand risen to the side of her own head, one has turned slightly to "
            "the person beside him — and every head is tipped toward the laid table "
            "ahead of them. Their hair is stated here because the camera is behind it: "
            "dark brown and black, some greying, worn loose or bound back, and where a "
            "woman covers her head it is ONE FOLD OF HER OWN DARK MANTLE and never a "
            "pale scarf. Beyond them, lit and sharp, the host stands in three-quarter "
            "FROM THE SIDE at the LEFT with BOTH ARMS OPEN AND LOW, palms up and out "
            "toward them, welcoming and touching nobody, his one visible eye on them "
            "and exiting the frame through the LEFT EDGE; at the RIGHT the servant is "
            "half-turned away with one hand pointing down at the made-up reclining "
            "places. THIS IS A WIDE FULL-LENGTH SCENE: the whole KNEE-HIGH U-shaped "
            "adzed-timber table, the bread and clay bowls, the bolsters and all six "
            "people are in frame together under the rough hewn beams. NOT ONE FACE IS "
            "TURNED TOWARD THE LENS."
        ),
    },
    {
        "id": "v2-r035-b28", "out": "s28-never-invited-to-anything.jpeg",
        "seg": "n7", "window": "89.190-93.849", "wide": False, "jesus": False,
        "locks": ["BANQUET-HALL", "HOUSE", "POOR", "NIGHT-LAMPLIGHT"],
        "narration": "Nobody had ever invited them to anything.",
        "must_show": "A close side-on view of one of the poor now lying propped on his left elbow at the low table, a torn piece of bread arrested in his right hand, looking at the food as if he cannot quite believe it.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_MOCK + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, night, and the ONLY light ONE shallow "
            "fired-clay oil lamp with a single small bare-wick flame standing ON "
            "THE TABLE IN THE NEAR FOREGROUND, below his chin and nearer the "
            "camera than his head, so its light travels UPWARD AND FORWARD onto "
            "the front planes of his face — the underside of the brow, the nose, "
            "the cheekbone, the chin, the throat — while his crown, the back of "
            "his head, his hair and his shoulders stay UNLIT AND DARK and merge "
            "into the black room behind him. NO LIGHT SOURCE STANDS BEHIND, ABOVE "
            "OR BEYOND HIS HEAD; there is no rim, edge, outline or corona "
            "anywhere on him, and he gives off no light of his own. Fine film grain, shallow depth "
            "of field. THIS IS A STRICT SIDE-ON PROFILE AND THE CAMERA SITS "
            "EXACTLY ON HIS LEFT: a man of about fifty is seen half-length at the "
            "RIGHT of the frame, PROPPED ON HIS LEFT ELBOW on a dark folded wool "
            "bolster with his body along the table, turned fully to the LEFT, so "
            "the viewer sees ONE cheek, ONE eye, ONE ear and the clean outline of "
            "brow, nose, lips and short grey-shot beard. THE FAR CHEEK AND THE FAR "
            "EYE ARE COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS "
            "OF HIS HEAD; his one visible eye looks down and away to the LEFT at "
            "the food and exits the picture through the LEFT EDGE. His RIGHT hand "
            "holds a torn piece of flat barley bread halfway up, arrested, not yet "
            "eaten; his expression is quiet astonishment with the eyes wet, not "
            "grief. He wears ONE patched dark umber wool tunic, its mending "
            "stitches plainly visible. Across the bottom third, close and softly "
            "out of focus, the bare adzed timber of the KNEE-HIGH table with clay "
            "bowls and an unstemmed clay cup on it. HE IS DIGNIFIED, never "
            "grotesque, comic or pitiable."
        ),
    },
    # ============ j22 — Luke 14:22, the SERVANT speaking (RED) ================
    {
        "id": "v2-r035-b29", "out": "s29-as-thou-hast-commanded.jpeg",
        "seg": "j22", "window": "93.849-96.010", "wide": True, "jesus": False,
        "locks": _HALL_LAMP + ["SERVANT", "POOR"], "char_refs": _HOST_SERV,
        "narration": "Lord, it is done as thou hast commanded,",
        "must_show": "The servant standing at his master's shoulder at the dark edge of the lit hall reporting back to him, one hand turned palm-up toward the filled places at the table.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_MOCK + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, night, and the ONLY light TWO shallow "
            "fired-clay oil lamps with single small bare-wick flames standing LOW "
            "ON THE TABLE out in front of both men, below both their chins and "
            "nearer the camera than either head, so the light comes UPWARD AND "
            "FORWARD onto the fronts of their bodies while both crowns, the backs "
            "of both heads and both sets of shoulders stay UNLIT AND DARK. NO "
            "LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND ANY HEAD; no rim, "
            "outline, corona on anybody. Fine film grain, deep focus. THE "
            "CAMERA STANDS BEHIND BOTH MEN AT THE DARK EDGE OF THE ROOM AND SHOOTS "
            "PAST THEM toward the lit table, so BOTH ARE SEEN FROM BEHIND and NOT "
            "ONE FACE IS TURNED TOWARD THE LENS. At the LEFT, nearest the camera, "
            "the host stands full length seen ENTIRELY FROM BEHIND, his deep "
            "indigo mantle down his back over his deep madder red tunic, his thick "
            "dark brown greying hair clear at the nape and temples. At the RIGHT, "
            "half a pace behind his master's shoulder, the servant stands in "
            "three-quarter FROM BEHIND, shorter and far slighter, his short black "
            "curly hair a dark cap at the crown and nape, his dark olive tunic and "
            "deep rust belt reading in the lamplight, ONE arm out and the hand "
            "turned palm-up toward the table in the gesture of a man reporting "
            "what he has done. THIS IS A WIDE FULL-LENGTH SCENE: beyond them the "
            "KNEE-HIGH U-shaped table runs across the frame with six of the poor "
            "reclining at it on their left elbows, all of them turned to the food "
            "and to each other, none of them looking back at the camera."
        ),
    },
    {
        "id": "v2-r035-b30", "out": "s30-yet-there-is-room.jpeg",
        "seg": "j22", "window": "96.010-98.806", "wide": False, "jesus": False,
        "locks": ["BANQUET-HALL", "HOUSE", "NIGHT-LAMPLIGHT"],
        "narration": "and yet there is room.",
        "must_show": "A close view along the far arm of the low table where three reclining places are still made up, empty and untouched, with clean clay cups waiting and nobody there.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_CREAM
        + "no person, figure, hand, arm, shoulder or face anywhere in this frame; " + _GAZE,
        "scene": (
            "One photograph, 50mm lens, night, camera LOW and level with the table "
            "top looking along its far arm, and the ONLY light ONE shallow "
            "fired-clay oil lamp with a single small bare-wick flame standing on "
            "the timber in the near foreground so the light falls forward along "
            "the wood and dies away into black at the far end. NO PERSON IN THE "
            "PICTURE AT ALL. Fine film grain, shallow depth of field. THE FRAME IS "
            "FILLED BY EMPTY PLACES: THREE reclining places made up side by side "
            "on the flagstones along the KNEE-HIGH adzed-timber table, separated "
            "far enough to be counted one by one, three and no more — each a dark "
            "folded hand-woven wool mat with a bolster set at its head — every one "
            "of them flat, smooth and UNDISTURBED, with nobody lying on any of "
            "them. On the bare wood above them stand three plain unstemmed "
            "fired-clay cups, clean and empty, and one shallow clay bowl of olives "
            "untouched. There is no cloth on the table, no glass, no metal and no "
            "cutlery. Beyond the last place the light gives out and the room goes "
            "to black. The whole picture is about the space nobody is filling."
        ),
    },
    # ============ n8 — and there was still room ===============================
    {
        "id": "v2-r035-b31", "out": "s31-still-room.jpeg",
        "seg": "n8", "window": "98.806-101.425", "wide": True, "jesus": False,
        "locks": _HALL_LAMP + ["POOR"], "char_refs": _HOST,
        "narration": "And there was still room.",
        "must_show": "The whole lamplit hall from above with the poor reclining along two arms of the low table and the entire third arm still standing empty, the host looking down it.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_MOCK + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens, night, and the ONLY light THREE shallow "
            "fired-clay oil lamps with single small bare-wick flames standing LOW "
            "ON THE TABLE, all of them below every chin in the room, so the light "
            "goes UPWARD AND FORWARD onto faces and hands while every crown and "
            "the back of every head stays UNLIT AND DARK and the room's corners "
            "fall to near black. NO LIGHT SOURCE STANDS BEHIND, ABOVE OR BEYOND "
            "ANY HEAD; no rim, outline, corona on anybody. Fine film "
            "grain, deep focus. THE CAMERA HANGS HIGH IN THE CORNER OF THE ROOM "
            "ABOVE AND BEHIND EVERYONE AND LOOKS STEEPLY DOWN ON THE WHOLE TABLE, "
            "so EVERY PERSON IS SEEN FROM ABOVE AND BEHIND, the tops of heads and "
            "backs toward the camera, and a gaze into the lens is geometrically "
            "impossible. THIS IS A WIDE FULL-LENGTH SCENE OF THE WHOLE ROOM AND "
            "THE POINT OF IT IS THE EMPTY SIDE: the KNEE-HIGH U-shaped "
            "adzed-timber table lies open below, and along TWO of its three arms "
            "the poor recline propped on their left elbows, eating with their "
            "right hands, turned to the food and to one another — while THE ENTIRE "
            "THIRD ARM runs away completely EMPTY, its mats and bolsters still "
            "flat and made up and nobody on any of them. At the near LEFT the host "
            "stands seen from above and behind, his greying dark brown hair clear "
            "at the crown and nape above his deep indigo mantle, his head turned "
            "down the empty arm and his face not visible. NOT ONE FACE IS TURNED "
            "TOWARD THE LENS."
        ),
    },
    # ============ j2 — Luke 14:23, the HOST speaking (RED) ====================
    {
        "id": "v2-r035-b32", "out": "s32-highways-and-hedges.jpeg",
        "seg": "j2", "window": "101.425-104.840", "wide": True, "jesus": False,
        "locks": ["HOUSE", "HOST", "SERVANT", "NIGHT-LAMPLIGHT", "JUDEAN-LAND"],
        "char_refs": _HOST_SERV,
        "narration": "Go out into the highways and hedges, and compel them to come in,",
        "must_show": "The host at his gate again, sending the servant out a second time and much further — his arm stretched out level toward the dark open country beyond the town, the servant already walking away up the road.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_FORCE + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 28mm lens, deep blue-black night with stars in the "
            "sky and the ONLY light ONE shallow fired-clay oil lamp with a single "
            "small bare-wick flame standing LOW ON THE STONE THRESHOLD between the "
            "two men, below both their chins and nearer the camera than either "
            "head, throwing light UPWARD onto the fronts of their bodies while "
            "every crown, back of head and shoulder stays UNLIT AND DARK. NO LIGHT "
            "SOURCE STANDS BEHIND, ABOVE OR BEYOND ANY HEAD; no rim, outline, "
            "corona on anybody, and nobody in the picture gives off light of their own. Fine film grain, deep focus. THE CAMERA "
            "STANDS OUT BEYOND BOTH MEN ON THE ROAD, BEHIND THE SERVANT, AND "
            "SHOOTS PAST HIM back toward the gate: the servant is in the near "
            "RIGHT foreground seen ENTIRELY FROM BEHIND, full length, his short "
            "black curls a dark cap at crown and nape, his dark olive tunic and "
            "deep rust belt reading low in the lamplight, ALREADY WALKING AWAY "
            "FROM THE GATE AND TOWARD THE OPEN COUNTRY, one shoulder turned back "
            "to listen, HIS FACE NOT VISIBLE. In the gateway the host stands in "
            "three-quarter from the side, full length, his whole right arm "
            "stretched out LEVEL AND FAR past the servant toward the dark land "
            "beyond, the hand open, his head turned fully away after his own "
            "pointing hand so his gaze runs off to the LEFT and out through the "
            "LEFT EDGE. NOBODY IS SEIZED, GRIPPED, PUSHED OR DRAGGED. NOT ONE FACE "
            "IS TURNED TOWARD THE LENS. THIS IS A WIDE FULL-LENGTH SCENE: both men "
            "head to sandals, the plain stone gateway and the town wall behind "
            "them, and ahead the pale dust road running out into black stony "
            "country under a starry sky."
        ),
    },
    {
        "id": "v2-r035-b33", "out": "s33-that-my-house-be-filled.jpeg",
        "seg": "j2", "window": "104.840-108.707", "wide": True, "jesus": False,
        "locks": ["HIGHWAY-HEDGES", "JUDEAN-LAND", "SERVANT", "POOR", "NIGHT-LAMPLIGHT",
                  "BACKGROUND-CAST"],
        "char_refs": _SERV,
        "narration": "that my house may be filled.",
        "must_show": "The servant out on the dark highway beyond the town, stooping at a rough shelter under a thorn hedge with his lamp low and his free hand held out open to the people sheltering there.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, deep blue-black night with stars, and the "
            "ONLY light ONE shallow fired-clay oil lamp with a single small "
            "bare-wick flame HELD LOW AT KNEE HEIGHT in the servant's own hand "
            "close to the ground, below every chin in the frame and nearer the "
            "camera than every head, so the light goes UPWARD AND FORWARD onto the "
            "fronts of the bodies and the thorn branches while every crown, back "
            "of head and shoulder stays UNLIT AND DARK. NO LIGHT SOURCE STANDS "
            "BEHIND, ABOVE OR BEYOND ANY HEAD; no rim, outline, corona on "
            "anybody. Fine film grain. THE CAMERA STANDS BEHIND AND ABOVE THE "
            "SERVANT AND SHOOTS DOWN AND PAST HIM into the shelter, so he is seen "
            "from behind and above and HIS FACE IS NOT VISIBLE. He is at the LEFT, "
            "full length, stooped low from the waist with the lamp down in one "
            "hand and the OTHER HAND HELD OUT OPEN AND EMPTY, palm up, toward the "
            "people under the hedge — not touching, not gripping, not pulling. "
            "THERE ARE EXACTLY THREE OTHER PEOPLE IN THIS PICTURE, separated far "
            "enough to be counted: a man sitting up out of a hollow scraped in the "
            "earth, a woman on her knees beside him with her mantle over her head, "
            "and a half-grown boy behind them, all three seen in three-quarter "
            "from the side with their faces lit from below and their eyes on the "
            "servant's outstretched hand, never on the lens. THIS IS A WIDE "
            "FULL-LENGTH SCENE: the shelter is a scrap of dark woven cloth pegged "
            "to two hewn sticks in the lee of a rough bank topped with piled DRY "
            "GREY-BROWN LEAFLESS THORN — bramble and boxthorn, spiny and half "
            "dead, NOT a clipped green hedge — with a ring of stones round a dead "
            "fire, the pale dust highway running past, and black stony country "
            "under stars."
        ),
    },
    # ============ n9 — the retelling: further out =============================
    {
        "id": "v2-r035-b34", "out": "s34-the-roads-and-the-edges.jpeg",
        "seg": "n9", "window": "108.707-112.290", "wide": True, "jesus": False,
        "locks": ["HIGHWAY-HEDGES", "JUDEAN-LAND", "SERVANT", "NIGHT-LAMPLIGHT"],
        "char_refs": _SERV,
        "narration": "Go further out, he said, to the roads and the edges of town,",
        "must_show": "The servant far out on the empty dark highway with his small lamp, walking on away from the distant town, the road running out into black open country ahead of him.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens, deep blue-black night with a thick field "
            "of stars overhead, the land reading only as shape and silhouette, and "
            "the ONLY light ONE shallow fired-clay oil lamp with a single small "
            "bare-wick flame CARRIED LOW AT HIP HEIGHT in the servant's hand, well "
            "below his chin and nearer the camera than his head, so its small pool "
            "of light lies UPWARD AND FORWARD on the dust in front of him and on "
            "the front of his legs while his crown, the back of his head, his hair "
            "and his shoulders stay UNLIT AND DARK. NO LIGHT SOURCE STANDS BEHIND, "
            "ABOVE OR BEYOND HIS HEAD; there is no rim, outline, corona "
            "anywhere on him, and he gives off no light of his own. Away from the lamp the picture "
            "falls to near black. Fine film grain, deep focus. THE CAMERA STANDS "
            "BEHIND THE SERVANT AND SHOOTS PAST HIM down the road, so he is seen "
            "ENTIRELY FROM BEHIND, small and full length, walking away from the "
            "camera; BECAUSE THE CAMERA IS BEHIND HIS HEAD, HIS HAIR IS STATED "
            "HERE: short thick black curly hair cut close to the skull, a clear "
            "dark cap of curl at the crown and the nape, nothing worn on it. HIS "
            "FACE IS NOT VISIBLE AT ALL and he is the ONLY person in the picture. "
            "THIS IS A WIDE FULL-LENGTH SCENE: the pale dust highway runs away "
            "from him into black stony country between rough banks of dry piled "
            "leafless thorn, with the town far behind at the LEFT edge showing "
            "only three or four small warm door-shaped points of lamplight, and "
            "the whole upper half of the frame is deep blue-black star sky."
        ),
    },
    {
        "id": "v2-r035-b35", "out": "s35-not-take-no-for-an-answer.jpeg",
        "seg": "n9", "window": "112.290-115.770", "wide": False, "jesus": False,
        "locks": ["HIGHWAY-HEDGES", "SERVANT", "POOR", "NIGHT-LAMPLIGHT"],
        "char_refs": _SERV,
        "narration": "and do not take no for an answer.",
        "must_show": "A close side-on view of the servant and an old man face to face by the roadside, the servant's open hand held out and waiting between them while the old man hesitates.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 85mm lens, night, and the ONLY light ONE shallow "
            "fired-clay oil lamp with a single small bare-wick flame standing ON "
            "THE GROUND in the near foreground between them, below both their "
            "chins and nearer the camera than either head, so the light travels "
            "UPWARD AND FORWARD onto the fronts of both faces and both hands while "
            "both crowns, the backs of both heads and both sets of shoulders stay "
            "UNLIT AND DARK and the night behind them goes to black. NO LIGHT "
            "SOURCE STANDS BEHIND, ABOVE OR BEYOND ANY HEAD; no rim, outline, "
            "corona on anybody, and nobody in the picture gives off light of their own. Fine film grain, shallow depth of field. "
            "THE CAMERA SITS LOW AND EXACTLY SIDE-ON TO THE LINE BETWEEN THEM AND "
            "SHOOTS ACROSS IT, so BOTH MEN ARE IN STRICT SIDE-ON PROFILE FACING "
            "EACH OTHER and neither can look at the lens; each far cheek and far "
            "eye is completely hidden behind the bridge of that man's own nose. "
            "THERE ARE EXACTLY TWO PEOPLE IN THIS PICTURE. At the LEFT the servant "
            "is turned fully RIGHT, half-crouched, HIS OPEN EMPTY HAND HELD OUT "
            "AND WAITING between them, palm up, not touching, not gripping and not "
            "pulling; his one visible eye is level on the old man's face and exits "
            "the frame through the RIGHT EDGE, and his short black curls and dark "
            "olive tunic are clear. At the RIGHT an old man of about seventy in "
            "ONE patched charcoal tunic and mantle is turned fully LEFT, his lined "
            "face lit from beneath, his one visible eye down on that offered hand "
            "and out through the LEFT EDGE, his own hand only halfway lifted, "
            "hesitating — the face of a man who does not believe this can be meant "
            "for him. HE IS DIGNIFIED, never grotesque, comic or pitiable."
        ),
    },
    {
        "id": "v2-r035-b36", "out": "s36-until-my-house-is-full.jpeg",
        "seg": "n9", "window": "115.770-119.685", "wide": True, "jesus": False,
        "locks": ["HIGHWAY-HEDGES", "JUDEAN-LAND", "SERVANT", "POOR", "NIGHT-LAMPLIGHT",
                  "BACKGROUND-CAST"],
        "char_refs": _SERV,
        "narration": "Make sure they know they are truly wanted, until my house is full.",
        "must_show": "A second, longer line of people walking back along the dark highway toward the town's lit gateway behind the servant, more of them than before, coming in willingly.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_TOWN + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_GREEN + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens, deep blue-black night with stars, and the "
            "ONLY lights TWO shallow fired-clay oil lamps with single small "
            "bare-wick flames carried LOW AT HIP HEIGHT in two of the walkers' "
            "hands, both below every chin and both nearer the camera than the "
            "heads they light, so the light goes UPWARD AND FORWARD onto the "
            "fronts of the bodies and the road while every crown, back of head and "
            "shoulder stays UNLIT AND DARK. NO LIGHT SOURCE STANDS BEHIND, ABOVE "
            "OR BEYOND ANY HEAD; no rim, outline, corona on anybody. Fine "
            "film grain, deep focus. THE CAMERA STANDS BEHIND AND ABOVE THE WHOLE "
            "LINE AND SHOOTS DOWN AND PAST THEM up the road, so EVERY PERSON IS "
            "SEEN FROM BEHIND and a gaze into the lens is geometrically "
            "impossible. THERE ARE EXACTLY SIX PEOPLE IN THIS PICTURE, separated "
            "far enough to be counted one by one, walking in a loose string toward "
            "the town: the servant leading at the front with a lamp low in his "
            "hand, then the old man in the patched charcoal mantle, then a woman "
            "with a lamp cupped low, then two more walking together with one "
            "steadying the other by the elbow, then a half-grown boy at the back. "
            "NOBODY IS DRAGGED, GRIPPED, PUSHED OR HERDED; they are walking in "
            "willingly. THIS IS A WIDE FULL-LENGTH SCENE: the pale dust highway "
            "runs ahead of them between rough banks of dry piled grey-brown "
            "leafless thorn toward the town's dark wall, where ONE plain stone "
            "gateway shows a warm lamplit opening. Deep blue-black star sky fills "
            "the upper third."
        ),
    },
    # ============ n10 — the closing application ===============================
    {
        "id": "v2-r035-b37", "out": "s37-that-is-how-good-he-is.jpeg",
        "seg": "n10", "window": "119.685-122.690", "wide": True, "jesus": False,
        "locks": _HALL_LAMP + ["POOR"], "char_refs": _HOST,
        "narration": "That is how good he is. When the ones who should have come",
        "must_show": "The host down on one knee at the low table beside the poor, filling an old man's clay cup from the wine jar with his own hands, serving them himself.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_MOCK + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 35mm lens, night, and the ONLY light TWO shallow "
            "fired-clay oil lamps with single small bare-wick flames standing LOW "
            "ON THE TABLE in front of both men, below both their chins and nearer "
            "the camera than either head, so the light comes UPWARD AND FORWARD "
            "onto the fronts of their faces and hands while every crown, back of "
            "head and shoulder stays UNLIT AND DARK. NO LIGHT SOURCE STANDS "
            "BEHIND, ABOVE OR BEYOND ANY HEAD; no rim, outline, corona on "
            "anybody. Fine film grain, shallow depth of field. THE CAMERA STANDS "
            "BEHIND AND ABOVE THE HOST AND SHOOTS DOWN AND PAST HIM across the "
            "table: he is at the LEFT, seen in three-quarter FROM BEHIND, DOWN ON "
            "ONE KNEE on the flagstones beside the reclining places with his deep "
            "indigo mantle fallen off one shoulder and his thick dark brown "
            "greying hair clear at the crown and nape, HIS FACE NOT VISIBLE, both "
            "hands on a plain fired-clay wine jar and TIPPING IT to pour — the "
            "wine is a dark thread in the lamplight and the cup is held steady "
            "under it. At the RIGHT an old man of about seventy in a patched "
            "charcoal tunic is propped on his LEFT elbow at the table holding that "
            "plain unstemmed clay cup up to be filled, seen in three-quarter from "
            "the side, his lit face turned down to the cup and his gaze exiting "
            "the frame through the BOTTOM EDGE. NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. THIS IS A WIDE FULL-LENGTH SCENE: beyond them the rest of the "
            "KNEE-HIGH table with four more of the poor reclining and eating, all "
            "turned to the food and to each other."
        ),
    },
    {
        "id": "v2-r035-b38", "out": "s38-he-opened-the-doors-wider.jpeg",
        "seg": "n10", "window": "122.690-126.230", "wide": True, "jesus": False,
        "locks": _HALL_LAMP + ["POOR", "SERVANT"], "char_refs": _HOST_SERV,
        "narration": "turned him down, he did not shrink his table. He opened the doors wider.",
        "must_show": "The whole lamplit hall from above with every place along all three arms of the low table now taken, the opening standing wide to the dark night and the servant bringing one more person in through it.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_MODERN_LAMP + _NO_MOCK + _NO_FORCE + _NO_CREAM + _GAZE,
        "scene": (
            "One photograph, 24mm lens, night, and the ONLY light FOUR shallow "
            "fired-clay oil lamps with single small bare-wick flames standing LOW "
            "ALONG THE TABLE, all of them below every chin in the room, so the "
            "light goes UPWARD AND FORWARD onto faces, hands, bread and clay while "
            "every crown and the back of every head stays UNLIT AND DARK and the "
            "ceiling above falls to black. NO LIGHT SOURCE STANDS BEHIND, ABOVE OR "
            "BEYOND ANY HEAD; no rim, outline, corona on anybody. Fine "
            "film grain, deep focus. THE CAMERA HANGS HIGH IN THE CORNER OF THE "
            "ROOM ABOVE AND BEHIND EVERYONE AND LOOKS STEEPLY DOWN ON THE WHOLE "
            "TABLE, so EVERY PERSON IS SEEN FROM ABOVE AND BEHIND, the tops of "
            "heads and backs toward the camera, and a gaze into the lens is "
            "geometrically impossible. THIS IS A WIDE FULL-LENGTH SCENE OF A FULL "
            "ROOM: along ALL THREE ARMS of the KNEE-HIGH U-shaped adzed-timber "
            "table the poor of the town and of the road recline propped on their "
            "left elbows, eating with their right hands, leaning to one another, "
            "hands reaching for bread — and NOT ONE MAT ALONG ANY ARM IS EMPTY. "
            "The fourth side is left open for serving. At the far side the broad "
            "opening STANDS WIDE TO THE BLACK NIGHT with its dark hanging cloth "
            "pushed right back and hooked aside, and the servant is coming through "
            "it with ONE more person, his open hand out low behind them in "
            "welcome, touching nobody. At the near LEFT the host stands seen from "
            "above and behind, his greying dark brown hair clear at the crown, "
            "looking down the full table. NOT ONE FACE IS TURNED TOWARD THE LENS."
        ),
    },
    {
        "id": "v2-r035-b39", "out": "s39-always-going-to-be-full.jpeg",
        "seg": "n10", "window": "126.230-130.650", "wide": False, "jesus": True, "ref": REF,
        "locks": _TABLE_JESUS,
        "narration": "The feast was always going to be full,",
        "must_show": "A close side-on view of Jesus back at the Pharisee's table finishing the parable, his lifted hand come to rest open on the wood, his face quiet.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 85mm lens, the flat hard sabbath daylight coming in "
            "almost level from the RIGHT and modelling the face from the front, "
            "the sun well out of frame and never behind his head, fine film grain, "
            "shallow but honest depth of field. THIS IS A STRICT SIDE-ON PROFILE "
            "AND THE CAMERA SITS EXACTLY ON HIS RIGHT: Jesus is seen half-length "
            "at the LEFT of the frame, propped on his left elbow at the low table "
            "and turned fully to the RIGHT, so the viewer sees ONE cheek, ONE eye, "
            "ONE ear and the clean outline of brow, nose, lips and beard against "
            "the pale limestone wall beyond. THE FAR CHEEK AND THE FAR EYE ARE "
            "COMPLETELY HIDDEN BEHIND THE BRIDGE OF HIS NOSE AND THE MASS OF HIS "
            "HEAD and cannot be seen at all; his one visible eye is level and "
            "steady on the man across the table from him and exits the picture "
            "through the RIGHT EDGE, so his pupils are nowhere near the lens. The "
            "story is finished: his lifted hand has come down and rests open and "
            "still on the bare adzed timber, his expression quiet and unguarded, "
            "neither stern nor smiling. Across the bottom third, close to the "
            "camera and softly out of focus, the near arm of the KNEE-HIGH table "
            "with a torn round of barley bread and a plain unstemmed clay cup on "
            "it. Behind him, out of focus in the dim room, ONE dark-clad shoulder "
            "of a reclining man in deep indigo, turned away. THE ONLY PALE WOOL IN "
            "THE PICTURE IS HIS OWN ROBE. His hair, beard, eyes and robe are "
            "exactly as locked."
        ),
    },
    {
        "id": "v2-r035-b40", "out": "s40-a-place-at-it-for-you.jpeg",
        "seg": "n10", "window": "130.650-134.190", "wide": True, "jesus": True, "ref": REF,
        "locks": _TABLE_JESUS,
        "narration": "and there has always been a place at it for you.",
        "must_show": "The whole Pharisee's sabbath room seen from behind and above, Jesus small at the far side of the low table, and one made-up reclining place standing empty and waiting nearest the camera on the open fourth side.",
        "must_not_show": _NO_HALO + _NO_HEAVEN + _NO_MODERN_DINE + _NO_CREAM + _NO_NIGHT + _GAZE,
        "scene": (
            "One photograph, 28mm lens, flat hard sabbath daylight falling through "
            "ONE high plain window opening in a single clean shaft across the "
            "flagstones, the sun well out of frame above and NEVER behind any "
            "head, fine film grain, deep focus. THE CAMERA STANDS LOW AND BEHIND "
            "THE OPEN FOURTH SIDE OF THE TABLE, BEHIND EVERY PERSON IN THE FRAME, "
            "and looks across the table into the room: because the camera is "
            "behind them all, EVERY MAN INCLUDING JESUS IS SEEN FROM BEHIND OR IN "
            "THREE-QUARTER FROM BEHIND, no eyes face the camera at all, and a gaze "
            "into the lens is geometrically impossible. THE THING NEAREST THE "
            "CAMERA IS AN EMPTY PLACE: right at the bottom of the frame, on the "
            "open fourth side, ONE reclining place lies made up and waiting — a "
            "dark folded hand-woven wool mat with a bolster set at its head, "
            "smooth and undisturbed — with a plain unstemmed fired-clay cup and a "
            "torn round of barley bread on the timber above it, and nobody on it. "
            "Beyond it the KNEE-HIGH U-shaped adzed-timber table runs away with "
            "four dark-clad men reclining along its far arms on their left elbows, "
            "seen from behind, and Jesus among them at the far side, small, "
            "half-turned away, one hand open on the wood. THIS IS A WIDE "
            "FULL-LENGTH SCENE of the whole plain room — bare pale limestone "
            "walls, rough hewn beams, worn flagstones, one plain woven hanging — "
            "and THE ONLY PALE WOOL IN THE WHOLE PICTURE IS HIS OWN ROBE; every "
            "other man is a solid dark saturated mass of indigo, umber, rust, "
            "olive, charcoal or maroon."
        ),
    },
]
