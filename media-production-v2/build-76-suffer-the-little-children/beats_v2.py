#!/usr/bin/env python3
"""V2 beat map — row 76, build-76-suffer-the-little-children (Mark 10:13-16).

COVERAGE: 14 pictures over 81.2 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 10:13-16 KJV):
  v13   "they BROUGHT young children to him, that he should TOUCH them:
        and his disciples REBUKED those that brought them" — parents with
        babies and small children; the disciples' wave-off is officious
        protectiveness, not malice.
  v14   "when Jesus SAW it, he was MUCH DISPLEASED" — Mark's unsoftened
        anger: the one recorded displeasure aimed at his own men, on the
        children's behalf. "SUFFER the little children to come unto me,
        and FORBID THEM NOT: for OF SUCH is the kingdom of God."
  v15   "Whosoever shall not receive the kingdom of God AS A LITTLE
        CHILD, he shall not enter therein" — the open-hands doctrine.
  v16   "he TOOK THEM UP IN HIS ARMS, put his hands upon them, and
        blessed them" — the gathering-up: children IN his arms, hands ON
        heads, one at a time, unhurried. + the HUSH: the row ends inside
        that unhurried blessing.

TIME OF DAY: one warm late afternoon throughout — golden roadside
light; the closing blessing in the day's deepest gold.

CONTENT-CARE: pure warmth; the disciples' rebuke painted as officious
busyness, their correction received sheepishly; children real and
various — a baby, a toddler, a shy one, a bold one.

CHANGING CONDITION (kept OUT of the locks): the children's approach —
held back, released, running, gathered, blessed; and the disciples —
barring, corrected, sheepishly helping.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "FAMILIES": (
        "FAMILIES LOCK: the parents and children — young mothers with "
        "babies in arm-slings, fathers carrying toddlers on shoulders, "
        "a grandmother leading twins, children from babes to about "
        "seven years old, in small SATURATED DEEP earth-colour tunics "
        "and dresses: dark russet, dusty indigo, deep olive, faded "
        "plum (never cream, never white; only Jesus wears cream). "
        "Faces shown clearly — among them ONE BOLD little girl of "
        "about four in a dark madder-red dress and ONE SHY boy of "
        "about six in dusty indigo who hides behind legs."
    ),
    "ROADSIDE": (
        "ROADSIDE LOCK: a warm roadside stopping place — a low "
        "dry-stone wall along a dirt road, an old spreading olive "
        "tree's shade, a flat sitting-stone beneath it, and terraced "
        "fields falling away golden behind. The same wall, tree and "
        "stone throughout. Late golden afternoon light."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r076-b01", "out": "s01-parents-were-bringing-their-little.jpeg", "seg": "n0",
        "window": "0.28-6.27", "wide": True, "jesus": True, "ref": REF,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": (
            "Parents were bringing their little kids to Jesus, just so he could "
            "put his hands on them and bless them."
        ),
        "must_show": "SCRIPTURE-EXACT: the bringing — families converging on the roadside where Jesus sits: babies slung, toddlers shouldered, small hands led; the simple hope visible.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the parents' hope plain — nothing asked but a touch.",
        "scene": (
            "Down the golden road, the camera off the verge taking "
            "the converging walks in profile, the families come "
            "converging on the olive tree's shade — a "
            "young mother with her baby in its "
            "arm-sling, a father with a toddler "
            "riding his shoulders, the grandmother "
            "leading her twins by both hands — all of "
            "them aimed at the flat stone where Jesus "
            "sits in the late light, carrying nothing "
            "to ask and nothing to offer except small "
            "children and the hope of a hand laid on "
            "each head. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b02", "out": "s02-and-they-brought-young-children.jpeg", "seg": "s13",
        "window": "6.84-13.39", "wide": True, "jesus": False, "ref": False,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": (
            "And they brought young children to him, that he should touch them: "
            "and his disciples rebuked those that brought them."
        ),
        "must_show": "SCRIPTURE-EXACT: the rebuke — two disciples interposed between families and teacher, arms out in the officious wave-off; parents checked mid-step, children confused.",
        "must_not_show": "no halo, glare or rim-light; the disciples OFFICIOUS not cruel — schedule-keepers guarding what needs no guard.",
        "scene": (
            "Between the families and the olive shade, the camera "
            "at the roadside so the barricade line reads in "
            "profile, "
            "shade two disciples have planted "
            "themselves — arms out, palms pushing "
            "air, the officious geometry of men "
            "guarding a schedule — and the families "
            "check mid-step before them: the mother's "
            "sling clutched closer, the father's "
            "toddler gone quiet on his shoulders, "
            "the bold little girl in madder-red "
            "peering around the human barricade at "
            "the seated figure it is guarding from "
            "her. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r076-b03", "out": "s03-that-old-word-suffer-just.jpeg", "seg": "n3",
        "window": "40.76-43.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROADSIDE"],
        "narration": "That old word suffer just means let.",
        "must_show": "the word unlatched — a small still: the roadside wall's wooden field-gate standing OPEN on its post; LET, as an object.",
        "must_not_show": "no halo, glare or rim-light; one open gate — permission's plainest picture.",
        "scene": (
            "A small still in the golden light: the "
            "field-gate in the dry-stone wall standing "
            "fully open on its worn post — no latch "
            "dropped, no bar across, the way through "
            "as wide as the gate can make it — the "
            "old word's whole meaning hanging on one "
            "hinge: let. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b04", "out": "s04-the-disciples-tried-to-wave.jpeg", "seg": "n1",
        "window": "14.81-21.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILIES"],
        "narration": (
            "The disciples tried to wave them off — the Teacher is busy, this "
            "is grown-up work, not the place for children."
        ),
        "must_show": "the wave-off close — a disciple's shooing hands, and below them the shy boy retreating behind his mother's legs; importance misread, small person rebuffed.",
        "must_not_show": "no halo, glare or rim-light; the child's retreat the cost — officiousness measured at knee height.",
        "scene": (
            "Close at the barricade: a disciple's "
            "big fisherman hands making their "
            "shooing motion — busy, busy, not now — "
            "and below the gesture's wind the shy "
            "boy in dusty indigo retreats behind "
            "his mother's legs, one eye and one "
            "fist of her skirt all that remains "
            "visible of him — grown-up importance "
            "doing its accidental damage at exactly "
            "knee height. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b05", "out": "s05-and-mark-does-not-soften.jpeg", "seg": "n2",
        "window": "23.34-26.17", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADSIDE"],
        "narration": "And Mark does not soften how he took it.",
        "must_show": "the displeasure — close on Jesus's face at what he sees: the one recorded anger of its kind, gathering on the children's behalf; grieved indignation.",
        "must_not_show": "no halo, glare or rim-light; the anger CLEAN — displeasure without contempt, aimed at the barrier not the men.",
        "scene": (
            "Close on Jesus's face in the olive "
            "shade: the warmth going stern in real "
            "time — brows drawing, jaw setting, the "
            "eyes fixed past the camera on the "
            "wave-off in progress — Mark's unsoftened "
            "word arriving on the locked features as "
            "exactly itself: much displeased, on "
            "behalf of everyone in the scene shorter "
            "than a fence post. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b06", "out": "s06-but-when-jesus-saw-it.jpeg", "seg": "s14",
        "window": "26.74-30.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": "But when Jesus saw it, he was much displeased, and said unto them,",
        "must_show": "SCRIPTURE-EXACT: the intervention — Jesus risen from the stone, moving toward the barricade, the correction already leaving him; the disciples turning to its arrival.",
        "must_not_show": "no halo, glare or rim-light; the rising itself the rebuke's first word — the Teacher unbusying himself instantly.",
        "scene": (
            "Jesus is up off the sitting-stone and "
            "moving — the correction already in the "
            "air ahead of him — and the two "
            "barricading disciples turn to its "
            "arrival with their shooing hands dying "
            "mid-gesture: the busy schedule they "
            "were guarding walking straight past "
            "them toward the checked families, "
            "much displeased and entirely available. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r076-b07", "out": "s07-suffer-the-little-children-to.jpeg", "seg": "j1",
        "window": "32.32-39.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": (
            "Suffer the little children to come unto me, and forbid them not: "
            "for of such is the kingdom of God."
        ),
        "must_show": "SCRIPTURE-EXACT: THE sentence — Jesus's arms opening wide toward the held-back children as the words go out; the barricade dissolving; the bold girl already breaking loose.",
        "must_not_show": "no halo, glare or rim-light; the opening arms the whole doctrine — and one small runner already through.",
        "scene": (
            "The sentence and the opening arms "
            "arrive together: Jesus's arms spreading "
            "wide toward the checked families as "
            "the words carry down the road — the "
            "disciples stepping back out of a "
            "barricade that has just been "
            "overruled — and through the first gap, "
            "already loose, the bold little girl in "
            "madder-red comes running full-tilt "
            "across the gold light, arms up, first "
            "citizen of the reopened kingdom. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r076-b08", "out": "s08-let-them-come-stand-in.jpeg", "seg": "n3",
        "window": "43.21-46.09", "wide": True, "jesus": True, "ref": REF,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": "Let them come. Don't stand in their way.",
        "must_show": "the way cleared — the road to Jesus open now: children streaming past the stepped-aside disciples; the corrected geometry.",
        "must_not_show": "no halo, glare or rim-light; the disciples aside and abashed — traffic wardens of a route that needed none.",
        "scene": (
            "The way stands cleared, the camera behind the "
            "stepped-aside disciples: children "
            "streaming down the open golden road "
            "toward the olive shade — the twins "
            "hand in hand at a trot, the toddler "
            "set down and wobbling determinedly, "
            "the baby's sling bouncing on its "
            "hurrying mother — while at the verge "
            "the two disciples stand stepped-aside "
            "and sheepish, studying the wall's "
            "stones like men suddenly interested "
            "in masonry. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b09", "out": "s09-then-he-went-further.jpeg", "seg": "n3",
        "window": "46.09-47.59", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADSIDE"],
        "narration": "Then he went further.",
        "must_show": "the escalation coming — close on Jesus's face turning from welcome to teaching: the children gathered, and something larger arriving for the adults.",
        "must_not_show": "no halo, glare or rim-light; the pivot gentle — delight deepening into doctrine.",
        "scene": (
            "Close on Jesus in the deep gold: the "
            "welcome's warmth still full on his face "
            "and something further gathering behind "
            "it — the eyes lifting from the "
            "children pooling around his knees to "
            "the watching ring of adults, a teacher "
            "about to hand the grown-ups the "
            "hardest lesson on the road, using the "
            "smallest people on it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b10", "out": "s10-verily-i-say-unto-you.jpeg", "seg": "j2",
        "window": "48.23-56.35", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": (
            "Verily I say unto you, Whosoever shall not receive the kingdom of "
            "God as a little child, he shall not enter therein."
        ),
        "must_show": "SCRIPTURE-EXACT: the doctrine — Jesus speaking it over the gathered children's heads TO the adults: the ring of parents and disciples receiving the reversal; smallness enthroned.",
        "must_not_show": "no halo, glare or rim-light; the children unbothered and playing at his knees while their example is preached over them.",
        "scene": (
            "Over the heads of the children pooled "
            "at his knees Jesus gives the adults "
            "their doctrine — the ring of parents "
            "and corrected disciples receiving it "
            "standing, the reversal landing on "
            "grown faces one by one — while its "
            "living illustration goes on unbothered "
            "below: the twins comparing pebbles, "
            "the toddler working at his own "
            "sandal — the kingdom's entrance "
            "requirements, playing in the dust. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r076-b11", "out": "s11-he-meant-nobody-earns-their.jpeg", "seg": "n4",
        "window": "57.81-60.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILIES"],
        "narration": "He meant: nobody earns their way into the kingdom of God.",
        "must_show": "the un-earning — close on a child's open empty hands lifted up to receive; the whole soteriology in small palms.",
        "must_not_show": "no halo, glare or rim-light; the hands empty and expectant — receiving as the only qualification.",
        "scene": (
            "Close in the golden light: a small "
            "child's two hands lifted open and "
            "empty — palms up, fingers spread, dirty "
            "from the road and holding absolutely "
            "nothing — raised in the universal "
            "posture of small people who expect to "
            "be given things simply because they "
            "are there and it is offered: the "
            "kingdom's entire entrance exam, passed "
            "by reflex. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b12", "out": "s12-you-receive-it-the-way.jpeg", "seg": "n4 + s16",
        "window": "60.91-70.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": (
            "You receive it the way a child receives a gift — with open hands. "
            "And he took them up in his arms, put his hands upon them, and "
            "blessed them."
        ),
        "must_show": "SCRIPTURE-EXACT: the taking up — Jesus with a child IN his arms and a hand on another's head, the blessing begun; arms full of the kingdom's citizens.",
        "must_not_show": "no halo, glare or rim-light; the holding real — a child's weight on his arm, another leaning at his knee; joy general.",
        "scene": (
            "The blessing begins with full arms: the "
            "bold girl in madder-red taken up and "
            "settled on Jesus's arm like she has "
            "lived there always, his free hand "
            "resting on one twin's dark head — the "
            "toddler hauling himself up by a "
            "handful of cream robe, the baby held "
            "out by its beaming mother for its "
            "turn — a man being climbed like a "
            "fig tree by the kingdom of God, and "
            "blessing it one head at a time. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r076-b13", "out": "s13-but-he-saw-them-do.jpeg", "seg": "n2",
        "window": "22.13-23.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROADSIDE"],
        "narration": "But he saw them do it.",
        "must_show": "the seeing — Jesus's eyes catching the wave-off across the road: attention arriving on the small injustice at the exact moment of it.",
        "must_not_show": "no halo, glare or rim-light; the catch immediate — nothing at knee height escapes this watcher.",
        "scene": (
            "From the sitting-stone Jesus's eyes "
            "catch it mid-gesture — the shooing "
            "hands, the checked families, the shy "
            "boy's retreat behind his mother's "
            "legs — the whole small injustice "
            "arriving in his gaze complete and "
            "instantly weighed: a watcher from whom "
            "nothing at knee height has ever once "
            "escaped, seeing his own men bar his "
            "own door. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r076-b14", "out": "s14-then-he-gathered-them-up.jpeg", "seg": "n5 + HUSH",
        "window": "71.89-80.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["FAMILIES", "ROADSIDE"],
        "narration": (
            "Then he gathered them up in his arms and blessed them, one at a "
            "time, unhurried — like there was nowhere else he needed to be."
        ),
        "must_show": "SCRIPTURE-EXACT + the HUSH: the unhurried blessing — the deep-gold closing scene: each child blessed in turn, the shy boy NOW at his knee, parents at rest; and the held quiet after — nowhere else to be.",
        "must_not_show": "no halo, glare or rim-light; the HUSH honoured — the final stillness warm and complete; the shy boy's arrival the quiet triumph.",
        "scene": (
            "The day's deepest gold, the camera low behind the "
            "waiting families' shoulders, holds the "
            "unhurried blessing: Jesus seated again "
            "on the flat stone with a child on each "
            "knee and the line of small heads "
            "waiting their easy turn — and arrived "
            "at last at his knee, unhidden, the shy "
            "boy in dusty indigo receiving his own "
            "hand-on-head with enormous solemn "
            "eyes — the parents at rest along the "
            "wall, the disciples seated in the "
            "grass like schoolboys, and over the "
            "whole roadside the held golden quiet "
            "of a man with nowhere else, in all the "
            "world, he needed to be. Every figure "
            "has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "ROADSIDE": "PLACE-REF/roadside.jpeg",  # build-38-persistent-widow v2-r038-b39
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "FAMILIES": "CAST-REF-V2/families.jpeg",
}
