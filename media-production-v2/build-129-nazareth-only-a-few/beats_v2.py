#!/usr/bin/env python3
"""V2 beat map — row 129, build-129-nazareth-only-a-few (Mark 6:1-6).

COVERAGE: 14 pictures over 78.2 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 6 KJV):
  6:1   "he went out from thence, and came into HIS OWN COUNTRY; and
        his disciples follow him."
  6:2   "he began to TEACH IN THE SYNAGOGUE: and many hearing him
        were astonished."
  6:3   "Is not this THE CARPENTER, the son of Mary, the brother of
        James, and Joses, and of Juda, and Simon? and are not his
        sisters here with us? And they were OFFENDED at him."
  6:4   "A PROPHET IS NOT WITHOUT HONOUR, but in his own country,
        and among his own kin, and in his own house."
  6:5   "And he COULD THERE DO NO MIGHTY WORK, save that he laid his
        hands upon A FEW SICK FOLK, and healed them."
  6:6   "And he MARVELLED because of their unbelief."

RENDERING LAWS:
  - MARY AND THE FAMILY ARE NEVER DEPICTED — the murmurers NAME them
    (b02/b03) but no render shows Mary, brothers or sisters (the
    three-Marys law stays untriggered; the townsfolk carry the
    scene).
  - The townsfolk are NOT villains: familiar, ordinary neighbours
    whose failure is FAMILIARITY — they knew the boy, so they cannot
    see the prophet. Skeptical, folded, dismissive — never jeering.
  - The healing beats (b10-b13) are the row's heart: "a few sick
    folk" = THREE sick people, the same three across the beats
    (counts law); illness with dignity (row-15 class) — warm skin,
    weariness and fever told by posture, no gore.
  - The unbelief is rendered ARCHITECTURALLY where possible: closed
    doors and shuttered windows (b09) answered by the ONE open door
    (b14) — the door rhyme is the row's frame.
  - Jesus's "marvel" (b11) is wonder-with-sadness — never contempt.

TIME OF DAY ARC (intentional): arrival and synagogue in clear
morning light; the cold-shoulder lane beats under flat bright noon;
the healings in warm afternoon gold; the open-door close at early
evening lamplight BY DESIGN.

CHANGING CONDITION (kept OUT of the locks): the doors of the lane —
shut through the unbelief beats, ONE standing open at the close;
the three sick folk — laid low, then healed and risen.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "NAZARETH": (
        "NAZARETH LOCK: Nazareth — a small hill town of pale "
        "stone-and-mudbrick houses stacked along narrow lanes, "
        "wooden doors and small shuttered windows, olive slopes "
        "rising behind the rooflines. The same lanes and skyline "
        "throughout."
    ),
    "SYNAGOGUE": (
        "SYNAGOGUE LOCK: the Nazareth synagogue — a modest "
        "single-room stone synagogue with plain benches along the "
        "walls, a small wooden reading stand, one high window "
        "throwing morning light. The same room throughout."
    ),
    "TOWNSFOLK": (
        "TOWNSFOLK LOCK: the townsfolk — ordinary Nazareth "
        "neighbours: weathered builders and farmers, wives with "
        "market baskets, a few grey elders; earth-toned working "
        "clothes of brown, rust and olive (no cream — only Jesus "
        "wears cream); familiar, skeptical, folded — never jeering "
        "villains. Varied faces, never uniform."
    ),
    "SICKFEW": (
        "SICKFEW LOCK: the few sick folk — THREE people, the same "
        "three in every shot: an old fevered woman wrapped in a "
        "dark shawl, a gaunt younger man on a pallet, and a stooped "
        "grey elder with a bound knee; warm living skin under their "
        "weariness (never corpse-grey), dark worn clothes, full "
        "dignity."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r129-b01", "out": "s01-jesus-went-back-to-nazareth.jpeg", "seg": "n0",
        "window": "0.28-3.48", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NAZARETH"],
        "narration": "Jesus went back to Nazareth, the town that watched Him grow up.",
        "must_show": "the homecoming — Jesus walking up the familiar lane into Nazareth, the stacked pale houses of his boyhood around him; recognition in the town's very stones.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION — walking INTO the town, camera behind him.",
        "scene": (
            "The hometown takes him back up its oldest lane, the "
            "camera following behind him as he climbs: Jesus "
            "walking into Nazareth past the pale stacked houses "
            "he grew up among — the well he drew from, the "
            "doorways that watched him carry lumber, the olive "
            "slopes above the rooflines exactly where he left "
            "them — every stone of the town familiar with the "
            "carpenter's tread, and none of it prepared for who "
            "is actually arriving. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r129-b02", "out": "s02-is-not-this-the-carpenter.jpeg", "seg": "s3",
        "window": "6.06-12.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": (
            "Is not this the carpenter, the son of Mary, the brother of "
            "James, and Joses, and of Juda, and Simon?"
        ),
        "must_show": "SCRIPTURE-EXACT: the murmuring — townsfolk on the synagogue benches leaning head to head, one gesturing toward the unseen speaker; the carpenter being catalogued by his relatives. Mary and family NEVER depicted.",
        "must_not_show": "ABSOLUTE: no Mary, no brothers, no sisters in frame — the naming is spoken only; the murmurers familiar, not jeering.",
        "scene": (
            "The résumé gets read out in whispers: along the "
            "synagogue benches the neighbours lean head to "
            "head, one builder's thick hand tipping toward the "
            "reading stand beyond the frame — is not this the "
            "CARPENTER? — the catalogue of his ordinary "
            "credentials passing down the row, mother named, "
            "brothers named, the whole family ledger produced "
            "from memory by people who have known every entry "
            "since it was born — familiarity doing what "
            "familiarity does to wonder. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r129-b03", "out": "s03-and-are-not-his-sisters.jpeg", "seg": "s3",
        "window": "12.27-14.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": "and are not his sisters here with us?",
        "must_show": "the clincher murmur — a wife's knowing nod toward the town beyond the door, an elder's shrug; the argument-from-familiarity completing itself. No family depicted.",
        "must_not_show": "ABSOLUTE: no sisters in frame — the nod aims at the town generally; the tone certain, not cruel.",
        "scene": (
            "The clincher is delivered with a nod at the whole "
            "town: a market-wife tips her head knowingly "
            "toward the door and the lanes beyond it — his "
            "sisters are HERE, the nod says, ordinary as "
            "washing-day — and beside her a grey elder gives "
            "the small shrug of a man closing a case: we know "
            "the house, we know the family, we know the boy — "
            "the town's whole intimate knowledge of him "
            "assembled into the one thing that will keep them "
            "from knowing him at all. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r129-b04", "out": "s04-but-the-people-known-him.jpeg", "seg": "n1",
        "window": "16.38-23.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": (
            "But the people who'd known Him as a boy couldn't believe. They "
            "took offense at Him — and their unbelief became a wall."
        ),
        "must_show": "the wall forming — the bench rows closing: arms folding, shoulders turning, faces shuttering one by one; unbelief as body language, a human wall.",
        "must_not_show": "no halo; no jeering, no shouting — the closing QUIET; a row of folded arms and turned shoulders.",
        "scene": (
            "The wall goes up without one stone: along the "
            "benches the arms fold one after another, "
            "shoulders angling away, chins settling, faces "
            "shuttering like the lane's small windows at dusk "
            "— no shout anywhere, no scene — just a "
            "congregation of people who watched a boy grow up "
            "quietly deciding, body by body, that nothing more "
            "than a boy could have grown — offense taken in "
            "silence and masonried, arm over folded arm, into "
            "a wall. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r129-b05", "out": "s05-a-prophet-is-not-without.jpeg", "seg": "jv4",
        "window": "23.77-30.92", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE"],
        "narration": (
            "A prophet is not without honour, but in his own country, and "
            "among his own kin, and in his own house."
        ),
        "must_show": "SCRIPTURE-EXACT: the saying — Jesus at the reading stand speaking it calm and sad, the old truth landing in his own hometown synagogue.",
        "must_not_show": "no halo, glare or rim-light on Jesus; sadness WITHOUT bitterness — a truth observed, not a wound displayed.",
        "scene": (
            "The oldest saying about hometowns is spoken inside "
            "one: Jesus at the small wooden reading stand, the "
            "high window's morning light on him, saying the "
            "sentence calm and level with the sadness folded "
            "in underneath — honour everywhere, except here; "
            "except among these; except home — not an "
            "accusation, barely even a complaint: a man naming "
            "a law of human eyes to the exact room that is, at "
            "this moment, demonstrating it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r129-b06", "out": "s06-he-taught-in-the-synagogue.jpeg", "seg": "n0",
        "window": "3.48-5.39", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": "He taught in the synagogue.",
        "must_show": "the teaching — Jesus at the stand mid-teaching, the hometown congregation on the benches, some faces briefly astonished before the doubt sets in.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a few faces genuinely ASTONISHED (per Mark 6:2) before the wall.",
        "scene": (
            "For a few sentences it almost happens: Jesus "
            "teaching from the little stand with the morning "
            "light behind him, and along the benches the "
            "hometown faces caught in honest astonishment — "
            "brows up, a builder leaning forward despite "
            "himself, an elder's mouth open around whence hath "
            "this man these things — the wonder arriving first "
            "the way it arrived everywhere else, one breath "
            "ahead of the doubt already reaching for it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r129-b07", "out": "s07-a-prophet-gets-honored-everywhere.jpeg", "seg": "n1b",
        "window": "32.44-38.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE", "TOWNSFOLK"],
        "narration": (
            "A prophet gets honored everywhere, He said — everywhere except "
            "home. Except among his own relatives."
        ),
        "must_show": "the exception illustrated — through the synagogue's open door the bright road OUT of town (where crowds honored him), against the cold folded benches inside; everywhere vs here in one frame.",
        "must_not_show": "no halo; the composition's two zones CLEAR — bright open road out the door, shuttered faces within.",
        "scene": (
            "The exception has a floor plan: through the "
            "synagogue's open door the road out of town runs "
            "bright and open toward the rest of the country — "
            "the everywhere that thronged him, pressed him, "
            "lowered its sick through roofs to reach him — "
            "while inside, in the cool of the one room that "
            "raised him, the benches hold their folded arms "
            "and settled chins — the whole world's welcome "
            "visible out one door, and home seated with its "
            "back to it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r129-b08", "out": "s08-except-in-his-own-house.jpeg", "seg": "n1b + n2",
        "window": "38.49-43.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NAZARETH"],
        "narration": "Except in his own house. He could do only a few mighty works there.",
        "must_show": "the quiet street — Jesus standing in a near-empty Nazareth lane at flat noon, hands at his sides, the town going about its business around him unasking.",
        "must_not_show": "no halo, glare or rim-light on Jesus; nobody approaching him — the emptiness around him the picture.",
        "scene": (
            "The mightiest hands in Galilee stand idle in a "
            "noon lane: Jesus alone in the flat bright street "
            "of his own town, hands at his sides, while "
            "Nazareth flows incuriously around him — a woman "
            "passing with her jars without a glance, a builder "
            "hauling timber the way the carpenter's son once "
            "did, doors shut on their own affairs — nobody "
            "asking, nobody bringing, nobody reaching — the "
            "power present and entirely unemployed, for the "
            "only reason it ever goes unemployed. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r129-b09", "out": "s09-not-because-his-power-ran.jpeg", "seg": "n2",
        "window": "43.65-48.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAZARETH"],
        "narration": (
            "Not because His power ran out, but because they wouldn't "
            "receive it."
        ),
        "must_show": "unbelief as architecture — the lane of CLOSED doors and shuttered windows in flat light; the refusal built into the street itself.",
        "must_not_show": "no halo; every door SHUT, every shutter closed — no people needed; the wall in wood and stone.",
        "scene": (
            "The refusal has a streetscape: down the narrow "
            "lane every wooden door stands shut and every "
            "small window holds its shutters closed against "
            "the flat noon — latch after latch, lane's length, "
            "a town's worth of thresholds bolted not against "
            "weather or thieves but against a gift — nothing "
            "ran out, nothing failed; the water was at every "
            "door and the doors were the drought. No people "
            "are needed in this frame."
        ),
    },
    {
        "id": "v2-r129-b10", "out": "s10-and-he-could-there-do.jpeg", "seg": "s1",
        "window": "49.02-55.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NAZARETH", "SICKFEW"],
        "narration": (
            "And he could there do no mighty work, save that he laid his "
            "hands upon a few sick folk, and healed them."
        ),
        "must_show": "SCRIPTURE-EXACT: the exception — Jesus laying both hands gently on the old fevered woman, the other two sick nearby awaiting; the healing tender and real in the warm afternoon.",
        "must_not_show": "no halo, glare or rim-light on Jesus; exactly THREE sick folk; illness with dignity — warm skin, no gore.",
        "scene": (
            "The exception to the drought is small and it is "
            "everything: in a warm afternoon courtyard Jesus "
            "kneels with both hands laid gently on the old "
            "fevered woman's shawled head, her face already "
            "easing under them — while nearby the gaunt young "
            "man waits on his pallet and the stooped elder "
            "leans on his stick, the whole of Nazareth's asking "
            "gathered into three worn bodies — no mighty works "
            "for the town, and every ounce of the mercy for "
            "the few who came. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r129-b11", "out": "s11-and-he-marvelled-because-of.jpeg", "seg": "s1 + n3",
        "window": "55.09-62.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NAZARETH", "SICKFEW"],
        "narration": (
            "And he marvelled because of their unbelief. Even amazement at "
            "their doubt didn't stop His mercy."
        ),
        "must_show": "SCRIPTURE-EXACT: the marvel — close on Jesus's face carrying genuine wonder-with-sadness at the town's unbelief, while behind him the healed woman sits UP, restored.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the marvel is WONDER and sorrow, never contempt; the healed woman visibly risen.",
        "scene": (
            "The only thing recorded to have amazed him twice "
            "was faith — and this is the other kind: close on "
            "Jesus's face turned toward the shuttered town, "
            "carrying genuine marvel — the wonder of a man "
            "confronted with a mystery, and the mystery is "
            "doubt — sadness folded through the amazement — "
            "while behind his shoulder the old woman he has "
            "just healed sits up straight in the warm light, "
            "proof that the amazement never once slowed his "
            "hands. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r129-b12", "out": "s12-a-few-sick-folk-that.jpeg", "seg": "n3b",
        "window": "63.15-68.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NAZARETH", "SICKFEW"],
        "narration": (
            "A few sick folk. That is all Nazareth brought Him, and He laid "
            "His hands on every one of them."
        ),
        "must_show": "every one — Jesus moving along the three: the woman healed and upright, his hands now on the young man's brow, the elder next; nobody skipped.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the SEQUENCE readable — one healed, one under his hands, one awaiting.",
        "scene": (
            "The whole offering gets the whole blessing: the "
            "line is only three long and he works it like a "
            "harvest — the old woman already upright and "
            "wondering at her own steady hands, Jesus now bent "
            "with his palms at the gaunt young man's brow, and "
            "the stooped elder next in line straightening "
            "already in anticipation — everything Nazareth "
            "could bring itself to bring him, laid out in one "
            "small courtyard, and not one of the three passed "
            "over. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r129-b13", "out": "s13-the-mercy-never-shrank-down.jpeg", "seg": "n3b",
        "window": "68.73-72.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SICKFEW"],
        "narration": "The mercy never shrank down to match the unbelief.",
        "must_show": "the undiminished mercy — extreme close: Jesus's hand laid full and unhurried on a fevered brow; total tenderness at minimum audience.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the touch FULL — nothing perfunctory; the frame intimate.",
        "scene": (
            "The mercy comes at only one size: extreme close "
            "on Jesus's hand laid full across the young man's "
            "fevered brow — palm flat, fingers gentle, "
            "unhurried as if this were the day's only work and "
            "the town were watching, which it is not — the "
            "same whole-hearted touch that fed five thousand "
            "and stilled a sea, spent entire on an audience of "
            "one sick man in a town that never asked — mercy "
            "that has never once checked the crowd size before "
            "deciding how much to be. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r129-b14", "out": "s14-faith-opens-the-door-where.jpeg", "seg": "n4",
        "window": "72.85-77.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NAZARETH"],
        "narration": "Faith opens the door. Where people believed, even a little, He worked.",
        "must_show": "the door rhyme resolved — the lane of shut doors at early lamplit evening, and ONE door standing open with warm light, a hopeful family welcoming Jesus in.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the ONE open door against the shut lane unmistakable; the family's welcome eager.",
        "scene": (
            "One latch turns, and that is enough: down the "
            "evening lane the doors stand shut as they stood "
            "all day — but ONE is open, warm lamplight "
            "spilling over its threshold stone, and in the "
            "doorway a small family beckons Jesus in with the "
            "eager unguarded welcome the town could not manage "
            "— he steps toward the light, received at last on "
            "his own street — because faith the size of one "
            "opened door has always been exactly enough for "
            "him to work with. Every figure has two arms, two "
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
    # SYNAGOGUE: build-05 auto-match REJECTED per the row-73 precedent —
    # Nazareth's synagogue is its OWN place, not the bent-woman synagogue
    # (build-05 wires to 52/55 only). Promote-first from b06.
}
# === end PLACE-PLATES ===
