#!/usr/bin/env python3
"""V2 beat map — row 8, build-08-lost-coin (Luke 15:8-10).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v5 (the live lock) are prepended by
the assembler so they stay byte-identical across every prompt.

WINDOWS RE-TIMED 2026-08-01 from the FIXED extract_beats.py (the old windows
carried the raw-vs-trimmed drift — up to 4.2 s late by n5). All starts are
absolute phrase times verified against the real V1 audio with silencedetect
(every boundary within 0.1 s). The b02/b03 split inside jv8 (10.60) sits in the
measured mid-sentence pause after "silver," (raw jv8.mp3 silence 2.80-3.50 →
absolute 10.25-10.95).

COVERAGE (STORY-COVERAGE-LAW): 12 pictures against V1's 6 unique stills, over
58.2 s — the shortest row in the queue, and the only one where the scaled target
(~9) sits BELOW the law's floor of 10. It comes in at 12 because the middle of
this narration is a genuine burst: "She loses one. / She lights a lamp. / She
sweeps the whole house." are three separate one-second sentences describing three
separate physical actions, and Cameron's burst rule gives each its own frame.
Six of the twelve are that chain. Nothing here is a held mood shot.

V1 BUILT THIS ROW AROUND A STARFIELD — four of its six stills were `stars.jpeg`.
V2 does not do that. Every abstract beat is re-staged on PEOPLE: the frame story
returns to Jesus and the crowd instead of cutting to a sky, and the closing "over
ONE" lands on one human face rather than a cosmos.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Luke 15:8-10 KJV):
  v8  "TEN pieces of silver" — she has exactly ten and loses exactly one, so the
      counting frames must be countable: nine and a gap, never a vague handful.
  v8  "doth not LIGHT A CANDLE" — the KJV "candle" is a small clay OIL LAMP, not
      a wax candle. A poor Galilean one-room house has one high window and is
      dark enough at midday that she needs it. Never paint a wax candle.
  v8  "and SWEEP the house" — a twig broom on a rough floor. She is partly
      listening for the coin to ring on stone, which is why the sweeping frame
      shows her head turned and still.
  v8  "and SEEK DILIGENTLY TILL she find it" — the narration underlines it: "not
      casually, carefully." b07 is on hands and knees with the lamp down at floor
      level and a heavy jar shifted aside. Diligence has to be visible.
  v9  "she calleth her FRIENDS and her NEIGHBOURS together" — the joy is public
      and immediate; she goes to the door with it.
  v10 "joy in the presence of the ANGELS OF GOD" — see CONTENT-CARE below.

CONTENT-CARE: row 8 is not in the §3 flag table = GREEN. One restraint is
applied on principle anyway. v10 names the angels of God, and this build DOES
NOT PAINT THEM — same logic as the adversary law from the other side: we do not
render what we have not been shown. b11 stays on Jesus and the faces of the
people listening to him, and lets the sentence do its own work. No heavenly
host, no shafts of light from the sky, no glowing figures.

THE ONE STRUCTURAL TRAP IN THIS ROW: Jesus states the whole parable in jv8
(10.4 s) and then the narrator walks through the SAME actions again in n1/n2a/n2b.
If both passes get the same pictures the video repeats itself inside forty
seconds. So the two passes are split by content: jv8 gets the COINS (having them,
then the gap where one was) and the narrator's pass gets the SEARCH (lamp, broom,
hands and knees). Same story, no repeated frame.

TIME OF DAY: one ordinary working day. Bright hard daylight outside the low
doorway; the inside of the house is deep shadow lit only by the small lamp and
one shaft from the high window — which is exactly why a woman lights a lamp at
noon to look for a coin. The celebration at the end is in that same daylight
outside her door.
"""

from pathlib import Path

OUTPUT_ASSET_DIR = "assets-realistic"
OUTPUT_VIDEO_NAME = "luke-15_lost-coin-realistic-v2.mp4"

# Identity anchor by IMAGE (CAST-BIBLE principle; row-2 CAST-DRIFT lesson —
# text locks alone do not hold a recurring face across 10 shots). The woman is
# the only story-local recurring character; her ONE canonical anchor is a
# neutral bust portrait generated this session, and every beat naming the
# WOMAN lock attaches it automatically.
REFS = {
    "WOMAN": "CAST-REF-V2/woman-ref.jpeg",
}

LOCKS = {
    # Realistic-cinematography lock, byte-identical wherever named (build-02
    # pattern): the Session 6 rejection was flat noon light, posed extras and
    # camera-gaze on every frame.
    "CAMERA": (
        "CAMERA LOCK: photographed like a real film still on location with a real "
        "cinema lens — light arrives from ONE believable direction and models "
        "faces with true shadow, shallow depth of field holds the subject sharp "
        "while the background falls gently away, and every person is caught "
        "mid-action in a truthful candid instant, never posed, never lined up, "
        "and NEVER looking at the camera."
    ),
    "WOMAN": (
        "WOMAN LOCK: the woman is the same person in every shot — a poor Galilean "
        "village woman of about forty, small and thin and strong, a sun-weathered "
        "face with fine lines, dark eyes, dark hair pulled back under a faded "
        "DUSTY-OCHRE headcloth. She wears a much-mended DARK RUSSET-BROWN wool robe "
        "with a plain woven sash and worn leather sandals (never cream, never white). "
        "Her hands are thin, strong and work-roughened. Her face is shown clearly."
    ),
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect).
    "HOUSE": (
        "HOUSE LOCK: one poor single-room Galilean village house — a floor of rough "
        "uneven flagstones with wide dirt-packed gaps between them, low walls of "
        "undressed stone and mud plaster darkened by years of smoke, a heavy timber "
        "roof beam, one small high window throwing a single hard shaft of daylight, "
        "and a low doorway open to the bright lane. A rolled sleeping mat, two large "
        "clay storage jars, a hand grindstone, a stack of reed baskets and a "
        "twig-bundle broom stand around the walls, with chaff and straw across the "
        "floor. Away from the window shaft the room is deep shadow, dark enough at "
        "midday to need a lamp."
    ),
    "LANE": (
        "LANE LOCK: the narrow lane outside — low flat-roofed village houses of "
        "rough stone and mud plaster crowded close, worn dirt underfoot, clay water "
        "jars and reed baskets against the walls, a shared courtyard with a fig tree, "
        "dry hills beyond the rooftops. The neighbour women and men are ordinary "
        "villagers in SATURATED DEEP earth colours — dark chocolate brown, deep "
        "russet, burnt ochre, dark olive, dusty indigo and faded plum wool. No "
        "villager wears off-white, ivory or any near-white cloth."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the people gathered to hear are ordinary working Galileans "
        "and tax collectors of every age — labourers, fishermen, women with children, "
        "two or three older men — seated close on the ground and on a low stone wall. "
        "They wear SATURATED DEEP earth colours: dark chocolate brown, deep russet, "
        "burnt ochre, dark olive, dusty indigo and faded plum wool. No one in the "
        "crowd wears off-white, ivory or any near-white cloth. Their faces are shown "
        "clearly."
    ),
}

REF = True

BEATS = [
    # -------------------------------------------------- n0 — the frame story ----
    {
        "id": "v2-r008-b01", "out": "s01-he-told-this-story.jpeg", "seg": "n0",
        "window": "0.28-7.45", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "LISTENERS", "LANE"],
        "narration": ("When Jesus wanted to show how God feels about one lost soul, "
                      "he didn't talk about crowds. He told this story."),
        "must_show": "Jesus sitting low among ordinary people in a village courtyard, beginning a story with an open hand — everyone close in and listening.",
        "must_not_show": "no halo, glare or rim-light; he is not raised above them or set apart at the frame edge — he is down at their level and every gaze converges on him. NOBODY — Jesus included — looks toward the camera; he looks at the people he is talking to.",
        "scene": (
            "In a small village courtyard under a fig tree in bright daylight, Jesus "
            "sits on a low stone wall with ordinary working people gathered close "
            "around him on the ground — a labourer with his knees up, a tax collector "
            "still in his good belt, two women with children leaning against them, an "
            "old man on a stool. Jesus has one hand open in the easy gesture of a man "
            "starting a story, and every face in the courtyard is turned in toward "
            "him. The camera is back far enough to hold him and the whole seated "
            "group head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ jv8 — the ten and the gap ----
    {
        "id": "v2-r008-b02", "out": "s02-ten-pieces-of-silver.jpeg", "seg": "jv8 p1a",
        "window": "7.45-10.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "HOUSE"],
        "narration": ("Either what woman having ten pieces of silver, (Luke 15:8)"),
        "must_show": "TEN countable silver coins — laid out in a row on a worn cloth across her knees, her hands touching them, everything she has.",
        "must_not_show": "not a vague handful and not a purse of money — the viewer must be able to count them; nothing rich or ornamental anywhere in the frame.",
        "scene": (
            "Close on the woman sitting on the floor of her house in the single hard "
            "shaft of daylight from the high window, a worn dark cloth spread across "
            "her knees. Laid out on it in ONE single straight row are EXACTLY NINE small dull "
            "silver coins — count them, nine in a line, evenly spaced, every coin "
            "flat and fully visible, none overlapping, none on its edge — and she "
            "holds the TENTH coin up between finger and thumb above the end of the "
            "row: nine and one, ten pieces of silver and not one more. Neither of "
            "her hands covers any coin in the row. Her weathered face is quiet and careful — this is everything she "
            "has. The dark room falls away around the shaft of light. Each hand has "
            "five fingers."
        ),
    },
    {
        "id": "v2-r008-b03", "out": "s03-one-is-missing.jpeg", "seg": "jv8 p1b",
        "window": "10.60-19.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "HOUSE"],
        "narration": ("if she lose one piece, doth not light a candle, and sweep the "
                      "house, and seek diligently till she find it? (Luke 15:8)"),
        "must_show": "NINE coins and an obvious empty gap in the row where the tenth should be — her hand stopped over it, her face gone still.",
        "must_not_show": "no panic yet and no tears — this is the quiet second before, and the gap in the row has to be unmistakable.",
        "scene": (
            "The same cloth, closer. There are now EXACTLY NINE silver coins in the row — FIVE to the left "
            "of a bare empty space and FOUR to the right of it, none overlapping — "
            "where the tenth coin should be, the worn weave of the cloth showing "
            "through the gap. The woman's hand has "
            "stopped dead just above that space, fingers slightly spread. Above the "
            "cloth her weathered face has gone completely still, her eyes fixed down "
            "on the gap, all the colour of the moment draining out of her. The shaft "
            "of daylight cuts across the cloth. Each hand has five fingers."
        ),
    },
    # ------------------------------------------- n1 / n2a / n2b — the search ----
    {
        "id": "v2-r008-b04", "out": "s04-she-loses-one.jpeg", "seg": "n1",
        "window": "19.26-21.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "HOUSE"],
        "narration": "She loses one.",
        "must_show": "her hands scrabbling through the folds of the cloth and shaking it out, checking the floor at her feet — the first frantic seconds.",
        "must_not_show": "she has not begun the real search yet; no lamp lit in this frame.",
        "scene": (
            "An upright vertical photograph from a low viewpoint, with the floor at "
            "the bottom of the frame and the room above it and the horizon level — "
            "the picture is the right way up. The woman is up on her knees on the "
            "flagstones with the "
            "worn cloth caught up in both hands, shaking it out hard and dragging her "
            "fingers through its folds, the nine coins spilled and rolling on the "
            "stone beside her. Her head is down and turned, eyes already searching the "
            "gaps between the flagstones around her knees. Chaff lifts off the floor "
            "in the shaft of window light. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r008-b05", "out": "s05-she-lights-a-lamp.jpeg", "seg": "n2a p1",
        "window": "21.18-22.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "HOUSE"],
        "narration": "She lights a lamp.",
        "must_show": "a small CLAY OIL LAMP with its wick just catching in her cupped hands, the tiny flame the brightest thing in a dark room.",
        "must_not_show": "NEVER a wax candle — the KJV 'candle' is an oil lamp; no lantern, no torch, no modern light of any kind.",
        "scene": (
            "Close on the woman's hands and face in the dark part of the room. She is "
            "holding a small shallow clay oil lamp in one cupped hand and the wick has "
            "just caught — a single small yellow flame standing up off the spout, the "
            "brightest thing in the frame, throwing warm light up onto her cheekbones "
            "and her intent lowered eyes and leaving the rough stone walls behind her "
            "in deep shadow. Her other hand is curled around the flame to shelter it. "
            "Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r008-b06", "out": "s06-she-sweeps-the-house.jpeg", "seg": "n2a p2",
        "window": "22.17-24.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "HOUSE"],
        "narration": "She sweeps the whole house.",
        "must_show": "ACTION-LOGIC: the twig broom actually IN CONTACT with the floor mid-stroke, dust and chaff lifting ahead of it, the lamp set down low on the stones nearby.",
        "must_not_show": "no broom held in the air doing nothing; she is not standing idle — the stroke must be visibly happening. She is COMPLETELY ALONE in her house: no other person, no face, no figure in any doorway or shadow anywhere in the frame.",
        "scene": (
            "The woman sweeps the flagstone floor of the single room, the bundled twig "
            "broom pressed down hard against the stone mid-stroke and a low cloud of "
            "chaff and dust rolling up ahead of its bristles. She has set the little "
            "clay lamp down on the floor a pace away so its light rakes flat across "
            "the stones, and her head is turned and held very still as she sweeps — "
            "she is listening for the coin to ring. The dark room, the storage jars "
            "and the high window shaft are around her. The camera is back far enough "
            "to see her head to sandals. She has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r008-b07", "out": "s07-seek-diligently.jpeg", "seg": "n2b",
        "window": "24.59-30.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "HOUSE"],
        "narration": ("She searches carefully — not casually, carefully — until she "
                      "finds it."),
        "must_show": "DILIGENCE MADE VISIBLE: down on hands and knees with her cheek near the floor, the lamp held low along the stones, a heavy storage jar shifted out from the wall behind her.",
        "must_not_show": "nothing casual anywhere in the frame — no standing and glancing about; the room must look like it has been taken apart. She is COMPLETELY ALONE: if the doorway or lane shows at all it is EMPTY — no person, no animal, no figure outside.",
        "scene": (
            "An upright vertical photograph with the floor at the bottom of the "
            "frame and the walls standing vertical — the picture is the right way "
            "up, never rotated. The woman is down on her hands and knees on the flagstones with her "
            "shoulder almost on the floor and her cheek turned low, holding the little "
            "clay lamp out at arm's length so its light rakes flat along the stone and "
            "throws every crack and gap into hard relief. Her other hand is pushed "
            "into the gap under the wall. Behind her one of the heavy clay storage "
            "jars has been dragged out from the wall, the sleeping mat is unrolled and "
            "flung aside and the baskets are tipped over — the whole room has been "
            "taken apart. Her face is set with absolute concentration. The camera is "
            "back far enough to hold her and the ransacked room. She has two arms, two "
            "hands and one head."
        ),
    },
    # ------------------------------------------------- jv9a / j1 / n3 — found ----
    {
        "id": "v2-r008-b08", "out": "s08-she-found-it.jpeg", "seg": "jv9a",
        "window": "30.23-36.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "HOUSE"],
        "narration": ("And when she hath found it, she calleth her friends and her "
                      "neighbours together, saying, (Luke 15:9)"),
        "must_show": "THE FIND — the small silver coin pinched up between her finger and thumb in the lamplight, and her whole face breaking open above it.",
        "must_not_show": "no light coming off the coin itself and nothing supernatural — it is a dull worn coin and the joy is entirely on her face.",
        "scene": (
            "Close on the woman still down on the floor, the little clay lamp beside "
            "her. She has the lost silver coin pinched up between her finger and "
            "thumb, held out into the lamplight, dull and worn and small. Her whole "
            "weathered face has broken open above it — mouth wide, eyes shut tight "
            "with relief, tears already coming, her other hand pressed flat to her "
            "chest. The warm lamplight is full on her face and the ransacked dark room "
            "is behind her. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r008-b09", "out": "s09-rejoice-with-me.jpeg", "seg": "j1 + n3",
        "window": "36.12-44.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "LANE"],
        "narration": ("Rejoice with me; for I have found the piece which I had lost. "
                      "(Luke 15:9) — Then she calls her neighbors and friends to "
                      "celebrate."),
        "must_show": "her out in her low doorway in the bright daylight, the coin held up high between her fingers, calling down the lane — and neighbour women already coming toward her.",
        "must_not_show": "do not put Jesus in this frame; nobody is indoors any more — the joy has gone public and that is the point.",
        "scene": (
            "The woman has come out into the hard bright daylight of the lane and "
            "stands in her own low doorway with the little silver coin held up high "
            "between finger and thumb above her head, her other arm flung wide, "
            "shouting down the lane with her face full of laughter. Along the lane "
            "neighbour women are already turning and coming toward her — one hurrying "
            "with a water jar still on her hip, another leaning out of a doorway with "
            "both hands raised, a child running ahead of them. The camera is back far "
            "enough to hold her doorway and the neighbours coming. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r008-b10", "out": "s10-all-this-over-one.jpeg", "seg": "n4",
        "window": "44.84-50.64", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "LANE"],
        "narration": ("One coin. Out of ten. The joy is disproportionate to the value "
                      "of the coin."),
        "must_show": "a full celebration in the little courtyard — a dozen neighbours crowded around her, laughing, clapping, food already coming out — over one small coin.",
        "must_not_show": "the celebration must look far too big for what was found; that mismatch is the entire point of the beat. Do not put Jesus in this frame.",
        "scene": (
            "The narrow courtyard outside her house is full of people. A dozen "
            "neighbour women and men have crowded in around her, laughing and "
            "clapping, one with both hands on her shoulders shaking her, another "
            "already carrying out a platter of bread and olives, two children chasing "
            "between the legs of the adults. In the middle of all of it the woman "
            "stands holding up one small dull silver coin between her fingers — a "
            "whole street's worth of joy over a single coin. Bright daylight, the fig "
            "tree, the low rooftops. The camera is back far enough to hold the whole "
            "crowded courtyard. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------------ j2 / n5 — the point ----
    {
        "id": "v2-r008-b11", "out": "s11-joy-over-one-sinner.jpeg", "seg": "j2",
        "window": "50.64-59.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "LISTENERS", "LANE"],
        "narration": ("Likewise, I say unto you, there is joy in the presence of the "
                      "angels of God over one sinner that repenteth. (Luke 15:10)"),
        "must_show": "back in the courtyard with Jesus finishing the story — his face warm and glad as he says it, the listening faces around him beginning to understand.",
        "must_not_show": "CONTENT-CARE — do NOT paint the angels, heaven, a heavenly host, or any shaft of light from the sky; nothing supernatural is in this frame. No halo, glare or rim-light on Jesus. His eyes rest on the LISTENERS beside and below him, in profile-to-three-quarter — he NEVER looks toward the camera, and neither does anyone else.",
        "scene": (
            "Back in the village courtyard in daylight. Jesus is finishing the story, "
            "leaning forward from the low wall with both hands open, and his face is "
            "warm and openly glad — a man telling people the best thing he knows. All "
            "around him the seated listeners are still — the tax collector with his "
            "head slightly back as it lands, a woman's hand come up to her mouth, the "
            "old man on the stool leaning in. Ordinary bright daylight and the fig "
            "tree above them; nothing in the sky. The camera is back far enough to "
            "hold Jesus and the group head to sandals. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r008-b12", "out": "s12-over-one.jpeg", "seg": "n5",
        "window": "59.94-62.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "LISTENERS"],
        "narration": "Over one. Not a crowd. One.",
        "must_show": "ONE FACE. Close on a single ordinary person in that crowd — a tax collector — realising the story was about him.",
        "must_not_show": "no crowd, no wide shot, nothing abstract and no starfield — the whole beat is one human face; do not put Jesus in the frame.",
        "scene": (
            "Very close on the face of one man sitting in the crowd — an ordinary tax "
            "collector in the middle of his thirties, a plain tired face, a short dark "
            "beard, dust on his shoulders. He is completely still and his eyes are "
            "fixed and shining, his jaw loose, as it arrives on him that the story was "
            "about one person and that the one person is him. The blurred shapes of "
            "the other listeners and the sunlit courtyard wall are soft behind him. "
            "Nothing else is in the frame."
        ),
    },
]

# ROUGH-DRAFT CONTINUITY (build-02/05 pattern): the rejected-look 2026-07-29
# still for a beat, when it exists, is attached as the approved rough draft —
# its camera angle, blocking and travel directions stand; faces and identity
# always come from the FACE/CHARACTER lock images, never from the draft.
# b11's old take FAILED at generation (no jpeg exists), so it wires nothing.
# The two Jesus beats (b01/b11) keep their roughs on trial: their old Jesus is
# the pre-V5 face, so QC watches those two frames for face-echo and the rough
# is dropped on any reroll (the row-2 b20 lesson).
_NO_ROUGH = {"v2-r008-b01", "v2-r008-b02", "v2-r008-b03", "v2-r008-b07"}  # b01 rough echoed the pre-V5 Jesus face; b02/b03 roughs carry uncountable coin piles; b07 rough drew two 90-degree-rotated takes (ROTATION-TRAP)
for _beat in BEATS:
    _asset = Path(__file__).resolve().parent / "assets" / _beat["out"]
    if _asset.is_file() and _beat["id"] not in _NO_ROUGH:
        _beat["rough_ref"] = str(_asset)
