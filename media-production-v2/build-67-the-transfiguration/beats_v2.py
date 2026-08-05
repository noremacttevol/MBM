#!/usr/bin/env python3
"""V2 beat map — row 67, build-67-the-transfiguration (Mark 9:2-8; Matthew
17:1-8).

COVERAGE: 16 pictures over 91.5 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 9:2-8; Matthew 17:1-8 KJV):
  v2    "taketh with him PETER, and JAMES, and JOHN ... into an HIGH
        MOUNTAIN APART" — the three from CAST_LOCKS; a bare high summit
        above the cloud line.
  v3    "his raiment became SHINING, EXCEEDING WHITE AS SNOW; so as no
        fuller on earth can white them" / Matthew: "his face did shine as
        the sun, and his raiment was WHITE AS THE LIGHT."
        ⚠️ THE ONE SCRIPTURE-MANDATED BRIGHTNESS IN THE LIBRARY: rendered
        as GARMENT-LIGHT in scripture's own terms — raiment white as
        sunlit snow, brightness OF the clothing and face, the summit lit
        by it. The anti-halo law still holds its core: NO halo RING, no
        painted disc, no rim-line outlining his head — the whiteness is
        total and fabric-borne, never an outline effect. His locked face
        remains exactly his own, fully visible.
  v4    "there appeared unto them ELIAS with MOSES: and they were talking
        with Jesus" — two glorious elders, painted with full dignity
        (they are prophets, not angels — permitted); their identity told
        by emblem: Moses grave with the law's authority, Elijah wild
        with the desert's.
  v5-6  Peter's tabernacles offer — "he wist not what to say; for they
        were sore afraid" — Mark's kindness kept: fear and babble
        painted tenderly.
  v7    "a CLOUD overshadowed them: and a VOICE came out of the cloud" —
        the bright cloud shown; THE VOICE NEVER EMBODIED — no figure, no
        light-source in the cloud; the words land on faces only.
  v8    "suddenly ... they saw no man any more, save JESUS ONLY" — the
        ordinary restored: the same friend, reaching down to lift them.

TIME OF DAY: the ascent in late afternoon; the summit event in its own
scripture-light against a deepening sky; the aftermath in plain quiet
dusk — 'Jesus only' in ordinary evening light, the contrast the point.

CONTENT-CARE: no flags. The fear painted kindly; the glory painted by
the book; the Father heard, never seen.

CHANGING CONDITION (kept OUT of the locks): the LIGHT ITSELF — ordinary
climb-light, the raiment's blazing white, the cloud's brightness, then
plain dusk. Stated per-beat; no lock carries it.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MOSES": (
        "MOSES LOCK: Moses is the same figure in every appearance — very "
        "old and unbowed, a great white beard to his chest, a broad "
        "graven face of lawgiver's authority, dressed in a DEEP "
        "EARTH-BROWN robe with a DARK RED mantle, and carrying nothing "
        "(never cream, never white robes; his dignity is in his face). "
        "His face is shown clearly."
    ),
    "ELIJAH": (
        "ELIJAH LOCK: Elijah is the same figure in every appearance — "
        "lean and weathered as desert rock, wild iron-grey hair and "
        "beard, fierce kind eyes, dressed in a rough DARK CAMEL-BROWN "
        "mantle bound with a wide leather belt (never cream, never "
        "white). His face is shown clearly."
    ),
    "SUMMIT": (
        "SUMMIT LOCK: the high mountain apart — a bare rounded summit "
        "of pale broken rock above the cloud line, thin grass in the "
        "clefts, lower ranges and valley haze far below, and a wide "
        "sky. The same rocks and skyline in every summit beat."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r067-b01", "out": "s01-jesus-took-three-of-his.jpeg", "seg": "n0",
        "window": "0.40-6.86", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN", "JAMES-Z", "SUMMIT"],
        "narration": (
            "Jesus took three of his closest friends — Peter, James, and John — "
            "up a high mountain, away from everyone."
        ),
        "must_show": "SCRIPTURE-EXACT: the ascent — the four climbing the last bare shoulder of the high summit in late-afternoon light, the world's haze far below; apartness as altitude.",
        "must_not_show": "no halo, glare or rim-light on Jesus (ordinary light in this beat); the four alone — no crowd anywhere in the world below.",
        "scene": (
            "Up the last bare shoulder of the high mountain, the "
            "camera below the path taking the climb in profile, "
            "the four climb in the late gold — "
            "Jesus ahead on the broken pale rock, Peter "
            "hauling himself past a boulder, James and "
            "John spaced on the slope below — and "
            "beneath them the whole world has dropped "
            "away into blue valley haze and distant "
            "ranges: four small figures walking up out "
            "of everything, into the thin bright quiet. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r067-b02", "out": "s02-and-there-in-front-of.jpeg", "seg": "n1",
        "window": "8.57-10.82", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN", "JAMES-Z", "SUMMIT"],
        "narration": "And there, in front of them, he changed.",
        "must_show": "SCRIPTURE-EXACT: the change beginning — Jesus a few paces apart on the summit as his raiment's white starts to exceed all ordinary white; the three friends' faces caught at the first second of it.",
        "must_not_show": "NO halo ring, no disc, no outline-light around his head — the brightness is OF the garments, beginning; his locked face fully his own and visible.",
        "scene": (
            "On the summit's pale rock Jesus stands a "
            "few paces apart — and the change has "
            "begun: his cream robe turning a white "
            "beyond any bleaching, white as high snow "
            "in full sun, the brightness belonging to "
            "the fabric itself and climbing — while "
            "behind him the three friends have frozen "
            "mid-step, Peter's hand still on the "
            "boulder, three faces caught at the exact "
            "first second of the impossible. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r067-b03", "out": "s03-his-clothes-turned-a-blinding.jpeg", "seg": "n1",
        "window": "10.82-18.88", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SUMMIT"],
        "narration": (
            "His clothes turned a blinding white, brighter than anything on "
            "earth, and for one moment they saw him shining with who he really "
            "is."
        ),
        "must_show": "SCRIPTURE-EXACT: the full transfiguration — Jesus in raiment white as the light itself, his face bright as sunlit day, the summit's rocks lit pale by the garment-light; glory by the book.",
        "must_not_show": "NO halo ring, no disc, no rim-outline — the whiteness total and fabric-borne, the face HIS OWN locked face, bright but exactly himself; the light source the raiment, never a shape behind him.",
        "scene": (
            "The summit holds its one impossible "
            "moment: Jesus stands in raiment gone "
            "white as the light itself — every fold of "
            "the robe bright as sun on snow, no fuller's "
            "white within a world of it — and his own "
            "familiar face above it bright as a clear "
            "noon, still exactly and unmistakably his "
            "face — while the pale rocks around his "
            "feet stand lit by what he is wearing, and "
            "the deepening sky behind makes the white "
            "absolute. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r067-b04", "out": "s04-this-is-my-son-whom.jpeg", "seg": "n3b",
        "window": "63.00-65.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SUMMIT"],
        "narration": "This is my Son, whom I love.",
        "must_show": "the sentence landing — close on Peter's upturned cloud-lit face receiving the Father's words: fear and glory together, a man hearing heaven speak.",
        "must_not_show": "NO source of the voice depicted — no figure, no beam, no shape in the brightness; the words exist only on the hearing face.",
        "scene": (
            "Close on Peter's upturned face in the "
            "cloud's pale brightness: the wild curls "
            "pressed back, eyes enormous, the fisherman's "
            "features holding terror and joy in the "
            "same grip as words from nowhere and "
            "everywhere land on him — a man being "
            "introduced, by a voice without any "
            "direction, to who his friend has been all "
            "along. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r067-b05", "out": "s05-two-of-the-greatest-prophets.jpeg", "seg": "n2a",
        "window": "20.58-25.37", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOSES", "ELIJAH", "SUMMIT"],
        "narration": (
            "Two of the greatest prophets, Moses and Elias, appeared and stood "
            "talking with him."
        ),
        "must_show": "SCRIPTURE-EXACT: the visitors — Moses and Elijah standing WITH the transfigured Jesus in easy conference on the summit: three figures, one conversation, centuries folded.",
        "must_not_show": "no halo rings on anyone; the two elders solid and dignified, not translucent phantoms; the talking REAL — gesture and attention among the three.",
        "scene": (
            "On the lit summit, the camera low among the rocks "
            "behind the three watching friends, the impossible "
            "conference stands in session: the ancient "
            "lawgiver in his earth-brown and dark red, "
            "graven face turned gravely to Jesus; the "
            "desert prophet lean and wild-haired in his "
            "camel-brown mantle, one hand mid-gesture — "
            "both solid as the rock they stand on — and "
            "between them the white-raimented Jesus "
            "listening and answering, three figures "
            "talking together as men talk, across "
            "fourteen centuries, about what comes "
            "next. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r067-b06", "out": "s06-peter-overwhelmed-blurted-out-the.jpeg", "seg": "n2b",
        "window": "27.05-30.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SUMMIT"],
        "narration": "Peter, overwhelmed, blurted out the first thing that came to him.",
        "must_show": "the blurt — Peter half-risen from the rocks, arm out, mouth already running ahead of his mind; the overwhelm speaking first.",
        "must_not_show": "no halo, glare or rim-light on the friends; the babble tender, never mocked — love with nowhere to put itself.",
        "scene": (
            "Half-risen from the pale rocks Peter is "
            "already talking — one arm flung out toward "
            "the three shining figures, his mouth "
            "running a full sentence ahead of any plan, "
            "James's hand rising too late to catch his "
            "brother's sleeve — a man so overwhelmed "
            "that silence has become impossible, "
            "offering the first words that will come, "
            "because none of the right ones exist. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r067-b07", "out": "s07-master-it-is-good-for.jpeg", "seg": "j1",
        "window": "32.33-40.22", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "MOSES", "ELIJAH", "SUMMIT"],
        "narration": (
            "Master, it is good for us to be here: and let us make three "
            "tabernacles; one for thee, and one for Moses, and one for Elias."
        ),
        "must_show": "SCRIPTURE-EXACT: the offer — Peter mid-proposal, hands sketching three shelters in the air toward the three glorious figures; architecture offered to glory.",
        "must_not_show": "no halo rings; the offer earnest and homely — a builder's hands solving heaven with tent-poles; gently absurd, never ridiculed.",
        "scene": (
            "Peter stands mid-proposal, the camera at his side so "
            "his sketching hands cross in profile toward the three, "
            "in the summit's "
            "strange light, his big hands sketching "
            "three tent-shapes in the air — one, two, "
            "three — toward Jesus in his blazing white "
            "and the two great elders beside him, his "
            "face all earnest hospitality — a "
            "fisherman offering to solve the meeting "
            "of ages with poles and goat-hair, because "
            "building a shelter is the only way he "
            "knows to say 'stay'. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r067-b08", "out": "s08-he-wanted-to-keep-the.jpeg", "seg": "n2c",
        "window": "41.84-45.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SUMMIT"],
        "narration": "He wanted to keep the moment. Build something, stay a while.",
        "must_show": "the wish beneath the babble — close on Peter's face amid the glory: the ache to make the moment permanent, plain under the fear.",
        "must_not_show": "no halo, glare or rim-light on the friends; the ache universal — everyone's wish at every summit, on one face.",
        "scene": (
            "Close on Peter's face in the pale light: "
            "under the fear and the babble, the ache "
            "stands plain — eyes moving over the "
            "shining conference like a man memorizing "
            "what he already knows is leaving, the "
            "wish to fence the moment and live inside "
            "it written in every line — the oldest "
            "human prayer at every mountaintop: let "
            "this stay. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r067-b09", "out": "s09-mark-adds-kindly-that-peter.jpeg", "seg": "n2c",
        "window": "45.18-50.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "JAMES-Z", "SUMMIT"],
        "narration": (
            "Mark adds, kindly, that Peter did not know what to say, because "
            "they were so afraid."
        ),
        "must_show": "the fear owned — the three friends low among the rocks: James gripping stone, John's arm over his eyes, Peter still talking; terror and wonder sharing three postures.",
        "must_not_show": "no halo, glare or rim-light on the friends; the fear dignified — strong men out of scale, not cowards.",
        "scene": (
            "Among the pale boulders the three friends "
            "hold three shapes of the same fear: James "
            "down on one knee with his hand clamped on "
            "the rock as if the mountain might move, "
            "young John with a forearm half-raised "
            "against the brightness, and Peter still "
            "upright, still talking, because words are "
            "the only footing he has left — three "
            "strong men being kindly recorded at the "
            "edge of what men can stand. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r067-b10", "out": "s10-then-a-bright-cloud-settled.jpeg", "seg": "n3",
        "window": "52.27-56.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["SUMMIT"],
        "narration": (
            "Then a bright cloud settled over the mountain, and out of it came "
            "a voice."
        ),
        "must_show": "SCRIPTURE-EXACT: the cloud — a luminous pale cloud descending onto the summit, folding over rocks and figures alike; brightness without any source-shape inside it.",
        "must_not_show": "NO figure, beam, or form within the cloud — pale luminous vapour only; the voice unrepresented; no halo rings.",
        "scene": (
            "Down onto the summit the cloud comes — a "
            "pale luminous mass folding over the "
            "rocks, sliding between the figures, "
            "erasing the far ranges and the sky until "
            "the whole mountaintop stands inside a "
            "brightness with no direction — vapour lit "
            "evenly from everywhere and nowhere, "
            "holding four men and their unfinished "
            "sentence in a white hush about to speak. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r067-b11", "out": "s11-this-is-my-beloved-son.jpeg", "seg": "j2",
        "window": "58.31-61.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN", "JAMES-Z", "SUMMIT"],
        "narration": "This is my beloved Son: hear him.",
        "must_show": "SCRIPTURE-EXACT: the identification — the friends fallen low in the bright cloud, and Jesus standing indicated by nothing but the words themselves; the sentence's weight on the whole frame.",
        "must_not_show": "NO voice-source, no pointing light, no figure in the cloud; Jesus simply present in the brightness — identified by hearing, not by sign.",
        "scene": (
            "Inside the even brightness the three "
            "friends have gone down among the rocks — "
            "faces to the stone, hands over heads — "
            "and Jesus stands quiet in the white air "
            "a few paces off, indicated by nothing: no "
            "beam finds him, no light points, nothing "
            "singles him out except the sentence "
            "itself, landing on three prostrate "
            "listeners with the weight of the only "
            "introduction that has ever mattered. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r067-b12", "out": "s12-listen-to-him-not-build.jpeg", "seg": "n3b",
        "window": "65.16-67.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SUMMIT"],
        "narration": "Listen to him. Not build for him.",
        "must_show": "the correction received — Peter's sketching hands sinking down out of their tent-shapes; the building instinct laid gently to rest.",
        "must_not_show": "no halo, glare or rim-light; the hands' descent the whole beat — architecture yielding to attention.",
        "scene": (
            "Close in the pale brightness: Peter's big "
            "hands — mid-air a moment ago, sketching "
            "tabernacles — sinking slowly down out of "
            "their shapes, the offered architecture "
            "dissolving unbuilt, his face above them "
            "changing from host to hearer — one "
            "instruction re-routing a fisherman's whole "
            "way of loving, from doing something to "
            "listening. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r067-b13", "out": "s13-not-stay-up-here-with.jpeg", "seg": "n3b",
        "window": "67.77-71.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["SUMMIT"],
        "narration": "Not stay up here with him. Listen to him.",
        "must_show": "the mountain relativized — the summit's rocks with the valley world visible again far below through thinning brightness: the place hearing will actually happen.",
        "must_not_show": "no halo, glare or rim-light; the world below the beat — where listening lives; the summit already loosening its hold.",
        "scene": (
            "Through the thinning brightness the world "
            "returns below the summit — the valley "
            "haze, the far ranges, the thread of a "
            "road, the smoke of somebody's evening "
            "fire — all of it small and waiting under "
            "the mountain's bare rocks: the actual "
            "country of listening, which was never up "
            "here, coming back into view exactly on "
            "time. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r067-b14", "out": "s14-of-everything-the-father-could.jpeg", "seg": "n3b + n4",
        "window": "71.13-79.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "JAMES-Z", "SUMMIT"],
        "narration": (
            "Of everything the Father could have said on that mountain, he gave "
            "them one sentence and one instruction. And then it was over."
        ),
        "must_show": "the economy of heaven — the three friends still low as the brightness lifts: one sentence's whole weight settling; the cloud already going.",
        "must_not_show": "no halo, glare or rim-light; the departure unmarked — brightness simply thinning; the sentence the only thing left behind.",
        "scene": (
            "The brightness thins around the three "
            "friends still low among the rocks — the "
            "even white paling back toward ordinary "
            "dusk air, the far world firming through "
            "it — and on the three half-risen faces "
            "the single sentence goes on settling, "
            "heavier than the cloud ever was: heaven's "
            "entire address, one line long, already "
            "outlasting the light it arrived in. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r067-b15", "out": "s15-the-light-faded-the-cloud.jpeg", "seg": "n4",
        "window": "79.47-87.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN", "JAMES-Z", "SUMMIT"],
        "narration": (
            "The light faded, the cloud lifted, and Jesus stood there alone — "
            "the same gentle friend, reaching down to lift them up."
        ),
        "must_show": "SCRIPTURE-EXACT: 'Jesus only' — plain dusk on the summit: Jesus in his ordinary cream robe again, bent over the friends, his hand reaching down to Peter's shoulder; the glory gone, the friend kept.",
        "must_not_show": "no halo, glare or rim-light — ORDINARY evening light, deliberately; the same locked face, the same robe, the reach downward the beat.",
        "scene": (
            "Plain quiet dusk holds the summit, the camera behind "
            "the three friends still low on the rocks: the "
            "cloud gone, the ranges standing ordinary "
            "in the last light — and Jesus, in his "
            "ordinary cream wool again, is bent over "
            "his three friends among the rocks, one "
            "hand reaching down to close on Peter's "
            "shoulder, the other beckoning James and "
            "John up — the same gentle friend who "
            "walked them up the hill, lifting them off "
            "their faces one by one, in light that "
            "asks nothing of anyone. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r067-b16", "out": "s16-do-not-be-afraid-he.jpeg", "seg": "n4",
        "window": "87.62-90.21", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "SUMMIT"],
        "narration": "Do not be afraid, he told them.",
        "must_show": "the closing image — close: Jesus's hand on Peter's shoulder, the two faces near in ordinary dusk; the words as touch; fear ending where it always ends.",
        "must_not_show": "no halo, glare or rim-light; ordinary light final — the mountain's last message delivered at friend-distance.",
        "scene": (
            "Close in the ordinary dusk: Jesus's hand "
            "firm and warm on Peter's shoulder, the "
            "two faces near — the fisherman's still "
            "white-edged with everything he has seen, "
            "and his friend's exactly, unmistakably "
            "the same face as always, saying the "
            "oldest sentence of the trade — the glory "
            "finished, the friendship not, and fear "
            "ending the only way it ever reliably "
            "ends: at arm's length, by name, from "
            "someone who stayed. Every figure has two "
            "arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
