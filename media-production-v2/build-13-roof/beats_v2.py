#!/usr/bin/env python3
"""V2 beat map — row 13, build-13-roof (Mark 2:1-12).

COVERAGE: 45 pictures against V1's 11, over 257.7 s = 5.7 s/picture.

SCRIPTURE FACTS (Mark 2:1-12 KJV):
  v1-2 Capernaum, "it was noised that he was IN THE HOUSE ... insomuch that there
       was NO ROOM to receive them, no, not so much as ABOUT THE DOOR."
  v3   "one sick of the palsy, which was BORNE OF FOUR" — four bearers, one at
       each corner, and that number is stated in the narration too.
  v4   "they UNCOVERED THE ROOF where he was: and when they had BROKEN IT UP,
       they LET DOWN THE BED wherein the sick of the palsy lay." A first-century
       Galilean roof is packed clay over reeds on beams, with an outside stair —
       diggable by hand, which is why this is possible rather than absurd.
  v5   "When Jesus saw THEIR FAITH" — the friends'. The paralysed man never
       speaks in the whole passage. n4 spends 20 seconds on that word.
  v5   "Son, thy sins be forgiven thee" — the FIRST thing said, before the legs.
  v6-7 the scribes "REASONING IN THEIR HEARTS" — they say nothing aloud, and
       b30-b32 must show closed mouths and moving eyes, never an outburst.
  v8   "Jesus PERCEIVED IN HIS SPIRIT that they so reasoned within themselves" —
       he answers what was never said.
  v11  "Arise, and take up thy bed, and go thy way into thine house."
  v12  "immediately he arose, TOOK UP THE BED, and WENT FORTH BEFORE THEM ALL."

THE MAT IS A PROP THAT MUST TRACK: carried by four at the corners (b01-b12) ->
lowered on four ropes (b16-b19) -> lying under him on the floor (b20-b38) ->
rolled up and tucked under his own arm (b41-b45). The thing that carried him is
the thing he carries out.

THE LEGS CHANGE, so the PARALYTIC lock fixes face, build and clothing and says
NOTHING about his legs — per beat: limp and useless through b39, trembling and
holding him from b40 on.

CONTENT-CARE: row 13 is GREEN. His paralysis is never grotesque — thin unused
legs and a carried body, never a medical close-up, never played for pity. His
dignity is intact in every frame; the friends treat him with enormous care.

TIME OF DAY: one bright morning. The house interior is DIM — small windows, a
packed crowd blocking the door — which is what makes the hole in the roof pour
daylight into it at b16. That contrast is the build's best visual idea and must
survive: dark room, one shaft of hard daylight, dust and straw falling through it.
"""

from pathlib import Path

OUTPUT_ASSET_DIR = "assets-realistic"
OUTPUT_VIDEO_NAME = "mark-2_man-through-the-roof-realistic-v2.mp4"
_BUILD = Path(__file__).resolve().parent

# Stable, accepted identity anchors for this one-story cast. Each person has
# exactly one non-conflicting face image. The old five-man group image remains
# useful as provenance, but it contains a different version of the paralysed
# man and therefore must never be supplied to generation or repair.
FRIEND_REFS = [
    str(_BUILD / "character-refs" / "friend-broad-black-beard.jpeg"),
    str(_BUILD / "character-refs" / "friend-wiry-grey-hair.jpeg"),
    str(_BUILD / "character-refs" / "friend-young-thin-beard.jpeg"),
    str(_BUILD / "character-refs" / "friend-shaved-stocky.jpeg"),
]
PARALYTIC_REF = str(_BUILD / "character-refs" / "paralysed-man.jpeg")

LOCKS = {
    "PARALYTIC": (
        "PARALYSED MAN LOCK: the man on the mat is the same person in every shot — a "
        "Jewish man of about thirty, thin and light from years of being carried, warm "
        "olive skin gone sallow from little sun, a short dark beard, dark hair, and a "
        "quiet watchful face with large dark eyes that miss nothing. He wears a plain "
        "DARK GREY-BROWN wool tunic, clean and cared for by other people (never "
        "cream, never white). His face is shown clearly and always with dignity."
    ),
    "FRIENDS": (
        "FOUR FRIENDS LOCK: the four bearers are the same four men in every shot — "
        "working Galilean men in their late twenties and thirties, strong and "
        "sun-browned: a big broad-shouldered one with a full black beard, a wiry "
        "older one with grey in his hair, a young one barely twenty with a thin "
        "beard, and a stocky one with a shaved head and thick arms. They wear "
        "work-stained wool tunics in SATURATED DEEP colours — rust-brown, dark olive, "
        "deep russet and blue-grey — belted with rope. None wears off-white, ivory or "
        "any near-white cloth. Their faces are shown clearly."
    ),
    "MAT": (
        "MAT LOCK: the bed is one particular object — a plain woven sleeping mat of "
        "pale straw-coloured reed and rush, about the length of a man, worn soft and "
        "dark at the middle from long use, with a rolled cloth at one end for a "
        "pillow and four short lengths of rope knotted to its corners."
    ),
    "HOUSE": (
        "HOUSE LOCK: a small Capernaum fisherman's house of rough dark basalt stone — "
        "one low crowded room with a beaten earth floor, thick walls, two small high "
        "windows letting in very little light, a low doorway, clay jars and a "
        "grindstone along the walls, and a FLAT ROOF of packed clay laid over "
        "close-set reeds on rough wooden beams, reached by narrow stone stairs "
        "climbing the outside wall. Inside the room is DIM and close."
    ),
    "SCRIBES": (
        "SCRIBES LOCK: the religious experts are the same three or four men in every "
        "shot — older scholars with long carefully combed grey and iron-grey beards, "
        "sharp deep-set eyes, an air of settled authority. They wear finely woven, "
        "DEEPLY DYED robes of NEAR-BLACK indigo and DARK UMBER with woven dark-red "
        "borders, and prayer shawls of that SAME saturated near-black wool with dark "
        "stripes and dark fringe. They are seated together apart from the crowd. "
        "Their faces are shown clearly."
    ),
    "CROWD": (
        "CROWD LOCK: the townspeople of Capernaum packing the house — fishermen, "
        "labourers, women, old men and children, pressed shoulder to shoulder. They "
        "wear SATURATED DEEP earth colours: dark chocolate brown, deep russet, burnt "
        "ochre, dark olive, dusty indigo and faded plum wool. No one in the crowd "
        "wears off-white, ivory or any near-white cloth."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------- n0 — four men carrying ----
    {
        "id": "v2-r013-b01", "out": "s01-capernaum.jpeg", "seg": "n0 p1-p2",
        "window": "0.28-5.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["HOUSE", "CROWD"],
        "narration": ("Capernaum, on the north shore of the Sea of Galilee. Jesus was "
                      "home — and the word got out."),
        "must_show": "the dark basalt village on the lake shore in bright morning, with a crowd already converging on one small house.",
        "must_not_show": "no principal characters yet; do not put Jesus in this frame.",
        "scene": (
            "A wide morning view of the small fishing village of Capernaum — low "
            "houses of rough dark basalt stone crowded along narrow lanes, fishing "
            "boats drawn up on the shingle and the flat blue lake beyond. People are "
            "converging from every lane toward one particular house, a stream of them "
            "hurrying in the same direction. Hard bright morning light on the black "
            "stone. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b02", "out": "s02-one-at-each-corner.jpeg", "seg": "n0 p3",
        "window": "5.51-15.16", "wide": True, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "FRIENDS", "MAT", "HOUSE"],
        "narration": ("By the time four men came up the street carrying their friend on "
                      "a sleeping mat, one at each corner, the house he was teaching in "
                      "had already swallowed half the town."),
        "must_show": "SCRIPTURE-EXACT: FOUR men, ONE AT EACH CORNER of the mat, carrying it level up the street, with the packed house ahead of them.",
        "must_not_show": "not two bearers and not a stretcher — four men, four corners; the man on the mat is carried with visible care.",
        "scene": (
            "Four working men come up the narrow basalt street carrying a woven reed "
            "sleeping mat between them, ONE MAN AT EACH CORNER, holding it level and "
            "steady at waist height. On it lies a thin young man, his head on a rolled "
            "cloth, watching the sky go past. Ahead of them at the end of the street "
            "the small stone house is completely surrounded, a crowd jammed solid "
            "around its door. Hard morning light. The camera is back far enough to see "
            "all five men head to sandals. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r013-b03", "out": "s03-he-could-not-walk.jpeg", "seg": "n0 p4-p5",
        "window": "15.16-18.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT"],
        "narration": "The man on the mat was paralyzed. He could not walk to Jesus.",
        "must_show": "close on the man lying on the mat — his face alert and present, his legs still and thin beneath the tunic.",
        "must_not_show": "CONTENT-CARE — no medical close-up of the legs, nothing grotesque, nothing played for pity. His face carries it, and it carries dignity.",
        "scene": (
            "Close on the young man lying on the woven reed mat as it is carried, seen "
            "from above and to the side. His face is calm, alert and completely "
            "present — dark eyes open and moving, taking everything in. Below, his "
            "legs lie perfectly still and thin under the plain grey-brown tunic, "
            "turned slightly inward, not moving at all with the motion of the mat. The "
            "hands of two bearers grip the corners at the frame's edges. Bright "
            "morning light. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b04", "out": "s04-they-decided-anyway.jpeg", "seg": "n0 p6",
        "window": "18.65-22.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["FRIENDS"],
        "narration": ("So the people who loved him decided he would get there anyway."),
        "must_show": "the four friends' faces close — determined, fond, entirely set on this; men who are not going to be stopped.",
        "must_not_show": "not grim; there is affection and stubbornness in it together.",
        "scene": (
            "Close on the four friends' faces as they carry, framed together. The big "
            "black-bearded one has his jaw set, the wiry grey-haired one is glancing "
            "ahead and calculating, the young one's eyes are bright and fixed, and the "
            "stocky shaven-headed one is grinning with effort. Every face is "
            "determined and fond at once. Sweat and dust on all of them in the hard "
            "morning light. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n1 — a wall of backs ----
    {
        "id": "v2-r013-b05", "out": "s05-a-wall-of-backs.jpeg", "seg": "n1 p1",
        "window": "22.75-25.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "HOUSE"],
        "narration": "But the doorway was a wall of backs.",
        "must_show": "the low doorway completely blocked by a solid mass of people packed into it, seen from outside — no gap at all.",
        "must_not_show": "not a single visible gap; do not put Jesus in this frame.",
        "scene": (
            "The low stone doorway of the house, seen from the street, is completely "
            "filled and blocked by a solid wall of human backs and shoulders — people "
            "jammed into the opening and standing three deep in front of it, craning "
            "and pressing forward, not one gap anywhere in the mass. The dark basalt "
            "wall rises around them. Hard morning light on the crowd. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b06", "out": "s06-no-one-giving-up-a-spot.jpeg", "seg": "n1 p2",
        "window": "25.18-33.78", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "PARALYTIC", "FRIENDS", "MAT", "HOUSE"],
        "narration": ("People packed the room, packed the doorway, spilled into the "
                      "street — no one was giving up a spot, not even for a man on a "
                      "mat."),
        "must_show": "the four friends pressed up against the outside of the crowd with the mat, and people glancing at them and turning away without moving.",
        "must_not_show": "nobody is cruel; they simply will not give up their place, which is worse.",
        "scene": (
            "The four friends have got the mat right up against the back of the crowd "
            "outside the house and can go no further. Two of them are calling and "
            "gesturing, and the people nearest have turned to look — one glances down "
            "at the man on the mat, then turns his shoulder back to the door without "
            "moving an inch; a woman shrugs helplessly and stays exactly where she is. "
            "The crowd spills out into the street around them. Hard sun. The camera is "
            "back far enough to see the friends, the mat and the crowd. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b07", "out": "s07-breathing-hard.jpeg", "seg": "n1 p3",
        "window": "33.78-40.14", "wide": True, "jesus": False, "ref": False,
        "locks": ["FRIENDS", "PARALYTIC", "MAT", "CROWD"],
        "narration": ("Four friends stood there breathing hard, holding their friend, "
                      "staring at an impossible crowd."),
        "must_show": "the four stopped, arms shaking with the weight, chests heaving, staring at a crowd they cannot get through — and still holding the mat level.",
        "must_not_show": "they have NOT set the mat down; holding it steady while defeated is the picture.",
        "scene": (
            "The four friends stand halted in the street still holding the mat level "
            "between them, their arms trembling with the weight and their chests "
            "heaving. All four are staring past the camera at the impossible packed "
            "crowd, faces running with sweat, the young one's mouth open. On the mat "
            "between them the young man lies quietly watching their faces. Nobody has "
            "put anything down. Hard morning light and dust. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b08", "out": "s08-one-of-them-looked-up.jpeg", "seg": "n1 p4-p5",
        "window": "40.14-43.05", "wide": True, "jesus": False, "ref": False,
        "locks": ["FRIENDS", "HOUSE"],
        "narration": "And then one of them looked up. At the roof.",
        "must_show": "one friend's head tipped back looking up at the flat roofline and the outside stair — the idea arriving.",
        "must_not_show": "only one of them is looking up yet; the others are still facing the door.",
        "scene": (
            "The wiry grey-haired friend has tipped his head right back and is looking "
            "straight up at the flat clay roofline of the house above them and at the "
            "narrow stone stairway climbing the outside wall toward it. His eyes have "
            "narrowed and something has just arrived behind them. The other three are "
            "still facing the blocked doorway and have not noticed. The dark basalt "
            "wall and the bright sky rise above. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    # ------------------------------------------------------ n2 — the digging ----
    {
        "id": "v2-r013-b09", "out": "s09-clay-over-reeds.jpeg", "seg": "n2 p1",
        "window": "43.30-51.57", "wide": True, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": ("Here is something worth knowing: houses there had flat roofs of "
                      "packed clay over reeds and beams, with a stairway up the outside "
                      "wall."),
        "must_show": "the construction, plainly readable: the flat clay roof surface, the reed layer and wooden beams at a broken edge, and the stone stair going up the outside.",
        "must_not_show": "no people needed; this frame exists to make the next four believable.",
        "scene": (
            "A clear view of the house from the side and slightly above, showing how "
            "it is built: a flat roof of smooth packed clay, and at its broken outer "
            "edge the layers are visible — packed clay laid over tightly bundled reeds "
            "laid across rough wooden beams. A narrow stone stairway with no rail "
            "climbs the outside wall to the roof. Bright morning sun and hard shadow "
            "on the black basalt."
        ),
    },
    {
        "id": "v2-r013-b10", "out": "s10-dig-it-with-your-hands.jpeg", "seg": "n2 p2-p3",
        "window": "51.57-58.60", "wide": True, "jesus": False, "ref": False,
        "locks": ["FRIENDS", "PARALYTIC", "MAT", "HOUSE"],
        "narration": ("You could dig through one with your hands in a few minutes — and "
                      "patch it in a day. Which is exactly what they did."),
        "must_show": "the four hauling the mat up the narrow outside stair — awkward, careful, the man held level, one steadying from below.",
        "must_not_show": "the man must never look unsafe or undignified; they are enormously careful with him.",
        "scene": (
            "The four friends are hauling the mat up the narrow stone stair on the "
            "outside of the house — two above walking backwards with the top corners, "
            "two below lifting the bottom end high, all of them working to keep the "
            "mat level. The young man lies steady on it with one hand gripping the "
            "reed edge, calm. The stair is narrow and has no rail and they are taking "
            "enormous care. Hard morning sun on the black wall. The camera is back far "
            "enough to see all of them. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r013-b11", "out": "s11-tearing-through-the-clay.jpeg", "seg": "n2 p4",
        "window": "58.60-68.41", "wide": True, "jesus": False, "ref": False,
        "locks": ["FRIENDS", "HOUSE"],
        "narration": ("Four men on a stranger's roof, tearing through the clay, "
                      "coughing in the dust, grinning at each other like men doing "
                      "something magnificent and slightly insane."),
        "must_show": "ACTION-LOGIC: hands actually tearing clay UP and OUT of a widening hole and flinging it aside on the roof; reeds and beams exposed; all four grinning through the dust.",
        "must_not_show": "no tools needed — hands and a broken potsherd; the debris goes onto the roof beside the hole, never down into the room.",
        "scene": (
            "On the flat clay roof, all four friends are on their knees around a "
            "widening ragged hole, tearing the packed clay UP and OUT with their bare "
            "hands and flinging the broken lumps aside onto the roof beside them. "
            "Bundled reeds and a rough wooden beam are exposed at the hole's edge, and "
            "torn reed ends stick up everywhere. Pale dust hangs thick around them and "
            "all four are filthy with it, coughing, and grinning at each other like "
            "men who know exactly how mad this is. Hard sun overhead. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------------- n3 — the lowering ----
    {
        "id": "v2-r013-b12", "out": "s12-the-ceiling-cracked-open.jpeg", "seg": "n3 p1",
        "window": "68.94-73.12", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "HOUSE"],
        "narration": ("Below them, in the middle of the sermon, the ceiling cracked "
                      "open."),
        "must_show": "FROM INSIDE the dim room looking up: the first crack and a fall of dirt from the ceiling, faces turning up, Jesus stopped mid-sentence.",
        "must_not_show": "no halo, glare or rim-light; the hole is not open yet — this is the first breach.",
        "scene": (
            "Inside the dim crowded room, looking up past the packed heads. A crack "
            "has opened in the clay ceiling between the wooden beams and a first fall "
            "of dirt and dust is coming down through it in a thin stream. All over the "
            "room faces are tipping up toward it, mouths opening. Jesus has stopped "
            "speaking and is looking up too, one hand still raised where it was. The "
            "room is dark and close and lit only by two small windows. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b13", "out": "s13-daylight-poured-in.jpeg", "seg": "n3 p2",
        "window": "73.12-77.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "HOUSE"],
        "narration": ("Daylight poured into the dark room through falling dust and "
                      "straw."),
        "must_show": "⚠️ THE BUILD'S BEST IMAGE: a hard shaft of daylight dropping through the torn hole into the dark room, thick with falling dust and straw.",
        "must_not_show": "nothing supernatural about the light — it is ordinary sunshine through a hole in a roof; do not put Jesus in this frame.",
        "scene": (
            "Inside the dark room, a ragged hole has been torn open in the ceiling and "
            "a hard column of ordinary daylight is dropping straight down through it "
            "onto the beaten earth floor. The shaft is thick and solid with drifting "
            "dust, falling crumbs of dry clay and loose straw turning slowly as they "
            "come down. Around it the crowded room is dim, and the upturned faces at "
            "the edges of the light are half lit and staring. The camera is back far "
            "enough to hold the hole, the shaft and the room. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b14", "out": "s14-four-faces-at-the-hole.jpeg", "seg": "n3 p3a",
        "window": "77.31-81.5", "wide": True, "jesus": False, "ref": False,
        "locks": ["FRIENDS", "HOUSE"],
        "narration": "And down through that column of light,",
        "must_show": "looking UP from inside at the four filthy faces ringing the torn hole against the bright sky, paying out four ropes.",
        "must_not_show": "an upright vertical photograph — the hole and sky at the top, the room below, horizon level; the picture is the right way up.",
        "scene": (
            "An upright vertical photograph looking up from inside the dim room "
            "through the torn hole to the bright sky beyond, the room at the bottom of "
            "the frame and the sky at the top. Four filthy dust-caked faces ring the "
            "ragged edge of the hole, silhouetted and squinting down, each man leaning "
            "in with a rope running taut through his hands as he pays it out. Torn "
            "reed ends and broken clay fringe the opening. Hard daylight floods around "
            "their heads. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b15", "out": "s15-swaying-on-four-ropes.jpeg", "seg": "n3 p3b",
        "window": "81.5-84.2", "wide": True, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "FRIENDS", "MAT", "CROWD", "HOUSE"],
        "narration": "swaying on four ropes, lowered with enormous care,",
        "must_show": "the mat halfway down inside the shaft of light, hanging level on four corner ropes, turning slowly, the crowd pressed back beneath it.",
        "must_not_show": "the mat must hang LEVEL and controlled — never tipping or dropping; the care is the point.",
        "scene": (
            "The woven reed mat hangs halfway down inside the column of daylight, held "
            "level and steady on the four ropes knotted to its corners, turning very "
            "slowly as it descends. The young man lies on it looking upward, one hand "
            "gripping the reed edge, held with obvious care. Below and around, the "
            "packed crowd has pressed back hard against the walls to clear the floor, "
            "every face turned up. Dust drifts through the light. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b16", "out": "s16-at-the-feet-of-jesus.jpeg", "seg": "n3 p3c",
        "window": "84.2-86.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PARALYTIC", "MAT", "CROWD", "HOUSE"],
        "narration": "came a man on a mat — landing right at the feet of Jesus.",
        "must_show": "the mat settling onto the earth floor in the shaft of light directly in front of Jesus, ropes going slack, the two of them face to face.",
        "must_not_show": "no halo, glare or rim-light on Jesus — the only light effect in the room is the sunshine through the hole.",
        "scene": (
            "The mat has come to rest on the beaten earth floor inside the column of "
            "daylight, and the four ropes have gone slack and are lying loose across "
            "it. The young man lies in the light looking up. Directly in front of him, "
            "close enough to touch, Jesus stands looking down at him — the mat has "
            "landed at his feet. The dim crowd rings the lit circle on every side, "
            "silent. Dust turns in the shaft. The camera is back far enough to hold "
            "both men and the ring of the room. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    # -------------------------------------------------- n4 — THEIR faith ----
    {
        "id": "v2-r013-b17", "out": "s17-easy-to-miss.jpeg", "seg": "n4 p1-p2",
        "window": "87.20-93.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": ("Now listen to what the story says next, because it is easy to "
                      "miss. When Jesus saw their faith — theirs."),
        "must_show": "Jesus looking UP through the hole at the four faces — not down at the man; that is the whole beat.",
        "must_not_show": "no halo, glare or rim-light; his eyes must be plainly directed UP and away from the mat.",
        "scene": (
            "Close on Jesus standing in the shaft of daylight, his face tipped UP and "
            "his eyes lifted toward the torn hole in the ceiling above him. Hard "
            "daylight falls full on his upturned face through the drifting dust, and "
            "his expression is warm and moved and slightly amused — he is looking at "
            "the men who made the hole, not at the man on the floor. Falling straw "
            "turns in the light around him."
        ),
    },
    {
        "id": "v2-r013-b18", "out": "s18-the-four-sweat-streaked-faces.jpeg", "seg": "n4 p3-p4",
        "window": "93.98-98.73", "wide": True, "jesus": False, "ref": False,
        "locks": ["FRIENDS", "HOUSE"],
        "narration": "The friends'. The four sweat-streaked faces ringing the hole in the roof.",
        "must_show": "close on the four dust-caked faces around the hole, looking down, sweat cutting clean lines through the filth.",
        "must_not_show": "do not put Jesus in this frame; this beat belongs entirely to the four.",
        "scene": (
            "Close on the four friends' faces crowded around the ragged edge of the "
            "hole, looking down into the room. All four are caked pale with clay dust "
            "and sweat has run clean dark lines down through it on every face. Their "
            "eyes are wide and fixed on something below, their mouths open, hands "
            "gripping the broken clay edge and the slack ropes. Bright sky behind "
            "their heads. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b19", "out": "s19-he-hadnt-said-a-word.jpeg", "seg": "n4 p5-p7",
        "window": "98.73-107.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT"],
        "narration": ("The man on the mat hadn't said a word. His friends' faith counted "
                      "for him. He was carried there — and heaven honored the carrying."),
        "must_show": "close on the man on the mat in the light — silent, mouth closed, eyes moving between the faces above and the man in front of him.",
        "must_not_show": "he must NOT be speaking or reaching; his stillness and silence are the beat; do not put Jesus in this frame.",
        "scene": (
            "Close on the young man lying on the reed mat in the shaft of daylight, "
            "seen from just above. His mouth is closed and he has said nothing. His "
            "dark eyes are moving — up toward the four faces at the hole, then across "
            "toward someone standing out of frame, then back. Dust and straw settle "
            "onto his tunic and his hair. His hands rest still on his chest. Hard "
            "daylight full on him. He has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n5 / j1 — the first word ----
    {
        "id": "v2-r013-b20", "out": "s20-braced-for-words-about-his-legs.jpeg", "seg": "n5",
        "window": "107.74-116.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PARALYTIC", "MAT", "HOUSE"],
        "narration": ("And Jesus looked at the man lying in the dusty light — a man "
                      "braced for words about his legs — and the first thing he said "
                      "was not about his legs at all."),
        "must_show": "Jesus crouched down to the mat, and the man visibly braced — jaw tight, eyes flicking toward his own legs, waiting for the subject he has heard his whole life.",
        "must_not_show": "no halo, glare or rim-light; nobody is touching his legs and no attention is on them.",
        "scene": (
            "Jesus has crouched down beside the mat in the column of daylight, forearms "
            "on his knees, bringing his face level with the young man's. The young man "
            "is braced — his jaw tight, his shoulders drawn up, his eyes flicking once "
            "down toward his own still legs and then back up, waiting for the thing "
            "everyone always says. Jesus is not looking at his legs at all; he is "
            "looking at his face. The dim crowd rings them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b21", "out": "s21-son-thy-sins-be-forgiven.jpeg", "seg": "j1",
        "window": "116.89-118.59", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "Son, thy sins be forgiven thee. (Mark 2:5)",
        "must_show": "close on Jesus saying it — warm, fatherly, entirely tender; the word 'son' visible in the face.",
        "must_not_show": "no halo, glare or rim-light; nothing formal or pronouncing about it — this is said gently and close.",
        "scene": (
            "Very close on Jesus's face crouched low in the shaft of daylight, "
            "speaking. His expression is warm and fatherly and completely tender — "
            "eyes soft and steady, brows lifted slightly in the middle, the beginning "
            "of a gentle smile — the face of a man calling somebody his own child. "
            "Dust turns in the hard light across his cheek. Nothing about it is formal."
        ),
    },
    # ------------------------------------------------ n6 — the deepest wound ----
    {
        "id": "v2-r013-b22", "out": "s22-the-first-word-was-son.jpeg", "seg": "n6 p1-p4",
        "window": "120.23-126.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARALYTIC"],
        "narration": ("The first word was son. Not a diagnosis. Not a lecture about his "
                      "legs. Son — and then forgiveness."),
        "must_show": "the word landing on his face — the braced expression collapsing into confusion and then something breaking open.",
        "must_not_show": "do not put Jesus in this frame.",
        "scene": (
            "Very close on the young man's face on the mat. The braced tightness has "
            "gone out of it all at once — his brows have drawn up in the middle, his "
            "mouth has fallen slightly open, and his eyes have gone wide and wet and "
            "searching, as though he is checking whether he heard it right. Something "
            "is breaking open behind his face. Hard daylight and drifting dust across "
            "him."
        ),
    },
    {
        "id": "v2-r013-b23", "out": "s23-the-shame-he-carried.jpeg", "seg": "n6 p5",
        "window": "126.92-137.48", "wide": True, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT", "CROWD", "HOUSE"],
        "narration": ("In that world, everyone assumed a body like his was the proof of "
                      "some hidden guilt — he had carried the shame along with the "
                      "paralysis his whole life."),
        "must_show": "the assumption made visible in the room — faces in the dim crowd looking at him with pity mixed with judgement, a few glancing away.",
        "must_not_show": "nobody says anything; it is all in how they look at him; do not put Jesus in this frame.",
        "scene": (
            "The young man lies on his mat in the lit circle, and around him in the dim "
            "packed room the faces are looking down at him with something complicated "
            "— pity mixed with appraisal, one older man's mouth turned down, two women "
            "with their heads inclined together, a man glancing away as if not to "
            "stare. Nobody is speaking. He is the only thing lit and they are all in "
            "shadow. The camera is back far enough to hold him and the ring of faces. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b24", "out": "s24-the-deepest-wound-first.jpeg", "seg": "n6 p6",
        "window": "137.48-140.16", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PARALYTIC"],
        "narration": "Jesus went to the deepest wound first.",
        "must_show": "the two faces close together in the light — Jesus steady and certain, the man's face coming apart.",
        "must_not_show": "no halo, glare or rim-light.",
        "scene": (
            "Close on the two faces near together in the shaft of daylight, Jesus "
            "crouched and the young man lying. Jesus's expression is steady, warm and "
            "certain, holding the man's eyes. The young man's face is coming apart — "
            "his chin trembling, tears running back into his hair, his eyes locked on "
            "Jesus's and unable to look away. Dust turning in the light between them. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b25", "out": "s25-already-the-miracle.jpeg", "seg": "n6 p7-p8",
        "window": "140.16-144.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT"],
        "narration": "His legs had not moved yet. And it was already the miracle.",
        "must_show": "the still legs on the mat in the foreground and his weeping, transformed face beyond them — nothing has changed in his body and everything has changed in him.",
        "must_not_show": "the legs must be plainly unchanged and still; do not put Jesus in this frame.",
        "scene": (
            "The camera is low along the mat, so the young man's thin unmoving legs "
            "under the grey-brown tunic fill the near foreground, absolutely still on "
            "the reed matting — and beyond them, in focus, his face is turned up in the "
            "hard daylight, wet with tears and completely transfigured with relief. "
            "The two halves of the frame disagree. Dust settles on both. He has two "
            "legs and one head."
        ),
    },
    # ------------------------------------------------ n7 / s7 — the scribes ----
    {
        "id": "v2-r013-b26", "out": "s26-in-the-corner-sat-the-scribes.jpeg", "seg": "n7 p1",
        "window": "144.77-151.47", "wide": True, "jesus": False, "ref": False,
        "locks": ["SCRIBES", "HOUSE"],
        "narration": ("But in the corner sat the scribes — the religious experts — and "
                      "nothing about this made them glad."),
        "must_show": "the scribes seated together in the dim corner, apart from the crowd, faces closed and unmoved while the room around them reacts.",
        "must_not_show": "do not put Jesus in this frame; they are not speaking or gesturing — stillness and dark clothing set them apart.",
        "scene": (
            "In a dim corner of the crowded room, three or four scribes sit together on "
            "a low bench slightly apart from everyone else, their near-black indigo "
            "robes and dark shawls making them the darkest mass in the room. Their "
            "faces are closed and entirely unmoved — mouths shut, eyes fixed forward, "
            "hands folded — while around them the ordinary people are craning and "
            "reacting. Only the edge of the daylight shaft reaches them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b27", "out": "s27-reasoned-in-their-hearts.jpeg", "seg": "n7 p2-p5",
        "window": "151.47-162.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["SCRIBES"],
        "narration": ("They didn't say a word out loud. They reasoned it in their "
                      "hearts: this is blasphemy. And on the logic, they were exactly "
                      "right. That was the point they refused to see."),
        "must_show": "SCRIPTURE-EXACT (v6): CLOSED MOUTHS and moving eyes — the thinking is entirely internal, one glancing at another without a word.",
        "must_not_show": "NOT ONE of them may be speaking, whispering or gesturing — v6 says they reasoned in their hearts, and an outburst breaks the verse.",
        "scene": (
            "Close on two of the scribes seated in the dim corner. Both mouths are "
            "firmly CLOSED and neither is speaking — but one's eyes have cut sideways "
            "to the other, and the other's brows have drawn down hard and his jaw has "
            "tightened, and something has plainly passed between them without a sound. "
            "A third behind them stares straight ahead with his lips pressed thin. "
            "Their hands are still. Dim light, deep shadow on their dark robes."
        ),
    },
    {
        "id": "v2-r013-b28", "out": "s28-why-doth-this-man-speak.jpeg", "seg": "s7 p1",
        "window": "163.28-165.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["SCRIBES"],
        "narration": "Why doth this man thus speak blasphemies? (Mark 2:7)",
        "must_show": "very close on one scribe's face — the outrage entirely behind the eyes, mouth still shut.",
        "must_not_show": "mouth stays CLOSED; do not put Jesus in this frame.",
        "scene": (
            "Very close on one scribe's face in the dim corner, filling the frame. His "
            "mouth is shut in a hard line and stays shut, but his eyes have gone "
            "narrow and hot and fixed, and a muscle is working in his jaw beneath the "
            "combed grey beard. Everything is happening behind the face. Deep shadow, "
            "a single edge of daylight on his cheekbone."
        ),
    },
    {
        "id": "v2-r013-b29", "out": "s29-who-can-forgive-sins-but-god.jpeg", "seg": "s7 p2",
        "window": "165.84-167.96", "wide": True, "jesus": False, "ref": False,
        "locks": ["SCRIBES", "HOUSE"],
        "narration": "who can forgive sins but God only? (Mark 2:7)",
        "must_show": "the group of them together, all silent, all thinking the same thing — a wall of closed dark faces in the corner.",
        "must_not_show": "still nobody speaking; do not put Jesus in this frame.",
        "scene": (
            "The three or four scribes seated together in the dim corner, framed as one "
            "dark closed block. Every mouth is shut, every face is set, and all their "
            "eyes are aimed at the same point out of frame. Their near-black robes "
            "merge into the shadow around them so they read as a single mass. Behind "
            "them the sunlit dust of the room is faintly bright. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    # --------------------------------------------- n8 / j2 — he answered them ----
    {
        "id": "v2-r013-b30", "out": "s30-stranger-than-the-ceiling.jpeg", "seg": "n8 p1-p2",
        "window": "169.48-176.00", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SCRIBES", "HOUSE"],
        "narration": ("And then came the strangest moment in that room — stranger than "
                      "the ceiling. Jesus knew what they were thinking."),
        "must_show": "Jesus turning his head and looking straight at the scribes in the dim corner — across a room, at men who have said nothing.",
        "must_not_show": "no halo, glare or rim-light; nobody has pointed them out to him.",
        "scene": (
            "Jesus has risen from the mat and turned his head, and he is looking "
            "directly across the crowded dim room at the scribes in their corner. His "
            "gaze is level and unmistakably aimed at them. Between him and them the "
            "packed crowd stands unaware, still looking at the man on the floor. The "
            "shaft of daylight is behind him and the corner ahead is in shadow. The "
            "camera is back far enough to hold Jesus and the seated scribes in one "
            "frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b31", "out": "s31-they-had-said-nothing.jpeg", "seg": "n8 p3",
        "window": "176.00-178.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["SCRIBES"],
        "narration": "They had said nothing, and he answered them anyway:",
        "must_show": "the scribes' faces reacting to being seen — a flicker of alarm, one sitting back, mouths still shut.",
        "must_not_show": "still no speech from them; do not put Jesus in this frame.",
        "scene": (
            "Close on the scribes in the corner as they realise they are being looked "
            "at. The nearest one's eyes have widened a fraction and he has drawn back "
            "slightly on the bench; another's folded hands have come apart; the third's "
            "head has turned sharply toward the others. Not one mouth has opened. The "
            "composure has cracked without a word being spoken. Dim light, dark robes."
        ),
    },
    {
        "id": "v2-r013-b32", "out": "s32-whether-is-it-easier.jpeg", "seg": "j2 a",
        "window": "179.56-183.6", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SCRIBES", "HOUSE"],
        "narration": ("Whether is it easier to say to the sick of the palsy, Thy sins "
                      "be forgiven thee; (Mark 2:9)"),
        "must_show": "Jesus speaking directly to the scribes across the room, the crowd turning to follow his look and realising who he is talking to.",
        "must_not_show": "no halo, glare or rim-light; no anger — the question is put plainly.",
        "scene": (
            "Jesus stands in the middle of the room speaking across it to the seated "
            "scribes, one hand open and lifted in a plain questioning gesture. All "
            "around him the crowd is turning to follow his look, heads swivelling "
            "toward the dim corner as people work out who he is addressing. The scribes "
            "sit still under it. The daylight shaft falls between them. The camera is "
            "back far enough to hold Jesus, the turning crowd and the scribes. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b33", "out": "s33-or-to-say-arise-and-walk.jpeg", "seg": "j2 b",
        "window": "183.6-187.69", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PARALYTIC", "MAT", "HOUSE"],
        "narration": ("or to say, Arise, and take up thy bed, and walk? (Mark 2:9)"),
        "must_show": "Jesus's hand turning back to indicate the man on the mat as he names the second option — the whole room's eyes following the gesture down to the still legs.",
        "must_not_show": "no halo, glare or rim-light; nothing has happened to the man yet.",
        "scene": (
            "Jesus has turned his open hand back and down to indicate the young man "
            "lying on the reed mat in the shaft of daylight, still exactly as he was, "
            "his legs unmoving. Around the room every head is following the gesture "
            "and looking down at the mat, and the crowd has gone completely silent. "
            "The young man looks back up at Jesus. Dust hangs in the light. The camera "
            "holds Jesus, the mat and the near crowd. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # -------------------------------------------------------- n9 — the point ----
    {
        "id": "v2-r013-b34", "out": "s34-which-is-easier-to-say.jpeg", "seg": "n9 p1-p2",
        "window": "189.07-196.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["SCRIBES"],
        "narration": ("He was asking them: which is easier to say? Anyone can announce "
                      "that sins are forgiven — no one can check."),
        "must_show": "the scribes caught by the logic — one's eyes moving as he follows it, the beginning of understanding they do not want.",
        "must_not_show": "do not put Jesus in this frame; still no speech from them.",
        "scene": (
            "Close on the scribes' faces in the corner as the question works on them. "
            "The nearest one's eyes have started moving, tracking the argument to its "
            "end, and his mouth has come very slightly open before closing again; "
            "another has gone perfectly still with his brows lowered; the third's chin "
            "has come up defensively. They can all see where it goes and none of them "
            "wants to arrive. Dim light on dark wool."
        ),
    },
    {
        "id": "v2-r013-b35", "out": "s35-everyone-finds-out.jpeg", "seg": "n9 p3",
        "window": "196.10-203.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "PARALYTIC", "MAT", "HOUSE"],
        "narration": ("But tell a paralyzed man to stand, and everyone in the room finds "
                      "out in a second what your words are worth."),
        "must_show": "the whole room holding its breath — every face in the dim crowd fixed on the man on the mat, waiting.",
        "must_not_show": "do not put Jesus in this frame; nothing has happened yet — this is the held breath before it.",
        "scene": (
            "A wide view of the packed dim room with every single face turned toward "
            "the lit mat on the floor and nobody moving at all. Mouths are open, eyes "
            "are wide, one woman has a hand pressed to her chest, a man near the front "
            "has stopped mid-step. The young man lies in the shaft of daylight in the "
            "middle of all that attention with his legs still unmoved. The whole room "
            "is holding its breath. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b36", "out": "s36-so-that-you-will-know.jpeg", "seg": "n9 p4-p5",
        "window": "203.33-210.76", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PARALYTIC"],
        "narration": ("So — he said — so that you will know the forgiveness was real, "
                      "watch this. He turned back to the man on the mat:"),
        "must_show": "Jesus turning back down to the young man, and the young man's face lifting to meet him — the room forgotten between them.",
        "must_not_show": "no halo, glare or rim-light; no showmanship in his face.",
        "scene": (
            "Close on the two of them as Jesus turns back and comes down toward the "
            "mat again, his face losing the room and settling entirely on the young "
            "man. There is nothing performative in his expression — it is warm and "
            "matter of fact. Below him the young man's face has lifted, his eyes wide "
            "and locked on Jesus's, his breath caught. Hard daylight and dust around "
            "them. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b37", "out": "s37-arise-take-up-thy-bed.jpeg", "seg": "j3",
        "window": "211.33-215.27", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("I say unto thee, Arise, and take up thy bed, and go thy way into "
                      "thine house. (Mark 2:11)"),
        "must_show": "close on Jesus speaking it — quiet, certain, ordinary; a hand held out low toward the man rather than raised in command.",
        "must_not_show": "no halo, glare or rim-light; nothing thunderous — it is said the way you would tell someone their meal is ready.",
        "scene": (
            "Close on Jesus's face and one low outstretched hand in the shaft of "
            "daylight, speaking. His expression is quiet and entirely certain and "
            "completely ordinary — no strain, no drama, no raised voice in it at all. "
            "His hand is open and turned up, held low toward the man on the floor, "
            "more invitation than command. Dust turns in the hard light. His hand has "
            "five fingers."
        ),
    },
    # -------------------------------------------------------- n10 — he stood ----
    {
        "id": "v2-r013-b38", "out": "s38-and-immediately-he-did.jpeg", "seg": "n10 p1",
        "window": "216.57-218.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT"],
        "narration": "And immediately, he did.",
        "must_show": "⚠️ THE TURN: the legs MOVING for the first time — one knee drawing up, a foot pressing flat against the reed mat, muscles engaging.",
        "must_not_show": "he is not upright yet; this is the first movement, and it must be plainly his previously motionless legs responding; do not put Jesus in this frame.",
        "scene": (
            "Close and low on the young man's legs on the mat. One knee has DRAWN UP "
            "and a bare foot has come flat and pressed down hard against the woven "
            "reed, the tendons standing out along the top of the foot and the calf "
            "gone tight with effort — legs that have not moved in years taking weight. "
            "His hand has come down to push off the mat beside him. Hard daylight and "
            "settling dust. He has two legs and two feet with five toes each."
        ),
    },
    {
        "id": "v2-r013-b39", "out": "s39-legs-like-a-newborn-colt.jpeg", "seg": "n10 p2",
        "window": "218.08-225.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PARALYTIC", "MAT", "CROWD", "HOUSE"],
        "narration": ("He stood — on legs trembling like a newborn colt's — while the "
                      "crowd pulled back and the dust floated in the light."),
        "must_show": "him STANDING, upright but unsteady, knees visibly trembling, arms out for balance, in the column of daylight; the crowd recoiling backwards.",
        "must_not_show": "no halo, glare or rim-light; he must NOT be steady or confident — the shakiness is what makes it real.",
        "scene": (
            "The young man is ON HIS FEET in the shaft of daylight, upright but "
            "swaying — his knees visibly trembling, both arms flung out wide for "
            "balance, his weight rocking, his face astonished and wet. All around him "
            "the packed crowd has recoiled backwards, pressing away from him against "
            "the walls with hands up and mouths open. Jesus stands close beside him, "
            "watching, not holding him. Dust floats through the light. The camera is "
            "back far enough to see him head to feet. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # ---------------------------------------------------- n10b — the mat ----
    {
        "id": "v2-r013-b40", "out": "s40-he-rolled-up-his-mat.jpeg", "seg": "n10b p1",
        "window": "225.88-229.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT"],
        "narration": ("Then he bent down, rolled up his mat, and tucked it under his arm."),
        "must_show": "him BENT DOWN on his own legs, hands rolling the reed mat up — a movement his body could not have made a minute ago.",
        "must_not_show": "nobody helps him; do not put Jesus in this frame.",
        "scene": (
            "The young man has bent right down on his own legs, knees flexed and "
            "back curved, and is rolling the woven reed mat up from one end with both "
            "hands, the four corner ropes trailing loose. His face is intent on the "
            "simple task and there is dust in his hair. Nobody's hands are helping "
            "him. Hard daylight falls across the mat and his bent shoulders. Each hand "
            "has five fingers."
        ),
    },
    {
        "id": "v2-r013-b41", "out": "s41-the-bed-that-carried-him.jpeg", "seg": "n10b p2",
        "window": "229.44-231.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT"],
        "narration": "The bed that had carried him, he carried home.",
        "must_show": "the rolled mat tucked firmly under his own arm, and his face above it — the reversal complete.",
        "must_not_show": "do not put Jesus in this frame; the object and who is carrying whom is the entire beat.",
        "scene": (
            "Close on the young man standing with the rolled reed mat tucked firmly "
            "under one arm and clamped against his ribs, the loose corner ropes hanging "
            "down. His other hand rests on top of the roll. His face above it is "
            "streaked with dust and tears and lit up with disbelieving joy. Hard "
            "daylight across him. Each hand has five fingers."
        ),
    },
    # ---------------------------------------------------- n11 — out the door ----
    {
        "id": "v2-r013-b42", "out": "s42-they-made-room-now.jpeg", "seg": "n11 p1-p2",
        "window": "232.49-240.13", "wide": True, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "MAT", "CROWD", "HOUSE"],
        "narration": ("He walked out the door in front of everyone — through the same "
                      "crowd that had no room for him an hour before. They made room now."),
        "must_show": "THE INVERSE OF b05: the doorway that was a solid wall of backs is now an open lane, and he walks out through it on his own legs with the mat under his arm.",
        "must_not_show": "do not put Jesus in this frame; the composition must plainly answer the blocked-doorway frame.",
        "scene": (
            "The crowd has split apart and opened a clear lane straight through the "
            "packed room and out through the low stone doorway into the bright street "
            "beyond. The young man walks down the middle of it on his own legs, the "
            "rolled mat under his arm, still a little unsteady, his head up. On both "
            "sides the people press themselves back against the walls to give him room, "
            "faces astonished, some reaching out to touch his shoulder as he passes. "
            "Daylight floods in through the open doorway ahead of him. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b43", "out": "s43-they-were-all-amazed.jpeg", "seg": "n11 p3",
        "window": "240.13-247.36", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CROWD", "HOUSE"],
        "narration": ("Mark says they were all amazed, and gave the glory to God, and "
                      "said to each other: we have never seen anything like this."),
        "must_show": "the room erupting — hands lifted, faces lit up, people gripping each other and talking at once, Jesus among them.",
        "must_not_show": "no halo, glare or rim-light; he is in the crowd, not apart from it.",
        "scene": (
            "The room has erupted. People are on their feet with hands lifted and "
            "faces blazing, gripping each other's arms, all talking at once, one man "
            "with both palms up and his head back, a woman laughing with tears down "
            "her face. Jesus stands in among them, not apart, watching the doorway "
            "where the man went out. The torn hole in the ceiling still pours daylight "
            "and dust down into the middle of it all. The camera is back far enough to "
            "hold the room. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b44", "out": "s44-four-friends-on-the-roofline.jpeg", "seg": "n11 p4",
        "window": "247.36-253.98", "wide": True, "jesus": False, "ref": False,
        "locks": ["FRIENDS", "HOUSE"],
        "narration": ("And up on the roofline, four filthy, grinning friends pounded "
                      "each other's shoulders and laughed toward heaven."),
        "must_show": "the four on the roof against the open sky — filthy, pounding each other's shoulders, heads back laughing, arms up.",
        "must_not_show": "do not put Jesus in this frame; this is the friends' payoff and belongs entirely to them.",
        "scene": (
            "Up on the flat clay roof against the wide bright sky, the four friends "
            "have gone completely to pieces with joy — the big black-bearded one has "
            "both arms around the young one's neck, the stocky shaven-headed one is "
            "pounding the wiry grey-haired one's shoulder with his fist, two of them "
            "have their heads thrown back laughing straight up at the sky, and all "
            "four are caked head to foot in pale clay dust. The ragged hole they made "
            "gapes beside them with the torn reeds sticking up. Hard morning sun. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r013-b45", "out": "s45-we-never-saw-it-on-this-fashion.jpeg", "seg": "s12",
        "window": "254.54-256.40", "wide": True, "jesus": False, "ref": False,
        "locks": ["PARALYTIC", "FRIENDS", "MAT", "CROWD", "HOUSE"],
        "narration": "We never saw it on this fashion. (Mark 2:12)",
        "must_show": "the closing frame from the street: the young man walking away up the sunlit lane with his mat under his arm, the crowd pouring out of the door behind him.",
        "must_not_show": "do not put Jesus in this frame; the last image belongs to the man walking home.",
        "scene": (
            "Out in the bright street, the young man walks away up the sunlit basalt "
            "lane with the rolled reed mat under his arm, seen from behind and to one "
            "side, his stride still slightly uneven but his back straight and his head "
            "up. Behind him the crowd is pouring out of the low doorway of the house "
            "into the street, pointing after him and calling to one another, and high "
            "above them the four filthy friends are visible on the roofline. Hard "
            "bright morning sun on the black stone. Every figure has two arms, two "
            "hands and one head."
        ),
    },
]

# The first V2 draft inherited windows from an older, shortened render.  The
# current story source contains all 23 existing narration/scripture clips, so
# every visual beat is locked here to that complete 298.817-second timeline.
# This table is intentionally explicit: it is also a reviewable guard against
# images drifting ahead of the words (especially the healing, mat, and exit).
CURRENT_AUDIO_TIMING = {
    "s01-capernaum.jpeg": ("n0", 0.280, 7.078),
    "s02-one-at-each-corner.jpeg": ("n0b", 7.078, 16.855),
    "s03-he-could-not-walk.jpeg": ("n0b", 16.855, 20.390),
    "s04-they-decided-anyway.jpeg": ("n0b", 20.390, 24.544),
    "s05-a-wall-of-backs.jpeg": ("n1", 24.544, 27.266),
    "s06-no-one-giving-up-a-spot.jpeg": ("n1", 27.266, 36.898),
    "s07-breathing-hard.jpeg": ("n1", 36.898, 44.022),
    "s08-one-of-them-looked-up.jpeg": ("n1", 44.022, 47.561),
    "s09-clay-over-reeds.jpeg": ("n2", 47.561, 57.304),
    "s10-dig-it-with-your-hands.jpeg": ("n2b", 57.304, 65.069),
    "s11-tearing-through-the-clay.jpeg": ("n2b", 65.069, 76.491),
    "s12-the-ceiling-cracked-open.jpeg": ("n3", 76.491, 80.982),
    "s13-daylight-poured-in.jpeg": ("n3", 80.982, 85.483),
    "s14-four-faces-at-the-hole.jpeg": ("n3", 85.483, 89.985),
    "s15-swaying-on-four-ropes.jpeg": ("n3", 89.985, 92.886),
    "s16-at-the-feet-of-jesus.jpeg": ("n3", 92.886, 96.109),
    "s17-easy-to-miss.jpeg": ("n4", 96.109, 103.412),
    "s18-the-four-sweat-streaked-faces.jpeg": ("n4", 103.412, 108.528),
    "s19-he-hadnt-said-a-word.jpeg": ("n4", 108.528, 118.232),
    "s20-braced-for-words-about-his-legs.jpeg": ("n5", 118.232, 128.406),
    "s21-son-thy-sins-be-forgiven.jpeg": ("j1", 128.406, 132.066),
    "s22-the-first-word-was-son.jpeg": ("n6", 132.066, 141.382),
    "s23-the-shame-he-carried.jpeg": ("n6b", 141.382, 151.877),
    "s24-the-deepest-wound-first.jpeg": ("n6c", 151.877, 154.742),
    "s25-already-the-miracle.jpeg": ("n6c", 154.742, 159.670),
    "s26-in-the-corner-sat-the-scribes.jpeg": ("n7", 159.670, 166.220),
    "s27-reasoned-in-their-hearts.jpeg": ("n7", 166.220, 177.765),
    "s28-why-doth-this-man-speak.jpeg": ("s7", 177.765, 180.646),
    "s29-who-can-forgive-sins-but-god.jpeg": ("s7", 180.646, 184.743),
    "s30-stranger-than-the-ceiling.jpeg": ("n8", 184.743, 191.641),
    "s31-they-had-said-nothing.jpeg": ("n8", 191.641, 195.408),
    "s32-whether-is-it-easier.jpeg": ("j2", 195.408, 200.194),
    "s33-or-to-say-arise-and-walk.jpeg": ("j2", 200.194, 206.675),
    "s34-which-is-easier-to-say.jpeg": ("n9", 206.675, 214.029),
    "s35-everyone-finds-out.jpeg": ("n9", 214.029, 221.592),
    "s36-so-that-you-will-know.jpeg": ("n9", 221.592, 229.961),
    "s37-arise-take-up-thy-bed.jpeg": ("j3", 229.961, 237.196),
    "s38-and-immediately-he-did.jpeg": ("n10", 237.196, 238.811),
    "s39-legs-like-a-newborn-colt.jpeg": ("n10", 238.811, 247.153),
    "s40-he-rolled-up-his-mat.jpeg": ("n10b", 247.153, 251.252),
    "s41-the-bed-that-carried-him.jpeg": ("n10b", 251.252, 254.764),
    "s42-they-made-room-now.jpeg": ("n11", 254.764, 262.162),
    "s43-they-were-all-amazed.jpeg": ("n11", 262.162, 269.163),
    "s44-four-friends-on-the-roofline.jpeg": ("n11", 269.163, 276.116),
    "s45-we-never-saw-it-on-this-fashion.jpeg": ("s12", 276.116, 279.404),
}

if set(CURRENT_AUDIO_TIMING) != {beat["out"] for beat in BEATS}:
    raise RuntimeError("CURRENT_AUDIO_TIMING must cover every Story 13 image exactly")
for _beat in BEATS:
    _seg, _start, _end = CURRENT_AUDIO_TIMING[_beat["out"]]
    _beat["seg"] = _seg
    _beat["window"] = f"{_start:.3f}-{_end:.3f}"

# Preserve each earlier frame's useful camera/blocking as a rough draft while
# regenerating the final photograph. Friend shots receive four individual
# anchors; man shots receive his one isolated identity anchor.
_ROUGH = _BUILD / "assets"
for _beat in BEATS:
    _rough = _ROUGH / _beat["out"]
    if _rough.is_file():
        _beat["rough_ref"] = str(_rough)
    _locks = set(_beat.get("locks", []))
    _beat["char_refs"] = []
    if "FRIENDS" in _locks:
        _beat["char_refs"].extend(FRIEND_REFS)
    if "PARALYTIC" in _locks:
        _beat["char_refs"].append(PARALYTIC_REF)
