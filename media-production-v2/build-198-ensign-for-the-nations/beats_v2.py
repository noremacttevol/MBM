#!/usr/bin/env python3
"""V2 beat map — row 198, build-198-ensign-for-the-nations (Isaiah 11:10-12 — the root of
Jesse stands for an ensign of the people; "the Lord shall set his hand again the second time
to recover the remnant of his people... And he shall set up an ensign for the nations, and
shall assemble the outcasts of Israel, and gather together the dispersed of Judah from the
four corners of the earth").

COVERAGE: 12 pictures over 52.740 s (card_start) = ~4.40 s/picture (lesson 12 movie-coverage).
Three places: ISAIAH-HEIGHT (the prophet pointing far ahead, and the ENSIGN — a real banner —
raised on the height for the nations to see), GATHERING-ROADS (the outcasts and dispersed
streaming home from the four corners), and HOMELAND (the gathered come home). RESTORATION
cornerstone: the SECOND-TIME gathering of Israel, a banner raised so the scattered can find
their way home.

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 198): "Not new audio."
FIXED AT $0 (this Fable-5 author lane): all 7 segment mp3s in the V1 build's audio/ are
ElevenLabs new-voice (ffprobe-confirmed 44100/128k mono, identical spec to the fixed
row 191; audio-eleven.log + .audio-eleven-done marker dated 2026-07-29 09:47). The delivered
V1 mp4 (2026-07-23 06:56) PREDATES that re-voice and stream-copied the STALE old-voice track —
which is exactly what Cameron heard. This build now sets **AUDIO_FROM_V1_SEGMENTS = True** so
v2_assemble rebuilds the shipped track from those new-voice segments instead of copying the
stale mp4 audio. Same fix as rows 191/177/78/80/82. The review card MUST tell Cameron the
voice is the real new voice. See QC.md COMPLAINT LEDGER.
=====================================================================

SPEAKER LAW (Old-Testament prophecy, book of Isaiah):
  s1  Isaiah 11:11  "And it shall come to pass in that day, that the Lord shall set his hand
      again the second time to recover the remnant of his people..."   = SCRIPTURE → LIGHT-BLUE.
  s2  Isaiah 11:12  "And he shall set up an ensign for the nations, and shall assemble the
      outcasts of Israel, and gather together the dispersed of Judah from the four corners of
      the earth."                                                       = SCRIPTURE → LIGHT-BLUE.
n0, n1, n2, n3 and card are the NARRATOR → white. There is NO God-voice segment and NO
red-letter. **NO Jesus / NO cream / NO white** anywhere (Old Testament prophecy; cream is
reserved for Jesus, who is not embodied here).

**HARD GATE — GOD AND THE MESSIAH ARE NEVER EMBODIED.** "the root of Jesse", "this one would
stand as a banner... nations could find their way to Him", "the Lord shall set his hand again"
are NEVER shown as a figure, face, hand-from-sky, beam or symbol. Isaiah's own metaphor carries
the root of Jesse: a fresh GREEN SHOOT rising from an old cut TREE-STUMP (Isaiah 11:1 — "a rod
out of the stem of Jesse"), NOT a person. "Him" and the invitation are carried by the ENSIGN —
a real raised BANNER/standard on the height (a plain cloth banner on a tall pole; an object,
not a divine figure) — and by the gathering of real people. The "second time" recovery and the
gathering are carried by real exiles coming home. Drift-word gate: no halo / glow / rim-light /
beam in any scene text; the banner carries NO rendered writing.

CONTENT-CARE: the outcasts and dispersed (b06/b08/b09/b10) are weary travellers finding their
way home with growing hope and dignity — never misery, squalor, chains or gore. The gathering
is glad and hopeful, an invitation answered, never a forced march.

TIME-OF-DAY: bright warm daylight throughout, so the raised banner reads clearly against the
sky and the roads home are plainly seen. Not night; no divine light.

PLACES / LOCKS:
  ISAIAH-HEIGHT   the windswept height where Isaiah points ahead and the ensign banner is
                  raised for the nations (b01-b04, b07). NEW build-local place; promote b01.
  GATHERING-ROADS the roads from the four corners where the outcasts and dispersed stream home
                  toward the raised banner (b05, b06, b08-b11). NEW; promote b05.
  HOMELAND        the home country the scattered are gathered into (b12). NEW; promote b12.
People locks: ISAIAH (the prophet — BYTE-IDENTICAL to build-192), GATHERED-EXILES (the diverse
outcasts of Israel and dispersed of Judah returning from every nation). None wear cream/white.

AUDIO: AUDIO_FROM_V1_SEGMENTS = True (complaint fix — rebuild from the new-voice segments).
card_start = 52.740 s. Picture-only otherwise — do NOT re-voice (segments already correct).
"""

AUDIO_FROM_V1_SEGMENTS = True

# ISAIAH is reused BYTE-IDENTICAL to build-192 (recurring cast). ISAIAH-HEIGHT, GATHERING-ROADS
# and HOMELAND are NEW build-local places the runner promotes. Jesus / the Messiah is not
# embodied (every beat jesus=False); the root of Jesse is Isaiah's shoot-from-stump metaphor,
# the ensign is a real banner. No image REFS; only text locks. No one wears cream/white.
LOCKS = {
    "ISAIAH-HEIGHT": (
        "ISAIAH-HEIGHT LOCK: the same place in every frame — a windswept ancient stony "
        "height above a wide land, bare tan hills and a broad valley falling away under a "
        "bright open sky, a weathered olive tree-stump and an outcrop of rock on the "
        "summit, and a tall plain wooden pole where a banner is raised. Ancient Near-Eastern "
        "landscape only; no modern building, vehicle, pole-line, wire or sign; no rendered "
        "writing anywhere. The same height, valley and bright sky throughout, in warm "
        "daylight."
    ),
    "GATHERING-ROADS": (
        "GATHERING-ROADS LOCK: the same place in every frame — worn ancient roads and "
        "tracks winding down out of distant hills and across dry plains from many "
        "directions, converging toward a far height where a banner stands small on the "
        "skyline. Bare Near-Eastern country, low stone waymarks, dust and scrub. Ancient "
        "and real; no modern road, vehicle, pole, wire or sign, no rendered writing. The "
        "same converging roads and the distant banner throughout, in warm daylight."
    ),
    "HOMELAND": (
        "HOMELAND LOCK: the same place in every frame — the home country the scattered are "
        "gathered into: a green sheltered valley of terraced fields, olive groves, a few "
        "low stone houses and a well, warm and welcoming after the long roads. Ancient and "
        "real; no modern building, vehicle, pole, wire or sign, no rendered writing. The "
        "same home valley throughout, in warm daylight."
    ),
    "ISAIAH": (
        "ISAIAH LOCK: the same man in every frame he appears — Isaiah, an Old Testament "
        "prophet of about fifty-five, warm tan sun-worn skin, dark hair going grey and a "
        "full dark-grey beard, deep steady eyes, in a plain undyed brown-and-ochre wool "
        "prophet's robe with a coarse mantle (never cream, never white). Grave, earnest "
        "and unafraid, one arm often raised as he declares. The same face, beard and robe "
        "throughout."
    ),
    "GATHERED-EXILES": (
        "GATHERED-EXILES LOCK: the outcasts of Israel and dispersed of Judah returning — a "
        "wide, diverse mix of ordinary Hebrew and other ancient peoples of every age and "
        "both sexes, of varied skin-tones, in worn dusty travelling wool and linen (none "
        "in cream, none in white), some with bundles, staffs, water-skins and children. "
        "Weary but hopeful travellers with dignity; distinct individual faces, never twins "
        "or cloned faces; ordinary-sized, two hands and one head each; no modern clothing, "
        "packs, tools, flags or signage."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r198-b01", "out": "s01-isaiah-points-ahead.jpeg", "seg": "n0",
        "window": "0.000-4.800", "wide": True, "jesus": False, "ref": False,
        "locks": ["ISAIAH-HEIGHT", "ISAIAH"],
        "narration": "The prophet Isaiah pointed far ahead to a figure he called the root of Jesse —",
        "must_show": "the establishing frame (NON-Jesus, the plate the runner promotes) — Isaiah on the windswept height, arm extended toward the far horizon, pointing ahead to a day and a One yet to come; the empty tall banner-pole and the old tree-stump on the summit with him.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Messiah figure, face, hand-from-sky or beam; no halo or ring of light; no modern object; no rendered writing on the banner or anywhere; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "An establishing wide on the windswept height in warm daylight, camera set behind "
            "and to the side of Isaiah so his back is three-quarters to the lens and his arm "
            "and gaze reach far out toward the horizon, never to the camera: Isaiah — a "
            "grey-bearded prophet in brown-and-ochre wool (not cream) — stands on the summit "
            "pointing far ahead to a day yet to come. A tall plain wooden banner-pole (no "
            "banner yet) and an old weathered olive tree-stump stand near him; bare hills "
            "fall away to the bright horizon. Ordinary-sized; warm daylight on him and the "
            "land, not around his head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b02", "out": "s02-the-root-of-jesse.jpeg", "seg": "n0",
        "window": "4.800-10.180", "wide": False, "jesus": False, "ref": False,
        "locks": ["ISAIAH-HEIGHT"],
        "narration": "David's family tree, springing new life from an old, cut-down stump.",
        "must_show": "an insert of Isaiah's own metaphor — a fresh, living GREEN SHOOT rising straight out of an old cut-down tree-stump; new life from the family tree of Jesse. NO person, NO figure.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Messiah figure or face; no person at all in this insert; no halo or ring of light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert on the summit in warm daylight: a fresh, vivid GREEN SHOOT with "
            "tender new leaves rises straight up out of the grey, weathered, cut-down "
            "tree-stump — new life springing from the old stem of Jesse, Isaiah's own image "
            "of the root of Jesse. Just the stump and the living shoot, no person in frame. "
            "Warm daylight on the shoot, not a ring of light anywhere; nothing is written; no "
            "divine figure."
        ),
    },
    {
        "id": "v2-r198-b03", "out": "s03-stand-as-a-banner.jpeg", "seg": "n1",
        "window": "10.180-14.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["ISAIAH-HEIGHT", "ISAIAH"],
        "narration": "This one would stand as a banner, a signal, lifted up",
        "must_show": "the ensign raised — a plain cloth banner run up the tall pole on the height and catching the wind; a signal lifted up. Isaiah beside it, hand on the halyard. The banner is a real object; no figure stands on the height as the banner.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Messiah figure standing in for the banner; no halo or ring of light; no rendered writing or emblem on the banner; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot on the height in warm daylight: a plain, undecorated cloth banner is run "
            "up the tall wooden pole and catches the wind, lifted high as a signal; Isaiah "
            "(not cream) stands at the foot of the pole, a hand on the raising-cord, looking "
            "up at it. The banner is a plain object with nothing written or emblazoned on it. "
            "His gaze is up at the banner, not to the camera; warm daylight on the banner and "
            "the height, not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b04", "out": "s04-so-nations-find-the-way.jpeg", "seg": "n1",
        "window": "14.200-19.100", "wide": False, "jesus": False, "ref": False,
        "locks": ["ISAIAH-HEIGHT"],
        "narration": "so the nations could find their way to Him. Not hidden. Raised high, for all to see.",
        "must_show": "the banner high on the height against the open sky, plainly visible for miles, roads and lands falling away below it — raised high, not hidden, so the far nations can see it and find their way.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Messiah figure; no halo or ring of light; no rendered writing on the banner; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A wide low-angle on the height in warm daylight, camera set low at the foot of "
            "the banner-pole looking up along it to the broad open sky so the pole and banner "
            "lead the eye up and away and no person is in frame facing the lens: the plain "
            "banner stands high against the sky, the hills and roads of the land falling away "
            "far below, plainly visible for miles — raised high and not hidden so the distant "
            "nations can see it and find their way. The banner carries nothing written. Warm "
            "daylight and open sky around it, not a ring of light; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b05", "out": "s05-the-second-time.jpeg", "seg": "s1",
        "window": "19.100-22.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING-ROADS", "GATHERED-EXILES"],
        "narration": "And it shall come to pass in that day, that the Lord shall set his hand again the second time",
        "must_show": "BLUE caption (SCRIPTURE) — the gathering begun: scattered exiles on a distant road lifting their heads and setting out toward the far banner on the skyline; the Lord's hand at work the SECOND time, shown through the people starting home.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure or hand-from-sky; no halo or ring of light; no chains, misery or gore; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot on a worn road winding out of distant hills in warm daylight: a scattered "
            "group of exiles (worn travelling wool, not cream, bundles and staffs) lift their "
            "heads and set out along the track toward the far height where the small banner "
            "stands on the skyline — the gathering beginning again. Weary but hopeful, "
            "dignified. Their travel and gazes go toward the distant banner, not to the "
            "camera; warm daylight on the road, not around any head; nothing is written "
            "anywhere; no divine figure or hand."
        ),
    },
    {
        "id": "v2-r198-b06", "out": "s06-recover-the-remnant.jpeg", "seg": "s1",
        "window": "22.500-27.610", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING-ROADS", "GATHERED-EXILES"],
        "narration": "to recover the remnant of his people.",
        "must_show": "BLUE caption (SCRIPTURE) — a closer shot of a remnant of the people on the road, a family and a few others, drawing together as they journey toward the banner; the remnant recovered and brought back.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure or hand-from-sky; no halo or ring of light; no chains, misery or gore; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closer shot on the gathering road in warm daylight: a remnant of the people — "
            "a family with a child and a few other travellers (worn wool, not cream) — draw "
            "together as they journey, faces set with hope toward the banner ahead; a "
            "remnant being recovered. Ordinary-sized people on one road, one head each, gazes "
            "forward along the road, not to the camera; warm daylight on them, not around any "
            "head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b07", "out": "s07-ensign-for-the-nations.jpeg", "seg": "s2",
        "window": "27.610-31.000", "wide": True, "jesus": False, "ref": False,
        "locks": ["ISAIAH-HEIGHT", "GATHERED-EXILES"],
        "narration": "And he shall set up an ensign for the nations,",
        "must_show": "BLUE caption (SCRIPTURE) — the ensign for the nations: the raised banner on the height with peoples of different nations, small in the distance below, visibly turning and moving toward it from several directions.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Messiah figure; no halo or ring of light; no rendered writing on the banner; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A high wide from the height in warm daylight, camera set on the summit just "
            "behind the banner-pole looking down over the land so the pole is in the near "
            "foreground and the peoples below have their backs and travel turned away toward "
            "the banner, never toward the lens: the plain banner stands raised in the "
            "foreground, and far below, diverse peoples of several nations (varied travelling "
            "dress, none cream) are small on the roads and slopes, visibly turning and moving "
            "toward the banner from more than one direction — an ensign set up for the "
            "nations. The banner carries nothing written; warm daylight over the land, not "
            "around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b08", "out": "s08-assemble-the-outcasts.jpeg", "seg": "s2",
        "window": "31.000-34.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING-ROADS", "GATHERED-EXILES"],
        "narration": "and shall assemble the outcasts of Israel,",
        "must_show": "BLUE caption (SCRIPTURE) — the outcasts of Israel assembling: those long cast out and alone now joining together on the road, welcomed in among the others, no longer outsiders.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo or ring of light; no misery, squalor or gore; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot on the gathering road in warm daylight: a lone, weary outcast (worn wool, "
            "not cream) is met and drawn in among the other travellers, welcoming hands on "
            "his shoulders, no longer cast out — the outcasts of Israel assembled together. "
            "Ordinary-sized people, one head each, gazes meeting warmly between them, not to "
            "the camera; warm daylight on them, not around any head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b09", "out": "s09-from-the-four-corners.jpeg", "seg": "s2",
        "window": "34.200-38.860", "wide": True, "jesus": False, "ref": False,
        "locks": ["GATHERING-ROADS", "GATHERED-EXILES"],
        "narration": "and gather together the dispersed of Judah from the four corners of the earth.",
        "must_show": "BLUE caption (SCRIPTURE) — the four corners: roads coming from every direction across the wide land, streams of the dispersed converging toward the distant banner from north, south, east and west.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo or ring of light; no map, compass or rendered writing; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A high wide over the land in warm daylight, camera raised high and looking down "
            "so every road runs away into the distance and the travellers have their backs "
            "turned away toward the far banner, never toward the lens: streams of the "
            "dispersed (varied travelling dress, none cream) move along tracks converging "
            "from the far corners of the land toward the distant banner small on the skyline "
            "— gathered together from the four corners of the earth. No map or compass shown; "
            "warm daylight over the land, not around any head; nothing is written anywhere; "
            "no divine figure."
        ),
    },
    {
        "id": "v2-r198-b10", "out": "s10-brought-home.jpeg", "seg": "n2",
        "window": "38.860-43.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING-ROADS", "GATHERED-EXILES"],
        "narration": "Exiles in every direction, lifted out of every nation, brought home.",
        "must_show": "exiles from every direction brought home — a fuller road of returning people of many nations together, faces lifting with relief as the home country comes into view ahead.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo or ring of light; no misery or gore; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot along a fuller stretch of the gathering road in warm daylight: returning "
            "people of many nations (varied travelling dress, none cream) walk together, "
            "faces lifting with relief as the green home country begins to show ahead — "
            "exiles from every direction brought home. Ordinary-sized people on one road, one "
            "head each, gazes forward toward home, not to the camera; warm daylight on them, "
            "not around any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b11", "out": "s11-the-invitation.jpeg", "seg": "n2",
        "window": "43.000-47.570", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING-ROADS", "GATHERED-EXILES"],
        "narration": "The ensign is the invitation; the gathering is His work.",
        "must_show": "the invitation answered — travellers close to the height now, looking up to the raised banner above them as they climb the last road toward it; the banner calls, the people come.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo or ring of light; no rendered writing on the banner; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot on the last road up toward the height in warm daylight: travellers (worn "
            "wool, not cream) climb the final stretch, looking up to the plain banner raised "
            "above them on the summit — the ensign that called them, the gathering answered. "
            "The banner carries nothing written. Their gazes go up to the banner, not to the "
            "camera; warm daylight on them and the banner, not around any head; nothing is "
            "written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r198-b12", "out": "s12-come-home.jpeg", "seg": "n3",
        "window": "47.570-52.740", "wide": True, "jesus": False, "ref": False,
        "locks": ["HOMELAND", "GATHERED-EXILES"],
        "narration": "The banner is raised — and the seeking ones, from every people, come home.",
        "must_show": "the closing image — the gathered ones arriving in the green home valley, greeted and at rest after the long roads, the raised banner just visible on the height behind them; the seeking ones from every people come home.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo or ring of light; no rendered writing on the banner; no modern object; nothing written; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "A closing wide in the green home valley in warm daylight, camera at eye level a "
            "little behind the arriving travellers so their backs are three-quarters to the "
            "lens and their gazes go out into the welcoming valley, never to the camera: the "
            "gathered ones (varied travelling dress, none cream) of every people arrive among "
            "the terraced fields and olive groves, greeted and at rest after the long roads, "
            "the plain banner just visible small on the height behind them. Ordinary-sized "
            "people on one ground plane; warm daylight over the valley, not around any head; "
            "nothing is written anywhere; no divine figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# ISAIAH-HEIGHT, GATHERING-ROADS and HOMELAND are NEW places with no committed plate yet; the
# runner promotes ISAIAH-HEIGHT from b01, GATHERING-ROADS from b05, HOMELAND from b12 (all
# frames here are NON-Jesus). Keep the raised banner and the distant-banner-on-the-skyline
# consistent across the reused frames. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: all places and the ISAIAH/GATHERED-EXILES people are carried by the
# build-local text locks above (ISAIAH byte-identical to build-192). Jesus / the Messiah is not
# embodied in this row (every beat jesus=False); the root of Jesse is the shoot-from-stump
# metaphor and the ensign is a real banner; no one wears cream or white.
REFS = {
}
