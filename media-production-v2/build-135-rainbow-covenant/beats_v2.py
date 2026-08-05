#!/usr/bin/env python3
"""V2 beat map — row 135, build-135-rainbow-covenant (Genesis 8-9).

COVERAGE: 44 pictures over 250.2 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Genesis KJV):
  8:4   the ark RESTED "upon the mountains of Ararat."
  8:18-20 Noah went forth — EIGHT people (Noah, his wife, his THREE
        sons, their THREE wives) — "and Noah builded an ALTAR unto
        the LORD... and offered burnt offerings."
  8:22  "While the earth remaineth, SEEDTIME and HARVEST, and COLD
        and HEAT, and SUMMER and WINTER, and DAY and NIGHT shall not
        cease."
  9:1   "Be fruitful, and multiply, and replenish the earth."
  9:9-11 "I establish my covenant WITH YOU, and with your seed...
        neither shall all flesh be cut off any more by the waters of
        a flood."
  9:13  "I do set my BOW in the cloud" — the Hebrew word is the
        BATTLE-BOW; hung unstrung, aimed away.
  9:16  "the bow shall be in the cloud; and I WILL LOOK UPON IT,
        that I MAY REMEMBER" — the sign is set where GOD sees it.

RENDERING LAWS:
  - THE EIGHT ARE ALWAYS EIGHT (this row's own complaint class —
    counts): Noah, his wife, three sons, three wives. Count them in
    EVERY family frame. Noah: ~600-storied as aged — render as a
    vigorous white-bearded elder; the sons grown men; the wives
    distinct women. Same eight faces throughout.
  - GOD IS NEVER EMBODIED — the voice and covenant come over sky
    and altar-smoke; no figure, ever (scripture-hides class).
  - THE DROWNED WORLD IS AFTERMATH ONLY: washed-bare valleys, mud
    flats drying, stranded driftwood and waterlines on the hills —
    NEVER bodies, NEVER human wreckage. The horror is over before
    frame one; the earth is clean, quiet, and new.
  - THE BOW is the row's doctrine-image: b31-b33 render an actual
    unstrung BATTLE-BOW hung on a wall (the warrior retiring his
    weapon), then the rainbow as the same shape in cloud — aimed
    AWAY from the earth (arc opening downward-away, per the verse's
    logic). Never a war scene.
  - The rainbow is painted REAL — a true arc in washed light after
    rain; no sparkle effects, no double-exaggeration.
  - Animals: orderly pairs leaving the ark, natural species, calm.

TIME OF DAY ARC (intentional): the stilled-ark morning in silver
post-rain light; the disembarking and blessing in washed clean
morning; the altar at golden afternoon, smoke straight; the fear-of
-clouds beat under REAL returning grey (deliberate); the covenant
and bow in break-light — sun through parting cloud; the closing
frames in full warm light with the bow high.

CHANGING CONDITION (kept OUT of the locks): the sky — silver, then
threatening grey (once, b17-b19), then break-light with the bow;
the altar — unbuilt, building, smoking.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "ARK": (
        "ARK LOCK: the ark — a vast weathered gopher-wood vessel, "
        "high-sided and barn-like with one great door in its flank, "
        "aground and tilted slightly on a green mountain shoulder. "
        "The same vessel and resting place throughout."
    ),
    "FAMILY": (
        "FAMILY LOCK: the eight — EXACTLY EIGHT people in every "
        "family shot, never more, never fewer: NOAH, a vigorous "
        "white-bearded elder in a DEEP UMBER robe; his WIFE, aged "
        "and steady in DARK MOSS-GREEN; THREE grown SONS with dark "
        "beards in rust, slate-blue and brown tunics; THREE WIVES, "
        "distinct women in olive, madder and charcoal dresses. No "
        "cream anywhere. The same eight faces throughout."
    ),
    "MOUNTAIN": (
        "MOUNTAIN LOCK: the new world — the green mountain shoulder "
        "below the ark, washed valleys falling away in terraces of "
        "drying mud flats and fresh grass, waterlines faint on the "
        "far hills, stranded silver driftwood; clean, quiet, empty "
        "of all other people. The same slopes throughout."
    ),
    "ALTAR": (
        "ALTAR LOCK: Noah's altar — a low ring-stacked altar of "
        "rough field stones on the open slope near the ark, its "
        "smoke rising thin and STRAIGHT. The same altar throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r135-b01", "out": "s01-the-rain-had-stopped.jpeg", "seg": "n1",
        "window": "0.28-1.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "The rain had stopped.",
        "must_show": "the stopping — the washed world under a silver clearing sky, the last drops falling from leaves, stillness arriving; the first quiet in a year.",
        "must_not_show": "ABSOLUTE: no bodies, no human wreckage — clean washed earth and silver light only.",
        "scene": (
            "The loudest year in history ends in three words of "
            "quiet: the silver morning hangs still over washed "
            "green slopes, the last raindrops letting go of "
            "leaf-tips one by one into the hush, thin mist "
            "standing in the valleys like breath — no thunder "
            "anywhere, no drumming on wood, no sound at all "
            "except water finishing — the rain, after "
            "everything, simply stopped. No people are in this "
            "frame."
        ),
    },
    {
        "id": "v2-r135-b02", "out": "s02-here-is-the-first-thing.jpeg", "seg": "n3",
        "window": "50.72-53.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["ALTAR", "FAMILY", "MOUNTAIN"],
        "narration": "Here is the first thing Noah built in the new world.",
        "must_show": "the first building — Noah setting a field stone onto the low ring of the altar-in-progress, the seven others near; the new world's first construction project.",
        "must_not_show": "no halo; COUNT: all eight present; the altar half-built — first thing, still becoming.",
        "scene": (
            "The new world's first construction is not a roof: "
            "Noah bends on the open slope setting a rough field "
            "stone onto the low ring of an altar half-built, "
            "his white beard bright in the washed light — and "
            "around him the other seven pause their unloading "
            "to watch the old man work — the whole surviving "
            "human race, eight strong, standing witness while "
            "its patriarch spends the first labour of the "
            "cleaned earth on gratitude before shelter. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b03", "out": "s03-then-one-morning-the-ark.jpeg", "seg": "n1",
        "window": "8.86-14.44", "wide": True, "jesus": False, "ref": False,
        "locks": ["ARK", "MOUNTAIN"],
        "narration": (
            "Then one morning the ark sat still on a mountainside, and the "
            "earth lay quiet and washed and new."
        ),
        "must_show": "the stilled ark — the vast weathered vessel aground and slightly tilted on the green mountain shoulder, the washed new world falling away below in silver morning light.",
        "must_not_show": "ABSOLUTE: no bodies, no wreckage — the earth clean and empty; the ark whole and huge.",
        "scene": (
            "The morning it all went still, the camera set low "
            "on the slope taking the great hull from the side: "
            "the ark aground at last on the green mountain "
            "shoulder — vast, weathered, barn-high, tilted "
            "gently into the grass like a resting animal — and "
            "below it the new world falls away washed and "
            "silver: drying terraces, faint waterlines on far "
            "hills, mist in the clean valleys — a planet "
            "rinsed down to quiet, holding one boat, waiting "
            "to begin again. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r135-b04", "out": "s04-there-were-eight-of-them.jpeg", "seg": "n2",
        "window": "19.05-23.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": "There were eight of them, and everything they had ever known was gone.",
        "must_show": "COUNT-CRITICAL: exactly EIGHT figures on the wet slope below the ark, small against the washed emptiness; the entire human race in one frame.",
        "must_not_show": "ABSOLUTE: exactly eight — count them; the emptiness around them total but clean.",
        "scene": (
            "The census of mankind takes one glance: eight "
            "figures stand on the wet green slope — Noah "
            "white-bearded at their front, his wife at his "
            "arm, three sons, three sons' wives, huddled "
            "close in the enormous silver quiet — and around "
            "their little knot the washed world runs empty to "
            "every horizon: no smoke of any village, no road, "
            "no voice — everything they ever knew rinsed away "
            "beneath them, and everything that will ever be, "
            "standing in eight pairs of wet sandals. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b05", "out": "s05-the-whole-human-story-was.jpeg", "seg": "n2",
        "window": "23.35-25.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": "The whole human story was starting over.",
        "must_show": "the restart — a close pair of frames-worth in one: the first footprints pressed into clean mud, and the family's faces lifted toward the open land; page one again.",
        "must_not_show": "no halo; the footprints FRESH in unmarked mud — the first marks of the new chapter.",
        "scene": (
            "Page one gets its first marks: in the clean "
            "unmarked mud of the slope the family's fresh "
            "footprints press one after another away from the "
            "ark's shadow — the first human tracks of the "
            "second beginning — and above them the eight "
            "faces lift toward the empty green land with the "
            "unreadable expression of people handed a blank "
            "world: grief still wet in their eyes, and "
            "underneath it, unstoppable as spring, the "
            "beginning of beginning again. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b06", "out": "s06-be-fruitful-and-multiply-and.jpeg", "seg": "gv91",
        "window": "30.08-33.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": "Be fruitful, and multiply, and replenish the earth.",
        "must_show": "SCRIPTURE-EXACT: the blessing arriving — the eight with faces lifted to the bright opening sky, the words falling on them as light; GOD NEVER EMBODIED.",
        "must_not_show": "ABSOLUTE: no figure in the sky — the blessing carried by broadening light on lifted faces.",
        "scene": (
            "The first words of the new world come down as "
            "weather: the eight stand with faces lifted while "
            "the silver sky opens its first true breadth of "
            "warm light over them — be FRUITFUL, multiply, "
            "FILL it — the blessing arriving with no figure "
            "and no thunder, only the broadening brightness "
            "on eight upturned faces and the sudden green of "
            "the slopes taking the sun — a commission the "
            "size of a planet, delivered to a family of "
            "eight. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r135-b07", "out": "s07-fill-it-back-up-go.jpeg", "seg": "n2b",
        "window": "35.44-37.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["ARK", "MOUNTAIN"],
        "narration": "Fill it back up. Go live.",
        "must_show": "the commission enacted — the animals streaming out of the ark's great door in orderly pairs, fanning down the slope toward the green valleys; life dispersing.",
        "must_not_show": "no halo; the pairs ORDERLY and natural — real species, calm procession, no chaos.",
        "scene": (
            "The cargo hears the same commission: down the "
            "ark's great ramp the animals come in their calm "
            "unhurried pairs — deer stepping high through the "
            "wet grass, oxen swaying, birds unspooling into "
            "the washed air in ribbons — the procession "
            "fanning wider as it descends, pair by pair "
            "peeling off toward valley and thicket and crag — "
            "a year's held breath of life let out at last "
            "across the empty green, with orders everyone "
            "understood: fill it back up; go live. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b08", "out": "s08-eight-people-standing-in-the.jpeg", "seg": "n2b",
        "window": "37.06-44.85", "wide": True, "jesus": False, "ref": False,
        "locks": ["FAMILY", "ARK", "MOUNTAIN"],
        "narration": (
            "Eight people standing in the wreckage of a drowned world, and "
            "God's opening word to them is a blessing and a future."
        ),
        "must_show": "COUNT-CRITICAL wide — the camera behind the eight's backs as they face the washed valleys: the drowned world as CLEAN aftermath (mud flats, waterlines, driftwood), the light warm on their shoulders; blessing over ruin.",
        "must_not_show": "ABSOLUTE: no bodies, no human debris — nature's aftermath only; exactly eight backs.",
        "scene": (
            "What they survey and what surveys them, the "
            "camera set behind the eight's backs at the "
            "slope's edge: below them the drowned world lies "
            "clean in its aftermath — terraced mud flats "
            "drying to soft clay colours, faint waterlines "
            "ringing the far hills, silver driftwood cast "
            "along the valley seams — loss at the scale of a "
            "planet, rinsed and quiet — and on their eight "
            "backs, warm as a hand, the opening light of a "
            "God whose first word to the wreckage was a "
            "future. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r135-b09", "out": "s09-but-one-heavy-question-still.jpeg", "seg": "n2b",
        "window": "44.85-50.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": (
            "But one heavy question still hung over it all. Could anyone "
            "trust the sky again?"
        ),
        "must_show": "the question — one of the wives' wary upward glance at a passing cloud, her hand tightening on her husband's arm; the sky as an open wound.",
        "must_not_show": "no halo; ONE small cloud only — the fear in the FACES, not the weather.",
        "scene": (
            "One small cloud crosses the new sky and eight "
            "hearts check it: the youngest wife's face tips "
            "up, wary, tracking the white drift overhead the "
            "way you track a dog that has bitten — her hand "
            "finding her husband's arm and tightening — "
            "nothing in the cloud but water and light, and "
            "everything in the upturned eyes: the question "
            "the whole cleaned world cannot answer for them "
            "yet — whether the sky that did THAT can ever be "
            "trusted again. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r135-b10", "out": "s10-not-a-house-not-a.jpeg", "seg": "n3",
        "window": "53.87-55.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["ALTAR", "MOUNTAIN"],
        "narration": "Not a house. Not a fence.",
        "must_show": "the priorities — the finished low stone altar standing alone on the open slope, no house and no fence anywhere in frame; the first building, named by its absences.",
        "must_not_show": "no halo; NOTHING else built — the altar's aloneness the picture.",
        "scene": (
            "The building list of the new world, in order: on "
            "the whole green mountain shoulder there stands "
            "exactly one made thing — the low ring of rough "
            "stacked stones, knee-high, empty and ready — no "
            "wall raised against weather, no fence against "
            "beasts, no roof against the feared sky — every "
            "practical building unbegun while the impractical "
            "one stands finished — first things put first by "
            "a family that has just learned, at full price, "
            "which things are first. No people are in this "
            "frame."
        ),
    },
    {
        "id": "v2-r135-b11", "out": "s11-he-gathered-stones-and-built.jpeg", "seg": "n3",
        "window": "55.33-63.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["ALTAR", "FAMILY", "MOUNTAIN"],
        "narration": (
            "He gathered stones and built an altar, and he gave thanks. And "
            "God answered that small smoking altar with a promise about the "
            "whole future."
        ),
        "must_show": "the thanks and the answer — the altar smoking thin and STRAIGHT into the still air, Noah with hands lifted, the seven around; the sky beginning to warm above the smoke; GOD NEVER EMBODIED.",
        "must_not_show": "ABSOLUTE: no figure in the sky — the answer is warming light meeting rising smoke; count eight.",
        "scene": (
            "The smallest fire on earth gets heaven's full "
            "attention: the altar's thin smoke climbs "
            "perfectly straight into the still morning — the "
            "whole planet's worship rising from one knee-high "
            "ring of stones — Noah's arms lifted beside it, "
            "his seven gathered close — and above the climbing "
            "grey thread the sky itself begins to warm, light "
            "descending to meet the smoke halfway, an answer "
            "already forming that will be about nothing less "
            "than the entire future. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b12", "out": "s12-for-the-better-part-of.jpeg", "seg": "n1",
        "window": "1.49-8.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["ARK"],
        "narration": (
            "For the better part of a year, one family and a great wooden "
            "boat full of animals had ridden out the end of the world they "
            "knew."
        ),
        "must_show": "the year remembered — the ark alone on endless grey water under rain, small against the swell; the long ride, told from merciful distance.",
        "must_not_show": "ABSOLUTE: no drowning imagery, no victims — the ark and the water only; endurance, not catastrophe.",
        "scene": (
            "The year behind them looked like this for months "
            "on end: the great wooden vessel alone on a grey "
            "world of water, rain hatching the swells, no "
            "horizon anywhere that is not more water — the "
            "ark riding it high-sided and stubborn, one "
            "lamp-warm seam of light at its shuttered vent — "
            "a family and a zoo and the future itself packed "
            "in gopher wood, riding out the end of everything "
            "across the loneliest sea there has ever been. "
            "No people are visible in this frame."
        ),
    },
    {
        "id": "v2-r135-b13", "out": "s13-while-the-earth-remaineth-seedtime.jpeg", "seg": "jv22",
        "window": "64.21-73.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": (
            "While the earth remaineth, seedtime and harvest, and cold and "
            "heat, and summer and winter, and day and night shall not cease."
        ),
        "must_show": "SCRIPTURE-EXACT: the rhythm promised — one landscape holding the cycle's tokens: green shoots in near soil, ripe grain on a far terrace, the sun low and the first star up; the wheel of times in a single frame.",
        "must_not_show": "no halo; the composition CALENDAR-like but natural — no split-screen effects; one believable golden hour holding the tokens.",
        "scene": (
            "The promise reads like a farmer's calendar "
            "carved into one valley: near at hand the wet "
            "soil stands pricked with new green shoots — "
            "seedtime — while a far terrace holds a stand of "
            "grain gone heavy and gold — harvest — and over "
            "both the low sun burns warm at one edge of the "
            "sky while the first cold star opens at the "
            "other: heat and cold, day and night, summer and "
            "winter, the whole great wheel promised into "
            "motion for as long as the earth shall stand. No "
            "people are in this frame."
        ),
    },
    {
        "id": "v2-r135-b14", "out": "s14-planting-time-and-gathering-time.jpeg", "seg": "n4",
        "window": "74.70-79.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": "Planting time and gathering time, winter and summer, morning and night.",
        "must_show": "the rhythm begun — two of the sons breaking the first furrow and scattering the first seed on a cleared terrace; the family entering the promised cycle.",
        "must_not_show": "no halo; the work HOPEFUL — first furrow in clean soil, seed from a saved bag.",
        "scene": (
            "The family files into the promised rhythm at the "
            "planting end: on a cleared terrace two of the "
            "sons work the first furrow of the new world — "
            "one leaning the wooden plough through the soft "
            "washed soil, the other walking the open line "
            "broadcasting seed from the precious saved bag in "
            "steady sweeping arcs — the first deposit ever "
            "made into the new covenant of seasons, sown by "
            "men betting everything on a promise about "
            "harvest. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r135-b15", "out": "s15-the-world-would-keep-its.jpeg", "seg": "n4",
        "window": "79.31-83.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "The world would keep its rhythm for as long as it stands.",
        "must_show": "the rhythm running — the same terrace weeks on: the furrow rows greened into young grain moving in wind under travelling cloud-shadow; the machine of seasons visibly working.",
        "must_not_show": "no halo; the growth VISIBLE against b14's bare furrows — time passing kept.",
        "scene": (
            "The machine turns over and catches: the same "
            "terrace weeks later stands striped in young "
            "green — the furrows risen into ranks of new "
            "grain that lean and recover under the moving "
            "wind, cloud-shadows travelling the slope like "
            "slow hands — the rhythm running exactly as "
            "promised, day feeding night feeding day, the "
            "world's oldest engine restarted and holding its "
            "beat for as long as the earth shall stand. No "
            "people are in this frame."
        ),
    },
    {
        "id": "v2-r135-b16", "out": "s16-but-god-was-not-finished.jpeg", "seg": "n4",
        "window": "83.01-90.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": (
            "But God was not finished, because he knew something about these "
            "eight people. He knew what rain now meant to them."
        ),
        "must_show": "what rain means now — close on Noah's weathered face at a doorway... of the ark's shadow, eyes on the horizon where weather builds; the knowledge behind his stillness.",
        "must_not_show": "no halo; the coming weather DISTANT and slight — his face carrying the history.",
        "scene": (
            "One word has changed its meaning forever for "
            "exactly eight people: close on Noah's weathered "
            "face turned toward the far horizon, where an "
            "ordinary bank of afternoon cloud is quietly "
            "building — nothing in it, every farmer's friend "
            "— and the old eyes hold it with a stillness that "
            "is not calm: the look of a man for whom the word "
            "RAIN will never again mean water on barley, and "
            "of a God who knows it, and is not finished with "
            "them yet. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r135-b17", "out": "s17-think-about-the-first-time.jpeg", "seg": "n5",
        "window": "90.90-97.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": (
            "Think about the first time clouds rolled in after the flood. "
            "For Noah's family, a dark sky was no longer just weather."
        ),
        "must_show": "the first dark sky — REAL grey rolling in over the slopes (deliberate), the eight drawn instinctively together, faces up, work dropped; fear with dignity.",
        "must_not_show": "no halo; COUNT eight; the fear DIGNIFIED — drawn together, not scattered screaming; the grey heavy but ordinary.",
        "scene": (
            "The first test of the new sky arrives on an "
            "ordinary afternoon: grey rolls in over the "
            "western slopes the way grey has always rolled — "
            "and the eight stop as one, tools lowered, work "
            "abandoned mid-motion, drawing together on the "
            "open ground with their faces turned up — hands "
            "finding hands down the little line of them — a "
            "family watching weather the way survivors watch "
            "it, remembering with their whole bodies what "
            "the sky did last time it darkened. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b18", "out": "s18-it-was-the-memory-of.jpeg", "seg": "n5",
        "window": "97.92-103.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": (
            "It was the memory of everything they had lost. And God did not "
            "scold them for being afraid."
        ),
        "must_show": "the memory in one face — close on Noah's wife under the grey: grief and fear together, utterly dignified; and the light around her NOT punishing — soft, patient.",
        "must_not_show": "no halo; no scolding weather — the grey soft at its edges; her dignity total.",
        "scene": (
            "What the dark sky holds for her is not weather "
            "at all: close on Noah's wife with the grey "
            "rolling over — the old face lifted, rain-fear "
            "and grief sharing the deep lines, every drowned "
            "neighbour and lost dooryard of the former world "
            "moving behind her steady eyes — and the light "
            "around her stays soft at the edges, patient, "
            "unpunishing: heaven watching an old woman be "
            "afraid of the sky, and preparing, instead of a "
            "scolding, a gift. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b19", "out": "s19-he-moved-to-meet-the.jpeg", "seg": "n5",
        "window": "103.31-104.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "He moved to meet the fear.",
        "must_show": "the meeting — the grey sky BREAKING: one great shaft of warm light descending through the parting cloud toward the slopes; mercy moving first; GOD NEVER EMBODIED.",
        "must_not_show": "ABSOLUTE: no figure in the light — the break itself is the movement.",
        "scene": (
            "Heaven crosses the room first: through the heavy "
            "grey a seam opens — cloud parting along a long "
            "line, and down through the gap one great shaft "
            "of warm gold descends to lie across the green "
            "slopes like an arm laid over a shoulder — the "
            "fear not waited out or reasoned with but MET, "
            "the sky that frightened them moving toward them "
            "with light in its hands, first. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r135-b20", "out": "s20-and-i-behold-i-establish.jpeg", "seg": "jv9",
        "window": "105.42-111.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": (
            "And I, behold, I establish my covenant with you, and with your "
            "seed after you."
        ),
        "must_show": "SCRIPTURE-EXACT: the covenant spoken — the eight beneath the break-light, faces lifted into the words; the promise arriving over the family; GOD NEVER EMBODIED.",
        "must_not_show": "ABSOLUTE: no figure — the words carried by the descending warm light on eight upturned faces; count eight.",
        "scene": (
            "The words come down the light-shaft like a hand "
            "on the head: the eight stand gathered beneath "
            "the great warm break in the grey, faces lifted, "
            "and the covenant arrives over them — I, behold "
            "I, ESTABLISH — the doubled pronoun leaning its "
            "whole weight on who is doing this — with YOU, "
            "and your seed after you, the little knot of "
            "eight suddenly standing for every generation "
            "that will ever descend the mountain from them. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r135-b21", "out": "s21-a-covenant-is-the-most.jpeg", "seg": "n6",
        "window": "113.44-120.08", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "A covenant is the Bible's most serious word for a promise, one "
            "that binds the person who makes it."
        ),
        "must_show": "the word's weight — a period covenant token: two hands clasping over a stone with a cut mark, oath-posture; the binding made physical, timeless and simple.",
        "must_not_show": "no halo; period-true simplicity — no documents, no seals; the clasp and the marked stone.",
        "scene": (
            "The Bible's most serious word has always had a "
            "shape: two hands clasped hard over a boundary "
            "stone cut with a single mark — the old oath-"
            "posture of the ancient world, wrist to wrist, "
            "witnessed by sky — a promise with a body, "
            "binding the one who makes it the way rope binds: "
            "not a sentiment, not a hope, but a thing DONE, "
            "after which the promiser is no longer free — "
            "covenant, the word that means the door has been "
            "closed behind the promise. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b22", "out": "s22-and-notice-who-is-doing.jpeg", "seg": "n6",
        "window": "120.08-122.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": "And notice who is doing the binding here.",
        "must_show": "the direction of binding — the eight standing with EMPTY open hands under the break-light; nothing being signed, sworn or given upward; the traffic all one-way, downward.",
        "must_not_show": "ABSOLUTE: no oath-posture from the family — hands visibly open and empty; count eight.",
        "scene": (
            "Look at the eight pairs of hands: every one of "
            "them empty — no offering raised, no oath sworn, "
            "no token held up, eight people standing in the "
            "warm descending light with their palms open at "
            "their sides like people receiving weather — all "
            "the binding in this covenant travelling one "
            "direction only, downward, from the sky that "
            "owes them nothing to the family that could "
            "never repay it — notice, says the row, WHO is "
            "being bound. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r135-b23", "out": "s23-noah-is-not-asked-to.jpeg", "seg": "n6",
        "window": "122.86-130.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": (
            "Noah is not asked to promise anything, sign anything, or earn "
            "anything. God binds himself, one way, for free."
        ),
        "must_show": "the free gift — close on Noah's open upturned empty hands, the warm light lying in the palms like something given; grace's direction in one image.",
        "must_not_show": "no halo; the hands EMPTY and receiving — nothing offered up.",
        "scene": (
            "The terms of the covenant fit in two old open "
            "hands: close on Noah's upturned palms — empty, "
            "work-scarred, six hundred years worn — with the "
            "warm break-light lying in them like a weight "
            "that can be felt — nothing demanded into them, "
            "nothing signed by them, nothing owed from them — "
            "the whole contract written, sealed and paid on "
            "the other side, and delivered into a pair of "
            "hands whose only job is to be open. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b24", "out": "s24-to-noah-to-his-children.jpeg", "seg": "n6",
        "window": "130.18-135.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "ARK", "MOUNTAIN"],
        "narration": (
            "To Noah, to his children, and to every living creature that "
            "walked off that boat."
        ),
        "must_show": "the covenant's full roster — the eight on the slope AND the animals grazing wide below them, birds over; the promise's roll call in one frame.",
        "must_not_show": "no halo; count eight; the animals dispersed natural down the slopes.",
        "scene": (
            "The covenant's signature page includes every "
            "heartbeat on the mountain: the eight stand "
            "together on the upper slope, and below them the "
            "new world's whole zoology grazes wide across "
            "the green — deer at the thicket line, oxen deep "
            "in the wet grass, goats picking along the rocks, "
            "birds writing slow loops over the valleys — "
            "every living creature that walked off the boat, "
            "named into the same promise as the family, no "
            "sparrow left off the roster. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b25", "out": "s25-noah-and-his-family-stepped.jpeg", "seg": "n2",
        "window": "15.05-19.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "ARK", "MOUNTAIN"],
        "narration": "Noah and his family stepped out onto wet grass under an open sky.",
        "must_show": "the stepping-out — the eight descending the ark's great ramp onto the wet green, first steps onto the new earth; the door open behind them.",
        "must_not_show": "no halo; COUNT eight on or at the ramp; the grass WET and bright.",
        "scene": (
            "The first walk of the new world is eight people "
            "long: down the ark's great ramp they come — "
            "Noah first with his staff, his wife's hand in "
            "his, the sons and their wives behind in a "
            "careful descending line — sandals meeting wet "
            "living grass for the first time in a year, the "
            "great door standing open behind them and the "
            "washed sky standing open above — mankind "
            "stepping back onto its planet through the only "
            "doorway that survived. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b26", "out": "s26-and-i-will-establish-my.jpeg", "seg": "jv11",
        "window": "136.15-148.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": (
            "And I will establish my covenant with you; neither shall all "
            "flesh be cut off any more by the waters of a flood; neither "
            "shall there any more be a flood to destroy the earth."
        ),
        "must_show": "SCRIPTURE-EXACT: the never-again — the wide washed earth under the break-light, the flood's faint waterlines on the hills visibly DRYING and fading; the promise written on the land itself.",
        "must_not_show": "ABSOLUTE: no figure; the waterlines FADING — the earth visibly released from the sentence.",
        "scene": (
            "The land itself receives the never-again: under "
            "the widening warm light the washed valleys run "
            "to the horizon, and on the far hills the "
            "flood's faint waterlines — the high-tide marks "
            "of the end of the world — stand visibly drying, "
            "paling, fading back into ordinary hillside — "
            "the earth being released from its sentence "
            "ring by ring — never again all flesh, never "
            "again the waters, the promise soaking into the "
            "ground like the light. No people are in this "
            "frame."
        ),
    },
    {
        "id": "v2-r135-b27", "out": "s27-never-again-that-is-the.jpeg", "seg": "n7",
        "window": "150.01-155.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY"],
        "narration": (
            "Never again. That is the whole promise, with no conditions "
            "attached and no expiration date."
        ),
        "must_show": "the two words landing — the eight's faces as never-again reaches them: the first full unbracing, shoulders dropping, a wife's tears breaking free; relief with dignity.",
        "must_not_show": "no halo; count eight; the relief PHYSICAL — bodies unbracing after a year braced.",
        "scene": (
            "Two words unbrace eight bodies at once: NEVER "
            "AGAIN moves through the little family like "
            "warmth through cold hands — Noah's shoulders "
            "coming down from their year-long guard, a son's "
            "held breath leaving him audibly, the youngest "
            "wife's tears breaking loose at last and her "
            "husband's arm around her — no conditions "
            "clause for them to fail, no expiry for their "
            "grandchildren to dread — the whole promise, "
            "whole, forever, landing on the people who "
            "needed it most. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r135-b28", "out": "s28-and-then-god-does-something.jpeg", "seg": "n7",
        "window": "155.65-158.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "And then God does something wonderfully tender.",
        "must_show": "the tenderness beginning — the light after rain going strange and full: sun through falling silver drizzle, the air itself preparing; the moment before the sign.",
        "must_not_show": "ABSOLUTE: no bow YET — the charged sunlit rain only; no figure.",
        "scene": (
            "The air itself gets ready for the gift: sun "
            "breaks fully through while the last silver "
            "drizzle still falls, and the whole valley fills "
            "with that rare charged light — every raindrop "
            "lit falling, the green slopes deepening, the "
            "grey retreating east with the storm's remnant — "
            "the exact meteorology of mercy assembling over "
            "the mountain, sun and rain in the same sky at "
            "the same time, one breath before the tenderest "
            "thing in Genesis. No people are in this frame."
        ),
    },
    {
        "id": "v2-r135-b29", "out": "s29-he-gives-the-promise-a.jpeg", "seg": "n7",
        "window": "158.59-162.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": "He gives the promise a sign you can see with your eyes.",
        "must_show": "the first sight — the eight turning as one toward something off-frame lighting their faces with wonder; the sign arriving in their eyes before ours.",
        "must_not_show": "ABSOLUTE: the bow NOT yet in frame — the wonder on eight faces announces it; count eight.",
        "scene": (
            "We see it first in eight faces: the family turns "
            "as one toward the eastern sky — and wonder "
            "arrives on them like sunrise, mouths opening, "
            "the fear draining visibly out of the same eyes "
            "that tracked every cloud for months, a son's "
            "arm rising slowly to point — whatever stands in "
            "that sky off-frame is remaking their faces as "
            "we watch, the promise becoming, at last, "
            "something you can SEE. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r135-b30", "out": "s30-i-do-set-my-bow.jpeg", "seg": "jv13",
        "window": "162.55-169.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": (
            "I do set my bow in the cloud, and it shall be for a token of a "
            "covenant between me and the earth."
        ),
        "must_show": "SCRIPTURE-EXACT: THE BOW — the full rainbow standing complete over the washed valley against the retreating grey, real and painted true; the token itself at full size.",
        "must_not_show": "ABSOLUTE: no sparkle effects, no doubled exaggeration — one true arc in washed light; no figure in the sky.",
        "scene": (
            "The token stands up across the whole eastern "
            "sky: one complete rainbow, foot to foot across "
            "the washed valley — rising out of the drying "
            "flats, arcing high over the retreating grey, "
            "planting its far end on the green shoulder of "
            "the hills — colour laid into the air with a "
            "steadiness no shower ever owned, real as "
            "weather and larger than any weather's excuse "
            "for it — the covenant hanging its signature "
            "where the whole earth can read it. No people "
            "are in this frame."
        ),
    },
    {
        "id": "v2-r135-b31", "out": "s31-the-word-there-is-simply.jpeg", "seg": "n8",
        "window": "170.94-177.87", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The word there is simply bow, and it is the same word the Bible "
            "uses for a battle bow, a weapon of war."
        ),
        "must_show": "the word's other meaning — a great battle-bow of wood and horn lying across a warrior's rack, arrows beside; the weapon the word names, at rest.",
        "must_not_show": "ABSOLUTE: no battle, no violence — the weapon at rest on its rack; period-true.",
        "scene": (
            "The Hebrew word owns exactly one picture, and "
            "this is it: a great battle-bow of layered wood "
            "and horn lying across its wooden rack in a "
            "quiet armoury corner — the grip worn dark with "
            "campaigns, the quiver of arrows leaned beside — "
            "a weapon of war at rest, the same word, letter "
            "for letter, that Genesis reaches for when God "
            "names the thing he is about to hang in the "
            "clouds. No people are in this frame."
        ),
    },
    {
        "id": "v2-r135-b32", "out": "s32-god-hangs-a-bow-in.jpeg", "seg": "n8",
        "window": "177.87-182.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "God hangs a bow in the clouds, unstrung, aimed away from the earth.",
        "must_show": "the doctrine in the arc — the rainbow again with its geometry READ: the arc opening downward like an unstrung bow hung up, its 'aim' turned away from the land below.",
        "must_not_show": "ABSOLUTE: no literal weapon in the sky — the real rainbow, with the composition letting its bow-shape and away-aim read.",
        "scene": (
            "Read the shape the way the first eight read it: "
            "the great arc stands over the valley with its "
            "back bent toward heaven and its opening turned "
            "down over the land — a bow hung up by its "
            "middle, unstrung, incapable — and if it aimed "
            "anywhere at all it would aim upward, away, out "
            "past the sky it hangs in — the weapon of the "
            "storm retired in plain sight of the people it "
            "will never again be drawn against. No people "
            "are in this frame."
        ),
    },
    {
        "id": "v2-r135-b33", "out": "s33-it-is-the-picture-of.jpeg", "seg": "n8",
        "window": "182.38-186.75", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It is the picture of a warrior hanging up his weapon on the wall.",
        "must_show": "the metaphor exact — strong scarred hands hanging the great unstrung battle-bow on wall pegs, turning away done; the war's end in one act.",
        "must_not_show": "ABSOLUTE: no face needed, no battle — the hanging-up itself; the bow visibly UNSTRUNG.",
        "scene": (
            "The gesture behind the rainbow is this one: two "
            "strong scarred hands lift the great bow — "
            "unstrung, its cord wound loose around the grip "
            "— and set it onto the wall pegs above the "
            "hearth, pressing it home into the rest it will "
            "not leave — the day's oldest sign of a war "
            "ended, a warrior's declaration written in "
            "furniture: this weapon has hung its last "
            "campaign, and the hands that hung it are free "
            "for other work. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r135-b34", "out": "s34-the-storm-between-heaven-and.jpeg", "seg": "n8",
        "window": "186.75-189.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "The storm between heaven and earth is over.",
        "must_show": "the peace signed — the full bow over the now-sunlit valley, the last grey gone from the sky's far edge; armistice as landscape.",
        "must_not_show": "ABSOLUTE: no remaining threat in the sky — the grey exiting the frame's edge; the light whole.",
        "scene": (
            "The armistice takes effect across the whole "
            "visible world: the bow stands full over a "
            "valley gone entirely to sunlight, the last "
            "shred of grey slipping off the frame's far "
            "edge like a signature completing — washed "
            "slopes steaming faintly gold, the air rinsed "
            "and ringing — between heaven and earth, where "
            "the longest storm in history stood, nothing "
            "now but colour and settled light: the war "
            "over, the treaty visible, the sky safe to "
            "love again. No people are in this frame."
        ),
    },
    {
        "id": "v2-r135-b35", "out": "s35-and-the-bow-shall-be.jpeg", "seg": "jv16",
        "window": "190.18-202.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": (
            "And the bow shall be in the cloud; and I will look upon it, "
            "that I may remember the everlasting covenant between God and "
            "every living creature of all flesh that is upon the earth."
        ),
        "must_show": "SCRIPTURE-EXACT: I-will-look-upon-it — the bow seen from HIGH ABOVE the cloud-tops, arcing below against the earth; the sign from the side that matters: heaven's view of its own reminder.",
        "must_not_show": "ABSOLUTE: no figure, no eye imagery — the aerial vantage itself carries whose view this is.",
        "scene": (
            "For one frame the row borrows the only vantage "
            "that matters: from high above the broken "
            "cloud-tops the bow arcs BELOW, its colours laid "
            "against the little green earth like a mark on "
            "a page — the world's valleys small beyond it, "
            "the family's mountain a fold among folds — the "
            "sign seen from the side it was actually set "
            "for: the view from which Someone will look "
            "upon it, and remember, every time any sky "
            "anywhere clears. No people are in this frame."
        ),
    },
    {
        "id": "v2-r135-b36", "out": "s36-and-the-very-first-thing.jpeg", "seg": "n2",
        "window": "25.81-29.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": "And the very first thing God said to them was not a warning.",
        "must_show": "the not-a-warning — the eight braced as if for judgment, heads slightly bowed — and the light arriving WARM instead; the flinch meeting kindness.",
        "must_not_show": "ABSOLUTE: no figure; the family's braced posture easing as the warmth lands; count eight.",
        "scene": (
            "They brace for the scolding that never comes: "
            "the eight stand close with heads slightly "
            "bowed, shoulders set, survivors awaiting the "
            "terms — whatever a God says to the remnant of "
            "a world that earned a flood — and what arrives "
            "over them instead is warmth: the light coming "
            "down kind across their braced backs, the first "
            "syllables already blessing before anyone dared "
            "look up — a family flinching from thunder and "
            "receiving, of all imaginable things, a future. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r135-b37", "out": "s37-did-you-catch-who-the.jpeg", "seg": "n9",
        "window": "204.31-209.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "Did you catch who the sign is for? God set the reminder where he would see it.",
        "must_show": "the addressee — the bow high in the sky with the land small below; the sign's placement itself the argument: hung in HEAVEN's view, not on earth's wall.",
        "must_not_show": "ABSOLUTE: no figure, no eye — the height of the sign carries the point.",
        "scene": (
            "Notice where the string got tied: the bow "
            "stands at the very top of the sky, high over "
            "the small green land — not carved on a "
            "doorpost down here, not hung in any human "
            "hall, but set at heaven's own eye level, in "
            "the one place the earth can barely reach and "
            "the sky cannot avoid — a reminder positioned "
            "for its actual reader, who looks DOWN through "
            "clouds, and remembers. No people are in this "
            "frame."
        ),
    },
    {
        "id": "v2-r135-b38", "out": "s38-the-rainbow-is-the-string.jpeg", "seg": "n9",
        "window": "209.13-218.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": (
            "The rainbow is the string God tied around his own finger. "
            "Before it ever comforts you, it is his own promise, kept "
            "deliberately in his own sight."
        ),
        "must_show": "the doctrine warmed — the family beneath the bow, and near ground: a mother tying a remembering-string around a child's small finger; the homely metaphor beside the cosmic one.",
        "must_not_show": "no halo; the string-tying TENDER and clear; the bow above; count the family eight.",
        "scene": (
            "The homeliest picture in the row explains the "
            "grandest: in the near ground one of the wives "
            "ties a little thread around her small son's "
            "finger — the born-since baby of the new world — "
            "so he will not forget his errand; and above "
            "them both, foot to foot across the sky, the "
            "bow stands tied around the finger of heaven "
            "for exactly the same reason — a God who "
            "deliberately keeps his own promise where his "
            "own eye will land on it, every clearing, "
            "forever. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r135-b39", "out": "s39-and-the-promise-held.jpeg", "seg": "n10",
        "window": "218.63-219.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "And the promise held.",
        "must_show": "the holding — the same valley in a later season, rain freshly passed, fields ripe, the bow up again; the machine of mercy still running.",
        "must_not_show": "no halo; the land visibly OLDER-SEASONED than before — time passed, promise kept.",
        "scene": (
            "Three words, tested by every storm since: the "
            "same valley in another season entirely — "
            "terraces gone gold with a later harvest, trees "
            "grown, the rain just passed off eastward — and "
            "up over the wet bright land the bow stands "
            "again, exactly where it stood, doing exactly "
            "what it was hung to do — the promise not "
            "framed and shelved but WORKING, season after "
            "season, holding. No people are in this frame."
        ),
    },
    {
        "id": "v2-r135-b40", "out": "s40-rain-has-come-and-gone.jpeg", "seg": "n10",
        "window": "219.96-228.39", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Rain has come and gone for thousands of years since that "
            "mountainside, and when the shower passes, the same sign still "
            "climbs the sky."
        ),
        "must_show": "the millennia — a DIFFERENT green land (no ark, later age): shower passing, the same bow climbing over ordinary fields and a far small village; the sign unchanged across ages.",
        "must_not_show": "no halo; period-neutral timelessness — no modern objects; the sameness of the bow the point.",
        "scene": (
            "Change the valley, keep the sign: a different "
            "green country in a different age — hedged "
            "fields, a far small village on a rise, sheep "
            "scattered on wet pasture — the shower walking "
            "off east in silver curtains, and up over the "
            "rinsed land the same bow climbs that climbed "
            "over Ararat: same colours, same stance, same "
            "unstrung peace — thousands of years of rain "
            "come and gone, and the signature never once "
            "missing from a cleared sky. No people are "
            "distinguishable in this frame."
        ),
    },
    {
        "id": "v2-r135-b41", "out": "s41-children-point-at-it-nobody.jpeg", "seg": "n10",
        "window": "228.39-230.98", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Children point at it. Nobody runs from it.",
        "must_show": "the healed sky — village children on wet grass pointing up at the bow, delighted, unafraid; the covenant's success measured in children's faces.",
        "must_not_show": "no halo; pure delight — not one fearful face; the bow high beyond their pointing arms.",
        "scene": (
            "The covenant's success is measurable in "
            "children: on the wet bright grass a scatter of "
            "village children has stopped mid-game to point "
            "— arms up, faces thrown open with delight, one "
            "small girl bouncing on her toes — at the great "
            "coloured arc standing over their world — and "
            "in all that upturned wonder there is not one "
            "flicker of fear, not one child who runs: the "
            "sky's most dangerous memory, converted by one "
            "promise into the most pointed-at thing on "
            "earth. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r135-b42", "out": "s42-that-is-what-it-feels.jpeg", "seg": "n10 + n11",
        "window": "230.98-238.77", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That is what it feels like to live inside a promise God is "
            "keeping. This is the God the whole story has been about."
        ),
        "must_show": "living inside the promise — a family at their door watching the bow together, at ease, the land safe around them; ordinary life held inside kept covenant.",
        "must_not_show": "no halo; the ease TOTAL — no bracing anywhere; warmth, home, safety.",
        "scene": (
            "Living inside a kept promise looks wonderfully "
            "ordinary: a family stands easy at their own "
            "doorway in the after-rain light — father's arm "
            "on the doorframe, mother's hand on a child's "
            "shoulder, supper warm behind them — watching "
            "the bow stand over their fields the way you "
            "watch a sunset: unafraid, unhurried, at home — "
            "a household going about its evening entirely "
            "inside the walls of a promise Someone else is "
            "keeping, which is the whole architecture of "
            "their peace. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r135-b43", "out": "s43-a-god-who-knows-exactly.jpeg", "seg": "n11",
        "window": "238.77-244.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["FAMILY", "MOUNTAIN"],
        "narration": (
            "A God who knows exactly what frightens his people, and answers "
            "fear with beauty instead of blame."
        ),
        "must_show": "the answer's character — the eight beneath the full bow, fear visibly gone from the same faces that dreaded the clouds; beauty doing the comforting.",
        "must_not_show": "no halo; count eight; the SAME faces as the fear beats, transformed.",
        "scene": (
            "Set the two afternoons side by side in the same "
            "eight faces: the family stands beneath the full "
            "bow, and every face that tracked the grey with "
            "dread now tips up into colour — the youngest "
            "wife who gripped her husband's arm smiling "
            "openly at the sky, Noah's wife's deep lines "
            "gone soft, the old man himself steady-eyed and "
            "shining — fear answered not with argument, not "
            "with blame for feeling it, but with something "
            "beautiful hung exactly where the fear used to "
            "live. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r135-b44", "out": "s44-a-god-who-binds-himself.jpeg", "seg": "n11",
        "window": "244.98-249.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": (
            "A God who binds himself with promises, and then keeps them. He "
            "has not changed."
        ),
        "must_show": "the closing frame — the full bow over the green world in clean warm light, complete and quiet; the kept promise as the last image; timeless.",
        "must_not_show": "ABSOLUTE: no figure; the bow full and true; nothing added — the sign is the sermon.",
        "scene": (
            "The last word belongs to the sign itself: the "
            "full bow stands complete over the green washed "
            "world in clean warm light — foot to foot, "
            "colour to colour, exactly as first hung — no "
            "caption in the sky, no figure, nothing added "
            "in all the thousands of years since the "
            "mountainside — a God who binds himself and "
            "then, storm after storm after storm, keeps "
            "the binding — unchanged, and visibly still on "
            "duty over every clearing sky. No people are in "
            "this frame."
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
