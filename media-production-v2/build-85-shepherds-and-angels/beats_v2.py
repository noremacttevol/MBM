#!/usr/bin/env python3
"""V2 beat map — row 85, build-85-shepherds-and-angels (Luke 2:8-19).

COVERAGE: 23 pictures over 132.3 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 2:8-19 KJV):
  v8    "shepherds abiding in the field, keeping WATCH OVER THEIR FLOCK
        BY NIGHT" — a night pasture outside Bethlehem.
  v9    "the ANGEL of the Lord came upon them, and the GLORY of the
        Lord shone round about them: and they were SORE AFRAID."
  v10-11 "Fear not... good tidings of great joy, which shall be to ALL
        PEOPLE. For UNTO YOU is born this day in the city of David a
        Saviour, which is Christ the Lord."
  v13   "suddenly there was with the angel a MULTITUDE of the heavenly
        host praising God" — the sky filled.
  v14   "Glory to God in the highest, and on earth PEACE, GOOD WILL
        toward men."
  v15-16 "Let us now go even unto Bethlehem... And they came WITH
        HASTE, and found Mary, and Joseph, and the babe lying in a
        manger."
  v17-18 they made known abroad the saying; all that heard WONDERED.
  v19   "But MARY KEPT all these things, and PONDERED them in her
        heart."

ANGEL RENDERING (CONTENT-CARE law — narration demands angels here):
angels are painted as REAL, plain-robed figures in PALE SILVER-GREY
robes — NO wings, NO halos, no outlines of light on any figure; the
v9 "glory" is a great BLAZE of white light filling the field from
above, distinct from the figures themselves. Never the word glow.

JESUS FLAG NOTE: the child is a NEWBORN — adult JESUS LOCK/ref do not
apply; all beats run jesus=False. STABLE/MARY/JOSEPH locks match row
84 (the same night, the same cave).

TIME OF DAY: deep NIGHT throughout — starlit pasture, the great white
blaze during the angel beats, then starlight again; the stable beats
in small-lamp warmth. Correct story darkness, not the row-11 defect.

CHANGING CONDITION (kept OUT of the locks): the sky — stars, then one
blazing presence, then a filled host, then stars again; the shepherds
— drowsy watch, terror, joy, haste, telling.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream (and the adult Jesus does not appear in this row).
LOCKS = {
    "FIELD": (
        "FIELD LOCK: a night pasture on the hills outside Bethlehem — "
        "dry tussocked grass and limestone outcrops, a low banked "
        "watch-fire, a scatter of grey-woolled sheep, and the town's "
        "small dark hill in the distance. The same slope, fire and "
        "distant town throughout."
    ),
    "SHEPHERDS": (
        "SHEPHERDS LOCK: the shepherds are the same four men in every "
        "shot — an old greybeard leaning on a long crook, two "
        "weathered brothers in their thirties, and a boy of about "
        "fourteen; all in rough DARK EARTH-BROWN and CHARCOAL-GREY "
        "mantles and head cloths (never cream, never white), "
        "work-worn and real."
    ),
    "ANGEL": (
        "ANGEL LOCK: the herald angel is a tall, real human figure in "
        "a plain PALE SILVER-GREY robe — NO wings, no ring of light "
        "above the head, no light outlining the body; a calm, strong, "
        "ageless face with dark hair; feet on the ground when standing "
        "among men."
    ),
    "STABLE": (
        "STABLE LOCK: the stable is a rough LIMESTONE CAVE at the "
        "town's edge — uneven rock walls, clean straw on the floor, "
        "a WOODEN FEED-TROUGH manger on legs, a patient OX and a "
        "grey DONKEY tethered at the wall, one small clay oil lamp, "
        "and the door opening to the deep starry night. The same "
        "cave, trough and animals throughout."
    ),
    "MARY": (
        "MARY LOCK: Mary is the same young woman in every shot — "
        "about eighteen, a gentle open face with warm brown eyes, "
        "dark hair under a DEEP INDIGO-BLUE veil, a plain DEEP "
        "INDIGO-BLUE dress (never cream, never white). Weary, "
        "serene, and dignified in every frame."
    ),
    "JOSEPH": (
        "JOSEPH LOCK: Joseph is the same man in every shot — about "
        "thirty, a carpenter's broad hands, short dark beard, "
        "sun-browned face, in a DARK RUSSET-BROWN robe with a "
        "CHARCOAL-GREY head cloth (never cream, never white). "
        "Steady, protective, tired."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r085-b01", "out": "s01-outside-bethlehem-shepherds-were-keeping.jpeg", "seg": "n0",
        "window": "0.28-9.24", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS"],
        "narration": (
            "Outside Bethlehem, shepherds were keeping watch over their "
            "flocks by night — ordinary men working the late shift, about "
            "the lowest job there was."
        ),
        "must_show": "SCRIPTURE-EXACT: the night watch — the four shepherds around their low banked fire among the sheep, the starry night huge over the slope, Bethlehem's small dark hill in the distance.",
        "must_not_show": "no halo, glare or rim-light; the men ORDINARY and work-worn — a plain night shift, nothing yet stirring.",
        "scene": (
            "The night pasture keeps its slow watch, the camera "
            "beyond the fire's ring behind the flock's grey backs: "
            "the four shepherds around "
            "the low banked fire — the old "
            "greybeard nodding on his crook, "
            "the brothers trading low words, "
            "the boy poking the embers — grey "
            "sheep dotted drowsing up the dark "
            "tussocked slope, the stars thick "
            "and cold overhead, and far off "
            "the small black hill of Bethlehem "
            "with its last lamps going out — "
            "the lowest job in Israel, on an "
            "ordinary night. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b02", "out": "s02-not-for-the-palace.jpeg", "seg": "n1b",
        "window": "35.01-36.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD"],
        "narration": "Not for the palace.",
        "must_show": "the not-palace — the distant dark horizon where the great world sleeps: no light going toward any palace; the empty grand direction, passed over.",
        "must_not_show": "no halo, glare or rim-light; no palace shown grandly — just the dark distance the news did NOT go to.",
        "scene": (
            "The frame looks the other way "
            "for one beat: out over the dark "
            "ridgelines toward the great "
            "sleeping world — the direction "
            "of palaces and thrones and "
            "marble halls, all of it black "
            "and silent under the stars, not "
            "one ray of this night's news "
            "travelling toward any of it — "
            "the grand address list passed "
            "over whole, while the light "
            "stands parked above a sheep "
            "field. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b03", "out": "s03-suddenly-an-angel-of-the.jpeg", "seg": "n1",
        "window": "9.88-15.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS", "ANGEL"],
        "narration": (
            "Suddenly an angel of the Lord stood before them, and the glory "
            "of the Lord blazed all around."
        ),
        "must_show": "SCRIPTURE-EXACT: the appearing — the silver-grey-robed angel standing on the grass before the fire, and a great white BLAZE of light flooding the whole slope from above; night turned to brilliance.",
        "must_not_show": "ABSOLUTE: no wings, no halo, no light outlining the figure — the blaze fills the AIR and ground, the angel a solid real figure within it.",
        "scene": (
            "Between one heartbeat and the "
            "next the night tears open: a "
            "tall figure in plain silver-grey "
            "stands on the grass before the "
            "watch-fire where no one stood — "
            "feet on the ground, face calm "
            "and strong — and around him the "
            "whole slope floods with a great "
            "white blaze pouring down out of "
            "the dark, grass and fleece and "
            "stunned faces lit noon-bright at "
            "midnight, the sheep scattering "
            "up the hill from a light with "
            "no lamp in it. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r085-b04", "out": "s04-and-the-angel-said.jpeg", "seg": "n1",
        "window": "16.98-18.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANGEL"],
        "narration": "And the angel said:",
        "must_show": "the herald about to speak — close on the angel's calm strong face in the surrounding brilliance, mouth opening on the first word.",
        "must_not_show": "no wings, no halo, no light-outline on the figure; the face REAL and human-warm, not marble.",
        "scene": (
            "Close on the herald's face in "
            "the flooding brightness: calm, "
            "strong, ageless, the dark hair "
            "stirred by no wind of earth, the "
            "eyes bent kindly on four "
            "terrified sheep-men as the mouth "
            "opens on the first word — a "
            "messenger built to stand in "
            "throne rooms, spending the "
            "biggest announcement in history "
            "on the night shift, by choice. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r085-b05", "out": "s05-for-unto-you-is-born.jpeg", "seg": "j1",
        "window": "25.11-31.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS", "ANGEL"],
        "narration": (
            "For unto you is born this day in the city of David a Saviour, "
            "which is Christ the Lord."
        ),
        "must_show": "SCRIPTURE-EXACT: the announcement — the angel's arm extended toward distant Bethlehem, the shepherds' lit faces following the gesture; the news aimed at THEM.",
        "must_not_show": "no wings, no halo, no light-outline; the pointing arm CLEAR — the city of David named by gesture across the night.",
        "scene": (
            "The herald's arm sweeps out over "
            "the blazing grass toward the "
            "small dark hill of Bethlehem — "
            "UNTO YOU is born THIS DAY — and "
            "the four lit faces swing along "
            "the pointing line: the greybeard "
            "clutching his crook, the "
            "brothers half-risen, the boy's "
            "mouth open — a Saviour announced "
            "with a delivery address and a "
            "date, to men whose names no "
            "census taker had bothered "
            "getting right. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r085-b06", "out": "s06-listen-to-who-he-says.jpeg", "seg": "n1b",
        "window": "32.89-35.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERDS"],
        "narration": "Listen to who he says it is for.",
        "must_show": "the addressees — close on the four shepherds' blazing-lit faces: rough, unshaved, work-worn, and being addressed by heaven; the FOR YOU landing.",
        "must_not_show": "no halo, glare or rim-light on the men; their roughness UNSOFTENED — exactly these faces, chosen.",
        "scene": (
            "Close on the four faces the "
            "light picked: the greybeard's "
            "deep-creased squint, the "
            "brothers' wind-burned cheeks and "
            "broken noses, the boy's fire-"
            "smudged jaw — night-shift faces, "
            "smelling of sheep and smoke, "
            "unshaved and unimportant by "
            "every measure the world keeps — "
            "and heaven's whole address "
            "written across them: unto YOU. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r085-b07", "out": "s07-not-for-the-temple-for.jpeg", "seg": "n1b",
        "window": "36.50-40.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS"],
        "narration": (
            "Not for the temple. For you — the men out in the field on the "
            "night shift."
        ),
        "must_show": "the choice of field over temple — the lit shepherds amid their sheep and rock, the great light holding THEM; the working field as heaven's chosen venue.",
        "must_not_show": "no halo, glare or rim-light on figures; the field's ordinariness intact — crooks, fire, wool, dung and stone, all inside the brilliance.",
        "scene": (
            "The wide frame holds heaven's "
            "chosen venue in full: a working "
            "sheep field — dung-dotted grass, "
            "a smoking watch-fire, wool "
            "snagged on thorn, four men with "
            "crooks — every ordinary inch of "
            "it standing inside the great "
            "white blaze like a room heaven "
            "walked into on purpose, while "
            "somewhere far off the temple "
            "sleeps unvisited — the night "
            "shift, outranking the establishment "
            "by grace. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b08", "out": "s08-and-in-a-moment-the.jpeg", "seg": "n2",
        "window": "41.39-47.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS", "ANGEL"],
        "narration": (
            "And in a moment the one angel became a vast multitude of the "
            "heavenly host, filling the whole sky."
        ),
        "must_show": "SCRIPTURE-EXACT: the multitude — the sky above the slope filled rank upon rank with plain-robed figures in the brilliance, the one herald below them; the shepherds tiny beneath a filled heaven.",
        "must_not_show": "ABSOLUTE: no wings, no halo, glare or rim-light, no light-outlines on any figure — a host of real plain-robed figures standing in the bright air, receding by rank into the light.",
        "scene": (
            "The sky itself changes tenancy, the camera low behind "
            "the four kneeling silhouetted-dark shoulders: "
            "above the blazing slope the "
            "brightness fills rank upon rank "
            "with standing figures — plain-"
            "robed in silver-grey, real as "
            "soldiers on parade, row behind "
            "row receding up into the light "
            "until counting fails — the one "
            "herald below them like the "
            "first note of a chord, and "
            "under it all four small men and "
            "their sheep, flattened with awe "
            "on a hillside beneath a filled "
            "heaven. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b09", "out": "s09-glory-to-god-in-the.jpeg", "seg": "j2",
        "window": "48.48-52.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "ANGEL"],
        "narration": (
            "Glory to God in the highest, and on earth peace, good will "
            "toward men."
        ),
        "must_show": "SCRIPTURE-EXACT: the anthem — the host mid-praise: mouths open, arms lifted, the whole bright sky singing one thing over the dark earth.",
        "must_not_show": "no wings, no halo, glare or rim-light, no light-outlines; the singing VISIBLE — open mouths, lifted faces, a sky-wide chorus.",
        "scene": (
            "The filled sky sings: rank on "
            "plain-robed rank with faces "
            "lifted and mouths open on the "
            "same words, arms rising like a "
            "field of grain in one wind — "
            "GLORY in the highest pouring "
            "upward, PEACE and GOOD WILL "
            "raining down — the dark sleeping "
            "earth below receiving heaven's "
            "verdict on the human race, "
            "delivered in full choir over a "
            "sheep pasture at midnight. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r085-b10", "out": "s10-that-is-what-the-sky.jpeg", "seg": "n2b",
        "window": "54.38-57.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERDS"],
        "narration": "That is what the sky said. Not a warning.",
        "must_show": "the message's kindness landing — close on the shepherds' upturned faces: terror melting into open wonder as the words prove kind.",
        "must_not_show": "no halo, glare or rim-light; the transition READABLE — fear's grip loosening, wonder arriving in its place.",
        "scene": (
            "Close on the four upturned faces "
            "as the words sort themselves "
            "into kindness: the greybeard's "
            "white-knuckled grip easing down "
            "the crook, the brothers' braced "
            "shoulders coming loose, the "
            "boy's terror tipping over into "
            "open-mouthed wonder — men who "
            "crouched for a blow finding the "
            "sky full of good will instead, "
            "and hardly knowing where in "
            "their bodies to put it. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r085-b11", "out": "s11-not-a-demand-peace-and.jpeg", "seg": "n2b",
        "window": "57.59-66.60", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS"],
        "narration": (
            "Not a demand. Peace, and good will — heaven's opinion of the "
            "human race, said out loud over a sheep field."
        ),
        "must_show": "the verdict's venue — the whole scene held gently: bright host above, humble field and listening men below; heaven's opinion delivered over grass and wool.",
        "must_not_show": "no wings, no halos, no light-outlines; the field HUMBLE to the last detail under the glorious sky — the contrast is the meaning.",
        "scene": (
            "The frame holds, the camera far across the slope "
            "taking sky and field from the side, the whole "
            "impossible pairing: above, the "
            "sky-wide shining ranks of the "
            "host in full anthem — below, a "
            "stony pasture, a guttered watch-"
            "fire, bewildered sheep, and four "
            "men in patched wool standing in "
            "the grandest verdict ever "
            "pronounced — peace, good will — "
            "heaven's settled opinion of the "
            "human race, read aloud over the "
            "least of its real estate. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r085-b12", "out": "s12-they-were-terrified.jpeg", "seg": "n1",
        "window": "15.11-16.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERDS"],
        "narration": "They were terrified.",
        "must_show": "SCRIPTURE-EXACT: sore afraid — the shepherds recoiling in the sudden brilliance: an arm flung over eyes, a body stumbling back over a rock, the boy gripping the greybeard.",
        "must_not_show": "no halo, glare or rim-light on figures; the terror PHYSICAL and honest — real men, really afraid.",
        "scene": (
            "The brilliance hits and the men "
            "break like startled birds: one "
            "brother stumbling backward over "
            "a rock with his arm flung "
            "across his eyes, the other "
            "frozen mid-crouch, the boy "
            "clamped to the greybeard's "
            "mantle with both fists while "
            "the old man's crook comes up "
            "between them and the light like "
            "a stick against the sun — night-"
            "shift courage doing its honest "
            "best against a torn-open sky. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r085-b13", "out": "s13-when-the-angels-had-gone.jpeg", "seg": "n3",
        "window": "67.25-71.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS"],
        "narration": (
            "When the angels had gone away into heaven, the shepherds said "
            "to one another:"
        ),
        "must_show": "SCRIPTURE-EXACT: the after — the ordinary starry night restored over the slope, the four men clustered at the fire, faces close, urgent counsel beginning.",
        "must_not_show": "no residual light-effects — the sky plain stars again; the huddle ALIVE, hands already gesturing toward town.",
        "scene": (
            "The sky is only stars again — "
            "sudden, enormous, ordinary — and "
            "the slope stands dark around the "
            "little fire where four changed "
            "men cluster head to head: eyes "
            "still full of what just left, "
            "voices tumbling over each other, "
            "the boy's arm already flung out "
            "toward the small black hill of "
            "Bethlehem — a committee meeting "
            "of the lowest men in Israel, "
            "lasting all of one breath. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r085-b14", "out": "s14-let-us-now-go-even.jpeg", "seg": "s15",
        "window": "71.98-78.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERDS"],
        "narration": (
            "Let us now go even unto Bethlehem, and see this thing which is "
            "come to pass, which the Lord hath made known unto us."
        ),
        "must_show": "SCRIPTURE-EXACT: the resolve — close on the huddle at decision: the greybeard's nod, crooks taken up, bodies turning townward as one.",
        "must_not_show": "no halo, glare or rim-light; the decision UNANIMOUS and instant — no dissenter, no lingering.",
        "scene": (
            "Close on the moment the decision "
            "lands: the greybeard's single "
            "slow nod, and around it the "
            "instant unanimity of men who "
            "have stopped needing convincing "
            "— crooks snatched up, mantles "
            "cinched, every body already "
            "turned townward on the balls of "
            "its feet — LET US NOW GO — four "
            "shepherds voting with their "
            "whole bones to leave the only "
            "flock they have ever left "
            "untended. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b15", "out": "s15-they-did-not-stand-around.jpeg", "seg": "n3b",
        "window": "80.58-84.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS"],
        "narration": (
            "They did not stand around discussing it. They came with haste "
            "into the town."
        ),
        "must_show": "SCRIPTURE-EXACT: the haste — the four running downslope through the starlight toward Bethlehem's dark hill, mantles flying, the boy out front.",
        "must_not_show": "no halo, glare or rim-light; the run FLAT-OUT — night-shift men sprinting like boys, the field left behind.",
        "scene": (
            "Down the dark slope they run, the camera beside their "
            "line so the sprint crosses in profile toward the "
            "town's far lights — "
            "flat-out, mantles streaming, the "
            "boy's young legs pulling him out "
            "front with the brothers pounding "
            "behind and the old greybeard "
            "hitching along at his fastest "
            "in forty years — four figures "
            "flying through starlit tussocks "
            "toward the sleeping town below, "
            "haste made holy, the first feet "
            "on earth ever to run TOWARD "
            "this news. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b16", "out": "s16-they-found-mary-and-joseph.jpeg", "seg": "n4",
        "window": "85.68-91.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY", "JOSEPH", "SHEPHERDS"],
        "narration": (
            "They found Mary and Joseph, and the baby lying in the manger — "
            "exactly as they had been told."
        ),
        "must_show": "SCRIPTURE-EXACT: the finding — the shepherds crowding the cave's mouth, the lamplit family within: Mary, Joseph, the swaddled babe in the trough; the sign matching word for word.",
        "must_not_show": "no halo on the child or anyone; the shepherds at the THRESHOLD, awed and hesitant, wool and night air still on them.",
        "scene": (
            "At the cave's mouth, the camera inside behind the "
            "lamplit family's shoulders, the four "
            "runners pull up breathless — and "
            "there it all is, exactly as "
            "spoken: the small lamp's amber "
            "room, Mary resting against the "
            "rock in her indigo veil, Joseph "
            "rising watchful from beside "
            "her, and in the straw-lined "
            "feed-trough the swaddled child — "
            "the sign checking itself off "
            "detail by detail while the "
            "shepherds hang at the threshold, "
            "suddenly shy of the thing they "
            "sprinted for. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r085-b17", "out": "s17-there-he-was-the-saviour.jpeg", "seg": "n5",
        "window": "92.17-100.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "SHEPHERDS"],
        "narration": (
            "There he was: the Saviour of the world, a tiny newborn asleep "
            "in a feed trough, wrapped in strips of cloth."
        ),
        "must_show": "the beholding — the shepherds kneeling in close around the manger, rough faces bent over the tiny swaddled sleeper; the world's Saviour at wool-scented arm's length.",
        "must_not_show": "no halo on the child; the kneeling men HUGE and gentle around the small trough — scale and tenderness together.",
        "scene": (
            "The four big men fold down "
            "small around the feed-trough — "
            "knees in the straw, crooks laid "
            "aside, the greybeard's scarred "
            "hand hovering an inch above the "
            "wrapping and not daring — and "
            "between their bent shoulders the "
            "whole announcement lies asleep: "
            "a tiny newborn in strips of "
            "cloth, chest rising and falling "
            "in the lamp's warmth, the "
            "Saviour of the world within "
            "reach of hands that smell of "
            "sheep. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b18", "out": "s18-the-shepherds-could-not-keep.jpeg", "seg": "n6",
        "window": "100.77-102.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERDS"],
        "narration": "The shepherds could not keep it in.",
        "must_show": "the overflow — close on the shepherds' faces at the threshold turning back to the night: joy cracking through, grins breaking, news outgrowing its containers.",
        "must_not_show": "no halo, glare or rim-light; the joy IRREPRESSIBLE — men visibly losing the fight to stay quiet.",
        "scene": (
            "Close at the cave mouth as the "
            "containment fails: the brothers "
            "turning to each other with grins "
            "cracking their wind-burned "
            "faces wide open, the boy "
            "half-laughing, half-crying, the "
            "greybeard shaking his head over "
            "and over like a man checking a "
            "coin that keeps being real — "
            "four ordinary chests packed "
            "past capacity with the one "
            "story too big to walk home "
            "quietly with. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r085-b19", "out": "s19-they-went-out-glorifying-and.jpeg", "seg": "n6",
        "window": "102.72-108.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERDS"],
        "narration": (
            "They went out glorifying and praising God, telling everyone "
            "they met what they had seen and heard."
        ),
        "must_show": "SCRIPTURE-EXACT: the telling — the shepherds in the lamplit lane, animated mid-story to roused householders at doors and windows; wonder spreading face to face.",
        "must_not_show": "no halo, glare or rim-light; the listeners WONDERING (v18) — doors opening, heads leaning out, sleep abandoned.",
        "scene": (
            "Down the narrow lamplit lane "
            "the news goes off like sparks in "
            "stubble: the shepherds mid-"
            "story with arms sweeping the "
            "sky's remembered ranks, a "
            "householder leaning out his "
            "door with a lamp, heads "
            "appearing at windows above, a "
            "woman pressing both hands to "
            "her mouth — night-shift men "
            "glorifying God at full volume "
            "in a sleeping street, and "
            "wonder catching from face to "
            "face faster than they can talk. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r085-b20", "out": "s20-but-mary-kept-all-these.jpeg", "seg": "n7",
        "window": "108.89-112.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY"],
        "narration": "But Mary kept all these things, and pondered them in her heart.",
        "must_show": "SCRIPTURE-EXACT: the pondering — close on Mary in the lamp's quiet: the child gathered to her, her eyes open and deep, everything being kept.",
        "must_not_show": "no halo; the stillness ABSOLUTE against the lane's distant commotion — one silent keeper in a noisy story.",
        "scene": (
            "Inside the cave the lamp keeps "
            "its small quiet, and in it Mary "
            "sits perfectly still with the "
            "swaddled child gathered against "
            "her — her eyes open, deep, "
            "travelling slowly over nothing "
            "visible — the shepherds' distant "
            "shouting a faint music at the "
            "edge of the night — while every "
            "detail of this day is carried, "
            "one by one, down into the "
            "keeping-place her heart has "
            "cleared for it. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r085-b21", "out": "s21-in-a-story-full-of.jpeg", "seg": "n7b",
        "window": "114.28-119.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY", "JOSEPH"],
        "narration": (
            "In a story full of people shouting, Luke stops to tell you "
            "about the one person who said nothing."
        ),
        "must_show": "the contrast — the wide quiet cave: Mary silent with the child, Joseph at rest, the open door letting in the faint far commotion; stillness framed against noise.",
        "must_not_show": "no halo; the quiet the COMPOSITION — the loud world outside the door, the still centre within.",
        "scene": (
            "The wide frame sets the two "
            "volumes side by side: through "
            "the cave's open mouth the "
            "faint far lamplight and "
            "commotion of a town waking up "
            "to news — and within, the still "
            "amber room where nobody says "
            "anything at all: Joseph settled "
            "back against the rock with his "
            "eyes closing, the animals "
            "breathing slow, and Mary at the "
            "centre holding the child and "
            "her silence with the same two "
            "arms. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b22", "out": "s22-she-gathered-it-all-up.jpeg", "seg": "n7b",
        "window": "119.97-131.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["STABLE", "MARY"],
        "narration": (
            "She gathered it all up — the angels, the shepherds, the trough, "
            "the strangers at the door in the middle of the night — and she "
            "held on to it, and turned it over, for the rest of her life."
        ),
        "must_show": "the keeping — Mary's face bent over the sleeping child in the lamplight: memory visibly at work behind the quiet eyes; a lifetime's treasury receiving its first deposits.",
        "must_not_show": "no halo; nothing literal-symbolic in frame — the gathering happens entirely in her attentive face.",
        "scene": (
            "Close on the keeper at her "
            "work: Mary's face bent over the "
            "sleeping child, the lamp's "
            "small flame steady in her dark "
            "eyes while behind them the day "
            "is gathered piece by piece — "
            "the torn-open sky retold at her "
            "door, the running men, the "
            "trough's absurd humility, the "
            "smell of sheep and straw — each "
            "one turned over slowly and laid "
            "down whole in a treasury she "
            "will draw on for the rest of "
            "her life. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r085-b23", "out": "s23-fear-not-for-behold-i.jpeg", "seg": "j1",
        "window": "18.96-25.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIELD", "SHEPHERDS", "ANGEL"],
        "narration": (
            "Fear not: for, behold, I bring you good tidings of great joy, "
            "which shall be to all people."
        ),
        "must_show": "SCRIPTURE-EXACT: FEAR NOT — the angel's calming open palms toward the cowering shepherds, the brilliance around them; terror being met with gentleness.",
        "must_not_show": "no wings, no halo, glare or rim-light, no light-outline; the palms OPEN and lowered toward the men — the universal gesture of no-harm.",
        "scene": (
            "The herald's two hands come out "
            "and down, palms open toward the "
            "cowering men — the oldest "
            "gesture of no-harm there is — "
            "FEAR NOT — and the words move "
            "through the brilliance like "
            "warmth through cold water: the "
            "flung-up arms lowering inch by "
            "inch, the boy's grip easing on "
            "the old man's mantle, four "
            "terrors being individually "
            "gentled by a messenger who "
            "brought only joy and has all "
            "night to prove it. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "FIELD": "PLACE-REF/field.jpeg",  # build-25-wheat-and-tares v2-r025-b04
}
# === end PLACE-PLATES ===
