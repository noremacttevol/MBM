#!/usr/bin/env python3
"""V2 beat map — row 154, build-154-everlasting-gospel (Revelation 14:6-7).

COVERAGE: 23 pictures over 128.6 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Revelation 14 KJV):
  14:6  "I saw ANOTHER ANGEL FLY IN THE MIDST OF HEAVEN, having the
        EVERLASTING GOSPEL to preach unto them that dwell on the
        earth, and to EVERY NATION, AND KINDRED, AND TONGUE, AND
        PEOPLE."
  14:7  "Saying with a loud voice, FEAR GOD, and GIVE GLORY to him;
        for the hour of his judgment is come: and WORSHIP HIM THAT
        MADE heaven, and earth, and the sea, and the fountains of
        waters."
  Seen by JOHN, exiled on PATMOS.

ROW INTENT: the restored-good-news row (BRIDGE tone) — the gospel
misplaced through long dark stretches, then sent out AGAIN from
heaven for everyone. Everything stays inside Revelation's own frame.

RENDERING LAWS:
  - THE ANGEL FOLLOWS THE ROW-85 CANON adapted to Rev 14's flight:
    a REAL robed figure, WINGLESS, silver-grey, dignified — aloft
    in the midst of heaven (mantle streaming, held high by no
    visible means), holding the OPEN BOOK out; never cherubic,
    never winged, never a light-being. Glory is light from above
    him, physical. Automatic reject on wings.
  - It is JOHN'S VISION: the aged exile sees it from the Patmos
    shore; frame the angel high and far in most beats.
  - THE DARK-AGE FRAMES (b01/b02) are dignified longing — few
    guttering lamps, hands lifted under starless overcast; never
    mocking any people; the loss is tender.
  - The book's script is INDISTINCT everywhere (no-readable-text).
  - Every-nation frames (b12/b13) show varied distinct peoples and
    lands under ONE sky — no clone crowds, no favoured group.
  - The relighting arc (b21/b22) is lamp-to-lamp PHYSICAL flame —
    the good news re-sent as spreading light down a dark lane.

TIME OF DAY ARC (intentional): the dark-age frames under starless
overcast night (deliberate); Patmos at sea-dawn as heaven opens;
the angel frames in high clean daylight of the opened heaven; the
creation panorama at star-set through sunrise; the relighting at
deep evening turning warm; the close at lamplit night, one flame
offered.

CHANGING CONDITIONS (kept OUT of the locks): the world's lamps —
guttering and few, then relit lane by lane; the sky — sealed
overcast, then opened height.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "JOHN": (
        "JOHN LOCK: John of Patmos is the same man in every shot — "
        "aged and lean, about ninety, long white hair and beard, "
        "deep undimmed eyes, in a worn DARK SEA-GREY mantle (never "
        "cream, never white); exile's weathering, apostle's fire."
    ),
    "ANGEL": (
        "ANGEL LOCK: the angel is the same figure in every shot — "
        "a REAL dignified messenger, WINGLESS always, in layered "
        "SILVER-GREY robes with a dark sash, strong calm face, "
        "holding one OPEN BOOK; aloft in the midst of heaven with "
        "mantle streaming, held high by no visible means; glory is "
        "physical light from above him, never from him. NEVER "
        "winged, never glowing, never a light-being."
    ),
    "PATMOS": (
        "PATMOS LOCK: the Patmos shore — a rocky exile island "
        "shore, grey sea, wind-bent scrub, a cave-mouth above the "
        "tideline. The same shore throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r154-b01", "out": "s01-for-long-stretches-of-history.jpeg", "seg": "n1",
        "window": "0.28-8.05", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "For long stretches of history, whole peoples lived without it — "
            "the good news about God, misplaced, buried, or never yet heard."
        ),
        "must_show": "the long dark — a wide timeless night landscape of scattered settlements under starless overcast, only a FEW small guttering lamps burning far apart; the loss tender, never mocking.",
        "must_not_show": "no halo; the dark DIGNIFIED — longing, not ignorance-mockery; the few lamps guttering low.",
        "scene": (
            "For centuries the map of the good news looked "
            "like this at night: a wide dark country under "
            "starless overcast, settlements scattered sparse "
            "across the black — and burning in all that "
            "distance only a few small lamps, far apart and "
            "guttering, each one tended by somebody who kept "
            "what little had been handed down — whole peoples "
            "living whole lifetimes between the lights, the "
            "news about God misplaced somewhere behind them "
            "on the road of years. No people are "
            "distinguishable in this frame."
        ),
    },
    {
        "id": "v2-r154-b02", "out": "s02-men-reached-for-heaven-in.jpeg", "seg": "n1",
        "window": "8.05-12.22", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Men reached for heaven in the dark and could not quite find the way.",
        "must_show": "the reaching — on a dim ridge under the sealed overcast, varied figures with hands lifted toward a sky that gives nothing back; longing with dignity.",
        "must_not_show": "no halo; the reachers DIGNIFIED and sincere — real longing, no answer yet; the sky sealed.",
        "scene": (
            "The reaching never stopped even when the finding "
            "did: on the dim ridge a scatter of figures "
            "stands with hands lifted toward the sealed "
            "overcast — an old man's arms spread wide, a "
            "mother holding her child up as if height might "
            "help, a young man's palms open at the empty "
            "grey — sincere as any prayer ever prayed, aimed "
            "with everything they had at a heaven whose door "
            "they could feel but not find — the ache of the "
            "long dark, worn with dignity. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b03", "out": "s03-and-then-in-a-vision.jpeg", "seg": "n2",
        "window": "12.77-17.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOHN", "PATMOS"],
        "narration": "And then, in a vision, John of Patmos saw heaven open, and something come.",
        "must_show": "the opening — aged John on the Patmos shore at sea-dawn, face lifted as the overcast PARTS along a great seam of light; the vision beginning.",
        "must_not_show": "no halo on John; the parting PHYSICAL — cloud opening on height; nothing arrived yet.",
        "scene": (
            "The sealed sky finally gets a seam: on the rocky "
            "Patmos shore at sea-dawn the old exile's face "
            "comes up — white hair whipping in the salt "
            "wind — as the grey overcast PARTS along a long "
            "bright line, cloud rolling back from cloud, "
            "height opening above height where no height "
            "was — John of Patmos, ninety years old and "
            "banished to a rock, watching heaven open for "
            "the man least able and most worthy to tell "
            "anyone — and something, far up, beginning to "
            "come. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r154-b04", "out": "s04-not-an-army-not-a.jpeg", "seg": "n2",
        "window": "17.59-24.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANGEL"],
        "narration": (
            "Not an army, not a storm, but an angel, sent on an errand of "
            "mercy, carrying a message meant for the whole earth."
        ),
        "must_show": "the messenger — the WINGLESS silver-grey angel first seen: high and far in the opened height, real and dignified, the open book in his hands; mercy's errand-runner, per canon.",
        "must_not_show": "ABSOLUTE: no wings, no light-being — a real robed figure aloft; the book open; glory as light from ABOVE him.",
        "scene": (
            "What comes through the opened height is one "
            "messenger with a book: high in the parted "
            "heavens the angel hangs small and real — a "
            "dignified robed figure in layered silver-grey, "
            "WINGLESS, mantle streaming in the height's "
            "wind, held aloft by nothing the eye can find — "
            "and in his hands, open outward, one book — no "
            "army behind him, no storm around him, the "
            "clean light of the opened sky falling from "
            "above onto an errand-runner of mercy carrying "
            "mail for the entire earth. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b05", "out": "s05-it-is-older-than-the.jpeg", "seg": "n4",
        "window": "53.04-59.97", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "It is older than the nations, the same true message from the "
            "beginning, carried down from heaven and offered fresh again."
        ),
        "must_show": "the old-made-fresh — the open book close: pages ancient and worn soft, yet the light on them clean and new; age and freshness in one object. Script indistinct.",
        "must_not_show": "no halo; NO readable text — the pages' age and the light's freshness carry it.",
        "scene": (
            "The book in the angel's hands is no new "
            "edition: close on the open pages — worn soft "
            "at their edges, creased by ages of carrying, "
            "the indistinct old script deep in the grain of "
            "them — and over all that age the light lies "
            "clean and morning-new, the way dawn lies on an "
            "ancient hill — older than every nation "
            "currently holding borders, unimproved because "
            "it never needed improving, offered again "
            "exactly as first written. No people are needed "
            "in this frame."
        ),
    },
    {
        "id": "v2-r154-b06", "out": "s06-the-angel-flew-across-the.jpeg", "seg": "n3",
        "window": "25.53-34.75", "wide": True, "jesus": False, "ref": False,
        "locks": ["ANGEL"],
        "narration": (
            "The angel flew across the height of heaven for all to see, "
            "holding out an open book: the good news about God, ready to be "
            "given back to a world that had lost hold of it."
        ),
        "must_show": "the crossing — the wide frame: the angel aloft crossing the height, book held OUT, and far below the broad curve of lands and seas where every eye could lift and see.",
        "must_not_show": "ABSOLUTE: no wings; the lands below WIDE and varied; the book outward, offered.",
        "scene": (
            "The delivery route crosses the whole ceiling of "
            "the world, the camera set low on the dark lands "
            "taking the height from the side: the silver-"
            "grey figure moves aloft across the opened "
            "heaven — mantle streaming with the crossing, "
            "the open book held OUT from his hands like a "
            "lamp carried through a dark house — and far "
            "beneath his route the lands spread wide: "
            "coasts, valleys, sleeping towns, every one of "
            "them under the flight path on purpose — the "
            "good news, airborne again, being carried back "
            "to a world that lost it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b07", "out": "s07-so-here-is-the-quiet.jpeg", "seg": "n8",
        "window": "112.74-115.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOHN", "PATMOS"],
        "narration": "So here is the quiet wonder of this verse.",
        "must_show": "the wonder — close on old John's face, tears bright in the sea-wind, the vision's meaning settling on the exile; quiet awe.",
        "must_not_show": "no halo; the awe QUIET — an old man moved, not overwhelmed.",
        "scene": (
            "The oldest living apostle takes the vision "
            "personally: close on John's weathered face in "
            "the sea-wind — the deep undimmed eyes bright "
            "with tears that the gusts keep taking, the "
            "white beard whipped sideways, and underneath "
            "the weather of it all a quiet enormous "
            "wonder settling in — the man who watched the "
            "gospel's first morning from a fishing boat, "
            "now shown from a prison island that it will "
            "be sent out AGAIN — and finding the mercy of "
            "that almost too kind to hold. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b08", "out": "s08-and-i-saw-another-angel.jpeg", "seg": "kv6",
        "window": "35.30-46.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANGEL", "JOHN", "PATMOS"],
        "narration": (
            "And I saw another angel fly in the midst of heaven, having the "
            "everlasting gospel to preach unto them that dwell on the earth, "
            "and to every nation, and kindred, and tongue, and people,"
        ),
        "must_show": "SCRIPTURE-EXACT: the full verse — John small on the shore below, the angel high in the midst of heaven with the open book; seer and seen in one frame.",
        "must_not_show": "ABSOLUTE: no wings; the composition VERTICAL — old man on rock, messenger in height, the book between them and the world.",
        "scene": (
            "The verse happens in one vertical frame: at its "
            "foot the old exile stands small on the wet "
            "Patmos rock, face craned upward — and high "
            "above him, in the exact midst of the opened "
            "heaven, the silver-grey messenger holds his "
            "station with the everlasting gospel open in "
            "his hands — I SAW, John will write, ANOTHER "
            "ANGEL — to every nation, kindred, tongue and "
            "people — the whole address-list of mankind "
            "hanging between a prisoner's eyes and a "
            "courier's book. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b09", "out": "s09-notice-the-word-everlasting.jpeg", "seg": "n4",
        "window": "47.66-49.32", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Notice the word: everlasting.",
        "must_show": "the word's weight — the open book alone in clean height-light, its worn pages steady in the wind; permanence as an object.",
        "must_not_show": "no halo; script indistinct; the book STEADY while everything streams.",
        "scene": (
            "One word in the verse out-ages everything "
            "around it: the open book rides steady in the "
            "height's streaming wind — pages that should "
            "flutter lying calm, the worn old leaves "
            "holding their place while mantle and cloud "
            "and light all stream past — EVERLASTING: not "
            "the newest message on earth but the oldest, "
            "the one that predates every kingdom that "
            "ever lost it and will outwait every kingdom "
            "that ignores it. No people are needed in "
            "this frame."
        ),
    },
    {
        "id": "v2-r154-b10", "out": "s10-this-good-news-was-never.jpeg", "seg": "n4",
        "window": "49.32-53.04", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "This good news was never really invented, or improved, by anyone.",
        "must_show": "the unchanged line — two page-fragments side by side, one ancient and one older still, the SAME indistinct line traced identical on both; sameness across ages.",
        "must_not_show": "no halo; NO readable text — the identical line-shapes carry the sameness.",
        "scene": (
            "Compare the editions and find no edits: two "
            "page-fragments lie side by side in the clean "
            "light — one ancient, one older still, "
            "different hands and different centuries — and "
            "across both, traced identical, the SAME line "
            "of indistinct script: same shape, same sweep, "
            "same ending — copied faithfully down the ages "
            "by scribes who understood their one job was "
            "not to improve it — good news with no "
            "revision history, because it arrived finished. "
            "No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r154-b11", "out": "s11-and-notice-who-it-is.jpeg", "seg": "n5",
        "window": "60.57-62.15", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And notice who it is for.",
        "must_show": "the address-list — from the height looking DOWN: the wide world's lands below, faces beginning to lift from fields and shores and towns.",
        "must_not_show": "no halo; the lifting faces VARIED and far; the vantage high.",
        "scene": (
            "Read the delivery addresses from the courier's "
            "height: below the opened heaven the world lies "
            "wide — terraced valleys, fishing coasts, "
            "walled towns, tent camps at the desert's edge — "
            "and across all of it, small and scattered and "
            "beginning, faces are lifting: a farmer "
            "straightening from his rows, a sailor's chin "
            "coming up off his mending, a child pointing "
            "first — the address-list of the everlasting "
            "gospel, which reads, in full: everyone. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b12", "out": "s12-not-one-favoured-people-not.jpeg", "seg": "n5",
        "window": "62.15-68.25", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Not one favoured people, not one language or land, but every "
            "nation, every family, every tongue."
        ),
        "must_show": "the every-nation tapestry — varied distinct peoples in varied dress across varied lands, all under ONE opened sky; no group favoured, no clone faces.",
        "must_not_show": "no halo; the variety REAL (dress, land, feature) — rows 90/107 clone law; one sky over all.",
        "scene": (
            "The list has no asterisks anywhere on it: "
            "across the frame the lands and their peoples "
            "stand varied and distinct — mountain herders "
            "in felted wool, river farmers in wrapped "
            "cotton, coast folk with nets, desert families "
            "at their tents — faces of every cast and age, "
            "no two alike and no group nearer the light "
            "than any other — and over every last one of "
            "them the SAME opened sky, holding the same "
            "book, on the same errand. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b13", "out": "s13-no-one-is-too-far.jpeg", "seg": "n5",
        "window": "68.25-72.50", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "No one is too far away, too foreign, or too late to be handed this.",
        "must_show": "the farthest address — one small solitary hut at the very edge of a vast empty land, and the opened sky's light reaching IT too; the reach total.",
        "must_not_show": "no halo; the hut's remoteness EXTREME and the light's arrival unmistakable.",
        "scene": (
            "Check the farthest address on the map and find "
            "it served: at the very edge of a vast empty "
            "land — past the last road, past the last "
            "neighbour, where the maps go quiet — one small "
            "hut stands alone with its thread of smoke — "
            "and the opened sky's clean light lies across "
            "its roof exactly as it lies on the great "
            "cities — too far, too foreign, too late: "
            "three categories the everlasting gospel has "
            "never once recognized. No people are "
            "distinguishable in this frame."
        ),
    },
    {
        "id": "v2-r154-b14", "out": "s14-the-call-is-simple-and.jpeg", "seg": "n6",
        "window": "73.04-75.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANGEL"],
        "narration": "The angel's call is simple and clean.",
        "must_show": "the clean call — the angel closer now: the calm strong face, one open hand extended in the simplest summoning gesture; nothing ornate.",
        "must_not_show": "ABSOLUTE: no wings; the gesture SIMPLE — one open hand; the face calm and real.",
        "scene": (
            "The summons has no fine print: the messenger "
            "nearer now in the clean height-light — the "
            "calm strong face of a courier who believes "
            "his letter, the silver-grey layers stilled — "
            "and one hand extended open in the simplest "
            "gesture a call can wear: come — no terms "
            "unrolled, no seals to break, no ceremony "
            "attached — an invitation whose entire "
            "apparatus is a book, a hand, and the truth. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r154-b15", "out": "s15-honour-god-give-him-the.jpeg", "seg": "n6",
        "window": "75.40-83.64", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Honour God, give him the glory, and worship the One who made "
            "it all — the heavens, the earth, the sea, and every spring of "
            "water."
        ),
        "must_show": "the Maker's résumé — one creation panorama: star-strewn heavens above, green earth and bright sea below, and near ground a clear SPRING rising among stones; all four named things.",
        "must_not_show": "no halo, no figure — the four creations themselves; the spring's water clear and alive.",
        "scene": (
            "The worship-summons attaches its evidence in "
            "one panorama: the last stars still strewn "
            "high in the paling heavens, the green earth "
            "rolling down to a sea going bright at the "
            "horizon — and in the near ground, rising "
            "quiet among mossed stones, a clear spring "
            "braiding its cold new water into the light — "
            "heavens, earth, sea, and the fountains of "
            "waters: the Maker's four-line résumé, "
            "submitted in evidence at dawn. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r154-b16", "out": "s16-turn-your-face-back-toward.jpeg", "seg": "n6",
        "window": "83.64-86.07", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Turn your face back toward your Maker.",
        "must_show": "the turn — a single figure's face turning UP from the ground into the opened light; the smallest full repentance: a lifted face.",
        "must_not_show": "no halo; the turn READABLE — from down-turned to lifted; the light physical.",
        "scene": (
            "The whole summons can be obeyed with the neck: "
            "a single figure who has walked eyes-down "
            "through the frame's bottom edge stops — and "
            "the face comes UP: off the ground, past the "
            "horizon, into the opened light falling from "
            "the parted height — nothing else moved yet, "
            "no vows, no journey, just the oldest turn "
            "there is performed at its smallest scale — a "
            "face, returned to facing its Maker, which is "
            "where every longer turning starts. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b17", "out": "s17-saying-with-a-loud-voice.jpeg", "seg": "kv7",
        "window": "86.64-97.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANGEL"],
        "narration": (
            "Saying with a loud voice, Fear God, and give glory to him; for "
            "the hour of his judgment is come: worship him that made heaven "
            "and earth, and the sea, and the fountains of waters."
        ),
        "must_show": "SCRIPTURE-EXACT: the loud voice — the angel arms-wide in the height, the call going OUT over the lands below; proclamation at full reach.",
        "must_not_show": "ABSOLUTE: no wings, no fear-imagery below — the call summons, the lands listen; judgment named, never depicted.",
        "scene": (
            "The proclamation goes out at the volume of "
            "heaven: the angel's arms spread wide in the "
            "midst of the height, the open book braced "
            "against one forearm, and the call rolls DOWN "
            "over the listening lands — FEAR GOD, give "
            "GLORY, the hour is COME: WORSHIP HIM that "
            "MADE — heaven and earth and sea and every "
            "fountain of waters — the summons breaking "
            "over coasts and valleys like weather made of "
            "words, loud enough for every nation and "
            "gentle enough to be good news. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b18", "out": "s18-so-the-only-question-is.jpeg", "seg": "n8",
        "window": "124.54-127.04", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "So the only question is a gentle one.",
        "must_show": "the gentle question — a listening face at lamplit evening, quiet, open, considering; the summons arrived at one person's scale.",
        "must_not_show": "no halo; the considering HONEST — openness, not pressure.",
        "scene": (
            "After the height and the nations, the row "
            "comes down to one lamplit face: a listener at "
            "evening with the small flame warm on their "
            "features — quiet, open, genuinely "
            "considering — the everlasting gospel's whole "
            "planetary delivery route ending, as it always "
            "ends, at the scale of one person and one "
            "question, asked gently, with all the time in "
            "the world behind it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b19", "out": "s19-it-is-a-call-to.jpeg", "seg": "n7",
        "window": "98.79-105.86", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "It is a call to come home to the God of creation — the same "
            "God who set the stars in place and filled the seas."
        ),
        "must_show": "the homecoming — a figure walking a night road TOWARD a warm-lit home under a sky rich with set stars, the sea silvered beyond; creation as the road home's country.",
        "must_not_show": "no halo; DIRECTION — toward the lit home; the stars and sea real and grand.",
        "scene": (
            "The call's destination is a lit doorway inside "
            "creation: down the night road a figure walks "
            "steadily HOME — toward the one warm window "
            "burning at the land's fold — while overhead "
            "the stars stand set in their deep places and "
            "beyond the fields the filled sea runs "
            "silvered to the world's edge — the whole "
            "handiwork arranged around one small walking "
            "return, because coming home to the God of "
            "creation means every step of the road is "
            "already his. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r154-b20", "out": "s20-not-a-distant-idea-but.jpeg", "seg": "n7",
        "window": "105.86-112.24", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Not a distant idea, but the Maker of the very ground under "
            "your feet, quietly asking for your heart."
        ),
        "must_show": "the near Maker — close: bare feet on real earth, and a kneeling hand pressed flat to the warm soil; the ground itself the argument for nearness.",
        "must_not_show": "no halo; the TOUCH the frame — skin on soil; nothing abstract.",
        "scene": (
            "The theology gets as near as the ground: close "
            "on bare feet planted in the warm real earth — "
            "dust in the toe-creases, grass at the ankles — "
            "and a hand coming down to press flat against "
            "the soil, palm to the planet — the Maker of "
            "exactly THIS, the touch says: this ground, "
            "this warmth, this holding-up that has never "
            "once failed under you — not a distant idea "
            "anywhere in reach, and quietly asking, "
            "through all of it, for the heart. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b21", "out": "s21-the-good-news-was-never.jpeg", "seg": "n8",
        "window": "115.57-118.47", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "The good news was never abandoned for good.",
        "must_show": "the relighting — a carried flame touching a cold dark lamp's wick, the lamp CATCHING; the never-abandoned made physical.",
        "must_not_show": "no halo; the catch EXACT — flame passing to wick, light returning.",
        "scene": (
            "The proof is one wick catching: in the deep "
            "evening a carried flame tips against the cold "
            "lamp that guttered out an age ago — and the "
            "wick CATCHES, light climbing back into the "
            "old clay cup, the corner it once served "
            "warming back out of the dark — never "
            "abandoned, the catching says: banked, "
            "carried, kept somewhere burning, and brought "
            "back on purpose to every lamp that lost it. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r154-b22", "out": "s22-heaven-sent-it-out-again.jpeg", "seg": "n8",
        "window": "118.47-124.54", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Heaven sent it out again, on purpose, for everyone — which "
            "means it was sent for you, too."
        ),
        "must_show": "the spreading — down a dark lane, lamp lighting lamp lighting lamp, windows warming one by one into the distance; the re-sending in motion.",
        "must_not_show": "no halo; the spread PHYSICAL — flame to wick down the lane; each window individual.",
        "scene": (
            "Watch the re-sending travel a single street: "
            "down the dark lane the light goes lamp to "
            "lamp — a hand carrying flame to a neighbour's "
            "wick, that lamp lighting the next doorway's, "
            "windows warming one by one into the "
            "distance until the far end of the lane "
            "glimmers like a constellation being strung — "
            "sent out AGAIN, on purpose, address by "
            "address — and somewhere down the list, "
            "spelled correctly, yours. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r154-b23", "out": "s23-will-you-receive-it.jpeg", "seg": "n8",
        "window": "127.04-128.39", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Will you receive it?",
        "must_show": "the closing offer — a small lit lamp held OUT toward the viewer's side of the frame by one steady hand; the receiving left open; invitation exact.",
        "must_not_show": "no halo; the lamp offered TOWARD the frame's edge — no receiving hand yet; the question is the space.",
        "scene": (
            "The last frame holds the lamp out and waits: "
            "one steady hand extends the small lit lamp "
            "toward the frame's near edge — the flame "
            "calm, the clay warm, the offer complete — and "
            "the space where a receiving hand would close "
            "around it stands open, unfilled, exactly the "
            "size of the question: will you receive it? — "
            "the everlasting gospel's whole errand ending "
            "where it always ends, an inch from somebody's "
            "reach, held out. Every figure has two arms, "
            "two hands and one head."
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
