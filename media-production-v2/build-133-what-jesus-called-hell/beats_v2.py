#!/usr/bin/env python3
"""V2 beat map — row 133, build-133-what-jesus-called-hell (Mark 9:43-48; Jer 7, 19).

COVERAGE: 22 pictures over 139.3 s = 6.3 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  Mark 9:43 "if thy hand offend thee, CUT IT OFF: it is better for
        thee to enter into life maimed, than having two hands to go
        into HELL, into the fire that never shall be quenched."
  Mark 9:47 "if thine EYE offend thee, pluck it out: it is better
        for thee to enter into the kingdom of God with one eye..."
  Mark 9:48 (Isaiah 66:24) "Where their WORM dieth not, and the FIRE
        is not quenched."
  The word: GEHENNA = the VALLEY OF HINNOM, a real ravine along the
        south side of Jerusalem. Jer 7:31-32 / 19:6: TOPHETH, where
        children were passed through fire — Jeremiah: it shall be
        called THE VALLEY OF SLAUGHTER.
  Cameron's brief (QUEUE row 133, asked for by name): "the word
        Jesus used was Gehenna — a real burning place outside
        Jerusalem's wall. The eternal-torture-chamber picture came
        from later tradition, not from him. Judgment is real; the
        torturer God is not. CARE: no horror imagery — the real
        valley, the real words."

RENDERING LAWS (content-care — the strictest row in the library):
  - NO HORROR IMAGERY, EVER: no torture, no demons, no pitchforks,
    no underworld maps, no suffering figures in fire, no maiming.
    Automatic reject, no reroll spent.
  - THE HAND/EYE VERSES ARE NEVER DEPICTED LITERALLY (b10/b12/b15):
    no cutting, no plucking, no wounds. They are carried by Jesus's
    own raised hand, his earnest eyes, and a craftsman's precious
    working hand — severity in the WORDS, preciousness in the frames.
  - TOPHETH'S HISTORY IS NEVER SHOWN (b05): no children, no fire, no
    ritual — ONLY the ruined shrine stones and the prophet's grief
    and condemnation. Absolute.
  - The valley is REAL GEOGRAPHY: a dry ravine below Jerusalem's
    southern wall — refuse heaps, thin smolder lines at most (the
    historical burning-ground), desolate, never theatrical.
  - LATER TRADITION'S art (b01/b17) is shown AS art — dim, faded,
    indistinct dark paintings on a wall, viewers at distance;
    nothing lurid rendered sharp.
  - The row lands on the SPEAKER'S character (b21/b22): the searcher,
    the runner, the Savior — warmth answering severity. Judgment
    real; the torturer God is not.

TIME OF DAY ARC (intentional): the tradition frames in dim interior
gloom BY DESIGN; the valley history frames under grey overcast; the
teaching frames in clear hard daylight above the real valley; b13's
smolder at dusk; the closing pair in warm evening gold toward the
city's lights.

CHANGING CONDITION (kept OUT of the locks): none material — the
row's motion is between eras (prophets, Jesus, later art) and
registers (severity, love).
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "VALLEY": (
        "VALLEY LOCK: the Valley of Hinnom — a dry rocky ravine "
        "running below Jerusalem's high southern wall, terraced "
        "ledges, old refuse and ash heaps on its floor, a few thin "
        "smolder lines at most; desolate and real, never "
        "theatrical. The same ravine and wall throughout."
    ),
    "OVERLOOK": (
        "OVERLOOK LOCK: the teaching overlook — a walled ledge on "
        "the city side above the ravine, pale Jerusalem stone, the "
        "valley visible below and the city rising behind. The same "
        "ledge throughout."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the listeners — a small sober group of "
        "disciples and ordinary followers in earth-toned robes of "
        "brown, rust, olive and slate (no cream — only Jesus wears "
        "cream); varied ages and faces, gripped and serious."
    ),
    "PROPHET": (
        "PROPHET LOCK: the prophet is the same man in every shot — "
        "aged and gaunt with wild grey hair and beard, in a rough "
        "DARK CHARCOAL mantle (never cream, never white); grief and "
        "moral fire together, the LORD's mourner over the valley."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r133-b01", "out": "s01-many-of-the-pictures-people.jpeg", "seg": "n0",
        "window": "0.28-4.66", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Many of the pictures people carry of hell came through "
            "centuries of art and tradition."
        ),
        "must_show": "the inherited pictures AS pictures — a dim stone gallery wall hung with old faded paintings whose dark shapes stay indistinct, two small viewers before them; tradition's gallery, nothing lurid sharp.",
        "must_not_show": "ABSOLUTE: nothing in the paintings readable as torture — indistinct dark masses and muted reds only; the frame is about WHERE the pictures came from.",
        "scene": (
            "The pictures most people carry were painted long "
            "after: a dim stone gallery where old canvases hang "
            "in heavy frames, their varnish-dark scenes gone "
            "muddy and indistinct with centuries — vague dark "
            "masses, muted smoulders of red, nothing the eye "
            "can quite resolve — while two small viewers stand "
            "before them in the gloom, receiving, as their "
            "grandparents did, an inheritance of images that "
            "came from easels and imaginations, not from the "
            "mouth they are attributed to. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r133-b02", "out": "s02-but-to-hear-one-of.jpeg", "seg": "n0",
        "window": "7.29-14.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY"],
        "narration": (
            "But to hear one of his most famous warnings clearly, start with "
            "the history inside the word Gehenna."
        ),
        "must_show": "the real referent — first sight of the actual Valley of Hinnom below Jerusalem's southern wall at grey morning; a real place with a real name.",
        "must_not_show": "no halo; NOTHING supernatural — dry rock, old ash, city wall; geography, not theology yet.",
        "scene": (
            "The word has an address, and this is it: the "
            "Valley of Hinnom opening below Jerusalem's high "
            "southern wall in the grey morning light — a dry "
            "rocky ravine of terraced ledges and old ash "
            "heaps, ordinary thorn scrub on its slopes, the "
            "great pale wall running above it — a place you "
            "could walk to in ten minutes from the temple "
            "courts, with a history soaked into its stones "
            "and a name that would travel farther than any "
            "place on earth. No people are needed in this "
            "frame."
        ),
    },
    {
        "id": "v2-r133-b03", "out": "s03-gehenna-is-the-greek-form.jpeg", "seg": "n1",
        "window": "14.79-21.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY"],
        "narration": (
            "Gehenna is the Greek form of the name Valley of Hinnom, a real "
            "ravine along the southern side of Jerusalem."
        ),
        "must_show": "the geography exact — the ravine's full run along the wall's southern line, the city rising above; the map-fact made visible.",
        "must_not_show": "no halo; nothing burning beyond a thin refuse smolder at most — the reality plain.",
        "scene": (
            "The geography lesson costs one long look: the "
            "ravine runs its whole dry length along the "
            "southern wall — the city stacked pale and alive "
            "above the rim, washing on rooflines, smoke from "
            "cooking fires — and below the wall the valley "
            "floor with its terraces and refuse heaps and one "
            "thin lazy smolder line where the city's discards "
            "burn out — Gehenna, in Greek; Hinnom, at home; a "
            "ravine with a postal address, on the shadow side "
            "of the holy city. No people are needed in this "
            "frame."
        ),
    },
    {
        "id": "v2-r133-b04", "out": "s04-long-before-jesus-that-name.jpeg", "seg": "n1",
        "window": "21.43-28.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY"],
        "narration": (
            "Long before Jesus, that name had become a memory of one of "
            "Judah's darkest apostasies."
        ),
        "must_show": "the dark memory in STONES ONLY — an old ruined high-place: weathered altar stones broken and scattered on a valley ledge under heavy grey sky; history's shadow with nothing enacted.",
        "must_not_show": "ABSOLUTE: nothing depicted of the acts — no figures, no fire, no children, ever; ruined stones and grey weather carry all of it.",
        "scene": (
            "What the name remembers is told by ruins alone: on "
            "a ledge of the valley an old high-place lies "
            "broken — weathered altar stones toppled and "
            "scattered, blackened ancient soot deep in their "
            "grain, thorn scrub growing up through the cracks "
            "of a platform no one has dared rebuild — under a "
            "sky of heavy grey, the site of Judah's darkest "
            "hour standing wrecked and wordless, saying only "
            "that something happened here that God never "
            "commanded and never forgot. No people are in "
            "this frame."
        ),
    },
    {
        "id": "v2-r133-b05", "out": "s05-the-prophets-condemned-a-place.jpeg", "seg": "n2",
        "window": "28.64-33.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY", "PROPHET"],
        "narration": (
            "The prophets condemned a place there called Topheth, where "
            "children had been passed through fire."
        ),
        "must_show": "the condemnation ONLY — the prophet standing against the ruined shrine stones, arm raised in denunciation, grief breaking his old face; the crime existing only in his words and sorrow.",
        "must_not_show": "ABSOLUTE: no children, no fire, no ritual, nothing enacted or implied visually — the ruined stones and the prophet's grief are the entire content.",
        "scene": (
            "The crime is present only in the old man's face: "
            "the prophet stands against the broken altar "
            "stones with his arm raised in denunciation, wild "
            "grey hair whipping in the valley wind — and the "
            "moral fire in his eyes is banked over grief, an "
            "old man's voice breaking on what was done in "
            "this place to the smallest of Judah — the "
            "condemnation thundering over empty ruined stones "
            "and nothing else, because some history is only "
            "ever to be spoken, never shown. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r133-b06", "out": "s06-jeremiah-said-it-would-be.jpeg", "seg": "n2",
        "window": "33.44-36.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY", "PROPHET"],
        "narration": "Jeremiah said it would be called the Valley of Slaughter.",
        "must_show": "the renaming — the prophet's arm sweeping the whole valley under a storm-dark sky, pronouncing the doom-name over it; judgment as prophecy, nothing enacted.",
        "must_not_show": "ABSOLUTE: no slaughter imagery — the terrible name lands on empty valley and dark weather only.",
        "scene": (
            "The valley gets its terrible new name from a "
            "hilltop: the prophet's arm sweeps the ravine's "
            "whole length under a sky gone storm-dark over "
            "the wall — the Valley of SLAUGHTER, the sentence "
            "runs, for what was done here and what it will "
            "cost — and the name falls on nothing but empty "
            "terraces and old stones and weather, prophecy "
            "doing its work the way prophecy does: renaming a "
            "place so that no one can ever again walk it "
            "innocently. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r133-b07", "out": "s07-the-name-carried-shame-ruin.jpeg", "seg": "n2",
        "window": "36.53-40.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY"],
        "narration": "The name carried shame, ruin, and judgment.",
        "must_show": "the name's cargo — the valley floor as the city's burning-ground: refuse heaps, thin smolder lines, drifting ash under flat grey light; desolation without theatre.",
        "must_not_show": "ABSOLUTE: no figures suffering, no flames leaping — thin smoke lines and ash; the desolation matter-of-fact.",
        "scene": (
            "What the name carried is what the valley became: "
            "the ravine floor spread with the city's refuse "
            "heaps — broken pottery, spoiled goods, the "
            "discards of ten thousand households — thin "
            "smolder lines wandering through the piles and a "
            "fine grey ash drifting on the wind under flat "
            "colourless light — shame's landscape, ruin's "
            "warehouse, judgment's standing illustration, kept "
            "burning low at the city's back door where "
            "everyone could see it and no one wanted to look. "
            "No people are in this frame."
        ),
    },
    {
        "id": "v2-r133-b08", "out": "s08-jesus-did-give-severe-warnings.jpeg", "seg": "n0",
        "window": "4.66-7.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": "Jesus did give severe warnings.",
        "must_show": "the severity owned — close on Jesus's grave face; the row concedes it plainly: he DID warn, and meant it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gravity total, warmth underneath — never harsh.",
        "scene": (
            "Nothing in this story softens him: close on "
            "Jesus's face in the clear hard daylight, and the "
            "gravity in it is absolute — the deep eyes level, "
            "the mouth set, a man about to say the severest "
            "sentences of his ministry and mean every word — "
            "no thunderbolts, no theatre, just the particular "
            "seriousness of love that has seen exactly what "
            "sin does and has no intention of describing it "
            "politely. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r133-b09", "out": "s09-jesus-used-it-along-with.jpeg", "seg": "n3",
        "window": "47.25-55.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "LISTENERS", "VALLEY"],
        "narration": (
            "Jesus used it, along with the closing image from Isaiah of fire "
            "and the worm, to make the danger of sin impossible to ignore:"
        ),
        "must_show": "the word aimed at its referent — Jesus teaching on the overlook, his arm pointing DOWN at the real valley below the wall; the listeners' eyes following to the actual place.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION — every gaze follows the arm to the real ravine.",
        "scene": (
            "The sermon points at something you can walk to: "
            "Jesus on the walled ledge with his listeners "
            "gathered close, his arm extended DOWN toward the "
            "ravine below the southern wall — THAT place, the "
            "gesture says; you have all smelled its smoke — "
            "and the sober faces follow the pointing arm over "
            "the parapet to the real terraces and the real "
            "thin smolder of the city's burning-ground, the "
            "danger of sin suddenly wearing local geography "
            "instead of distant myth. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r133-b10", "out": "s10-and-if-thy-hand-offend.jpeg", "seg": "j1",
        "window": "55.94-68.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "LISTENERS"],
        "narration": (
            "And if thy hand offend thee, cut it off: it is better for thee "
            "to enter into life maimed, than having two hands to go into "
            "hell, into the fire that never shall be quenched:"
        ),
        "must_show": "SCRIPTURE-EXACT, NEVER LITERAL — Jesus holds his OWN hand up before the listeners as he speaks the severe words; the preciousness of a hand made visible; the crowd gripped.",
        "must_not_show": "ABSOLUTE: no cutting, no wound, no maiming imagery of any kind — the raised whole hand and the grave voice carry all the severity.",
        "scene": (
            "The severest sentence is preached on an open "
            "hand: Jesus holds his own hand up before them — "
            "turning it once in the hard light, a carpenter's "
            "hand, scarred and skilled and irreplaceable — as "
            "the terrible arithmetic leaves him: better to "
            "lose even THIS than keep a cherished sin to the "
            "end of its road — the hand held whole and high "
            "through every word, the cutting living entirely "
            "in the sentence, where he put it and where it "
            "stays. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r133-b11", "out": "s11-by-the-time-mark-recorded.jpeg", "seg": "n3",
        "window": "40.98-46.50", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "By the time Mark recorded Jesus' warning, Gehenna was a "
            "place-name charged with that biblical history."
        ),
        "must_show": "the recording — a scribe at his lamp writing the Gospel onto a scroll, careful and reverent; the charged word passing into ink.",
        "must_not_show": "no halo; the script INDISTINCT period writing — no readable text.",
        "scene": (
            "The word crosses into ink at a small table: the "
            "evangelist bent over his scroll in the lamp's "
            "warm ring, reed pen moving careful and steady, "
            "the day's memories becoming lines — and among "
            "them the place-name with seven centuries of "
            "freight in it, set down exactly as the Teacher "
            "used it: Gehenna, the valley everyone in "
            "Jerusalem could point to, carrying its whole "
            "biblical history into every language that would "
            "ever borrow the verse. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r133-b12", "out": "s12-and-if-thine-eye-offend.jpeg", "seg": "j2",
        "window": "68.83-79.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "LISTENERS"],
        "narration": (
            "And if thine eye offend thee, pluck it out: it is better for "
            "thee to enter into the kingdom of God with one eye, than having "
            "two eyes to be cast into hell fire:"
        ),
        "must_show": "SCRIPTURE-EXACT, NEVER LITERAL — close on Jesus's earnest eyes as he gives the second severe image; the listeners sober and still; severity in words alone.",
        "must_not_show": "ABSOLUTE: no plucking, no wound, no eye-injury imagery of any kind — his own clear steady eyes carry the verse.",
        "scene": (
            "The second sentence is spoken eye to eye: close "
            "on Jesus's face as the words come, his own clear "
            "steady eyes holding his listeners' — better to "
            "enter the kingdom half-blind than march into "
            "ruin with perfect vision — the deep brown gaze "
            "unflinching through its own terrible image, "
            "putting the price of sin in the only currency "
            "bodies understand, while every eye looking back "
            "at him stays whole, and blinks, and understands. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r133-b13", "out": "s13-where-their-worm-dieth-not.jpeg", "seg": "j3",
        "window": "80.26-84.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["VALLEY"],
        "narration": "Where their worm dieth not, and the fire is not quenched.",
        "must_show": "SCRIPTURE-EXACT: Isaiah's closing image at its real referent — the valley's smolder lines at dusk, low red embers in the refuse under a darkening sky; desolation, no figures.",
        "must_not_show": "ABSOLUTE: no suffering figures, no leaping flames, no faces in smoke — low embers and thin smoke on empty ground only.",
        "scene": (
            "The verse's picture is the valley at the day's "
            "end: dusk settles over the ravine and the refuse "
            "heaps keep their low red banked embers "
            "breathing under the ash — thin smoke standing in "
            "grey threads against the darkening wall, the "
            "burning-ground doing what it does through every "
            "night of every year, never quite consuming, "
            "never quite done — Isaiah's terrible image at "
            "its home address: empty ground, low fire, and "
            "time. No people are in this frame."
        ),
    },
    {
        "id": "v2-r133-b14", "out": "s14-the-images-are-deliberately-severe.jpeg", "seg": "n4",
        "window": "84.75-86.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["OVERLOOK", "LISTENERS"],
        "narration": "The images are deliberately severe.",
        "must_show": "the severity landing — along the listeners' faces: gripped, sober, nobody comfortable; the deliberate weight doing its work.",
        "must_not_show": "no halo; gripped SERIOUSNESS, not terror — the faces working, not fleeing.",
        "scene": (
            "The severity arrives exactly as designed: along "
            "the listening faces on the ledge the words do "
            "their deliberate work — a young man's jaw tight, "
            "an older woman's hand pressed at her collar, a "
            "fisherman staring down at his own two intact "
            "hands — nobody comfortable, nobody scared past "
            "thinking, every face doing the sober arithmetic "
            "the images were built to force: what, in my one "
            "life, is this about? Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r133-b15", "out": "s15-hand-and-eye-name-things.jpeg", "seg": "n4",
        "window": "86.99-96.02", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Hand and eye name things as precious as parts of your own body, "
            "yet no cherished sin is worth surrendering life in God's "
            "kingdom."
        ),
        "must_show": "the preciousness — a craftsman's skilled hand at fine work in warm window light: whole, practiced, irreplaceable; what the images price the choice in.",
        "must_not_show": "ABSOLUTE: nothing severed or harmed — the hand whole and working; the preciousness IS the picture.",
        "scene": (
            "What the images are denominated in, at full "
            "value: a craftsman's hand at fine work in the "
            "warm light of a workshop window — guiding a "
            "carving blade through olive wood in curls, every "
            "practiced tendon doing its irreplaceable job — "
            "forty years of skill in one moving hand, the "
            "single most precious tool its owner will ever "
            "hold — which is exactly the currency the warning "
            "prices sin in, so that nobody could mistake the "
            "size of the sum. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r133-b16", "out": "s16-love-does-not-make-the.jpeg", "seg": "n4",
        "window": "96.02-98.82", "wide": False, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK"],
        "narration": "Love does not make the warning smaller.",
        "must_show": "love and severity in one face — close on Jesus: full warmth and full gravity coexisting, neither diluting the other.",
        "must_not_show": "no halo, glare or rim-light on Jesus; BOTH registers present — tenderness that will not soften the truth.",
        "scene": (
            "Both things are true on the one face: close on "
            "Jesus in the late light, and the warmth in the "
            "deep eyes is total — and so is the gravity, "
            "neither one thinning the other by a single "
            "degree — the face of a physician who loves the "
            "patient completely and will not, for any comfort, "
            "shrink the diagnosis — love at full strength "
            "refusing to make the warning one word smaller "
            "than the danger, precisely because it is love. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r133-b17", "out": "s17-later-art-supplied-pitchforks-elaborate.jpeg", "seg": "n5",
        "window": "102.84-107.88", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Later art supplied pitchforks, elaborate torture chambers, and "
            "maps of the underworld."
        ),
        "must_show": "the additions AS additions — the dim gallery again: more old dark canvases, shapes indistinct, a painter's easel and pigments beside them; the machinery of imagination, not revelation.",
        "must_not_show": "ABSOLUTE: nothing in the paintings rendered sharp or lurid — muddy indistinct masses; the easel and pigments make the point.",
        "scene": (
            "Where the extra furniture came from is a studio, "
            "not a scripture: the dim gallery again, its dark "
            "old canvases holding their muddy indistinct "
            "crowds of shapes — and beside them, telling the "
            "whole story, a painter's easel with its pigment "
            "pots and brushes standing where the images were "
            "actually manufactured — pitchforks, chambers, "
            "maps of places no prophet drew: supplied by "
            "centuries of imagination working in oils, and "
            "billed, unfairly, to the man on the overlook. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r133-b18", "out": "s18-scripture-itself-uses-several-warning.jpeg", "seg": "n5",
        "window": "107.88-116.36", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Scripture itself uses several warning images: death, "
            "destruction, darkness, exclusion, and fire."
        ),
        "must_show": "the true image-set as OBJECTS — a still-life row: a guttering lamp near dark, a closed door, dry chaff by a small fire pit, a broken jar; scripture's own vocabulary, nothing animated.",
        "must_not_show": "ABSOLUTE: no people suffering — objects and states only; the fire pit small and low.",
        "scene": (
            "Scripture's own picture-vocabulary fits on one "
            "table of things: a clay lamp guttering down to "
            "its last blue-edged flame, a heavy wooden door "
            "shut fast in shadow, a handful of dry chaff "
            "beside a small low fire pit, a jar broken past "
            "mending — death, darkness, exclusion, "
            "destruction, fire — the Bible's actual warning "
            "images laid out plain and objectless of victims: "
            "states to be avoided, said five ways, by a Book "
            "that wants nobody in any of them. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r133-b19", "out": "s19-the-images-are-meant-to.jpeg", "seg": "n5",
        "window": "116.36-123.45", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The images are meant to call you back, not satisfy curiosity "
            "about every detail beyond death."
        ),
        "must_show": "the calling-back — on a darkening road, a traveller TURNED, facing back toward the warm lit windows of home in the distance; the warning's true function as a turn.",
        "must_not_show": "no halo; the turn readable (rhymes with the row-117 reversal frame); the home-light warm and far.",
        "scene": (
            "What the images are FOR is happening on this "
            "road: a traveller has stopped in the darkening "
            "lane and turned — fully turned, feet and "
            "shoulders and face — back toward the far warm "
            "windows of home warm-lit down the valley, the "
            "wrong direction abandoned behind him in the "
            "dusk — the whole purpose of every severe "
            "sentence accomplished in one reversed silhouette: "
            "not information about the dark, but a man walking "
            "back toward the light while there is road left. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r133-b20", "out": "s20-love-tells-the-truth-about.jpeg", "seg": "n4",
        "window": "98.82-102.16", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Love tells the truth about what destroys us.",
        "must_show": "love's warning enacted small — a father's arm barring his small child back from an open well's edge, firm and gentle at once; protective truth in one gesture.",
        "must_not_show": "no halo; the child SAFE — caught well back from the edge, no peril rendered close; the father's face loving, not fearful.",
        "scene": (
            "Every parent already preaches this sermon: at the "
            "village well a father's arm comes across his "
            "small child's chest, firm as a gate and gentle "
            "as a blessing, easing her back from the low "
            "stone rim she was toddling toward — no, the arm "
            "says, not because I am against you; because I "
            "know what is down there — love telling the plain "
            "truth about what destroys, in the oldest and "
            "kindest gesture the truth has ever worn. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r133-b21", "out": "s21-read-the-warning-beside-the.jpeg", "seg": "n6",
        "window": "123.99-134.31", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "Read the warning beside the whole life of the speaker: the "
            "shepherd who searches for the lost, the father who runs down "
            "the road, the Savior who enters death to bring people home."
        ),
        "must_show": "the speaker's whole life — Jesus carrying a found lamb across his shoulders through golden evening toward home; the searcher himself, warmth answering severity.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the lamb REAL and calm on his shoulders; the walk homeward.",
        "scene": (
            "The man who gave the warning looks like this the "
            "rest of the week: Jesus walking the golden "
            "evening slope with a found lamb draped calm "
            "across his shoulders, one hand steadying its "
            "forelegs, his stride bent for home — the searcher "
            "who leaves the ninety-nine, the runner down the "
            "father's road, the Savior who will walk into "
            "death itself to carry people out of it — the "
            "warning's author, photographed at his day job, "
            "which was always rescue. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r133-b22", "out": "s22-he-warns-because-sin-destroys.jpeg", "seg": "n6",
        "window": "134.31-138.95", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OVERLOOK", "VALLEY"],
        "narration": "He warns because sin destroys and because he came to save.",
        "must_show": "the closing geography — Jesus standing on the overlook BETWEEN: the desolate valley on one side below, the city's warm evening lights on the other; his open hand toward the lights; the whole row in one composition.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the composition's two zones clear — ruin below one way, home-light the other, and him between, pointing home.",
        "scene": (
            "The last frame is a map with a man on it, the "
            "camera set behind the listeners' backs at the "
            "ledge: Jesus stands on the overlook between the "
            "two geographies — below on one side the grey "
            "desolate ravine with its thin dying smolder, and "
            "on the other the city rising into warm evening "
            "lamplight, window upon window of suppers and "
            "families — and his open hand is extended toward "
            "the LIGHTS: the warning's whole purpose standing "
            "in one gesture between the ruin and the home, "
            "pointing home. Every figure has two arms, two "
            "hands and one head."
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
