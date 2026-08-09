#!/usr/bin/env python3
"""V2 beat map — row 121, build-121-salt-and-light (Matthew 5:13-16).

COVERAGE: 29 pictures over 167.2 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 5 KJV):
  5:1   the Sermon on the Mount setting — "he went up into a
        mountain: and when he was set, his disciples came unto him" —
        Jesus SEATED, teaching, an ordinary Galilean crowd on the
        grass.
  5:13  "Ye are the SALT of the earth: but if the salt have lost his
        savour... it is thenceforth good for nothing, but to be cast
        out, and to be TRODDEN UNDER FOOT of men."
  5:14  "Ye are the LIGHT of the world. A CITY THAT IS SET ON AN HILL
        cannot be hid."
  5:15  "Neither do men light a candle, and put it UNDER A BUSHEL,
        but ON A CANDLESTICK; and it giveth light unto ALL THAT ARE
        IN THE HOUSE."
  5:16  "LET YOUR LIGHT SO SHINE before men, that they may see your
        good works, and GLORIFY YOUR FATHER which is in heaven" — the
        light points PAST the doer to God.

RENDERING LAWS:
  - JESUS: the locked face (REF + JESUS LOCK) in every frame he is
    in; seated teaching posture on the hillside per 5:1; warm,
    unhurried, gazes of listeners visibly on him. No halo, ever —
    the lamp-light beats especially must keep all light PHYSICAL
    (clay lamps, dusk windows), never a light effect on any person.
  - The sayings are illustrated by VIGNETTES (market salt, kitchen,
    lamp-house, hill town, village lane) — period-true, no modern
    objects (row-7 complaint class): clay lamps with flame, bushel
    baskets, brass scales, stone and mudbrick.
  - "You" beats land on the CROWD's ordinary faces — fishermen,
    mothers, farmers, children — dignity, variety, no clone faces
    (rows 90/107).

TIME OF DAY ARC (intentional): the hillside teaching in warm late-
afternoon gold throughout (one continuous sermon); the salt vignettes
in bright market/kitchen day; the LIGHT vignettes at DUSK by design —
the hill town at lamplighting, the one-room house at evening lamp
time, the lane at nightfall; the closing dispersal in golden last
light. The dusk in b14/b17-b21/b26 is intentional and correct, not
the row-11 defect.

CHANGING CONDITION (kept OUT of the locks): the lamp — lit on the
stand, dimmed under the bushel, raised high again; the crowd —
gathered, then dispersing homeward at the close.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a green grassy slope "
        "above the Sea of Galilee, wildflowers in the grass, the "
        "blue lake and far hills below, warm late-afternoon light. "
        "The same slope and lake view throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the listening crowd — ordinary Galileans seated "
        "on the grass: weathered fishermen, mothers with children, "
        "sun-browned farmers, a few elders; varied earth-toned robes "
        "of brown, rust, olive and slate (no cream — only Jesus "
        "wears cream), varied ages and faces, never uniform."
    ),
    "MARKET": (
        "MARKET LOCK: the village market corner — a wooden stall "
        "under an awning with clay jars and sacks, a small brass "
        "balance scale, bright day. The same stall throughout."
    ),
    "KITCHEN": (
        "KITCHEN LOCK: a village kitchen — a small stone-and-mudbrick "
        "room with a clay oven, hanging herbs, clay crocks on a "
        "wooden shelf, a doorway open to daylight. The same room "
        "throughout."
    ),
    "LAMPHOUSE": (
        "LAMPHOUSE LOCK: the one-room home at evening — mudbrick "
        "walls, a low table, sleeping mats, a wooden LAMPSTAND, a "
        "woven BUSHEL BASKET by the wall, one small clay oil lamp "
        "with a real flame. The same room and furnishings throughout."
    ),
    "HILLTOWN": (
        "HILLTOWN LOCK: the far town set on a hill — pale stone "
        "houses stacked up a ridge above the lake, visible for "
        "miles. The same town and ridge throughout."
    ),
    "LANE": (
        "LANE LOCK: the village lane at evening — packed-earth "
        "street between mudbrick houses, doorways and small "
        "windows, first stars over the rooflines. The same lane "
        "throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r121-b01", "out": "s01-jesus-sat-on-a-green.jpeg", "seg": "n1",
        "window": "0.28-9.75", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Jesus sat on a green hillside above the Sea of Galilee, an "
            "ordinary crowd gathered on the grass around him — fishermen, "
            "mothers, farmers, children."
        ),
        "must_show": "SCRIPTURE-EXACT: the Sermon setting — Jesus SEATED on the green slope, the ordinary crowd settled on the grass around him, the blue lake below; every listening gaze converged on him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd VARIED — fishermen, mothers, farmers, children, no two faces alike.",
        "scene": (
            "The sermon has the best seat in Galilee, the camera "
            "looking past the seated crowd's backs up the slope: "
            "Jesus seated on the green hillside with the grass and "
            "wildflowers around him, the blue lake and far hills "
            "spread below, and gathered close on the slope the most "
            "ordinary congregation ever assembled — weathered "
            "fishermen with rope-scarred hands, mothers with "
            "children settled in their laps, sun-browned farmers, a "
            "leaning elder — every face turned to the seated "
            "teacher, who looks back at them like a man about to "
            "hand out an inheritance. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b02", "out": "s02-live-openly-good-kind-honest.jpeg", "seg": "n7",
        "window": "130.02-135.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE"],
        "narration": (
            "Live openly good — kind, honest, generous — right out where "
            "people can see it."
        ),
        "must_show": "the open goodness — in the evening lane, a woman handing warm bread across to an old neighbour in full view of the street; kindness done in the open, unhidden.",
        "must_not_show": "no halo; nothing performative — she is busy with the GIVING, not the audience.",
        "scene": (
            "The charge looks like this in a real street: in the "
            "evening lane a woman leans from her doorway to press "
            "warm bread into an old neighbour's hands — out in the "
            "open, in front of the water-carriers and the children "
            "and anyone else the street holds, nothing hidden and "
            "nothing performed — her attention entirely on the old "
            "man's grip and not at all on who might be watching, "
            "which is exactly the kind of seen that the sermon "
            "meant. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r121-b03", "out": "s03-and-to-these-plain-unremarkable.jpeg", "seg": "n1",
        "window": "9.75-15.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "And to these plain, unremarkable people he said something "
            "astonishing about who they were."
        ),
        "must_show": "the audience of the astonishing — close along the crowd's ordinary faces: a rope-scarred fisherman, a tired mother, a dusty farmer, listening hard; plainness about to be dignified.",
        "must_not_show": "no halo; no idealizing — real weathered working faces, each distinct.",
        "scene": (
            "The faces about to be astonished are gloriously "
            "unremarkable: close along the front of the crowd — a "
            "fisherman whose hands are more rope-scar than skin, a "
            "mother rocking a drowsy child with her eyes fixed "
            "uphill, a farmer with field dust still in the creases "
            "of his neck — nobody a scribe, nobody important, "
            "everybody listening with the particular stillness of "
            "people who suspect, correctly, that the next sentence "
            "is about them. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r121-b04", "out": "s04-ye-are-the-salt-of.jpeg", "seg": "jv13",
        "window": "18.29-25.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Ye are the salt of the earth: but if the salt have lost his "
            "savour, wherewith shall it be salted?"
        ),
        "must_show": "SCRIPTURE-EXACT: the saying — Jesus seated, open hand extended toward the crowd as he gives them the name; the nearest listeners' faces taking it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture GIVING, not lecturing.",
        "scene": (
            "The astonishing sentence is handed over: Jesus seated "
            "in the warm gold light, one open hand extended toward "
            "the crowd the way a man hands something valuable "
            "across a table — YE are the salt of the earth — and on "
            "the nearest faces the first startled arithmetic of it, "
            "fishermen and field hands being told they are the "
            "thing that keeps the whole world from spoiling, by a "
            "teacher whose eyes say he is not exaggerating. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b05", "out": "s05-it-is-thenceforth-good-for.jpeg", "seg": "jv13",
        "window": "25.07-32.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE"],
        "narration": (
            "it is thenceforth good for nothing, but to be cast out, and to "
            "be trodden under foot of men."
        ),
        "must_show": "SCRIPTURE-EXACT: the fate of flat salt — pale spent salt scattered on the packed-earth path, sandaled feet walking over it without a glance.",
        "must_not_show": "no halo; no faces needed — the FEET and the trodden salt carry the verse.",
        "scene": (
            "The verse's warning lies underfoot: a scatter of pale "
            "spent salt strewn across the packed earth of the lane "
            "where it was thrown out, and passing over it without "
            "so much as a downward glance the worn sandaled feet of "
            "the village going about its day — the once-precious "
            "crystals pressed flat into the dirt, indistinguishable "
            "from the dust in one more footfall — good for nothing, "
            "exactly as promised, and trodden exactly so. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b06", "out": "s06-he-began-with-salt.jpeg", "seg": "n1",
        "window": "15.74-17.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET"],
        "narration": "He began with salt.",
        "must_show": "the subject itself — a small clay bowl of coarse grey-white salt on the market stall, a work-worn hand taking a pinch; humble and precious at once.",
        "must_not_show": "no halo; period-true only — clay, wood, coarse crystals; nothing refined or modern.",
        "scene": (
            "The first sermon illustration sits in a clay bowl: "
            "coarse grey-white salt heaped small and precious on "
            "the market stall's worn boards, catching the bright "
            "day like crushed frost — and a work-worn hand taking a "
            "careful pinch of it, the thumb and two fingers of "
            "somebody who knows exactly what it costs and exactly "
            "what it does — the humblest treasure in the village, "
            "about to be handed to a hillside full of people as "
            "their own job description. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b07", "out": "s07-in-that-world-salt-was.jpeg", "seg": "n2",
        "window": "34.06-35.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET"],
        "narration": "In that world salt was precious.",
        "must_show": "the preciousness — the merchant weighing salt on the small brass balance while two buyers watch the pans intently; worth measured like coin.",
        "must_not_show": "no halo; the scale PERIOD-TRUE — a simple brass balance, no modern weights.",
        "scene": (
            "Its price is written on the watching faces: at the "
            "stall the merchant tips coarse salt into one pan of "
            "the small brass balance, weight against weight, while "
            "two buyers lean in close enough to fog the metal — "
            "eyes following every crystal the way eyes follow "
            "silver — a commodity handled by the pinch and paid "
            "for by the grain, worth guarding, worth haggling "
            "over, worth exactly the comparison the teacher on the "
            "hill is about to spend it on. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b08", "out": "s08-that-he-told-them-is.jpeg", "seg": "n2",
        "window": "39.73-46.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "That, he told them, is what you are — you keep the world from "
            "going bad, and you bring out the good in it."
        ),
        "must_show": "the naming — Jesus leaning toward the crowd, both hands open at them, conferring the identity; warmth and full seriousness together.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd receiving DIGNITY, not flattery.",
        "scene": (
            "The identity is conferred like a commission: Jesus "
            "leaning slightly forward from his seat with both hands "
            "open toward the crowd — that is what YOU are — the "
            "warm gold light on his earnest face, no smile of "
            "flattery and no edge of test, just the level look of a "
            "man informing people of their actual worth: keepers of "
            "the world's goodness, bringers-out of its flavour, "
            "appointed on a hillside between their nets and their "
            "fields. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r121-b09", "out": "s09-you-matter-that-much.jpeg", "seg": "n2",
        "window": "46.62-48.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "You matter that much.",
        "must_show": "the landing — close on two or three crowd faces as the worth sinks in: a fisherman's guarded eyes easing, a mother's chin lifting; ordinary people believing it a little.",
        "must_not_show": "no halo; the change SMALL and true — no weeping, no rapture; quiet dignity arriving.",
        "scene": (
            "The sentence finds its mark quietly: close on the "
            "front row as the words settle — the old fisherman's "
            "guarded squint easing open by a degree, the tired "
            "mother's chin coming up off her child's hair, a young "
            "farmer glancing sideways to see if the others heard it "
            "too — nothing dramatic, just the small unbending of "
            "people who walked up the hill ordinary and are being "
            "told, by someone they believe, that they matter that "
            "much. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r121-b10", "out": "s10-but-salt-has-one-job.jpeg", "seg": "n3",
        "window": "48.99-58.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["KITCHEN"],
        "narration": (
            "But salt has one job, and if it goes flat and loses its flavour "
            "it is no use to anyone — it just gets swept out and walked "
            "over."
        ),
        "must_show": "the sweeping-out — in the kitchen doorway a woman sweeps spent flat salt out onto the path with a rush broom; the useless remainder leaving the house.",
        "must_not_show": "no halo; her face MATTER-OF-FACT — this is housework, not a parable performed.",
        "scene": (
            "What happens to flavourless salt happens in every "
            "kitchen: at the bright doorway a woman works her rush "
            "broom in short practical strokes, sweeping a sad pale "
            "drift of spent salt over the threshold and out onto "
            "the path — matter-of-fact as any housework, no "
            "ceremony for the stuff that stopped doing its one job "
            "— the crock it failed still on the shelf behind her, "
            "waiting to be filled with salt that still tastes like "
            "something. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r121-b11", "out": "s11-he-was-not-threatening-them.jpeg", "seg": "n3",
        "window": "58.18-62.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": (
            "He was not threatening them; he was telling them not to waste "
            "what they were."
        ),
        "must_show": "the tone — close on Jesus's face mid-teaching: earnest, warm, urgent without any anger; a friend warning against waste, not a judge warning of wrath.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOTHING stern — the gentleness is the point.",
        "scene": (
            "The tone of the warning is the whole theology of it: "
            "close on Jesus's face in the warm light, and there is "
            "no thunder anywhere in it — the brows earnest, the "
            "eyes on his people with the particular urgency of "
            "someone who can see what they are worth being left in "
            "the sun to go flat — a friend's warning, spoken the "
            "way you tell somebody not to leave a treasure out in "
            "the rain, because it is theirs and it is real and he "
            "wants them to keep it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r121-b12", "out": "s12-stay-yourselves-ye-are-the.jpeg", "seg": "n3 + jv14",
        "window": "64.19-68.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Stay yourselves. Ye are the light of the world.",
        "must_show": "SCRIPTURE-EXACT: the second name — Jesus's hand rising from the salt saying toward the wide bright sky; the crowd's faces lifting with the gesture.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the LIGHT in the frame is plain daylight only.",
        "scene": (
            "The second name is bigger than the first: Jesus's open "
            "hand rises from the crowd toward the wide bright sky "
            "over the lake — ye are the LIGHT of the world — and "
            "the listening faces lift with the gesture, fishermen "
            "and mothers blinking up into plain afternoon daylight "
            "while the teacher hands them a title that big without "
            "a flicker of irony — the same ordinary people, "
            "renamed twice in one sermon, each name larger than "
            "their whole village. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r121-b13", "out": "s13-a-city-that-is-set.jpeg", "seg": "jv14 + n4",
        "window": "68.27-74.72", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD", "HILLTOWN"],
        "narration": (
            "A city that is set on an hill cannot be hid. Then he pointed "
            "them to light."
        ),
        "must_show": "SCRIPTURE-EXACT: the pointing — Jesus's arm extended toward the far hilltop town across the lake; the crowd's heads turned, following the point to the same ridge.",
        "must_not_show": "no halo; DIRECTION LAW — every gaze follows the pointing arm to the town, nobody looking elsewhere.",
        "scene": (
            "The next illustration is already built and waiting: "
            "Jesus's arm extends past the crowd toward the far "
            "ridge across the lake where the pale stone town sits "
            "stacked on its hill — and every head on the slope "
            "turns with the pointing hand, fishermen shading their "
            "eyes, children standing up in the grass to see — the "
            "whole congregation looking one direction at one small "
            "city that has never once, in all its centuries on "
            "that ridge, managed to hide. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b14", "out": "s14-a-town-built-up-on.jpeg", "seg": "n4",
        "window": "74.72-82.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLTOWN"],
        "narration": (
            "A town built up on a hilltop, its lamps lit at dusk, can be "
            "seen for miles — there is no hiding it."
        ),
        "must_show": "the town at lamplighting — dusk on the ridge, the stacked stone houses pricked with warm lamplit windows, visible across the whole darkening country. INTENTIONAL DUSK.",
        "must_not_show": "no halo; the dusk DELIBERATE (not the row-11 defect) — warm windows against blue evening.",
        "scene": (
            "The illustration performs itself every evening: dusk "
            "settles blue over the lake country and the hilltop "
            "town answers it window by window — warm lamplight "
            "pricking on in the stacked stone houses until the "
            "whole ridge wears its little constellation, visible "
            "from every road, every boat, every farm for miles of "
            "darkening land — a city doing the one thing a lit "
            "city on a hill cannot help doing, which is being "
            "seen. No people are distinguishable at this distance."
        ),
    },
    {
        "id": "v2-r121-b15", "out": "s15-that-he-said-is-you.jpeg", "seg": "n4",
        "window": "82.04-89.49", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "That, he said, is you: not something the world should have to "
            "squint to find, but a light set up where everyone can see."
        ),
        "must_show": "the application — Jesus turning from the far town back to the crowd, open hand moving from ridge to people; the comparison landing on their faces.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the light PLAIN daylight — the metaphor stays verbal.",
        "scene": (
            "The comparison completes its arc: Jesus's open hand "
            "swings back from the far ridge to the people on the "
            "grass — from THAT to YOU — and the crowd receives the "
            "trajectory, a few heads still half-turned toward the "
            "town while their eyes come back to the teacher, "
            "wearing the look of people being measured against a "
            "city and told, unbelievably, that they are the "
            "brighter landmark — not to be squinted for, but set "
            "up where every eye can find them. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b16", "out": "s16-it-kept-food-from-spoiling.jpeg", "seg": "n2",
        "window": "35.83-39.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["KITCHEN"],
        "narration": "It kept food from spoiling and it made plain things taste good.",
        "must_show": "salt's two jobs in one kitchen — fish being packed in salt in a clay crock, and beside it a woman tasting stew from a wooden spoon, pleased.",
        "must_not_show": "no halo; both jobs VISIBLE — preservation in the crock, flavour on her face.",
        "scene": (
            "Both of salt's jobs share one kitchen: on the table a "
            "clay crock where silver fish are being laid down in "
            "white layers of salt, packed against the spoiling "
            "months — and at the clay oven beside it a woman lifts "
            "a wooden spoon from the stew, tastes, and her whole "
            "face agrees with the seasoning — preservation in the "
            "crock and flavour at the pot, the two humble miracles "
            "the teacher on the hill just handed to his listeners "
            "as their own work in the world. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b17", "out": "s17-neither-do-men-light-a.jpeg", "seg": "jv15",
        "window": "90.07-98.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPHOUSE"],
        "narration": (
            "Neither do men light a candle, and put it under a bushel, but "
            "on a candlestick; and it giveth light unto all that are in the "
            "house."
        ),
        "must_show": "SCRIPTURE-EXACT: the lamp on the stand — a hand setting the lit clay lamp on the wooden lampstand, warm light reaching the whole one-room house and the family in it; the bushel basket idle by the wall.",
        "must_not_show": "no halo; the light PHYSICAL from the flame only; the basket VISIBLE and unused.",
        "scene": (
            "The verse is staged in every home each evening: a hand "
            "sets the small lit clay lamp up on the wooden "
            "lampstand, and the one-room house fills — warm "
            "flame-light finding the low table, the sleeping mats, "
            "the faces of the family settling for the evening, "
            "every corner served by one small fire lifted high — "
            "while against the wall the woven bushel basket sits "
            "idle at its proper work of measuring grain, employed "
            "by nobody, ever, for the smothering of lamps. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b18", "out": "s18-nobody-lights-a-lamp-and.jpeg", "seg": "n5",
        "window": "99.93-102.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPHOUSE"],
        "narration": "Nobody lights a lamp and then hides it under a basket.",
        "must_show": "the absurdity enacted — a man lowering the bushel basket over the lit lamp on its stand, the room already dimming around the act; visibly foolish.",
        "must_not_show": "no halo; the flame not yet out — light leaking at the basket's rim as it descends.",
        "scene": (
            "The absurdity is demonstrated so nobody forgets it: a "
            "man lowers the woven bushel basket down over the lit "
            "lamp on its stand — the room's warm light collapsing "
            "around the act, shadows climbing the mudbrick walls, "
            "the family's faces falling into dimness — while a "
            "last stubborn seam of light leaks at the descending "
            "rim like the lamp protesting the arrangement — the "
            "one thing no one in the history of houses has ever "
            "done on purpose, done once, for the lesson. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b19", "out": "s19-that-would-be-pointless-smothering.jpeg", "seg": "n5",
        "window": "102.73-107.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPHOUSE"],
        "narration": "That would be pointless — smothering the very thing they lit it for.",
        "must_show": "the pointlessness — the basket seated over the lamp, the room in gloom, the family's faces in shadow around a light that exists and serves no one.",
        "must_not_show": "no halo; a thin seam of light at the basket's rim only — the waste made visible.",
        "scene": (
            "The result argues against itself: the basket sits "
            "seated over the lamp and the house sits in gloom — "
            "the family's faces gone to shadow around the low "
            "table, the corners lost, the whole room poorer by "
            "one hidden flame — while at the basket's rim a thin "
            "seam of wasted light marks where the burning goes on "
            "serving nobody — a lamp fully lit and fully useless, "
            "the very thing it was kindled for smothered under a "
            "grain-measure. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r121-b20", "out": "s20-you-set-it-up-high.jpeg", "seg": "n6",
        "window": "107.86-114.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAMPHOUSE"],
        "narration": (
            "You set it up high, on a stand, so its light reaches into every "
            "corner and everyone in the house can see."
        ),
        "must_show": "the restoration — the basket lifted away and the lamp raised high on its stand, warm light flooding back into every corner, the family's faces bright again.",
        "must_not_show": "no halo; the relief on the FACES — light restored where it belongs.",
        "scene": (
            "The room gets its light back the way it was always "
            "meant to: the basket swung away to the wall and the "
            "small lamp lifted high onto its wooden stand, the "
            "warm flame-light rolling back out to the corners — "
            "the low table found again, the sleeping mats, the "
            "children's faces tipping up bright around the little "
            "fire — one flame doing for the whole house what it "
            "was kindled to do, from exactly the high place it "
            "was made to do it from. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b21", "out": "s21-your-goodness-was-never-meant.jpeg", "seg": "n6",
        "window": "114.52-120.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE"],
        "narration": (
            "Your goodness was never meant to be hidden away. It was meant "
            "to give light to the people around you."
        ),
        "must_show": "the application — an open doorway at nightfall spilling warm lamplight across the lane, a passing neighbour's face caught and warmed in it; goodness reaching the street.",
        "must_not_show": "no halo; the light from the DOORWAY only, physical and warm.",
        "scene": (
            "What the lamp teaches, the doorway preaches: an open "
            "door at nightfall spills its warm lamplight clear "
            "across the packed earth of the lane, a long bright "
            "lane-crossing carpet of it — and a neighbour passing "
            "in the dark walks into the spill and is warmed and "
            "lit by somebody else's evening — the house's small "
            "goodness reaching people who never knocked, the way "
            "light does when nobody hides it, which is the entire "
            "sermon in one street. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r121-b22", "out": "s22-let-your-light-so-shine.jpeg", "seg": "jv16",
        "window": "121.07-128.45", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Let your light so shine before men, that they may see your good "
            "works, and glorify your Father which is in heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the charge — Jesus with both arms open over the crowd in the late gold light, giving the commission; the crowd receiving it as a sending.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gold is the SUN's, on everyone equally.",
        "scene": (
            "The commission is given with both hands: Jesus with "
            "his arms open over the seated crowd, the late gold "
            "lying equally on his cream robe and their browns and "
            "russets, speaking the charge that turns listeners "
            "into lamps — let it SHINE, so the seeing runs past "
            "you to your Father — and across the slope the "
            "ordinary faces take it the way people take a sending "
            "rather than a saying, already half-turned toward the "
            "villages they will carry it home to. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b23", "out": "s23-stay-salty.jpeg", "seg": "n3",
        "window": "62.65-64.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Stay salty.",
        "must_show": "the phrase landing light — a young fisherman in the crowd breaking into a grin at the words; the sermon's warmth felt.",
        "must_not_show": "no halo; the grin REAL and quick — one face's delight, not a laughing crowd.",
        "scene": (
            "The sermon's smallest sentence gets its smile: close "
            "on a young fisherman in the second row as the words "
            "land — the sunburnt face cracking into a quick "
            "involuntary grin, the kind a man wears when a teacher "
            "says something that sounds exactly like the docks — "
            "around him the older heads stay grave and attentive, "
            "but for one beat the hillside holds a boy delighted "
            "that the kingdom of heaven apparently knows how to "
            "talk like a fisherman. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b24", "out": "s24-but-notice-the-reason-not.jpeg", "seg": "n8",
        "window": "135.90-138.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE"],
        "narration": "But notice the reason. Not so they will admire you.",
        "must_show": "the anti-vanity — a man steadying an old beggar and giving bread, his own face turned to his task while passers-by notice; the doer not collecting the credit.",
        "must_not_show": "no halo; NO posing — his eyes on the beggar, never on the audience.",
        "scene": (
            "The reason is guarded in the doer's own eyes: in the "
            "lane a man kneels to steady an old beggar and press "
            "bread into the shaking hands — and though two "
            "passers-by have stopped to watch, his face never "
            "once turns toward the watching: eyes down on the old "
            "man's grip, on the work itself — the good deed done "
            "in full view and aimed entirely away from applause, "
            "the seen part accidental, the serving part the whole "
            "point. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r121-b25", "out": "s25-so-that-when-they-see.jpeg", "seg": "n8",
        "window": "138.94-145.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE"],
        "narration": (
            "So that when they see the good you do, their eyes will lift "
            "past you to God, and they will love him for it."
        ),
        "must_show": "the eyes lifting PAST — the helped old beggar looking up beyond his helper's shoulder toward the evening sky in thanks; gratitude travelling through the doer to God.",
        "must_not_show": "no halo; nothing IN the sky — the lifting gaze itself carries the doctrine.",
        "scene": (
            "Where the credit goes is written in one upward look: "
            "the old beggar, bread held to his chest, lifts his "
            "face right past the shoulder of the man who helped "
            "him — up beyond the rooflines to the deepening "
            "evening sky, lips moving in a thanks that skips the "
            "middleman entirely — while the helper, still "
            "steadying him, becomes exactly what the sermon "
            "designed him to be: not the destination of the "
            "gratitude, just the clear glass it shines through on "
            "its way home. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r121-b26", "out": "s26-your-light-is-not-about.jpeg", "seg": "n8",
        "window": "145.11-148.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLTOWN"],
        "narration": "Your light is not about you at all. It points home to your Father.",
        "must_show": "the pointing-home — the lamplit hill town under the first stars, its warm windows answering the sky's lights; earthly light and heaven's in one upward frame.",
        "must_not_show": "no halo; the composition VERTICAL — town light below, stars above, the eye led upward.",
        "scene": (
            "The picture points the same direction as the doctrine: "
            "the hilltop town wears its warm lamplit windows under "
            "a sky where the first stars have come out — the "
            "little human lights and the great high ones stacked "
            "in one vertical frame, the eye climbing naturally "
            "from the ridge's warm glimmer up into the deepening "
            "blue — every lamp in the town aimed, whether it "
            "knows it or not, at the Father the whole shining was "
            "always about. No people are distinguishable at this "
            "distance."
        ),
    },
    {
        "id": "v2-r121-b27", "out": "s27-that-is-the-whole-charge.jpeg", "seg": "n9",
        "window": "149.46-155.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": (
            "That is the whole charge, and it is a gentle one. You do not "
            "have to become something you are not."
        ),
        "must_show": "the gentleness — close on Jesus's face at the sermon's close: warm, settled, a hand resting at his own chest; a charge given like a gift.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOTHING demanding in the face — pure warmth.",
        "scene": (
            "The whole charge fits in one gentle face: close on "
            "Jesus in the last warm light, one hand resting easy "
            "at his own chest, the deep brown eyes moving over his "
            "people with unhurried affection — no demand anywhere "
            "in the features, no bar being raised — the look of "
            "someone finishing a commission that asks nobody to "
            "become anything, only to stay what he has just told "
            "them they already are, and to stop hiding it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b28", "out": "s28-you-already-are-salt-you.jpeg", "seg": "n9",
        "window": "155.60-162.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "You already are salt; you already are light. Just don't lose "
            "your savour, and don't hide your lamp."
        ),
        "must_show": "the crowd changed — the ordinary faces in the golden last light, carrying the two names; the same people as b03, visibly dignified.",
        "must_not_show": "no halo; the SAME faces as the early beats — continuity of the fisherman, the mother, the farmer.",
        "scene": (
            "The same faces from the sermon's start wear its ending "
            "differently: the rope-scarred fisherman, the tired "
            "mother, the dusty farmer — golden last light on the "
            "same ordinary features, and something new in the way "
            "they hold their heads: people who climbed the hill as "
            "nobody in particular sitting now in possession of two "
            "names, salt and light, already theirs, needing only "
            "to be kept — the most valuable things anyone ever "
            "told them, folded up to carry home. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r121-b29", "out": "s29-go-out-stay-bright-and.jpeg", "seg": "n9",
        "window": "162.52-166.92", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": "Go out, stay bright, and be exactly what the world needs.",
        "must_show": "the sending — the crowd dispersing down the hillside paths toward their villages in golden evening, Jesus watching from the slope; the charge walking out into the world.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION LAW — the crowd moves DOWNHILL AWAY toward the villages, backs to the camera.",
        "scene": (
            "The sermon ends by scattering, the camera set behind "
            "Jesus's shoulder at the crest: down the green slope "
            "the crowd breaks apart along the worn paths, "
            "fishermen toward the shore, farmers toward the far "
            "fields, mothers with children on hips toward the "
            "village — all of them walking away downhill into the "
            "golden evening with their backs to the height, "
            "carrying salt and light out to every house below — "
            "while the teacher stands watching his commission "
            "disperse exactly as intended: outward. Every figure "
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
    "HILLSIDE": "PLACE-REF/hillside.jpeg",  # build-121-salt-and-light s01-jesus-sat-on-a-green (manual)
    "HILLTOWN": "PLACE-REF/hilltown.jpeg",  # build-121-salt-and-light s14-a-town-built-up-on (manual)
    "KITCHEN": "PLACE-REF/kitchen.jpeg",  # build-121-salt-and-light s10-but-salt-has-one-job (manual)
    "LAMPHOUSE": "PLACE-REF/lamphouse.jpeg",  # build-121-salt-and-light s17-neither-do-men-light-a (manual)
    "LANE": "PLACE-REF/lane.jpeg",  # build-121-salt-and-light s02-live-openly-good-kind-honest (manual)
    "MARKET": "PLACE-REF/market.jpeg",  # build-121-salt-and-light s06-he-began-with-salt (manual)
}
# === end PLACE-PLATES ===
