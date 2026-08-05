#!/usr/bin/env python3
"""V2 beat map — row 105, build-105-face-to-face (Exodus 33:7-23; 34:29).

COVERAGE: 26 pictures over 148.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Exodus 33 KJV):
  v7    "Moses took the tabernacle, and pitched it WITHOUT THE CAMP,
        afar off... and called it the TABERNACLE OF THE CONGREGATION
        (Tent of Meeting)."
  v8    "all the people ROSE UP, and STOOD EVERY MAN AT HIS TENT
        DOOR, and looked after Moses" — the whole camp on its feet
        watching him walk out.
  v9    "the CLOUDY PILLAR DESCENDED, and STOOD AT THE DOOR of the
        tabernacle."
  v11   "the LORD spake unto Moses FACE TO FACE, as a man speaketh
        unto his FRIEND."
  v14   "MY PRESENCE SHALL GO WITH THEE, and I will give thee REST."
  v18   Moses's ask: "I beseech thee, SHEW ME THY GLORY."
  v19   the answer: "I will make all my GOODNESS pass before thee."
  v20   "THOU CANST NOT SEE MY FACE: for there shall no man see me,
        and live." — care, not refusal.
  v21-23 "a place BY ME... a CLIFT OF THE ROCK... I will COVER THEE
        WITH MY HAND while I pass by."
  34:29 descending, "the SKIN OF HIS FACE SHONE; and he WIST NOT."

GOD RENDERING (CONTENT-CARE law, strictest row yet): the LORD is
NEVER embodied — no figure, face, shape, silhouette OR literal hand
anywhere. The pillar of cloud is cloud; the face-to-face intimacy is
carried by Moses's posture and the near presence of light within the
tent; the v22 covering hand is rendered as a deep sheltering SHADOW
folding over the cleft while brilliance passes — never an actual
hand. Never the word glow (the b25 narration's wording stays in the
audio only; scenes use shine/bright).

TIME OF DAY ARC (intentional): camp beats in clear morning; the tent
meetings in soft day with the cloud's own shadow; the cleft sequence
in overwhelming passing brilliance against mountain rock; the shining
descent in ordinary afternoon light. Not the row-11 defect.

CHANGING CONDITION (kept OUT of the locks): the cloud pillar —
absent, descending, standing, passing; Moses's face — ordinary, then
shining; the camp — working, then standing at every tent door.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream (not in this row).
LOCKS = {
    "MOSES": (
        "MOSES LOCK: Moses is the same man in every shot — about "
        "eighty and still powerful, a long grey-white beard, deep-"
        "lined weathered face, in a DARK MADDER-RED robe over a "
        "CHARCOAL tunic with a rough staff (never cream, never "
        "white); the bearing of a man at ease with holy ground."
    ),
    "CAMP": (
        "CAMP LOCK: the Israelite camp — a great spread of dark "
        "goat-hair tents in ordered rows on a dusty plain, cook "
        "fires and tethered flocks, mountains ringing the horizon. "
        "The same tent rows and skyline throughout."
    ),
    "TENT": (
        "TENT LOCK: the Tent of Meeting — one dark goat-hair tent "
        "pitched ALONE on open ground well outside the camp's edge, "
        "plain and weathered, its door flap facing back toward the "
        "distant tent rows. The same lone tent throughout."
    ),
    "CLEFT": (
        "CLEFT LOCK: the mountain cleft — a man-sized vertical "
        "split in a sheer granite face high on the mountain, deep "
        "enough to stand in, raw rock all around. The same split "
        "and face throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r105-b01", "out": "s01-moses-pitched-a-tent-a.jpeg", "seg": "n1",
        "window": "0.28-5.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "CAMP", "TENT"],
        "narration": (
            "Moses pitched a tent a little way outside the camp and called "
            "it the Tent of Meeting."
        ),
        "must_show": "SCRIPTURE-EXACT: the tent without the camp — Moses staking the lone dark tent on open ground, the great camp's rows visible behind at a distance; apartness deliberate.",
        "must_not_show": "no figure of God, no halo; the DISTANCE readable — one tent, alone, a walk away from everyone.",
        "scene": (
            "On open ground a good walk "
            "from everyone, Moses drives "
            "the last stake: one plain "
            "dark goat-hair tent standing "
            "alone on the dusty plain, "
            "its guy-lines humming in the "
            "wind — and behind it, far "
            "enough to be a journey, "
            "the whole great camp in its "
            "ordered rows, smoke rising "
            "from a thousand fires — a "
            "meeting place pitched "
            "deliberately apart, quiet "
            "bought with distance. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b02", "out": "s02-it-was-the-place-he.jpeg", "seg": "n1",
        "window": "5.81-11.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "It was the place he went to be with God — set apart, quiet, "
            "away from everything else."
        ),
        "must_show": "the set-apartness — Moses at the lone tent's door in the plain's silence, hand on the flap; a threshold kept for one purpose.",
        "must_not_show": "no figure of God, no halo; the QUIET the subject — wind, space, one man, one door.",
        "scene": (
            "The tent keeps its one "
            "purpose in the silence: "
            "Moses standing at the door "
            "flap with his staff grounded "
            "and his weathered hand on "
            "the rough cloth, the plain's "
            "wind moving past, the camp's "
            "noise a distant murmur "
            "behind him — a threshold "
            "used for nothing else in "
            "the world, pausing at it "
            "the way a man pauses at "
            "the door of the friend "
            "who matters most. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b03", "out": "s03-whenever-moses-walked-out-to.jpeg", "seg": "n2",
        "window": "11.97-17.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "CAMP", "TENT"],
        "narration": (
            "Whenever Moses walked out to that tent, something happened "
            "that had never happened for anyone."
        ),
        "must_show": "the walk out — Moses crossing the open ground from camp toward the lone tent, staff in hand; the whole camp beginning to turn and watch behind him.",
        "must_not_show": "no figure of God, no halo; the anticipation in the WATCHERS — heads turning row by row.",
        "scene": (
            "The walk begins and the "
            "whole camp feels it: Moses "
            "striding out alone across "
            "the open ground toward the "
            "far dark tent, staff "
            "swinging with the old "
            "strong rhythm — and behind "
            "him, row by row down the "
            "tent streets, work stopping: "
            "a hammer resting, a jar set "
            "down, faces lifting and "
            "turning after the lone "
            "figure the way grass turns "
            "after wind — because "
            "everyone knows where that "
            "road goes. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r105-b04", "out": "s04-all-the-people-would-rise.jpeg", "seg": "n3",
        "window": "17.86-27.97", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOSES", "CAMP", "TENT"],
        "narration": (
            "All the people would rise and stand, each at the door of their "
            "own tent, and watch him go, and worship — because they knew "
            "where he was going, and who was waiting for him."
        ),
        "must_show": "SCRIPTURE-EXACT: every man at his tent door — the camp's rows lined with standing figures at their own doors, all facing the small walking man; a nation on its feet in reverence.",
        "must_not_show": "no figure of God, no halo; the standing UNIVERSAL — every visible tent door filled with its watcher.",
        "scene": (
            "A nation stands up at its doors, the camera down a "
            "tent-row behind the standing watchers' backs: "
            "doors: down every visible "
            "row of the great camp, "
            "figures rising at their own "
            "tent flaps — fathers with "
            "children lifted to see, "
            "old women with hands "
            "pressed to their mouths, "
            "young men gone still — "
            "every face aimed at one "
            "small striding figure "
            "crossing the emptiness "
            "toward the lone dark tent, "
            "and here and there along "
            "the rows, heads beginning "
            "to bow — a whole people "
            "worshipping at the sight "
            "of someone else's "
            "appointment. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r105-b05", "out": "s05-not-his-power.jpeg", "seg": "n6b",
        "window": "91.11-92.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": "Not his power.",
        "must_show": "the not-power beat — close on Moses's listening face inside the tent's soft light: awe without terror; whatever is being offered, it is not force.",
        "must_not_show": "ABSOLUTE: no figure, shape or hand of God; the register GENTLE — power conspicuously absent from the moment.",
        "scene": (
            "Close on the listening face "
            "in the tent's soft light, "
            "and on what is NOT arriving "
            "in it: no bracing against "
            "force, no squint against "
            "majesty, no flinch of a man "
            "before a throne — the deep-"
            "lined features open and at "
            "ease, receiving something "
            "that is plainly not power — "
            "the awe on him the kind you "
            "wear for goodness at close "
            "range, which asks nothing "
            "of the spine but stillness. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r105-b06", "out": "s06-as-moses-reached-the-tent.jpeg", "seg": "n4",
        "window": "28.54-36.56", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "As Moses reached the tent, a great pillar of cloud would come "
            "down and stand at the door — the presence of God himself, come "
            "down to meet one man."
        ),
        "must_show": "SCRIPTURE-EXACT: the pillar descending — the great column of cloud coming down out of clear sky to STAND at the tent door as Moses arrives; the meeting's two parties at one threshold.",
        "must_not_show": "ABSOLUTE: no figure, face or form in or of the cloud — cloud only, standing impossibly; no halo.",
        "scene": (
            "As his hand reaches, the camera far back behind the "
            "watching camp so pillar and tent read from the side, the "
            "flap, the sky keeps the "
            "appointment: a great column "
            "of cloud coming down out of "
            "the clear blue — unhurried, "
            "deliberate, impossibly "
            "vertical — to stand at the "
            "tent's door like a visitor "
            "who has arrived, its base "
            "just off the trodden "
            "ground, its height going up "
            "past seeing — the presence "
            "come down the whole "
            "distance of heaven to meet "
            "one dusty man at one "
            "goat-hair door. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b07", "out": "s07-and-the-lord-spake-unto.jpeg", "seg": "nface",
        "window": "37.18-41.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "And the LORD spake unto Moses face to face, as a man speaketh "
            "unto his friend."
        ),
        "must_show": "SCRIPTURE-EXACT: face to face — inside the tent: Moses seated easy and near, face lifted toward a warm nearness of light before him; conversation's intimacy with NO figure present.",
        "must_not_show": "ABSOLUTE: no figure, face, shape or outline in the light — the friendship carried entirely by Moses's easy, engaged posture.",
        "scene": (
            "Inside the dark tent the "
            "impossible intimacy: Moses "
            "seated close and easy on "
            "the woven mat, staff laid "
            "aside, leaning slightly "
            "forward the way a man "
            "leans at a friend's table — "
            "his lined face lit warm by "
            "a nearness of light before "
            "him that fills the tent's "
            "heart and holds no shape "
            "at all — talk passing in "
            "both directions in the "
            "hush, easy as bread "
            "between old friends. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b08", "out": "s08-not-a-master-barking-at.jpeg", "seg": "n5",
        "window": "43.20-45.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": "Not a master barking at a servant.",
        "must_show": "the not-that — Moses's posture the proof: no cringe, no bowed servility; a man sitting WITH, not under.",
        "must_not_show": "ABSOLUTE: no figure of God; nothing servile in Moses — shoulders easy, head level.",
        "scene": (
            "The posture tells the whole "
            "theology: nothing in the "
            "old man's body of the "
            "servant braced for orders — "
            "no cringe in the shoulders, "
            "no bowed-neck flinch, no "
            "waiting-for-the-bark "
            "stillness — Moses sits "
            "level-headed and easy in "
            "the warm light, one knee "
            "up, hands loose — the "
            "seating arrangement of "
            "friendship, in the one "
            "tent on earth where you "
            "would least expect it. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r105-b09", "out": "s09-not-a-king-across-a.jpeg", "seg": "n5",
        "window": "45.94-52.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "Not a king across a vast throne room — easy, honest, close. "
            "God wanted Moses."
        ),
        "must_show": "the closeness — the tent's smallness itself: the warm light near enough to touch, no throne-room distance anywhere; intimacy in architecture.",
        "must_not_show": "ABSOLUTE: no figure of God, no throne imagery — the tent small, the nearness total.",
        "scene": (
            "The architecture preaches "
            "against every throne room "
            "ever built: goat-hair walls "
            "a spear-length apart, a "
            "woven mat, a man — and the "
            "warm shapeless light near "
            "enough to touch, filling "
            "the little space to its "
            "seams — no hundred-pillar "
            "hall, no long red carpet "
            "of approach, no distance "
            "engineered to make a "
            "visitor small — closeness "
            "chosen by the One who "
            "owns all the distance "
            "there is. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r105-b10", "out": "s10-not-just-his-obedience-his.jpeg", "seg": "n5",
        "window": "52.07-55.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": "Not just his obedience. His friendship.",
        "must_show": "the friendship close — Moses's face mid-conversation: listening, half-smiling, fully himself; wanted for company, and knowing it.",
        "must_not_show": "ABSOLUTE: no figure of God; the half-smile REAL — comfort no servant ever wore.",
        "scene": (
            "Close on the face of a man "
            "who is wanted: the deep-"
            "lined features mid-"
            "conversation, listening "
            "with the beginning of a "
            "smile in the white beard, "
            "an eyebrow raised at "
            "something said — fully "
            "himself, holding nothing "
            "in reserve, easy in a way "
            "obedience alone never "
            "makes a face — the look "
            "of a man who has "
            "discovered that the Maker "
            "of everything enjoys his "
            "company, and comes back "
            "for it. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r105-b11", "out": "s11-my-presence-shall-go-with.jpeg", "seg": "jv14 + n5b",
        "window": "55.63-62.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT", "CAMP"],
        "narration": (
            "My presence shall go with thee, and I will give thee rest. Not "
            "send someone ahead."
        ),
        "must_show": "SCRIPTURE-EXACT: the promise — from the tent door: Moses looking out at the long road and camp beyond, the cloud pillar standing WITH him at the threshold; accompaniment pledged.",
        "must_not_show": "ABSOLUTE: no figure in the cloud; the WITH visible — pillar and man side by side facing the same horizon.",
        "scene": (
            "The promise takes its "
            "picture at the door: Moses "
            "standing in the opened "
            "flap looking out at "
            "everything still ahead — "
            "the camp, the wilderness, "
            "the unmarked years — and "
            "beside him at the "
            "threshold, close as a "
            "companion's shoulder, the "
            "great cloud column standing "
            "faced the same direction — "
            "MY PRESENCE SHALL GO WITH "
            "THEE — not a scout sent "
            "forward, not a watcher "
            "far off: company, for the "
            "whole road. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r105-b12", "out": "s12-not-watch-from-somewhere-far.jpeg", "seg": "n5b + n6",
        "window": "62.87-68.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "Not watch from somewhere far off. Go with you. And that "
            "friendship made Moses bold."
        ),
        "must_show": "the boldness rising — close on Moses's face turning back into the tent: a request assembling behind the eyes, daring growing out of trust.",
        "must_not_show": "ABSOLUTE: no figure of God; the boldness TRUST'S child — no impudence in it.",
        "scene": (
            "Close on trust turning into "
            "daring: Moses's face as he "
            "turns back into the warm "
            "light with something "
            "assembling behind the old "
            "eyes — the request no one "
            "has ever made, weighing "
            "itself on his tongue — not "
            "impudence, nothing of the "
            "presumer in it: just the "
            "plain boldness that grows "
            "wild wherever real "
            "friendship has been "
            "planted, reaching now for "
            "the biggest thing it can "
            "imagine asking. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b13", "out": "s13-he-asked-for-the-one.jpeg", "seg": "n6 + s18",
        "window": "68.54-74.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "He asked for the one thing no one had ever dared to ask. I "
            "beseech thee, shew me thy glory."
        ),
        "must_show": "SCRIPTURE-EXACT: the ask — Moses risen to his knees in the tent's light, arms half-lifted, the enormous request leaving him: SHEW ME THY GLORY.",
        "must_not_show": "ABSOLUTE: no figure of God; the ask REVERENT-BOLD — knees down, face up, everything wagered.",
        "scene": (
            "And he asks it: down on his "
            "knees in the warm shapeless "
            "light with his arms half-"
            "lifted and his white head "
            "back — I BESEECH THEE — the "
            "words that no patriarch, "
            "no prophet, no angel-"
            "wrestler ever dared — SHEW "
            "ME THY GLORY — the whole "
            "capital of a lifetime's "
            "friendship spent on one "
            "request, flung open-handed "
            "at the very center of the "
            "light. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r105-b14", "out": "s14-i-will-make-all-my.jpeg", "seg": "jv19",
        "window": "76.19-82.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "I will make all my goodness pass before thee, and I will "
            "proclaim the name of the LORD before thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the answer — Moses's kneeling face receiving the granted-more-than-asked: wonder breaking across the old features as GOODNESS is promised.",
        "must_not_show": "ABSOLUTE: no figure of God; the grant carried in HIS face — astonishment at the word chosen.",
        "scene": (
            "The answer comes back "
            "larger and gentler than "
            "the ask: across the "
            "kneeling face wonder "
            "breaks like slow water — "
            "granted, GRANTED — and "
            "with it the strange word "
            "the light has chosen for "
            "itself: not my majesty, "
            "not my power, not my "
            "terror — ALL MY GOODNESS "
            "shall pass before thee — "
            "the deep-lined features "
            "working at the word like "
            "a man handed a treasure "
            "in a currency he did not "
            "know existed. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r105-b15", "out": "s15-show-me-your-glory-moses.jpeg", "seg": "n6b",
        "window": "84.09-86.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": "Show me your glory, Moses asked.",
        "must_show": "the ask held — the kneeling silhouette against the tent's warm light, arms open: the request itself as an image, suspended.",
        "must_not_show": "ABSOLUTE: no figure of God; the frame SIMPLE — one asker, one light.",
        "scene": (
            "The frame holds the ask "
            "like a held breath: the "
            "old man's kneeling shape "
            "dark against the tent's "
            "filled warmth, arms open "
            "at his sides, white beard "
            "lifted — one human being "
            "and one request suspended "
            "together in the small "
            "goat-hair room where the "
            "boundary of what a man "
            "may say to God has just "
            "been moved, permanently, "
            "by a friend. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r105-b16", "out": "s16-and-god-answered-i-will.jpeg", "seg": "n6b",
        "window": "86.33-91.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": (
            "And God answered — I will make all my goodness pass in front "
            "of you."
        ),
        "must_show": "the yes received — close on Moses's bowed head under the answer: gratitude bending the strong old frame; a yes bigger than the ask.",
        "must_not_show": "ABSOLUTE: no figure of God; the bending GRATITUDE — not fear.",
        "scene": (
            "Close on what a yes that "
            "size does to a man: the "
            "strong old frame bending "
            "slowly forward under it, "
            "the white head bowing not "
            "in fear but in the "
            "particular gravity of "
            "gratitude, one weathered "
            "hand coming to rest flat "
            "over his own heart — the "
            "boldest request ever made "
            "being answered with more "
            "than it asked, and its "
            "asker folding gently "
            "under the weight of being "
            "loved that much. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b17", "out": "s17-not-his-greatness-his-goodness.jpeg", "seg": "n6b",
        "window": "92.09-98.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "Not his greatness. His goodness. Of everything he could have "
            "shown a friend, that is what he chose."
        ),
        "must_show": "the chosen word — the quiet tent scene at peace: Moses and the warm light in their friendship's stillness; GOODNESS as the revelation's whole self-portrait.",
        "must_not_show": "ABSOLUTE: no figure of God; the stillness WARM — the choice of goodness felt as tenderness in the light itself.",
        "scene": (
            "The tent rests inside the "
            "choice that was made: the "
            "old man quiet on the mat, "
            "the shapeless warmth "
            "filling the little room "
            "with something that can "
            "only be called kindness at "
            "scale — of all the "
            "self-portraits omnipotence "
            "might paint for its friend "
            "— the storms, the suns, "
            "the mathematics — it chose "
            "the one word a shepherd "
            "could carry down a "
            "mountain: GOOD — and the "
            "room is full of it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b18", "out": "s18-thou-canst-not-see-my.jpeg", "seg": "jv20",
        "window": "99.44-105.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "TENT"],
        "narration": (
            "Thou canst not see my face: for there shall no man see me, and "
            "live."
        ),
        "must_show": "SCRIPTURE-EXACT: the limit set — Moses's face receiving the cannot: solemnity without hurt; a boundary drawn in love across the friendship.",
        "must_not_show": "ABSOLUTE: no figure of God; NO rejection in Moses's face — the limit heard as protection.",
        "scene": (
            "The one boundary of the "
            "friendship is drawn, and "
            "drawn gently: THOU CANST "
            "NOT SEE MY FACE — and on "
            "the old listening features "
            "no wound appears, no door-"
            "slammed flinch — solemnity, "
            "rather: the stillness of a "
            "man being told the stove "
            "is hot by someone guarding "
            "his hands — a limit that "
            "arrives wearing the same "
            "kindness as the yes did, "
            "because it is made of the "
            "same material. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b19", "out": "s19-that-was-not-a-refusal.jpeg", "seg": "n6c",
        "window": "106.95-108.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": "That was not a refusal.",
        "must_show": "the not-refusal — Moses's steady unhurt face: the cannot understood rightly; trust intact and visibly deeper.",
        "must_not_show": "ABSOLUTE: no figure of God; the trust DEEPENED — no disappointment lines anywhere.",
        "scene": (
            "Close on a no received "
            "rightly: the weathered face "
            "steady and unhurt, the "
            "deep eyes holding the "
            "cannot up to the light "
            "and finding it made of "
            "the same care as every "
            "yes before it — no "
            "disappointment settling in "
            "the old lines, trust "
            "going down a fathom "
            "deeper instead — the rare "
            "wisdom of a man who can "
            "tell a locked door from "
            "a shielding arm. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r105-b20", "out": "s20-it-was-care-the-way.jpeg", "seg": "n6c",
        "window": "108.40-113.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": (
            "It was care — the way you would not hand a child something far "
            "too heavy to hold."
        ),
        "must_show": "care's shape — close on Moses's own great scarred hands open in his lap: the hands that carry stone tablets, still too small for one sight; finitude held tenderly.",
        "must_not_show": "ABSOLUTE: no figure of God; the image HIS hands — strong, and not strong enough, and safe.",
        "scene": (
            "Close on the strongest "
            "hands in Israel, open in "
            "an old man's lap: palms "
            "that shattered stone "
            "tablets and split a sea's "
            "worth of arguments, scarred "
            "and massive in the tent's "
            "warm light — and still, "
            "for one particular weight, "
            "a child's hands: too small "
            "by whole heavens for the "
            "unveiled sight — held "
            "back from it not by rank "
            "but by love, the way you "
            "keep the anvil from the "
            "toddler reaching for it. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r105-b21", "out": "s21-so-god-did-the-gentlest.jpeg", "seg": "n7",
        "window": "114.00-116.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "CLEFT"],
        "narration": "So God did the gentlest thing.",
        "must_show": "the gentlest thing begun — high on the mountain: Moses being led to the man-sized cleft in the sheer granite, the sky already changing with what approaches.",
        "must_not_show": "ABSOLUTE: no figure or hand of God — Moses climbs to the cleft alone; the approach only in the sky's charging light.",
        "scene": (
            "High on the raw mountain "
            "the gentlest arrangement "
            "is prepared: Moses climbing "
            "the last granite shelf to "
            "the man-sized split in the "
            "sheer face — a slot of "
            "shadow exactly deep enough "
            "to hold one human being — "
            "while behind the far "
            "ridges the whole sky has "
            "begun to charge with a "
            "brightness that is not "
            "weather, and the air goes "
            "tight the way it does "
            "before the sea arrives. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r105-b22", "out": "s22-he-tucked-moses-into-a.jpeg", "seg": "n7",
        "window": "116.11-126.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "CLEFT"],
        "narration": (
            "He tucked Moses into a cleft in the rock, and covered him with "
            "his own hand, and let all his goodness pass by — near enough "
            "to feel, too much to look at."
        ),
        "must_show": "SCRIPTURE-EXACT rendered per law: Moses pressed deep in the cleft, a deep sheltering SHADOW folded over the opening while an overwhelming brilliance passes across the mountain face beyond.",
        "must_not_show": "ABSOLUTE: no literal hand, no figure, no shape in the brilliance — the covering is SHADOW, the passing is LIGHT; Moses safe within.",
        "scene": (
            "And then the passing: the "
            "whole mountain face flooding "
            "with a brilliance that "
            "turns granite to molten "
            "outline — and over the one "
            "man-sized cleft, exactly "
            "there and nowhere else, a "
            "deep sheltering shadow "
            "folded down like a wing of "
            "darkness, holding its "
            "small pocket of night "
            "around the pressed-in "
            "prophet while all the "
            "goodness in existence "
            "pours past a hand-breadth "
            "away — near enough to "
            "shake his bones, too much "
            "by infinities to look at. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r105-b23", "out": "s23-he-protected-his-friend-even.jpeg", "seg": "n7",
        "window": "126.82-131.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "CLEFT"],
        "narration": "He protected his friend even from the weight of his own glory.",
        "must_show": "the protection close — Moses within the cleft's held shadow: eyes pressed shut, face awed and SAFE, the brilliance rimming the rock edges beyond the shadow's border.",
        "must_not_show": "ABSOLUTE: no hand or figure; the safety the subject — sheltered smallness inside passing immensity.",
        "scene": (
            "Close inside the kept "
            "darkness: Moses pressed to "
            "the cold granite with his "
            "eyes shut tight and his "
            "beard trembling in the "
            "shuddering air, the "
            "brilliance beyond the "
            "shadow's edge turning the "
            "rock rims white-hot with "
            "light — and around him, "
            "unbroken, the little "
            "pocket of gentle dark "
            "holding like a cupped "
            "palm — a man kept safe "
            "from his own answered "
            "prayer by the very One "
            "passing by. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r105-b24", "out": "s24-and-when-moses-came-back.jpeg", "seg": "n8",
        "window": "131.73-136.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES", "CAMP"],
        "narration": (
            "And when Moses came back down, his face was shining. He did "
            "not even know it."
        ),
        "must_show": "SCRIPTURE-EXACT: the shining unknown — Moses descending toward the camp in ordinary afternoon, his face bright as sunlit snow; people below shading their eyes; HE unaware.",
        "must_not_show": "no halo or ring of light — the SKIN of the face itself bright; his manner completely ordinary, oblivious.",
        "scene": (
            "Down the ordinary afternoon "
            "trail comes the extraordinary "
            "face: Moses picking his "
            "way toward camp with his "
            "mind on his footing — and "
            "the skin of his face "
            "bright as sunlit snow, "
            "bright past explaining, so "
            "that far below people "
            "stop and shade their eyes "
            "at him like men looking "
            "east at dawn — while the "
            "one person on the "
            "mountain who cannot see "
            "it hitches his robe and "
            "keeps walking, entirely "
            "unaware. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r105-b25", "out": "s25-that-is-what-happens-to.jpeg", "seg": "n9",
        "window": "136.69-144.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOSES"],
        "narration": (
            "That is what happens to someone who spends time close to God — "
            "you start, quietly, to glow with a little of him."
        ),
        "must_show": "the borrowed brightness — close on the shining face in ordinary light: warmth caught from Presence, worn unawares; the change gentle and real.",
        "must_not_show": "no halo or ring of light — the brightness IN the skin, soft as reflected morning; nothing theatrical.",
        "scene": (
            "Close on what proximity "
            "leaves behind: the old "
            "face in plain afternoon "
            "light, and in the skin of "
            "it a soft brightness that "
            "no sun accounts for — "
            "caught the way linen "
            "catches the smell of "
            "cedar, the way a stone "
            "keeps noon's warmth into "
            "evening — Presence, worn "
            "unawares in the flesh of "
            "a man who only knows he "
            "was with his Friend, and "
            "came home. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r105-b26", "out": "s26-it-began-with-a-friendship.jpeg", "seg": "n9",
        "window": "144.30-148.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["TENT", "CAMP"],
        "narration": "It began with a friendship, at a tent, outside the camp.",
        "must_show": "the closing image — the lone tent on the open ground in evening light, the camp's fires far behind; the meeting place itself, humble and world-changing.",
        "must_not_show": "no figure, no halo; the frame PEOPLE-EMPTY — the tent and the trodden path to it carrying the whole meaning.",
        "scene": (
            "The closing frame keeps the "
            "unlikely address: one plain "
            "goat-hair tent alone on "
            "the evening plain, its "
            "guy-lines humming, a "
            "well-trodden path worn "
            "bare between it and the "
            "distant firelit camp — no "
            "marble anywhere, no gold, "
            "no gate — just the spot "
            "of ground where the Maker "
            "of everything kept "
            "standing appointments with "
            "a man, and the path that "
            "friendship wore in the "
            "earth by being used. "
            "Every figure has two arms, "
            "two hands and one head."
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
