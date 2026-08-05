#!/usr/bin/env python3
"""V2 beat map — row 118, build-118-jonah-god-who-relents (Jonah 1-4).

COVERAGE: 46 pictures over 262.1 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Jonah KJV):
  1:2   "Arise, go to NINEVEH, that GREAT CITY, and cry against it."
  1:3   Jonah flees to JOPPA, ships for TARSHISH — the exact opposite
        direction.
  1:4-15 the GREAT STORM; the lots fall on Jonah; his words: "TAKE ME
        UP, AND CAST ME FORTH INTO THE SEA... for my sake this great
        tempest is upon you." The casting is a SACRIFICE he asks for.
  1:17  "the LORD had PREPARED A GREAT FISH... Jonah was in the belly
        of the fish THREE DAYS AND THREE NIGHTS." — sent to CATCH and
        KEEP him, not to punish.
  2:9   the prayer's end: "SALVATION IS OF THE LORD."
  3:1-4 the second identical commission; the sermon: "YET FORTY DAYS,
        AND NINEVEH SHALL BE OVERTHROWN."
  3:5-10 the whole city REPENTS, king to beggar, sackcloth and
        fasting — "and God REPENTED of the evil... and he did it not."
  4:2   Jonah's confession: "I KNEW that thou art a GRACIOUS God, and
        MERCIFUL, SLOW TO ANGER, and of GREAT KINDNESS."
  4:11  the book's last word — God still arguing FOR mercy: "SHOULD
        NOT I SPARE NINEVEH... sixscore thousand persons... and also
        much cattle?"

RENDERING LAWS: God is NEVER embodied — the word comes to a listening
Jonah, over sea, over city. The casting-overboard is a REQUESTED
SACRIFICE — sailors lowering him with grief, never hurling with
violence. The fish is a great dark sea-creature, awesome not
monstrous; the belly a dark enclosing deep with faint sea-light,
painterly not gruesome. Nineveh's destruction NEVER happens and is
never previewed. The repentance is dignified city-wide sorrow.

TIME OF DAY ARC (intentional): the call at lamplit night; flight and
storm in green-black tempest dark; the deep in blue-black; the beach
at clean dawn; Nineveh under vast hazy day; the repentance at dusk
into lamplit night; the hill and the last argument in warm morning.

CHANGING CONDITION (kept OUT of the locks): Jonah's direction — away,
down, back, in, and finally seated arguing; the sea — raging, then
flat calm; the city — doomed on the calendar, then spared.
"""

# LOCKS: one entry per recurring person and per setting. Clothing colours
# stated POSITIVELY and dark — only Jesus wears cream (not in this row).
LOCKS = {
    "JONAH": (
        "JONAH LOCK: Jonah is the same man in every shot — about "
        "forty-five, stocky and strong, a short grizzled dark beard, "
        "a stubborn downturned mouth and honest angry eyes, in a "
        "DEEP SEA-GREEN robe with a DARK LEATHER belt (never cream, "
        "never white)."
    ),
    "SHIP": (
        "SHIP LOCK: the Tarshish ship — a broad wooden merchant "
        "vessel, one great square sail, high curved prow, cargo "
        "lashed amidships, a crew of weathered sailors in DARK "
        "salt-stained tunics. The same vessel and crew throughout."
    ),
    "FISH": (
        "FISH LOCK: the great fish — an immense dark-backed "
        "sea-creature, whale-vast, barnacle-flecked, with one huge "
        "calm eye; awesome and deliberate, never monstrous. The "
        "same creature throughout."
    ),
    "NINEVEH": (
        "NINEVEH LOCK: Nineveh — a colossal foreign city on a "
        "plain: tiered walls wide enough to drive chariots on, "
        "great gates flanked by carved WINGED-BULL statues, "
        "ziggurat towers in the haze. The same walls, gates and "
        "skyline throughout."
    ),
    "HILL": (
        "HILL LOCK: the watching hill — a dry rise east of the "
        "city with a single bare tree and a makeshift brush "
        "shelter, the great walls in full view below. The same "
        "rise and view throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r118-b01", "out": "s01-god-had-a-hard-errand.jpeg", "seg": "n1",
        "window": "0.28-3.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "God had a hard errand for a man named Jonah.",
        "must_show": "the man met — Jonah at his lamplit table at night, sturdy and settled; the errand about to arrive on an ordinary evening.",
        "must_not_show": "no figure of God; the ordinariness the setup — a man at supper, unwarned.",
        "scene": (
            "The book opens on an "
            "ordinary man at an ordinary "
            "lamp: Jonah at his table in "
            "the night quiet, stocky and "
            "settled, bread half-eaten, "
            "the stubborn mouth at rest — "
            "a prophet between errands, "
            "expecting nothing harder "
            "tonight than sleep — and "
            "the air of the little room "
            "already changing, the way "
            "air does, just before the "
            "word arrives. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b02", "out": "s02-he-was-to-go-to.jpeg", "seg": "n1",
        "window": "3.13-10.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": (
            "He was to go to Nineveh — a huge, violent, foreign city, the "
            "capital of the empire everyone in Israel was afraid of."
        ),
        "must_show": "the errand's address — Nineveh vast on its plain: tiered walls, winged-bull gates, ziggurats in haze; the feared capital at full intimidating scale.",
        "must_not_show": "no violence enacted — the menace carried by SCALE and foreignness alone.",
        "scene": (
            "The errand's address fills "
            "the horizon: Nineveh on its "
            "plain — walls tiered and "
            "endless, wide enough on top "
            "for chariots to race, the "
            "great gates flanked by "
            "stone winged bulls five "
            "men high, ziggurats "
            "standing in the heat-haze "
            "beyond — the capital of "
            "the empire whose name "
            "mothers in Israel used to "
            "make children come "
            "inside — huge, foreign, "
            "feared, and about to be "
            "warned. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b03", "out": "s03-and-this-is-how-the.jpeg", "seg": "n1",
        "window": "10.65-13.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "And this is how the word came to him.",
        "must_show": "the word arriving — Jonah's head lifting sharply from the lamp, the listening seizing him; the call's arrival on his face.",
        "must_not_show": "ABSOLUTE: no figure or source — the arrested listening carries it.",
        "scene": (
            "Mid-bite, the word finds "
            "him: Jonah's head coming up "
            "sharp from the lamplit "
            "bread, the honest angry "
            "eyes going wide and fixed "
            "on nothing the room "
            "contains — the whole sturdy "
            "frame stilled into "
            "listening the way prophets "
            "are seized, unasked and "
            "unmistakable — the errand "
            "arriving through the quiet "
            "with an address in it he "
            "will spend three chapters "
            "refusing. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b04", "out": "s04-arise-go-to-nineveh-that.jpeg", "seg": "gv1",
        "window": "13.62-22.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "NINEVEH"],
        "narration": (
            "Arise, go to Nineveh, that great city, and cry against it; for "
            "their wickedness is come up before me."
        ),
        "must_show": "SCRIPTURE-EXACT: the commission — Jonah risen at his door facing the far east horizon where the great city lies; the command's direction laid on the night.",
        "must_not_show": "ABSOLUTE: no figure as the voice — Jonah and the eastward night carry it.",
        "scene": (
            "The command stands him up "
            "and points him east: Jonah "
            "at his open door in the "
            "night, facing the far dark "
            "horizon beyond which the "
            "great city sprawls — ARISE, "
            "GO TO NINEVEH — the words "
            "laying the road out over "
            "the black hills mile by "
            "unwanted mile — CRY "
            "AGAINST IT — a warning to "
            "be carried to the empire "
            "of fear by one stocky "
            "reluctant man, whose face "
            "is already turning, "
            "slowly, the other way. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r118-b05", "out": "s05-go-to-that-great-city.jpeg", "seg": "n1b",
        "window": "23.79-29.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": (
            "Go to that great city and preach against it, God said, because "
            "I have seen how bad it has gotten."
        ),
        "must_show": "the errand weighed — close on Jonah's face working through the command: distaste, fear and calculation crossing it in turn.",
        "must_not_show": "no figure of God; the resistance forming visibly — the mouth's stubborn set deepening.",
        "scene": (
            "Close on a prophet doing "
            "unprophetic math: the "
            "command still ringing, and "
            "across the grizzled face "
            "the responses crossing in "
            "order — distaste first, at "
            "the very name of the "
            "place; then fear, honest "
            "and reasonable; and then, "
            "settling in behind the "
            "stubborn mouth, something "
            "harder than either: a "
            "calculation about mercy, "
            "and who might get it, "
            "that he does not like the "
            "answer to. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b06", "out": "s06-notice-what-that-actually-is.jpeg", "seg": "n1b",
        "window": "29.89-31.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": "Notice what that actually is.",
        "must_show": "the noticing — the great city again, but framed now as ADDRESSEE: the walls under a sky that is watching, the warning as attention.",
        "must_not_show": "no destruction imagery — the city being NOTICED, which is the mercy.",
        "scene": (
            "Look again at what just "
            "happened: the great feared "
            "city on its plain — and "
            "over it now, framed "
            "differently, the fact the "
            "narration is pointing at: "
            "heaven has NOTICED "
            "Nineveh — not written it "
            "off, not crossed it out, "
            "not turned its back — "
            "noticed it, enough to "
            "send a man on foot with "
            "a message — which is not "
            "how you treat a city you "
            "have given up on. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b07", "out": "s07-but-jonah-did-not-want.jpeg", "seg": "n2",
        "window": "36.51-39.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "But Jonah did not want mercy for people like that.",
        "must_show": "the refusal's root — close on Jonah's hardened face: not fear now but grudge; mercy for THEM the one thing he cannot stomach.",
        "must_not_show": "no cartoon villainy — an honest man's real grudge, human and recognizable.",
        "scene": (
            "Close on the book's real "
            "engine: not cowardice — "
            "the sturdy frame has "
            "never run from danger — "
            "but this, hardening the "
            "honest face like frost: "
            "PEOPLE LIKE THAT — the "
            "empire's butchers, his "
            "people's dread — and "
            "mercy, God's own brand "
            "of it, wide enough to "
            "reach even them if they "
            "so much as turned — the "
            "one outcome Jonah's "
            "wounded, human, "
            "recognizable heart cannot "
            "stomach being party to. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r118-b08", "out": "s08-he-found-a-ship-going.jpeg", "seg": "n2",
        "window": "40.14-48.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "SHIP"],
        "narration": (
            "He found a ship going the exact opposite way and sailed off, "
            "trying to put an ocean between himself and a God he thought "
            "was far too forgiving."
        ),
        "must_show": "SCRIPTURE-EXACT: the flight — Joppa's harbor: Jonah boarding the broad merchant ship, fare paid, the sail filling WESTWARD; the opposite direction under way.",
        "must_not_show": "no figure of God; the direction READABLE — sun/coast geometry putting Nineveh at his back.",
        "scene": (
            "At Joppa the refusal buys "
            "its ticket: Jonah up the "
            "gangplank of the broad "
            "merchant ship with his "
            "fare paid and his face "
            "set hard to the west — "
            "the great square sail "
            "filling for Tarshish, the "
            "farthest port a map "
            "could offer — the whole "
            "eastward errand put "
            "astern with the coast "
            "and the morning — a man "
            "spending good silver to "
            "put an ocean between "
            "himself and a mercy he "
            "considers dangerously "
            "oversized. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b09", "out": "s09-god-would-far-rather-warn.jpeg", "seg": "n1b",
        "window": "32.71-36.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": "God would far rather warn a wicked city than lose it.",
        "must_show": "the preference — Nineveh's gates at evening with its crowds streaming home: the city as PEOPLE, worth warning; the mercy's arithmetic in one view.",
        "must_not_show": "no destruction; the crowds HUMAN — families, children, workers at the gates.",
        "scene": (
            "The city resolves, the camera low in the gate's "
            "shadow taking the homeward stream from the side, into "
            "its true contents at "
            "evening: through the "
            "winged-bull gates the "
            "crowds stream home — "
            "porters and mothers, "
            "soldiers off duty "
            "carrying market figs, "
            "children riding "
            "shoulders, an old woman "
            "scolding a donkey — "
            "thousands on thousands of "
            "ordinary evenings inside "
            "the feared walls — the "
            "arithmetic of the "
            "warning laid bare: all "
            "this, God would far "
            "rather warn than lose. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b10", "out": "s10-a-great-storm-caught-the.jpeg", "seg": "n3",
        "window": "49.30-54.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHIP"],
        "narration": (
            "A great storm caught the ship, so fierce the sailors were sure "
            "they would all drown."
        ),
        "must_show": "SCRIPTURE-EXACT: the tempest — the ship overwhelmed in green-black seas: sail shredding, crew hauling and bailing, water bursting over the prow; terror at full sea-scale.",
        "must_not_show": "action-logic law — bailing OUT over the gunwale, ropes to real rigging; no one in the water yet.",
        "scene": (
            "The sea stands up, the camera braced at the stern "
            "behind the sailors' backs, against "
            "the runaway's road: green-"
            "black walls of water "
            "bursting over the high "
            "prow, the great sail "
            "shredding at its edges, "
            "sailors hauling double on "
            "real rigging while others "
            "fling bailed water OUT "
            "over the leeward gunwale "
            "in flying sheets — the "
            "broad ship climbing seas "
            "like hills and dropping "
            "into valleys that swallow "
            "the sky — a storm with "
            "an errand in it, and "
            "every hand aboard sure "
            "of drowning. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b11", "out": "s11-he-knew-it-already.jpeg", "seg": "n3",
        "window": "58.69-59.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "SHIP"],
        "narration": "He knew it already.",
        "must_show": "the knowing — close on Jonah amid the chaos: alone calm, guilt settled and certain; the storm's cause aware of itself.",
        "must_not_show": "no panic on him — the terrible calm of a man who knows exactly why.",
        "scene": (
            "In the middle of the "
            "screaming chaos, one calm "
            "face: Jonah braced at the "
            "mast with spray sheeting "
            "past him, and in the "
            "honest eyes none of the "
            "crew's wild guessing — "
            "only the settled, heavy "
            "certainty of a man who "
            "has known since the "
            "first gust exactly whose "
            "name this weather is "
            "written in — the storm's "
            "cause, standing quiet at "
            "the center of its "
            "effect, already deciding "
            "something. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b12", "out": "s12-his-prayer-ends-in-four.jpeg", "seg": "n5",
        "window": "119.02-120.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "His prayer ends in four words.",
        "must_show": "the prayer's end nearing — Jonah in the deep dark, face upturned, the prayer's last words gathering; surrender's edge.",
        "must_not_show": "the belly PAINTERLY dark — enclosing depth, faint blue sea-light, nothing gruesome.",
        "scene": (
            "In the deep enclosing dark "
            "the long prayer narrows "
            "to its point: Jonah's "
            "face upturned in the "
            "faint blue sea-light of "
            "the strangest sanctuary "
            "ever prayed in, the "
            "resentment prayed down "
            "to sediment, the running "
            "prayed out entirely — "
            "and rising in him now, "
            "four words wide, the "
            "sentence the whole "
            "three-day dark was "
            "carrying him toward. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b13", "out": "s13-take-me-up-and-cast.jpeg", "seg": "s112",
        "window": "64.72-73.16", "wide": True, "jesus": False, "ref": False,
        "locks": ["JONAH", "SHIP"],
        "narration": (
            "Take me up, and cast me forth into the sea; so shall the sea "
            "be calm unto you: for I know that for my sake this great "
            "tempest is upon you."
        ),
        "must_show": "SCRIPTURE-EXACT: the offer — Jonah shouting his own sentence over the storm to the stunned crew, arms open, pointing to the sea and himself; sacrifice proposed by its subject.",
        "must_not_show": "the crew's HORROR at the idea visible — no eagerness anywhere; his offer steady.",
        "scene": (
            "Over the storm's roar, the camera looking past "
            "the ringed sailors' backs, the "
            "passenger sentences "
            "himself: Jonah with his "
            "arms open to the stunned "
            "ring of sailors — TAKE ME "
            "UP, AND CAST ME FORTH — "
            "one hand at his own "
            "chest, the other flung "
            "at the raging green-"
            "black — FOR MY SAKE THIS "
            "TEMPEST — and on the "
            "salt-streaked faces "
            "around him, horror at "
            "the arithmetic: the one "
            "honest road out of the "
            "storm running straight "
            "over their passenger's "
            "life, offered by the "
            "passenger. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b14", "out": "s14-throw-me-in-he-said.jpeg", "seg": "n3b",
        "window": "74.73-80.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "SHIP"],
        "narration": (
            "Throw me in, he said. The sea will go quiet, because this "
            "storm is on me, not on you."
        ),
        "must_show": "the on-me — close on Jonah's steady storm-lit face making the case: ownership of the storm claimed whole; the crew's anguish around him.",
        "must_not_show": "no despair-theatrics — responsibility, taken like a man picking up a load.",
        "scene": (
            "Close on responsibility "
            "picking up its own load: "
            "Jonah's storm-lit face "
            "steady among the anguished "
            "crew, making the case "
            "against himself without "
            "one tremor of theater — "
            "ON ME, NOT ON YOU — the "
            "stubborn mouth that ran "
            "from an errand refusing, "
            "here at the edge of "
            "everything, to let "
            "strangers pay his fare — "
            "the first decent thing "
            "in the book, said loud "
            "enough to beat the wind. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b15", "out": "s15-he-would-rather-drown-than.jpeg", "seg": "n3b",
        "window": "80.16-87.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": (
            "He would rather drown than preach to Nineveh — but he would "
            "not let a boatful of strangers go down with him."
        ),
        "must_show": "the tangled heart — Jonah's face holding both truths: the grudge unbroken AND the decency real; a complicated man at full complexity.",
        "must_not_show": "neither truth erased — stubbornness and sacrifice in one expression.",
        "scene": (
            "Close on the most "
            "complicated face in the "
            "minor prophets: still "
            "stubborn to the bone — "
            "drowning genuinely "
            "preferable, even now, to "
            "preaching mercy at "
            "Nineveh — and beside the "
            "grudge, unerasable, the "
            "other thing: a boatful "
            "of pagan strangers he "
            "has known two days, whom "
            "he will not let pay for "
            "his running — a man "
            "wrong about the big "
            "thing and right about "
            "the near one, wearing "
            "both at once. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b16", "out": "s16-so-at-last-they-did.jpeg", "seg": "n3b",
        "window": "87.12-91.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "SHIP"],
        "narration": (
            "So at last they did the only thing left, and cast him into "
            "the raging sea."
        ),
        "must_show": "SCRIPTURE-EXACT rendered as sacrifice: the sailors LOWERING Jonah over the rail with gripping, grieving hands — release at the sea's edge, faces anguished; never a hurl.",
        "must_not_show": "ABSOLUTE: no violent throwing — a grieved lowering and letting go; the sea receiving, not detailed drowning.",
        "scene": (
            "They do it the way you do "
            "a thing you hate: four "
            "sailors easing Jonah "
            "over the heaving rail "
            "with gripped forearms "
            "and locked hands, "
            "lowering him toward the "
            "green-black roar while "
            "the rest turn their "
            "faces away — grief in "
            "every knuckle, prayers "
            "in a language he does "
            "not speak — and then "
            "the letting go: the "
            "hands opening at last, "
            "the sea taking its "
            "passenger, the deed done "
            "gently that could not "
            "be done at all any "
            "other way. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b17", "out": "s17-and-here-is-the-first.jpeg", "seg": "n4",
        "window": "92.49-98.05", "wide": True, "jesus": False, "ref": False,
        "locks": ["SHIP"],
        "narration": (
            "And here is the first surprise of this story. The sea should "
            "have been the end of him."
        ),
        "must_show": "the sea gone flat — the aftermath: the ship riding easy on water flattening to glassy calm, crew at the rail staring at the quiet; the storm's instant death.",
        "must_not_show": "Jonah not visible in the water — the CALM the subject; awe on the crew.",
        "scene": (
            "The instant he is taken — the camera behind the "
            "spared crew at the rail — "
            "the argument ends: the "
            "green-black fury "
            "flattening around the "
            "ship like a fist "
            "unclenching — waves "
            "dying mid-rise, the wind "
            "walking away across the "
            "water, the torn sail "
            "hanging suddenly slack "
            "in air gone soft — and "
            "along the rail the "
            "spared crew staring at "
            "a sea turned glassy "
            "calm over the place "
            "where their passenger "
            "went, beginning, every "
            "man of them, to fear "
            "his God properly. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b18", "out": "s18-instead-god-sent-a-great.jpeg", "seg": "n4",
        "window": "98.05-105.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["FISH"],
        "narration": (
            "Instead, God sent a great fish — not to punish Jonah, but to "
            "catch him, and carry him, and keep him alive in the deep."
        ),
        "must_show": "SCRIPTURE-EXACT: the prepared fish — beneath the calming surface: the immense dark creature rising deliberate through the blue toward the small sinking figure; rescue shaped like awe.",
        "must_not_show": "the fish AWESOME not monstrous — the calm eye, the deliberate rise; the catch imminent, not gruesome.",
        "scene": (
            "Beneath the flattening "
            "silver ceiling the rescue "
            "rises: the great fish — "
            "whale-vast, dark-backed, "
            "barnacle-flecked, its one "
            "huge eye calm as deep "
            "water itself — climbing "
            "deliberate through the "
            "blue toward the small "
            "sea-green figure sinking "
            "slowly down the light — "
            "not a punishment on the "
            "hunt but a vessel on "
            "schedule: prepared, "
            "aimed, and opening the "
            "deep's strangest door to "
            "catch a drowning "
            "runaway alive. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b19", "out": "s19-the-judgment-never-fell.jpeg", "seg": "n8",
        "window": "204.38-205.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": "The judgment never fell.",
        "must_show": "the unfallen — Nineveh whole under a clearing bright sky: walls intact, gates busy, the fortieth day arrived and nothing but morning; the never in one view.",
        "must_not_show": "ABSOLUTE: no destruction, not even clouds of threat remaining — the sky washed clean.",
        "scene": (
            "The fortieth day arrives "
            "and brings only morning: "
            "Nineveh whole on its "
            "plain under a sky washed "
            "bright and clean — the "
            "tiered walls intact to "
            "their last course, the "
            "winged-bull gates busy "
            "with ordinary traffic, "
            "washing strung between "
            "windows that were "
            "supposed to be rubble by "
            "now — the countdown "
            "completed, the calendar "
            "kept, and the judgment, "
            "against every schedule, "
            "simply never falling. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b20", "out": "s20-for-three-days-and-three.jpeg", "seg": "n5",
        "window": "106.23-110.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": (
            "For three days and three nights, in the dark, Jonah finally "
            "stopped running."
        ),
        "must_show": "SCRIPTURE-EXACT: the belly's stillness — Jonah seated in the dark enclosing deep, faint blue light, knees drawn up; the running finally stopped, stillness total.",
        "must_not_show": "PAINTERLY dark — enclosing curved depth and faint sea-light only; nothing anatomical or gruesome.",
        "scene": (
            "The running ends where no "
            "road goes: Jonah seated "
            "small in the enclosing "
            "dark, knees drawn up, the "
            "faint blue of deep-sea "
            "light breathing dimly "
            "through the strange "
            "curved gloom around him — "
            "no door to try, no ship "
            "to book, no west left "
            "anywhere — three days "
            "and three nights of the "
            "first stillness of his "
            "adult life, in the one "
            "waiting room on earth "
            "that runners cannot "
            "leave early. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b21", "out": "s21-from-the-belly-of-the.jpeg", "seg": "n5",
        "window": "110.78-119.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": (
            "From the belly of the fish he prayed, and his hard, resentful "
            "heart began at last to turn back toward the God who would not "
            "let him drown."
        ),
        "must_show": "the turning prayer — Jonah's hands unclenching into prayer in the faint blue dark, the hard face softening by degrees; resentment melting into address.",
        "must_not_show": "painterly dark maintained; the softening GRADUAL — a hard heart's slow thaw.",
        "scene": (
            "In the blue-black quiet "
            "the hard heart begins its "
            "thaw: the clenched "
            "fisherman's fists opening "
            "slowly into something "
            "like prayer, the stubborn "
            "downturned mouth moving "
            "over words it has not "
            "used in years — resentment "
            "melting off the honest "
            "face degree by degree as "
            "the fact underneath it "
            "surfaces at last: the God "
            "he ran from is the same "
            "God who just refused, at "
            "some expense, to let him "
            "drown. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b22", "out": "s22-salvation-is-of-the-lord.jpeg", "seg": "s29 + n5b",
        "window": "121.40-125.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "Salvation is of the LORD. Rescue belongs to God.",
        "must_show": "SCRIPTURE-EXACT: the four words — Jonah's upturned face at full surrender in the faint light: SALVATION IS OF THE LORD; the book's theology said from the deep.",
        "must_not_show": "painterly dark; the surrender COMPLETE — nothing held back in the face.",
        "scene": (
            "Four words, said from the "
            "bottom of everything: "
            "Jonah's face upturned in "
            "the faint blue dark, "
            "emptied of the grudge's "
            "last sediment, saying the "
            "whole theology of his "
            "strange book at last — "
            "SALVATION IS OF THE "
            "LORD — not of prophets, "
            "who run; not of ships, "
            "which founder; not of "
            "deserving, his or "
            "Nineveh's or anyone's — "
            "of the LORD — surrendered "
            "to, finally, in the one "
            "place with no exits. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b23", "out": "s23-that-is-the-whole-lesson.jpeg", "seg": "n5b",
        "window": "125.92-134.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["FISH"],
        "narration": (
            "That is the whole lesson of the fish, and Jonah says it from "
            "the one place on earth where he could not save himself and had "
            "nothing left to bargain with."
        ),
        "must_show": "the lesson's classroom — the great fish moving vast and deliberate through the deep blue toward the far pale coast; the carrier at its patient work.",
        "must_not_show": "the creature CALM — a vessel keeping course, awesome and unhurried.",
        "scene": (
            "The classroom swims: the "
            "great dark fish moving "
            "vast and unhurried "
            "through the blue fathoms, "
            "the one calm eye reading "
            "the water, the far pale "
            "smudge of coastline "
            "standing in the light "
            "ahead — a vessel on "
            "assignment, carrying in "
            "its patient dark the "
            "one passenger on earth "
            "with nothing left to "
            "bargain with — which is, "
            "the book observes, the "
            "exact condition under "
            "which human beings "
            "finally learn who rescue "
            "belongs to. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b24", "out": "s24-it-is-a-warning.jpeg", "seg": "n1b",
        "window": "31.71-32.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": "It is a warning.",
        "must_show": "the category named — the city's great gate close: the place a warning is for; a door that can still be knocked on.",
        "must_not_show": "no doom imagery — a warning's whole nature is that nothing has fallen yet.",
        "scene": (
            "Close on what the errand "
            "actually is: the great "
            "gate of the feared city "
            "in plain daylight — "
            "carved bulls, iron-bound "
            "doors, traffic passing "
            "through — a door, in "
            "other words: knockable, "
            "warnable, still standing "
            "wide — because a warning "
            "is by nature a mercy "
            "wearing work clothes: "
            "you do not send one to "
            "a city whose fate is "
            "sealed; you send one to "
            "a city whose fate is "
            "still, deliberately, "
            "open. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b25", "out": "s25-arise-go-unto-nineveh-that.jpeg", "seg": "jvA",
        "window": "134.99-142.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": (
            "Arise, go unto Nineveh, that great city, and preach unto it "
            "the preaching that I bid thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the second commission — Jonah on the dawn beach, salt-crusted and alive, head lifted to the same words again; the errand re-issued whole.",
        "must_not_show": "ABSOLUTE: no figure as the voice; no reproach in the light — the repeat clean of punishment.",
        "scene": (
            "On the clean dawn beach "
            "the same words find him "
            "again: Jonah on his knees "
            "in the wet sand, "
            "salt-crusted, wrung out, "
            "and entirely alive — and "
            "arriving through the "
            "morning air, word for "
            "patient word, the "
            "identical errand: ARISE, "
            "GO UNTO NINEVEH — no "
            "preface about the "
            "running, no invoice for "
            "the fish, no probation "
            "clause — the commission "
            "reissued as if the "
            "flight had never "
            "happened, which is its "
            "own kind of mercy. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b26", "out": "s26-so-he-ran.jpeg", "seg": "n2",
        "window": "39.53-40.14", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "So he ran.",
        "must_show": "the run — Jonah striding hard down the westward road away from the rising sun, bundle over shoulder; flight in two words.",
        "must_not_show": "the geometry CLEAR — sunrise at his back, west ahead.",
        "scene": (
            "Two words, one direction: "
            "Jonah striding hard down "
            "the coast road with his "
            "bundle over his shoulder "
            "and the sunrise squarely "
            "at his back — the "
            "errand's east shrinking "
            "behind him with every "
            "stubborn step, the sea's "
            "west opening ahead — a "
            "prophet in full flight "
            "from a command, walking "
            "with the particular "
            "energy of a man who "
            "knows exactly which "
            "direction he is wrong "
            "in. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b27", "out": "s27-the-fish-set-him-safe.jpeg", "seg": "n6",
        "window": "144.34-153.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "FISH"],
        "narration": (
            "The fish set him safe on dry land, and God gave him the exact "
            "same errand a second time — no mention of the running, no "
            "punishment attached."
        ),
        "must_show": "SCRIPTURE-EXACT: the deliverance — the dawn shallows: the great fish standing off in the light as Jonah wades the last steps to the beach; carrier and carried parting.",
        "must_not_show": "the delivery DIGNIFIED — wading ashore in the shallows, the creature calm beyond him.",
        "scene": (
            "The strange ferry makes "
            "its landing: in the dawn "
            "shallows Jonah wades the "
            "last thigh-deep steps "
            "toward the pale beach, "
            "sea-green robe streaming, "
            "while behind him in the "
            "deeper light the great "
            "dark back of his carrier "
            "stands off, one calm eye "
            "watching its passenger "
            "delivered — three days' "
            "cargo set down safe on "
            "the exact shore his "
            "errand needs, by the "
            "gentlest freight service "
            "heaven ever prepared. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b28", "out": "s28-this-time-jonah-went-he.jpeg", "seg": "n6",
        "window": "153.56-158.63", "wide": True, "jesus": False, "ref": False,
        "locks": ["JONAH", "NINEVEH"],
        "narration": (
            "This time Jonah went. He walked into the great city and cried "
            "out his warning."
        ),
        "must_show": "the obedience — small Jonah walking in through the colossal winged-bull gate into the city's vastness; one man, one message, the great streets receiving him.",
        "must_not_show": "the scale honest — one stocky figure against imperial enormity.",
        "scene": (
            "This time the feet obey, the camera high behind "
            "him as he walks in: "
            "one stocky sea-green "
            "figure walking in under "
            "the five-man-high carved "
            "bulls of the great gate, "
            "swallowed instantly by "
            "streets wide as rivers "
            "and crowds thick as "
            "harvest — the empire's "
            "capital roaring around "
            "one reluctant Hebrew "
            "with one sentence to "
            "say — and he squares the "
            "stubborn shoulders, "
            "draws the first breath "
            "of the strangest sermon "
            "ever preached, and "
            "begins. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b29", "out": "s29-yet-forty-days-and-nineveh.jpeg", "seg": "s34",
        "window": "159.22-162.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "NINEVEH"],
        "narration": "Yet forty days, and Nineveh shall be overthrown.",
        "must_show": "SCRIPTURE-EXACT: the sermon — Jonah mid-cry in a great street, the eight words leaving him; foreign faces beginning to stop and turn.",
        "must_not_show": "no relish overdone — the crier grim, the words bare; listeners ARRESTED.",
        "scene": (
            "The entire sermon takes "
            "eight words: Jonah "
            "planted in the great "
            "street with his head "
            "back, crying it over the "
            "market's roar — YET "
            "FORTY DAYS, AND NINEVEH "
            "SHALL BE OVERTHROWN — no "
            "second verse, no altar "
            "call, no comfort clause — "
            "and around the grim "
            "crier the imperial "
            "traffic beginning, here "
            "and there, to stop: a "
            "porter setting down his "
            "load, a merchant's "
            "count trailing off, "
            "foreign faces turning "
            "toward a countdown in "
            "an accent from a "
            "conquered land. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b30", "out": "s30-forty-more-days-and-this.jpeg", "seg": "n6b",
        "window": "163.85-168.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": (
            "Forty more days and this city is finished. That was the entire "
            "sermon."
        ),
        "must_show": "the sermon's bareness — close on Jonah's grim crying face: duty discharged to the letter, hope for them nowhere in it.",
        "must_not_show": "the honesty kept — he half-wants the countdown true; that shadow visible, human.",
        "scene": (
            "Close on the barest sermon "
            "ever preached and the "
            "divided man preaching it: "
            "the grizzled face at "
            "full cry, doing the duty "
            "to its letter — every "
            "word delivered, nothing "
            "softened, nothing added — "
            "and behind the honest "
            "eyes, unhidden, the "
            "shadow the last chapter "
            "will drag into daylight: "
            "some part of the crier "
            "hoping his own countdown "
            "holds — mercy's "
            "messenger, still half "
            "at war with mercy. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b31", "out": "s31-no-comfort-in-it-anywhere.jpeg", "seg": "n6b",
        "window": "168.57-176.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["JONAH", "NINEVEH"],
        "narration": (
            "No comfort in it anywhere, no invitation, no offer — just a "
            "countdown, preached by a man who was hoping it would come "
            "true."
        ),
        "must_show": "the countdown spreading — the sermon's wake through the streets: the words being repeated mouth to mouth down lanes and stalls, unease rippling outward.",
        "must_not_show": "no panic-riot — sober spreading dread; the city LISTENING against all odds.",
        "scene": (
            "The eight words, the camera down the great street "
            "taking the passing crowd from the side, outrun "
            "their preacher: down the "
            "great streets the sermon "
            "travels mouth to mouth — "
            "a fishwife repeating it "
            "to a customer, a soldier "
            "carrying it through a "
            "barracks gate, scribes "
            "murmuring it over their "
            "tablets — FORTY DAYS — "
            "the countdown spreading "
            "through the imperial "
            "roar like cold through "
            "water, and the city "
            "doing the one thing "
            "nobody in Israel would "
            "have bet a fig on: "
            "listening. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b32", "out": "s32-and-the-second-surprise-is.jpeg", "seg": "n7",
        "window": "177.56-181.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": (
            "And the second surprise is bigger than the first. They "
            "listened."
        ),
        "must_show": "the listening — close on foreign faces genuinely stricken: a merchant's dropped bravado, a soldier's bowed head; the warning landing in hearts.",
        "must_not_show": "no caricature of the foreigners — real contrition beginning on real faces.",
        "scene": (
            "Close on the miracle "
            "nobody predicted: foreign "
            "faces — the empire's "
            "faces, the feared "
            "faces — stricken open by "
            "eight words: a big "
            "merchant's bravado gone "
            "off him like a dropped "
            "cloak, a scarred soldier "
            "staring at his own "
            "hands, a young mother "
            "pulling her children "
            "close with the countdown "
            "in her eyes — Nineveh, "
            "of all cities on the "
            "map, taking a Hebrew "
            "warning straight to "
            "heart. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b33", "out": "s33-from-the-king-on-his.jpeg", "seg": "n7",
        "window": "181.76-193.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": (
            "From the king on his throne down to the poorest beggar, the "
            "whole city turned — sackcloth, fasting, and honest sorrow — "
            "begging God for mercy they knew they did not deserve."
        ),
        "must_show": "SCRIPTURE-EXACT: the city-wide turning — the great square at dusk: the king down off his throne-litter in sackcloth among his people, rich and poor alike in rough cloth and ashes, honest sorrow everywhere.",
        "must_not_show": "the repentance DIGNIFIED — bowed heads and sackcloth, no groveling spectacle; king and beggar leveled.",
        "scene": (
            "The whole empire's capital — the camera high past "
            "a thousand kneeling backs — "
            "kneels in rough cloth: "
            "the great square at dusk "
            "filled edge to edge — and "
            "at its center the king "
            "himself, down off his "
            "gilded litter, crown set "
            "aside, sackcloth on his "
            "own shoulders among the "
            "porters and beggars "
            "wearing the same — rich "
            "robes traded for haircloth "
            "across a hundred thousand "
            "backs, fasting posted at "
            "every door, and rising "
            "off all of it the one "
            "sound heaven bends "
            "closest for: honest "
            "sorrow, asking for what "
            "it knows it has not "
            "earned. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b34", "out": "s34-they-cast-lots-to-find.jpeg", "seg": "n3",
        "window": "54.33-58.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHIP", "JONAH"],
        "narration": (
            "They cast lots to find out whose fault it was, and the lot "
            "fell on Jonah."
        ),
        "must_show": "SCRIPTURE-EXACT: the lot falling — the storm-lit huddle around the cast lots on the pitching deck, every eye coming up from the marker to Jonah.",
        "must_not_show": "the crew's look QUESTIONING not hostile — dread, not menace.",
        "scene": (
            "On the pitching deck the "
            "old sea-court convenes: "
            "the crew huddled from the "
            "spray around the cast "
            "lots, the marked shard "
            "lying face-up in the "
            "lantern light — and "
            "every salt-streaked face "
            "rising slowly from the "
            "marker to the passenger "
            "braced at the mast — not "
            "hostile yet, only "
            "asking, with the storm "
            "howling the question's "
            "urgency: who ARE you, "
            "and what did you bring "
            "aboard our ship? Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b35", "out": "s35-and-god-who-had-been.jpeg", "seg": "n8",
        "window": "193.78-201.69", "wide": True, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": (
            "And God, who had been looking for a reason to spare them all "
            "along, saw that they turned from their evil — and he relented."
        ),
        "must_show": "SCRIPTURE-EXACT: the relenting — over the sackclothed city, the heavy sky breaking OPEN into clean evening gold; mercy as weather, the turning seen and answered.",
        "must_not_show": "ABSOLUTE: no figure in the sky — the relenting rendered entirely as the light's change over the kneeling city.",
        "scene": (
            "Over the kneeling city — the camera higher than "
            "the walls, the crowd all bowed backs below — the "
            "verdict changes in the "
            "sky: the heavy waiting "
            "grey that hung the "
            "countdown breaking open "
            "along its whole width — "
            "clean evening gold "
            "pouring down through the "
            "rent onto sackcloth and "
            "ash and upturned foreign "
            "faces — the turning "
            "SEEN, from higher than "
            "the walls, and answered "
            "in the only language "
            "big enough: light, "
            "poured out over a "
            "hundred thousand people "
            "who asked for mercy "
            "they knew they did not "
            "deserve, and got it. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b36", "out": "s36-he-did-not-destroy-the.jpeg", "seg": "n8",
        "window": "201.69-204.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": "He did not destroy the city. He forgave it.",
        "must_show": "forgiveness at street level — a lane at the gold evening: a family shedding sackcloth for supper, lamps lighting, life resuming under mercy.",
        "must_not_show": "no destruction anywhere ever — ordinary evening life as the forgiveness's proof.",
        "scene": (
            "Forgiveness looks like "
            "this at street level: a "
            "lane in the new gold "
            "evening where a family "
            "sheds its sackcloth on "
            "the doorstep and goes in "
            "to a first supper in "
            "days — lamps lighting "
            "window by window down "
            "the lane, a child "
            "laughing somewhere for "
            "the first time all "
            "week, the bread smell "
            "starting again — the "
            "great word RELENTED "
            "translated into its "
            "native tongue: ordinary "
            "evenings, allowed to "
            "continue. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b37", "out": "s37-and-jonah-watching-from-a.jpeg", "seg": "n8",
        "window": "205.92-210.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "JONAH", "NINEVEH"],
        "narration": (
            "And Jonah, watching from a hill outside the walls, was "
            "furious. Listen to why."
        ),
        "must_show": "SCRIPTURE-EXACT: the angry watcher — Jonah on his dry hill under the bare tree, arms crossed hard, glaring down at the spared shining city; fury at mercy.",
        "must_not_show": "the fury HUMAN — a sulking hurt man, not a monster; the city radiant below.",
        "scene": (
            "On the dry hill east of "
            "the walls sits the only "
            "unhappy man in the "
            "region: Jonah under his "
            "bare tree with his arms "
            "crossed hard and his "
            "stubborn mouth clamped, "
            "glaring down at a city "
            "gone golden with reprieve "
            "— the lamps lighting, the "
            "suppers resuming, the "
            "hundred thousand spared — "
            "and the prophet of the "
            "whole miracle sitting "
            "above it in a fury he "
            "cannot pray away, for a "
            "reason he is about to "
            "say out loud. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b38", "out": "s38-i-knew-that-thou-art.jpeg", "seg": "s42",
        "window": "211.39-218.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "HILL"],
        "narration": (
            "I knew that thou art a gracious God, and merciful, slow to "
            "anger, and of great kindness, and repentest thee of the evil."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — close on Jonah's furious upturned face hurling the accusation that is a creed: I KNEW thou art gracious; theology as complaint.",
        "must_not_show": "no figure of God; the paradox VISIBLE — the truest description of God in the book, said in anger.",
        "scene": (
            "Close on the strangest "
            "prayer in scripture: "
            "Jonah's face upturned and "
            "furious, hurling at "
            "heaven — as accusation — "
            "the most beautiful creed "
            "in his whole Bible: I "
            "KNEW IT — gracious, "
            "merciful, SLOW TO ANGER, "
            "of GREAT KINDNESS — every "
            "word true, every word "
            "meant as complaint — a "
            "man indicting God for "
            "the exact character that "
            "saved his own life three "
            "chapters ago, too angry "
            "to hear himself "
            "preaching. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b39", "out": "s39-i-knew-it-he-says.jpeg", "seg": "n8b",
        "window": "219.57-222.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "I knew it, he says. I knew you would forgive them.",
        "must_show": "the knew-it — Jonah's face in the hill's warm light: the grudge bared to its root; certainty of mercy as his grievance.",
        "must_not_show": "the honesty kept — bitterness and truth in one breath.",
        "scene": (
            "Close on the grudge at "
            "its bare root: I KNEW "
            "YOU WOULD FORGIVE THEM — "
            "the words grinding out "
            "of the stubborn mouth "
            "with years behind them — "
            "not I feared, not I "
            "suspected: I KNEW — the "
            "prophet's whole flight, "
            "the ship, the storm, the "
            "deep, all of it "
            "confessing its one "
            "motive in the warm hill "
            "light: he ran because "
            "he was certain of "
            "exactly the mercy that "
            "just lit the lamps of "
            "Nineveh. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b40", "out": "s40-that-is-the-confession-at.jpeg", "seg": "n8b",
        "window": "222.54-228.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "JONAH", "NINEVEH"],
        "narration": (
            "That is the confession at the bottom of the book. Jonah never "
            "ran because he thought God was harsh."
        ),
        "must_show": "the bottom of the book — the wide scene: the small angry figure on the hill, the vast forgiven city glowing-warm below; the whole argument in one geography.",
        "must_not_show": "drift-word care: no 'glow' phrasing in text; the city's warmth as lamplit gold.",
        "scene": (
            "The whole book sits in "
            "one wide evening frame: "
            "the small furious figure "
            "cross-armed on his dry "
            "hill, and below him, "
            "vast and lamplit gold in "
            "the dusk, the city he "
            "was certain would be "
            "forgiven — a hundred "
            "thousand suppers burning "
            "warm across the plain — "
            "the confession mapped in "
            "geography: he never ran "
            "from a harsh God; "
            "nobody flees to Tarshish "
            "from harshness — he ran "
            "from a kindness he knew "
            "would win. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r118-b41", "out": "s41-he-ran-because-he-was.jpeg", "seg": "n8b",
        "window": "228.49-231.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH"],
        "narration": "He ran because he was afraid God was too good.",
        "must_show": "the diagnosis — Jonah's face softening despite itself in the warm light: the accusation collapsing into the compliment it always was.",
        "must_not_show": "the softening SLIGHT — a crack in the sulk, not a conversion yet.",
        "scene": (
            "Close on an accusation "
            "discovering it is a "
            "compliment: TOO GOOD — "
            "the charge hanging in "
            "the warm evening air, "
            "and on the grizzled "
            "furious face, despite "
            "everything, the smallest "
            "crack in the sulk — "
            "because there is no way "
            "to say it that does not "
            "praise: a God so bent "
            "toward sparing that his "
            "own prophet crossed the "
            "sea to escape being "
            "used for it — the worst "
            "thing Jonah can find to "
            "say, and the best thing "
            "anyone has ever said. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b42", "out": "s42-and-should-not-i-spare.jpeg", "seg": "jvB",
        "window": "231.80-244.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "JONAH", "NINEVEH"],
        "narration": (
            "And should not I spare Nineveh, that great city, wherein are "
            "more than sixscore thousand persons that cannot discern "
            "between their right hand and their left hand; and also much "
            "cattle?"
        ),
        "must_show": "SCRIPTURE-EXACT: the last question — over the hill and the spared city in the morning light, the question hanging: SHOULD NOT I SPARE; Jonah listening, the city's smallest visible below.",
        "must_not_show": "ABSOLUTE: no figure as the voice — the morning light over city and sulking prophet carries it.",
        "scene": (
            "The book's last voice asks "
            "its question over the "
            "whole morning: the spared "
            "city shining on its "
            "plain, the sulking "
            "prophet on his hill — "
            "SHOULD NOT I SPARE "
            "NINEVEH — the words "
            "moving over the walls "
            "and the small far "
            "figures in the streets — "
            "SIXSCORE THOUSAND who "
            "cannot tell right hand "
            "from left — children, "
            "the question means; the "
            "confused, the never-"
            "taught — AND ALSO MUCH "
            "CATTLE — mercy's "
            "arithmetic extended even "
            "to the animals, asked "
            "gently of the one man "
            "still voting no. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b43", "out": "s43-and-what-he-told-them.jpeg", "seg": "n3",
        "window": "59.82-64.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["JONAH", "SHIP"],
        "narration": (
            "And what he told them is the first decent thing he does in "
            "the whole book."
        ),
        "must_show": "the decency beginning — Jonah facing the crew in the storm, drawing breath for the confession-and-offer; the turn toward the first decent act.",
        "must_not_show": "the crew's fear around him; his face RESOLVED.",
        "scene": (
            "In the lantern-lit chaos "
            "the runaway squares up "
            "to his first decent act: "
            "facing the ring of "
            "terrified sailors with "
            "the lot lying against "
            "him, drawing the long "
            "breath of a man about "
            "to stop hiding — the "
            "confession assembling, "
            "the offer behind it — "
            "three chapters of "
            "running arriving at the "
            "one thing even a "
            "furious, stubborn, "
            "mercy-resenting prophet "
            "will not do: let "
            "strangers drown for "
            "him. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r118-b44", "out": "s44-a-hundred-and-twenty-thousand.jpeg", "seg": "n9",
        "window": "245.82-253.40", "wide": True, "jesus": False, "ref": False,
        "locks": ["NINEVEH"],
        "narration": (
            "A hundred and twenty thousand people who cannot tell their "
            "right hand from their left — and the animals too."
        ),
        "must_show": "the sixscore thousand — inside the spared city at morning: children thick in a lane's play, the confused and the simple among them, cattle at a trough; the ones the question was about.",
        "must_not_show": "the tenderness TOTAL — the least-knowing of the city, beloved and shown so.",
        "scene": (
            "The question's whole constituency — the camera low "
            "in the lane taking the games from the side — fills a "
            "morning lane: children "
            "thick underfoot at their "
            "games — the exact ones "
            "who cannot tell right "
            "hand from left — an old "
            "simple man smiling at "
            "the wall in his patch "
            "of sun, a baby asleep "
            "in a doorway basket, "
            "and at the lane's end "
            "the cattle nosing their "
            "trough, also counted, "
            "also mentioned — the "
            "hundred and twenty "
            "thousand reasons, "
            "walking around alive in "
            "the light of the mercy "
            "that argued for them. "
            "Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r118-b45", "out": "s45-that-is-how-the-book.jpeg", "seg": "n9",
        "window": "253.40-255.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "JONAH"],
        "narration": "That is how the book ends.",
        "must_show": "the open ending — Jonah on the hill in morning light, the question still on the air, his answer unspoken; the book's deliberate unresolve.",
        "must_not_show": "no resolution faked — his face mid-think, the sulk loosened, undecided.",
        "scene": (
            "The book ends with a man "
            "mid-think: Jonah on his "
            "hill in the clean morning "
            "light, the great question "
            "still hanging on the "
            "air around him — SHOULD "
            "NOT I SPARE — and his "
            "answer nowhere: the "
            "crossed arms loosened "
            "but not open, the "
            "stubborn mouth working "
            "at something it has not "
            "yet agreed to say — the "
            "story stopping deliberately "
            "here, on the hinge, "
            "with the prophet — and "
            "the reader — left "
            "holding the reply. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r118-b46", "out": "s46-not-with-jonah-answering-but.jpeg", "seg": "n9",
        "window": "255.22-261.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "NINEVEH"],
        "narration": (
            "Not with Jonah answering, but with God still arguing for "
            "mercy, out loud, with his own prophet."
        ),
        "must_show": "the closing image — the wide morning: the spared city shining whole on its plain under the open sky, the empty-feeling hill beside it; mercy's argument left standing over everything.",
        "must_not_show": "ABSOLUTE: no figure in the sky; the city RADIANT-whole — the last word mercy's, rendered as morning.",
        "scene": (
            "The closing frame gives "
            "the last word to the "
            "light: the spared city "
            "whole and shining on its "
            "morning plain — walls "
            "intact, gates streaming, "
            "a hundred thousand "
            "ordinary days beginning "
            "inside the mercy that "
            "argued for them — and "
            "beside it the dry little "
            "hill where the argument "
            "was had, small against "
            "all that reprieved "
            "life — the book left "
            "open on purpose, with "
            "God still mid-sentence "
            "for mercy, and the "
            "morning agreeing with "
            "him. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # HILL: build-38 auto-match REJECTED (village doorway frame, not a dry
    # rise overlooking Nineveh's walls) — promote-first from b37.
    # FISH --take from build-30 also REJECTED (netted beach fish, not the
    # whale-vast great fish) — promote-first from b18.
}
# === end PLACE-PLATES ===
