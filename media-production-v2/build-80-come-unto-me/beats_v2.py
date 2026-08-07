#!/usr/bin/env python3
"""V2 beat map — row 80, build-80-come-unto-me (Matthew 11:28-30).

COVERAGE: 14 pictures over 83.0 s = 5.9 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 11:28-30 KJV):
  v28   "Come unto me, ALL ye that LABOUR and are HEAVY LADEN, and I
        will give you REST." — addressed to the worn-out; the coming
        happens WHILE still loaded, no precondition.
  v29   "Take MY YOKE upon you, and LEARN of me; for I am MEEK and
        LOWLY IN HEART: and ye shall find rest unto your souls."
  v30   "For my yoke is EASY, and my burden is LIGHT."
  YOKE FACT: a yoke is the carved wooden beam joining TWO oxen so the
  load is pulled by both — a two-sided, SHARED instrument; the image
  is partnership under one beam, not solitary harness.

FRAME-STAGING: a village-lane teaching row — DISTINCT from the boat
rows (Matt 13) and the mount rows: here Jesus stands among homeward
labourers in a working lane; the metaphor beats cut away to a
plough-team field.

TIME OF DAY ARC (intentional): warm DAY'S END throughout — the hour
worn-out workers walk home — deepening to last gold light at the
close. This is a correct story sunset, not the row-11 defect.

CONTENT-CARE: no flags. The weary rendered with dignity — tired, never
wretched; the mercy IN the text carried to the last frame: the load
shared, never mocked.

CHANGING CONDITION (kept OUT of the locks): the carrier's burden — on
his back alone at the start, steadied by a second pair of hands at the
close; and the ox team — one beast labouring, then two sharing.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "LANE": (
        "LANE LOCK: a Galilean village lane at day's end — worn "
        "flagstones between low stone walls and doorways, a fig tree "
        "at the bend, warm low gold light down its length. The same "
        "lane, walls and tree throughout."
    ),
    "CARRIER": (
        "CARRIER LOCK: the burdened man we track is the same man in "
        "every shot — about forty-five, heavy-shouldered and bone-"
        "tired, short greying dark beard, in a DARK UMBER-BROWN work "
        "tunic (never cream, never white), bent under a big rough "
        "GRAIN SACK roped across his back."
    ),
    "OXFIELD": (
        "OXFIELD LOCK: a half-ploughed field at the village edge — "
        "dark turned earth beside pale stubble, a single CARVED WOODEN "
        "DOUBLE YOKE with two bow-loops, and matched RUSSET-BROWN oxen; "
        "the same field, beam and beasts throughout."
    ),
}

REF = True

# AUDIO-FIX (AUDIO-FIX session, Machine A, 2026-08-06): the V1 mp4
# matthew-11_come-unto-me.mp4 (rendered 2026-07-29 09:47) is STALE vs this
# build's own narration — all 11 SPEAKER-LAW segment mp3s (audio/*.mp3) are
# NEWER (2026-07-29 23:03, the intended new-voice audio), so
# assert_v1_final_is_current's recency tripwire refuses to copy the stale AAC.
# Segment-ID parity with make_narration.py is exact (11/11: n0a,n0b,n0c,n1,n1b,
# n2a,n2b,j1,j2,j3,card), so rebuild the track from these segments at the
# extract offsets instead of copying the stale mp4. $0 — nothing re-voiced,
# nothing re-timed; V1 stays read-only. Same mechanism as the shipped row-69 fix.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r080-b01", "out": "s01-to-a-crowd-of-people.jpeg", "seg": "n0a",
        "window": "0.40-5.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["LANE", "CARRIER"],
        "narration": (
            "To a crowd of people worn down by work, by rules, by just "
            "getting through the day,"
        ),
        "must_show": "the worn-down — the lane at day's end filled with homeward labourers: the carrier bent under his sack, a woman with a water jar, a farmer dragging his mattock; tiredness in every spine.",
        "must_not_show": "no halo, glare or rim-light; the weariness DIGNIFIED — worked-out people, never wretched or ragged caricatures.",
        "scene": (
            "The lane carries the day's end home, the camera at the "
            "lane's side taking the homeward traffic in profile: "
            "labourers strung down the warm gold "
            "flagstones — the heavy-shouldered "
            "carrier bent under his roped grain "
            "sack, a woman balancing her water "
            "jar with both aching arms, a farmer "
            "dragging his mattock like it grew "
            "heavier since noon — every spine in "
            "the picture writing the same "
            "sentence: worn down, and still not "
            "done. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r080-b02", "out": "s02-jesus-made-one-of-the.jpeg", "seg": "n0b",
        "window": "6.95-10.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LANE"],
        "narration": "Jesus made one of the gentlest offers ever spoken.",
        "must_show": "the offerer — Jesus standing in the lane among the tired traffic, still and warm in the low light, about to speak; faces beginning to turn.",
        "must_not_show": "no halo, glare or rim-light on Jesus; he stands AMONG them at street level — no platform, no distance.",
        "scene": (
            "In the middle of the tired traffic "
            "Jesus stands at street level — no "
            "step, no stone to raise him — warm "
            "and still in the lane's low gold, "
            "waiting the small moment it takes "
            "for weariness to notice stillness "
            "— and along the walls the homeward "
            "faces begin to turn, one by one, "
            "toward a man who looks at worn-out "
            "people the way others look at "
            "friends arriving. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r080-b03", "out": "s03-come-unto-me-all-ye.jpeg", "seg": "j1",
        "window": "11.96-17.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LANE", "CARRIER"],
        "narration": (
            "Come unto me, all ye that labour and are heavy laden, and I will "
            "give you rest."
        ),
        "must_show": "SCRIPTURE-EXACT: the offer — Jesus's arms opening to the burdened lane; the loaded listeners — carrier, jar-woman, farmer — caught mid-turn toward the words.",
        "must_not_show": "no halo, glare or rim-light; the arms open to ALL of them — no one singled out, no one excluded by the gesture.",
        "scene": (
            "Jesus's arms open down the length of the lane, the "
            "camera behind the burdened listeners' shoulders — "
            "the gesture wide "
            "enough to take in every bent back "
            "in it — and the burdened turn into "
            "it mid-step: the carrier twisting "
            "under his sack to see, the woman's "
            "jar going still on its hip, the "
            "farmer's mattock stopping mid-drag "
            "— an invitation flung open like a "
            "door at the exact hour every load "
            "on that street weighed its most. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r080-b04", "out": "s04-come-to-me-all-of.jpeg", "seg": "n0c",
        "window": "19.01-24.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["CARRIER"],
        "narration": (
            "Come to me, all of you who are worn out and carrying too much — "
            "and I will give you rest."
        ),
        "must_show": "the offer landing — close on the carrier's lifted face under the sack's rope: rest named out loud to a man who forgot the word existed.",
        "must_not_show": "no halo, glare or rim-light; the load still ON him — hope arriving before relief does.",
        "scene": (
            "Close on the carrier's face lifted "
            "from under his load — the rope "
            "still biting his shoulder, the "
            "sack's whole weight still his — and "
            "in the tired eyes the word REST "
            "landing like rain on a field that "
            "stopped expecting any: not relief "
            "yet, nothing lighter yet, just the "
            "unfamiliar sensation of being "
            "addressed by name in his exhaustion "
            "and offered the one thing he "
            "quit asking for. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r080-b05", "out": "s05-he-does-not-say-come.jpeg", "seg": "n0c",
        "window": "24.64-27.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["CARRIER", "LANE"],
        "narration": "He does not say come once you have it handled.",
        "must_show": "the non-condition — the carrier mid-lane, load fully on, nothing sorted, nothing improved; exactly the state the invitation covers.",
        "must_not_show": "no halo, glare or rim-light; NOTHING tidied about him — dusty, bent, unhandled, and invited anyway.",
        "scene": (
            "The carrier stands mid-lane exactly "
            "as the day left him: sack full and "
            "roped on, tunic sweat-dark down the "
            "spine, dust to the knee, not one "
            "thing about his life handled or "
            "sorted or improved since sunrise — "
            "and it is THIS man, in THIS state, "
            "the invitation was aimed at — no "
            "cleanup required at the door, no "
            "waiting room for the put-together. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r080-b06", "out": "s06-a-yoke-was-the-wooden.jpeg", "seg": "n1",
        "window": "31.86-38.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["OXFIELD"],
        "narration": (
            "A yoke was the wooden beam that let two oxen pull a load "
            "together, so no single animal carried it alone."
        ),
        "must_show": "the yoke explained — the field cutaway: the matched russet oxen side by side under the ONE carved double beam, pulling the plough together; sharing made visible.",
        "must_not_show": "no halo, glare or rim-light; the yoke clearly DOUBLE — two bow-loops, two animals, one beam, one load.",
        "scene": (
            "The cutaway opens on the half-ploughed field, the "
            "camera beside the furrow so team and yoke read in "
            "profile, in the same low "
            "gold: the two russet oxen side by "
            "side under the single carved beam, "
            "its twin bow-loops cradling both "
            "necks, the plough biting dark earth "
            "behind them — one load moving on "
            "two backs, the beam translating "
            "every pound of it into halves — "
            "the whole invention built on a "
            "single idea: nothing pulls alone. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r080-b07", "out": "s07-he-says-come-while-you.jpeg", "seg": "n0c",
        "window": "27.56-30.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LANE", "CARRIER"],
        "narration": "He says come while you are still under it.",
        "must_show": "the coming-while-loaded — the carrier stepping toward Jesus down the lane WITH the sack still roped on his back; the invitation accepted mid-burden.",
        "must_not_show": "no halo, glare or rim-light; the sack STILL ON during the approach — the load and the coming happening together.",
        "scene": (
            "Down the gold lane the carrier "
            "comes — sack still roped high on "
            "his bent back, rope still biting, "
            "every step still costing what steps "
            "have cost all day — walking toward "
            "Jesus not after the load is solved "
            "but UNDER it, the two facts sharing "
            "one man: still heavy laden, and "
            "already coming — while Jesus "
            "watches him approach like the whole "
            "offer was written for exactly this "
            "walk. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r080-b08", "out": "s08-take-my-yoke-upon-you.jpeg", "seg": "j2",
        "window": "39.85-48.16", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LANE"],
        "narration": (
            "Take my yoke upon you, and learn of me; for I am meek and lowly "
            "in heart: and ye shall find rest unto your souls."
        ),
        "must_show": "SCRIPTURE-EXACT: meek and lowly — close on Jesus speaking it gently, face level with his tired listeners; a teacher describing himself truthfully.",
        "must_not_show": "no halo, glare or rim-light; NOTHING lofty in the framing — his face at their level, the meekness in the eyes, not performed.",
        "scene": (
            "Close on Jesus's face at the level "
            "of the tired faces around him — the "
            "warm brown eyes carrying the claim "
            "as plain fact, not performance: "
            "meek, and lowly in heart — a "
            "teacher whose self-description is "
            "the least demanding sentence any of "
            "them has heard from any authority "
            "in years, offered in the tone of a "
            "man holding a door rather than a "
            "man raising a bar. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r080-b09", "out": "s09-for-my-yoke-is-easy.jpeg", "seg": "j3",
        "window": "49.85-52.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LANE", "CARRIER"],
        "narration": "For my yoke is easy, and my burden is light.",
        "must_show": "SCRIPTURE-EXACT: the promise sealed — Jesus's hand resting on the loaded carrier's shoulder, beside the rope; the words given man to man.",
        "must_not_show": "no halo, glare or rim-light; the hand on the SHOULDER, near the rope's bite — the promise touching the exact sore point.",
        "scene": (
            "Jesus's hand comes to rest on the "
            "carrier's shoulder — deliberately, "
            "right beside the rope's worn bite, "
            "on the exact sore inch the sack has "
            "argued with all day — and the "
            "promise passes man to man at "
            "arm's length: easy, and light — "
            "words laid directly onto the place "
            "that has the most reason to "
            "disbelieve them, by the one voice "
            "with the standing to keep them. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r080-b10", "out": "s10-take-my-yoke-on-you.jpeg", "seg": "n1b",
        "window": "54.55-62.80", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CARRIER"],
        "narration": (
            "Take my yoke on you, he said, and learn from me, because I am "
            "gentle and I am humble — and you will find rest for your soul."
        ),
        "must_show": "the rest beginning — close on the carrier's face under Jesus's near, steady one: the day's clench easing out of the jaw and brow; soul-rest starting before the sack moves.",
        "must_not_show": "no halo, glare or rim-light; the sack STILL on his back — the easing internal first, the face unlearning its clench.",
        "scene": (
            "The two faces close in the low "
            "gold: Jesus's steady and near, and "
            "the carrier's slowly unlearning "
            "its day — the jaw's clench letting "
            "go by degrees, the driven-up "
            "shoulders easing though the sack "
            "has not moved an inch — rest "
            "arriving in the only order it ever "
            "truly comes: the soul first, the "
            "load after — a man finding out the "
            "promise starts working before the "
            "weight does. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r080-b11", "out": "s11-he-is-not-handing-you.jpeg", "seg": "n1b",
        "window": "62.80-65.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["OXFIELD"],
        "narration": "He is not handing you a heavier beam.",
        "must_show": "the beam close — the carved double yoke seen near: worn smooth, two bow-loops, one side occupied by the labouring ox, the OTHER LOOP EMPTY and open.",
        "must_not_show": "no halo, glare or rim-light; the empty loop UNMISTAKABLE — an open place at the beam, waiting.",
        "scene": (
            "Close on the carved beam itself in "
            "the field's gold light: old wood "
            "worn satin-smooth by years of "
            "necks, its two bow-loops plain to "
            "see — one filled by the labouring "
            "russet ox, straining alone at the "
            "whole load — and the other loop "
            "standing EMPTY and open beside it, "
            "an unoccupied place at the beam "
            "shaped exactly like the missing "
            "half of the pull. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r080-b12", "out": "s12-he-is-stepping-into-the.jpeg", "seg": "n1b",
        "window": "65.67-70.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["OXFIELD"],
        "narration": (
            "He is stepping into the empty side of the one you are already "
            "pulling."
        ),
        "must_show": "the empty side filled — the second russet ox stepping IN under the open loop beside the tired one; the beam levelling as the load becomes two beasts' work.",
        "must_not_show": "no halo, glare or rim-light; the beam visibly LEVELLING — the tired animal's strain easing as the second shoulder takes its half.",
        "scene": (
            "Across the turned earth the second "
            "russet ox steps in — its neck "
            "sliding under the open bow-loop "
            "beside its straining partner — and "
            "the old beam levels as the load "
            "splits: the tired animal's tremble "
            "easing, the plough resuming its "
            "line through the dark ground, one "
            "impossible pull turned ordinary by "
            "a second shoulder arriving under "
            "the same wood — the whole gospel of "
            "the yoke in one step. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r080-b13", "out": "s13-he-promising-a-life-with.jpeg", "seg": "n2a",
        "window": "71.67-74.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["OXFIELD"],
        "narration": "He wasn't promising a life with nothing to carry.",
        "must_show": "the honest promise — the paired team pulling on across the field: the plough still biting, the load still REAL; work continuing, shared.",
        "must_not_show": "no halo, glare or rim-light; the load NOT vanished — furrow still cutting, muscles still working, the difference partnership not absence.",
        "scene": (
            "The paired team pulls on across "
            "the field in the deepening gold — "
            "the plough still biting its dark "
            "furrow, the beam still bearing real "
            "weight, both russet backs still "
            "working — nothing about the load "
            "abolished, nothing about the field "
            "shortened — only the arithmetic "
            "changed for good: the same acres, "
            "the same pull, and no single "
            "creature alone under any of it. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r080-b14", "out": "s14-he-was-promising-to-get.jpeg", "seg": "n2b",
        "window": "76.48-81.68", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LANE", "CARRIER"],
        "narration": (
            "He was promising to get under the load with you, so it never has "
            "to be carried alone again."
        ),
        "must_show": "the closing image — back in the lane at last light: Jesus walking beside the carrier, one hand up under the grain sack's weight, sharing it between them step for step.",
        "must_not_show": "no halo, glare or rim-light; the sharing REAL — Jesus's hand genuinely bearing weight under the sack, the carrier's back straighter, both walking.",
        "scene": (
            "The lane's last gold holds the "
            "closing picture: Jesus walking "
            "beside the carrier, his near hand "
            "up under the roped grain sack and "
            "honestly bearing its weight, the "
            "carrier's bent spine straightening "
            "by the step as the load becomes a "
            "thing between two backs — the "
            "promise made flesh at the most "
            "ordinary scale there is: a shared "
            "weight, a level beam, a road home "
            "no one walks alone. Every figure "
            "has two arms, two hands and one "
            "head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "LANE": "PLACE-REF/lane.jpeg",  # build-38-persistent-widow v2-r038-b46
}
# === end PLACE-PLATES ===
