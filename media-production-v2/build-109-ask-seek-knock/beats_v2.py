#!/usr/bin/env python3
"""V2 beat map — row 109, build-109-ask-seek-knock (Matthew 7:7-11).

COVERAGE: 23 pictures over 129.6 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 7 KJV):
  v7    "ASK, and it shall be given you; SEEK, and ye shall find;
        KNOCK, and it shall be opened unto you." — Sermon on the
        Mount hillside teaching.
  v8    "For EVERY ONE that asketh receiveth..." — universal, not for
        the specially worthy.
  v9-10 "what man is there of you, whom if his son ask BREAD, will he
        give him a STONE? Or if he ask a FISH, will he give him a
        SERPENT?" — home-scale absurdities; rendered as the GOOD gift
        given, the wrong gift only implied (never enacted).
  v11   "If ye then, BEING EVIL, know how to give good gifts unto
        your children, HOW MUCH MORE shall your Father which is in
        heaven give good things to them that ask him?"

FRAME-STAGING: hillside teaching beats DISTINCT from other mount rows
— spring-flowered slope, close informal ring; the father-child
vignettes in one recurring village home.

TIME OF DAY: bright spring morning on the hillside; the home vignettes
in warm midday window-light; the close in gold afternoon.

CONTENT-CARE: no flags. No stone or serpent ever placed in a child's
hands — the absurdity lives in narration; the pictures give bread and
fish. The child-father warmth carried with full dignity.

CHANGING CONDITION (kept OUT of the locks): the three verbs — hands
out, then searching, then knocking; the door — shut, then opening;
the gifts — asked, then given.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream.
LOCKS = {
    "SLOPE": (
        "SLOPE LOCK: the teaching hillside — a green spring slope "
        "scattered with red anemones above the lake's far blue, "
        "listeners seated close in an informal ring on the grass. "
        "The same slope, flowers and lake-line throughout."
    ),
    "HOME": (
        "HOME LOCK: the village home — a small one-room house: "
        "packed-earth floor, a low table, a bread oven's warm mouth, "
        "one deep window pouring midday light, a heavy WOODEN DOOR "
        "with an iron ring. The same room, window and door "
        "throughout."
    ),
    "FATHER": (
        "FATHER LOCK: the father is the same man in every home shot "
        "— about thirty-five, short dark beard, kind tired eyes, in "
        "a DARK RUST-BROWN work tunic (never cream, never white)."
    ),
    "CHILD": (
        "CHILD LOCK: the child is the same boy in every home shot — "
        "about five, round-cheeked, dark curls, in a small DEEP "
        "OLIVE tunic (never cream, never white); trusting and "
        "direct."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r109-b01", "out": "s01-people-have-always-wondered-how.jpeg", "seg": "n1",
        "window": "0.28-2.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["SLOPE"],
        "narration": "People have always wondered how prayer really works.",
        "must_show": "the wondering — listeners on the slope before the teaching begins: puzzled earnest faces, hands loosely folded, the question older than all of them.",
        "must_not_show": "no halo; the puzzlement HONEST — ordinary people with a real question.",
        "scene": (
            "On the flowered spring slope "
            "the oldest question waits in "
            "the faces: farmers and "
            "mothers and old men settled "
            "on the grass with their "
            "hands loosely folded, brows "
            "carrying the puzzle every "
            "generation hands the next — "
            "how does it work, the "
            "talking to heaven; does it "
            "reach; does it move "
            "anything — a hillside of "
            "honest wondering, waiting "
            "on an answer. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r109-b02", "out": "s02-jesus-teaching-on-a-hillside.jpeg", "seg": "n1",
        "window": "6.36-10.91", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SLOPE"],
        "narration": "Jesus, teaching on a hillside, made it startlingly simple.",
        "must_show": "the teacher — Jesus seated among the ring on the flowered slope, at ease, the simplicity already in his open manner; the lake blue and far below.",
        "must_not_show": "no halo, glare or rim-light; the manner INFORMAL — seated with them, not above them.",
        "scene": (
            "The answer arrives sitting down, the camera at the "
            "ring's edge behind the near listeners' shoulders: "
            "down: Jesus settled on the "
            "grass among the ring, "
            "anemones red around his "
            "feet, the lake far and "
            "blue below the slope — no "
            "pulpit, no scroll, his "
            "hands already moving in "
            "the easy open way of a "
            "man about to make a hard "
            "thing simple — the whole "
            "machinery of prayer about "
            "to be explained in three "
            "words a child could carry "
            "home. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r109-b03", "out": "s03-ask-and-it-shall-be.jpeg", "seg": "jv7",
        "window": "11.44-17.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SLOPE"],
        "narration": (
            "Ask, and it shall be given you; seek, and ye shall find; "
            "knock, and it shall be opened unto you:"
        ),
        "must_show": "SCRIPTURE-EXACT: the three verbs — Jesus teaching them with three distinct hand-shapes: an open asking palm, a shading searching brow, a knocking fist; the ring following each.",
        "must_not_show": "no halo, glare or rim-light; the THREE gestures distinct and readable in sequence.",
        "scene": (
            "The teaching comes with its "
            "own sign language: ASK — "
            "his palm turning open and "
            "up, simple as a child's — "
            "SEEK — the hand rising to "
            "shade his brow, scanning "
            "the far blue distance — "
            "KNOCK — the loose fist "
            "rapping twice on the air "
            "as on a door — three "
            "plain motions any hand on "
            "the hillside can copy, "
            "and around the ring, "
            "already, hands beginning "
            "to copy them. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r109-b04", "out": "s04-three-words-and-each-one.jpeg", "seg": "n2",
        "window": "19.41-23.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["SLOPE"],
        "narration": (
            "Three words, and each one is warmer and more personal than the "
            "last."
        ),
        "must_show": "the warming — listeners' faces down the ring catching the teaching's warmth in gradation: interest, then hope, then something like relief.",
        "must_not_show": "no halo; the gradient READABLE across three or four faces.",
        "scene": (
            "The warmth moves down the "
            "ring like morning down a "
            "wall: on the first face, "
            "interest — a farmer's brow "
            "lifting at the plainness "
            "of it; on the next, hope — "
            "a mother's lips parting as "
            "the words find something "
            "long shelved; on the "
            "third, open relief — an "
            "old man's eyes going wet "
            "at the idea that it might "
            "really be this simple, "
            "this warm, this near. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r109-b05", "out": "s05-ask-like-a-child-who.jpeg", "seg": "n2",
        "window": "23.10-29.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "CHILD"],
        "narration": (
            "Ask — like a child who simply puts out its hands, trusting, "
            "expecting good."
        ),
        "must_show": "ASK illustrated — the home vignette: the small boy with both hands out and up to someone just off-frame, face utterly expectant; asking without anxiety.",
        "must_not_show": "no halo; the expectancy TOTAL — no begging posture, no doubt anywhere in the small frame.",
        "scene": (
            "The first verb gets its "
            "portrait at home: the small "
            "boy in the warm window-"
            "light with both hands out "
            "and open, face tipped up, "
            "round cheeks certain — no "
            "cringe of the beggar in "
            "him, no speech prepared, "
            "no doubt anywhere in the "
            "little body that what "
            "comes down into these "
            "hands will be good — "
            "asking the way children "
            "invented it: trust, with "
            "arms. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r109-b06", "out": "s06-wear-god-down.jpeg", "seg": "n1",
        "window": "4.87-6.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["SLOPE"],
        "narration": "Wear God down?",
        "must_show": "the wrong theory — a listener's face mid-misconception: strained, effortful, as if prayer were arm-wrestling; the theory about to be retired.",
        "must_not_show": "no halo; the strain gently comic-sad, not mocked.",
        "scene": (
            "Close on the theory the "
            "hillside came in with: one "
            "weathered listener's face "
            "screwed up in imagined "
            "effort — jaw set, knuckles "
            "white around each other — "
            "prayer pictured as siege "
            "work, wearing heaven down "
            "the way water wears "
            "stone, if only you push "
            "long enough and loud "
            "enough — the exhausting "
            "arithmetic of it written "
            "in the tired lines, one "
            "minute before retirement. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r109-b07", "out": "s07-seek-more-than-a-word.jpeg", "seg": "n3",
        "window": "30.33-40.22", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Seek — more than a word now; it is getting up and searching, "
            "patient and hopeful, sure that what you are looking for is "
            "really there to be found."
        ),
        "must_show": "SEEK illustrated — a hopeful searcher on a hill path at morning: scanning the country ahead with shaded eyes, moving, patient; search with certainty in it.",
        "must_not_show": "no halo; the search HOPEFUL — nothing frantic or lost about the posture.",
        "scene": (
            "The second verb walks out "
            "into the morning: a "
            "traveller on the hill path "
            "with his hand shading his "
            "eyes, scanning the folded "
            "country ahead ridge by "
            "ridge — moving as he "
            "looks, patient as a man "
            "reading a friend's "
            "directions, certain in "
            "every unhurried stride "
            "that the thing he is "
            "looking for is really out "
            "there and really findable — "
            "seeking, done in hope's "
            "gait. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r109-b08", "out": "s08-for-every-one-that-asketh.jpeg", "seg": "jv8",
        "window": "40.78-48.58", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SLOPE"],
        "narration": (
            "For every one that asketh receiveth; and he that seeketh "
            "findeth; and to him that knocketh it shall be opened."
        ),
        "must_show": "SCRIPTURE-EXACT: the universal promise — Jesus's arm sweeping the WHOLE ring of ordinary faces: every one; no one outside the gesture.",
        "must_not_show": "no halo, glare or rim-light; the sweep INCLUSIVE — old, young, poor, doubtful, all inside it.",
        "scene": (
            "The promise gets its full circumference, the camera "
            "outside the ring so the sweeping arm crosses in "
            "profile: "
            "circumference: Jesus's arm "
            "sweeping the whole seated "
            "ring — EVERY ONE — the "
            "gesture passing over the "
            "farmer and the widow and "
            "the boy at the edge and "
            "the man who came only to "
            "listen, excluding exactly "
            "nobody on the flowered "
            "grass — asketh, seeketh, "
            "knocketh, three doors with "
            "the same word carved over "
            "all of them: whosoever. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r109-b09", "out": "s09-not-perfectly.jpeg", "seg": "n7",
        "window": "118.76-119.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "CHILD"],
        "narration": "Not perfectly.",
        "must_show": "the not-perfectly — the small boy's asking hands again, grubby and imperfect: dirt under nails, a scraped knuckle; asked anyway, received anyway.",
        "must_not_show": "no halo; the imperfection ENDEARING — real child's hands, no polish.",
        "scene": (
            "Close on the standard the "
            "asking actually requires: "
            "two small hands held out "
            "in the window-light with "
            "the morning still on them "
            "— dirt under the little "
            "nails, a scraped knuckle "
            "from the wall he climbed, "
            "a smudge of yesterday's "
            "fig — nothing washed, "
            "nothing rehearsed, nothing "
            "perfect anywhere in the "
            "offer — and held out "
            "anyway with total "
            "confidence, which turns "
            "out to be the whole "
            "requirement. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r109-b10", "out": "s10-knock-and-keep-knocking-on.jpeg", "seg": "n4",
        "window": "50.06-57.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME"],
        "narration": (
            "Knock — and keep knocking — on a door you cannot yet see "
            "behind. And the promise is that the door does open."
        ),
        "must_show": "KNOCK illustrated — a hand knocking at the heavy wooden door, and the door caught mid-OPENING: warm light spilling through the widening gap.",
        "must_not_show": "no halo; the opening IN PROGRESS — the gap widening, the light coming through.",
        "scene": (
            "The third verb meets its "
            "answer mid-motion: a hand "
            "raised at the heavy wooden "
            "door in one more of its "
            "patient knocks — and the "
            "door already giving: the "
            "iron ring turning, the "
            "gap widening along the "
            "jamb, warm gold light "
            "spilling through the "
            "opening seam onto the "
            "knuckles that kept "
            "faith with the wood — a "
            "door knocked on blind, "
            "opening exactly as "
            "promised, from the side "
            "you could not see. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r109-b11", "out": "s11-not-maybe-not-for-the.jpeg", "seg": "n4",
        "window": "57.74-61.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["SLOPE"],
        "narration": "Not maybe. Not for the specially worthy.",
        "must_show": "the no-qualifiers — plain faces of the unspecial on the slope: a laborer, an old woman, a fidgety boy; the promise's actual demographic.",
        "must_not_show": "no halo; the faces ORDINARY on purpose — nobody impressive in frame.",
        "scene": (
            "Close on the promise's "
            "actual demographic: a "
            "day-laborer with grass in "
            "his hair, an old woman "
            "whose knuckles say fifty "
            "years of wash-water, a "
            "boy who cannot sit still "
            "even for this — not one "
            "impressive face in the "
            "frame, not one resume "
            "among them — precisely "
            "the crowd the every-one "
            "was written for, and "
            "nobody checking "
            "credentials at any of "
            "the three doors. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r109-b12", "out": "s12-every-one-who-asks-receives.jpeg", "seg": "n4 + n5",
        "window": "61.08-67.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SLOPE"],
        "narration": (
            "Every one who asks, receives. Then Jesus makes it personal "
            "with a picture from any home."
        ),
        "must_show": "the pivot to home — Jesus leaning forward with the storyteller's shift, hands beginning a domestic shape; the ring drawing in for the picture.",
        "must_not_show": "no halo, glare or rim-light; the shift COZY — a story about to happen, the hillside leaning in.",
        "scene": (
            "The teaching pulls its "
            "chair closer: Jesus "
            "leaning forward on the "
            "grass with the "
            "storyteller's shift in his "
            "shoulders, hands starting "
            "to shape something small "
            "and domestic in the air — "
            "a loaf, a table, a "
            "child's height off the "
            "ground — and the ring "
            "tightening toward him by "
            "inches all around, the "
            "hillside settling in for "
            "a picture from inside "
            "every house they have "
            "ever lived in. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r109-b13", "out": "s13-or-what-man-is-there.jpeg", "seg": "jv910",
        "window": "67.94-73.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": (
            "Or what man is there of you, whom if his son ask bread, will "
            "he give him a stone?"
        ),
        "must_show": "SCRIPTURE-EXACT rendered right-way: the boy asking up at his father — and the father already reaching to the table's fresh BREAD; no stone anywhere near the exchange.",
        "must_not_show": "ABSOLUTE: no stone offered or held — the absurdity stays in narration; the bread the only gift in frame.",
        "scene": (
            "The question answers itself "
            "in any kitchen: the small "
            "boy at his father's knee "
            "with his hands up — bread, "
            "abba — and the father's "
            "arm already moving, "
            "unthinking as breath, to "
            "the fresh loaf on the low "
            "table — tearing the warm "
            "end off for the small "
            "reaching fingers — the "
            "stone of the question "
            "existing nowhere in the "
            "room, because no father "
            "in the world keeps one "
            "on the bread shelf. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r109-b14", "out": "s14-or-if-he-ask-a.jpeg", "seg": "jv910",
        "window": "73.55-77.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": "Or if he ask a fish, will he give him a serpent?",
        "must_show": "SCRIPTURE-EXACT rendered right-way: the father laying a good FISH into the boy's dish; the serpent never present; the giving ordinary and sure.",
        "must_not_show": "ABSOLUTE: no serpent anywhere in frame — the fish given, the absurdity narration-only.",
        "scene": (
            "The second absurdity dies "
            "the same quiet death: the "
            "boy's dish held up hopeful "
            "at the table's edge, and "
            "into it, from the "
            "father's hand, a good "
            "fish — silver, fresh, the "
            "day's best of the catch — "
            "laid in with the ordinary "
            "sureness of ten thousand "
            "suppers — nothing coiled "
            "anywhere in the warm "
            "room, nothing cruel in "
            "the cupboard, the whole "
            "dark alternative unable "
            "to survive thirty seconds "
            "in a real father's "
            "kitchen. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r109-b15", "out": "s15-a-child-asks-its-father.jpeg", "seg": "n5b",
        "window": "78.74-84.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": (
            "A child asks its father for bread. What kind of father hands "
            "his hungry child a stone instead?"
        ),
        "must_show": "the trust exchange — the boy eating the warm bread against his father's knee, the father's hand in the dark curls; the answer to the rhetorical question, lived.",
        "must_not_show": "ABSOLUTE: no stone; the domestic peace TOTAL — question refuted by supper.",
        "scene": (
            "The rhetorical question "
            "eats its answer: the boy "
            "leaned against his "
            "father's knee working "
            "through the warm torn "
            "bread with both hands and "
            "his whole attention, and "
            "the father's rough hand "
            "resting easy in the dark "
            "curls, neither of them "
            "aware of being anybody's "
            "theology — what kind of "
            "father — THIS kind, says "
            "the crumb-scattered, "
            "utterly unremarkable "
            "peace of an ordinary "
            "supper. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r109-b16", "out": "s16-or-a-snake-when-he.jpeg", "seg": "n5b",
        "window": "84.16-88.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER"],
        "narration": "Or a snake when he asks for a fish? No father you would trust.",
        "must_show": "the father's face — close on the kind tired eyes at the thought: the very idea alien to them; trustworthiness as a face.",
        "must_not_show": "ABSOLUTE: no snake; the refutation entirely in the good face's incapacity for it.",
        "scene": (
            "Close on the refutation "
            "itself: the father's face — "
            "tired from work, kind past "
            "argument — and the very "
            "idea of the cruel gift "
            "finding nothing in it to "
            "attach to: no corner of "
            "those eyes where such a "
            "thing could live, no "
            "line of that mouth that "
            "has ever curved toward a "
            "child's harm — the whole "
            "dark hypothesis sliding "
            "off a plain good face "
            "like water off oiled "
            "wood. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r109-b17", "out": "s17-if-ye-then-being-evil.jpeg", "seg": "jv11",
        "window": "89.26-99.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SLOPE"],
        "narration": (
            "If ye then, being evil, know how to give good gifts unto your "
            "children, how much more shall your Father which is in heaven "
            "give good things to them that ask him?"
        ),
        "must_show": "SCRIPTURE-EXACT: the how-much-more — Jesus's hands measuring a small span, then thrown wide to the whole sky; the argument's scale jump made visible.",
        "must_not_show": "no halo, glare or rim-light; the TWO measures distinct — hand-span, then horizon.",
        "scene": (
            "The argument makes its "
            "great jump in his hands: "
            "first the small measure — "
            "finger and thumb a "
            "hand-span apart: your "
            "love, flawed and tired "
            "and real — then both arms "
            "thrown wide at the whole "
            "spring sky over the lake — "
            "HOW MUCH MORE — the "
            "distance between a "
            "father's kitchen and the "
            "Father's heaven measured "
            "out in one gesture, and "
            "every listener's eyes "
            "going wide with the "
            "sweep of it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r109-b18", "out": "s18-do-you-have-to-say.jpeg", "seg": "n1",
        "window": "2.85-4.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["SLOPE"],
        "narration": "Do you have to say it just right?",
        "must_show": "the performance worry — a listener silently rehearsing words, lips moving, fingers counting phrases; prayer as exam, about to be dismissed.",
        "must_not_show": "no halo; the rehearsing TENDER-comic — a real worry, kindly observed.",
        "scene": (
            "Close on the exam-theory "
            "of prayer: an earnest "
            "listener with his lips "
            "moving silently through a "
            "rehearsal, fingers "
            "counting off phrases "
            "like beads, brow knotted "
            "over the right order of "
            "the holy words — get it "
            "wrong and surely it "
            "doesn't count — the "
            "anxious grammar of "
            "talking to heaven, "
            "carried up the hillside "
            "by a man about to be "
            "gloriously relieved of "
            "it. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r109-b19", "out": "s19-if-flawed-tired-imperfect-parents.jpeg", "seg": "n6",
        "window": "100.54-108.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": (
            "If flawed, tired, imperfect parents still love to give their "
            "kids good things — how much more does a perfect Father delight "
            "to give to you?"
        ),
        "must_show": "the flawed-and-giving — the tired father at day's end still producing a small treasure for the boy: a carved toy, delight on both faces; imperfect love giving well.",
        "must_not_show": "no halo; the tiredness VISIBLE and the delight bigger — both true at once.",
        "scene": (
            "The argument's small "
            "premise, proven at dusk: "
            "the father home spent from "
            "the field, dust still on "
            "him, shoulders done — and "
            "producing from behind his "
            "back, with the last "
            "energy of the day, a "
            "little carved wooden "
            "donkey for the boy — the "
            "child's shout, the tired "
            "face breaking open with "
            "delight bigger than the "
            "tiredness — flawed, worn, "
            "imperfect love, still "
            "giving good things on "
            "reflex, at cost. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r109-b20", "out": "s20-prayer-is-not-twisting-arm.jpeg", "seg": "n6",
        "window": "108.61-111.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME"],
        "narration": "Prayer is not twisting God's arm.",
        "must_show": "the untwisting — the home's door standing already ajar in warm light: no force needed on a door not locked; the metaphor at rest.",
        "must_not_show": "no halo; NO straining figure — the ajar door alone makes the point.",
        "scene": (
            "The frame retires the "
            "siege theory with one "
            "quiet fact: the heavy "
            "wooden door standing "
            "already ajar in the warm "
            "afternoon light — iron "
            "ring at rest, jamb "
            "unforced, a hand's-width "
            "of gold spilling through "
            "the standing gap — "
            "nothing here to twist, "
            "nothing to batter, no "
            "resistance anywhere in "
            "the architecture — the "
            "whole exhausting theory "
            "of reluctant heaven, "
            "refuted by a door that "
            "was never locked. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r109-b21", "out": "s21-it-is-a-child-asking.jpeg", "seg": "n6 + n7",
        "window": "111.37-118.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": (
            "It is a child asking a good Father who is glad to be asked. So "
            "the invitation is just this: ask."
        ),
        "must_show": "the gladness — the father crouched to the boy's level, face lit at being asked; the asking received as gift by the asked.",
        "must_not_show": "no halo; the GLADNESS the subject — being asked visibly delights him.",
        "scene": (
            "The secret at the bottom "
            "of the teaching: the "
            "father down on his heels "
            "at the boy's own level, "
            "and on his face — at "
            "nothing more than being "
            "asked — open gladness: "
            "the small request "
            "received like a present, "
            "the tired eyes bright at "
            "being wanted, being "
            "trusted, being the one "
            "the little hands came "
            "to — asking, it turns "
            "out, is a gift that runs "
            "both directions, and the "
            "good Father has always "
            "known it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r109-b22", "out": "s22-not-impressively-simply-honestly-like.jpeg", "seg": "n7",
        "window": "119.82-124.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "CHILD"],
        "narration": "Not impressively. Simply, honestly, like a child.",
        "must_show": "the standard set — the boy mid-ask in plainest words: no performance, face open, need named simply; the model prayer-poster.",
        "must_not_show": "no halo; NOTHING rehearsed in him — simplicity as the whole art.",
        "scene": (
            "Close on the only "
            "technique the teaching "
            "requires: the boy asking "
            "in the warm light with "
            "his whole plain self — no "
            "folded formal hands, no "
            "borrowed big words, no "
            "glance around to check "
            "his form — just the open "
            "face, the direct eyes, "
            "the need named the way "
            "children name things: "
            "simply, first try, out "
            "loud — the entire art of "
            "prayer, demonstrated by "
            "someone five years old. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r109-b23", "out": "s23-the-father-is-not-reluctant.jpeg", "seg": "n7",
        "window": "124.20-129.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "FATHER", "CHILD"],
        "narration": (
            "The Father is not reluctant. He is leaning in, glad to hear "
            "your voice."
        ),
        "must_show": "the closing image — the father leaning IN toward the boy mid-sentence, elbow on knee, wholly attentive in the gold light; eagerness to hear as the final picture.",
        "must_not_show": "no halo; the LEAN the meaning — toward, always toward.",
        "scene": (
            "The closing frame keeps "
            "the posture that answers "
            "every fear about prayer: "
            "the father leaned all the "
            "way IN — elbow on knee, "
            "chin in hand, face a "
            "hand-span from the boy's "
            "unspooling story in the "
            "gold afternoon light — "
            "nothing reluctant anywhere "
            "in the frame, no arm "
            "crossed, no eye on the "
            "door — just gladness, "
            "leaning toward a small "
            "voice like a man warming "
            "his hands at it. Every "
            "figure has two arms, two "
            "hands and one head."
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
