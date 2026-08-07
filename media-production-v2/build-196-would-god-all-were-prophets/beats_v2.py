#!/usr/bin/env python3
"""V2 beat map — row 196, build-196-would-god-all-were-prophets (Numbers 11:16-17, 24-29 —
Moses is overwhelmed, the LORD shares the Spirit that rested on Moses with seventy elders,
Eldad and Medad prophesy in the camp, Joshua says "forbid them," and Moses answers: "Enviest
thou me for my sake? would God that all the LORD's people were prophets, and that the LORD
would put his spirit upon them!").

COVERAGE: 16 pictures over 60.100 s (card_start) = ~3.76 s/picture (lesson 12 movie-coverage).
ONE place: the WILDERNESS-CAMP (the Sinai camp of tents with the central tabernacle tent —
BYTE-IDENTICAL to build-177, the same Exodus/Numbers encampment). The tent-of-meeting scenes
are shots at the central tabernacle tent within that same camp; the Eldad/Medad, runner and
Joshua scenes are out among the tents. Human spine: MOSES, crushed by the burden, who does NOT
guard the gift but wishes it wider over every tent.

=====================================================================
No open Cameron complaint (v2_outline.py 196). Fresh V2 beat map; Board Audio = OK.
=====================================================================

SPEAKER LAW (Old-Testament narrative, book of Numbers):
  s0  Numbers 11:28  "My lord Moses, forbid them."                        = JOSHUA's words
      → SCRIPTURE → LIGHT-BLUE caption (not a God-voice, not red).
  s1  Numbers 11:29  "Enviest thou me for my sake? would God that all the LORD's people
      were prophets, and that the LORD would put his spirit upon them!"   = MOSES's words
      → SCRIPTURE → LIGHT-BLUE caption.
Every other segment (n0, n1a, n1b, n2, n3a, n3b, n4, card) is the NARRATOR → white. There is
NO red-letter and NO God-voice segment in this row (the narrator REPORTS what God told Moses;
God never speaks on-screen). **NO Jesus / NO cream / NO white** anywhere (Old Testament; cream
is reserved for Jesus, who is absent).

**HARD GATE — GOD AND THE SPIRIT ARE NEVER EMBODIED.** "God told Moses" (n1a), "the Spirit
that rested on Moses" (n1b), "the Spirit came down on those seventy" / "the Spirit came on
them too" (n2), "the LORD would put his spirit upon them" (s1) are NEVER a divine figure,
face, dove, flame, tongue of fire, beam, hand-from-sky, ring or symbol. Numbers 11 describes
NO fire (that is Pentecost — do NOT import it). The Spirit resting and the men prophesying are
carried ONLY by the MEN themselves — faces alight with conviction, mouths open speaking God's
words, hands lifted — under warm natural daylight. The "sharing" of the Spirit (b04) is shown
by Moses among the reverent elders, NOT by any visible substance or beam passing between them.
Drift-word gate: no halo / glow / rim-light / beam in any scene text.

CONTENT-CARE: the "weight crushing Moses" (b01/b02) is weariness and burden — a bowed, tired
old man — never despair, collapse or anything gory. Joshua's alarm (b10/b11/b12) is earnest
concern, never anger or violence. Moses's answer (b13/b14) is warm and generous, never
rebuking or proud. The prophesying elders and Eldad/Medad are joyful/earnest, never in a
frenzy or trance.

TIME-OF-DAY: warm late-afternoon daylight throughout, so every face, gesture and the spread
of tents reads clearly. Not night; no divine light.

PLACES / LOCKS:
  WILDERNESS-CAMP  the Sinai camp of tents with the central tabernacle tent — reused
                   BYTE-IDENTICAL to build-177 (the same encampment across the Torah videos).
                   Every beat is in this one camp. NEW here only in that build-177 is not yet
                   built (no committed plate exists); runner promotes WILDERNESS-CAMP from b01
                   — or `--wire` build-177's plate once that row is built, IF its daylight
                   matches (177's plate is dusk; this row is late-afternoon daylight).
People locks: MOSES (BYTE-IDENTICAL to build-177 — recurring cast), ISRAELITES (BYTE-IDENTICAL
to build-177 — the camp people), SEVENTY-ELDERS (the seventy trusted elders), ELDAD-MEDAD (the
two men who stayed in the camp), JOSHUA (Moses's young aide), CAMP-RUNNER (the young man who
runs with the news). None wear cream or white.

AUDIO: default AUDIO LOCK stream-copy (no re-voice; no open complaint). Board Audio = OK.
card_start = 60.100 s. Picture-only — do NOT re-voice.
"""

# WILDERNESS-CAMP + MOSES + ISRAELITES are reused BYTE-IDENTICAL to build-177 (recurring
# place/cast). SEVENTY-ELDERS, ELDAD-MEDAD, JOSHUA and CAMP-RUNNER are build-local. Jesus is
# absent (every beat jesus=False); no image REFS; only text locks. No one wears cream/white;
# God and the Spirit are never embodied.
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
        "ISRAELITES LOCK: the people of the camp are a mixed, "
        "diverse crowd of ordinary Hebrew men, women and children of the ancient "
        "world, in varied dusty earth-toned hand-woven wool and linen, none in "
        "cream and none in white robes, some carrying tools, bundles or "
        "water-skins. Distinct, ordinary-sized people with two hands and one head "
        "each, never twinned, never cloned faces, never modern clothing, tools, "
        "flags or signage."
    ),
    "SEVENTY-ELDERS": (
        "SEVENTY-ELDERS LOCK: the seventy trusted elders of Israel — grave, "
        "respected older Hebrew men, mostly grey- or dark-bearded, in plain "
        "earth-toned wool robes (never cream, never white), gathered about Moses "
        "at the tabernacle tent. Distinct individual faces, a range of ages and "
        "builds, never twins or cloned faces; ordinary-sized men."
    ),
    "ELDAD-MEDAD": (
        "ELDAD-MEDAD LOCK: two ordinary Hebrew men of the camp who stayed back "
        "among the tents — one about forty with a dark beard, one about fifty with "
        "a greying beard, both in plain earth-toned wool (never cream, never "
        "white); clearly two different, distinct men, never twins. The same two "
        "men wherever they appear."
    ),
    "JOSHUA": (
        "JOSHUA LOCK: Moses's young aide — a strong Hebrew man of about thirty-five, "
        "short dark hair and a short dark beard, in a plain belted earth-toned tunic "
        "and mantle (never cream, never white), earnest and dutiful. The same man "
        "wherever he appears; ordinary-sized, two hands, one head."
    ),
    "CAMP-RUNNER": (
        "CAMP-RUNNER LOCK: a young Hebrew man of about twenty who runs with the "
        "news — lean, short dark hair, beardless or light-bearded, in a short "
        "belted earth-toned tunic hitched for running (never cream, never white). "
        "The same young man wherever he appears; ordinary-sized."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r196-b01", "out": "s01-the-weight.jpeg", "seg": "n0",
        "window": "0.000-3.900", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "ISRAELITES"],
        "narration": "The weight of leading a whole nation was crushing Moses.",
        "must_show": "the establishing wide (NON-Jesus, the plate the runner promotes) — the vast Sinai camp of tents, Moses bowed and weary in the foreground with the whole encamped nation spread behind him; the crushing weight of leading them all.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, face, dove, flame or beam; no halo or ring of light; no modern object, vehicle, pole or wire; no rendered writing; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the wilderness camp in warm late-afternoon daylight, "
            "camera set behind and above Moses's shoulder on a low rise so his bowed back "
            "is three-quarters to the lens and his gaze goes out and down over the sprawling "
            "camp, never to the camera: Moses — a weathered grey-bearded elder in an "
            "earth-toned robe (not cream), a wooden staff loose in his hand — stands stooped "
            "under the burden while dozens of dark goats'-hair tents and the central "
            "tabernacle tent spread across the stony basin, the people small among them. A "
            "real encampment, no one lined up facing the lens. Ordinary-sized people on one "
            "ground plane; warm daylight over the camp, not around any head; nothing is "
            "written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b02", "out": "s02-cannot-carry-alone.jpeg", "seg": "n0",
        "window": "3.900-8.050", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES"],
        "narration": "He told the LORD he could not carry the people alone, not one more day.",
        "must_show": "Moses alone at the tabernacle tent, head bowed and hands open, pouring out to the LORD that he cannot carry the people alone — the LORD is NOT shown, only Moses praying.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, face, dove, flame or beam; no halo or ring of light; no modern object; no rendered writing; not a cartoon.",
        "scene": (
            "A medium on Moses (not cream) at the entrance of the central tabernacle tent in "
            "warm daylight, alone: head bowed, hands turned open at his sides, his weathered "
            "face lifted in weary appeal as he pours out to the LORD that he cannot carry "
            "the people alone one more day. No figure answers him — the LORD is not shown. "
            "His gaze is up and away, not to the camera; warm daylight on his face and the "
            "dark tent curtains, not around his head; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r196-b03", "out": "s03-gather-me-seventy.jpeg", "seg": "n1a",
        "window": "8.050-11.680", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "SEVENTY-ELDERS"],
        "narration": "So God told Moses to gather seventy trusted men.",
        "must_show": "Moses calling and gathering the seventy trusted elders to the tabernacle tent — grave older men coming together around him at his summons.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no modern object; no rendered writing; not a cartoon.",
        "scene": (
            "A shot at the tabernacle tent in warm daylight: Moses (not cream), one hand "
            "raised in summons, gathers the seventy grave elders (earth-toned robes, distinct "
            "faces) who come together around him — trusted men called to share the load. "
            "Ordinary-sized men on one ground plane, one head each, their gazes toward Moses "
            "and the tent, not to the camera; warm daylight on them, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b04", "out": "s04-the-spirit-shared.jpeg", "seg": "n1b",
        "window": "11.680-15.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "SEVENTY-ELDERS"],
        "narration": "He would take some of the Spirit that rested on Moses and share it with them,",
        "must_show": "the sharing — Moses standing among the elders gathered close and reverent at the tent, the Spirit that rested on him about to rest on them; shown ONLY by Moses and the elders, NO visible substance or beam passing between them.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame, tongue of fire or beam; no visible spirit-substance or light passing between people; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close group shot at the tabernacle tent in warm daylight: Moses (not cream) "
            "stands among the seventy elders drawn close and reverent, heads bowed, the "
            "moment the Spirit that rested on him is about to rest on them — carried only by "
            "their gathered stillness and Moses at the centre, nothing visible passing "
            "between them, no substance, no beam. Ordinary-sized men, one head each, gazes "
            "inward and down in reverence, not to the camera; warm daylight on the group, not "
            "around any head; nothing is written anywhere; no divine figure or spirit-form."
        ),
    },
    {
        "id": "v2-r196-b05", "out": "s05-bear-the-load-together.jpeg", "seg": "n1b",
        "window": "15.000-18.320", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "SEVENTY-ELDERS"],
        "narration": "and together they would help bear the load.",
        "must_show": "the load shared — Moses and the elders now standing together, shoulder to shoulder, ready to help carry the burden of the people; relief and resolve on Moses's face.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot at the tabernacle tent in warm daylight: Moses (not cream) now stands "
            "shoulder to shoulder with the elders, no longer alone — resolve and relief on "
            "his weathered face as they turn together toward the waiting camp, ready to bear "
            "the load with him. Ordinary-sized men on one ground plane, one head each, gazes "
            "out toward the camp, not to the camera; warm daylight on them, not around any "
            "head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b06", "out": "s06-seventy-prophesy.jpeg", "seg": "n2",
        "window": "18.320-22.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "SEVENTY-ELDERS"],
        "narration": "When the Spirit came down on those seventy, they began to speak God's words.",
        "must_show": "the seventy prophesying — the elders' faces alight with conviction, mouths open speaking God's words, hands lifted; the Spirit shown ONLY by the men themselves, no figure/dove/flame.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame, tongue of fire or beam; no halo, ring or beam of light; no frenzy or trance; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of the seventy elders at the tabernacle tent in warm daylight, faces "
            "suddenly alight with conviction, mouths open speaking God's words, several hands "
            "lifted — they have begun to prophesy. The Spirit is shown only through the "
            "changed, earnest men themselves; nothing descends, no dove, no flame, no beam. "
            "Joyful and earnest, not a frenzy. Ordinary-sized men, one head each, gazes "
            "upward and outward in conviction, not to the camera; warm daylight on their "
            "faces, not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b07", "out": "s07-eldad-and-medad.jpeg", "seg": "n2",
        "window": "22.400-26.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "ELDAD-MEDAD"],
        "narration": "But two men, Eldad and Medad, had stayed back in the camp —",
        "must_show": "the two men, Eldad and Medad, out among the ordinary tents of the camp — clearly two distinct men who had NOT gone up to the tabernacle tent with the others.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no modern object; nothing written; not a cartoon; the two men are distinct, not twins.",
        "scene": (
            "A shot among the ordinary goats'-hair tents of the camp in warm daylight: two "
            "distinct men — Eldad, about forty and dark-bearded, and Medad, about fifty and "
            "greying (both earth-toned wool, not cream) — stand together by their tents, the "
            "central tabernacle tent small in the distance behind them; they had stayed back "
            "in the camp. Ordinary-sized, one head each, gazes between them and toward the "
            "camp, not to the camera; warm daylight on them, not around any head; nothing is "
            "written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b08", "out": "s08-spirit-among-the-tents.jpeg", "seg": "n2",
        "window": "26.500-30.950", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "ELDAD-MEDAD"],
        "narration": "and the Spirit came on them too, right there among the tents.",
        "must_show": "Eldad and Medad prophesying right there among the tents — their faces alight, mouths open speaking God's words, just like the seventy, far from the tabernacle tent; Spirit shown ONLY by the two men.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame, tongue of fire or beam; no halo, ring or beam of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot among the tents in warm daylight: Eldad and Medad (not cream), faces "
            "alight with the same conviction, mouths open speaking God's words and hands "
            "lifted — the Spirit has come on them too, right there among the ordinary tents, "
            "far from the tabernacle. Shown only through the two changed men; nothing "
            "descends, no dove, no flame, no beam. A few camp folk nearby turn, startled. "
            "Ordinary-sized people, one head each, gazes upward and outward, not to the "
            "camera; warm daylight on them, not around any head; nothing is written anywhere; "
            "no divine figure."
        ),
    },
    {
        "id": "v2-r196-b09", "out": "s09-the-runner.jpeg", "seg": "n3a",
        "window": "30.950-33.630", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "CAMP-RUNNER"],
        "narration": "A runner hurried to Moses with the news.",
        "must_show": "a young man running hard through the lanes of the camp toward the tabernacle tent, carrying the news to Moses.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot along a lane of the camp in warm daylight: a lean young man in a short "
            "hitched earth-toned tunic (not cream) runs hard between the goats'-hair tents "
            "toward the central tabernacle tent ahead of him, urgency on his face — carrying "
            "the news to Moses. His travel goes forward into frame toward the distant tent, "
            "his gaze ahead, not to the camera; warm daylight on the lane, not around his "
            "head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b10", "out": "s10-joshua-worried.jpeg", "seg": "n3b",
        "window": "33.630-38.700", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "JOSHUA", "MOSES"],
        "narration": "Joshua, Moses's right-hand man, was worried — stop them, he said.",
        "must_show": "Joshua, alarmed, turning to Moses at the tabernacle tent and urging him to stop Eldad and Medad — earnest concern, not anger.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no anger or violence; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot at the tabernacle tent in warm daylight: Joshua (not cream), a strong "
            "young dark-bearded man, turns to Moses with alarm on his face, one hand gesturing "
            "back toward the tents, urging him to stop the two men — earnest worry, not anger. "
            "Moses (not cream) stands calm beside him. Ordinary-sized, one head each, their "
            "gazes between each other and back toward the camp, not to the camera; warm "
            "daylight on them, not around any head; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r196-b11", "out": "s11-not-how-it-works.jpeg", "seg": "n3b",
        "window": "38.700-41.530", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "JOSHUA"],
        "narration": "That is not how it is supposed to work.",
        "must_show": "a close on Joshua's troubled face — convinced the gift belongs only to the appointed seventy, not to two men left in the camp; earnest, protective concern.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no anger or violence; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Joshua (not cream) in warm daylight, brow furrowed, troubled — sure "
            "in his heart that the gift belongs only to the appointed seventy and not to two "
            "men left down in the camp; earnest, protective concern. His gaze is off toward "
            "the tents, not to the camera; warm daylight on his face, not around his head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b12", "out": "s12-forbid-them.jpeg", "seg": "s0",
        "window": "41.530-44.810", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "JOSHUA", "MOSES"],
        "narration": "My lord Moses, forbid them.",
        "must_show": "BLUE caption (SCRIPTURE — Joshua's words) — Joshua appealing directly to Moses, 'my lord Moses, forbid them,' one hand toward the camp; Moses listening.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no anger or violence; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot at the tabernacle tent in warm daylight: Joshua (not cream) appeals "
            "directly to Moses, one hand thrown toward the camp — 'my lord Moses, forbid "
            "them' — his young face urgent; Moses (not cream) listens, unruffled and kind. "
            "Ordinary-sized, one head each, Joshua's gaze on Moses, Moses's gaze steady on "
            "Joshua, not to the camera; warm daylight on them, not around any head; nothing "
            "is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b13", "out": "s13-enviest-thou-me.jpeg", "seg": "s1",
        "window": "44.810-48.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "JOSHUA"],
        "narration": "Enviest thou me for my sake?",
        "must_show": "BLUE caption (SCRIPTURE — Moses's words) — a close on Moses answering Joshua warmly and gently, no jealousy in him, 'enviest thou me for my sake?'; his face generous, not rebuking.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no anger, pride or rebuke; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Moses (not cream) in warm daylight, turning to Joshua with a warm, "
            "gentle expression — no jealousy in him at all — as he asks, unhurried, 'enviest "
            "thou me for my sake?' A generous, kindly old face, never rebuking. His gaze is "
            "on Joshua at frame edge, not to the camera; warm daylight on his face, not "
            "around his head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b14", "out": "s14-would-god-all-were-prophets.jpeg", "seg": "s1",
        "window": "48.500-53.380", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "ISRAELITES"],
        "narration": "would God that all the LORD's people were prophets, and that the LORD would put his spirit upon them!",
        "must_show": "BLUE caption (SCRIPTURE — Moses's words) — the wide wish: Moses's arm swept open over the WHOLE camp of tents and all the people, wishing the gift on every one of them; the LORD's Spirit is NOT shown, only Moses and the camp.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no visible spirit over the camp; no halo, ring or beam of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A wide at the camp's edge in warm daylight, camera behind Moses's shoulder so his "
            "back and lifted arm are three-quarters to the lens and his gaze sweeps out over "
            "the whole camp, never to the camera: Moses (not cream) throws his arm open wide "
            "across the dozens of tents and all the people spread before him, wishing the "
            "LORD's Spirit on every one of them. Nothing hangs over the camp — no spirit, no "
            "beam, no light-form; only the old man and the tents in daylight. Ordinary-sized "
            "people on one ground plane; warm daylight over the camp, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r196-b15", "out": "s15-most-generous-answer.jpeg", "seg": "n4",
        "window": "53.380-56.700", "wide": False, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES"],
        "narration": "One of the most generous answers in all of scripture.",
        "must_show": "a close on Moses's warm, open, generous face — the most generous answer in scripture; a man glad to see the gift spread, not guarded.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Moses (not cream) in warm daylight, his weathered face open, warm and "
            "generous, a faint glad smile — a man delighted, not threatened, to see God's "
            "gift spread wide. His gaze is out over the camp, not to the camera; warm "
            "daylight on his face, not around his head; nothing is written anywhere; no "
            "divine figure."
        ),
    },
    {
        "id": "v2-r196-b16", "out": "s16-wished-it-wider.jpeg", "seg": "n4",
        "window": "56.700-60.100", "wide": True, "jesus": False, "ref": False,
        "locks": ["WILDERNESS-CAMP", "MOSES", "ISRAELITES"],
        "narration": "Moses did not guard the gift — he wished it wider.",
        "must_show": "the closing image — Moses among his people, open-handed toward the whole camp of tents, having wished the gift wider over every tent rather than guarding it for the few.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no visible spirit over the camp; no halo, ring or beam of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing wide in warm daylight, camera at eye level a little behind Moses so his "
            "back is three-quarters to the lens and his gaze and open hands go out over the "
            "camp, never to the camera: Moses (not cream) stands among his people, hands open "
            "toward the whole spread of tents, having wished the gift wider over every tent "
            "instead of guarding it for the few — ordinary men, women and children of the "
            "camp turning toward him. Nothing hangs over the camp — no spirit, no beam, no "
            "light-form. Ordinary-sized people on one ground plane; warm daylight over the "
            "camp, not around any head; nothing is written anywhere; no divine figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# WILDERNESS-CAMP is reused byte-identical to build-177 (same Sinai encampment). build-177 is
# not built yet, so no committed plate exists; the runner promotes WILDERNESS-CAMP from b01 —
# or --wire build-177's plate once that row is built, IF the daylight matches (177 is dusk;
# this row is late-afternoon daylight). All frames are NON-Jesus. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: all places and people are carried by the build-local text locks above
# (WILDERNESS-CAMP, MOSES and ISRAELITES byte-identical to build-177). Jesus does not appear in
# this row (every beat jesus=False); no one wears cream or white; God and the Spirit are never
# embodied.
REFS = {
}
