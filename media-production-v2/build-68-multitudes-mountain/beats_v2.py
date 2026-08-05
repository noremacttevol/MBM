#!/usr/bin/env python3
"""V2 beat map — row 68, build-68-multitudes-mountain (Matthew 15:29-32).

COVERAGE: 35 pictures over 197.6 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 15:29-32 KJV):
  v29   "Jesus ... came nigh unto the sea of Galilee; and went up into a
        mountain, and SAT DOWN there" — the sitting is the whole strategy:
        he sat where he could be found. The mountainside overlooks the
        lake from the eastern (Decapolis) side.
  v30   "great multitudes came unto him, HAVING WITH THEM those that were
        lame, blind, dumb, maimed, and many others, and CAST THEM DOWN AT
        JESUS' FEET; and he healed them" — the row's engine is the
        CARRYING: planks, backs, led hands — every climb somebody's love
        for somebody. The laying-down at his feet is a locked image.
        'And he healed them' — four words, no fanfare: the healings are
        painted as quiet completed facts (a first word spoken, eyes
        opened on a face, legs walking down), never as spectacle.
  v31   "the multitude WONDERED ... and they GLORIFIED THE GOD OF ISRAEL"
        — many here are outsiders to Israel (Decapolis side); the wonder
        crosses that line.
  v32   "I have compassion on the multitude, because they CONTINUE WITH
        ME NOW THREE DAYS, and have nothing to eat: and I WILL NOT SEND
        THEM AWAY FASTING, lest they faint in the way" — the three days'
        staying, and the God who counts stomachs after remaking bodies.

TIME OF DAY: a THREE-DAY arc — the sitting and the climbing in bright
morning; the healings through a long golden afternoon; the staying
through a lamplit-and-campfire night beat; the compassion saying on the
third day's morning. Shifts stated per-beat, all scripture-driven.

CONTENT-CARE: healing dignity laws throughout — the carried sick are
persons, never a spectacle of affliction; disabilities painted plainly
and kindly (a plank litter, a led hand, a mute woman's still mouth);
every healing shown as restored ordinary life, not drama.

CHANGING CONDITION (kept OUT of the locks): the healed states — carried
UP, walking DOWN; silent, then speaking; led, then leading. And the
crowd's duration: arriving, gathered, camped, three days deep.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MOUNTAIN": (
        "MOUNTAINSIDE LOCK: a broad grassy mountainside above the Sea of "
        "Galilee's eastern shore — terraced natural ledges of rock and "
        "grass, a worn climbing path, scattered boulders, and below, the "
        "lake's blue running to the far hills. The same ledges, path and "
        "lake-view in every beat."
    ),
    "CROWD": (
        "MULTITUDE LOCK: the crowd is a whole region's people — Galilean "
        "and Decapolis families mixed, men, women, children, elders, in "
        "SATURATED DEEP earth colours: dark browns, deep russet, dark "
        "olive, burnt ochre, dusty indigo, faded plum (never cream, "
        "never white; only Jesus wears cream). Faces shown clearly and "
        "with dignity — the carried sick above all."
    ),
    "PLANKMAN": (
        "CARRIED FATHER LOCK: the old man on the plank is the same in "
        "every shot — about seventy, wasted thin, with a long white "
        "beard and patient hooded eyes, wrapped in a DARK RUST blanket "
        "on a rough board litter (never cream, never white). His two "
        "grown sons carry him — broad men in DARK OLIVE and UMBER with "
        "sweat-dark backs. All faces shown clearly."
    ),
    "MUTEWOMAN": (
        "SILENT WOMAN LOCK: the woman who has never spoken is the same "
        "in every shot — about thirty-five, gentle-faced, with "
        "expressive dark eyes that do her talking, a DEEP MADDER-ROSE "
        "head-cloth and a DARK PLUM dress (never cream, never white). "
        "Her husband is a stocky patient man in DARK BROWN. Faces shown "
        "clearly."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r068-b01", "out": "s01-after-the-coast-jesus-came.jpeg", "seg": "n0",
        "window": "0.28-6.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN"],
        "narration": (
            "After the coast, Jesus came back toward the Sea of Galilee, "
            "climbed partway up a mountain, and sat down."
        ),
        "must_show": "SCRIPTURE-EXACT: the sitting — Jesus alone on a rock ledge partway up the grassy mountainside, seated, the lake below; the simplest act in the gospels.",
        "must_not_show": "no halo, glare or rim-light on Jesus; alone and unannounced — a man sitting down on a hill.",
        "scene": (
            "On a rock ledge partway up the broad grassy "
            "mountainside Jesus sits down alone in the "
            "bright morning — forearms on his knees, the "
            "climb's dust on his hem, the great blue of "
            "the lake spread below him to the far hills — "
            "no crowd, no herald, no arrangement: one man "
            "seated on a hillside in the most "
            "consequential act of sitting the region "
            "will ever hear about. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b02", "out": "s02-all-he-did.jpeg", "seg": "n0",
        "window": "6.48-7.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN"],
        "narration": "That's all he did.",
        "must_show": "the sufficiency — close on the seated figure: stillness as invitation; nothing performed, everything offered.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the plainness absolute — availability as posture.",
        "scene": (
            "Close on the seated figure in the morning "
            "light: hands loose, face turned easy toward "
            "the climbing path below, the whole posture "
            "one of unhurried waiting — no gesture made, "
            "no word sent out — availability itself, "
            "sitting on a rock with the wind moving the "
            "grass around it. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b03", "out": "s03-and-the-whole-region-emptied.jpeg", "seg": "n0",
        "window": "10.01-14.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": (
            "And the whole region emptied itself onto that mountainside to find "
            "him."
        ),
        "must_show": "the emptying — from high on the slope: the paths below alive with converging streams of people from every direction, villages visibly draining toward the mountain.",
        "must_not_show": "no halo, glare or rim-light; the convergence the picture — many small streams becoming one climb.",
        "scene": (
            "From high on the mountainside, the camera behind the "
            "seated teacher's shoulder looking down, the whole "
            "region's answer is visible: down on the "
            "shore plain the paths run alive with "
            "people — streams converging from lakeside "
            "villages, from the eastern towns, from "
            "boats drawn up on the shingle — all of it "
            "bending toward the one climbing path, a "
            "countryside emptying itself uphill toward "
            "a man who sat down. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b04", "out": "s04-matthew-says-great-multitudes-came.jpeg", "seg": "n1",
        "window": "14.93-19.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": (
            "Matthew says great multitudes came — and they did not come "
            "empty-handed."
        ),
        "must_show": "the burdened climb — the path close: climbers carrying not goods but PEOPLE; the first litters and led hands visible in the stream.",
        "must_not_show": "no halo, glare or rim-light; the cargo human — every burden a person, every carrier a lover of that person.",
        "scene": (
            "Up the worn climbing path the multitude "
            "comes burdened — and the burdens are "
            "people: a plank litter riding on two "
            "brothers' shoulders, an old woman on a "
            "young man's back, a blind neighbour's hand "
            "gripped and guided over the stones — the "
            "whole procession hauling upward the very "
            "ones who could never have climbed, love "
            "doing the legwork for a region's broken. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r068-b05", "out": "s05-somebody-hauled-their-father-up.jpeg", "seg": "n1",
        "window": "24.12-27.72", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLANKMAN", "MOUNTAIN"],
        "narration": "Somebody hauled their father up a rocky slope on a plank.",
        "must_show": "SCRIPTURE-EXACT in spirit: the plank — the two sons working their father's board litter up a steep rocky pitch, sweat-dark, careful; the old man's patient face riding between them.",
        "must_not_show": "no halo, glare or rim-light; the labour real — angles, grips, sweat; the father's dignity absolute on his board.",
        "scene": (
            "Up the steepest rocky pitch the two broad "
            "sons work their father's plank litter — "
            "the leading brother backwards up the "
            "stones, feeling each step, the other "
            "bracing below with the board's weight in "
            "his forearms — and between them, wrapped "
            "in his rust blanket, the wasted old man "
            "rides with his hooded eyes on the sky, "
            "one thin hand holding the plank's edge, "
            "patient as the mountain itself. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b06", "out": "s06-somebody-carried-a-grown-brother.jpeg", "seg": "n1",
        "window": "27.72-31.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "Somebody carried a grown brother on their back.",
        "must_show": "the brother-carry — close: a man bent under his grown brother's weight on his back, the carried man's arms around his neck; adult weight, chosen gladly.",
        "must_not_show": "no halo, glare or rim-light; the weight honest — bent back, planted staff; the carried man's face against his brother's shoulder.",
        "scene": (
            "Close on the climb: a man bent nearly "
            "double under his grown brother's full "
            "weight — the carried man's wasted legs "
            "hanging, his arms wrapped tight around "
            "the carrier's neck, his cheek pressed to "
            "his brother's sweat-dark shoulder — the "
            "carrier's staff planted at every step, "
            "his face set uphill with the particular "
            "endurance of a man who would not put "
            "this burden down for wages. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b07", "out": "s07-every-step-of-that-climb.jpeg", "seg": "n1",
        "window": "35.69-41.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": (
            "Every step of that climb was somebody's love for somebody, written "
            "in sweat."
        ),
        "must_show": "love's handwriting — extreme close at path level: a carrier's straining foot on the stone, and beside it the shadow of the litter he bears; the climb's cost in one step.",
        "must_not_show": "no halo, glare or rim-light; foot, stone, shadow — devotion at its unit scale.",
        "scene": (
            "Extreme close at the path's stone: a "
            "carrier's sandalled foot planted mid-"
            "stride, tendons standing, dust caked to "
            "the sweat of the ankle — and thrown "
            "across the rock beside it, the long "
            "shadow of the loaded litter he is "
            "bearing up the mountain — one step of "
            "thousands, each one written in the same "
            "ink. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r068-b08", "out": "s08-here-is-exactly-how-matthew.jpeg", "seg": "n2",
        "window": "42.12-44.44", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Here is exactly how Matthew writes it:",
        "must_show": "the record — a close still of a scroll's dense column under a reading lamp, a scribe's finger at the line; the verse about to be quoted, as artifact.",
        "must_not_show": "no halo, glare or rim-light; ancient script only, no legible modern words.",
        "scene": (
            "A close still in warm lamplight: a "
            "gospel scroll's dense hand-lettered "
            "column, and a reader's finger resting at "
            "one line partway down — the ink a "
            "little darker there, as if the copyist "
            "pressed harder — the exact sentence "
            "waiting under the fingertip, four "
            "centuries of readers deep. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b09", "out": "s09-and-great-multitudes-came-unto.jpeg", "seg": "s30",
        "window": "44.99-54.79", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN", "CROWD", "PLANKMAN"],
        "narration": (
            "And great multitudes came unto him, having with them those that "
            "were lame, blind, dumb, maimed, and many others, and cast them "
            "down at Jesus' feet; and he healed them."
        ),
        "must_show": "SCRIPTURE-EXACT: the laying at his feet — the ledge before the seated Jesus filling with the laid-down sick: the plank set down, litters ranged, led ones seated; the verse made geography.",
        "must_not_show": "no halo, glare or rim-light on Jesus; 'cast down at his feet' painted as urgent tender placement, never dumping; his hands already moving toward the nearest.",
        "scene": (
            "Before the seated Jesus the ledge fills "
            "with the laid-down: the old man's plank "
            "set gently at his very feet, a litter "
            "ranged beside it, the blind neighbour "
            "seated close and his guide's hands "
            "withdrawing, a mother placing her "
            "still-mouthed daughter's hand almost on "
            "the healer's knee — a semicircle of the "
            "region's pain arranged at one man's feet "
            "— and his hands already reaching for the "
            "nearest of them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b10", "out": "s10-think-about-what-that-means.jpeg", "seg": "n1",
        "window": "21.41-24.12", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "Think about what that means on a mountain.",
        "must_show": "the mountain's argument — the slope's whole steep length from below: the climbing path switchbacking up; what carrying a person up THIS means.",
        "must_not_show": "no halo, glare or rim-light; the gradient the subject — the mountain shown as the price of bringing anyone.",
        "scene": (
            "From the shore plain, the camera behind the climbing "
            "path's first bearers, the mountain states "
            "its terms: the grassy slope climbing "
            "steep and long, the path switchbacking "
            "up through the boulder-fields, the "
            "healer's ledge a distant notch high "
            "against the sky — a gradient any healthy "
            "walker would respect, posted like a "
            "price above a whole region that decided, "
            "person by carried person, to pay it. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r068-b11", "out": "s11-no-interviews.jpeg", "seg": "n3",
        "window": "78.57-79.91", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN"],
        "narration": "No interviews.",
        "must_show": "the absence of process — Jesus's hand simply taken hold of by a sick man's, no queue, no questions; touch as the whole intake.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no gatekeeping visible anywhere — hands meeting is the entire procedure.",
        "scene": (
            "Close in the afternoon gold: a sick "
            "man's trembling hand simply takes hold "
            "of Jesus's, and Jesus's closes around "
            "it — no register, no waiting mark, no "
            "question asked or form of words — the "
            "entire admissions process of the "
            "mountain conducted in one grip between "
            "two hands. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b12", "out": "s12-the-lame-the-blind-the.jpeg", "seg": "n3",
        "window": "55.84-69.49", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN", "CROWD", "PLANKMAN", "MUTEWOMAN"],
        "narration": (
            "The lame, the blind, the mute, the maimed — he stacks up the words "
            "until you can see it: the pain of an entire region, gathered into "
            "one place, and one man moving through it."
        ),
        "must_show": "SCRIPTURE-EXACT: the one man moving — the wide ledge dense with the laid-down and their families, and Jesus moving THROUGH them: kneeling at one litter while hands reach from the next.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the region's pain dignified — a field hospital of love, one healer walking its rows.",
        "scene": (
            "Across the wide golden ledge, the camera at its rim "
            "taking the gathered rows from the side, the "
            "region's pain lies gathered in its rows — "
            "planks and litters, led elders seated on "
            "stones, children held on laps — and one "
            "cream-clad figure moves through it on "
            "his knees and feet by turns: bent now "
            "over the old man's plank, one hand "
            "already reached toward the next litter, "
            "the silent woman's husband guiding her "
            "forward through the crowd behind him — "
            "one man working an afternoon the size of "
            "a region. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r068-b13", "out": "s13-and-then-the-gospel-gives.jpeg", "seg": "n3",
        "window": "69.49-76.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PLANKMAN"],
        "narration": (
            "And then the gospel gives us four of the biggest words in the "
            "Bible, with no fanfare at all: and he healed them."
        ),
        "must_show": "the four words happening — Jesus's hand resting on the plank-borne father's white head, the old man's hooded eyes opening wide and clear; a healing at the verse's own volume: quiet.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO spectacle — a hand, a head, and eyes clearing; the fanfare's absence the point.",
        "scene": (
            "At the plank's side Jesus kneels with "
            "one hand resting on the old father's "
            "white head — and under the hand the "
            "change happens at the verse's own "
            "volume: the hooded eyes opening wide "
            "and clear, colour arriving in the wasted "
            "face, the thin hand on the plank's edge "
            "closing into a fist of strength it has "
            "not owned in years — four enormous "
            "words, performed in a whisper. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b14", "out": "s14-it.jpeg", "seg": "n3",
        "window": "76.40-77.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLANKMAN"],
        "narration": "That's it.",
        "must_show": "the aftermath's simplicity — the old man SITTING UP on his plank unassisted, looking at his own raised hands; the sons frozen mid-wonder behind.",
        "must_not_show": "no halo, glare or rim-light; the sitting-up the whole event — decades reversed in one ordinary motion.",
        "scene": (
            "On the plank the old man has sat "
            "himself up — unassisted, spine straight, "
            "the rust blanket fallen to his lap — and "
            "he is looking at his own two raised "
            "hands turning in the gold light, while "
            "behind him his broad sons stand frozen "
            "mid-reach, their help suddenly and "
            "forever unnecessary. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b15", "out": "s15-no-list.jpeg", "seg": "n3",
        "window": "79.91-81.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "No list.",
        "must_show": "the unrecorded scale — the ledge's crowd from above, dense with risings and embraces, utterly unlisted; no scribe anywhere, no count being kept.",
        "must_not_show": "no halo, glare or rim-light; the absence of record the beat — history's biggest unlisted afternoon.",
        "scene": (
            "From above, the ledge works its "
            "unrecorded wonders in bulk: figures "
            "rising off litters across the whole "
            "grassy shelf, embraces closing over "
            "healed heads, a plank being turned into "
            "a bench by the family that no longer "
            "needs it — and nowhere in the crowd a "
            "scribe, a tally, a register: heaven's "
            "busiest ledger page, left blank on "
            "purpose. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r068-b16", "out": "s16-he-sat-down-where-he.jpeg", "seg": "n0",
        "window": "7.77-10.01", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN"],
        "narration": "He sat down where he could be found.",
        "must_show": "findability — the seated figure on his ledge seen from the path below: visible, reachable, positioned for discovery; accessibility as location.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the sightline the beat — from the path, he can be SEEN.",
        "scene": (
            "From the climbing path's first turn the "
            "seated figure is plainly visible above — "
            "cream against the green ledge, framed by "
            "two boulders, exactly where any climber's "
            "eye lands first — not hidden on the "
            "summit, not lost in a valley: seated at "
            "the precise findable height of a man who "
            "wants to be found. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b17", "out": "s17-somewhere-on-that-mountain-a.jpeg", "seg": "n4",
        "window": "88.67-97.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["MUTEWOMAN", "MOUNTAIN"],
        "narration": (
            "Somewhere on that mountain, a woman who had never spoken said her "
            "husband's name for the first time. Somewhere an old man's eyes "
            "came open on his children's faces."
        ),
        "must_show": "the first word — the silent woman's mouth shaping a name, her hands at her own throat in wonder, her husband's face shattering with joy an inch away.",
        "must_not_show": "no halo, glare or rim-light; the speaking's smallness — one name, one listener, the whole world changed at conversation distance.",
        "scene": (
            "Close in the golden afternoon: the "
            "gentle-faced woman's lips move around "
            "their first word — a name — her own "
            "hands flying to her throat at the sound "
            "of herself, her dark speaking eyes "
            "enormous — and an inch away her stocky "
            "husband's face is coming apart with joy, "
            "a man hearing thirty-five years of "
            "silence end with his own name inside "
            "the first sentence. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b18", "out": "s18-somewhere-legs-that-had-been.jpeg", "seg": "n4",
        "window": "97.78-102.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLANKMAN", "MOUNTAIN"],
        "narration": (
            "Somewhere legs that had been carried up the mountain carried their "
            "owner back down it."
        ),
        "must_show": "the reversal walk — the old father WALKING down the path on his own legs, his sons carrying only the empty plank behind him; the mountain descended by its own miracle.",
        "must_not_show": "no halo, glare or rim-light; the empty plank the trophy — carried down light, its cargo self-propelled ahead.",
        "scene": (
            "Down the switchbacked path the old "
            "father walks on his own legs — white "
            "beard in the descent's breeze, his stride "
            "careful then bolder then almost showing "
            "off — while behind him his two broad "
            "sons carry between them nothing but the "
            "empty plank, swinging light as a ladder, "
            "the day's whole story told by what is on "
            "it: nothing. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b19", "out": "s19-multiply-that-by-a-hillside.jpeg", "seg": "n4",
        "window": "102.10-105.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": "Multiply that by a hillside. That was the afternoon.",
        "must_show": "the multiplication — the whole slope in late gold: risings, first steps, embraces and astonishments scattered across every ledge; the afternoon at full scale.",
        "must_not_show": "no halo, glare or rim-light; joy in the dozens — every knot on the hillside its own healed story.",
        "scene": (
            "The whole mountainside works in the late "
            "gold: on every ledge and grass shelf its "
            "own small resurrection — a man testing "
            "new legs between two friends, a family "
            "wept around an elder whose eyes track "
            "their faces, a child running a first "
            "circle while her mother laughs into her "
            "hands — dozens of separate stories "
            "detonating quietly all over one hill in "
            "one single afternoon. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b20", "out": "s20-and-matthew-tells-you-what.jpeg", "seg": "n5",
        "window": "106.37-108.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": "And Matthew tells you what the crowd did with it:",
        "must_show": "the response gathering — faces across the crowd turning from their private joys toward something communal: wonder becoming worship in the turning.",
        "must_not_show": "no halo, glare or rim-light; the pivot from receiving to praising — faces lifting together.",
        "scene": (
            "Across the crowded ledge the private "
            "joys begin to turn communal: faces "
            "lifting from embraces, hands rising from "
            "healed shoulders, the hillside's many "
            "separate wonders turning toward one "
            "another and upward — a crowd discovering "
            "that what happened to each of them "
            "happened to all of them, and beginning, "
            "in the turning, to say so. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b21", "out": "s21-insomuch-that-the-multitude-wondered.jpeg", "seg": "s31",
        "window": "109.50-120.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": (
            "Insomuch that the multitude wondered, when they saw the dumb to "
            "speak, the maimed to be whole, the lame to walk, and the blind to "
            "see: and they glorified the God of Israel."
        ),
        "must_show": "SCRIPTURE-EXACT: the glorifying — the hillside crowd with arms and faces lifted in open praise, the healed among them as the evidence; worship at landscape scale.",
        "must_not_show": "no halo, glare or rim-light; no heaven imagery — praise as raised human arms and lifted faces on a real hill.",
        "scene": (
            "The mountainside praises, the camera behind the "
            "nearest lifted arms: across the "
            "ledges the multitude stands with arms "
            "and faces lifted — the healed themselves "
            "raised highest, the old father's arms up "
            "on his own legs, the speaking woman's "
            "voice audibly in the middle of it — a "
            "whole region glorifying the God of "
            "Israel from an eastern hillside, with "
            "the lake burning gold below them. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b22", "out": "s22-they-came-carrying-people.jpeg", "seg": "n1",
        "window": "19.45-21.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "They came carrying people.",
        "must_show": "the freight distilled — a close still: a rough plank litter's worn grips, rubbed smooth by carrying hands; love's equipment.",
        "must_not_show": "no halo, glare or rim-light; the object as testament — grips worn by devotion's mileage.",
        "scene": (
            "A close still on the path's stone: a "
            "rough board litter set down at rest, its "
            "two carrying-ends rubbed pale and smooth "
            "by years of the same gripping hands, a "
            "folded rust blanket squared on its "
            "boards — the plain freight equipment of "
            "a family's love, between journeys. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b23", "out": "s23-they-could-not-believe-their.jpeg", "seg": "n5b",
        "window": "121.54-134.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "MUTEWOMAN", "PLANKMAN"],
        "narration": (
            "They could not believe their eyes — people who had never spoken "
            "were talking, broken bodies were whole, the lame were walking, the "
            "blind could see."
        ),
        "must_show": "the four wonders live — one wide frame holding all four named categories in their healed states: the speaking woman mid-sentence, whole limbs at work, walkers walking, a see-er seeing.",
        "must_not_show": "no halo, glare or rim-light; one continuous scene, never panels — the verse's four verbs distributed naturally through one crowd.",
        "scene": (
            "One wide golden frame holds the verse's "
            "four verbs at work: near the front the "
            "madder-rose-veiled woman talks — TALKS — "
            "with three astonished neighbours; beyond "
            "her a man flexes a restored arm at his "
            "own eye level like new equipment; the "
            "old father demonstrates his walking to a "
            "circle of laughing strangers; and at the "
            "ledge's edge an elder stands seeing, "
            "turning slowly through the whole "
            "lake-and-sky view like a man drinking. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r068-b24", "out": "s24-somebody-led-a-blind-neighbor.jpeg", "seg": "n1",
        "window": "31.02-35.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "Somebody led a blind neighbor by the hand over every single stone.",
        "must_show": "the led climb — close on the two joined hands and the guiding voice's mouth mid-warning; navigation as friendship, stone by stone.",
        "must_not_show": "no halo, glare or rim-light; the grip's care the picture — two hands and a thousand stones.",
        "scene": (
            "Close on the climb: two hands joined — "
            "the guide's leading grip firm and turned "
            "back, the blind neighbour's following "
            "hand trusting it completely — while the "
            "guide's half-turned face calls the next "
            "stone's shape over his shoulder, and two "
            "pairs of feet negotiate one boulder "
            "between them — a mile of mountain being "
            "translated, word by word and grip by "
            "grip, into a friend's darkness. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b25", "out": "s25-on-that-side-of-the.jpeg", "seg": "n5b",
        "window": "134.02-141.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "On that side of the sea, many of them were outsiders to Israel "
            "entirely. The healing preached better than any sermon."
        ),
        "must_show": "the line crossed — Decapolis faces among the praising crowd: foreign dress details mixed through the earth tones, outsiders glorifying the God of Israel.",
        "must_not_show": "no halo, glare or rim-light; the mixture dignified — Greek-styled cloaks and fringed shawls praising side by side.",
        "scene": (
            "Through the praising crowd the mixture "
            "shows: a Greek-cut cloak beside a "
            "fringed prayer shawl, a Decapolis "
            "merchant's clipped beard beside a "
            "Galilean farmer's full one, foreign "
            "amulets forgotten on chests whose owners "
            "have their arms raised to Israel's God — "
            "a border erased for one afternoon by "
            "evidence no argument ever matched. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b26", "out": "s26-and-here-is-the-detail.jpeg", "seg": "n6",
        "window": "141.93-144.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": "And here is the detail people miss: they stayed.",
        "must_show": "the staying — the hillside at dusk with the crowd SETTLING, not leaving: cloaks spread, small fires kindling, families bedding down on the ledges.",
        "must_not_show": "no halo, glare or rim-light; the camp forming — nobody's face pointed downhill; home postponed by wonder.",
        "scene": (
            "Dusk comes down and the hillside does "
            "not empty: across the ledges the crowd "
            "settles instead — cloaks spread on the "
            "grass, small cook-fires kindling in "
            "stone rings, children already asleep on "
            "laps, the healed and their carriers "
            "sitting shoulder to shoulder in the "
            "failing gold — a multitude voting with "
            "its bedding to stay near the reason it "
            "climbed. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r068-b27", "out": "s27-three-days-on-a-mountainside.jpeg", "seg": "n6",
        "window": "144.95-150.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": (
            "Three days, on a mountainside, until the food ran out — and nobody "
            "wanted to go home."
        ),
        "must_show": "the third day — the camp aged visibly: fire-rings blackened, provision cloths shaken empty, faces thinner and still HAPPY; hunger outvoted by belonging.",
        "must_not_show": "no halo, glare or rim-light; the empty cloths plain — food gone, joy not; a camp past its supplies and past caring.",
        "scene": (
            "Three days deep, the hillside camp shows "
            "its age: fire-rings blackened and cold "
            "at their edges, provision cloths shaken "
            "out and folded empty, a last crust "
            "divided four ways between children — "
            "and everywhere on the thinner faces the "
            "same unreasonable contentment, a crowd "
            "that has run entirely out of bread and "
            "not at all out of reasons to stay. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r068-b28", "out": "s28-when-the-disciples-started-worrying.jpeg", "seg": "n6",
        "window": "150.71-156.19", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "MOUNTAIN"],
        "narration": (
            "When the disciples started worrying about the crowd's empty "
            "stomachs, listen to what Jesus said:"
        ),
        "must_show": "the worry brought — Peter and another disciple crouched by Jesus gesturing at the vast hungry camp; logistics meeting compassion.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the disciples' concern practical and kind — bookkeepers of an impossible kitchen.",
        "scene": (
            "By Jesus's ledge in the third morning's "
            "light Peter crouches with another "
            "disciple, one arm sweeping the vast "
            "camped hillside below — thousands, no "
            "bread, three days — the honest arithmetic "
            "of two practical men laid out before "
            "their teacher, whose face is already "
            "listening past the numbers to the "
            "stomachs inside them. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b29", "out": "s29-i-have-compassion-on-the.jpeg", "seg": "j1",
        "window": "156.89-168.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN"],
        "narration": (
            "I have compassion on the multitude, because they continue with me "
            "now three days, and have nothing to eat: and I will not send them "
            "away fasting, lest they faint in the way."
        ),
        "must_show": "SCRIPTURE-EXACT: the compassion spoken — close on Jesus's face looking out over the camped thousands: the counting of their days and their hunger visible as tenderness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the verse's arithmetic in his eyes — three days counted, every stomach carried.",
        "scene": (
            "Close on Jesus in the third morning's "
            "light, his gaze moving slow across the "
            "camped hillside below — and the whole "
            "verse resident in his face: the three "
            "days counted like a shepherd counts "
            "nights, the empty provision cloths "
            "noticed one by one, the long hungry "
            "road home already walked in his mind on "
            "their behalf — compassion doing its "
            "quiet bookkeeping before it feeds "
            "anyone. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r068-b30", "out": "s30-no-names.jpeg", "seg": "n3",
        "window": "77.38-78.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN"],
        "narration": "No names.",
        "must_show": "anonymity honoured — a healed stranger's joyful face among the crowd, never to be identified; one of the thousands the verse covers without naming.",
        "must_not_show": "no halo, glare or rim-light; the facelessness of the record against the face's full reality — one anonymous joy.",
        "scene": (
            "Close in the golden crowd: one healed "
            "stranger's face — a middle-aged woman "
            "laughing upward with tears standing on "
            "her cheeks, whole in some way the frame "
            "does not even need to specify — one of "
            "the afternoon's thousands, fully real "
            "and forever unnamed, her whole story "
            "carried by history inside three words "
            "of someone else's sentence. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b31", "out": "s31-i-feel-for-these-people.jpeg", "seg": "n6b",
        "window": "169.49-171.42", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN"],
        "narration": "I feel for these people, he said.",
        "must_show": "the feeling plain — Jesus's face over the camp: not policy, not strategy, plain human feeling for hungry people; the sentence at face value.",
        "must_not_show": "no halo, glare or rim-light on Jesus; unadorned sympathy — the row's simplest close-up.",
        "scene": (
            "Close on Jesus's face in the morning "
            "light, the camped multitude soft below "
            "his gaze: nothing in the expression but "
            "the sentence itself — plain human "
            "feeling for tired hungry people who "
            "stayed too long because they loved "
            "being near him — sympathy with no "
            "agenda item behind it, wearing its own "
            "face. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r068-b32", "out": "s32-they-have-been-with-me.jpeg", "seg": "n6b",
        "window": "171.42-179.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": (
            "They have been with me three days now and they have nothing to "
            "eat, and I am not sending them home hungry, in case they collapse "
            "on the way."
        ),
        "must_show": "the road foreseen — Jesus's gaze following the long descent path toward the far villages: the hungry journey home, pre-walked by his concern; the crowd safe behind him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the path's length the beat — compassion doing route-planning.",
        "scene": (
            "From the ledge Jesus's gaze runs down "
            "the long descent path as it switchbacks "
            "toward the shore and the far village "
            "smoke — miles of hungry walking measured "
            "out in one look — while behind him the "
            "camped thousands wait in the morning "
            "light, unaware that their journey home "
            "has already been walked, weighed and "
            "vetoed on their behalf by the man on "
            "the rock. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r068-b33", "out": "s33-he-noticed-their-stomachs-he.jpeg", "seg": "n7",
        "window": "180.36-185.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD"],
        "narration": (
            "He noticed their stomachs. He had just remade their bodies, and he "
            "was thinking about their lunch."
        ),
        "must_show": "the scale inversion — a close still: a healed man's strong restored hand holding an empty bread cloth; the big miracle done, the small need seen.",
        "must_not_show": "no halo, glare or rim-light; the two facts in one frame — remade hand, empty cloth.",
        "scene": (
            "A close still in the morning light: a "
            "man's strong restored hand — whole, "
            "steady, remade three days ago on this "
            "very hill — holding an empty provision "
            "cloth shaken out to its last crumbs "
            "— the greater miracle and the smaller "
            "need resting in the same palm, both of "
            "them, as it turns out, on the same "
            "agenda. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r068-b34", "out": "s34-that-is-who-sat-down.jpeg", "seg": "n7",
        "window": "185.45-197.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": (
            "That is who sat down on that mountain: not a distant power taking "
            "appointments, but a God who counts the days you have been carrying "
            "something heavy, and cares how far you have to walk home."
        ),
        "must_show": "the character summed — Jesus seated again on his ledge amid the camped crowd, a child asleep against his knee, the healed and their families near; power at family distance.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the nearness the doctrine — no appointment distance anywhere in the frame.",
        "scene": (
            "On his rock ledge Jesus sits amid the "
            "third morning's camp — a child asleep "
            "against his knee, the old father sitting "
            "close enough to lean, the speaking woman "
            "and her husband cross-legged in the "
            "first ring of many — the whole hillside "
            "arranged around him at the distance "
            "families keep, not the distance thrones "
            "do: a God findable by anyone with a "
            "plank and a hill's worth of love. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r068-b35", "out": "s35-thousands-of-the-greatest-moments.jpeg", "seg": "n3",
        "window": "81.19-88.02", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNTAIN", "CROWD"],
        "narration": (
            "Thousands of the greatest moments of thousands of lives, all "
            "hidden inside one quiet sentence."
        ),
        "must_show": "the closing image — the mountainside at golden hour, the whole healed multitude spread across it, and the lake's gold below: the quiet sentence's entire hidden cargo, in one frame.",
        "must_not_show": "no halo, glare or rim-light; the vastness tender — thousands of stories, one hillside, one light.",
        "scene": (
            "The mountainside at golden hour, the camera far off "
            "taking the whole slope from the side, holds "
            "everything the sentence hides: the "
            "healed multitude spread across every "
            "ledge and grass shelf — walkers and "
            "speakers and see-ers and the carried-"
            "no-longer, their families around them, "
            "their empty litters stacked like old "
            "history — and below it all the lake "
            "lying in beaten gold to the far hills: "
            "thousands of lives' greatest afternoons, "
            "folded into four words and one hill. "
            "Every figure has two arms, two hands "
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
