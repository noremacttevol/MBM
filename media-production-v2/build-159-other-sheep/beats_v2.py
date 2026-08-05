#!/usr/bin/env python3
"""V2 beat map — row 159, build-159-other-sheep (John 10:14-16).

COVERAGE: 20 pictures over 127.1 s = 6.4 s/picture (matches the library density).

SCRIPTURE FACTS (John 10 KJV):
  10:14 "I am the good shepherd, and KNOW MY SHEEP, and am KNOWN
        OF MINE."
  10:16 "And OTHER SHEEP I have, which are NOT OF THIS FOLD: them
        also I MUST BRING, and they SHALL HEAR MY VOICE; and there
        shall be ONE FOLD, and ONE SHEPHERD."
  Same John 10 shepherd discourse as row 143 (i-am-the-door) —
  same teaching hillside, same parable shepherd, same fold.

ROW INTENT: the outsider-counted-in row — the flock in front of him
is not all the sheep he has; far-off people he already owns will
hear his voice, and the scattered become ONE fold under ONE
shepherd. The viewer is one of the other sheep.

RENDERING LAWS:
  - THE ILLUSTRATIVE SHEPHERD (b02/b03/b04/b05/b06/b14/b16-b20) is
    build-21's/143's parable shepherd, NOT jesus-locked — the
    SHEPHERD lock below is byte-identical with rows 21/143 (one
    parable shepherd across the library). Jesus appears as HIMSELF
    only in the teaching beats (b01/b07/b09/b10/b15).
  - THE FOLD is 143's fold byte-identical: dry-stone, exactly ONE
    opening, NO gate, NO bars ever — a rendered gate is an
    automatic reject (the row-143 gap law holds here too).
  - DIRECTION LAW (row-14): the home world (hillside, fold) sits
    frame-LEFT; the far country sits frame-RIGHT. b10's gesture
    exits right; b16's lone sheep looks left toward the call;
    b17's shepherd travels left-to-right; b20's returning sheep
    enters the fold moving right-to-left. Stated per beat.
  - THE FAR COUNTRY (b11/b12) is UNNAMED and universal — a
    different hill country at dusk, small far settlement, people
    at distance; NO map, NO recognizable geography, NO doctrine
    props: the row only says "other places."
  - NOT TWO RIVAL FLOCKS (b13): the two converging flocks get
    EQUAL light and equal size — neither favoured; no dark-vs-lit
    grading between them.
  - The listeners' shock (b08) is arrested attention — stopped
    cold, never anger, never scowling.

TIME OF DAY ARC (intentional): the teaching slope in warm day; the
parable flock frames in clear pastoral day; the far country at
soft dusk (their evening is not darkness — kept warm); the
gathering and close at violet dusk with the fold's small fire.

CHANGING CONDITIONS (kept OUT of the locks): the flock — grazing,
turning to his step, converging, folded; the far sheep — alone,
then walking, then arriving.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "FOLD": (
        "FOLD LOCK: the hill sheepfold — a dry-stone fold on a "
        "night hillside with exactly ONE opening in its wall and NO "
        "gate: an open gap the width of a man; cream-wool sheep "
        "within, deep-blue night or violet dusk, a small shepherd's "
        "fire by the gap. The same fold, wall and single opening "
        "throughout."
    ),
    "SHEPHERD": (
        "SHEPHERD LOCK: one working Judean shepherd of about THIRTY-FIVE — never "
        "old, never grey, never white-bearded. He is lean, broad-shouldered and "
        "weather-hardened, sun-darkened to a deep brown at the face, neck and "
        "forearms, with thick black hair to the jaw pushed back off his forehead and "
        "a short full black beard with no grey in it at all. He has a straight nose, "
        "a heavy brow and dark brown eyes set deep from squinting into distance. He "
        "wears a short knee-length tunic of coarse undyed DARK EARTH-BROWN wool, "
        "worn thin at the shoulder, with a wide folded rust-brown cloth sash knotted "
        "at the waist, a rolled coarse DARK UMBER-BROWN wool mantle slung across one "
        "shoulder, and hard-worn dark leather sandals. HE WEARS NO SHEEPSKIN, NO "
        "FLEECE-LINED GARMENT AND NOTHING PALE, WHITE OR CREAM-COLOURED ANYWHERE ON "
        "HIS BODY — every piece of cloth on him is dark brown or rust-brown. He carries a long "
        "hand-cut olivewood staff with a natural crook, its wood polished dark by his "
        "hands. HE IS NEVER IN CREAM, OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH. He is "
        "the same man, same age, same black hair and beard, same brown tunic in every "
        "frame he appears in, near or far, sharp or blurred, front or back, and he is "
        "never aged, greyed, thinned, or replaced by another man. He is the "
        "SAME shepherd as build-21's (the lost-sheep parable) — one parable "
        "shepherd across both rows. He is the parable's shepherd, NOT Jesus."
    ),
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a dry grazing slope "
        "in warm daylight where Jesus teaches, listeners seated on "
        "the rocks, the fold visible on the hill beyond. The same "
        "slope throughout."
    ),
    "FAR-COUNTRY": (
        "FAR-COUNTRY LOCK: the far land — a DIFFERENT hill country "
        "at soft warm dusk: unfamiliar ridgelines, a small far "
        "settlement of low dwellings with evening fires, its own "
        "grazing slopes; no landmark, no map-recognizable feature. "
        "The same far country in every far-country frame."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the hillside listeners — a modest mixed "
        "crowd of Judean men and women seated on the rocks of the "
        "slope in earth-toned robes of brown, rust, olive and slate "
        "(no cream — only Jesus wears cream); distinct faces, all "
        "ages, never twinned, never uniform."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r159-b01", "out": "s01-on-a-hillside-surrounded-by.jpeg", "seg": "n1",
        "window": "0.28-7.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "LISTENERS"],
        "narration": (
            "On a hillside, surrounded by his listeners, Jesus reached for "
            "the most familiar picture they had — a shepherd and his flock."
        ),
        "must_show": "the ONE establishing wide — camera low on the slope behind the seated listeners' shoulders looking UP the rise to Jesus teaching; the fold visible small on the hill beyond frame-LEFT; every listener's gaze converging on him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gazes CONVERGE on him — nobody wandering; the fold beyond tiny, not competing.",
        "scene": (
            "The discourse opens where the crowd already "
            "lives, the camera set low on the dry grazing "
            "slope behind the seated listeners so the frame "
            "climbs with the hill: Jesus stands a few steps "
            "up the rise in the warm day, mid-teaching, one "
            "hand open toward the families settled on the "
            "rocks below him — and every face on the slope "
            "is turned up to him, the whole hillside's "
            "attention converging on one man reaching for "
            "the most familiar picture in their world, the "
            "stone fold itself standing small on the hill "
            "beyond his shoulder at the frame's left edge. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r159-b02", "out": "s02-he-was-the-shepherd-he.jpeg", "seg": "n1",
        "window": "7.94-13.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": (
            "He was the shepherd, he told them, the good one, and the sheep "
            "were his very own."
        ),
        "must_show": "the picture itself — the parable shepherd standing among his grazing flock in clear pastoral day, staff in hand, at ease among sheep that are HIS; ownership read as belonging, not herding.",
        "must_not_show": "he is the PARABLE shepherd, not Jesus — dark earth-brown tunic, never cream; no halo.",
        "scene": (
            "The picture stands up as he names it: the "
            "shepherd out on the open pasture in the clear "
            "day, olivewood staff planted easy, cream-wool "
            "sheep grazing close around his knees without a "
            "flicker of wariness — not a hired man watching "
            "an employer's animals but an owner standing in "
            "the middle of what is his very own, the flock "
            "arranged around him the way a family arranges "
            "itself around its father. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b03", "out": "s03-it-is-a-tender-thing.jpeg", "seg": "n2",
        "window": "14.18-16.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": "It is a tender thing to be known like that.",
        "must_show": "the tenderness insert — close on the shepherd's weathered hand resting on one ewe's head, her eyes half-closed under it; the knowing made touchable.",
        "must_not_show": "no halo; the hand GENTLE — resting, not gripping; one sheep, one hand, nothing else needed.",
        "scene": (
            "One hand carries the whole sentence: close in "
            "on the shepherd's sun-darkened fingers resting "
            "on the head of a single ewe, her wool pressed "
            "up between them, her eyes half-closing under "
            "the familiar weight the way an animal only "
            "does under a touch it has known its whole "
            "life — tenderness as fact, being known made "
            "into something you can photograph. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b04", "out": "s04-not-counted-as-part-of.jpeg", "seg": "n2",
        "window": "16.52-29.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": (
            "Not counted as part of a crowd, but known — each one, by name, "
            "by voice, by the particular way it strays and the particular way "
            "it finds its way home."
        ),
        "must_show": "the particular knowing — the shepherd crouched to meet ONE returning stray coming back over the pasture toward him, his hand out, her trot unmistakably homeward; the rest of the flock grazing behind him unbothered.",
        "must_not_show": "no halo; the stray RETURNING under her own feet — not carried, not chased; his posture welcome, never scolding.",
        "scene": (
            "Known one at a time: the shepherd drops to a "
            "crouch on the open pasture as a single ewe "
            "comes trotting back over the grass toward "
            "him — her particular gait, her particular "
            "crooked path home, the one he could name "
            "blindfolded — his hand already out at her "
            "height, the flock grazing on behind his back "
            "because this moment belongs to her alone: not "
            "a head in a count but a name coming home to "
            "the voice that knows it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b05", "out": "s05-and-the-knowing-runs-both.jpeg", "seg": "n3",
        "window": "30.41-32.23", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And the knowing runs both ways.",
        "must_show": "the both-ways insert — a tight frame of three or four sheep LIFTING their heads together from grazing, ears turned to one point off frame-left; the recognition, not yet the following.",
        "must_not_show": "no shepherd in frame — the lifted heads ARE the sentence; ears and gazes agree on one off-frame point.",
        "scene": (
            "The other direction of the knowing: tight on a "
            "handful of grazing sheep as every head comes "
            "up at once — mid-chew, ears swivelled to the "
            "same point beyond the frame's left edge, four "
            "gazes agreeing on one arriving step before a "
            "single hoof has moved — recognition running "
            "from the flock back toward the man, the "
            "knowing answered in kind. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b06", "out": "s06-his-own-know-him-too.jpeg", "seg": "n3",
        "window": "32.23-42.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": (
            "His own know him too — the sound of his voice, the shape of his "
            "care — the way sheep will lift their heads at one familiar step "
            "and follow no stranger."
        ),
        "must_show": "the following — the shepherd walking the pasture frame-right-to-left, the flock strung out BEHIND him mid-follow, every head oriented to his back; his step the thing they trust.",
        "must_not_show": "no halo; no stranger figure rendered — 'follow no stranger' is carried by how completely they follow HIM; nobody drives the flock from behind.",
        "scene": (
            "The proof walks: the shepherd crosses the "
            "pasture at his own unhurried pace, staff "
            "swinging, and the flock comes after him in a "
            "loose ribbon — not driven, DRAWN, every head "
            "up and oriented to the set of his shoulders, "
            "lambs trotting the gaps closed — the whole "
            "line moving on nothing but the sound of one "
            "familiar step, the shape of one man's care, a "
            "trust no stranger's voice could counterfeit. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r159-b07", "out": "s07-i-am-the-good-shepherd.jpeg", "seg": "kv14",
        "window": "43.52-47.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "LISTENERS"],
        "narration": (
            "I am the good shepherd, and know my sheep, and am known of mine."
        ),
        "must_show": "SCRIPTURE-EXACT: the claim — Jesus on the warm day slope saying the words, hand flat at his own chest on 'I am'; nearest listeners' faces soft with the tenderness of it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand-flat-at-chest gesture (the I AM series signature); no shepherd costume on Jesus — he wears his cream robe.",
        "scene": (
            "The picture gets its name: Jesus on the warm "
            "slope brings one hand flat against his own "
            "chest as the words land — I am the good "
            "shepherd — the nearest listeners' faces going "
            "soft around him, because the tender picture "
            "they have been watching in their minds has "
            "just been claimed by the man in front of them: "
            "the knowing, and the being known, both his. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r159-b08", "out": "s08-but-then-jesus-said-something.jpeg", "seg": "n4",
        "window": "48.82-51.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["LISTENERS"],
        "narration": "But then Jesus said something that must have stopped them cold.",
        "must_show": "the arrest — a tight two-shot of listeners' faces caught mid-reaction: stillness, parted lips, attention snapped taut; stopped cold, not angry.",
        "must_not_show": "NO scowls, NO anger — arrested attention only; Jesus out of frame (the sentence is about THEIR faces).",
        "scene": (
            "The slope goes still: tight on two listeners "
            "in the crowd — an older man and a young "
            "woman — caught in the exact instant a sentence "
            "lands wrong-footed, his brow just beginning to "
            "knit, her lips parted on a breath she has "
            "forgotten to finish, both gazes locked on the "
            "unseen speaker up the rise frame-left — not "
            "offence, ARREST, the stillness of people who "
            "need the next sentence more than air. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b09", "out": "s09-this-flock-right-here-in.jpeg", "seg": "n4",
        "window": "51.70-57.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "LISTENERS"],
        "narration": (
            "This flock, right here in front of me, he told them — you are "
            "not all the sheep I have."
        ),
        "must_show": "the turn — Jesus's open hand sweeping the crowd in front of him ('this flock, right here') while his eyes already lift PAST them toward the horizon; the sentence pivoting mid-gesture.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture takes in the crowd, the GAZE goes beyond it — both must read.",
        "scene": (
            "The sentence turns in his hands: Jesus sweeps "
            "one open palm across the families seated below "
            "him — this flock, right here — but his eyes "
            "have already lifted over their heads to the "
            "hazy distance beyond the slope, holding both "
            "halves of the thought at once: everything in "
            "front of him claimed, and something past the "
            "horizon claimed just as surely — you are not "
            "all the sheep I have. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b10", "out": "s10-there-are-others-in-other.jpeg", "seg": "n4",
        "window": "57.40-60.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE"],
        "narration": "There are others, in other places, not of this fold.",
        "must_show": "the beyond — over Jesus's shoulder from behind: his lifted hand pointing out past the slope's edge toward the far haze, the gesture EXITING frame-RIGHT; the crowd soft below.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pointing arm exits RIGHT (the far-country direction); nothing rendered at the horizon yet — haze only.",
        "scene": (
            "Others, elsewhere: the camera slides behind "
            "Jesus's shoulder so the frame looks where he "
            "does — his arm lifted past the slope's edge, "
            "hand open toward the far haze at the frame's "
            "right, the seated crowd soft and low beneath "
            "the gesture — pointing at people nobody on "
            "this hillside has ever met, in places none of "
            "them have seen, sheep of his that no fold "
            "here has ever held. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b11", "out": "s11-people-they-had-never-met.jpeg", "seg": "n5",
        "window": "61.42-67.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAR-COUNTRY"],
        "narration": (
            "People they had never met, in lands they had never seen, who "
            "also belonged to him and were waiting to be brought in."
        ),
        "must_show": "the far country — unfamiliar dusk ridgelines, a small far settlement with evening fires, a family at distance outside a low dwelling; belonging that doesn't know its shepherd's face yet.",
        "must_not_show": "NO map, NO recognizable geography, NO doctrine props — unnamed and universal; dusk WARM, never ominous; faces at distance, not portraits.",
        "scene": (
            "The camera crosses the horizon the gesture "
            "pointed at: a different hill country under "
            "soft warm dusk — ridgelines no one on the "
            "teaching slope would recognize, a small "
            "settlement of low dwellings with its evening "
            "fires just lit, a family standing small at "
            "distance outside their door as the light goes "
            "amber — people with no idea they have just "
            "been spoken of on a hillside far away, already "
            "belonged-to, already waited-for. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b12", "out": "s12-and-about-them-he-made.jpeg", "seg": "n5",
        "window": "67.98-74.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAR-COUNTRY"],
        "narration": (
            "And about them he made a quiet, sweeping promise: they too "
            "shall hear my voice."
        ),
        "must_show": "the promise landing — in the far country at dusk, two or three far-country people LIFTING their heads together toward one unseen point (the b05 rhyme, done in humans); hearing before understanding.",
        "must_not_show": "no visualized voice, no light-shaft, no figure arriving — the lifted heads carry it entirely; the b05 sheep rhyme must read.",
        "scene": (
            "The promise arrives before the messenger "
            "does: in the amber dusk of the far settlement "
            "a man straightens from his evening work and a "
            "woman turns in her doorway, both heads coming "
            "up at once toward the same unseen point past "
            "the ridgeline — the exact motion the sheep "
            "made on a pasture they will never see — they "
            "too shall hear my voice, already true in the "
            "way they lift their faces to a call that has "
            "not yet come. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r159-b13", "out": "s13-not-two-rival-flocks-not.jpeg", "seg": "n6",
        "window": "75.11-79.21", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not two rival flocks. Not one favoured and one forgotten.",
        "must_show": "the equality frame — TWO flocks converging from two valleys onto one shared slope, EQUAL in size and EQUAL in light; the meeting edge where the first sheep of each mingle.",
        "must_not_show": "ABSOLUTE: neither flock larger, brighter, or nearer — no favoured/forgotten grading; no shepherd in frame yet; no collision — a mingling.",
        "scene": (
            "Two streams, one grass: from two facing "
            "valleys two flocks come down onto the same "
            "broad slope in the last gold of the day — the "
            "same count of cream-wool backs on the left as "
            "on the right, the same warm light lying on "
            "both — and at the seam where they meet the "
            "first sheep of each are already grazing "
            "shoulder to shoulder, the line between the two "
            "flocks failing to exist the moment they "
            "touch — no rival, no favourite, no forgotten. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r159-b14", "out": "s14-in-the-end-one-fold.jpeg", "seg": "n6",
        "window": "79.21-86.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": (
            "In the end, one fold and one shepherd — every scattered sheep "
            "gathered home under the same gentle hand."
        ),
        "must_show": "the end-picture — at violet dusk the united flock files toward the ONE fold, the shepherd standing at its single gateless opening, his hand touching each back as it passes in; one fold, one man, one gap.",
        "must_not_show": "ABSOLUTE: no gate, no bars — the open gap (143's fold law); ONE shepherd only; the file of sheep moving right-to-left INTO the fold.",
        "scene": (
            "Where the whole discourse has been walking: "
            "the dry-stone fold at violet dusk with its one "
            "open gap and its small fire, and the united "
            "flock filing in from the right in an unhurried "
            "line — the shepherd standing at the opening "
            "with his staff crooked in one elbow, his free "
            "hand riding briefly on each woolly back as it "
            "presses past his knee into the safe dark — "
            "every scattered one arriving under the same "
            "gentle hand, one fold receiving them, one "
            "shepherd counting them home. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b15", "out": "s15-and-other-sheep-i-have.jpeg", "seg": "kv16",
        "window": "86.86-97.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "LISTENERS"],
        "narration": (
            "And other sheep I have, which are not of this fold: them also I "
            "must bring, and they shall hear my voice; and there shall be one "
            "fold, and one shepherd."
        ),
        "must_show": "SCRIPTURE-EXACT: the great verse — Jesus on the day slope, the fold small on the hill beyond frame-left, his open hand carrying from the crowd out toward the horizon as the promise runs its full length; the listeners very still.",
        "must_not_show": "no halo, glare or rim-light on Jesus; both anchors present — the FOLD beyond (this fold) and the open horizon (the others); nothing new invented.",
        "scene": (
            "The verse gathers everything the pictures "
            "said: Jesus stands on the warm slope with the "
            "little stone fold on the hill beyond his "
            "shoulder at the frame's left and the open "
            "hazy distance running out to the right, and "
            "his open hand travels the whole span as he "
            "speaks — from the families at his feet, out "
            "past the slope's edge to the sheep no one "
            "here has met — them also I must bring — the "
            "listeners holding still under a promise wider "
            "than their hillside. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b16", "out": "s16-so-if-you-have-ever.jpeg", "seg": "n7",
        "window": "98.76-107.28", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So if you have ever felt like an outsider — like one of the "
            "other sheep, far from where the story seemed to be happening — "
            "hear this."
        ),
        "must_show": "the outsider frame — ONE sheep alone on a darkening slope far from any flock, head LIFTED, ears turned toward frame-LEFT (the direction of the unheard call); alone but listening.",
        "must_not_show": "not injured, not trapped, not pitiful — simply FAR; dusk kept soft, never frightening; no wolf, no threat.",
        "scene": (
            "The frame for everyone who has ever stood "
            "outside the story: one sheep alone on a wide "
            "darkening slope, no flock in sight, grass to "
            "the horizon — and her head is UP, ears turned "
            "hard toward the frame's left edge where "
            "something too far to hear is nonetheless "
            "being said — far from where everything seemed "
            "to be happening, and listening anyway, which "
            "is the whole posture of hope. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b17", "out": "s17-he-counted-you-in-from.jpeg", "seg": "n7",
        "window": "107.28-112.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": (
            "He counted you in from the beginning. He always meant to come "
            "for you too."
        ),
        "must_show": "the coming — the shepherd mid-stride crossing open country left-to-right, staff in hand, purposeful, dusk light; travelling TOWARD where b16's far sheep waits; already on his way.",
        "must_not_show": "no halo; no hurry-panic — purposeful, unhurried certainty; travel direction LEFT-TO-RIGHT (toward the far country) exact.",
        "scene": (
            "He is already walking: the shepherd crosses "
            "the open dusk country in long unhurried "
            "strides, left to right across the frame, staff "
            "swinging with the pace of a man who has known "
            "the way from the beginning — not searching, "
            "GOING, toward a slope he has never grazed and "
            "a sheep who has never heard his step — counted "
            "in before she knew there was a count, come "
            "for because he always meant to come. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b18", "out": "s18-that-is-the-wide-patient.jpeg", "seg": "n8",
        "window": "112.99-115.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": "That is the wide, patient heart of the Good Shepherd.",
        "must_show": "the wide heart — the shepherd from behind on a high crest at dusk, small against a vast rolling distance where TWO far flocks graze in different valleys; the scale of what he owns and loves.",
        "must_not_show": "no halo; he is SMALL in the frame — the wideness is the point; both far flocks visible, neither nearer.",
        "scene": (
            "The heart measured in landscape: from behind, "
            "the shepherd stands small on a high crest in "
            "the last amber light, staff planted, and the "
            "country falls away enormous below him — one "
            "flock a pale scatter in the left valley, "
            "another a pale scatter in the right, both his, "
            "both held in the same long patient look — a "
            "heart the size of everything the eye can "
            "reach, and wider, because some of what it "
            "holds is past the horizon. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b19", "out": "s19-he-has-sheep-the-crowd.jpeg", "seg": "n8",
        "window": "115.80-120.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHEPHERD"],
        "narration": (
            "He has sheep the crowd never counted, and he will not rest "
            "until they hear him and come."
        ),
        "must_show": "the not-resting — the shepherd walking ON into the deepening dusk past a ridge, back to camera, still travelling left-to-right; behind him the fold's far fire; ahead, the dark country still unwalked.",
        "must_not_show": "no halo; no weariness slump — unresting means STILL GOING; the fold's fire behind frame-left ties home to journey.",
        "scene": (
            "Rest refused: the shepherd's back moves away "
            "over a dusk ridge, left to right, staff "
            "striking its steady rhythm, the small warm "
            "point of the fold's fire far behind him at the "
            "frame's left edge and the unwalked dark "
            "country opening ahead — sheep out there the "
            "crowd never counted, names on his tongue no "
            "one on the hillside has heard — and he will "
            "keep this pace until every one of them has "
            "heard it and come. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r159-b20", "out": "s20-when-you-hear-his-voice.jpeg", "seg": "n8",
        "window": "120.81-126.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOLD", "SHEPHERD"],
        "narration": (
            "So the only question is a gentle one. When you hear his voice, "
            "will you know it, and follow?"
        ),
        "must_show": "the closing invitation — the fold at deep violet dusk, fire lit, the shepherd at the open gap with one hand held out toward frame-RIGHT, and ONE sheep (the far one) arriving right-to-left, one step from the opening; the choice one step wide.",
        "must_not_show": "ABSOLUTE: no gate, no bars — the open gap; the arriving sheep moving RIGHT-TO-LEFT into home; her step MID-STRIDE — arriving, not arrived; tender, unposed.",
        "scene": (
            "The question stands in a doorway of stone: "
            "the fold at deep violet dusk, the small fire "
            "throwing warm light through the one open gap, "
            "the flock a soft crowded dark within — and the "
            "shepherd stands beside the opening with his "
            "hand held low and open toward the right, "
            "where one sheep — the far one, come all this "
            "way — is one mid-stride step from the "
            "threshold, her head up, his voice the thing "
            "she followed here — will you know it, and "
            "follow: the door has no gate, and never did. "
            "Every figure has two arms, two hands and one "
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
    "FOLD": "PLACE-REF/fold.jpeg",  # build-21-lost-sheep v2-r021-b12
}
# === end PLACE-PLATES ===
