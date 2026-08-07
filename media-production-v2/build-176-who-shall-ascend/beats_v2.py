#!/usr/bin/env python3
"""V2 beat map — row 176, build-176-who-shall-ascend (Psalm 24, "Who shall ascend
into the hill of the LORD?... the King of glory shall come in").

COVERAGE: 17 pictures over 65.068 s (card_start) = ~3.8 s/picture (lesson 12
movie-coverage). ONE establishing wide per place (b01 the hill of the Lord at
dawn, b04 the great everlasting gates, b14 the holy place / temple court); every
other beat is a single, a close, an insert or a two-shot. A human spine runs
through it: one humble WORSHIPPER we follow (clean hands, a pure heart, receives
the blessing) inside the wider procession of WORSHIPPERS.

NO OPEN CAMERON COMPLAINT — `v2_outline.py 176` shows none. Fresh V2 picture map
on the already-authored SPEAKER-LAW narration (audio OK).

SPEAKER LAW (see make_narration.py): Psalm 24 is David at the pen from start to
finish — a psalmist asking about the LORD and answering himself, the LORD never
opening his mouth in it. So EVERY scripture beat (s1, s2, s3, s4, s5) is the
SCRIPTURE voice → LIGHT-BLUE captions. There is NO red-letter and NO God-voice
in this row (both scripture beats were wrongly painted Jesus-red in V1; the
rebuild moved them to blue).

**GOD / THE KING OF GLORY IS NEVER EMBODIED.** This is the central content-care
call of the row. "The King of glory shall come in" and "the LORD strong and
mighty, the LORD mighty in battle" are carried by the FLUNG-WIDE everlasting
doors, the radiant dawn light pouring through the opened gate, and the awe and
reverence on the worshippers' faces — NEVER a divine figure, face, hand, throne,
beam-as-a-being, or any halo/ring of light around a head or in the gate. "Mighty
in battle" is shown as MAJESTY AND AWE, never violence, army, weapons or gore.
NO Jesus and NO cream anywhere in this row (OT psalm, Deity not embodied).

CONTENT-CARE: the hill of the LORD and the holy place are credible ancient
biblical architecture in the manner of the Jerusalem temple — dressed pale stone,
broad steps, tall plain columns, great timber-and-bronze doors — NEVER a modern
building and NEVER a specific present-day temple. No rendered writing anywhere
(captions live in the bottom band only).

PLACES (all NEW build-local):
  HILL-OF-THE-LORD  the holy hill / temple mount and its ascent at dawn
                    (b01-b03, b05-b07, b10)
  ANCIENT-GATES     the great everlasting doors and their threshold
                    (b04, b08, b09, b11, b12, b13)
  TEMPLE-COURT      the holy place inside the gates where the blessing is received
                    (b14-b17)
NEW places (runner promotes each from its first good frame, lesson 11):
  HILL-OF-THE-LORD  promote b01 (its establishing wide)
  ANCIENT-GATES     promote b04 (its establishing wide)
  TEMPLE-COURT      promote b14 (its establishing wide)
Steps in QC.md.
"""

# LOCKS: all build-local. No cream on anyone (only Jesus wears cream, and Jesus
# is not in this row). No image face sheets exist for these figures — each is
# carried by a byte-identical text lock.
LOCKS = {
    "HILL-OF-THE-LORD": (
        "HILL-OF-THE-LORD LOCK: the same place in every frame — the holy hill of "
        "the Lord, an ancient stone temple standing on the flat crown of a high "
        "hill above the city, reached by a broad worn stone ascent that climbs its "
        "flank. Credible first-century-world biblical architecture in the manner "
        "of the Jerusalem temple: dressed pale limestone, broad steps, tall plain "
        "columns, a wide open forecourt, warm dawn light on the stone, the lower "
        "roofs and hills falling away below under an open sky. The same hill, "
        "temple and ascent throughout — NEVER a modern building, dome of glass or "
        "steel, spire, sign, wire, pole or fixture, never a specific present-day "
        "temple, and no rendered writing of any kind."
    ),
    "ANCIENT-GATES": (
        "ANCIENT-GATES LOCK: the same gateway in every frame — the great "
        "everlasting doors of the house of the Lord: a tall arched stone portal "
        "in the temple wall closed by massive ancient double doors of dark aged "
        "timber banded and studded with weathered bronze, set at the head of the "
        "broad stone steps. Credible ancient biblical work, plain and mighty, no "
        "modern hinge, lock, glass, sign, wire or fixture and no rendered writing "
        "of any kind. The same portal, doors and steps throughout."
    ),
    "TEMPLE-COURT": (
        "TEMPLE-COURT LOCK: the same place in every frame — the holy place inside "
        "the gates: a broad open stone forecourt of the ancient temple, warm "
        "dressed pale limestone paving, tall plain columns down one side, the "
        "open sky above and the great doors standing behind. Credible ancient "
        "biblical architecture, no modern building, fixture, glass, sign, wire or "
        "pole and no rendered writing of any kind. The same court throughout."
    ),
    "WORSHIPPER": (
        "WORSHIPPER LOCK: the one worshipper we follow is the same man in every "
        "shot — an ordinary Hebrew man of about thirty-five, brown-skinned, with "
        "short dark hair and a trimmed dark beard, in a plain earth-toned "
        "hand-woven wool tunic and mantle (never cream, never white), bare-headed, "
        "his face humble and earnest. The SAME man throughout, never twinned, "
        "never a cloned face; ordinary-sized, with two hands and one head."
    ),
    "WORSHIPPERS": (
        "WORSHIPPERS LOCK: the procession of worshippers is a mixed, diverse crowd "
        "of ordinary Hebrew men, women and children of the ancient world, in "
        "varied earth-toned hand-woven wool and linen, some with staffs or bundles "
        "for the climb, none in cream and none in white robes. Distinct, "
        "ordinary-sized people with two hands and one head each, never twinned, "
        "never cloned faces, never modern clothing, flags or signage."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r176-b01", "out": "s01-the-hill-at-dawn.jpeg", "seg": "n0",
        "window": "0.400-3.100", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILL-OF-THE-LORD"],
        "narration": "Psalm 24 begins like a procession approaching the place where heaven and earth meet.",
        "must_show": "the ONE establishing wide of the holy hill — the camera looks up from below toward the ancient temple standing on the crown of the high hill in the first dawn light, the broad stone ascent climbing its flank; the place where heaven and earth meet.",
        "must_not_show": "no God figure, face, hand or beam-being; no modern building, dome, spire, sign or fixture; no specific present-day temple; no Jesus and no cream; no halo, ring of light or rim-light on anything; no scroll, writing or panel; no modern object.",
        "scene": (
            "The camera is set low on the road below and looks up in a high "
            "three-quarter view past the ascending steps toward the flat crown of "
            "a high hill, where an ancient stone temple of dressed pale limestone "
            "stands in the first warm dawn light above the lower roofs and hills. "
            "The broad worn stone ascent climbs the near flank. It is credible "
            "ancient biblical architecture, broad-stepped and plain-columned; "
            "nothing is written anywhere on it and no ring of light surrounds it — "
            "only the clean dawn on the stone."
        ),
    },
    {
        "id": "v2-r176-b02", "out": "s02-the-procession-approaches.jpeg", "seg": "n0",
        "window": "3.100-6.037", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL-OF-THE-LORD", "WORSHIPPERS"],
        "narration": "Psalm 24 begins like a procession approaching the place where heaven and earth meet.",
        "must_show": "the procession approaching — from behind, a line of ordinary worshippers moving up the stone road toward the temple on the hill; drawn upward, not driven.",
        "must_not_show": "no God figure or beam-being; no modern dress, sign or vehicle; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no modern object; no posed line facing the lens.",
        "scene": (
            "The camera stands on the ascent behind the backs of the worshippers "
            "and looks up the worn stone road toward the temple on the crown of "
            "the hill: an ordinary procession of Hebrew men, women and children "
            "climbs steadily upward together in the dawn light, staffs and bundles "
            "in hand. Ordinary-sized, distinct people with two hands and one head "
            "each, none in cream and none turned to the camera; nothing is written "
            "anywhere and no ring of light surrounds anyone."
        ),
    },
    {
        "id": "v2-r176-b03", "out": "s03-who-shall-ascend.jpeg", "seg": "s1",
        "window": "6.037-8.678", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL-OF-THE-LORD", "WORSHIPPER"],
        "narration": "Who shall ascend into the hill of the LORD?",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the ascent as a question: the one worshipper we follow paused mid-climb on the stone steps, looking up toward the distant temple; who shall ascend.",
        "must_not_show": "no God figure or beam-being; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "On the broad stone ascent, the one humble worshipper pauses mid-climb, "
            "one hand on a step above him, and lifts his earnest face toward the "
            "distant temple on the crown of the hill — a man weighing whether he "
            "may go up. The road and the lower hills lie behind and below in the "
            "morning light. An ordinary-sized man with two hands and one head, not "
            "in cream, his gaze up the hill and not the camera; nothing is written "
            "anywhere and no ring of light surrounds his head."
        ),
    },
    {
        "id": "v2-r176-b04", "out": "s04-stand-in-his-holy-place.jpeg", "seg": "s1",
        "window": "8.678-12.493", "wide": True, "jesus": False, "ref": False,
        "locks": ["ANCIENT-GATES", "WORSHIPPER"],
        "narration": "or who shall stand in his holy place?",
        "must_show": "SCRIPTURE-EXACT — the establishing wide of the great gates: the one worshipper stands small at the head of the steps before the tall closed everlasting doors, gazing up at them; who shall stand in his holy place.",
        "must_not_show": "no God figure, face or beam-being; no modern hinge, lock, glass, sign or fixture; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "The camera stands a little behind and below the worshipper and looks "
            "up past his back toward the great everlasting doors of the temple — a "
            "tall arched stone portal closed by massive ancient double doors of "
            "dark banded timber studded with weathered bronze, set at the head of "
            "the broad steps. He stands small before them in the dawn, gazing up, "
            "asking whether he may stand in this holy place. Ordinary-sized, with "
            "two hands and one head, not in cream, his face to the doors and not "
            "the camera; nothing is written anywhere and no ring of light "
            "surrounds anything."
        ),
    },
    {
        "id": "v2-r176-b05", "out": "s05-clean-hands.jpeg", "seg": "s2",
        "window": "12.493-15.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL-OF-THE-LORD", "WORSHIPPER"],
        "narration": "He that hath clean hands, and a pure heart;",
        "must_show": "SCRIPTURE-EXACT — a close insert of the worshipper's open, clean, work-worn hands held out at the ascent; clean hands.",
        "must_not_show": "no God figure or beam-being; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no blood or stain.",
        "scene": (
            "A close insert on the one worshipper's two open hands held out palms "
            "up in the morning light — ordinary, clean, work-worn hands, nothing "
            "hidden in them, the plain act of a man showing he comes with clean "
            "hands. The stone of the ascent lies soft behind. Two complete hands "
            "with five fingers each; nothing is written anywhere and no ring of "
            "light surrounds them."
        ),
    },
    {
        "id": "v2-r176-b06", "out": "s06-a-pure-heart.jpeg", "seg": "s2",
        "window": "15.400-18.600", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL-OF-THE-LORD", "WORSHIPPER"],
        "narration": "He that hath clean hands, and a pure heart;",
        "must_show": "SCRIPTURE-EXACT — a close on the worshipper's calm, honest face, eyes lowered in humility on the ascent; a pure heart.",
        "must_not_show": "no God figure or beam-being; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A close on the one worshipper's face on the ascent — calm, honest and "
            "unguarded, his eyes lowered in quiet humility, the earnest look of a "
            "man with a pure heart. Soft dawn light and the pale stone sit behind "
            "him. An ordinary-sized man with one head, not in cream, his eyes down "
            "and not to the camera; nothing is written anywhere and no ring of "
            "light surrounds his head."
        ),
    },
    {
        "id": "v2-r176-b07", "out": "s07-not-bloodline-or-rank.jpeg", "seg": "n1",
        "window": "18.600-21.949", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL-OF-THE-LORD", "WORSHIPPER", "WORSHIPPERS"],
        "narration": "The answer was not about bloodline or rank.",
        "must_show": "the humble man among the finer — the plain worshipper on the ascent beside a couple of more richly dressed pilgrims, all climbing together as equals; the gate is about the heart, not status.",
        "must_not_show": "no God figure or beam-being; no throne, crown or badge of office singled out; no modern dress or object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel.",
        "scene": (
            "On the ascent the one plain worshipper climbs shoulder to shoulder "
            "with two more richly robed pilgrims, none set above the other — the "
            "poor man and the well-dressed man on the same steps in the same "
            "morning light, going up together as equals. Ordinary-sized, distinct "
            "people with two hands and one head each, none in cream, their faces "
            "up the hill and not to the camera; nothing is written anywhere and no "
            "ring of light surrounds anyone."
        ),
    },
    {
        "id": "v2-r176-b08", "out": "s08-lift-up-your-heads.jpeg", "seg": "s4",
        "window": "21.949-26.213", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANCIENT-GATES", "WORSHIPPERS"],
        "narration": "Lift up your heads, O ye gates; and be ye lift up, ye everlasting doors;",
        "must_show": "SCRIPTURE-EXACT — a nearer look at the great closed everlasting doors from below, worshippers gathered small at their foot with faces lifted toward them; lift up your heads, O ye gates.",
        "must_not_show": "no God figure, face or beam-being; no modern hinge, lock, glass or fixture; no Jesus and no cream; no halo, ring of light or rim-light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "A nearer view looking up at the great everlasting doors — massive "
            "ancient double doors of dark banded timber and weathered bronze, still "
            "shut, filling the tall stone portal above the broad steps. At their "
            "foot a knot of worshippers stands small with faces lifted toward the "
            "doors in expectation. Ordinary-sized, distinct people with two hands "
            "and one head each, none in cream, seen from behind and the side; "
            "nothing is written anywhere and no ring of light surrounds the doors."
        ),
    },
    {
        "id": "v2-r176-b09", "out": "s09-the-king-of-glory-comes-in.jpeg", "seg": "s4",
        "window": "26.213-35.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANCIENT-GATES", "WORSHIPPERS"],
        "narration": "and the King of glory shall come in.",
        "must_show": "SCRIPTURE-EXACT — the doors FLUNG WIDE and radiant dawn light pouring through the open everlasting gate onto the awestruck worshippers; the King of glory shall come in — carried by the open gate and the light, NEVER a figure.",
        "must_not_show": "GOD IS NEVER SHOWN — no King figure, no divine face, hand, throne or robed being in the gateway or in the light; no beam shaped like a person; no modern object; no Jesus and no cream; no halo or ring of light around any head; no scroll, writing or panel.",
        "scene": (
            "The great everlasting doors stand flung wide and bright dawn light "
            "pours through the open portal down the broad steps onto the "
            "worshippers, who draw back in awe with faces lifted into the "
            "brightness — the gate opened for the King of glory to come in. The "
            "gateway itself is open and radiant and EMPTY of any figure; the light "
            "is plain morning light, no shape or being within it. Ordinary-sized, "
            "distinct people with two hands and one head each, none in cream, seen "
            "from behind and the side; nothing is written anywhere and no ring of "
            "light surrounds any head."
        ),
    },
    {
        "id": "v2-r176-b10", "out": "s10-single-to-royal-arrival.jpeg", "seg": "n3a",
        "window": "35.000-40.353", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANCIENT-GATES", "WORSHIPPER", "WORSHIPPERS"],
        "narration": "The poem widens from a single worshiper to a royal arrival.",
        "must_show": "the widening — the one worshipper in the near foreground with the whole gathered assembly beyond him all turned toward the opened gate; the frame widens from one man to a royal arrival.",
        "must_not_show": "no God figure or beam-being; no King, throne, crown or robed divine being in the gateway; no modern dress or object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "The one humble worshipper stands near in the foreground, seen from "
            "behind, and beyond him the whole gathered assembly spreads across the "
            "steps, every face turned up toward the opened everlasting gate and "
            "the morning brightness within it — the moment widening from a single "
            "worshipper to a great arrival. The open gateway stays empty of any "
            "figure. Ordinary-sized, distinct people with two hands and one head "
            "each, none in cream, faces to the gate and not the camera; nothing is "
            "written anywhere and no ring of light surrounds any head."
        ),
    },
    {
        "id": "v2-r176-b11", "out": "s11-who-is-this-king.jpeg", "seg": "s5",
        "window": "40.353-42.494", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANCIENT-GATES", "WORSHIPPERS"],
        "narration": "Who is this King of glory?",
        "must_show": "SCRIPTURE-EXACT — a close on two or three awestruck worshippers gazing up into the opened gate, the question on their faces; who is this King of glory.",
        "must_not_show": "GOD IS NEVER SHOWN — no King figure, divine face or being in the gate or the light; no beam shaped like a person; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A close on two or three worshippers among the crowd, faces lifted and "
            "lips parted in wonder as they gaze up toward the opened everlasting "
            "gate and the brightness beyond it — the unspoken question, who is "
            "this King of glory. The gateway beyond them stays open, radiant and "
            "empty of any figure. Ordinary-sized, distinct people with two hands "
            "and one head each, none in cream, their eyes on the gate and not the "
            "camera; nothing is written anywhere and no ring of light surrounds "
            "any head."
        ),
    },
    {
        "id": "v2-r176-b12", "out": "s12-the-lord-strong-and-mighty.jpeg", "seg": "s5",
        "window": "42.494-47.590", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANCIENT-GATES", "WORSHIPPERS"],
        "narration": "The LORD strong and mighty, the LORD mighty in battle.",
        "must_show": "SCRIPTURE-EXACT — the majesty shown as AWE: the worshippers bowing low and shielding their faces before the mighty opened gate and the strong morning light; the LORD strong and mighty — reverence, never war.",
        "must_not_show": "GOD IS NEVER SHOWN and there is NO VIOLENCE — no King, warrior, divine figure, face or being; no army, soldier, sword, spear, shield, weapon, armour, battle or gore anywhere; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel.",
        "scene": (
            "Before the mighty opened everlasting gate the worshippers bow low, "
            "some kneeling, some shielding their eyes with a raised forearm against "
            "the strong dawn light that fills the great portal — the majesty of "
            "the Lord strong and mighty read entirely in their reverence and awe. "
            "The gateway stays open and radiant and empty of any figure; there is "
            "no army, weapon or battle anywhere, only worship. Ordinary-sized, "
            "distinct people with two hands and one head each, none in cream; "
            "nothing is written anywhere and no ring of light surrounds any head."
        ),
    },
    {
        "id": "v2-r176-b13", "out": "s13-the-one-who-comes-in.jpeg", "seg": "n4b",
        "window": "47.590-50.808", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANCIENT-GATES", "WORSHIPPER"],
        "narration": "He is the one who comes in.",
        "must_show": "the arrival received — a close on the one worshipper's uplifted face turned into the brightness of the opened gate, awe and welcome in his eyes; he is the one who comes in — shown on the man's face, not on a figure.",
        "must_not_show": "GOD IS NEVER SHOWN — no King, divine face, figure or being in the gate or the light; no beam shaped like a person; no modern object; no Jesus and no cream; no halo or rim-light on his head; no scroll, writing or panel.",
        "scene": (
            "A close on the one worshipper's face turned up into the brightness "
            "pouring from the opened everlasting gate, his eyes wide with awe and "
            "welcome, his whole look answering that the awaited One has come in. "
            "The radiant gateway sits soft and empty of any figure beyond him. An "
            "ordinary-sized man with one head, not in cream, his face to the light "
            "and not the camera; nothing is written anywhere and no ring of light "
            "surrounds his head."
        ),
    },
    {
        "id": "v2-r176-b14", "out": "s14-receive-the-blessing.jpeg", "seg": "s3",
        "window": "50.808-54.200", "wide": True, "jesus": False, "ref": False,
        "locks": ["TEMPLE-COURT", "WORSHIPPER"],
        "narration": "He shall receive the blessing from the LORD,",
        "must_show": "SCRIPTURE-EXACT — the establishing wide of the holy place: the one worshipper stands within the open temple court, face lifted, receiving blessing under the morning light; he shall receive the blessing — the giver unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand, throne or being; no beam shaped like a person; no modern building or fixture; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "The camera looks past the worshipper's back into the broad open stone "
            "court of the holy place — pale dressed paving, tall plain columns "
            "down one side, the great doors standing behind and the open sky "
            "above. The one worshipper stands within it, face lifted and hands "
            "loosely open, receiving a blessing that comes from above and unseen. "
            "Warm plain morning light lies over the court; the giver is not shown. "
            "An ordinary-sized man with two hands and one head, not in cream, seen "
            "from behind; nothing is written anywhere and no ring of light "
            "surrounds his head."
        ),
    },
    {
        "id": "v2-r176-b15", "out": "s15-righteousness-from-god.jpeg", "seg": "s3",
        "window": "54.200-57.615", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE-COURT", "WORSHIPPER"],
        "narration": "and righteousness from the God of his salvation.",
        "must_show": "SCRIPTURE-EXACT — a nearer view of the worshipper standing settled and upright in the court, at peace and unashamed; righteousness from the God of his salvation.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or being; no beam shaped like a person; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A nearer view of the one worshipper standing settled and upright in "
            "the open temple court, shoulders eased, his face quiet and unashamed "
            "in the morning light — a man made righteous and at peace, standing "
            "where he asked whether he could stand. Pale columns and the open sky "
            "sit beyond. An ordinary-sized man with two hands and one head, not in "
            "cream, his gaze inward and not to the camera; nothing is written "
            "anywhere and no ring of light surrounds his head."
        ),
    },
    {
        "id": "v2-r176-b16", "out": "s16-purity-does-not-purchase.jpeg", "seg": "n2",
        "window": "57.615-61.300", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE-COURT", "WORSHIPPER"],
        "narration": "Purity does not purchase that blessing;",
        "must_show": "the empty open hands — a close insert of the worshipper's open, empty hands in the court, nothing offered or bought; purity does not purchase the blessing, it only makes him ready.",
        "must_not_show": "no God figure or beam-being; no coin, money, price or offering in the hands; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel.",
        "scene": (
            "A close insert of the one worshipper's two open, empty hands held "
            "loosely before him in the temple court — nothing offered in them, no "
            "price paid, only readiness — the plain truth that purity buys "
            "nothing, it only makes a man ready to receive. The pale court stone "
            "sits soft behind. Two complete hands with five fingers each and "
            "nothing held in them; nothing is written anywhere and no ring of "
            "light surrounds them."
        ),
    },
    {
        "id": "v2-r176-b17", "out": "s17-ready-to-receive.jpeg", "seg": "n2",
        "window": "61.300-65.068", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE-COURT", "WORSHIPPER"],
        "narration": "it describes the person ready to receive what God gives.",
        "must_show": "the ready man at the open way — the worshipper standing receptive within the court facing the open path ahead, unhurried and welcome; the person ready to receive what God gives.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or being; no beam shaped like a person; no modern object; no Jesus and no cream; no halo or rim-light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "The one worshipper stands receptive within the open temple court, "
            "seen from behind and the side, facing an open sunlit way that leads "
            "on through the columns — calm, unhurried and welcome, a man simply "
            "ready to receive what God will give. Warm plain morning light fills "
            "the court ahead of him. An ordinary-sized man with two hands and one "
            "head, not in cream, his face to the open way and not the camera; "
            "nothing is written anywhere and no ring of light surrounds his head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# All three places are NEW (no stash plate yet); the runner promotes each from
# its own first good frame (b01 / b04 / b14), so PLACE_REFS stays empty here.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: every person is carried by a byte-identical text lock (no face
# sheets exist for these figures). NO Jesus in this row.
REFS = {
}
