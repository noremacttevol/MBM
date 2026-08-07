#!/usr/bin/env python3
"""V2 beat map — row 197, build-197-sons-and-daughters-prophesy (Joel 2:28-29 — "And it shall
come to pass afterward, that I will pour out my spirit upon all flesh; and your sons and your
daughters shall prophesy, your old men shall dream dreams, your young men shall see visions:
and also upon the servants and upon the handmaids in those days will I pour out my spirit."),
fulfilled decades later at Pentecost when Peter said the promise had arrived.

COVERAGE: 13 pictures over 59.180 s (card_start) = ~4.55 s/picture (lesson 12 movie-coverage).
Three places: JOEL-HEIGHT (the prophet looking down the corridor of time), PEOPLE-STREET (an
ordinary town where the Spirit falls on every kind of person — sons, daughters, old men, young
men, servants, handmaids), and JERUSALEM-PENTECOST (decades later, Peter standing to say the
promise had arrived, the Spirit poured out on a crowd of every nation). RESTORATION
cornerstone: the Spirit is poured out on ALL FLESH — never locked in one building or one office.

=====================================================================
No open Cameron complaint (v2_outline.py 197). Fresh V2 beat map; Board Audio = OK.
=====================================================================

SPEAKER LAW (Old-Testament prophecy quoted, then its New-Testament fulfilment):
  s1  Joel 2:28  "And it shall come to pass afterward, that I will pour out my spirit upon
      all flesh; and your sons and your daughters shall prophesy..."   = GOD-voice → GREEN.
  s2  Joel 2:29  "And also upon the servants and upon the handmaids in those days will I
      pour out my spirit."                                             = GOD-voice → GREEN.
n0, n1, n2, n3 and card are the NARRATOR → white. There is NO red-letter (Jesus does not
appear and does not speak). **NO Jesus / NO cream / NO white** anywhere (cream is reserved for
Jesus, who is absent — this is Joel, and the Pentecost of Acts 2 where Peter, not Jesus,
stands).

**HARD GATE — GOD AND THE SPIRIT ARE NEVER EMBODIED, AND PENTECOST IS SHOWN WITHOUT FIRE.**
God SPEAKS in s1/s2 (green captions) but is NEVER a figure, face, dove, flame, beam,
hand-from-sky, ring or symbol. "I will pour out my spirit upon all flesh", "sons and daughters
shall prophesy", "old men shall dream dreams", "young men shall see visions" are carried ONLY
by the PEOPLE themselves — faces alight with conviction, mouths open, eyes lifted — under warm
natural daylight; NOTHING is poured, rained or beamed down. The Pentecost beats (b10/b11)
show PETER standing and preaching and the diverse crowd receiving the Spirit through their own
changed faces — deliberately NO tongues of fire, NO dove, NO beam (consistent with the
Spirit-never-embodied gate of builds 165/166; the Acts-2 fire is NOT imported unless Cameron
asks, the way he asked for the Father in build-179). Drift-word gate: no halo / glow /
rim-light / beam in any scene text.

CONTENT-CARE: "old men shall dream dreams" is a peaceful reverie, never distress; "young men
shall see visions" is wonder, not fear; the servants and handmaids (b07/b08) are shown with
full dignity, lifted up, never demeaned. The prophesying of every kind of person is joyful and
earnest, never a frenzy or trance.

TIME-OF-DAY: warm daylight throughout (JOEL-HEIGHT in bright clear light; PEOPLE-STREET and
JERUSALEM-PENTECOST warm day). Not night; no divine light.

PLACES / LOCKS:
  JOEL-HEIGHT       a windswept height where the prophet Joel looks out over the generations
                    to come (b01/b02). NEW build-local place; runner promotes from b01.
  PEOPLE-STREET     an ordinary first-century town street/square where the Spirit falls on
                    every kind of person (b03-b09). NEW build-local place; runner promotes b03.
  JERUSALEM-PENTECOST  the Jerusalem square where Peter stands at Pentecost and the Spirit is
                    poured out on the crowd of every nation (b10-b13). NEW build-local place;
                    runner promotes from b10.
People locks: JOEL (the prophet), ALL-FLESH (the diverse individuals and crowd on whom the
Spirit falls — every age, both sexes, free and bond), PETER (canonical GLOBAL cast — attaches
by token, jesus=False). None wear cream or white.

AUDIO: default AUDIO LOCK stream-copy (no re-voice; no open complaint). Board Audio = OK.
card_start = 59.180 s. Picture-only — do NOT re-voice.
"""

# JOEL and ALL-FLESH are build-local text locks; PETER attaches from the global canonical cast
# by token (no local definition, jesus=False). JOEL-HEIGHT, PEOPLE-STREET and
# JERUSALEM-PENTECOST are NEW build-local places the runner promotes. Jesus is absent (every
# beat jesus=False); no image REFS beyond the global PETER cast token; no one wears cream/white;
# God and the Spirit are never embodied.
LOCKS = {
    "JOEL-HEIGHT": (
        "JOEL-HEIGHT LOCK: the same place in every frame — a windswept ancient stony "
        "height above a wide valley, bare tan hills rolling to the horizon under a broad "
        "bright sky, a few dry shrubs and an outcrop of rock. Ancient Near-Eastern "
        "landscape only; no modern building, vehicle, pole, wire or sign, no rendered "
        "writing. The same height, valley and bright sky throughout, in warm daylight."
    ),
    "PEOPLE-STREET": (
        "PEOPLE-STREET LOCK: the same place in every frame — an ordinary first-century "
        "town street and small square: worn stone paving between low mud-brick and stone "
        "houses, dark doorways, a well-head, a few plain market stalls and worn steps, "
        "everyday life going on. Ancient and real; no modern object anywhere; nothing "
        "legible or rendered is written on any surface. The same street and warm daylight "
        "throughout."
    ),
    "JERUSALEM-PENTECOST": (
        "JERUSALEM-PENTECOST LOCK: the same place in every frame — a broad open square in "
        "first-century Jerusalem: pale dressed-stone paving and steps, low flat-roofed "
        "stone houses and a colonnade edge, the pale city rising behind, a great mixed "
        "crowd from many nations gathering. Ancient and real; no modern building, vehicle, "
        "pole, wire, sign or rendered writing anywhere. The same square, steps and city "
        "behind, in warm daylight throughout."
    ),
    "JOEL": (
        "JOEL LOCK: the prophet Joel is the same man in every shot — a weathered Hebrew "
        "prophet of about sixty, brown-skinned and sun-darkened, a long grey-streaked "
        "beard and dark-grey hair, deep steady eyes, in a plain earth-toned hand-woven "
        "wool robe and mantle (never cream, never white), a plain wooden staff in hand, "
        "grave and far-seeing. The same man throughout; ordinary-sized, two hands, one "
        "head, never twinned or cloned."
    ),
    "ALL-FLESH": (
        "ALL-FLESH LOCK: the people on whom the Spirit falls are a wide, diverse mix of "
        "ordinary human beings of the ancient world — young men and young women, old men "
        "and old women, working men and bondservants and maidservants, of varied "
        "skin-tones and features — in plain, varied earth-toned wool and linen (none in "
        "cream, none in white). Every one a distinct individual with a real face, never "
        "twins or cloned faces; ordinary-sized, two hands and one head each; no modern "
        "clothing, tools, flags or signage. Together they are 'all flesh' — every kind of "
        "person."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r197-b01", "out": "s01-joel-names-the-future.jpeg", "seg": "n0",
        "window": "0.000-4.300", "wide": True, "jesus": False, "ref": False,
        "locks": ["JOEL-HEIGHT", "JOEL"],
        "narration": "The prophet Joel looked down the long corridor of time",
        "must_show": "the establishing frame (NON-Jesus, the plate the runner promotes) — Joel alone on a windswept height, gazing out over the wide valley and the far hills, looking down the long corridor of time toward a day still to come.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, face, dove, flame or beam; no halo or ring of light; no modern object; no rendered writing; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "An establishing wide on a windswept ancient height in warm daylight, camera set "
            "behind and to the side of Joel so his back is three-quarters to the lens and his "
            "gaze travels far out over the valley and hills, never to the camera: Joel — a "
            "grey-bearded prophet in an earth-toned robe (not cream), a wooden staff in hand "
            "— stands on the outcrop looking down the long corridor of time toward a day yet "
            "to come. Bare tan hills roll to the bright horizon. Ordinary-sized; warm "
            "daylight on him and the land, not around his head; nothing is written anywhere; "
            "no divine figure."
        ),
    },
    {
        "id": "v2-r197-b02", "out": "s02-not-for-a-few.jpeg", "seg": "n0",
        "window": "4.300-9.160", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOEL-HEIGHT", "JOEL"],
        "narration": "and described a day the LORD promised — not for a few, but for all.",
        "must_show": "a closer shot of Joel, hand open toward the valley, speaking the promise the LORD gave — a day not for a few but for everyone; his face lit with the greatness of it.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closer three-quarter shot of Joel (not cream) on the height in warm daylight, "
            "one hand opened out over the wide valley, his weathered face lit with the "
            "greatness of the promise as he describes the day the LORD swore — not for a few "
            "but for all. His gaze goes out over the land, not to the camera; warm daylight "
            "on his face, not around his head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b03", "out": "s03-pour-out-on-all-flesh.jpeg", "seg": "s1",
        "window": "9.160-13.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["PEOPLE-STREET", "ALL-FLESH"],
        "narration": "I will pour out my spirit upon all flesh;",
        "must_show": "GREEN caption (GOD-voice) — the establishing PEOPLE-STREET frame (the plate the runner promotes): a wide of a town street full of every kind of person, faces beginning to lift and light with conviction; the Spirit poured on all flesh, shown ONLY by the people, nothing poured or beamed down.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; nothing poured, rained or beamed from the sky; no halo, ring or beam of light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of an ordinary town street in warm daylight, camera at eye "
            "level behind a foreground figure whose back is to the lens, looking down the "
            "street: it is full of every kind of person — young and old, men and women, "
            "working folk and servants (varied earth-toned wool, none cream) — and their "
            "faces are lifting and beginning to light with conviction, the Spirit falling on "
            "all flesh. Nothing is poured, rained or beamed from the sky; the outpouring is "
            "shown only through the changed people. A real street, no one lined up facing the "
            "lens. Ordinary-sized people on one ground plane; warm daylight over the street, "
            "not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b04", "out": "s04-sons-and-daughters.jpeg", "seg": "s1",
        "window": "13.500-17.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["PEOPLE-STREET", "ALL-FLESH"],
        "narration": "and your sons and your daughters shall prophesy,",
        "must_show": "GREEN caption (GOD-voice) — a young man AND a young woman side by side, both prophesying, mouths open speaking God's words, faces alight; sons and daughters alike given the Spirit.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo, ring or beam of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot in the town street in warm daylight: a young man of about twenty and "
            "a young woman of about eighteen (plain earth-toned wool, not cream) stand side "
            "by side, both prophesying — mouths open speaking God's words, faces alight with "
            "the same conviction — sons and daughters alike given the Spirit. Shown only "
            "through the two young people; nothing descends on them. Ordinary-sized, one head "
            "each, gazes lifted in conviction, not to the camera; warm daylight on their "
            "faces, not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b05", "out": "s05-old-men-dream-dreams.jpeg", "seg": "s1",
        "window": "17.800-22.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["PEOPLE-STREET", "ALL-FLESH"],
        "narration": "your old men shall dream dreams,",
        "must_show": "GREEN caption (GOD-voice) — an old man in a peaceful reverie, eyes closed or half-closed, a look of wonder on his aged face as he dreams dreams from God; peaceful, never distressed.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no visible dream-image or vision floating; no halo or ring of light; no distress; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on an old man (grey-bearded, earth-toned wool, not cream) seated on the "
            "worn steps of the street in warm daylight, eyes softly closed and his weathered "
            "face at peace and full of wonder — he dreams dreams from God. Nothing floats "
            "above or around him; the dream is carried only by his peaceful, wondering face. "
            "His head is tilted in reverie, not to the camera; warm daylight on his face, not "
            "around his head; nothing is written anywhere; no divine figure or floating "
            "vision."
        ),
    },
    {
        "id": "v2-r197-b06", "out": "s06-young-men-see-visions.jpeg", "seg": "s1",
        "window": "22.000-26.490", "wide": False, "jesus": False, "ref": False,
        "locks": ["PEOPLE-STREET", "ALL-FLESH"],
        "narration": "your young men shall see visions:",
        "must_show": "GREEN caption (GOD-voice) — a young man with his eyes lifted and wide with wonder, beholding a vision God gives him; awe on his face, the vision itself NOT shown.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no visible vision, apparition or floating image; no halo, ring or beam of light; no fear; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on a young man (short dark beard, earth-toned wool, not cream) standing "
            "in the street in warm daylight, his eyes lifted and wide with wonder and awe as "
            "he beholds a vision God gives him. The vision itself is NOT shown — only his "
            "awed, upward-gazing face carries it; nothing floats or shines before him. His "
            "gaze is up and off past the frame, not to the camera; warm daylight on his "
            "face, not around his head; nothing is written anywhere; no divine figure or "
            "floating apparition."
        ),
    },
    {
        "id": "v2-r197-b07", "out": "s07-upon-the-servants.jpeg", "seg": "s2",
        "window": "26.490-29.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["PEOPLE-STREET", "ALL-FLESH"],
        "narration": "And also upon the servants",
        "must_show": "GREEN caption (GOD-voice) — a working bondservant, his hands still dusty from labour, straightening as the Spirit fills him, his face lifting with dignity and conviction; the lowest in status given the same gift.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; nothing demeaning; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on a working bondservant (a plain rough earth-toned tunic, not cream) in "
            "the street in warm daylight, his hands still dusty from labour, straightening "
            "from his work as his face lifts with dignity and conviction — the lowest in "
            "status given the very same Spirit. Shown only through the man himself; nothing "
            "descends. Ordinary-sized, one head, gaze lifted, not to the camera; warm "
            "daylight on his face, not around his head; nothing is written anywhere; no "
            "divine figure."
        ),
    },
    {
        "id": "v2-r197-b08", "out": "s08-and-the-handmaids.jpeg", "seg": "s2",
        "window": "29.000-33.440", "wide": False, "jesus": False, "ref": False,
        "locks": ["PEOPLE-STREET", "ALL-FLESH"],
        "narration": "and upon the handmaids in those days will I pour out my spirit.",
        "must_show": "GREEN caption (GOD-voice) — a young maidservant at her work, a water-jar or basket set down, filled with the Spirit, her face lifted with dignity and joy; the handmaid given the gift alongside everyone else.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; nothing poured or beamed down; no halo or ring of light; nothing demeaning; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on a young maidservant (plain earth-toned dress and head-cloth, not "
            "cream) in the street in warm daylight, a water-jar just set down at her side, "
            "her face lifting with dignity and quiet joy as the Spirit fills her — the "
            "handmaid given the gift alongside everyone else. Shown only through the woman "
            "herself; nothing is poured or beamed onto her. Ordinary-sized, one head, gaze "
            "lifted, not to the camera; warm daylight on her face, not around her head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b09", "out": "s09-every-kind-of-person.jpeg", "seg": "n1",
        "window": "33.440-39.280", "wide": True, "jesus": False, "ref": False,
        "locks": ["PEOPLE-STREET", "ALL-FLESH"],
        "narration": "Not stopped by age or status — every kind of person, filled with the same Spirit.",
        "must_show": "a wide of the whole street — old and young, free and bond, men and women together, every kind of person filled with the same Spirit, faces alight; the gift stopped by no age and no status.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; nothing poured or beamed from the sky; no halo, ring or beam of light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A wide of the whole town street in warm daylight, camera behind a foreground "
            "figure whose back is to the lens: old men and young women, working servants and "
            "free townsfolk, men and women all through the street (varied earth-toned wool, "
            "none cream), every kind of person, faces alight with the same conviction — the "
            "gift stopped by no age and no status. Shown only through the people; nothing "
            "descends. A real crowded street, no one lined up facing the lens. Ordinary-sized "
            "people on one ground plane; warm daylight over them, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b10", "out": "s10-peter-stands.jpeg", "seg": "n2",
        "window": "39.280-44.000", "wide": True, "jesus": False, "ref": False,
        "locks": ["JERUSALEM-PENTECOST", "PETER", "ALL-FLESH"],
        "narration": "Decades later, on the day of Pentecost, the apostle Peter stood and said this promise had arrived.",
        "must_show": "the establishing JERUSALEM-PENTECOST frame (the plate the runner promotes) — Peter standing on the steps before a great mixed crowd of many nations, arm raised as he declares Joel's promise has arrived. NO tongues of fire, NO dove, NO beam — the Spirit is not embodied.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame, tongue of fire or beam over anyone; no halo, ring or beam of light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing wide of the broad Jerusalem square in warm daylight, camera at "
            "the edge of the crowd looking toward the steps so the crowd's backs and "
            "three-quarter faces turn toward Peter and every gaze travels to him, never to "
            "the camera: PETER (the canonical apostle, earth-toned robe, not cream) stands on "
            "the steps, one arm raised, declaring to the great mixed crowd of many nations "
            "that Joel's promise has arrived. There are NO tongues of fire, no dove and no "
            "beam anywhere — the Spirit is shown only in the lit, attentive faces of the "
            "crowd. A real gathering, not a staged line. Ordinary-sized people on one ground "
            "plane; warm daylight over the square, not around any head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b11", "out": "s11-the-spirit-arrived.jpeg", "seg": "n2",
        "window": "44.000-49.580", "wide": False, "jesus": False, "ref": False,
        "locks": ["JERUSALEM-PENTECOST", "ALL-FLESH"],
        "narration": "The Spirit had come, just as Joel foretold.",
        "must_show": "the Pentecost crowd receiving — people of every nation in the square, faces alight and mouths open, filled with the Spirit exactly as Joel foretold; shown ONLY through the changed people, NO fire/dove/beam.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame, tongue of fire or beam over anyone; no halo, ring or beam of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot into the Pentecost crowd in warm daylight: people of many nations "
            "(varied earth-toned dress, none cream), faces alight and mouths open, filled "
            "with the Spirit just as Joel foretold — the promise arrived. Shown only through "
            "the changed, wondering people; there is no tongue of fire, no dove, no beam over "
            "anyone. Ordinary-sized people, one head each, gazes lifted and turned toward one "
            "another, not to the camera; warm daylight on their faces, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b12", "out": "s12-not-locked-away.jpeg", "seg": "n3",
        "window": "49.580-54.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["JERUSALEM-PENTECOST", "ALL-FLESH"],
        "narration": "The promise was never meant to be locked in one building or one office.",
        "must_show": "the Spirit not locked away — ordinary Spirit-filled people streaming OUT of the shadow of a single building into the open sunlit square, the gift belonging to everyone, not shut inside walls or held by a few officials.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot at the edge of the Jerusalem square in warm daylight: ordinary "
            "Spirit-filled people (varied earth-toned dress, none cream) stream out from the "
            "shadow of a single stone building into the open sunlit square, glad and "
            "unconfined — the promise was never locked inside walls or held by a few "
            "officials. Ordinary-sized people on one ground plane, gazes and travel going out "
            "into the light of the open square, not to the camera; warm daylight ahead of "
            "them, not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r197-b13", "out": "s13-poured-out-for-all.jpeg", "seg": "n3",
        "window": "54.400-59.180", "wide": True, "jesus": False, "ref": False,
        "locks": ["JERUSALEM-PENTECOST", "ALL-FLESH"],
        "narration": "It was poured out — freely, widely, for all.",
        "must_show": "the closing wide — the whole open square full of every kind of Spirit-filled person, the gift spread freely and widely to all; a picture of the promise reaching everyone.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, dove, flame or beam; nothing poured or beamed from the sky; no halo, ring or beam of light; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A closing wide of the whole open Jerusalem square in warm daylight, camera "
            "raised a little behind the near edge of the crowd so their backs and "
            "three-quarter faces fill the foreground and their gazes spread out across the "
            "square, never to the camera: the square is full of every kind of Spirit-filled "
            "person — young and old, free and bond, of many nations (varied earth-toned "
            "dress, none cream) — the gift poured out freely, widely, for all. Nothing is "
            "poured or beamed from the sky; the outpouring is shown only through the multitude "
            "of lit faces. Ordinary-sized people on one ground plane; warm daylight over the "
            "square, not around any head; nothing is written anywhere; no divine figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# JOEL-HEIGHT, PEOPLE-STREET and JERUSALEM-PENTECOST are NEW places with no committed plate
# yet; the runner promotes JOEL-HEIGHT from b01, PEOPLE-STREET from b03, JERUSALEM-PENTECOST
# from b10 (all frames here are NON-Jesus). Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS beyond the global PETER cast token: all places and the JOEL/ALL-FLESH people
# are carried by the build-local text locks above. Jesus does not appear in this row (every
# beat jesus=False); no one wears cream or white; God and the Spirit are never embodied and
# Pentecost is shown without fire.
REFS = {
}
