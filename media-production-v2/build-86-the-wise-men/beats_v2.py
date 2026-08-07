#!/usr/bin/env python3
"""V2 beat map — row 86, build-86-the-wise-men (Matthew 2:1-12).

COVERAGE: 22 pictures over 123.7 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 2:1-12 KJV):
  v1-2  "there came WISE MEN FROM THE EAST to Jerusalem, saying, Where
        is he that is born King of the Jews? for we have seen HIS STAR
        in the east, and are come to WORSHIP him." — scholars, a long
        journey, the question asked in Herod's own city.
  v3    "When Herod the king had heard these things, he was TROUBLED."
  v8    the lie: "Go and search diligently for the young child; and
        when ye have found him, bring me word again, that I may come
        and worship him also."
  v9    "the star... went before them, till it came and STOOD OVER
        where the young child was."
  v11   "when they were come into THE HOUSE, they saw the YOUNG CHILD
        with Mary his mother, and FELL DOWN, and worshipped him: and
        ...presented unto him gifts; GOLD, and FRANKINCENSE, and
        MYRRH." — a HOUSE, not the stable; a young child, not a
        newborn.
  v12   "being WARNED OF GOD IN A DREAM that they should not return to
        Herod, they departed into their own country ANOTHER WAY."

JESUS FLAG NOTE: the child is a YOUNG CHILD (a toddler) — the adult
JESUS LOCK/ref do not apply; all beats run jesus=False and the child
is painted per scene (dark-haired toddler, no halo). MARY lock matches
rows 84/85.

DREAM RENDERING (CONTENT-CARE): the v12 warning is shown as the
sleeping desert camp only — a sleeper stirring, resolve at dawn; NO
figure, voice or apparition depicted.

TIME OF DAY ARC (intentional): the star and journey beats at NIGHT;
Herod's hall in cold DAYLIGHT; the Bethlehem house in warm LATE
AFTERNOON into lamplit evening; the dream in deep night; the departure
at DAWN, another way. Correct story lighting, not the row-11 defect.

CHANGING CONDITION (kept OUT of the locks): the star — leading, then
standing still; the gifts — sealed in their chests, then opened; the
road — toward Jerusalem, then Bethlehem, then home another way.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream (and the adult Jesus does not appear in this row).
LOCKS = {
    "MAGI": (
        "MAGI LOCK: the wise men are the same three scholars in every "
        "shot — an old white-bearded Persian in DEEP SAPPHIRE-BLUE "
        "robes, a middle-aged dark-skinned scholar in DARK CRIMSON, "
        "and a younger black-bearded one in DEEP EMERALD-GREEN (never "
        "cream, never white); rich but road-worn travel robes, dusty "
        "hems, learned faces."
    ),
    "HEROD": (
        "HEROD LOCK: Herod is the same man in every shot — old and "
        "heavy, a grey-streaked beard, shrewd sunken eyes, in DARK "
        "PURPLE and gold-worked robes with a thin gold circlet (never "
        "cream, never white); fear kept behind a courtier's smile."
    ),
    "HALL": (
        "HALL LOCK: Herod's audience hall — polished dark stone "
        "columns, a raised throne platform, braziers, guards in dark "
        "iron at the walls; cold grand daylight from high windows. "
        "The same hall throughout."
    ),
    "HOUSE": (
        "HOUSE LOCK: the Bethlehem house — a small one-room village "
        "home: packed-earth floor, rough plastered walls, a low "
        "doorway, one small window, a clay lamp in a niche. The same "
        "little room throughout."
    ),
    "MARY": (
        "MARY LOCK: Mary is the same young woman in every shot — "
        "about twenty, a gentle open face with warm brown eyes, dark "
        "hair under a DEEP INDIGO-BLUE veil, a plain DEEP INDIGO-BLUE "
        "dress (never cream, never white). Serene and dignified."
    ),
    "DESERT": (
        "DESERT LOCK: the eastern road — pale rolling desert and "
        "scrubland under an enormous sky, a small camel train with "
        "packs and travel chests, campfires at night. The same "
        "country and beasts throughout."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): the authoritative V1 mp4
# is 130.833s but the recomputed timeline is 132.046s (|Δ|=1.213s > 1.0, trailing-
# silence shortfall), so the packet-copy AUDIO LOCK refuses. Rebuild the track from
# this build's own 14 mp3 segments at the timeline offsets — nothing re-voiced, $0.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r086-b01", "out": "s01-some-time-after-jesus-was.jpeg", "seg": "n0",
        "window": "0.40-6.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["MAGI", "DESERT"],
        "narration": (
            "Some time after Jesus was born, travelers came from the east — "
            "scholars who had read the skies."
        ),
        "must_show": "SCRIPTURE-EXACT: the travellers — the three magi and their small camel train crossing the night desert, one brilliant star low ahead of them; scholars on a long road.",
        "must_not_show": "no halo, glare or rim-light on figures; the caravan SMALL in the vast night — three scholars, not a royal parade.",
        "scene": (
            "Across the pale night desert, the camera far off the "
            "track taking the train in profile under the stars, the "
            "small caravan makes its patient "
            "line: three robed scholars swaying "
            "on their camels — sapphire, crimson "
            "and emerald gone dusky in the "
            "starlight — pack-beasts and travel "
            "chests behind, and ahead of them, "
            "low and brilliant over the western "
            "ridge, the one star that reads "
            "differently from all the rest, "
            "pulling three learned lives across "
            "a continent by its light. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r086-b02", "out": "s02-they-had-seen-his-star.jpeg", "seg": "n0",
        "window": "6.33-14.61", "wide": True, "jesus": False, "ref": False,
        "locks": ["MAGI", "HALL"],
        "narration": (
            "They had seen his star, and followed it all the way to "
            "Jerusalem, where they walked into the king's hall and asked a "
            "dangerous question."
        ),
        "must_show": "the arrival at court — the three dusty travellers striding up Herod's cold grand hall between the columns and guards, road-dirt on rich robes; purpose in every step.",
        "must_not_show": "no halo, glare or rim-light; the hall's grandeur COLD against their travel-worn directness.",
        "scene": (
            "Into the cold polished grandeur, the camera behind the "
            "flanking courtiers' shoulders, of "
            "the king's hall the three come "
            "striding — desert dust still on "
            "their sapphire, crimson and emerald "
            "hems, the long road still in their "
            "gait — past braziers and dark-iron "
            "guards and courtiers turning to "
            "stare, three foreign scholars "
            "carrying one question up the middle "
            "of the most dangerous floor in "
            "Judea as if it weighed nothing at "
            "all. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r086-b03", "out": "s03-where-is-he-that-is.jpeg", "seg": "j1",
        "window": "16.29-18.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HALL"],
        "narration": "Where is he that is born King of the Jews?",
        "must_show": "SCRIPTURE-EXACT: the question — close on the old sapphire-robed magus asking it plainly before the throne platform; the words landing on the hall like a dropped blade.",
        "must_not_show": "no halo, glare or rim-light; the asking INNOCENT of court politics — a scholar's honest question in a snake pit.",
        "scene": (
            "Close on the old Persian's face as "
            "he asks it — white beard, learned "
            "calm, the question offered up to "
            "the throne platform as plainly as "
            "asking directions at a well — WHERE "
            "IS HE THAT IS BORN KING — and "
            "behind him the hall's air tightens: "
            "a courtier's cup pausing, a guard's "
            "eyes sliding sideways, the word "
            "BORN doing its quiet treason in a "
            "room owned by a king who wasn't. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r086-b04", "out": "s04-for-we-have-seen-his.jpeg", "seg": "j1",
        "window": "18.76-22.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HALL"],
        "narration": (
            "for we have seen his star in the east, and are come to worship "
            "him."
        ),
        "must_show": "SCRIPTURE-EXACT: the reason — the magi gesturing east toward the high windows, conviction on all three faces; COME TO WORSHIP stated in a king's hall.",
        "must_not_show": "no halo, glare or rim-light; the star NOT visible in the day hall — it lives in their pointing and their certainty.",
        "scene": (
            "The crimson-robed scholar's arm "
            "sweeps toward the high eastern "
            "windows — WE HAVE SEEN HIS STAR — "
            "and the three faces carry the whole "
            "journey in their certainty: months "
            "of desert read off a single point "
            "of light, ended here with the word "
            "WORSHIP said out loud, of someone "
            "else, in the hall of a man who has "
            "killed for less than a pronoun. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r086-b05", "out": "s05-understand-what-they-had-just.jpeg", "seg": "n0b",
        "window": "24.52-26.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": "Understand what they had just done.",
        "must_show": "the danger registering — the hall's reaction close: courtiers exchanging frozen glances, a scribe's stylus stopped mid-stroke; the room understanding before the visitors do.",
        "must_not_show": "no halo, glare or rim-light; the fear AMBIENT — everyone but the magi knows what this king does with rivals.",
        "scene": (
            "Close on the hall understanding "
            "faster than its guests: two "
            "courtiers trading a frozen glance "
            "over their cups, the court scribe's "
            "stylus stopped dead mid-stroke, a "
            "chamberlain's swallow travelling "
            "his throat — every local face doing "
            "the same instant arithmetic about "
            "kings and rivals and what happens "
            "next, while the three travellers "
            "stand innocently inside their own "
            "question. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b06", "out": "s06-they-asked-the-sitting-king.jpeg", "seg": "n0b",
        "window": "26.19-30.27", "wide": True, "jesus": False, "ref": False,
        "locks": ["MAGI", "HEROD", "HALL"],
        "narration": (
            "They asked the sitting king of Jerusalem to point them to the "
            "real one."
        ),
        "must_show": "the collision — the wide hall: the three travellers below, Herod above on his platform, circlet and purple; the sitting king asked for the real one's address.",
        "must_not_show": "no halo, glare or rim-light; Herod's face CONTROLLED — the trouble held behind the courtier's smile.",
        "scene": (
            "The wide hall stages the collision, the camera at the "
            "side wall so platform and floor read in one profile: "
            "on the raised platform Herod in his "
            "dark purple and thin gold circlet, "
            "heavy and shrewd and utterly still "
            "— and below him on the polished "
            "floor three dusty scholars waiting "
            "with honest faces for the sitting "
            "king of Jerusalem to kindly point "
            "the way to the real one — the "
            "question hanging in the cold light "
            "between the throne and the door. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r086-b07", "out": "s07-he-sent-them-on-to.jpeg", "seg": "n1",
        "window": "34.85-37.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HEROD", "HALL"],
        "narration": "He sent them on to Bethlehem with an errand of his own:",
        "must_show": "the commissioning — Herod come down close to the magi, an arm half-around in false warmth, his other hand pointing them south; the errand being attached.",
        "must_not_show": "no halo, glare or rim-light; the warmth FALSE and readable — hospitality worn over calculation.",
        "scene": (
            "Herod comes down off his platform "
            "wearing his warmest self: an arm "
            "hovering half-around the old "
            "Persian's shoulders, the other hand "
            "sweeping graciously south toward "
            "Bethlehem's road, the shrewd sunken "
            "eyes doing their private counting "
            "above the smile — a king gift-"
            "wrapping an errand of his own and "
            "tying it, gently, to three honest "
            "men's saddles. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b08", "out": "s08-go-and-search-diligently-for.jpeg", "seg": "s8",
        "window": "39.43-47.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEROD"],
        "narration": (
            "Go and search diligently for the young child; and when ye have "
            "found him, bring me word again, that I may come and worship him "
            "also."
        ),
        "must_show": "SCRIPTURE-EXACT: the lie delivered — close on Herod's face saying it: the smile working, the eyes not; WORSHIP HIM ALSO shaped by a mouth that means the opposite.",
        "must_not_show": "no halo, glare or rim-light; the doubleness in ONE face — pleasant lips, cold flat eyes.",
        "scene": (
            "Close on the lie at its work: "
            "Herod's mouth warm and generous "
            "around the words — BRING ME WORD, "
            "THAT I MAY COME AND WORSHIP HIM "
            "ALSO — while above the working "
            "smile the sunken eyes stay flat and "
            "cold as coins on a corpse, two "
            "different men sharing one face for "
            "the length of a sentence, and only "
            "one of them speaking. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r086-b09", "out": "s09-herod-was-frightened-and-he.jpeg", "seg": "n1",
        "window": "31.97-34.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEROD", "HALL"],
        "narration": "Herod was frightened, and he was clever about it.",
        "must_show": "SCRIPTURE-EXACT: troubled (v3) — close on Herod alone in his stillness after the question: the fear surfacing for one private beat, then the cleverness closing over it.",
        "must_not_show": "no halo, glare or rim-light; BOTH visible in sequence — the flinch of fear, the mask reassembling.",
        "scene": (
            "Close on the king in the beat "
            "nobody else catches: the word BORN "
            "still ringing, and across the heavy "
            "face one raw flash of the real "
            "thing — a old man's fear of the "
            "cradle he cannot bribe — before the "
            "cleverness slides back over it "
            "smooth as a visor, the fingers "
            "unclenching on the throne's arm, "
            "the smile being chosen from the "
            "rack. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b10", "out": "s10-go-and-look-carefully-for.jpeg", "seg": "n1b",
        "window": "49.25-57.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HEROD", "HALL"],
        "narration": (
            "Go and look carefully for the child, he said, and when you find "
            "him, come back and tell me, so that I can come and worship him "
            "too."
        ),
        "must_show": "the send-off — the magi bowing courteously to the king at the hall's door, the errand accepted in good faith; the trap travelling with them unseen.",
        "must_not_show": "no halo, glare or rim-light; the magi's trust GENUINE — no suspicion on their faces yet.",
        "scene": (
            "At the hall's great door the "
            "courtesies close the trap: the "
            "three scholars bowing their learned "
            "farewell, thanks given for the "
            "king's gracious interest, the "
            "errand folded trustingly in with "
            "their maps and their gift-chests — "
            "and Herod above them inclining his "
            "circleted head in benediction, "
            "watching his hook ride out the "
            "door on three honest backs. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r086-b11", "out": "s11-every-word-of-that-was.jpeg", "seg": "n1b",
        "window": "57.51-59.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEROD", "HALL"],
        "narration": "Every word of that was a lie.",
        "must_show": "the mask off — Herod turned away from the closed door, the smile gone entirely: the cold appetite plain now that no one watches.",
        "must_not_show": "no halo, glare or rim-light; NO violence imaged — the lie's truth carried in the emptied face alone.",
        "scene": (
            "The great door closes and the "
            "king's face closes with it: turned "
            "away into the brazier-shadow, the "
            "smile gone like a lamp put out, "
            "nothing left in the heavy features "
            "but the cold arithmetic underneath "
            "— a man alone with what he actually "
            "intends, in a hall where every "
            "gracious word he just spoke lies "
            "dead on the polished floor behind "
            "him. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b12", "out": "s12-they-were-led-at-last.jpeg", "seg": "n2a",
        "window": "64.36-66.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HOUSE"],
        "narration": "They were led at last to a house in Bethlehem.",
        "must_show": "SCRIPTURE-EXACT: the star STOOD OVER (v9) — night: the brilliant star standing directly above the small village house, the three travellers halted before its low door.",
        "must_not_show": "no halo, glare or rim-light on figures; the star STATIONARY overhead — journey's end written in the sky's geometry.",
        "scene": (
            "In the Bethlehem night the long "
            "journey runs out of road: the "
            "brilliant star stands stopped, "
            "directly and unmistakably above one "
            "small flat-roofed house — and "
            "before its low lamplit door the "
            "three travellers rein up and sit "
            "their camels in silence, looking "
            "from the humble mud-plastered walls "
            "up to the fixed light and back, "
            "checking an address written across "
            "two storeys of the universe. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r086-b13", "out": "s13-and-there-he-was-not.jpeg", "seg": "n2b",
        "window": "68.60-71.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE", "MARY"],
        "narration": "And there he was — not in a palace, but with his mother.",
        "must_show": "SCRIPTURE-EXACT: the young child WITH MARY (v11) — the lamplit room: the dark-haired toddler on Mary's lap by the small lamp; the whole kingdom, one room big.",
        "must_not_show": "no halo on the child; a TODDLER, not a newborn — the house plain, the pair complete.",
        "scene": (
            "Through the low doorway the lamp "
            "shows what the star was standing "
            "over: a packed-earth room, a niche "
            "lamp burning small, and Mary in her "
            "indigo veil with the young child on "
            "her lap — a dark-haired toddler, "
            "one small hand wound in his "
            "mother's sleeve, blinking at the "
            "strangers' shapes in his doorway — "
            "no throne, no court, no marble: a "
            "mother and a child, which was the "
            "whole address. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b14", "out": "s14-the-wise-men-knelt-before.jpeg", "seg": "n3",
        "window": "73.37-78.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HOUSE", "MARY"],
        "narration": (
            "The wise men knelt before the little child — everything their "
            "long journey had been for."
        ),
        "must_show": "SCRIPTURE-EXACT: fell down and worshipped — the three rich-robed scholars on their knees on the dirt floor before the toddler, heads bowing; the journey's whole purpose enacted.",
        "must_not_show": "no halo; the kneeling FULL — knees to packed earth, foreheads inclining, rich robes pooling in dust.",
        "scene": (
            "Down onto the packed-earth floor "
            "the three go — sapphire, crimson "
            "and emerald pooling in the dust as "
            "old knees and learned knees fold "
            "before a toddler on his mother's "
            "lap — heads bowing under the little "
            "lamp, months of desert and every "
            "star chart they own arriving at "
            "this exact posture in this exact "
            "room, worship spending itself where "
            "the light said to. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r086-b15", "out": "s15-matthew-writes-it-down-like.jpeg", "seg": "n3",
        "window": "78.99-80.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": "Matthew writes it down like this:",
        "must_show": "the hush before the verse — the lamplit room held still: kneeling shapes, the small lamp's flame, the record about to speak.",
        "must_not_show": "no halo; the frame QUIET — a breath of stillness in the little room.",
        "scene": (
            "The little room holds still for "
            "the record: the lamp's flame "
            "standing straight in its niche, the "
            "kneeling travellers' bowed shapes "
            "at rest, the child's small face in "
            "the amber light, dust settling "
            "where the robes disturbed it — a "
            "moment already turning into the "
            "sentence a tax collector will one "
            "day write down for the whole world "
            "to keep. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b16", "out": "s16-he-had-no-intention-of.jpeg", "seg": "n1b",
        "window": "59.84-62.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEROD", "HALL"],
        "narration": "He had no intention of worshipping anybody.",
        "must_show": "the truth of him — Herod brooding alone by a brazier, circlet heavy, jaw set; a king who kneels to nothing, planning accordingly.",
        "must_not_show": "no halo, glare or rim-light; NO weapons or violence imaged — intention carried in posture and eyes only.",
        "scene": (
            "Alone by the brazier's coals the "
            "king broods in his purple: the thin "
            "gold circlet catching the ember-"
            "light, the heavy jaw set, both "
            "hands closed on the back of a chair "
            "as if it were the future's neck — a "
            "man who has never knelt to anything "
            "in his long shrewd life, and does "
            "not intend to begin with a child in "
            "a village he can barely find on his "
            "own tax rolls. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b17", "out": "s17-and-when-they-were-come.jpeg", "seg": "j2",
        "window": "82.65-95.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HOUSE", "MARY"],
        "narration": (
            "And when they were come into the house, they saw the young "
            "child with Mary his mother, and fell down, and worshipped him: "
            "and when they had opened their treasures, they presented unto "
            "him gifts; gold, and frankincense, and myrrh."
        ),
        "must_show": "SCRIPTURE-EXACT: the whole verse — the kneeling magi with their three treasure chests OPEN before the child and Mary: gold's gleam, the resin jars of frankincense and myrrh, worship and gifts in one frame.",
        "must_not_show": "no halo; the three gifts DISTINCT — coined gold, pale resin, dark resin jar; presentation mid-gesture.",
        "scene": (
            "The verse fills the little room: "
            "the three still on their knees, and "
            "before the child and his mother the "
            "opened treasures of a far country — "
            "the old Persian tilting a chest of "
            "coined gold into the lamplight, the "
            "crimson scholar lifting the pale "
            "crumbled frankincense in its bowl, "
            "the youngest holding out the dark "
            "sealed jar of myrrh — a king's "
            "ransom presented across a "
            "packed-earth floor to a toddler in "
            "his mother's arms. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r086-b18", "out": "s18-god-warned-them-in-a.jpeg", "seg": "n4a",
        "window": "111.41-114.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "DESERT"],
        "narration": "God warned them in a dream not to go back to Herod.",
        "must_show": "SCRIPTURE-EXACT rendered per law: the warning as the sleeping camp only — the three asleep by embers under the stars, the old one stirring troubled; NO figure or apparition anywhere.",
        "must_not_show": "ABSOLUTE: no dream-figure, no apparition, no shape in the sky or air — only sleeping men, one stirring; the warning invisible.",
        "scene": (
            "In the desert camp the night does "
            "its quiet work: the three asleep in "
            "their travel robes around the "
            "banked embers, camels kneeling dark "
            "against the stars — and the old "
            "Persian stirring in his sleep, "
            "brow folding, hand closing on his "
            "blanket as something surer than "
            "reasoning turns him over — a "
            "warning passing through the camp "
            "without form or sound, leaving "
            "three changed itineraries behind "
            "it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r086-b19", "out": "s19-then-they-opened-up-what.jpeg", "seg": "n3b",
        "window": "97.70-104.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HOUSE"],
        "narration": (
            "Then they opened up what they had carried across the world and "
            "gave it to him — gold, and frankincense, and myrrh."
        ),
        "must_show": "the gifts close — the three offerings in the lamp's light at the child's level: gold coin, pale frankincense, the myrrh jar; a world's wealth at toddler height.",
        "must_not_show": "no halo; the gifts at the CHILD'S level on the floor — given down, not displayed up.",
        "scene": (
            "Close on the floor where the world "
            "has set down its wealth: the small "
            "chest of gold spilling its heavy "
            "coins in the lamplight, the bowl of "
            "pale frankincense breathing its "
            "resin sweetness, the dark myrrh jar "
            "with its wax seal — all of it "
            "placed low, at a standing toddler's "
            "height, where two small hands could "
            "reach the ransom of kings — the "
            "long road's whole cargo, delivered "
            "down. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b20", "out": "s20-they-had-crossed-a-desert.jpeg", "seg": "n3b",
        "window": "104.70-109.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HOUSE"],
        "narration": (
            "They had crossed a desert to kneel on a dirt floor in a village "
            "nobody had heard of."
        ),
        "must_show": "the journey's shape — through the open low door: the kneeling scholars inside the humble lamplit room, and beyond the doorway the night desert's edge they crossed; both ends of the road in one frame.",
        "must_not_show": "no halo; the contrast HONEST — world-class learning folded small in a room the world never heard of.",
        "scene": (
            "The open door holds both ends of "
            "the road at once: inside, three of "
            "the East's great minds kneeling in "
            "rich robes on a packed-dirt floor "
            "by one clay lamp — and out past "
            "the low lintel, the dark edge of "
            "the desert they spent to get here, "
            "starlit and enormous — a journey "
            "any court in the world would call "
            "madness, balancing perfectly in "
            "the ledger of the only court that "
            "counts. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r086-b21", "out": "s21-so-they-went-home-another.jpeg", "seg": "n4a",
        "window": "114.20-118.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["MAGI", "DESERT"],
        "narration": (
            "So they went home another way, and the king never got his "
            "answer."
        ),
        "must_show": "SCRIPTURE-EXACT: another way — dawn: the caravan swinging east by a different road, Jerusalem's distant hill left off their line entirely; the detour that saved a child.",
        "must_not_show": "no halo, glare or rim-light; the new heading VISIBLE — the road home bending wide of the city on the horizon.",
        "scene": (
            "At first light, the camera on a rise behind the turning "
            "train, the caravan swings "
            "wide: the three riders and their "
            "beasts taking a different road "
            "east, the track bending deliberately "
            "away from the far grey hill where "
            "Jerusalem and its waiting king sit "
            "off their new line — dawn at their "
            "backs' left instead of ahead, maps "
            "redrawn overnight by a wordless "
            "warning, and somewhere behind them "
            "a palace that will wait for a "
            "report already riding the other "
            "way. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r086-b22", "out": "s22-the-nations-had-come-to.jpeg", "seg": "n4b",
        "window": "120.01-122.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAGI", "HOUSE", "MARY"],
        "narration": "The nations had come to bow to the King.",
        "must_show": "the closing image — the room remembered: three foreign scholars bowed before the child and his mother in the small lamp's light; the nations' first bow, already made.",
        "must_not_show": "no halo; the closing frame REVERENT and still — the bow held, the gifts at rest, the little King unimpressed and loved.",
        "scene": (
            "The closing frame keeps the room "
            "the way history will: three "
            "scholars of the nations bowed low "
            "in sapphire, crimson and emerald on "
            "a village floor, their opened gifts "
            "at rest in the lamp's amber circle, "
            "and above the bowed heads the young "
            "child steadied on his mother's "
            "indigo lap — the wide world's first "
            "delegation, kneeling in a room "
            "with one lamp — the nations come "
            "to bow to the King, early, and "
            "exactly on time. Every figure has "
            "two arms, two hands and one head."
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
