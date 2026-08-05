#!/usr/bin/env python3
"""V2 beat map — row 155, build-155-falling-away (2 Thessalonians 2:1-3).

COVERAGE: 22 pictures over 123.1 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (2 Thessalonians 2 KJV):
  2:1-2 the Thessalonians SHAKEN by rumor "that the day of Christ is
        at hand" — "be not soon shaken in mind, or be troubled,
        neither by spirit, nor by word, nor by LETTER AS FROM US."
  2:3   "Let no man deceive you by any means: for that day shall not
        come, EXCEPT THERE COME A FALLING AWAY FIRST, and that man
        of sin be revealed, the son of perdition."

ROW INTENT: the foretold-apostasy row (BRIDGE) — the dimming was
predicted, which means the returning was always in the plan. Dread
turned to hope; the row's engine is the GREAT LAMPSTAND: lit,
dimming flame by flame, dark, then RELIT flame by flame (the 154
relighting rhyme).

RENDERING LAWS:
  - PAUL is ROW 138's canon face — the lock below is byte-identical
    to build-138 (compact, balding, pointed beard, rust-brown);
    face-board against 138.
  - THE MAN OF SIN (b17) is NAMED IN THE VERSE, NEVER DEPICTED — no
    sinister figure, no shadowed villain, ever; the beat stays on
    the letter and the hearers. Automatic reject otherwise.
  - The falling-away is rendered as DIMMING AND DRIFT — lampstand
    flames going out, figures drifting from a lit assembly into
    dusk — sorrowful, never sneering at anyone; no villains among
    the drifters.
  - The believers are YOUNG-CHURCH ordinary — house-congregation
    scale, honest fear, honest steadying.
  - b18's night carries its DAWN — the east faintly paling; the
    warning's hope built into the sky.
  - b22's close TAKES the flame (contrast 154's open hand): the
    offered light received.

TIME OF DAY ARC (intentional): the rattled assembly at lamplit
evening; Paul's writing at deep lamplit night; the dimming frames
into true dusk and dark (deliberate); b18's night with paling east;
the relighting into warm growing lamplight; the close bright with
taken flame.

CHANGING CONDITIONS (kept OUT of the locks): the great lampstand —
full-lit, dimming flame by flame, dark, relit flame by flame; the
assembly room — full, thinning, empty, refilling.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream (not in this row). PAUL is
# byte-identical to build-138.
LOCKS = {
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact "
        "and wiry, about fifty, balding with a fringe of dark hair, "
        "a full pointed dark beard, keen deep-set eyes, in a plain "
        "DARK RUST-BROWN travel robe (never cream, never white); a "
        "tentmaker's strong hands; earnest fire without anger."
    ),
    "ROOM": (
        "ROOM LOCK: Paul's writing room — a small plain rented "
        "chamber at night: a work table with tentmaker's tools "
        "pushed aside, one clay lamp, parchment and reed pens. The "
        "same room throughout."
    ),
    "HALL": (
        "HALL LOCK: the Thessalonian assembly — a modest house-"
        "courtyard congregation space with benches and a GREAT "
        "STANDING LAMPSTAND of many small flames at its centre. The "
        "same courtyard and lampstand throughout."
    ),
    "BELIEVERS": (
        "BELIEVERS LOCK: the young church — ordinary Thessalonian "
        "believers in earth-toned robes of brown, rust, olive and "
        "slate (no cream — only Jesus wears cream): labourers, "
        "traders, mothers, a few elders; varied honest faces, "
        "never uniform."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r155-b01", "out": "s01-the-young-believers-in-thessalonica.jpeg", "seg": "n1",
        "window": "0.28-2.68", "wide": True, "jesus": False, "ref": False,
        "locks": ["HALL", "BELIEVERS"],
        "narration": "The young believers in Thessalonica were rattled.",
        "must_show": "the rattled assembly — the lamplit courtyard congregation in anxious knots, worried murmuring, the great lampstand burning full at centre; fear moving through a young church.",
        "must_not_show": "no halo; the fear HONEST — worry, not panic-theatre; the lampstand FULL-lit (its arc begins whole).",
        "scene": (
            "The young church is worried in every corner of "
            "its courtyard, the camera looking across the "
            "benches past the gathered believers' backs: "
            "knots of them stand murmuring in the lamplight — "
            "a trader's hands working as he whispers, two "
            "mothers close-headed, an elder rubbing his "
            "brow — while at the centre the great standing "
            "lampstand burns at its full count of flames, "
            "steady over a congregation that is anything "
            "but — Thessalonica's young believers, rattled "
            "to the benches by news nobody can verify. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r155-b02", "out": "s02-so-paul-sat-down-to.jpeg", "seg": "n1",
        "window": "8.50-11.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "ROOM"],
        "narration": "So Paul sat down to write them a steadying letter.",
        "must_show": "the steadying pen — Paul at his lamplit work table, tentmaker's tools pushed aside, the letter begun; calm purpose in the compact frame.",
        "must_not_show": "no halo; script indistinct; the tools PUSHED ASIDE — the tentmaker at his other trade.",
        "scene": (
            "The steadying arrives by courier, and it starts "
            "here: Paul at the small work table in the "
            "lamp's ring, the awls and canvas of the day-"
            "trade pushed to the table's edge, a fresh "
            "parchment squared before him and the reed pen "
            "already moving — the compact shoulders set, "
            "the keen eyes calm — a rattled congregation "
            "eight hundred miles away about to be talked "
            "down off its fear by a man writing at night "
            "after a full day's tentmaking. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r155-b03", "out": "s03-his-first-word-to-them.jpeg", "seg": "n2",
        "window": "12.05-13.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "ROOM"],
        "narration": "His first word to them was calm.",
        "must_show": "the calm — close on Paul's steady face over the page, the lamp's small flame unwavering beside; calm as a deliberate opening move.",
        "must_not_show": "no halo; the lamp-flame STEADY (mirroring him); script indistinct.",
        "scene": (
            "The letter's first ingredient is the writer's "
            "own pulse: close on Paul's face bent over the "
            "page — level, unhurried, the keen eyes moving "
            "at thinking speed and not one beat faster — "
            "while beside the parchment the clay lamp's "
            "small flame stands perfectly unwavering in "
            "the still night air — calm, chosen on "
            "purpose as the opening word, by a man who "
            "knows that frightened people read the tone "
            "before they read the words. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r155-b04", "out": "s04-do-not-let-yourselves-be.jpeg", "seg": "n2",
        "window": "13.81-25.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "Do not let yourselves be shaken or alarmed, he said, by every "
            "excited rumor and secondhand report, or stampeded into fear by "
            "things you cannot even trace to their source."
        ),
        "must_show": "the rumor-chain — down a lamplit lane, the whisper passing mouth to ear to mouth, faces more alarmed at each link; the untraceable source visible as distortion.",
        "must_not_show": "no halo; the chain READABLE — each teller more agitated; no villain, just human telephone.",
        "scene": (
            "Watch the rumor grow an arm's length at a "
            "time: down the lamplit lane the whisper "
            "travels mouth to ear to mouth — the first "
            "teller merely worried, the second wide-eyed, "
            "the third gripping his listener's sleeve — "
            "each link adding heat and losing source, "
            "until what began as a question arrives at "
            "the lane's end as a certainty on fire — the "
            "exact machinery Paul's letter is written to "
            "jam: excited, secondhand, and traceable to "
            "absolutely nobody. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r155-b05", "out": "s05-he-wanted-them-anchored-not.jpeg", "seg": "n3",
        "window": "25.71-29.65", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "He wanted them anchored, not tossed around by the loudest voice in the room.",
        "must_show": "the anchor — in a chopping harbour, ONE ship riding steady at its anchor line while smaller loose boats toss; steadiness as equipment, not temperament.",
        "must_not_show": "no halo; the anchored ship visibly CALM in the same chop tossing the others.",
        "scene": (
            "Same harbour, same chop, two entirely "
            "different nights: across the wind-scuffed "
            "water the loose boats toss and swing at "
            "every gust — masts describing anxious arcs — "
            "while in their midst one ship rides steady, "
            "bow held true to the weather by the taut "
            "line running down to an anchor nobody can "
            "see — the difference not in the water but in "
            "the ground-tackle: anchored, versus at the "
            "mercy of whatever blows loudest. No people "
            "are needed in this frame."
        ),
    },
    {
        "id": "v2-r155-b06", "out": "s06-feelings-and-hearsay-are-not.jpeg", "seg": "n3",
        "window": "29.65-35.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["BELIEVERS"],
        "narration": (
            "Feelings and hearsay are not the same as truth, and a "
            "frightened crowd is rarely a wise one."
        ),
        "must_show": "crowd vs reader — the agitated swirl of alarmed believers, and at its edge ONE seated figure reading the actual letter, still and clear.",
        "must_not_show": "no halo; the contrast exact — swirling agitation around one anchored reader.",
        "scene": (
            "One person in the courtyard is consulting a "
            "source: around the benches the alarm swirls — "
            "gestures flying, voices overlapping, fear "
            "feeding fear in the lamplight — while at the "
            "swirl's edge a single believer sits still "
            "with the actual letter open in her hands, "
            "reading, her face clearing line by line — "
            "feelings loose in the room and truth seated "
            "at its edge, and the difference between them "
            "visible in one woman's quieting shoulders. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r155-b07", "out": "s07-before-the-end-there-would.jpeg", "seg": "n4",
        "window": "55.05-58.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": "Before the end, there would come a falling away.",
        "must_show": "the dimming begins — the great lampstand with its FIRST flames gone out, thin smoke threads rising from cooled wicks, the light lessened; sorrowful, not sinister.",
        "must_not_show": "no halo; the going-out SORROWFUL — thin smoke, growing shadow; no dark force depicted.",
        "scene": (
            "The prophecy begins at the lampstand, one "
            "flame at a time: across the great stand's "
            "many small cups the first few have gone "
            "out — thin threads of smoke rising straight "
            "from the cooled wicks, the courtyard's "
            "shadows reaching a little further in — no "
            "wind did it, no hand in frame: just the slow "
            "foretold lessening, light withdrawing from "
            "places that held it — a falling away, "
            "beginning the way such things begin: "
            "quietly, at the edges, first. No people are "
            "needed in this frame."
        ),
    },
    {
        "id": "v2-r155-b08", "out": "s08-that-ye-be-not-soon.jpeg", "seg": "kv2",
        "window": "36.03-45.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL", "BELIEVERS"],
        "narration": (
            "That ye be not soon shaken in mind, or be troubled, neither by "
            "spirit, nor by word, nor by letter as from us, as that the day "
            "of Christ is at hand."
        ),
        "must_show": "SCRIPTURE-EXACT: the letter read — an elder reading Paul's letter aloud to the gathered assembly, the steadying visibly landing; the lampstand still full behind.",
        "must_not_show": "no halo; script indistinct; the calming VISIBLE — shoulders lowering along the benches.",
        "scene": (
            "The letter does its work out loud: the elder "
            "stands by the full-lit lampstand with Paul's "
            "parchment held high, reading the steadying "
            "clauses into the courtyard's hush — be NOT "
            "soon shaken — not by spirit, nor word, nor "
            "forged letter — and along the benches the "
            "young church's shoulders come down inch by "
            "inch, the rattled faces stilling as apostolic "
            "calm arrives by courier and gets read "
            "directly into the room's fear. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r155-b09", "out": "s09-then-paul-told-them-plainly.jpeg", "seg": "n4",
        "window": "46.79-49.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "ROOM"],
        "narration": "Then Paul told them plainly what to watch for.",
        "must_show": "the plain telling — Paul's direct level face, pen lifted mid-thought; the watchman's clarity before the hard sentence.",
        "must_not_show": "no halo; PLAINNESS the register — no drama in the face, only clarity.",
        "scene": (
            "The next paragraph requires the writer's "
            "plainest voice: Paul's pen lifts from the "
            "page and the keen eyes fix on the middle "
            "distance where hard sentences get composed — "
            "no softening under consideration, no "
            "riddling — the tentmaker's directness "
            "gathering itself to tell a young frightened "
            "church exactly what must happen first, "
            "because the kindest thing a watchman owns "
            "is his plainness. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r155-b10", "out": "s10-that-day-he-said-would.jpeg", "seg": "n4",
        "window": "49.05-55.05", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That day, he said, would not arrive until something else "
            "happened first — and it was sobering."
        ),
        "must_show": "the sequence — a long road with TWO waymark stones: a near one and a far one; the near marker unmistakably FIRST on the way; order as geography.",
        "must_not_show": "no halo; the two markers' ORDER readable — near first, far after; the road one road.",
        "scene": (
            "The schedule is laid out in roadside stone: "
            "the long road runs toward the horizon "
            "carrying two waymarks — a near stone standing "
            "plain at the first rise, and far beyond it, "
            "small with distance, the second — no route "
            "to the far one that does not pass the near "
            "one first, no shortcut anywhere in the "
            "geography — that day, says the letter, "
            "stands at the SECOND stone; and the first, "
            "sobering marker has a name. No people are "
            "in this frame."
        ),
    },
    {
        "id": "v2-r155-b11", "out": "s11-a-drifting-from-the-truth.jpeg", "seg": "n5",
        "window": "58.90-62.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": "A drifting from the truth. A dimming of the light that had been lit.",
        "must_show": "the dimming advanced — the lampstand with MOST flames now out, the courtyard's dark grown; the light that HAD been lit, going.",
        "must_not_show": "no halo; sorrow not menace — smoke threads, deep shadow, the few flames precious.",
        "scene": (
            "The lampstand keeps the prophecy's ledger: "
            "most of its cups stand dark now — wick after "
            "cooled wick down the branching arms, the "
            "courtyard's benches sunk in grown shadow, "
            "the few surviving flames burning precious "
            "and small — a light that was LIT, dimming — "
            "not attacked, not stormed: drifted from, "
            "cup by cup, keeper by keeper, until the "
            "room that blazed remembers blazing. No "
            "people are needed in this frame."
        ),
    },
    {
        "id": "v2-r155-b12", "out": "s12-many-hearts-over-time-turning.jpeg", "seg": "n5",
        "window": "62.50-70.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL", "BELIEVERS"],
        "narration": (
            "Many hearts, over time, turning away from what the apostles had "
            "actually given them, until much of it was lost from view."
        ),
        "must_show": "the drift — figures leaving the dimming courtyard one by one through the gate into dusk, unhurried, ordinary; the assembly thinning; sorrowful, no villains.",
        "must_not_show": "ABSOLUTE: no villains among the drifters — ordinary people drifting; the sorrow in the thinning room.",
        "scene": (
            "Nobody slams the gate on the way out of a "
            "drift: through the courtyard's arch the "
            "figures leave one and two at a time into the "
            "dusk — unhurried, unpursued, ordinary people "
            "with ordinary reasons, each departure small "
            "enough to explain — while behind them the "
            "benches thin and the dimming lampstand holds "
            "what light it still has — hearts turning "
            "away by degrees, over years, until what the "
            "apostles actually handed over stands mostly "
            "in shadow, mostly unvisited. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r155-b13", "out": "s13-but-here-is-the-part.jpeg", "seg": "n6",
        "window": "70.83-73.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "ROOM"],
        "narration": "But here is the part that turns dread into hope.",
        "must_show": "the turn — Paul's face lifting from the hard paragraph with the letter's hope arriving in it; the writer ahead of his readers' dread.",
        "must_not_show": "no halo; the lift READABLE — gravity turning toward hope.",
        "scene": (
            "The writer knows something the hard paragraph "
            "hides: Paul's face comes up from the page — "
            "and the gravity in it is turning, the way a "
            "key turns: the keen eyes warming over the "
            "sobering lines he has just set down, the "
            "pointed beard lifting a degree — because the "
            "man writing the warning can already see "
            "around its corner, to the part that makes "
            "the dread survivable: foretold, all of it, "
            "on purpose. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r155-b14", "out": "s14-paul-is-telling-them-ahead.jpeg", "seg": "n6",
        "window": "73.62-80.66", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Paul is telling them ahead of time. A falling away would not "
            "mean God had failed, or his plan had broken."
        ),
        "must_show": "foretold = plan intact — the storm-warned household register (152 rhyme): a father pointing at FAR weather while the family prepares calmly; known in advance as proof of care.",
        "must_not_show": "no halo; the storm FAR; the calm preparation the picture.",
        "scene": (
            "A warning ahead of time is the signature of a "
            "plan still working: at the farm door the "
            "father's arm aims his family's eyes at the "
            "far dark line of building weather — hours "
            "off, plainly seen — and the household moves "
            "easy through its preparations, flock folding, "
            "shutters going to, nobody's hands shaking — "
            "because weather that is POINTED AT before it "
            "arrives is weather inside somebody's "
            "foresight — and foresight is the opposite of "
            "a plan gone wrong. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r155-b15", "out": "s15-it-would-mean-the-very.jpeg", "seg": "n6",
        "window": "80.66-84.16", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "It would mean the very thing he predicted was coming to pass.",
        "must_show": "the fulfilled marker — a traveller on the long road PASSING the near waymark stone exactly as mapped; the map held open and trusted MORE; prediction confirming the guide.",
        "must_not_show": "no halo; the passing exact — hand or map acknowledging the FIRST stone; the far marker still ahead.",
        "scene": (
            "Reaching the grim landmark proves the map: "
            "the traveller comes level with the near "
            "waymark stone — exactly where the drawn "
            "route said it would stand — and his hand "
            "drops briefly onto its weathered top while "
            "the far marker waits small on the horizon "
            "ahead — not thrown by the landmark: "
            "CONFIRMED by it — a hard place on the road "
            "that, by being exactly where the guide "
            "said, makes the guide worth trusting to the "
            "end. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r155-b16", "out": "s16-rumors-were-flying-that-the.jpeg", "seg": "n1",
        "window": "2.68-8.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL", "BELIEVERS"],
        "narration": (
            "Rumors were flying that the great Day of the Lord had already "
            "come, and they were frightened and confused."
        ),
        "must_show": "the rumor at flight — an agitated messenger in the courtyard waving a LETTER (the forged one), alarm radiating; the specific false report landing.",
        "must_not_show": "no halo; script indistinct on the waved letter; the messenger sincere-alarmed, not villainous.",
        "scene": (
            "The rumor arrives holding paperwork: into the "
            "lamplit courtyard bursts an agitated "
            "messenger with a letter held high — as from "
            "PAUL, he cries, the Day already COME — and "
            "alarm radiates off the benches in a widening "
            "ring: a mother's hand to her mouth, an elder "
            "rising, voices overlapping into fright — the "
            "great Day, missed?! — a young church's worst "
            "fear delivered by a sincere man waving a "
            "forgery nobody yet knows is one. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r155-b17", "out": "s17-let-no-man-deceive-you.jpeg", "seg": "kv3",
        "window": "84.78-94.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL", "BELIEVERS"],
        "narration": (
            "Let no man deceive you by any means: for that day shall not "
            "come, except there come a falling away first, and that man of "
            "sin be revealed, the son of perdition;"
        ),
        "must_show": "SCRIPTURE-EXACT: the verse heard — the elder reading the hard clause to the hushed assembly, sober faces receiving it; THE MAN OF SIN NEVER DEPICTED — the letter and hearers only.",
        "must_not_show": "ABSOLUTE: no sinister figure, no shadowed villain anywhere — the named clause stays in the READ text; sober hush the frame.",
        "scene": (
            "The hardest clause is read into a hush that "
            "holds: the elder's voice carries the verse "
            "over the benches — let NO man deceive you — "
            "a falling away FIRST — and the courtyard "
            "receives it at full sobriety: faces going "
            "grave down the rows, a father's arm "
            "circling his son's shoulders, the lampstand "
            "flames steady over people learning the "
            "road's true order — the dark words present "
            "only as words, weighed in lamplight by a "
            "church being told the truth on purpose. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r155-b18", "out": "s18-and-you-do-not-warn.jpeg", "seg": "n7",
        "window": "95.61-99.24", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And you do not warn people about a night unless a morning is meant to follow.",
        "must_show": "the night with its dawn built in — a deep quiet night landscape whose EASTERN sky is already faintly paling; the warning's hope in the horizon.",
        "must_not_show": "no halo; the paling FAINT but unmistakable — night honest, morning certain.",
        "scene": (
            "Read the night's fine print along its eastern "
            "edge: the land lies deep in honest dark — "
            "hills black, valleys held, the small hours "
            "doing their long work — but low on the "
            "eastern rim the sky has begun its faint "
            "paling, one shade, two, the first grey of a "
            "morning already in the mail — because "
            "warnings about night are only ever issued by "
            "someone who intends a dawn — and this "
            "night's horizon is signed. No people are in "
            "this frame."
        ),
    },
    {
        "id": "v2-r155-b19", "out": "s19-a-falling-away-only-makes.jpeg", "seg": "n7",
        "window": "99.24-107.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "A falling away only makes sense if there is something to fall "
            "back to — a truth that can be restored, brought back, and lit "
            "again."
        ),
        "must_show": "the relighting begun — at the dark lampstand, a carried flame touching the FIRST cold wick alight again (the 154 rhyme); restoration starting where the dimming did.",
        "must_not_show": "no halo; the FIRST catch exact — one wick alight, the dark stand waiting; flame physical.",
        "scene": (
            "The word 'away' has always implied an "
            "address: at the dark lampstand a carried "
            "flame tips against the first cold wick — and "
            "it CATCHES, light climbing back into the "
            "little cup, the nearest branching arms "
            "warming out of the long shadow — one flame "
            "returned to a stand built for dozens — "
            "because a falling AWAY only grammars if "
            "there is a something to fall away FROM, and "
            "whatever can be left can, on purpose, be "
            "lit again. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r155-b20", "out": "s20-so-this-hard-little-verse.jpeg", "seg": "n8",
        "window": "108.39-111.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "ROOM"],
        "narration": "So this hard little verse is really a quiet promise.",
        "must_show": "the promise in plain ink — Paul's finished letter held gently in his hands, the lamp warm on it; hard words, kind purpose.",
        "must_not_show": "no halo; script indistinct; the HOLDING gentle — a letter written in love.",
        "scene": (
            "The hard verse cools into what it always was: "
            "Paul holds the finished letter gently in both "
            "hands in the lamp's warmth, reading his own "
            "hard sentences back — the falling away, the "
            "sober order of things — and his face over "
            "them is not grim but tender: a watchman's "
            "letter, every difficult clause of it laid "
            "down so that people he loves will not be "
            "shaken when the road does what roads do — "
            "a promise, wearing warning's clothes. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r155-b21", "out": "s21-the-dimming-was-foretold-which.jpeg", "seg": "n8",
        "window": "111.76-116.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["HALL"],
        "narration": (
            "The dimming was foretold, which means the returning was always "
            "part of the plan."
        ),
        "must_show": "the relighting advanced — the lampstand catching flame by flame down its arms, the courtyard warming back; the returning in visible progress.",
        "must_not_show": "no halo; the progression READABLE — several lit, more catching, the dark retreating.",
        "scene": (
            "The stand relights in the same order it "
            "darkened, reversed: flame by flame the cups "
            "catch down the branching arms — three "
            "burning, then five, then eight, the "
            "courtyard's benches warming back out of "
            "their long shadow, the walls remembering "
            "their colour — a returning with the same "
            "unhurried certainty as the dimming, because "
            "both halves were always in the one plan: "
            "foretold going, foretold coming back. No "
            "people are needed in this frame."
        ),
    },
    {
        "id": "v2-r155-b22", "out": "s22-so-the-only-question-is.jpeg", "seg": "n8",
        "window": "116.36-122.79", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "So the only question is a hopeful one. When the light is "
            "offered again, will you know it, and take hold?"
        ),
        "must_show": "the closing take — an offered flame passing to a REACHING hand that closes around the lamp's handle; the light received (contrast 154's open ending); hope answered.",
        "must_not_show": "no halo; the TAKING exact — fingers closing on the handle, flame steady between two people.",
        "scene": (
            "This row's last frame answers the one before "
            "it ever asks: the offered lamp passes "
            "between two hands — the giver's steady, the "
            "receiver's REACHING, fingers closing warm "
            "around the clay handle with the flame riding "
            "steady through the exchange — offered again, "
            "the narration says, and here is the other "
            "half the question hopes for: known, and "
            "taken hold of — light changing keeping "
            "without losing a degree of its burning. "
            "Every figure has two arms, two hands and "
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
    # HALL --take from build-22 REJECTED (the parable king's hall — a modest
    # Thessalonian house-courtyard with its lampstand is its own place).
    # Promote-first from b01.
}
# === end PLACE-PLATES ===
