#!/usr/bin/env python3
"""V2 beat map — row 147, build-147-joseph-forgives (Genesis 45:1-8; 50:15-21).

COVERAGE: 16 pictures over 91.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Genesis KJV):
  37:28 the brothers SOLD Joseph to the Midianite caravan for
        twenty pieces of silver.
  41:40-43 Pharaoh set him "over all the land of Egypt" — second
        only to Pharaoh.
  45:1  "Cause every man to go out from me" — the room CLEARED
        before the reveal.
  45:4  "I AM JOSEPH YOUR BROTHER, WHOM YE SOLD INTO EGYPT."
  45:5  "be not grieved, NOR ANGRY WITH YOURSELVES... for God did
        send me before you TO PRESERVE LIFE."
  50:20 (after Jacob's death, the brothers fearing revenge): "ye
        THOUGHT EVIL against me; but GOD MEANT IT UNTO GOOD... to
        save much people alive."

RENDERING LAWS:
  - THE SELLING (b01) IS DISTANCE AND AFTERMATH ONLY: the far
    caravan taking young Joseph across the desert, the brothers
    small on a ridge — NO violence, NO pit scene, NO struggle,
    ever.
  - JOSEPH wears Egyptian regalia over a Hebrew face — the SAME
    face young (b01, at distance), vizier-age (b02-b11) and older
    (b12-b16); the gold collar and vizier linen never make him
    cold: warmth under authority is his register.
  - THE BROTHERS are TEN men (counts law) — varied, weathered,
    guilt-worn; their terror at the reveal is honest; their arc
    runs terror → unclenching → weeping relief → (older) fear →
    embraced. Never villains in frame — men who did a terrible
    thing and carried it.
  - The truth-telling is the row's spine: Joseph NAMES the evil
    plainly (b05/b06/b14) and forgives with it named — no soft-
    focus forgiveness; honesty and mercy in the same face.
  - The famine's rescue (b15) is bread lines and full granaries —
    Egypt fed; no starvation imagery, ever.

TIME OF DAY ARC (intentional): b01 at harsh desert noon (the worst
day); the hall scenes in cool interior light with high windows;
the reveal warming as the scene proceeds; the Genesis-50 scenes in
golden late light; the close in full warm gold.

CHANGING CONDITIONS (kept OUT of the locks): Joseph's age — young
at distance, vizier, older; the brothers' postures — bowed,
frozen, unclenched, embraced.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "JOSEPH": (
        "JOSEPH LOCK: Joseph is the same man in every shot — a "
        "Hebrew face under Egyptian office: handsome and open, "
        "clean-shaven in the Egyptian manner, dark-eyed, warm; as "
        "vizier he wears fine WHITE-LINEN Egyptian dress with a "
        "broad GOLD COLLAR and dark kohl (the linen is Egyptian "
        "costume, permitted; he is the one exception to the "
        "no-pale-cloth rule, by office); warmth always visible "
        "under the authority. Aged appropriately per beat: young "
        "at distance in b01, vizier-age (~40) through Genesis 45, "
        "older (~55) in Genesis 50."
    ),
    "BROTHERS": (
        "BROTHERS LOCK: the ten brothers — TEN men in every group "
        "shot (counts law): weathered Canaanite shepherds from "
        "grey-bearded Reuben down to young Benjamin's elder set, "
        "in worn earth-toned robes of brown, rust and olive (no "
        "cream); varied faces, guilt-worn, never villains."
    ),
    "HALL": (
        "HALL LOCK: Joseph's audience hall — a cool Egyptian "
        "chamber of pale sandstone columns painted with bands of "
        "colour, high clerestory light, a low dais with the "
        "vizier's chair. The same hall throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r147-b01", "out": "s01-years-before-own-brothers-had.jpeg", "seg": "n0a",
        "window": "0.40-4.82", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Years before, Joseph's own brothers had sold him into slavery "
            "out of jealousy."
        ),
        "must_show": "the worst day at DISTANCE — the far Midianite caravan crossing the harsh noon desert with young Joseph small among the traders, the brothers a knot of tiny figures on the ridge behind; aftermath framing, no violence.",
        "must_not_show": "ABSOLUTE: no pit, no struggle, no violence — distance carries everything; harsh noon light.",
        "scene": (
            "The worst day of two families is framed from far "
            "enough away to bear: across the harsh noon desert "
            "the Midianite caravan files small toward Egypt — "
            "camels, bales, traders, and among them one "
            "seventeen-year-old figure walking where he is "
            "led — while on the ridge behind, tiny against "
            "the glare, the knot of his brothers stands "
            "watching the distance take him — jealousy's "
            "whole transaction complete, twenty silver "
            "pieces heavy in a shepherd's bag, and thirteen "
            "years of God's strange arithmetic just begun. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r147-b02", "out": "s02-now-he-was-second-only.jpeg", "seg": "n0b",
        "window": "6.26-9.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "HALL"],
        "narration": "Now he was second only to Pharaoh in all Egypt.",
        "must_show": "the elevation — Joseph the vizier on the low dais of his columned hall, gold collar and fine linen, attendants and petitioners; authority at full height, warmth intact underneath.",
        "must_not_show": "no halo; the grandeur EGYPTIAN and real; his face still warm under the office.",
        "scene": (
            "Where the caravan's cargo ended up, the camera "
            "looking up the painted hall past the petitioners' "
            "backs: Joseph seated on the vizier's chair in "
            "fine white linen and the broad gold collar, "
            "attendants flanking the dais, the morning's "
            "petitioners bowing in the cool clerestory light — "
            "second man of the greatest kingdom on earth, "
            "grain-lord of the famine years — and under the "
            "kohl and the office, unmistakable to anyone who "
            "knew the boy, the same warm dark eyes. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b03", "out": "s03-when-the-brothers-came-begging.jpeg", "seg": "n1",
        "window": "10.46-16.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS", "HALL"],
        "narration": (
            "When the brothers came begging for food in the famine, they "
            "didn't recognize the brother they'd betrayed."
        ),
        "must_show": "the unknowing audience — the TEN brothers bowed low before the vizier's dais, faces down, hunger-worn; Joseph looking down at them KNOWING; the recognition entirely one-way.",
        "must_not_show": "no halo; COUNT ten; his knowing held behind the vizier's composure — one-way recognition the frame.",
        "scene": (
            "The men on the floor have no idea whose floor it "
            "is: the ten brothers bow low before the dais — "
            "weathered shepherds in worn wool, hunger-marks "
            "on their faces, sacks slack at their sides — "
            "begging grain from an Egyptian lord whose kohl-"
            "lined eyes move slowly across them, face by "
            "face by face, naming every one behind the "
            "vizier's composure — the betrayed brother "
            "looking down at his betrayers from the one seat "
            "in the world they could never imagine him in. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r147-b04", "out": "s04-then-he-sent-every-egyptian.jpeg", "seg": "n1",
        "window": "16.20-19.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "HALL"],
        "narration": "Then he sent every Egyptian out of the room, and told them.",
        "must_show": "SCRIPTURE-EXACT: the clearing — Joseph's raised command hand, the Egyptian attendants filing out the hall's doors; the room emptying for family business.",
        "must_not_show": "no halo; the attendants' exit ORDERLY; the tension climbing in the emptying room.",
        "scene": (
            "What he is about to say has no room in it for "
            "witnesses: Joseph's hand rises in a single "
            "command and the hall begins to empty — "
            "attendants and scribes and guards filing out "
            "through the great doors without a question, "
            "sandals whispering on stone — until the painted "
            "columns hold only one Egyptian lord and ten "
            "bowed shepherds and thirteen years of unfinished "
            "business — the door closing on the last "
            "official, and the vizier's composure beginning, "
            "at last, to come apart. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b05", "out": "s05-i-am-joseph-your-brother.jpeg", "seg": "s0",
        "window": "20.88-23.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS", "HALL"],
        "narration": "I am Joseph your brother, whom ye sold into Egypt.",
        "must_show": "SCRIPTURE-EXACT: the reveal — Joseph on his feet, composure broken open, tears starting as he says it; the ten frozen mid-bow, terror and disbelief arriving together.",
        "must_not_show": "no halo; COUNT ten; his tears REAL — the office falling away from the brother underneath.",
        "scene": (
            "Four words end thirteen years of disguise: "
            "Joseph is on his feet with the vizier's "
            "composure in pieces around him, tears cutting "
            "the kohl as it finally comes out — I am JOSEPH — "
            "your brother — whom ye SOLD — and along the "
            "floor the ten frozen faces come up one by one "
            "into the impossible recognition: the boy from "
            "the pit, wearing Egypt, standing over their "
            "grain sacks with their whole crime in his "
            "mouth and something unreadable behind his "
            "tears. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r147-b06", "out": "s06-he-soften-it-and-he.jpeg", "seg": "n1b",
        "window": "25.80-33.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS", "HALL"],
        "narration": (
            "He didn't soften it and he didn't skip it — he said the worst "
            "thing they ever did straight to their faces, and then he kept "
            "talking."
        ),
        "must_show": "the named evil — Joseph steady now, the terrible words plainly said, eyes level on his brothers; their terror total; honesty as the door to what follows.",
        "must_not_show": "no halo; NOTHING softened in his face yet — level truth; the brothers braced for execution.",
        "scene": (
            "The word SOLD stands in the room and he does "
            "not take it back: Joseph steady on his feet, "
            "the tears mastered, saying the worst thing "
            "they ever did straight into their faces — "
            "sold; me; you — no cushion under any syllable, "
            "no merciful vagueness — and the ten stand "
            "braced as men before a drawn sword, waiting "
            "for the vengeance that arithmetic owes them — "
            "while the vizier of Egypt, having named the "
            "crime exactly, draws breath and keeps talking. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r147-b07", "out": "s07-now-therefore-be-not-grieved.jpeg", "seg": "s1",
        "window": "35.08-42.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS", "HALL"],
        "narration": (
            "Now therefore be not grieved, nor angry with yourselves, that "
            "ye sold me hither: for God did send me before you to preserve "
            "life."
        ),
        "must_show": "SCRIPTURE-EXACT: the turn — Joseph's arms opening toward his braced brothers, the comfort arriving where the sword was expected; the sentence that reframes thirteen years.",
        "must_not_show": "no halo; the arms OPEN (never raised in judgment); the brothers' bracing beginning to crack.",
        "scene": (
            "The sword they braced for turns out to be open "
            "arms: Joseph's hands spread wide toward the ten "
            "— be NOT grieved — the impossible direction of "
            "the sentence registering on face after braced "
            "face — nor angry with YOURSELVES — the vizier "
            "of Egypt standing in his emptied hall "
            "reassigning thirteen years of their worst "
            "deed to a larger author: GOD sent me — before "
            "you — to preserve LIFE — mercy arriving with "
            "the crime still named and warm on the floor "
            "between them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r147-b08", "out": "s08-tear-yourselves-up-over-it.jpeg", "seg": "n1c",
        "window": "44.61-47.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS"],
        "narration": "Don't tear yourselves up over it, he said.",
        "must_show": "the permission beginning — close on two brothers' faces as the impossible kindness lands: guilt's grip visibly loosening by a degree.",
        "must_not_show": "no halo; the unclenching SMALL and true — disbelief before relief.",
        "scene": (
            "The sentence nobody says to the guilty is being "
            "said to them: close on two of the brothers as "
            "it lands — Judah's jaw slackening around "
            "disbelief, Simeon's braced shoulders dropping "
            "an inch from his ears — don't tear yourselves "
            "up — the grip of thirteen years of three-in-"
            "the-morning guilt loosening one finger at a "
            "time, against every instinct, on the word of "
            "the one man on earth entitled to tighten it. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r147-b09", "out": "s09-be-angry-at-yourselves-that.jpeg", "seg": "n1c",
        "window": "47.11-50.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS"],
        "narration": "Don't be angry at yourselves that you sold me here.",
        "must_show": "the specific pardon — Joseph moving down from the dais TO them, closing the distance; the specific crime specifically released.",
        "must_not_show": "no halo; DIRECTION — down and toward them; no brother grovelling, all stunned.",
        "scene": (
            "He comes down off the dais to say it at their "
            "level: Joseph descends the low steps and closes "
            "the distance his office built, stopping among "
            "them where a lord never stands — not angry at "
            "yourselves — the pardon aimed at the exact "
            "crime by name — that you sold ME, HERE — no "
            "general amnesty from a safe height but the "
            "specific release of the specific debt, "
            "delivered at arm's length by the creditor "
            "himself. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r147-b10", "out": "s10-god-sent-me-ahead-of.jpeg", "seg": "n1c",
        "window": "50.14-53.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "HALL"],
        "narration": "God sent me ahead of you — to keep people alive.",
        "must_show": "the reframe — Joseph's hand sweeping toward the hall's doorway and the granary court beyond: full stores, grain sacks, life preserved; the larger authorship visible.",
        "must_not_show": "no halo; the granaries FULL through the doorway — provision, not opulence.",
        "scene": (
            "The evidence for the reframe is stacked outside "
            "the door: Joseph's hand sweeps toward the "
            "hall's great doorway, and beyond it the granary "
            "court stands golden with provision — sacks "
            "ranked in their hundreds, grain running from "
            "the measuring scoops, porters loading famine "
            "relief for half a world — sent AHEAD, the "
            "gesture says; look what the sending was FOR — "
            "thirteen dark years re-filed in one sweep as "
            "the supply line of a rescue. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b11", "out": "s11-he-gave-them-the-one.jpeg", "seg": "n1c",
        "window": "53.00-58.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS"],
        "narration": (
            "He gave them the one thing they could not give themselves: "
            "permission to stop hating themselves."
        ),
        "must_show": "the permission received — a brother's sob finally breaking, Joseph's hand warm on the back of his neck; the release physical at last.",
        "must_not_show": "no halo; the sob HONEST — relief, not grovelling; Joseph's hand a brother's, not a lord's.",
        "scene": (
            "The thing no man can hand himself is handed "
            "over: one of the ten breaks at last — a sob "
            "tearing up out of a grey-bearded shepherd who "
            "has carried the pit inside him for thirteen "
            "years — and Joseph's hand comes warm to the "
            "back of his brother's bowed neck, holding him "
            "through it — permission, the grip says; stop; "
            "put it down — the one gift that only ever "
            "travels one direction: from the wronged, to "
            "the ones who did it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b12", "out": "s12-much-later-when-their-father.jpeg", "seg": "n2",
        "window": "60.19-66.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS"],
        "narration": (
            "Much later, when their father died and the brothers feared "
            "revenge, Joseph spoke the line that closes the wound."
        ),
        "must_show": "the later fear — the brothers OLDER, bowed again before older Joseph in golden late light, mourning-worn, braced for the revenge they still fear; his grief that they still fear him.",
        "must_not_show": "no halo; all aged consistently; Joseph's face GRIEVED at their fear, never stern.",
        "scene": (
            "Years and a father's funeral later, the old "
            "fear comes back wearing mourning clothes: the "
            "brothers — greyer now, faces cut deeper — bow "
            "before Joseph once again in the golden late "
            "light, braced once again, certain that with "
            "Jacob buried the ledger reopens — and on "
            "Joseph's older face, before any word, the "
            "grief of a man discovering that the people he "
            "forgave have carried the fear all these "
            "years anyway — and readying, once more, the "
            "line that closes wounds. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b13", "out": "s13-but-as-for-you-ye.jpeg", "seg": "s2",
        "window": "67.56-76.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS"],
        "narration": (
            "But as for you, ye thought evil against me; but God meant it "
            "unto good, to bring to pass, as it is this day, to save much "
            "people alive."
        ),
        "must_show": "SCRIPTURE-EXACT: the great line — older Joseph speaking it gently over his bowed brothers, one hand toward them (the evil named), one toward the fed land beyond (the good meant).",
        "must_not_show": "no halo; the TWO directions of the sentence in his two hands — named evil, meant good.",
        "scene": (
            "The greatest sentence about providence is "
            "spoken with both hands: one turns toward his "
            "bowed brothers — YE thought evil, and he does "
            "not unsay it — and the other opens toward the "
            "doorway and the fed golden land beyond — but "
            "GOD meant it unto GOOD — the two clauses held "
            "apart and together in the air between his "
            "arms: the crime real, the providence realer, "
            "and much people alive this day in the space "
            "between his hands. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b14", "out": "s14-you-meant-it-for-evil.jpeg", "seg": "n3",
        "window": "78.10-82.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH"],
        "narration": (
            "You meant it for evil, he told them — I'm not going to call it "
            "anything else."
        ),
        "must_show": "the honesty kept — close on older Joseph's level, kind, utterly honest face; the evil named without heat and without discount.",
        "must_not_show": "no halo; NO sternness and NO softening — level kind honesty, the row's signature register.",
        "scene": (
            "Forgiveness never once required him to lie: "
            "close on the older face — kohl-lined, "
            "kind-eyed, absolutely level — saying the plain "
            "half of the sentence without heat and without "
            "discount: you MEANT it for evil; I will not "
            "call it weather, or misunderstanding, or "
            "nothing — the truth held straight so the mercy "
            "leaning on it has something solid to stand on — "
            "honesty and forgiveness sharing one face "
            "without crowding. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b15", "out": "s15-a-whole-lot-of-people.jpeg", "seg": "n3",
        "window": "82.85-85.19", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "a whole lot of people are still alive.",
        "must_show": "the rescue's receipts — the granary court alive: bread and grain passing into ordinary hands, children eating, a queue moving with full sacks; the good God meant, at street level.",
        "must_not_show": "ABSOLUTE: no starvation imagery — the FED, not the famished; provision working.",
        "scene": (
            "The good God meant has faces and they are "
            "eating: the granary court runs at full "
            "provision — grain hissing from the measuring "
            "scoop into a mother's held-open sack, a boy "
            "walking off with bread in both fists, porters "
            "keeping the queue moving under the golden "
            "light — Egyptians and Canaanites and every "
            "hungry neighbour of the famine years, alive "
            "this day and standing in line to stay that "
            "way — the receipts of providence, paid out "
            "daily at street level. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r147-b16", "out": "s16-he-pretend-it-hurt-he.jpeg", "seg": "n3",
        "window": "85.19-90.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOSEPH", "BROTHERS"],
        "narration": (
            "He didn't pretend it hadn't hurt. He saw God's hand turning "
            "their evil into rescue."
        ),
        "must_show": "the closing embrace — older Joseph embracing his brothers in the warm gold, tears on the old faces, the storehouses golden beyond; wound closed with the truth intact.",
        "must_not_show": "no halo; COUNT ten in the embrace-knot; the tears on BOTH sides; the granaries visible beyond.",
        "scene": (
            "The wound closes with everyone's eyes open: "
            "older Joseph steps into his brothers and the "
            "embrace takes all of them — grey heads against "
            "his gold collar, ten weathered men and the boy "
            "they sold folded into one knot in the warm "
            "late light, tears running free on both sides "
            "of the old crime — and beyond the doorway the "
            "storehouses stand golden with the rescue their "
            "evil was bent into — nothing pretended, "
            "nothing unfelt, everything forgiven: God's "
            "hand, visible at last to every man in the "
            "room. Every figure has two arms, two hands "
            "and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # HALL --take from build-22 REJECTED (the parable king's hall — accepted
    # only for row 43; declined for Herod 86 and the council 63; an EGYPTIAN
    # painted-column hall is its own place). Promote-first from b02.
}
# === end PLACE-PLATES ===
