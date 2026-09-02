#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 23: The Famine of the Word.

The Great Apostasy as Amos saw it: not a famine of bread, but of hearing.
Centuries of honest, praying people with no prophet to find — and a God who
honored agency, heard every prayer, and was counting the days.
Anchors: Amos 8:11-12; 1 Nephi 13:26; 2 Timothy 3:5; JS-History 1:19.

Reverence law for this episode: the medieval faithful are shown with HONOR —
their sincerity is real and God heard them. The tragedy is the missing
authority, never the people. Nothing is mocked.
"""

NARRATOR, SCRIPTURE, DEVIL = "narrator", "scripture", "devil"

EP = 323
NUM = 23
SLUG = "famine-of-the-word"
TITLE = "The Famine of the Word"
META = "Amos 8 · 1 Nephi 13"

SEGMENTS = [
    ("n1", NARRATOR,
     "Seven hundred years before Christ, the prophet Amos saw our chapter "
     "of the story coming — and he called it a famine."),
    ("s1", SCRIPTURE,
     "Behold, the days come, saith the Lord God, that I will send a famine "
     "in the land, not a famine of bread, nor a thirst for water, but of "
     "hearing the words of the Lord: And they shall wander from sea to sea, "
     "and from the north even to the east, they shall run to and fro to "
     "seek the word of the Lord, and shall not find it."),
    ("n2", NARRATOR,
     "Not a famine of bread. A famine of hearing. This is what the world "
     "looks like after the last apostle dies."),
    ("n3", NARRATOR,
     "The men who held the keys were hunted down, one by one. And when the "
     "last of them was gone, no one on earth had the authority to ordain "
     "what came next."),
    ("n4", NARRATOR,
     "So the drift began. Slow. Sincere. Fatal. Baptism changed shape. "
     "Authority was assumed instead of conferred. Councils met and voted on "
     "what God is — until the Father and the Son became a formless mystery "
     "no child could recognize as anyone's Father."),
    ("n5", NARRATOR,
     "Then the doors were declared shut. Revelation — finished. The heavens "
     "— closed. As if the God who had spoken in every generation since Adam "
     "had simply run out of things to say."),
    ("n6", NARRATOR,
     "And the book that remained — true, and precious, and carried through "
     "the centuries by brave and faithful hands — did not come through "
     "whole."),
    ("s2", SCRIPTURE,
     "They have taken away from the gospel of the Lamb many parts which are "
     "plain and most precious; and also many covenants of the Lord have "
     "they taken away."),
    ("n7", NARRATOR,
     "Without the plain parts, whole doctrines collapsed in the dark. "
     "Infants were pronounced guilty. Grace and works went to war. And "
     "asking God a direct question began to sound like madness."),
    ("n8", NARRATOR,
     "Now hear what the famine was not. It was not God abandoning His "
     "children. Men with agency killed the messengers. Men with power "
     "changed the ordinances. God honored their freedom — the same freedom "
     "He defended in heaven — and He never once stopped preparing the way "
     "back."),
    ("n9", NARRATOR,
     "For seventeen hundred years, honest people prayed real prayers and "
     "loved God with everything they had — with no prophet to find. "
     "Grandmothers. Monks in cold chapels. Mothers at bedsides. God heard "
     "every single one of them. And He was counting the days."),
    ("n10", NARRATOR,
     "Because a famine is not forever. Amos said the word would go missing "
     "— he never said it was destroyed. On a wooded hill in another "
     "hemisphere, a buried book was waiting. And heaven was watching a "
     "calendar."),
    ("n11", NARRATOR,
     "So the next time someone tells you the heavens are closed, remember "
     "what that idea really is. It is not a comfort. It is a famine. And "
     "famines end when God sends bread."),
]

CARD_SEG = ("card", NARRATOR,
            "Seventeen hundred years of searching, from sea to sea. The "
            "famine ends in a grove of trees.")

CARD_TEXT = ("The famine ends\n"
             "in a grove of trees.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty-Three — The Famine of the Word")

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
        "The prophet Amos on a dusk Judean hillside among his flocks: an "
        "aged weathered shepherd-prophet standing very still, staff in "
        "hand, face lifted toward a darkening eastern sky in three-quarter "
        "profile — the look of a man watching something far beyond the "
        "horizon arrive. Wind moves his rough wool mantle; sheep graze "
        "dim on the slope below.",
        "an aged shepherd-prophet with staff, three-quarter profile to a "
        "darkening sky, flock below",
        "his eyes on the lens, scrolls, halo, city skyline",
        era="ancient")),
    ("p02", "s1", _p(
        "The wandering begins: a ragged family — father, mother, two "
        "grown sons with travel staffs — seen ENTIRELY FROM BEHIND, four "
        "backs and the backs of four heads, walking AWAY from the camera "
        "down a grey endless sea-shore, their figures receding toward the "
        "far haze. The camera stands low on the sand directly behind "
        "them; not one face, cheek or profile is visible — cloaks, "
        "shoulders, heels only, cold surf on one side, dunes on the "
        "other, wind pressing their cloaks forward. Nothing ahead but "
        "distance.",
        "a family with staffs from behind on an endless grey shore, "
        "walking away into distance",
        "any face turned back, buildings, boats, anyone facing the lens",
        wide=True, era="ancient")),
    ("p03", ("s1", 0.38), _p(
        "From the north: an UPRIGHT vertical mountain scene — five "
        "cowled travellers in single file climbing AWAY from the "
        "camera, up a snowbound pass that rises into white-grey murk "
        "at the top of the frame, the nearest full-height at the "
        "frame's base, the line receding smaller and higher, bent "
        "into the driving snow, leaning on staffs, cloaks streaming "
        "back. A level horizon buried in murk; the climb fills the "
        "frame's height. Cold, vast, pitiless.",
        "five cowled travellers in single file climbing away and "
        "upward through driving snow, nearest full-height at the base",
        "faces to camera, sideways or rotated composition, wolves, "
        "torches, any warm light",
        wide=True, era="old-world")),
    ("p04", ("s1", 0.72), _p(
        "To and fro: a crowded ancient crossroads market where a knot of "
        "dusty travellers question a white-bearded elder — the nearest "
        "traveller's arms open in pleading, the elder's palms turned up "
        "empty in answer, other seekers pressing close, every face turned "
        "toward the elder or the ground, none toward the camera which "
        "shoots past a near shoulder. The gesture tells it: nothing here.",
        "travellers pleading with an elder whose empty palms turn up, "
        "camera past a near shoulder, no face to lens",
        "coins, laughter, anyone facing the camera",
        era="ancient")),
    ("p05", "n2", _p(
        "An abandoned assembly room of the first saints: benches empty "
        "along stone walls, a fallen cloth on the floor, thick dust "
        "hanging in two shafts of late window light, one clay lamp cold "
        "on its stand. No people at all. The silence is the subject.",
        "an empty first-century assembly room, dust in light shafts, "
        "cold lamp, no people",
        "any person, skeleton, cobweb excess, broken windows",
        era="first-century")),
    ("p06", "n3", _p(
        "After the last apostle: in a lamplit house-church room the "
        "camera looks from the doorway PAST the dark shoulder and back "
        "of a near mourner toward the room's centre, where an empty "
        "teacher's stool holds a folded travelling cloak — the brightest "
        "lit thing in the room. Around the walls a scattering of "
        "mourners sit and stand with heads DEEPLY BOWED or faces buried "
        "in hands, every body angled toward the stool, every face "
        "hidden by bowing or hands or turned fully away — NOT ONE face "
        "toward the camera. Two low flames gutter.",
        "an empty stool with folded cloak as the room's focus, bowed "
        "mourners around the walls, doorway camera past a shoulder",
        "a body, a coffin, anyone facing the lens, bright light",
        era="first-century")),
    ("p07", "n4", _p(
        "Grandeur replacing intimacy: the interior of a vast marble "
        "basilica seen down its full length from the high gallery — gold "
        "surfaces, towering columns, hanging lamps, incense haze in the "
        "light — and far below on the patterned floor, a thin scatter of "
        "tiny worshippers dwarfed to insignificance by the architecture. "
        "Majestic, cold, and very far from a fisherman's room.",
        "a vast gold-and-marble basilica interior from high above with "
        "tiny scattered worshippers far below",
        "mockery, decay, anyone identifiable, readable inscriptions",
        wide=True)),
    ("p08", ("n4", 0.52), _p(
        "The council votes on God: rows of robed churchmen in a great "
        "stone hall raising their hands in formal vote, seen from behind "
        "the last row so the raised arms and cowled heads recede toward a "
        "distant dais with unrolled parchments — the camera shoots past "
        "the near backs; not one face is turned toward the lens. "
        "Candlelight and stone; solemn, procedural, human.",
        "rows of robed men from behind with hands raised in vote toward "
        "a parchment dais",
        "faces to camera, shouting, caricature, readable text",
        wide=True)),
    ("p09", ("n4", 0.78), _p(
        "What the abstraction feels like: a small child stands alone at "
        "the centre of a vast dim cathedral floor, tiny beneath columns "
        "that vanish upward into cold darkness, looking up and up — seen "
        "from behind at the child's height so the stone immensity "
        "overwhelms the frame and the child's face is never visible. "
        "Somewhere far above, grey light. Nothing anywhere a child could "
        "run to.",
        "a tiny child from behind looking up into cold vanishing stone "
        "height",
        "the child's face, warmth, any figure of God, statues of faces",
        )),
    ("p10", "n5", _p(
        "The doors declared shut: two robed men swing the immense bronze "
        "doors of a church closed from within, the last blade of daylight "
        "narrowing across the stone floor toward the camera as the gap "
        "shrinks — both men seen from behind in full strain, the door's "
        "weight visible in their backs and braced feet.",
        "great bronze doors being pulled shut from inside, the daylight "
        "blade narrowing on the floor, two straining backs",
        "faces to camera, congregation, panic",
        )),
    ("p11", ("n5", 0.55), _p(
        "A chained book: in a stone library alcove, a massive "
        "vellum-bound volume lies on a slanted lectern with a hand-forged "
        "iron chain running from its cover to a ring in the wall, one "
        "candle beside it, its pages closed. Any lettering on the spine "
        "is aged past reading. The chain is the subject.",
        "a great closed book chained by iron to the wall of its alcove, "
        "one candle",
        "readable words, hands, faces, torn pages",
        )),
    ("p12", "n6", _p(
        "The faithful copyist: close on an old monk's ink-stained hands "
        "guiding a quill across vellum by candlelight, his cowled head "
        "bowed just into the frame's top edge, the strokes of his work "
        "soft-focus and completely illegible. Care in every knuckle. "
        "This man is a hero, and the light says so.",
        "an old monk's hands mid-copy by candlelight, cowled head bowed, "
        "warm honoring light, illegible strokes",
        "readable letters, his eyes visible, mockery, gloom",
        )),
    ("p13", "s2", _p(
        "What the centuries took: an ancient codex lies open under "
        "raking candlelight, and across its aged pages several wide "
        "HORIZONTAL BANDS of the text block are simply GONE — faded to "
        "ghost-blank parchment in irregular rectangular runs the shape "
        "of missing PARAGRAPHS, edges water-stained, one lower corner "
        "torn away — the surviving strokes between the gaps blurred and "
        "unreadable. The blank regions are plain rectangles of empty "
        "page: no shape, symbol, cross, figure or pattern is formed by "
        "any gap. A reader's empty hands rest either side of the book, "
        "palms open, holding nothing.",
        "an open ancient codex with rectangular paragraph-shaped blank "
        "gaps and a torn corner, open empty hands resting beside it",
        "any cross, symbol or figure formed by the gaps; readable "
        "words; ink still wet; scissors",
        )),
    ("p14", "n7", _p(
        "The cost in the nursery: night in a cold stone side-chapel, "
        "young parents huddled at a carved font clutching their days-old "
        "baby toward a tired priest, both parents' faces raw with FEAR — "
        "fear for the child's soul — lit by two candles, everyone's gaze "
        "on the infant, no one toward the camera. The scene is tender "
        "and wrong at once: love, urgency, and a doctrine of guilt that "
        "was never true.",
        "frightened young parents pressing their newborn toward a "
        "priest at a night font, all gazes on the child",
        "cruelty from the priest, anyone facing the lens, gargoyles, "
        "caricature",
        )),
    ("p15", ("n7", 0.6), _p(
        "The war of ideas: a scholar alone at midnight among open books "
        "and disputation papers, head sunk in his hands, candle guttering "
        "in the draught, pages of illegible argument spilling to the "
        "floor — a man drowning in words about God with no way to ask "
        "Him anything.",
        "a scholar head-in-hands over spilled illegible pages at "
        "midnight, guttering candle",
        "readable text, his eyes to the lens, demons, caricature",
        )),
    ("p16", "n8", _p(
        "What men's choices left behind: rain sweeping a dark moorland "
        "at dusk, and on its rise the roofless shell of an old stone "
        "chapel — walls broken, doorway empty — except that one small "
        "arched window still holds its shape whole against the last grey "
        "light. Loss and endurance in a single ruin; no people anywhere.",
        "a roofless ruined chapel on a rain-swept moor with ONE intact "
        "arched window against the light",
        "people, fire, lightning striking, collapse in progress",
        wide=True, devil=True)),
    ("p17", "n9", _p(
        "The famine's saints: an old grandmother kneels at a bedside in "
        "a poor cottage, rushlight burning, her worn hands knotted "
        "together on the blanket, head bowed over them, shawled and "
        "small and absolutely sincere — the camera close at the "
        "bedside's foot, her face soft in downturned profile. Heaven "
        "hears this woman. The warm light on her hands says so.",
        "an old woman's knotted praying hands on a bedside blanket, "
        "bowed shawled head in profile, rushlight warmth",
        "her eyes to the lens, squalor played for pity, any mockery",
        )),
    ("p18", ("n9", 0.42), _p(
        "A monk alone in a freezing pre-dawn chapel, kneeling upright on "
        "bare stone before a plain unadorned altar, his breath visible "
        "in the candlelight, cowl back, weathered face lifted with "
        "closed eyes — seen from the side at a respectful distance down "
        "the empty aisle. Devotion with no audience.",
        "a lone kneeling monk in profile, visible breath, plain altar, "
        "empty cold chapel",
        "his eyes on the lens, ornament, other people, sunbeams",
        )),
    ("p19", ("n9", 0.74), _p(
        "A mother through the night: she sits on the floor beside her "
        "sick child's low bed, one hand on the small chest, the other "
        "pressed to her own mouth, eyes closed, tears bright on her "
        "cheeks in the candlelight — praying without words, seen from "
        "beside the bed so both faces show in profile, the child's "
        "flushed and asleep.",
        "a mother's hand on her sick child's chest, her other hand at "
        "her mouth, closed wet eyes, both in candlelit profile",
        "either face to the lens, death imagery, medicine bottles",
        )),
    ("p20", "n10", _p(
        "Another hemisphere, waiting: golden late-afternoon light over a "
        "quiet wooded drumlin hill rising from young-forest country — "
        "unbroken wilderness, maples and oaks in full leaf, birdsong "
        "weather, not a person or a building in sight. An ordinary "
        "beautiful hill keeping an extraordinary secret.",
        "a serene wooded drumlin hill in golden light, pure wilderness, "
        "no people or structures",
        "any person, path, fence, monument, glow from the ground",
        wide=True, era="america-1820")),
    ("p21", ("n10", 0.55), _p(
        "Heaven watching a calendar: the same wooded hill at full night "
        "under an immense brilliant sky — the milky way arching over the "
        "dark treeline, stars in their thousands, the hill a sleeping "
        "silhouette of forest below. Patience made visible.",
        "the dark forested hill under a vast brilliant star field and "
        "milky way arch",
        "any figure, light from the hill, meteors, text",
        wide=True, era="america-1820")),
    ("p22", "n11", _p(
        "The answer begins: first sunrise light strikes the ruined "
        "moorland chapel from Episode's earlier frame — and pours "
        "straight through its one whole window, laying a bright "
        "window-shaped panel of gold across the wet grass inside the "
        "broken walls. The rain has passed; the sky burns clean behind "
        "it.",
        "sunrise streaming through the ruin's one intact window onto "
        "the grass within, clean burning sky",
        "people, rainbows, beams drawn as rays, text",
        )),
    ("p23", ("n11", 0.6), _p(
        "Bread again, close and warm: strong weathered hands break a "
        "round crusted loaf apart in full morning light at a plain "
        "wooden table, steam rising from the opened crumb, flour still "
        "on the knuckles. Nothing else — the frame is the promise: "
        "famines end when God sends bread.",
        "hands breaking a steaming fresh loaf in morning light on bare "
        "wood",
        "faces, knives, plates of feast, text",
        )),
]
