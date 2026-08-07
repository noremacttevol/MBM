#!/usr/bin/env python3
"""V2 beat map — row 180, build-180-before-i-formed-thee (Jeremiah 1:5-8 — "Before
I formed thee in the belly I knew thee... I ordained thee a prophet unto the
nations").

COVERAGE: 19 pictures over 93.01 s (card_start) = ~4.9 s/picture (lesson 12
movie-coverage). Two establishing wides (b02 the home/village, b14 the open road);
everything else is singles and inserts that follow JEREMIAH, the frightened young
man being called, as the human spine. The two longest GOD verses (s1 10.7 s, g7
9.6 s) are each split across 2 beats so the picture reads as movement.

NO OPEN CAMERON COMPLAINT — `v2_outline.py 180` shows none. Fresh V2 picture map on
the SPEAKER-LAW narration.

AUDIO: default AUDIO LOCK stream-copy (no flag). Board Audio = OK. Picture-only
rebuild — do NOT re-voice.

SPEAKER LAW (see make_narration.py):
  s1   Jeremiah 1:5  "Before I formed thee in the belly I knew thee..."   GOD → GREEN
  s1b  Jeremiah 1:6  "Ah, Lord GOD! ... I cannot speak: for I am a child."
                     SCRIPTURE (Jeremiah answering) → LIGHT-BLUE
  g7   Jeremiah 1:7  "Say not, I am a child: for thou shalt go..."        GOD → GREEN
  s2   Jeremiah 1:8  "Be not afraid of their faces..."                    GOD → GREEN
Everything else is the NARRATOR (white). NO Jesus and NO cream (Old Testament).

**HARD GATE — GOD IS NEVER EMBODIED.** On the GOD-voice beats (b06, b07, b14, b15,
b17) the LORD speaks and calls but is NEVER shown: no figure, face, hand, mouth,
throne or beam-shaped-being, and no halo/glow/ring of light around anything (the
drift-word gate also bans those literal words — word the light as warm / radiant /
morning light in the scene, resting ON Jeremiah, never a ring around a head). The
call is carried by warm light settling over Jeremiah, by the road opening before
him, and by the NARRATION — the source stays unseen. (This is the DEFAULT gate;
row 179's deliberate embodiment was a one-off Cameron explicitly asked for and does
NOT apply here — there is no such request on this row.)

CONTENT-CARE: plain milk, no flags. A gentle, hopeful calling story — blessing,
not pressure (the narration says so). Time of day: the arc runs from a quiet
interior worry to a bright open road at morning — warm, hopeful light growing as
Jeremiah's fear turns to resolve.

PLACES:
  JEREMIAH-HOME (NEW)  the young man's home and courtyard in the priestly village
                       of Anathoth where the call comes (b01-b13).
  OPEN-ROAD     (NEW)  the road leading out of the village toward the far
                       nations — the future opening before him (b14-b19).
NEW places (runner promotes each from its first good frame, lesson 11):
  JEREMIAH-HOME  promote b02 (establishing wide of the home/village)
  OPEN-ROAD      promote b14 (establishing wide of the empty open road — a GOD beat
                 with NO figure, so it makes a clean setting plate)
Steps in QC.md. No stash plate exists for either yet.
"""

# LOCKS: all build-local. No Jesus / no cream (OT). State clothing colours
# POSITIVELY and dark; only Jesus wears cream and he is not in this row.
LOCKS = {
    "JEREMIAH-HOME": (
        "JEREMIAH-HOME LOCK: the same place in every frame — the home of a young "
        "man of a priestly family in the village of Anathoth, first-century-style "
        "ancient Judea: plain mud-brick and rough stone walls, a packed-earth "
        "floor, a low wooden bench and clay lamp indoors, a small walled courtyard "
        "with a fig or olive tree and a view out over the pale stone village and "
        "dry hills beyond. Humble, ancient, warm; no modern object, no glass, no "
        "writing rendered as art. The same house, courtyard and light throughout."
    ),
    "OPEN-ROAD": (
        "OPEN-ROAD LOCK: the same place in every frame — a dusty ancient road "
        "leading out from the village of Anathoth across open country toward the "
        "far horizon: trodden earth track, low stone walls and scattered scrub to "
        "either side, dry rolling hills and, far off, the faint shapes of distant "
        "towns and lands under a wide bright morning sky. Ancient and open; no "
        "modern object, no vehicle, no writing. The same road, hills and morning "
        "light throughout."
    ),
    "JEREMIAH": (
        "JEREMIAH LOCK: the same young man in every shot — a Hebrew youth of about "
        "twenty of the priestly family of Anathoth, warm olive-tan Middle-Eastern "
        "skin, dark brown hair and only a light young beard, earnest sensitive "
        "features, young enough to still look almost a boy. He wears a simple "
        "undyed brown-and-grey rough wool tunic and mantle (NEVER cream, never "
        "white, never fine cloth). Across the row his face turns from fear and "
        "doubt to quiet resolve — but he is the SAME young man throughout, never "
        "twinned, never a cloned face, ordinary-sized, two hands, one head. He is "
        "young and slight, never a grand or heroic figure."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r180-b01", "out": "s01-too-small-for-the-job.jpeg", "seg": "n0",
        "window": "0.400-3.322", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "A young man named Jeremiah felt far too small for the job.",
        "must_show": "a close on young Jeremiah, downcast and daunted — a slight youth sitting alone in his humble home, feeling far too small for something large being asked of him.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah, a slight young man of about twenty, sitting alone "
            "on the low bench of his humble mud-brick home, shoulders drawn in, head "
            "bowed, his young face troubled and daunted. Soft interior daylight from "
            "a small opening falls across him. He looks far too young and small for "
            "something great being laid on him. Ordinary-sized, one head, gaze down "
            "and not to the camera; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r180-b02", "out": "s02-called-to-the-nations.jpeg", "seg": "n0",
        "window": "3.322-8.392", "wide": True, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "God was calling him to speak to nations, and he was certain he could not do it.",
        "must_show": "the ONE establishing wide of the home/village — Jeremiah stands in his courtyard looking out over the village and the far hills toward the wide world he is being sent to, plainly certain he cannot do it.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "The camera stands just behind Jeremiah in his small walled courtyard, "
            "looking past his shoulder and back out over the pale stone village of "
            "Anathoth and the dry hills rolling away to a far horizon under morning "
            "light. He is turned away from us toward that wide world, a fig tree "
            "beside him, his young frame small against the great distance he is "
            "being sent into — overwhelmed and certain he cannot. Camera behind "
            "him, his back to the lens; ordinary-sized, one ground plane; nothing "
            "is written anywhere."
        ),
    },
    {
        "id": "v2-r180-b03", "out": "s03-not-the-day-he-heard-it.jpeg", "seg": "n1",
        "window": "8.392-10.865", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "But the call did not begin the day he heard it.",
        "must_show": "Jeremiah stilled and listening — a close as he lifts his head a little, the fear pausing, beginning to sense the call is older than this day.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah as he lifts his bowed head a little in the quiet of "
            "his home, his troubled face going still and listening, as though he is "
            "beginning to sense that this call did not start the moment he heard it. "
            "Soft warm interior light on his young features. Ordinary-sized, one "
            "head, gaze lifting and not to the camera; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r180-b04", "out": "s04-before-he-was-born.jpeg", "seg": "n1",
        "window": "10.865-17.063", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "Long before he was born, before he ever drew a breath, the plan was already set.",
        "must_show": "a quiet reflective beat on the reach back before his life — Jeremiah's young face in warm light, the sense that a plan for him was set long before he ever drew breath.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; nothing depicting a womb or an unborn child literally; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah, his young face turned toward a soft warm shaft of "
            "morning light in his home, calm and wondering, as the thought settles "
            "that a plan for his life was already set long before he was ever born. "
            "The light rests gently on him and gives the sense of something older "
            "and larger than himself. Ordinary-sized, one head, gaze into the light "
            "and not to the camera; nothing is written anywhere and no ring of "
            "light rings his head."
        ),
    },
    {
        "id": "v2-r180-b05", "out": "s05-chosen-and-blessed.jpeg", "seg": "n2",
        "window": "17.063-23.377", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "The God who made him had already chosen him — and blessing, not pressure, was the shape of it.",
        "must_show": "the presence settling as blessing — Jeremiah at peace as a warm light settles over him, the calling felt as blessing and not as weight; his fear easing.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah as a warm, gentle light settles over him in his "
            "home and his troubled young face begins to ease — the sense of being "
            "chosen felt as a blessing resting on him, not a weight pressing down. "
            "His shoulders loosen a little; the light is kind. Ordinary-sized, one "
            "head, his gaze softening upward and not to the camera; nothing is "
            "written anywhere and the warm light rests on him, not around him."
        ),
    },
    {
        "id": "v2-r180-b06", "out": "s06-i-knew-thee.jpeg", "seg": "s1",
        "window": "23.377-28.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "Before I formed thee in the belly I knew thee;",
        "must_show": "GOD-VOICE, GREEN caption — the being-known: Jeremiah bathed in a warm knowing light, the sense that he was known by God from before the beginning; the Maker unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; no depiction of a womb or unborn child; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah, his eyes half-closing as a warm, all-knowing light "
            "fills the room around him — the feeling of having been known, all the "
            "way back before he was ever formed. His young face is caught between "
            "awe and tears. The speaker is unseen; only the warm light and Jeremiah. "
            "Ordinary-sized, one head, gaze inward and not to the camera; nothing is "
            "written anywhere and the light fills the room, not a ring around his "
            "head."
        ),
    },
    {
        "id": "v2-r180-b07", "out": "s07-ordained-a-prophet.jpeg", "seg": "s1",
        "window": "28.500-35.929", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "and before thou camest forth out of the womb I sanctified thee, and I ordained thee a prophet unto the nations.",
        "must_show": "GOD-VOICE, GREEN caption — the setting-apart: Jeremiah slowly rising to his feet in the warm light, steadied and set apart, ordained to the nations; the door or window opening toward the wider world beyond.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, hand laying on him or beam-being; no crown, sceptre or throne; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "Jeremiah rises slowly to his feet in the warm light of his home, "
            "steadier now, his young face lifting toward the open doorway where the "
            "bright morning and the far hills of the nations show beyond — set apart "
            "and given a work far larger than his village. No hand or figure touches "
            "him; only the light and the opening view. Ordinary-sized, one head, "
            "gaze toward the doorway and not to the camera; nothing is written "
            "anywhere and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r180-b08", "out": "s08-read-it-again.jpeg", "seg": "n1r",
        "window": "35.929-37.299", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "Read that again slowly.",
        "must_show": "a held, quiet insert on Jeremiah taking the words in — utterly still, letting the promise sink deep; a beat of stillness.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A quiet, held close on Jeremiah's young face, perfectly still in the "
            "warm light of his home, eyes wide and inward as the words settle deep "
            "into him — a moment of stillness to let the promise land. Ordinary-"
            "sized, one head, gaze inward and not to the camera; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r180-b09", "out": "s09-set-you-apart.jpeg", "seg": "n1r",
        "window": "37.299-41.746", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "Before you were ever born, I set you apart, and I gave you this work.",
        "must_show": "understanding dawning — Jeremiah's face lifting with a growing wonder as he grasps that he was set apart and given this work before he was born.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah as understanding dawns across his young face — the "
            "troubled look giving way to a slow, growing wonder that he was set "
            "apart and handed this work long before he was born. Warm morning light "
            "on his features. Ordinary-sized, one head, gaze lifting and not to the "
            "camera; nothing is written anywhere and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r180-b10", "out": "s10-they-had-already-met.jpeg", "seg": "n1r",
        "window": "41.746-49.613", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "God is telling a frightened young man that they had already met — long before anybody in Jerusalem knew his name.",
        "must_show": "the intimacy of it — Jeremiah moved almost to tears in the warm light, the sense that God and he had already long known each other, unknown as he still is to the great city.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah, his young face moved almost to tears in the warm "
            "light of his home, the wonder of being already long known by God "
            "settling over him — a nobody from a small village whom the great city "
            "has never heard of, and yet known from the first. Through the doorway "
            "behind, the faint pale shapes of a distant city sit small on the "
            "horizon. Ordinary-sized, one head, gaze inward and not to the camera; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r180-b11", "out": "s11-ah-lord-god.jpeg", "seg": "s1b",
        "window": "49.613-50.472", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "Ah, Lord GOD!",
        "must_show": "SCRIPTURE-EXACT (light-blue, Jeremiah speaking) — Jeremiah's cry: a close as he lifts a hand and cries out to the Lord, overwhelmed.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah as he lifts one hand a little toward heaven and "
            "cries out, overwhelmed, his young face open and searching upward in the "
            "warm light of his home — the first word of his answer to the Lord. "
            "Ordinary-sized, one head, gaze up and not to the camera; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r180-b12", "out": "s12-i-am-a-child.jpeg", "seg": "s1b",
        "window": "50.472-54.454", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "behold, I cannot speak: for I am a child.",
        "must_show": "SCRIPTURE-EXACT (light-blue) — Jeremiah protesting his youth: he presses a hand to his chest, shaking his head, plainly feeling he is only a child and cannot speak.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah pressing a hand to his own chest, half shaking his "
            "young head, his face pleading — he feels he is only a child and cannot "
            "possibly speak for God. Warm interior light. Ordinary-sized, one head, "
            "gaze up and pleading, not to the camera; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r180-b13", "out": "s13-only-a-child.jpeg", "seg": "n3a",
        "window": "54.454-57.627", "wide": False, "jesus": False, "ref": False,
        "locks": ["JEREMIAH-HOME", "JEREMIAH"],
        "narration": "Jeremiah answered that he was only a child.",
        "must_show": "Jeremiah small and young — a beat that lets his youth show plainly, a slight boyish figure feeling wholly unequal to the task.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A slightly wider close on Jeremiah standing in his home, arms drawn in, "
            "looking very young and slight in the plain room, his eyes lowered — a "
            "boy who feels wholly unequal to what is being asked. Soft warm light. "
            "Ordinary-sized, one head, gaze low and not to the camera; nothing is "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r180-b14", "out": "s14-say-not-i-am-a-child.jpeg", "seg": "g7",
        "window": "57.627-62.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["OPEN-ROAD"],
        "narration": "Say not, I am a child: for thou shalt go to all that I shall send thee,",
        "must_show": "GOD-VOICE, GREEN caption — the ONE establishing wide of the OPEN ROAD, empty of any figure: the dusty road leading out of the village across open country toward the far nations, opening bright before him; thou shalt go to all that I send thee. The Maker unseen.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face or beam-being; no person in the frame at all here; no Jesus, no cream; no halo or ring of light; no modern object or vehicle; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "The camera looks straight down the empty dusty road as it leads out "
            "from the village across open country toward the far horizon, low stone "
            "walls and scrub to either side, dry hills rolling away and the faint "
            "shapes of distant lands under a wide bright morning sky — the way "
            "opening before the one who will be sent. No figure of any kind is in "
            "the frame; only the road, the land and the morning light. The camera "
            "sits low on the track looking away from the village straight down the "
            "empty road (no figures, so no one's back or face is toward the lens); "
            "nothing is written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r180-b15", "out": "s15-thou-shalt-speak.jpeg", "seg": "g7",
        "window": "62.500-69.149", "wide": False, "jesus": False, "ref": False,
        "locks": ["OPEN-ROAD", "JEREMIAH"],
        "narration": "and whatsoever I command thee thou shalt speak.",
        "must_show": "GOD-VOICE, GREEN caption — Jeremiah steadied to speak: he stands now at the head of the open road, straightening, his young face setting with new steadiness — ready to say whatever he is commanded.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, hand on him or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "Jeremiah stands at the head of the open road out of the village, seen "
            "from the side and a little below, straightening to his full slight "
            "height, his young face firming with a new steadiness as he faces the "
            "way ahead — ready to speak whatever he is commanded. Bright morning "
            "light across the road. No hand or figure touches him. Ordinary-sized, "
            "one head, gaze down the road and not to the camera; nothing is written "
            "anywhere and no ring of light rings his head."
        ),
    },
    {
        "id": "v2-r180-b16", "out": "s16-go-where-i-send-you.jpeg", "seg": "n3b",
        "window": "69.149-77.372", "wide": False, "jesus": False, "ref": False,
        "locks": ["OPEN-ROAD", "JEREMIAH"],
        "narration": "The LORD replied — go where I send you, speak what I command, and do not be afraid, for I am with you to deliver you.",
        "must_show": "resolve beginning — Jeremiah taking his first steps onto the open road, his fear giving way to resolve, going because he is sent and not alone.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure walking with him or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "Jeremiah takes his first steps out onto the open road from the village, "
            "seen from behind and the side, his young frame set with beginning "
            "resolve, the bright country opening ahead of him — he goes because he "
            "is sent, and not alone, though no figure walks visibly beside him. "
            "Warm morning light along the track. Ordinary-sized, one head, his back "
            "toward the lens and his face to the road; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r180-b17", "out": "s17-be-not-afraid.jpeg", "seg": "s2",
        "window": "77.372-84.968", "wide": False, "jesus": False, "ref": False,
        "locks": ["OPEN-ROAD", "JEREMIAH"],
        "narration": "Be not afraid of their faces: for I am with thee to deliver thee, saith the LORD.",
        "must_show": "GOD-VOICE, GREEN caption — Jeremiah unafraid: he pauses on the road and looks out toward the distant nations without fear, steadied by the promise that God is with him to deliver him.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no crowd of hostile faces shown; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "Jeremiah pauses on the open road and looks steadily out toward the far "
            "distant lands he is being sent to, his young face calm and unafraid "
            "now, chin level, no fear in him — held by the promise that God is with "
            "him to deliver him. Bright morning light over the wide country. No "
            "figure beside him; the distant nations are only faint shapes far off, "
            "no hostile faces near. Ordinary-sized, one head, gaze to the horizon "
            "and not to the camera; nothing is written anywhere and no ring of "
            "light rings his head."
        ),
    },
    {
        "id": "v2-r180-b18", "out": "s18-walks-with-you-now.jpeg", "seg": "n4",
        "window": "84.968-89.008", "wide": True, "jesus": False, "ref": False,
        "locks": ["OPEN-ROAD", "JEREMIAH"],
        "narration": "The same God who knew you before you were born is the one who walks with you now.",
        "must_show": "the going-forth wide — Jeremiah walking on down the open road toward the far country, small against the wide land, going with the God who knew him before he was born.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure walking beside him or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art; not a posed line facing the lens.",
        "scene": (
            "A wide from behind and above as Jeremiah walks on down the open road "
            "toward the far country, a small slight figure with his back to us, the "
            "dry hills and distant lands spread bright before him under the morning "
            "sky — going forward with the God who knew him before he was born, "
            "though no figure walks visibly at his side. Camera behind and above, "
            "his back to the lens; ordinary-sized on one ground plane; nothing is "
            "written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r180-b19", "out": "s19-the-courage-is-his-gift.jpeg", "seg": "n4",
        "window": "89.008-93.009", "wide": False, "jesus": False, "ref": False,
        "locks": ["OPEN-ROAD", "JEREMIAH"],
        "narration": "The calling is His; the courage is His gift.",
        "must_show": "the closing — a close on Jeremiah's young face on the road, resolved and at peace, the fear gone; the calling and the courage both given to him, the child who became a prophet.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no Jesus, no cream; no halo or ring of light; no modern object; no scroll or writing as art.",
        "scene": (
            "A close on Jeremiah's young face on the open road, turned a little "
            "toward the bright distance, calm and resolved, the fear wholly gone — "
            "the boy who is becoming a prophet, the calling and the courage both "
            "given to him. Warm morning light on his features. Ordinary-sized, one "
            "head, gaze to the distance and not to the camera; nothing is written "
            "anywhere and no ring of light rings his head."
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

# No image REFS: JEREMIAH is carried by a byte-identical text lock (no face sheet
# exists). NO Jesus and NO cream in this row.
REFS = {
}
