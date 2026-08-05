#!/usr/bin/env python3
"""V2 beat map — row 150, build-150-shepherd-psalm (Psalm 23).

COVERAGE: 21 pictures over 122.5 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Psalm 23 KJV):
  v1 "The LORD is my shepherd; I SHALL NOT WANT."
  v2 "He maketh me to LIE DOWN in green pastures: he leadeth me
     beside the STILL waters."
  v3 "He RESTORETH my soul: he leadeth me in the paths of
     righteousness FOR HIS NAME'S SAKE."
  v4 "Yea, though I walk through the VALLEY OF THE SHADOW OF DEATH,
     I will fear no evil: for THOU art with me; thy ROD and thy
     STAFF they comfort me." — the He→THOU turn happens in the dark.
  v5 "Thou preparest a TABLE before me in the presence of mine
     enemies: thou ANOINTEST my head with oil; my CUP RUNNETH OVER."
  v6 "Surely goodness and mercy shall FOLLOW me... and I will DWELL
     in the house of the LORD for ever."
  Author: DAVID — the shepherd-king writing about being shepherded.

RENDERING LAWS:
  - DAVID HAS TWO AGES, one face: the KING (~50, writing with harp
    near) and the remembered YOUNG SHEPHERD (~17, in the psalm's
    field frames) — same features, aged; face-board the pair.
  - THE VALLEY (b11/b13) is a REAL dark gorge — deep shadow, real
    dark, light at its far end; NO death imagery, no bones, no
    spectres, ever. The comfort is rod, staff, and nearness.
  - THE ENEMIES (b14/b15) are FAR RIDGE SILHOUETTES only — vague,
    distant, unable to approach; never close, never armed in
    detail; the table's calm is the picture.
  - The He→THOU grammar turn (b12/b13) is the row's discovery:
    nearness increases IN the dark — the sheep pressing close to
    the shepherd's legs in the gorge.
  - Goodness-and-mercy PURSUING (b18/b19) is rendered as the
    shepherd walking BEHIND the homeward flock, striding — the
    following made of the shepherd himself.
  - All light physical; the psalm's scroll script indistinct.

TIME OF DAY ARC (intentional): the king's writing frames at warm
lamplit evening; the pasture frames in soft green morning; the
valley at TRUE deep shadow with far daylight (deliberate); the
table at golden late afternoon; the homecoming at warm dusk; the
close at lamplit night, at rest.

CHANGING CONDITIONS (kept OUT of the locks): David's age per frame
(king writing / young shepherd remembered); the flock — grazing,
lying down, led, through the gorge, home.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row).
LOCKS = {
    "DAVID": (
        "DAVID LOCK: David is the same face at two ages — as KING "
        "(~50): a strong lined face, russet-grey beard, in a DEEP "
        "ROYAL-BLUE robe with a dark mantle (never cream, never "
        "white), the harp near; as the remembered YOUNG SHEPHERD "
        "(~17): the same features young — ruddy, bright-eyed, in a "
        "short DARK RUST tunic with a sling at his belt and a "
        "shepherd's staff. One face, two ages, per beat."
    ),
    "PASTURE": (
        "PASTURE LOCK: the green pastures — deep spring-green "
        "meadows in a sheltered valley, a slow stream widening to "
        "GLASS-STILL pools, willows at the banks; cream-wool sheep. "
        "The same valley and pools throughout."
    ),
    "GORGE": (
        "GORGE LOCK: the valley of shadow — a narrow deep-cut gorge "
        "of dark rock, the path threading its floor in true deep "
        "shade, a bright doorway of daylight at its FAR end. The "
        "same gorge and far light throughout."
    ),
    "TABLE": (
        "TABLE LOCK: the prepared table — a sturdy wooden table "
        "spread with a woven cloth, flat bread, a horn of oil and "
        "one generous cup, set in open golden hill-country. The "
        "same table and setting throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r150-b01", "out": "s01-three-thousand-years-ago-a.jpeg", "seg": "n0",
        "window": "0.40-4.57", "wide": True, "jesus": False, "ref": False,
        "locks": ["DAVID"],
        "narration": (
            "Three thousand years ago a shepherd-king wrote a song about "
            "being shepherded himself."
        ),
        "must_show": "the shepherd-king — KING David at his lamplit evening chamber, harp beside him, pen at the scroll; through the window the far hills where the song was learned.",
        "must_not_show": "no halo; script INDISTINCT; both halves of him present — royal robe, shepherd's far hills.",
        "scene": (
            "The author outranks every shepherd and answers to "
            "one, the camera looking into the chamber past the "
            "harp's dark shoulder: King David at his writing "
            "table in the lamplit evening — the royal blue "
            "robe, the russet-grey beard, the strong lined "
            "hands that once broke lions now holding a reed "
            "pen over the scroll — and through the open window "
            "behind him the far dark hills where a boy once "
            "watched sheep under these same stars: the "
            "shepherd-king, writing home. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r150-b02", "out": "s02-the-lord-is-my-shepherd.jpeg", "seg": "s1",
        "window": "7.97-10.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "PASTURE"],
        "narration": "The LORD is my shepherd; I shall not want.",
        "must_show": "SCRIPTURE-EXACT: the opening line lived — YOUNG David the shepherd among his contented flock in the green valley, at ease, wanting nothing; the singer inside his own metaphor.",
        "must_not_show": "no halo; YOUNG David (same face, ~17); the flock's contentment total.",
        "scene": (
            "The song's first line is a memory of mornings "
            "like this: young David — the same face, ruddy "
            "and seventeen — stands easy among his grazing "
            "flock in the deep green valley, staff loose "
            "across his shoulders, the sheep spread "
            "unbothered around him — a boy who is, this "
            "morning, everything to these animals that the "
            "LORD will be to him: provider, protector, "
            "the reason nothing on this hillside wants for "
            "anything. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r150-b03", "out": "s03-david-begins-with-trust-not.jpeg", "seg": "n0b",
        "window": "12.47-15.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["PASTURE"],
        "narration": "David begins with trust, not scarcity.",
        "must_show": "trust as landscape — the flock feeding unhurried across abundant green, no scanning, no huddling; plenty and safety as the opening premise.",
        "must_not_show": "no halo; NOTHING anxious anywhere in the flock — ease is the picture.",
        "scene": (
            "The psalm opens its books on abundance: the "
            "flock feeds unhurried across the deep green — "
            "heads down in the sweet grass, lambs sprawled "
            "flat in the warmth, not one ear turned to scan "
            "the ridgelines, not one animal pressed against "
            "another in worry — a hillside whose whole "
            "economy runs on the fact of its shepherd — "
            "trust, published in wool across a green page, "
            "before one hard thing has been mentioned. No "
            "people are needed in this frame."
        ),
    },
    {
        "id": "v2-r150-b04", "out": "s04-it-starts-like-this.jpeg", "seg": "n0",
        "window": "5.12-6.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID"],
        "narration": "It starts like this:",
        "must_show": "the first line — close on the king's pen touching the scroll's first line in lamplight; the song beginning in ink. Script indistinct.",
        "must_not_show": "no halo; NO readable text — the pen's touch and fresh ink line only.",
        "scene": (
            "The most-loved poem in the world starts as one "
            "wet line of ink: close on the reed pen's tip "
            "touching down at the scroll's head in the "
            "lamp's warm ring — the first stroke drawn "
            "steady, the line still shining wet, the king's "
            "scarred knuckles quiet around the reed — three "
            "thousand years of deathbeds and cradles and "
            "green Sunday mornings, all waiting downstream "
            "of the sentence this hand is beginning. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r150-b05", "out": "s05-he-maketh-me-to-lie.jpeg", "seg": "s2",
        "window": "21.34-27.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["PASTURE"],
        "narration": (
            "He maketh me to lie down in green pastures: he leadeth me "
            "beside the still waters."
        ),
        "must_show": "SCRIPTURE-EXACT: the verse itself — sheep LYING DOWN in the deep green, and the stream's GLASS-STILL pool holding the sky; the psalm's most famous picture, exact.",
        "must_not_show": "no halo; the water STILL as glass (never rushing); the lying-down general.",
        "scene": (
            "The two famous images share one sheltered "
            "valley: across the deep spring green the flock "
            "lies DOWN — folded legs, settled wool, chins "
            "on the grass — while beside them the stream "
            "widens into a pool gone still as glass, "
            "holding the willows and the sky upside down "
            "without a ripple — grass a sheep can trust "
            "and water a sheep can drink without fear of "
            "the current: the whole verse, lying quietly "
            "in one valley. No people are needed in this "
            "frame."
        ),
    },
    {
        "id": "v2-r150-b06", "out": "s06-the-image-is-deliberate-a.jpeg", "seg": "n1a",
        "window": "28.97-33.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "PASTURE"],
        "narration": "The image is deliberate: a sheep lies down only when it feels safe.",
        "must_show": "the fact behind the image — close on one ewe folded fully down at rest, eyes soft, unafraid — with the young shepherd's legs standing near; safety as the precondition.",
        "must_not_show": "no halo; the ewe's ease TOTAL — soft eyes, settled breath; his nearness the reason.",
        "scene": (
            "Shepherds know what the poets borrowed: close "
            "on one ewe folded fully down in the sweet "
            "grass — legs tucked, wool settled, the dark "
            "eyes gone soft and half-lidded — and standing "
            "near enough to touch, the young shepherd's "
            "steady legs and grounded staff — because a "
            "sheep is a walking list of fears, and it lies "
            "down for exactly one reason: somebody it "
            "trusts is standing guard over the moment. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r150-b07", "out": "s07-he-restoreth-my-soul-the.jpeg", "seg": "s3a + n1b",
        "window": "34.86-42.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "PASTURE"],
        "narration": (
            "He restoreth my soul: The Shepherd does more than keep David "
            "alive; he brings him back when he is spent."
        ),
        "must_show": "SCRIPTURE-EXACT: the restoring — the young shepherd lifting a spent, cast ewe back onto her feet, steadying her until she stands; restoration as a shepherd's real work.",
        "must_not_show": "no halo; the ewe SPENT, not injured — cast and weary; the lift gentle and practiced.",
        "scene": (
            "Restoring a soul looks like this on a "
            "hillside: the young shepherd crouches over a "
            "cast ewe — down too long, legs folded wrong, "
            "too spent to right herself — and gathers her "
            "up with practiced arms, setting her back on "
            "her feet and holding steady while the legs "
            "remember their job — not rescue from death, "
            "something quieter and more common: brought "
            "BACK, stood up, breathed alongside until "
            "walking works again — the verse every worn-"
            "out believer was written for. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r150-b08", "out": "s08-he-leadeth-me-in-the.jpeg", "seg": "s3b",
        "window": "44.36-48.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "PASTURE"],
        "narration": "he leadeth me in the paths of righteousness for his name's sake.",
        "must_show": "SCRIPTURE-EXACT: the right path — the flock following the young shepherd single-file along a true worn path on the hillside; led, not driven; he AHEAD.",
        "must_not_show": "no halo; DIRECTION — the shepherd ahead, the flock following the path he chose.",
        "scene": (
            "Right paths are chosen from the front: the "
            "young shepherd walks AHEAD along the worn "
            "hillside track, and behind him the flock "
            "follows single-file — nose to tail down the "
            "path he picked, past the drop he knows about "
            "and the bad water he does not stop at — led, "
            "never driven, every safe step of theirs "
            "riding on his knowledge of the ground — a "
            "shepherd's route-craft, staked on his own "
            "name every time the flock arrives whole. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r150-b09", "out": "s09-the-guarantee-is-the-own.jpeg", "seg": "n2",
        "window": "50.02-54.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "PASTURE"],
        "narration": "The guarantee is the Shepherd's own character, not David's performance.",
        "must_show": "for-his-name's-sake — the shepherd's steady back leading on; the flock's safety resting visibly on HIM, not on any sheep's merit.",
        "must_not_show": "no halo; the composition weights the SHEPHERD — the flock ordinary, the leader the guarantee.",
        "scene": (
            "Notice whose reputation the safety rides on: "
            "the shepherd's steady back leads on up the "
            "path, staff swinging its easy rhythm — and "
            "behind him the flock is just a flock: some "
            "obedient, some straggling, one lamb wandering "
            "a step wide and being whistled back — nothing "
            "in their performance holding the system up — "
            "the whole guarantee walking in front of them, "
            "in the character of the one whose name is on "
            "the flock. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r150-b10", "out": "s10-everything-after-that-opening-line.jpeg", "seg": "n0b",
        "window": "15.21-19.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID"],
        "narration": "Everything after that opening line shows what the Shepherd's care looks like.",
        "must_show": "the song unfolding — the king writing on in lamplight, and through the window the green remembered hills bright with morning; the two worlds of the psalm in one frame.",
        "must_not_show": "no halo; script indistinct; the WINDOW carries the memory-world.",
        "scene": (
            "The poem is a window with a desk in front of "
            "it: the king writes on in the lamp's warm "
            "ring — line after line filling the scroll — "
            "while through the chamber window behind him "
            "the remembered hills stand green and "
            "morning-bright, further away than any window "
            "should reach — every verse he sets down "
            "another mile of that country: pasture, pool, "
            "path, and the darker ground coming — care, "
            "itemized by a man who received it first. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r150-b11", "out": "s11-yea-though-i-walk-through.jpeg", "seg": "s4",
        "window": "55.47-64.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "GORGE"],
        "narration": (
            "Yea, though I walk through the valley of the shadow of death, "
            "I will fear no evil: for thou art with me; thy rod and thy "
            "staff they comfort me."
        ),
        "must_show": "SCRIPTURE-EXACT: the valley — the shepherd and flock passing THROUGH the deep-shadowed gorge, rod and staff in his hands, the bright far end visible; real dark, no fear imagery beyond it.",
        "must_not_show": "ABSOLUTE: no death imagery, no bones, no spectres — real deep shadow and the THROUGH; rod and staff both visible.",
        "scene": (
            "The dark part of the route is on the map and "
            "the shepherd walks it anyway: down the gorge's "
            "shadowed floor the little procession moves — "
            "true deep shade, the rock walls close, the "
            "flock bunched and quiet — and at their centre "
            "the shepherd with the ROD in one fist for "
            "whatever the dark holds and the STAFF in the "
            "other for the flock's own stumbling — while "
            "far ahead, small and certain, the gorge's "
            "bright doorway of daylight waits: THROUGH, "
            "says the whole picture; this valley is a "
            "road, not a residence. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r150-b12", "out": "s12-notice-what-changes-here-up.jpeg", "seg": "n3",
        "window": "66.40-70.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID"],
        "narration": "Notice what changes here: up to now David has been saying He.",
        "must_show": "the grammar noticed — the king's face lifting from the scroll mid-thought, pen paused; the discovery arriving in the writing.",
        "must_not_show": "no halo; the pause READABLE — pen lifted, eyes away, the noticing.",
        "scene": (
            "The poet catches his own pronoun changing: the "
            "king's pen stops mid-line and his face lifts "
            "from the scroll, eyes gone away into the "
            "middle distance of the chamber — HE leadeth; "
            "HE restoreth; HE, HE, all down the sunlit "
            "verses — and then the valley entered the poem, "
            "and something in the grammar moved closer — "
            "the discovery arriving now in the lamplight, "
            "pen in the air, that the dark did something "
            "to the distance. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r150-b13", "out": "s13-in-the-valley-he-starts.jpeg", "seg": "n3",
        "window": "70.43-77.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "GORGE"],
        "narration": (
            "In the valley he starts saying You. He gets closer to the "
            "Shepherd in the dark, not further away."
        ),
        "must_show": "the nearness in the dark — IN the gorge: a sheep pressed hard against the shepherd's legs, his hand down on its head; THOU-art-with-me as physical closeness.",
        "must_not_show": "ABSOLUTE: no death imagery; the closeness the whole frame — pressed wool, resting hand, deep shade.",
        "scene": (
            "The pronoun changed because the distance did: "
            "in the gorge's deepest shade a ewe presses "
            "hard against the shepherd's legs — flank to "
            "shin, wool crushed close, walking in his "
            "stride the way fear walks in trust — and his "
            "free hand comes down to rest on her head as "
            "they move — THOU art with me: not a doctrine "
            "at this depth of shadow but a pressure, warm "
            "and immediate, at exactly the place the dark "
            "presses hardest — closer in the valley than "
            "anywhere on the sunlit grass. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r150-b14", "out": "s14-thou-preparest-a-table-before.jpeg", "seg": "s5a",
        "window": "78.51-82.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABLE"],
        "narration": "Thou preparest a table before me in the presence of mine enemies:",
        "must_show": "SCRIPTURE-EXACT: the table — the spread wooden table in open golden country, laid full; on the FAR ridgeline, vague distant silhouettes watching, unable to approach.",
        "must_not_show": "ABSOLUTE: the enemies FAR and vague — ridge silhouettes only, never close, never detailed; the table's calm the picture.",
        "scene": (
            "The strangest banquet in scripture is set in "
            "the open on purpose: the wooden table stands "
            "spread in the golden hill-country — cloth "
            "laid, bread stacked, the horn of oil and the "
            "generous cup in their places — while far off "
            "on the ridgeline a scatter of vague "
            "silhouettes stands watching, small as thorn "
            "bushes and exactly as able to interfere — a "
            "meal prepared with unhurried care in full "
            "view of everything that wishes it could "
            "prevent it. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r150-b15", "out": "s15-even-danger-has-to-watch.jpeg", "seg": "n4a",
        "window": "84.44-87.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABLE", "DAVID"],
        "narration": "Even danger has to watch while the Shepherd provides.",
        "must_show": "the calm meal — the guest (young David) seated and EATING at ease at the table, back straight, unhurried; the far watchers still on their ridge, still helpless.",
        "must_not_show": "ABSOLUTE: enemies stay far silhouettes; the guest's EASE the doctrine — eating slowly in full view.",
        "scene": (
            "The provocation of the table is how slowly he "
            "eats at it: young David sits at the spread "
            "cloth in the golden light, tearing bread "
            "without hurry, cup at his hand, back straight "
            "and shoulders easy — while the ridge's far "
            "silhouettes hold their distance, present, "
            "watching, and perfectly helpless — safety "
            "performed at dinner pace in the presence of "
            "everything that objects to it: the "
            "Shepherd's table, where danger's whole role "
            "is spectator. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r150-b16", "out": "s16-thou-anointest-my-head-with.jpeg", "seg": "s5b",
        "window": "89.12-92.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABLE", "DAVID"],
        "narration": "thou anointest my head with oil; my cup runneth over.",
        "must_show": "SCRIPTURE-EXACT: the anointing and the overflow — a host's hand pouring oil onto the seated guest's head, AND the cup filled past its brim, running onto the cloth.",
        "must_not_show": "no halo; the overflow REAL — wine over the brim, pooling; the oil's pour gentle on the head.",
        "scene": (
            "The host's generosity gets physically out of "
            "hand: from above, a steady hand tips the horn "
            "and the oil comes down bright onto the guest's "
            "bowed head — the old extravagant welcome, "
            "running warm at the hairline — while on the "
            "cloth the cup has already passed its brim, "
            "wine trembling over the lip and spreading its "
            "dark generous ring into the weave — anointed "
            "and overfilled at the same table, by a host "
            "whose measures simply do not stop at full. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r150-b17", "out": "s17-this-is-welcome-and-abundance.jpeg", "seg": "n4b",
        "window": "94.78-98.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["TABLE"],
        "narration": "This is welcome and abundance, not bare survival.",
        "must_show": "the abundance itself — the table close: bread broken open, oil bright, the run-over cup shining in the gold light; more than enough as the point.",
        "must_not_show": "no halo; the spread GENEROUS, never gaudy — a shepherd's riches: bread, oil, wine, light.",
        "scene": (
            "Count what is on the cloth and notice the "
            "arithmetic: bread broken open past what one "
            "guest eats, the oil-horn still half full "
            "after the anointing, the cup shining in its "
            "own spilled ring, the gold light lying across "
            "all of it like a second tablecloth — nothing "
            "rationed anywhere, nothing measured to "
            "survive on — a table set by Someone whose "
            "idea of enough starts where ours runs over. "
            "No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r150-b18", "out": "s18-surely-goodness-and-mercy-shall.jpeg", "seg": "s6a",
        "window": "99.58-103.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "PASTURE"],
        "narration": "Surely goodness and mercy shall follow me all the days of my life:",
        "must_show": "SCRIPTURE-EXACT: the following — the flock heading home at warm dusk with the shepherd walking BEHIND them; the following made of the shepherd himself, rear guard of goodness.",
        "must_not_show": "no halo; DIRECTION — flock ahead toward home, shepherd BEHIND; the pursuit-position exact.",
        "scene": (
            "At the day's end the shepherd changes position "
            "and the verse is born: the flock strings out "
            "ahead down the homeward path in the warm dusk "
            "— and BEHIND them, where the stragglers and "
            "the wolves and the night all live, the "
            "shepherd walks rear guard, staff easy, eyes "
            "on every trailing lamb — goodness and mercy "
            "in their true station: not up front where "
            "you can watch them, but behind you, where "
            "you are weakest, following all the way home. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r150-b19", "out": "s19-david-pictures-those-gifts-not.jpeg", "seg": "n5a",
        "window": "105.44-110.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID", "PASTURE"],
        "narration": (
            "David pictures those gifts not trailing weakly behind, but "
            "pursuing him."
        ),
        "must_show": "the pursuit — the shepherd striding ENERGETICALLY after the flock, closing distance on a straggler, purposeful; following as active chase.",
        "must_not_show": "no halo; the stride VIGOROUS — pursuit, not drift; the straggler being caught up to.",
        "scene": (
            "The Hebrew word is closer to hunted-down than "
            "tagging-along: the shepherd's easy walk breaks "
            "into a purposeful stride — closing hard on a "
            "straggling lamb that has fallen back into the "
            "dusk, his staff swinging with intent, ground "
            "disappearing under him — goodness that will "
            "not let the slowest sheep drift out of its "
            "reach, mercy that RUNS when the gap opens — "
            "pursued, all the days of his life, by exactly "
            "the two hunters a soul wants on its trail. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r150-b20", "out": "s20-and-i-will-dwell-in.jpeg", "seg": "s6b",
        "window": "111.66-114.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["PASTURE"],
        "narration": "and I will dwell in the house of the LORD forever.",
        "must_show": "SCRIPTURE-EXACT: the arriving — the warm-lit fold-house at dusk, its door standing open, the flock streaming IN; home as the psalm's destination.",
        "must_not_show": "no halo; the door OPEN and warm; DIRECTION — inward, home; lamplight physical.",
        "scene": (
            "The song's last road leads to a lit doorway: "
            "the stone fold-house stands warm against the "
            "dusk with its wide door open and lamplight "
            "lying out across the threshold — and the "
            "flock streams IN, wool brushing the "
            "doorposts, animal after animal crossing from "
            "the cooling dark into the kept warmth — "
            "dwelling, the verse calls it: not visiting, "
            "not passing through — the house of the LORD "
            "receiving its own for good, which is where "
            "every road in the psalm was always going. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r150-b21", "out": "s21-the-song-ends-where-every.jpeg", "seg": "n5b",
        "window": "116.51-121.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["DAVID"],
        "narration": (
            "The song ends where every sheep longs to be: safely in the "
            "Shepherd's presence."
        ),
        "must_show": "the double rest — the flock folded asleep in the lamplit fold; and the old king's finished scroll beside the quiet harp, his face at peace; both worlds closed at rest.",
        "must_not_show": "no halo; the TWO rests in one frame-pair feel — sheep safe, psalmist at peace; script indistinct.",
        "scene": (
            "Both halves of the poet come home in the last "
            "verse: in the lamplit fold the flock lies "
            "folded and breathing slow, safe inside the "
            "Shepherd's kept walls — and at the palace "
            "table the finished scroll lies curled beside "
            "the quiet harp, the old king leaned back with "
            "his eyes closed and his face gone to peace — "
            "the boy from the pastures and the king from "
            "the wars, both, at the end of the song, "
            "exactly where every sheep alive longs to be: "
            "in the presence, safe, home. Every figure "
            "has two arms, two hands and one head."
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
