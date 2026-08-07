#!/usr/bin/env python3
"""V2 beat map — row 163, build-163-apostles-prophets (Ephesians 2:19-20).

COVERAGE: 18 pictures over 116.71 s = 6.5 s/picture.

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 163` shows no prior
review). Fresh authoring — the LEARNING/COST laws in the positive.

SCRIPTURE FACTS (Ephesians 2 KJV, the passage this row narrates):
  2:19 "Now therefore ye are no more strangers and foreigners, but
        fellowcitizens with the saints, and of the household of God;"  -> kv19
  2:20 "And are built upon the foundation of the apostles and
        prophets, Jesus Christ himself being the chief corner stone;"  -> kv20

ROW INTENT: the belonging/authority-has-a-design row (RESTORATION-adjacent,
kept strictly in the Bible's own frame). Outsiders are brought near and made
family; the church is not a shapeless crowd but a house with a real design —
a foundation of apostles and prophets, and Christ the cornerstone everything
aligns to. The close asks the viewer to come inside.

THE PICTURE CHANGES ON PURPOSE (Paul's own move, n4). The first half is a
FAMILY at a warm HOUSEHOLD — strangers on the far edge, the door thrown open,
the outsider drawn in and seated as a son. Then Paul "changed the picture from
a family to a building," so the second half is a BUILD-SITE — foundation,
masons, the cornerstone, living people fitted into the walls. The beat map
follows that hinge exactly at b07.

BOOKEND: the same weary outsider whose longing face we hold at b02 (outside,
no place) is the person standing INSIDE the finished doorway at b16-b17 (a
place, belonging). That arc is the whole point — build it so a viewer feels it.

WHO IS SHOWN:
  - CHRIST THE CORNERSTONE (b12, b13): Jesus stands at the cornerstone of the
    rising house, his hand on the great squared stone, the two walls aligning
    to him — "everything is lined up to him." Locked V2 Jesus (LOCK v5 + REF),
    only he wears cream, ordinary-sized (SCALE GATE, lesson 14). He is NOT
    turned into a literal stone and carries NO light around his head.
  - PAUL is NOT embodied — the narration referring to Paul rides over the
    illustrative imagery; no talking-head author, no invented apostle portrait.
  - THE APOSTLES AND PROPHETS (WITNESSES) are a small line of dignified,
    resolute men standing ON the foundation course — generic first-century
    witnesses, distinct faces, NOT posed as the named Twelve (no face-lock
    burden, no cloned faces).

RENDERING LAWS:
  - MOVIE COVERAGE (lesson 12): two establishing wides only — the far-edge
    household (b01) and the build-site (b07); everything else is a single,
    two-shot or insert. Groups stay SMALL, never a crowd.
  - Realistic biblical photography, no cartoon (Law 14). First-century
    materials only: dressed limestone ashlar, timber scaffolding, plumb line,
    oil lamps, woven cloth. No modern tools, no invented scripture props, no
    theological symbols beyond the plain architecture the text itself names.
  - Only Jesus wears cream. The Father is never depicted (he is not in this
    passage). No DRIFT words (halo/glow/pale) — warm light is 'lamplight' /
    'warm light', never a glow around a head.

TIME OF DAY ARC: the outsiders at dusk-longing (b01-b03); the threshold and
the family interior in warm lamplight (b04-b06); the build-site in clear
working daylight (b07-b13); the belonging bookend back in warm doorway light
(b16-b18).
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. The shared JESUS lock + REF come from v2_prompt.py.
LOCKS = {
    "HOUSEHOLD": (
        "HOUSEHOLD LOCK: the same warm first-century home in every frame — a "
        "modest dressed-stone house around a small courtyard, a heavy timber "
        "door in a plain stone threshold, a low table of bread and fruit "
        "within, clay oil lamps giving warm light; woven earth-toned "
        "hangings. The same house and doorway throughout — never a palace, "
        "never a temple, never modern glass or metal."
    ),
    "FAMILY": (
        "FAMILY LOCK: the household's people — a first-century family of "
        "parents, grown sons and daughters and children, warm open faces, "
        "plain earth-toned wool of brown, rust, ochre and olive (never cream "
        "— only Jesus wears cream); distinct individuals of all ages, "
        "welcoming, never twinned, never a cloned face."
    ),
    "OUTSIDERS": (
        "OUTSIDERS LOCK: weary foreigners and strangers of the road — a small "
        "group carrying travel-worn bundles, dust on their feet and clothes, "
        "faces marked by longing and tiredness, in faded grey-brown and "
        "muted travelling cloth (never cream); distinct real people, never "
        "twinned, never a uniform crowd."
    ),
    "BUILD-SITE": (
        "BUILD-SITE LOCK: the same first-century house under construction in "
        "every frame — a deep, level foundation course of massive squared "
        "limestone ashlar blocks, walls of dressed stone rising from it, "
        "timber scaffolding lashed with rope, a plumb line hanging true, "
        "baskets of lime mortar and mason's iron tools, pale stone dust in "
        "clear working daylight. The same rising house throughout — never "
        "finished, never modern scaffolding, never a crane or metal tool."
    ),
    "BUILDERS": (
        "BUILDERS LOCK: first-century stonemasons — sturdy working men in "
        "short dust-greyed tunics, forearms bare, distinct sun-browned faces "
        "of varied ages (never cream); real labourers handling real stone, "
        "never twinned, never a cloned face."
    ),
    "WITNESSES": (
        "WITNESSES LOCK: the apostles and prophets as the foundation — a "
        "small line of resolute, dignified men standing firm on the great "
        "foundation stones: a couple of elder grey-bearded prophets and a few "
        "steady middle-aged apostles, plain earth-toned robes (never cream — "
        "only Jesus wears cream); distinct individuals, NOT posed as a named "
        "roster, never twinned, never a cloned face."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r163-b01", "out": "s01-once-strangers.jpeg", "seg": "n1",
        "window": "0.280-6.000", "wide": True, "jesus": False, "ref": False,
        "locks": ["OUTSIDERS", "HOUSEHOLD"],
        "narration": (
            "The people Paul was writing to had once been outsiders — "
            "foreigners, strangers, on the far edge of God's promises,"
        ),
        "must_show": "the ONE establishing wide of the family half — camera behind the small group of outsiders' backs at dusk, looking across open ground to a distant warm-lit household they are outside of; the distance between them and the light readable as geography.",
        "must_not_show": "not a crowd — a small group; the outsiders in shadow at the margin, the house far off; no faces posed at the lens; no modern building.",
        "scene": (
            "Belonging drawn as distance: the camera stands at dusk a few steps "
            "behind a small group of travel-worn outsiders, looking past their "
            "backs across open ground to a modest stone household warm with "
            "lamplight far off — a home they stand outside of, on the far "
            "edge, the space between them and its light the whole ache of the "
            "shot. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r163-b02", "out": "s02-no-place-at-the-table.jpeg", "seg": "n1",
        "window": "6.000-11.447", "wide": False, "jesus": False, "ref": False,
        "locks": ["OUTSIDERS"],
        "narration": "with no place at the table and no share in the family.",
        "must_show": "a close on the faces of the outsiders — chiefly ONE weary traveller (the bookend face) whose longing is plain: no place at the table, no share in the family; hold this face so it can return at the end.",
        "must_not_show": "no self-pity theatrics — quiet tiredness and longing; not the whole group, mainly the one face; no cream.",
        "scene": (
            "The far edge, held on a face: a close on the outsiders, and chiefly "
            "on one weary traveller whose eyes carry the whole of it — no place "
            "at any table, no share in any family, only the road and the cold "
            "outside the light. Dust on the skin, faded travelling cloth. This "
            "is the face the story will bring inside. Two hands, one head."
        ),
    },
    {
        "id": "v2-r163-b03", "out": "s03-something-changed.jpeg", "seg": "n2",
        "window": "11.447-13.558", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSEHOLD"],
        "narration": "But something had changed everything.",
        "must_show": "an insert of the heavy timber door of the household beginning to open from within, a widening band of warm lamplight falling out across the dark threshold — change arriving as a door not staying shut.",
        "must_not_show": "no figure yet; just the door easing open and the warm light widening; no glow around anything, only lamplight spilling through the gap.",
        "scene": (
            "Everything turns on a door that does not stay shut: an insert of "
            "the household's heavy timber door easing open from within, a "
            "widening band of warm lamplight falling out across the dark stone "
            "threshold — the exact moment the shut world becomes an open one. "
            "Weathered wood, iron hinges, real lamplight, nothing modern."
        ),
    },
    {
        "id": "v2-r163-b04", "out": "s04-brought-near.jpeg", "seg": "n2",
        "window": "13.558-22.251", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSEHOLD", "FAMILY", "OUTSIDERS"],
        "narration": (
            "The door had been thrown open, and those who were far off had been "
            "brought near — no longer guests to be tolerated, but family to be "
            "embraced."
        ),
        "must_show": "a two-shot at the threshold: a member of the household reaching out with both hands to draw the weary outsider in across the doorway, warm light behind them — welcome, not mere tolerance.",
        "must_not_show": "no stiff formal greeting — a real embrace/draw-inward; the outsider still road-worn, being pulled toward warmth; no cream on either.",
        "scene": (
            "Not tolerated, taken in: at the open doorway a member of the "
            "household reaches out with both hands and draws the weary "
            "traveller in across the threshold, the warm lamplight of the home "
            "spilling around them both — far-off made near, a guest becoming "
            "family in the space of one gesture. Both in earth-toned wool, each "
            "with two hands and one head."
        ),
    },
    {
        "id": "v2-r163-b05", "out": "s05-sons-and-daughters-at-home.jpeg", "seg": "n3",
        "window": "22.251-30.015", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSEHOLD", "FAMILY"],
        "narration": (
            "Paul reached for a beautiful picture: Not a crowd of strangers "
            "passing through, but sons and daughters at home, belonging."
        ),
        "must_show": "a warm interior: the family gathered close at the low lamplit table, the former outsider now seated among them mid-meal, at ease — sons and daughters at home, belonging, not passing through.",
        "must_not_show": "not a large crowd — a small family group; the former outsider clearly one of them now, relaxed; realistic lamplit room, no cream.",
        "scene": (
            "The picture Paul reached for, made warm: inside the lamplit house "
            "the family is gathered close at the low table, bread and fruit "
            "between them, and the once-weary traveller sits among them at ease, "
            "shoulders down, belonging — sons and daughters at home rather than "
            "strangers passing through. Distinct faces of all ages in earth-"
            "toned wool; every figure two hands, one head."
        ),
    },
    {
        "id": "v2-r163-b06", "out": "s06-fellowcitizens.jpeg", "seg": "kv19",
        "window": "30.015-38.285", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSEHOLD", "FAMILY"],
        "narration": (
            "Now therefore ye are no more strangers and foreigners, but "
            "fellowcitizens with the saints, and of the household of God;"
        ),
        "must_show": "SCRIPTURE-EXACT: a close on the former outsider's face — the same face that longed outside in b02 — now at rest in the warm household, fully one of them; no more a stranger, of the household of God.",
        "must_not_show": "must read as the SAME person from b02, now belonging; no cream; the change is on the face, not in captions.",
        "scene": (
            "The verse landing on a single changed face: a close on the traveller "
            "who stood longing in the dark — the very same face — now warm in "
            "the lamplight of the household, the tiredness eased into rest, no "
            "more a stranger or a foreigner but of the family, of the household "
            "of God. Earth-toned wool, one head, warm light on the skin, nothing "
            "around the head."
        ),
    },
    {
        "id": "v2-r163-b07", "out": "s07-a-house-must-be-built.jpeg", "seg": "n4",
        "window": "38.285-42.793", "wide": True, "jesus": False, "ref": False,
        "locks": ["BUILD-SITE", "BUILDERS"],
        "narration": (
            "But a household needs a house — and a house needs to be built, and "
            "built right."
        ),
        "must_show": "the ONE establishing wide of the building half — camera at the site's edge from the side, behind a mason's shoulder and back, looking across the deep foundation course and rising dressed-stone walls with scaffolding; the picture has changed from family to construction.",
        "must_not_show": "no crane or modern scaffolding; masons at work, not posing; the change of subject (family -> building) clear; the site orderly, not rubble.",
        "scene": (
            "Paul changes the picture, and so does the camera: the camera stands "
            "at the site's edge from the side, behind a working mason's shoulder "
            "and back, and we look past them across a deep "
            "level foundation course and dressed-stone walls rising under lashed "
            "timber scaffolding in clear working daylight — a household needs a "
            "house, and a house has to be built, and built right. Real "
            "first-century stonework, pale dust in the light; every man two "
            "hands, one head."
        ),
    },
    {
        "id": "v2-r163-b08", "out": "s08-the-dwelling-place.jpeg", "seg": "n4",
        "window": "42.793-49.015", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILD-SITE", "BUILDERS"],
        "narration": (
            "So Paul changed the picture from a family to a building, the "
            "dwelling place of God among his people."
        ),
        "must_show": "a medium of masons setting a course of dressed stones into the rising wall, mortar and plumb line in use — the dwelling place taking real shape, stone on stone.",
        "must_not_show": "no modern tools; the work coordinated and careful; not a crowd, two or three masons; no cream.",
        "scene": (
            "A dwelling made the slow honest way: two or three masons lift and "
            "seat a course of dressed limestone into the rising wall, lime "
            "mortar spread, the plumb line hanging true beside them — the "
            "dwelling place of God among his people taking shape stone by "
            "deliberate stone. Dust-greyed tunics, real iron tools; each man "
            "two hands, one head."
        ),
    },
    {
        "id": "v2-r163-b09", "out": "s09-rests-on-a-foundation.jpeg", "seg": "n5",
        "window": "49.015-51.663", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILD-SITE"],
        "narration": "Every real building rests on a foundation.",
        "must_show": "an insert low along the great foundation course — massive squared limestone blocks set deep and dead level, a plumb line and the shadow of the rising wall above; the solid ground the rest will stand on.",
        "must_not_show": "no figures needed; just the deep, level, massive foundation stones, real and heavy; nothing invented carved into them.",
        "scene": (
            "What everything else will rest on: an insert running low along the "
            "great foundation course — massive squared limestone blocks set deep "
            "and dead level, joints tight, a plumb line true against them and "
            "the rising wall's shadow above — the solid ground the whole "
            "structure will stand on. Real weathered stone, nothing carved or "
            "invented."
        ),
    },
    {
        "id": "v2-r163-b10", "out": "s10-apostles-and-prophets.jpeg", "seg": "n5",
        "window": "51.663-63.134", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILD-SITE", "WITNESSES"],
        "narration": (
            "And this one, Paul said, was laid on the apostles and the prophets "
            "— men God had called and taught, whose witness became the solid "
            "ground the whole structure would stand on."
        ),
        "must_show": "a small line of the apostles and prophets standing firm ON the great foundation stones — a couple of elder prophets and a few steady apostles, resolute, the rising walls behind them; the men who ARE the foundation.",
        "must_not_show": "NOT the named Twelve posed as a roster — generic dignified witnesses, distinct faces, no cloned faces; not a crowd; no cream.",
        "scene": (
            "The foundation given faces: a small line of resolute men stands "
            "firm along the great foundation course — a couple of elder "
            "grey-bearded prophets and a few steady middle-aged apostles, plain "
            "earth-toned robes, the rising dressed-stone walls behind them — men "
            "God called and taught, whose witness became the solid ground the "
            "whole house would stand on. Distinct individuals, never cloned; "
            "each two hands, one head."
        ),
    },
    {
        "id": "v2-r163-b11", "out": "s11-the-cornerstone-set.jpeg", "seg": "n6",
        "window": "63.134-70.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILD-SITE", "BUILDERS"],
        "narration": (
            "And at the most important place of all — the cornerstone, the "
            "stone that sets the angle, holds two walls together, and keeps the "
            "whole building square and true —"
        ),
        "must_show": "an insert of the great squared cornerstone at the angle where two walls meet — masons aligning it with the plumb line, both walls keyed to it; the one stone that sets the angle and keeps everything square.",
        "must_not_show": "no figure of Christ yet (that is the next beat); focus on the cornerstone itself at the corner, plumb and true; no invented mark on the stone.",
        "scene": (
            "The one stone everything else obeys: an insert of the great squared "
            "cornerstone seated at the exact angle where two rising walls meet, "
            "masons checking it against the plumb line, both courses keyed into "
            "it — the stone that sets the angle, holds two walls together and "
            "keeps the whole building square and true. Massive dressed "
            "limestone, real tools; hands whole, five fingers each."
        ),
    },
    {
        "id": "v2-r163-b12", "out": "s12-christ-himself.jpeg", "seg": "n6",
        "window": "70.000-77.797", "wide": False, "jesus": True, "ref": True,
        "locks": ["BUILD-SITE"],
        "narration": "stood Christ himself. Everything is lined up to him.",
        "must_show": "Jesus standing at the cornerstone of the rising house, one hand laid on the great squared corner stone, the two walls and the builders' work visibly aligning to him — everything lined up to him; he is the cornerstone made personal.",
        "must_not_show": "Jesus NOT turned into a literal stone and NOT enlarged (ordinary-sized man); no light around his head; his hand ON the cornerstone, calm and central.",
        "scene": (
            "The cornerstone with a face: Jesus stands at the angle of the "
            "rising house, one hand laid on the great squared corner stone, the "
            "two walls and every line of the builders' work running true toward "
            "where he stands — everything lined up to him. Warm working daylight "
            "plain on his tanned skin, dark hair and beard, and his cream robe. "
            "He is an ordinary-sized man with two hands and one head; nothing "
            "lights his head."
        ),
    },
    {
        "id": "v2-r163-b13", "out": "s13-chief-corner-stone.jpeg", "seg": "kv20",
        "window": "77.797-86.193", "wide": False, "jesus": True, "ref": True,
        "locks": ["BUILD-SITE", "WITNESSES"],
        "narration": (
            "And are built upon the foundation of the apostles and prophets, "
            "Jesus Christ himself being the chief corner stone;"
        ),
        "must_show": "SCRIPTURE-EXACT: the whole design in one frame — Jesus at the cornerstone with his hand on it, the line of apostles and prophets on the foundation to one side, the rising house keyed to him; foundation, witnesses and cornerstone together.",
        "must_not_show": "Jesus ordinary-sized among the men, never a giant; no halo/light around his head; the witnesses distinct, not cloned; groups small, not a crowd.",
        "scene": (
            "The verse assembled into one steady composition: Jesus stands at "
            "the chief corner stone with his hand on it, and to one side the "
            "small line of apostles and prophets stands firm on the great "
            "foundation course, the rising walls of the house keyed true to the "
            "corner where he stands — built on the foundation of the apostles "
            "and prophets, Jesus Christ himself the chief corner stone. Jesus in "
            "cream and ordinary-sized; every figure two hands, one head."
        ),
    },
    {
        "id": "v2-r163-b14", "out": "s14-a-design.jpeg", "seg": "n7",
        "window": "86.193-92.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILD-SITE"],
        "narration": (
            "So the church was never meant to be a loose, shapeless crowd. It "
            "has a design —"
        ),
        "must_show": "a medium of the house now clearly shaped and ordered — squared walls rising true from the foundation to the cornerstone, everything plumb and deliberate; a design, not a heap.",
        "must_not_show": "no chaos or rubble; the structure ordered and intentional; no figures needed, or masons small; no invented plans-on-paper prop.",
        "scene": (
            "Not a heap — a design: a medium of the rising house seen whole, "
            "squared dressed-stone walls climbing true from the deep foundation "
            "to the keyed cornerstone, every course deliberate and plumb — the "
            "opposite of a loose, shapeless crowd, a thing built to a shape. "
            "Clear working daylight, real stone, nothing modern."
        ),
    },
    {
        "id": "v2-r163-b15", "out": "s15-living-people-fitted.jpeg", "seg": "n7",
        "window": "92.000-100.449", "wide": False, "jesus": False, "ref": False,
        "locks": ["BUILD-SITE", "FAMILY"],
        "narration": (
            "a foundation of apostles and prophets, a cornerstone that is "
            "Christ, and living people fitted together into a home for God. "
            "There is a blueprint."
        ),
        "must_show": "living people being welcomed into their place in the structure — ordinary believers (the family faces) stepping into the walls' shelter as if fitted in like stones, a house becoming a home for God.",
        "must_not_show": "not people literally turned to stone — real people finding their place within the built house; small group, distinct faces; no cream; no glow.",
        "scene": (
            "The stones that breathe: ordinary believers — the same warm family "
            "faces — step into their places within the sheltering built walls, "
            "each fitted in and settling as if the house had been waiting for "
            "exactly them, a structure of stone becoming a home for God. Small, "
            "distinct group in earth-toned wool; every figure two hands, one "
            "head."
        ),
    },
    {
        "id": "v2-r163-b16", "out": "s16-not-a-stranger.jpeg", "seg": "n8",
        "window": "100.449-105.293", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSEHOLD"],
        "narration": (
            "And the best part is where that leaves you. You are not a stranger "
            "at the door."
        ),
        "must_show": "the bookend — a close on the once-weary traveller (the b02/b06 face) now standing INSIDE the finished doorway, warm light around them, no longer outside; not a stranger at the door but through it.",
        "must_not_show": "must read as the SAME person from b02; no longer road-worn and cold — at home; no cream; the doorway finished now, not under construction.",
        "scene": (
            "The bookend closes: the traveller who stood longing outside in the "
            "dark now stands INSIDE the finished doorway of the home, warm light "
            "around them, the road washed off — not a stranger at the door but a "
            "person through it, where they belong. The same face as the "
            "longing one, at rest. Earth-toned wool, two hands, one head."
        ),
    },
    {
        "id": "v2-r163-b17", "out": "s17-you-have-a-place.jpeg", "seg": "n8",
        "window": "105.293-110.634", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSEHOLD", "FAMILY"],
        "narration": (
            "In this house you have a place, fitted in and belonging, part of "
            "what God is building."
        ),
        "must_show": "the former outsider now settled among the household inside the warm home — a place clearly theirs, welcomed and belonging, part of what is being built.",
        "must_not_show": "not passing through — a place that is theirs; small warm family group; no cream; realistic lamplit interior.",
        "scene": (
            "A place with their name on it: the former outsider sits settled "
            "among the household in the warm lamplit home, welcomed hands and "
            "easy faces around them — a place that is theirs, fitted in and "
            "belonging, part of what God is building rather than a guest soon "
            "gone. Distinct earth-toned family; every figure two hands, one "
            "head."
        ),
    },
    {
        "id": "v2-r163-b18", "out": "s18-will-you-come-inside.jpeg", "seg": "n8",
        "window": "110.634-116.714", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSEHOLD"],
        "narration": (
            "So the only question is a hopeful one. When he offers you a place "
            "in it, will you come inside?"
        ),
        "must_show": "the closing invitation to the viewer — the finished home's open door seen from OUTSIDE, warm lamplight spilling out toward the camera, a welcoming hand extended from within across the threshold; the doorway offered to 'you'.",
        "must_not_show": "no face required — the camera is 'you'; an OPEN welcoming door and an offered hand, warm light spilling out; no glow around anything, only lamplight; nothing invented.",
        "scene": (
            "The film holds the door for the person watching: the finished home's "
            "heavy timber door stands open, seen from outside on the threshold, "
            "warm lamplight spilling out across the stone toward the lens, and a "
            "welcoming hand reaches out from within — a place offered, the way in "
            "clear, the only question a hopeful one. Real doorway, real "
            "lamplight, an open hand with five fingers; nothing modern, nothing "
            "invented."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
