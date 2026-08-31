#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 7: Two Trees.

Eden as the first classroom: two trees planted by God, a commandment with a
permission slip (Moses 3:17), the serpent's council-pitch in costume, and
Eve's brave choice. Anchors: Moses 3:16-17; Moses 4:5-12; 2 Nephi 2:16,
22-25.

The serpent is shown as scripture names it — a real serpent, never a
humanoid devil (Devil Law). Eve's choice is depicted as courage, never as
a fooled woman's blunder.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 307
NUM = 7
SLUG = "two-trees"
TITLE = "Two Trees"
META = "Moses 3-4 · 2 Nephi 2"

SEGMENTS = [
    ("n1", NARRATOR,
     "A garden. Two trees. And the whole plan balanced between them. Eden "
     "was not a paradise for lounging. It was the first classroom — and "
     "the lesson was choice."),
    ("n2", NARRATOR,
     "God planted the garden eastward in Eden, and put the man and the "
     "woman in it. Innocent. Deathless. Safe. And — read it carefully — "
     "not yet able to grow."),
    ("s1", SCRIPTURE,
     "And they would have had no children; wherefore they would have "
     "remained in a state of innocence, having no joy, for they knew no "
     "misery; doing no good, for they knew no sin."),
    ("n3", NARRATOR,
     "No joy — because no misery. No good — because no sin. Frozen. Eden "
     "was beautiful the way a photograph is beautiful. Perfect, and going "
     "nowhere."),
    ("n4", NARRATOR,
     "So God did something the critics never notice. He put two trees in "
     "the middle — the tree of life, and the tree of knowledge — and gave "
     "the one commandment that made choosing real. Listen to how He "
     "actually said it:"),
    ("g1", FATHER,
     "Of every tree of the garden thou mayest freely eat, but of the tree "
     "of the knowledge of good and evil, thou shalt not eat of it. "
     "Nevertheless, thou mayest choose for thyself, for it is given unto "
     "thee; but, remember that I forbid it."),
    ("n5", NARRATOR,
     "Thou mayest choose for thyself. Did you catch that? The forbidden "
     "tree came with a permission slip. God fenced it with a warning — "
     "and left the gate unlocked on purpose. Because a choice with only "
     "one option is not a choice."),
    ("s2", SCRIPTURE,
     "Wherefore, the Lord God gave unto man that he should act for "
     "himself. Wherefore, man could not act for himself save it should be "
     "that he was enticed by the one or the other."),
    ("n6", NARRATOR,
     "Enticed by the one or the other. Opposition is not sabotage of the "
     "plan — it is equipment. And right on schedule, the other enticement "
     "slid into the garden."),
    ("n7", NARRATOR,
     "The serpent came carrying the first lie ever told on this earth. "
     "Listen closely. You have heard this voice before."),
    ("d1", DEVIL,
     "Ye shall not surely die; for God doth know that in the day ye eat "
     "thereof, then your eyes shall be opened, and ye shall be as gods, "
     "knowing good and evil."),
    ("n8", NARRATOR,
     "Half-truths stitched with poison — his signature ever since. Their "
     "eyes would open; that part was true. But underneath it was the "
     "council pitch all over again: trust me instead of Him. He wanted "
     "the fall to happen his way. Under his flag."),
    ("n9", NARRATOR,
     "And here is what he has never once understood. He thought he was "
     "wrecking God's plan. He was springing it. The fall was always the "
     "doorway — the only question was whose hand would open the door."),
    ("n10", NARRATOR,
     "Eve weighed it. Scripture says she saw the tree was to be desired "
     "to make one wise. This was not a fooled woman blundering. It was "
     "the bravest decision ever made in innocence. She chose growth. Adam "
     "chose to stay with her. And the door opened."),
    ("n11", NARRATOR,
     "So the next time someone tells you Eden was the day everything went "
     "wrong, remember the two trees. God planted both. He named the "
     "price, honored the choice, and had the rescue already signed. That "
     "is not a God who lost control. That is a Father who refused to "
     "keep His children in a photograph."),
]

CARD_SEG = ("card", NARRATOR,
            "Eden was not the day it all went wrong. It was the day it "
            "all began.")

CARD_TEXT = ("The day it all began.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Seven — Two Trees")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="eden")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "Eden entire: from a high shoulder of the garden, an impossible "
        "green world — giant ancient trees, clear braided rivers, "
        "meadows of flowering grass, waterfalls smoking in morning "
        "light, herds moving unafraid in the open — beauty at a scale "
        "no fallen forest reaches. No people in frame yet.",
        "a vast pristine garden world of giant trees, braided rivers "
        "and unafraid herds in morning light",
        "buildings, paths, fences, people, drawn rays",
        wide=True)),
    ("p02", "n2", _p(
        "The innocents at home: Adam and Eve walk together through an "
        "open glade, seen from behind at a distance — a fallow deer "
        "walking calmly at Eve's hip, bright birds crossing low, "
        "neither human head turned back — the two of them utterly "
        "unafraid and utterly unhurried. Morning light through the "
        "canopy.",
        "the first couple from behind in a glade with a deer walking "
        "calmly beside them",
        "faces visible, clothing details modern, fear in any animal",
        wide=True, locks=["ADAM", "EVE"])),
    ("p03", "s1", _p(
        "Innocence, frozen: Adam and Eve stand motionless at the edge "
        "of a glass-still pool, seen in profile at a distance, their "
        "perfect reflections doubled in the water — two figures and "
        "their mirror images, nothing moving, not a ripple — beautiful "
        "and fixed as a painting that cannot change.",
        "the couple motionless in profile doubled by a mirror-still "
        "pool, nothing moving",
        "smiles, motion blur, animals, faces to camera",
        locks=["ADAM", "EVE"])),
    ("p04", "n3", _p(
        "Going nowhere: a single perfect fruit hanging heavy on its "
        "bough, skin flawless, dew beaded and holding, the light "
        "unchanging — extreme close, absolutely still, almost too "
        "perfect. Beauty with no clock running.",
        "one flawless dew-beaded fruit hanging in unchanging light, "
        "extreme close",
        "insects, decay, hands, text",
        )),
    ("p05", "n4", _p(
        "The two trees: on a gentle rise at the garden's heart, TWO "
        "great trees stand a stone's throw apart, balanced in one "
        "frame — the left one silver-barked and full of pale luminous "
        "fruit, the right one darker-leaved with deep amber fruit — "
        "equals in size and majesty, morning mist drifting between "
        "them. The choice, planted. No people, no serpent yet.",
        "two majestic trees balanced in one frame on a rise — pale "
        "luminous fruit on one, deep amber fruit on the other",
        "signs, fences, figures, snakes, one tree dominant",
        wide=True)),
    ("p06", "g1", _p(
        "The commandment: Adam and Eve kneel side by side in a glade "
        "flooded from ahead by a warm brilliance beyond the trees — "
        "the light of a Presence the frame does not show — both seen "
        "from behind at a reverent distance, heads lifted toward the "
        "brightness, the garden luminous around them. The light is "
        "environmental, from beyond the treeline, with no figure in "
        "it.",
        "the couple kneeling from behind, faces lifted to a warm "
        "brilliance beyond the trees, no figure in the light",
        "any figure or silhouette in the brightness, faces visible, "
        "drawn rays, halo shapes",
        locks=["ADAM", "EVE"])),
    ("p07", "n5", _p(
        "The unlocked gate: the knowledge tree's lowest bough in "
        "close-up — its deep amber fruit hanging exactly at an adult's "
        "easy reach over open ground, no fence, no thorn hedge, no "
        "barrier of any kind between the grass and the fruit — the "
        "reachability itself the whole subject.",
        "amber fruit at easy arm's height over open unfenced grass, "
        "close",
        "fences, thorns, warning of any kind, hands, serpent",
        )),
    ("p08", "s2", _p(
        "Enticed by the one or the other: Eve stands midway between "
        "the two trees, seen in full-length profile — her body still "
        "turned toward the silver tree of life behind her, but her "
        "face turned the other way, toward the dark-leaved tree ahead "
        "— caught exactly on the pivot of the ages, thinking. Neither "
        "tree touched.",
        "Eve in profile midway between the two trees, body toward "
        "one, face turned toward the other, thinking",
        "her eyes on the lens, the serpent visible, reaching yet, "
        "distress",
        locks=["EVE"])),
    ("p09", "n6", _p(
        "The other enticement arrives: a great serpent glides along a "
        "moss-covered branch into the frame — iridescent, muscular, "
        "unhurried, its head leading toward the frame's right where "
        "the amber fruit hangs soft-focus — a real magnificent animal, "
        "nothing cartoonish, its eye NOT aimed at the camera.",
        "a real iridescent serpent gliding along a branch toward "
        "soft-focus amber fruit",
        "cartoon features, a hooded cobra pose, eyes to the lens, "
        "fangs bared",
        )),
    ("p10", "n7", _p(
        "The voice you have heard before: under the knowledge tree's "
        "canopy the daylight COOLS — a soft formless dimming gathering "
        "in the leaves behind the serpent's branch, the garden's "
        "warmth failing just there and nowhere else — while beyond "
        "the cool pocket the garden stays bright. The serpent lies "
        "still on its branch; the dimming has no shape.",
        "a soft shapeless cooling of the light in the canopy around "
        "the still serpent's branch, bright garden beyond",
        "ANY figure or face in the dimness, smoke, the serpent "
        "looking at the lens",
        devil=True)),
    ("p11", "d1", _p(
        "The first lie: the serpent's head in sharp close-up beside "
        "the hanging amber fruit, forked tongue mid-flick, scales "
        "catching the cooled light — and beyond it, soft-focus, Eve's "
        "listening face turned toward it, attentive and unafraid. Her "
        "features stay recognizably hers even in blur.",
        "the serpent's head sharp beside the fruit, tongue mid-"
        "flick, Eve's soft-focus listening face beyond",
        "the serpent facing the lens, Eve sharp while it is sharp, "
        "fear on her face",
        locks=["EVE"], devil=True)),
    ("p12", "n8", _p(
        "The pitch working: Eve's face in strong close-up, thought "
        "visibly moving behind her eyes — not enchantment, ANALYSIS: "
        "brows drawn a degree, gaze fixed on the unseen fruit off-"
        "frame right, lips parted with an unasked question. The "
        "garden light warm on one cheek, the canopy's cool on the "
        "other.",
        "Eve's close face mid-analysis, warm light one cheek and "
        "cool the other, gaze fixed off-frame right",
        "her eyes on the lens, trance, tears, the serpent in frame",
        locks=["EVE"], devil=True)),
    ("p13", "n9", _p(
        "The garden holds its breath: a wide still frame of the two "
        "trees' rise from a distance — every bird silent on its "
        "branch, the mist stopped between the trunks, the light "
        "angled long and expectant across the grass — the hinge of "
        "history disguised as a quiet morning. No people visible "
        "from this distance.",
        "the two trees' rise wide and utterly still, long expectant "
        "light, birds perched silent",
        "figures readable, the serpent, weather drama, rays",
        wide=True)),
    ("p14", "n10", _p(
        "The bravest decision: Eve's hand closes around the amber "
        "fruit — grip firm, wrist steady, no tremble — and her face "
        "beyond it in three-quarter carries clear-eyed RESOLVE: chin "
        "level, eyes open and certain, the expression of a woman "
        "choosing growth with the price read. Nothing in the frame "
        "says fooled.",
        "Eve's firm hand closing on the fruit and her resolute "
        "clear-eyed three-quarter face beyond it",
        "trembling, tears, trance, the serpent visible, her eyes "
        "on the lens",
        locks=["EVE"])),
    ("p15", ("n10", 0.45), _p(
        "Adam chooses her, and the door: Adam's face in close "
        "three-quarter as Eve's hand offers the fruit into the "
        "frame's lower corner — his eyes on hers off-frame, the "
        "weight of the price fully in his face, and underneath it "
        "the settled decision of a man who will not be parted from "
        "his wife or the plan. His hand rises to receive.",
        "Adam's grave three-quarter face and rising hand as the "
        "fruit is offered into frame, decision settled",
        "his eyes on the lens, horror, the serpent, Eve's face in "
        "this frame",
        locks=["ADAM"])),
    ("p16", ("n10", 0.78), _p(
        "Eyes opened: the two of them side by side, faces close "
        "together in three-quarter, both gazes lifted OUT at the "
        "garden as if seeing it for the first time — awe, weight, "
        "and the first faint chill of mortality all arriving at "
        "once. Behind them the light has turned one degree toward "
        "evening.",
        "both faces close in three-quarter, newly opened eyes "
        "lifted out at the world, awe and weight together",
        "shame theatrics, nakedness emphasized, tears streaming, "
        "faces to camera",
        locks=["ADAM", "EVE"])),
    ("p17", "n11", _p(
        "Leaving with dignity: Adam and Eve walk hand in hand away "
        "from the camera down the long glade toward the garden's "
        "eastern gap, full-length from directly behind, heads up — "
        "not fleeing, WALKING, together, into what they chose. The "
        "camera stays low on the grass behind their heels.",
        "the couple hand in hand from directly behind, heads up, "
        "walking away down the glade toward the eastern gap",
        "faces or profiles, stooping, an angel, a sword",
        wide=True, locks=["ADAM", "EVE"])),
    ("p18", ("n11", 0.55), _p(
        "The trees behind them: from the threshold looking back — "
        "the two great trees small now at the glade's far end, the "
        "silver tree of life just catching a thin vertical line of "
        "white flame taking up its guard-post beside it in the far "
        "distance — the past sealing itself gently while the light "
        "goes amber.",
        "the two distant trees from the threshold with a thin far "
        "flame-line beginning its guard by the silver one",
        "an angel figure, a sword shape, faces, darkness",
        )),
    ("p19", ("n11", 0.8), _p(
        "The first morning outside: from just beyond the garden's "
        "threshold stones, the wild unmade world ahead under a "
        "sunrise immense and clean — hard ground, far mountains, a "
        "bright thread of river — everything unearned and possible. "
        "No people in frame; the door has just opened.",
        "the wild sunrise world waiting beyond the threshold "
        "stones, hard and beautiful",
        "figures, buildings, paths, drawn rays",
        wide=True)),
]
