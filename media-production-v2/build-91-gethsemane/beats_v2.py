#!/usr/bin/env python3
"""V2 beat map — row 91, build-91-gethsemane (Matt 26:36-46; Mark 14:32-42;
Luke 22:39-46).

COVERAGE: 40 pictures over 225.4 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  Matt 26:36  "a place called GETHSEMANE" — an olive grove across the
        Kidron (John 18:1-2: "a garden... Jesus OFTTIMES RESORTED
        thither"); after the hymn, at night.
  Matt 26:37  he takes PETER, JAMES and JOHN deeper; "began to be
        sorrowful and very heavy."
  Matt 26:38  "My soul is exceeding sorrowful, even unto death: tarry
        ye here, and WATCH WITH ME."
  Luke 22:41  "withdrawn from them about a STONE'S CAST, and KNEELED
        DOWN, and prayed."
  Luke 22:42  "Father, if thou be willing, remove THIS CUP from me:
        nevertheless NOT MY WILL, but thine, be done."
  Luke 22:43  "there appeared an ANGEL unto him from heaven,
        STRENGTHENING him."
  Luke 22:44  "his SWEAT was as it were GREAT DROPS OF BLOOD falling
        down to the ground." — a physician's simile; rendered as
        anguish and heavy falling drops, restrained, no gore.
  Luke 22:45  he finds them "SLEEPING FOR SORROW."
  Matt 26:41  "WATCH AND PRAY... the spirit indeed is willing, but the
        flesh is weak."
  Matt 26:44  he prays a THIRD time, "the same words."
  Matt 26:46  "RISE, let us be going: behold, he is at hand that doth
        betray me." — torches across the valley; he walks TOWARD them.

ANGEL RENDERING (CONTENT-CARE law): the Luke 22:43 angel is a real,
plain-robed figure in PALE SILVER-GREY — NO wings, no ring of light,
nothing outlining the body; strength given by presence and support.

TIME OF DAY: deep NIGHT throughout — moonlight through old olives,
the city's few lamps across the black valley; the arrest-party beats
lit by distant torches only. Correct story darkness, not the row-11
defect.

CONTENT-CARE: the agony rendered with full dignity — anguish real and
unhidden but never contorted-grotesque; the blood-sweat as heavy dark
drops in dim light, no red gore; the arrest party distant torchlight,
no weapons detailed, no violence (that is the next row's off-screen
territory).

CHANGING CONDITION (kept OUT of the locks): his burden — walking in,
breaking, wrestled, settled, resolved; the three — awake, asleep,
woken; the valley — dark, then threaded with far torches.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER, JAMES-Z and JOHN come from the shared CAST_LOCKS.
LOCKS = {
    "GROVE": (
        "GROVE LOCK: Gethsemane — an ancient olive grove on the lower "
        "slope across the Kidron valley: massive gnarled silver-grey "
        "olive trunks, moon-pale rock outcrops, roots and packed "
        "earth, low stone terrace walls; full moonlight through the "
        "leaves, and across the black valley the city's wall and its "
        "few small lamps. The same trees, rocks and skyline "
        "throughout."
    ),
    "EIGHT": (
        "EIGHT LOCK: the waiting disciples at the garden's edge — "
        "eight travel-worn men in DARK EARTH-BROWN, CHARCOAL and DEEP "
        "OLIVE robes (never cream, never white), settling among the "
        "roots by the gate; weary, loyal, human."
    ),
    "ANGEL": (
        "ANGEL LOCK: the strengthening angel is a tall, real human "
        "figure in a plain PALE SILVER-GREY robe — NO wings, no ring "
        "of light above the head, no light outlining the body; a "
        "calm, strong, ageless face with dark hair; feet on the "
        "ground, hands that truly hold."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r091-b01", "out": "s01-it-was-late-on-the.jpeg", "seg": "n1",
        "window": "0.28-2.14", "wide": True, "jesus": False, "ref": False,
        "locks": ["GROVE"],
        "narration": "It was late on the night before he died.",
        "must_show": "the hour — the moonlit grove empty and still, the dark valley and the city's few lamps beyond; the night itself, waiting.",
        "must_not_show": "no halo, glare or rim-light; the frame EMPTY of people — the stage before the story steps onto it.",
        "scene": (
            "The old grove waits in the "
            "moonlight: gnarled silver trunks "
            "standing in their own black "
            "shadows, pale rock breaking the "
            "slope, the leaves hanging "
            "still in the windless dark — "
            "and beyond the terrace wall the "
            "valley lies black to the city's "
            "far wall, where a handful of "
            "small lamps burn late over "
            "Passover — an ordinary olive "
            "yard on the one night of its "
            "life. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b02", "out": "s02-the-supper-was-over-the.jpeg", "seg": "n1",
        "window": "2.14-13.20", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "EIGHT", "PETER", "JOHN"],
        "narration": (
            "The supper was over, the songs were sung, and Jesus led his "
            "friends out of the city, down across the valley, and up into a "
            "quiet grove of olive trees."
        ),
        "must_show": "the walk in — the file of eleven following Jesus up the moonlit slope into the grove, the city's wall and lamps behind them across the valley.",
        "must_not_show": "no halo, glare or rim-light; the file QUIET — supper's song faded, night settling on the shoulders.",
        "scene": (
            "Up from the valley floor the "
            "little company climbs in "
            "moonlight — Jesus first through "
            "the terrace gap, the eleven "
            "strung behind him in a quiet "
            "file, cloaks drawn against the "
            "night chill — the city's wall "
            "and its few late lamps falling "
            "away behind them across the "
            "black Kidron, the last psalm "
            "still dying out of their "
            "breathing as the old trees "
            "take them in one by one. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r091-b03", "out": "s03-he-had-come-here-often.jpeg", "seg": "n1",
        "window": "13.20-15.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "He had come here often.",
        "must_show": "the familiarity — close on Jesus's hand resting on a known gnarled trunk in passing; a place his feet know in the dark.",
        "must_not_show": "no halo, glare or rim-light; the touch HABITUAL — an old friendship with a place.",
        "scene": (
            "Close on the old friendship "
            "between a man and a place: "
            "Jesus's hand finding the same "
            "gnarled trunk it has found a "
            "hundred evenings, resting there "
            "a moment in passing — the bark "
            "worn smooth at exactly that "
            "height — his feet choosing the "
            "root-steps in the dark without "
            "looking, the grove receiving "
            "him the way a room receives "
            "the one who lives in it. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r091-b04", "out": "s04-at-the-edge-of-the.jpeg", "seg": "n2",
        "window": "18.35-23.87", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "EIGHT"],
        "narration": (
            "At the edge of the garden he stopped, and asked most of them to "
            "sit and wait while he went ahead to pray."
        ),
        "must_show": "SCRIPTURE-EXACT: sit ye here — Jesus turning at the grove's edge, hand gesturing the eight down among the roots; the parting of the company beginning.",
        "must_not_show": "no halo, glare or rim-light; the eight SETTLING — cloaks spreading, backs finding trunks; obedient and tired.",
        "scene": (
            "At the terrace wall Jesus turns "
            "and his quiet hand settles the "
            "company: the eight folding down "
            "among the moonlit roots — one "
            "spreading his cloak, another "
            "setting his back against a "
            "trunk with a tired sigh, the "
            "long day arriving in all their "
            "bones at once — SIT YE HERE, "
            "WHILE I PRAY YONDER — the "
            "night's first parting, made "
            "gently, at the garden's edge. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b05", "out": "s05-he-told-them-gently-to.jpeg", "seg": "n2",
        "window": "23.87-29.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["EIGHT"],
        "narration": (
            "He told them gently to pray as well, so that what was coming "
            "would not overtake them."
        ),
        "must_show": "the gentle charge — close on Jesus bent toward the settling men, the pray-also given like a father's goodnight; care for THEM on the worst night of HIS life.",
        "must_not_show": "no halo, glare or rim-light; the tone TENDER — instruction as protection, not command.",
        "scene": (
            "Close on the tenderness of the "
            "charge: Jesus bent slightly "
            "toward the settling men, his "
            "voice low as a father's at a "
            "doorway — PRAY, THAT YE ENTER "
            "NOT — the words tucked around "
            "them like a blanket against "
            "weather only he can see coming "
            "— a man one hour from his own "
            "agony, spending the walk in on "
            "the protection of his tired "
            "friends. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b06", "out": "s06-then-he-went-deeper-into.jpeg", "seg": "n2",
        "window": "29.00-31.54", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "Then he went deeper into the trees.",
        "must_show": "the going deeper — Jesus's cream-robed figure moving away up the slope into the older darker trees, the moonlight taking him in and out of shadow.",
        "must_not_show": "no halo, glare or rim-light; the figure RECEDING — the grove deepening around him.",
        "scene": (
            "The grove deepens around his "
            "going: the cream-robed figure "
            "moving away up the slope "
            "between the ancient trunks, "
            "moonlight taking him and "
            "shadow giving him back, tree "
            "by tree, the ground rising and "
            "the branches lowering until "
            "the garden's oldest darkness "
            "stands all around him — a man "
            "walking deliberately toward "
            "the loneliest hour in the "
            "history of the world. Every "
            "figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r091-b07", "out": "s07-he-took-only-three-with.jpeg", "seg": "n3",
        "window": "32.16-37.53", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": (
            "He took only three with him — Peter, James, and John, the ones "
            "who had been closest to him."
        ),
        "must_show": "SCRIPTURE-EXACT: the three taken — Peter, James and John following him deeper among the old trunks; the inner circle, drawn close for the hard hour.",
        "must_not_show": "no halo, glare or rim-light; the three's loyalty VISIBLE — close behind him, watchful, uneasy.",
        "scene": (
            "Three shapes follow him into "
            "the deeper trees: Peter's broad "
            "frame first, then James and "
            "John close together, picking "
            "their way over the moonlit "
            "roots after the cream of his "
            "robe — the same three from the "
            "bright mountain and the little "
            "girl's room, called now into a "
            "darker witnessing — uneasy "
            "without knowing why yet, and "
            "coming anyway, because he "
            "asked. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b08", "out": "s08-and-as-he-walked-something.jpeg", "seg": "n3",
        "window": "37.53-44.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "And as he walked, something began to break over him: a weight "
            "none of them had ever seen him carry."
        ),
        "must_show": "SCRIPTURE-EXACT: began to be sorrowful and very heavy — close on Jesus mid-stride as the weight arrives: the shoulders bowing, a hand reaching for a trunk, the face changing.",
        "must_not_show": "no halo, glare or rim-light; the breaking DIGNIFIED — a strong man bending under real weight, never collapsing theatrically.",
        "scene": (
            "Mid-stride, it arrives: the "
            "frame close on Jesus as "
            "something no one has ever seen "
            "on him comes down over his "
            "frame like a loaded yoke — the "
            "straight shoulders bowing by "
            "degrees, one hand going out to "
            "an olive trunk and gripping "
            "it, the warm face altering in "
            "the moonlight as sorrow the "
            "size of the world finds him "
            "alone among the trees and "
            "settles on. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r091-b09", "out": "s09-he-was-sorrowful-and-deeply.jpeg", "seg": "n3",
        "window": "44.02-46.88", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "He was sorrowful, and deeply troubled.",
        "must_show": "the sorrow named — close on his moonlit face: grief and trouble open in it, unhidden; the strongest face they knew, in honest distress.",
        "must_not_show": "no halo, glare or rim-light; the face TROUBLED, never contorted — deep water, not wreckage.",
        "scene": (
            "Close on the face the three "
            "have followed for three years, "
            "changed: the warm brown eyes "
            "dark with a trouble that has "
            "no floor, the brow carrying "
            "weather they have never seen "
            "on it, the mouth pressed "
            "against something rising — "
            "sorrow worn openly, without "
            "performance and without "
            "disguise, by the one man they "
            "believed nothing on earth "
            "could shake. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r091-b10", "out": "s10-he-did-not-hide-it.jpeg", "seg": "n4",
        "window": "54.68-56.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN"],
        "narration": "He did not hide it from them.",
        "must_show": "the openness — Jesus facing the three with the sorrow plain on him; their stricken faces receiving what he refuses to mask.",
        "must_not_show": "no halo, glare or rim-light; NO brave mask — honesty between friends, and the three shaken by it.",
        "scene": (
            "He turns to them with none of "
            "it hidden: the sorrow standing "
            "plain in his face and posture, "
            "offered to his three friends "
            "unmasked — and the sight lands "
            "on them harder than any storm "
            "did: Peter's certainty gone "
            "from his eyes, John's young "
            "face stricken, James looking "
            "helplessly from brother to "
            "brother — strong men "
            "discovering that their anchor "
            "can weep. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b11", "out": "s11-he-told-them-plainly-how.jpeg", "seg": "n4",
        "window": "56.12-66.29", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": (
            "He told them plainly how heavy his heart was — heavy enough, he "
            "said, to crush the life out of him — and he asked them simply "
            "to stay near, and stay awake."
        ),
        "must_show": "the plain telling — Jesus close before the three under the trees, hand to his own chest; the stay-near request passing to their shaken faces.",
        "must_not_show": "no halo, glare or rim-light; the request SMALL and human — nearness and wakefulness, all he asks.",
        "scene": (
            "Under the old branches he tells "
            "them plainly, hand flat on his "
            "own chest where the weight "
            "sits: heavy enough to kill — "
            "the words given straight into "
            "their shaken faces — and then "
            "the request, so small against "
            "the size of the night: stay "
            "near me; stay awake with me — "
            "the Lord of storms asking his "
            "three friends for the plainest "
            "human comfort there is: "
            "company. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b12", "out": "s12-he-did-not-want-to.jpeg", "seg": "n4",
        "window": "66.29-68.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "He did not want to be alone.",
        "must_show": "the human need — close on Jesus's face at the asking: the simple, universal not-wanting-to-be-alone, undisguised.",
        "must_not_show": "no halo, glare or rim-light; the need UNASHAMED — divinity not cancelling the human ache.",
        "scene": (
            "Close on the plainest thing he "
            "ever asked for: the face in "
            "the moonlight holding the "
            "ache every human being has "
            "carried into every dark night "
            "since the first one — the "
            "simple animal-and-soul need "
            "for another heartbeat nearby — "
            "worn without shame by the "
            "maker of company himself, on "
            "the night everything was "
            "about to be carried alone. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b13", "out": "s13-everything-he-had-just-wrestled.jpeg", "seg": "n12",
        "window": "217.10-222.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": (
            "Everything he had just wrestled with in the dark, he now "
            "carried toward the cross."
        ),
        "must_show": "the carrying-forward — Jesus walking steadily down through the grove toward the gate and the far torchlight, the three behind him; the settled will in motion.",
        "must_not_show": "no halo, glare or rim-light; his stride RESOLVED — no dragging, no flinching; the torches distant points only.",
        "scene": (
            "Down through the trees he "
            "walks it forward: the settled "
            "will moving at a steady, "
            "unhurried stride toward the "
            "grove's gate, the three "
            "hurrying to keep up behind — "
            "and far below across the "
            "black valley the little "
            "thread of torches climbing to "
            "meet him — everything the "
            "dark hours wrestled and won "
            "now walking on two feet, "
            "carried by choice toward the "
            "morning's tree. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r091-b14", "out": "s14-then-he-went-on-a.jpeg", "seg": "n5",
        "window": "69.34-77.46", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Then he went on a little further by himself, about as far as a "
            "man can throw a stone, and he sank down onto the ground among "
            "the roots and the rocks."
        ),
        "must_show": "SCRIPTURE-EXACT: a stone's cast, kneeled down — Jesus alone at the grove's heart, sinking to his knees among roots and pale rock in the moonlight; the three small behind through the trees.",
        "must_not_show": "no halo, glare or rim-light; the distance READABLE — a stone's throw between him and the three; the sinking heavy and real.",
        "scene": (
            "A stone's throw deeper the "
            "night takes him alone: among "
            "the roots and moon-pale rocks "
            "at the grove's heart Jesus "
            "sinks down — knees to the "
            "packed earth, then the weight "
            "folding him lower — while back "
            "through the trunks the three "
            "watching shapes shrink to "
            "shadows at exactly the "
            "distance a man can throw a "
            "stone and no further — close "
            "enough to see, too far to "
            "hold. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b15", "out": "s15-everything-that-was-coming-all.jpeg", "seg": "n5",
        "window": "77.46-82.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Everything that was coming, all of it, he carried to his Father "
            "in prayer."
        ),
        "must_show": "the carrying — close on the kneeling figure bowed over the earth, hands pressed to the ground; the whole coming weight being handed upward in words.",
        "must_not_show": "no halo, glare or rim-light; the prayer PHYSICAL — a body bent around its burden, speaking into the dirt.",
        "scene": (
            "Close on the carrying: the "
            "kneeling body bowed until his "
            "face is nearly to the packed "
            "earth, both hands pressed flat "
            "among the roots, the moon on "
            "the curve of his spine — and "
            "the words going up from that "
            "lowest posture, everything "
            "that is coming named piece by "
            "piece into the dirt and "
            "handed, piece by piece, to "
            "the only One strong enough to "
            "be asked. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r091-b16", "out": "s16-father-if-thou-be-willing.jpeg", "seg": "jv42",
        "window": "83.10-90.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Father, if thou be willing, remove this cup from me: "
            "nevertheless not my will, but thine, be done."
        ),
        "must_show": "SCRIPTURE-EXACT: the prayer itself — the kneeling Jesus with face lifted to the night sky, anguish and surrender together in the moonlit features.",
        "must_not_show": "no halo, glare or rim-light; NO literal cup object in frame — the cup lives in the words; face lifted, not crushed.",
        "scene": (
            "The prayer lifts his face to "
            "the night: moonlight full on "
            "the anguished features as the "
            "words go up — IF THOU BE "
            "WILLING, REMOVE THIS CUP — the "
            "honest asking of a man who "
            "wants another way with "
            "everything in him — and then, "
            "in the same breath, the "
            "surrender that outweighs "
            "worlds: NEVERTHELESS — NOT MY "
            "WILL, BUT THINE — both halves "
            "true at once on one lifted "
            "face. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b17", "out": "s17-but-this-night-was-not.jpeg", "seg": "n1",
        "window": "15.12-17.79", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "EIGHT"],
        "narration": "But this night was not like the others.",
        "must_show": "the difference — the company entering the familiar grove, but the mood changed: Jesus's face graver than the place has ever seen it, the men subdued.",
        "must_not_show": "no halo, glare or rim-light; the WRONGNESS subtle — same grove, different weight.",
        "scene": (
            "The familiar gate takes them in "
            "as always — the same worn gap "
            "in the terrace wall, the same "
            "moon through the same old "
            "branches — but the grove seems "
            "to know before the men do: "
            "Jesus's face graver than this "
            "place has ever seen it, the "
            "usual evening ease gone from "
            "the file behind him, eleven "
            "men entering an ordinary "
            "garden on a night that has "
            "already stopped being "
            "ordinary. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b18", "out": "s18-he-asked-honestly-if-there.jpeg", "seg": "n6",
        "window": "92.04-99.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "He asked, honestly, if there were any other way — if this cup "
            "of suffering could pass from him, let it pass."
        ),
        "must_show": "the honest asking — close on the praying face and open upturned hands: the real request really made, nothing performed.",
        "must_not_show": "no halo, glare or rim-light; the asking GENUINE — hope in it, not theatre.",
        "scene": (
            "Close on the honesty of it: "
            "the upturned open hands, the "
            "face asking the way a man "
            "asks who genuinely hopes — is "
            "there another road, any other "
            "road, one door anywhere in "
            "the universe that is not this "
            "one — the request made whole "
            "and real into the night sky, "
            "with nothing held back and "
            "nothing performed, by a Son "
            "certain his Father hears. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b19", "out": "s19-whatever-his-father-wanted-that.jpeg", "seg": "n6",
        "window": "102.41-106.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "Whatever his Father wanted, that was what he wanted more.",
        "must_show": "the deeper wanting — the praying face settling from anguish toward alignment: the more-wanted will winning visibly.",
        "must_not_show": "no halo, glare or rim-light; the settling REAL — surrender as strength arriving, not defeat.",
        "scene": (
            "The frame holds the settling: "
            "across the moonlit face the "
            "storm of the asking slowly "
            "gives way to something deeper "
            "and older than the fear — the "
            "want beneath the want — the "
            "features aligning by degrees "
            "toward his Father's will like "
            "a compass needle coming home, "
            "not because the dread is gone "
            "but because the love is "
            "bigger, and always was. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b20", "out": "s20-not-his-own-will-he.jpeg", "seg": "n6 + n7",
        "window": "106.43-112.83", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Not his own will, he prayed, but his Father's. This was no "
            "calm, quiet moment."
        ),
        "must_show": "the struggle's violence — the kneeling figure gripped in real wrestling: fists in the dirt, body rocked forward, the agony physical.",
        "must_not_show": "no halo, glare or rim-light; the struggle DIGNIFIED but VIOLENT — a body fighting a war, never grotesque.",
        "scene": (
            "The wide frame shows what the "
            "words cost: the kneeling body "
            "rocked forward over the earth, "
            "fists closed full of dirt and "
            "root, the breath coming visible "
            "in the cold night air, the "
            "cream wool dark with sweat "
            "down the spine — prayer as "
            "combat, a will being bent "
            "toward heaven by main "
            "strength, in the dark, alone — "
            "no calm anywhere in the "
            "picture, and no retreat "
            "either. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b21", "out": "s21-luke-who-was-a-physician.jpeg", "seg": "n7",
        "window": "112.83-120.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Luke, who was a physician, tells us that as he prayed in that "
            "anguish, his sweat fell like great drops of blood to the "
            "ground."
        ),
        "must_show": "SCRIPTURE-EXACT rendered restrained: the anguish at its peak — sweat heavy on the brow and beading dark, great drops falling to the moonlit earth; the physician's detail, no gore.",
        "must_not_show": "ABSOLUTE: no red gore, no wounds, nothing grotesque — heavy dark drops in dim light, dignity total.",
        "scene": (
            "Close on the physician's "
            "detail: the brow shining and "
            "heavy in the moonlight, sweat "
            "gathered thick at the "
            "hairline and temple — and "
            "falling, drop after great "
            "heavy drop, dark in the dim "
            "light, to spot the packed "
            "earth between his braced "
            "hands — a body pressed to the "
            "very borders of what bodies "
            "can carry, recorded exactly by "
            "the one gospel writer trained "
            "to know what he was looking "
            "at. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b22", "out": "s22-the-suffering-was-real-and.jpeg", "seg": "n7",
        "window": "120.98-124.63", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "The suffering was real, and he felt every ounce of it.",
        "must_show": "the realness — the suffering face unspared and unsoftened: exhaustion, anguish, endurance all present; nothing anesthetized.",
        "must_not_show": "no halo, glare or rim-light; NO serenity imposed — the cost shown honestly, with dignity.",
        "scene": (
            "The frame refuses to look "
            "away: the face in the "
            "moonlight carrying the full "
            "un-anesthetized weight — eyes "
            "pressed shut and glittering "
            "wet at the lashes, jaw "
            "trembling with the effort of "
            "the next breath, every line "
            "of the features testifying "
            "that nothing about this is "
            "being absorbed painlessly by "
            "divinity — felt, all of it, "
            "ounce by ounce, on purpose. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b23", "out": "s23-and-still-he-stayed-and.jpeg", "seg": "n7",
        "window": "124.63-128.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "And still he stayed, and still he prayed.",
        "must_show": "the staying — the kneeling figure holding his ground among the roots, unmoved from the place of prayer; endurance as the whole picture.",
        "must_not_show": "no halo, glare or rim-light; NO retreat in the posture — planted, remaining, continuing.",
        "scene": (
            "The wide grove holds the one "
            "unmoving thing in it: the "
            "kneeling figure planted among "
            "the roots and pale rocks, "
            "bowed but not gone, shaken "
            "but not risen to run — the "
            "gate stands open downhill, "
            "the dark offers a hundred "
            "roads out of this, and he "
            "stays: knees in the same "
            "dirt, words still climbing, a "
            "man remaining in the fire by "
            "choice because love is on the "
            "other side of it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b24", "out": "s24-and-heaven-did-not-leave.jpeg", "seg": "n8",
        "window": "128.74-133.93", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "ANGEL"],
        "narration": (
            "And heaven did not leave him there alone. An angel came to him "
            "out of the darkness and strengthened him."
        ),
        "must_show": "SCRIPTURE-EXACT (Luke 22:43): the strengthening — the silver-grey-robed figure kneeling beside the exhausted Jesus, hands truly supporting his shoulders; presence as the answer.",
        "must_not_show": "ABSOLUTE: no wings, no ring of light, nothing outlining the figure — a real solid presence, feet on the earth, holding him up.",
        "scene": (
            "Out of the darkness between "
            "the trunks help arrives on "
            "two quiet feet: a tall figure "
            "in plain silver-grey kneeling "
            "down into the dirt beside the "
            "spent and shaking man, strong "
            "hands taking his shoulders "
            "and truly bearing weight — "
            "not lifting the cup, not "
            "ending the night, just "
            "holding him up inside it — "
            "heaven's answer arriving as "
            "presence, solid enough to "
            "lean against. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r091-b25", "out": "s25-answer-in-that-hour-was.jpeg", "seg": "n8",
        "window": "133.93-142.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE", "ANGEL"],
        "narration": (
            "God's answer, in that hour, was not to take the pain away. It "
            "was to come near, and hold him up, and give him what he needed "
            "to go on."
        ),
        "must_show": "the shape of the answer — close on the support: the angel's hands steady on him, Jesus's breathing steadying against the hold; strength transferring, pain remaining.",
        "must_not_show": "no wings, no ring of light, no light-outline; the pain NOT removed — visibly still there, now shared against.",
        "scene": (
            "Close on the shape God's "
            "answer took: the silver-grey "
            "figure's hands firm at his "
            "shoulders and back, and "
            "against that hold the "
            "shattered breathing slowly "
            "finding its floor — the "
            "anguish not lifted one ounce, "
            "the night not shortened one "
            "minute, but underneath the "
            "unremoved weight, strength "
            "arriving like bread: enough "
            "for the next breath, and the "
            "one after, all the way to "
            "morning. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b26", "out": "s26-he-was-not-abandoned.jpeg", "seg": "n8",
        "window": "142.30-144.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE", "ANGEL"],
        "narration": "He was not abandoned.",
        "must_show": "the not-alone — the two figures together in the moonlit dark: the held and the holding; abandonment refuted in one image.",
        "must_not_show": "no wings, no ring of light, no light-outline; the frame INTIMATE — two figures, one truth.",
        "scene": (
            "One picture answers the "
            "oldest fear: in the deep "
            "moonlit dark of the grove, "
            "two figures — the exhausted "
            "man and the strong quiet "
            "presence kneeling with him, "
            "shoulder under his arm, "
            "holding — the loneliest hour "
            "ever suffered on earth, and "
            "even it, even here, not "
            "actually alone: heaven's arm "
            "literally around the one "
            "carrying everything. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b27", "out": "s27-when-he-rose-and-came.jpeg", "seg": "n9",
        "window": "144.62-152.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": (
            "When he rose and came back to his three friends, he found them "
            "fast asleep. Not from carelessness — Luke says they were "
            "sleeping for sorrow."
        ),
        "must_show": "SCRIPTURE-EXACT: sleeping for sorrow — Jesus standing over the three collapsed sleepers among the roots: grief-worn faces slack, bodies fallen rather than settled.",
        "must_not_show": "no halo, glare or rim-light; the sleep GRIEF'S — tear-tracked, fallen-where-they-sat; no comic snoring.",
        "scene": (
            "He comes back to find sorrow "
            "has done what watchfulness "
            "could not fight: the three "
            "fallen asleep where grief "
            "felled them — Peter slumped "
            "sideways against a trunk with "
            "his mouth open, James and "
            "John collapsed together like "
            "dropped cloaks, tear-tracks "
            "dried on the young face — not "
            "carelessness but casualties, "
            "hearts worn past keeping "
            "their own eyes open, while he "
            "stands over them in the "
            "moonlight, looking down. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b28", "out": "s28-their-own-grief-had-worn.jpeg", "seg": "n9",
        "window": "152.85-158.18", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": (
            "Their own grief had worn them out. He had asked them to watch "
            "with him, and they could not."
        ),
        "must_show": "the failure looked at — close on Jesus's face regarding the sleepers: disappointment present, condemnation absent; the could-not understood.",
        "must_not_show": "no halo, glare or rim-light; NO anger — sorrow meeting weakness with comprehension.",
        "scene": (
            "Close on his face as he looks "
            "down at what he asked for and "
            "did not get: the one small "
            "request of the night — watch "
            "with me — asleep at his feet "
            "— and in the moonlit features "
            "not one line of condemnation: "
            "disappointment, yes, the "
            "loneliness deepened another "
            "shade, but over it the "
            "comprehension of a maker who "
            "knows exactly what clay can "
            "and cannot do at midnight. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b29", "out": "s29-watch-and-pray-that-ye.jpeg", "seg": "jv41",
        "window": "158.72-166.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN"],
        "narration": (
            "Watch and pray, that ye enter not into temptation: the spirit "
            "indeed is willing, but the flesh is weak."
        ),
        "must_show": "SCRIPTURE-EXACT: the gentle waking — Jesus crouched to the blinking, shame-faced three, the words given as diagnosis and mercy in one.",
        "must_not_show": "no halo, glare or rim-light; the waking GENTLE — a hand on a shoulder, no shaking.",
        "scene": (
            "He wakes them the gentle way: "
            "crouched down to their level "
            "with a hand on Peter's "
            "shoulder, waiting out the "
            "blinking and the shame "
            "flooding up the fisherman's "
            "face — and giving them, "
            "instead of the rebuke they "
            "brace for, the kindest "
            "diagnosis ever written: THE "
            "SPIRIT IS WILLING, THE FLESH "
            "IS WEAK — their failure "
            "explained to them tenderly by "
            "its chief casualty. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b30", "out": "s30-my-soul-is-exceeding-sorrowful.jpeg", "seg": "jv38",
        "window": "47.45-53.16", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": (
            "My soul is exceeding sorrowful, even unto death: tarry ye here, "
            "and watch with me."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — Jesus speaking it directly to the three's faces: EXCEEDING SORROWFUL, EVEN UNTO DEATH; the tarry-and-watch entrusted.",
        "must_not_show": "no halo, glare or rim-light; the words UNSOFTENED — the three receiving a sentence too heavy for them.",
        "scene": (
            "He gives the three the whole "
            "truth in one sentence: MY "
            "SOUL IS EXCEEDING SORROWFUL — "
            "EVEN UNTO DEATH — the words "
            "passing into their faces like "
            "cold water, Peter's jaw "
            "loosening, John going pale in "
            "the moonlight — and then the "
            "commission laid into their "
            "hands like something "
            "breakable: TARRY YE HERE, AND "
            "WATCH WITH ME — the night's "
            "whole asking, entrusted to "
            "flesh. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b31", "out": "s31-he-woke-them-but-he.jpeg", "seg": "n10",
        "window": "167.87-172.46", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": (
            "He woke them, but he did not scold them. He understood exactly "
            "what they were made of."
        ),
        "must_show": "the no-scold — the woken three sitting up shame-faced among the roots, and Jesus's posture over them all gentleness; understanding in place of rebuke.",
        "must_not_show": "no halo, glare or rim-light; NO pointed finger, no turned back — mercy's body language only.",
        "scene": (
            "The scene the three will "
            "remember all their lives: "
            "caught failing, sitting up "
            "shame-faced in the roots with "
            "sleep still on them — and "
            "over them not one gesture of "
            "the scold: his hand steadying "
            "James's shoulder as he rises, "
            "his face holding nothing to "
            "make the shame worse — a "
            "maker reviewing exactly what "
            "he made them of, and loving "
            "them inside its limits. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r091-b32", "out": "s32-their-hearts-longed-to-be.jpeg", "seg": "n10",
        "window": "172.46-177.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN"],
        "narration": (
            "Their hearts longed to be faithful; their tired bodies simply "
            "gave out."
        ),
        "must_show": "the two truths — close on the woken faces: love and mortification together; willing spirits reading their own weak flesh.",
        "must_not_show": "no halo, glare or rim-light; BOTH legible — devotion real, exhaustion real, neither cancelling the other.",
        "scene": (
            "Close on the two truths "
            "sharing the woken faces: in "
            "Peter's eyes the fierce "
            "loyalty that would die for "
            "him before dawn asks its "
            "question, and under it the "
            "gray exhaustion that could "
            "not keep one hour's watch; "
            "John's young features the "
            "same war in softer lines — "
            "hearts fully willing, bodies "
            "fully spent, and both facts "
            "written on the same skin at "
            "once. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r091-b33", "out": "s33-he-knew-the-difference-and.jpeg", "seg": "n10",
        "window": "177.21-183.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JOHN"],
        "narration": (
            "He knew the difference, and he was tender with them even now, "
            "on the worst night of his life."
        ),
        "must_show": "the tenderness — a small gesture held close: Jesus drawing a cloak up over John's shoulders as the young man settles again; care spent outward from inside the agony.",
        "must_not_show": "no halo, glare or rim-light; the gesture SMALL and domestic — a blanket, on the worst night.",
        "scene": (
            "The smallest gesture of the "
            "night, kept close: Jesus's "
            "own hands drawing the fallen "
            "cloak up over John's shoulders "
            "as the young man sags back "
            "into sleep — tucking it at "
            "the neck against the cold, "
            "the way a mother does — a man "
            "with the world coming down "
            "on him in an hour, spending "
            "his own broken minutes on "
            "keeping his friend warm. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b34", "out": "s34-he-went-back-and-prayed.jpeg", "seg": "n11",
        "window": "183.49-191.37", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "He went back and prayed again, and a third time, the very same "
            "words, until his heart was fully settled. The struggle was "
            "over."
        ),
        "must_show": "SCRIPTURE-EXACT: the third praying — the kneeling figure again at the same worn place, posture now steadier; repetition wearing the struggle down to settlement.",
        "must_not_show": "no halo, glare or rim-light; the CHANGE visible against b20 — same place, same words, spine straighter, storm passing.",
        "scene": (
            "Back at the same worn patch "
            "of earth the same words go up "
            "a third time — and the frame "
            "shows what repetition has "
            "won: the kneeling spine "
            "straighter than an hour ago, "
            "the hands open now instead of "
            "fisted, the breathing long "
            "and level in the cold air — "
            "the same prayer wearing the "
            "same channel until the flood "
            "ran through it clean — a "
            "heart arriving, at last, "
            "fully settled. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r091-b35", "out": "s35-he-had-looked-straight-at.jpeg", "seg": "n11",
        "window": "191.37-196.52", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "He had looked straight at everything that was coming, and he "
            "had said yes to his Father anyway."
        ),
        "must_show": "the yes — close on the risen face in the moonlight: cleared, resolved, unafraid; the anguish passed through, not around.",
        "must_not_show": "no halo, glare or rim-light; the peace EARNED — traces of the night still on him, resolve over them.",
        "scene": (
            "Close on the face the "
            "struggle left behind: the "
            "tear-salt and sweat of the "
            "night still marking it, the "
            "exhaustion real in the eyes — "
            "and over all of it, settled "
            "like weather clearing, the "
            "YES: a resolve with no "
            "flinch left in it, the look "
            "of a man who stared down the "
            "entire bill, read every "
            "line, and signed — anyway, "
            "and on purpose. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r091-b36", "out": "s36-he-rose-from-that-place.jpeg", "seg": "n11 + jv46",
        "window": "196.52-204.36", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": (
            "He rose from that place resolved. Rise, let us be going: "
            "behold, he is at hand that doth betray me."
        ),
        "must_show": "SCRIPTURE-EXACT: rise, let us be going — Jesus on his feet rousing the three, his arm toward the valley; command and calm together, the hour arrived.",
        "must_not_show": "no halo, glare or rim-light; the rousing URGENT but steady — a commander's wake-up, not panic.",
        "scene": (
            "He is on his feet and the "
            "night changes gear: RISE — "
            "the three shaken awake to "
            "his voice gone steady as "
            "bedrock, his arm already out "
            "toward the valley where the "
            "hour is climbing — LET US BE "
            "GOING — no tremor left "
            "anywhere in him, the man who "
            "knelt shaking an hour ago now "
            "waking his friends with the "
            "calm of a captain whose "
            "course is set, because it is. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r091-b37", "out": "s37-but-even-in-his-agony.jpeg", "seg": "n6",
        "window": "99.25-102.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "But even in his agony he did not stop there.",
        "must_show": "the not-stopping — the praying figure pressing past the asking into the deeper clause; continuation visible in the unbroken posture.",
        "must_not_show": "no halo, glare or rim-light; the prayer CONTINUING — no rising, no turning away from it.",
        "scene": (
            "The prayer does not end at "
            "the asking: the kneeling "
            "figure stays down past his "
            "own request, pressing on into "
            "the harder clause the way a "
            "swimmer pushes past the "
            "reef-line into deep water — "
            "the honest IF-THOU-BE-WILLING "
            "already spoken, and the body "
            "in the moonlight visibly "
            "going further, toward the "
            "NEVERTHELESS that will hold "
            "up the world. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r091-b38", "out": "s38-across-the-valley-torches-were.jpeg", "seg": "n12",
        "window": "205.84-213.98", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Across the valley, torches were already winding up the hill — "
            "the men who had come to arrest him. He did not run, and he did "
            "not hide."
        ),
        "must_show": "SCRIPTURE-EXACT: the torches — the black valley threaded with a distant winding line of torch-points climbing toward the grove; Jesus watching it come, planted.",
        "must_not_show": "ABSOLUTE: the party DISTANT — points of firelight only, no faces, no weapons detailed; Jesus's stance unmoving.",
        "scene": (
            "From the grove's edge the "
            "night shows him what is "
            "coming for him: down across "
            "the black valley a thin "
            "winding thread of torch-fire, "
            "climbing — point after point "
            "swinging up the far path in "
            "no particular hurry, certain "
            "of its errand — and at the "
            "terrace wall Jesus stands "
            "planted and watching it "
            "come, his feet exactly where "
            "they are, the moonlight "
            "finding no flight anywhere in "
            "his body. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r091-b39", "out": "s39-he-woke-his-friends-and.jpeg", "seg": "n12",
        "window": "213.98-217.10", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE", "PETER", "JAMES-Z", "JOHN"],
        "narration": "He woke his friends, and he walked out to meet it.",
        "must_show": "the walking-to-meet — Jesus striding down toward the grove's gate ahead of the scrambling three, toward the far torchlight; the meeting chosen.",
        "must_not_show": "no halo, glare or rim-light; HIS the leading stride — the three behind, the torches still distant points.",
        "scene": (
            "He leads the way toward it: "
            "striding down through the "
            "moonlit trunks ahead of the "
            "three still scrambling up "
            "from sleep behind him, his "
            "face set toward the gate and "
            "the far climbing fire-points "
            "beyond it — not marched out, "
            "not dragged, not found — a "
            "man walking open-eyed down "
            "his own garden path to meet "
            "the thing he just finished "
            "saying yes to. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r091-b40", "out": "s40-he-did-it-on-purpose.jpeg", "seg": "n12",
        "window": "222.04-224.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "He did it on purpose. He did it for us.",
        "must_show": "the closing image — close on the resolved face at the grove's gate in the moonlight: purpose and love in the same steady features; the FOR US carried in the eyes.",
        "must_not_show": "no halo, glare or rim-light; the face STEADY to the last frame — chosen, not endured.",
        "scene": (
            "The closing frame holds the "
            "face at the gate: moonlit, "
            "marked by the night, and "
            "utterly steady — the eyes "
            "carrying both halves of the "
            "sentence at once: ON PURPOSE, "
            "in the set of the jaw that "
            "no torch-line can turn; FOR "
            "US, in the warmth that all "
            "the anguish never burned out "
            "of the brown eyes — a man "
            "stepping through his garden "
            "gate carrying the reason, "
            "which was always people. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
]
