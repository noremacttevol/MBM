#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 26: The Grove.

Spring 1820. One verse, one prayer, the darkness that fought it, and two
glorified Personages. The famine of the word ends in ten seconds.
Anchors: James 1:5; JS-History 1:5-20, 25.

Reverence bar: highest in the series. The vision is depicted with the two
Personages plainly distinct — the Son in his locked cream, the Father in
radiant white — light without halo language, awe without spectacle. The
darkness that seizes Joseph is FORMLESS (Devil Law).
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, DEVIL = ("narrator", "jesus", "father",
                                             "scripture", "devil")

EP = 326
NUM = 26
SLUG = "the-grove"
TITLE = "The Grove"
META = "James 1 · JS—History 1"

SEGMENTS = [
    ("n1", NARRATOR,
     "Spring, eighteen twenty. Palmyra, New York. A fourteen-year-old farm "
     "boy is about to walk into the woods with one question — and end a "
     "seventeen-hundred-year famine."),
    ("n2", NARRATOR,
     "His town was at war over religion. Camp meetings, rival preachers, "
     "every church claiming to be right. Joseph Smith wanted his sins "
     "forgiven and wanted to know where to go. And nobody's answer settled "
     "anything."),
    ("s1", SCRIPTURE,
     "If any of you lack wisdom, let him ask of God, that giveth to all men "
     "liberally, and upbraideth not; and it shall be given him."),
    ("n3", NARRATOR,
     "One verse in the book of James went through him like fire. Ask God. "
     "Not a preacher. Not a council. Ask the God who gives to everyone, "
     "generously — and never scolds you for asking."),
    ("n4", NARRATOR,
     "So on the morning of a beautiful clear spring day, he walked into the "
     "grove of trees on his family's farm, found the place he had picked "
     "out, knelt down — and for the first time in his life, prayed out "
     "loud."),
    ("n5", NARRATOR,
     "And the darkness came for him first. Remember whose kingdom that "
     "prayer threatened. A power seized him. It bound his tongue so he "
     "could not speak, and thick darkness gathered around him, until he "
     "thought he was finished."),
    ("s2", SCRIPTURE,
     "I saw a pillar of light exactly over my head, above the brightness of "
     "the sun; which descended gradually until it fell upon me."),
    ("s3", SCRIPTURE,
     "When the light rested upon me I saw two Personages, whose brightness "
     "and glory defy all description, standing above me in the air."),
    ("g1", FATHER,
     "This is My Beloved Son. Hear Him!"),
    ("n6", NARRATOR,
     "The Father — a real, glorified Person — calling a boy by name and "
     "pointing to His Son. The Son — the living, risen Jesus Christ — "
     "standing beside Him in the air. Every question the famine had "
     "starved for centuries: answered in ten seconds."),
    ("n7", NARRATOR,
     "God is not a formless mystery. The heavens are not sealed shut. The "
     "Father and the Son are two distinct beings. And they know a farm boy "
     "by his first name — because the first word of the vision was "
     "Joseph."),
    ("n8", NARRATOR,
     "The boy asked his question, and got his answer: join none of them. "
     "The authority had left the earth centuries ago — and heaven was "
     "about to bring it back."),
    ("n9", NARRATOR,
     "He walked out of those trees into a world that would hate him for "
     "it. Preachers mocked. Neighbors turned. He was fourteen years old, "
     "and he never took one word of it back. Here is how he said it "
     "himself, years later:"),
    ("s4", SCRIPTURE,
     "I had actually seen a light, and in the midst of that light I saw "
     "two Personages, and they did in reality speak to me; and though I "
     "was hated and persecuted for saying that I had seen a vision, yet it "
     "was true. For I had seen a vision; I knew it, and I knew that God "
     "knew it, and I could not deny it."),
    ("n10", NARRATOR,
     "The famine of the word ended that spring morning — broken by a "
     "teenager who took one Bible verse completely at its word."),
    ("n11", NARRATOR,
     "And the invitation he used was never his alone. It is still in the "
     "book. If any of you lack wisdom — ask. He answered a farm boy. He "
     "answers you."),
]

CARD_SEG = ("card", NARRATOR,
            "God answered a fourteen-year-old in the woods. The heavens are "
            "open. Ask.")

CARD_TEXT = ("The heavens are open.\n"
             "Ask.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Six — The Grove")

SPOKEN = {"Palmyra": "pal MY ruh"}

JOSEPH = (
    "JOSEPH LOCK: the same boy as the attached reference in every picture — "
    "Joseph Smith at fourteen: a sturdy American farm boy, tall for his age, "
    "with thick sandy light-brown hair, a fair sun-tanned open face, strong "
    "brow, light-coloured thoughtful eyes, dressed in plain 1820 homespun — "
    "collarless linen shirt, wool trousers with suspenders, worn leather "
    "boots. Earnest, strong, unpolished. No halo, no glow.")

LOCKS = {"JOSEPH-SMITH": JOSEPH}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="america-1820")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "Dawn over an 1820 New York farm in spring: a log farmhouse with "
        "chimney smoke, split-rail fences, a plowed field edge — and far "
        "across the field a lone boy walking away from the camera toward a "
        "stand of tall hardwood trees, small in the wide frame. Mist lies "
        "in the low ground; the light is new.",
        "an 1820 log farmstead at dawn and one distant boy walking away "
        "toward a hardwood grove",
        "his face, any road or town, anyone else, anything post-1830",
        wide=True, locks=["JOSEPH-SMITH"])),
    ("p02", "n2", _p(
        "A torch-lit revival camp meeting at night: a preacher up on a "
        "stump mid-exhortation with arm flung high, a crowd of farm "
        "families pressing close in firelight, some hands raised, some "
        "heads shaking in argument at the edges — the camera stands behind "
        "the back rows and shoots past shoulders and bonnets toward the "
        "preacher, so no face near the lens is turned to it. Heat, torch "
        "flame, contention and hunger together.",
        "a night camp meeting from behind the crowd, stump preacher "
        "mid-gesture, torchlight, argument at the edges",
        "anyone facing the lens, banners with words, mockery of the "
        "worshippers",
        wide=True)),
    ("p03", ("n2", 0.55), _p(
        "Joseph at the meeting's edge: fourteen, in homespun, standing "
        "just outside the torchlight where the dark begins, arms folded "
        "tight, his face in warm-lit three-quarter turned toward the "
        "unseen preacher off the left frame edge — troubled, weighing, "
        "too honest to pretend certainty he does not feel.",
        "the boy in three-quarter at the crowd's torchlit edge, arms "
        "folded, troubled attention aimed off-frame left",
        "his eyes on the lens, tears, anyone else in focus near him",
        locks=["JOSEPH-SMITH"])),
    ("p04", "n3", _p(
        "By the hearth at night: Joseph on a low stool with the heavy "
        "family Bible open across his knees, firelight on his face, one "
        "finger resting under a line on the page, his head bent close — "
        "the page's print soft and unreadable in the warm light, his "
        "expression caught at the exact moment a sentence lands. The "
        "camera watches from beside the hearth in three-quarter.",
        "the boy bent over a big Bible on his knees by firelight, finger "
        "under a line, struck expression, print unreadable",
        "readable words on the page, his eyes on the lens, candles "
        "everywhere",
        locks=["JOSEPH-SMITH"])),
    ("p05", ("n3", 0.62), _p(
        "Close on Joseph's face lifting from the page: firelight on one "
        "side, the room's dark on the other, his light-coloured eyes "
        "aimed past the camera's right shoulder into the middle distance "
        "— the look of a decision arriving whole. The Bible's edge blurs "
        "at the frame's bottom.",
        "the boy's face close, just lifted from reading, decision in the "
        "eyes aimed past the lens",
        "his pupils centred on the lens, tears, halo, glow",
        locks=["JOSEPH-SMITH"])),
    ("p06", "n4", _p(
        "The clear spring morning: Joseph walks into the grove — tall "
        "maples and beeches in young leaf, morning light shafting long "
        "and low through trunks, the boy seen full-length from behind "
        "stepping over roots into the deepening green, the camera low on "
        "the path behind him. His axe is left leaning on a stump at the "
        "frame's edge: he came for something else today.",
        "the boy from behind entering deep spring woods in long morning "
        "light, an axe left behind on a stump",
        "his face, any path signage, anyone else, mist overdone",
        wide=True, locks=["JOSEPH-SMITH"])),
    ("p07", ("n4", 0.55), _p(
        "The place he picked: a small natural clearing walled in green. "
        "Joseph kneels down onto the leaf-mould, hands coming together, "
        "head beginning to bow — caught in the exact moment between "
        "kneeling and praying, seen from the side at a still, respectful "
        "distance. Dappled light moves on his shoulders.",
        "the boy mid-kneel in a green clearing, hands meeting, head "
        "starting to bow, side view",
        "his eyes on the lens, sunbeams as drawn rays, any figure",
        locks=["JOSEPH-SMITH"])),
    ("p08", "n5", _p(
        "The darkness seizes him: the clearing's light DIES from the "
        "edges inward — green going grey-black around a shrinking pool "
        "of dim morning — and inside it the kneeling boy is doubled "
        "over, one hand clawed into the leaf-mould, the other at his "
        "throat, mouth open in a cry that is not coming out. The "
        "darkness is EMPTY: pure failing light, no shape, no figure, "
        "nothing to see and everything to fear.",
        "light dying from the clearing's edges around the doubled-over "
        "boy, hand at his throat, formless empty darkness",
        "ANY figure, face, eyes, smoke-shape or claw in the dark; "
        "lightning; his eyes to the lens",
        devil=True, locks=["JOSEPH-SMITH"])),
    ("p09", ("n5", 0.6), _p(
        "Close at ground level: the boy's fist buried in dead leaves and "
        "black soil, knuckles white with strain, his bowed head and "
        "shaking shoulders soft-focus beyond, the last dim light failing "
        "across his back while the frame's edges stand in featureless "
        "dark. The fight is nearly lost.",
        "a white-knuckled fist in the leaf-mould, bowed shaking "
        "shoulders beyond, edges of the frame in empty dark",
        "any shape in the darkness, blood, his face clearly visible",
        devil=True, locks=["JOSEPH-SMITH"])),
    ("p10", "s2", _p(
        "Deliverance begins overhead: from low in the clearing looking "
        "straight up the tree trunks — high above the crowns, a column "
        "of light brighter than noon descends through the spring "
        "canopy, exactly over the clearing, its brilliance pushing the "
        "darkness off the edges of the frame as it comes. The trunks "
        "stand like pillars around it; the kneeling boy's shoulder "
        "edges the bottom of the frame.",
        "a descending column of daylight-brilliance through the canopy "
        "seen from below, darkness retreating at the edges",
        "any figure yet, drawn light rays with hard edges, halo rings, "
        "lens flare streaks",
        devil=True, locks=["JOSEPH-SMITH"])),
    ("p11", "s3", _p(
        "The vision: the spring clearing filled with light like standing "
        "inside morning itself — the young green leaves washed almost "
        "white by it — and above the kneeling boy, TWO glorified "
        "Personages stand IN THE AIR, their sandaled feet plainly "
        "several feet OFF the forest floor with open air beneath them: "
        "the Father in a radiant pure-white robe, and at his right hand "
        "the Son in his familiar cream — two distinct grown men, calm "
        "and majestic, looking down at the boy with warmth. SCREEN-SIDE "
        "LAW: because the Son stands at the Father's RIGHT hand and they "
        "face the camera, the Son in cream occupies the VIEWER'S LEFT "
        "half of the frame and the Father in white occupies the VIEWER'S "
        "RIGHT half — never the other way around. The clearing is deep "
        "woods on every side — no fence, rail or farm object anywhere. "
        "The brilliance fills the AIR of the whole clearing EVENLY — no "
        "outline, no aura, no edge of light around their bodies. In the "
        "near foreground the kneeling boy is FOURTEEN — tall, teenage, "
        "broad-shouldered for his age — seen from low behind his "
        "shoulder, his face not visible from this angle.",
        "two distinct glorified men standing plainly in the air with "
        "open space under their feet, above a kneeling TEENAGE boy "
        "seen from behind, spring leaves washed in even brilliance",
        "the boy child-sized or younger than fourteen, wings, halos, "
        "aura outlines around their bodies, drawn rays, identical "
        "faces, transparent bodies, either face toward the lens, "
        "autumn colours",
        jesus=True, ref=True, wide=True,
        locks=["FATHER", "JOSEPH-SMITH"])),
    ("p12", "g1", _p(
        "The presentation: closer on the two Personages in the air of "
        "the brilliant clearing, FRAMED FROM MID-THIGH UP so that NO "
        "ground, path, floor or forest floor appears anywhere in the "
        "frame — only the two figures against soft spring-green canopy "
        "and washed bright air, their robes hanging still — SCREEN-SIDE LAW: the Son in cream stands on "
        "the VIEWER'S LEFT and the Father in white on the VIEWER'S "
        "RIGHT (the Son at the Father's right hand), never reversed — "
        "the Father's right hand extended open toward the Son beside "
        "him on the viewer's left in the unmistakable gesture of "
        "introduction, His face angled DOWN toward the unseen boy "
        "below the frame's bottom edge; the Son's eyes already resting "
        "on the same low place with complete warmth. Two faces, two "
        "persons, one purpose. The light is even through the whole "
        "air; no outline or aura edges their bodies. Neither looks at "
        "the camera.",
        "both Personages in the air with open space below their hems, "
        "the Father's presenting hand toward the Son, both faces "
        "angled down toward the unseen boy",
        "feet on the ground, fences or farm objects, identical faces, "
        "halos, aura outlines, autumn colours, either gaze at the "
        "lens",
        jesus=True, ref=True, locks=["FATHER"])),
    ("p13", "n6", _p(
        "The boy in the light: Joseph's upturned face close, bathed in "
        "brilliance from above, tear-tracks bright on his cheeks, lips "
        "parted, the terror gone and pure awe in its place — his gaze "
        "climbing past the camera's upper left toward the Personages "
        "out of frame. The light on his face is soft and total, from "
        "the scene, not from him.",
        "the boy's tear-bright upturned face in total soft light, awe "
        "replacing fear, gaze up past the frame",
        "his eyes on the lens, glow off his skin, darkness remaining",
        locks=["JOSEPH-SMITH"])),
    ("p14", "n7", _p(
        "Two, plainly: the Personages framed together at mid-distance, "
        "standing IN THE AIR side by side with clear open space "
        "between them and open air visibly beneath their feet — "
        "SCREEN-SIDE LAW: the Son in cream on the VIEWER'S LEFT, the "
        "Father in white on the VIEWER'S RIGHT (the Son at the "
        "Father's right hand), never reversed — the Father's "
        "silver-white head and radiant white robe, the Son's dark "
        "hair and cream robe, each unmistakably his own person — "
        "both faces angled DOWNWARD toward the unseen boy below the "
        "frame's lower edge, majesty and kindness together, neither "
        "face aimed anywhere near the camera. The young SPRING-green "
        "leaves behind them are washed pale by the even brilliance of "
        "the air; no aura or outline edges their bodies.",
        "two distinct Personages side by side IN THE AIR with space "
        "between them and beneath them, both faces angled down toward "
        "the unseen boy, spring leaves washed pale",
        "feet on the ground, gazes toward the camera, faces merging "
        "or matching, halos, aura outlines, wings, autumn colours",
        jesus=True, ref=True, locks=["FATHER"])),
    ("p15", ("n7", 0.62), _p(
        "His name: extreme close on Joseph's face at the instant of "
        "being known — eyes wide, brows lifted, the small involuntary "
        "flinch of a boy who has just heard his own first name spoken "
        "from the air above him. Light floods one side of his face; "
        "his gaze is up and left, past the lens, never into it.",
        "extreme close of the boy's face at the instant of hearing his "
        "name, eyes wide, gaze up-left past the lens",
        "his pupils on the lens, tears streaming anew, any figure in "
        "frame",
        locks=["JOSEPH-SMITH"])),
    ("p16", "n8", _p(
        "The Son speaks with him: a close three-quarter of Jesus's face "
        "inclined gently downward toward the boy below the frame's "
        "bottom edge — gravity and gentleness together, the face of "
        "someone giving a fourteen-year-old the truth and a work that "
        "will cost him everything. The brilliant air softens everything "
        "behind him.",
        "Jesus's face close in three-quarter, inclined down toward the "
        "unseen boy, gentle gravity",
        "his eyes on the lens, halo, glow, a stern or grim set",
        jesus=True, ref=True)),
    ("p17", "n9", _p(
        "Out of the trees: Joseph walks out of the grove's edge into "
        "full open morning, seen in three-quarter from behind — his "
        "posture changed, shoulders square, one hand steadying himself "
        "on the last trunk as he steps into the field light toward the "
        "distant farmhouse. The woods behind him stand ordinary and "
        "green again; the camera stays in their shade and shoots past "
        "the trunks after him.",
        "the boy stepping from tree-shade into open field light in "
        "three-quarter from behind, squared shoulders, distant "
        "farmhouse",
        "his face fully shown, anyone waiting, light effects in the "
        "sky",
        wide=True, locks=["JOSEPH-SMITH"])),
    ("p18", ("n9", 0.45), _p(
        "The price begins: a Palmyra street of clapboard storefronts — "
        "Joseph walks steadily along the boardwalk while knots of "
        "townsmen turn to scoff: a merchant mid-laugh to his neighbor, "
        "a man shaking his head, two women turning away — every "
        "scorning face aimed at Joseph or each other, none at the "
        "camera, which shoots along the boardwalk past them from "
        "behind a porch post. "
        "Joseph's own face is calm, eyes level, mid-stride.",
        "the boy walking a boardwalk through visible scorn — laughing "
        "and head-shaking townsfolk aimed at him, his face calm and "
        "level",
        "anyone facing the lens, thrown objects, violence, signage "
        "with readable words",
        wide=True, locks=["JOSEPH-SMITH"])),
    ("p19", "s4", _p(
        "Years later, unshaken: Joseph as a young man now, seated at a "
        "plain table by candlelight with a quill in his stilled hand, "
        "his face lifted from the page in firm three-quarter — the "
        "same features grown into their strength, the same "
        "light-coloured eyes steady on the middle distance past the "
        "camera. The page below is soft and unreadable; the "
        "testimony is in the set of his face.",
        "the same face a few years older, quill stilled, firm steady "
        "three-quarter gaze past the lens, unreadable page",
        "his eyes on the lens, grey hair, halo, readable writing",
        locks=["JOSEPH-SMITH"])),
    ("p20", "n10", _p(
        "The grove after: the small clearing empty in full mid-morning "
        "light — leaf-mould pressed where a boy knelt, green leaves "
        "luminous, long soft light between the trunks, absolute peace. "
        "No people. The place itself remembers.",
        "the empty clearing in full gentle morning light, pressed "
        "leaf-mould where he knelt, no people",
        "any figure, light column remaining, mist, drawn rays",
        )),
    ("p21", "n11", _p(
        "The invitation now: in a present-day room at dawn, a person "
        "sits by a window with an open book in their lap — seen "
        "entirely from behind in silhouette-soft morning light, "
        "identity unknowable, the window's light falling across the "
        "open pages and the quiet room. It could be anyone. It could "
        "be the viewer.",
        "an unidentifiable person from behind at a dawn window with an "
        "open book, present day, quiet",
        "their face from any angle, readable text, phone screens "
        "readable, brand marks",
        era="modern")),
    ("p22", ("n11", 0.6), _p(
        "Final frame: from the grove floor looking straight up the "
        "great trunks into the sunlit spring crown — a natural "
        "cathedral of green and light climbing the full vertical "
        "frame, morning sky burning soft white-gold through the "
        "leaves at the top. No people. The heavens, open.",
        "straight-up view of tall trunks into a light-filled spring "
        "canopy, vertical and cathedral-like",
        "figures, birds in flocks, drawn rays, lens flare streaks",
        )),
]
