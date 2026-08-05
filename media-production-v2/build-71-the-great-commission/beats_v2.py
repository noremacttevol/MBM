#!/usr/bin/env python3
"""V2 beat map — row 71, build-71-the-great-commission (Matthew 28:16-20).

COVERAGE: 21 pictures over 118.2 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 28:16-20 KJV):
  v16   "the ELEVEN disciples went away into Galilee, into a MOUNTAIN
        where Jesus had appointed them" — eleven, not twelve: the gap in
        the count is a quiet visible fact; a green Galilean mountain in
        spring morning light.
  v17   "they WORSHIPPED him: but some DOUBTED" — both honoured: the
        falling down AND the standing hesitation, in one frame, neither
        scolded.
  v18   "ALL POWER is given unto me in heaven and in earth" — the risen
        Jesus: SAME locked face, SAME cream robe; the resurrection
        carried by morning light and the healed nail-marks at his wrists
        (scarred clean, no wound detail) — never by glow.
  v19   "teach ALL NATIONS, baptizing them in the name of the FATHER,
        and of the SON, and of the HOLY GHOST" — the three named
        distinctly (b13 leans on it); the horizon-wide sending.
  v20   "lo, I AM WITH YOU ALWAY, even unto the END OF THE WORLD" — the
        promise as the row's floor; the closing beats run the sentence
        down two thousand years to the viewer.
  PRE-CONTEXT (b01, b12, b03): crucified — rendered as the DISTANT hill
        with three EMPTY crosses against a dark dawn (off-screen law;
        no figures, no blood); buried — the sealed tomb's stone; alive
        — the risen one in plain morning light.

TIME OF DAY: the pre-context beats at dark dawn (crosses) and grey dawn
(tomb), breaking to clear morning for everything on the mountain; the
closing reach-beats run morning light around the world's horizon.

CONTENT-CARE: crucifixion/burial handled by the off-screen law — empty
crosses distant, sealed stone, nothing graphic; doubt dignified per
v17; the risen body reverent — scarred wrists clean, no wound detail.

CHANGING CONDITION (kept OUT of the locks): the disciples' postures —
climbing unsure, fallen in worship, standing in doubt, gathered close,
then scattering to the horizons. The count stays visibly ELEVEN.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MOUNT": (
        "GALILEE MOUNTAIN LOCK: a green rounded mountain in spring — "
        "grass and wildflowers over stone shoulders, the lake's blue "
        "visible far below to the east, terraced valleys west, and a "
        "broad summit meadow. The same meadow, lake-view and skyline "
        "in every mountain beat."
    ),
    "ELEVEN": (
        "THE ELEVEN LOCK: the remaining disciples — the four from "
        "CAST_LOCKS (PETER, ANDREW, JOHN, JAMES-Z) among seven other "
        "weathered Galilean men in SATURATED DEEP earth colours: dark "
        "browns, deep russet, dark olive, burnt ochre, dusty indigo "
        "(never cream, never white; only Jesus wears cream). ALWAYS "
        "eleven — countable where the frame allows. Faces shown "
        "clearly."
    ),
    "TOMB": (
        "TOMB LOCK: a rock-hewn garden tomb — a low doorway cut in a "
        "limestone face, the great disc-stone in its channel, an olive "
        "garden around it. Used SEALED in the burial beat only."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r071-b01", "out": "s01-he-had-been-crucified.jpeg", "seg": "n1",
        "window": "0.28-1.67", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "He had been crucified.",
        "must_show": "⚑ OFF-SCREEN LAW: the fact at distance — the low hill with three EMPTY crosses small against a dark storm-dawn sky; no figures, ever.",
        "must_not_show": "NO bodies, NO blood, NO close view — the hill far, the crosses bare; the sentence carried by silhouette and sky.",
        "scene": (
            "Under a dark storm-dawn sky the low hill "
            "stands at a great distance — and on its "
            "crown, small and bare against the grey "
            "light, three empty crosses lean at their "
            "worked angles — no figure near them, no "
            "detail given, the whole terrible sentence "
            "reduced by distance and mercy to three "
            "dark marks on a hill the world will never "
            "forget the shape of. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b02", "out": "s02-before-he-returned-to-his.jpeg", "seg": "n1",
        "window": "6.89-15.56", "wide": True, "jesus": False, "ref": False,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "Before he returned to his Father, he gathered the eleven one last "
            "time, on a mountain in Galilee he had told them to go to."
        ),
        "must_show": "SCRIPTURE-EXACT: the appointed climb — the ELEVEN ascending the green mountain path in morning light; the count visible, the twelfth's absence quietly legible.",
        "must_not_show": "no halo, glare or rim-light; eleven countable on the path — the gap in the number left unremarked and present.",
        "scene": (
            "Up the green spring mountainside, the camera off the "
            "path taking the climb in profile, the "
            "eleven climb in a loose line through the "
            "wildflowers — Peter at the front with his "
            "old forward lean, John helping the eldest "
            "over a stone shoulder, the others strung "
            "behind in their dark road-worn colours — "
            "eleven men on a path built in their "
            "memory for twelve, climbing to an "
            "appointment none of them can imagine the "
            "size of. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r071-b03", "out": "s03-and-now-he-was-alive.jpeg", "seg": "n1",
        "window": "3.02-6.89", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "And now he was alive, and it was almost over.",
        "must_show": "the risen fact — Jesus standing in plain morning light on the summit meadow: the same face, the same cream robe, ALIVE; at his wrists the clean healed marks.",
        "must_not_show": "no halo, glare or rim-light — resurrection carried by morning and presence; the wrist-marks scarred CLEAN, no wound detail.",
        "scene": (
            "On the summit meadow Jesus stands in the "
            "plain clean light of morning — the same "
            "locked face, the same cream wool moving "
            "in the spring wind, utterly and quietly "
            "alive — and at his wrists, where the "
            "sleeves fall back, the healed marks show "
            "clean and pale: history's whole turning "
            "carried in ordinary daylight on a green "
            "hill, without one special effect. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r071-b04", "out": "s04-they-climbed-it-not-really.jpeg", "seg": "n2",
        "window": "16.12-22.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "They climbed it not really knowing what to expect. And when they "
            "saw him standing there, alive, they fell down and worshipped him."
        ),
        "must_show": "SCRIPTURE-EXACT: the seeing and the falling — the eleven cresting the meadow and going down in worship at the sight of him; knees hitting grass in a wave.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the worship physical and immediate — a wave of falling, faces down and faces up mixed.",
        "scene": (
            "The eleven crest the meadow, the camera behind their "
            "cresting shoulders, and the "
            "sight takes their legs: a wave of "
            "falling moves through them — Peter down "
            "first with both knees in the grass, "
            "John sinking with his hands over his "
            "mouth, the eldest lowering himself on "
            "another's arm — eleven men going down "
            "before the figure standing quiet in the "
            "morning light, worship arriving faster "
            "than understanding, exactly as it "
            "should. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r071-b05", "out": "s05-some-of-them-still-could.jpeg", "seg": "n2",
        "window": "22.77-27.68", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "Some of them still could hardly believe it was real. He did not "
            "scold the doubt."
        ),
        "must_show": "SCRIPTURE-EXACT (v17): worship AND doubt in one frame — most fallen, but two still standing back with unsure faces; and Jesus's gaze on the doubters GENTLE.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the doubters dignified — honest men at their limit, received without rebuke.",
        "scene": (
            "In the kneeling wave two still stand — "
            "back a pace, faces working, one with his "
            "hand pressed to his own chest testing "
            "whether he is dreaming, the other's eyes "
            "going from the marks to the face and "
            "back, unable to land — and Jesus's gaze "
            "rests on exactly these two with perfect "
            "unhurried gentleness: doubt being given "
            "all the time it needs, on the morning "
            "that has all the time there is. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r071-b06", "out": "s06-he-gave-them-the-whole.jpeg", "seg": "n2 + jv18",
        "window": "27.68-33.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "He gave them the whole world anyway. All power is given unto me in "
            "heaven and in earth."
        ),
        "must_show": "SCRIPTURE-EXACT: the claim of all power — Jesus stepping in among the kneeling and standing eleven, arms opening to the whole horizon as the sentence goes out.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the authority spoken among friends on grass — heaven's widest claim at picnic distance.",
        "scene": (
            "Jesus steps in among them — between the "
            "kneeling and the still-standing, the "
            "doubters included in the circle without "
            "comment — and his arms open wide as the "
            "sentence goes out, taking in the lake "
            "below, the valleys west, the whole "
            "morning horizon in one sweep: all power "
            "in heaven and earth, announced on a "
            "grassy summit to eleven road-worn men, "
            "two of whom are still catching up. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r071-b07", "out": "s07-every-authority-there-is-in.jpeg", "seg": "n3",
        "window": "35.59-39.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": (
            "Every authority there is, in heaven and on the earth, belongs to "
            "him."
        ),
        "must_show": "the claim's face — close on Jesus: total authority worn with total gentleness; the healed wrist-mark visible as the claim's price tag.",
        "must_not_show": "no halo, glare or rim-light; authority as calm — and the wrist-mark quietly in frame: how the power was paid for.",
        "scene": (
            "Close on Jesus in the morning light: the "
            "warm eyes level and utterly certain, all "
            "the authority there is resting in the "
            "face the way strength rests in a working "
            "man's shoulders — worn, not brandished — "
            "and at the frame's edge, where the "
            "cream sleeve falls back, the clean "
            "healed mark at the wrist: the receipt "
            "for every ounce of it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b08", "out": "s08-whatever-he-was-about-to.jpeg", "seg": "n3",
        "window": "39.98-45.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELEVEN"],
        "narration": (
            "Whatever he was about to ask of them, he had the right to ask it, "
            "and the power to back it."
        ),
        "must_show": "the listeners braced — the eleven's faces gathering close: fishermen and tax men about to be handed the world; the scale arriving on ordinary faces.",
        "must_not_show": "no halo, glare or rim-light; the ordinariness of the faces the point — the world's least likely board of directors, assembling.",
        "scene": (
            "Close along the gathered faces: Peter's "
            "weathered attention, John's young "
            "brightness, the eldest's deep-lined "
            "listening, the doubters' faces steadied "
            "now and leaning in with the rest — "
            "eleven ordinary working faces arranged "
            "in the morning light around a sentence "
            "still coming, like men at a table where "
            "the deed to everything is about to be "
            "read aloud. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b09", "out": "s09-go-ye-therefore-and-teach.jpeg", "seg": "jv19",
        "window": "45.92-54.42", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "Go ye therefore, and teach all nations, baptizing them in the name "
            "of the Father, and of the Son, and of the Holy Ghost:"
        ),
        "must_show": "SCRIPTURE-EXACT: the commission — Jesus's arm extended full toward the world's horizon past the lake, the eleven turning to follow the line of it; the GO given.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture horizon-length — a sending the size of the map.",
        "scene": (
            "Jesus's arm extends full-length, the camera at his "
            "side so the gesture crosses in profile toward "
            "the horizon — past the lake's blue, past "
            "the far hills, past everything the "
            "morning can show — and the eleven turn "
            "as one to follow the line of it, eleven "
            "faces lifting toward distances none of "
            "them has ever crossed: Galilee's "
            "fishermen being pointed at the whole "
            "round world, by the only arm with the "
            "right to point that far. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b10", "out": "s10-and-then-the-promise-that.jpeg", "seg": "n5",
        "window": "89.76-92.44", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "And then the promise that holds the whole thing up.",
        "must_show": "the promise gathering — close on Jesus's face turning from the horizon back to THEM: the sending's engine about to be named; tenderness after the immensity.",
        "must_not_show": "no halo, glare or rim-light; the turn from map to men — the promise personal before it is global.",
        "scene": (
            "Close on Jesus as his gaze comes back "
            "from the horizon to the eleven faces "
            "around him — the immensity of the "
            "sending still in the air, and his "
            "expression turning from the map to the "
            "men: warm, particular, promise-shaped — "
            "the whole world just assigned, and the "
            "assigner's face saying plainly that the "
            "next sentence is the one that makes it "
            "possible. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b11", "out": "s11-go-to-everyone-not-one.jpeg", "seg": "n4",
        "window": "55.92-66.15", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Go to everyone. Not one nation, not one kind of person, but all of "
            "them, to the far edges of the map, and bring them in through "
            "baptism."
        ),
        "must_show": "the everyone — a horizon montage in ONE scene: from the mountain's height, the world's variety implied in the visible distance — roads, a port's sails, far ridges fading past counting.",
        "must_not_show": "no halo, glare or rim-light; one continuous vista (never panels) — the map's far edges suggested by depth of distance.",
        "scene": (
            "From the mountain's height the everyone "
            "spreads in one deep vista: the lake with "
            "its fishing sails, the coast road "
            "running north with its caravans, a far "
            "port's white sails at the haze's edge, "
            "ridge fading behind ridge past all "
            "counting into the morning — every "
            "visible distance implying a farther one, "
            "the map's edges receding exactly the "
            "way the commission's do: without limit. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r071-b12", "out": "s12-he-had-been-buried.jpeg", "seg": "n1",
        "window": "1.67-3.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": "He had been buried.",
        "must_show": "⚑ OFF-SCREEN LAW: the burial as the SEALED tomb — the great disc-stone rolled home across the low doorway in grey dawn light; the fact in stone.",
        "must_not_show": "NO body, no mourner close-ups — the sealed stone alone; grief carried by grey light and shut rock.",
        "scene": (
            "In the grey dawn of the olive garden the "
            "tomb stands sealed: the great disc-stone "
            "rolled home in its channel across the "
            "low-cut doorway, the chisel-marks still "
            "sharp on the limestone face, dew heavy "
            "on the grass before the threshold — the "
            "world's heaviest full stop, carved and "
            "rolled and, as the morning will shortly "
            "discover, temporary. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b13", "out": "s13-and-hear-the-three-he.jpeg", "seg": "n4",
        "window": "66.15-72.46", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "And hear the three he names together, plainly, one breath apart: "
            "Three."
        ),
        "must_show": "the three named — Jesus's hand marking three quiet counts in the air before the listening eleven; the naming's plainness the doctrine.",
        "must_not_show": "no halo, glare or rim-light; NO symbols, no triangle imagery — three counted fingers and a plain sentence.",
        "scene": (
            "Before the listening circle Jesus's "
            "hand marks the naming — one, two, three "
            "quiet counts in the morning air, the "
            "Father, the Son, the Holy Ghost given "
            "each their own full breath — and the "
            "eleven receive the three-fold name with "
            "bowed attention, a baptismal formula "
            "being minted on a grass summit, plain "
            "as bread and permanent as rock. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r071-b14", "out": "s14-teaching-them-to-observe-all.jpeg", "seg": "jv20",
        "window": "73.06-82.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "Teaching them to observe all things whatsoever I have commanded "
            "you: and, lo, I am with you alway, even unto the end of the world."
        ),
        "must_show": "SCRIPTURE-EXACT: the promise given — Jesus among the eleven with a hand on the nearest shoulder as the ALWAY goes out; presence pledged at touch distance.",
        "must_not_show": "no halo, glare or rim-light; the promise physical — a hand on a shoulder underwriting the whole map.",
        "scene": (
            "Among the circle Jesus stands with one "
            "hand resting on Peter's shoulder as the "
            "promise goes out — I am with you alway — "
            "the words landing on eleven faces like "
            "provision loaded for a journey, the "
            "doubters' faces steadiest of all now — "
            "the entire commission's weight being "
            "underwritten by one present-tense "
            "sentence and one warm hand. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r071-b15", "out": "s15-amen.jpeg", "seg": "jv20",
        "window": "82.33-84.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNT"],
        "narration": "Amen.",
        "must_show": "the seal — a quiet still: the summit meadow's grass in the morning wind, the moment after the greatest sentence; the world's hinge, at rest.",
        "must_not_show": "no halo, glare or rim-light; stillness as amen — grass, wind, morning.",
        "scene": (
            "A quiet still on the summit meadow: the "
            "spring grass and wildflowers moving in "
            "the morning wind, the lake's blue "
            "steady below, the light clean on the "
            "stone shoulders — the moment after the "
            "greatest marching order in history, "
            "held by the mountain the way a held "
            "breath holds, one beat, before "
            "everything begins. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b16", "out": "s16-teach-them-not-just-to.jpeg", "seg": "n5",
        "window": "85.78-89.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELEVEN"],
        "narration": (
            "Teach them not just to hear it but to live it, everything he had "
            "shown them."
        ),
        "must_show": "the curriculum remembered — close on the eleven's faces holding three years of shown things: bread broken, feet washed, lepers touched; memory as syllabus.",
        "must_not_show": "no halo, glare or rim-light; the remembering visible — faces full of specific taught moments.",
        "scene": (
            "Close along the circle's faces in the "
            "morning light: each holding its own "
            "footage — Peter's eyes somewhere on a "
            "boat's remembered water, John's on a "
            "supper's remembered bread, the eldest's "
            "on some touched leper only he saw — "
            "eleven living libraries of everything "
            "shown for three years, being told that "
            "the showing is now theirs to do. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r071-b17", "out": "s17-i-am-with-you-always.jpeg", "seg": "n5",
        "window": "92.44-95.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "I am with you always. Not until it gets hard.",
        "must_show": "the ALWAYS unconditioned — close on Jesus's face at the word: presence promised without an escape clause; the sentence's spine.",
        "must_not_show": "no halo, glare or rim-light; the unconditional carried by steadiness — no fine print anywhere in the face.",
        "scene": (
            "Close on Jesus's face at the promise's "
            "centre: the warm eyes holding the "
            "eleven's gaze one by one as the word "
            "ALWAYS goes down — no clause forming "
            "behind it, no horizon on it, no "
            "condition in the set of the mouth — a "
            "presence being pledged with the "
            "unlimited plainness of a man signing "
            "his whole name. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b18", "out": "s18-not-until-you-fail-always.jpeg", "seg": "n5",
        "window": "95.94-99.76", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": "Not until you fail. Always, to the very end.",
        "must_show": "the promise landing on the failer — Jesus's gaze resting particularly on Peter: the man who denied him receiving the ALWAYS first; grace's addressing order.",
        "must_not_show": "no halo, glare or rim-light; Peter's receiving face the beat — a failed man being promised permanent company.",
        "scene": (
            "The ALWAYS finds its first address: "
            "Jesus's gaze resting on Peter — the "
            "fisherman's weathered face taking the "
            "word with the particular gratitude of "
            "the one man on the mountain who has "
            "already tested the promise's opposite "
            "and lived — a denier being told, in "
            "front of everyone, that the company is "
            "permanent, failures included, to the "
            "very end. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b19", "out": "s19-that-command-has-never-stopped.jpeg", "seg": "n6",
        "window": "100.34-108.41", "wide": True, "jesus": False, "ref": False,
        "locks": ["ELEVEN", "MOUNT"],
        "narration": (
            "That command has never stopped moving. Every person who ever told "
            "you about Jesus was standing in the long tail of that one sentence "
            "on that mountain."
        ),
        "must_show": "the sentence in motion — the eleven descending the mountain in different directions at last: the scattering begun, eleven trajectories leaving one summit.",
        "must_not_show": "no halo, glare or rim-light; the divergence the picture — one meadow emptying along many paths.",
        "scene": (
            "Down from the summit, the camera high behind the "
            "parting group, the scattering "
            "begins: the eleven descending by "
            "different shoulders of the mountain — "
            "two toward the lake and its boats, "
            "three down the western valley path, "
            "others angling north and south along "
            "the ridges — eleven dark figures "
            "leaving one green meadow on eleven "
            "diverging lines, the single sentence "
            "behind them already travelling in "
            "every direction at once. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b20", "out": "s20-it-reached-across-two-thousand.jpeg", "seg": "n6",
        "window": "108.41-113.15", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "It reached across two thousand years and the whole round earth to "
            "get to you."
        ),
        "must_show": "the reach personalized — a hand passing a small worn scripture into another waiting hand across a plain table; the relay's latest exchange, timeless.",
        "must_not_show": "no halo, glare or rim-light; the handoff simple — the two-thousand-year relay at its unit act.",
        "scene": (
            "Across a plain wooden table in warm "
            "light, the relay's unit act: one "
            "weathered hand passing a small worn "
            "scripture — cover soft with carrying, "
            "pages thumbed — into a younger hand "
            "opening to receive it — the exact "
            "gesture, repeated across twenty "
            "centuries and every sea, by which one "
            "sentence on one mountain finally "
            "arrived at every particular person it "
            "was always aimed at. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r071-b21", "out": "s21-that-is-how-far-he.jpeg", "seg": "n6",
        "window": "113.15-117.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNT"],
        "narration": (
            "That is how far he was willing to send someone, so that you would "
            "know."
        ),
        "must_show": "the closing image — the empty summit meadow in full morning, the eleven's paths visible dispersing below, the horizon wide beyond; a sending still in flight, aimed at the viewer.",
        "must_not_show": "no halo, glare or rim-light; the emptiness charged — the meadow as launch site; the horizon as address list.",
        "scene": (
            "The summit meadow stands empty in the "
            "full morning — the grass still holding "
            "eleven flattened places in its circle — "
            "and below, on every descending path, "
            "the small dark figures grow smaller "
            "toward the lake, the valleys, the "
            "roads, the world — while beyond them "
            "the horizon runs wide and unfinished in "
            "the light: a sending two thousand years "
            "deep and still in flight, with one more "
            "address on its list. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
# TOMB wiring REMOVED by the author 2026-08-05: the stash matched
# build-37's parable tomb by token name, but b12 is JESUS'S OWN sealed
# garden tomb — a different place from Lazarus's/the rich man's cave.
# Promote-first from b12's approved frame, and that frame must seed
# rows 96 (it-is-finished), 97 (empty-tomb) and 98 (mary-her-name).
PLACE_REFS = {}
# === end PLACE-PLATES ===
