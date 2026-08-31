#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 27: The Book Rises.

The seed wakes: Moroni — the same man who buried the plates — sent back
for them; four years of schooling; translation by gift and power; the
witnesses; and five thousand copies off a Palmyra press.
Anchors: JS—History 1:30-34; Book of Mormon title page; 2 Nephi 29:10.

Casting payoff: the angel Moroni wears MORONI-GP's exact face from episode
24, now glorified — heaven does not lose track of its librarians.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 327
NUM = 27
SLUG = "book-rises"
TITLE = "The Book Rises"
META = "JS—History 1 · 2 Nephi 29"

SEGMENTS = [
    ("n1", NARRATOR,
     "Three years after the grove, the seed in the hill got its wake-up "
     "call. This is the night the buried book rose."),
    ("n2", NARRATOR,
     "September, eighteen twenty-three. Joseph — seventeen now — praying "
     "late at night for forgiveness and direction. And light grew in his "
     "little room until it outshone noon — and a person stood in the air "
     "above the floor."),
    ("s1", SCRIPTURE,
     "He called me by name, and said unto me that he was a messenger "
     "sent from the presence of God to me, and that his name was "
     "Moroni."),
    ("n3", NARRATOR,
     "Moroni. The same man who buried the plates fourteen centuries "
     "earlier — sent back for them. Heaven does not lose track of its "
     "librarians. The last man of the fallen nation became the first "
     "messenger of the Restoration."),
    ("s2", SCRIPTURE,
     "He said there was a book deposited, written upon gold plates, "
     "giving an account of the former inhabitants of this continent, and "
     "the source from whence they sprang. He also said that the fulness "
     "of the everlasting Gospel was contained in it, as delivered by the "
     "Savior to the ancient inhabitants."),
    ("n5", NARRATOR,
     "Four years of schooling followed — Moroni returning each "
     "September, the boy maturing into a man — until eighteen twenty-"
     "seven, when the plates were finally placed in Joseph's hands, "
     "with a charge to guard them with his life."),
    ("n6", NARRATOR,
     "Then, translation — by the gift and power of God. An unschooled "
     "farmhand, dictating hour after hour: five hundred and thirty-one "
     "printed pages in roughly sixty-five working days. Scholars still "
     "cannot explain the pace — and the manuscript shows almost no "
     "revision."),
    ("n7", NARRATOR,
     "And what came off those plates answers the famine point by point. "
     "The plain and precious things — back. The covenants — back. Its "
     "own title page states the whole mission:"),
    ("s3", SCRIPTURE,
     "To the convincing of the Jew and Gentile that Jesus is the "
     "Christ, the Eternal God, manifesting himself unto all nations."),
    ("n8", NARRATOR,
     "Some said then — and some still say — we already have a Bible; we "
     "need no more. God had answered that objection twenty-four "
     "centuries before anyone raised it:"),
    ("j1", JESUS,
     "Wherefore, because that ye have a Bible ye need not suppose that "
     "it contains all my words; neither need ye suppose that I have not "
     "caused more to be written."),
    ("n9", NARRATOR,
     "Two witnesses. One God. The Book of Mormon does not replace the "
     "Bible — it stands beside it, and each testifies of the other. And "
     "eleven men beyond Joseph handled the plates, hefted them, turned "
     "their leaves — and signed their names to it for the rest of their "
     "lives. Several of them kept that testimony even after falling out "
     "with Joseph himself."),
    ("n10", NARRATOR,
     "The book went to press in Palmyra in eighteen thirty. Five "
     "thousand copies — a believing farmer's farm mortgaged to pay for "
     "them. The famine's answer, stacked and drying in a print shop."),
    ("n11", NARRATOR,
     "And the invitation printed in its final chapter is still the "
     "engine of everything: read it, remember how merciful the Lord has "
     "been — and ask God, in the name of Christ, if it is true. "
     "Millions have. You can. Moroni buried it for you. The least you "
     "can do is open it."),
]

CARD_SEG = ("card", NARRATOR,
            "Buried by the last survivor. Delivered back by the same "
            "man. Addressed to you.")

CARD_TEXT = ("The seed came up.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Seven — The Book Rises")

SPOKEN = {"Moroni": "moh ROH nigh", "Palmyra": "pal MY ruh"}

MORONI_GLORIFIED = (
    "MORONI GLORIFIED LOCK: the SAME face as the attached reference — "
    "the last Nephite of episode twenty-four — now a glorified "
    "resurrected messenger: the same deep bronze features, the same "
    "grey-shocked temples and short beard, the grief transfigured into "
    "blazing peace, wearing a loose robe of most exquisite whiteness, "
    "bare feet, standing in the air where the scene says so. No wings, "
    "no halo, no aura outline — the room's brilliance is environmental.")

JOSEPH_YM = (
    "JOSEPH LOCK (young man): the same face as the attached reference "
    "grown a few years older — seventeen to twenty-two: taller, broader, "
    "the same thick sandy light-brown hair and open fair sun-tanned "
    "face, same strong brow and light-coloured eyes, plain 1820s "
    "homespun. Never aged past his early twenties. No halo, no glow.")

LOCKS = {"MORONI-GP": MORONI_GLORIFIED, "JOSEPH-SMITH": JOSEPH_YM}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="america-1820")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The wake-up call: the wooded drumlin hill at first light — "
        "and this dawn is DIFFERENT: the sun's first rays breaking "
        "exactly over its crown, the mist on its slopes burning "
        "through, the whole hill lit like something switched on. The "
        "waiting, ending. No people.",
        "the drumlin hill with sunrise breaking exactly over its "
        "crown, mist burning through",
        "figures, paths, monuments, drawn rays hard-edged",
        wide=True)),
    ("p02", "n2", _p(
        "The praying boy: Joseph at seventeen kneels beside his low "
        "rope bed in a small log-walled bedroom at deep night — "
        "homespun shirt, bare feet on plank floor, head bowed over "
        "clasped hands, one candle long since out — earnest, "
        "private, and completely unaware of what is coming.",
        "seventeen-year-old Joseph kneeling at his rope bed in a "
        "dark log bedroom, candle out, earnest",
        "light arriving yet, his eyes on the lens, siblings",
        locks=["JOSEPH-SMITH"])),
    ("p03", ("n2", 0.55), _p(
        "The light grows: the little bedroom FILLING with brilliance "
        "brighter than noon — every plank and quilt-fold lit "
        "shadowless, and Joseph half-risen from his knees, one arm "
        "instinctively shielding then LOWERING as awe replaces "
        "alarm, his face washed in the impossible light whose "
        "source stands just above the frame's top edge.",
        "the log bedroom lit brighter than noon, Joseph half-risen "
        "with shielding arm lowering into awe",
        "the messenger in this frame, windows blazing, fire",
        locks=["JOSEPH-SMITH"])),
    ("p04", "s1", _p(
        "The librarian, sent back: the glorified messenger stands IN "
        "THE AIR of the small room, bare feet plainly above the "
        "plank floor — the SAME bronze face from the cave and the "
        "hill, grief transfigured to blazing peace, his exquisite "
        "white robe still in the brilliance — and below him Joseph "
        "looks up from beside the bed, lit and unafraid. Fourteen "
        "centuries, closing in one frame.",
        "the glorified messenger with Moroni's exact face standing "
        "in the air of the bedroom, Joseph looking up unafraid",
        "wings, halo, aura outline, feet on the floor, either "
        "face to the lens",
        locks=["MORONI-GP", "JOSEPH-SMITH"])),
    ("p05", ("s1", 0.6), _p(
        "My name is Moroni: the messenger's face close — the deep "
        "bronze features, the grey-shocked temples, the short beard "
        "of the man who once wrote alone by firelight — now lit "
        "from within by expression alone: the calm of finished "
        "grief, the warmth of a courier finally delivering. His "
        "gaze angles down toward the unseen boy.",
        "the glorified messenger's close face — the same features "
        "as the last Nephite, grief become blazing peace, gaze "
        "down toward the unseen boy",
        "halo, glow, wings, his eyes on the lens",
        locks=["MORONI-GP"])),
    ("p06", "s2", _p(
        "The telling: Moroni's arm extends toward the bedroom's "
        "small window — and Joseph's wide eyes follow the line of "
        "the pointing hand — the messenger describing gold plates "
        "and an everlasting gospel while the night outside the "
        "glass holds the direction of a hill the boy has known "
        "his whole life.",
        "Moroni's arm extended toward the small dark window, "
        "Joseph's eyes following the line",
        "the hill visible yet, plates in frame, faces to lens",
        locks=["MORONI-GP", "JOSEPH-SMITH"])),
    ("p07", ("s2", 0.6), _p(
        "The direction of the hill: through the small farmhouse "
        "window's wavy glass, the drumlin hill stands dark against "
        "the star-thick night — framed exactly by the panes, "
        "patient as ever, suddenly the most important geography "
        "on earth. No people; the view itself.",
        "the dark drumlin hill framed in wavy window-glass under "
        "thick stars",
        "light on the hill, figures, curtains fancy",
        )),
    ("p08", "n5", _p(
        "Four Septembers: on the hillside in autumn gold, the "
        "opened stone box sits between them — Moroni standing in "
        "quiet instruction, Joseph now visibly older kneeling at "
        "the box's edge listening hard, the plates' gleam just "
        "showing under the lifted lid — a tutorial with a "
        "fourteen-century syllabus. Seen from beside the box.",
        "Moroni instructing over the opened stone box while an "
        "older Joseph kneels listening, gleam under the lid",
        "wings, halo, plates fully out, faces to lens",
        locks=["MORONI-GP", "JOSEPH-SMITH"])),
    ("p09", ("n5", 0.6), _p(
        "1827 — placed in his hands: at dusk on the hill, the "
        "wrapped weight passes from the messenger's hands into "
        "Joseph's braced arms — the young man's face grave with "
        "the charge landing on him, Moroni's hands still steadying "
        "the bundle's underside at the moment of transfer. The "
        "handoff of the whole Restoration.",
        "the wrapped plates mid-transfer from Moroni's hands into "
        "Joseph's braced arms at dusk, both grave",
        "gold visible, wings, halo, faces to lens",
        locks=["MORONI-GP", "JOSEPH-SMITH"])),
    ("p10", "n6", _p(
        "Guard them with your life: Joseph at a dead RUN through "
        "darkening woods, the wrapped bundle clamped under one arm "
        "like a stone of great price, his free hand tearing "
        "branches aside, coat flying — hunted already, caught "
        "mid-stride from the side, fierce and fast.",
        "Joseph sprinting through dark woods with the wrapped "
        "bundle clamped under one arm",
        "attackers visible, blood, his face to the lens",
        locks=["JOSEPH-SMITH"])),
    ("p11", ("n6", 0.4), _p(
        "By gift and power: the translation table by candlelight — "
        "Joseph seated with his face buried toward the instrument "
        "cupped in his hat's dark, dictating, while across the "
        "plain table a scribe's quill races over paper, pages "
        "already stacked at his elbow — two farm chairs, one "
        "candle, and scripture arriving at speed. All writing "
        "soft and unreadable.",
        "Joseph dictating face-toward-hat while a scribe's quill "
        "races, pages stacked, one candle",
        "readable words, the plates open on the table, faces to "
        "lens",
        locks=["JOSEPH-SMITH"])),
    ("p12", ("n6", 0.75), _p(
        "The pace: extreme close on the scribe's quill flying "
        "across the page — ink still wet on the last three lines, "
        "a finished stack thick beside the inkwell, candle-warmth "
        "raking the paper's weave — sixty-five days outrunning "
        "every explanation. Script soft and unreadable.",
        "a racing quill, wet ink, and a thick finished stack by "
        "candlelight, unreadable",
        "readable words, blots, printed type",
        )),
    ("p13", "n7", _p(
        "The famine's answer, bound: rough work-hands hold the "
        "finished manuscript — a thick block of pages tied with "
        "cord — in morning window light, the paper edges soft "
        "with handling, the weight of it plainly real in the "
        "gripping fingers. Everything the centuries starved for, "
        "in one stack.",
        "work-hands holding a thick cord-tied manuscript block in "
        "window light",
        "readable text, printing, faces",
        )),
    ("p14", "s3", _p(
        "The mission statement: the book's first printed leaf "
        "lies fresh on the press-room table — its type-set lines "
        "soft and UNREADABLE in the raking light, but its "
        "purpose carried by the caption — a printer's stained "
        "thumb still holding the sheet's corner flat. The point "
        "of everything, going to ink.",
        "a fresh printed leaf with soft unreadable type held "
        "flat by a printer's stained thumb",
        "READABLE words or title, modern type, faces",
        )),
    ("p15", "j1", _p(
        "More witnesses, not fewer: two oil lamps burn side by "
        "side on one plain table — twin flames, one light — "
        "against the soft dark of a farmhouse wall. The Bible "
        "and the book beside it, told in fire. Nothing else in "
        "frame.",
        "two lamps burning side by side as one light on a plain "
        "table",
        "books in frame, hands, text",
        )),
    ("p16", "n9", _p(
        "The witnesses: around a farmhouse table in full "
        "daylight, eleven plain-dressed men lean in as the "
        "metal plates lie OPEN before them — one man lifting a "
        "leaf between his fingers, another hefting the whole "
        "weight with both hands and raised brows, a third "
        "tracing engraving with a fingertip — examination, not "
        "ceremony; farmers auditing gold. Faces on the plates, "
        "none to the lens.",
        "eleven daylight witnesses examining open metal plates — "
        "lifting a leaf, hefting the weight, tracing engraving",
        "angels in frame, readable characters, faces to lens",
        wide=True)),
    ("p17", "n10", _p(
        "Palmyra, 1830: the Grandin press-room in work-lamp "
        "warmth — the iron press mid-pull, and everywhere the "
        "BOOK: printed sheets drying on lines overhead, folded "
        "gatherings stacked waist-high, an apprentice carrying "
        "a fresh armload — five thousand copies of the famine's "
        "answer coming into the world. Type and pages "
        "unreadable.",
        "an 1830 press-room mid-pull with the book's sheets "
        "drying overhead and gatherings stacked waist-high",
        "readable pages, modern machinery, faces to lens",
        wide=True)),
    ("p18", "n11", _p(
        "Addressed to you: in the present day, two hands open "
        "the same thick book at a morning window — the spine "
        "cracking softly, pages fanning past the thumbs, warm "
        "light across the unreadable text — Moroni's letter, "
        "opening seventeen centuries after the firelight it was "
        "written by.",
        "modern hands opening the thick book at a bright morning "
        "window, pages fanning, print unreadable",
        "readable title or text, faces, brand marks",
        era="modern")),
    ("p19", ("n11", 0.7), _p(
        "The metronome resolves: the drumlin hill in FULL golden "
        "morning at last — every previous era saw it waiting in "
        "dusk, night and half-light, and now the whole crown "
        "stands lit, the young orchards below bright, the long "
        "patience paid. No people, no marks. Just morning, "
        "finally.",
        "the drumlin hill fully lit in golden morning, orchards "
        "bright below",
        "figures, monuments, mist, drawn rays",
        wide=True)),
]
