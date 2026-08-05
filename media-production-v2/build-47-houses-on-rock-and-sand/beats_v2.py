#!/usr/bin/env python3
"""V2 beat map — row 47, build-47-houses-on-rock-and-sand (Matthew 7:24-29).

COVERAGE: 37 pictures over 208.1 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 7:24-29 KJV):
  Context: the CLOSE of the Sermon on the Mount (v28 "when Jesus had ended
  these sayings") — the frame beats stage the grassy mount above the lake
  at late afternoon, the great seated crowd, and the astonished silence at
  the end. A staging distinct from every earlier row.
  v24   "whosoever HEARETH these sayings of mine, AND DOETH THEM ... built
        his house upon a ROCK" — both men HEAR the same words; the
        narration hammers it, so both builders appear in the listening
        crowd beat.
  v25   "the RAIN descended, and the FLOODS came, and the WINDS blew, and
        beat upon that house; and IT FELL NOT" — one storm, two houses.
        The flood is a WADI FLASH FLOOD: the smooth dry riverbed becoming
        a wall of water — regional truth the narration teaches.
  v26-27 the sand builder: the same words heard, the digging skipped; his
        house IDENTICAL-looking in fair weather (the narration insists —
        one twin-houses beat); "IT FELL: and great was the fall of it."
        THE MAN GETS OUT (narration protects him — he is shown scrambling
        clear, wet and alive; no death, no body).
  v28-29 "the people were ASTONISHED at his doctrine: for he taught them
        as one having AUTHORITY, and not as the scribes" — the stunned
        crowd beat, then the closing invitation ('the door is open, and
        the light is already on inside').

TIME OF DAY: the mount frame beats are late golden afternoon. The
building beats run dry-season daylight over weeks. The STORM beats are
dark grey-green storm daylight with driven rain — a daytime tempest (no
time stated in scripture; not the row-11 night defect, and stated so
here). The aftermath is rinsed clear morning. The closing door beat is
warm dusk with a lit window.

CONTENT-CARE: row 47 has no flag in §3. The sand-house builder ESCAPES —
shown alive on the bank; loss of goods only, never of life.

CHANGING CONDITION (kept OUT of the locks): the weather — dry season,
gathering storm, full tempest, rinsed morning — and the two houses'
states. The wise builder's trench and the twin fair-weather houses are
per-beat facts.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "WISE-B": (
        "WISE BUILDER LOCK: the first builder is the same man in every "
        "shot — about forty, compact and deliberate, with a short black "
        "beard, steady eyes and thick capable forearms. He wears a DARK "
        "TERRACOTTA work tunic kilted up, with a leather tool belt "
        "(never cream, never white). His face is shown clearly — "
        "patience worn as competence."
    ),
    "SAND-B": (
        "SAND BUILDER LOCK: the second builder is the same man in every "
        "shot — about thirty-five, quick and likeable, with a trimmed "
        "brown beard, bright hasty eyes and expressive hands. He wears "
        "a DUSTY TEAL work tunic with a cloth belt (never cream, never "
        "white). His face is shown clearly — hurry, not wickedness, is "
        "his whole flaw."
    ),
    "PLAIN": (
        "BUILDING PLAIN LOCK: a broad building plain below brown hills — "
        "a smooth pale band of DRY RIVERBED sand curving through its "
        "middle, a shelf of grey BEDROCK breaking the slope above the "
        "bed's far bank, scattered thorn scrub, and a track crossing "
        "toward the village. The same riverbed curve, rock shelf and "
        "track in every plain beat."
    ),
    "MOUNT": (
        "TEACHING MOUNT LOCK: the grassy saddle of a hill above the "
        "distant blue of the lake — wildflowers in the grass, "
        "terraces below, and a great seated crowd of every age "
        "spread across the slope in SATURATED DEEP earth colours "
        "(never cream, never white; only Jesus wears cream). Faces "
        "shown clearly. Late golden afternoon light."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r047-b01", "out": "s01-he-had-been-teaching-all.jpeg", "seg": "n1",
        "window": "0.28-5.21", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": (
            "He had been teaching all afternoon, and he ended with a story "
            "about two men and two houses."
        ),
        "must_show": "the frame — the mount at late gold: Jesus standing before the vast seated crowd, the long sermon visibly near its end, the lake far below.",
        "must_not_show": "no halo, glare or rim-light on Jesus; an afternoon's weight in the scene — shadows long, the crowd settled deep.",
        "scene": (
            "On the grassy saddle in the late golden light, the "
            "camera off on the slope's flank taking speaker and "
            "crowd from the side, "
            "Jesus stands before a crowd that has sat "
            "through a whole afternoon — hundreds settled "
            "deep into the wildflowered slope, cloaks spread, "
            "children asleep on laps, the far lake gone soft "
            "blue below — and he is gathering the long "
            "sermon toward its ending, one hand rising for "
            "the last story of the day. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b02", "out": "s02-it-sounds-simple.jpeg", "seg": "n1",
        "window": "5.21-6.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "It sounds simple.",
        "must_show": "the simple materials — a quiet still: a heap of building stones and a stretch of smooth pale sand side by side on the plain; the whole story's inventory.",
        "must_not_show": "no halo, glare or rim-light; two materials, one choice — deceptive plainness.",
        "scene": (
            "A quiet still on the building plain in clear "
            "light: at one side a heap of rough grey "
            "building stones waiting on the slope, and "
            "beside it, smooth as a swept floor, the pale "
            "band of the dry riverbed's sand running away "
            "through the frame — stone and sand, lying in "
            "the same sun, telling nobody anything yet. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r047-b03", "out": "s03-both-of-them-heard-him.jpeg", "seg": "n2",
        "window": "12.04-13.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "SAND-B", "MOUNT"],
        "narration": "Both of them heard him.",
        "must_show": "SCRIPTURE-CRITICAL: the two builders side by side IN the listening crowd — same row, same words reaching both faces.",
        "must_not_show": "no halo, glare or rim-light; the two men visibly equal here — same attention, same hearing; the difference comes later.",
        "scene": (
            "Close in the seated crowd on the golden slope: "
            "the compact terracotta-clad builder and the "
            "quick teal-clad one sit almost shoulder to "
            "shoulder in the same row, both faces lifted "
            "toward the unseen teacher, both listening with "
            "the same open attention — two men receiving "
            "the identical afternoon, indistinguishable in "
            "everything the eye can check. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b04", "out": "s04-that-matters-so-hold-onto.jpeg", "seg": "n2 + n3",
        "window": "14.65-22.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "PLAIN"],
        "narration": (
            "That matters, so hold onto it: both men heard exactly the same "
            "thing. The first man goes home to build."
        ),
        "must_show": "the first homecoming — the wise builder arriving on the plain with his tools and stone-sledge, surveying the ground with unhurried measuring eyes.",
        "must_not_show": "no halo, glare or rim-light; the survey BEFORE the work — a man reading ground the way scholars read.",
        "scene": (
            "In the clear morning the compact builder stands "
            "on the plain with his tool bag down and his "
            "stone-sledge ropes still over one shoulder, "
            "turning slowly where he stands — his steady "
            "eyes travelling from the smooth easy sand of "
            "the riverbed up to the grey rock shelf on the "
            "far bank and back — a man reading the ground "
            "like a contract before he signs it with a "
            "house. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r047-b05", "out": "s05-in-that-country-you-build.jpeg", "seg": "n3",
        "window": "22.00-29.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": (
            "In that country you build in the dry season, and the easy ground "
            "is the smooth, flat sand of a dry riverbed."
        ),
        "must_show": "the regional truth — the dry riverbed at its most inviting: smooth, flat, pale, level as a floor through the plain; the trap in its fair-weather disguise.",
        "must_not_show": "no halo, glare or rim-light; the sand GENUINELY attractive — level, clean, ready-looking; no visible menace.",
        "scene": (
            "The dry riverbed curves through the plain like "
            "a road already built — its sand smooth, pale "
            "and dead level from bank to bank, swept clean "
            "by winters nobody is thinking about in this "
            "heat, firm-looking underfoot, mercifully flat "
            "in a country of slopes — the most inviting "
            "building ground for a day's walk in any "
            "direction, lying exactly where water goes when "
            "there is water. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r047-b06", "out": "s06-but-this-man-walks-past.jpeg", "seg": "n3",
        "window": "29.61-32.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "PLAIN"],
        "narration": "But this man walks past the easy ground.",
        "must_show": "the walk-past — the wise builder crossing the inviting sand WITHOUT stopping, heading up the far bank toward the grey rock shelf with his loaded sledge.",
        "must_not_show": "no halo, glare or rim-light; the refusal in motion — the easy ground underfoot and declined mid-stride.",
        "scene": (
            "Straight across the smooth inviting sand the "
            "builder hauls his loaded stone-sledge without "
            "so much as a pause — his boots printing the "
            "easy level ground he is declining, his steady "
            "eyes already up on the grey rock shelf of the "
            "far bank where the pulling gets hard — a man "
            "walking over the comfortable answer on his way "
            "to the true one. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b07", "out": "s07-he-digs-down-through-the.jpeg", "seg": "n4",
        "window": "33.53-40.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "PLAIN"],
        "narration": (
            "He digs. Down through the loose soil, all the way to bedrock, and "
            "he lays his foundation on the stone."
        ),
        "must_show": "SCRIPTURE-EXACT: the digging — the builder waist-deep in his foundation trench above the rock shelf, spoil heaped, the grey bedrock just bared at the trench's floor.",
        "must_not_show": "no halo, glare or rim-light; real depth — waist-deep at least; the bared bedrock visibly REACHED.",
        "scene": (
            "Waist-deep in his own trench on the high bank "
            "the builder swings his pick — spoil heaped high "
            "on both sides, sweat darkening his terracotta "
            "back — and at the trench's floor, just bared "
            "beneath the last of the loose brown soil, the "
            "grey bedrock shows flat and absolute, the "
            "bottom of the question, arrived at the hard "
            "way. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r047-b08", "out": "s08-it-is-slow-hard-work.jpeg", "seg": "n4",
        "window": "40.81-46.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B"],
        "narration": (
            "It is slow, hard work, and when he is done not one person will "
            "ever see it."
        ),
        "must_show": "the invisible cost — close on the builder's blistered hands laying the first foundation stone true on the bedrock at the trench's dim floor.",
        "must_not_show": "no halo, glare or rim-light; the trench's privacy — work done well where no eye will follow.",
        "scene": (
            "Down in the trench's shadow the builder's "
            "blistered hands set the first great foundation "
            "stone onto the bared bedrock — knuckles raw, "
            "the stone eased a thumb's width left and "
            "checked with a wooden level, then eased again — "
            "craftsmanship spent lavishly at the bottom of "
            "a hole that mortar and backfill will hide "
            "before the week is out. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b09", "out": "s09-the-whole-house-depends-on.jpeg", "seg": "n4",
        "window": "46.46-49.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "The whole house depends on the part nobody can see.",
        "must_show": "the hidden spine — a cutaway-feel close: the finished foundation course gripping the bedrock as backfill buries it; the load path made visible once, then covered.",
        "must_not_show": "no halo, glare or rim-light; the covering mid-act — soil sliding over true stonework.",
        "scene": (
            "Close at the trench's edge: the finished "
            "foundation course lies gripped to the grey "
            "bedrock in true mortared joints — and the "
            "backfill is already sliding over it from a "
            "tipped basket, dry soil running across the "
            "clean stonework and taking it out of the "
            "world's sight forever — the house's whole "
            "future disappearing correctly underground. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r047-b10", "out": "s10-therefore-whosoever-heareth-these-sayings.jpeg", "seg": "jv24",
        "window": "50.43-60.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": (
            "Therefore whosoever heareth these sayings of mine, and doeth them, "
            "I will liken him unto a wise man, which built his house upon a "
            "rock."
        ),
        "must_show": "SCRIPTURE-EXACT: the likening — Jesus on the mount delivering the verse, one hand flat and firm on the air like a man patting stone; the crowd's builders listening hard.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the flat-hand gesture — rock, mimed; the sermon's engineering lesson.",
        "scene": (
            "On the golden mount Jesus gives the likening "
            "with one hand pressed flat and firm on the air "
            "before him — the exact gesture of a mason "
            "testing sound stone — his voice's weight "
            "visible in the stillness of the nearest rows, "
            "where working men who have dug real trenches "
            "hear their trade suddenly promoted into "
            "scripture. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r047-b11", "out": "s11-picture-two-men-in-that.jpeg", "seg": "n2",
        "window": "10.20-12.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "Picture two men in that crowd.",
        "must_show": "the crowd scanned — a wide slow look across the seated hundreds on the slope, any two of whom could be the story's two; the camera hunting faces.",
        "must_not_show": "no halo, glare or rim-light on Jesus (small at frame's edge); the crowd the subject — everyman's parable seeded among real faces.",
        "scene": (
            "From behind Jesus's shoulder the camera sweeps the "
            "wide slope of seated listeners filling the "
            "frame in the late gold — row upon row of "
            "farmers, fishermen, mothers, tradesmen, old "
            "men, every face holding the afternoon's words "
            "in its own way — and somewhere in the sweep of "
            "them, indistinguishable from their neighbours, "
            "sit the story's two men, wearing ordinary "
            "faces like everyone else's, with the small "
            "cream figure of the teacher far at the slope's "
            "foot. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r047-b12", "out": "s12-it-takes-longer-and-for.jpeg", "seg": "n5",
        "window": "61.93-68.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "PLAIN"],
        "narration": (
            "It takes longer. And for a while, in the good weather, it does not "
            "look one bit better than any other house on the plain."
        ),
        "must_show": "the unglamorous truth — the wise builder's house finished on its bank in fair weather: plain, ordinary, indistinguishable; weeks of hidden work buying zero visible advantage.",
        "must_not_show": "no halo, glare or rim-light; deliberately ordinary — nothing about the house advertises its foundation.",
        "scene": (
            "On the high bank above the riverbed the "
            "finished house stands in the fair-weather "
            "light — a plain flat-roofed stone house like a "
            "hundred others, its walls honest and "
            "unremarkable, a water jar by the door, nothing "
            "anywhere on its face to show the weeks in the "
            "trench — while its builder packs his tools "
            "below it, a man whose best work will not be "
            "visible until the worst day of the year. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b13", "out": "s13-because-of-what-was-underneath.jpeg", "seg": "n6",
        "window": "83.83-86.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "Because of what was underneath it.",
        "must_show": "the answer beneath — the storm-lashed house in cutaway-feel: rain streaming off it above, and below ground the foundation course gripping bedrock, unmoved.",
        "must_not_show": "no halo, glare or rim-light; the underground grip shown once at the crisis — the hidden spine bearing the visible storm.",
        "scene": (
            "In the grey-green storm light the house stands "
            "streaming on its bank — and the frame's lower "
            "depth shows what the storm cannot see: beneath "
            "the flooded surface, the mortared foundation "
            "course still gripping the grey bedrock exactly "
            "as it was laid, water sheeting harmlessly over "
            "stonework that has not moved a hair, the whole "
            "roaring argument above being answered from "
            "below in complete silence. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b14", "out": "s14-and-the-rain-descended-and.jpeg", "seg": "jv25",
        "window": "68.98-78.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": (
            "And the rain descended, and the floods came, and the winds blew, "
            "and beat upon that house; and it fell not: for it was founded upon "
            "a rock."
        ),
        "must_show": "SCRIPTURE-EXACT: the storm at the rock house — a daytime tempest: driven grey rain, the riverbed below running brown and violent, wind-bent scrub — and the house standing square and unmoved on its bank.",
        "must_not_show": "no halo, glare or rim-light; DAYTIME storm (grey-green, stated in header — not the night defect); the house's stillness against everything moving.",
        "scene": (
            "The daytime tempest owns the plain: rain "
            "driving in grey sheets, the thorn scrub bent "
            "flat, and the riverbed below transformed — "
            "brown water wall-to-wall where the smooth sand "
            "lay, tearing at its own banks — while up on "
            "the rock shelf the plain little house stands "
            "perfectly, almost insolently square, rain "
            "streaming off its unmoved walls, the one "
            "vertical thing in a horizontal world. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b15", "out": "s15-the-storm-hit-it-with.jpeg", "seg": "n6",
        "window": "80.24-83.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "PLAIN"],
        "narration": "The storm hit it with everything, and the house did not even move.",
        "must_show": "the family inside — through the streaming window: the builder and his family calm at their lamplit table while the tempest rages soundless beyond the wall.",
        "must_not_show": "no halo, glare or rim-light; interior peace against exterior fury — supper during a siege the walls are winning.",
        "scene": (
            "Through the small deep window, past the water "
            "sheeting off the lintel: the builder and his "
            "family sit at their lamplit table over supper — "
            "a child spooning lentils, his wife breaking "
            "bread, the builder's steady face easy in the "
            "lamp's warmth — while the whole grey violence "
            "of the storm hurls itself soundlessly against "
            "walls that are not discussing it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b16", "out": "s16-now-the-second-man-he.jpeg", "seg": "n7",
        "window": "86.73-89.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAND-B", "MOUNT"],
        "narration": "Now the second man. He heard the very same words.",
        "must_show": "the second hearer — close on the teal-clad builder in the crowd, genuinely listening, genuinely moved; the hearing was never his problem.",
        "must_not_show": "no halo, glare or rim-light; NO smirk, no inattention — he hears it all and likes it; that is the tragedy's setup.",
        "scene": (
            "Close in the golden crowd: the quick teal-clad "
            "builder listens with his whole bright face — "
            "nodding along, elbowing his neighbour at a "
            "good line, eyes warm with real appreciation — "
            "a man receiving the sermon's every word and "
            "enjoying them the way he enjoys most things: "
            "quickly, sincerely, and with no particular "
            "plans. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r047-b17", "out": "s17-but-when-he-goes-home.jpeg", "seg": "n7",
        "window": "89.42-97.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAND-B", "PLAIN"],
        "narration": (
            "But when he goes home, he builds the fast, easy way, straight down "
            "on the smooth sand, and he skips the digging altogether."
        ),
        "must_show": "SCRIPTURE-EXACT: the shortcut — the sand builder laying his first wall course directly on the smooth riverbed sand, no trench anywhere, work racing along.",
        "must_not_show": "no halo, glare or rim-light; the speed attractive — the wall rising visibly fast; the missing trench the frame's quiet alarm.",
        "scene": (
            "Down on the smooth pale sand of the riverbed "
            "the teal-clad builder lays stone at a happy "
            "sprint — the first course set directly on the "
            "swept sand, the second already rising, his "
            "mortar boy jogging to keep up — no trench, no "
            "spoil heap, no pick anywhere on the site, just "
            "clean fast visible progress on ground as flat "
            "as a table and as temporary as weather. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b18", "out": "s18-but-everything-he-had-built.jpeg", "seg": "n9",
        "window": "139.94-142.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAND-B", "PLAIN"],
        "narration": "But everything he had built was gone.",
        "must_show": "the loss surveyed — the morning after: the sand builder standing on the bank looking at the swept-bare riverbed where his house stood; alive, soaked, emptied.",
        "must_not_show": "no halo, glare or rim-light; the man ALIVE and whole — the loss total but material; grief without injury.",
        "scene": (
            "In the rinsed clear light of the morning after, "
            "the teal-clad builder stands soaked and alive "
            "on the riverbank, arms hanging, looking down "
            "at the place where his house was — the "
            "riverbed swept back to smooth wet sand from "
            "bank to bank, one doorpost stump and a "
            "scatter of his stones lodged far downstream "
            "the only mail the flood left him. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b19", "out": "s19-and-every-one-that-heareth.jpeg", "seg": "jv26",
        "window": "98.27-107.97", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": (
            "And every one that heareth these sayings of mine, and doeth them "
            "not, shall be likened unto a foolish man, which built his house "
            "upon the sand:"
        ),
        "must_show": "SCRIPTURE-EXACT: the second likening — Jesus's open hand now tilted loosely, letting imagined sand run through the fingers; the crowd sobered.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the sand-through-fingers mime — the sermon's second material, demonstrated.",
        "scene": (
            "On the mount Jesus's demonstrating hand has "
            "turned over — tilted loose, fingers slightly "
            "parted, miming sand running out of a fist — "
            "and along the nearest rows the working men who "
            "nodded at the rock have gone soberer, one "
            "mason looking down at his own palms, the "
            "second likening finding its addresses with the "
            "same ease as the first. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b20", "out": "s20-and-here-is-the-thing.jpeg", "seg": "n8",
        "window": "109.50-112.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "And here is the thing. His house looked fine.",
        "must_show": "the twin illusion — BOTH finished houses in one fair-weather frame: rock-house on its bank, sand-house on the riverbed, visually equal in the sunshine.",
        "must_not_show": "no halo, glare or rim-light; genuinely indistinguishable — the frame must refuse to favour either.",
        "scene": (
            "One wide fair-weather frame holds them both: "
            "up on the bank the rock builder's plain house, "
            "and below on the smooth pale bed the sand "
            "builder's — the same flat roofs, the same "
            "honest walls, the same water jars by the same "
            "doors, sunlight lying on both without "
            "preference — two identical answers to the "
            "same sermon, one of which is wrong in a place "
            "the sunshine cannot reach. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b21", "out": "s21-it-went-up-faster-it.jpeg", "seg": "n8",
        "window": "112.25-118.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAND-B", "PLAIN"],
        "narration": (
            "It went up faster, it stood there in the sunshine, and you could "
            "not have told the two houses apart."
        ),
        "must_show": "the shortcut enjoyed — the sand builder relaxing on his finished doorstep in the sunshine, housewarming jug in hand, while the rock builder still hauls stone on the far bank.",
        "must_not_show": "no halo, glare or rim-light; the sand builder's happiness REAL and won fairly by the visible rules — the frame lets him enjoy it.",
        "scene": (
            "On his finished doorstep down on the smooth "
            "sand the teal-clad builder lounges in the "
            "sunshine with a housewarming jug, waving "
            "cheerfully across the riverbed — where up on "
            "the far bank the terracotta-clad builder, "
            "weeks behind, still hauls stone past his spoil "
            "heaps toward walls barely knee-high — the "
            "scoreboard of the visible world posting its "
            "usual early numbers. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b22", "out": "s22-not-until-the-weather-turned.jpeg", "seg": "n8",
        "window": "118.66-120.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "Not until the weather turned.",
        "must_show": "the turn — the plain under a darkening sky: the first grey squall line coming over the brown hills, the light going green-grey, both houses waiting below.",
        "must_not_show": "no halo, glare or rim-light; the gathering only — first wind in the scrub, the storm's edge; the exam paper being handed out.",
        "scene": (
            "Over the brown hills the weather turns: a long "
            "grey squall line rolling in with its rain "
            "already hanging beneath it like a dragged "
            "curtain, the plain's light going green-grey "
            "and strange, the thorn scrub beginning to "
            "lean — and below, small in the changing "
            "light, the two identical houses stand waiting "
            "on their two different answers. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b23", "out": "s23-and-the-rain-descended-and.jpeg", "seg": "jv27",
        "window": "121.23-130.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": (
            "And the rain descended, and the floods came, and the winds blew, "
            "and beat upon that house; and it fell: and great was the fall of "
            "it."
        ),
        "must_show": "SCRIPTURE-EXACT, RESTRAINED: the fall — the sand house mid-collapse into the risen brown flood: walls folding, roof timbers going over — with NO ONE inside or near it.",
        "must_not_show": "no halo, glare or rim-light; the house EMPTY as it falls (the man is out — next beats show him safe); loss of stone and timber only.",
        "scene": (
            "In the storm's grey-green fury the sand house "
            "is going: the flood running wall-to-wall where "
            "the smooth bed was, the near wall folding "
            "outward in a collapse of wet stone, the roof "
            "timbers swinging down into the brown water, "
            "the doorway's rectangle losing its shape — an "
            "empty house being unmade by the water it was "
            "standing in line for since its first course "
            "was laid. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r047-b24", "out": "s24-when-he-finished-the-crowd.jpeg", "seg": "n11a",
        "window": "167.84-169.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "When he finished, the crowd just sat there.",
        "must_show": "SCRIPTURE-EXACT (v28): the astonished silence — the sermon ended, Jesus lowering his hand, and the whole vast slope of people sitting motionless in the last gold.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOBODY moving — a hillside of held breath.",
        "scene": (
            "The sermon has ended: Jesus stands with his "
            "hand just lowered in the deep last gold, and "
            "across the whole vast slope not one person has "
            "moved — hundreds sitting motionless in their "
            "rows, a mother's hand stilled on her child's "
            "hair, an old man's staff forgotten across his "
            "knees, the entire hillside holding the "
            "afternoon's words the way ground holds rain. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r047-b25", "out": "s25-the-same-dry-riverbed-became.jpeg", "seg": "n9",
        "window": "131.74-139.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAND-B", "PLAIN"],
        "narration": (
            "The same dry riverbed became a wall of water, it tore the sand out "
            "from under the house, and there was nothing left. The man got out."
        ),
        "must_show": "SCRIPTURE-PROTECTIVE: the escape — the sand builder scrambling up the bank out of the shallows, hauled the last step by a neighbour's grip, soaked and safe as his house goes behind him.",
        "must_not_show": "no halo, glare or rim-light; the RESCUE prominent — two hands gripping; the man unambiguously alive and clear.",
        "scene": (
            "Up the streaming bank the teal-clad builder "
            "scrambles out of the flood's edge — soaked to "
            "the beard, one knee driving into the mud, his "
            "forearm locked in the two-handed grip of a "
            "neighbour hauling him the last step onto "
            "grass — while behind and below him the brown "
            "water works at the folding remains of his "
            "house, taking everything he built and missing "
            "everything he is. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b26", "out": "s26-two-houses-one-storm.jpeg", "seg": "n10",
        "window": "143.34-145.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "Two houses. One storm.",
        "must_show": "the verdict frame — the morning-after plain: the rock house standing rinsed and whole on its bank; the swept-bare sand where the other stood; one picture, whole sermon.",
        "must_not_show": "no halo, glare or rim-light; clean morning light — the exam graded, the results posted in landscape.",
        "scene": (
            "The rinsed clear morning lays the whole verdict "
            "out in one frame: on the high bank the rock "
            "house stands whole and dripping and ordinary, "
            "its water jar still by its door — and below "
            "it the riverbed runs smooth wet sand from "
            "bank to bank, swept as clean of the second "
            "house as if the summer had imagined it — two "
            "answers to one storm, posted side by side in "
            "morning light. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r047-b27", "out": "s27-one-standing-one-swept-away.jpeg", "seg": "n10",
        "window": "145.30-147.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "SAND-B", "PLAIN"],
        "narration": "One standing, one swept away.",
        "must_show": "the two builders after — the rock builder coming down his bank with a blanket and bread FOR the soaked sand builder; the parable refusing to gloat.",
        "must_not_show": "no halo, glare or rim-light; mercy between the two men — the wise one's first act is kindness, not vindication.",
        "scene": (
            "Down from his standing house the terracotta-"
            "clad builder comes with a dry blanket over one "
            "arm and bread in his hand — crossing the wet "
            "grass to where his soaked neighbour sits "
            "emptied on a stone — and settling the blanket "
            "around the man's shoulders with the "
            "unceremonious grip of one workman for another: "
            "the sermon's wisdom doing, an hour after the "
            "storm, exactly what it heard. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b28", "out": "s28-and-the-only-difference-between.jpeg", "seg": "n10",
        "window": "147.98-155.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": (
            "And the only difference between them was down in the foundation, "
            "where nobody could see it, until the day the water came up and "
            "asked."
        ),
        "must_show": "the difference bared — the flood-cut bank: the storm has exposed the rock house's foundation in cross-section — mortared courses on bedrock, revealed at last by the water that tested them.",
        "must_not_show": "no halo, glare or rim-light; the water itself as the revealer — the hidden work finally visible, by ordeal.",
        "scene": (
            "Where the flood cut the bank away, the earth "
            "stands opened like a book: in the raw "
            "cross-section beneath the standing house, the "
            "mortared foundation courses show gripping the "
            "grey bedrock, laid true in the dark years ago "
            "and bared now by the one force with authority "
            "to ask — the water's question, and the "
            "trench's old answer, meeting in daylight at "
            "last. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r047-b29", "out": "s29-and-it-came-to-pass.jpeg", "seg": "s28",
        "window": "156.17-166.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": (
            "And it came to pass, when Jesus had ended these sayings, the "
            "people were astonished at his doctrine: For he taught them as one "
            "having authority, and not as the scribes."
        ),
        "must_show": "SCRIPTURE-EXACT: the astonishment — faces along the crowd wide with it; Jesus standing simply in the deep gold, the authority carried in stillness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; authority WITHOUT effects — his plainness against their astonishment is the verse.",
        "scene": (
            "The camera looks along the front rows from the "
            "side, faces in three-quarter, as the astonishment stands "
            "open on every face — the mason's mouth parted, "
            "an old scribe-taught elder shaking his head "
            "slowly at sixty years of secondhand teaching, "
            "a young woman's eyes bright with something "
            "unnamed — while at the slope's foot Jesus "
            "stands perfectly plain in the deep gold, a "
            "carpenter on a hillside, owning every word he "
            "spent the afternoon giving away. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b30", "out": "s30-it-is-one-of-the.jpeg", "seg": "n1",
        "window": "6.65-9.61", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "It is one of the most searching things he ever said.",
        "must_show": "the searchingness — close on Jesus's face as the story begins: gentle, and aimed; a plumb-line dropped kindly.",
        "must_not_show": "no halo, glare or rim-light on Jesus; kindness and precision together — the story that measures its hearers.",
        "scene": (
            "Close on Jesus in the late gold: his face as "
            "the last story begins — warm, unhurried, and "
            "precisely aimed, the eyes moving slowly across "
            "the crowd like a builder's level across a "
            "course of stone — gentleness holding a "
            "plumb-line, about to let it down through "
            "every life on the hillside. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b31", "out": "s31-they-had-never-heard-anyone.jpeg", "seg": "n11a",
        "window": "169.64-174.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNT"],
        "narration": (
            "They had never heard anyone teach like that. Their own scholars "
            "quoted other men."
        ),
        "must_show": "the contrast remembered — two grey elders in the crowd exchanging a long look, lifetimes of secondhand teaching recalibrating between them.",
        "must_not_show": "no halo, glare or rim-light; the look between the elders carries the verse — expertise astonished.",
        "scene": (
            "Close in the crowd: two grey-bearded elders "
            "turn to each other in a long wordless look — "
            "men who have sat under every visiting teacher "
            "for forty years, who know exactly what "
            "quotation sounds like — each finding in the "
            "other's face the same unprecedented "
            "arithmetic: no citations all afternoon, and "
            "more authority than all of them together. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r047-b32", "out": "s32-this-one-spoke-as-though.jpeg", "seg": "n11a + n11",
        "window": "174.20-179.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": (
            "This one spoke as though the words belonged to him. Do not miss "
            "what he is actually saying."
        ),
        "must_show": "ownership of the words — Jesus close, hand resting flat on his own chest at 'these sayings of MINE'; the claim inside the sermon.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand on the chest quiet — the largest claim on the mount, made smallest.",
        "scene": (
            "Close in the last light: Jesus with one hand "
            "resting flat against his own chest — the "
            "gesture that went with 'these sayings of "
            "mine' — his face calm around a claim bigger "
            "than the hill he stands on, made without "
            "raising his voice: a teacher identifying the "
            "rock in the story by touching where it "
            "stands. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r047-b33", "out": "s33-both-men-heard-him-hearing.jpeg", "seg": "n11",
        "window": "179.83-183.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "SAND-B", "MOUNT"],
        "narration": (
            "Both men heard him. Hearing was never the thing that made the "
            "difference."
        ),
        "must_show": "the equal hearing reprised — the two builders side by side in the crowd once more, identical in attention; the row's key fact restated in faces.",
        "must_not_show": "no halo, glare or rim-light; visually the SAME beat as their introduction — the sameness is the argument.",
        "scene": (
            "The two builders again, side by side in their "
            "crowd row exactly as before — the terracotta "
            "and the teal, the same lifted faces, the same "
            "complete attention, the same afternoon light "
            "on both — nothing between them different yet, "
            "and everything between them already decided "
            "somewhere the hillside cannot see. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b34", "out": "s34-the-wise-man-is-simply.jpeg", "seg": "n11 + n12",
        "window": "183.85-191.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "PLAIN"],
        "narration": (
            "The wise man is simply the one who went home and did something "
            "about what he heard. That is the whole invitation."
        ),
        "must_show": "the doing — the wise builder walking home from the mount at dusk with his pick already over his shoulder, the sermon converting to trench-work before the light fails.",
        "must_not_show": "no halo, glare or rim-light; the sermon-to-spade pipeline — obedience with no ceremony between hearing and digging.",
        "scene": (
            "Down the track from the teaching hill in the "
            "dusk the terracotta-clad builder walks home "
            "with his pick already over his shoulder — "
            "collected from his gate in the same motion "
            "as his greeting to his wife — heading past "
            "the house lamp toward the rock shelf while "
            "the sermon is still warm, a man whose notes "
            "from the afternoon are about to be taken in "
            "trench-form. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r047-b35", "out": "s35-every-word.jpeg", "seg": "n2",
        "window": "13.50-14.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE-B", "SAND-B"],
        "narration": "Every word.",
        "must_show": "total reception — extreme close: the two builders' four eyes in one tight frame, all four fixed the same way; nothing missed by either.",
        "must_not_show": "no halo, glare or rim-light; one continuous close scene of two adjacent faces — never a split panel.",
        "scene": (
            "An extreme close frame across the two adjacent "
            "faces in the crowd: four eyes in the golden "
            "light, all fixed on the same distant speaker "
            "with the same unbroken attention, two brows "
            "carrying the same lines of concentration — "
            "every word of the afternoon entering both men "
            "through identical doors, on its way to two "
            "different fates. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r047-b36", "out": "s36-not-to-admire-what-he.jpeg", "seg": "n12",
        "window": "191.55-203.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": (
            "Not to admire what he said, and not to be afraid of the storm, but "
            "to build your actual life on his words, one of them at a time, "
            "starting now."
        ),
        "must_show": "the invitation practical — a NEW trench begun at fresh morning: first spade in the ground above the rock shelf, string lines pegged, a life's foundation starting one cut at a time.",
        "must_not_show": "no halo, glare or rim-light; beginning-sized — one spade-cut, one morning, the whole future implied and unbuilt.",
        "scene": (
            "Fresh morning on the high bank: a new "
            "foundation is one spade-cut old — the first "
            "dark bite of turned earth above the rock "
            "shelf, string lines pegged taut in their "
            "small square, a water skin and bread bundle "
            "set by a stone for the long day ahead — the "
            "least dramatic and most decisive picture a "
            "life can take: begun, correctly, this "
            "morning. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r047-b37", "out": "s37-the-door-is-open-and.jpeg", "seg": "n12",
        "window": "203.25-207.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": "The door is open, and the light is already on inside.",
        "must_show": "the closing image — the rock house at warm dusk: door standing open, lamplight inside, the path up the bank lit by it; the built life, offering itself.",
        "must_not_show": "no halo, glare or rim-light; lamplight through a doorway only — the invitation's last, warmest architecture.",
        "scene": (
            "Warm dusk on the high bank: the plain stone "
            "house stands with its door open and its "
            "lamp lit inside, the warm light falling out "
            "across the threshold and a little way down "
            "the path toward the riverbed — a house that "
            "has already kept its family through one storm, "
            "holding its door open onto the darkening "
            "plain for whoever is still down on the sand "
            "deciding. Every figure has two arms, two "
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
    "PLAIN": "PLACE-REF/plain.jpeg",  # build-38-persistent-widow v2-r038-b46
}
# === end PLACE-PLATES ===
