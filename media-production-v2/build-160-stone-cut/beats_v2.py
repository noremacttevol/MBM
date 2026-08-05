#!/usr/bin/env python3
"""V2 beat map — row 160, build-160-stone-cut (Daniel 2:31-45).

COVERAGE: 21 pictures over 145.9 s = 6.9 s/picture (matches the library density).

SCRIPTURE FACTS (Daniel 2 KJV):
  2:31-33 the GREAT IMAGE: head of fine GOLD, breast and arms of
        SILVER, belly and thighs of BRASS, legs of IRON, feet part
        IRON part CLAY. "This great image... the form thereof was
        terrible."
  2:34  "a stone was cut out WITHOUT HANDS, which smote the image
        upon his FEET."
  2:35  "...broken to pieces together, and became like the CHAFF of
        the summer threshingfloors; and the WIND carried them away,
        that NO PLACE was found for them: and the stone... became a
        GREAT MOUNTAIN, and FILLED THE WHOLE EARTH."
  2:44  "the God of heaven shall set up a kingdom, which shall
        NEVER be destroyed... it shall stand for ever."
  2:45  "the stone was cut out of the mountain WITHOUT HANDS."

ROW INTENT: the unstoppable-kingdom row (BRIDGE) — every human
empire falls; God's kingdom, not made by men, cannot be unmade by
them, and it grows until it fills the earth. The close offers the
viewer belonging in it.

RENDERING LAWS:
  - WITHOUT HANDS (absolute — the 157 opening-law pattern): the
    stone is NEVER touched by any hand, chisel, tool, workman or
    army, in ANY frame. It breaks free alone (b08), strikes alone
    (b09), grows alone (b11/b12). Any depicted cutting mechanism,
    hand or figure at the stone = reject. b07 is the doctrine
    insert: the clean fresh break-socket in the mountainside with
    the slope EMPTY of anyone.
  - TWO WORLDS, never mixed: the COURT frames (b01/b02/b13/b16)
    are lamplit Babylonian throne-hall; the DREAM frames
    (b03-b12, b14/b15, b17-b21) live on the vast dream plain /
    mountain — still, enormous, wind-swept air. No court figure
    ever stands in the dream; the dream is never a wall-painting
    or vision-bubble inside the court.
  - THE STATUE is a STATUE — its shattering harms nobody; NO
    people, NO armies anywhere on the dream plain. "Dazzling and
    terrible" = scale and glare, never a face of horror.
  - GOD IS NEVER EMBODIED; no divine hand even at the cutting —
    that is the entire point of the row.
  - THE KING's trouble is dignified sleeplessness, never
    caricature; the wise men's failure (b01) is a felt absence in
    the hall, not mocked men.
  - DANIEL is a young exile (~25) — calm, clear-eyed, plainly
    dressed among Babylon's splendour; he explains, never gloats.
  - THE STONE stays UNHEWN — rough natural grey rock, visibly
    tool-markless at every size, from boulder to mountain.

TIME OF DAY ARC (intentional): the court at deep lamplit night (a
troubled-dream story); the dream plain in vast amber twilight; the
collapse in the same twilight with wind; the mountain frames
climbing toward clear morning; the close in full dawn.

CHANGING CONDITIONS (kept OUT of the locks): the stone — socketed,
freed, striking, grown, mountain; the statue — towering, struck,
dust; the plain — still, then wind-swept, then green at the
mountain's spread.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "DANIEL": (
        "DANIEL LOCK: Daniel is the same man in every shot — a "
        "young Judean exile of about twenty-five: clear steady dark "
        "eyes, short dark beard, composed intelligent face; a plain "
        "undyed DARK SLATE-GREY robe with a simple dark sash "
        "(never cream, never court finery) — visibly the plainest "
        "man in any Babylonian room he stands in."
    ),
    "KING": (
        "KING LOCK: the king of Babylon is the same man in every "
        "shot — a powerfully built monarch of about fifty: heavy "
        "black square-curled Babylonian beard, deep-set weary dark "
        "eyes, gold circlet crown; layered robes of DEEP ROYAL BLUE "
        "and purple with gold thread (never cream). His trouble is "
        "sleepless gravity, never weakness."
    ),
    "COURT": (
        "COURT LOCK: the Babylonian throne hall — glazed brick "
        "walls of deep blue with gold reliefs, massive columns, "
        "bronze oil-lamps burning low, the raised throne dais; "
        "deep lamplit night throughout. The same hall every court "
        "frame."
    ),
    "STATUE": (
        "STATUE LOCK: the dream image — one colossal standing "
        "statue on the dream plain, dazzling and terrible: head of "
        "polished GOLD, chest and arms of SILVER, belly and thighs "
        "of BRONZE, legs of dark IRON, feet of iron marbled with "
        "crumbling grey CLAY; rigid, expressionless, enormous. The "
        "same statue, same metals in the same order, every frame "
        "until it falls."
    ),
    "STONE": (
        "STONE LOCK: the stone — rough NATURAL grey rock, UNHEWN, "
        "with no tool mark, chisel line or worked face at any "
        "size; the same grey stone whether boulder or mountain. "
        "Never touched by any hand or tool in any frame."
    ),
    "DREAM-PLAIN": (
        "DREAM-PLAIN LOCK: the dream's world — a vast level plain "
        "under enormous amber twilight sky, a great dark mountain "
        "range far at one edge; still monumental air, no "
        "buildings, no people anywhere. The same plain and range "
        "every dream frame."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r160-b01", "out": "s01-the-king-of-babylon-had.jpeg", "seg": "n1",
        "window": "0.28-6.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["KING", "COURT"],
        "narration": (
            "The king of Babylon had a dream that troubled him deeply, and "
            "none of his wise men could tell him what it meant."
        ),
        "must_show": "the ONE court wide — camera low at the hall's far end looking down the column row to the dais: the king seated forward on his throne, brow in hand, lamps burned low; the space before the dais conspicuously EMPTY where answers should be standing.",
        "must_not_show": "no wise men rendered as fools — their failure is the EMPTY floor; the king's trouble dignified, never weak; deep lamplit night.",
        "scene": (
            "The hall answers with silence, the camera set "
            "low at the throne room's far end with the columns' backs "
            "nearest the lens, so the blue "
            "glazed columns march away toward the dais and every "
            "line of the room exits at the frame's far centre: the "
            "king of Babylon sits far forward on his "
            "throne in the low lamplight, crown heavy, "
            "brow pressed into one hand — a man whose "
            "sleep has been taken from him by something he "
            "saw in it — and the wide floor before the "
            "dais, where a court's worth of wise men "
            "should be standing with answers, holds "
            "nothing at all but lamplight. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b02", "out": "s02-so-a-young-exile-named.jpeg", "seg": "n1",
        "window": "6.51-11.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["DANIEL", "KING", "COURT"],
        "narration": (
            "So a young exile named Daniel, who served the God of heaven, "
            "was brought in to explain it."
        ),
        "must_show": "the arrival — over the king's shoulder from the dais: Daniel walking up the lamplit hall toward the throne, plain slate-grey robe among the splendour, calm and unafraid.",
        "must_not_show": "no guards manhandling him — brought in, not dragged; his plainness against the hall's gold must read.",
        "scene": (
            "The answer arrives in the plainest robe in "
            "Babylon: over the king's massive shoulder the "
            "frame looks down the hall as Daniel comes up "
            "the long lamplit floor alone — a young exile "
            "in undyed slate-grey among all that blue "
            "glaze and gold relief, steps unhurried, face "
            "calm with the composure of a man who serves "
            "a God who does not lose sleep — brought in to "
            "explain what all the kingdom's wisdom could "
            "not touch. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r160-b03", "out": "s03-in-the-dream-the-king.jpeg", "seg": "n2",
        "window": "12.06-24.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["STATUE", "DREAM-PLAIN"],
        "narration": (
            "In the dream, the king had seen an enormous statue, dazzling "
            "and terrible — a head of gold, chest of silver, belly of "
            "bronze, legs of iron, and feet of iron mixed with crumbling "
            "clay."
        ),
        "must_show": "the image entire — the colossal statue standing full-height on the dream plain, all four metals in order top to bottom, the clay-marbled feet readable at its base; dazzling scale, rigid stillness.",
        "must_not_show": "ABSOLUTE: metals in the stated order, never shuffled; no face of horror — 'terrible' is SCALE and glare; no people anywhere on the plain.",
        "scene": (
            "The dream stands up to its full height: on "
            "the vast amber plain the statue rises "
            "enormous and rigid against the twilight sky — "
            "the head burning polished gold at the top of "
            "it, silver chest and arms below, the belly's "
            "burnished bronze band, dark iron legs like towers, and "
            "down at the base, where the whole weight "
            "lands, feet of iron marbled through with dull "
            "crumbling grey clay — dazzling and terrible "
            "by sheer size alone, still as only a made "
            "thing can be. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r160-b04", "out": "s04-it-stood-for-the-great.jpeg", "seg": "n2",
        "window": "24.89-29.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["STATUE", "DREAM-PLAIN"],
        "narration": "It stood for the great kingdoms of the world, one after another.",
        "must_show": "the meaning frame — the statue from ground level at its clay-iron feet looking UP its towering height, each metal band stacked on the one below; empire on empire, read vertically.",
        "must_not_show": "no armies, banners or map imagery — the stacked metals ARE the kingdoms; the vulnerable feet nearest the camera.",
        "scene": (
            "What it means is how it is stacked: the "
            "camera drops to the dream plain's floor at "
            "the statue's feet and looks straight up the "
            "impossible height of it — clay-and-iron feet "
            "hugest and nearest, then the dark iron legs, "
            "the bronze, the silver, the far small blaze "
            "of the golden head against the sky — kingdom "
            "standing on kingdom, one after another, the "
            "whole tower of human empire resting its "
            "entire weight on the crumbling mix at the "
            "bottom. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r160-b05", "out": "s05-and-then-in-the-dream.jpeg", "seg": "n3",
        "window": "29.92-33.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["DREAM-PLAIN"],
        "narration": "And then, in the dream, something small appeared.",
        "must_show": "the turn — the far dark mountain range across the plain, and on one high slope a SMALL pale point of fresh-broken stone catching the light; tiny against the vastness; the statue out of frame or a far silhouette.",
        "must_not_show": "nothing dramatic yet — smallness is the sentence; no hands, no figures on the mountain.",
        "scene": (
            "The dream turns on something almost too small "
            "to notice: across the whole width of the amber "
            "plain the far mountain range lies dark against "
            "the sky, and high on one slope a single pale "
            "point has appeared — fresh stone catching the "
            "twilight where everything around it is old and "
            "dark — small the way a seed is small, nothing "
            "beside the towering glare of metal far behind "
            "the camera, and the only thing in the dream "
            "that is new. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r160-b06", "out": "s06-a-single-stone-cut-out.jpeg", "seg": "n3",
        "window": "33.88-39.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "A single stone, cut out of a mountain — but cut by no human "
            "hand."
        ),
        "must_show": "the cutting-as-result — closer on the mountainside: the rough grey stone standing FREE of the slope beside its fresh break-line, the parting CLEAN and new; NO hand, tool or figure anywhere; the separation already accomplished.",
        "must_not_show": "ABSOLUTE: no hands, no chisel, no workman, no mechanism, no divine hand — the freed stone and the fresh break carry it entirely.",
        "scene": (
            "The impossible thing is shown already done: "
            "close on the high mountainside where the "
            "rough grey stone now stands FREE — clear of "
            "the living rock, a fresh pale break-line "
            "running down the slope behind it where the "
            "two were one a moment ago — and the whole "
            "slope around it is empty, no scaffold, no "
            "tool, no climber, nothing with hands on the "
            "entire mountain: cut out, with the cutting "
            "itself belonging to no one the dream can "
            "show. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r160-b07", "out": "s07-no-chisel-no-workman-no.jpeg", "seg": "n3",
        "window": "39.13-41.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE"],
        "narration": "No chisel, no workman, no army.",
        "must_show": "the doctrine insert — tight on the fresh break-socket in the mountainside: raw clean rock face, NO tool marks, and the empty slope around it; absence as the whole picture.",
        "must_not_show": "ABSOLUTE: not one tool mark, chisel line, rope, ladder or footprint — the insert exists to prove the absence.",
        "scene": (
            "Three absences, photographed: tight on the "
            "socket the stone left in the mountain — raw "
            "fresh rock in a clean parting, its face "
            "unmarked by any chisel line, the ledges "
            "around it bare of any workman's ladder or "
            "rope, the slope below printed by no army's "
            "ten thousand feet — a cut with no cutter "
            "anywhere in the world of the dream, which is "
            "exactly what the dream wants remembered. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r160-b08", "out": "s08-it-simply-broke-free-all.jpeg", "seg": "n3",
        "window": "41.63-44.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": "It simply broke free, all on its own.",
        "must_show": "the motion — the stone mid-descent down the empty mountainside, dust and small rock kicking behind it, moving under its own weight and will; travel direction toward frame-RIGHT (the statue's side).",
        "must_not_show": "no pusher, no launcher, no hand — alone; the motion READABLE (kicked dust, tumbled trail behind it).",
        "scene": (
            "And then it moves: the grey stone comes down "
            "the mountainside on its own — bounding heavy "
            "and certain through the twilight, a trail of "
            "kicked dust and scattered small rock rising "
            "behind it to prove the speed, the empty slope "
            "streaming past — no one pushed, no one aimed, "
            "nothing on the mountain but the stone itself "
            "and the direction it has chosen, rightward "
            "across the frame toward the far glare of "
            "metal on the plain. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b09", "out": "s09-forasmuch-as-thou-sawest-that.jpeg", "seg": "kv45",
        "window": "45.20-62.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "STATUE", "DREAM-PLAIN"],
        "narration": (
            "Forasmuch as thou sawest that the stone was cut out of the "
            "mountain without hands, and that it brake in pieces the iron, "
            "the brass, the clay, the silver, and the gold; the great God "
            "hath made known to the king what shall come to pass hereafter: "
            "and the dream is certain, and the interpretation thereof sure."
        ),
        "must_show": "SCRIPTURE-EXACT: the strike — the instant the stone meets the statue's iron-and-clay FEET: impact at the base, the first web of cracks leaping up the iron legs, the colossus's dazzling height above already doomed; the stone small, the effect total.",
        "must_not_show": "ABSOLUTE: it strikes the FEET, never the head or chest; no hand guides it; no people near; the statue harms nobody as it begins to go.",
        "scene": (
            "The small thing meets the great thing exactly "
            "where the dream said: at the statue's base the "
            "grey stone strikes the iron-and-clay feet — "
            "the impact caught at the instant of contact, "
            "clay bursting to powder at the point of the "
            "blow, a web of bright cracks already leaping "
            "up the dark iron legs toward all that silver "
            "and gold towering dazzling and doomed above — "
            "one unhewn stone against the whole stacked "
            "weight of empire, and it is the empire that "
            "is giving way. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b10", "out": "s10-that-little-stone-made-by.jpeg", "seg": "n4",
        "window": "64.29-78.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "That little stone, made by God and not by men, struck the great "
            "statue at its feet — and the whole towering thing came crashing "
            "down, shattered to dust, and blew away on the wind like chaff, "
            "until not a trace was left."
        ),
        "must_show": "the collapse — the statue mid-fall in ruin: gold, silver, bronze and iron breaking downward together into a rising cloud, and the wind ALREADY streaming the dust away across the plain; the stone standing untouched in the foreground.",
        "must_not_show": "no people harmed or present; the dust STREAMS AWAY on wind (the chaff clause must read); the stone unchipped, unmoved.",
        "scene": (
            "The whole tower of empire comes down at "
            "once: gold head, silver chest, bronze and "
            "iron folding downward into each other in a "
            "single roaring ruin, the metals losing their "
            "order and then their shapes and then "
            "everything but dust — and the twilight wind "
            "is already at work, streaming the pale cloud "
            "away across the empty plain like chaff off a "
            "summer threshing-floor, unmaking even the "
            "memory of where it stood — while in the "
            "foreground the little grey stone sits "
            "untouched, unchipped, finished with its one "
            "blow. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r160-b11", "out": "s11-but-the-stone-did-not.jpeg", "seg": "n5",
        "window": "79.42-81.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": "But the stone did not stop. It began to grow.",
        "must_show": "the growth begun — the stone alone on the swept-clean plain, now visibly LARGER than the boulder that struck — house-sized, its rough unhewn faces the same; the last dust thinning on the horizon.",
        "must_not_show": "no hands, no builders — it grows ALONE; unhewn surfaces at the new size; no trace of the statue anywhere.",
        "scene": (
            "The plain is clean and the stone is not "
            "finished: where the colossus stood there is "
            "nothing now but level twilight ground and "
            "the last pale thinning of dust on the "
            "horizon — and the grey stone, alone in all "
            "that emptiness, is LARGER — house-high "
            "already, its rough faces unmistakably the "
            "same unhewn rock, swelling with a slow "
            "living purpose that no quarry ever gave a "
            "stone — not stopping, only beginning. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b12", "out": "s12-it-became-a-mountain-and.jpeg", "seg": "n5",
        "window": "81.89-88.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "It became a mountain, and then a greater mountain, until it "
            "filled the whole earth, from one end of it to the other."
        ),
        "must_show": "the filling — the stone become a MOUNTAIN spanning the entire frame edge to edge, its skirts running past both borders, first morning light finding its high faces; the old far range dwarfed or gone.",
        "must_not_show": "no summit temple, city or crown — a MOUNTAIN, natural and unhewn at every scale; it must touch BOTH frame edges (fills the earth).",
        "scene": (
            "And it does not stop being a stone so much as "
            "the earth stops being anything else: mountain "
            "now — a grey unhewn immensity climbing out of "
            "the plain into the first true morning light, "
            "its rock shoulders running clean past both "
            "edges of the frame so that no end of it can "
            "be seen, its high faces catching dawn while "
            "its skirts fill every horizon — from one end "
            "of the earth to the other, one stone, still "
            "growing when the frame gives out. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b13", "out": "s13-daniel-told-the-king-what.jpeg", "seg": "n6",
        "window": "88.94-91.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["DANIEL", "KING", "COURT"],
        "narration": "Daniel told the king what it meant.",
        "must_show": "the telling — a two-shot at the lamplit dais: Daniel standing calm before the seated king, mid-explanation, one hand open; the king leaning in, listening hard.",
        "must_not_show": "no gloating on Daniel, no fear — calm service; the king LISTENING, his weariness giving way to attention.",
        "scene": (
            "Back in the lamplit hall the dream gets its "
            "voice: Daniel stands before the dais in his "
            "plain slate-grey, one hand open midway "
            "through the telling, face calm as still "
            "water — and the king of Babylon, who has not "
            "truly slept since he saw it, leans forward "
            "off his throne toward the young exile, crown "
            "and gold thread forgotten, because the "
            "plainest man in the room is the only one "
            "holding what he needs. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b14", "out": "s14-every-human-empire-however-golden.jpeg", "seg": "n6",
        "window": "91.15-96.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["DREAM-PLAIN"],
        "narration": (
            "Every human empire, however golden, would rise and then fall "
            "and be forgotten."
        ),
        "must_show": "the forgetting insert — back in the dream: the great GOLD HEAD alone, half-buried and tipped in the plain's pale dust, its dazzle gone matte; wind moving the dust across it.",
        "must_not_show": "no skulls, ruins-of-war or bodies — one half-buried golden head carries all of it; the dust actively drifting (being forgotten, present tense).",
        "scene": (
            "What becomes of golden: in the dream's "
            "emptiness the great head lies alone where the "
            "wind is burying it — tipped on one cheek in "
            "the pale dust, the polish that once burned "
            "against the sky gone matte under a drifting "
            "skin of grey, dust moving across the "
            "enormous still face in slow ropes with every "
            "gust — however golden, going the way of "
            "everything men stack up: down, and then "
            "under, and then out of mind. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b15", "out": "s15-but-god-himself-would-set.jpeg", "seg": "n6",
        "window": "96.08-101.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "But God himself would set up a kingdom of his own, and that one "
            "would be different."
        ),
        "must_show": "the different one — the stone-mountain in morning light rising beyond the dust-plain where the head lies buried small in the foreground distance; living rock against dead metal, one frame, the contrast exact.",
        "must_not_show": "GOD NEVER EMBODIED — the mountain is the kingdom's whole image; the buried head SMALL and far, the mountain dominant.",
        "scene": (
            "Different is visible from here: low across "
            "the pale dust-plain the frame finds the "
            "half-buried glint of the golden head, small "
            "now and losing to the wind — and beyond it, "
            "filling the morning sky, the grey mountain "
            "stands in clean early light, rock where the "
            "other was metal, grown where the other was "
            "built, standing where the other is being "
            "erased — a kingdom set up by no council and "
            "no chisel, and so unlike every kingdom the "
            "plain has ever carried. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b16", "out": "s16-and-in-the-days-of.jpeg", "seg": "kv44",
        "window": "101.88-115.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["DANIEL", "KING", "COURT"],
        "narration": (
            "And in the days of these kings shall the God of heaven set up a "
            "kingdom, which shall never be destroyed: and the kingdom shall "
            "not be left to other people, but it shall break in pieces and "
            "consume all these kingdoms, and it shall stand forever."
        ),
        "must_show": "SCRIPTURE-EXACT: the declaration — Daniel before the dais at full conviction, one hand lifted with the words, eyes steady on the king; the king gripping his throne's arm, hearing a verdict on every crown including his own.",
        "must_not_show": "no gloating, no fear — Daniel serene, the king SOBERED not humiliated; lamplight; no dream imagery mixed into the hall.",
        "scene": (
            "The interpretation arrives at its summit: "
            "Daniel's hand comes up with the words — a "
            "kingdom the God of heaven himself will set "
            "up, never destroyed, never handed on, "
            "standing forever — his voice quiet and "
            "level and completely certain in the lamplit "
            "hall, and the king's hand closes slowly on "
            "the arm of his throne as he takes it in: a "
            "verdict on every crown in the world, "
            "delivered kindly, by the plainest man in "
            "Babylon. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r160-b17", "out": "s17-never-handed-off-to-someone.jpeg", "seg": "n7",
        "window": "116.81-118.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": "Never handed off to someone else.",
        "must_show": "the permanence insert — the mountain's high grey shoulder against clear morning sky, massive, unmoved, held by no one; simply THERE.",
        "must_not_show": "no flags, thrones or claimants on it — un-handed-off means nobody's banner flies there.",
        "scene": (
            "Four words against the sky: the mountain's "
            "high grey shoulder stands in the clear "
            "morning, enormous and unadorned — no banner "
            "planted on it, no throne cut into it, no "
            "successor's mark anywhere on the living "
            "rock — a kingdom that changes hands never, "
            "because the hands it belongs to are not the "
            "kind that let go. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b18", "out": "s18-not-built-by-human-hands.jpeg", "seg": "n7",
        "window": "118.72-128.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "Not built by human hands, and so not able to be torn down by "
            "them either — a kingdom cut from the mountain of God, that "
            "would outlast every throne on earth and stand forever."
        ),
        "must_show": "the doctrine landscape — the whole mountain serene in morning light filling the high frame, and low in the far dust the LAST faint traces of the statue's metals almost gone; outlasting, in one look.",
        "must_not_show": "ABSOLUTE: no tool mark on any rock face (the b07 rhyme at mountain scale); the metal traces FAINT — nearly finished being forgotten.",
        "scene": (
            "The logic of it fills one landscape: what no "
            "hands raised, no hands can pull down — the "
            "mountain standing serene and entire in the "
            "morning light, every face of it unhewn, not "
            "one chisel line on all that living grey — "
            "while far below in the old dust the last "
            "faint glints of gold and iron are nearly "
            "done disappearing, every throne's ending "
            "already written in the wind that carries "
            "them — and the rock stands on, with forever "
            "ahead of it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r160-b19", "out": "s19-so-this-ancient-dream-is.jpeg", "seg": "n8",
        "window": "129.30-133.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "So this ancient dream is really a promise you can build your "
            "life on."
        ),
        "must_show": "the promise made personal — at the mountain's foot in warm dawn, one open flat shelf of the unhewn rock in the foreground: solid, level, sunlit — foundation offered; nobody in frame.",
        "must_not_show": "no figure yet — the sunlit rock shelf IS the offer; no tool marks; warmth, not grandeur.",
        "scene": (
            "The dream comes down to where a life could "
            "stand: at the mountain's foot the dawn finds "
            "one broad shelf of the unhewn rock — level, "
            "solid, warm-lit, wide enough to build on — "
            "the immensity above it going up out of frame "
            "and this one human-sized ledge offered in "
            "the foreground: ancient dream, present "
            "promise, ground that will still be here "
            "after every other ground has gone. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b20", "out": "s20-the-kingdoms-of-men-come.jpeg", "seg": "n8",
        "window": "133.35-139.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "The kingdoms of men come and go, but God is setting up one that "
            "never ends — a stone that fills the whole earth."
        ),
        "must_show": "the summary wide-feeling frame — the mountain edge-to-edge under full dawn, its green lower slopes catching life, the sky gold; the plain's dust finally empty of every trace; permanence as morning.",
        "must_not_show": "no remaining metal glint anywhere — 'not a trace' is now fully true; the mountain touches both frame edges again.",
        "scene": (
            "Morning settles the whole question: the "
            "mountain runs from one edge of the frame to "
            "the other under a full gold dawn, its lower "
            "slopes taking the first green of living "
            "things, the plain before it swept clean at "
            "last of every glint the empires left — the "
            "kingdoms of men gone the way of their dust, "
            "and the one that never ends standing into "
            "the light, still filling, still the whole "
            "earth's horizon. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r160-b21", "out": "s21-when-that-kingdom-is-offered.jpeg", "seg": "n8",
        "window": "139.93-145.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["STONE", "DREAM-PLAIN"],
        "narration": (
            "So the only question is a hopeful one. When that kingdom is "
            "offered to you, will you belong to it?"
        ),
        "must_show": "the closing invitation — a small unwalked path beginning at the frame's bottom edge and climbing gently onto the mountain's green lower slope in morning light; the way in, offered to the viewer; nobody on it.",
        "must_not_show": "no gate, no figure, no signage — an open path only; it must START at the viewer's edge of the frame (the offer is to YOU).",
        "scene": (
            "The last frame leaves the viewer standing at "
            "a beginning: from the very bottom edge of "
            "the picture a small footpath sets off "
            "through the dawn grass — unwalked, unfenced, "
            "open — and climbs gently up onto the "
            "mountain's green lower slope, into the "
            "morning light going up the immense grey "
            "shoulders beyond — a kingdom that cannot "
            "fall, with a way in that starts exactly "
            "where you are standing — offered: will you "
            "belong to it? Every figure has two arms, "
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
