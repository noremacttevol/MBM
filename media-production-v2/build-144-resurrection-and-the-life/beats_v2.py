#!/usr/bin/env python3
"""V2 beat map — row 144, build-144-resurrection-and-the-life (John 11:17-44).

COVERAGE: 10 pictures over 45.5 s = 4.6 s/picture (matches the library density).

SCRIPTURE FACTS (John 11 KJV):
  11:17 "he had lain in the grave FOUR DAYS already."
  11:20-27 MARTHA went and met him: "I know that he shall rise again
        in the resurrection at the last day." Jesus: "I AM THE
        RESURRECTION, AND THE LIFE: he that believeth in me, though
        he were dead, yet shall he live: And whosoever liveth and
        believeth in me shall NEVER DIE. Believest thou this?" —
        "Yea, Lord: I believe."
  11:44 "he that was dead CAME FORTH, bound hand and foot with
        graveclothes."

RENDERING LAWS:
  - MARTHA, LAZARUS and the TOMB are ROW 17's — locks byte-identical
    to build-17 (same woman, same brother, same Bethany cave-tomb
    with its wheel-stone); REFS pin Martha to build-16's approved
    frame exactly as row 17 does. Face-board against builds 16/17.
  - Lazarus's coming-forth (b10) follows row 17's canon: bound in
    clean linen graveclothes, walking upright and ALIVE — nothing
    macabre, no decay, ever; the wonder is wholeness.
  - Martha's grief is heavy AND faithful at once (the narration
    says both) — never collapsed, never serene: grief with a spine.
  - Jesus's I AM (b05/b08) is spoken INTO grief — tender gravity,
    the claim made beside a tomb, not a pulpit.
  - The stone is row 17's wheel-slab; b10 shows it ROLLED OPEN in
    its channel.

TIME OF DAY ARC (intentional): one grey-bright overcast afternoon
throughout (a mourning-day light), warming to broken sun exactly at
b10 — the light turns when the dead man walks.

CHANGING CONDITION (kept OUT of the locks): the stone — closed,
then rolled open at b10; the light — grey, then broken-through.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags. MARTHA, LAZARUS and
# TOMB are byte-identical to build-17.
LOCKS = {
    "MARTHA": (
        "MARTHA LOCK: Martha is the same woman in every shot — about "
        "thirty-five, the older sister, strong-boned and capable, broader "
        "through the shoulders, warm olive-brown skin, dark hair bound back "
        "tightly under a practical DARK-OCHRE headcloth with loose strands "
        "stuck to her damp forehead, level dark brows and a direct, "
        "intelligent face. She wears a hard-wearing DEEP RUSSET-BROWN wool "
        "dress with the sleeves pushed back and a work-stained apron-cloth "
        "at her waist (never cream, never white). Her hands are strong and "
        "red from work. Her face is shown clearly and is never shrewish. "
        "HER HAIR IS ALWAYS BOUND UP AND COVERED BY THE DARK-OCHRE "
        "HEADCLOTH — it never hangs loose or flows over her shoulders. Her "
        "skin is WARM OLIVE-BROWN and sun-worked, the same tone in every "
        "shot."
    ),
    "LAZARUS": (
        "LAZARUS LOCK: Lazarus is the same man in every shot — about "
        "thirty, the younger brother, lean and open-faced with deep smile "
        "lines, warm olive-brown skin like his sisters', thick black hair "
        "and a close-trimmed black beard. When clothed and well he wears a "
        "DARK OLIVE-GREEN tunic with a plain sash (never cream, never "
        "white). His face is shown clearly — a man people are glad to sit "
        "beside."
    ),
    "TOMB": (
        "TOMB LOCK: the family tomb outside Bethany — a burial cave cut "
        "into a low limestone hillside, its squared dark doorway reached "
        "by a shallow worn ramp, closed by ONE great round-edged "
        "wheel-like stone slab that rolls in a cut channel across the "
        "mouth, with dry grass, thistle and grey field-stone terracing on "
        "the slope around it and open daylight country beyond. The same "
        "cave, channel, stone and slope throughout."
    ),
}

REF = True

REFS = {
    "MARTHA": "../build-16-mary-martha/assets/s18-martha-martha.jpeg",
}

BEATS = [
    {
        "id": "v2-r144-b01", "out": "s01-lazarus-had-been-in-the.jpeg", "seg": "n0",
        "window": "0.28-2.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": "Lazarus had been in the tomb four days.",
        "must_show": "the four days — the tomb's wheel-stone CLOSED across the dark doorway, mourning stillness on the slope, grey-bright overcast; finality as architecture.",
        "must_not_show": "ABSOLUTE: nothing macabre — the closed stone and the grey light carry all of it.",
        "scene": (
            "Four days is long enough for hope to file its "
            "papers: the great wheel-stone stands rolled shut "
            "in its channel across the cave's dark mouth, dry "
            "grass leaning on the terraced slope, a mourner's "
            "torn ribbon caught on the thistle by the ramp — "
            "the grey-bright overcast pressing evenly on "
            "everything like the fourth day itself — a "
            "doorway that has finished being a doorway, by "
            "every rule the hillside knows. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r144-b02", "out": "s02-his-sister-martha-came-to.jpeg", "seg": "n0",
        "window": "2.47-7.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": (
            "His sister Martha came to Jesus, heavy with grief but still "
            "full of faith."
        ),
        "must_show": "the meeting — Martha coming up the road to Jesus, grief heavy in her frame and faith unbroken in her direct eyes; both at once, with a spine.",
        "must_not_show": "no halo, glare or rim-light on Jesus; Martha NEVER collapsed — grief upright; her headcloth bound per lock.",
        "scene": (
            "She comes to him the way she does everything — "
            "directly: Martha up the Bethany road with her "
            "grief carried like a full jar, shoulders square "
            "under the weight of four days, the strong red-"
            "knuckled hands twisting her apron-cloth once and "
            "then stilled — and in the direct eyes that find "
            "Jesus's face there is everything at the same "
            "time: the ache, the reproach of the delayed, "
            "and underneath it all, unbroken, the faith that "
            "walked her out here to say so. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r144-b03", "out": "s03-she-said-she-believed-her.jpeg", "seg": "n1a",
        "window": "7.99-11.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": "She said she believed her brother would rise again at the last day.",
        "must_show": "the far hope — Martha speaking her last-day faith, one hand gesturing toward the far horizon; a true hope held at a distance.",
        "must_not_show": "no halo, glare or rim-light on Jesus; her faith REAL but aimed far — the horizon gesture the picture.",
        "scene": (
            "Her theology is sound and her hope is far away: "
            "Martha speaks it steadily to him — I KNOW he "
            "shall rise again, at the resurrection, at the "
            "last day — her strong hand moving out toward the "
            "grey horizon as she says it, placing her "
            "brother's rising safely at the far edge of "
            "time — a true hope, correctly filed, stored at "
            "the one distance where it cannot be asked to do "
            "anything about this afternoon. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r144-b04", "out": "s04-jesus-answered-with-a-promise.jpeg", "seg": "n1b",
        "window": "12.32-15.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": "Jesus answered with a promise bigger than the last day.",
        "must_show": "the bigger answer coming — Jesus's face gathering its gravity as he prepares the claim; Martha's far-aimed hope about to be brought near.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the tenderness TOTAL — the claim is for a grieving woman, not a crowd.",
        "scene": (
            "The correction he is about to make is one of "
            "distance, not doctrine: Jesus's face gathers "
            "over Martha's far-off hope with the particular "
            "gravity he keeps for grief — nothing of the "
            "lecture in it, everything of the tide — a "
            "promise assembling behind the deep brown eyes "
            "that will pick up her last-day resurrection "
            "from the horizon where she parked it and set "
            "it down directly in front of her, wearing "
            "sandals, asking to be believed. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r144-b05", "out": "s05-i-am-the-resurrection-and.jpeg", "seg": "j1",
        "window": "16.55-24.35", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": (
            "I am the resurrection, and the life: he that believeth in me, "
            "though he were dead, yet shall he live:"
        ),
        "must_show": "SCRIPTURE-EXACT: the claim into grief — Jesus close before Martha, the I AM spoken directly into her eyes; tomb-side tenderness and total authority in one register.",
        "must_not_show": "no halo, glare or rim-light on Jesus; spoken INTO grief — no pulpit distance; her face receiving it.",
        "scene": (
            "The biggest I AM of them all is said to an "
            "audience of one grieving woman: Jesus close "
            "before Martha on the grey road, his eyes "
            "holding her direct ones — I AM the resurrection "
            "— not at the last day: standing here — AND the "
            "life — the claim arriving into her grief at "
            "conversational distance, tomb-side, tender and "
            "absolute at once, while everything she "
            "correctly believed about the far future "
            "quietly relocates into the man in front of "
            "her. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r144-b06", "out": "s06-not-a-theory-about-life.jpeg", "seg": "n2",
        "window": "25.68-27.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": "Not a theory about life after death.",
        "must_show": "the anti-theory — the closed wheel-stone again, blunt and real; the claim's opponent is THIS, not an idea.",
        "must_not_show": "ABSOLUTE: nothing macabre; the stone's bluntness the whole frame.",
        "scene": (
            "What the claim is up against is not an idea: "
            "the wheel-stone sits shut in its channel, "
            "tonnage and limestone, blunt as arithmetic — "
            "no theory ever rolled one of these, no "
            "doctrine ever needed to — four days of "
            "silence behind it and all the hillside's dry "
            "grass leaning in the grey light — the exact "
            "kind of fact that theories are written to "
            "make peace with, about to meet the one "
            "speaker who never came to make peace with "
            "it. No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r144-b07", "out": "s07-he-said-he-himself-is.jpeg", "seg": "n2",
        "window": "27.53-32.56", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": (
            "He said He Himself is the life — and that trusting Him beats "
            "the grave."
        ),
        "must_show": "the personal claim — Jesus's hand at his own chest before Martha; HIMSELF the life; her face working through the enormity.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the chest gesture exact (the I AM rows' signature).",
        "scene": (
            "The claim keeps its address at his own chest: "
            "Jesus's hand lies flat over his heart as he "
            "says it — HE HIMSELF, not a process, not a "
            "someday — the life, standing in the road, "
            "catching her eyes and holding them — and on "
            "Martha's strong direct face the enormity works "
            "through in real time: the grave four days "
            "behind her shoulder, and in front of her a "
            "man quietly claiming to outrank it, and asking "
            "to be trusted on the spot. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r144-b08", "out": "s08-and-whosoever-liveth-and-believeth.jpeg", "seg": "j2",
        "window": "33.16-36.46", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": "And whosoever liveth and believeth in me shall never die.",
        "must_show": "SCRIPTURE-EXACT: never die — the promise's widest reach spoken gently; Martha held in it; the grey light easing at its edges.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the easing of the light SUBTLE — dawn inside overcast.",
        "scene": (
            "The promise widens until it covers everyone "
            "who will ever grieve: whosoever liveth — the "
            "words gentle and enormous over the grey road — "
            "and believeth in me, shall NEVER die — and "
            "around the two of them the overcast eases a "
            "half-tone at its edges, as if the afternoon "
            "itself were leaning in — a sentence flung "
            "past Martha, past Bethany, past the fourth "
            "day of every tomb there will ever be, and "
            "landing wherever this is being heard. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r144-b09", "out": "s09-believest-thou-this-martha-said.jpeg", "seg": "j2 + n3a",
        "window": "36.46-41.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA"],
        "narration": "Believest thou this? Martha said yes.",
        "must_show": "SCRIPTURE-EXACT: the question and the yes — Jesus's asking face; Martha's answer breaking through the grief: yes — direct, tear-bright, unbroken.",
        "must_not_show": "no halo, glare or rim-light on Jesus; her YES with her whole direct face — grief and faith at once.",
        "scene": (
            "The question comes to her by name and she does "
            "not flinch it: believest thou THIS? — the "
            "asking face close and kind and inescapable — "
            "and Martha answers the way Martha does "
            "everything: directly — yes — the word breaking "
            "up through four days of grief with her chin "
            "level and her eyes tear-bright and steady — "
            "yea, Lord: I believe — a confession with red "
            "knuckles and a bound headcloth, worth every "
            "creed ever written after it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r144-b10", "out": "s10-and-moments-later-her-brother.jpeg", "seg": "n3b",
        "window": "41.95-45.15", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB", "LAZARUS", "MARTHA"],
        "narration": "And moments later, her brother walked out of the tomb.",
        "must_show": "SCRIPTURE-EXACT, row-17 canon — the stone ROLLED OPEN, Lazarus walking OUT upright in clean linen graveclothes, ALIVE; broken sun arriving; Martha's joy; Jesus at the ramp.",
        "must_not_show": "ABSOLUTE: nothing macabre — clean linen, upright walk, whole warm face; the wonder is WHOLENESS; sun breaking exactly now.",
        "scene": (
            "The doorway goes back to being a doorway: the "
            "great wheel-stone stands rolled open in its "
            "channel and out of the dark, upright and "
            "walking, comes Lazarus — clean linen "
            "graveclothes loosening at his arms, the "
            "open-faced smile-lined face warm and ALIVE in "
            "the first broken sunlight of the afternoon — "
            "Martha's cry somewhere between laughter and "
            "weeping as she starts up the ramp, and Jesus "
            "standing calm at its foot: the resurrection "
            "and the life, four days late by every clock "
            "except his own, exactly on time. Every figure "
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
    "TOMB": "PLACE-REF/tomb.jpeg",  # build-37-rich-man-lazarus v2-r037-b45
}
# === end PLACE-PLATES ===
