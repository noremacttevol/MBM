#!/usr/bin/env python3
"""V2 beat map — row 192, build-192-the-fast-god-has-chosen (Isaiah 58:6-8 — "Is not this
the fast that I have chosen? to loose the bands of wickedness, to undo the heavy burdens,
and to let the oppressed go free, and that ye break every yoke? Is it not to deal thy bread
to the hungry, and that thou bring the poor that are cast out to thy house? when thou seest
the naked, that thou cover him... Then shall thy light break forth as the morning...").

COVERAGE: 16 pictures over 65.139 s (card_start) = ~4.07 s/picture (lesson 12
movie-coverage). Three places: the TOWN (an Old Testament Israelite town — its square and
streets, where Isaiah declares, where the empty show-fast is kept, and where bonds and
yokes are loosed), the HOME (a poor Israelite family's house — doorway, threshold, low
table and hearth, where bread is shared, the cast-out poor are taken in, and the naked are
covered), and DAYBREAK (the same town and land at daybreak, the light breaking forth as the
morning). Human spine: a representative DOER — the "thou" of Isaiah 58 who stops the hollow
fast and keeps the true one (loosing bonds, feeding, sheltering, clothing) — with his WIFE
beside him; ISAIAH the prophet carries the LORD's words; THE-NEEDY are those he serves.

=====================================================================
No open Cameron complaint (v2_outline.py 192). Fresh V2 beat map; Board Audio = OK.
=====================================================================

SPEAKER LAW (see make_narration.py — Isaiah is an Old Testament prophet; the LORD speaks
through him). The GOD-voice segments carry GREEN captions:
  s1  Isaiah 58:6  "Is not this the fast that I have chosen? ... break every yoke?"  GOD
  g7  Isaiah 58:7  "Is it not to deal thy bread to the hungry ... thine own flesh?"   GOD
  s2  Isaiah 58:8  "Then shall thy light break forth as the morning ..."             GOD
Every other segment (n0, n1a, n1b, n2, n3, card) is the NARRATOR → white. There is NO
red-letter and NO Jesus in this row: **every beat jesus=False and NO ONE wears cream or
white** (cream is reserved for Jesus, who is absent — this is the Old Testament).

**HARD GATE — GOD / THE LORD IS NEVER EMBODIED.** s1, g7 and s2 are the GOD-voice (green
captions), but the LORD is NEVER shown. The words are carried by ISAIAH the prophet
declaring them, by the acts of mercy themselves, and by the breaking dawn — never by any
figure, face, hand, throne, beam-as-person, dove or symbol. The "light breaking forth as
the morning" is a real daybreak — warm gold light rising over the rooftops and hills, NEVER
a figure or a face in the sky, NEVER a ring or beam shaped like a person. No halo, ring or
rim-light around anyone's head (drift-word gate — word the light as radiant / warm / golden
morning).

CONTENT-CARE: the bondage the true fast undoes is shown as RELIEF and LIBERATION, never
violence or gore — cords slipping from a freed man's wrists, a crushing load lifted off a
bent back, a wooden yoke raised off a bowed neck and set down; no wounds, no blood, no
striking. The empty show-fast (b02) is hollow religiosity — bowed heads, sackcloth and a
little ash, a hungry performance — reverent, not mocking or grotesque. The acts of mercy
are warm and dignified; the poor and the naked keep their dignity (a shivering person is
covered gently, not exposed).

TIME-OF-DAY: the TOWN and HOME scenes are warm ordinary daylight; the DAYBREAK scenes are a
real sunrise breaking gold over the town — no night, no divine glow.

PLACES / LOCKS (all three are NEW build-local places — no committed plate yet; the runner
promotes each from its first NON-Jesus frame, and every frame in this row is NON-Jesus):
  TOWN      the Israelite town square & streets (b01/b02/b03/b04/b05) — promote from b01.
  HOME      the poor family's house & doorway (b06/b07/b08/b09/b10/b11/b12) — promote b06.
  DAYBREAK  the town & land at sunrise (b13/b14/b15/b16) — promote from b13.
People locks: ISAIAH (the prophet), DOER (the representative householder — the "thou"),
WIFE (the doer's wife, serving beside him), THE-NEEDY (the bound, hungry, cast-out and
naked he serves), TOWNSFOLK (God's people Isaiah addresses; the empty-fast keepers in b02).
None wear cream or white.

AUDIO: default AUDIO LOCK stream-copy (no re-voice; no open complaint). Board Audio = OK.
card_start = 65.139 s. Picture-only — do NOT re-voice.
"""

# All three places + the people are declared as build-local text LOCKS here; PLACE_REFS
# stays empty and the runner promotes each place from its first NON-Jesus frame (see QC.md).
# No one wears cream/white (this is OT; Jesus is absent).
LOCKS = {
    "TOWN": (
        "TOWN LOCK: the same place in every frame — an Old Testament Israelite town: a "
        "small dusty open square and its narrow streets, low mud-brick and dressed-stone "
        "houses with flat roofs and dark doorways, a stone well-head and a few market "
        "stalls, worn steps and a town wall beyond. Ancient and real; no modern object "
        "anywhere, and nothing legible or rendered is written on any surface. The same "
        "square and streets throughout, in warm ordinary daylight."
    ),
    "HOME": (
        "HOME LOCK: the same place in every frame — a poor Israelite family's house: a "
        "plain stone-and-mud-brick dwelling with a broad low timber door and threshold, a "
        "single room within holding a low wooden table, woven floor-mats, clay bowls and "
        "jars, a small hearth and folded blankets. Ancient and spare; no modern object "
        "anywhere, and nothing written. The same doorway, threshold and room throughout, "
        "in warm ordinary daylight."
    ),
    "DAYBREAK": (
        "DAYBREAK LOCK: the same place in every frame — the Israelite town and the land "
        "around it at sunrise: the flat rooftops, the town wall and the low hills beyond, "
        "with the first warm gold light of morning rising over the horizon and touching "
        "the stone. It is a real daybreak — the light fills the sky and rests on the "
        "rooftops and hills; it is NEVER a figure, a face or a hand in the sky and never a "
        "beam or ring shaped like a person. Ancient and real; no modern object anywhere, "
        "and nothing written. The same town and hills at the same sunrise throughout."
    ),
    "ISAIAH": (
        "ISAIAH LOCK: the same man in every frame he appears — Isaiah, an Old Testament "
        "prophet of about fifty-five, warm tan sun-worn skin, dark hair going grey and a "
        "full dark-grey beard, deep steady eyes, in a plain undyed brown-and-ochre wool "
        "prophet's robe with a coarse mantle (never cream, never white). Grave, earnest "
        "and unafraid, one arm often raised as he declares. The same face, beard and robe "
        "throughout."
    ),
    "DOER": (
        "DOER LOCK: the same man in every frame he appears — a representative Israelite "
        "householder of about forty, the 'thou' of the passage, warm olive-brown skin, "
        "short dark beard streaked grey, weathered strong hands, in a plain dust-brown "
        "wool tunic and mantle (never cream, never white). He stops the hollow fast and "
        "keeps the true one — loosing bonds, sharing bread, taking the poor in, covering "
        "the cold. The same face, beard and clothing throughout."
    ),
    "WIFE": (
        "WIFE LOCK: the same woman in every frame she appears — the doer's wife of about "
        "thirty-five, warm olive-brown skin, dark hair covered by a modest deep-red and "
        "brown headscarf, in a plain russet-brown wool dress and mantle (never cream, "
        "never white). She serves beside her husband — carrying bread, welcoming the poor, "
        "laying a blanket over the cold. The same face and clothing throughout."
    ),
    "THE-NEEDY": (
        "THE-NEEDY LOCK: the ones the true fast serves — distinct individual "
        "first-century poor people, not twins: a bound and burdened captive (cords at his "
        "wrists, a heavy load on his back, a wooden yoke on his shoulders), a gaunt hungry "
        "man, a cast-out poor family with two thin children, and a shivering half-clad "
        "person. Plain ragged, dust-worn earth-toned wool (never cream, never white); they "
        "keep their dignity throughout. Distinct faces, the same kind of people throughout."
    ),
    "TOWNSFOLK": (
        "TOWNSFOLK LOCK: the people of the town — a mixed group of ordinary Old Testament "
        "Israelite men, women and a few children in plain earth-toned wool (never cream, "
        "never white); the people Isaiah addresses, and in the empty-fast frame those who "
        "fast to be seen, in sackcloth with a little ash. Distinct individual faces, not "
        "twins. The same kind of people throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r192-b01", "out": "s01-isaiah-declares.jpeg", "seg": "n0",
        "window": "0.000-3.400", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOWN", "ISAIAH", "TOWNSFOLK"],
        "narration": "Isaiah told God's people what kind of fast the LORD actually wants",
        "must_show": "the establishing wide, NON-Jesus (the TOWN plate) — Isaiah the prophet standing in the town square before God's people, one arm raised as he declares what fast the LORD truly wants.",
        "must_not_show": "no Jesus and no one in cream or white; no God or LORD figure anywhere; no halo, glare or rim-light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the Old Testament town square in warm daylight, camera "
            "set low and slightly behind the townspeople looking across the square toward "
            "Isaiah, so the people are three-quarters to the lens and their gaze travels "
            "inward and forward onto the prophet and exits the frame toward him, never to "
            "the camera. Isaiah — a grey-bearded prophet in plain brown-and-ochre wool (not "
            "cream) — stands on the worn steps, one arm raised, declaring to God's people "
            "gathered before him; the low stone houses and town wall rise beyond. Ancient "
            "and real; warm daylight rests on the stone, not around anyone's head; nothing "
            "is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b02", "out": "s02-the-empty-fast.jpeg", "seg": "n0",
        "window": "3.400-6.614", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "TOWNSFOLK"],
        "narration": "— not just going hungry to look holy.",
        "must_show": "a close on the empty show-fast — townsfolk bowed in sackcloth with a little ash, going hungry to be seen as holy, hollow and performing; the point is that this is not the fast the LORD wants.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no mockery or grotesque faces (reverent, not cruel); no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on two or three townsfolk in the town in warm daylight keeping the "
            "hollow fast — bowed heads, plain sackcloth, a little grey ash on the brow, "
            "faces drawn and performing their hunger to be seen as holy. Plain earth-toned "
            "wool and sackcloth (none cream). Ordinary-sized people, one head each, gazes "
            "downcast and inward, not to the camera; warm daylight on them, not around any "
            "head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b03", "out": "s03-the-fast-i-have-chosen.jpeg", "seg": "s1",
        "window": "6.614-11.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "ISAIAH", "TOWNSFOLK"],
        "narration": "Is not this the fast that I have chosen?",
        "must_show": "GREEN caption (GOD-voice, spoken through the prophet) — Isaiah before the people, hand open, asking the LORD's question: is not THIS the fast I have chosen? God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure, face, hand-from-sky, throne or beam; no Jesus and no one in cream or white; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Isaiah on the steps in the town square in warm daylight, one hand "
            "open toward the people as he speaks the LORD's question — is not this the fast "
            "I have chosen? The townsfolk look up to him, caught by the words. Only the "
            "prophet carries the words; no figure stands in for the LORD. Brown-and-ochre "
            "wool (not cream). Ordinary-sized people, one head each, gazes on Isaiah and "
            "not to the camera; warm daylight, no ring of light around any head; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r192-b04", "out": "s04-loose-the-bands.jpeg", "seg": "s1",
        "window": "11.500-16.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "DOER", "THE-NEEDY"],
        "narration": "to loose the bands of wickedness, to undo the heavy burdens,",
        "must_show": "GREEN caption (GOD-voice) — the true fast acted out: the DOER loosing the cords from a bound captive's wrists and lifting a crushing load off his back — bonds of wickedness loosed, heavy burdens undone. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol; no Jesus and no one in cream or white; no violence, no wounds, no blood (relief, not striking); no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot in a town street in warm daylight: the doer in dust-brown wool (not "
            "cream) crouches and loosens the cords from a bound captive's wrists while "
            "lifting a heavy load off the man's bent back — the bands of wickedness loosed, "
            "the heavy burden undone. The freed man straightens in relief; the cords slip "
            "away, no cutting or striking. Ordinary-sized men, one head each, gazes on the "
            "freeing hands between them, not to the camera; warm daylight on them, not "
            "around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b05", "out": "s05-break-every-yoke.jpeg", "seg": "s1",
        "window": "16.500-21.665", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN", "DOER", "THE-NEEDY"],
        "narration": "and to let the oppressed go free, and that ye break every yoke?",
        "must_show": "GREEN caption (GOD-voice) — the oppressed set free: the DOER lifting a heavy wooden yoke up off a bowed man's neck and setting it down, the man rising free — every yoke broken. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol; no Jesus and no one in cream or white; no violence or blood; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the town in warm daylight: the doer lifts a heavy wooden yoke up and "
            "off the neck and shoulders of a bowed, oppressed man and sets it down on the "
            "ground; the man straightens and rises free, relief and light in his face. "
            "Plain dust-brown and ragged wool (none cream). Ordinary-sized men, one head "
            "each, gazes on the lifted yoke and each other, not to the camera; warm "
            "daylight, no ring around any head; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r192-b06", "out": "s06-bread-to-the-hungry.jpeg", "seg": "g7",
        "window": "21.665-26.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "DOER", "THE-NEEDY"],
        "narration": "Is it not to deal thy bread to the hungry,",
        "must_show": "GREEN caption (GOD-voice) — the establishing HOME frame (NON-Jesus, the HOME plate): the DOER at his own doorway placing a loaf of bread into the hands of a gaunt hungry man. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol; no Jesus and no one in cream or white; no halo, glare or rim-light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing medium at the home doorway in warm daylight, camera a little "
            "to the side so both men are three-quarters to the lens and their gaze meets "
            "over the bread, not the camera: the doer in dust-brown wool (not cream) stands "
            "on his own threshold and places a whole loaf of bread into the open hands of a "
            "gaunt hungry man — dealing his bread to the hungry. The plain stone house, "
            "broad timber door and hearth beyond. Ordinary-sized men, one head each; warm "
            "daylight rests on them, not around any head; nothing is written anywhere; no "
            "divine figure."
        ),
    },
    {
        "id": "v2-r192-b07", "out": "s07-bring-the-poor-home.jpeg", "seg": "g7",
        "window": "26.500-32.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "DOER", "WIFE", "THE-NEEDY"],
        "narration": "and that thou bring the poor that are cast out to thy house?",
        "must_show": "GREEN caption (GOD-voice) — the doer and his wife bringing a cast-out poor family with two thin children in over their own threshold and into their home. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol; no Jesus and no one in cream or white; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot at the home threshold in warm daylight: the doer holds the broad timber "
            "door open and his wife (russet-brown dress and headscarf, not cream) reaches a "
            "welcoming hand to a cast-out poor family — a weary father, mother and two thin "
            "children in ragged wool — drawing them in over the threshold into the warm "
            "room. Bringing the poor that are cast out to their house. Ordinary-sized "
            "people, one head each, gazes on one another and into the home, not to the "
            "camera; warm daylight and the hearth-light within, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b08", "out": "s08-cover-the-naked.jpeg", "seg": "g7",
        "window": "32.000-38.683", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "WIFE", "THE-NEEDY"],
        "narration": "when thou seest the naked, that thou cover him; and that thou hide not thyself from thine own flesh?",
        "must_show": "GREEN caption (GOD-voice) — the wife laying a warm blanket gently over the shoulders of a shivering, half-clad person inside the home — covering the naked, and not hiding from one's own flesh and kin. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol; no Jesus and no one in cream or white; no nudity or exposure (the cold person is covered gently, keeping dignity); no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot inside the home in warm daylight: the wife (russet-brown, not cream) "
            "lays a thick woven blanket gently over the shoulders of a shivering, half-clad "
            "person seated by the hearth, wrapping them warm — covering the naked and not "
            "hiding from her own flesh. The cold person is covered and dignified, never "
            "exposed. Ordinary-sized people, one head each, gazes on the wrapping hands and "
            "each other, not to the camera; warm hearth-light, not around any head; nothing "
            "is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b09", "out": "s09-share-your-bread.jpeg", "seg": "n1a",
        "window": "38.683-41.660", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "DOER", "WIFE", "THE-NEEDY"],
        "narration": "Share your bread with the hungry.",
        "must_show": "the family sharing a meal — the doer and his wife breaking bread with the hungry man and the poor family around the low table inside the home, all eating together.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot around the low table inside the home in warm daylight: the doer and his "
            "wife (none cream) breaking a loaf and sharing it with the hungry man and the "
            "poor family, all seated together on the floor-mats eating from clay bowls — "
            "bread shared, no one apart. Ordinary-sized people, one head each, gazes on the "
            "shared bread and one another, not to the camera; warm light on the meal, not "
            "around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b10", "out": "s10-bring-them-in.jpeg", "seg": "n1b",
        "window": "41.660-45.489", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "DOER", "THE-NEEDY"],
        "narration": "Bring the poor, the ones with nowhere to go, into your home.",
        "must_show": "the open door — the doer welcoming the poor family with nowhere to go in through the wide-open house door, gesturing them inside to shelter.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot at the home doorway in warm daylight: the wide timber door stands open "
            "and the doer (dust-brown, not cream) turns with an open, welcoming arm, "
            "gesturing the weary poor family — the ones with nowhere to go — in from the "
            "street to the shelter of his home, the warm room waiting beyond. Ordinary-"
            "sized people, one head each, gazes into the doorway and on one another, not to "
            "the camera; warm daylight outside and warm hearth-light within, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b11", "out": "s11-cover-them.jpeg", "seg": "n2",
        "window": "45.489-48.100", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "DOER", "THE-NEEDY"],
        "narration": "When you see someone with no clothes, cover them.",
        "must_show": "an insert on the act of clothing — the doer's hands draping a warm cloak around a cold, poorly-clad person's shoulders and drawing it closed.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no nudity or exposure (dignity kept); no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert inside the home in warm daylight on the doer's weathered hands "
            "(dust-brown sleeve, not cream) draping a warm woven cloak around the shoulders "
            "of a cold, poorly-clad person and drawing it closed at the chest — clothing "
            "the one who had none, gently and with dignity. Natural hands, ordinary scale; "
            "warm light rests on the cloak, not around any head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b12", "out": "s12-thine-own-flesh.jpeg", "seg": "n2",
        "window": "48.100-50.745", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOME", "DOER", "THE-NEEDY"],
        "narration": "Don't turn away from your own family.",
        "must_show": "the doer not turning away from his own kin — clasping the shoulder of a poor kinsman and drawing him near rather than hiding from his own flesh.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close two-shot at the home threshold in warm daylight: the doer (dust-brown, "
            "not cream) clasps the shoulder of a poor kinsman and draws him near, meeting "
            "his eyes with kindness — not turning away or hiding from his own flesh and "
            "family. Ordinary-sized men, one head each, gazes meeting between them, not to "
            "the camera; warm daylight on them, not around any head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b13", "out": "s13-light-break-as-morning.jpeg", "seg": "s2",
        "window": "50.745-54.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAYBREAK"],
        "narration": "Then shall thy light break forth as the morning,",
        "must_show": "GREEN caption (GOD-voice) — the establishing DAYBREAK frame (NON-Jesus, the DAYBREAK plate): the town and hills at sunrise, the first warm gold light of morning breaking forth over the rooftops. God is NOT shown — the light is a real daybreak, not a figure.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure, face-in-the-sky, hand or beam-shaped-like-a-person; no Jesus and no one in cream or white; no halo or ring around anyone; no modern object; nothing written; not a cartoon.",
        "scene": (
            "An establishing wide of the Israelite town and the low hills beyond at "
            "sunrise, camera set low looking east across the flat rooftops toward the "
            "horizon so the growing light breaks forth over the town and fills the frame — "
            "the first warm gold light of morning rising and touching the stone. It is a "
            "real daybreak; there is no figure, face, hand or beam in the sky. Ancient "
            "rooftops, the town wall, the hills; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r192-b14", "out": "s14-health-spring-forth.jpeg", "seg": "s2",
        "window": "54.500-58.526", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAYBREAK", "THE-NEEDY"],
        "narration": "and thine health shall spring forth speedily:",
        "must_show": "GREEN caption (GOD-voice) — the ones who were bound and hungry now restored and well in the morning light: the freed man and the poor family standing upright and strong in the daybreak, health springing forth. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol in the sky; no Jesus and no one in cream or white; no halo or ring around any head; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the town at daybreak in warm gold morning light: the once-bound man "
            "and the cast-out family, now fed, clothed and free, stand upright and strong "
            "in the rising light — health springing forth speedily, colour back in their "
            "faces. Plain earth-toned wool (none cream). No figure in the sky. Ordinary-"
            "sized people, one head each, gazes out into the new morning, not to the "
            "camera; warm sunrise light on them, not around any head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b15", "out": "s15-call-and-he-answers.jpeg", "seg": "n3",
        "window": "58.526-61.900", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAYBREAK", "DOER"],
        "narration": "The LORD promises — call, and He answers.",
        "must_show": "the doer at daybreak lifting his face and open hands toward the morning in prayer — calling, and the light of the answering morning resting over him. God is NOT shown as a figure; the answer is the breaking light itself.",
        "must_not_show": "no LORD figure, face or beam-as-person in the sky; no Jesus and no one in cream or white; no halo or ring around his head; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of the doer (dust-brown, not cream) standing on his rooftop or "
            "threshold at daybreak, face lifted and hands opened toward the rising morning "
            "in quiet prayer — calling on the LORD. The warm gold light of the answering "
            "morning fills the sky and rests over the town; there is no figure, face or "
            "beam in the sky. Ordinary-sized, one head, gaze up into the light and not to "
            "the camera; the sunrise light is in the sky and on the stone, never a ring "
            "around his head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r192-b16", "out": "s16-darkness-becomes-noonday.jpeg", "seg": "n3",
        "window": "61.900-65.139", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAYBREAK", "DOER", "WIFE", "THE-NEEDY"],
        "narration": "Help others, and your own darkness becomes noonday.",
        "must_show": "the closing image — the doer and his wife together with the ones they helped, all standing in the full bright morning light of the town, the once-dark now become noonday. God is NOT shown.",
        "must_not_show": "no LORD figure or symbol in the sky; no Jesus and no one in cream or white; no halo or ring around any head; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing shot in the town square, now flooded with full bright morning light: "
            "the doer and his wife (none cream) stand together with the freed man, the "
            "hungry man and the poor family they took in — all of them upright and glad in "
            "the risen light, their darkness become noonday. No figure in the sky. "
            "Ordinary-sized people on one square, one head each, gazes on one another and "
            "out into the bright morning, not to the camera; the noonday light fills the "
            "square and rests on the stone, never a ring around any head; nothing is "
            "written anywhere; no divine figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# TOWN, HOME and DAYBREAK are NEW places — no committed plate yet. The runner promotes each
# from its first NON-Jesus frame (all frames here are NON-Jesus): TOWN from b01, HOME from
# b06, DAYBREAK from b13. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: all three places and every person are carried by the build-local text
# locks above. Jesus does not appear in this row (every beat jesus=False); no one wears
# cream or white; God/the LORD is never embodied.
REFS = {
}
