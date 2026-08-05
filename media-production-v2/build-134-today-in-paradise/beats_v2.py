#!/usr/bin/env python3
"""V2 beat map — row 134, build-134-today-in-paradise (Luke 23:39-43; John 20:17).

COVERAGE: 18 pictures over 103.4 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  Luke 23:42 the penitent thief: "LORD, REMEMBER ME when thou comest
        into thy kingdom."
  Luke 23:43 "Verily I say unto thee, TODAY shalt thou be with me IN
        PARADISE."
  John 20:17 (three days later, to Mary): "TOUCH ME NOT; for I AM
        NOT YET ASCENDED to my Father."
  Cameron's brief (QUEUE row 134, asked for by name): "where did the
        thief go that day? Not final heaven — three days later Jesus
        tells Mary he has not yet ascended. The Bible itself shows
        more geography to mercy than one-heaven-one-chance allows.
        Asks the better question, names nothing."

RENDERING LAWS:
  - CRUCIFIXION FRAMES (b03-b08) follow the rows-94/95/96 canon
    exactly: chest-up framing, NO wounds shown ever, no nails
    detailed, no blood; the cold grey-overcast HILL lock and the
    THIEF lock are BYTE-IDENTICAL to build-95 (same man, same
    Calvary). The mercy is carried by FACES turned toward each
    other.
  - MARY and TOMB locks are BYTE-IDENTICAL to build-98 (same woman,
    same garden tomb, rows 71/96/97 family). The risen Jesus is
    natural — cream robe, warm, real, NO wounds shown, no shining.
  - PARADISE (b14/b15/b17/b18) is a WAITING place, deliberately
    modest: a warm resting garden-country at morning — real, good,
    and not the end of the road. NEVER rendered as final-heaven
    spectacle (no gates, no thrones, no clouds of glory) — "names
    nothing."
  - The two-doors picture (b01/b02) is the FALSE binary being
    described: two stark doors in a dark wall, then the same wall
    opened wide onto broader country. Symbolic, clean, no fear
    imagery.
  - b16's grief is comforted grief — a mourner at a simple grave,
    dignity total (rows 44/74 class); the trapdoor is only ever
    spoken, never pictured.

TIME OF DAY ARC (intentional): the doors frames in neutral dim
BY DESIGN; Calvary under build-95's cold grey overcast; the tomb
frames in build-98's first-gold Easter morning; paradise and the
close in soft warm morning light.

CHANGING CONDITION (kept OUT of the locks): the wall of doors —
shut, then opened wide; Friday's grey, then Sunday's gold.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags. HILL and THIEF are
# byte-identical to build-95; TOMB and MARY to build-98.
LOCKS = {
    "HILL": (
        "HILL LOCK: Calvary — a bare rounded rock rise outside the "
        "city wall: grey stone and thin scrub, THREE raised wooden "
        "crosses against a cold grey-overcast sky, the city wall low "
        "in the distance, small knots of watchers held back on the "
        "slope. The same rise, crosses and sky throughout."
    ),
    "THIEF": (
        "THIEF LOCK: the penitent thief is the same man in every "
        "shot — on the cross to the RIGHT of centre: about forty, a "
        "broad worn face, grey-shot dark beard, deep tired eyes; "
        "shown chest-up, no wounds, honesty arriving at his last "
        "hour."
    ),
    "TOMB": (
        "TOMB LOCK: a rock-cut garden tomb — a low doorway cut into "
        "a limestone face, a GREAT DISC STONE rolled aside from the "
        "opening, a hewn stone bench within, olive trees and spring "
        "flowers in the garden around. The same face, stone and "
        "garden throughout."
    ),
    "MARY": (
        "MARY LOCK: Mary Magdalene is the same woman in every shot — "
        "about thirty, long dark hair under a slipped DEEP "
        "MADDER-RED shawl, a plain DEEP MADDER-RED dress (never "
        "cream, never white), her face tear-streaked and utterly "
        "dignified; devotion its strongest feature."
    ),
    "REST": (
        "REST LOCK: the waiting country — a quiet garden-country at "
        "soft morning: green meadows with an unhurried stream, "
        "olive and cypress standing calm, gentle mist lifting off "
        "the grass; real, modest and good — NEVER gates, thrones, "
        "or clouds of glory. The same country throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r134-b01", "out": "s01-you-may-have-been-told.jpeg", "seg": "n0",
        "window": "0.28-9.97", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "You may have been told there are only two doors when you die — "
            "one heaven, one hell — and the moment your heart stops, one of "
            "them slams shut forever."
        ),
        "must_show": "the taught picture — two stark identical doors in a dark stone wall, shut with finality; the two-door theology as bare architecture; clean and symbolic, no fear imagery.",
        "must_not_show": "ABSOLUTE: no flames, no light-vs-dark theatrics behind the doors — two shut doors in a dim wall, nothing more.",
        "scene": (
            "The picture many people were handed has exactly "
            "two pieces: a dark stone wall in dim even light, "
            "and set into it two stark identical doors — heavy, "
            "shut, final — nothing written on either, nothing "
            "visible past their seams, the whole eternal "
            "question reduced to a corridor and a coin-flip — "
            "architecture with no waiting room, no mercy's "
            "antechamber, no third fact of any kind: two "
            "doors, one instant, forever — the inherited "
            "floor plan, drawn as taught. No people are in "
            "this frame."
        ),
    },
    {
        "id": "v2-r134-b02", "out": "s02-two-sentences-from-jesus-quietly.jpeg", "seg": "n0",
        "window": "9.97-14.44", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Two sentences from Jesus quietly open that picture wider.",
        "must_show": "the widening — the same dark wall, but now OPENED: both doors ajar and the wall itself giving onto a broad morning country beyond; the floor plan enlarged by light.",
        "must_not_show": "ABSOLUTE: nothing destroyed — the wall opened, not broken; the country beyond soft and real, not spectacle.",
        "scene": (
            "Two sentences renovate the whole floor plan: the "
            "same dark wall stands in the same dim light — but "
            "opened now, both doors swung ajar and a wide gap "
            "of morning showing where the masonry once "
            "insisted on only two ways — beyond it a broad "
            "soft country of green and early light, larger "
            "than the corridor ever admitted, no slamming "
            "anywhere in the architecture — the picture not "
            "torn down but quietly widened, the way truth "
            "widens things: with more room, not more noise. "
            "No people are in this frame."
        ),
    },
    {
        "id": "v2-r134-b03", "out": "s03-the-first-he-said-while.jpeg", "seg": "n1",
        "window": "15.05-17.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "The first he said while he was dying.",
        "must_show": "SCRIPTURE-EXACT, rows-94/95/96 canon — Calvary at merciful distance: the three crosses against cold grey overcast; the sentence's setting, no wounds anywhere.",
        "must_not_show": "ABSOLUTE: no wounds, no nails detailed, no blood — distant framing; the grey sky the mood.",
        "scene": (
            "The first sentence has the hardest address in "
            "scripture: Calvary's bare rounded rise under its "
            "cold grey ceiling of cloud, the three raised "
            "crosses dark against the overcast, small knots "
            "of watchers held back down the slope, the city "
            "wall low and far — the place where a dying man "
            "will spend one of his last breaths on the "
            "prisoner beside him, framed from the merciful "
            "distance the whole library keeps: near enough "
            "for the words, far enough for the mercy. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r134-b04", "out": "s04-next-to-him-hung-a.jpeg", "seg": "n1",
        "window": "17.04-21.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "THIEF"],
        "narration": (
            "Next to him hung a criminal, a man who had earned his cross and "
            "knew it."
        ),
        "must_show": "the thief — chest-up on the right-of-centre cross: the broad worn face, grey-shot beard, deep tired eyes; honesty about his own guilt visible; NO wounds.",
        "must_not_show": "ABSOLUTE: no wounds, no gore — chest-up framing; his pain carried by the face alone, dignity intact.",
        "scene": (
            "The man beside him has no illusions left: chest-"
            "up on the right-hand cross, the thief's broad "
            "worn face hangs tired against the grey sky — "
            "grey-shot beard, deep-cut lines, the eyes of a "
            "man doing honest arithmetic at the end of a "
            "dishonest life and finding his own column "
            "correct: earned, all of it, and he knows it — "
            "no self-pity anywhere in the ruined face, just "
            "the terrible clean honesty that sometimes "
            "arrives at last hours. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r134-b05", "out": "s05-and-in-his-last-hour.jpeg", "seg": "n1",
        "window": "21.94-27.31", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL", "THIEF"],
        "narration": (
            "And in his last hour, that man turned his head and asked Jesus "
            "to remember him."
        ),
        "must_show": "the turn — the thief's head turned toward Jesus on the centre cross, the ask forming on his face; two faces angled toward each other against the grey; chest-up, no wounds.",
        "must_not_show": "ABSOLUTE: no wounds; the TURN is the picture — his face toward Jesus, hope's last unlikely direction.",
        "scene": (
            "The last thing the thief does with his strength "
            "is turn his head: against the cold grey the worn "
            "face rotates toward the centre cross — toward "
            "the one dying man on this hill who has spent the "
            "morning forgiving people — and the ask gathers "
            "on his features with nothing left to lose: "
            "remember me — a lifetime's first prayer, aimed "
            "sideways between two crosses, at the only "
            "neighbour who ever hung close enough to hear "
            "it. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r134-b06", "out": "s06-lord-remember-me-when-thou.jpeg", "seg": "s1 + j1",
        "window": "27.94-35.81", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL", "THIEF"],
        "narration": (
            "Lord, remember me when thou comest into thy kingdom. Verily I "
            "say unto thee, today shalt thou be with me in paradise."
        ),
        "must_show": "SCRIPTURE-EXACT: the exchange — the two faces toward each other, chest-up, the promise passing between the crosses; Jesus's face full of spent tender authority; NO wounds.",
        "must_not_show": "ABSOLUTE: no wounds, no gore — faces and words only; the tenderness at full cost.",
        "scene": (
            "The shortest gospel service on record is held "
            "between two crosses: the thief's plea still on "
            "his lips, and Jesus's face turned to him through "
            "the pain — spent, grey-lit, and full of an "
            "authority no cross has touched — TODAY, the "
            "promise crosses the gap, with ME, in PARADISE — "
            "salvation transacted in one breath each, no "
            "altar, no ritual, no time left for anything but "
            "the mercy itself, which turns out to be the only "
            "part that was ever required. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r134-b07", "out": "s07-today-not-after-a-lifetime.jpeg", "seg": "n2",
        "window": "36.47-43.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "THIEF"],
        "narration": (
            "Today. Not after a lifetime of good behavior, not after "
            "religion had its say — today."
        ),
        "must_show": "the TODAY landing — close on the thief's face as the word reaches him: disbelief breaking into the first peace his face has ever worn; chest-up, no wounds.",
        "must_not_show": "ABSOLUTE: no wounds; the transformation in the FACE — a lifetime's fear standing down.",
        "scene": (
            "One word does what forty years could not: close "
            "on the thief's ruined face as TODAY arrives in "
            "it — the deep tired eyes widening, the honest "
            "mouth coming open, disbelief breaking up like "
            "grey weather into the first peace the face has "
            "ever worn — no probation in the word, no "
            "waiting period, no religion left to satisfy — "
            "today, said the neighbour, and the dying man "
            "believes him, and the belief looks like rest "
            "arriving early. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r134-b08", "out": "s08-mercy-reached-a-dying-thief.jpeg", "seg": "n2",
        "window": "43.09-46.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL"],
        "narration": "Mercy reached a dying thief at the very last minute.",
        "must_show": "the reach measured — the two crosses side by side against the grey, the small gap of air between them; mercy's shortest recorded distance.",
        "must_not_show": "ABSOLUTE: no wounds — merciful framing; the GAP between the crosses the subject.",
        "scene": (
            "The distance mercy crossed is measurable in "
            "cubits: the two crosses stand side by side "
            "against the cold overcast, and between them "
            "nothing but a few feet of grey afternoon air — "
            "the full extent of the road the thief's "
            "salvation had to travel — no pilgrimage, no "
            "temple, no ladder of years: one turned head, one "
            "sentence's width of sky, at the last minute of "
            "the last hour — the shortest recorded distance "
            "between a ruined life and paradise. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r134-b09", "out": "s09-most-people-know-that-verse.jpeg", "seg": "n2",
        "window": "46.42-51.28", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Most people know that verse. Here is the one almost nobody sets "
            "beside it."
        ),
        "must_show": "the setting-beside — two small scroll fragments laid side by side on a plain table in lamplight, a hand placing the second next to the first; the row's method in one image.",
        "must_not_show": "no halo; script INDISTINCT period writing — no readable text; the juxtaposition the picture.",
        "scene": (
            "The row's whole method fits on one plain table: "
            "in the lamp's quiet ring a hand sets a second "
            "small scroll fragment down beside a first — two "
            "sentences from the same voice, three days apart, "
            "laid edge to edge in the light where they can "
            "finally read each other — the famous one and its "
            "forgotten neighbour, side by side for perhaps "
            "the first time in the reader's life, about to "
            "widen a floor plan between them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r134-b10", "out": "s10-three-days-later-on-easter.jpeg", "seg": "n3",
        "window": "51.92-58.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": (
            "Three days later, on Easter morning, Mary reaches for the risen "
            "Jesus, and he stops her with something strange:"
        ),
        "must_show": "SCRIPTURE-EXACT: the garden meeting — first-gold Easter morning at the tomb; Mary reaching toward the risen Jesus, his hand gently raised in the staying gesture; joy and strangeness together. NO wounds shown.",
        "must_not_show": "no halo, no shining effects on Jesus — natural, warm, real; NO wounds visible; Mary's reach mid-motion.",
        "scene": (
            "Sunday's gold changes everything except her "
            "reflex to reach: in the tomb garden's first "
            "morning light Mary is already moving toward him "
            "— tear-streaked face blazing with recognition, "
            "hands rising toward the Teacher who is somehow, "
            "warmly, impossibly standing among the olive "
            "trees — and his hand comes up gentle in the "
            "staying gesture, halting the embrace mid-reach "
            "with something stranger than either death or "
            "morning: not yet. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r134-b11", "out": "s11-touch-me-not-for-i.jpeg", "seg": "j2",
        "window": "58.99-62.89", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": "Touch me not; for I am not yet ascended to my Father:",
        "must_show": "SCRIPTURE-EXACT: the strange sentence — close on the two: his gentle staying hand, her halted reach, the words' oddness alive on both faces; morning gold around them.",
        "must_not_show": "no halo, no shining; NO wounds; the gesture GENTLE — a pause, not a rejection.",
        "scene": (
            "The sentence is as strange as the morning is "
            "bright: close on the halted reach — Mary's "
            "fingers stopped a hand's-breadth from his "
            "sleeve, his palm turned gentle between them, "
            "nothing of rejection in it and everything of "
            "schedule — NOT YET ascended, the words run, as "
            "if even risen glory keeps appointments — and on "
            "both faces the live strangeness of a fact "
            "nobody's theology had a shelf for: three days "
            "out of the tomb, and still not yet home to the "
            "Father. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r134-b12", "out": "s12-read-those-two-slowly-side.jpeg", "seg": "n4",
        "window": "63.52-71.15", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Read those two slowly, side by side. On Friday he told the "
            "thief they would be together in paradise that same day."
        ),
        "must_show": "the reading — the two scroll fragments side by side in lamplight, a finger resting on the FIRST; Friday's promise under study.",
        "must_not_show": "no halo; script indistinct; the finger on the first fragment — the method continuing.",
        "scene": (
            "The slow reading begins at Friday: the two "
            "fragments lie side by side in the lamp's ring "
            "and a careful finger comes to rest on the first "
            "— today, paradise, with me, spoken from a cross "
            "to a thief with hours to live — the reader's "
            "hand holding the sentence still on the table "
            "the way you hold a coin to check its metal, "
            "because the next fragment over is about to ask "
            "this one a question nobody thought to ask for "
            "centuries. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r134-b13", "out": "s13-on-sunday-he-says-he.jpeg", "seg": "n4",
        "window": "71.15-74.92", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "On Sunday he says he has not yet gone up to his Father.",
        "must_show": "the second reading — the finger moved to the SECOND fragment; Sunday's sentence under the same lamp; the tension between the two now physical on the table.",
        "must_not_show": "no halo; script indistinct; the two fragments clearly SEPARATE and both present.",
        "scene": (
            "Sunday's fragment gets the same slow finger: the "
            "hand moves to the second scroll piece — not yet "
            "ascended, it runs, three days after today-in-"
            "paradise was spoken and kept — and now the two "
            "sentences lie in the lamplight looking at each "
            "other across an inch of table, Friday's promise "
            "and Sunday's schedule, both true, both his, "
            "and between them a doorway of geography quietly "
            "opening in the floor of everything the reader "
            "was taught. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r134-b14", "out": "s14-which-means-the-paradise-he.jpeg", "seg": "n4",
        "window": "74.92-80.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["REST"],
        "narration": (
            "Which means the paradise he promised the thief was not yet the "
            "final home with the Father."
        ),
        "must_show": "the deduction pictured — first sight of the waiting country: the modest good garden-land at soft morning, mist lifting; real and good and visibly NOT a final-glory scene.",
        "must_not_show": "ABSOLUTE: no gates, thrones, clouds of glory, or spectacle — a modest beautiful resting country only.",
        "scene": (
            "What the two sentences make room for looks like "
            "this: a quiet garden-country at soft morning — "
            "green meadows sloping to an unhurried stream, "
            "olive and cypress standing calm in lifting "
            "mist, light lying gentle over everything — good, "
            "real, restful, and unmistakably modest: no "
            "gates, no thrones, no final splendour — a place "
            "a tired thief could arrive at by evening and "
            "recognize at once as mercy, and not yet the end "
            "of anything. No people are in this frame."
        ),
    },
    {
        "id": "v2-r134-b15", "out": "s15-it-was-somewhere-in-between.jpeg", "seg": "n4",
        "window": "80.12-85.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["REST"],
        "narration": (
            "It was somewhere in between — real, and good, and not the end "
            "of the road."
        ),
        "must_show": "the in-between made visible — the waiting country with a path running THROUGH it and onward toward far brighter hills; rest now, road continuing.",
        "must_not_show": "ABSOLUTE: no spectacle at the path's end — the far hills simply brighter, undetailed; the continuing the point.",
        "scene": (
            "The country's best feature is its road: through "
            "the green resting meadows a worn path runs — "
            "past the stream, between the cypresses — and "
            "does not end anywhere in the frame: it climbs "
            "on toward far hills that hold a brighter, "
            "undetailed light at the horizon's edge — a land "
            "built for staying in AND for going on from, "
            "rest with a road through it — somewhere in "
            "between, exactly as deduced, with the end of "
            "the road mercifully out of frame. No people "
            "are in this frame."
        ),
    },
    {
        "id": "v2-r134-b16", "out": "s16-that-should-change-how-you.jpeg", "seg": "n5",
        "window": "85.95-92.86", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That should change how you grieve. The people you love who died "
            "without every box checked did not fall through a trapdoor."
        ),
        "must_show": "the changed grief — a mourner at a simple grave under morning light, grief visibly EASED: shoulders down, face lifted toward the light; comfort, dignity total.",
        "must_not_show": "ABSOLUTE: no trapdoor imagery, nothing dark — the frame is the comfort itself; the mourner dignified.",
        "scene": (
            "The deduction arrives where it matters most — at "
            "a graveside: a mourner stands by the simple "
            "stone in the morning light, flowers laid, and "
            "something in the standing has changed — the "
            "shoulders down from grief's clench, the face "
            "lifted into the warmth instead of pressed "
            "toward the ground — a person doing the new "
            "arithmetic over someone dearly loved and "
            "imperfectly finished: not fallen through any "
            "floor; resting, in a real and kindly place, "
            "with time. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r134-b17", "out": "s17-mercy-has-more-room-than.jpeg", "seg": "n5",
        "window": "92.86-96.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["REST"],
        "narration": "Mercy has more room than you were told, and more time.",
        "must_show": "the room and the time — the waiting country wide under the climbing morning: broad meadows, long unhurried light; spaciousness itself.",
        "must_not_show": "ABSOLUTE: no spectacle — the wideness and the unhurried light carry the sentence.",
        "scene": (
            "The two things mercy has more of are both "
            "visible from one rise: ROOM — the resting "
            "country running wide and green in every "
            "direction, meadow past stream past grove, far "
            "more of it than any two-door corridor ever "
            "allowed — and TIME — the morning climbing slow "
            "and unhurried over all of it, no clock anywhere "
            "in the light, no slamming scheduled — the "
            "geography of grace at its true acreage, more "
            "than you were told on both counts. No people "
            "are in this frame."
        ),
    },
    {
        "id": "v2-r134-b18", "out": "s18-there-is-a-place-still.jpeg", "seg": "n5",
        "window": "96.71-102.99", "wide": True, "jesus": True, "ref": REF,
        "locks": ["REST"],
        "narration": (
            "There is a place still called paradise, a place of waiting, and "
            "the Shepherd is there too."
        ),
        "must_show": "the closing frame — the waiting country at full soft morning, a scatter of resting figures at peace, and the Shepherd himself walking among them: Jesus present in the in-between.",
        "must_not_show": "no halo, no shining on Jesus — natural, warm, cream-robed; the resting figures peaceful; no spectacle.",
        "scene": (
            "The last fact is the best one, the camera looking "
            "across the meadow from the rise, taking the "
            "resting country from the side: through the soft "
            "morning a scatter of figures rests easy in the "
            "green — seated by the stream, walking the path, "
            "unhurried as the light — and moving among them, "
            "cream-robed and warm and unmistakable, the "
            "Shepherd walks his waiting flock the way he "
            "walked Galilee — present, HERE too, in the "
            "in-between — because there was never anywhere "
            "in the whole geography of mercy that he "
            "intended to leave unshepherded. Every figure "
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
    # HILL: build-38 auto-match REJECTED (village doorway frame is not
    # Calvary). Anchor instead on build-95's approved HILL frames.
    # TOMB: build-37 auto-match REJECTED per build-95's authored law —
    # build-37 is the PARABLE tomb (arid, no garden); this is JESUS'S garden
    # tomb (rows 71/96/97/98 family). Take 97/98's approved garden frame.
}
# === end PLACE-PLATES ===
