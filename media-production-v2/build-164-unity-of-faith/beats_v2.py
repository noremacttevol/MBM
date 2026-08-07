#!/usr/bin/env python3
"""V2 beat map — row 164, build-164-unity-of-faith (Ephesians 4:11-14).

COVERAGE: 25 pictures over 124.39 s = ~5.0 s/picture (matches the library
density set by rows 161-163; lesson 12 movie-coverage, every physical idea a
frame).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 164` shows no prior
review). Fresh authoring — the job is the LEARNING/COST laws in the positive:
cover every beat, keep one locked people/one locked leaders/one locked place,
and hand the runner a plate-promote plan so the two NEW recurring places do not
drift, WITHOUT spending an author credit.

SCRIPTURE FACTS (Ephesians 4 KJV, the passage this row narrates):
  4:11  "And he gave some, apostles; and some, prophets; and some,
        evangelists; and some, pastors and teachers;"              -> kv11
  4:13  "Till we all come in the unity of the faith, and of the
        knowledge of the Son of God, unto a perfect man, unto the
        measure of the stature of the fulness of Christ:"          -> kv13
  4:14  "That we henceforth be no more children, tossed to and fro,
        and carried about with every wind of doctrine, by the
        sleight of men, and cunning craftiness, whereby they lie
        in wait to deceive;"                                       -> s14

SPEAKER LAW (the row-39 lesson, confirmed by this build's make_narration.py):
Ephesians is an epistle — PAUL writing. A red-letter King James prints NO red
in Ephesians 4. So there is NO Jesus red-letter beat in this row: kv11, kv13
and s14 are ALL the SCRIPTURE voice (light blue), sitting on the people/leaders
the verse describes, never on Jesus's face. kv11's subject is Christ ("he
gave"), but Paul is the one saying it and it is ABOUT Christ, not FROM him —
so it stays SCRIPTURE (same call as build-163).

ROW INTENT: milk that leans RESTORATION, kept strictly inside the Bible's own
frame and NEVER naming any church. The risen Lord did not leave his church
without leaders; the gifts (apostles, prophets, evangelists, pastors, teachers)
were given until we ALL come to unity — and since the church plainly has not
arrived, the gifts were never meant to be temporary. The close asks the viewer
whether they will take the place offered them and grow up in it.

HOW JESUS IS DEPICTED (lesson 8 + the Standing Laws): Jesus appears ONLY as the
locked V2 risen Lord (LOCK v5 + REF), and only in the giving of the gifts
(b01-b03) and the closing invitation (b25). Only he wears cream; ordinary-sized
man, never a giant (SCALE GATE, lesson 14); NO halo/glow/rim-light and no light
around his head — where heaven is meant ("from above", "returned to heaven")
it is warm light at the frame's top edge, never a figure or face in the sky.

GOD / THE SON-AS-GOAL IS NEVER EMBODIED FOR MEASURE: at "the knowledge of the
Son of God" (b11/b13) and "the stature of the fulness of Christ" (b14), Christ
is the DISTANT GOAL — warm dawn light on the far high town, a full-grown
believer standing to his stature — never a second giant Christ figure set up
for comparison (that would trip the SCALE GATE and invent a symbol).

MOVIE COVERAGE (lesson 12): the establishing wide is b01 and ONLY b01;
everything else is a single, a two-shot, or an insert. The "church" is always a
SMALL band of distinct real faces, never the whole congregation crowded in.
An abstract epistle still gets concrete coverage: every physical image Paul
uses — poured-out gifts, a hand on a shepherd, a body knit together, a road
with a destination, a child tossed in the wind, deceivers lying in wait, a
scroll under a lamp — gets its own frame.

TWO NEW RECURRING PLACES (the runner promotes, per lesson 11 — do NOT promote a
Jesus-bearing frame): GATHERING-HILL (b01 is Jesus, so promote the NON-Jesus
b13 as its plate, then wire b24; b01/b25 carry their own Jesus lock over the
same place text) and JOURNEY-ROAD (promote b10, wire b21). Steps in QC.md.

TIME OF DAY ARC (intentional): the giving of the gifts and the gathered church
in warm clear dawn; the "tossed to and fro / winds of doctrine" beats (b15-b19)
under a hard grey driving wind; the close returning to still, settled dawn as
the viewer is drawn in.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. The shared JESUS lock + REF come from v2_prompt.py via
# the jesus/ref flags — never written here.
LOCKS = {
    "GATHERING-HILL": (
        "GATHERING-HILL LOCK: the same place in every frame — a broad grassy "
        "hillside above a modest first-century town, low dry-stone terrace "
        "walls, a few gnarled olive trees, the town's pale flat rooftops "
        "stepping down below, distant dun hills beyond; soft clear dawn light. "
        "The same hill, terraces and town throughout — never a temple, never a "
        "palace, never a walled shrine, never any modern structure."
    ),
    "JOURNEY-ROAD": (
        "JOURNEY-ROAD LOCK: the same place in every frame — a worn dirt road "
        "climbing between low dry hills toward a distant first-century town set "
        "on a high place, its pale walls and rooftops catching warm dawn light; "
        "olive trees, dry grass and loose stones along the verges. The same "
        "road and the same far town throughout — never a paved or modern road, "
        "never a signpost, never a modern building."
    ),
    "BELIEVERS": (
        "BELIEVERS LOCK: the ordinary church people — a small band of first-"
        "century men and women of varied ages, distinct real sun-browned "
        "faces, dark hair and beards of differing lengths, plain earth-toned "
        "wool of brown, rust, ochre, olive and grey (never cream — only Jesus "
        "wears cream); ordinary, real people, never twinned, never a cloned "
        "face, never a uniform crowd."
    ),
    "MINISTERS": (
        "MINISTERS LOCK: the leaders the risen Lord gave — apostles, prophets, "
        "evangelists, pastors and teachers: dignified, distinct first-century "
        "men of varied ages, some elder and grey-bearded, some steady and "
        "middle-aged, several carrying a shepherd's staff or an open scroll; "
        "plain earth-toned robes of brown, umber, olive and undyed grey (never "
        "cream — only Jesus wears cream); real distinct individuals, NOT posed "
        "as a named roster, never twinned, never a cloned face."
    ),
    "DECEIVERS": (
        "DECEIVERS LOCK: the clever men who lie in wait — smooth, watchful "
        "persuaders in richer, finer robes of dark wine-red, deep grey and "
        "umber (never cream), well-groomed, plausible and self-assured, their "
        "eyes always calculating; distinct real men, clearly finer-dressed and "
        "smoother than the plain true leaders, never cartoonish, never "
        "monstrous, never twinned."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r164-b01", "out": "s01-not-left-leaderless.jpeg", "seg": "n1",
        "window": "0.280-5.510", "wide": True, "jesus": True, "ref": True,
        "locks": ["GATHERING-HILL", "BELIEVERS"],
        "narration": (
            "When the risen Lord returned to heaven, he did not leave his "
            "church leaderless and on its own."
        ),
        "must_show": "the ONE establishing wide — camera on the hillside a few steps behind the small band of believers, looking past their shoulders and backs to the risen Jesus standing before them in warm dawn light; a real gathering place, his people gathered and not abandoned.",
        "must_not_show": "not the whole church crowded in — a SMALL band; no light around Jesus's head, no halo or glow; Jesus ordinary-sized, never a giant; no faces posed to the lens; no panel, border or text.",
        "scene": (
            "A leave-taking that is not an abandonment: the camera stands on the "
            "grassy hillside a few steps behind a small band of believers, "
            "looking past their shoulders and backs to where the risen Jesus "
            "stands facing them in the warm early light, the town's pale "
            "rooftops below. Their gazes travel away from the lens toward him. "
            "He is about to return to his Father, yet the moment reads as "
            "provision, not desertion — he leaves them cared for. Every figure "
            "has two arms, two hands and one head; all are of ordinary human "
            "height, the light warm and plain with nothing ringing his head."
        ),
    },
    {
        "id": "v2-r164-b02", "out": "s02-gifts-from-above.jpeg", "seg": "n1",
        "window": "5.510-9.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["GATHERING-HILL", "BELIEVERS"],
        "narration": "From above, he poured out gifts on his people —",
        "must_show": "Jesus with both hands lifted in blessing over the small band, warm light spilling down from above the top of the frame onto the people — gifts poured out from above as he goes.",
        "must_not_show": "no figure or face in the sky (heaven never embodied); no halo, glow or light around Jesus's own head; ordinary-sized; only he wears cream; no panel or text.",
        "scene": (
            "The giving drawn as an open-handed blessing: Jesus lifts both hands "
            "over the small band of his people, and warm light comes down onto "
            "them from above the top of the frame, as though the gifts of "
            "heaven were being poured out through him onto the upturned faces "
            "below. The light stays at the frame's upper edge and never becomes "
            "a figure, a face or a shape in the sky. He is an ordinary-sized "
            "man; the believers are distinct earth-toned people, each with two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r164-b03", "out": "s03-living-leaders-given.jpeg", "seg": "n1",
        "window": "9.500-13.469", "wide": False, "jesus": True, "ref": True,
        "locks": ["MINISTERS"],
        "narration": (
            "and the greatest of those gifts were living leaders, given to "
            "shepherd and to teach."
        ),
        "must_show": "a two-shot — Jesus laying one hand on the shoulder of a weathered minister who holds a shepherd's staff and an open scroll, commissioning him; the gift shown as a real living man given to shepherd and teach.",
        "must_not_show": "not a crowd; the minister NOT in cream (only Jesus); no halo or light around Jesus's head; both ordinary-sized, neither enlarged.",
        "scene": (
            "The gift is a person, not a thing: a two-shot at the hill's edge in "
            "warm light, Jesus laying one hand on the shoulder of a weathered, "
            "grey-flecked minister who carries a shepherd's staff in one hand "
            "and an open scroll in the other — commissioned to shepherd and to "
            "teach. The minister's face is set and glad, turned to Jesus. Jesus "
            "is an ordinary-sized man; the minister wears plain earth-toned "
            "wool. Both have two hands and one head, and nothing lights Jesus's "
            "head."
        ),
    },
    {
        "id": "v2-r164-b04", "out": "s04-apostles-and-prophets.jpeg", "seg": "kv11",
        "window": "13.469-17.700", "wide": False, "jesus": False, "ref": False,
        "locks": ["MINISTERS"],
        "narration": "And he gave some, apostles; and some, prophets;",
        "must_show": "SCRIPTURE-EXACT — a tight shot of two distinct ministers standing as the offices named: a resolute middle-aged apostle with a traveller's staff, and beside him an elder grey-bearded prophet with an open scroll; real, distinct faces.",
        "must_not_show": "NOT the whole Twelve or a named roster line-up; NOT posed staring at the lens; no cream; distinct faces, never twinned; no panel or text.",
        "scene": (
            "The first offices as two real men: a resolute middle-aged apostle, "
            "a traveller's staff in his hand and the dust of sent journeys on "
            "him, stands beside an older grey-bearded prophet holding an open "
            "scroll, the prophet's eyes lifted in thought. They are turned "
            "toward one another and the work, not to the camera. Two clearly "
            "different men in plain earth-toned robes, each with two hands and "
            "one head, in clear morning light."
        ),
    },
    {
        "id": "v2-r164-b05", "out": "s05-evangelists-pastors-teachers.jpeg", "seg": "kv11",
        "window": "17.700-21.906", "wide": False, "jesus": False, "ref": False,
        "locks": ["MINISTERS", "BELIEVERS"],
        "narration": "and some, evangelists; and some, pastors and teachers;",
        "must_show": "SCRIPTURE-EXACT — an earnest evangelist telling the good news to a listening stranger, and just behind, a pastor-teacher with an open scroll instructing a seated believer; the remaining offices as real working men.",
        "must_not_show": "not a crowd; distinct faces, never twinned; no cream; no modern objects; no legible modern text on the scroll; no panel or border.",
        "scene": (
            "The other offices caught mid-work: in front, an earnest evangelist "
            "leans a little toward a road-worn stranger, telling him something "
            "that has stopped the man where he stands; just behind, a "
            "pastor-teacher sits with an open scroll across his knees, one hand "
            "guiding a seated believer's eye down the lines. Distinct "
            "sun-browned faces, plain earth-toned wool, warm morning light. "
            "Every figure has two hands and one head; the scroll bears only "
            "plain ancient marks, nothing legible or modern."
        ),
    },
    {
        "id": "v2-r164-b06", "out": "s06-mend-and-mature.jpeg", "seg": "n2",
        "window": "21.906-27.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["MINISTERS", "BELIEVERS"],
        "narration": (
            "He gave them for a reason. Their whole calling was to mend and "
            "mature the ordinary believers —"
        ),
        "must_show": "a close two-shot — a patient minister mending and maturing an ordinary believer: steadying the younger man with one hand and guiding his hand over an open scroll; care between two people, not a crowd.",
        "must_not_show": "no crowd; the believer NOT in cream; distinct faces; no modern objects; whole hands; no panel or text.",
        "scene": (
            "The purpose of the gift shown as patient care: a close two-shot of "
            "a steady older minister and a younger believer, the minister's one "
            "hand resting on the younger man's shoulder and his other guiding "
            "the believer's hand along the lines of an open scroll — mending "
            "what is unsettled, maturing what is young. Both are ordinary men in "
            "earth-toned wool, distinct faces in warm light, each with two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r164-b07", "out": "s07-body-built-up.jpeg", "seg": "n2",
        "window": "27.200-32.741", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "to do the work of the ministry, and to build up the body until it "
            "stood strong and whole."
        ),
        "must_show": "a small group of ordinary believers standing strong and whole together, shoulder to shoulder and steady at work in ministry — the body built up, complete and unshaken.",
        "must_not_show": "not a large crowd — a small band; distinct faces, never twinned; no cream; nobody a giant; no panel, border or text.",
        "scene": (
            "The result made visible: a small band of believers stands together "
            "shoulder to shoulder on the hill, sturdy and settled, a couple of "
            "them carrying the plain tools of service — grown from scattered "
            "individuals into one strong and whole body. Their weathered faces "
            "are distinct and calm, their wool earth-toned, the morning light "
            "even across them. Every figure is of ordinary height, with two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r164-b08", "out": "s08-never-a-scattered-crowd.jpeg", "seg": "n3",
        "window": "32.741-35.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "So the people were never meant to be a scattered crowd.",
        "must_show": "the 'scattered' contrast — a few lone believers spread far apart across a bare slope, turned away from one another, each isolated; the wrong, unwanted state Paul names.",
        "must_not_show": "NOT a knit or gathered group (that is the next beat); no crowd; distinct isolated figures; no cream; no panel or text.",
        "scene": (
            "The wrong state, drawn plainly: three or four lone believers stand "
            "far apart across a bare, dry slope, each turned away from the "
            "others, no one near enough to touch — scattered, separate, going "
            "nowhere together. The distances between them are wide and the "
            "light is flat and cool. Each is a distinct figure of ordinary "
            "height in earth-toned wool, with two hands and one head."
        ),
    },
    {
        "id": "v2-r164-b09", "out": "s09-knit-together.jpeg", "seg": "n3",
        "window": "35.800-42.703", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS", "GATHERING-HILL"],
        "narration": (
            "Taught and strengthened, they were knit together, growing closer, "
            "becoming one body that could bear one another up."
        ),
        "must_show": "the turn — the same believers now knit close together, one of them steadying and lifting a weary companion under the arm — growing into one body that bears one another up.",
        "must_not_show": "no crowd; distinct faces, never twinned; no cream; nobody a giant; natural contact and whole hands; no panel or text.",
        "scene": (
            "The opposite of the scattered slope: the believers are drawn in "
            "close together on the hillside now, shoulders nearly touching, and "
            "one of them has slipped an arm under a weary companion and is "
            "lifting him steady on his feet — knit together, growing closer, one "
            "body bearing one another up. Distinct earth-toned people, warm "
            "morning light, hands whole and natural, every figure of ordinary "
            "height with one head."
        ),
    },
    {
        "id": "v2-r164-b10", "out": "s10-destination-in-view.jpeg", "seg": "n4",
        "window": "42.703-47.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOURNEY-ROAD", "BELIEVERS"],
        "narration": (
            "And there was a destination in view. All of them were being drawn "
            "toward the same place —"
        ),
        "must_show": "the road — the small band walking together along the dirt road, backs to the camera, toward the distant town on its high place lit with dawn; a shared destination plainly in view, all moving the same way.",
        "must_not_show": "no crowd; travel clearly AWAY from the lens toward the far town; distinct backs; no cream; no paved or modern road, no modern buildings; no panel.",
        "scene": (
            "A people with somewhere to go: the small band walks together up the "
            "worn dirt road with their backs to the camera, and far ahead the "
            "pale town on its high place catches the dawn — the destination in "
            "plain view, every one of them drawn the same direction toward the "
            "same place. Dust rises softly at their heels; the light ahead is "
            "warm. The figures are of ordinary height in earth-toned wool, each "
            "with two hands and one head."
        ),
    },
    {
        "id": "v2-r164-b11", "out": "s11-one-shared-faith.jpeg", "seg": "n4",
        "window": "47.500-51.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "one shared faith, one true knowledge of the Son of God,",
        "must_show": "a close on a few believers' faces lifted the same direction toward the far warm light — one shared faith, one knowledge drawing them together as one.",
        "must_not_show": "the Son of God NOT embodied here — he is the distant goal, warm light at the far frame edge, no figure and no light around any head; no crowd; no cream; no panel.",
        "scene": (
            "One hope on several faces: a close grouping of a few believers, "
            "cheeks and eyes lifted the same way toward the warm light on the "
            "far high town, their expressions settled into a single shared "
            "confidence — one faith, one knowledge of the Son of God holding "
            "them together. The light they look toward stays distant at the "
            "frame's edge and never becomes a figure. Distinct earth-toned "
            "faces, ordinary height, one head each."
        ),
    },
    {
        "id": "v2-r164-b12", "out": "s12-full-maturity.jpeg", "seg": "n4",
        "window": "51.800-56.020", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "a people grown at last into full and finished maturity.",
        "must_show": "a single ordinary believer grown to full maturity — standing to full height in clear dawn light, settled and strong, a person come of age in the faith.",
        "must_not_show": "no crowd; nobody a giant; no cream; no halo or light around the head; no panel or text.",
        "scene": (
            "Maturity on one steady figure: a single believer stands to his full "
            "height in the clear dawn, weight even, shoulders settled, a "
            "weathered face grown calm and sure — a person brought up at last "
            "into full and finished maturity. Plain earth-toned wool, warm even "
            "light, an ordinary-sized man with two hands and one head, nothing "
            "ringing his head."
        ),
    },
    {
        "id": "v2-r164-b13", "out": "s13-unity-of-the-faith.jpeg", "seg": "kv13",
        "window": "56.020-61.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING-HILL", "BELIEVERS"],
        "narration": (
            "Till we all come in the unity of the faith, and of the knowledge "
            "of the Son of God,"
        ),
        "must_show": "SCRIPTURE-EXACT — the small band of believers gathered together as one on the hillside, close and unified, faces turned inward to one another and upward toward the far light — come into the unity of the faith.",
        "must_not_show": "not a large crowd — a small close band; distinct faces, never twinned; the Son of God NOT embodied (warm dawn light only, at the frame edge); no cream; no light around any head.",
        "scene": (
            "Unity held in one frame: the small band of believers is gathered "
            "together on the hillside, drawn in close, some faces turned to one "
            "another and some lifted the same way toward the warm dawn light on "
            "the far town — come into the unity of the faith and the knowledge "
            "of the Son of God, one people at last. The light stays distant and "
            "becomes no figure. Distinct earth-toned faces of ordinary height, "
            "each with two hands and one head."
        ),
    },
    {
        "id": "v2-r164-b14", "out": "s14-full-stature.jpeg", "seg": "kv13",
        "window": "61.500-67.006", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "unto a perfect man, unto the measure of the stature of the "
            "fulness of Christ:"
        ),
        "must_show": "SCRIPTURE-EXACT — a believer standing to his full stature in dawn light, grown up complete and finished — a perfect, whole man brought up to the full measure Paul names.",
        "must_not_show": "Christ NOT embodied for comparison — no second, giant Christ figure and no figure in the sky; nobody a giant; no cream; no halo or light around the head; no panel.",
        "scene": (
            "The measure shown as one finished man: a believer stands to his "
            "full height in the strengthening dawn, complete and whole, his "
            "bearing grown up into everything he was meant to become — a perfect "
            "man brought to the full measure of stature. There is no second "
            "towering figure beside him for scale; the fullness is read in the "
            "man himself. Plain earth-toned wool, warm light, ordinary height, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r164-b15", "out": "s15-tossed-to-and-fro.jpeg", "seg": "s14",
        "window": "67.006-73.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "That we henceforth be no more children, tossed to and fro, and "
            "carried about with every wind of doctrine,"
        ),
        "must_show": "SCRIPTURE-EXACT — a young believer caught off balance in a hard driving wind, cloak and hair whipping sideways, dry leaves and dust streaming past, staggering a step — tossed to and fro, carried about by every wind.",
        "must_not_show": "no calm and no fantasy — a real hard windstorm on real ground; no invented symbols; distinct face; no cream; no panel or text.",
        "scene": (
            "The warning made physical: a young believer is caught off balance "
            "in a hard, driving wind on the bare slope, his cloak and hair torn "
            "sideways, one foot staggering to keep him up, dry leaves and grit "
            "streaming past him — pushed and dragged this way and that, carried "
            "about by every gust. The sky above has gone flat and grey. He is a "
            "distinct young man of ordinary height in earth-toned wool, with two "
            "hands and one head, in real storm-wind, nothing invented."
        ),
    },
    {
        "id": "v2-r164-b16", "out": "s16-lie-in-wait-to-deceive.jpeg", "seg": "s14",
        "window": "73.500-79.869", "wide": False, "jesus": False, "ref": False,
        "locks": ["DECEIVERS", "BELIEVERS"],
        "narration": (
            "by the sleight of men, and cunning craftiness, whereby they lie "
            "in wait to deceive;"
        ),
        "must_show": "SCRIPTURE-EXACT — a pair of smooth, watchful deceivers waiting in shadow at the frame's edge, eyes fixed on the staggering believer, one beginning to reach out a persuasive open hand — cunning men lying in wait to deceive.",
        "must_not_show": "the deceivers clearly finer-dressed and smoother than the true ministers, NOT in cream; no cartoon villainy, no horns, no invented marks; distinct faces; no panel.",
        "scene": (
            "The trap behind the wind: two smooth, well-groomed men wait in the "
            "grey shadow at the edge of the frame, finer-dressed than any plain "
            "shepherd, their calculating eyes fixed on the staggering young "
            "believer, one of them just beginning to extend a persuasive open "
            "hand toward him — patient, plausible, lying in wait to deceive. "
            "They are distinct real men in richer dark robes, ordinary height, "
            "two hands and one head each; no monster, nothing invented."
        ),
    },
    {
        "id": "v2-r164-b17", "out": "s17-without-steady-leading.jpeg", "seg": "n5",
        "window": "79.869-84.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": "Paul set the opposite right beside it. Without that steady leading,",
        "must_show": "the cause — a small group of believers with NO minister among them, an empty leaderless gap in their midst, faces uncertain and glancing about — what happens when the steady leading is absent.",
        "must_not_show": "NO minister present in this frame (the point is his absence); no crowd; distinct uncertain faces; no cream; no panel or text.",
        "scene": (
            "The picture of a lack: a small group of believers stands on the "
            "wind-scoured slope with a plain empty space open in the middle of "
            "them where a leader should be — no minister anywhere among them — "
            "and their faces glance about uncertain, no one sure which way to "
            "turn. The gap in their midst is the subject. Distinct earth-toned "
            "people of ordinary height, two hands and one head each, in cool "
            "unsettled light."
        ),
    },
    {
        "id": "v2-r164-b18", "out": "s18-carried-off-by-every-wind.jpeg", "seg": "n5",
        "window": "84.500-89.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "believers stay children — pushed back and forth, carried off by "
            "every new wind of teaching,"
        ),
        "must_show": "several believers pulled in DIFFERENT directions in the same driving wind — some leaning and drifting one way, others the other, no two going the same way — pushed back and forth, carried off by every new wind.",
        "must_not_show": "not one figure — a few, pulled apart; real wind on real ground; no invented symbols; distinct faces; no cream; no panel.",
        "scene": (
            "Drift shown as disagreement of motion: several believers are "
            "scattered across the slope in the same hard wind, but each is "
            "leaning and stumbling a different way — one dragged left, one "
            "pulled right, one bent back — no two carried the same direction, "
            "all of them pushed back and forth by competing gusts. Cloaks snap "
            "in different directions. Distinct earth-toned figures of ordinary "
            "height, two hands and one head each, real wind, nothing invented."
        ),
    },
    {
        "id": "v2-r164-b19", "out": "s19-easy-prey.jpeg", "seg": "n5",
        "window": "89.200-93.927", "wide": False, "jesus": False, "ref": False,
        "locks": ["DECEIVERS", "BELIEVERS"],
        "narration": "easy prey for clever men who lie in wait to fool them.",
        "must_show": "a clever deceiver up close working on a lone, unsteady believer — leaning in with a persuasive smile, one guiding hand on the shoulder turning the young man off his way; the believer half-turning, taken in.",
        "must_not_show": "the deceiver distinct, finer and smoother than the true ministers, NOT in cream; no cartoon menace; distinct faces; whole hands; no panel or text.",
        "scene": (
            "The prey taken: a smooth, finely-robed deceiver has come in close on "
            "a lone unsteady believer, leaning to his ear with a warm "
            "persuasive smile, one guiding hand on the young man's shoulder "
            "turning him gently off his own way — and the believer is "
            "half-turned toward him, already half-taken in. Two distinct real "
            "men of ordinary height, the deceiver's robe richer and darker, both "
            "with whole hands and one head, in cool light."
        ),
    },
    {
        "id": "v2-r164-b20", "out": "s20-the-study-gem.jpeg", "seg": "n6",
        "window": "93.927-98.500", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Here is the quiet study gem.",
        "must_show": "a quiet study insert — an open first-century scroll of Paul's letter lit by a small clay oil lamp, a reader's hand resting on the lines, the room still — a gem found in careful reading.",
        "must_not_show": "no modern book, paper or print; NO legible modern letters or numbers on the scroll; warm lamp light with no halo or glow around anything; no panel, border or text overlay.",
        "scene": (
            "The turn to close reading: an insert looking down at an open "
            "first-century papyrus scroll spread on a plain wooden table, a "
            "small clay oil lamp beside it throwing warm low light across the "
            "lines, and a reader's weathered hand resting quietly on the words "
            "as if pausing on something just found. The room is still and dim "
            "around the lamp. The scroll bears only plain ancient ink strokes, "
            "nothing legible or modern; the hand is whole with five fingers."
        ),
    },
    {
        "id": "v2-r164-b21", "out": "s21-not-arrived-yet.jpeg", "seg": "n6",
        "window": "98.500-104.430", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOURNEY-ROAD", "BELIEVERS"],
        "narration": (
            "If those leaders were given until we ALL arrive at that unity, and "
            "the church has plainly not arrived yet, then the gifts were never "
            "meant to be temporary."
        ),
        "must_show": "the same road again — the believers still walking, backs to the lens, the far town on its high place still well ahead and clearly NOT yet reached; the journey to unity plainly unfinished, so the leading is still needed.",
        "must_not_show": "NOT arrived — the town unmistakably still distant ahead, not entered; no crowd; travel away from the lens; no cream; no modern road or building; no panel.",
        "scene": (
            "The argument carried by distance: the small band is still on the "
            "worn road with their backs to the camera, and the pale town on its "
            "high place still stands well ahead of them, not yet reached — the "
            "road plainly unfinished, the people still short of the unity they "
            "are walking toward. Because the arriving is not done, the leading "
            "that carries them is not done either. Ordinary-height figures in "
            "earth-toned wool, two hands and one head each, warm light ahead."
        ),
    },
    {
        "id": "v2-r164-b22", "out": "s22-kept-from-drifting.jpeg", "seg": "n6",
        "window": "104.430-109.080", "wide": False, "jesus": False, "ref": False,
        "locks": ["MINISTERS", "BELIEVERS"],
        "narration": (
            "His people still need apostles and prophets to keep them from "
            "drifting."
        ),
        "must_show": "a minister catching a drifting believer — a steady hand and staff turning a wanderer back toward the road and the others, keeping him from drifting off; the leading still doing its work now.",
        "must_not_show": "the minister distinct and NOT in cream; no crowd; whole hands; distinct faces; nobody a giant; no panel or text.",
        "scene": (
            "The leading still at work: a weathered minister with a shepherd's "
            "staff has reached out and laid a steady hand on a believer who was "
            "wandering off the road, turning him gently back toward the others "
            "walking ahead — keeping him from drifting away. The minister's face "
            "is patient, the believer's caught between straying and returning. "
            "Both are ordinary men in earth-toned wool, distinct faces, two "
            "hands and one head each, in warm morning light."
        ),
    },
    {
        "id": "v2-r164-b23", "out": "s23-never-alone.jpeg", "seg": "n7",
        "window": "109.080-113.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS", "GATHERING-HILL"],
        "narration": (
            "And that is where it leaves you. You were never meant to grow up "
            "alone,"
        ),
        "must_show": "a single ordinary believer — the viewer's stand-in — standing a little apart at the edge of the gathered others on the hill, alone and thoughtful, considering the invitation.",
        "must_not_show": "no crowd; the one figure clearly set slightly apart from the band; distinct face; no cream; no halo or light around the head; no panel.",
        "scene": (
            "The story turns to the one watching: a single believer stands a few "
            "steps apart at the edge of the gathered band on the hillside, "
            "half-facing them, alone and thoughtful — the viewer's own place in "
            "the story, someone who has been growing up alone and is weighing "
            "whether to come in. The others are near but he stands just outside "
            "them. An ordinary man in earth-toned wool, distinct face, two hands "
            "and one head, calm dawn light."
        ),
    },
    {
        "id": "v2-r164-b24", "out": "s24-grow-up-together.jpeg", "seg": "n7",
        "window": "113.500-119.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING-HILL", "BELIEVERS"],
        "narration": (
            "or to be blown about by whatever is newest. You are meant to grow "
            "up in this, together, into one settled faith."
        ),
        "must_show": "the once-apart believer drawn IN — welcomed shoulder to shoulder into the gathered band on the hill, hands on his shoulders bringing him among them, all settled and unified together in calm light — growing up together into one settled faith.",
        "must_not_show": "not a large crowd — a small close band; distinct faces, never twinned; no cream; nobody a giant; the wind gone, the light calm and still; no panel or text.",
        "scene": (
            "The invitation begun: the believer who stood apart is being drawn "
            "into the gathered band on the hillside now, a couple of welcoming "
            "hands on his shoulders bringing him in among them shoulder to "
            "shoulder, faces turning to receive him — the storm-wind gone, the "
            "light calm and warm, the whole small band settled and grown up "
            "together into one faith. Distinct earth-toned people of ordinary "
            "height, whole hands, one head each."
        ),
    },
    {
        "id": "v2-r164-b25", "out": "s25-will-you-come-and-grow.jpeg", "seg": "n7",
        "window": "119.000-124.389", "wide": False, "jesus": True, "ref": True,
        "locks": ["GATHERING-HILL", "BELIEVERS"],
        "narration": (
            "When he offers you a place in it, will you come and grow?"
        ),
        "must_show": "the risen Jesus at the gathered band's side, turning toward the viewer and holding out one open hand in welcome, a place plainly opened among the people for the one watching — the invitation to come and grow, left hopeful and open.",
        "must_not_show": "no halo, glow or light around Jesus's head; ordinary-sized, never a giant; only he wears cream; an OPEN offered hand, never grasping; no panel, border or text.",
        "scene": (
            "The film hands the invitation across: the risen Jesus stands at the "
            "side of the gathered band on the hill, turned toward the camera, "
            "one hand held open and out in welcome toward the viewer, and beside "
            "him the believers have opened a real place in their midst — a gap "
            "made ready for the one watching to step into. His face is warm and "
            "hopeful in the calm dawn, an ordinary-sized man, nothing ringing "
            "his head; the offered hand is open, not grasping, five fingers "
            "whole."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
#
# EMPTY BY DESIGN. GATHERING-HILL and JOURNEY-ROAD are NEW recurring places with
# no stash match, so there is no plate to wire at author time. The runner
# promotes them from this build's first good NON-Jesus frame (never a Jesus
# frame — lesson 11): promote b13 for GATHERING-HILL then wire b09/b23/b24
# (b01/b25 carry their own Jesus lock over the same place); promote b10 for
# JOURNEY-ROAD then wire b21. Full steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
