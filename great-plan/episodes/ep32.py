#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 32: Kingdoms of Glory.

The ending worthy of the Father: organized missionaries beyond death,
every child safe in the highest heaven, the He-lives testimony of 1832,
kingdoms instead of an incinerator — and the most generous account of
God's justice ever revealed.
Anchors: D&C 138; D&C 137:10; D&C 76:22-23; 1 Cor 15:41; Article of
Faith 3.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 332
NUM = 32
SLUG = "kingdoms-of-glory"
TITLE = "Kingdoms of Glory"
META = "D&C 76 · 137 · 138"

SEGMENTS = [
    ("n1", NARRATOR,
     "Last question of the war: how does it end — for everyone? The "
     "billions who never heard. The babies. If God is who this film "
     "says He is, the ending has to be worthy of Him. It is."),
    ("n2", NARRATOR,
     "Start with where everyone goes first. Not heaven-or-hell — the "
     "spirit world, where the dead are TAUGHT. You have heard Peter say "
     "it twice in this series. In nineteen eighteen, a prophet was "
     "shown the machinery:"),
    ("s1", SCRIPTURE,
     "From among the righteous, he organized his forces and appointed "
     "messengers, clothed with power and authority, and commissioned "
     "them to go forth and carry the light of the gospel to them that "
     "were in darkness, even unto all the spirits of men."),
    ("n4", NARRATOR,
     "The children? You know the answer from episode eight. But hear "
     "the revelation that settled it forever:"),
    ("s2", SCRIPTURE,
     "And I also beheld that all children who die before they arrive at "
     "the years of accountability are saved in the celestial kingdom of "
     "heaven."),
    ("n5", NARRATOR,
     "All children. Highest heaven. No exceptions. If you have lost a "
     "little one — that is where they are. And that is who God is."),
    ("n6", NARRATOR,
     "Then the judgment itself. In eighteen thirty-two, the vision of "
     "the end was opened to Joseph Smith and Sidney Rigdon — and the "
     "first thing they wrote down was not thrones. It was Him:"),
    ("s3", SCRIPTURE,
     "And now, after the many testimonies which have been given of him, "
     "this is the testimony, last of all, which we give of him: That he "
     "lives! For we saw him, even on the right hand of God; and we "
     "heard the voice bearing record that he is the Only Begotten of "
     "the Father."),
    ("n7", NARRATOR,
     "He lives — we saw him. And then the vision opened the ending: "
     "kingdoms. Plural. Glory fitted to what every soul can receive. "
     "Paul had already told the Corinthians:"),
    ("s4", SCRIPTURE,
     "There is one glory of the sun, and another glory of the moon, and "
     "another glory of the stars: for one star differeth from another "
     "star in glory."),
    ("n8", NARRATOR,
     "Celestial. Terrestrial. Telestial. Sun, moon, and stars — and "
     "even the least is a glory that surpasses all understanding. The "
     "Father does not run an incinerator. He runs a homecoming."),
    ("n9", NARRATOR,
     "Is hell real? Yes — as anguish before judgment. Outer darkness "
     "waits only for the rare few who gain full knowledge and choose "
     "full rebellion anyway. For every other darkness there is a door "
     "out — and Christ holds it open to the last instant."),
    ("n10", NARRATOR,
     "Add up the ending. Every child, safe. Every never-reached soul, "
     "reached. Resurrection, free, for all. Kingdoms, not a furnace. "
     "Now say the article of faith with me:"),
    ("s5", SCRIPTURE,
     "We believe that through the Atonement of Christ, all mankind may "
     "be saved, by obedience to the laws and ordinances of the "
     "Gospel."),
    ("n11", NARRATOR,
     "All mankind may be saved. That is the most generous account of "
     "God's justice ever revealed — and the only ending that matches "
     "the Father you have watched: the one who wept with Enoch, and "
     "paid the whole bill in a garden. Vengeance was never the plan. "
     "Family was."),
]

CARD_SEG = ("card", NARRATOR,
            "Heaven is not a gated community. It is a Father losing as "
            "close to nobody as agency allows.")

CARD_TEXT = ("Vengeance was never the plan.\n"
             "Family was.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Thirty-Two — Kingdoms of Glory")

SPOKEN = {"Rigdon": "RIG dun", "Telestial": "tuh LESS chul"}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="modern")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The question, at scale: an old churchyard at first light — "
        "generations of leaning headstones running away down the "
        "slope into morning mist, every inscription weathered past "
        "reading, dew silvering the grass between them. Everyone who "
        "ever wondered how it ends. No people.",
        "generations of unreadable leaning headstones running into "
        "morning mist",
        "readable names or dates, mourners, gloom styling",
        wide=True)),
    ("p02", "s1", _p(
        "The mission field beyond: the vast calm grey-white assembly "
        "from the flood episode — but ORGANIZED now: among the "
        "numberless listeners, many bright-clothed messengers move "
        "and teach, one at the center of each gathered cluster, "
        "light pooling wherever they stand — a mission, at the scale "
        "of the dead. Seen from high behind the crowds.",
        "the vast spirit assembly now clustered around many bright "
        "teaching messengers, light pooling at each",
        "wings, halos, gloom, faces to camera",
        era="heaven", wide=True)),
    ("p03", ("s1", 0.5), _p(
        "One at a time, there too: a bright-clothed messenger grips "
        "the shoulder of a rough-dressed listening man whose face is "
        "breaking — disbelief becoming hope in real time — the two "
        "of them in profile, the crowd soft beyond. The gospel doing "
        "on that side exactly what it does on this one.",
        "a messenger's hand on a rough-dressed man's shoulder, his "
        "face breaking from disbelief into hope, profiles",
        "wings, tears streaming, faces to camera",
        era="heaven")),
    ("p04", ("s1", 0.78), _p(
        "The machinery, this side: the temple font's bright water "
        "from just above its surface — one ring of ripples widening "
        "from a center the frame does not show, the twelve oxen's "
        "backs soft beneath, white light everywhere. One name, just "
        "served. No people in frame.",
        "one widening ripple-ring on bright font water over soft "
        "oxen backs",
        "swimmers, splashing, faces",
        )),
    ("p05", "s2", _p(
        "All children: a bright orchard in full morning — a dozen "
        "small children mid-game among the blossoming trees, "
        "running, swinging on a low bough, two crouched over "
        "something wonderful in the grass — laughter readable in "
        "every small body, light warm and endless. Safe is a "
        "place, and it looks like this.",
        "a dozen small children mid-play in a blossoming bright "
        "orchard, laughter readable in the bodies",
        "adults, wings, halos, faces to camera",
        wide=True)),
    ("p06", "n5", _p(
        "For the ones who lost one: a young mother kneels at a "
        "small grave at dawn — and her face, lifted into the "
        "arriving light, is caught exactly at the turn: grief "
        "still wet on it, and hope physically entering, like "
        "warmth into cold hands. The smallest headstone stays "
        "unreadable; the light does the speaking.",
        "a young mother's lifted face at a small grave, grief "
        "turning to hope in arriving dawn light",
        "readable stone, despair alone, others",
        )),
    ("p07", "n6", _p(
        "The vision of the end: in a plain upper room, Joseph and "
        "another man sit struck motionless mid-vision — both faces "
        "lifted and lit by something the room's windows cannot "
        "explain, eyes open and fixed on the unseen, while around "
        "the walls a dozen witnesses watch the watchers in awe. "
        "Eighteen thirty-two, mid-revelation.",
        "two seated seers lit and struck mid-vision, a dozen "
        "witnesses watching the watchers",
        "the vision rendered in frame, halos, faces to camera",
        era="america-1820", locks=["JOSEPH-SMITH"])),
    ("p08", "s3", _p(
        "The testimony, last of all: the risen Jesus close — alive, "
        "warm, sovereign — his locked face in glory-light with the "
        "gladness of the Kirtland appearance, gaze angled past the "
        "camera's shoulder toward every witness who ever said THAT "
        "HE LIVES. The whole revelation's first fact, in one face.",
        "the risen Jesus's close warm sovereign face, gaze past "
        "the lens",
        "his eyes on the lens, halo, white hair, wounds",
        jesus=True, ref=True)),
    ("p09", "s4", _p(
        "Sun, moon and stars in one sky: dusk over open country — "
        "the setting sun still burning gold on the western horizon, "
        "the full moon already risen pale in the deepening east, "
        "and between them, high in the violet, the first three "
        "stars — all three glories sharing one honest sky. No "
        "people.",
        "setting sun, risen full moon and first stars sharing one "
        "dusk sky over open country",
        "planets labeled-looking, drawn rays, figures",
        wide=True)),
    ("p10", ("s4", 0.6), _p(
        "Reading the sky: a family stretched on a blanket on a "
        "hillside beneath that same dusk — parents and three kids "
        "in a row on their backs, one small arm pointing up, all "
        "faces to the heavens and away from the camera at the "
        "blanket's foot. The doctrine, stargazed.",
        "a family on their backs on a hillside blanket, one small "
        "arm pointing up at the dusk sky",
        "faces to camera, telescopes, city glow",
        )),
    ("p11", "n8", _p(
        "Even the least is glory: an utterly ordinary roadside "
        "meadow at golden hour rendered breathtaking — seed-heads "
        "blazing, insects drifting like sparks, one crooked fence "
        "post crowned in backlit grass — the 'least' of landscapes, "
        "surpassing understanding anyway. No people.",
        "an ordinary meadow at golden hour made breathtaking — "
        "blazing seed-heads, drifting spark-like insects",
        "figures, buildings, drawn rays",
        )),
    ("p12", ("n8", 0.6), _p(
        "Placement, mercy-shaped: at dusk a shepherd sorts his "
        "flock through gates into two hurdle-folds — and he does "
        "it CARRYING the lame ewe against his chest while his "
        "free hand guides the others through, every animal "
        "handled toward shelter, none driven. Judgment, the way "
        "this Father does it.",
        "a shepherd sorting sheep into folds at dusk while "
        "carrying the lame ewe against his chest",
        "whips, dogs snarling, culling implications",
        era="ancient")),
    ("p13", "n9", _p(
        "Held open to the last: full night on an empty moor — and "
        "one doorway of warm light standing open in a dark "
        "farmhouse wall, the lamp inside throwing a long gold "
        "path across the grass toward the frame's dark edge, the "
        "threshold empty, the door wedged wide. Nobody is made "
        "to walk in. Nobody is locked out.",
        "one warm open doorway throwing a long gold path across "
        "night grass, threshold empty, door wedged wide",
        "figures, storm, bolts or chains",
        )),
    ("p14", "n10", _p(
        "The ending, set: a single immensely LONG farm table at "
        "dawn light stretching away down an orchard row — dozens "
        "of mismatched chairs, places laid, lamps still burning "
        "down its length, steam rising from somewhere near — "
        "seats for absolutely everyone who will come. Not one "
        "chair leaned against the table's edge.",
        "one immensely long laid table with mismatched chairs "
        "stretching down a dawn orchard row",
        "guests seated yet, name cards readable, gates",
        wide=True)),
    ("p15", "s5", _p(
        "The family creed: a child's small hand and a "
        "grandfather's spotted one hold OPEN the same small thick "
        "book between them — two generations, one page, morning "
        "window light across the unreadable print and the four "
        "thumbs. All mankind, may be saved.",
        "a child's hand and a grandfather's holding one small "
        "open book together in window light",
        "readable text, faces, jewellery",
        )),
    ("p16", "n11", _p(
        "The Father the ending matches: His close face once more — "
        "the tears of the Enoch episode long dried, the sorrow "
        "kept but transfigured, the beginnings of a smile deep in "
        "the silver beard, warm light full on the features that "
        "wept over the chain. A Father at the end of a very long "
        "plan, watching it come home.",
        "the Father's close warm face, old sorrow transfigured, a "
        "beginning smile deep in the beard",
        "His eyes on the lens, tears now, halo",
        era="heaven", locks=["FATHER"])),
    ("p17", ("n11", 0.6), _p(
        "First arrivals: the long dawn table again — and now, far "
        "down the orchard row, the first family walking in toward "
        "it from behind, a child skipping ahead of the parents "
        "toward the lamps and the steam and the endless laid "
        "places. The homecoming, beginning. ",
        "the first family from behind approaching the long laid "
        "dawn table, child skipping ahead",
        "faces, crowds yet, gates",
        wide=True)),
]
