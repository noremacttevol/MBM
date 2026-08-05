#!/usr/bin/env python3
"""V2 beat map — row 114, build-114-abraham-sodom (Genesis 18).

COVERAGE: 23 pictures over 129.7 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Genesis 18 KJV):
  v1-2  "the LORD appeared unto him in the plains of MAMRE: and he sat
        in the TENT DOOR in the HEAT OF THE DAY... lo, THREE MEN stood
        by him" — travelers first; Abraham does not yet know them.
  v4-8  the sacred hospitality: water for FEET, MEAL baked fresh,
        the calf, butter and milk; "he STOOD BY THEM under the TREE,
        and they did eat."
  v16,22 "the men rose up... toward Sodom... and Abraham went with
        them to bring them on the way"; "the men turned their faces
        from thence, and went toward Sodom: but Abraham STOOD YET
        BEFORE THE LORD."
  v23-32 the pleading ladder: fifty — forty-five — forty — thirty —
        twenty — TEN. "Shall not the Judge of all the earth do
        right?" Every answer: yes, spare.
  v33   "the LORD went his way... and Abraham returned unto his
        place." — home in the dusk, amazed.

GOD RENDERING (the row's hard edge): the text's three MEN are painted
as three plain-robed TRAVELERS for the meal beats (Abraham "did not
know at first who they were" — the pictures know no more than he
does). From v22 on — the narration itself shifting to "the warm
presence of the Lord" — the two travelers walk on and the LORD is
rendered ONLY as warm presence-light before Abraham on the height:
no figure, face or silhouette ever. NO wings, no rings of light on
the travelers at any point.

SODOM: never shown near, never burning — only far pale cities on the
darkening plain under heavy sky. The destruction is entirely
off-screen and outside this row.

TIME OF DAY ARC (intentional): the HEAT OF THE DAY for tent and meal
(hard bright noon); the walk out and the pleading through the long
gold late afternoon; home at dusk. Correct story lighting.

CHANGING CONDITION (kept OUT of the locks): the travelers — three at
the tent, then two departing, then presence only; the number —
fifty, stepping down to ten; the light — noon to gold to dusk.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream (not in this row).
LOCKS = {
    "CAMP": (
        "CAMP LOCK: the camp at Mamre — a great spreading OAK over "
        "hard bright ground, a broad black goat-hair TENT with its "
        "front pinned open, cushions and a low mat in the oak's "
        "shade. The same oak, tent and shade throughout."
    ),
    "ABRAHAM": (
        "ABRAHAM LOCK: Abraham is the same man in every shot — very "
        "old and still vigorous, a long white beard, hawk-bright "
        "eyes in a deep-lined face, in a DEEP RUSSET-BROWN robe with "
        "a CHARCOAL head cloth (never cream, never white)."
    ),
    "TRAVELERS": (
        "TRAVELERS LOCK: the three travelers are the same in every "
        "shot where they appear — tall, calm, road-dusted men in "
        "plain PALE SILVER-GREY travelling robes — NO wings, no "
        "rings of light, nothing outlining them; strong ageless "
        "faces; they eat, walk and rest like men."
    ),
    "HEIGHT": (
        "HEIGHT LOCK: the overlook height — a bare ridge above the "
        "great plain: far below, small and pale, the cities of the "
        "plain under a heavy darkening sky; long gold light on the "
        "ridge itself. The same ridge and distant cities throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r114-b01", "out": "s01-in-the-heat-of-the.jpeg", "seg": "n1",
        "window": "0.28-6.25", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMP", "ABRAHAM", "TRAVELERS"],
        "narration": (
            "In the heat of the day, three travelers appeared at Abraham's "
            "tent. He did not know at first who they were."
        ),
        "must_show": "SCRIPTURE-EXACT: the appearing — Abraham at his tent door in hard noon light, and the three silver-grey travelers standing on the bright ground before him; strangers, as far as he knows.",
        "must_not_show": "ABSOLUTE: no wings, rings of light or outlines on the travelers — road-dusted men; Abraham's face welcoming, not yet awed.",
        "scene": (
            "Out of the shimmering noon, the camera at the oak's "
            "side taking tent door and arrivals in one profile, "
            "three figures stand suddenly "
            "on the bright ground: tall "
            "road-dusted men in plain "
            "silver-grey, calm as wells, "
            "waiting at the edge of the "
            "oak's shade — and in the "
            "tent door the old man "
            "rising from his heat-of-day "
            "drowse, hawk eyes taking "
            "them in as what they seem: "
            "three tired strangers on "
            "the worst hour of the road, "
            "which to Abraham has "
            "always been reason enough "
            "to run. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r114-b02", "out": "s02-he-only-knew-they-were.jpeg", "seg": "n1",
        "window": "6.25-11.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMP", "ABRAHAM", "TRAVELERS"],
        "narration": (
            "He only knew they were strangers, and tired, and that "
            "hospitality was sacred."
        ),
        "must_show": "the sacred welcome — Abraham bowing low before the three, arm sweeping them toward the oak's shade; hospitality as liturgy.",
        "must_not_show": "no wings or light-effects; the bow DEEP — the desert's oldest sacrament beginning.",
        "scene": (
            "The old man does what the "
            "desert holds holiest: bows "
            "low before three strangers "
            "he has never met, white "
            "beard nearly to the bright "
            "ground, his arm sweeping "
            "them toward the oak's deep "
            "shade like a man opening "
            "his whole life's door — "
            "rest, water, bread, "
            "whatever is mine — the "
            "ancient liturgy of the "
            "tent offered entire before "
            "one name has been asked, "
            "because tired strangers "
            "outrank every question. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r114-b03", "out": "s03-he-washed-their-feet-baked.jpeg", "seg": "n2",
        "window": "11.98-18.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMP", "ABRAHAM", "TRAVELERS"],
        "narration": (
            "He washed their feet, baked fresh bread, set out the best he "
            "had, and waited on them himself under the oak."
        ),
        "must_show": "SCRIPTURE-EXACT: the feast served — the three seated in the oak's shade with feet washed, fresh bread and the best set before them, and old Abraham STANDING to serve them himself.",
        "must_not_show": "no wings or light-effects; Abraham STANDING while they eat (v8) — the host as servant.",
        "scene": (
            "Under the great oak the "
            "best of everything appears: "
            "the three travelers seated "
            "on cushions with their feet "
            "washed clean, fresh bread "
            "still steaming from the "
            "coals, curds and milk and "
            "the tender calf set out on "
            "the mat — and the richest "
            "man in the region standing "
            "beside the tree like a "
            "table-servant, refilling, "
            "carrying, watching their "
            "hands for the next need — "
            "a prince waiting on "
            "strangers under his own "
            "oak. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r114-b04", "out": "s04-and-as-they-ate-they.jpeg", "seg": "n2",
        "window": "18.64-24.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMP", "ABRAHAM", "TRAVELERS"],
        "narration": (
            "And as they ate, they brought him astonishing news — and a "
            "heavy word about Sodom."
        ),
        "must_show": "the news at the meal — the central traveler speaking as they eat, Abraham arrested mid-serve: wonder and weight arriving in one conversation.",
        "must_not_show": "no wings or light-effects; the shift in AIR — Abraham's face catching that these are no ordinary guests.",
        "scene": (
            "Between one serving and the "
            "next, the meal changes "
            "nature: the central "
            "traveler speaking quietly "
            "over the bread — news that "
            "stops the old man's hands "
            "mid-pour, wonder first, "
            "the laugh of impossible "
            "promise — and then the "
            "second word, heavier, "
            "turning the shade cold at "
            "its edges: SODOM — and "
            "Abraham looking from face "
            "to calm face, beginning "
            "to understand what has "
            "been eating at his table. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r114-b05", "out": "s05-for-those-cities-had-grown.jpeg", "seg": "n3",
        "window": "24.61-28.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT"],
        "narration": "For those cities had grown very dark, and judgment was near.",
        "must_show": "the dark cities far — the plain from the height: the pale cities small below under a heavy bruised sky; darkness as weather and distance, nothing burning.",
        "must_not_show": "ABSOLUTE: no fire, no destruction — distant intact cities under heavy sky only.",
        "scene": (
            "Far off and small on the "
            "great plain the cities sit "
            "under their own weather: "
            "pale walls and towers "
            "huddled in the haze, and "
            "above them — nowhere else "
            "on the whole horizon — a "
            "heavy bruised darkness "
            "hanging low, pressing, "
            "waiting — nothing burning, "
            "nothing fallen, just a "
            "sky that has finished "
            "deliberating standing over "
            "towns that do not look "
            "up — judgment near, and "
            "visible only as weight. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r114-b06", "out": "s06-two-of-the-travelers-went.jpeg", "seg": "n3",
        "window": "28.21-37.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["HEIGHT", "ABRAHAM", "TRAVELERS"],
        "narration": (
            "Two of the travelers went on ahead. But Abraham stayed behind, "
            "standing before the warm presence of the Lord — and he began "
            "to plead."
        ),
        "must_show": "SCRIPTURE-EXACT: the parting (v22) — the two travelers descending toward the plain, and Abraham on the ridge turned toward a WARM GOLD PRESENCE-LIGHT where the third stood; the shift from men to presence.",
        "must_not_show": "ABSOLUTE: no figure in the presence-light from here on — the two walk away as men, the LORD remains as light only.",
        "scene": (
            "On the gold ridge, the camera behind Abraham's still "
            "shoulder as the two descend away down the slope, the "
            "company divides into its "
            "true natures: the two "
            "travelers already "
            "descending the long slope "
            "toward the darkened plain, "
            "silver-grey and small "
            "against the distance — and "
            "where the third stood, "
            "beside the old man, no "
            "figure now but a warmth "
            "of gold light standing on "
            "the ridge like presence "
            "itself — and Abraham "
            "turning to face it, "
            "gathering the breath of "
            "his life, beginning to "
            "plead. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r114-b07", "out": "s07-not-for-himself.jpeg", "seg": "n4",
        "window": "37.93-39.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": "Not for himself.",
        "must_show": "the direction of the plea — close on Abraham's face aimed out toward the far cities, not upward for himself; intercession's outward posture.",
        "must_not_show": "ABSOLUTE: no figure of God; his own safety visibly not in question — the worry all outbound.",
        "scene": (
            "Close on a face pleading in "
            "the wrong direction for "
            "self-interest: the old "
            "hawk-bright eyes aimed "
            "not up at his own "
            "standing, which is safe, "
            "nor back at his own tent, "
            "which is far from the "
            "darkness — but OUT, "
            "across the plain, toward "
            "cities he does not live "
            "in and mostly does not "
            "know — the whole worry of "
            "the lined face spent on "
            "other people's rooftops. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r114-b08", "out": "s08-for-strangers-for-the-good.jpeg", "seg": "n4",
        "window": "39.20-44.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT", "ABRAHAM"],
        "narration": (
            "For strangers — for the good people who might still be down in "
            "that doomed city."
        ),
        "must_show": "the imagined righteous — Abraham's arm extended over the plain toward the far cities: pleading for faces he has never seen; the cities small and human below.",
        "must_not_show": "ABSOLUTE: no figure of God, no fire — the cities' smallness making them pitiable, not hateful.",
        "scene": (
            "His arm goes out over the "
            "whole plain as he pleads: "
            "the far pale cities small "
            "under their heavy sky — "
            "and in the old man's "
            "voice, faces he has never "
            "met being argued for one "
            "by one: some honest "
            "potter down there, some "
            "kind grandmother, some "
            "child who never chose "
            "any of it — strangers, "
            "invisible at this "
            "distance and utterly "
            "real to the pleader, "
            "each one worth standing "
            "longer in the road for. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r114-b09", "out": "s09-wilt-thou-also-destroy-the.jpeg", "seg": "s23",
        "window": "45.59-50.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": (
            "Wilt thou also destroy the righteous with the wicked? Shall not "
            "the Judge of all the earth do right?"
        ),
        "must_show": "SCRIPTURE-EXACT: the boldest question — close on Abraham speaking it into the warm presence-light: reverent audacity; a man holding God to God's own goodness.",
        "must_not_show": "ABSOLUTE: no figure in the light; the audacity REVERENT — bowed frame, lifted honest face.",
        "scene": (
            "The boldest question of the "
            "old world leaves an old "
            "man's mouth: bowed at the "
            "shoulders before the warm "
            "gold light, face lifted "
            "honest into it — WILT "
            "THOU ALSO DESTROY THE "
            "RIGHTEOUS WITH THE "
            "WICKED — a creature "
            "holding his Creator to "
            "the Creator's own "
            "character, respectfully, "
            "trembling, and completely "
            "in earnest — SHALL NOT "
            "THE JUDGE OF ALL THE "
            "EARTH DO RIGHT — asked "
            "by a man who is betting "
            "everything that the "
            "answer is yes. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r114-b10", "out": "s10-if-i-find-in-sodom.jpeg", "seg": "jv26",
        "window": "52.51-59.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT", "ABRAHAM"],
        "narration": (
            "If I find in Sodom fifty righteous within the city, then I "
            "will spare all the place for their sakes."
        ),
        "must_show": "SCRIPTURE-EXACT: the first yes — the ridge scene: Abraham's face flooding with relieved wonder as the answer comes from the warm light; the whole plain under the promise.",
        "must_not_show": "ABSOLUTE: no figure in the light; the YES landing visibly — an old man's held breath releasing.",
        "scene": (
            "The answer comes back "
            "better than the asking "
            "dared: from the warm gold "
            "presence the words move "
            "over the ridge — IF I "
            "FIND FIFTY, I WILL SPARE "
            "ALL THE PLACE — and the "
            "old man's held breath "
            "goes out of him in one "
            "long shudder of relieved "
            "wonder: yes — an entire "
            "plain's reprieve hung on "
            "fifty unknown decent "
            "souls, granted before "
            "the request finished "
            "echoing — the Judge of "
            "all the earth, doing "
            "right, gladly. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r114-b11", "out": "s11-yes-god-said.jpeg", "seg": "n5",
        "window": "61.44-62.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": "Yes, God said.",
        "must_show": "the yes held — close on Abraham's stunned grateful face in the gold: the first yes still landing; mercy easier to get than he dreamed.",
        "must_not_show": "ABSOLUTE: no figure; the stun GLAD — a man out-hoped by the answer.",
        "scene": (
            "Close on a man out-hoped "
            "by heaven: Abraham's "
            "deep-lined face in the "
            "warm gold, stunned still "
            "by the ease of it — he "
            "had braced to haggle, "
            "rehearsed his ground, "
            "prepared for granite — "
            "and the first ask went "
            "through like a stone "
            "through water: YES — "
            "mercy sitting there "
            "already willing, waiting "
            "all along for somebody "
            "to just ask it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r114-b12", "out": "s12-and-you-can-almost-feel.jpeg", "seg": "n5",
        "window": "62.65-67.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": (
            "And you can almost feel Abraham's courage grow. What about "
            "forty-five?"
        ),
        "must_show": "the growing courage — Abraham stepping half a pace CLOSER to the light, hands beginning to bargain: forty-five offered on his fingers; boldness feeding on mercy.",
        "must_not_show": "ABSOLUTE: no figure; the step TOWARD — courage measured in distance closed.",
        "scene": (
            "Courage does its "
            "arithmetic and steps "
            "closer: the old man half "
            "a pace nearer the warm "
            "light than he stood a "
            "moment ago, shoulders "
            "unbending, hands coming "
            "up into the bargain — "
            "forty and five, offered "
            "on spread fingers with a "
            "trader's tilt of the "
            "head and a son's "
            "hopeful eyes — boldness "
            "growing the only way it "
            "ever safely grows: fed "
            "by discovering how kind "
            "the other party already "
            "is. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r114-b13", "out": "s13-what-about-forty-thirty-each.jpeg", "seg": "n5",
        "window": "67.64-74.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT", "ABRAHAM"],
        "narration": (
            "What about forty? Thirty? Each time, gently, the answer came "
            "back — yes."
        ),
        "must_show": "the descending ladder — Abraham mid-negotiation on the gold ridge, fingers counting down; the warm light constant and patient through every step; yes upon yes.",
        "must_not_show": "ABSOLUTE: no figure; the light UNCHANGED at each step — no wearying, no dimming.",
        "scene": (
            "Down the ladder the old "
            "trader climbs, and the "
            "light never once "
            "hardens: forty — yes — "
            "the fingers folding, the "
            "voice steadying — thirty — "
            "yes — each descent met "
            "with the same unhurried "
            "warmth, no flicker of "
            "wearying anywhere in the "
            "gold, no edge creeping "
            "into the patience — an "
            "old man discovering with "
            "every rung that he is "
            "not wearing mercy down: "
            "he is climbing down "
            "into how deep it "
            "already goes. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r114-b14", "out": "s14-yes-i-will-spare-it.jpeg", "seg": "n5 + n6",
        "window": "74.67-78.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": "Yes. I will spare it. He is not wearing God down.",
        "must_show": "the not-wearing-down — Abraham's face registering the truth mid-ladder: no victory-strain in him, only deepening wonder; the negotiation revealed as discovery.",
        "must_not_show": "ABSOLUTE: no figure; NO haggler's triumph — awe replacing strategy.",
        "scene": (
            "Mid-ladder, the truth of "
            "the transaction dawns on "
            "the trader: there is no "
            "strain of victory in the "
            "old face, because there "
            "has been no victory — "
            "every yes came too fast, "
            "too warm, too glad to be "
            "won — and the hawk eyes "
            "widen with the real "
            "discovery: he is not "
            "moving God an inch; he "
            "is being walked, rung by "
            "rung, down into a mercy "
            "that was always this "
            "deep, by the Mercy "
            "itself. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r114-b15", "out": "s15-he-is-discovering-how-merciful.jpeg", "seg": "n6",
        "window": "78.64-85.11", "wide": True, "jesus": False, "ref": False,
        "locks": ["HEIGHT"],
        "narration": (
            "He is discovering how merciful God already is — how much God "
            "would rather spare than destroy."
        ),
        "must_show": "mercy's preference — the wide ridge and plain: the warm gold light leaning OUT over the darkened cities, not away; the presence oriented toward sparing.",
        "must_not_show": "ABSOLUTE: no figure, no fire — the light's direction the whole theology: toward the doomed, not turned from them.",
        "scene": (
            "The frame catches, the camera far along the ridge "
            "taking height and plain from the side, mercy's "
            "compass: on the ridge the "
            "warm gold presence-light "
            "stands leaning not away "
            "from the darkened plain "
            "but OUT over it — its "
            "warmth reaching down the "
            "long slope toward the "
            "small pale cities under "
            "their heavy sky, like a "
            "lamp held toward a room "
            "someone hopes is still "
            "occupied — the whole "
            "posture of the light "
            "saying what the ladder "
            "of yeses has been "
            "saying: RATHER SPARE — "
            "always, rather spare. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r114-b16", "out": "s16-so-abraham-dares-one-last.jpeg", "seg": "n6",
        "window": "85.11-88.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": "So Abraham dares one last step.",
        "must_show": "the last daring — Abraham gathering himself for the final rung: hands pressed together, the number TEN forming; the boldest smallness.",
        "must_not_show": "ABSOLUTE: no figure; the gathering VISIBLE — a man spending his last courage.",
        "scene": (
            "One rung remains and the "
            "old man gathers for it: "
            "hands pressed together "
            "at his breast, the white "
            "head bowing, breath "
            "drawn slow — the number "
            "TEN forming behind his "
            "lips like the last coin "
            "in a purse — every "
            "descent so far granted, "
            "and still this one feels "
            "like standing at a "
            "cliff's lip: to ask the "
            "Judge of all the earth "
            "to hang a whole plain's "
            "fate on ten — and he "
            "dares it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r114-b17", "out": "s17-oh-let-not-the-lord.jpeg", "seg": "s32",
        "window": "88.90-95.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": (
            "Oh let not the Lord be angry, and I will speak yet but this "
            "once: Peradventure ten shall be found there."
        ),
        "must_show": "SCRIPTURE-EXACT: the last plea — close on Abraham's face at maximum reverent daring: LET NOT THE LORD BE ANGRY... PERADVENTURE TEN; everything in the asking.",
        "must_not_show": "ABSOLUTE: no figure; the reverence and the daring BOTH at full strength.",
        "scene": (
            "The last plea goes up with "
            "both its hands showing: "
            "OH LET NOT THE LORD BE "
            "ANGRY — the reverence "
            "laid down first, real "
            "and trembling — AND I "
            "WILL SPEAK YET BUT THIS "
            "ONCE — the old face "
            "lifted full into the "
            "warm light with its "
            "final number held out "
            "like bread in famine — "
            "PERADVENTURE TEN — ten "
            "decent souls in two "
            "cities, the smallest "
            "handhold mercy has ever "
            "been asked to hang a "
            "plain on. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r114-b18", "out": "s18-i-will-not-destroy-it.jpeg", "seg": "jv32",
        "window": "96.86-99.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT", "ABRAHAM"],
        "narration": "I will not destroy it for ten's sake.",
        "must_show": "SCRIPTURE-EXACT: the tenth yes — the ridge at its stillest: the answer given over the whole gold landscape; Abraham bowed in the warm light, the plain held under the final mercy.",
        "must_not_show": "ABSOLUTE: no figure; the stillness the register — the ladder's last rung, granted.",
        "scene": (
            "And the tenth yes settles "
            "over everything: I WILL "
            "NOT DESTROY IT — FOR "
            "TEN'S SAKE — the words "
            "moving out over the gold "
            "ridge and the darkened "
            "plain and the small far "
            "cities all at once, and "
            "the old man bowing slowly "
            "into the warm light "
            "until his beard touches "
            "his breast — the boldest "
            "negotiation in scripture "
            "ended the only way it "
            "was ever going to end: "
            "with mercy having said "
            "yes at every single "
            "rung. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r114-b19", "out": "s19-let-me-speak-just-once.jpeg", "seg": "n6b",
        "window": "100.62-104.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["ABRAHAM"],
        "narration": (
            "Let me speak just once more, Abraham said. What if there are "
            "only ten?"
        ),
        "must_show": "the once-more held — Abraham's pleading hands open at ten fingers in the gold light; the number itself displayed; humility and hope in one gesture.",
        "must_not_show": "ABSOLUTE: no figure; TEN literal on his two spread hands.",
        "scene": (
            "The final number stands "
            "up on his own two hands: "
            "ten fingers spread open "
            "in the warm gold light — "
            "the entire remaining "
            "case for two cities held "
            "up in the oldest counting "
            "frame there is — JUST "
            "ONCE MORE, the humble "
            "preface, and then the "
            "hands themselves doing "
            "the asking: this many; "
            "only this many; would "
            "this many be enough — "
            "an old man's open hands, "
            "pleading a plain's whole "
            "case. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r114-b20", "out": "s20-for-the-sake-of-ten.jpeg", "seg": "n7",
        "window": "105.42-112.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT"],
        "narration": (
            "For the sake of ten good people, the whole place would be "
            "spared. That is the God Abraham found at the top of that hill."
        ),
        "must_show": "the found God — the ridge-top in full gold: the warm presence-light standing over the sweeping view; the hill remembered as the place mercy was discovered.",
        "must_not_show": "ABSOLUTE: no figure, no fire — the hilltop as a landmark of discovery, lit whole.",
        "scene": (
            "The hilltop becomes a "
            "landmark while you watch: "
            "the bare gold ridge with "
            "the warm presence-light "
            "standing over its whole "
            "sweep of world — plain, "
            "cities, darkening sky and "
            "all — the exact patch of "
            "ground where a man "
            "climbed down a ladder of "
            "questions and found, at "
            "every rung, the same "
            "astonishing floor: a God "
            "who would spare a whole "
            "corrupt plain for ten "
            "decent strangers — found "
            "here, at the top of "
            "this hill, by asking. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r114-b21", "out": "s21-not-one-straining-to-condemn.jpeg", "seg": "n7",
        "window": "112.23-118.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT"],
        "narration": (
            "Not one straining to condemn — one who could be talked, again "
            "and again, toward mercy."
        ),
        "must_show": "the character summarized — the warm light at rest on the ridge in the last gold: nothing coiled or striking in it; approachability as atmosphere.",
        "must_not_show": "ABSOLUTE: no figure; NOTHING severe in the light — rest, warmth, openness to being asked.",
        "scene": (
            "The frame takes the "
            "light's character portrait: "
            "warm gold at rest on the "
            "bare ridge in the day's "
            "last honey — nothing "
            "coiled in it, nothing "
            "strained toward striking, "
            "no thunder held back at "
            "cost — just an openness "
            "with room in it for the "
            "next question, and the "
            "next, and the one after "
            "that — the kind of "
            "presence an old man "
            "could stand before for "
            "an afternoon, arguing "
            "for strangers, and leave "
            "loving more than when "
            "he came. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r114-b22", "out": "s22-abraham-went-home-in-the.jpeg", "seg": "n8",
        "window": "118.67-125.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMP", "ABRAHAM"],
        "narration": (
            "Abraham went home in the dusk, amazed. He had dared to plead "
            "for strangers, and found God kinder than he had hoped."
        ),
        "must_show": "SCRIPTURE-EXACT: the return (v33) — Abraham walking home down the dusk path toward the tent and oak, lamplit now; amazement carried in the slow shaking of his head.",
        "must_not_show": "ABSOLUTE: no figure of God; the walk WONDERING — a man replaying the afternoon.",
        "scene": (
            "Home through the blue dusk "
            "the pleader walks his "
            "amazement: the black tent "
            "warm with lamplight under "
            "the great oak ahead, the "
            "path soft underfoot — and "
            "the old man coming down "
            "it slow, shaking his "
            "white head over and over "
            "at the day: he argued "
            "with the Judge of all "
            "the earth till dusk, for "
            "people he never met — "
            "and lost not one round, "
            "because the Judge kept "
            "taking his side. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r114-b23", "out": "s23-god-let-a-man-argue.jpeg", "seg": "n8",
        "window": "125.61-129.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["HEIGHT"],
        "narration": "God let a man argue with him — and kept saying yes.",
        "must_show": "the closing image — the empty ridge-top in last light: the place of the argument holding its gold; the standing invitation of the spot itself.",
        "must_not_show": "ABSOLUTE: no figure; the emptiness INVITING — the negotiating ground left open for the next bold pleader.",
        "scene": (
            "The closing frame keeps "
            "the negotiating ground: "
            "the bare ridge-top empty "
            "in the last of the gold, "
            "the plain darkening "
            "below, the worn spot "
            "where an old man stood "
            "his afternoon still "
            "holding the warmth — a "
            "courtroom with no walls "
            "where a creature argued "
            "the Creator toward mercy "
            "and heard yes ten times "
            "running — left open on "
            "the hilltop like a "
            "standing appointment, "
            "for whoever dares to "
            "plead next. Every figure "
            "has two arms, two hands "
            "and one head."
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
