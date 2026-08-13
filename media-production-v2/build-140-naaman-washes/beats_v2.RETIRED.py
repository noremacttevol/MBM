#!/usr/bin/env python3
"""V2 beat map — row 140, build-140-naaman-washes (2 Kings 5:1-14).

COVERAGE: 16 pictures over 90.8 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (2 Kings 5 KJV):
  5:1   "Naaman, CAPTAIN of the host of the king of Syria, was a
        GREAT man... HONOURABLE... MIGHTY in valour, but he was a
        LEPER."
  5:2-3 "a LITTLE MAID... brought away captive out of the land of
        Israel... Would God my lord were with the prophet that is
        in Samaria! for he would recover him of his leprosy."
  5:9   "Naaman came WITH HIS HORSES AND WITH HIS CHARIOT, and
        stood at the DOOR of the house of Elisha."
  5:10  Elisha "SENT A MESSENGER" — did not come out: "Go and WASH
        IN JORDAN SEVEN TIMES."
  5:11-12 Naaman "was WROTH... turned and went away in a RAGE."
  5:13  his SERVANTS reason with him: "if the prophet had bid thee
        do some GREAT thing, wouldest thou not have done it?"
  5:14  "Then went he down, and dipped himself SEVEN TIMES in
        Jordan... and his flesh came again like unto the flesh of a
        LITTLE CHILD, and he was CLEAN."

RENDERING LAWS:
  - LEPROSY WITH TOTAL DIGNITY (row-15 class, strictly): the
    affliction is suggested ONLY by linen wrappings at wrist and
    neck and by Naaman's guarded privacy — NEVER lesions, NEVER
    close-up skin detail, NEVER grotesque. b14's restoration is
    shown as WHOLENESS (clean warm skin, wonder) — no before-gore.
  - THE LITTLE MAID is a captive child rendered with full dignity
    and warmth — earnest, kind, never cowed; her faith drives the
    whole story.
  - THE SEVEN DIPS are a COUNT (counts law): b12 shows the early
    dips (once, twice), b13 the SEVENTH — the discipline of the
    number visible in the scene text.
  - The plain-vs-great contrast is the row's engine: chariots and
    silver at a modest doorway (b05), the prophet's messenger
    instead of ceremony (b06); render the plainness lovingly, never
    shabby.
  - Naaman's rage is proud hurt, not villainy — a great man
    offended, then humbled, then made new.

TIME OF DAY ARC (intentional): Syria and the journey in hard bright
day; Elisha's doorway at plain noon; the Jordan in soft green-gold
afternoon; the restoration and close in warm late gold; b16's
application vignette at quiet lamplight BY DESIGN.

CHANGING CONDITIONS (kept OUT of the locks): the wrist/neck
wrappings — present until the seventh dip, GONE after; Naaman's
bearing — armored pride, rage, humility, wonder.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "NAAMAN": (
        "NAAMAN LOCK: Naaman is the same man in every shot — a "
        "powerful broad Syrian commander, about fifty, close-"
        "cropped grey-flecked dark hair and a short square beard, "
        "in DARK BRONZE-AND-LEATHER armor over a DEEP WINE-RED "
        "tunic (never cream, never white); linen wrappings at one "
        "wrist and the side of his neck until the healing; pride, "
        "rage, humility and wonder by turns, always commanding."
    ),
    "MAID": (
        "MAID LOCK: the little maid is the same girl in every "
        "shot — an Israelite servant girl of about eleven, dark "
        "braided hair, in a simple DARK MOSS-GREEN dress with a "
        "plain head-scarf (never cream, never white); earnest, "
        "kind, unafraid; full dignity always."
    ),
    "HOUSE": (
        "HOUSE LOCK: Elisha's house — a small plain mudbrick house "
        "with a low wooden door and a swept dirt yard, a fig tree "
        "at the corner; modest and clean, lovingly plain. The same "
        "house and yard throughout."
    ),
    "JORDAN": (
        "JORDAN LOCK: the Jordan — a green-banked river running "
        "slow between reeds and tamarisks, shallows of clean "
        "brown-green water over stones, soft afternoon light. The "
        "same bend and banks throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r140-b01", "out": "s01-naaman-was-a-great-man.jpeg", "seg": "n0",
        "window": "0.28-6.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["NAAMAN"],
        "narration": (
            "Naaman was a great man. Captain of the armies of Syria, "
            "honorable, mighty in valour."
        ),
        "must_show": "the greatness — Naaman reviewing his ranked chariots and spearmen on a Syrian parade ground, every line of him command; the great man at full height.",
        "must_not_show": "no halo; the wrappings PRESENT but incidental at wrist/neck — greatness the frame, not the affliction.",
        "scene": (
            "Syria's best soldier owns the morning, the camera "
            "looking down the parade line past his ranked "
            "spearmen's backs: Naaman walks the review in "
            "bronze and wine-red, chariots gleaming in their "
            "row, captains straightening as he passes — every "
            "line of the broad frame stating what the whole "
            "kingdom knows: honourable, mighty, the king's "
            "right arm — a great man at the full height of a "
            "great career, wearing his small linen wrist-"
            "wrapping like the afterthought he pretends it is. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r140-b02", "out": "s02-and-under-all-that-armor.jpeg", "seg": "n0",
        "window": "6.23-9.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN"],
        "narration": "And under all that armor — he was a leper.",
        "must_show": "the private truth — Naaman alone at evening, armor set aside, regarding the linen wrapping at his wrist with a shadowed face; the affliction told by the wrapping and his guard, NEVER by skin detail.",
        "must_not_show": "ABSOLUTE: no lesions, no skin close-ups, nothing grotesque — the wrapping and the heavy face carry everything.",
        "scene": (
            "The tent's privacy knows what the parade ground "
            "does not: Naaman alone in the lamplight with the "
            "bronze set on its stand, turning his forearm "
            "slowly to regard the linen wrapping at his wrist "
            "— the one enemy his valour cannot reach — the "
            "commanding face gone heavy and guarded in the "
            "quiet, a great man alone with the word that "
            "follows his name in whispers through both "
            "kingdoms: leper — under all that armor, exactly "
            "as mortal as anyone. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b03", "out": "s03-in-his-house-served-a.jpeg", "seg": "n1 + w1",
        "window": "9.80-18.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAID"],
        "narration": (
            "In his house served a young girl carried captive out of "
            "Israel. She knew where healing was. Would God my lord were "
            "with the prophet that is in Samaria!"
        ),
        "must_show": "SCRIPTURE-EXACT: the little maid — the Israelite girl speaking earnestly to her mistress in the great house, her small face bright with certainty; captive, kind, unafraid.",
        "must_not_show": "no halo; the girl's DIGNITY total — a serving child, never cowed; her hope the room's brightest thing.",
        "scene": (
            "The best intelligence in Syria belongs to the "
            "smallest person in the house: the little Israelite "
            "maid, eleven and braided and far from home, sets "
            "down her water jar and speaks up to her mistress "
            "with her whole earnest heart — would God my lord "
            "were with the prophet in Samaria — a captive girl "
            "spending her hope on the household that took her, "
            "certain of a healing two kingdoms' worth of "
            "generals and physicians know nothing about. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b04", "out": "s04-for-he-would-recover-him.jpeg", "seg": "w1",
        "window": "18.83-21.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAID"],
        "narration": "for he would recover him of his leprosy.",
        "must_show": "the certainty — close on the maid's face, utterly sure, her small hand lifted toward the west where Samaria lies; faith without a flicker.",
        "must_not_show": "no halo; ZERO doubt in the young face — the certainty is the picture.",
        "scene": (
            "Her certainty has a compass bearing: close on "
            "the small earnest face as her hand lifts toward "
            "the western hills — there, the gesture says, in "
            "Samaria, is a man of God, and he WOULD heal my "
            "master — no hedge in the young voice, no maybe "
            "in the steady eyes, just the whole unbruised "
            "faith of a child who has seen what her people's "
            "God does, offered freely to the house of her "
            "captivity. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r140-b05", "out": "s05-so-naaman-came-with-his.jpeg", "seg": "n2",
        "window": "22.65-30.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN", "HOUSE"],
        "narration": (
            "So Naaman came — with his horses, his chariots, his silver and "
            "gold — and stood at the door of a plain little house."
        ),
        "must_show": "SCRIPTURE-EXACT: the contrast — the glittering column (chariots, horses, chests of silver) drawn up before Elisha's small plain mudbrick house; magnificence idling at a modest door.",
        "must_not_show": "no halo; the house LOVINGLY plain, never shabby; the treasure visible in open chests.",
        "scene": (
            "Two economies meet at a wooden door: Naaman's "
            "column stands drawn up in the lane — chariots "
            "bright, horses stamping, open chests showing "
            "silver and folded scarlet — enough wealth to buy "
            "the village outright — and before all of it, "
            "small and swept and entirely unimpressed, "
            "Elisha's plain mudbrick house with its low "
            "wooden door and fig tree — the great man of "
            "Syria dismounting his glory at the one address "
            "that has never once been for sale. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b06", "out": "s06-the-prophet-even-come-out.jpeg", "seg": "n2",
        "window": "30.20-33.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN", "HOUSE"],
        "narration": "The prophet didn't even come out. He sent a messenger.",
        "must_show": "the affront — a plain servant at the barely-open door delivering the word; Naaman's face beginning its offended climb; ceremony conspicuously absent.",
        "must_not_show": "no halo; the messenger ORDINARY and calm; the door mostly shut — the slight architectural.",
        "scene": (
            "The reception is one plain man at a half-open "
            "door: a simple servant in working clothes stands "
            "in the gap of Elisha's doorway with the message "
            "and nothing else — no prophet, no procession, no "
            "bowing household staff — while before him Syria's "
            "second-greatest man sits his chariot with the "
            "offended colour already climbing his face: two "
            "kingdoms' protocol expecting an audience, and "
            "receiving instead a doorway's worth of errand-"
            "boy. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r140-b07", "out": "s07-go-and-wash-in-jordan.jpeg", "seg": "s1",
        "window": "34.19-39.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": (
            "Go and wash in Jordan seven times, and thy flesh shall come "
            "again to thee, and thou shalt be clean."
        ),
        "must_show": "SCRIPTURE-EXACT: the instruction — the messenger's simple open-handed gesture toward the river valley eastward; the whole cure in one plain sentence and one pointed direction.",
        "must_not_show": "no halo; the gesture SIMPLE — no scroll, no rite; the direction toward the valley clear.",
        "scene": (
            "The most expensive prescription in Syria costs "
            "seven dips: the messenger's hand opens simply "
            "toward the east where the Jordan valley runs "
            "green below the hills — go, wash, seven times — "
            "the entire cure delivered in a sentence you "
            "could teach a child, no rite attached, no fee "
            "schedule, no ceremony worthy of anybody's "
            "greatness — just a direction, a river, and a "
            "number, handed over the doorstep like borrowed "
            "salt. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r140-b08", "out": "s08-and-naaman-was-furious-he.jpeg", "seg": "n3",
        "window": "41.35-47.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN"],
        "narration": (
            "And Naaman was furious. He had expected something great — a "
            "mighty ceremony worthy of a mighty man."
        ),
        "must_show": "the fury — Naaman's fist tight on the chariot rail, jaw knotted, proud hurt blazing; the imagined grand ceremony dying behind his eyes.",
        "must_not_show": "no halo; PROUD HURT, not villainy — a great man offended, still great.",
        "scene": (
            "The rage of a great man is mostly wounded "
            "imagination: Naaman's fist whitens on the "
            "chariot rail, the square jaw knotting, the "
            "commander's eyes blazing over the little house — "
            "he had CAST this scene: the prophet striding "
            "out, the called-on Name, the hand waved grandly "
            "over the affliction before assembled witnesses — "
            "a healing sized to his rank — and the theatre "
            "in his head dies hard against a half-open door "
            "and a sentence about bathing. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b09", "out": "s09-it-was-too-plain-too.jpeg", "seg": "n3",
        "window": "47.83-51.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN", "HOUSE"],
        "narration": "It was too plain. Too simple. He turned and rode away in a rage.",
        "must_show": "the riding-off — the column wheeling away from the plain house in dust, Naaman's back rigid; DIRECTION: away from the door, the cure left behind.",
        "must_not_show": "no halo; the turn UNMISTAKABLE — chariots wheeling, dust rising, the little house steady behind.",
        "scene": (
            "Pride pulls the whole column off the cure: the "
            "chariots wheel hard in the lane, horses "
            "snorting into the dust of the turn, and Naaman "
            "rides at their head with his back rigid as a "
            "spear-shaft — away from the door, away from the "
            "river, away from the only sentence in two "
            "kingdoms that can help him — while behind the "
            "rising dust Elisha's little house stands "
            "unmoved, its half-open door still holding the "
            "offer exactly where he left it. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b10", "out": "s10-if-the-prophet-had-bid.jpeg", "seg": "s2",
        "window": "52.48-57.04", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN"],
        "narration": (
            "If the prophet had bid thee do some great thing, wouldest thou "
            "not have done it?"
        ),
        "must_show": "SCRIPTURE-EXACT: the servants' courage — two of his servants approaching the halted chariot humbly, one reasoning up at him with careful open hands; loyalty risking the rage.",
        "must_not_show": "no halo; the servants HUMBLE and brave at once; Naaman listening despite himself.",
        "scene": (
            "The bravest men in the column are the unarmed "
            "ones: at the halt two of Naaman's servants "
            "approach the chariot wheel and one reasons "
            "carefully up at the thunderhead above them — "
            "master, had he asked some GREAT thing, a "
            "campaign, a mountain of gold — would you not "
            "have done it? — the logic offered on open "
            "palms, loyalty walking straight into the rage "
            "on behalf of the man having it — and the "
            "commander's jaw, despite everything, beginning "
            "to loosen around the point. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b11", "out": "s11-how-much-rather-then-when.jpeg", "seg": "s2",
        "window": "57.04-60.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN"],
        "narration": (
            "how much rather then, when he saith to thee, Wash, and be "
            "clean?"
        ),
        "must_show": "the logic landing — the servant's gentle open hands finishing the argument; Naaman's face turning from rage toward the river's direction; the pivot.",
        "must_not_show": "no halo; the pivot VISIBLE — the proud face softening by degrees, eyes going east.",
        "scene": (
            "Six words finish what fury started to lose: "
            "wash — and be CLEAN — the servant's hands open "
            "gently around the little sentence as if setting "
            "it on a table, nothing added — and above him "
            "the great face performs its slow surrender: "
            "the jaw easing, the blazing eyes turning east "
            "toward the green line of the valley, pride "
            "discovering what pride always discovers last — "
            "that the small obedience was only ever beneath "
            "the man too big to be healed. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b12", "out": "s12-so-the-great-captain-went.jpeg", "seg": "n4",
        "window": "62.23-67.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN", "JORDAN"],
        "narration": (
            "So the great captain went down, and dipped himself in the "
            "Jordan. Once. Twice."
        ),
        "must_show": "the early dips — Naaman waist-deep in the green shallows in a plain under-tunic, armor left on the bank, mid-dip; the COUNT begun (once, twice); wrappings still on.",
        "must_not_show": "no halo; the armor visibly LEFT on the bank; nothing yet changed — early in the count.",
        "scene": (
            "Greatness wades in wearing only obedience: the "
            "bronze and the wine-red lie folded on the bank "
            "with his sword atop them, and Naaman stands "
            "waist-deep in the slow green water in a plain "
            "soaked under-tunic — going down, coming up, "
            "going down again — once, twice, the linen "
            "wrappings dark with river water, nothing "
            "whatsoever happening yet — a commander counting "
            "dips in a foreign river on a servant-girl's "
            "faith and a doorstep sentence. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b13", "out": "s13-seven-times-exactly-as-the.jpeg", "seg": "n4",
        "window": "67.50-70.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN", "JORDAN"],
        "narration": "Seven times, exactly as the man of God had said.",
        "must_show": "the SEVENTH dip — Naaman rising through the surface on the final count, water sheeting off; the number kept exactly; the moment of the change arriving.",
        "must_not_show": "no halo; the count's discipline the frame — the seventh, no shortcut taken.",
        "scene": (
            "The seventh time is the one the story was "
            "waiting for: Naaman drives down through the "
            "green water once more — the full count, no "
            "shortcut, exactly as the man of God said — and "
            "comes up through the breaking surface with the "
            "river sheeting off his head and shoulders, "
            "eyes still shut, the number kept to its last "
            "digit by a man who has finally learned to "
            "follow an order as given — and the water "
            "running off him runs off something new. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b14", "out": "s14-and-his-flesh-came-again.jpeg", "seg": "s3 + n5",
        "window": "71.35-80.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN", "JORDAN"],
        "narration": (
            "And his flesh came again like unto the flesh of a little "
            "child, and he was clean. The instruction wasn't beneath him."
        ),
        "must_show": "SCRIPTURE-EXACT: the restoration as WHOLENESS — Naaman standing in the shallows staring at his own clean whole forearm, the sodden wrappings loose in his other hand, wonder breaking his face.",
        "must_not_show": "ABSOLUTE: no before-gore, no lesion contrast — clean warm whole skin and WONDER carry the miracle; the wrappings off.",
        "scene": (
            "The proof peels off with the wet linen: Naaman "
            "stands in the thigh-deep shallows staring at "
            "his own bared forearm — clean, whole, warm as "
            "a boy's — the sodden wrappings hanging loose "
            "and pointless from his other fist — and the "
            "commander's face breaks open around the wonder "
            "the way faces do when the impossible turns "
            "ordinary in front of them: flesh like a little "
            "child's, on the arm of Syria's hardest man, "
            "wearing nothing but river water and grace. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r140-b15", "out": "s15-it-was-the-way-back.jpeg", "seg": "n5",
        "window": "80.15-81.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAAMAN", "JORDAN"],
        "narration": "It was the way back.",
        "must_show": "the way back — Naaman in the gold shallows, both clean hands open before his own eyes, the river running past; humility's reward held up to the light.",
        "must_not_show": "no halo; the quiet TOTAL — one man, two clean hands, one river.",
        "scene": (
            "The way back turns out to be seven steps down "
            "into a river: Naaman stands in the late gold "
            "shallows with both hands open before his own "
            "eyes — turning them slowly, backs and palms, a "
            "general inspecting the best terrain report of "
            "his life — the Jordan sliding green and "
            "unbothered past his knees, the bank's armor "
            "waiting where pride left it, and the plain "
            "little instruction proven, at last, to have "
            "been the whole road home. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r140-b16", "out": "s16-if-been-away-the-way.jpeg", "seg": "n5",
        "window": "81.59-90.44", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "If you've been away, the way back may look almost too simple — "
            "pray again, read again, come back again. Do the simple thing."
        ),
        "must_show": "the application — a quiet lamplit room: an ordinary person kneeling again at their bedside in prayer, the simple thing being done; timeless, period-neutral, tender.",
        "must_not_show": "no halo; period-neutral simplicity — no modern objects; the kneeling itself the whole frame.",
        "scene": (
            "The Jordan runs through every quiet room: in "
            "the small lamplight an ordinary person kneels "
            "again at the bedside — hands folded on the "
            "blanket, head bowed, the posture a little "
            "stiff with long disuse — praying again, the "
            "way back looking exactly as unimpressive as "
            "it looked to Naaman: too plain, too simple, "
            "and the only thing that works — one knee down, "
            "then the other, seven dips' worth of humility "
            "in a single kneeling, and the way home open "
            "from anywhere. Every figure has two arms, two "
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
    # HOUSE --take from build-16 REJECTED (the Bethany dusk lane — declined
    # 11+ times across builds; Elisha's house is its own place). Promote-first
    # from b05. JORDAN promote-first from b12.
}
# === end PLACE-PLATES ===
