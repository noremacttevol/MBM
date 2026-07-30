#!/usr/bin/env python3
"""V2 beat map — row 70, build-70-temptations (Matthew 4:1-11).

COVERAGE: 42 pictures over 236.9 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 4:1-11 KJV):
  v1    "Then was Jesus LED UP OF THE SPIRIT into the wilderness TO BE
        TEMPTED of the devil" — straight from the river, on purpose; the
        Judean waste: bare rock, heat, silence.
  v2    "FASTED FORTY DAYS and forty nights ... he was afterward an
        hungred" — the fast painted as real human wasting: hollowing
        cheeks, slowing steps, days marked in shadow and stone.
  ⚑ THE TEMPTER IS NEVER EMBODIED (A-law, CONTENT-CARE): no figure, no
        shadow-being, no serpent, no silhouette — every temptation is
        Jesus ALONE, addressed by a voice the frames refuse to house.
        The three tests are painted as their SETTINGS and OBJECTS: the
        stones, the pinnacle drop, the kingdoms vista — with Jesus's
        answering face the only combatant shown.
  v3-4  stones to bread — the bait's reasonableness: loaf-shaped desert
        stones; "It is written: MAN SHALL NOT LIVE BY BREAD ALONE."
  v5-7  the pinnacle — "IF ... cast thyself down" (scripture quoted by
        the voice); "THOU SHALT NOT TEMPT THE LORD THY GOD." The height
        real, the city far below; no leap, no angels painted mid-air.
  v8-10 the mountain of kingdoms — "ALL THESE THINGS WILL I GIVE THEE" —
        the vista as a feast of distant glories; "GET THEE HENCE, SATAN"
        — Jesus's command aimed at the empty air, final.
  v11   "angels came and MINISTERED unto him" — rendered RESTRAINED as
        two plain-robed ministering figures at dawn with bread and
        water — no wings, no light-effects, real as the row-37 bearers;
        plus the dawn itself, 'the way dawn comes after the longest
        night.'
  Hebrews 4:15 (b38) — "in all points tempted like as we are, yet
        without sin" — the application beats close the row.

TIME OF DAY: the arc runs forty days — hard noon glare for the fast's
depth, the first temptation at blazing midday, the pinnacle in white
morning height-light, the kingdoms at sunset's most gorgeous hour (the
offer's own colouring — deliberate), and the ministering at clean DAWN.
All stated per-beat.

CHANGING CONDITION (kept OUT of the locks): the fast's toll on Jesus —
day-one strength, week-three hollowing, day-forty gauntness — carried
per-beat in face and stride; and restored ease at the dawn ministering.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "DESERT": (
        "WILDERNESS LOCK: the Judean waste — bare broken badlands of "
        "sun-scorched rock and dust, wadis cut deep and dry, no green "
        "thing, heat-shimmer by day and knife-cold starlight by night, "
        "and one low overhung ledge that serves as the fast's shelter. "
        "The same ledge and skyline in the camp beats."
    ),
    "PINNACLE": (
        "PINNACLE LOCK: the temple's highest corner — a narrow stone "
        "parapet at the sanctuary roof's south-east angle, the great "
        "courts and then the whole city falling away small below, the "
        "Kidron valley beyond, wind at this height. The same parapet "
        "and drop in the pinnacle beats."
    ),
    "SUMMIT": (
        "KINGDOMS SUMMIT LOCK: an exceeding high mountain's bare crown "
        "— black rock above the cloud-line, and below and beyond, "
        "spread to every horizon, the lit distances of the world: "
        "cities, rivers, roads and far golden lands under a sunset "
        "sky. The same crown and vista in the summit beats."
    ),
    "MINISTERS": (
        "MINISTERING FIGURES LOCK: the two ministers are plain-robed "
        "figures in DEEP BLUE, calm-faced and real — no wings, no "
        "light-effects, no floating; they kneel and serve like "
        "travellers, carrying bread, water and a folded blanket. "
        "Faces shown clearly, serene."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r070-b01", "out": "s01-straight-from-the-river-still.jpeg", "seg": "n0",
        "window": "0.28-8.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": (
            "Straight from the river, still carrying his Father's words — this "
            "is my beloved Son — Jesus was led by the Spirit up into the "
            "wilderness."
        ),
        "must_show": "SCRIPTURE-EXACT: the leading up — Jesus climbing alone from the green river valley into the bare badlands, the Jordan's thread far behind, the waste opening ahead.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the transition stark — green behind, nothing ahead; his stride still strong, day one.",
        "scene": (
            "Up out of the river valley Jesus climbs "
            "alone into the badlands — behind and below "
            "him the Jordan's green thread and the last "
            "tamarisks, ahead of him nothing but broken "
            "sun-scorched rock rising to a bare skyline "
            "— his stride still river-strong, his wet-"
            "dried robe dusted to the knee, a man "
            "walking out of the best sentence of his "
            "life into the emptiest country it will "
            "ever be tested in. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b02", "out": "s02-not-by-accident.jpeg", "seg": "n0",
        "window": "8.74-10.42", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "Not by accident.",
        "must_show": "the purpose — close on Jesus's face set toward the waste: no wandering in it; a man keeping an appointment.",
        "must_not_show": "no halo, glare or rim-light on Jesus; deliberateness total — the wilderness as destination.",
        "scene": (
            "Close on Jesus's face against the "
            "badlands' shimmer: the warm eyes set "
            "forward with the unmistakable focus of a "
            "kept appointment — no drift in the gaze, "
            "no glance back at the green — a man "
            "walking into forty days the way other men "
            "walk into a scheduled meeting, because "
            "that is exactly what it is. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b03", "out": "s03-notice-what-he-did-not.jpeg", "seg": "n3",
        "window": "73.73-75.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["DESERT"],
        "narration": "Notice what he did NOT do.",
        "must_show": "the unused power — the loaf-shaped stones lying exactly as they were, untouched, unchanged; the miracle that never happened, as still life.",
        "must_not_show": "no halo, glare or rim-light; the stones stubbornly stone — the refusal recorded in their unchanged grain.",
        "scene": (
            "A close still in the hard noon light: the "
            "scatter of loaf-shaped desert stones lying "
            "exactly where the ages left them — "
            "sun-split, dust-filmed, and utterly, "
            "permanently stone — the most famous "
            "un-performed miracle in history recorded "
            "in untouched rock, beside the print of "
            "sandals that walked away. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b04", "out": "s04-before-the-teaching-before-the.jpeg", "seg": "n0",
        "window": "11.87-24.20", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": (
            "Before the teaching, before the miracles, there was going to be a "
            "battle, and it was going to happen in the emptiest place in the "
            "country: bare rock, no shade, no food, no company."
        ),
        "must_show": "the battlefield surveyed — the waste at its emptiest: Jesus a small figure amid a vast broken nothing; the arena's four privations visible as landscape.",
        "must_not_show": "no halo, glare or rim-light; the emptiness the antagonist's home ground — no living thing anywhere in frame but him.",
        "scene": (
            "The waste at full scale: broken badlands "
            "running ridge behind ridge to a bare "
            "horizon, heat-shimmer standing off the "
            "rock, not one green blade or moving "
            "creature anywhere — and small in the "
            "middle distance, the single cream-clad "
            "figure walking deeper in: one man "
            "entering an arena built entirely of "
            "absences — no shade, no food, no water, "
            "no company — where the century's real "
            "first battle is scheduled. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b05", "out": "s05-he-fasted-forty-days-and.jpeg", "seg": "n1",
        "window": "24.80-27.27", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "He fasted forty days and forty nights.",
        "must_show": "the fast's calendar — Jesus at his overhung ledge camp amid tally-like day-shadows: the duration made visible in stone and light.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the forty days as lived time — a camp aged by weeks, a man thinning.",
        "scene": (
            "At the low overhung ledge the fast keeps "
            "its long house: Jesus seated in its thin "
            "shade visibly weeks in — the robe hanging "
            "looser, the cheekbones rising, a line of "
            "small stones set in a row at the ledge's "
            "lip like counted days — while the noon "
            "glare hammers the waste beyond the "
            "shadow's edge, and the silence stands as "
            "deep as the heat. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b06", "out": "s06-mark-that-he-was-not.jpeg", "seg": "n1",
        "window": "27.27-30.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "Mark that: he was not floating above any of it.",
        "must_show": "the humanity insisted — close on the fast's real toll: cracked lips, hollowed cheek, dust in the beard; divinity not exempting flesh.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the suffering dignified and REAL — hunger doing to him what it does to anyone.",
        "scene": (
            "Close on Jesus's face deep in the fast: "
            "lips cracked white at their corners, the "
            "cheeks hollowed under the dust-greyed "
            "beard, the skin drawn over bones the "
            "river never showed — and in the warm "
            "eyes, undimmed, the same steady purpose — "
            "a body paying hunger's full price at "
            "hunger's standard rates, floated above "
            "by absolutely nothing. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b07", "out": "s07-and-when-he-was-at.jpeg", "seg": "n1",
        "window": "33.67-39.29", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": (
            "And when he was at his weakest and emptiest — that is exactly when "
            "the tempter came."
        ),
        "must_show": "⚑ A-law: the arrival WITHOUT an arriver — the waste's light subtly wrong, the silence pressurized, Jesus's gaunt head lifting toward an empty quarter of air; presence rendered as attention.",
        "must_not_show": "NO figure, NO shadow-being, NO shape — the tempter exists only in the direction of Jesus's lifted attention; no halo, glare or rim-light.",
        "scene": (
            "At the ledge on the fortieth noon the "
            "silence changes weight: the heat-shimmer "
            "stills, the waste's light goes subtly "
            "flat — and Jesus's gaunt head lifts, "
            "slowly, toward an empty quarter of air "
            "off the shade's edge, his eyes finding "
            "and holding a point where the frame "
            "shows nothing at all — the oldest "
            "opportunist in creation arriving at the "
            "weakest hour, visible only as the "
            "direction of a starving man's steady "
            "attention. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b08", "out": "s08-if-thou-be-the-son.jpeg", "seg": "s3",
        "window": "39.92-44.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["DESERT"],
        "narration": (
            "If thou be the Son of God, command that these stones be made "
            "bread."
        ),
        "must_show": "SCRIPTURE-EXACT: the first bait — the loaf-shaped stones close: rounded desert rocks uncannily like fresh loaves, arranged by geology into temptation.",
        "must_not_show": "NO tempter shown; the stones' bread-likeness the whole cruelty — form without substance, at a starving man's feet.",
        "scene": (
            "Close at the shade's edge: a scatter of "
            "rounded desert stones lying in the "
            "glare — sun-baked to a crust-brown, "
            "domed and cleft exactly as loaves are "
            "domed and cleft, one even dusted pale "
            "as flour — geology's accidental bakery "
            "arranged at a fasting man's feet, every "
            "shape a promise and every substance a "
            "stone. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b09", "out": "s09-hear-what-that-little-word.jpeg", "seg": "n2",
        "window": "45.39-47.46", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "Hear what that little word IF is doing.",
        "must_show": "the word's target — close on Jesus's gaunt face: the IF aimed at the river's sentence, and the sentence holding; attack met by memory.",
        "must_not_show": "NO tempter; no halo, glare or rim-light — the battle interior, the face its whole theatre.",
        "scene": (
            "Close on the gaunt face in the flat "
            "light: the little word's hook visibly "
            "landing and finding no purchase — the "
            "eyes steady with something held behind "
            "them, a river's sentence standing guard "
            "— a starving man being invited to doubt "
            "the only words he brought to the desert, "
            "and declining, without heat, to hand "
            "them over. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b10", "out": "s10-the-very-first-attack-was.jpeg", "seg": "n2",
        "window": "50.28-55.92", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The very first attack was aimed at that sentence — prove it, earn "
            "it, doubt it."
        ),
        "must_show": "the target named — a remembered flash of the river moment: the dove at the wet shoulder, the opened sky; the sentence under attack, shown at its minting.",
        "must_not_show": "no halo, glare or rim-light; the memory clean — the baptism's fact as the fast's anchor.",
        "scene": (
            "A remembered brightness against the "
            "desert dark: the river moment as it was — "
            "the wet shoulder, the white dove settled "
            "plain upon it, the great rift of clean "
            "sky standing open above the green water — "
            "the exact minting of the sentence now "
            "under siege, held in memory's keeping "
            "forty days into the proving of it. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b11", "out": "s11-and-the-bait-was-reasonable.jpeg", "seg": "n2",
        "window": "55.92-61.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": (
            "And the bait was reasonable: you're starving, you have the power, "
            "feed yourself."
        ),
        "must_show": "the bait's logic — Jesus's gaunt hand hovering above a loaf-shaped stone, near enough to take; reason's whole case in the hand's stillness.",
        "must_not_show": "NO tempter; the hand NEVER touching — hovering the beat; hunger's argument honoured and refused in one held inch.",
        "scene": (
            "In the hard light Jesus's wasted hand "
            "hangs above the most loaf-like of the "
            "stones — near enough that one closing of "
            "the fingers would decide it, the "
            "knuckles sharp under the skin, the arm "
            "trembling faintly with the fast — and "
            "the hand holds, one inch above the "
            "reasonable, neither taking nor "
            "retreating, while the whole argument "
            "runs its course through a starving "
            "body. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b12", "out": "s12-use-what-you-are-for.jpeg", "seg": "n2",
        "window": "61.62-63.83", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Use what you are for you.",
        "must_show": "the principle refused — a close still: a carpenter's strong tools lying unused beside their maker's own unfinished meal-table; power kept off one's own errands.",
        "must_not_show": "no halo, glare or rim-light; the metaphor homely — tools that serve others, resting.",
        "scene": (
            "A close still in workshop light: a "
            "carpenter's well-kept tools — adze, "
            "plane, mallet — lying at rest on a bench "
            "beside a plain unfinished table, and on "
            "the bench's far end the workman's own "
            "meal: bread and water untouched while "
            "the work for others stands first — "
            "power's oldest discipline, resting in "
            "the order of a bench. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b13", "out": "s13-it-is-written-man-shall.jpeg", "seg": "j1",
        "window": "64.45-72.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": (
            "It is written, Man shall not live by bread alone, but by every "
            "word that proceedeth out of the mouth of God."
        ),
        "must_show": "SCRIPTURE-EXACT: the first answer — Jesus's cracked lips delivering the written word into the empty air, the hovering hand withdrawing to rest; scripture as the whole weapon.",
        "must_not_show": "NO tempter; no halo, glare or rim-light — the answer aimed at the same empty quarter; the stone left stone.",
        "scene": (
            "The answer goes out into the empty air: "
            "Jesus's cracked lips shaping the written "
            "sentence with a scholar's precision and "
            "a starving man's breath — his hand "
            "withdrawing from above the loaf-stone to "
            "rest on his own knee — one line of old "
            "scripture, quoted at conversational "
            "volume into a silence that arrived with "
            "opinions, ending the exchange. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b14", "out": "s14-he-did-not-argue.jpeg", "seg": "n3",
        "window": "75.21-76.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "He did not argue.",
        "must_show": "the non-debate — Jesus's face closed to negotiation: no counter-offer forming, no engagement; the argument simply not attended.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the refusal's economy — a door not opened.",
        "scene": (
            "Close on the gaunt face after the "
            "answer: nothing further forming in it — "
            "no rebuttal gathering, no clever second "
            "line, no flicker of a man enjoying an "
            "exchange — the features settled back "
            "into the fast's patience like a door "
            "clicked shut, an argument dying of "
            "non-attendance in the desert air. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b15", "out": "s15-he-answered-with-a-line.jpeg", "seg": "n3",
        "window": "78.85-84.38", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "He answered with a line of scripture — a sentence any of us could "
            "memorize — and stood on it."
        ),
        "must_show": "the weapon's availability — a close still: a worn small scroll open at one line on a plain shelf, thumb-marked; the same armament, on anyone's shelf.",
        "must_not_show": "no halo, glare or rim-light; the ordinariness the point — a memorizable line in reach of any hand.",
        "scene": (
            "A close still in plain lamplight: a "
            "small worn scroll lying open on a "
            "household shelf, one line of its dense "
            "script rubbed faintly shinier than the "
            "rest by a returning thumb — beside it a "
            "child's practice tablet with the same "
            "line copied out twice — the Son of "
            "God's entire desert arsenal, stocked on "
            "an ordinary family's shelf. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b16", "out": "s16-the-son-of-god-fought.jpeg", "seg": "n3",
        "window": "84.38-90.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": (
            "The Son of God fought hungry, as a man, with the same weapon you "
            "have on your shelf."
        ),
        "must_show": "the solidarity of the method — the gaunt Jesus at his ledge, hands empty of everything but memory; deity fighting with a man's equipment.",
        "must_not_show": "no halo, glare or rim-light; the equipment visibly ordinary — empty hands, remembered words, human hunger.",
        "scene": (
            "At the ledge in the hard light Jesus "
            "sits with his empty hands open on his "
            "knees — no staff, no scroll, no bread, "
            "nothing in the whole camp but a row of "
            "counted stones and the words he carries "
            "in memory — the best-armed combatant in "
            "the history of the wilderness, equipped "
            "with exactly what any hungry believer "
            "owns: nothing, and every word of God. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r070-b17", "out": "s17-the-second-try-was-stranger.jpeg", "seg": "n4",
        "window": "90.97-92.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["PINNACLE"],
        "narration": "The second try was stranger.",
        "must_show": "the scene shifted — the pinnacle's parapet introduced: the narrow stone edge, the wind, the drop's first suggestion; strangeness as altitude.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the parapet empty and waiting — vertigo before anyone stands in it.",
        "scene": (
            "The temple's highest corner in white "
            "morning light: the narrow stone parapet "
            "running to its south-east angle, wind "
            "moving dust along the coping, and past "
            "its edge the courts' pale geometry "
            "falling away small below — a ledge "
            "built for no foot traffic at all, "
            "standing empty in the height-light, "
            "waiting for the strangest conversation "
            "of the forty days. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b18", "out": "s18-in-a-flash-he-was.jpeg", "seg": "n4",
        "window": "92.81-101.70", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PINNACLE"],
        "narration": (
            "In a flash he was at the highest corner of the temple, the city "
            "far below — and the voice turned religious. It quoted scripture "
            "back at him."
        ),
        "must_show": "SCRIPTURE-EXACT: the pinnacle — Jesus standing at the parapet's angle, the whole city small beneath, wind in the robe; alone at the height with the unbodied voice.",
        "must_not_show": "NO tempter figure anywhere; no halo, glare or rim-light — the drop and the wind and one man; the voice's presence only in his listening.",
        "scene": (
            "At the parapet's very angle Jesus "
            "stands with the wind pressing his robe — "
            "the great courts and then the whole "
            "city dropping away small below him, the "
            "Kidron a shadow-thread beyond — alone "
            "on masonry no one stands on, his gaunt "
            "face turned slightly as if to a speaker "
            "at his shoulder where the bright empty "
            "height-light holds nothing at all — the "
            "second interview, convened at the top "
            "of the world. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b19", "out": "s19-led-there.jpeg", "seg": "n0",
        "window": "10.42-11.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "Led there.",
        "must_show": "the leading — Jesus mid-stride into the waste with the wind at his back pressing him forward; guidance rendered as weather and willingness.",
        "must_not_show": "no dove repainted here, no light-effects; the Spirit's leading carried by direction and consent alone.",
        "scene": (
            "On the climbing track into the badlands "
            "Jesus walks with the wind full at his "
            "back — the dust streaming past his "
            "ankles ahead of him, the robe pressed "
            "forward against his shoulders like a "
            "hand — a man not wandering but "
            "conducted, his own consenting stride "
            "and the pressing wind agreeing on the "
            "single direction of deeper in. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b20", "out": "s20-if-thou-be-the-son.jpeg", "seg": "s6",
        "window": "102.31-115.22", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PINNACLE"],
        "narration": (
            "If thou be the Son of God, cast thyself down: for it is written, "
            "He shall give his angels charge concerning thee: and in their "
            "hands they shall bear thee up, lest at any time thou dash thy foot "
            "against a stone."
        ),
        "must_show": "SCRIPTURE-EXACT: the misquoted psalm at the drop — Jesus looking down the pinnacle's full fall to the tiny court below: the leap proposed, the promise twisted; the drop painted honest.",
        "must_not_show": "NO angels painted mid-air, NO tempter; no halo, glare or rim-light — the drop and the man's steady regard of it carry the whole verse.",
        "scene": (
            "From behind Jesus's shoulder the "
            "proposal shows its arena: the parapet's "
            "edge and then the fall — course below "
            "course of pale masonry dropping to a "
            "court where worshippers move small as "
            "grain — the leap's whole theatre laid "
            "out with its promised audience, while "
            "the gaunt man at the edge studies the "
            "distance down with the level eyes of "
            "someone reading a contract's twisted "
            "clause. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b21", "out": "s21-he-got-hungrier-every-single.jpeg", "seg": "n1",
        "window": "30.64-33.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "He got hungrier every single day, the way you would.",
        "must_show": "hunger's ordinariness — Jesus at the ledge at dusk pressing a fist against his own middle: the universal gesture; the fast at human scale.",
        "must_not_show": "no halo, glare or rim-light; the gesture anyone's — hunger doing its common work on an uncommon man.",
        "scene": (
            "At the ledge in the dusk's cold Jesus "
            "sits with one fist pressed hard against "
            "his own middle — the oldest, commonest "
            "gesture of an empty stomach — his gaunt "
            "face bearing it the way working men "
            "bear it, jaw set, breath measured — "
            "day upon day of the exact hunger anyone "
            "would feel, being felt exactly. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b22", "out": "s22-throw-yourself-down-it-said.jpeg", "seg": "n4b",
        "window": "116.65-125.79", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PINNACLE"],
        "narration": (
            "Throw yourself down, it said — the angels are promised to catch "
            "you. Force your Father to prove himself, publicly, on demand."
        ),
        "must_show": "the test's mechanism — Jesus's sandalled feet at the parapet's very lip, unmoving; the demanded spectacle declined at the toes.",
        "must_not_show": "NO leap begun, NO angels, NO tempter; the feet planted the whole answer's preview.",
        "scene": (
            "Close at the parapet's lip: Jesus's "
            "worn sandalled feet planted a hand's "
            "width from the edge — the wind snapping "
            "the robe's hem past them, the drop's "
            "pale depth falling away beyond the "
            "toes — and the feet utterly unmoving, "
            "weight settled back through the heels, "
            "the whole proposed spectacle being "
            "declined from the ground up. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b23", "out": "s23-make-god-perform.jpeg", "seg": "n4b",
        "window": "125.79-127.85", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Make God perform.",
        "must_show": "the demand's shape — a close still: a market conjurer's empty little stage-table with its cup and props, tawdry in daylight; what the pinnacle proposal actually was.",
        "must_not_show": "no halo, glare or rim-light; the tawdriness plain — heaven demoted to a street act, refused.",
        "scene": (
            "A close still in flat daylight: a street "
            "conjurer's little folding table standing "
            "abandoned in a market corner — the "
            "battered cups, the hidden-pea props, the "
            "worn velvet gone bald at the corners — "
            "the whole tired machinery of performance "
            "on demand, photographed as what the "
            "morning's grandest proposal amounted "
            "to. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b24", "out": "s24-it-is-written-again-thou.jpeg", "seg": "j2",
        "window": "128.54-132.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PINNACLE"],
        "narration": "It is written again, Thou shalt not tempt the Lord thy God.",
        "must_show": "SCRIPTURE-EXACT: the second answer — Jesus turning from the edge as he gives it: the written line and the turned back ending the interview together.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the turn from the drop the punctuation.",
        "scene": (
            "At the pinnacle Jesus turns from the "
            "edge — the answer leaving him as his "
            "shoulder comes around, the written line "
            "delivered over it into the bright empty "
            "height — his feet already carrying him "
            "back along the parapet toward the "
            "stairs, an interview ended by scripture "
            "and a turned back in the same easy "
            "motion. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b25", "out": "s25-trust-does-not-run-experiments.jpeg", "seg": "n5",
        "window": "134.09-139.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["SUMMIT"],
        "narration": (
            "Trust does not run experiments on the one it trusts. Then came the "
            "last offer, the biggest one."
        ),
        "must_show": "the last arena — the kingdoms summit introduced: black rock crown above the clouds, the sunset vista's first breadth; the biggest offer's stage.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the vista's gorgeousness beginning — the offer's own colouring.",
        "scene": (
            "The last arena assembles itself: a black "
            "rock crown standing above the cloud-line "
            "in the day's most gorgeous hour — and "
            "below and beyond it, breaking into view "
            "through the cloud-gaps, the first "
            "glimpses of the lit world: a river "
            "burning gold, far cities pricked with "
            "evening fires, roads running to every "
            "horizon — the biggest offer in history "
            "setting its own magnificent table. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b26", "out": "s26-from-a-high-mountain-all.jpeg", "seg": "n5",
        "window": "139.94-146.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SUMMIT"],
        "narration": (
            "From a high mountain, all the kingdoms of the world and the glory "
            "of them, spread out like a feast."
        ),
        "must_show": "SCRIPTURE-EXACT: the vista entire — Jesus on the black crown with the whole world's glory spread below to every horizon under the sunset; the feast of kingdoms at full width.",
        "must_not_show": "NO tempter; no halo, glare or rim-light on Jesus — the sunset's glory belongs to the OFFER, never outlines him.",
        "scene": (
            "From the black rock crown the world "
            "performs its whole inventory: kingdoms "
            "spread to every horizon under the "
            "sunset — marble cities catching the last "
            "gold, harbours crowded with sails, "
            "mountain roads strung with caravans, "
            "river valleys deep in harvest — glory "
            "laid out edge to edge like a feast on "
            "the world's own table — and at the "
            "crown's lip one gaunt cream-clad figure "
            "stands regarding all of it with level "
            "eyes. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b27", "out": "s27-all-these-things-will-i.jpeg", "seg": "s9",
        "window": "146.95-150.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["SUMMIT"],
        "narration": (
            "All these things will I give thee, if thou wilt fall down and "
            "worship me."
        ),
        "must_show": "SCRIPTURE-EXACT: the price named — the vista's most gorgeous reach close, and at the frame's edge the bare rock where a knee would go; everything, priced at one bow.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the kneeling-spot's bare rock the contract's signature line, unsigned.",
        "scene": (
            "The offer's two halves share one close "
            "frame: filling most of it, the vista's "
            "richest reach — a golden capital on its "
            "river, glory upon glory in the sunset — "
            "and at the frame's near edge, in "
            "shadow, one flat patch of bare black "
            "rock exactly the size of a man's two "
            "knees: the entire contract, laid out "
            "with its signature line empty. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r070-b28", "out": "s28-all-of-it-yours-right.jpeg", "seg": "n5b",
        "window": "152.29-158.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SUMMIT"],
        "narration": (
            "All of it, yours, right now — one bow, to me. It was the crown "
            "without the cross."
        ),
        "must_show": "the shortcut's anatomy — Jesus's face against the burning vista: the crown's whole appeal registered honestly, and beneath it the longer road already chosen.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the temptation REAL on his face — an offer felt at full weight before refusal.",
        "scene": (
            "Close on Jesus's gaunt face with the "
            "burning kingdoms soft behind it: the "
            "offer registering honestly — the eyes "
            "moving once across all that gold, the "
            "weight of the shortcut landing as real "
            "weight — and underneath the registering, "
            "unmoved, the old set of a man whose "
            "road runs through a darker hill than "
            "this one, and who has known it all "
            "along. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b29", "out": "s29-everything-he-came-to-win.jpeg", "seg": "n5b",
        "window": "158.36-166.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["SUMMIT"],
        "narration": (
            "Everything he came to win, offered as a shortcut with only one "
            "small condition: worship the wrong king."
        ),
        "must_show": "the condition's smallness and size — the bare kneeling-rock close: one knee's worth of stone, the cheapest and costliest square foot in the world.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the rock plain — the whole war reduced to where a knee does not go.",
        "scene": (
            "Extreme close in the sunset's edge-"
            "light: the flat patch of bare black "
            "rock — pitted, cooling, exactly "
            "knee-sized — the smallest real estate "
            "in the whole gorgeous evening, and the "
            "only ground the entire offer actually "
            "wanted: one square foot of stone, "
            "waiting for a bow that is not coming. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r070-b30", "out": "s30-heaven-had-just-said-this.jpeg", "seg": "n2",
        "window": "47.46-50.28", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Heaven had just said, this IS my Son.",
        "must_show": "the sentence's certainty — the river memory's core: the opened sky's brightness over the water; the IS against every IF.",
        "must_not_show": "no figures needed — sky, rift and river as the sentence's monument; no rays.",
        "scene": (
            "The memory at its core: the great "
            "bright rift standing open in the cloud "
            "over the green Jordan, daylight doubled "
            "on the moving water below — no figure "
            "in frame, just the opened heaven and "
            "the river it spoke over — the IS of "
            "the Father's sentence, built in sky, "
            "against which every desert IF will "
            "break for forty days. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b31", "out": "s31-get-thee-hence-satan-for.jpeg", "seg": "j3",
        "window": "166.64-174.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SUMMIT"],
        "narration": (
            "Get thee hence, Satan: for it is written, Thou shalt worship the "
            "Lord thy God, and him only shalt thou serve."
        ),
        "must_show": "SCRIPTURE-EXACT: the dismissal — Jesus at full height on the crown, arm flung toward the empty air in absolute command; the third answer as eviction.",
        "must_not_show": "NO tempter visible even in departure — the command aimed at vacancy; no halo, glare or rim-light on Jesus.",
        "scene": (
            "On the black crown against the burning "
            "sky Jesus stands at his full gaunt "
            "height, one arm flung straight toward "
            "the empty air off the summit's edge — "
            "the command leaving him with the whole "
            "authority the forty days have been "
            "measuring — a starving man evicting an "
            "empire's salesman from a mountaintop "
            "with a written sentence and a pointed "
            "hand, into air that was always going "
            "to be shown empty. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b32", "out": "s32-get-away-from-me-he.jpeg", "seg": "n6a",
        "window": "175.67-180.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SUMMIT"],
        "narration": (
            "Get away from me. He did not haggle with the offer, and he did not "
            "admire it."
        ),
        "must_show": "the finality — close on Jesus's face after the command: the interview OVER in every feature; no negotiation's residue anywhere.",
        "must_not_show": "NO tempter; no halo, glare or rim-light; the over-ness total — a face with nothing left pending in it.",
        "scene": (
            "Close on Jesus's face in the sunset's "
            "last strength: the command gone out and "
            "the features already settling behind "
            "it — no lingering on the vista, no "
            "backward audit of the offer's terms, "
            "not one grain of a negotiator's "
            "residue — the face of a man whose "
            "meeting has ended, checking nothing, "
            "regretting nothing, already turning "
            "toward the long walk down. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b33", "out": "s33-he-named-it-and-ended.jpeg", "seg": "n6a + s11",
        "window": "180.11-187.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SUMMIT", "MINISTERS"],
        "narration": (
            "He named it and ended it. Then the devil leaveth him, and, behold, "
            "angels came and ministered unto him."
        ),
        "must_show": "SCRIPTURE-EXACT, RESTRAINED: the turn of the tide — the summit's air gone clean, and the two plain-robed ministers arriving up the rocks with bread, water and a blanket; help on foot, at last.",
        "must_not_show": "NO wings, NO light-effects, no floating — the ministers climb like travellers; no halo on anyone; the departure of the enemy shown only as the air's new cleanness.",
        "scene": (
            "The summit's air stands suddenly clean — "
            "the flat wrongness gone out of the "
            "light, the wind ordinary again — and up "
            "over the black rocks the two deep-blue-"
            "robed ministers come climbing on their "
            "own two feet, one with bread and a "
            "water-skin, the other with a folded "
            "blanket over an arm — help arriving the "
            "way help arrives, walking, at the exact "
            "minute the war ended. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b34", "out": "s34-and-it-was-over-the.jpeg", "seg": "n6",
        "window": "188.62-192.78", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SUMMIT"],
        "narration": "And it was over. The devil left him — for a season.",
        "must_show": "the over-ness and the ellipsis — Jesus sitting down at last on the crown's rock, the long exhale visible; and the horizon holding its 'for a season' quietly.",
        "must_not_show": "NO tempter, no dark shape departing; the 'for a season' carried by distance and dusk, not by imagery.",
        "scene": (
            "On the crown's rock Jesus sits down at "
            "last — the first sitting of victory, "
            "knees up, head back against the stone, "
            "the long exhale of forty days leaving "
            "him visibly — while beyond his rest the "
            "dusk horizon runs its quiet unmeasured "
            "distance: somewhere out there a season, "
            "and after it a garden; but not tonight. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r070-b35", "out": "s35-and-angels-came-and-ministered.jpeg", "seg": "n6",
        "window": "192.78-198.23", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SUMMIT", "MINISTERS"],
        "narration": (
            "And angels came and ministered to him, the way dawn comes after "
            "the longest night."
        ),
        "must_show": "SCRIPTURE-EXACT, RESTRAINED: the ministering — DAWN on the summit: the two blue-robed figures kneeling beside the seated Jesus, bread broken into his hands, the blanket around his shoulders.",
        "must_not_show": "NO wings, NO light-effects — dawn's own light only; service as travellers' kindness; no halo on anyone.",
        "scene": (
            "Dawn comes up clean over the summit — "
            "and the ministering with it: the two "
            "blue-robed figures kneeling on the rock "
            "beside the seated Jesus, one breaking "
            "bread directly into his wasted hands, "
            "the other settling the blanket around "
            "his shoulders against the height's "
            "cold — the first food of six weeks and "
            "the first company, arriving together "
            "with the light, exactly the way dawn "
            "arrives: on schedule, after the worst. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r070-b36", "out": "s36-bread-after-the-fast-company.jpeg", "seg": "n6",
        "window": "198.23-203.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MINISTERS"],
        "narration": "Bread, after the fast. Company, after the silence.",
        "must_show": "the two gifts close — Jesus's hands around real bread, eating slowly; a minister's steadying hand at his shoulder; hunger and solitude ending in one frame.",
        "must_not_show": "no wings, no light-effects, no halo; the eating human and slow — a fast broken gently.",
        "scene": (
            "Close in the dawn light: Jesus's gaunt "
            "hands around a torn piece of real "
            "bread, eating with the careful slowness "
            "of a long fast's first meal — eyes "
            "closed over the taste — while at his "
            "shoulder a blue-sleeved hand rests "
            "steady, and the water-skin waits "
            "uncorked at his knee — bread after the "
            "fast, a hand after the silence, both "
            "being received like the treasures they "
            "are. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b37", "out": "s37-his-father-had-not-been.jpeg", "seg": "n6",
        "window": "203.05-207.89", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SUMMIT"],
        "narration": (
            "His Father had not been absent for one minute of it — he had been "
            "trusted."
        ),
        "must_show": "the trust vindicated — Jesus's face at rest in the dawn, fed and warmed: the river's sentence intact, the whole fast re-read as presence.",
        "must_not_show": "no halo, glare or rim-light; the vindication interior — peace as evidence.",
        "scene": (
            "Close on Jesus's face in the young "
            "dawn: fed now, warmed, the blanket's "
            "edge at his jaw — and the features "
            "resting in a peace with history in it: "
            "not relief that help finally came, but "
            "the settled vindication of a man who "
            "knew the whole time whose silence he "
            "was trusting, and has just been proven "
            "exactly right. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b38", "out": "s38-for-we-have-not-an.jpeg", "seg": "s415",
        "window": "208.54-218.24", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "For we have not an high priest which cannot be touched with the "
            "feeling of our infirmities; but was in all points tempted like as "
            "we are, yet without sin."
        ),
        "must_show": "the Hebrews verse as image — a close still: the desert's loaf-stone, a pinnacle pebble and a black summit chip laid together on a plain cloth; the three tests, kept like evidence of understanding.",
        "must_not_show": "no halo, glare or rim-light; the three small stones the whole doctrine — tempted in all points, understood forever.",
        "scene": (
            "A close still on plain dark cloth: "
            "three small stones laid side by side — "
            "a crust-brown loaf-shaped desert "
            "stone, a pale chip of temple masonry, "
            "a black flake of summit rock — the "
            "three examinations' exhibits, gathered "
            "and kept the way courts keep evidence: "
            "proof, forever on file, that every "
            "point of our weakness has been stood "
            "in first. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b39", "out": "s39-he-did-not-use-his.jpeg", "seg": "n3",
        "window": "76.55-78.85", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": "He did not use his own power.",
        "must_show": "the power sheathed — Jesus's empty open hands in his lap at the ledge, capable of everything, doing nothing; omnipotence at rest by choice.",
        "must_not_show": "no halo, glare or rim-light; the hands' emptiness the discipline — nothing summoned, nothing taken.",
        "scene": (
            "Close on Jesus's two hands open in his "
            "lap in the desert light: wasted, "
            "steady, and utterly at rest — hands "
            "that calmed water and will raise the "
            "dead, holding nothing, changing "
            "nothing, taking nothing — the fullest "
            "power in the wilderness sheathed in "
            "its own patience, one fast-day at a "
            "time. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r070-b40", "out": "s40-that-is-what-the-book.jpeg", "seg": "n7",
        "window": "219.70-227.87", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That is what the book of Hebrews is saying. We do not have a "
            "Savior who cannot understand our weakness — he was tempted in "
            "every way we are."
        ),
        "must_show": "the understanding applied — a human vignette: a weary modern-timeless man at a night table with his head in his hands, and beside his elbow a small scroll open at its line; understood company in a hard hour.",
        "must_not_show": "no halo, glare or rim-light; the man's struggle unnamed and universal; the open line his one companion.",
        "scene": (
            "At a plain table in a lamp's small "
            "circle a weary man sits with his head "
            "in his hands — the posture of any hard "
            "midnight, the struggle unnamed — and at "
            "his elbow, open where a thumb has "
            "worried it soft, a small scroll's one "
            "line waits in the light — a tired human "
            "being keeping company, knowingly or "
            "not, with the only sympathy in the "
            "universe that was earned in a desert. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r070-b41", "out": "s41-hungry-alone-offered-every-shortcut.jpeg", "seg": "n7",
        "window": "227.87-230.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["DESERT"],
        "narration": "Hungry, alone, offered every shortcut.",
        "must_show": "the résumé of understanding — the empty ledge camp at dusk: the counted stones, the shelter's worn shadow, the fast's whole address; where the sympathy was earned.",
        "must_not_show": "no halo, glare or rim-light; the camp as credentials — forty days' residence, on display.",
        "scene": (
            "The ledge camp stands empty in the "
            "dusk: the row of forty counted stones "
            "along its lip, the ground worn smooth "
            "where one body kept its vigil, the "
            "overhang's shadow reaching out across "
            "rock that held a starving man through "
            "six weeks of silence — the plain "
            "wilderness address where the world's "
            "entire supply of earned sympathy was "
            "manufactured. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r070-b42", "out": "s42-he-has-stood-in-your.jpeg", "seg": "n7",
        "window": "230.79-236.61", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DESERT"],
        "narration": (
            "He has stood in your exact spot. That is why he knows how to stand "
            "next to you in it."
        ),
        "must_show": "the closing image — the desert track at dawn: Jesus walking back toward the green valley and the world, restored and resolute; the tested one returning to stand beside the tested.",
        "must_not_show": "no halo, glare or rim-light; the return the promise — out of the waste, toward everyone.",
        "scene": (
            "Down the dawn-lit track Jesus walks "
            "out of the badlands toward the "
            "green valley and the waking world — "
            "fed, warmed, the blanket folded over "
            "one shoulder, his stride carrying the "
            "new gravity of a man coming from a "
            "won war nobody watched — the desert "
            "falling away behind him, and ahead, "
            "in every direction the road can "
            "reach, all the people whose exact "
            "spots he now knows from standing in "
            "them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
]
