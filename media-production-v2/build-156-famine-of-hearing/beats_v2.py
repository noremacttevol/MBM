#!/usr/bin/env python3
"""V2 beat map — row 156, build-156-famine-of-hearing (Amos 8:11-12).

COVERAGE: 22 pictures over 122.6 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Amos 8 KJV):
  8:11  "Behold, the days come, saith the Lord GOD, that I will send
        a FAMINE in the land, NOT a famine of bread, nor a thirst
        for water, but of HEARING THE WORDS OF THE LORD."
  8:12  "And they shall WANDER FROM SEA TO SEA, and from the north
        even to the east, they shall RUN TO AND FRO to seek the word
        of the LORD, and SHALL NOT FIND IT."

ROW INTENT: the word-famine row (BRIDGE, companion to rows 152/155):
plenty on the tables, starvation of the soul; the ache as PROOF the
word exists; the famine as the hour before the harvest. Ends with
the meal set again and a place left open.

RENDERING LAWS:
  - AMOS and the GATE are ROW 152's — locks byte-identical to
    build-152; face-board Amos against 152.
  - The famine is NEVER physical hunger depicted: every table is
    FULL, every well brims — the starvation is in eyes and empty
    scroll-niches. No starvation imagery, ever.
  - The wandering (b13/b16) is map-scale futility with dignity —
    small searchers crossing vast lands, earnest, never mocked.
  - b19's shape-as-proof: a carved wall-niche exactly LAMP-SHAPED,
    empty and waiting — the ache's logic in stone.
  - b22's close: a set table whose centrepiece is an OPEN BOOK
    among the loaves, one empty stool drawn back toward the viewer.
    Script indistinct everywhere.

TIME OF DAY ARC (intentional): the warning at the gate in full day;
the plenty-yet-hollow frames in flat abundant noon; the searching
across changing horizons (dawn ridge, noon valley, dusk shore); the
ache frames at lamplit evening; the pre-harvest dawn; the close in
warm supper lamplight.

CHANGING CONDITIONS (kept OUT of the locks): the tables — full
throughout (the famine is elsewhere); the searchers — setting out,
scattering, empty-handed; the final table — set, with the book, and
one place open.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row). AMOS
# and GATE are byte-identical to build-152.
LOCKS = {
    "AMOS": (
        "AMOS LOCK: Amos is the same man in every shot — a sturdy "
        "plain herdsman of about forty-five: sun-blackened, "
        "thick-wristed, a rough dark beard, in a coarse DARK "
        "GOAT-BROWN tunic with a wide leather belt and a herdsman's "
        "scrip (never cream, never white); a working man's stance "
        "always — the ordinariness is the point."
    ),
    "GATE": (
        "GATE LOCK: the town gate and market — a stone gateway with "
        "benches, market stalls crowding its shadow, townsfolk in "
        "varied earth-toned and fine dark robes. The same gate "
        "throughout."
    ),
    "SEEKERS": (
        "SEEKERS LOCK: the searching people — varied earnest "
        "travellers in earth-toned robes of brown, rust, olive and "
        "slate (no cream — only Jesus wears cream) with staffs and "
        "road-bundles; all ages, varied faces, dignified in their "
        "seeking, never mocked."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r156-b01", "out": "s01-the-prophet-amos-gave-his.jpeg", "seg": "n1",
        "window": "0.28-2.88", "wide": True, "jesus": False, "ref": False,
        "locks": ["AMOS", "GATE"],
        "narration": "The prophet Amos gave his people a strange warning.",
        "must_show": "the warning given — Amos at the town gate before the market crowd, the strange word beginning; row 152's man at row 152's gate.",
        "must_not_show": "no halo; AMOS per 152's lock exactly; the crowd's puzzlement starting.",
        "scene": (
            "The herdsman-prophet is back at the gate with a "
            "stranger word than last time, the camera looking "
            "through the gateway past the market crowd's "
            "backs: Amos plants himself on the worn "
            "threshold-stones — the same goat-brown tunic, "
            "the same thick working wrists — and begins a "
            "warning that furrows every brow in earshot, "
            "because it is about famine, and every stall "
            "around him is heaped with food. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r156-b02", "out": "s02-but-not-the-kind-you.jpeg", "seg": "n1",
        "window": "5.02-7.17", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "But not the kind you are picturing.",
        "must_show": "the misdirection — a granary FULL to its rafters, grain heaped gold and abundant; the famine you pictured, cancelled.",
        "must_not_show": "no halo; the plenty TOTAL — heaped, secure, undramatic.",
        "scene": (
            "Whatever famine the word conjured, the "
            "storehouse contradicts it: the granary stands "
            "full to its rafter-shadows — grain heaped in "
            "golden dunes past the measuring posts, sacks "
            "ranked deep along both walls, not one empty "
            "corner in the whole cool dim plenty — the "
            "picture everyone's mind drew at the word "
            "FAMINE, painted over in abundance before the "
            "prophet's sentence even finishes. No people "
            "are needed in this frame."
        ),
    },
    {
        "id": "v2-r156-b03", "out": "s03-it-would-be-a-famine.jpeg", "seg": "n2",
        "window": "12.89-17.30", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It would be a famine of a different kind — a hunger for the word of God.",
        "must_show": "the true scarcity — a synagogue's scroll-niche standing EMPTY, the reading-stand bare, dust in the light; the word's absence as architecture.",
        "must_not_show": "no halo; the emptiness EXACT — niche and stand bare; nothing destroyed, just absent.",
        "scene": (
            "The famine's true warehouse is this small "
            "empty alcove: the synagogue's scroll-niche "
            "stands bare — the shelf swept, the cloth "
            "folded, no rollers standing in their worn "
            "places — and below it the reading-stand holds "
            "nothing but dust turning in the window's "
            "light — no fire took them, no army: the words "
            "have simply grown scarce, and the room built "
            "around hearing them stands quiet as a dry "
            "well. No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r156-b04", "out": "s04-a-time-when-the-living.jpeg", "seg": "n2",
        "window": "17.30-24.87", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "A time when the living voice from heaven grew scarce, and "
            "people ached for it without always knowing what the ache even "
            "was."
        ),
        "must_show": "the unnamed ache — a figure at a dusk window, fed and housed and staring out at nothing nameable; the hollow that has no word yet.",
        "must_not_show": "no halo; the ache INTERIOR — comfort all around, the eyes elsewhere.",
        "scene": (
            "The ache arrives years before its name does: "
            "at the dusk window a figure stands with supper "
            "finished behind them and the lamp lit and "
            "every visible need met — staring out at the "
            "darkening hills with the particular "
            "unfocused longing of a person missing "
            "something they cannot list — a hunger with no "
            "shelf in the house, for a voice they have "
            "never heard and somehow remember. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r156-b05", "out": "s05-a-famine-is-coming-he.jpeg", "seg": "n1",
        "window": "2.88-5.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["AMOS", "GATE"],
        "narration": "A famine is coming, he said.",
        "must_show": "the word landing — close on Amos's grave warning face at the gate; the sentence's weight before its twist.",
        "must_not_show": "no halo; gravity PLAIN — a herdsman's directness.",
        "scene": (
            "The word FAMINE clears its own space in the "
            "market noise: close on Amos's sun-blackened "
            "face as he says it — level, grave, without "
            "one grain of theatre — a man who has watched "
            "flocks starve in dry years using the heaviest "
            "word a farm country knows, and meaning it — "
            "coming, he says; days are coming — while "
            "behind him the stalls stand heaped and the "
            "wells brim, and nobody yet understands. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r156-b06", "out": "s06-you-could-go-about-your.jpeg", "seg": "n3",
        "window": "25.43-35.18", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "You could go about your days, eat your fill, and still feel a "
            "hollow place inside that no meal could reach — a quiet starving "
            "of the soul for something true and living from God."
        ),
        "must_show": "the fed hollow — the row-141 register: a man leaned back from a FULL finished meal, eyes searching the middle distance; the part food cannot reach, starving quietly.",
        "must_not_show": "no halo; the table FULL and finished; the emptiness in the EYES only.",
        "scene": (
            "The starving happens on a full stomach: the "
            "man leans back from a finished supper — bowl "
            "scraped, bread reduced to crumbs, the cup "
            "drained twice — and his eyes have gone away "
            "over the lamp into the middle distance, "
            "searching a horizon the room does not "
            "contain — fed to the ribs and hollow "
            "somewhere north of them, in the unfurnished "
            "room every soul keeps for a voice from "
            "heaven, currently empty, currently aching. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r156-b07", "out": "s07-there-would-be-bread-on.jpeg", "seg": "n1",
        "window": "7.17-12.31", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "There would be bread on the tables and water in the wells, and "
            "still the land would starve."
        ),
        "must_show": "the paradox panorama — laden tables in the lane, a brimming well, plenty everywhere — and the faces above it joyless, distant; the land starving through its abundance.",
        "must_not_show": "no halo; NO physical hunger anywhere — the starvation entirely in the faces.",
        "scene": (
            "The paradox seats itself down the whole lane: "
            "tables stand laden outside the doorways — "
            "bread stacked, olives glistening, the well at "
            "the lane's head brimming to its stone lip — "
            "and above all that plenty the faces are "
            "strangely joyless: eating without relish, "
            "drawing water without thanks, full people "
            "wearing the distant look of the "
            "unaccountably poor — a land starving in the "
            "one pantry no harvest restocks. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r156-b08", "out": "s08-behold-the-days-come-saith.jpeg", "seg": "kv11",
        "window": "35.76-49.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["AMOS", "GATE"],
        "narration": (
            "Behold, the days come, saith the Lord GOD, that I will send a "
            "famine in the land, not a famine of bread, nor a thirst for "
            "water, but of hearing the words of the LORD:"
        ),
        "must_show": "SCRIPTURE-EXACT: the full verse — Amos proclaiming at the gate, one hand toward the heaped stalls (not bread), the other toward the empty distance (the hearing); the two-hands contrast.",
        "must_not_show": "no halo; the TWO directions readable — plenty dismissed, absence named.",
        "scene": (
            "The verse is delivered with both hands "
            "working: one sweeps the heaped market stalls "
            "and the brimming well — NOT of bread, NOT of "
            "water, the plenty dismissed with a turn of "
            "the wrist — and the other rises empty toward "
            "the wide quiet sky — but of HEARING — the "
            "words of the LORD — Amos at the gate naming "
            "the one shortage no caravan can remedy, "
            "while the crowd looks from his full hand to "
            "his empty one and begins, slowly, to "
            "understand. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r156-b09", "out": "s09-and-when-people-feel-that.jpeg", "seg": "n4",
        "window": "50.70-54.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["SEEKERS"],
        "narration": "And when people feel that kind of hunger, they do what hungry people do.",
        "must_show": "the rising to search — at dawn, seekers shouldering staffs and road-bundles at their doorways, setting out; hunger becoming motion.",
        "must_not_show": "no halo; the setting-out EARNEST — provisioned, purposeful, dignified.",
        "scene": (
            "Hunger has always known exactly one response: "
            "in the dawn light the doorways give up their "
            "seekers — a father shouldering the road-"
            "bundle, an old woman taking her staff from "
            "its corner, a young man cinching sandals on "
            "the step — households setting out the way "
            "hungry people have set out since hunger "
            "began: toward wherever the rumour of food "
            "is — except the food these doorways lack is "
            "a word, and nobody is sure of its country. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r156-b10", "out": "s10-they-go-looking.jpeg", "seg": "n4",
        "window": "54.51-55.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["SEEKERS"],
        "narration": "They go looking.",
        "must_show": "the scattering — from one crossroads, seekers taking every road at once toward every horizon; the search fanning out.",
        "must_not_show": "no halo; the fan-out READABLE — every direction taken from one point.",
        "scene": (
            "From the crossroads the search takes every "
            "road at once: seekers fan out along all four "
            "ways — north toward the hills, east into the "
            "rising light, small figures diminishing down "
            "each dusty spoke with their staffs swinging — "
            "no two parties choosing the same horizon, "
            "because nobody knows which horizon keeps the "
            "word — looking, everywhere, which is what "
            "you do when anywhere might hold it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r156-b11", "out": "s11-they-search-high-and-low.jpeg", "seg": "n4",
        "window": "55.82-62.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["SEEKERS"],
        "narration": (
            "They search high and low, near and far, hoping to stumble on "
            "the thing that will finally fill them."
        ),
        "must_show": "high and low — seekers checking a ridge shrine above and a valley well below in one frame; the search thorough and empty-handed.",
        "must_not_show": "no halo; both checks EMPTY — the shrine bare, the well only water; dignity in the searching.",
        "scene": (
            "They check the high places and the low ones "
            "in the same long afternoon: on the ridge a "
            "pair of seekers stoop into a wayside shrine "
            "and find its niche bare — while below in the "
            "valley others lean over the well's lip as if "
            "the word might live where the water does, "
            "and draw up only water — high and low, near "
            "and far, thorough as hunger makes people — "
            "and everywhere the same polite emptiness "
            "where the filling thing should be. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r156-b12", "out": "s12-but-think-about-what-that.jpeg", "seg": "n7",
        "window": "95.01-97.44", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "But think about what that hunger really means.",
        "must_show": "the reflective turn — a seeker paused on the road at evening, staff planted, face gone thoughtful; the hunger itself becoming the clue.",
        "must_not_show": "no halo; the pause GENUINE — thought arriving mid-journey.",
        "scene": (
            "Mid-road, the search pauses to examine "
            "itself: a seeker stops with staff planted in "
            "the evening light, road-dust to the knee, "
            "and the tired face goes suddenly thoughtful — "
            "the first stillness of the whole hungry "
            "journey — because a question has caught up "
            "with him between towns: what does it MEAN, "
            "this specific ache — where did a soul learn "
            "to miss something it has never tasted? "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r156-b13", "out": "s13-amos-saw-them-wandering-from.jpeg", "seg": "n5",
        "window": "62.81-71.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["SEEKERS"],
        "narration": (
            "Amos saw them wandering from one end of the world to the "
            "other, running here and there, chasing every rumor of where "
            "the word of God might still be found."
        ),
        "must_show": "the map-scale wandering — a vast landscape from shore to far ranges, small seeker-parties scattered across it on every road and pass; the world-wide chase.",
        "must_not_show": "no halo; the seekers SMALL against the vastness — earnest, scattered, dignified.",
        "scene": (
            "The prophecy's map fills with small hurrying "
            "figures, the camera set high on the ridge "
            "taking the whole land from the side: from the grey "
            "shore at one edge to the far blue ranges at "
            "the other, the seeker-parties move tiny "
            "along every visible road — a file crossing "
            "the river ford, two specks on the high pass, "
            "a knot hurrying the coast track after the "
            "newest rumour — the whole world walked from "
            "end to end by people chasing a word, exactly "
            "as the herdsman said they would. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r156-b14", "out": "s14-but-in-a-famine-of.jpeg", "seg": "n6",
        "window": "71.91-76.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["SEEKERS"],
        "narration": "But in a famine of the word, the seeking alone does not satisfy.",
        "must_show": "the unsatisfied search — a seeker kneeling at yet another bare niche at dusk, hands resting empty on the cold stone shelf; effort without finding.",
        "must_not_show": "no halo; the emptiness QUIET — no despair-theatre; tired honest hands on bare stone.",
        "scene": (
            "The hundredth empty shelf feels like the "
            "first: at dusk the seeker kneels before yet "
            "another wayside niche — swept, bare, cold — "
            "and lets his tired hands rest open on the "
            "stone where the word was supposed to be — no "
            "theatrics left in him, just the quiet "
            "arithmetic of a search that has spent its "
            "legs and purse and found the shelves of the "
            "whole country empty — seeking, faithful and "
            "footsore, and not the same as finding. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r156-b15", "out": "s15-they-looked-and-looked-and.jpeg", "seg": "n6",
        "window": "76.03-82.96", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "They looked, and looked, and could not lay hold of it — "
            "because what they were hungry for had grown rare in the land."
        ),
        "must_show": "the empty grasp — close: a reaching hand closing on dusk air where nothing is; the could-not-lay-hold made physical.",
        "must_not_show": "no halo; the closing hand EMPTY — air between the fingers; the light failing gently.",
        "scene": (
            "The search's whole result fits in one closing "
            "hand: it reaches into the failing dusk light — "
            "fingers spreading, then folding — and closes "
            "on air, exactly air, the nothing between "
            "them complete — looked, and looked, from sea "
            "to sea and shelf to shelf, and could not lay "
            "HOLD — not because the hands were weak but "
            "because the thing they were built to hold "
            "had grown rare in the land, and rarity is "
            "the one distance walking cannot cross. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r156-b16", "out": "s16-and-they-shall-wander-from.jpeg", "seg": "kv12",
        "window": "83.57-93.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["SEEKERS"],
        "narration": (
            "And they shall wander from sea to sea, and from the north even "
            "to the east, they shall run to and fro to seek the word of the "
            "LORD, and shall not find it."
        ),
        "must_show": "SCRIPTURE-EXACT: sea to sea — the wandering at the SHORE: seekers on the grey tideline having reached the land's very edge, the sea barring further search; the verse's geography complete.",
        "must_not_show": "no halo; the shore the LIMIT — the search run out of land; dignity intact.",
        "scene": (
            "The search reaches the place where land "
            "stops keeping its promises: on the grey "
            "tideline the seekers stand at the world's "
            "wet edge — staffs planted in the sand, "
            "road-bundles sagging, the sea running out "
            "ahead of them to a horizon with no more "
            "roads in it — sea to sea completed, north "
            "to east run through — the verse's whole "
            "geography walked to its coastline, and the "
            "word of the LORD not found on any mile of "
            "it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r156-b17", "out": "s17-so-the-only-question-is.jpeg", "seg": "n8",
        "window": "116.06-118.31", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "So the only question is a hopeful one.",
        "must_show": "the hopeful pivot — a listener's face at lamplight, brightening with the question's warmth; hope after the long ache.",
        "must_not_show": "no halo; the brightening SUBTLE — hope, not rapture.",
        "scene": (
            "After all the empty shelves, the question "
            "arrives warm: a listening face in the "
            "lamplight, and across it the slow "
            "brightening — brows easing, the corners of "
            "the mouth lifting a degree — of somebody "
            "realizing the story they are inside has a "
            "hopeful last chapter — the famine described, "
            "the ache explained, and now a question "
            "coming whose answer might be supper. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r156-b18", "out": "s18-you-do-not-ache-for.jpeg", "seg": "n7",
        "window": "97.44-100.10", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "You do not ache for what was never real.",
        "must_show": "the ache as evidence — a hand pressed flat at the chest over the hollow place; the longing itself testifying.",
        "must_not_show": "no halo; the press GENTLE — locating, not clutching.",
        "scene": (
            "The hollow place is itself a kind of "
            "testimony: a hand comes to rest flat against "
            "the chest — over the exact interior room "
            "where the ache keeps its address — locating "
            "it the way you locate a bruise, gently, with "
            "respect — because no one aches for a "
            "fiction: thirst proves water, hunger proves "
            "bread, and this particular hollow proves a "
            "voice that once filled it and can fill it "
            "again. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r156-b19", "out": "s19-the-very-fact-that-a.jpeg", "seg": "n7",
        "window": "100.10-107.60", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The very fact that a soul can starve for God's word is proof "
            "that such a word exists, and that it was always meant to be "
            "found."
        ),
        "must_show": "shape-as-proof — a carved wall-niche exactly LAMP-SHAPED, empty in the evening light; the fit implying the lamp; the ache's logic in stone.",
        "must_not_show": "no halo; the niche's SHAPE unmistakable — carved for exactly one thing, waiting.",
        "scene": (
            "The empty niche is an argument in stone: "
            "carved into the wall, exactly lamp-shaped — "
            "the base's round seat, the little vault "
            "sized to a flame's height, the soot-shadow "
            "where light once sat — empty now in the "
            "evening, and eloquent: nobody carves a "
            "lamp-shaped hollow by accident, and no soul "
            "wears a word-shaped hunger for a word that "
            "never was — the fit is the proof, and the "
            "proof says: made to be found. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r156-b20", "out": "s20-so-a-famine-is-never.jpeg", "seg": "n8",
        "window": "108.20-113.26", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So a famine is never the end of the story; it is the ache that "
            "comes right before the harvest."
        ),
        "must_show": "the hour before harvest — a grain field at dawn one day from ripe, heads heavy and gold-turning; the hungry season's last morning.",
        "must_not_show": "no halo; the almost-ripeness READABLE — heavy heads, gold arriving; nothing yet cut.",
        "scene": (
            "Famines keep a calendar, and this is its "
            "last page: the grain field stands at dawn "
            "one day short of the sickle — heads bowed "
            "heavy, the green giving up its last hold to "
            "gold, the whole field leaning together in "
            "the first light like a held breath — the "
            "hungry season's final morning, with the "
            "harvest so near you can smell the bread in "
            "it — because the ache, in God's arithmetic, "
            "has only ever come right before the "
            "filling. No people are in this frame."
        ),
    },
    {
        "id": "v2-r156-b21", "out": "s21-god-does-not-leave-his.jpeg", "seg": "n8",
        "window": "113.26-116.06", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "God does not leave his people hungry forever.",
        "must_show": "the setting-out of bread — warm loaves being carried to a long table, the meal being laid again; provision returning in hands.",
        "must_not_show": "no halo; the laying-out IN MOTION — loaves arriving, the table filling.",
        "scene": (
            "The table is being laid again, and by hands: "
            "warm loaves come to the long boards two and "
            "three at a time — set down, arranged, "
            "steaming faintly in the lamplight — the "
            "pitcher following, the bowls, the good "
            "cloth smoothed ahead of each arrival — a "
            "meal assembling with the unhurried certainty "
            "of a promise being kept — because the famine "
            "was never the policy: only the ache before "
            "the feeding, and the feeding is being "
            "carried in. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r156-b22", "out": "s22-when-the-word-is-set.jpeg", "seg": "n8",
        "window": "118.31-122.27", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "When the word is set before you again, will you sit down and "
            "eat?"
        ),
        "must_show": "the closing invitation — the set table with an OPEN BOOK at its centre among the loaves, ONE empty stool drawn back toward the viewer; the place held open. Script indistinct.",
        "must_not_show": "no halo; NO readable text; the empty stool's invitation exact — drawn back, waiting.",
        "scene": (
            "The last frame sets your place: the long "
            "table stands laid in the warm lamplight — "
            "loaves, cup, pitcher — and at its centre, "
            "among the food, lies the meal the whole "
            "famine was about: an open book, its "
            "indistinct lines waiting like bread — and "
            "one stool stands drawn back from the "
            "table's near side, empty, angled toward "
            "whoever is watching — the word, set before "
            "you again; the seat, pulled out; the "
            "question, yours. No people are in this "
            "frame."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # GATE: share row 152's promoted GATE frame when it exists (byte-identical
    # lock, same place). Promote-first from b01 otherwise.
}
# === end PLACE-PLATES ===
