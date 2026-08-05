#!/usr/bin/env python3
"""V2 beat map — row 110, build-110-lords-prayer (Luke 11:1; Matthew 6:7-13).

COVERAGE: 23 pictures over 130.4 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  Luke 11:1  "as he was PRAYING IN A CERTAIN PLACE, when he ceased,
        one of his disciples said... LORD, TEACH US TO PRAY, as John
        also taught his disciples."
  Matt 6:9-13 the prayer itself: OUR FATHER — hallowed — kingdom come
        — will be done — DAILY BREAD — forgive AS WE FORGIVE — lead
        us not — deliver — thine is the kingdom, power, glory.
  Matt 6:7  the warning before it: "use not VAIN REPETITIONS... they
        think that they shall be heard for their MUCH SPEAKING."
  Matt 6:5  the corner-performer: prays "standing... in the corners
        of the streets, that they may BE SEEN of men."

STAGING: the teaching in a quiet olive place at soft morning; the
petition beats illustrated with small domestic vignettes (bread on a
table, two neighbours reconciling, a child in a father's lap); the
corner-performer shown kindly, not cartooned.

TIME OF DAY: soft clear morning throughout; the child-lap and close
beats in warm gold.

CONTENT-CARE: no flags. "Deliver us from evil" carried by shelter
imagery only — nothing embodied, no dark figure.

CHANGING CONDITION (kept OUT of the locks): the disciples — watching
him pray, then asking, then learning; the prayer — line by line, each
with its picture.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream.
LOCKS = {
    "PLACE": (
        "PLACE LOCK: the certain place — a quiet olive terrace in "
        "soft morning light: old trunks, low dry-stone wall, a worn "
        "flat prayer-stone, the valley hazy below. The same terrace "
        "throughout."
    ),
    "HOME": (
        "HOME LOCK: the vignette home — a small village room: low "
        "table, bread oven's mouth, one deep window of warm light. "
        "The same room throughout."
    ),
    "FATHER": (
        "FATHER LOCK: the vignette father is the same man in every "
        "such shot — about thirty-five, short dark beard, kind "
        "tired eyes, in a DARK RUST-BROWN tunic (never cream, never "
        "white)."
    ),
    "CHILD": (
        "CHILD LOCK: the vignette child is the same small girl in "
        "every such shot — about four, dark curls, in a little DEEP "
        "MADDER-RED dress (never cream, never white); trusting and "
        "chatty."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r110-b01", "out": "s01-one-day-his-followers-asked.jpeg", "seg": "n1 + s11",
        "window": "0.28-6.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLACE", "PETER", "JOHN"],
        "narration": (
            "One day his followers asked him a simple question. Lord, teach "
            "us to pray, as John also taught his disciples."
        ),
        "must_show": "SCRIPTURE-EXACT: the ask after his praying — Jesus rising from the prayer-stone, the watching disciples close with the request on their faces; teach US that.",
        "must_not_show": "no halo, glare or rim-light; their watching HUNGRY — men who saw something they want.",
        "scene": (
            "The request is born from watching, the camera on the "
            "slope's side taking riser and watchers in one profile: "
            "watching: Jesus rising easy "
            "from the worn flat stone "
            "where he has been praying "
            "in the soft morning light — "
            "and the disciples close by "
            "with the hunger plain on "
            "their faces: whatever that "
            "was, whatever he has with "
            "heaven when he kneels "
            "there — LORD, TEACH US "
            "THAT — Peter's voice "
            "carrying the ask for all "
            "of them, students "
            "applying for the one "
            "class that matters. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b02", "out": "s02-they-expected-maybe-a-technique.jpeg", "seg": "n1b",
        "window": "8.37-11.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN"],
        "narration": "They expected, maybe, a technique. A ritual.",
        "must_show": "the expectation — the disciples readying to memorize: earnest faces set for complexity, fingers ready to count steps; braced for a system.",
        "must_not_show": "no halo, glare or rim-light; the bracing STUDIOUS — men expecting homework.",
        "scene": (
            "Close on students braced "
            "for a system: John's young "
            "face set to memorize, "
            "Peter's brow furrowed for "
            "complexity, another "
            "disciple's fingers already "
            "half-raised to count off "
            "the expected steps — "
            "postures, hours, washings, "
            "the proper order of the "
            "sacred words — a row of "
            "earnest faces prepared "
            "for a heavy curriculum, "
            "about to receive "
            "something the size of a "
            "child's goodnight. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b03", "out": "s03-instead-jesus-gave-them-a.jpeg", "seg": "n1b + jv9a",
        "window": "11.26-16.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PLACE"],
        "narration": (
            "Instead, Jesus gave them a family word. After this manner "
            "therefore pray ye:"
        ),
        "must_show": "the family word coming — close on Jesus's warm face beginning the teaching: intimacy where technique was expected; the first word already forming.",
        "must_not_show": "no halo, glare or rim-light; the register DOMESTIC — a family matter, not a rite.",
        "scene": (
            "Close on the curriculum "
            "confounding its students: "
            "Jesus's face warm and "
            "almost amused as he "
            "begins — no list coming, "
            "no ladder of techniques — "
            "the first word already "
            "shaping on his lips being "
            "not a formula's opening "
            "but a family word, the "
            "kind spoken across supper "
            "tables and shouted from "
            "courtyards — prayer about "
            "to be taught the way you "
            "teach a child the name "
            "for its own house. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b04", "out": "s04-our-father-which-art-in.jpeg", "seg": "jv9",
        "window": "18.29-23.13", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PLACE", "PETER", "JOHN"],
        "narration": (
            "Our Father which art in heaven, Hallowed be thy name. Thy "
            "kingdom come."
        ),
        "must_show": "SCRIPTURE-EXACT: the prayer begun — Jesus praying it slowly for them, face lifted; the disciples' lips beginning to move after his, learning line one.",
        "must_not_show": "no halo, glare or rim-light; the learning VISIBLE — lips following, the prayer passing mouth to mouth.",
        "scene": (
            "The prayer is taught the "
            "way songs are: Jesus "
            "praying it slowly with "
            "his face lifted to the "
            "soft sky — OUR FATHER — "
            "and around him on the "
            "terrace the lips beginning "
            "to move after his, half a "
            "beat behind: Peter's "
            "mouth shaping FATHER "
            "like a man tasting new "
            "bread, John's young voice "
            "just audible on HALLOWED — "
            "the family word going "
            "mouth to mouth down the "
            "morning, first of a "
            "billion recitations. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r110-b05", "out": "s05-thy-will-be-done-in.jpeg", "seg": "jv9",
        "window": "23.13-26.60", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Thy will be done in earth, as it is in heaven.",
        "must_show": "SCRIPTURE-EXACT: earth as heaven — a wide good-earth frame: terraced fields being worked in morning light under a vast serene sky; the two realms rhyming.",
        "must_not_show": "no halo; the rhyme COMPOSITIONAL — ordered sky over ordered fields, peace above and below.",
        "scene": (
            "The line gets its landscape, the camera high on the "
            "terrace so every worker bends away from the lens at his own row: "
            "below, the terraced fields "
            "in morning light — a "
            "ploughman laying his "
            "straight dark furrows, "
            "women sowing in easy "
            "rhythm, order and bread "
            "being made — and above, "
            "the vast serene morning "
            "sky arranged like a "
            "kingdom at peace — the "
            "two halves of the frame "
            "rhyming top to bottom, "
            "AS IT IS IN HEAVEN laid "
            "visibly over IN EARTH, "
            "the prayer's great hope "
            "drawn as weather. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b06", "out": "s06-not-a-distant-judge-not.jpeg", "seg": "n2",
        "window": "28.14-30.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": "Not a distant judge. Not a force.",
        "must_show": "the not-that — the vignette: the little girl running to her father's opening arms in the warm doorway; the word FATHER defined by its picture.",
        "must_not_show": "no halo; NOTHING judicial or abstract in frame — arms, doorway, running child.",
        "scene": (
            "The word gets defined by "
            "its picture: the small "
            "girl in her madder-red "
            "dress running full-tilt "
            "across the room at the "
            "man in the doorway — and "
            "the doorway already "
            "kneeling, arms already "
            "open, the catch as "
            "certain as sunrise — no "
            "bench, no gavel, no "
            "distant force anywhere in "
            "the warm light: just what "
            "FATHER has always meant "
            "at running-speed to "
            "someone four years old. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r110-b07", "out": "s07-and-the-very-first-thing.jpeg", "seg": "n2",
        "window": "33.13-44.49", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And the very first thing you long for, once you know him, is "
            "not for yourself at all — that his name be honoured, and his "
            "good kingdom come, everywhere."
        ),
        "must_show": "the outward longing — a praying figure on a rooftop at morning, face and open hands lifted OUT over the waking town: the first petitions aimed at the world, not the self.",
        "must_not_show": "no halo; the direction OUTWARD — over the town, past the self.",
        "scene": (
            "The prayer's strange first "
            "movement, drawn: a lone "
            "figure on a flat rooftop "
            "at morning with hands "
            "open not around her own "
            "needs but OUT — over the "
            "waking town below, the "
            "smoking ovens, the "
            "children spilling into "
            "lanes, the whole "
            "unhallowed hurrying "
            "world — asking first, "
            "before bread, before "
            "anything: let them know "
            "your name here; let your "
            "good kingdom come to "
            "every roof I can see. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r110-b08", "out": "s08-a-father-you-belong-to.jpeg", "seg": "n2",
        "window": "30.99-33.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": "A Father you belong to.",
        "must_show": "the belonging — the girl settled on the father's hip like she grew there: possession mutual and total; belonging as posture.",
        "must_not_show": "no halo; the settledness ABSOLUTE — she rides his hip like home ground.",
        "scene": (
            "Close on what belonging "
            "looks like at four years "
            "old: the girl settled on "
            "her father's hip with the "
            "boneless certainty of a "
            "child on home ground — "
            "one small arm slung round "
            "his neck as by right, "
            "her cheek against his "
            "shoulder mid-chatter, his "
            "forearm the oldest seat "
            "she knows — not held so "
            "much as BELONGING, the "
            "way a branch belongs to "
            "its tree — the whole "
            "theology of OUR FATHER, "
            "riding one hip. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b09", "out": "s09-give-us-this-day-our.jpeg", "seg": "jv11",
        "window": "45.00-50.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME"],
        "narration": (
            "Give us this day our daily bread. And forgive us our debts, as "
            "we forgive our debtors."
        ),
        "must_show": "SCRIPTURE-EXACT: the daily bread — the day's plain loaf fresh from the oven's mouth on the low table, steam rising in the window light; enough, for today.",
        "must_not_show": "no halo; ONE day's bread only — no stockpile; the sufficiency the picture.",
        "scene": (
            "The petition sits steaming "
            "on the table: one day's "
            "loaf, just drawn from the "
            "oven's warm mouth, its "
            "steam curling up through "
            "the deep window's morning "
            "light — not a granary, "
            "not a week's stack, not "
            "wealth: today's bread for "
            "today's table, asked for "
            "and arrived — the whole "
            "honest scale of the "
            "prayer's wanting, golden "
            "and plain and enough, "
            "with tomorrow left "
            "trustingly unbaked. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b10", "out": "s10-then-the-plain-honest-things.jpeg", "seg": "n3",
        "window": "52.16-58.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": (
            "Then the plain, honest things. Bread — it is fine to ask for "
            "the ordinary needs of the day."
        ),
        "must_show": "the ordinary sanctioned — the family at the plain meal in window light: bread broken, cups filled; the ordinary need met and holy.",
        "must_not_show": "no halo; the meal MODEST — dignity of the everyday, nothing fancy.",
        "scene": (
            "Permission arrives at an "
            "ordinary table: the little "
            "family at their plain "
            "meal in the window's warm "
            "light — the loaf broken "
            "and passing, water poured, "
            "the girl's cup steadied "
            "by her father's finger — "
            "nothing on the table any "
            "market would notice, and "
            "all of it now officially "
            "worth praying about: the "
            "ordinary hungers of an "
            "ordinary day, welcome by "
            "name at the throne of "
            "heaven. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r110-b11", "out": "s11-and-forgiveness-asked-for-and.jpeg", "seg": "n3",
        "window": "58.37-61.63", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And forgiveness — asked for, and passed on.",
        "must_show": "the two-way mercy — a village lane vignette: two neighbours mid-reconciliation, hands clasping over an old grievance, wives and children watching relief break out.",
        "must_not_show": "no halo; BOTH faces relieved — forgiveness landing on giver and receiver alike.",
        "scene": (
            "In the village lane an old "
            "grievance dies in "
            "daylight: two neighbours — "
            "stiff with each other "
            "since the boundary-stone "
            "quarrel — meeting at last "
            "in the middle ground, "
            "hands clasping rough and "
            "sudden, the apology and "
            "the pardon arriving in "
            "the same shake — and "
            "around them the relief "
            "breaking out in the "
            "watching doorways: wives' "
            "shoulders dropping, a "
            "child released to play "
            "with the other yard's "
            "children again. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b12", "out": "s12-we-receive-mercy-with-the.jpeg", "seg": "n3",
        "window": "61.63-65.81", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "We receive mercy with the same hands we use to give it away.",
        "must_show": "the same hands — close on two pairs of hands: one open receiving, one open giving, in the same warm light; mercy's single current.",
        "must_not_show": "no halo; the HANDS the whole image — receiving and giving as one motion.",
        "scene": (
            "Close on mercy's plumbing: "
            "two pairs of hands in the "
            "same warm light — one "
            "pair open and upturned, "
            "receiving, and the same "
            "worn pair a breath later "
            "turned outward, passing "
            "it on to a third — the "
            "current running through, "
            "not pooling: pardon "
            "arriving and leaving by "
            "the same palms, the way "
            "a channel is filled only "
            "while it flows — asked "
            "for, and passed on, one "
            "unbroken motion. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b13", "out": "s13-and-lead-us-not-into.jpeg", "seg": "jv13",
        "window": "66.34-75.61", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And lead us not into temptation, but deliver us from evil: For "
            "thine is the kingdom, and the power, and the glory, forever."
        ),
        "must_show": "SCRIPTURE-EXACT: the leading and keeping — a father leading his small son by the hand ALONG the safe high path, the crumbling edge passed by below; shelter as guidance.",
        "must_not_show": "ABSOLUTE: nothing embodied as evil — the danger only a crumbling drop passed safely; no dark figure.",
        "scene": (
            "The last petitions walk a "
            "mountain path: a father "
            "leading his small son by "
            "the hand along the high "
            "trail — choosing the "
            "inside line without a "
            "word, his body between "
            "the boy and the crumbling "
            "drop that falls away "
            "below — the danger passed "
            "not fought: steered "
            "around, outwalked, made "
            "irrelevant by a hand that "
            "knows the way — LEAD US "
            "NOT — DELIVER US — "
            "guidance as the oldest "
            "form of rescue. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b14", "out": "s14-amen-keep-me-safe.jpeg", "seg": "jv13 + n4",
        "window": "75.61-79.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": "Amen. Keep me safe.",
        "must_show": "the amen — the girl's bedtime: small hands folded under her father's larger ones in the lamplight, the day's prayer sealed; safety asked and granted at once.",
        "must_not_show": "no halo; the scene TINY and complete — a child's amen, fully sufficient.",
        "scene": (
            "The great prayer ends the "
            "size it started: bedtime "
            "in the lamplight, the "
            "girl's small hands folded "
            "and her father's larger "
            "ones cupped warm around "
            "them, her whispered amen "
            "still in the air — KEEP "
            "ME SAFE — four words and "
            "a nod, the whole "
            "cathedral of the teaching "
            "scaled down to one "
            "lamplit bed and found "
            "not one stone smaller — "
            "sealed, heard, and "
            "already granted. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b15", "out": "s15-lead-me-away-from-what.jpeg", "seg": "n4",
        "window": "79.34-85.59", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PLACE"],
        "narration": (
            "Lead me away from what would harm me. And it ends where it "
            "began — with him: Short."
        ),
        "must_show": "the return to him — the olive terrace again: Jesus finishing the taught prayer with the disciples, the circle complete; brevity visible in the morning's stillness.",
        "must_not_show": "no halo, glare or rim-light; the ENDING quiet — a short prayer fully landed.",
        "scene": (
            "The teaching comes home to "
            "its terrace: Jesus letting "
            "the last line settle over "
            "the ring in the soft "
            "morning stillness — the "
            "whole prayer said, "
            "beginning to end, in less "
            "time than a man needs to "
            "draw water — and the "
            "disciples sitting inside "
            "the shortness of it, "
            "checking almost comically "
            "for the rest, finding "
            "instead that everything "
            "got said — begun with "
            "Father, ended with him "
            "too, and nothing missing "
            "between. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r110-b16", "out": "s16-honest-nothing-showy.jpeg", "seg": "n4",
        "window": "85.59-88.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLACE", "PETER"],
        "narration": "Honest. Nothing showy.",
        "must_show": "the plain prayer worn — Peter trying the prayer himself on the terrace, halting and honest, eyes closed; unadorned praying begun.",
        "must_not_show": "no halo, glare or rim-light; the attempt HALTING — a big man's first plain prayer, precious for its plainness.",
        "scene": (
            "Close on the teaching "
            "taking its first steps: "
            "Peter with his eyes shut "
            "on the terrace, trying it "
            "himself — the big "
            "fisherman's lips working "
            "slow through OUR FATHER "
            "like a man walking a new "
            "plank bridge, no flourish "
            "anywhere, one halting "
            "honest line at a time — "
            "nothing showy possible "
            "in him and nothing showy "
            "needed: prayer, plain as "
            "rope, already holding "
            "his whole weight. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b17", "out": "s17-but-when-ye-pray-use.jpeg", "seg": "jv7",
        "window": "88.86-97.36", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLACE"],
        "narration": (
            "But when ye pray, use not vain repetitions, as the heathen do: "
            "for they think that they shall be heard for their much "
            "speaking."
        ),
        "must_show": "SCRIPTURE-EXACT: the warning — Jesus teaching it with a gentle dismissing wave; in the middle distance a street-corner declaimer mid-performance, arms theatrical, admirers around.",
        "must_not_show": "no halo, glare or rim-light; the performer KINDLY drawn — earnest error, not villainy.",
        "scene": (
            "The warning points gently down the hill, the camera "
            "behind the listening ring toward the far street: "
            "down the hill: from the "
            "terrace Jesus's hand makes "
            "its soft dismissing wave "
            "toward the town below, "
            "where at a street corner "
            "a robed declaimer stands "
            "mid-performance — arms "
            "flung theatrical, voice "
            "visibly enormous, a small "
            "ring of admirers "
            "collecting like an "
            "audience — much speaking, "
            "beautifully produced, "
            "aimed at every ear in "
            "the street except the "
            "One being addressed. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r110-b18", "out": "s18-that-was-his-warning-just.jpeg", "seg": "n5",
        "window": "98.86-103.39", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "That was his warning, just before this: prayer is not a performance.",
        "must_show": "the performance retired — the corner-declaimer's props at rest: the fine prayer shawl folded on a bench, the corner empty in plain light; theatre closed.",
        "must_not_show": "no halo; no mockery — just the empty stage and folded costume, quietly eloquent.",
        "scene": (
            "The frame closes the "
            "theatre kindly: the street "
            "corner empty now in plain "
            "unspectacular light, the "
            "fine tasselled prayer "
            "shawl folded neat on the "
            "stone bench where the "
            "audience used to stand — "
            "no performer, no admirers, "
            "the whole production "
            "quietly struck — because "
            "the real conversation, it "
            "turns out, was never "
            "playing this venue: it "
            "happens in rooms with "
            "the door shut, unbilled. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r110-b19", "out": "s19-not-many-clever-words-not.jpeg", "seg": "n5",
        "window": "103.39-107.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME"],
        "narration": "Not many clever words, not standing on a corner to be admired.",
        "must_show": "the shut door — the home's simple door closed with warm lamplight under it: the secret room where real prayer lives; privacy as intimacy.",
        "must_not_show": "no halo; the door's WARMTH — light under it, presence within implied.",
        "scene": (
            "The real venue announces "
            "itself by a line of light: "
            "the home's plain wooden "
            "door shut on the evening, "
            "and beneath it, along the "
            "worn threshold, warm "
            "lamplight seeping gold — "
            "someone inside, unseen and "
            "unadmired, talking to "
            "their Father with the "
            "door closed exactly as "
            "taught — no audience, no "
            "cleverness, no corner — "
            "and the light under the "
            "door somehow the fullest "
            "picture of prayer in the "
            "whole row. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r110-b20", "out": "s20-the-prayer-god-loves-most.jpeg", "seg": "n5 + n6",
        "window": "107.24-113.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "CHILD"],
        "narration": (
            "The prayer God loves most may be the simplest one a child ever "
            "whispered. That is really all it is."
        ),
        "must_show": "the simplest prayer — the girl kneeling alone at her small bed, whispering with her eyes squeezed shut; heaven's favourite genre.",
        "must_not_show": "no halo; the whisper TINY and total — nothing else in the frame competing.",
        "scene": (
            "Close on heaven's favourite "
            "genre: the small girl "
            "kneeling at her low bed "
            "in the lamplight with her "
            "eyes squeezed shut in "
            "concentration, dark curls "
            "falling forward, the "
            "whisper moving her lips — "
            "words nobody will ever "
            "record, grammar heaven "
            "does not check — a prayer "
            "the length of a breath, "
            "aimed with total "
            "confidence, and received, "
            "somewhere, like treasure. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r110-b21", "out": "s21-not-a-speech-to-impress.jpeg", "seg": "n6",
        "window": "113.86-120.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": (
            "Not a speech to impress heaven. A child, climbing into the lap "
            "of a good Father, and simply talking to him."
        ),
        "must_show": "the lap — the girl climbed up into her father's lap in the warm evening light, mid-chatter, his whole attention hers; prayer's true picture.",
        "must_not_show": "no halo; the CLIMB hers — she got up there herself, welcome assumed.",
        "scene": (
            "The definition arrives in "
            "one warm picture: the girl "
            "climbing up into her "
            "father's lap by her own "
            "small determined effort — "
            "welcome so assumed it "
            "needs no asking — "
            "settling in against his "
            "chest and starting "
            "straight into the day's "
            "news, and the father's "
            "whole attention coming "
            "down around her like a "
            "blanket — no speech, no "
            "impressing, no distance "
            "to cross: a lap, and "
            "talking — which is the "
            "entire doctrine. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b22", "out": "s22-so-you-do-not-need.jpeg", "seg": "n7",
        "window": "121.53-125.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME"],
        "narration": "So you do not need the right words. You only need to begin.",
        "must_show": "the beginning — a lamplit corner with a waiting stillness: a chair, the window's evening; a place to simply start; invitation spatial.",
        "must_not_show": "no halo; the frame UNOCCUPIED and warm — the beginning left for the viewer.",
        "scene": (
            "The frame sets out the only "
            "requirement: a quiet "
            "lamplit corner of the "
            "room — the low chair by "
            "the window, the evening "
            "settling blue outside, "
            "the lamp's small gold "
            "steady on the plaster — "
            "no book of right words "
            "laid out, no script on "
            "the sill, nothing needed "
            "in the waiting stillness "
            "but somebody willing to "
            "sit down and begin — the "
            "chair angled, ever so "
            "slightly, toward whoever "
            "is looking at it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r110-b23", "out": "s23-and-the-beginning-is-just.jpeg", "seg": "n7",
        "window": "125.11-130.12", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PLACE"],
        "narration": (
            "And the beginning is just two words, the ones he gave them "
            "first of all: Our Father."
        ),
        "must_show": "the closing image — the olive terrace in gold light: Jesus and the disciples praying it together, the two first words on every mouth; the family word, shared out forever.",
        "must_not_show": "no halo, glare or rim-light; the TOGETHERNESS the close — one prayer, many mouths, begun.",
        "scene": (
            "The closing frame prays, the camera outside the "
            "circle behind the bowed shoulders: "
            "the terrace gone gold "
            "with late light, Jesus "
            "and the ring of disciples "
            "with heads bowed together, "
            "and on every mouth the "
            "same two words moving — "
            "OUR FATHER — Peter's "
            "gravel and John's youth "
            "and the teacher's warmth "
            "braided into one beginning "
            "— the family word handed "
            "out for good, already on "
            "its way from this hillside "
            "to every language and "
            "bedside and foxhole on "
            "earth. Every figure has "
            "two arms, two hands and "
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
