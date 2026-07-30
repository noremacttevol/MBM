#!/usr/bin/env python3
"""V2 beat map — row 113, build-113-where-art-thou (Genesis 2-3).

COVERAGE: 26 pictures over 147.6 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Genesis 3 KJV):
  v8    "they heard THE VOICE of the LORD God WALKING IN THE GARDEN
        in the COOL OF THE DAY: and Adam and his wife HID THEMSELVES
        ... amongst the TREES."
  v9    "WHERE ART THOU?" — the Father's question, asked by One who
        knows the answer, so the hider can come out.
  v10   "I heard thy voice... and I WAS AFRAID, because I was naked;
        and I HID myself." — fear, not defiance.
  v12-13 the answers; "The serpent beguiled me, and I did eat."
  v21   "Unto Adam also and to his wife did the LORD God make COATS
        OF SKINS, and CLOTHED THEM." — the unexpected mercy.
  v23   the sending out — clothed, not alone, with the promise.

GOD RENDERING (CONTENT-CARE law, absolute): the LORD is NEVER
embodied — the "voice walking" is rendered as moving golden evening
light and stirred leaves through the garden, never a figure, hand or
silhouette; the coats of skins are FOUND laid ready in the light,
their making unseen.

SERPENT: NEVER painted — it exists only in the woman's quoted words.

MODESTY (absolute): Adam and Eve are framed with complete discretion
in every beat — waist-up behind foliage, at distance, in shadow, or
clothed (fig-leaf girdles from v7 onward, skin coats from v21);
nothing immodest in any frame. Shame is carried by POSTURE.

TIME OF DAY: the golden COOL OF THE DAY throughout — long warm
evening light in the garden; the exile beats at dusk with warmth kept
in the light. Correct story lighting.

CHANGING CONDITION (kept OUT of the locks): their covering — none
(discreetly framed), then fig leaves, then coats of skins; the
garden — open peace, then hiding places, then behind them; the
light — companion, then approaching, then following them out.
"""

# LOCKS: one entry per recurring person and per setting. Clothing changes
# across the row and stays OUT of these locks. Only Jesus wears cream (he
# does not appear in this row).
LOCKS = {
    "GARDEN": (
        "GARDEN LOCK: Eden — a deep lush garden in long golden "
        "evening light: great old trees with low sweeping branches, "
        "flowering thickets, a clear stream over smooth stones, "
        "fruit heavy everywhere. The same trees, stream and light "
        "throughout."
    ),
    "ADAM": (
        "ADAM LOCK: the man is the same in every shot — young, "
        "strong and unlined, warm tan skin, shoulder-length dark "
        "hair and a short dark beard; always framed with complete "
        "modesty (foliage, distance, shadow, or clothing)."
    ),
    "EVE": (
        "EVE LOCK: the woman is the same in every shot — young and "
        "unlined, warm tan skin, very long thick dark hair falling "
        "past her waist; always framed with complete modesty "
        "(her hair, foliage, distance, shadow, or clothing)."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r113-b01", "out": "s01-in-the-beginning-there-was.jpeg", "seg": "n1",
        "window": "0.28-3.96", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "In the beginning there was a garden, and in the garden, peace.",
        "must_show": "the garden at peace — Eden wide in golden evening light: great trees, the stream, fruit heavy, no person in frame yet; peace as a place.",
        "must_not_show": "no figures yet; no halo; the peace TOTAL — nothing in the frame afraid of anything.",
        "scene": (
            "Before everything else, the "
            "place: a garden deep in "
            "golden evening light — "
            "great trees sweeping their "
            "branches low over flowering "
            "thickets, a clear stream "
            "running easy over smooth "
            "stones, fruit hanging "
            "heavy and unguarded on "
            "every side — and over all "
            "of it a peace so complete "
            "that nothing in the frame "
            "has ever once needed to "
            "hide from anything: the "
            "world as it was meant, "
            "resting in its first "
            "evening light. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b02", "out": "s02-people-and-god-walking-together.jpeg", "seg": "n1",
        "window": "3.96-9.71", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "People and God walking together in the cool of the day, with "
            "nothing to hide and nothing to fear."
        ),
        "must_show": "the walking-together — the man and woman at ease strolling the garden path at distance amid deep foliage, and BESIDE their way a moving warmth of golden light through the trees: companionship with the unseen; modesty by distance and foliage.",
        "must_not_show": "ABSOLUTE: no figure of God — the presence is moving light only; the couple framed discreet, unashamed ease in their walk.",
        "scene": (
            "Down the evening path the "
            "first friendship takes its "
            "walk: the man and woman "
            "strolling far off through "
            "the deep green, easy and "
            "unhurried, her long dark "
            "hair swaying to her waist "
            "— and moving BESIDE their "
            "way, keeping pace through "
            "the trees, a warmth of "
            "golden light that stirs "
            "the leaves as it goes — "
            "three walking together in "
            "the cool of the day, "
            "nothing hidden anywhere "
            "in the garden and nothing "
            "afraid. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b03", "out": "s03-there-was-only-one-thing.jpeg", "seg": "n2",
        "window": "10.23-13.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "There was only one thing they were asked not to do.",
        "must_show": "the one tree — a single distinct fruit tree standing apart in its own light: beautiful, unfenced, its fruit unlike the others; the one boundary, unwalled.",
        "must_not_show": "no serpent anywhere; no fence — trust the only barrier.",
        "scene": (
            "In its own clearing the one "
            "boundary of paradise "
            "stands unfenced: a single "
            "tree unlike its brothers — "
            "taller, stranger, its "
            "fruit catching the evening "
            "light with a beauty that "
            "asks to be looked at — no "
            "wall around it, no thorn "
            "hedge, no guard: nothing "
            "keeping the whole garden's "
            "abundance and this one "
            "withheld thing apart "
            "except a single trusted "
            "word. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b04", "out": "s04-and-as-people-do-they.jpeg", "seg": "n2",
        "window": "13.41-21.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "EVE"],
        "narration": (
            "And, as people do, they did it anyway — reaching for the one "
            "thing that was not theirs, hoping it would make them more than "
            "they were."
        ),
        "must_show": "the reach — close through foliage: the woman's hand closing on the fruit, the man's hand near hers; the taking at its instant; faces intent, framed discreetly by leaves.",
        "must_not_show": "ABSOLUTE: no serpent; modesty total — hands, faces and leaf-framed shoulders only.",
        "scene": (
            "Through the leaves the "
            "oldest mistake happens in "
            "close-up: her hand closing "
            "around the strange fruit's "
            "weight, his reaching in "
            "beside hers a breath "
            "behind — two faces framed "
            "in foliage, intent and "
            "hungry for something no "
            "fruit contains: to be "
            "MORE, to be as gods, to "
            "be other than the beloved "
            "creatures they already "
            "were — the twig bending, "
            "the stem giving, and "
            "everything, everything "
            "changing at the snap. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b05", "out": "s05-and-everything-changed-for-the.jpeg", "seg": "n3",
        "window": "22.29-25.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": "And everything changed. For the first time they felt shame.",
        "must_show": "shame's arrival — the two turned from each other in the thicket's shadow, arms wrapped around themselves, heads down; the first shame as pure posture, discreetly framed.",
        "must_not_show": "modesty absolute — shadow and foliage doing the covering; faces and curled postures carry everything.",
        "scene": (
            "The change arrives in "
            "their bodies first: deep "
            "in the thicket's shadow "
            "the two turn AWAY from "
            "each other for the first "
            "time in their lives — "
            "arms wrapping their own "
            "shoulders, spines "
            "curling, her hair pulled "
            "forward like a cloak, "
            "his head down — two "
            "people who an hour ago "
            "had nothing to hide, "
            "discovering the terrible "
            "new instinct of the "
            "covered: the first shame, "
            "learning its first "
            "posture. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b06", "out": "s06-they-saw-themselves-and-did.jpeg", "seg": "n3",
        "window": "25.73-31.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "They saw themselves, and did not like what they saw, and "
            "scrambled to cover up, hiding from each other."
        ),
        "must_show": "SCRIPTURE-EXACT: the fig leaves — the two hurriedly working broad fig leaves into rough girdles in the shadow, backs half-turned, fingers clumsy with haste; self-covering as panic.",
        "must_not_show": "modesty total — the leaf-work framed close on hands and bowed profiles; nothing immodest.",
        "scene": (
            "The first clothing is made "
            "in a panic: broad fig "
            "leaves torn down in "
            "handfuls, clumsy fingers "
            "threading them onto "
            "twisted vine, the two "
            "working fast with their "
            "backs half-turned to each "
            "other in the green shadow "
            "— the man's jaw tight, "
            "the woman's hands "
            "shaking on the stems — "
            "humanity's first craft "
            "project, invented in "
            "shame, worn in haste, "
            "hiding them from the "
            "one person each was made "
            "for. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r113-b07", "out": "s07-and-then-they-heard-him.jpeg", "seg": "n4",
        "window": "32.38-39.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "And then they heard him coming — the warm presence of God "
            "moving through the garden in the cool of the evening, the way "
            "he always had."
        ),
        "must_show": "SCRIPTURE-EXACT: the voice walking — the garden path filling with moving golden light, leaves stirring along its way, the evening warmth approaching as it always had; NO figure.",
        "must_not_show": "ABSOLUTE: no figure, shape or silhouette in the light — presence as light and stirred leaves only.",
        "scene": (
            "Down the evening path comes "
            "the sound they know best "
            "in the world: the warm "
            "golden light moving "
            "through the trees the way "
            "it has moved every "
            "evening of their lives — "
            "leaves stirring along its "
            "way, the stream "
            "brightening as it passes, "
            "the whole garden turning "
            "toward it like a face — "
            "the presence arriving for "
            "the usual walk, in the "
            "usual cool, unaware of "
            "nothing, coming anyway. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b08", "out": "s08-and-this-time-they-ran.jpeg", "seg": "n4 + jv9",
        "window": "39.89-45.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "And this time, they ran and hid themselves among the trees. "
            "Where art thou?"
        ),
        "must_show": "SCRIPTURE-EXACT: the hiding and the question — the leaf-girdled two pressed behind a great trunk in shadow, and the golden light standing in the clearing beyond, the question filling the garden; NO figure in the light.",
        "must_not_show": "ABSOLUTE: no figure of God; the couple's hiding FEARFUL, faces visible around the trunk's edge; modesty held.",
        "scene": (
            "For the first time in the "
            "world, someone hides from "
            "God: the two pressed "
            "flat behind a great "
            "trunk's shadow, leaf-"
            "girdled and trembling, "
            "her face buried against "
            "his shoulder, his eyes "
            "squeezed shut around the "
            "edge of the bark — while "
            "out in the clearing the "
            "golden light stands "
            "still, and the question "
            "moves through every leaf "
            "of the garden, gentle "
            "and enormous: WHERE ART "
            "THOU. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b09", "out": "s09-where-are-you-not-what.jpeg", "seg": "n5",
        "window": "46.58-49.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "Where are you. Not, what have you done.",
        "must_show": "the question's shape — the still golden clearing holding the question: warm light waiting, not searching-angry; the wording's mercy as atmosphere.",
        "must_not_show": "ABSOLUTE: no figure; NOTHING accusatory in the light — patience visible as stillness.",
        "scene": (
            "The frame rests inside the "
            "question's wording: the "
            "golden light standing "
            "patient in the clearing — "
            "not sweeping the thickets "
            "like a search party, not "
            "flaring with any anger, "
            "just waiting, warm and "
            "still, in the place where "
            "the walk always started — "
            "a question built with no "
            "accusation in it anywhere: "
            "not WHAT HAVE YOU DONE, "
            "which corners; but WHERE "
            "ARE YOU, which invites. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b10", "out": "s10-where-are-you-the-cry.jpeg", "seg": "n5",
        "window": "50.77-56.02", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "Where are you — the cry of a Father looking for a child who is "
            "hiding."
        ),
        "must_show": "the Father-and-hiding-child shape — the wide garden: the small hidden two behind their tree, the great patient light in the clearing; the geometry of every parent's evening search.",
        "must_not_show": "ABSOLUTE: no figure of God; the composition TENDER — hide-and-seek gone wrong, love still seeking.",
        "scene": (
            "The wide frame holds the "
            "oldest family scene there "
            "is: somewhere in the "
            "darkening green, two "
            "small frightened people "
            "pressed behind a tree — "
            "and filling the clearing "
            "they can no longer face, "
            "the great warm light of a "
            "Father at evening, calling "
            "a child's name into the "
            "garden — the same "
            "geometry as every parent "
            "who ever stood in a "
            "doorway at dusk calling "
            "toward the trees, wanting "
            "only the coming-out. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b11", "out": "s11-he-knew-exactly-where-they.jpeg", "seg": "n5",
        "window": "56.02-63.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "He knew exactly where they were. He asked so they would come "
            "out. And, trembling, the man answered."
        ),
        "must_show": "the coming-out beginning — the man stepping trembling from behind the trunk into the light's edge, leaf-girdled, the woman close behind his shoulder; the hardest first step.",
        "must_not_show": "ABSOLUTE: no figure of God; the step VOLUNTARY — drawn out by the question, not dragged.",
        "scene": (
            "The question does its "
            "work: from behind the "
            "great trunk the man steps "
            "trembling into the edge of "
            "the gold — leaf-girdled, "
            "arms half-crossed over "
            "himself, every muscle "
            "wanting the shadow back — "
            "and the woman close "
            "behind his shoulder, her "
            "hair drawn around her "
            "like a mantle — two "
            "hiders coming out not "
            "because they were found, "
            "but because they were "
            "asked, which is the whole "
            "reason the question was a "
            "question. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r113-b12", "out": "s12-i-heard-thy-voice-in.jpeg", "seg": "s10",
        "window": "63.84-68.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM"],
        "narration": (
            "I heard thy voice in the garden, and I was afraid, because I "
            "was naked; and I hid myself."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — close on the man's trembling face in the gold light saying it: fear owned out loud; the first honest sentence after the fall.",
        "must_not_show": "ABSOLUTE: no figure of God; the face AFRAID and honest — dignity kept through the trembling.",
        "scene": (
            "Close on the first "
            "confession ever made: the "
            "man's face in the golden "
            "light, trembling and "
            "bare of every excuse he "
            "will think of later — I "
            "HEARD THY VOICE — the "
            "words shaking loose one "
            "at a time — I WAS AFRAID "
            "— the whole broken "
            "morning owned in one "
            "breath — AND I HID "
            "MYSELF — a man telling "
            "God the truth about "
            "fear while still inside "
            "it, which is the bravest "
            "sentence fear allows. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b13", "out": "s13-that-is-the-whole-of.jpeg", "seg": "n5b",
        "window": "70.19-73.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": "That is the whole of it. Not defiance — fear.",
        "must_show": "fear not defiance — the two standing small in the light's edge: nothing rebellious anywhere in their postures, only frightened children before a parent.",
        "must_not_show": "no figure of God; NO fists, no jutted chins — the diagnosis visible: afraid, not defiant.",
        "scene": (
            "The frame checks them for "
            "rebellion and finds none: "
            "two small figures at the "
            "light's edge with nothing "
            "defiant anywhere on them — "
            "no jutted chin, no "
            "clenched fist, no turned "
            "back — just the hunched "
            "shoulders and downcast "
            "faces of children who "
            "broke the one thing and "
            "are standing in front of "
            "the parent — the fall's "
            "true anatomy on display: "
            "not a rebellion that "
            "needs crushing, a fear "
            "that needs finding. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b14", "out": "s14-shame-has-never-once-made.jpeg", "seg": "n5b",
        "window": "73.64-80.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "Shame has never once made a person run toward God. It makes "
            "them run behind a tree."
        ),
        "must_show": "the law of shame — the great hiding tree itself in the evening light: the trampled ground behind it where hiders pressed; the universal hiding place, humanity-sized.",
        "must_not_show": "no figures needed — the tree and its worn hiding-shadow carry the sentence.",
        "scene": (
            "The frame studies "
            "humanity's oldest piece "
            "of furniture: the great "
            "tree itself in the "
            "failing gold, and behind "
            "its trunk the pressed "
            "grass and scuffed earth "
            "of the hiding place — "
            "the exact shadow every "
            "generation since has "
            "found its own version "
            "of: the bottle, the "
            "busyness, the locked "
            "room, the long silence — "
            "shame's one unchanging "
            "instinct, standing rooted "
            "in the first garden: not "
            "toward him; behind "
            "something. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r113-b15", "out": "s15-what-is-this-that-thou.jpeg", "seg": "jv13",
        "window": "80.62-82.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["EVE"],
        "narration": "What is this that thou hast done?",
        "must_show": "SCRIPTURE-EXACT: the question to the woman — her face in the gold light receiving it: sorrow, not interrogation-terror; the gentle asking that draws truth.",
        "must_not_show": "ABSOLUTE: no figure of God; her dignity held — a woman about to tell the truth.",
        "scene": (
            "The question comes to her "
            "gently and lands with all "
            "its weight: the woman's "
            "face in the golden light, "
            "her long hair drawn "
            "around her like a "
            "mantle, eyes wet and "
            "level — WHAT IS THIS "
            "THAT THOU HAST DONE — "
            "not a prosecutor's trap "
            "but a Father's sorrowing "
            "invitation to say it "
            "herself, out loud, the "
            "way truth heals only "
            "when it comes from the "
            "one who hid it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b16", "out": "s16-the-serpent-beguiled-me-and.jpeg", "seg": "w13 + n6",
        "window": "84.27-90.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["EVE"],
        "narration": (
            "The serpent beguiled me, and I did eat. I was deceived, she "
            "said, and I ate."
        ),
        "must_show": "SCRIPTURE-EXACT: her confession — close on the woman speaking it plainly: deceived, and owning her part anyway; the truth said whole; NO serpent shown.",
        "must_not_show": "ABSOLUTE: no serpent anywhere in frame — it lives only in her words; her face honest, unbroken.",
        "scene": (
            "Close on the second "
            "confession: the woman's "
            "face steadying as she "
            "says it whole — I WAS "
            "DECEIVED — the truth of "
            "that real and said — AND "
            "I DID EAT — her own part "
            "owned right beside it, "
            "not hidden behind the "
            "deceiving — a woman "
            "standing in the gold "
            "light telling the whole "
            "shape of what happened, "
            "the lie that came to "
            "her and the hand that "
            "was still hers — truth, "
            "complete at last. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b17", "out": "s17-no-excuses-left-just-the.jpeg", "seg": "n6",
        "window": "90.69-95.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": "No excuses left — just the truth, spoken out loud at last.",
        "must_show": "the emptied-out honesty — the two standing plainly in the clearing's light, everything told; the strange relief of no more hiding visible in their loosened postures.",
        "must_not_show": "ABSOLUTE: no figure of God; the relief SUBTLE — spent, honest, lighter.",
        "scene": (
            "When the last excuse is "
            "spent, something almost "
            "like rest arrives: the two "
            "standing plainly in the "
            "clearing's gold, nothing "
            "left untold, hands empty "
            "at their sides at last — "
            "and in the loosened "
            "shoulders, under all the "
            "fear of what must come, "
            "the strange lightness "
            "known to everyone who "
            "has ever finally said "
            "the whole thing out "
            "loud: the hiding was "
            "heavier than the truth "
            "turned out to be. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b18", "out": "s18-there-were-consequences-there-always.jpeg", "seg": "n6",
        "window": "95.07-103.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "There were consequences; there always are. The easy garden was "
            "behind them now, and a hard world lay ahead."
        ),
        "must_show": "the two worlds — from the garden's edge: behind, the deep green ease; ahead through the gap, the harder dusk country of thorn and stone; the couple between them.",
        "must_not_show": "ABSOLUTE: no figure of God, no flaming sword — the hard world stated by landscape alone.",
        "scene": (
            "From the garden's edge the "
            "two geographies of the "
            "sentence face each other: "
            "at their backs the deep "
            "green ease of everything "
            "they knew — fruit heavy, "
            "stream running, evening "
            "gold — and ahead through "
            "the gap in the trees, "
            "the other country at "
            "dusk: stony ground "
            "climbing away, thorn "
            "scrub, a wind with an "
            "edge in it — and between "
            "the two worlds, small "
            "and holding hands, the "
            "people who traded one "
            "for the other. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b19", "out": "s19-they-stood-there-ashamed-waiting.jpeg", "seg": "n6",
        "window": "103.08-107.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": "They stood there, ashamed, waiting for the end of everything.",
        "must_show": "the braced-for-ending — the two with heads bowed and eyes shut in the dusk light, hands gripped together, braced for annihilation.",
        "must_not_show": "ABSOLUTE: no figure of God; the bracing TOTAL — two people expecting the worst sentence there is.",
        "scene": (
            "They stand braced for the "
            "end of the world they "
            "broke: heads bowed in the "
            "dusk light, eyes shut, "
            "her hand gripped white "
            "inside his — two small "
            "people who have heard "
            "the consequences and are "
            "now waiting, trembling, "
            "for the only thing shame "
            "can imagine coming next: "
            "the unmaking, the wrath, "
            "the end of everything — "
            "certain of it, braced "
            "for it, and about to be "
            "wrong. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b20", "out": "s20-and-instead-god-did-something.jpeg", "seg": "n7",
        "window": "108.20-112.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "And instead, God did something they never expected. He made "
            "them clothes."
        ),
        "must_show": "SCRIPTURE-EXACT rendered per law: the coats of skins FOUND — two well-made garments of soft dark leather laid ready on a sunlit stone, warm light resting on them; the making unseen.",
        "must_not_show": "ABSOLUTE: no figure or hands of God — the garments simply THERE, laid with visible care.",
        "scene": (
            "What waits for them is not "
            "the end: on a smooth "
            "stone in the last warm "
            "light lie two garments — "
            "coats of soft dark "
            "leather, well made, "
            "man-sized and woman-"
            "sized, laid out with the "
            "unmistakable care of "
            "hands that measured "
            "their wearers exactly — "
            "no maker anywhere in "
            "sight, only the work "
            "itself, resting in the "
            "gold like a sentence "
            "commuted: clothing, "
            "where annihilation was "
            "expected. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r113-b21", "out": "s21-with-his-own-care-he.jpeg", "seg": "n7",
        "window": "112.24-123.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": (
            "With his own care he covered their shame — better coverings "
            "than the leaves they had grabbed for themselves — because they "
            "could not fix what they had broken, but he could cover them in "
            "it."
        ),
        "must_show": "the clothing received — the two now dressed in the dark leather coats, the wilted fig leaves discarded at their feet; her face undone by the kindness; covered, by him.",
        "must_not_show": "ABSOLUTE: no figure of God; the CONTRAST at their feet — crushed leaves versus true garments.",
        "scene": (
            "They put on what was made "
            "for them: the dark soft "
            "coats settling over their "
            "shoulders like a kept "
            "promise, fitting exactly — "
            "and at their feet, "
            "discarded, the pitiful "
            "wilted fig-leaf girdles "
            "of their own panicked "
            "making — the woman's face "
            "undone entirely by the "
            "kindness of it, the man "
            "smoothing the leather "
            "with a trembling hand — "
            "covered, not by their "
            "scrambling, but by the "
            "very One they hid from. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b22", "out": "s22-not-how-dare-you.jpeg", "seg": "n5",
        "window": "49.42-50.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "Not, how dare you.",
        "must_show": "the withheld thunder — the garden's light holding gentle in the clearing where wrath would stand: the question's tone as weather; nothing scorched anywhere.",
        "must_not_show": "ABSOLUTE: no figure; NO storm, no darkening — gentleness where thunder was earned.",
        "scene": (
            "The frame listens for "
            "thunder and hears none: "
            "the clearing where wrath "
            "had every right to stand "
            "holds only the gentle "
            "gold of the usual "
            "evening — no darkening "
            "sky, no scorched grass, "
            "no wind bent in anger — "
            "the first sin in the "
            "history of the world, "
            "answered not with HOW "
            "DARE YOU but with a "
            "question soft enough "
            "for a hiding child to "
            "answer — mercy, setting "
            "its tone before its "
            "terms. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b23", "out": "s23-then-he-sent-them-out.jpeg", "seg": "n8",
        "window": "123.69-129.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN", "ADAM", "EVE"],
        "narration": (
            "Then he sent them out into the wide world — but not naked, and "
            "not alone, and not without a promise."
        ),
        "must_show": "SCRIPTURE-EXACT: the sending — the leather-clothed two walking out through the garden's gap into the dusk country, hand in hand, warm light following at their backs.",
        "must_not_show": "ABSOLUTE: no figure of God, no flaming sword — the exile's mercy carried by the following light and the held hands.",
        "scene": (
            "The exile leaves like a "
            "sending, not a casting "
            "out: the two walking "
            "through the gap in the "
            "trees into the stony dusk "
            "country hand in hand — "
            "clothed in the coats he "
            "made, provisioned with a "
            "promise neither fully "
            "understands — and behind "
            "them, pouring through "
            "the gap and laying long "
            "gold down the hard road "
            "ahead of their feet, "
            "the garden's warm light, "
            "following its children "
            "out. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r113-b24", "out": "s24-clothed-by-the-very-one.jpeg", "seg": "n8 + n9",
        "window": "129.83-135.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["ADAM", "EVE"],
        "narration": (
            "Clothed by the very One they had run from. That is the God of "
            "the very first story."
        ),
        "must_show": "the summary held — close on the two walking in their made coats, faces forward into the dusk: fear replaced by a chastened, held steadiness; the first story's God legible on them.",
        "must_not_show": "ABSOLUTE: no figure of God; their steadiness NEW — sobered, covered, not crushed.",
        "scene": (
            "Close on what the first "
            "story leaves its people "
            "wearing: the two walking "
            "forward into the dusk in "
            "coats cut by the hands "
            "they hid from — faces "
            "sobered and steady, fear "
            "traded for something "
            "harder-won: the knowledge "
            "of being covered by the "
            "One they wronged — every "
            "step in leather that "
            "preaches better than "
            "words what kind of God "
            "wrote the opening chapter: "
            "one who clothes his "
            "runaways for the road. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r113-b25", "out": "s25-not-one-who-waits-for.jpeg", "seg": "n9",
        "window": "135.35-139.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "Not one who waits for you to clean yourself up and come find him.",
        "must_show": "the not-waiting — the garden path itself at evening: the way in open, light already moving OUT along it; a God who travels toward, drawn as a road.",
        "must_not_show": "ABSOLUTE: no figure; the light OUTBOUND on the path — the direction the whole doctrine.",
        "scene": (
            "The path settles the "
            "doctrine by its light: "
            "the garden way at "
            "evening, open and "
            "unbarred — and the warm "
            "gold not pooled at its "
            "far end waiting for the "
            "cleaned-up to arrive, "
            "but moving OUTWARD along "
            "the stones, through the "
            "gap, out into the "
            "thorn-country where the "
            "hiders went — a God "
            "drawn as a direction: "
            "not the destination of "
            "the worthy, the traveler "
            "toward the lost. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r113-b26", "out": "s26-one-who-comes-walking-through.jpeg", "seg": "n9",
        "window": "139.24-147.40", "wide": True, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "One who comes walking through the garden in the cool of the "
            "evening, calling, still calling — where are you? — because he "
            "wants you back."
        ),
        "must_show": "the closing image — the garden in the cool of evening with the golden presence moving down the path toward the viewer's side of the frame, leaves stirring; the question still going out; NO figure ever.",
        "must_not_show": "ABSOLUTE: no figure, shape or silhouette — moving light and stirred leaves to the last frame; the call aimed OUT of the picture.",
        "scene": (
            "The closing frame is still "
            "happening: the garden in "
            "the cool of the evening, "
            "and down its path toward "
            "the near edge of the "
            "picture the warm golden "
            "light comes walking — "
            "leaves stirring along its "
            "way, the stream "
            "brightening as it "
            "passes — moving toward "
            "whoever is watching, "
            "with the first question "
            "still going out ahead of "
            "it into every hiding "
            "place there has ever "
            "been: WHERE ART THOU — "
            "asked because he wants "
            "you back. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
]
