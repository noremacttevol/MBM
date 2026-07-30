#!/usr/bin/env python3
"""V2 beat map — row 30, build-30-net (Matthew 13:47-50).

COVERAGE: 25 pictures over 141.3 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 13:47-50 KJV):
  v47   "the kingdom of heaven is like unto a NET, that was cast into the
        sea, and GATHERED OF EVERY KIND" — a great dragnet swept wide; the
        gathering is indiscriminate and comes FIRST. ⚑ Flag J (CONTENT-CARE
        §3 row 30): 'the net gathers EVERY kind first' — the wide-open
        gathering beats are the heart and the warmth of the row.
  v48   "when it was FULL, they drew to SHORE, and SAT DOWN, and gathered
        the good into vessels, but cast the bad away" — the sorting happens
        only AFTER everyone is ashore, done seated and deliberate.
  v49   "the ANGELS shall come forth, and sever the wicked from among the
        just" — per the row-21 precedent (no angels painted, no heaven
        painted), the angels are NOT depicted. The narration says plainly
        whose job the sorting is (b19: 'The angels do it. God does it.') —
        the pictures stay inside the parable's own fish-and-shore imagery.
  v50   "and shall cast them into the FURNACE OF FIRE: there shall be
        wailing and gnashing of teeth" — ⚑ Flag J RESTRAINED: painted as
        the set-aside catch carried away at dusk toward a small DISTANT
        shore fire, thin smoke, grave tone — never close flames, never any
        person or creature shown in fire, no suffering depicted.
  Spoken IN THE HOUSE (Matthew 13:36 context). Rows 25/28/29 staged that
  room three ways already — THIS build's frame beats put Jesus at the deep
  window of the room with the sea visible beyond it, gesturing the story
  out onto the water. New composition, no repeat.

TIME OF DAY: frame beats are warm afternoon window light. The parable runs
a fisherman's real day: bright MORNING for the casting and the drag,
midday for the full net and the beaching, long GOLD AFTERNOON for the
seated sorting, and a grave DUSK for the setting-aside and distant-fire
beats (correct and deliberate — the end-of-the-world beats should feel
like day's end). The closing grace beats return to wide bright morning —
the cast that includes everyone.

CHANGING CONDITION (kept OUT of the locks): the net's state — folded,
flying, sunk and dragging, bursting full, beached — and the day's hour
move beat to beat and are never locked.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "CREW": (
        "FISHING CREW LOCK: the fishermen are the same four men in every "
        "shot — a heavy grey-bearded elder with a deep chest; a broad "
        "black-bearded man of forty; and two lean sun-darkened younger "
        "brothers with short dark beards. They wear work-worn wool tunics "
        "kilted to the knee in DARK UMBER-BROWN, DEEP RUSSET, DARK OLIVE "
        "and DUSTY INDIGO respectively, with rope belts (never cream, "
        "never white; only Jesus wears cream). Their faces are shown "
        "clearly."
    ),
    "DRAGNET": (
        "DRAGNET LOCK: one great old dragnet — a long deep wall of "
        "hand-knotted dark-brown cordage with small stone weights along "
        "its bottom rope and wooden floats along its top rope, patched in "
        "places with newer cord. The same net in every net beat."
    ),
    "SEA": (
        "SEA OF GALILEE LOCK: open water on the Sea of Galilee — clear "
        "green-blue water, low brown-gold hills ringing the far shore, "
        "and one broad-beamed weathered wooden fishing boat with a single "
        "mast, its deck boards, thwarts and gunwales worn pale. Figures "
        "in the boat always stand or kneel visibly INSIDE it, deck under "
        "their feet, gunwale around them."
    ),
    "BEACH": (
        "SORTING BEACH LOCK: a wide pebble-and-sand beach with the boat's "
        "bow run up onto it, woven baskets and large clay vessels ranged "
        "on the stones, a driftwood log, and the green-blue water lapping "
        "the shingle. The same beach in every shore beat."
    ),
    "HOUSE-ROOM": (
        "HOUSE ROOM LOCK: the main room of a Capernaum house — thick "
        "honey-stone walls, rush mats and low cushions on a beaten-earth "
        "floor, a shelf of clay vessels in shadow, and one deep-set "
        "window through which the distant green-blue of the sea shows "
        "beyond the rooftops. Warm afternoon light."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r030-b01", "out": "s01-jesus-told-one-more-short.jpeg", "seg": "n1",
        "window": "0.28-5.99", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": (
            "Jesus told one more short story about the kingdom of heaven, and "
            "this time he set it out on the water."
        ),
        "must_show": "the frame — Jesus beside the deep window of the house room, one hand gesturing out toward the strip of distant sea visible through it, disciples turning to look.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the sea through the window is small and distant — a view, not a backdrop.",
        "scene": (
            "In the warm afternoon light of the stone room Jesus stands "
            "beside the deep-set window, one hand lifted toward the "
            "small bright strip of distant green-blue sea showing beyond "
            "the rooftops through it, his face turned back toward the "
            "disciples seated on the mats — and two of them are already "
            "twisting round to follow his hand toward the water. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b02", "out": "s02-again-the-kingdom-of-heaven.jpeg", "seg": "j1",
        "window": "6.60-13.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "SEA"],
        "narration": (
            "Again, the kingdom of heaven is like unto a net, that was cast "
            "into the sea, and gathered of every kind:"
        ),
        "must_show": "SCRIPTURE-EXACT: the cast — the great dragnet flying out over the water in a wide arc from the boat, floats fanned along its top rope, the crew mid-heave inside the hull.",
        "must_not_show": "no halo, glare or rim-light; every man visibly INSIDE the boat, deck under his feet; the net reads as one great flying wall of mesh.",
        "scene": (
            "Bright morning on the open green-blue water: from the "
            "broad-beamed boat the great dark dragnet is caught mid-air "
            "in a wide flying arc, its wooden floats fanned along the "
            "top rope and its stone weights pulling the bottom edge "
            "down toward the surface — while inside the hull the four "
            "fishermen lean into the heave, the grey elder braced at "
            "the stern, the two young brothers' arms still extended "
            "from the throw, every man's feet planted on the deck "
            "boards inside the gunwale. Low gold hills ring the far "
            "shore. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b03", "out": "s03-but-notice-whose-job-it.jpeg", "seg": "n8",
        "window": "102.13-104.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": "But notice whose job it is.",
        "must_show": "a close shot of the sorting hands at work over the catch — experienced, deliberate, authorised; the deciding hands, not ours.",
        "must_not_show": "no halo, glare or rim-light; hands and fish only fill the frame — the point is WHOSE hands.",
        "scene": (
            "A close shot in long gold afternoon light: the grey elder's "
            "thick experienced hands moving over the heaped catch, one "
            "hand lifting a fat silver fish toward the basket while the "
            "other steadies the pile — deliberate, practised, unhurried "
            "hands that have earned the right to decide, filling the "
            "whole frame with the work. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r030-b04", "out": "s04-picture-fishermen-throwing-a-great.jpeg", "seg": "n2",
        "window": "14.94-22.09", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "SEA"],
        "narration": (
            "Picture fishermen throwing a great wide net off the side of the "
            "boat, letting it sink down and drag through the whole sea."
        ),
        "must_show": "the drag — the net's float-line stretched in a long curve across the water behind the moving boat, the crew paying out rope over the gunwale.",
        "must_not_show": "no halo, glare or rim-light; the floats trace the net's whole sunken width — the sweep must read as HUGE.",
        "scene": (
            "From above and behind the boat's stern quarter in bright "
            "morning light: the line of small wooden floats stretches in "
            "a long slow curve across the green-blue water far behind "
            "the boat, tracing the whole sunken width of the dragging "
            "net beneath — while at the stern two of the crew pay the "
            "heavy tow ropes out over the gunwale, backs braced, and "
            "the elder leans on the steering oar inside the hull. The "
            "wake runs soft and wide. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r030-b05", "out": "s05-and-here-is-the-first.jpeg", "seg": "n3",
        "window": "22.73-26.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["DRAGNET", "SEA"],
        "narration": (
            "And here is the first beautiful thing. That net does not pick and "
            "choose."
        ),
        "must_show": "under the surface — the great dark wall of mesh moving through sunlit green water, fish of every size ahead of it, none turned away.",
        "must_not_show": "no halo, glare or rim-light; an underwater view is correct here — the net as a wide welcoming wall, not a trap's menace.",
        "scene": (
            "Beneath the surface in green sunlit water: the great dark "
            "wall of knotted mesh moves through the frame at a slow "
            "diagonal, stone weights brushing the pale sandy bottom and "
            "floats dimpling the bright ceiling of the surface above — "
            "and ahead of it swim fish of every size and kind at once, "
            "fat silver ones, small darting ones, one strange whiskered "
            "bottom-fish, all being gathered by the same wide sweep. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b06", "out": "s06-it-sweeps-up-every-kind.jpeg", "seg": "n3",
        "window": "26.95-37.55", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "SEA"],
        "narration": (
            "It sweeps up every kind of fish there is: big ones, small ones, "
            "common ones, strange ones, everything the sea has in it, gathered "
            "in together."
        ),
        "must_show": "SCRIPTURE-EXACT: EVERY KIND — the net closing toward the boat, its narrowing circle of water boiling with visibly different fish, the crew hauling from inside the hull.",
        "must_not_show": "no halo, glare or rim-light; the variety must READ — clearly different sizes, shapes and colours in one gathering; all hands inside the boat.",
        "scene": (
            "The net's float-line has closed into a wide circle beside "
            "the boat and the ringed water inside it churns with every "
            "kind of fish at once — broad silver-flanked ones rolling, "
            "small green-backed ones flickering in shoals, a long thin "
            "pike-like fish, a dark flat one — while the four fishermen "
            "haul the closing ropes hand over hand from inside the "
            "hull, feet braced wide on the deck boards, the gunwale "
            "pressing their thighs. Bright late-morning light. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b07", "out": "s07-the-net-is-not-fussy.jpeg", "seg": "n4",
        "window": "38.22-40.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["DRAGNET"],
        "narration": "The net is not fussy about who gets caught up in it.",
        "must_show": "a close shot at the mesh itself — utterly different fish pressed side by side in the same knotted cords, none sorted, none refused.",
        "must_not_show": "no halo, glare or rim-light; the fish are alive and vigorous, not suffering — caught, not harmed.",
        "scene": (
            "A close shot of the wet dark mesh bulging with its mixed "
            "catch just at the waterline: a fat silver bream pressed "
            "flank to flank with a small green sardine, a whiskered "
            "catfish and a fine spotted fish side by side in the same "
            "hand-knotted cords, water streaming bright off the ropes — "
            "every kind held together by the one net, none refused. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b08", "out": "s08-the-gathering-is-wide-open.jpeg", "seg": "n4",
        "window": "40.72-42.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["DRAGNET", "SEA"],
        "narration": "The gathering is wide open.",
        "must_show": "the widest frame of the row — the whole sweep of the float-line across the open water under a big sky, the boat small at one end.",
        "must_not_show": "no halo, glare or rim-light; scale and openness — the net's reach dwarfs everything else in the frame.",
        "scene": (
            "The widest view of the morning: under a great bright sky "
            "the line of wooden floats sweeps in an enormous open curve "
            "across the green-blue water, spanning nearly the whole "
            "frame, with the weathered boat small at its far end and "
            "the low gold hills lying distant beyond — a gathering arm "
            "flung wide enough for a whole sea. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b09", "out": "s09-nobody-swimming-in-that-sea.jpeg", "seg": "n4",
        "window": "42.66-48.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["DRAGNET", "SEA"],
        "narration": (
            "Nobody swimming in that sea is too ordinary, or too far gone, to "
            "be swept up into it."
        ),
        "must_show": "the least of the catch honoured — under the surface, one small plain drab fish, alone near the bottom, with the great net's sweep coming for it too.",
        "must_not_show": "no halo, glare or rim-light; the little fish is utterly ordinary — and the net's whole width is unmistakably coming to include it.",
        "scene": (
            "Under the green sunlit water near the pale sandy bottom "
            "one small drab mud-coloured fish hangs alone in the open, "
            "plain as a pebble, far from every shoal — and behind it "
            "the whole towering dark sweep of the net moves in, wide "
            "enough for a thousand and coming, unmistakably, for this "
            "one as well. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r030-b10", "out": "s10-which-when-it-was-full.jpeg", "seg": "j48",
        "window": "49.28-56.76", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "BEACH"],
        "narration": (
            "Which, when it was full, they drew to shore, and sat down, and "
            "gathered the good into vessels, but cast the bad away."
        ),
        "must_show": "SCRIPTURE-EXACT: the beaching — the four men hauling the bursting net up the shingle in one straining line, the boat's bow already run up on the stones.",
        "must_not_show": "no halo, glare or rim-light; the haul is heavy TEAM work — one rope, four backs, the full net furrowing the shingle behind them.",
        "scene": (
            "At the wide pebble beach under high midday light the four "
            "fishermen haul in one straining line up the shingle, the "
            "thick tow rope over four shoulders, wet backs bowed — and "
            "behind them the bursting dark net furrows the stones at "
            "the waterline, heavy with its silver-flashing mixed catch, "
            "while the boat's bow stands run up on the beach beside "
            "them. Baskets and clay vessels wait ranged on the stones "
            "ahead. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b11", "out": "s11-when-the-net-is-full.jpeg", "seg": "n5",
        "window": "57.82-63.85", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "BEACH"],
        "narration": (
            "When the net is full, the fishermen drag the whole heavy thing up "
            "onto the shore, and they sit down beside it."
        ),
        "must_show": "SCRIPTURE-EXACT: 'and sat down' — the crew SEATED around the beached catch, settling to the work without hurry; the sitting itself is the beat.",
        "must_not_show": "no halo, glare or rim-light; nobody stands over the catch — all four are down on stones, log or heels; deliberateness, not drama.",
        "scene": (
            "The great net lies beached and heaped with its mixed catch "
            "on the shingle, and around it the four fishermen have SAT "
            "DOWN — the grey elder on the driftwood log, the broad man "
            "cross-legged on the stones, the two young brothers on "
            "their heels — sleeves pushed up, baskets drawn close, "
            "settling to a long deliberate work in the early-afternoon "
            "light with the lapping water behind them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b12", "out": "s12-and-only-then-once-everyone.jpeg", "seg": "n5",
        "window": "63.85-68.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": (
            "And only then, once everyone is already gathered in, does any "
            "sorting begin."
        ),
        "must_show": "the order of grace made visible — the WHOLE catch safe ashore in the net's lap, and only the first single fish just now being lifted from it.",
        "must_not_show": "no halo, glare or rim-light; the emphasis is sequence — everything gathered FIRST, sorting only beginning; one fish in hand, all the rest still together.",
        "scene": (
            "Close over the beached net's brimming lap of mixed fish, "
            "safe ashore to the last one — and above it just one hand, "
            "the elder's, lifting the very first silver fish out toward "
            "an empty basket at the frame's edge, the whole rest of the "
            "gathered catch still lying together untouched below. The "
            "sorting is one fish old; the gathering was total. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b13", "out": "s13-they-gather-the-good-fish.jpeg", "seg": "n6",
        "window": "69.57-76.35", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": (
            "They gather the good fish carefully into baskets, keeping them, "
            "valuing them, not losing a single one."
        ),
        "must_show": "SCRIPTURE-EXACT: the keeping — good fish laid with CARE into the woven baskets and clay vessels, two baskets already full, gentle two-handed handling.",
        "must_not_show": "no halo, glare or rim-light; the good fish are handled like value — two hands, laid not tossed; full baskets show nothing is lost.",
        "scene": (
            "In long gold afternoon light the crew works seated around "
            "the catch: the broad black-bearded man lays a fat silver "
            "fish into a woven basket with both hands, careful as a "
            "man shelving bread, while beside him two baskets already "
            "stand filled to their brims and one of the young brothers "
            "steadies a clay vessel for the next — every good fish "
            "placed, none dropped, none left. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b14", "out": "s14-and-the-ones-that-cannot.jpeg", "seg": "n7",
        "window": "77.00-79.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": "And the ones that cannot be kept, they set aside.",
        "must_show": "⚑ Flag J RESTRAINED: the setting-aside — a small separate heap apart from the baskets, the elder's hand placing one there, his face grave and unhurried.",
        "must_not_show": "no halo, glare or rim-light; NO violence, no flinging — set aside, quietly; the small heap is simply apart, and the beat is sober, not cruel.",
        "scene": (
            "Close in the late gold light: the elder's weathered hand "
            "sets one dark unusable fish down on a small separate heap "
            "on the bare stones, apart from the full baskets — placed, "
            "not thrown — and above the motion his grey-bearded face "
            "is grave and unhurried, a man doing a necessary thing "
            "without pleasure. The brimming baskets stand warm at the "
            "frame's edge. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r030-b15", "out": "s15-jesus-said-that-is-a.jpeg", "seg": "n7",
        "window": "79.99-83.64", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": "Jesus said that is a picture of how things finally end.",
        "must_show": "back in the room — Jesus grave now, the disciples sobered, the afternoon light gone lower and warmer across the mats.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gravity without threat — the room simply stiller than before.",
        "scene": (
            "The stone room again, the window light now lower and more "
            "amber across the rush mats: Jesus sits with his hands "
            "quiet in his lap, his face grave and gentle at once, and "
            "the listening disciples have sobered with him — the "
            "youngest looking down at the mat, the elder ones very "
            "still. Beyond the deep window the little strip of distant "
            "sea has gone pale in the late light. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b16", "out": "s16-so-shall-it-be-at.jpeg", "seg": "j2",
        "window": "84.24-91.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": (
            "So shall it be at the end of the world: the angels shall come "
            "forth, and sever the wicked from among the just"
        ),
        "must_show": "SCRIPTURE-EXACT, kept in the parable's imagery (no angels painted): the sorting at day's end — dusk on the beach, the work nearly done, full baskets in a row and the small set-aside heap apart, long shadows, solemn stillness.",
        "must_not_show": "no halo, glare or rim-light; NO angels, no sky-figures, no heaven painted (row-21 precedent); dusk colouring is deliberate — the end-of-day gravity carries the verse.",
        "scene": (
            "Dusk has come down over the sorting beach: the row of "
            "filled baskets and clay vessels stands dark and heavy "
            "along the shingle, the small set-aside heap lies apart "
            "near the waterline, and the four fishermen work on in "
            "near-silhouette against the last deep amber over the "
            "water, their long shadows running up the stones — the "
            "whole beach gone solemn and final as the light goes. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b17", "out": "s17-and-shall-cast-them-into.jpeg", "seg": "j50",
        "window": "92.61-98.78", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": (
            "And shall cast them into the furnace of fire: there shall be "
            "wailing and gnashing of teeth."
        ),
        "must_show": "⚑ Flag J RESTRAINED: the youngest fisherman carrying the set-aside basket away down the darkening beach toward a SMALL DISTANT fire near the far rocks, thin smoke rising, his walk heavy and grave.",
        "must_not_show": "no halo, glare or rim-light; the fire is SMALL, FAR and low — no close flames, nothing and no one shown in fire, no suffering depicted; the gravity is in the walk and the distance.",
        "scene": (
            "In the last blue-grey of dusk the youngest fisherman walks "
            "away down the darkening shingle with the set-aside basket "
            "held against his chest, his head down and his pace heavy — "
            "and far ahead of him, small at the beach's rocky far end, "
            "a low fire burns with one thin line of smoke standing up "
            "into the fading sky. The full baskets and his crewmates "
            "remain warm and close in the near frame behind him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b18", "out": "s18-there-is-a-real-end.jpeg", "seg": "n8",
        "window": "99.79-102.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["BEACH"],
        "narration": "There is a real end, and a real sorting.",
        "must_show": "the two destinations in one still frame — the row of full baskets near and warm, the small distant fire's thin smoke far down the dusk beach beyond them.",
        "must_not_show": "no halo, glare or rim-light; a still, sober frame — no people; the two facts side by side, with the kept baskets dominant.",
        "scene": (
            "A still dusk frame on the quiet beach: in the near "
            "foreground the row of brimming fish baskets stands solid "
            "and close on the shingle, dark and safely full — and far "
            "beyond them down the empty curve of the shore the tiny "
            "distant fire shows as a low point of warmth with its one "
            "thin thread of smoke against the last light over the "
            "water. Near and far, kept and not. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b19", "out": "s19-the-angels-do-it-god.jpeg", "seg": "n8",
        "window": "104.15-106.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": "The angels do it. God does it.",
        "must_show": "authority in the hands — the elder alone at the sorting in dusk light, and NO other hands anywhere near the catch; the work belongs to him.",
        "must_not_show": "no halo, glare or rim-light; no angels painted; one sorter only in frame — everyone else's hands visibly at rest or absent.",
        "scene": (
            "In the deep dusk light the grey elder alone bends over the "
            "last of the catch, his two hands the only hands in the "
            "frame at the work — while at the frame's edge the broad "
            "fisherman sits back on the driftwood log with his own "
            "hands folded still in his lap, watching, taking no part "
            "in the deciding. The sorting belongs to one. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b20", "out": "s20-at-the-very-end-it.jpeg", "seg": "n8 + n9",
        "window": "106.67-113.20", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": (
            "At the very end. It was never handed to us to do. So here is what "
            "the little story leaves you with."
        ),
        "must_show": "the room at the story's landing — Jesus turning his open hand toward the disciples, giving the parable's weight over to them gently.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gentleness after gravity — the open hand releases, it does not point.",
        "scene": (
            "In the low amber window light Jesus turns one open hand "
            "palm-up toward the seated disciples, unhurried, handing "
            "the story's weight over to them as gently as passing "
            "bread — and their faces take it differently, one relieved, "
            "one thoughtful, the youngest lifting his head as though "
            "released from something. The strip of distant sea beyond "
            "the window has gone dusk-pale. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b21", "out": "s21-you-do-not-have-to.jpeg", "seg": "n9",
        "window": "113.20-117.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "BEACH"],
        "narration": (
            "You do not have to spend your life deciding who belongs and who "
            "does not."
        ),
        "must_show": "the burden nobody has to carry — the two young brothers at the dusk waterline rinsing their hands in the shallows, the sorting behind them finished by another.",
        "must_not_show": "no halo, glare or rim-light; their postures are LIGHT — unburdened men done with a day's honest work, none of the deciding on their shoulders.",
        "scene": (
            "At the dusk waterline the two young brothers crouch side "
            "by side rinsing their hands and forearms in the dark "
            "shallows, shoulders loose, one saying something that makes "
            "the other laugh quietly — the finished sorting, the full "
            "baskets and the elder all behind them up the beach, none "
            "of it theirs to carry. The water laps soft around their "
            "wrists. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r030-b22", "out": "s22-that-is-not-your-net.jpeg", "seg": "n9 + n10",
        "window": "117.33-126.44", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "SEA"],
        "narration": (
            "That is not your net, and it is not your sorting. Your part is "
            "simply this: the net was cast for the whole sea, and it was cast "
            "for you."
        ),
        "must_show": "the cast again, made personal — bright morning returns; the great net flying wide over the water, its open arc sweeping TOWARD the camera's own place in the sea.",
        "must_not_show": "no halo, glare or rim-light; morning light returns deliberately here; the arc must open toward the viewer — the cast includes the one watching.",
        "scene": (
            "Bright morning light returns over the green-blue water: "
            "from the weathered boat the great dragnet flies out in its "
            "wide arc once more, floats fanned against the clean sky — "
            "but this time the open sweep of it curves out toward the "
            "camera's own low place at the water's surface, the "
            "gathering arm reaching across the frame for the very spot "
            "from which the picture is seen. The crew heaves inside "
            "the hull beyond. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r030-b23", "out": "s23-the-gathering-came-first-grace.jpeg", "seg": "n10",
        "window": "126.44-131.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "BEACH"],
        "narration": (
            "The gathering came first. Grace reached out wide enough to catch "
            "you up in it."
        ),
        "must_show": "the welcome of the net — a close shot of the small plain drab fish from the earlier beat lifted ashore in the elder's two cupped hands, kept.",
        "must_not_show": "no halo, glare or rim-light; it is the SAME small ordinary fish — and it goes to the basket, not the heap; tenderness in the big hands.",
        "scene": (
            "A close shot in warm morning light: cradled in the elder's "
            "two big cupped hands, the small drab mud-coloured fish "
            "from the deep water lies safe above the beached net — and "
            "the hands are carrying it toward the open woven basket at "
            "the frame's edge where the fine silver fish already lie. "
            "The plainest catch of the day, kept with the best. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b24", "out": "s24-that-is-how-good-he.jpeg", "seg": "n11",
        "window": "131.95-133.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": "That is how good he is.",
        "must_show": "a close portrait of Jesus in the dusk-warm room — the goodness itself, quiet in his face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a still, warm, close face — nothing else asked of the frame.",
        "scene": (
            "A close head-and-shoulders portrait of Jesus in the last "
            "warm amber of the window light, his warm brown eyes "
            "resting steady on the unseen listeners, the faintest "
            "settled smile inside the dark beard — goodness sitting in "
            "the face as plainly as tiredness sits in a workman's. The "
            "honey-stone wall holds the dusk warmth behind him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r030-b25", "out": "s25-he-threw-the-net-over.jpeg", "seg": "n11",
        "window": "133.48-141.05", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREW", "DRAGNET", "SEA"],
        "narration": (
            "He threw the net over the whole ocean of us, of every kind, so "
            "that not one soul who wanted to be found would be missed."
        ),
        "must_show": "the closing image — the widest morning frame: the great net's arc hanging over the whole bright sea, boat small beneath it, the water alive with every kind of fish rising toward the gathering.",
        "must_not_show": "no halo, glare or rim-light; generosity at full scale — the net wide as the frame, the sea full, nothing outside the sweep.",
        "scene": (
            "The widest, brightest frame of the row: under a great "
            "clean morning sky the dragnet's arc hangs at the top of "
            "its flight across nearly the whole width of the picture, "
            "floats strung like a written line against the light, the "
            "weathered boat and its straining crew small beneath it — "
            "and the green-blue water below is alive from edge to "
            "edge with rising fish of every size and kind, the whole "
            "sea inside the sweep of one cast. Every figure has two "
            "arms, two hands and one head."
        ),
    },
]
