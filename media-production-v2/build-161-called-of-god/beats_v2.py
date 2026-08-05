#!/usr/bin/env python3
"""V2 beat map — row 161, build-161-called-of-god (Hebrews 5:1-5).

COVERAGE: 24 pictures over 145.8 s = 6.1 s/picture (matches the library density).

OPEN CAMERON COMPLAINT (MUST BE FIXED — this row was rejected over it):
  "At 1:30 aaron went grey and the anointing oil was poured over his
  hat and that is all wrong this picture needs to be redone."
  Two absolute gates, both at the anointing (b16, ~86-92 s):
  1. AARON NEVER GOES GREY — his hair and beard are BLACK in every
     frame of the build, identical first frame to last. Face-board
     him hardest at b16.
  2. The oil is poured on his BARE, BOWED HEAD — he wears NO mitre,
     cap or head-covering in the ordination beats (b13-b17). Oil on
     any hat/mitre = automatic reject.

SCRIPTURE FACTS (Hebrews 5 KJV):
  5:1  "every high priest taken from among men is ordained for men
       ... that he may offer both gifts and sacrifices for sins"
  5:2  "who can have compassion... for that he himself also is
       compassed with infirmity"
  5:4  "And no man taketh this honour unto himself, but he that is
       called of God, as was Aaron."
  5:5  "So also Christ glorified not himself to be made an high
       priest; but he that said unto him, Thou art my Son..."
  Ordination background (Lev 8): Moses brought Aaron before the
  assembly, laid on hands, poured the anointing oil on his head.

ROW INTENT: the authority-is-given row (BRIDGE/RESTORATION-adjacent,
kept strictly in the Bible's own frame) — the office is never
self-taken; it comes by a real call and hands laid on a bowed head;
even Christ received rather than seized. The close asks where God
might be calling the viewer.

RENDERING LAWS:
  - RECEIVING-HANDS GRAMMAR runs the row: open palms, bowed heads,
    honour coming DOWN — never grasping, never self-crowning. b09
    and b21 are the paired open-hands inserts (man's, then
    Christ's).
  - GOD / THE FATHER IS NEVER EMBODIED: gv5's "Thou art my Son"
    lands on Jesus's lifted face in warm light from above frame —
    NO figure, NO dove, NO visualized voice, NO glow outlining him.
  - THE GENERIC HIGH PRIEST (b01-b07) is one man — the epistle's
    "every high priest" — NOT Aaron and NOT grey-gated; he wears
    the office's blue robe and jewelled breastplate. Aaron appears
    only from b10 on, in plain pre-consecration dove-grey wool.
  - MOSES is rows 67/105's Moses byte-identical — grey-white beard
    IS correct on him (the complaint's grey gate is AARON's alone).
  - The people's offerings and failings are dignified — the
    struggling man at b06 is met with gentleness, never shamed.
  - No modern objects; the tabernacle is the wilderness court —
    woven hangings, acacia posts, the bronze altar; never Herod's
    stone temple.

TIME OF DAY ARC (intentional): the tabernacle frames in clear warm
morning; the ordination sequence in strengthening midday sun (a
public daylight act); the Christ beats in quiet silver dawn on the
hill; the close in soft morning light.

CHANGING CONDITIONS (kept OUT of the locks): Aaron — among the
people, brought forward, bowed under hands, anointed, consecrated;
the oil — horn held, poured, running down.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "AARON": (
        "AARON LOCK: Aaron is the same man in every shot — a sturdy "
        "Levite of about fifty: thick BLACK shoulder-length hair "
        "and a full BLACK beard with NO grey hair anywhere, in any "
        "frame, ever — he never ages, greys or whitens between "
        "frames; warm deep-set dark eyes, a humble weathered face; "
        "a plain undyed DOVE-GREY wool tunic with a dark olive sash "
        "(never cream); BARE-HEADED in every ordination frame — no "
        "mitre, cap or head-covering."
    ),
    "MOSES": (
        "MOSES LOCK: Moses is the same man in every shot — about "
        "eighty and still powerful, a long grey-white beard, deep-"
        "lined weathered face, in a DARK MADDER-RED robe over a "
        "CHARCOAL tunic with a rough staff (never cream, never "
        "white); the bearing of a man at ease with holy ground."
    ),
    "PRIEST": (
        "PRIEST LOCK: the epistle's high priest is the same man in "
        "every shot — a grave Levite of about sixty, short iron-"
        "grey beard, kind tired eyes; over his linen he wears the "
        "office: a SKY-BLUE woven robe, the gold-threaded ephod, "
        "and the square jewelled breastplate with its twelve "
        "stones (never cream). He is NOT Aaron and appears only in "
        "the epistle frames."
    ),
    "TABERNACLE": (
        "TABERNACLE LOCK: the wilderness tabernacle court — woven "
        "linen hangings on acacia posts around a sand court, the "
        "bronze altar with its grate at the centre, the curtained "
        "tent itself beyond; clear desert light. The same court "
        "throughout — never a stone temple."
    ),
    "PEOPLE": (
        "PEOPLE LOCK: the assembly of Israel — men, women and "
        "children of the wilderness camp in earth-toned robes of "
        "brown, rust, olive and slate (no cream — only Jesus wears "
        "cream); distinct faces, all ages, dignified, never "
        "twinned, never uniform."
    ),
    "QUIET-HILL": (
        "QUIET-HILL LOCK: a bare quiet hilltop apart — worn rock "
        "and thin grass under a wide silver-dawn sky, empty "
        "horizons; stillness itself. The same hilltop in every "
        "hill frame."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r161-b01", "out": "s01-in-ancient-israel-one-man.jpeg", "seg": "n1",
        "window": "0.28-3.61", "wide": True, "jesus": False, "ref": False,
        "locks": ["PRIEST", "TABERNACLE", "PEOPLE"],
        "narration": "In ancient Israel, one man stood between the people and God.",
        "must_show": "the ONE wide — camera at the court's entry behind the gathered people's backs, their gazes travelling up the frame to the lone high priest standing between them and the bronze altar with the curtained tent beyond; the between-ness readable as geography.",
        "must_not_show": "no crowd inside the court — the people stay at the hangings' edge; the priest ALONE in the middle ground; God represented by nothing but the curtained tent.",
        "scene": (
            "One man's place in the world, drawn as a map: "
            "the camera stands at the court's entry with "
            "the people's backs nearest the lens, every "
            "gaze travelling away up the frame to where "
            "the high priest stands alone on the open "
            "sand — the gathered families behind him, the "
            "bronze altar and the curtained tent before "
            "him — one figure set bodily between the "
            "people and the holy place, which is the "
            "entire job, told in ground. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b02", "out": "s02-the-high-priest-carried-their.jpeg", "seg": "n1",
        "window": "3.61-9.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST", "TABERNACLE"],
        "narration": (
            "The high priest carried their gifts and their sins to the "
            "altar, and carried God's holiness back to them."
        ),
        "must_show": "the carrying — the priest mid-stride toward the bronze altar bearing the people's offering in both hands; the weight of what he carries readable in his careful hold.",
        "must_not_show": "no slaughter or blood detail — the offering borne with dignity; his direction TOWARD the altar exact.",
        "scene": (
            "The office is a walk made over and over: the "
            "high priest crosses the court's sand toward "
            "the bronze altar with the people's offering "
            "held in both careful hands — carrying what is "
            "theirs up to God, to carry what is God's "
            "back down to them — the blue robe and "
            "jewelled breastplate moving with the "
            "unhurried gravity of a man who makes this "
            "crossing for everyone he leaves behind him. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r161-b03", "out": "s03-it-was-the-most-sacred.jpeg", "seg": "n1",
        "window": "9.29-12.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST"],
        "narration": "It was the most sacred office a person could hold.",
        "must_show": "the office insert — close on the breastplate itself over the sky-blue robe: twelve set stones, gold thread, worn bindings; sacredness carried as craftsmanship and weight.",
        "must_not_show": "no sparkle effects or light rays off the stones — material truth only; script/engraving INDISTINCT.",
        "scene": (
            "What the office weighs is written on the "
            "chest that bears it: close on the square "
            "breastplate riding over the sky-blue robe — "
            "twelve stones in their gold settings, each a "
            "tribe, the gold thread dulled by handling "
            "and years, the shoulder-bindings worn where "
            "they are tied and retied — the most sacred "
            "trust a man could stand up under, made of "
            "cloth and stone and meaning. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b04", "out": "s04-for-every-high-priest-taken.jpeg", "seg": "kv1",
        "window": "13.19-21.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST", "TABERNACLE"],
        "narration": (
            "For every high priest taken from among men is ordained for men "
            "in things pertaining to God, that he may offer both gifts and "
            "sacrifices for sins."
        ),
        "must_show": "SCRIPTURE-EXACT: the offering — the priest at the bronze altar, arms lifted placing the gift on the grate, smoke rising thin into the desert sky; ordained-for-men at its work.",
        "must_not_show": "no gore; the smoke THIN and real, never a pillar of spectacle; his posture service, not performance.",
        "scene": (
            "The verse shows the job being done: at the "
            "bronze altar the high priest lifts the "
            "people's gift onto the grate, forearms bare "
            "to the work, a thin line of smoke leaning "
            "into the desert sky above the coals — gifts "
            "and sacrifices for sins, offered by a man "
            "taken from among the very men he offers "
            "for — the whole priesthood caught in one "
            "practiced, humble motion. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b05", "out": "s05-and-here-is-a-tender.jpeg", "seg": "n2",
        "window": "23.09-28.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST"],
        "narration": (
            "And here is a tender thing. The high priest was not a distant, "
            "perfect being."
        ),
        "must_show": "the human face — a close portrait of the priest with the breastplate soft-focused below: kind tired eyes, lined face, a man not a monument.",
        "must_not_show": "no idealizing — the tiredness and kindness BOTH present; nothing distant or marble about him.",
        "scene": (
            "Under the office, a face: close on the high "
            "priest with the jewelled weight of the "
            "breastplate falling soft below the frame's "
            "attention — deep-lined skin, an iron-grey "
            "beard, and eyes that are tired the way only "
            "kind men get tired — not a distant perfect "
            "being at all, but somebody's brother grown "
            "old carrying other people's burdens up to "
            "God. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r161-b06", "out": "s06-he-was-a-weak-man.jpeg", "seg": "n2",
        "window": "28.06-34.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST", "PEOPLE", "TABERNACLE"],
        "narration": (
            "He was a weak man himself, who knew his own failings, and so he "
            "could be gentle with everyone else's."
        ),
        "must_show": "the gentleness — a two-shot at the court's edge: a man bowed with shame holding out a small offering, and the priest receiving it with one hand while the other rests on the man's shoulder; compassion from shared weakness.",
        "must_not_show": "the ashamed man NEVER shamed further — met, not examined; both faces gentle; no onlookers gawking.",
        "scene": (
            "Weakness understanding weakness: at the "
            "court's edge a man holds out his small "
            "offering with his head down, shame folded "
            "into his shoulders — and the high priest "
            "receives it with one hand while the other "
            "settles on the man's shoulder, a touch with "
            "a lifetime of his own failings inside it — "
            "gentleness that is not a technique but a "
            "memory, one weak man being kind to another "
            "at the door of God. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b07", "out": "s07-he-was-one-of-the.jpeg", "seg": "n2",
        "window": "34.07-37.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST", "PEOPLE"],
        "narration": "He was one of the people, not above them.",
        "must_show": "the levelness — the priest standing IN the crowd at the hangings, shoulder to shoulder with ordinary families, same ground, same light; only the blue robe different.",
        "must_not_show": "no dais, no steps, no elevation — feet on the SAME sand; faces around him at his own eye-level.",
        "scene": (
            "Where he stands when the work is done: in "
            "among the people at the court's hangings, "
            "shoulder to shoulder with herdsmen and "
            "grandmothers and a child leaning on its "
            "father — the blue robe and breastplate the "
            "only difference between him and everyone "
            "touching elbows with him, his feet on the "
            "same sand, his eyes at their level — one of "
            "them, lifted from among them, never lifted "
            "above them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r161-b08", "out": "s08-but-an-office-that-holy.jpeg", "seg": "n3",
        "window": "37.65-46.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABERNACLE"],
        "narration": (
            "But an office that holy could not simply be claimed. However "
            "sincere a man was, however gifted, he could not reach out and "
            "take it for himself."
        ),
        "must_show": "the untakeable — the office's blue robe and breastplate laid out on a wooden stand in the court, and NO ONE near them; empty sand all around; holiness that cannot be reached for.",
        "must_not_show": "ABSOLUTE: no hand reaching, no figure approaching — the emptiness around the vestments IS the sentence.",
        "scene": (
            "What cannot be taken is shown untouched: on "
            "a plain wooden stand in the open court the "
            "office waits — the sky-blue robe hung "
            "straight, the jewelled breastplate resting "
            "against it, the gold thread quiet in the "
            "morning light — and around it, nothing but "
            "empty sand in every direction, no reaching "
            "hand, no approaching foot, no man however "
            "sincere or gifted anywhere near it: a holy "
            "thing that has never once been grabbed. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r161-b09", "out": "s09-you-cannot-hand-this-to.jpeg", "seg": "n3",
        "window": "46.97-50.84", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "You cannot hand this to yourself. It has to be given.",
        "must_show": "the receiving-hands insert — two empty open palms held out waiting, upturned, in warm light; nothing in them yet; the grammar of the whole row in one frame.",
        "must_not_show": "the hands EMPTY and OPEN — not grasping, not reaching upward to take; wrists relaxed; nothing descending yet.",
        "scene": (
            "The only posture the office answers to: two "
            "empty hands held open, palms up, in the warm "
            "morning light — a working man's hands, "
            "creased and ready, holding nothing at all — "
            "not reaching, not closing, just waiting the "
            "way a man waits for what he cannot hand to "
            "himself — because some things arrive only "
            "into openness, and this is what openness "
            "looks like. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r161-b10", "out": "s10-and-no-man-taketh-this.jpeg", "seg": "kv4",
        "window": "51.41-56.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON", "MOSES", "PEOPLE", "TABERNACLE"],
        "narration": (
            "And no man taketh this honour unto himself, but he that is "
            "called of God, as was Aaron."
        ),
        "must_show": "SCRIPTURE-EXACT: the call — Moses turned toward the assembly with his arm extended toward AARON among the people; Aaron's black-haired, black-bearded face caught looking up, summoned; the people making way.",
        "must_not_show": "AARON GATE: black hair and beard, NO grey, BARE head; Aaron does not step forward proudly — he is FOUND, called out of the crowd.",
        "scene": (
            "The verse arrives as a pointing arm: Moses "
            "stands before the assembly in his madder-red "
            "robe with one arm extended, not to the "
            "eager or the impressive but into the middle "
            "of the crowd — to Aaron, black-bearded, "
            "bare-headed, dove-grey among the earth "
            "tones, whose face has just lifted with the "
            "look of a man hearing his own name where he "
            "expected someone else's — called, as the "
            "people ripple quietly apart around him. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r161-b11", "out": "s11-think-of-how-aaron-became.jpeg", "seg": "n4",
        "window": "57.95-62.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON", "PEOPLE"],
        "narration": (
            "Think of how Aaron became high priest. He did not campaign for "
            "it or seize it."
        ),
        "must_show": "the unassuming man — Aaron still standing IN the crowd, hands quiet at his sides, neighbours turning to look at him; no self-promotion in his whole body.",
        "must_not_show": "AARON GATE: black hair/beard, no grey, bare head; his hands NEVER raised or reaching — quiet at his sides.",
        "scene": (
            "The man the call found was not campaigning: "
            "Aaron stands where he has always stood, in "
            "among his neighbours, hands hanging quiet at "
            "his sides, dove-grey wool unremarkable in "
            "the crowd's browns and olives — the faces "
            "around him turning toward him one by one "
            "while his own stays open and astonished — a "
            "man who reached for nothing, being reached "
            "for. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r161-b12", "out": "s12-god-named-him-and-moses.jpeg", "seg": "n4",
        "window": "62.76-67.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON", "MOSES", "PEOPLE", "TABERNACLE"],
        "narration": (
            "God named him, and Moses brought him before the people and set "
            "him apart."
        ),
        "must_show": "the bringing — Moses leading Aaron by the arm out of the crowd toward the court's open centre, the assembly watching; Aaron led, not striding.",
        "must_not_show": "AARON GATE: black hair/beard, no grey, bare head; GOD NEVER EMBODIED — the naming is carried by Moses's act; Aaron half a step BEHIND Moses's lead.",
        "scene": (
            "Set apart is a short walk in front of "
            "everyone: Moses's weathered hand closes "
            "gentle and certain around Aaron's forearm "
            "and draws him out of the crowd's edge into "
            "the open centre of the court — Aaron coming "
            "half a step behind, led where he would "
            "never have walked himself, the assembly's "
            "faces turning to follow the two of them — "
            "named by God, brought by Moses, and every "
            "eye watching the honour arrive from outside "
            "the man it lands on. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b13", "out": "s13-the-honour-came-down-to.jpeg", "seg": "n4",
        "window": "67.67-71.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON"],
        "narration": "The honour came down to him; it was never something he grasped.",
        "must_show": "the receiving posture — Aaron alone in frame, head BOWING, bare-headed, hands open at his sides palms forward; the grammar of coming-down met with openness.",
        "must_not_show": "AARON GATE: black hair/beard, no grey, BARE bowed head; hands OPEN and low — nothing grasped, nothing reached for.",
        "scene": (
            "How a man stands under an arriving honour: "
            "Aaron alone in the frame with his bare black-"
            "haired head just beginning to bow, his hands "
            "open at his sides with the palms turned "
            "slightly forward — the posture of a man "
            "letting something be lowered onto him rather "
            "than climbing up after it — grasping nothing, "
            "deserving nothing he would claim, receiving "
            "everything. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r161-b14", "out": "s14-and-notice-how-it-was.jpeg", "seg": "n5",
        "window": "72.50-80.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON", "MOSES", "TABERNACLE"],
        "narration": (
            "And notice how it was done. Not with a ceremony he arranged for "
            "himself, but with another man's hands laid on his head, "
            "ordaining him."
        ),
        "must_show": "the ordination — Moses's two hands laid flat on Aaron's bowed BARE head, Aaron kneeling or deeply bowed before him in the court; the central image of the row.",
        "must_not_show": "AARON GATE: black hair/beard under the hands, NO grey, NO head-covering of any kind; BOTH of Moses's hands on the head — the contact exact and complete.",
        "scene": (
            "The way authority actually moves: Aaron "
            "kneels bowed in the open court and Moses "
            "stands over him with both weathered hands "
            "laid flat on the bare black hair of his "
            "head — not hovering, LAID, the full warm "
            "weight of them — an ordination no man "
            "arranges for himself, done in daylight in "
            "front of the assembly by hands that already "
            "carry what they are giving. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b15", "out": "s15-the-authority-passed-by-touch.jpeg", "seg": "n5",
        "window": "80.47-85.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON", "MOSES"],
        "narration": (
            "The authority passed by touch and blessing, from someone who "
            "already held it."
        ),
        "must_show": "the passing insert — close on Moses's aged hands resting on Aaron's bowed black-haired head: two generations of skin, the touch itself the conduit; nothing else in frame.",
        "must_not_show": "AARON GATE: black hair, no grey, bare head; NO light-effects at the hands — the TOUCH is the whole picture.",
        "scene": (
            "Close enough to see what passes: Moses's "
            "hands, eighty years old and steady, resting "
            "with their whole gentle weight on the bowed "
            "black hair of a younger man's bare head — "
            "aged skin over dark hair, blessing moving "
            "the only way it has ever moved, by touch, "
            "from a man who holds it to a man who "
            "receives it — no spark, no wonder-light, "
            "just hands, which is the entire miracle. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r161-b16", "out": "s16-then-the-holy-oil-was.jpeg", "seg": "n6",
        "window": "86.03-92.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON", "MOSES", "TABERNACLE"],
        "narration": (
            "Then the holy oil was poured over him, running down, and Aaron "
            "was consecrated, set apart, given."
        ),
        "must_show": "THE COMPLAINT BEAT — the anointing done RIGHT: Moses pouring the oil from a small horn directly onto Aaron's BARE, BOWED, BLACK-HAIRED head, the oil visibly running down through his black hair into his BLACK beard; NO mitre, cap or covering anywhere.",
        "must_not_show": "ABSOLUTE CAMERON GATES: (1) Aaron's hair and beard BLACK — one grey hair fails the frame; (2) NO hat/mitre/covering on or near his head — oil onto BARE hair only; oil physics real — running down, not splashing.",
        "scene": (
            "The oil goes where the call went, onto the "
            "man himself: Moses tips the small anointing "
            "horn and the holy oil comes down in a thin "
            "bright line onto the bare crown of Aaron's "
            "bowed head — onto black hair, nothing "
            "between — and runs the way oil runs, down "
            "through the hair, along the temple, into "
            "the full black beard, tracing the whole "
            "shape of the man being consecrated — set "
            "apart, soaked in the giving, made high "
            "priest by what is poured and not by what is "
            "grasped. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r161-b17", "out": "s17-everything-about-that-day-says.jpeg", "seg": "n6",
        "window": "92.37-97.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["AARON", "PEOPLE", "TABERNACLE"],
        "narration": (
            "Everything about that day says the same thing: this was "
            "received, not taken."
        ),
        "must_show": "the consecrated man — Aaron risen, bare-headed, oil still darkening his black hair and beard, hands open, face humbled and lit with the weight of it; the assembly soft behind.",
        "must_not_show": "AARON GATE: black hair/beard (oil-darkened, never grey-lightened), bare head; no triumph in his face — received-ness; hands still OPEN.",
        "scene": (
            "What a given man looks like: Aaron stands "
            "risen in the court with the oil still "
            "darkening his black hair and running its "
            "slow lines into his beard, bare-headed under "
            "the desert sky, hands open at his sides the "
            "way they were when it all came down — and "
            "his face carries no victory at all, only the "
            "humbled brightness of a man who has just "
            "been handed something he knows he could "
            "never have taken — received, from first "
            "word to last drop. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b18", "out": "s18-so-also-christ-glorified-not.jpeg", "seg": "kv5",
        "window": "98.37-103.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["QUIET-HILL"],
        "narration": (
            "So also Christ glorified not himself to be made an high priest; "
            "but he that said unto him,"
        ),
        "must_show": "SCRIPTURE-EXACT: the greater Aaron — Jesus kneeling on the quiet dawn hilltop, head bowed, hands open on his knees; the same receiving grammar as b13, now his.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO Father figure, NO dove; his posture RECEIVING — bowed and open, never self-exalting.",
        "scene": (
            "The pattern climbs to its highest case: on "
            "the bare hilltop in the silver dawn Jesus "
            "kneels with his head bowed and his hands "
            "open on his knees — the exact posture the "
            "bare-headed Levite held under Moses's "
            "hands — glorifying himself not at all, "
            "arranging nothing, waiting in the stillness "
            "of a Son who will take no honour his Father "
            "does not give. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b19", "out": "s19-thou-art-my-son-today.jpeg", "seg": "gv5",
        "window": "105.58-108.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["QUIET-HILL"],
        "narration": "Thou art my Son, today have I begotten thee.",
        "must_show": "SCRIPTURE-EXACT: the Father's word — Jesus's face lifting on the dawn hill as warm morning light strengthens from above the frame; the words land on the listening face; FATHER NEVER EMBODIED.",
        "must_not_show": "ABSOLUTE: no figure, no dove, no visualized voice, no light-beam outlining him — strengthening natural dawn light and his lifted listening face carry everything.",
        "scene": (
            "The voice that gives the office: Jesus's "
            "bowed face lifts on the quiet hilltop as the "
            "dawn strengthens — warm morning light "
            "arriving over the whole hill at once, on the "
            "rock and the thin grass and the lifted "
            "listening face alike — Thou art my Son — "
            "nothing visible speaking, nothing needed, "
            "the words landing where they were always "
            "going to land, on the one who waited to be "
            "given what was his. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b20", "out": "s20-even-the-lord-himself-did.jpeg", "seg": "n7",
        "window": "110.36-118.37", "wide": False, "jesus": True, "ref": REF,
        "locks": ["QUIET-HILL"],
        "narration": (
            "And this is the astonishing part. Even the Lord himself did not "
            "make himself a high priest. The Father gave him the office and "
            "called him to it."
        ),
        "must_show": "the astonishment stated calm — Jesus risen to his feet on the dawn hill, head still slightly bowed, hands open at his sides (the b13 rhyme exactly); given, not self-made.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no crown, no priestly vestments on him — the office is carried in posture, not costume.",
        "scene": (
            "The astonishing part stands quietly in the "
            "morning: Jesus on his feet now on the "
            "hilltop, the dawn full around him, his head "
            "still carrying a little of its bow and his "
            "hands open at his sides — the same open-"
            "handed stance the anointed Levite held in "
            "the tabernacle court — the Lord of all of "
            "it, and even he did not reach: the Father "
            "gave, the Son received, and the office came "
            "down the way it always comes. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b21", "out": "s21-if-the-son-of-god.jpeg", "seg": "n7",
        "window": "118.37-125.36", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "If the Son of God received his authority instead of seizing "
            "it, then no one else gets to appoint themselves either."
        ),
        "must_show": "the paired insert — close on Jesus's two open hands held palms-up in the dawn light (the b09 rhyme, now his hands); empty, open, receiving; the argument sealed in an image.",
        "must_not_show": "no wounds shown (this is pre-cross doctrine imagery, hands only); hands OPEN and empty — never closing, never grasping.",
        "scene": (
            "The whole argument fits in two open hands: "
            "close on Jesus's palms held upward in the "
            "strengthening morning light — workman's "
            "hands, open and empty, asking nothing, "
            "seizing nothing — the same waiting openness "
            "an ordinary man once held out in a desert "
            "court — and if these hands would not "
            "appoint themselves, the question of anyone "
            "else doing it is already answered. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r161-b22", "out": "s22-and-that-is-the-quiet.jpeg", "seg": "n8",
        "window": "125.90-136.06", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And that is the quiet good news in this verse. The right to "
            "speak and act for God has always come the same way: a real "
            "call, and hands laid on a bowed head."
        ),
        "must_show": "the always-pattern — a timeless period frame: an older man's hands laid on a younger man's bowed bare head in soft light; the b14 composition distilled to its universal shape; faces soft, unparticular.",
        "must_not_show": "no modern clothing or setting — timeless period simplicity; the bowed head BARE; the same way, always.",
        "scene": (
            "The pattern, timeless: in a plain warm-lit "
            "space an older man stands with both hands "
            "laid on the bowed bare head of a younger "
            "one — no court now, no crowd, just the "
            "shape itself, the one shape this giving has "
            "ever taken — a real call, and hands laid on "
            "a bowed head, the same way from the desert "
            "court to now, quiet as good news usually "
            "is. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r161-b23", "out": "s23-it-is-not-earned-by.jpeg", "seg": "n8",
        "window": "136.06-140.03", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It is not earned by being impressive. It is given.",
        "must_show": "the unimpressive insert — one ordinary bowed head in plain wool, close and soft-lit; no credentials anywhere in the frame; givenness resting on an ordinary man.",
        "must_not_show": "nothing impressive in frame — no fine cloth, no badge of office; ordinariness IS the picture.",
        "scene": (
            "What it does not take: one ordinary bowed "
            "head fills the soft-lit frame — plain rough "
            "wool at the shoulders, workaday hair, "
            "nothing anywhere on the man that would "
            "impress a committee — and that is the whole "
            "point of him: not earned by shine, not "
            "handed to the remarkable, given — which "
            "means an ordinary bowed head is always "
            "enough to receive it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r161-b24", "out": "s24-where-might-god-be-calling.jpeg", "seg": "n8",
        "window": "140.03-145.54", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So the only question left is a hopeful one. Where might God be "
            "calling you?"
        ),
        "must_show": "the closing invitation — a low wooden stool waiting empty in a plain room, morning light falling across it from a doorway; the place where a bowed head would be; offered to the viewer.",
        "must_not_show": "no figure — the empty waiting place carries the question; the light WARM and arriving (morning, not departing).",
        "scene": (
            "The last frame keeps a place ready: a low "
            "wooden stool stands empty in a plain quiet "
            "room, and through the open doorway the "
            "morning light comes in and lies across it — "
            "across the seat where a person would sit, "
            "where a head would bow, where hands could "
            "be laid — nothing happening yet, everything "
            "possible, the question standing in the "
            "light: where might God be calling you? "
            "Every figure has two arms, two hands and "
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
}
# === end PLACE-PLATES ===
