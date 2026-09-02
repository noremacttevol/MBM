#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 25: Sparks in the Dark.

God's fingerprints on the famine centuries: the vision of the man on the
many waters, translators and the press, reformers who lit candles but
never claimed keys, and a free land prepared as the delivery address.
Anchors: 1 Nephi 13:12; D&C 101:80.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 325
NUM = 25
SLUG = "sparks-in-the-dark"
TITLE = "Sparks in the Dark"
META = "1 Nephi 13 · D&C 101"

SEGMENTS = [
    ("n1", NARRATOR,
     "Seventeen hundred years is a long time to wait. But watch what God "
     "was doing with the wait — because the dark centuries are covered "
     "with His fingerprints."),
    ("n2", NARRATOR,
     "Nephi saw it all in vision, two thousand years early. A man among "
     "the nations, moved upon by the Spirit, crossing the many waters:"),
    ("s1", SCRIPTURE,
     "And I looked and beheld a man among the Gentiles, who was "
     "separated from the seed of my brethren by the many waters; and I "
     "beheld the Spirit of God, that it came down and wrought upon the "
     "man; and he went forth upon the many waters, even unto the seed of "
     "my brethren, who were in the promised land."),
    ("n4", NARRATOR,
     "Meanwhile, God pried the book back open. Translators like Wycliffe "
     "and Tyndale put scripture into the language of plow-boys — and "
     "some of them died for it. Then a goldsmith named Gutenberg built a "
     "machine that made burning books pointless. The press. The word "
     "was out — forever."),
    ("n5", NARRATOR,
     "Reformers rose. Luther, nailing his protest to a church door. "
     "Calvin. Wesley, preaching in open fields. Good men. Brave men. "
     "They saw that something was deeply wrong, and they fought it with "
     "everything they had."),
    ("n6", NARRATOR,
     "And notice what not one of them ever claimed: God sent me with "
     "the keys. They claimed the church had drifted — true. They fixed "
     "what they could reach — nobly. But reformation repairs. It cannot "
     "restore. You cannot fix your way back to something heaven has to "
     "hand back."),
    ("n7", NARRATOR,
     "So God prepared a delivery address. A land with no state church "
     "and no king over conscience — where a farm boy could ask God a "
     "question without being burned for the answer. And He signed His "
     "name to it:"),
    ("s2", SCRIPTURE,
     "And for this purpose have I established the Constitution of this "
     "land, by the hands of wise men whom I raised up unto this very "
     "purpose, and redeemed the land by the shedding of blood."),
    ("n8", NARRATOR,
     "God claims the founding of America — by His own mouth. Not "
     "because the nation is perfect, but because the restoration needed "
     "one safe square of earth. Religious freedom went into law "
     "fourteen years before the boy who would need it was born."),
    ("n9", NARRATOR,
     "Now add it up. The book — translated, printed, and open on every "
     "farmhouse table. Freedom of conscience — written into law. And a "
     "buried record waiting in a hillside, a few miles from a farm one "
     "particular family would settle on, as if by chance."),
    ("n11", NARRATOR,
     "So honor the sparks. We owe them everything. And understand "
     "exactly why they were not enough: the famine was never a shortage "
     "of good men. It was a shortage of keys. And keys do not come from "
     "below. Next — a grove of trees."),
]

CARD_SEG = ("card", NARRATOR,
            "The reformers lit candles in the dark. Heaven was preparing "
            "the sunrise.")

CARD_TEXT = ("Candles in the dark.\n"
             "Then the sunrise.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Five — Sparks in the Dark")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="old-world")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "A spark in deep dark: one lit candle leans its flame to the "
        "wick of a second, unlit candle — the pass caught at the "
        "instant the new wick catches, twin flames joined by a thread "
        "of fire, absolute blackness around the small event. Nothing "
        "else in frame.",
        "one candle lighting a second at the instant the wick "
        "catches, blackness around",
        "hands, faces, candelabra, text",
        )),
    ("p02", "s1", _p(
        "The vision on the waters: a lone high-castled sailing ship "
        "runs on an immense open ocean, seen from high and behind — "
        "its sails full-bellied with a wind that ruffles nothing else "
        "on the sea, its wake a straight bright scar across the "
        "endless blue toward the west. Carried, more than sailing.",
        "one high-castled ship from high-behind, sails full on a "
        "windless-seeming immense sea, straight bright wake",
        "fleets, storms, land, flags readable",
        wide=True)),
    ("p03", ("s1", 0.45), _p(
        "Wrought upon: the navigator alone at the night rail — "
        "weathered face lifted to the stars, cloak stirring, one hand "
        "on the rigging and the other holding his cap to his chest — "
        "the look of a man obeying a pull he could not defend at any "
        "court. Lantern-warmth from the deck below.",
        "a weathered navigator at the night rail, face to the "
        "stars, cap held to his chest, compelled",
        "maps readable, crew, his eyes on the lens",
        )),
    ("p04", ("s1", 0.75), _p(
        "The families behind him: emigrant families huddled on a "
        "ship's open deck in cold dawn light — bundles and rope-tied "
        "chests, a mother's arm around two children under one "
        "blanket, a grey-bearded man reading to them from a small "
        "thick book — hope and salt-wind in every fold of cloth. "
        "No faces to the lens.",
        "huddled emigrant families on a cold dawn deck, one elder "
        "reading from a small thick book",
        "readable text, crew working, storms",
        )),
    ("p05", "n4", _p(
        "The translator: an UPRIGHT vertical composition — a hunted "
        "scholar STANDING full height at a tall slanted writing desk "
        "in a shuttered attic, rushlight above the page, worn "
        "volumes propped open around the desk and shelves rising "
        "into shadow above him, his pen flying on the English page, "
        "one ear plainly listening to the street below. His standing "
        "figure anchors the frame's full height. All writing soft "
        "and unreadable.",
        "a scholar standing full-height at a tall desk by rushlight, "
        "shelves rising above, pen mid-stroke",
        "readable words, sideways or rotated composition, soldiers, "
        "windows open",
        )),
    ("p06", ("n4", 0.4), _p(
        "What it cost: in a grey town square, soldiers feed an "
        "armload of books to a bonfire — pages curling to black "
        "moths above the flames, a silent crowd held back at the "
        "square's edge, one woman's hand over her mouth — the war "
        "on the word, fought with fire. No person is harmed in "
        "frame; the books are the martyrs shown.",
        "soldiers burning an armload of books, page-ash rising, a "
        "held-back silent crowd",
        "people burned, violence to people, faces to camera",
        )),
    ("p07", ("n4", 0.7), _p(
        "The machine that ended the burning: Gutenberg's press "
        "mid-PULL — the printer hauling the great screw-bar, an "
        "apprentice peeling a fresh printed sheet off the platen "
        "with both hands, wet pages hung drying on lines above, "
        "type-cases open — the exact moment scarcity died. The "
        "printed text stays soft and unreadable.",
        "a press mid-pull with a fresh sheet being peeled off and "
        "pages drying on lines, unreadable print",
        "readable words, modern machinery, crowds",
        )),
    ("p08", "n5", _p(
        "The protest nailed: at a great church door in cold "
        "morning, a robed monk drives a nail through the corner "
        "of a broad paper — hammer at the top of its second "
        "swing, the sheet lifting in the wind under his steadying "
        "hand, two students stopped mid-step behind him — defiance "
        "as carpentry. The theses' text soft and unreadable.",
        "a monk mid-hammer-swing nailing a broad unreadable paper "
        "to a church door, students stopped behind",
        "readable words, crowds, guards, his eyes on lens",
        )),
    ("p09", ("n5", 0.55), _p(
        "Fields become chapels: an open-air preacher on a farm "
        "wagon at golden evening, arm raised mid-sermon over a "
        "big crowd of laborers and families spread across the "
        "stubble field — shawls, pitchforks laid down, children "
        "on shoulders — the church walls gone and the hunger "
        "plainly not. Camera deep in the crowd, shooting past "
        "heads.",
        "a wagon-top field preacher over a spread laborer crowd "
        "at golden evening, seen past heads",
        "church buildings, faces to camera, banners",
        era="america-1820", wide=True)),
    ("p10", "n6", _p(
        "What none of them claimed: a reformer's two work-worn "
        "hands held open, palms up and EMPTY, over an open Bible "
        "on a plain table — the honest gesture of a man offering "
        "everything he has and holding no keys to offer — window "
        "light across the empty palms and the unreadable page.",
        "two open empty palms held over an open unreadable Bible "
        "in window light",
        "keys anywhere, rings, vestments, faces",
        )),
    ("p11", "n7", _p(
        "The delivery address: a wild American coastline from the "
        "sea at dawn — unbroken hardwood forest rolling back from "
        "white surf into blue-folded hills, no mast, no roof, no "
        "smoke from horizon to horizon — one safe square of earth, "
        "still wrapped. No people.",
        "unbroken forested American coast from the sea at dawn, "
        "no structures anywhere",
        "ships, settlements, natives, flags",
        wide=True, era="america-1820")),
    ("p12", "s2", _p(
        "Wise men raised up: close on a candlelit signing table — "
        "one aged hand steadying the great parchment while "
        "another dips a quill, more hands and lace cuffs waiting "
        "around the paper's edge, sealing-wax and sand-caster "
        "ready — the document's script aged and completely "
        "unreadable. A founding, seen at the distance of "
        "reverence.",
        "hands and quills around a great unreadable parchment by "
        "candlelight, wax and sand-caster ready",
        "readable words, faces, flags, maps",
        era="america-1820")),
    ("p13", "n8", _p(
        "Conscience, legalized: along a rutted valley road at "
        "morning, THREE small differing chapels stand within a "
        "mile of each other — white clapboard steeple, plain "
        "stone meetinghouse, log chapel — each with its own "
        "trickle of wagon-and-foot families arriving, nobody "
        "stopping anybody. Choice, written into a landscape.",
        "three differing small chapels along one road, each with "
        "its own arriving families, peaceable",
        "signage readable, conflict, cities",
        era="america-1820", wide=True)),
    ("p14", "n9", _p(
        "The convergence: inside a farmhouse at dusk — a thick "
        "family Bible open on the table by the window candle, and "
        "THROUGH the window glass, perfectly framed, the wooded "
        "drumlin hill standing dark against the last light. The "
        "book and the buried book, one windowpane apart. No "
        "people.",
        "an open family Bible by a farmhouse window with the "
        "drumlin hill framed in the glass beyond",
        "readable text, people, lamps electric",
        era="america-1820")),
    ("p15", ("n9", 0.6), _p(
        "As if by chance: a heaped farm wagon halts at that "
        "farmhouse in the dusk — a large family climbing down, "
        "father steadying the team, boys hauling a trunk, a "
        "mother lifting a lantern toward the dark doorway — all "
        "seen from behind at the gate. A family, arriving at an "
        "address heaven picked.",
        "a large family from behind unloading a heaped wagon at "
        "the dusk farmhouse, lantern lifting",
        "faces, the hill in this frame, neighbors",
        era="america-1820", wide=True)),
    ("p16", "n11", _p(
        "Candles and the coming sun: inside a dark chapel, a "
        "rack of small candles burns faithful in the gloom — and "
        "through the window above them, the first GREY of dawn "
        "has begun, not yet stronger than the flames, but "
        "arriving. Both lights true; only one is a sunrise.",
        "a rack of faithful candles in chapel gloom with first "
        "dawn grey arriving in the window above",
        "people, drawn rays, electric light",
        )),
    ("p17", ("n11", 0.55), _p(
        "Keys come from above: the pre-dawn sky over a dark "
        "hardwood treeline — the stars thinning, the east "
        "banded with the first watercolor of morning, the grove "
        "itself still a black fringe below holding tomorrow "
        "inside it. Minutes, now. No people.",
        "pre-dawn sky banding with first light over a black "
        "grove treeline",
        "figures, the sun risen, drawn rays",
        era="america-1820", wide=True)),
    ("p18", ("n11", 0.7), _p(
        "The payoff: the single candle from the opening frame — "
        "still burning, but now drowned in FULL SUNRISE flooding "
        "past it through a window, its little flame gone almost "
        "invisible inside the greater light it waited for. "
        "Nothing else in frame.",
        "the lone candle's flame nearly invisible inside "
        "flooding sunrise light",
        "hands, smoke, text",
        )),
]
