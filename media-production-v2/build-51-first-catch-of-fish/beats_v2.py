#!/usr/bin/env python3
"""V2 beat map — row 51, build-51-first-catch-of-fish (Luke 5:1-11).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 26 pictures over 144.4 s narration = 5.6 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Luke 5:1-11 KJV):
  v1   the people PRESSED UPON HIM to hear the word of God; he stood by the
       lake of Gennesaret.
  v2   TWO SHIPS standing by the lake; the fishermen were GONE OUT OF THEM,
       WASHING THEIR NETS. (They fished all night — every early shot carries
       that exhaustion; morning light throughout.)
  v3   he entered SIMON'S ship, prayed him to THRUST OUT A LITTLE from the
       land; SAT DOWN and taught the people OUT OF THE SHIP.
  v4   "Launch out into the deep, and let down your nets for a draught." (jv4)
  v5   "Master, we have toiled all the night, and have taken nothing:
       nevertheless AT THY WORD I will let down the net." (s5)
  v6   they inclosed a GREAT MULTITUDE of fishes: and their NET BRAKE.
  v7   they BECKONED unto their PARTNERS in the OTHER ship; both ships filled
       so that they BEGAN TO SINK — loaded low, gunwales near the water.
  v8   Simon Peter FELL DOWN AT JESUS' KNEES: "Depart from me; for I am a
       sinful man, O Lord." (s8)
  v9   he was ASTONISHED, and ALL THAT WERE WITH HIM.
  v10  the partners are named: JAMES AND JOHN, sons of Zebedee. "Fear not;
       from henceforth thou shalt catch men." (jv10)
  v11  they brought their ships TO LAND, FORSOOK ALL, and FOLLOWED HIM — the
       greatest catch of their lives left lying on the shore.

CONTENT-CARE: row 51 is not in the §3 flag table = GREEN.

TIME-OF-DAY ARC: the whole story is ONE MORNING after a night's fishing —
soft low early-morning light at the shore, brightening toward mid-morning out
on the deep, full late-morning sun for the catch, the kneeling and the leaving.
Never sunset colouring.

BOAT LAW (Standing Law j): every figure in a boat stays visibly INSIDE it —
deck under feet, gunwale connecting around them; ropes and nets connect to
rigging and water, never to nothing.

CAST-REF NOTE: when the first still with Simon's face is ACCEPTED at QC, copy
it to CAST-REF-V2/simon-ref.jpeg and add
"char_refs": ["CAST-REF-V2/simon-ref.jpeg"] to every later legible-face beat.
Same for James and John together (jamesjohn-ref.jpeg: b17, b25, b26) and the
crewman (crewman-ref.jpeg). Text locks alone do not hold a face.
"""

# AUDIO-FIX 2026-08-07 (Machine A `Dev`): "tear" → "tare" pronunciation fix.
# The authoritative V1 mp4 (2026-07-29) says "teer" (/tɪr/, crying) where n4 has
# "the net began to tear" — Cameron: "still mispronouncing tear it should be like
# tare but its still spelled the same". n4 (the ONLY segment with "tear") was
# re-voiced through the SAME locked ElevenLabs NARRATOR voice ("Brian", 44100/128k
# — the earlier orphaned fix used the WRONG engine, edge-tts 24000/48k) with the
# spoken word respelled "tear" → "tare" (= /tɛr/, the rip sense Cameron named; the
# caption text stays "tear"), atempo-matched back to the original duration (10.266s)
# so no still-window moves. Corrected mp3 lives in the V1 dir's audio/. This flag
# makes v2_assemble rebuild narration from the V1-dir mp3s at the extract_beats
# offsets (the fix the STALE-V1 guard recommends) so the shipped cut says "tare".
# Nothing else changed: same voice, same wording, same timing outside n4.
AUDIO_FROM_V1_SEGMENTS = True

LOCKS = {
    "SIMON": (
        "SIMON LOCK: Simon is the same man in every shot — a fisherman of "
        "about thirty-five, thick-set and powerful through the shoulders, "
        "deeply weathered olive-brown skin, dark curly hair, a full dark "
        "beard, heavy brows over quick dark eyes, rope-scarred hands. He "
        "wears a coarse DARK CHARCOAL-BROWN wool work tunic, sleeves pushed "
        "up, with a wide worn leather belt, the whole garment stained and "
        "stiff with lake water and fish oil — plainly darker than sky or "
        "water, never cream, never white. His face is shown clearly."
    ),
    "CREWMAN": (
        "CREWMAN LOCK: the crewman in Simon's boat is the same man in every "
        "shot — mid-twenties, lean and wiry, short dark hair, a sparse young "
        "dark beard, in a DARK OLIVE-BROWN wool work tunic with a plain rope "
        "belt, barefoot on the deck; never cream, never white."
    ),
    "JAMESJOHN": (
        "JAMES AND JOHN LOCK: the partners in the second boat are the same "
        "two brothers in every shot — James about thirty, square-built, a "
        "full dark beard and heavy forearms, in a DEEP RUSSET-BROWN wool "
        "work tunic; John about twenty, the youngest of them all, "
        "clean-jawed with only the first shadow of a beard, dark hair to "
        "the ears, in a DUSTY DARK INDIGO wool work tunic. Both wear plain "
        "leather belts; neither wears cream, off-white or any pale "
        "near-white cloth."
    ),
    "LAKE": (
        "LAKE LOCK: the lake of Gennesaret in early morning — calm grey-blue "
        "water going bright toward the east, a curved pebble-and-shingle "
        "shore, low green-brown hills folding down to the far waterline, "
        "gulls over the shallows. The crowd on the shore are ordinary "
        "Galilean working people in SATURATED DEEP earth colours — dark "
        "chocolate brown, deep russet, burnt ochre, dark olive and dusty "
        "indigo wool — every garment plainly darker than the pale morning "
        "sky and water; no one in the crowd wears cream, off-white, ivory "
        "or any pale near-white cloth."
    ),
    "BOATS": (
        "BOATS LOCK: the two fishing boats are the same in every shot — "
        "broad-beamed working boats of dark oiled cedar planking about "
        "eight paces long, a single stubby mast with the sail furled, oars "
        "shipped along the gunwales, and heaps of brown knotted flax nets "
        "with small stone sinkers. Everyone aboard stands or kneels plainly "
        "INSIDE the hull, deck under their feet, the gunwale running "
        "unbroken around them; every rope leads to rigging, net or water, "
        "never out of frame to nothing."
    ),
}

REF = True

# Identity law: SIMON in this row IS Peter — the same actor as the global
# PETER sheet in every video. The token "SIMON" does not auto-attach the
# global cast (it matches by token name), so pin it here. JAMESJOHN is a
# combined token for the partner boat's brothers — both sheets attached.
REFS = {
    "SIMON": ["../CAST-V2-REF/peter-front.jpeg", "../CAST-V2-REF/peter-quarter.jpeg"],
    "JAMESJOHN": ["../CAST-V2-REF/james-z-front.jpeg", "../CAST-V2-REF/john-front.jpeg"],
}

BEATS = [
    {
        "id": "v2-r051-b01", "out": "s01-the-crowd-pressed.jpeg", "seg": "n1 p1",
        "window": "0.28-5.20", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LAKE"],
        "narration": ("By the lake of Gennesaret, a crowd pressed in around "
                      "him, hungry to hear the word of God."),
        "must_show": "v1 — the press of the crowd at the water's edge, every gaze converging on Jesus.",
        "must_not_show": "no halo/glow; he is being crowded toward the waterline, not enthroned.",
        "scene": (
            "On the pebble shore in soft early-morning light, the "
            "camera at the water's edge taking shore and crowd "
            "from the side, Jesus stands "
            "almost at the waterline with the crowd pressing close around "
            "him in a tightening half-ring — working men, mothers with "
            "children on their hips, old men leaning in — every face turned "
            "hungrily to him, the front rank barely an arm's length away, "
            "the lake flat and bright behind him. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b02", "out": "s02-two-empty-boats.jpeg", "seg": "n1 p2a",
        "window": "5.20-9.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAKE", "BOATS"],
        "narration": "Two empty boats sat at the water's edge,",
        "must_show": "v2 — the two boats drawn up and empty, nets draped, the night's failure written in their emptiness.",
        "must_not_show": "no fish anywhere in either boat — that emptiness is the story's setup.",
        "scene": (
            "The two dark cedar fishing boats sit beached side by side at "
            "the shingle's edge in low morning light, empty — oars shipped, "
            "sails furled, wet brown nets hanging over their gunwales and "
            "not one fish in either hull. Down the shore beyond them the "
            "crowd around the distant teacher is a soft blur. Gulls stand "
            "idle on the stones; there is nothing here for them either."
        ),
    },
    {
        "id": "v2-r051-b03", "out": "s03-washing-empty-nets.jpeg", "seg": "n1 p2b",
        "window": "9.50-14.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "CREWMAN", "LAKE"],
        "narration": ("and beside them tired fishermen were washing out their "
                      "nets after a long night that had given them nothing."),
        "must_show": "the exhaustion — men ankle-deep in the shallows rinsing nets that held nothing, faces grey with the night.",
        "must_not_show": "no anger — just bone-tiredness; the failure is old news by morning.",
        "scene": (
            "Simon stands ankle-deep in the cold shallows dragging a long "
            "brown net through the water to rinse it, his charcoal-brown "
            "tunic soaked to the thigh, his bearded face slack and grey "
            "with a whole night's wasted work — and beside him the young "
            "crewman in olive-brown crouches on the wet stones picking "
            "weed from another fold of net, eyes half-shut. The empty "
            "boats stand behind them. Soft early light. Exactly two people "
            "are in the frame; each has two arms, two hands, two legs and "
            "one head."
        ),
    },
    {
        "id": "v2-r051-b04", "out": "s04-he-stepped-aboard.jpeg", "seg": "n2 p1-p2",
        "window": "14.52-18.18", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "LAKE", "BOATS"],
        "narration": ("He stepped into one of the boats. It belonged to a "
                      "fisherman named Simon."),
        "must_show": "v3 — Jesus stepping over the gunwale into Simon's beached boat; Simon looking up from his net, surprised.",
        "must_not_show": "no ceremony — a working boat borrowed plainly; Simon has no idea yet.",
        "scene": (
            "Jesus steps unhurried over the gunwale into the beached boat, "
            "one hand steadying himself on the stubby mast, plainly INSIDE "
            "the hull with the deck taking his weight — while Simon, a few "
            "steps off in the shallows with the dripping net still in his "
            "fists, has looked up mid-task at the stranger boarding his "
            "boat, surprise just breaking through the tiredness on his "
            "face. Morning light off the water. Exactly two people are in "
            "the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b05", "out": "s05-taught-from-the-water.jpeg", "seg": "n2 p3",
        "window": "18.18-24.75", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SIMON", "LAKE", "BOATS"],
        "narration": ("He asked him to push out a little way from the shore, "
                      "and then he sat down and taught the people from the "
                      "water."),
        "must_show": "v3 — Jesus SEATED in the floating boat a little off shore, teaching; the crowd banked along the waterline listening; Simon at the oars.",
        "must_not_show": "the boat is only a LITTLE way out — voices carry; not the deep yet.",
        "scene": (
            "The boat floats a stone's throw off the beach on flat "
            "bright water, the camera on the beach behind the "
            "banked crowd's shoulders looking out to it, on "
            "water, and Jesus SITS in the stern teaching, one hand moving "
            "with the words, fully inside the hull — Simon rests on the "
            "oars amidships, holding her steady, watching this stranger "
            "over his shoulder — while along the curved shoreline the "
            "whole crowd has settled to listen, a bank of deep russet, "
            "olive and indigo figures at the water's edge, every face "
            "turned out toward the boat. Morning sun climbing. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b06", "out": "s06-launch-out.jpeg", "seg": "jv4",
        "window": "24.75-29.68", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "LAKE", "BOATS"],
        "narration": ("Launch out into the deep, and let down your nets for a "
                      "draught. (Luke 5:4)"),
        "must_show": "v4 — Jesus turned to Simon, the quiet instruction; his hand indicating the open deep water.",
        "must_not_show": "no grand gesture; a working man's word to a working man.",
        "scene": (
            "In the floating boat Jesus has turned from the shore to face "
            "Simon at close quarters, his face calm and direct, one hand "
            "lifted in a small open motion out toward the wide empty water "
            "beyond the bow — and Simon, still at the oars, looks back at "
            "him from under heavy brows, the words just reaching him. Both "
            "men fully inside the hull, the far shore low behind them. "
            "Exactly two people are in the frame; each has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r051-b07", "out": "s07-bone-tired.jpeg", "seg": "n3 p1",
        "window": "29.68-31.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": "Simon was bone-tired.",
        "must_show": "close on Simon's face — the full weight of the sleepless night on it.",
        "must_not_show": "no exaggerated yawning; the tiredness sits deep and still.",
        "scene": (
            "A tight shot of Simon's weathered face in the climbing morning "
            "light: red-rimmed eyes, salt dried white in the creases at his "
            "temples and in his dark beard, the heavy-lidded thousand-yard "
            "look of a man at the end of a wasted night, his jaw set while "
            "he thinks. Exactly one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r051-b08", "out": "s08-every-instinct.jpeg", "seg": "n3 p2",
        "window": "31.18-37.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "BOATS"],
        "narration": ("They had worked that water all night and come back "
                      "with nothing, and every instinct a fisherman has told "
                      "him this was pointless."),
        "must_show": "the professional's doubt — Simon's eyes on the folded nets and the bright dead water; daytime is the WRONG time to fish.",
        "must_not_show": "no contempt toward Jesus in his face; the argument is with the lake, not the man.",
        "scene": (
            "Simon looks down at the heap of wet brown net piled amidships "
            "between his feet, one scarred hand resting on the folds, then "
            "out across the flat glaring mid-morning water where no "
            "fisherman would waste a cast — his face running the whole "
            "argument: wrong hour, wrong light, empty lake, a carpenter "
            "telling a fisherman his trade. Exactly one person is in the "
            "frame, inside the hull, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b09", "out": "s09-something-about-this-man.jpeg", "seg": "n3 p3",
        "window": "37.74-41.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": ("But something about this man made him answer the way "
                      "he did."),
        "must_show": "the turn — Simon's eyes coming up from the nets to Jesus's face, and something shifting.",
        "must_not_show": "no words yet; this frame is the look between them.",
        "scene": (
            "A close two-shot low in the boat: Simon's eyes have come up "
            "from the piled net to Jesus's face, and Jesus meets the look "
            "without blinking, steady and unhurried — and in the "
            "fisherman's heavy tired features something is visibly "
            "shifting, the professional certainty loosening its grip. "
            "Bright morning light off the water on both faces. Exactly two "
            "people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r051-b10", "out": "s10-at-thy-word.jpeg", "seg": "s5",
        "window": "41.77-50.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "BOATS"],
        "narration": ("Master, we have toiled all the night, and have taken "
                      "nothing: nevertheless at thy word I will let down the "
                      "net. (Luke 5:5)"),
        "must_show": "v5 — Simon mid-sentence, honest about the night, already reaching for the net as he says it.",
        "must_not_show": "not grudging — tired obedience with the first grain of faith in it.",
        "scene": (
            "Simon speaks straight at Jesus, his jaw working through the "
            "sentence, one hand thrown open toward the empty hull as "
            "witness of the empty night — but his other hand has already "
            "closed on the top fold of the piled net, the body obeying "
            "before the speech is even finished. Jesus listens from the "
            "stern, calm. Both men fully inside the hull. Exactly two "
            "people are in the frame; each has two arms, two hands of "
            "five fingers each and one head."
        ),
    },
    {
        "id": "v2-r051-b11", "out": "s11-out-to-the-deep.jpeg", "seg": "n3b p1-p2",
        "window": "50.34-56.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "CREWMAN", "LAKE", "BOATS"],
        "narration": ("Master, we worked that lake all night and caught "
                      "nothing. But because you say so, I will put the net "
                      "down again."),
        "must_show": "the boat pulling for the deep — oars in the water, the shore falling behind.",
        "must_not_show": "the second boat stays at the shore in this frame; only Simon's goes out.",
        "scene": (
            "The single boat pulls away across open water toward the deep, "
            "Simon and the young crewman bent to the oars in matched "
            "stroke, wakes curling off the blades, the crowd and the "
            "beached second boat shrinking on the bright shoreline behind "
            "the stern — and Jesus sits in the stern facing forward past "
            "the rowers toward the open lake. All three fully inside the "
            "hull. Late-morning sun on the water. Exactly three people are "
            "in the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b12", "out": "s12-the-net-goes-down.jpeg", "seg": "n3b p3-p4",
        "window": "56.65-63.44", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "CREWMAN", "LAKE", "BOATS"],
        "narration": ("Hear the word in the middle of that sentence. He had "
                      "every reason to say no, and he did it anyway."),
        "must_show": "the act of faith itself — the net paying out over the side into deep water, both men committed.",
        "must_not_show": "no fish yet — the water is still and gives no promise; that is the whole point of the frame.",
        "scene": (
            "Out on the still deep water Simon and the crewman stand "
            "braced inside the hull feeding the long brown net steadily "
            "out over the gunwale, the flax folds sliding from their "
            "hands into dark blue water that shows them absolutely "
            "nothing back, stone sinkers dropping away — an act of pure "
            "obedience on an empty lake. Jesus watches from the stern, "
            "still. Every rope runs from their hands over the gunwale "
            "into the water. Exactly three people are in the frame; each "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b13", "out": "s13-the-nets-filled.jpeg", "seg": "n4 p1",
        "window": "63.44-65.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "CREWMAN", "LAKE", "BOATS"],
        "narration": "The moment the nets went down, they filled.",
        "must_show": "v6 — the instant of the miracle: the ropes snapping taut, the water beginning to boil silver alongside.",
        "must_not_show": "no light effect; the miracle is fish and physics.",
        "scene": (
            "The net-ropes in both men's hands have snapped violently taut "
            "over the gunwale, jerking Simon and the crewman forward "
            "against their own grip, and alongside the hull the dark water "
            "has erupted into a churning, flashing mass of silver just "
            "under the surface — the lake that gave nothing all night "
            "suddenly alive from nowhere. Both men fully inside the hull, "
            "braced, the ropes running straight from their fists into the "
            "boiling water. Exactly two people are in the frame; each has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b14", "out": "s14-the-net-began-to-tear.jpeg", "seg": "n4 p2",
        "window": "65.63-74.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "CREWMAN", "LAKE", "BOATS"],
        "narration": ("A great shining mass of fish, far more than the ropes "
                      "were made to hold, and the net began to tear under "
                      "the sheer weight of it."),
        "must_show": "v6 — the net at the surface bulging with silver fish, flax strands visibly parting; the men heaving with everything they have.",
        "must_not_show": "the fish stay IN the water and net at this beat — not heaped in the boat yet.",
        "scene": (
            "Simon and the crewman haul side by side, backs bent double "
            "over the gunwale, forearms corded, dragging the net up to "
            "the surface where it bulges wide with a shining, heaving "
            "mass of silver fish — and along one strained seam the brown "
            "flax cords are visibly parting strand by strand under the "
            "impossible weight. Water sheets off the rising net. Both men "
            "fully inside the hull, feet braced on the deck. Late-morning "
            "sun blazing on the catch. Exactly two people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b15", "out": "s15-too-many-for-one-boat.jpeg", "seg": "n5 p1",
        "window": "74.20-75.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON", "CREWMAN", "LAKE", "BOATS"],
        "narration": "There were too many for one boat.",
        "must_show": "the problem of abundance — fish coming over the gunwale in a silver spill, the boat already listing.",
        "must_not_show": "the boat lists but does not swamp yet.",
        "scene": (
            "The catch comes over the side in a broad silver spill as both "
            "men tip a full bight of net inboard — fish sliding and "
            "slapping across the deck boards around their bare feet, the "
            "hull visibly heeled toward the heavy net still in the water, "
            "and Simon's face, caught mid-haul, is beginning to understand "
            "that the problem now is that the boat is too small. Both men "
            "fully inside the hull. Exactly two people are in the frame; "
            "each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b16", "out": "s16-they-waved-for-help.jpeg", "seg": "n5 p2a",
        "window": "75.85-80.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["CREWMAN", "LAKE", "BOATS"],
        "narration": ("They waved to their partners, James and John, in the "
                      "other boat to come and help,"),
        "must_show": "v7 — the beckoning: arms up signalling across the water; the far boat already pulling toward them.",
        "must_not_show": "shouting distance is too far — the SIGNAL is the communication.",
        "scene": (
            "The young crewman stands braced on the fish-slicked "
            "deck, the camera off the beam holding both boats in "
            "profile across the water, with "
            "both arms swinging high over his head in great urgent arcs, "
            "signalling across the bright water — and in the middle "
            "distance the second dark boat has already answered, bow "
            "swinging round, two figures pulling hard at its oars toward "
            "them. The loaded net still bulges alongside the near hull. "
            "Everyone fully inside their boats. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b17", "out": "s17-both-boats-sinking.jpeg", "seg": "n5 p2b",
        "window": "80.50-85.60", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SIMON", "CREWMAN", "JAMESJOHN", "LAKE", "BOATS"],
        "narration": ("and both boats were loaded until they sat low in the "
                      "water and began to sink."),
        "must_show": "v7 — the two boats side by side heaped with silver, gunwales riding at a hand's breadth from the waterline.",
        "must_not_show": "low and dangerous, but nobody bailing, nobody in the water — awed, not drowning.",
        "scene": (
            "The two boats lie lashed side by side on the bright "
            "water, the camera low off their beam so both hulls "
            "and the waterline read in profile, "
            "both heaped to the thwarts with glittering silver fish, both "
            "hulls pressed so deep that the water stands within a hand's "
            "breadth of the gunwales — Simon, the crewman, and the two "
            "brothers James and John all stand knee-deep in their own "
            "catch, gone still now, looking at what has happened to them, "
            "while Jesus sits calm in the stern of Simon's boat. All five "
            "fully inside the hulls. Blazing late-morning sun. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b18", "out": "s18-at-his-knees.jpeg", "seg": "n6 p1",
        "window": "85.60-88.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "LAKE", "BOATS"],
        "narration": "When Simon saw it, he fell down at Jesus' knees.",
        "must_show": "v8 — Simon DOWN, knees among the fish, gripping at Jesus's knees; the boat's silver hoard all around them.",
        "must_not_show": "no worship pose from paintings — a man collapsing where he stood.",
        "scene": (
            "Simon has gone down heavily onto his knees in the slither of "
            "silver fish covering the deck, his scarred hands gripping at "
            "Jesus's knees where he sits in the stern, his head dropping — "
            "a big man folding like his strings were cut, fish still "
            "sliding against his shins. Jesus looks down at him, utterly "
            "unafraid of the moment. Both fully inside the hull. Exactly "
            "two people are in the frame; each has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r051-b19", "out": "s19-not-thank-you.jpeg", "seg": "n6 p2",
        "window": "88.30-93.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["SIMON"],
        "narration": ("He did not feel worthy of any of it, and what came "
                      "out of him was not thank you."),
        "must_show": "close on Simon's stricken upturned face — the wonder curdling into unworthiness.",
        "must_not_show": "not fear of danger — fear of holiness; there is a difference and it lives in the eyes.",
        "scene": (
            "A tight shot of Simon's upturned face from just above: the "
            "triumph a fisherman should be wearing on the best morning of "
            "his life is nowhere in it — instead his eyes are wide and "
            "wet and frightened in a way deep water never frightened him, "
            "his mouth already forming words that are the opposite of "
            "thank you. Bright sun, silver fish blurred beneath him. "
            "Exactly one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r051-b20", "out": "s20-depart-from-me.jpeg", "seg": "s8",
        "window": "93.95-98.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": "Depart from me; for I am a sinful man, O Lord. (Luke 5:8)",
        "must_show": "v8 — the sentence itself: Simon at Jesus's knees begging him to leave, and Jesus not moving an inch.",
        "must_not_show": "Jesus's face holds no offence and no pity-from-above — level, warm, staying.",
        "scene": (
            "Low in the fish-heaped stern, Simon kneels with his fists "
            "knotted in the cloth at Jesus's knee, face lifted and broken "
            "open on the words, begging this man to go away from him — "
            "and Jesus's face, close above his, receives it level and "
            "warm and entirely unmoving, the face of a man who has just "
            "been asked to leave and has already decided to stay forever. "
            "Exactly two people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r051-b21", "out": "s21-kneeling-in-fish.jpeg", "seg": "n6b p1-p2",
        "window": "98.50-106.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "CREWMAN", "JAMESJOHN", "LAKE", "BOATS"],
        "narration": ("Go away from me, Lord. On the best morning of his "
                      "working life, kneeling in fish, the first thing he "
                      "wanted was distance."),
        "must_show": "the whole strange picture — wealth heaped to the thwarts, and the man who caught it on his knees asking its giver to leave.",
        "must_not_show": "the other three men frozen where they stand, staring — nobody moves during this.",
        "scene": (
            "A wider frame of the lashed boats riding low: Simon kneels "
            "amid the shin-deep silver hoard at Jesus's knees, head down "
            "now — and around the two of them everything has stopped, the "
            "crewman frozen with a fish still in his hand, James and John "
            "standing motionless in their own loaded boat, every eye on "
            "the kneeling man and the seated one. The sun blazes on more "
            "wealth than any of them has ever seen, and nobody is looking "
            "at it. All figures fully inside the hulls. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r051-b22", "out": "s22-who-this-was.jpeg", "seg": "n6b p3",
        "window": "106.73-113.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": ("The wonder of it had shown him exactly who he was, "
                      "and exactly who this was."),
        "must_show": "the double recognition — Simon's raised eyes seeing Jesus truly for the first time.",
        "must_not_show": "no halo, no glow, no rim-light on Jesus; the revelation is in Simon's eyes, not the lighting.",
        "scene": (
            "A close two-shot: Simon's face has come up again, tear-tracks "
            "cutting the salt on his cheeks, and his eyes have changed — "
            "the fear still in them, but underneath it the dawning, "
            "unbearable recognition of exactly whose boat he has been "
            "arguing about fish in — while Jesus's calm face holds his "
            "gaze in the plain blazing daylight, an ordinary morning sky "
            "behind his dark hair and nothing shining anywhere but the "
            "sun on the water. Exactly two people are in the frame; each "
            "has one head."
        ),
    },
    {
        "id": "v2-r051-b23", "out": "s23-fear-not.jpeg", "seg": "jv10",
        "window": "113.04-118.18", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON"],
        "narration": ("Fear not; from henceforth thou shalt catch men. "
                      "(Luke 5:10)"),
        "must_show": "v10 — the calling: Jesus's hand coming to rest on the kneeling man's shoulder as he says it.",
        "must_not_show": "no pulling him up yet; the word lands first, the lifting comes after.",
        "scene": (
            "Jesus leans forward from the stern seat and sets his hand "
            "firmly on Simon's soaked shoulder, his face close over the "
            "kneeling fisherman, speaking the words with a small certain "
            "warmth at the corners of his mouth — the hand that answers "
            "'depart from me' by taking hold. Simon's stunned face begins "
            "to lift under it. Bright noon light. Exactly two people are "
            "in the frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r051-b24", "out": "s24-he-calls-him.jpeg", "seg": "n7",
        "window": "118.18-130.22", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "LAKE", "BOATS"],
        "narration": ("He does not send Simon away. He calls him. The "
                      "trembling fisherman who begged him to leave is the "
                      "very man he wants, and from this day on he will be "
                      "gathering people, not fish."),
        "must_show": "Simon being raised — Jesus drawing him up from the fish to his feet, face to face, the call replacing the fear.",
        "must_not_show": "Simon's trembling is not gone — he rises shaking, and comes anyway.",
        "scene": (
            "In the low-riding boat Jesus has risen to his feet on the "
            "deck and grips Simon's forearm, drawing the big man up out "
            "of the heaped silver fish — Simon coming up unsteady, "
            "knee-deep in the catch, his tear-streaked face a hand's "
            "breadth from Jesus's own, fear and calling fighting it out "
            "in his eyes and the calling winning. Both men fully inside "
            "the hull, the bright lake wide behind them. Exactly two "
            "people are in the frame; each has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r051-b25", "out": "s25-the-catch-left-lying.jpeg", "seg": "n8 p1-p2",
        "window": "130.22-137.97", "wide": True, "jesus": False, "ref": False,
        "locks": ["SIMON", "CREWMAN", "JAMESJOHN", "LAKE", "BOATS"],
        "narration": ("And that was enough. They brought the boats to land, "
                      "left the greatest catch of their lives lying there "
                      "on the shore, and followed him."),
        "must_show": "v11 — the beached boats and the mountain of silver fish ABANDONED on the shingle; the men already walking away from it.",
        "must_not_show": "nobody looks back at the fish; the fortune is behind them and staying there.",
        "scene": (
            "The two boats stand beached and heeled on the shingle, "
            "the camera behind the abandoned catch looking down "
            "the shore after the leaving men, and "
            "spilling from them across the wet stones lies the greatest "
            "catch four fishermen ever landed — a long shining silver "
            "drift of fish glittering unattended in the sun, gulls "
            "already dropping toward it — while beyond it the four men "
            "walk away up the shore together, their backs to their "
            "fortune, not one head turned around. Late-morning light. "
            "Every figure has two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r051-b26", "out": "s26-they-followed-him.jpeg", "seg": "n8 p3",
        "window": "137.97-144.10", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SIMON", "CREWMAN", "JAMESJOHN", "LAKE"],
        "narration": ("They forsook all, the nets, the boats, the best day "
                      "they had ever had, and went with him."),
        "must_show": "v11 — the following: Jesus ahead, the four behind him on the shore road, boats and catch small and left behind.",
        "must_not_show": "no turning, no waving goodbye — the leaving is finished; only the road ahead.",
        "scene": (
            "SHOT FROM BEHIND THE FIVE MEN, all of their backs to the "
            "camera as they walk AWAY from us along the curve of the "
            "shore road — Jesus a pace in front, Simon at his shoulder, "
            "the crewman and the two brothers falling in behind, every "
            "one of them faced up the road in the direction they are "
            "walking, their faces hidden because they are looking where "
            "they are going and not back — and far beyond them the road "
            "bends inland away from the water. The beached boats and the "
            "silver heap of the abandoned catch sit small at the frame's "
            "near edge, behind the walkers, growing smaller. An upright "
            "vertical photograph, the ground at the bottom of the frame "
            "and the sky at the top, the horizon level — the picture is "
            "the right way up. Every figure has two arms, two legs and "
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
}
# === end PLACE-PLATES ===
