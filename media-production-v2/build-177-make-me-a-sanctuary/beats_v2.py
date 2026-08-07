#!/usr/bin/env python3
"""V2 beat map — row 177, build-177-make-me-a-sanctuary (Exodus 25:8, 25:22 — "let
them make me a sanctuary; that I may dwell among them").

COVERAGE: 19 pictures over 90.003 s (card_start) = ~4.7 s/picture (lesson 12
movie-coverage). ONE establishing wide per place (b01 the wilderness camp, b02
Moses on the mount, b07 the holy place / craft of the furniture); every other
beat is a single, a close, an insert or a two-shot. MOSES is the human spine.

OPEN CAMERON COMPLAINT (v2_outline.py 177): **"Not real new voice."** This is the
REDO-ALL voice-identity complaint — the cut must ship on the NEW ElevenLabs cast,
not the old edge-tts voices. FIXED AT SOURCE + DEFINITIVELY: all 13 segment mp3s
in this build's audio/ are ElevenLabs 44100 Hz/128 k (narrator Brian, GOD Bill),
confirmed by ffprobe; and this build sets **AUDIO_FROM_V1_SEGMENTS = True** so
v2_assemble rebuilds the shipped track from those new-voice segment mp3s at the
extract_beats offsets — the delivered V2 cut carries the new cast with certainty,
never a stale/old-voice stream-copy. The review card MUST tell Cameron the voice
is the real new voice now. See QC.md COMPLAINT LEDGER.

SPEAKER LAW (see make_narration.py): s1 (Ex 25:8) and g22 (Ex 25:22) are the GOD
voice → GREEN captions (Bill). Everything else is the NARRATOR (white). There is
NO Jesus red-letter and NO Jesus anywhere (OT, centuries before the Incarnation).

**HARD GATE — GOD IS NEVER EMBODIED.** On the two GOD-voice beats (b03 s1, b08/b09
g22) and every "meeting place" beat (b11/b12), God speaks and dwells but is NEVER
shown: no figure, face, hand, body, throne or beam-shaped-as-a-being, and no
halo/ring of light around anything. His presence "that I may dwell among them" is
the biblical CLOUD over the tent (Ex 40:34) — a natural soft cloud/radiance with
NO shape or face — and the meeting place "from above the mercy seat, between the
cherubims" is the EMPTY charged space above the lid, carrying at most soft light,
never a figure. NO cream anywhere (only Jesus wears cream; Jesus is not in this
row).

CONTENT-CARE: the two cherubim are the biblical CARVED SOLID-GOLD statues mounted
on the mercy-seat lid (Ex 25:18-20), wings arched toward each other — objects,
part of the ark, NOT living/flying angels and NOT God. The sanctuary is the
wilderness TABERNACLE — a plain goats'-hair TENT pitched in the middle of the
camp, NEVER a stone palace or a permanent temple. First-century-world-or-earlier
ancient Near-Eastern materials only; no modern object; no rendered writing
(captions live in the bottom band only). n4 "would take a face" is a spoken
foreshadow of Christ — do NOT depict Jesus; keep it the tent at dawn.

PLACES (all NEW build-local):
  WILDERNESS-CAMP  the Israelite camp of tents in the desert, the tabernacle tent
                   at its centre (b01, b03-b06, b13-b19)
  SINAI-MOUNT      the mountain where Moses receives the instruction (b02)
  TABERNACLE-HOLY  the holy place / craft of the ark, table and lampstand
                   (b07-b12)
NEW places (runner promotes each from its first good frame, lesson 11):
  WILDERNESS-CAMP  promote b01 (establishing wide)
  SINAI-MOUNT      promote b02
  TABERNACLE-HOLY  promote b07 (establishing wide)
Steps in QC.md.
"""

# The shipped narration is rebuilt from this build's OWN new-voice ElevenLabs
# segment mp3s (audio/<seg>.mp3, all 44100/128k) at the extract_beats offsets,
# so the delivered cut carries the real new cast — closes "Not real new voice".
AUDIO_FROM_V1_SEGMENTS = True

# LOCKS: all build-local. No cream on anyone (Jesus not in this row). No face
# sheets exist for these figures — each is carried by a byte-identical text lock.
LOCKS = {
    "WILDERNESS-CAMP": (
        "WILDERNESS-CAMP LOCK: the same place in every frame — the camp of Israel "
        "in the Sinai wilderness: dozens of low tents of dark goats'-hair cloth "
        "and earth-toned wool pitched across a broad stony desert basin ringed by "
        "bare tan hills, cook-fires and bundles among them, and at the centre the "
        "one larger TABERNACLE tent — a plain rectangular tent of dark goats'-hair "
        "curtains, the other tents circled around it. Ancient Near-Eastern desert "
        "encampment only: NEVER a modern building, vehicle, pole, wire, sign or "
        "fixture, never a stone palace or permanent temple, and no rendered "
        "writing of any kind. The same camp, hills and central tent throughout."
    ),
    "SINAI-MOUNT": (
        "SINAI-MOUNT LOCK: the same place in every frame — a high bare stone "
        "mountain of tan and grey rock rising over the desert, its upper slopes "
        "wrapped in a heavy cloud, the camp small on the plain far below. Ancient "
        "wilderness only, no building, path-rail, pole, wire or fixture and no "
        "rendered writing. The same mountain and cloud throughout."
    ),
    "TABERNACLE-HOLY": (
        "TABERNACLE-HOLY LOCK: the same place in every frame — the interior work "
        "and holy space of the tabernacle: warm lamplit gloom inside dark "
        "goats'-hair and richly dyed curtains, dressed acacia-wood work surfaces, "
        "the gold-worked sacred furniture standing on woven mats over packed "
        "desert ground. Ancient Near-Eastern craft only — hand tools, oil lamps, "
        "no modern object, machine, fixture, glass, sign, wire or rendered "
        "writing. The same lamplit holy interior throughout."
    ),
    "MOSES": (
        "MOSES LOCK: Moses is the same man in every shot — a weathered Hebrew "
        "elder of about eighty, brown-skinned and sun-darkened, with a long full "
        "grey beard and long grey hair, deep-set steady eyes, in a plain "
        "earth-toned hand-woven wool robe and mantle (never cream, never white), "
        "often a plain wooden staff in hand, grave and unhurried. The SAME man "
        "throughout, never twinned, never a cloned face; ordinary-sized, with two "
        "hands and one head."
    ),
    "ISRAELITES": (
        "ISRAELITES LOCK: the people and craftsmen of the camp are a mixed, "
        "diverse crowd of ordinary Hebrew men, women and children of the ancient "
        "world, in varied dusty earth-toned hand-woven wool and linen, none in "
        "cream and none in white robes, some carrying tools, bundles or "
        "water-skins. Distinct, ordinary-sized people with two hands and one head "
        "each, never twinned, never cloned faces, never modern clothing, tools, "
        "flags or signage."
    ),
    "THE-ARK": (
        "THE-ARK LOCK: the same object in every frame — the ark of the testimony: "
        "a rectangular acacia-wood chest overlaid in gold, carried by two gold "
        "poles through gold rings at its corners, closed by a solid-gold lid (the "
        "mercy seat); mounted on the lid two CARVED SOLID-GOLD cherubim — winged "
        "human-form statues facing each other from the two ends, their outstretched "
        "wings arched over toward the middle of the lid, leaving the space directly "
        "above the mercy seat open. They are CARVED STATUES that never move, never "
        "come alive and are never mistaken for God. The same ark, mercy seat and "
        "two gold cherubim throughout; no modern object and no rendered writing."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r177-b01", "out": "s01-the-camp-in-the-wilderness.jpeg", "seg": "n0",
        "window": "0.400-4.200", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "While Israel camped in the wilderness, the LORD gave Moses a strange instruction — have the people build me a sanctuary.",
        "must_show": "the ONE establishing wide of the camp — the camera looks down and across the Sinai wilderness camp at dusk, dozens of dark goats'-hair tents spread over the stony basin with the one larger tabernacle tent at the centre; Israel encamped in the wilderness.",
        "must_not_show": "no God figure, face or beam-being; no modern building, vehicle, pole, wire, sign or fixture; no stone palace or permanent temple; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no modern object.",
        "scene": (
            "The camera looks down from a low rise in a high three-quarter view "
            "across the wilderness camp at dusk: dozens of low tents of dark "
            "goats'-hair cloth spread over the stony desert basin ringed by bare "
            "tan hills, cook-fires beginning to kindle among them, and near the "
            "centre one larger plain tent standing among the rest. The last warm "
            "dusk light lies over the stone. Ancient desert encampment only; "
            "nothing is written anywhere and no ring of light surrounds anything."
        ),
    },
    {
        "id": "v2-r177-b02", "out": "s02-moses-on-the-mount.jpeg", "seg": "n0",
        "window": "4.200-7.981", "wide": True, "jesus": False, "ref": False,
        "locks": ["SINAI-MOUNT", "MOSES"],
        "narration": "the LORD gave Moses a strange instruction — have the people build me a sanctuary.",
        "must_show": "Moses receiving the instruction — Moses alone high on the cloud-wrapped mountain, head bowed and listening, the camp far below; the LORD giving him the word, the LORD Himself unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being in the cloud; no modern object; no Jesus and no cream; no halo or ring of light around Moses' head; no scroll, writing or panel.",
        "scene": (
            "The camera stands a little below and behind Moses and looks up past "
            "his back as he stands alone high on the bare stone mountain, head "
            "bowed and still, listening, the heavy cloud wrapping the slopes above "
            "him and the tiny camp spread on the plain far below. He receives a "
            "word from a presence that is not shown. An ordinary-sized old man "
            "with two hands and one head, not in cream, facing the cloud and not "
            "the camera; the cloud carries no shape or face, nothing is written "
            "anywhere and no ring of light surrounds his head."
        ),
    },
    {
        "id": "v2-r177-b03", "out": "s03-let-them-make-me-a-sanctuary.jpeg", "seg": "s1",
        "window": "7.981-13.556", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "And let them make me a sanctuary; that I may dwell among them.",
        "must_show": "GOD-VOICE, GREEN caption — the sanctuary among them: the central tabernacle tent standing raised in the middle of the camp with a soft cloud of presence resting over it, the circled tents around; that I may dwell among them — God present, God unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being in or above the cloud; the cloud has no shape or face; no stone palace or temple; no modern object; no Jesus and no cream; no halo/ring of light on any head; no scroll, writing or panel.",
        "scene": (
            "A nearer view across the camp toward the central tabernacle tent — a "
            "plain rectangular tent of dark goats'-hair curtains standing raised "
            "among the circled dwelling tents — with a soft low cloud of presence "
            "resting quietly over it in the fading light, the people's tents "
            "gathered close around. The cloud is plain and formless, carrying no "
            "shape or face. Ordinary desert camp; nothing is written anywhere and "
            "no ring of light surrounds anything."
        ),
    },
    {
        "id": "v2-r177-b04", "out": "s04-a-place-among-you.jpeg", "seg": "n0b",
        "window": "13.556-17.960", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "ISRAELITES"],
        "narration": "Build me a place, God said, so that I can live right there with you.",
        "must_show": "the place among them — Moses standing with a few of the people at the marked centre-ground of the camp, gesturing to the cleared space where the tent will stand right there among them.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "In the camp Moses stands with a small knot of the people at the "
            "cleared centre-ground and gestures to the open space where the "
            "tabernacle tent will stand, the dwelling tents close on every side — "
            "a place for God to live right there among them, not apart. Warm "
            "low light lies over the dust. Ordinary-sized, distinct people with "
            "two hands and one head each, none in cream, their eyes on the ground "
            "and Moses' hand and not the camera; nothing is written anywhere and "
            "no ring of light surrounds any head."
        ),
    },
    {
        "id": "v2-r177-b05", "out": "s05-not-a-far-off-palace.jpeg", "seg": "n0b",
        "window": "17.960-20.360", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "Not a palace on a far-off hill.",
        "must_show": "the humble plain tent, close — the ordinary goats'-hair tabernacle tent among the dusty camp; deliberately a plain near tent, NOT a grand palace on a distant hill.",
        "must_not_show": "no palace, grand hall, throne-room, colonnade or distant grand building of any kind; no God figure or beam-being; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "A close on the plain tabernacle tent itself among the camp — dark "
            "goats'-hair curtains, plain wooden frame, dust and cook-smoke around "
            "it, ordinary and humble in the low light. It is deliberately a "
            "modest near tent and nothing grand: no palace, hall or distant "
            "monument anywhere in view. Nothing is written anywhere and no ring of "
            "light surrounds it."
        ),
    },
    {
        "id": "v2-r177-b06", "out": "s06-tents-circled-around.jpeg", "seg": "n0b",
        "window": "20.360-27.180", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "ISRAELITES"],
        "narration": "A tent, pitched in the middle of the camp, with everybody else's tents circled around it.",
        "must_show": "the tent at the centre with the camp ringed around — a high wide look straight down over the camp showing the one tabernacle tent in the middle and all the people's tents pitched in a ring around it.",
        "must_not_show": "no God figure or beam-being; no modern building, vehicle, road or fixture; no stone palace or temple; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed faces to the lens.",
        "scene": (
            "The camera looks down from high above in a near-overhead three-quarter "
            "view over the whole camp: the single plain tabernacle tent stands in "
            "the middle and the people's dark tents are pitched in a wide ring "
            "circling around it across the desert floor, small figures moving "
            "among them. Bare hills close the horizon under dusk light. Ancient "
            "encampment only, seen from above so no face turns to the camera; "
            "nothing is written anywhere and no ring of light surrounds the "
            "central tent."
        ),
    },
    {
        "id": "v2-r177-b07", "out": "s07-the-ark-the-table-the-lampstand.jpeg", "seg": "n2a",
        "window": "27.180-33.271", "wide": True, "jesus": False, "ref": False,
        "locks": ["TABERNACLE-HOLY", "THE-ARK", "MOSES", "ISRAELITES"],
        "narration": "He told them exactly how — the ark, the table, the lampstand —",
        "must_show": "the establishing wide of the holy craft — the three sacred furniture pieces standing together in the lamplit tabernacle interior: the gold-worked ark with its two carved cherubim, the gold table, and the seven-branched gold lampstand, craftsmen at work around them.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; the cherubim are only the carved gold statues on the ark, never alive or flying; no modern object, tool or fixture; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "The camera looks across the warm lamplit tabernacle interior from "
            "behind the working craftsmen: the three gold-worked sacred pieces "
            "stand together on woven mats — the ark of acacia and gold with its "
            "two carved gold cherubim on the lid, a gold-overlaid table, and a "
            "tall seven-branched gold lampstand — while ordinary artisans shape and "
            "burnish them by hand in the oil-lamp light. Acacia-wood benches and "
            "hand tools around them. Ancient craft only; the cherubim are still "
            "carved statues; nothing is written anywhere and no ring of light "
            "surrounds anything."
        ),
    },
    {
        "id": "v2-r177-b08", "out": "s08-there-i-will-meet-with-thee.jpeg", "seg": "g22",
        "window": "33.271-39.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABERNACLE-HOLY", "THE-ARK"],
        "narration": "And there I will meet with thee, and I will commune with thee from above the mercy seat,",
        "must_show": "GOD-VOICE, GREEN caption — the ark close: the gold ark with its solid-gold mercy-seat lid and the two carved cherubim, the charged EMPTY space directly above the lid where the LORD will meet and commune; the meeting place, God unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand, body or beam-shaped-being above the mercy seat or anywhere; the cherubim stay carved gold statues; no modern object; no Jesus and no cream; no halo or ring of light around a head; no scroll, writing or panel.",
        "scene": (
            "A reverent close on the ark in the lamplit holy place: the gold "
            "acacia chest and its solid-gold lid, the two carved gold cherubim "
            "facing each other with wings arched over toward the middle, and the "
            "quiet open air directly above the mercy seat between them left "
            "charged and empty — the place from which the LORD will meet and "
            "commune, He Himself unseen. Warm lamp light lies on the gold; at most "
            "a faint soft brightness rests over the lid, with no shape or face in "
            "it. Nothing is written anywhere and no ring of light surrounds "
            "anything."
        ),
    },
    {
        "id": "v2-r177-b09", "out": "s09-between-the-two-cherubims.jpeg", "seg": "g22",
        "window": "39.000-44.496", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABERNACLE-HOLY", "THE-ARK"],
        "narration": "from between the two cherubims which are upon the ark of the testimony.",
        "must_show": "GOD-VOICE, GREEN caption — a tighter insert on the mercy seat between the two carved gold cherubim, the arched wings framing the empty charged space over the lid; from between the two cherubims upon the ark.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being between or above the cherubim; the cherubim stay carved gold statues, never living or moving; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "A tight insert looking along the gold lid between the two carved gold "
            "cherubim: their inward-facing figures and arched wings frame the "
            "quiet open space above the mercy seat, warm lamp light catching the "
            "worked gold. The space between and above them is left empty and "
            "still, the meeting place carrying no shape, face or being. Nothing "
            "is written anywhere and no ring of light surrounds anything."
        ),
    },
    {
        "id": "v2-r177-b10", "out": "s10-what-the-measurements-were-for.jpeg", "seg": "n2r",
        "window": "44.496-47.040", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABERNACLE-HOLY", "ISRAELITES"],
        "narration": "That is what all the measurements were for.",
        "must_show": "the exact craft — a close on a craftsman's hands measuring and marking the gold ark work with a cord and rule, careful and precise; what all the measurements were for.",
        "must_not_show": "no God figure or beam-being; no modern tool, tape, machine or object; no Jesus and no cream; no halo or ring of light; no scroll, writing or legible measurement markings.",
        "scene": (
            "A close on an artisan's work-worn hands stretching a knotted cord and "
            "a plain wooden straightedge along the edge of the gold-worked ark, "
            "measuring and marking a point with care in the lamp light — the exact "
            "and careful craft the whole pattern called for. Ancient hand tools "
            "only, no legible numbers or writing anywhere; two complete hands, and "
            "no ring of light surrounds them."
        ),
    },
    {
        "id": "v2-r177-b11", "out": "s11-right-there-above-the-lid.jpeg", "seg": "n2r",
        "window": "47.040-55.360", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABERNACLE-HOLY", "THE-ARK"],
        "narration": "There, God said — right there, above that lid, between those two carved angels — that is where I will meet you and talk with you.",
        "must_show": "the exact meeting place, named — a steady close on the mercy-seat lid and the space directly above it between the two carved gold cherubim, the one spot where God will meet and speak; right there, God unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being above the lid or between the cherubim; the two carved angels stay gold statues, not alive; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "A steady, quiet close framing the solid-gold mercy-seat lid and the "
            "still air directly above it, held between the two carved gold cherubim "
            "whose arched wings reach in from either side — the exact place named: "
            "right there, above that lid, between those two carved figures, where "
            "God will meet and speak. The space stays open, hushed and empty of "
            "any shape or face; warm lamp light rests on the gold. Nothing is "
            "written anywhere and no ring of light surrounds anything."
        ),
    },
    {
        "id": "v2-r177-b12", "out": "s12-he-gave-them-an-address.jpeg", "seg": "n2r",
        "window": "55.360-58.640", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABERNACLE-HOLY", "THE-ARK", "ISRAELITES"],
        "narration": "He gave them an address.",
        "must_show": "the fixed place set — the finished ark carried on its gold poles and set down in its appointed place in the holy tent, a settled and known spot; God gave them an address.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; the cherubim stay carved gold statues; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "In the lamplit holy place, two robed bearers lower the finished gold "
            "ark by its two gold carrying-poles and set it down in its appointed "
            "spot on the woven mat, the carved gold cherubim catching the lamp "
            "light — a fixed, known, settled place, an address where God had said "
            "He would be found. Ordinary-sized bearers with two hands and one "
            "head each, none in cream, intent on the ark and not the camera; "
            "nothing is written anywhere and no ring of light surrounds anything."
        ),
    },
    {
        "id": "v2-r177-b13", "out": "s13-i-am-near.jpeg", "seg": "n2b",
        "window": "58.640-62.812", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "every detail meant to say: I am near.",
        "must_show": "nearness — the central tabernacle tent seen close from within the ring of the people's tents, the dwellings pressed right up around it in the evening light; every detail says, I am near.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "A close, low view of the central tabernacle tent seen from within the "
            "ring of the people's dwelling tents, the ordinary homes pressed right "
            "up close around it, cook-fires and everyday life just steps away in "
            "the warm evening light — the whole arrangement saying plainly that "
            "God is near, in the middle of them. Ancient camp only; nothing is "
            "written anywhere and no ring of light surrounds the tent."
        ),
    },
    {
        "id": "v2-r177-b14", "out": "s14-for-theirs.jpeg", "seg": "n1a",
        "window": "62.812-66.357", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "ISRAELITES"],
        "narration": "Not for his sake. For theirs.",
        "must_show": "the people it was for — a close on a few ordinary faces of the camp near the tabernacle tent, quiet and comforted; not for God's sake but for theirs.",
        "must_not_show": "no God figure or beam-being; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A close on two or three ordinary faces of the camp — a weary father, "
            "a mother with a child — resting near the tabernacle tent in the "
            "evening light, their expressions quiet and comforted to have God "
            "settled among them. The tent sits soft behind them. Ordinary-sized, "
            "distinct people with one head each, none in cream, their eyes toward "
            "the tent and not the camera; nothing is written anywhere and no ring "
            "of light surrounds any head."
        ),
    },
    {
        "id": "v2-r177-b15", "out": "s15-in-the-middle-of-ordinary-days.jpeg", "seg": "n1b",
        "window": "66.357-72.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "ISRAELITES"],
        "narration": "So that he could dwell among them in the middle of their ordinary days.",
        "must_show": "ordinary life around the presence — everyday camp life going on close by the tabernacle tent: a woman grinding grain, a child playing, a man mending, all in easy nearness to the tent; God dwelling among their ordinary days.",
        "must_not_show": "no God figure or beam-being; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "Everyday life of the camp goes on close beside the central tabernacle "
            "tent in the warm daylight — a woman kneeling to grind grain, a child "
            "at play in the dust, a man mending a strap in a tent doorway — plain "
            "ordinary days lived out in easy nearness to the place where God "
            "dwells. The tent stands quiet among them. Ordinary-sized, distinct "
            "people with two hands and one head each, none in cream, absorbed in "
            "their work and not the camera; nothing is written anywhere and no "
            "ring of light surrounds anyone."
        ),
    },
    {
        "id": "v2-r177-b16", "out": "s16-a-people-on-the-move.jpeg", "seg": "n3a",
        "window": "72.200-76.417", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "ISRAELITES"],
        "narration": "The pattern was carried by a people on the move,",
        "must_show": "the camp on the move — the people striking the tents and setting out across the desert, the tabernacle's covered furniture borne along on poles among them; the pattern carried by a people on the move.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no modern vehicle, road or object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "The camera looks across the desert from behind the moving column as "
            "the people strike camp and set out — tents rolled and shouldered, "
            "the covered sacred furniture borne along on its poles by robed "
            "bearers among the walking crowd, dust rising over the stony plain and "
            "bare hills ahead. Ordinary-sized, distinct people seen mostly from "
            "behind, none in cream; nothing is written anywhere and no ring of "
            "light surrounds anyone."
        ),
    },
    {
        "id": "v2-r177-b17", "out": "s17-the-promise-was-fixed.jpeg", "seg": "n3b",
        "window": "76.417-81.167", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "THE-ARK", "ISRAELITES"],
        "narration": "yet the promise was fixed — God with his people.",
        "must_show": "the fixed promise amid the movement — the covered ark carried steady and central in the moving procession, the people close around it; whatever the journey, God stays with his people.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no modern object; no Jesus and no cream; no halo or ring of light; no scroll, writing or panel; no posed line facing the lens.",
        "scene": (
            "Within the moving procession the covered ark rides steady and central "
            "on its gold poles, borne on the shoulders of robed bearers with the "
            "people walking close around it across the desert — everything else "
            "shifting and travelling, but this one thing held fixed and near at "
            "the heart of them: God with his people. Ordinary-sized, distinct "
            "people, none in cream, intent on the ark and the way ahead and not "
            "the camera; nothing is written anywhere and no ring of light "
            "surrounds anything."
        ),
    },
    {
        "id": "v2-r177-b18", "out": "s18-a-tent-in-the-desert.jpeg", "seg": "n4",
        "window": "81.167-85.600", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "Centuries later that promise would take a face.",
        "must_show": "the tent at first light, forward-looking — the tabernacle tent standing in the camp under a clear dawn sky, quiet and hopeful; a promise here in a tent that would one day take a face — NO face shown yet.",
        "must_not_show": "NO Jesus and NO face of God or Christ anywhere — the 'face' is only spoken foreshadow; no God figure or beam-being; no cream; no modern object; no halo or ring of light; no scroll, writing or panel.",
        "scene": (
            "The tabernacle tent stands quiet in the camp under a clear, brightening "
            "dawn sky, the desert hills pale gold with first light and the "
            "dwelling tents still around it — a hopeful, forward-looking hush over "
            "the place where the promise began. Only the tent and the dawn are "
            "shown; no face of God or man is pictured. Nothing is written anywhere "
            "and no ring of light surrounds the tent."
        ),
    },
    {
        "id": "v2-r177-b19", "out": "s19-god-pitching-his-tent.jpeg", "seg": "n4",
        "window": "85.600-90.003", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP"],
        "narration": "But here it begins as a tent in the desert, God pitching his tent beside them.",
        "must_show": "the closing wide — the whole dawn camp with the tabernacle tent pitched right beside the people's tents, the soft cloud of presence resting over it; God pitching his tent beside them.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being in or above the cloud; no Jesus and no cream; no modern building, vehicle or object; no stone palace or temple; no halo or ring of light; no scroll, writing or panel; no posed faces to the lens.",
        "scene": (
            "The camera looks across the whole camp at dawn from a low rise in a "
            "high three-quarter view, past the backs of a few early risers below: "
            "the central tabernacle tent pitched right beside the people's dwelling "
            "tents, a soft formless cloud of presence resting quietly over it, the "
            "desert basin and pale hills opening beyond under the morning sky — "
            "God pitching His tent beside them, in the middle of the camp. The "
            "cloud carries no shape or face. Ancient encampment only, seen wide so "
            "no face turns to the camera; nothing is written anywhere and no ring "
            "of light surrounds the central tent."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# All three places are NEW (no stash plate yet); the runner promotes each from
# its own first good frame (b01 / b02 / b07), so PLACE_REFS stays empty here.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: every person is carried by a byte-identical text lock (no face
# sheets exist for these figures). NO Jesus in this row.
REFS = {
}
