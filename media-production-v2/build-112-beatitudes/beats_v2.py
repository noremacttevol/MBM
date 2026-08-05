#!/usr/bin/env python3
"""V2 beat map — row 112, build-112-beatitudes (Matthew 5:1-10).

COVERAGE: 27 pictures over 153.2 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 5 KJV):
  v1-2  "seeing the multitudes, he WENT UP into a mountain: and when
        he was SET (seated), his DISCIPLES CAME UNTO HIM: And he
        OPENED HIS MOUTH, and taught them" — a seated rabbi, the
        inner ring close, the multitude banked up the slope.
  v3-10 the eight blessings: poor in spirit — mourn — meek — hunger
        and thirst after righteousness — merciful — pure in heart —
        peacemakers — persecuted. Each blessing beat is illustrated
        by a FACE in the crowd that fits it (the world's overlooked,
        blessed by name).

FRAME-STAGING: the Mount of Beatitudes — DISTINCT from rows 109/111
(their flowered teaching slopes are small informal rings): here the
scale is a MULTITUDE banked up a broad hillside, Jesus seated on a
stone shelf partway up, disciples closest, the crowd rising behind.

TIME OF DAY: one clear bright morning throughout, warming toward gold
at the close.

CONTENT-CARE: no flags. The persecuted beat shows exclusion (a family
turned from a village gate) with NO violence; every "loser" face is
rendered with full dignity — the row's entire point.

CHANGING CONDITION (kept OUT of the locks): the crowd's expectation —
braced for the usual, then turned upside down; the blessing-faces —
one per beatitude, found in the crowd.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream.
LOCKS = {
    "MOUNT": (
        "MOUNT LOCK: the mount of the blessings — a broad green "
        "hillside above the lake's far blue: a natural stone shelf "
        "partway up where the teacher sits, the grassy slope banked "
        "with the seated multitude above and below it. The same "
        "shelf, slope and lake-line throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the multitude — hundreds of ordinary Galileans "
        "in DARK EARTH-BROWN, RUST, DEEP OLIVE, SLATE and MADDER "
        "robes (never cream, never white): farmers, widows, "
        "fishermen, mothers, old men, children; the world's "
        "overlooked, gathered."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r112-b01", "out": "s01-the-crowds-came-up-the.jpeg", "seg": "n1",
        "window": "0.28-8.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNT", "CROWD"],
        "narration": (
            "The crowds came up the mountain expecting, maybe, the usual — "
            "that God blesses the strong, the rich, the winners."
        ),
        "must_show": "the climb with the old expectation — the multitude streaming up the green hillside in morning light; the poor and worn climbing to hear who God prefers.",
        "must_not_show": "no halo; the crowd's WEAR visible — patched robes, tired backs, hope anyway.",
        "scene": (
            "Up the broad green hillside, the camera on the "
            "slope's flank taking the climbing streams in profile, "
            "the multitude climbs in the "
            "morning light — patched "
            "robes and work-bent backs, "
            "widows helped over the "
            "stones, children carried "
            "pick-a-back — hundreds of "
            "the world's unimportant "
            "people filing upward with "
            "the old expectation "
            "riding along: that they "
            "are climbing to hear, one "
            "more time, that God "
            "blesses the strong and "
            "the winning, which is to "
            "say, somebody else. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b02", "out": "s02-matthew-was-there-on-the.jpeg", "seg": "n1",
        "window": "8.04-13.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNT", "CROWD"],
        "narration": (
            "Matthew was there on the grass that day, and this is how he "
            "wrote down the beginning of it."
        ),
        "must_show": "the eyewitness — a keen-eyed man seated in the grass near the front, watching everything with a record-keeper's attention; the gospel's author before his book.",
        "must_not_show": "no halo; NO anachronistic writing tools in use — the memory being made, not yet written.",
        "scene": (
            "Close on the man who will "
            "write it down: keen-eyed, "
            "seated cross-legged in the "
            "grass near the front — a "
            "former tax-man's trained "
            "attention drinking in "
            "every detail the way he "
            "once counted coins: the "
            "seating, the faces, the "
            "morning light on the "
            "stone shelf — a memory "
            "being made word-perfect "
            "on a hillside, decades "
            "before ink will make it "
            "the most read sermon on "
            "earth. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b03", "out": "s03-his-friends-gathered-in-close.jpeg", "seg": "n1b",
        "window": "28.38-30.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "PETER", "JOHN"],
        "narration": "His friends gathered in close around him.",
        "must_show": "SCRIPTURE-EXACT: disciples came unto him — the inner ring settling close around the seated Jesus on the shelf: Peter and John nearest; concentric intimacy.",
        "must_not_show": "no halo, glare or rim-light; the RINGS readable — friends closest, multitude beyond.",
        "scene": (
            "The seating arranges itself "
            "in rings of love: Jesus "
            "settled on the stone shelf, "
            "and his friends drawing in "
            "close around him — Peter "
            "planting himself at his "
            "right knee, John "
            "cross-legged almost at his "
            "feet, the others shoulder "
            "to shoulder in the near "
            "grass — and beyond them "
            "the multitude banking up "
            "the slope, everyone as "
            "near as the hillside lets "
            "them get. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b04", "out": "s04-and-seeing-the-multitudes-he.jpeg", "seg": "s1f",
        "window": "14.28-23.38", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD", "PETER", "JOHN"],
        "narration": (
            "And seeing the multitudes, he went up into a mountain: and when "
            "he was set, his disciples came unto him: And he opened his "
            "mouth, and taught them, saying,"
        ),
        "must_show": "SCRIPTURE-EXACT: the whole verse staged — Jesus SEATED on the shelf, disciples come close, the multitude banked; the teaching's first breath.",
        "must_not_show": "no halo, glare or rim-light; Jesus SEATED (the rabbi's posture), never standing to declaim.",
        "scene": (
            "The verse composes itself, the camera behind the "
            "banked crowd's shoulders toward the seated shelf, "
            "on the hillside: the "
            "multitude seen and "
            "received, the teacher gone "
            "up and SEATED on the "
            "stone shelf in the "
            "rabbi's own posture — "
            "settled, unhurried, hands "
            "at rest — the disciples "
            "come in close about him "
            "and the great crowd "
            "quieting up the slope "
            "like wind dying across "
            "barley — and the mouth "
            "opening on the first "
            "words of the sermon the "
            "world would never stop "
            "reading. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b05", "out": "s05-he-saw-the-crowd-coming.jpeg", "seg": "n1b",
        "window": "24.89-28.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": "He saw the crowd coming, climbed the hillside, and sat down.",
        "must_show": "the seeing and seating — Jesus partway up, turning to SEE the climbing multitude, then taking his seat on the shelf; the teacher moved by the sight of them.",
        "must_not_show": "no halo, glare or rim-light; the SEEING first — his face toward the crowd before the sitting.",
        "scene": (
            "It begins with a looking: "
            "Jesus partway up the slope, "
            "turned back toward the "
            "climbing hundreds — the "
            "worn faces, the carried "
            "children, the hope in "
            "patched wool — and "
            "something in the seeing "
            "deciding everything, "
            "because he climbs to the "
            "stone shelf and sits "
            "down the way a man sits "
            "who intends to stay: this "
            "crowd, this morning, this "
            "sermon — for exactly "
            "these people. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b06", "out": "s06-and-then-he-opened-his.jpeg", "seg": "n1b",
        "window": "30.95-36.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": (
            "And then he opened his mouth and began to teach — and turned "
            "the whole thing upside down."
        ),
        "must_show": "the first word — close on Jesus's face as the teaching begins: warmth with revolution in it; the upside-down arriving gently.",
        "must_not_show": "no halo, glare or rim-light; the manner GENTLE — the overturning done softly.",
        "scene": (
            "Close on the gentlest "
            "revolution ever started: "
            "Jesus's face as the first "
            "words leave him — warm, "
            "unhurried, almost quiet — "
            "and carrying in that "
            "quietness a sentence "
            "built to turn every "
            "ranking the world keeps "
            "on its head: not the "
            "strong first, not the "
            "rich, not the winners — "
            "the whole pyramid of "
            "blessing inverted in the "
            "time it takes a seated "
            "man to open his mouth. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r112-b07", "out": "s07-blessed-are-the-poor-in.jpeg", "seg": "jv3",
        "window": "36.64-41.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": (
            "Blessed are the poor in spirit: for theirs is the kingdom of "
            "heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the first blessing — Jesus's open hand toward the crowd's emptiest-handed: a ragged man near the front with nothing to offer; the kingdom assigned to him FIRST.",
        "must_not_show": "no halo, glare or rim-light; the man DIGNIFIED in his poverty — the blessing landing visibly on him.",
        "scene": (
            "The first blessing goes "
            "looking for its owner: "
            "Jesus's open hand finding "
            "a ragged man near the "
            "front — a day-laborer "
            "whose whole posture "
            "apologizes for taking up "
            "grass, hands empty in his "
            "lap of everything "
            "including confidence — "
            "BLESSED ARE THE POOR IN "
            "SPIRIT — and the kingdom "
            "of heaven, the entire "
            "estate, deeded first to "
            "the man who came "
            "certain there was nothing "
            "here for him. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b08", "out": "s08-he-starts-with-the-very.jpeg", "seg": "n2",
        "window": "42.80-45.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": "He starts with the very people the world walks past.",
        "must_show": "the walked-past — close on faces the world overlooks: the ragged man, a bent widow, a scarred beggar; the sermon's chosen front row.",
        "must_not_show": "no halo; every face DIGNIFIED — overlooked, not pitiable.",
        "scene": (
            "Close on the sermon's "
            "chosen front row: the "
            "ragged laborer still "
            "stunned by his blessing, "
            "a bent widow whose eyes "
            "have not been met in the "
            "market for years, an old "
            "beggar with a scarred "
            "cheek holding his stick "
            "like an apology — the "
            "exact faces every street "
            "in every town has "
            "practiced walking past — "
            "gathered here to discover "
            "they are the ones the "
            "whole address was written "
            "to. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r112-b09", "out": "s09-not-the-and-the-ones.jpeg", "seg": "n2",
        "window": "45.39-52.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "Not the self-made and self-assured — the ones who know they "
            "have nothing to offer God but empty hands."
        ),
        "must_show": "the empty hands — close on open worn palms held loosely in laps through the crowd: nothing in any of them; the qualification for the kingdom.",
        "must_not_show": "no halo; the hands WORKING hands — calloused, empty, offered.",
        "scene": (
            "Close on the entry "
            "requirement, held in laps "
            "all over the hillside: "
            "hands — calloused, "
            "rope-scarred, wash-worn, "
            "field-cracked — lying "
            "open and empty in the "
            "morning light, holding "
            "between all of them not "
            "one credential, one "
            "coin, one argument for "
            "themselves — the exact "
            "emptiness the kingdom's "
            "first blessing named as "
            "its address, worn by the "
            "people who thought it "
            "disqualified them. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b10", "out": "s10-the-kingdom-he-says-belongs.jpeg", "seg": "n2",
        "window": "52.58-55.85", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": "The kingdom, he says, belongs to them first.",
        "must_show": "the first-ness — the wide slope: Jesus's gesture sweeping the humblest section of the crowd to the FRONT of the blessing; precedence reversed in composition.",
        "must_not_show": "no halo, glare or rim-light; the reversal SPATIAL — the back of every worldly line made the front of this one.",
        "scene": (
            "The line reforms itself "
            "under his gesture: Jesus's "
            "arm sweeping the crowd's "
            "humblest corner — the "
            "patched, the bent, the "
            "walked-past — to the very "
            "front of the kingdom's "
            "queue — THEIRS, FIRST — "
            "while every ranking the "
            "world drills into its "
            "children quietly reverses "
            "on a green hillside: the "
            "back of every line on "
            "earth, discovering it is "
            "the front of the one "
            "that matters. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b11", "out": "s11-blessed-are-they-that-mourn.jpeg", "seg": "jv456",
        "window": "56.41-63.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": (
            "Blessed are they that mourn: for they shall be comforted. "
            "Blessed are the meek: for they shall inherit the earth."
        ),
        "must_show": "SCRIPTURE-EXACT: mourners and meek — a grieving widow with tears wet on her face, and beside her a small quiet man; both under Jesus's blessing gesture.",
        "must_not_show": "no halo, glare or rim-light; the grief REAL and dignified — comfort promised, not yet erasing the tears.",
        "scene": (
            "Two blessings find two "
            "faces sitting side by "
            "side: a widow with grief "
            "still wet on her cheeks — "
            "mourning worn openly on "
            "the hillside because "
            "there is no strength "
            "left to hide it — and "
            "beside her a small quiet "
            "man who has never once "
            "pushed to any front in "
            "his life — and over both "
            "bowed heads the seated "
            "teacher's hand: COMFORTED, "
            "says the first blessing; "
            "THE EARTH, says the "
            "second, to the man who "
            "never claimed a foot of "
            "it. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r112-b12", "out": "s12-blessed-are-they-which-do.jpeg", "seg": "jv456",
        "window": "63.33-70.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "Blessed are they which do hunger and thirst after "
            "righteousness: for they shall be filled."
        ),
        "must_show": "SCRIPTURE-EXACT: the hunger — a young man's face aching visibly toward goodness: leaned forward, hands gripped, wanting to be different; hunger of the soul made facial.",
        "must_not_show": "no halo; the ache MORAL not physical — longing to be made good, unmistakable.",
        "scene": (
            "Close on a hunger no bread "
            "answers: a young man "
            "leaned all the way "
            "forward in the grass, "
            "hands gripped white "
            "between his knees, face "
            "aching openly toward the "
            "words — a man sick of "
            "what he keeps being, "
            "starving to be made "
            "good the way drought "
            "ground starves for rain — "
            "and the blessing finding "
            "him mid-ache: FILLED, it "
            "promises, to the one "
            "appetite the world has "
            "no market for. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b13", "out": "s13-the-grieving-will-be-comforted.jpeg", "seg": "n3",
        "window": "72.13-73.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": "The grieving will be comforted.",
        "must_show": "comfort beginning — the widow's neighbor's arm coming around her shoulders in the grass; the promise already rehearsing through human arms.",
        "must_not_show": "no halo; the comfort HUMAN and present — an arm, a leaning-in.",
        "scene": (
            "The promise starts "
            "rehearsing immediately: "
            "beside the weeping widow, "
            "a neighbor woman's arm "
            "coming around the shaking "
            "shoulders — no words, "
            "just the old sideways "
            "gathering-in that women "
            "have done at gravesides "
            "forever — grief leaning "
            "into the offered warmth "
            "in the morning grass — "
            "COMFORTED, the blessing "
            "said, and the hillside "
            "is already practicing, "
            "arm by arm. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r112-b14", "out": "s14-the-gentle-who-never-push.jpeg", "seg": "n3",
        "window": "73.67-80.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "The gentle, who never push to the front, will inherit "
            "everything. Those aching to be made good will be filled."
        ),
        "must_show": "the meek's placement — the small quiet man seated at the crowd's very edge, giving up his spot to a latecomer; meekness in action while inheriting everything.",
        "must_not_show": "no halo; the yielding HABITUAL — a lifetime's reflex caught once.",
        "scene": (
            "The inheritor of the earth "
            "demonstrates his claim: "
            "the small quiet man at "
            "the crowd's edge, "
            "shifting without being "
            "asked to give a "
            "late-come mother and "
            "child his patch of good "
            "grass — taking the rocky "
            "spot himself with the "
            "unthinking reflex of a "
            "man who has yielded "
            "every front seat of his "
            "life — and over his "
            "relocated head, unfelt "
            "by him, the deed to "
            "everything. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r112-b15", "out": "s15-every-blessing-goes-to-exactly.jpeg", "seg": "n3",
        "window": "80.32-84.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": (
            "Every blessing goes to exactly the person the world would call "
            "a loser."
        ),
        "must_show": "the upside-down roster — the wide slope: Jesus's blessing hand moving across the crowd's humblest faces one after another; the world's losers, collected as heirs.",
        "must_not_show": "no halo, glare or rim-light; the roster's DIGNITY absolute — the word loser refuted by every face it lands on.",
        "scene": (
            "The roster reads out, the camera at the slope's side "
            "so the moving blessing-hand crosses in profile, across "
            "the slope: the teacher's "
            "hand moving face to face "
            "over exactly the people "
            "every market and palace "
            "would wave off — the "
            "spiritually broke, the "
            "publicly grieving, the "
            "chronically gentle, the "
            "hungry-to-be-good — each "
            "one collected by the "
            "gesture like names read "
            "off a will — the world's "
            "whole loser column, "
            "re-filed under HEIRS on "
            "a green hillside before "
            "lunch. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b16", "out": "s16-blessed-are-the-merciful-for.jpeg", "seg": "jv78",
        "window": "85.50-89.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": "Blessed are the merciful: for they shall obtain mercy.",
        "must_show": "SCRIPTURE-EXACT: the merciful — a woman sharing her small bread with a stranger's child in the crowd; mercy caught mid-act, unposed.",
        "must_not_show": "no halo; the sharing SMALL and real — half a loaf, no ceremony.",
        "scene": (
            "Mercy gets caught in the "
            "act: a woman in the "
            "crowd, her own portion "
            "small, tearing it and "
            "handing half down to a "
            "stranger's hungry-eyed "
            "child without pausing "
            "her listening — no "
            "ceremony, no glance for "
            "witnesses, just the "
            "reflexive arithmetic of "
            "the merciful: you have "
            "less than me, here — and "
            "the blessing settling on "
            "her mid-tear: MERCY, "
            "obtained, with interest, "
            "forever. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b17", "out": "s17-blessed-are-the-pure-in.jpeg", "seg": "jv78",
        "window": "89.27-93.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": "Blessed are the pure in heart: for they shall see God.",
        "must_show": "SCRIPTURE-EXACT: the pure in heart — a child's utterly unguarded upturned face near the front, listening with whole-hearted openness; the see-God qualification, worn naturally.",
        "must_not_show": "no halo; the purity UNPERFORMED — a child simply listening with everything.",
        "scene": (
            "The qualification for the "
            "greatest promise turns "
            "out to be a child's "
            "resting state: a small "
            "girl near the front with "
            "her chin on her fists, "
            "face tipped up utterly "
            "unguarded — no angle in "
            "her listening, no "
            "second motive anywhere "
            "in the wide eyes, heart "
            "clean as morning water — "
            "THE PURE IN HEART SHALL "
            "SEE GOD, and she is "
            "looking straight at him "
            "already, without knowing "
            "the blessing is about "
            "her. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b18", "out": "s18-the-pure-in-heart-the.jpeg", "seg": "n4",
        "window": "95.34-101.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "The pure in heart — the simple, honest, unguarded ones — will "
            "actually see God."
        ),
        "must_show": "the unguarded ones — a row of open honest faces: the child, an old shepherd, a plain-spoken woman; simplicity as the seeing organ.",
        "must_not_show": "no halo; NOTHING clever in any face — honesty legible as rest.",
        "scene": (
            "Close along a row of the "
            "unguarded: the small girl "
            "with her chin on her "
            "fists, an old shepherd "
            "whose face has never once "
            "said anything it didn't "
            "mean, a plain-spoken "
            "woman with her hands "
            "open on her knees — "
            "faces without one hidden "
            "room in them, simple the "
            "way deep wells are "
            "simple — the actual "
            "optics of heaven, it "
            "turns out: hearts clean "
            "enough to see through. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r112-b19", "out": "s19-not-the-clever-or-the.jpeg", "seg": "n4",
        "window": "101.01-104.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": "Not the clever or the powerful. The clean of heart.",
        "must_show": "the contrast held — at the crowd's edge a fine-robed clever man calculating even here, and past him the clean-hearted row; who sees and who doesn't.",
        "must_not_show": "no halo; the clever man HUMAN, not villain — just visibly elsewhere behind the eyes.",
        "scene": (
            "The contrast sits at the "
            "crowd's edge: one "
            "fine-robed listener whose "
            "eyes are working even "
            "here — measuring the "
            "crowd, weighing the "
            "teacher's angles, "
            "calculating what this "
            "movement might be worth — "
            "clever to the bone and "
            "seeing, therefore, "
            "nothing — while past his "
            "shoulder the simple row "
            "gazes straight at what "
            "he is missing: the "
            "kingdom, in plain sight, "
            "visible only to the "
            "clean. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b20", "out": "s20-blessed-are-the-peacemakers-for.jpeg", "seg": "jv910",
        "window": "105.47-109.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "Blessed are the peacemakers: for they shall be called the "
            "children of God."
        ),
        "must_show": "SCRIPTURE-EXACT: the peacemaker — an older man in the crowd gently settling a flare-up between two neighbors over crowded space, a hand on each; peace being made in miniature.",
        "must_not_show": "no halo; the flare-up SMALL — jostled shoulders, not a brawl; the settling gentle.",
        "scene": (
            "Peacemaking happens in "
            "miniature right there in "
            "the crowd: two jostled "
            "neighbors flaring over "
            "trampled space, chests "
            "squaring — and between "
            "them, already, an older "
            "man's two hands landing "
            "easy on a shoulder each, "
            "his low word finding the "
            "joke in it, the flare "
            "dying into sheepish "
            "grins — a family "
            "resemblance surfacing in "
            "the mediator's weathered "
            "face just as the blessing "
            "names it: CHILDREN OF "
            "GOD. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r112-b21", "out": "s21-blessed-are-they-which-are.jpeg", "seg": "jv910",
        "window": "109.94-117.97", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Blessed are they which are persecuted for righteousness' sake: "
            "for theirs is the kingdom of heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the persecuted — a vignette beyond the hill: a small family turned away from a village gate for their uprightness, walking out with heads unbowed; NO violence.",
        "must_not_show": "ABSOLUTE: no violence, no thrown stones — exclusion only: a shut gate, turned backs, and unbowed departure.",
        "scene": (
            "The costliest blessing gets "
            "its quiet picture: at a "
            "village gate beyond the "
            "hill, a small family "
            "turned away — the gate "
            "shut to them, neighbors' "
            "backs turned, their goods "
            "on one handcart — walking "
            "out the road with their "
            "heads unbowed, paying "
            "full price for refusing "
            "to bend what was right — "
            "and over their small "
            "departing dignity, the "
            "same words that opened "
            "the sermon: THEIRS IS "
            "THE KINGDOM OF HEAVEN. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r112-b22", "out": "s22-the-ones-who-make-peace.jpeg", "seg": "n5",
        "window": "119.48-122.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "The ones who make peace instead of winning fights are called "
            "God's own children."
        ),
        "must_show": "the family name conferred — the peacemaker's face close after his work: the settled neighbors either side; quiet likeness to a Father visible.",
        "must_not_show": "no halo; the likeness in CHARACTER — gentleness worn like inherited features.",
        "scene": (
            "Close on a face that just "
            "chose peace over winning: "
            "the older mediator settled "
            "back between his two "
            "reconciled neighbors, "
            "breathing easy, wanting "
            "no credit — and in the "
            "weathered features, plain "
            "as inherited eyes or a "
            "father's jaw, the family "
            "resemblance the blessing "
            "named: gentleness held "
            "like strength, patience "
            "worn like a birthright — "
            "God's own child, "
            "recognizable at twenty "
            "paces by the peace he "
            "leaves behind him. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b23", "out": "s23-and-even-those-pushed-aside.jpeg", "seg": "n5",
        "window": "122.91-128.77", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And even those pushed aside for doing right are not forgotten — "
            "the kingdom is theirs, too."
        ),
        "must_show": "the not-forgotten — the turned-away family on the open road in warm light, the way ahead golden; exile re-lit as inheritance.",
        "must_not_show": "no halo; the road WARM — loss real, future realer.",
        "scene": (
            "The exiles' road refuses to "
            "read as defeat: the small "
            "family and their handcart "
            "out on the open way in "
            "the day's warming gold, "
            "the shut village shrinking "
            "behind, the road ahead "
            "running bright toward "
            "hills full of light — "
            "pushed aside, and walking "
            "somehow like landowners — "
            "because by the morning's "
            "new arithmetic they are "
            "exactly that: the "
            "kingdom, theirs, no gate "
            "on earth able to shut "
            "them out of it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b24", "out": "s24-every-last-person-the-world.jpeg", "seg": "n5",
        "window": "128.77-133.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": "Every last person the world overlooks, God is reaching for.",
        "must_show": "the reach — the wide hillside: Jesus's open arms taking in the ENTIRE multitude at once; nobody outside the gesture, the overlooked gathered whole.",
        "must_not_show": "no halo, glare or rim-light; the reach TOTAL — edges of the crowd included in the arms' line.",
        "scene": (
            "The sermon opens its arms, the camera far back "
            "behind the whole multitude's heads, "
            "all the way: Jesus on the "
            "stone shelf with both "
            "arms spread wide enough "
            "to take the whole "
            "hillside in — front row "
            "to farthest straggler, "
            "the widow and the "
            "laborer and the clever "
            "man at the edge and the "
            "child asleep on her "
            "mother's arm — every "
            "last overlooked soul on "
            "the slope caught inside "
            "one reaching span, and "
            "the reach, visibly, "
            "still hungry for more. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r112-b25", "out": "s25-so-if-you-have-ever.jpeg", "seg": "n6",
        "window": "133.62-141.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "So if you have ever felt small, unseen, worn thin, or passed "
            "over — listen closely."
        ),
        "must_show": "the addressed — close on the crowd's most unseen face lifting at the words: an exhausted middle-aged woman realizing the sermon means HER.",
        "must_not_show": "no halo; the realization DAWNING — years of invisibility meeting direct address.",
        "scene": (
            "Close on the moment "
            "invisibility ends: a "
            "middle-aged woman near "
            "the crowd's rear — worn "
            "thin by years nobody "
            "counted, unseen so long "
            "she stopped expecting "
            "eyes — her face lifting "
            "slowly at the words the "
            "way a plant lifts at "
            "water: SMALL, UNSEEN, "
            "WORN, PASSED OVER — her "
            "own biography read out "
            "loud on a mountain, and "
            "attached, unbelievably, "
            "to a blessing. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r112-b26", "out": "s26-in-his-kingdom-you-are.jpeg", "seg": "n6",
        "window": "141.38-147.93", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": (
            "In his kingdom, you are not at the back of the line. You are "
            "exactly the one he came for."
        ),
        "must_show": "the front of the line — the humble faces nearest Jesus in the gold light, the worn woman drawn forward among them; back-of-the-line abolished in the seating itself.",
        "must_not_show": "no halo, glare or rim-light; the geometry the message — the least, nearest.",
        "scene": (
            "The seating chart preaches "
            "the closing point: "
            "nearest the teacher in "
            "the warming gold sit "
            "exactly the wrong people "
            "by every rule of every "
            "line — the ragged "
            "laborer at his knee, the "
            "widow inside arm's "
            "reach, the worn unseen "
            "woman drawn forward to "
            "the grass by the shelf — "
            "the back of the line "
            "abolished not by decree "
            "but by seating, on a "
            "hillside where the least "
            "sit closest because he "
            "came for precisely them. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r112-b27", "out": "s27-that-is-how-upside-down.jpeg", "seg": "n6",
        "window": "147.93-152.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "CROWD"],
        "narration": "That is how upside down, and how good, his kingdom really is.",
        "must_show": "the closing image — the whole blessed hillside in full gold: teacher seated, multitude at peace, the lake shining below; the upside-down kingdom at rest, and good.",
        "must_not_show": "no halo, glare or rim-light; the goodness ATMOSPHERIC — the entire slope visibly better off than it climbed up.",
        "scene": (
            "The closing frame holds the "
            "whole overturned world at "
            "rest: the seated teacher "
            "on his stone shelf, the "
            "multitude spread easy "
            "down the gold-lit slope — "
            "mourners leaned into "
            "neighbors, children "
            "asleep, empty hands "
            "lying open like they "
            "are finally holding "
            "something — the lake "
            "shining below a hillside "
            "of the world's overlooked "
            "who climbed up losers "
            "and are sitting there, "
            "in the evening light, "
            "heirs. Every figure has "
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
