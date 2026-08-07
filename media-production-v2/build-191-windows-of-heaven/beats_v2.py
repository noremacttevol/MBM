#!/usr/bin/env python3
"""V2 beat map — row 191, build-191-windows-of-heaven (Malachi 3:10 — "Bring ye all the
tithes into the storehouse... and prove me now herewith, saith the LORD of hosts, if I
will not open you the windows of heaven, and pour you out a blessing, that there shall not
be room enough to receive it.").

COVERAGE: 14 pictures over 51.518 s (card_start) = ~3.68 s/picture (lesson 12
movie-coverage). Two places: the STOREHOUSE (the place set apart for the Lord's house,
where the people bring their tithes and where Malachi declares the LORD's offer) and the
HARVEST-LAND (the open fields under the sky where the "windows of heaven" pour out
blessing). Human spine: a representative FARMER who holds back, then brings everything in
and gathers the overflow; MALACHI the prophet carries the LORD's words.

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 191): "Not real new voice."
FIXED AT $0 (this author lane): all 8 segment mp3s are ElevenLabs new-voice
(ffprobe-confirmed 44100/128k; the s1 GOD segment reads F0 ≈ 134.5 Hz = the ElevenLabs
"Bill"/God voice, NOT edge-tts). The delivered V1 mp4 had stream-copied a STALE track;
this build now sets **AUDIO_FROM_V1_SEGMENTS = True** so v2_assemble rebuilds the shipped
track from those new-voice segments (not a stale stream-copy). Same fix as row 177. The
review card MUST tell Cameron the voice is the real new voice. See QC.md COMPLAINT LEDGER.
=====================================================================

SPEAKER LAW (see make_narration.py — Malachi is an OT prophet; the LORD speaks through
him):
  s1  Malachi 3:10  "Bring ye all the tithes into the storehouse..."  GOD → GREEN caption
Every other segment (n0, n1, n2, n2b, n3a, n3b, card) is the NARRATOR → white. There is NO
red-letter and NO Jesus in this row: **every beat jesus=False and NO ONE wears cream or
white** (cream is reserved for Jesus, who is absent — this is Old Testament).

**HARD GATE — GOD / THE LORD IS NEVER EMBODIED.** s1 is the GOD-voice (green caption), but
the LORD is NEVER shown. The words are carried by MALACHI the prophet declaring them and
by the sky and the harvest — never by any figure, face, hand, throne, beam-as-person, dove
or symbol. The "windows of heaven" are a radiant sky breaking open with light and rain over
the land — brilliant WHITE/GOLD light in the SKY, NEVER a figure or a face in the clouds,
NEVER a ring or beam shaped like a person. No halo, ring or rim-light around anyone's head
(drift-word gate — word light as radiant / brilliant / warm).

CONTENT-CARE: the LORD's "prove me / put me to the test" is an OFFER of goodness, not a
threat — no fear, no judgment imagery, no fire, no flood-as-disaster. The pouring blessing
is abundant rain, full storehouses and overflowing harvest baskets — joy and plenty, more
than there is room to hold.

TIME-OF-DAY: the STOREHOUSE opens at soft dawn and warms through the day; the HARVEST-LAND
scenes are a bright day with the sky breaking radiant open. No night.

PLACES / LOCKS (both NEW build-local places — no committed plate yet; runner promotes each
from its first NON-Jesus frame, all frames here are NON-Jesus):
  STOREHOUSE    the temple storehouse & its forecourt (b01/b02/b03/b04/b05/b06/b07/b11/
                b12/b14) — promote from b01.
  HARVEST-LAND  the open fields under the opening sky (b08/b09/b10/b13) — promote from b08.
People locks: MALACHI (the prophet), FARMER (representative worshipper — holds back →
brings all in → gathers the overflow), LEVITE (storehouse keeper), and TITHE-BRINGERS
(the people). None wear cream or white.

AUDIO: AUDIO_FROM_V1_SEGMENTS = True (complaint fix — rebuild from the new-voice segments).
card_start = 51.518 s. Picture-only otherwise — do NOT re-voice (segments already correct).
"""

AUDIO_FROM_V1_SEGMENTS = True

# NEW build-local places + people are declared as text LOCKS here; PLACE_REFS stays empty
# and the runner promotes each place from its first NON-Jesus frame (see QC.md). No one
# wears cream/white (this is OT; Jesus is absent).
LOCKS = {
    "STOREHOUSE": (
        "STOREHOUSE LOCK: the same place in every frame — the storehouse set apart for the "
        "Lord's house in the days of the second temple: a long stone-and-timber granary "
        "and its swept forecourt beside the temple wall, rows of large clay storage jars, "
        "woven baskets and sacks, low wooden bins for grain, a broad timber door, worn "
        "stone steps, and the temple's dressed-stone wall rising beyond. Ancient and real; "
        "no modern object anywhere, and nothing legible or rendered is written on any "
        "surface. The same storehouse and its forecourt throughout, in warm daylight."
    ),
    "HARVEST-LAND": (
        "HARVEST-LAND LOCK: the same place in every frame — open first-century farmland "
        "outside the town: ripe golden grain fields and terraced plots, a few olive and "
        "fig trees, low stone field-walls, and a wide sky overhead. In these frames the "
        "sky breaks radiant open with brilliant white-and-gold light and abundant rain "
        "falling on the fields — a blessing poured out, never a disaster. Ancient and "
        "real; no modern object anywhere, and nothing written. The same fields and opening "
        "sky throughout. The light fills the sky and the land; it is never a figure or a "
        "face in the clouds and never a ring around anyone's head."
    ),
    "MALACHI": (
        "MALACHI LOCK: the same man in every frame he appears — Malachi, an Old Testament "
        "prophet of about fifty-five, warm tan sun-worn skin, dark hair and a full "
        "dark-grey beard, deep steady eyes, in a plain undyed brown-and-ochre wool prophet's "
        "robe with a coarse mantle (never cream, never white). Grave, earnest and "
        "unafraid, one arm often raised as he declares. The same face, beard and robe "
        "throughout."
    ),
    "FARMER": (
        "FARMER LOCK: the same man in every frame he appears — a representative "
        "first-century worshipper and farmer of about forty, warm olive-brown skin, short "
        "dark beard streaked grey, weathered strong hands, in a plain dust-brown wool "
        "tunic and mantle (never cream, never white). Early he holds back, cautious; later "
        "he trusts and brings everything in, then gathers the overflow with joy. The same "
        "face, beard and clothing throughout."
    ),
    "LEVITE": (
        "LEVITE LOCK: the same man in every frame he appears — a temple Levite storehouse "
        "keeper of about forty-five, tan skin, trimmed dark beard, in a modest deep-blue "
        "and grey temple servant's robe (never cream, never white); receives and records "
        "the tithes at the storehouse. The same man throughout."
    ),
    "TITHE-BRINGERS": (
        "TITHE-BRINGERS LOCK: the people of the town — a mixed group of ordinary "
        "first-century men, women and a few children in plain earth-toned wool (never "
        "cream, never white), carrying sheaves, jars of oil, baskets of produce and young "
        "animals to the storehouse; distinct individual faces, not twins. The same kind of "
        "people throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r191-b01", "out": "s01-storehouse-at-dawn.jpeg", "seg": "n0",
        "window": "0.000-4.200", "wide": True, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "TITHE-BRINGERS"],
        "narration": "Through the prophet Malachi, the LORD made a strange offer to a people holding back —",
        "must_show": "the establishing wide, NON-Jesus (the STOREHOUSE plate) — the temple storehouse and its forecourt at soft dawn, its bins and jars mostly bare, and a few townspeople hanging back at the edge, holding their offerings close rather than bringing them in.",
        "must_not_show": "no Jesus and no one in cream or white; no God or LORD figure anywhere; no halo, glare or rim-light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the temple storehouse and its swept forecourt at soft "
            "dawn, camera set low across the forecourt looking toward the storehouse door "
            "so the hanging-back townspeople are three-quarters to the lens and their gaze "
            "goes inward toward the half-empty store, never to the camera. The bins, jars "
            "and baskets stand mostly bare; a few ordinary people linger at the edge, "
            "clutching sheaves and jars close, holding back rather than bringing them in. "
            "The temple wall rises beyond. Ancient and real; warm dawn light rests on the "
            "stone, not around anyone's head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r191-b02", "out": "s02-watch-what-i-do.jpeg", "seg": "n0",
        "window": "4.200-8.383", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "FARMER"],
        "narration": "bring everything in, and watch what I do.",
        "must_show": "a close on the FARMER at the storehouse door, an offering in his arms, weighing the strange invitation to bring everything in — cautious hope on his face.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the representative farmer at the storehouse door in early daylight, "
            "a sheaf and a jar of oil in his arms, weighing the strange invitation to bring "
            "everything in — cautious hope on his weathered face. Plain dust-brown wool "
            "(not cream). Ordinary-sized, one head, gaze toward the open store and not to "
            "the camera; warm light on him, not around his head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r191-b03", "out": "s03-place-set-apart.jpeg", "seg": "n1",
        "window": "8.383-11.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "LEVITE", "FARMER"],
        "narration": "The storehouse was the place set apart for the Lord's house,",
        "must_show": "the storehouse as the place set apart — the Levite keeper receiving an offering at the storeroom beside the temple wall, the place plainly dedicated to the Lord's house.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A medium inside the storehouse forecourt in warm daylight: the Levite keeper "
            "in his deep-blue and grey robe (not cream) receives an offering from the "
            "farmer, the temple wall close behind — plainly the place set apart for the "
            "Lord's house. Rows of clay jars and grain bins around them. Ordinary-sized "
            "men, one head each, gazes on the offering between them and not to the camera; "
            "warm light, not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r191-b04", "out": "s04-the-tithe-set-apart.jpeg", "seg": "n1",
        "window": "11.500-14.506", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE"],
        "narration": "and the tithe was the part meant for him.",
        "must_show": "an insert of the tithe itself — a tenth measure of grain and firstfruits set carefully apart into a marked basket, the portion meant for the Lord; hands measuring it out.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written or numbered on the baskets; not a cartoon.",
        "scene": (
            "A tight insert on hands measuring out a tenth of the grain and firstfruits — a "
            "ripe sheaf, a measure of grain and first figs — set carefully apart into a "
            "plain marked basket in the storehouse, the portion meant for the Lord. Warm "
            "daylight on the grain. Natural hands, ordinary scale; the light rests on the "
            "offering, not around any head; nothing legible is written on the baskets; no "
            "divine figure."
        ),
    },
    {
        "id": "v2-r191-b05", "out": "s05-bring-all-the-tithes.jpeg", "seg": "s1",
        "window": "14.506-19.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "MALACHI", "TITHE-BRINGERS"],
        "narration": "Bring ye all the tithes into the storehouse,",
        "must_show": "GREEN caption (GOD-voice, spoken through the prophet) — Malachi standing before the people in the storehouse forecourt, one arm raised, declaring the LORD's call to bring ALL the tithes in; the people beginning to come forward with their offerings. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure, face, hand, throne, beam or rays; no Jesus and no one in cream or white; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of Malachi the prophet in his brown-and-ochre robe (not cream) standing "
            "before the townspeople in the storehouse forecourt, one arm raised as he "
            "declares the LORD's call to bring all the tithes in; the people begin to come "
            "forward, sheaves and jars in their arms. No figure stands in for the LORD — "
            "the words are the prophet's declaring. Ordinary-sized people on one court, one "
            "head each, gazes on Malachi and the storehouse and not to the camera; warm "
            "daylight, no ring of light around any head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r191-b06", "out": "s06-meat-in-mine-house.jpeg", "seg": "s1",
        "window": "19.000-23.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "TITHE-BRINGERS"],
        "narration": "that there may be meat in mine house,",
        "must_show": "GREEN caption (GOD-voice) — the storehouse now filling with provision: grain heaped in the bins, jars of oil and baskets of produce brought in and set in rows, that there may be food in the Lord's house. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol; no Jesus and no one in cream or white; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of the storehouse filling in warm daylight — grain heaped in the bins, "
            "jars of oil and baskets of figs and produce carried in and set in rows by the "
            "townspeople — provision for the Lord's house. No divine figure appears. "
            "Ordinary-sized people, one head each, gazes on their work and not to the "
            "camera; warm light on the plenty, not around any head; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r191-b07", "out": "s07-prove-me-now.jpeg", "seg": "s1",
        "window": "23.500-28.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "MALACHI", "FARMER"],
        "narration": "and prove me now herewith, saith the LORD of hosts,",
        "must_show": "GREEN caption (GOD-voice) — Malachi extending an open hand in the LORD's astonishing invitation to 'prove me now'; the farmer and people caught and listening, weighing so bold an offer. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure, face, hand-from-sky, throne or beam; no Jesus and no one in cream or white; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot: Malachi in warm daylight extends an open hand as he speaks the "
            "LORD's astonishing invitation to prove him now; the farmer and a few "
            "townspeople stand caught and listening, weighing so bold an offer. Only the "
            "prophet carries the words — no figure stands in for the LORD. Plain wool robes "
            "(none cream). Ordinary-sized, one head each, gazes between Malachi and one "
            "another and not to the camera; warm daylight, no ring of light around any "
            "head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r191-b08", "out": "s08-windows-of-heaven.jpeg", "seg": "s1",
        "window": "28.000-31.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["HARVEST-LAND"],
        "narration": "if I will not open you the windows of heaven,",
        "must_show": "GREEN caption (GOD-voice) — the HARVEST-LAND plate (NON-Jesus): the wide sky breaking radiant open over the fields, brilliant white-and-gold light pouring down and the first abundant rain beginning to fall — the windows of heaven opened. NO figure or face in the sky.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure, face-in-the-clouds, hand or beam-shaped-like-a-person; no Jesus and no one in cream or white; no halo or ring around anyone; no storm-as-disaster, no lightning-strike; no modern object; nothing written; not a cartoon.",
        "scene": (
            "An establishing wide of the open golden farmland, camera low looking up across "
            "the fields toward the sky, which breaks radiant open — brilliant white-and-gold "
            "light streaming down through parting cloud and the first abundant rain "
            "beginning to fall on the ripe grain: the windows of heaven opened. The light "
            "and rain fill the whole sky and land; there is no figure, face or hand in the "
            "clouds, and no beam shaped like a person. Ancient fields, low stone walls; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r191-b09", "out": "s09-pour-out-a-blessing.jpeg", "seg": "s1",
        "window": "31.500-34.401", "wide": False, "jesus": False, "ref": False,
        "locks": ["HARVEST-LAND", "FARMER"],
        "narration": "and pour you out a blessing, that there shall not be room enough to receive it.",
        "must_show": "GREEN caption (GOD-voice) — the blessing poured out: abundant rain drenching a bursting harvest, grain and fruit heavier than the baskets can hold, the farmer amazed with his arms full and more spilling over. God is NOT shown.",
        "must_not_show": "GOD IS NOT SHOWN — no LORD figure or symbol in the sky; no Jesus and no one in cream or white; no halo or ring around any head; no flood-as-disaster; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the rain-blessed fields: abundant warm rain drenches a bursting "
            "harvest, sheaves and baskets heaped past overflowing, ripe fruit spilling over "
            "the rims; the farmer stands amazed, his arms full and more than he can hold "
            "tumbling around him — a blessing with not room enough to receive it. Plain "
            "dust-brown wool (not cream). No divine figure. Ordinary-sized, one head, gaze "
            "up at the pouring sky and over the plenty, not to the camera; radiant daylight, "
            "not a ring around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r191-b10", "out": "s10-a-dare-no-king.jpeg", "seg": "n2",
        "window": "34.401-39.730", "wide": False, "jesus": False, "ref": False,
        "locks": ["HARVEST-LAND", "TITHE-BRINGERS"],
        "narration": "A dare no king could make — test me, and see if I don't open the windows.",
        "must_show": "the people out in the fields looking up in wonder at the opened sky — a dare no earthly king could ever make, now seen with their own eyes; awe and joy on their faces.",
        "must_not_show": "no God or LORD figure in the sky; no Jesus and no one in cream or white; no king or crown; no halo or ring around any head; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of the townspeople out among the rain-blessed fields, faces turned up "
            "in wonder at the opened radiant sky — a dare no earthly king could make, now "
            "seen with their own eyes; awe and gladness on them. Plain earth-toned wool "
            "(none cream). No figure in the sky. Ordinary-sized people, one head each, "
            "gazes up and not to the camera; radiant daylight, no ring around any head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r191-b11", "out": "s11-prove-me.jpeg", "seg": "n2b",
        "window": "39.730-43.550", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "MALACHI"],
        "narration": "He is the only one in scripture who ever says: prove me.",
        "must_show": "a close on Malachi back in the storehouse forecourt, both hands opening in the singular invitation — the only voice in scripture that ever says 'prove me'; quiet, sure, inviting.",
        "must_not_show": "no God or LORD figure; no Jesus and no one in cream or white; no halo or ring around any head; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on Malachi in the storehouse forecourt in warm daylight, both hands "
            "opening outward in the singular, quiet invitation — the only voice in "
            "scripture that ever says 'prove me'. Brown-and-ochre robe (not cream). "
            "Ordinary-sized, one head, gaze steady and warm toward the people and not to "
            "the camera; warm light on him, not around his head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r191-b12", "out": "s12-put-me-to-the-test.jpeg", "seg": "n2b",
        "window": "43.550-46.483", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "FARMER", "LEVITE"],
        "narration": "Put me to the test, and watch what I do.",
        "must_show": "the farmer taking up the dare — stepping forward and laying his full tithe into the storehouse in open trust, putting the LORD to the test; the Levite receiving it.",
        "must_not_show": "no God or LORD figure; no Jesus and no one in cream or white; no halo or ring around any head; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot of the farmer stepping forward in the storehouse forecourt and laying "
            "his full basket of grain and firstfruits into the store in open trust — "
            "putting the LORD to the test — while the Levite keeper receives it. Plain wool "
            "robes (none cream). Ordinary-sized men, one head each, gazes on the offering "
            "between them and not to the camera; warm daylight, no ring around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r191-b13", "out": "s13-not-a-trickle.jpeg", "seg": "n3a",
        "window": "46.483-48.108", "wide": False, "jesus": False, "ref": False,
        "locks": ["HARVEST-LAND"],
        "narration": "Not a trickle.",
        "must_show": "a brief insert setting up the contrast — not a thin trickle: a single small trickle of rainwater running along a dry field furrow, meagre and slight, about to be overwhelmed.",
        "must_not_show": "no God or LORD figure; no Jesus and no one in cream or white; no halo or ring; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert low on a dry field furrow where a single thin trickle of "
            "rainwater runs, meagre and slight — the small measure the blessing is about to "
            "overwhelm. Ancient farmland, warm daylight on the earth; no figure; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r191-b14", "out": "s14-more-than-room-to-hold.jpeg", "seg": "n3b",
        "window": "48.108-51.518", "wide": False, "jesus": False, "ref": False,
        "locks": ["STOREHOUSE", "FARMER", "TITHE-BRINGERS"],
        "narration": "A pouring out, more than there is room to hold.",
        "must_show": "the closing image — the storehouse and the people's baskets brimming and overflowing with grain and fruit, more than there is room to hold, the farmer and townspeople gathering the overflow with joy.",
        "must_not_show": "no God or LORD figure; no Jesus and no one in cream or white; no halo or ring around any head; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing shot of the storehouse in warm daylight, its bins and the people's "
            "baskets brimming and spilling over with heaped grain and ripe fruit — more "
            "than there is room to hold — the farmer and townspeople gathering the overflow "
            "with joy and wonder. Plain earth-toned wool (none cream). No divine figure. "
            "Ordinary-sized people on one court, one head each, gazes over the plenty and "
            "to one another, not to the camera; warm light on the abundance, not around any "
            "head; nothing is written anywhere."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# STOREHOUSE and HARVEST-LAND are NEW places — no committed plate yet. The runner promotes
# each from its first NON-Jesus frame (all frames here are NON-Jesus): STOREHOUSE from b01,
# HARVEST-LAND from b08. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: both places and all people are carried by the build-local text locks
# above. Jesus does not appear in this row (every beat jesus=False); no one wears cream or
# white; God/the LORD is never embodied.
REFS = {
}
