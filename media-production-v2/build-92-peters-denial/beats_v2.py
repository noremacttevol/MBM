#!/usr/bin/env python3
"""V2 beat map — row 92, build-92-peters-denial (Luke 22:54-62).

COVERAGE: 10 pictures over 45.1 s = 4.5 s/picture (a short, tight row).

SCRIPTURE FACTS (Luke 22:54-62 KJV):
  v54   "they took him... into the HIGH PRIEST'S HOUSE. And Peter
        followed AFAR OFF."
  v55   "when they had KINDLED A FIRE in the midst of the hall, and
        were set down together, Peter sat down among them." — a night
        courtyard, a shared fire, strangers' faces.
  v56-57 a SERVANT MAID, "earnestly looked upon him": "This man was
        also with him." — "Woman, I know him not."
  v58-60 a second, then a THIRD accusation about "an hour after";
        each denial harder; "while he YET SPAKE, THE COCK CREW."
  v61   "And the Lord TURNED, and LOOKED UPON PETER." — across the
        courtyard, in custody; the look that breaks him.
  v62   "And Peter went out, and WEPT BITTERLY."

TIME OF DAY: deep NIGHT into first cold greyness — firelit courtyard
throughout; the rooster and the look at the night's coldest hour.
Correct story darkness, not the row-11 defect.

CONTENT-CARE: no flags. Jesus is IN CUSTODY here — shown under escort
at a distance, hands bound with rope at most, NO beating, bruising or
violence anywhere (the trial's abuse is off-screen territory). Peter's
collapse rendered with dignity — fear, not villainy; the closing beats
carry the mercy IN the text: the look is love, not scorn.

CHANGING CONDITION (kept OUT of the locks): the accusations — one,
then another, then the third; Peter's denial — uneasy, then harder,
then vehement; the night — deep dark toward cold grey; the rooster.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER comes from the shared CAST_LOCKS.
LOCKS = {
    "YARD": (
        "YARD LOCK: the high priest's courtyard at night — a paved "
        "court inside high stone walls, one open FIRE burning in the "
        "midst with servants and guards ringed close for warmth, a "
        "colonnaded porch along the far side, an arched gate to the "
        "street. The same fire, walls and porch throughout."
    ),
    "MAID": (
        "MAID LOCK: the servant girl is the same in every shot — "
        "about sixteen, quick dark eyes, dark hair under a DARK "
        "MADDER-RED head cloth, a plain DARK MADDER-RED dress (never "
        "cream, never white); sharp-sighted, not cruel."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r092-b01", "out": "s01-after-they-arrested-jesus-peter.jpeg", "seg": "n0",
        "window": "0.28-7.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["YARD", "PETER"],
        "narration": (
            "After they arrested Jesus, Peter followed at a distance and "
            "warmed himself by a fire in the courtyard, trying not to be "
            "noticed."
        ),
        "must_show": "SCRIPTURE-EXACT: the fire in the midst — the night courtyard: servants and guards ringed at the flames, and Peter among them with his mantle pulled high, angled away, hiding in plain sight.",
        "must_not_show": "no halo, glare or rim-light; Peter VISIBLY hiding — hood up, shoulders in, face angled from the light.",
        "scene": (
            "The high walls hold the cold "
            "night in and one fire against "
            "it: servants and off-watch "
            "guards ringed close at the "
            "flames, hands out, faces "
            "orange in the firelight — and "
            "among them, mantle dragged "
            "high and shoulders folded "
            "small, the big fisherman "
            "trying to be nobody: angled "
            "half away from the light, "
            "warming hands he cannot keep "
            "still, the worst seat in the "
            "world chosen because leaving "
            "was worse. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r092-b02", "out": "s02-a-servant-girl-looked-at.jpeg", "seg": "n1",
        "window": "8.14-11.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["YARD", "MAID", "PETER"],
        "narration": "A servant girl looked at him and said, this man was with him too.",
        "must_show": "SCRIPTURE-EXACT: the earnest look — the maid across the fire, eyes locked on Peter's firelit face, her finger beginning to lift; recognition landing in public.",
        "must_not_show": "no halo, glare or rim-light; the maid's look KEEN, not malicious — she is simply right.",
        "scene": (
            "Across the flames the young "
            "maid's quick dark eyes stop on "
            "him and stay: firelight full "
            "on Peter's face for one "
            "unlucky moment, her head "
            "tilting as memory catches, "
            "and the finger already "
            "lifting — THIS MAN WAS WITH "
            "HIM TOO — said clear across "
            "the fire-ring to everyone "
            "warming there, the words "
            "turning helmeted heads one "
            "by one toward the fisherman "
            "trying to be stone. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r092-b03", "out": "s03-peter-said-woman-i-know.jpeg", "seg": "n1",
        "window": "11.89-14.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Peter said, woman, I don't know him.",
        "must_show": "SCRIPTURE-EXACT: the first denial — close on Peter's firelit face saying it: the lie costing him visibly, eyes sliding away from hers.",
        "must_not_show": "no halo, glare or rim-light; the fear HONEST — a brave man's first crack, not a coward's ease.",
        "scene": (
            "Close on the first crack in "
            "the rock: Peter's face in the "
            "firelight shaping the lie — "
            "WOMAN, I KNOW HIM NOT — the "
            "eyes sliding off hers and "
            "into the flames as he says "
            "it, the jaw too tight, the "
            "voice pitched too casual — a "
            "man who swung a sword in the "
            "garden three hours ago, "
            "discovering what a "
            "sixteen-year-old's question "
            "can do to courage at a "
            "fireside. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r092-b04", "out": "s04-a-little-later-someone-else.jpeg", "seg": "n2",
        "window": "14.80-17.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["YARD", "PETER"],
        "narration": "A little later, someone else. Then a third.",
        "must_show": "the accusations multiplying — the fire-ring: a guard pointing at Peter from one side, another man leaning in from the other; the net visibly tightening.",
        "must_not_show": "no halo, glare or rim-light; the ring CLOSING — bodies angled toward him, no escape lane in the composition.",
        "scene": (
            "The net draws in around the "
            "fire: from one side a guard's "
            "arm comes up pointing — you "
            "are one of them — from the "
            "other a servant leans in "
            "certain of the Galilean burr "
            "in his voice, and the ring "
            "of firelit faces tightens by "
            "a body's width all around, "
            "every angle of the courtyard "
            "closing toward the one man "
            "with nowhere left to angle "
            "his face. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r092-b05", "out": "s05-each-time-peter-denied-it.jpeg", "seg": "n2",
        "window": "17.37-21.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": (
            "Each time Peter denied it harder — I don't know what you're "
            "talking about."
        ),
        "must_show": "SCRIPTURE-EXACT: the third denial at full pitch — Peter on his feet, arm slashing the air, face desperate and loud; the denial at its hardest.",
        "must_not_show": "no halo, glare or rim-light; the vehemence FEAR-DRIVEN — panic in the eyes above the shouting mouth.",
        "scene": (
            "The third denial comes up "
            "shouting: Peter on his feet "
            "with his arm slashing the "
            "accusation out of the air — I "
            "DO NOT KNOW WHAT YOU ARE "
            "TALKING ABOUT — the voice too "
            "loud for the lie it carries, "
            "the firelight catching pure "
            "panic in the eyes above the "
            "roaring mouth — a man "
            "burying the truth under "
            "volume, and hearing, under "
            "his own last word, the first "
            "note of a rooster. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r092-b06", "out": "s06-and-right-then-while-the.jpeg", "seg": "n3",
        "window": "22.25-26.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["YARD", "PETER"],
        "narration": (
            "And right then, while the words were still in his mouth, a "
            "rooster crowed."
        ),
        "must_show": "SCRIPTURE-EXACT: the cock crew — the courtyard at the sound: Peter frozen mid-gesture, faces half-turned; on the wall's top edge against the first grey, a rooster mid-crow.",
        "must_not_show": "no halo, glare or rim-light; Peter STOPPED DEAD — the sound hitting him like a physical blow.",
        "scene": (
            "The sound tears the night "
            "open: on the wall's top edge "
            "against the first cold grey "
            "of morning a rooster stands "
            "mid-crow, throat stretched — "
            "and below in the courtyard "
            "Peter stops dead with the "
            "denial still hanging in the "
            "air, his slashing arm frozen "
            "half-lowered, his face "
            "emptying as three months of "
            "warnings and three hours of "
            "lies arrive at his ears in "
            "one bird's cry. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r092-b07", "out": "s07-across-the-courtyard-jesus-turned.jpeg", "seg": "n4",
        "window": "26.73-31.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["YARD", "PETER"],
        "narration": (
            "Across the courtyard, Jesus turned and looked straight at "
            "Peter. Just looked at him."
        ),
        "must_show": "SCRIPTURE-EXACT: the Lord turned and looked — across the yard: Jesus under guard on the porch, hands bound with rope, turning his head; the look crossing the whole firelit space to Peter.",
        "must_not_show": "ABSOLUTE: no wounds, bruises or beating on Jesus — custody by rope and escort only; the look GENTLE, never accusing.",
        "scene": (
            "Across the whole firelit yard "
            "the moment happens in "
            "silence: on the far porch, "
            "between his guards, Jesus — "
            "hands bound before him with "
            "plain rope — turns his head, "
            "and finds Peter's face over "
            "the fire and the crowd and "
            "the distance as surely as if "
            "the courtyard were empty — "
            "one look, travelling the "
            "cold air between them, "
            "carrying nothing in it that "
            "Peter braced for. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r092-b08", "out": "s08-and-peter-remembered-jesus-had.jpeg", "seg": "n5a",
        "window": "31.84-35.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "And Peter remembered — Jesus had told him this would happen.",
        "must_show": "the remembering — close on Peter's stricken face as the prophecy lands: before-the-cock-crows surfacing whole; the collapse beginning behind the eyes.",
        "must_not_show": "no halo, glare or rim-light; the memory VISIBLE as devastation — recognition, not confusion.",
        "scene": (
            "Close on the memory arriving "
            "like a wave over a wall: "
            "Peter's stricken firelit face "
            "as the supper-table sentence "
            "surfaces word for word — "
            "BEFORE THE COCK CROW, THOU "
            "SHALT DENY ME THRICE — his "
            "own confident answer "
            "surfacing after it, and the "
            "count, one-two-three, "
            "completing itself behind his "
            "eyes while the rooster's cry "
            "still rings off the stone. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r092-b09", "out": "s09-he-went-outside-and-wept.jpeg", "seg": "n5b + n5c",
        "window": "35.85-39.79", "wide": True, "jesus": False, "ref": False,
        "locks": ["YARD", "PETER"],
        "narration": "He went outside and wept bitterly. But the look wasn't scorn.",
        "must_show": "SCRIPTURE-EXACT: went out and wept — Peter stumbling out through the arched gate into the grey street, breaking as he goes; the fire and the yard left behind.",
        "must_not_show": "no halo, glare or rim-light; the weeping BITTER and real — a big man coming apart, dignity kept by honesty.",
        "scene": (
            "He cannot stay inside it: "
            "Peter shoulders blind through "
            "the arched gate into the cold "
            "grey street, one hand "
            "dragging along the stone for "
            "balance as the breaking "
            "arrives — the big frame "
            "buckling against the outside "
            "wall, face in his hands, the "
            "sobs coming up from somewhere "
            "below the sea — a man who "
            "held against storms and "
            "swords, wrecked completely by "
            "one look and one bird. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r092-b10", "out": "s10-it-was-the-face-of.jpeg", "seg": "n5c",
        "window": "39.79-44.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["YARD"],
        "narration": (
            "It was the face of someone who already knew, and already loved "
            "him anyway."
        ),
        "must_show": "the closing image — close on the look itself remembered: Jesus's bound-handed figure and his face across the firelight, full of knowing love, no scorn anywhere in it.",
        "must_not_show": "ABSOLUTE: no wounds or bruises; no scorn, no disappointment-theatre — foreknowledge and love in one steady face.",
        "scene": (
            "The closing frame keeps the "
            "look Peter kept for the rest "
            "of his life: Jesus's face "
            "across the dying firelight — "
            "rope at his wrists, guards at "
            "his shoulders — and in the "
            "warm brown eyes nothing of "
            "the scorn a traitor braces "
            "for: only the steady, "
            "unsurprised love of someone "
            "who counted all three "
            "denials before they were "
            "spoken and paid for them "
            "anyway — the face that made "
            "the weeping bitter, and the "
            "restoration certain. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
]
