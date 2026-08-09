#!/usr/bin/env python3
"""V2 beat map — row 119, build-119-fourth-man-in-fire (Daniel 3).

COVERAGE: 35 pictures over 197.6 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Daniel 3 KJV):
  v1    the image of gold, "threescore cubits" high (ninety feet), on
        the PLAIN OF DURA.
  v5-7  "at what time ye hear the sound of the cornet, flute, harp...
        FALL DOWN AND WORSHIP" — a whole plain face-down.
  v15   the dare: "and WHO IS THAT GOD that shall deliver you out of
        my hands?"
  v17-18 the answer: "our God whom we serve IS ABLE to deliver us...
        BUT IF NOT... we will NOT SERVE thy gods."
  v19-21 the furnace heated SEVEN TIMES hotter; the three cast in
        BOUND, in their garments.
  v24-25 the king ASTONIED: "Lo, I see FOUR men LOOSE, WALKING in the
        midst of the fire, and they have no hurt; and the form of the
        fourth is like THE SON OF GOD."
  v26-27 "come forth" — not a hair singed, coats unchanged, "nor the
        SMELL of fire had passed on them."
  v28   the king's own blessing: "Blessed be the God of Shadrach,
        Meshach, and Abednego."

FOURTH-FIGURE RENDERING (the row's hard edge): the fourth man is kept
EXACTLY as mysterious as the king's testimony — a tall FORM walking
with the three inside the flames, robes reading pale through the
fire, the face never resolved (always turned, veiled in brightness,
or at distance). NOT jesus-locked, NOT winged, no ring of light —
"the form of the fourth," and no more. The narration's "whatever else
that fourth figure was" governs the paint.

FIRE: scriptural furnace-fire, fierce and real — but the three are
never shown in pain (they never were); the casting-in is the bound
men at the mouth in the great flare, then unharmed standing within.
Never the word glow.

TIME OF DAY: one hard bright imperial day throughout — sun on gold,
then the furnace's orange roar against it.

CHANGING CONDITION (kept OUT of the locks): the ropes — bound, then
burned away; the count in the fire — three, then FOUR, then three
walking out; the king — furious, astonished, blessing.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream (not in this row).
LOCKS = {
    "KING": (
        "KING LOCK: Nebuchadnezzar is the same man in every shot — "
        "powerfully built, a square oiled black beard, in DEEP "
        "PURPLE robes worked with gold and a high gold crown (never "
        "cream, never white); pride, fury and astonishment by turns, "
        "always imperial."
    ),
    "THREE": (
        "THREE LOCK: Shadrach, Meshach and Abednego are the same "
        "three in every shot — young Hebrew officials, short dark "
        "beards, in matching DEEP BLUE court robes with dark sashes "
        "(never cream, never white); calm, upright, unbowed."
    ),
    "FURNACE": (
        "FURNACE LOCK: the furnace — a great brick smelting kiln "
        "with a wide arched MOUTH, its interior a roaring orange "
        "furnace-light, a stone ramp rising to the opening. The "
        "same kiln, mouth and ramp throughout."
    ),
    "PLAIN": (
        "PLAIN LOCK: the plain of Dura — a vast flat assembly "
        "ground under hard sun, and rising from it the NINETY-FOOT "
        "GOLDEN IMAGE on its stone base, sun-blazing, visible for "
        "miles. The same image and plain throughout."
    ),
}

REF = True

# AUDIO-FIX 2026-08-09 (AUDIO-FIX lane, Machine A `Dev`, $0): STALE-V1 — Cameron's
# "mispronounced bow" complaint (#119) was fixed in make_narration.py:79
# (SPOKEN 'bows'→'boughs', /bau/) and lives in the 2026-07-28 segment mp3s, but
# the shipping V1 mp4 was committed 2026-07-24 (pre-fix). Set this flag so
# v2_assemble renders narration from THIS build's own bow-fixed mp3s instead of
# copying the stale mp4 audio. Nothing re-voiced — the fix already exists in the
# segments. See QC.md 🅿️ RUNNER PARK.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r119-b01", "out": "s01-a-king-built-a-golden.jpeg", "seg": "n1",
        "window": "0.28-7.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["PLAIN", "KING"],
        "narration": (
            "A king built a golden statue ninety feet high and made one "
            "rule: when the music plays, everyone bows."
        ),
        "must_show": "SCRIPTURE-EXACT: the image and the rule — the colossal golden statue blazing on the plain, the king before it with the massed musicians ready; the rule assembled.",
        "must_not_show": "no halo; the statue's SCALE overwhelming — people ant-small at its base.",
        "scene": (
            "The rule stands, the camera looking past the massed "
            "officials' backs, ninety feet "
            "tall in the hard sun: the "
            "golden image blazing on "
            "its stone base above the "
            "vast plain, so huge the "
            "officials at its feet "
            "read as ants — and before "
            "it the king in his purple, "
            "arm raised toward the "
            "massed cornets and harps "
            "and flutes waiting on "
            "their platform — one man's "
            "pride cast in metal at "
            "landscape scale, with a "
            "soundtrack, and a single "
            "rule attached: when the "
            "music plays, every knee "
            "on the plain. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b02", "out": "s02-and-everyone-did-a-whole.jpeg", "seg": "n1",
        "window": "7.83-12.69", "wide": True, "jesus": False, "ref": False,
        "locks": ["PLAIN"],
        "narration": (
            "And everyone did — a whole plain of people face-down in the "
            "dust."
        ),
        "must_show": "SCRIPTURE-EXACT: the mass bow — the plain covered horizon-wide with prostrate thousands, faces down before the golden colossus; conformity as landscape.",
        "must_not_show": "no halo; the bow TOTAL to the horizon — one unbroken carpet of backs.",
        "scene": (
            "The music plays, the camera high above the plain, "
            "and the "
            "plain goes down: thousands "
            "upon thousands face-first "
            "into the dust in one "
            "rolling wave — satraps and "
            "soldiers, scribes and "
            "servants, an empire's "
            "whole administration "
            "flattened before the "
            "blazing gold until the "
            "ground itself seems "
            "carpeted in backs from "
            "the statue's base to the "
            "heat-shimmered horizon — "
            "conformity at imperial "
            "scale, purchased by one "
            "trumpet blast. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b03", "out": "s03-everyone-except-three.jpeg", "seg": "n1",
        "window": "12.69-14.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["PLAIN", "THREE"],
        "narration": "Everyone except three.",
        "must_show": "SCRIPTURE-EXACT: the three standing — amid the horizon-wide carpet of prostrate backs, THREE figures upright in deep blue; the exception visible for miles.",
        "must_not_show": "no halo; their standing CALM — no defiant posturing, simply not bowed.",
        "scene": (
            "In the sea — the camera skimming low across it — "
            "of flattened "
            "backs, three verticals: "
            "Shadrach, Meshach and "
            "Abednego upright in their "
            "deep blue court robes "
            "amid the endless prostrate "
            "plain — not posturing, "
            "not shouting, hands quiet "
            "at their sides, faces "
            "calm under the golden "
            "colossus — just standing, "
            "the way trees stand in "
            "mown grass — an exception "
            "three men wide, visible "
            "from the king's platform, "
            "visible for miles. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b04", "out": "s04-so-they-were-dragged-before.jpeg", "seg": "n2",
        "window": "19.18-26.05", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "THREE"],
        "narration": (
            "So they were dragged before the furious king, who gave them "
            "one last chance, and finished it with a dare."
        ),
        "must_show": "the arraignment — the three marched under guard before the enthroned furious king; his pointed finger, their calm; the last chance being offered.",
        "must_not_show": "no rough violence — firm escort, not beating; the king's fury imperial.",
        "scene": (
            "Before the throne platform — the camera following "
            "behind the guards — "
            "the three are marched in "
            "under guard: soldiers at "
            "their elbows, the deep "
            "blue robes still unbowed "
            "in their lines, and above "
            "them the king with fury "
            "banked behind the oiled "
            "black beard — the pointed "
            "royal finger, the offer "
            "of one last music, one "
            "last chance to fold — "
            "and rising behind the "
            "offer, already loaded, "
            "the dare that will spend "
            "the rest of the chapter "
            "being answered. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b05", "out": "s05-shadrach-meshach-and-abednego-would.jpeg", "seg": "n2",
        "window": "14.87-19.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": (
            "Shadrach, Meshach, and Abednego would not bow to anything but "
            "God."
        ),
        "must_show": "the three named — close on the three calm faces in a row: conviction settled, fear present but ruled; the not-bowing as character.",
        "must_not_show": "no halo; fear ALLOWED on them — courage is fear governed, visible.",
        "scene": (
            "Close on the three faces "
            "the empire cannot bend: "
            "young, beardless-court-"
            "smooth no longer, fear "
            "honest in their eyes — "
            "they know exactly what "
            "furnaces are — and over "
            "the fear, ruling it like "
            "a hand on a rein, the "
            "settled thing: some knees "
            "belong to God alone, and "
            "these are three pairs of "
            "them — conviction worn "
            "quiet, side by side by "
            "side. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r119-b06", "out": "s06-but-if-ye-worship-not.jpeg", "seg": "s315",
        "window": "26.61-35.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "THREE", "FURNACE"],
        "narration": (
            "But if ye worship not, ye shall be cast the same hour into "
            "the midst of a burning fiery furnace; and who is that God "
            "that shall deliver you out of my hands?"
        ),
        "must_show": "SCRIPTURE-EXACT: the threat and the dare — the king's arm flung toward the roaring furnace mouth in the distance, the question hurled at the three; the stakes in one gesture.",
        "must_not_show": "no halo; the furnace VISIBLE and roaring at distance — the threat concrete.",
        "scene": (
            "The threat gets pointed at — the camera past the "
            "three men's backs toward the pointing king: "
            "the king's ringed arm "
            "flung out toward the "
            "great kiln across the "
            "ground, its arched mouth "
            "roaring orange even in "
            "the hard sun — THE SAME "
            "HOUR, into THAT — and "
            "then, leaning down at "
            "the three calm faces, "
            "the dare he will eat "
            "before sundown: AND WHO "
            "IS THAT GOD THAT SHALL "
            "DELIVER YOU OUT OF MY "
            "HANDS — a question asked "
            "in total confidence of "
            "its answer, wrongly. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b07", "out": "s07-bow-or-burn.jpeg", "seg": "n2b",
        "window": "36.82-37.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["FURNACE"],
        "narration": "Bow, or burn.",
        "must_show": "the ultimatum distilled — the furnace mouth close: the roaring orange arch, heat-shimmer bending the air; three words as architecture.",
        "must_not_show": "no one in frame — the mouth alone, the choice made visible.",
        "scene": (
            "Three words, one doorway: "
            "the furnace mouth close "
            "up — the wide brick arch "
            "packed with roaring "
            "orange, heat-shimmer "
            "bending the air above the "
            "stone ramp, the breath "
            "of it pushing out across "
            "the ground like a wall "
            "you can lean on — the "
            "empire's whole theology "
            "reduced to its actual "
            "size: a hot doorway and "
            "a command — bow, or "
            "burn — with the third "
            "option not yet visible "
            "to anyone but heaven. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b08", "out": "s08-and-who-is-this-god.jpeg", "seg": "n2b",
        "window": "37.63-42.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "And who is this God of yours who could possibly get you out "
            "of my hands?"
        ),
        "must_show": "the dare close — the king's confident sneering face, hands spread at his own power; the question at its proudest.",
        "must_not_show": "no halo; the confidence TOTAL — a man who has never yet been answered.",
        "scene": (
            "Close on the proudest "
            "question in Babylon: the "
            "king's face confident to "
            "the last pore, the oiled "
            "beard tilted, both ringed "
            "hands spread at the "
            "obvious — MY hands, which "
            "hold the plain, the "
            "army, the furnace, the "
            "hour of your death — WHO "
            "IS THAT GOD — asked by a "
            "man whose acquaintance "
            "with gods is limited to "
            "the ones he builds — an "
            "education scheduled for "
            "this afternoon. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b09", "out": "s09-the-king-is-going-to.jpeg", "seg": "n2b",
        "window": "43.70-47.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": "The king is going to answer it himself before this is over.",
        "must_show": "the foreshadow — the king's confident profile against the far furnace-light; the question hanging, its answerer unaware.",
        "must_not_show": "no halo; the irony CARRIED by composition — his face, the fire beyond.",
        "scene": (
            "The frame sets up the "
            "chapter's long irony: the "
            "king's confident profile "
            "in the foreground, crown "
            "bright in the sun — and "
            "beyond him, small and "
            "roaring across the "
            "ground, the furnace whose "
            "light will shortly turn "
            "him into the day's chief "
            "witness — the man who "
            "asked WHO IS THAT GOD "
            "standing quite unaware "
            "that he has assigned "
            "himself the answer, "
            "under oath, in front of "
            "his whole court. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b10", "out": "s10-our-god-whom-we-serve.jpeg", "seg": "s317",
        "window": "47.92-55.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE", "KING"],
        "narration": (
            "Our God whom we serve is able to deliver us from the burning "
            "fiery furnace, and he will deliver us out of thine hand, O "
            "king."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — the three answering the throne calmly, the middle one speaking for all: ABLE, and WILL; faith stated to power's face.",
        "must_not_show": "no halo; the calm ABSOLUTE — courtesy kept (O king), courage total.",
        "scene": (
            "The answer comes back "
            "courteous and unbending: "
            "the middle of the three "
            "speaking for all with his "
            "chin level and his voice "
            "even — OUR GOD WHOM WE "
            "SERVE IS ABLE — the "
            "words laid before the "
            "throne like a shield set "
            "down calmly on a table — "
            "AND HE WILL DELIVER US, "
            "O KING — the royal title "
            "kept, the royal theology "
            "declined, in the same "
            "breath, by three men "
            "with a furnace in their "
            "peripheral vision. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b11", "out": "s11-but-if-not-be-it.jpeg", "seg": "s317",
        "window": "55.33-62.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": (
            "But if not, be it known unto thee, O king, that we will not "
            "serve thy gods, nor worship the golden image which thou hast "
            "set up."
        ),
        "must_show": "SCRIPTURE-EXACT: the BUT IF NOT — close on the three faces at the sentence's hinge: rescue surrendered, obedience kept; the bravest conditional ever spoken.",
        "must_not_show": "no halo; the words' WEIGHT on all three faces — no bravado, pure settled will.",
        "scene": (
            "And then the three bravest "
            "words in the book: BUT IF "
            "NOT — the three faces "
            "steady as the sentence "
            "crosses its hinge, every "
            "guarantee laid down on "
            "the far side of it — if "
            "the fire wins, if the "
            "rescue never comes, if "
            "the God who is able "
            "chooses not — BE IT "
            "KNOWN, O KING: still no "
            "bow — obedience unhooked "
            "from outcome entirely, "
            "by three men who mean "
            "it with the furnace "
            "roaring in earshot. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b12", "out": "s12-our-god-can-save-us.jpeg", "seg": "n3",
        "window": "64.37-68.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": "Our God can save us, they said, and we believe he will.",
        "must_show": "the confidence half — the three faces bright with real expectation: deliverance genuinely believed; hope's full weight first.",
        "must_not_show": "no halo; the hope REAL — not resignation dressed up; they expect rescue.",
        "scene": (
            "Close on the half of "
            "faith everyone forgets "
            "they had: real hope — the "
            "three faces genuinely "
            "bright with expectation, "
            "eyes carrying the actual "
            "belief that the God of "
            "their fathers will reach "
            "into Babylon's fire for "
            "them this very hour — no "
            "grim fatalism here, no "
            "martyrs courting the "
            "flame: three men who "
            "would very much like to "
            "live, betting first on "
            "deliverance, and meaning "
            "that too. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b13", "out": "s13-but-if-not-if-he.jpeg", "seg": "n3",
        "window": "68.06-71.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": "But if not — if he does not — we still will not bow.",
        "must_show": "the anyway — the three faces crossing from hope into the deeper thing: allegiance independent of outcome; the still-not settled in their jaws.",
        "must_not_show": "no halo; the transition READABLE — hope kept, contingency released.",
        "scene": (
            "And behind the hope, the "
            "bedrock: the three faces "
            "crossing visibly from "
            "expectation into the "
            "deeper country — IF HE "
            "DOES NOT — the rescue "
            "released from its role "
            "as condition, the jaws "
            "settling, the eyes going "
            "from bright to granite "
            "without losing their "
            "warmth — WE STILL WILL "
            "NOT BOW — allegiance "
            "standing free of outcome "
            "at last, which is the "
            "only place allegiance "
            "ever stands entirely. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b14", "out": "s14-they-did-not-obey-because.jpeg", "seg": "n3",
        "window": "74.96-78.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": "They did not obey because they were promised a rescue.",
        "must_show": "the no-contract — the three's open empty hands at their sides: no bargain held, no terms clutched; obedience without receipt.",
        "must_not_show": "no halo; the hands EMPTY the image — nothing negotiated in them.",
        "scene": (
            "Close on the terms of "
            "their obedience: three "
            "pairs of hands hanging "
            "open and empty at three "
            "blue-robed sides — no "
            "contract clutched in any "
            "of them, no rescue-"
            "receipt, no signed "
            "guarantee of walking "
            "out — the empty-handed "
            "posture of men who "
            "obeyed before the ending "
            "was disclosed and would "
            "have obeyed after — "
            "faith holding nothing, "
            "and held by everything. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b15", "out": "s15-they-obeyed-because-he-is.jpeg", "seg": "n3",
        "window": "78.58-81.32", "wide": True, "jesus": False, "ref": False,
        "locks": ["THREE", "PLAIN"],
        "narration": "They obeyed because he is God either way.",
        "must_show": "the either-way — the three small and upright beneath the vast sky, the golden image and furnace both in the wide frame; allegiance placed above both outcomes.",
        "must_not_show": "no halo; the composition's THIRDS — statue, furnace, and three standing men, sky over all.",
        "scene": (
            "The wide frame — the camera far behind the three "
            "small figures — lays out "
            "the whole board: the "
            "golden image blazing at "
            "one side, the furnace "
            "roaring at the other, "
            "and between the two "
            "empires of threat, three "
            "small upright figures "
            "under the enormous sky — "
            "which arches over statue "
            "and fire and men alike, "
            "vast and unowned by "
            "Babylon — EITHER WAY, "
            "the sky agrees: rescued "
            "or not, he is God, and "
            "the three stand inside "
            "that fact like a "
            "fortress. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b16", "out": "s16-so-the-king-had-the.jpeg", "seg": "n4",
        "window": "81.89-93.62", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "THREE", "FURNACE"],
        "narration": (
            "So the king had the furnace stoked seven times hotter than "
            "ever and had the three cast in, still bound hand and foot — a "
            "fire so fierce no one should have survived a single breath of "
            "it."
        ),
        "must_show": "SCRIPTURE-EXACT: the casting-in — the stoked furnace at white-orange fury, the three bound figures at the mouth's flare being committed to it; the king watching; ferocity total, pain never shown.",
        "must_not_show": "the three's faces CALM at the threshold — no agony ever; the handlers at distance-blur (their fate untold here).",
        "scene": (
            "The furnace is fed, the camera at the ramp's foot "
            "behind the stokers, until "
            "the bricks themselves "
            "shine: stokers heaving "
            "fuel until the arched "
            "mouth roars white-orange "
            "and the ramp stones "
            "smoke — seven times its "
            "fiercest, a fire that "
            "kills at a distance — and "
            "up the ramp into that "
            "flare the three are "
            "committed, bound hand "
            "and foot in their court "
            "robes, calm at the "
            "threshold as the "
            "brightness takes them — "
            "while below, arms "
            "crossed, the king "
            "watches his answer "
            "begin. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r119-b17", "out": "s17-and-that-is-exactly-when.jpeg", "seg": "n5",
        "window": "94.14-97.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["FURNACE"],
        "narration": "And that is exactly when the impossible began.",
        "must_show": "the hinge — the furnace mouth's blinding interior, and within the brightness: shapes where no shapes should stand; the impossible's first glimpse.",
        "must_not_show": "the fourth NOT yet distinct — only the wrongness of standing forms in killing fire.",
        "scene": (
            "The mouth of the fire "
            "shows what fire cannot "
            "contain: deep in the "
            "white-orange blaze where "
            "nothing living should "
            "outlast one breath — "
            "shapes: upright, moving, "
            "unmistakably shapes — the "
            "flame bending around "
            "them like current around "
            "stones — the watching "
            "ground going silent rank "
            "by rank as the "
            "impossible begins to be "
            "visible, and begins, "
            "worse, to be COUNTABLE. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b18", "out": "s18-the-ropes-burned-away-but.jpeg", "seg": "n5",
        "window": "97.19-100.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE", "FURNACE"],
        "narration": "The ropes burned away, but the men did not.",
        "must_show": "SCRIPTURE-EXACT: loosed — within the fire: the bindings falling from the three's wrists as ash and sparks, the men whole; the fire's one permitted meal.",
        "must_not_show": "no pain anywhere — the loosing almost gentle; robes untouched.",
        "scene": (
            "Inside the blaze the fire "
            "is permitted exactly one "
            "meal: the ropes — "
            "charring off the three "
            "pairs of wrists and "
            "ankles in curls of ash "
            "and rising sparks, the "
            "bonds dropping away like "
            "shed husks — while the "
            "wrists themselves, the "
            "robes, the beards, the "
            "men entire stand whole "
            "in the roar — the "
            "furnace discovering its "
            "new appetite: everything "
            "that binds them, and "
            "nothing that is them. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b19", "out": "s19-they-stood-up-inside-the.jpeg", "seg": "n5",
        "window": "100.04-106.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE", "FURNACE"],
        "narration": (
            "They stood up inside the fire, unharmed, not a single thread "
            "of their clothing even scorched."
        ),
        "must_show": "the standing — the three upright and whole within the great blaze, deep blue robes vivid against the orange; ease where death should be.",
        "must_not_show": "no scorching anywhere on them; their posture EASED — wonder, not endurance.",
        "scene": (
            "And then they simply stand "
            "up in it: three men "
            "rising easy inside a "
            "roaring room of flame, "
            "the deep blue of their "
            "court robes vivid and "
            "unscorched against the "
            "white-orange walls of "
            "fire, faces turning to "
            "each other in dawning "
            "wonder — not enduring "
            "the furnace but standing "
            "in it the way you stand "
            "in wind — the deadliest "
            "place in Babylon "
            "converted, around "
            "exactly three bodies, "
            "into weather. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b20", "out": "s20-then-the-king-leapt-up.jpeg", "seg": "n6",
        "window": "106.69-111.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "Then the king leapt up off his seat in astonishment. He had "
            "thrown in three men, bound."
        ),
        "must_show": "SCRIPTURE-EXACT: the king astonied — Nebuchadnezzar surging up off his seat, crown askew, staring at the furnace; imperial composure shattered.",
        "must_not_show": "no halo; the astonishment TOTAL — the proud face undone by counting.",
        "scene": (
            "The throne cannot hold "
            "him: Nebuchadnezzar "
            "surging up off his seat "
            "with the crown knocked "
            "askew, the oiled beard "
            "dropping open, both "
            "ringed hands gripping "
            "the platform rail as he "
            "stares into the blaze — "
            "the man who has watched "
            "a hundred executions "
            "from this chair, on his "
            "feet and counting, "
            "recounting, counting "
            "again — because the "
            "arithmetic coming back "
            "from the fire is wrong "
            "by exactly one. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b21", "out": "s21-and-this-is-what-he.jpeg", "seg": "n6",
        "window": "111.56-115.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": "And this is what he said out loud, in front of his whole court.",
        "must_show": "the testimony coming — the king turned to his court, arm flung back at the fire, the impossible report leaving him; the court frozen.",
        "must_not_show": "no halo; the court's frozen faces around his outburst.",
        "scene": (
            "The report bursts out of "
            "him in front of "
            "everyone: the king wheeled "
            "around to his frozen "
            "court — counsellors, "
            "captains, the officials "
            "who drafted the decree — "
            "his arm flung back at "
            "the roaring mouth, his "
            "voice cracking imperial "
            "protocol wide open — DID "
            "NOT WE CAST THREE MEN "
            "BOUND — the question "
            "hurled at rows of "
            "stunned nodding heads, "
            "clearing the ground for "
            "the sentence no king of "
            "Babylon was ever "
            "supposed to say. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b22", "out": "s22-lo-i-see-four-men.jpeg", "seg": "s325",
        "window": "115.65-123.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE", "FURNACE"],
        "narration": (
            "Lo, I see four men loose, walking in the midst of the fire, "
            "and they have no hurt; and the form of the fourth is like the "
            "Son of God."
        ),
        "must_show": "SCRIPTURE-EXACT: the FOUR — within the blaze: the three in blue walking whole, and WITH them a fourth tall form, robes reading pale through the fire, face never resolved; the count that broke a king.",
        "must_not_show": "ABSOLUTE: the fourth's face NEVER shown or detailed — a form in brightness, turned or veiled in fire-light; no wings, no ring of light, not jesus-locked.",
        "scene": (
            "And there, in the midst of "
            "the fire, the count "
            "stands corrected: the "
            "three in their vivid "
            "blue, walking loose and "
            "easy through the roar — "
            "and WITH them, matching "
            "their pace, a fourth — "
            "taller, robes reading "
            "pale through the "
            "white-orange, its face "
            "lost in the brightness "
            "no matter how the eye "
            "strains — a form, the "
            "king will say, like the "
            "Son of God — walking "
            "the furnace with three "
            "faithful men as if the "
            "fire were a garden "
            "path. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r119-b23", "out": "s23-and-the-fourth-one-the.jpeg", "seg": "n6b",
        "window": "124.70-128.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "FURNACE"],
        "narration": "And the fourth one, the king says, looks like the Son of God.",
        "must_show": "the naming — the king's awed firelit face saying it, eyes fixed on the blaze; the title crossing pagan lips.",
        "must_not_show": "the fourth not in this frame — the WITNESS's face carries it.",
        "scene": (
            "Close on the naming, and "
            "the mouth it comes from: "
            "the king's face firelit "
            "and awed, the pride "
            "burned off it entirely, "
            "eyes fixed into the "
            "blaze at what walks "
            "there — and crossing the "
            "proud pagan lips, "
            "unbriefed by any priest "
            "of his, the title: LIKE "
            "THE SON OF GOD — a man "
            "who an hour ago asked "
            "what god could possibly "
            "interfere, now supplying, "
            "unprompted, the highest "
            "name he can reach for "
            "what he sees. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b24", "out": "s24-the-man-who-gave-the.jpeg", "seg": "n6b",
        "window": "128.46-134.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "The man who gave the order to light that furnace is now the "
            "eyewitness describing what came of it."
        ),
        "must_show": "the converted witness — the king mid-description to his court, hands shaping what he sees; persecutor turned reporter.",
        "must_not_show": "no halo; the description URGENT — a man needing others to confirm his eyes.",
        "scene": (
            "The prosecution becomes "
            "the star witness: the "
            "king mid-description "
            "before his court, hands "
            "shaping the impossible "
            "in the air — four, he "
            "insists, FOUR, loose, "
            "walking, unhurt — his "
            "eyes going back to the "
            "fire between phrases to "
            "recheck what cannot be "
            "checked enough — the "
            "author of the execution "
            "order now its most "
            "urgent reporter, needing "
            "his own counsellors to "
            "tell him his eyes still "
            "work. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r119-b25", "out": "s25-they-were-not-alone-in.jpeg", "seg": "n7",
        "window": "134.97-143.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE", "FURNACE"],
        "narration": (
            "They were not alone in the fire. Whatever else that fourth "
            "figure was, it walked with them, and where it walked the "
            "flames could not touch them."
        ),
        "must_show": "the accompanied — the four walking together deep in the blaze, the fire standing OFF around their path; company as protection made visible.",
        "must_not_show": "ABSOLUTE: the fourth's face unresolved always; the flame-free path around the walkers.",
        "scene": (
            "The theology of the "
            "furnace, painted: four "
            "figures walking together "
            "through the heart of the "
            "roar — and around their "
            "little moving company, "
            "visible as a shape in "
            "the fire itself, the "
            "flames standing OFF: "
            "bending back from the "
            "path they walk the way "
            "grass bends from wind, a "
            "corridor of safety "
            "travelling with the "
            "walkers — not alone: the "
            "whole miracle in two "
            "words, and the pale "
            "faceless fourth the "
            "reason for both of "
            "them. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r119-b26", "out": "s26-god-had-not-kept-them.jpeg", "seg": "n7",
        "window": "143.65-147.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE", "FURNACE"],
        "narration": (
            "God had not kept them out of the furnace — he met them inside "
            "it."
        ),
        "must_show": "the met-inside — close on the three's faces IN the fire: not enduring but accompanied, wonder and peace where agony was scheduled.",
        "must_not_show": "the fourth at frame's edge as pale presence only; the faces at PEACE.",
        "scene": (
            "Close on the faces the "
            "fire was supposed to "
            "end: the three inside "
            "the blaze with an "
            "expression no martyr's "
            "chronicle prepared "
            "anyone for — peace, and "
            "past peace, WONDER — "
            "eyes turned toward the "
            "pale presence at the "
            "frame's bright edge, "
            "walking their walk with "
            "them — the sentence "
            "every sufferer since "
            "has kept in a pocket: "
            "not kept OUT of the "
            "furnace; MET, inside "
            "it — which turned out "
            "to be better. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r119-b27", "out": "s27-shadrach-meshach-and-abednego-ye.jpeg", "seg": "s326",
        "window": "148.10-154.13", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "THREE", "FURNACE"],
        "narration": (
            "Shadrach, Meshach, and Abednego, ye servants of the most high "
            "God, come forth, and come hither."
        ),
        "must_show": "SCRIPTURE-EXACT: the summons out — the king at the furnace mouth's safe distance calling them BY NAME with the new title: SERVANTS OF THE MOST HIGH GOD; the three emerging into the light.",
        "must_not_show": "the fourth not emerging — only the three walk out; the king's posture now reverent.",
        "scene": (
            "The king himself, the camera behind his royal "
            "shoulder at the roaring mouth, comes "
            "down to do the calling: "
            "as near the roaring "
            "mouth as flesh can "
            "stand, hands cupped, "
            "shouting the three names "
            "into the blaze with a "
            "title no decree of his "
            "ever held — SERVANTS OF "
            "THE MOST HIGH GOD — COME "
            "FORTH — and out of the "
            "white-orange the three "
            "come walking, blue robes "
            "vivid, faces calm, "
            "stepping from the heart "
            "of the fire onto the "
            "ramp as easily as men "
            "stepping out of a "
            "doorway — three of them "
            "now, and only three. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b28", "out": "s28-hold-on-to-that-question.jpeg", "seg": "n2b",
        "window": "42.14-43.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["FURNACE"],
        "narration": "Hold on to that question.",
        "must_show": "the question held — the furnace's distant fire under the hard sky: the dare left hanging over the scene, unanswered yet; suspense as landscape.",
        "must_not_show": "no one in frame — the hanging question rendered as the waiting fire.",
        "scene": (
            "The narration pockets the "
            "king's question for "
            "later, and the frame "
            "holds where the answer "
            "will come from: the "
            "furnace across the "
            "ground under the hard "
            "sky, its orange mouth "
            "breathing, patient as an "
            "unopened letter — WHO IS "
            "THAT GOD — the dare "
            "hanging on the hot air "
            "over the plain, waiting "
            "the space of one royal "
            "tantrum to be answered "
            "in person, from inside "
            "the fire. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b29", "out": "s29-the-man-who-demanded-they.jpeg", "seg": "n8",
        "window": "155.63-160.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING"],
        "narration": (
            "The man who demanded they call his statue god is now calling "
            "their God the highest one there is."
        ),
        "must_show": "the reversal — the king's humbled face, the golden image small and irrelevant behind him; MOST HIGH conceded by the statue's own builder.",
        "must_not_show": "no halo; the statue BEHIND and diminished in the composition.",
        "scene": (
            "The frame catches the "
            "great demotion: the king "
            "face-forward and humbled "
            "in the fire's light — and "
            "behind him, back over "
            "his shoulder, his own "
            "ninety feet of gold "
            "standing suddenly "
            "irrelevant against the "
            "sky, a very large "
            "ornament — MOST HIGH, he "
            "has just called the God "
            "of three slaves, and "
            "the word rearranges the "
            "skyline: whatever is "
            "most high, the statue's "
            "own builder just "
            "testified, it is not "
            "the statue. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b30", "out": "s30-and-they-walked-from-the.jpeg", "seg": "n8",
        "window": "160.90-167.88", "wide": True, "jesus": False, "ref": False,
        "locks": ["THREE", "FURNACE", "PLAIN"],
        "narration": (
            "And they walked from the heart of the fire onto solid ground, "
            "alive and whole, in front of everyone who had watched them go "
            "in."
        ),
        "must_show": "the walk-out — the three coming down the ramp whole before the massed witnesses of the plain; the same crowd that watched the casting-in, watching this.",
        "must_not_show": "the crowd's AWE — thousands of faces stunned; the three unmarked.",
        "scene": (
            "Down the smoking ramp — the camera past the front "
            "rank's staring backs — and "
            "onto solid ground they "
            "come, in front of "
            "everybody: the three "
            "walking whole out of the "
            "furnace's roar before "
            "the same massed thousands "
            "who watched them carried "
            "up bound — satraps on "
            "their feet, soldiers "
            "forgetting their "
            "spears, the whole plain "
            "of former bowers staring "
            "at three unmarked men "
            "stepping out of certain "
            "death like passengers "
            "off a ferry — alive, "
            "whole, and witnessed by "
            "an empire. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b31", "out": "s31-the-officials-crowded-around-and.jpeg", "seg": "n9",
        "window": "168.48-178.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": (
            "The officials crowded around and could not believe it. Not a "
            "hair of their heads was singed, their coats were not burned, "
            "and there was not even the smell of fire on them."
        ),
        "must_show": "SCRIPTURE-EXACT: the inspection — officials crowding the three, touching sleeves, lifting hems, sniffing close in disbelief: no singe, no scorch, NO SMELL of fire.",
        "must_not_show": "the inspection ASTONISHED not hostile — the empire's auditors finding nothing.",
        "scene": (
            "The empire audits the "
            "miracle at close range: "
            "officials crowding the "
            "three in a disbelieving "
            "ring — fingers pinching "
            "blue sleeves that should "
            "be ash, palms testing "
            "hair for singe, one "
            "counsellor actually "
            "leaning in to SMELL the "
            "nearest shoulder and "
            "rearing back wide-eyed — "
            "because there is "
            "nothing: no scorch, no "
            "soot, not even the "
            "campfire smell a "
            "bread-oven leaves — the "
            "fire denied down to the "
            "last sense. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b32", "out": "s32-the-fire-had-done-nothing.jpeg", "seg": "n9",
        "window": "178.09-179.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": "The fire had done nothing at all.",
        "must_show": "the nothing — close on one unmarked sleeve-cuff and steady hand: the flame's complete failure in one detail.",
        "must_not_show": "the detail PLAIN — fabric and skin, untouched, in ordinary light.",
        "scene": (
            "Close on the flame's "
            "complete report card: one "
            "deep blue sleeve-cuff in "
            "the plain afternoon "
            "light — the weave "
            "unmarked, the dye "
            "unfaded, the hand below "
            "it steady and whole to "
            "the fingernails — held "
            "up in the ordinary sun "
            "as the sum total of what "
            "seven-times-heated fire "
            "accomplished against a "
            "man who would not bow: "
            "nothing — nothing at "
            "all. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r119-b33", "out": "s33-blessed-be-the-god-of.jpeg", "seg": "s328",
        "window": "180.53-187.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "THREE", "PLAIN"],
        "narration": (
            "Blessed be the God of Shadrach, Meshach, and Abednego, who "
            "hath sent his angel, and delivered his servants that trusted "
            "in him."
        ),
        "must_show": "SCRIPTURE-EXACT: the king's blessing — Nebuchadnezzar before the plain proclaiming it, arm toward the three; the dare's answer given by its asker.",
        "must_not_show": "no halo; the proclamation PUBLIC — the whole assembly hearing the new theology.",
        "scene": (
            "The proudest voice, the camera taking the massed "
            "plain from the side, in the "
            "world blesses somebody "
            "else's God: the king "
            "before the massed plain "
            "with his arm out at the "
            "three unburned men — "
            "BLESSED BE THE GOD OF "
            "SHADRACH, MESHACH, AND "
            "ABEDNEGO — the words "
            "rolling over the same "
            "ground his music ruled "
            "at morning — WHO HATH "
            "SENT HIS ANGEL, AND "
            "DELIVERED HIS SERVANTS — "
            "the dare of the day "
            "answered at last, out "
            "loud, in full assembly, "
            "by the very mouth that "
            "made it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r119-b34", "out": "s34-that-is-one-of-the.jpeg", "seg": "n3",
        "window": "71.54-74.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["THREE"],
        "narration": "That is one of the bravest things anyone ever said.",
        "must_show": "the bravery weighed — the three's quiet faces held a beat after the BUT IF NOT: the sentence's cost and grandeur resting on them.",
        "must_not_show": "no halo; the stillness the tribute — courage at rest after speaking.",
        "scene": (
            "The frame holds still a "
            "beat to let the sentence "
            "weigh: the three quiet "
            "faces just after BUT IF "
            "NOT has left them — no "
            "trumpets marking it, no "
            "chorus, just three men "
            "standing inside the "
            "words they cannot take "
            "back and would not — "
            "the bravest conditional "
            "in scripture settling "
            "over its speakers like "
            "a mantle, worn plainly, "
            "in front of a king and "
            "a furnace and God. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r119-b35", "out": "s35-that-is-the-same-man.jpeg", "seg": "n10",
        "window": "189.06-197.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["KING", "THREE", "FURNACE", "PLAIN"],
        "narration": (
            "That is the same man who asked, an hour earlier, who is that "
            "God that shall deliver you out of my hands. He got his answer, "
            "and he said it himself."
        ),
        "must_show": "the closing image — the whole scene at rest: the cooling furnace, the humbled king, the three whole in the late light, the golden image ignored behind; the answered dare as landscape.",
        "must_not_show": "no halo; the statue UNATTENDED in the background — the day's true center shifted for good.",
        "scene": (
            "The closing frame surveys "
            "the day the dare came "
            "home: the furnace "
            "cooling its empty roar "
            "behind them, the three "
            "standing whole and "
            "unsinged in the long "
            "late light, the king "
            "humbled and alive with "
            "new theology — and "
            "behind it all, still "
            "ninety feet tall and "
            "suddenly nobody's god, "
            "the golden image, "
            "unbowed-to and "
            "unattended — WHO IS THAT "
            "GOD, the morning asked; "
            "the evening answers in "
            "the asker's own words, "
            "and means them. Every "
            "figure has two arms, two "
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
    # PLAIN: build-38 auto-match REJECTED (village doorway frame, not the
    # plain of Dura with the golden colossus) — promote-first from b01.
}
# === end PLACE-PLATES ===
