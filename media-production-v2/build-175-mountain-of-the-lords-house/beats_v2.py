#!/usr/bin/env python3
"""V2 beat map — row 175, build-175-mountain-of-the-lords-house (Isaiah 2:2-3,
"the mountain of the LORD's house shall be established in the top of the
mountains... and all nations shall flow unto it").

COVERAGE: 15 pictures over 73.31 s (card_start) = ~4.9 s/picture (lesson 12
movie-coverage). ONE establishing wide per place (b01 the mountain temple, b05 the
ascending path of the nations); every other beat is a single, a close or a
two-shot.

NO OPEN CAMERON COMPLAINT — `v2_outline.py 175` shows none. Fresh V2 picture map
on the already-authored SPEAKER-LAW narration (audio OK).

SPEAKER LAW: Isaiah — s1, s2a and s2b are the SCRIPTURE voice → LIGHT-BLUE
captions. The narration itself states it plainly in n0b ("That is Isaiah writing,
NOT God speaking"), so there is NO red-letter and NO God-voice in this row.
**GOD IS NEVER EMBODIED** — no figure, face, hand, beam or shaft from heaven
anywhere; his teaching "going out" (b11/b14) is carried by PEOPLE, shown as
natural light. NO Jesus and NO cream anywhere in this row (Isaiah's vision, OT).

CONTENT-CARE: the "house of the LORD" is a grand ANCIENT stone temple exalted on
a mountain (credible first-century-world biblical architecture, in the manner of
the Jerusalem temple) — NEVER a modern building and NEVER a specific real
present-day temple. "All nations" are diverse peoples of the ANCIENT world in
varied period dress (never modern clothing, flags or signage). No rendered
writing anywhere (captions live in the bottom band only).

PLACES:
  MOUNTAIN-TEMPLE (NEW build-local)  the exalted house of the Lord on the summit
                                     (b01-b04, b09, b11, b14)
  MOUNTAIN-PATH (NEW build-local)    the ascending roads where the nations stream
                                     up, and Isaiah's vantage (b05-b08, b10, b12,
                                     b13, b15)
NEW places (runner promotes each from its first good frame, lesson 11):
  MOUNTAIN-TEMPLE  promote b01
  MOUNTAIN-PATH    promote b05 (its establishing wide)
Steps in QC.md.
"""

# LOCKS: all build-local. ISAIAH is BYTE-IDENTICAL to build-192/build-198 (recurring
# cast — the prophet is one man across all his videos; unified 2026-08-07, author lane).
# No cream on anyone (only Jesus wears cream, and Jesus is not in this row).
LOCKS = {
    "MOUNTAIN-TEMPLE": (
        "MOUNTAIN-TEMPLE LOCK: the same place in every frame — a grand ANCIENT "
        "stone temple, the house of the Lord, standing exalted on the flat summit "
        "of a high mountain that rises above every hill around it. It is credible "
        "first-century-world biblical architecture in the manner of the Jerusalem "
        "temple: dressed pale-gold limestone, broad steps, tall plain columns and "
        "a wide open forecourt, warm dawn light on the stone, ranked hills falling "
        "away far below on every side under an open sky. The same temple, summit "
        "and hills throughout — NEVER a modern building, dome of glass or steel, "
        "spire, sign, wire, pole or fixture, never a specific present-day temple, "
        "and no rendered writing of any kind."
    ),
    "MOUNTAIN-PATH": (
        "MOUNTAIN-PATH LOCK: the same place in every frame — the broad worn roads "
        "and stone stairways that climb the flanks of the high mountain toward the "
        "temple on its summit, winding up bare terraced slopes and pale rock under "
        "an open sky, the ranked lower hills spread out far below. The same slopes, "
        "roads and stairways throughout — never modern surfacing, rail, wire, pole "
        "or sign, and no rendered writing of any kind."
    ),
    "ISAIAH": (
        "ISAIAH LOCK: the same man in every frame he appears — Isaiah, an Old Testament "
        "prophet of about fifty-five, warm tan sun-worn skin, dark hair going grey and a "
        "full dark-grey beard, deep steady eyes, in a plain undyed brown-and-ochre wool "
        "prophet's robe with a coarse mantle (never cream, never white). Grave, earnest "
        "and unafraid, one arm often raised as he declares. The same face, beard and robe "
        "throughout."
    ),
    "NATIONS-PILGRIMS": (
        "NATIONS-PILGRIMS LOCK: the peoples of many ancient nations streaming up "
        "toward the temple — a mixed, diverse crowd of ordinary men, women and "
        "children of different lands and complexions of the ANCIENT world, in "
        "varied period dress of hand-woven wool and linen, some with staffs, "
        "bundles or water-skins for the journey, none in cream. Distinct, "
        "ordinary-sized people, never twinned, never cloned faces, never modern "
        "clothing, flags or signage."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r175-b01", "out": "s01-the-mountain-at-dawn.jpeg", "seg": "n0",
        "window": "0.400-4.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-TEMPLE"],
        "narration": "In the last days, a mountain would rise above all mountains —",
        "must_show": "the ONE establishing wide of the mountain temple — the camera looks up from far below toward the great ancient house of the Lord standing exalted on the summit above all the ranked hills, in the first dawn light; a mountain risen above all mountains.",
        "must_not_show": "no God figure, face or beam; no modern building, dome, spire, sign or fixture; no specific present-day temple; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object.",
        "scene": (
            "The camera is set low on the valley floor far below and looks up in "
            "a high three-quarter view across ranked lower hills toward "
            "the flat high summit, where a grand ancient stone temple of dressed "
            "pale-gold limestone stands exalted in the first warm dawn light, "
            "raised above every hill around it under a wide open sky. Bare terraced "
            "slopes fall away beneath it. It is credible ancient biblical "
            "architecture, broad-stepped and plain-columned; nothing is written "
            "anywhere on it and no light rings it — only the dawn on the stone."
        ),
    },
    {
        "id": "v2-r175-b02", "out": "s02-drawing-every-people.jpeg", "seg": "n0",
        "window": "4.500-8.129", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-TEMPLE", "NATIONS-PILGRIMS"],
        "narration": "not by height, but by drawing every people to it.",
        "must_show": "the draw — the summit temple beyond, and in the middle distance a scattering of ordinary people of different lands turning and beginning to move toward it; drawn, not driven.",
        "must_not_show": "no God figure or beam; no modern building, dress, flag or sign; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "Below the exalted stone temple on the summit, in the middle distance "
            "a scattering of ordinary people of different ancient lands and "
            "complexions turn and begin to walk toward it across the terraced "
            "slopes — drawn toward the house of the Lord rather than driven. Warm "
            "dawn light lies over the hills. Ordinary-sized, distinct people with "
            "two hands and one head each, none in cream and none turned to the "
            "camera; nothing is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r175-b03", "out": "s03-established-on-the-top.jpeg", "seg": "s1",
        "window": "8.129-12.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-TEMPLE"],
        "narration": "And it shall come to pass in the last days, that the mountain of the LORD's house shall be established in the top of the mountains,",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the house established on the height: a nearer view of the ancient temple standing solid and settled on the summit stone, firmly founded above the mountains.",
        "must_not_show": "no God figure or beam; no modern building, dome, spire or sign; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object.",
        "scene": (
            "A nearer view of the great ancient temple settled solid on the summit "
            "stone, its broad steps and plain columns firm in the dawn light, the "
            "ranked mountains standing lower all around it — the house of the Lord "
            "established in the top of the mountains. Nothing is written anywhere "
            "on the stone and no light rings it, only clean morning light."
        ),
    },
    {
        "id": "v2-r175-b04", "out": "s04-exalted-above-the-hills.jpeg", "seg": "s1",
        "window": "12.500-16.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-TEMPLE"],
        "narration": "and shall be exalted above the hills;",
        "must_show": "SCRIPTURE-EXACT — the temple lifted high: a view from the forecourt edge looking outward and down over the far-below hills, the house raised above them all; exalted above the hills.",
        "must_not_show": "no God figure or beam; no modern building or fixture; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object.",
        "scene": (
            "From the edge of the temple's stone forecourt the view opens outward "
            "and down over ranked hills lying far below in the morning haze, the "
            "great house standing raised high above them all. Pale dressed stone "
            "and open sky frame the drop. Nothing is written anywhere and no light "
            "rings anything — only the height and the morning air."
        ),
    },
    {
        "id": "v2-r175-b05", "out": "s05-all-nations-flow.jpeg", "seg": "s1",
        "window": "16.800-21.161", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "NATIONS-PILGRIMS"],
        "narration": "and all nations shall flow unto it.",
        "must_show": "SCRIPTURE-EXACT — the ONE establishing wide of the ascent: the camera looks up the mountain road from behind the pilgrims as a mixed multitude of many ancient nations streams steadily up toward the summit temple; all nations flowing to it.",
        "must_not_show": "no God figure or beam; no modern dress, flag, sign, vehicle or fixture; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no posed line to the lens.",
        "scene": (
            "The camera stands on the mountain road behind the backs of the "
            "pilgrims and looks up the winding stone way toward the distant summit "
            "temple: a broad, mixed multitude of ordinary people of many ancient "
            "lands and complexions — men, women and children with staffs and "
            "bundles — climbs steadily upward in a living stream. Bare terraced "
            "slopes and far hills fall away on either side. Ordinary-sized, "
            "distinct people with two hands and one head each, none in cream and "
            "none turned to the camera; nothing is written anywhere and no light "
            "rings any head."
        ),
    },
    {
        "id": "v2-r175-b06", "out": "s06-isaiah-beholds.jpeg", "seg": "n0b",
        "window": "21.161-27.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "ISAIAH"],
        "narration": "That is Isaiah writing, not God speaking — a prophet describing what he was shown.",
        "must_show": "the prophet who saw it — Isaiah standing on a height, one hand lifted toward the distant summit temple, gazing at the vision he was shown; a man describing what he sees, not God.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam; no rendered writing, scroll-text or legible lettering; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "On a rocky height above the road the prophet Isaiah stands in his "
            "brown-and-ochre wool prophet's robe and coarse mantle, one hand lifted toward the far "
            "summit temple, his bearded face grave and far-seeing as he takes in "
            "the vision he has been shown — a man beholding and describing, not a "
            "god speaking. The mountain and the ascending road lie below him under "
            "the open sky. An ordinary-sized man with two hands and one head, not "
            "in cream, his gaze on the distant temple and not the camera; nothing "
            "is written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r175-b07", "out": "s07-every-nation-streaming.jpeg", "seg": "n0b",
        "window": "27.500-37.869", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "NATIONS-PILGRIMS"],
        "narration": "the house of the Lord will be set up higher than anything else on earth, and people from every nation will come streaming toward it.",
        "must_show": "the streaming nations, closer — a nearer look along the climbing road at the mixed pilgrims of many lands moving upward together, the summit temple high beyond; every nation coming.",
        "must_not_show": "no God figure or beam; no modern dress, flag, sign or vehicle; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "A nearer look along the climbing mountain road: ordinary pilgrims of "
            "many ancient lands and complexions move upward together in an easy, "
            "steady flow — an old couple, a family with a child, travellers with "
            "staffs — the exalted summit temple standing high beyond them in the "
            "morning light. Terraced slopes fall away below. Ordinary-sized, "
            "distinct people with two hands and one head each, none in cream, their "
            "faces set up the road and not to the camera; nothing is written "
            "anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r175-b08", "out": "s08-come-let-us-go-up.jpeg", "seg": "s2a",
        "window": "37.869-42.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "NATIONS-PILGRIMS"],
        "narration": "And many people shall go and say, Come ye, and let us go up to the mountain of the LORD, to the house of the God of Jacob;",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the invitation among the people: on the road, one pilgrim turning to beckon others onward and upward with an open, glad gesture; come, let us go up.",
        "must_not_show": "no God figure or beam; no modern dress, flag or sign; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Close on the climbing road: one ordinary pilgrim turns back toward "
            "companions behind and beckons them onward and up with an open, glad "
            "hand, his face eager, others answering the call — people inviting one "
            "another up to the house of the Lord. The road climbs on toward the "
            "far summit beyond. Ordinary-sized, distinct people with two hands and "
            "one head each, none in cream, their eyes on one another and the road, "
            "not the camera; nothing is written anywhere and no light rings any "
            "head."
        ),
    },
    {
        "id": "v2-r175-b09", "out": "s09-he-will-teach-us.jpeg", "seg": "s2a",
        "window": "42.500-46.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-TEMPLE", "NATIONS-PILGRIMS"],
        "narration": "and he will teach us of his ways,",
        "must_show": "SCRIPTURE-EXACT — the learning at the house: in the temple forecourt pilgrims of many lands gathered and seated to be taught, faces attentive and lifted; he will teach us of his ways.",
        "must_not_show": "no God figure or beam (the teaching is received, the teacher unseen or an ordinary elder); no modern building or dress; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "In the broad stone forecourt of the summit temple, pilgrims of many "
            "ancient lands sit gathered on the warm paving, faces attentive and "
            "lifted as they are taught, an ordinary robed elder among them "
            "gesturing as he instructs — the ways of the Lord being learned. Pale "
            "columns and the open sky stand beyond. Ordinary-sized, distinct "
            "people with two hands and one head each, none in cream, their eyes on "
            "the teaching and not the camera; nothing is written anywhere and no "
            "light rings any head."
        ),
    },
    {
        "id": "v2-r175-b10", "out": "s10-walk-in-his-paths.jpeg", "seg": "s2a",
        "window": "46.500-50.175", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "NATIONS-PILGRIMS"],
        "narration": "and we will walk in his paths:",
        "must_show": "SCRIPTURE-EXACT — the walking — a close on pilgrims' feet and the worn stone path, sandalled feet moving steadily up the mountain way; we will walk in his paths.",
        "must_not_show": "no God figure or beam; no modern surfacing, footwear or object; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel.",
        "scene": (
            "A low close on the worn stone path of the mountain road, several "
            "pairs of ordinary sandalled feet in earth-toned hems moving steadily "
            "upward over the pale dressed stone — the plain, deliberate act of "
            "walking in his paths, the way climbing on toward the summit ahead. "
            "Dust and morning light lie on the stone; nothing is written anywhere "
            "and no light rings anything."
        ),
    },
    {
        "id": "v2-r175-b11", "out": "s11-out-of-zion.jpeg", "seg": "s2b",
        "window": "50.175-56.408", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-TEMPLE", "NATIONS-PILGRIMS"],
        "narration": "for out of Zion shall go forth the law, and the word of the LORD from Jerusalem.",
        "must_show": "SCRIPTURE-EXACT — the word going out: from the temple forecourt people setting out and DOWN the mountain roads in several directions, carrying the teaching outward from Zion to the world.",
        "must_not_show": "no God figure, beam or glowing word/scroll in the sky; no rendered writing or lettering; no modern building or dress; no Jesus and no cream; no halo, glare or rim-light; no modern object; no posed line to the lens.",
        "scene": (
            "From the edge of the summit temple's forecourt, people who have been "
            "taught set out and down the mountain roads in several directions, "
            "purposeful and glad, carrying what they have learned outward from the "
            "house of the Lord toward the lands below — the law and the word going "
            "forth from Zion. The ranked hills and open sky lie beyond. "
            "Ordinary-sized, distinct people with two hands and one head each, "
            "none in cream, their faces set outward down the roads and not to the "
            "camera; nothing is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r175-b12", "out": "s12-drawn-by-invitation.jpeg", "seg": "n1",
        "window": "56.408-61.300", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "NATIONS-PILGRIMS"],
        "narration": "Nations streaming uphill — not summoned by force, but drawn by invitation.",
        "must_show": "the willing climb — a warm nearer view of the pilgrims of many lands climbing gladly and unhurried, faces open and eager; drawn by invitation, not driven by force.",
        "must_not_show": "NO soldier, weapon, chain, coercion or force of any kind; no God figure or beam; no modern dress, flag or sign; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "A warm nearer view of the mountain road: pilgrims of many ancient "
            "lands climb gladly and unhurried, faces open and eager, helping one "
            "another over the steeper stone — a crowd that has come because it "
            "chose to, drawn by invitation and not driven by force. The summit "
            "temple stands high beyond. Ordinary-sized, distinct people with two "
            "hands and one head each, none in cream, their faces up the road and "
            "not to the camera; nothing is written anywhere and no light rings any "
            "head."
        ),
    },
    {
        "id": "v2-r175-b13", "out": "s13-the-mountain-all-choose.jpeg", "seg": "n1",
        "window": "61.300-65.251", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "NATIONS-PILGRIMS"],
        "narration": "The mountain everyone chooses to climb.",
        "must_show": "close on a few glad faces among the pilgrims turned upward toward the summit, having chosen to make the climb; the mountain everyone chooses.",
        "must_not_show": "no God figure or beam; no modern dress or object; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no face posed to the lens.",
        "scene": (
            "A close among the climbing pilgrims: a few distinct faces of "
            "different ancient lands lifted upward toward the summit temple, "
            "tired but glad, eyes set on the height they have chosen to climb. "
            "The road and slopes sit soft behind them. Ordinary-sized, distinct "
            "people with two hands and one head each, none in cream, their eyes up "
            "toward the temple and not the camera; nothing is written anywhere and "
            "no light rings any head."
        ),
    },
    {
        "id": "v2-r175-b14", "out": "s14-teaching-goes-out.jpeg", "seg": "n2a",
        "window": "65.251-69.915", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-TEMPLE", "NATIONS-PILGRIMS"],
        "narration": "And from that high place, God's teaching would go out",
        "must_show": "the teaching sent from the height — from the summit forecourt, taught people turning to carry the word outward and down, the high place behind them and the wide world below; God's teaching going out through them.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand, beam or glowing word; no rendered writing; no modern building or dress; no Jesus and no cream; no halo, glare or rim-light; no modern object; no posed line to the lens.",
        "scene": (
            "High on the temple forecourt, people who have been taught turn to go "
            "outward and down, the great house behind them and the wide world of "
            "hills spread out far below — the teaching of the Lord carried out "
            "from the high place through ordinary people who received it. Warm "
            "morning light lies over the stone and the lands beyond. "
            "Ordinary-sized, distinct people with two hands and one head each, "
            "none in cream, their faces set outward and not to the camera; nothing "
            "is written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r175-b15", "out": "s15-to-everyone-everywhere.jpeg", "seg": "n2b",
        "window": "69.915-73.306", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN-PATH", "NATIONS-PILGRIMS"],
        "narration": "to everyone, everywhere.",
        "must_show": "the reach — a wide look down the mountain roads spreading out toward the far lands, small groups of the taught fanning outward in every direction to the world; to everyone, everywhere.",
        "must_not_show": "no God figure or beam; no modern dress, flag, sign or vehicle; no Jesus and no cream; no halo, glare or rim-light; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "A wide look down from the mountain over the roads spreading out "
            "across the hills toward far distant lands, small groups of the taught "
            "fanning outward along them in every direction under the bright "
            "morning sky — the word reaching outward toward everyone, everywhere. "
            "Ranked hills and far horizons open away beneath. Ordinary-sized, "
            "distinct people small in the distance, none in cream and none turned "
            "to the camera; nothing is written anywhere and no light rings any "
            "head."
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

# No image REFS: every person is carried by a byte-identical text lock (no face
# sheets exist for these figures). NO Jesus in this row.
REFS = {
}
