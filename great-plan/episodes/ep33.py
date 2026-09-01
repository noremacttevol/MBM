#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 33: He Will Finish It.

The collision ends: every knee, the chain coming back around, the wheat
explaining the wait, becoming like Him, God wiping tears — and back to
the room where it started. Ends on the James 1:5 handoff: ask.
Anchors: Philippians 2:10-11; Revelation 20:1-3; Matthew 13:29-30;
2 Peter 3:9; 1 John 3:2; Romans 8:16-17; Revelation 21:3-4.

Devil Law to the last: even at the binding, he is a writhing mass of
formless darkness — never a figure, never a face.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 333
NUM = 33
SLUG = "he-will-finish-it"
TITLE = "He Will Finish It"
META = "Revelation 20-21 · 1 John 3"

SEGMENTS = [
    ("n1", NARRATOR,
     "Thirty-two episodes ago, two speeches collided in a council "
     "before the world. This is how it ends — and where you come in."),
    ("n2", NARRATOR,
     "The Son is coming back. Not as a baby this time — as the King. "
     "And every eye will see it."),
    ("s1", SCRIPTURE,
     "That at the name of Jesus every knee should bow, of things in "
     "heaven, and things in earth, and things under the earth; and "
     "that every tongue should confess that Jesus Christ is Lord, to "
     "the glory of God the Father."),
    ("n3", NARRATOR,
     "Every knee — including the one that rebelled first. And then, "
     "the sentence this whole war has been waiting for:"),
    ("s2", SCRIPTURE,
     "And I saw an angel come down from heaven, having the key of the "
     "bottomless pit and a great chain in his hand. And he laid hold on "
     "the dragon, that old serpent, which is the Devil, and Satan, and "
     "bound him a thousand years."),
    ("n4", NARRATOR,
     "Bound — with a great chain. The chain he flaunted over Enoch's "
     "world comes back around. And the earth gets a thousand years "
     "without his voice in the air."),
    ("n5", NARRATOR,
     "But why not today? If the King can end it, why the wait? He "
     "answered that himself — in a parable this series has already "
     "shown you:"),
    ("j1", JESUS,
     "Nay; lest while ye gather up the tares, ye root up also the "
     "wheat with them. Let both grow together until the harvest."),
    ("s3", SCRIPTURE,
     "The Lord is not slack concerning his promise, as some men count "
     "slackness; but is longsuffering to us-ward, not willing that any "
     "should perish, but that all should come to repentance."),
    ("n8", NARRATOR,
     "And when it is finished — what was it all FOR? John answers with "
     "the family secret of the entire plan:"),
    ("s4", SCRIPTURE,
     "Beloved, now are we the sons of God, and it doth not yet appear "
     "what we shall be: but we know that, when he shall appear, we "
     "shall be like him; for we shall see him as he is."),
    ("n9", NARRATOR,
     "Like him. That was the point in the council — children, growing "
     "up into what their Father is. The devil called that blasphemy. "
     "The Father calls it parenthood."),
    ("n10", NARRATOR,
     "Then the last scene of the old world — God's oldest gesture, and "
     "the answer, at last, to the God who wept with Enoch:"),
    ("s6", SCRIPTURE,
     "And God shall wipe away all tears from their eyes; and there "
     "shall be no more death, neither sorrow, nor crying, neither "
     "shall there be any more pain: for the former things are passed "
     "away."),
    ("n11", NARRATOR,
     "Back to the room where it started. He told us this would work — "
     "bodies, agency, a Savior, everything recoverable except the "
     "will to refuse. It worked. Thy will be done, and the glory be "
     "thine forever — and the glory, it turns out, is us. Home. So, "
     "one thing left: ask Him if it is true. He answered a farm boy "
     "in the woods. The invitation has your name on it. Ask."),
]

CARD_SEG = ("card", NARRATOR,
            "He told us it would work. It worked. Now ask Him yourself "
            "— the invitation has your name on it.")

CARD_TEXT = ("Ask Him yourself.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Thirty-Three — He Will Finish It")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="modern")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "Bookend: the pre-creation expanse from the very first frame of "
        "the series — deep indigo above, the eternal dawn's first gold "
        "along the infinite horizon — the exact image episode one "
        "opened on, holding the whole story between itself and now. No "
        "figures, no world.",
        "the deep indigo pre-creation expanse with first gold rising "
        "along an infinite horizon",
        "any planet, figure, drawn rays, text",
        era="heaven")),
    ("p02", "n2", _p(
        "The last public event begins: an ordinary modern street at "
        "midday — and the whole EASTERN sky is opening: a brilliance "
        "beyond weather building above the rooftops, while below every "
        "pedestrian has stopped mid-stride, every face turned up, keys "
        "and bags frozen in hands. Seen along the street past stopped "
        "shoulders; the light's centre stays above the frame.",
        "a stopped modern street with every face turned up at an "
        "opening eastern brilliance above the rooftops",
        "any figure in the sky yet, panic, readable signs, faces to "
        "lens",
        wide=True)),
    ("p03", "s1", _p(
        "Every knee: down the same street, the crowd is KNEELING — a "
        "wave of it, some slowly, some already down, a workman's hand "
        "over his heart, a woman lowering her stroller-grip to the "
        "pavement, every body angled east toward the light — seen "
        "from behind the kneeling wave. Nobody was forced; every "
        "spine says so.",
        "a street crowd kneeling in an eastward wave, unforced, seen "
        "from behind",
        "soldiers, coercion, faces to camera",
        wide=True)),
    ("p04", ("s1", 0.6), _p(
        "The King, seen: Jesus descending through parting brilliance — "
        "upright in the air, arms opening, the cream robe and the "
        "locked face now in the glory of the Bountiful descent "
        "magnified — clouds of light rolling back from him like doors. "
        "The camera looks up with the world; his feet stand on "
        "nothing; no aura outlines him — the whole sky is the light.",
        "Jesus upright in opening sky-brilliance, arms opening, "
        "clouds rolling back like doors, feet on nothing",
        "wings, halo, aura outline, armies, drawn rays",
        jesus=True, ref=True, wide=True)),
    ("p05", "s2", _p(
        "The binding: a mighty angel — a glorified man, no wings — "
        "hauls a GREAT IRON CHAIN closed around a writhing MASS OF "
        "FORMLESS DARKNESS at the lip of a bottomless shaft — the "
        "darkness pure shapeless black, no face, no limbs, no eyes, "
        "compressing under the links like smoke under a net — the "
        "angel's stance all leverage and finality, the key huge at "
        "his belt. The chain, come back around.",
        "a wingless mighty angel chaining a purely formless black "
        "mass at a shaft's lip, great key at his belt",
        "ANY face, eyes, limbs, horns or figure in the darkness; "
        "wings; flames",
        devil=True)),
    ("p06", "n4", _p(
        "A thousand years of quiet: broad daylight in deep meadow "
        "grass — a small child asleep on its back, arms flung wide "
        "in total safety, while a WOLF lies curled at rest an arm's "
        "length away and a lamb grazes between them — Isaiah's "
        "picture, photographed. Nothing in the frame knows how to "
        "be afraid anymore.",
        "a child asleep in meadow grass with a resting wolf and "
        "grazing lamb an arm's length away",
        "parents hovering, fear, fantasy styling",
        )),
    ("p07", "j1", _p(
        "The why of the wait: extreme close in a ripening wheat "
        "field — wheat stalks and darnel tares growing "
        "INTERTWINED, their roots visibly wound together at the "
        "soil line where the frame dips, one golden head and one "
        "false head side by side in the same light. Pull one now, "
        "tear both.",
        "wheat and tares intertwined at the visible root line, "
        "golden head and false head side by side",
        "harvesters, scythes, storm",
        era="first-century")),
    ("p08", "s3", _p(
        "Longsuffering, at the gate: an old father stands at his "
        "farm gate in the last light, one hand on the post, "
        "looking down the long empty road — the posture held so "
        "many evenings the grass is worn where he stands — dinner "
        "light warm in the house behind him. Not slack. Waiting.",
        "an old father at his gate at dusk watching a long empty "
        "road, grass worn where he stands",
        "his face close, tears, the returner visible",
        era="ancient")),
    ("p09", ("s3", 0.55), _p(
        "Still deciding: a lone figure stands at a quiet modern "
        "crossroads at the exact turn of dawn — night's streetlamps "
        "still burning down one road, the other road running "
        "straight into the sunrise — hands in pockets, weight "
        "shifting, the choice legible in the stance. Seen from "
        "behind. The clock, running slow for exactly this person.",
        "a lone figure from behind at a dawn crossroads between a "
        "lamplit road and a sunrise road",
        "signs readable, traffic, their face",
        )),
    ("p10", "s4", _p(
        "Like him: a father walks ahead across firm wet sand at "
        "morning, and behind him his small child stretches each "
        "stride to land EXACTLY in the father's footprints — arms "
        "out for balance, tongue of concentration, three prints "
        "conquered and the fourth mid-air — both from behind, the "
        "sea bright beyond. The doctrine, at toddler scale.",
        "a child from behind stretching to walk in a father's "
        "footprints across wet sand",
        "faces, crowds, text",
        )),
    ("p11", ("n9", 0.5), _p(
        "Heirs: at a weathered farm gate, an old hand presses a "
        "worn ring of keys into a grown child's open palm — both "
        "hands work-shaped from the same fields, the farm rolling "
        "away gold behind them, the transfer caught at the moment "
        "both hold the keys together. Everything the Father has.",
        "old hands pressing a worn key-ring into grown hands at a "
        "farm gate, both holding at the transfer",
        "faces, documents, jewellery",
        )),
    ("p12", "s6", _p(
        "The wiping: the Father's great hand cups a weeping "
        "woman's face — His thumb mid-stroke across her cheek, "
        "taking the tear — her eyes closing under the touch, her "
        "own hand rising to hold His wrist; His face above hers "
        "soft-focused and bent close. The gesture Enoch saw "
        "reversed at last: the God who wept, drying the tears. "
        "The series' most tender frame.",
        "the Father's thumb mid-wipe across a weeping woman's "
        "cheek, her hand holding His wrist, His bent face soft "
        "above",
        "faces to camera, halo, theatrical light",
        era="heaven", locks=["FATHER"])),
    ("p13", ("s6", 0.6), _p(
        "Former things, passed away: a hospital room emptied of "
        "its purpose — the bed made and vacant, machines dark and "
        "unplugged, and the window thrown fully OPEN with morning "
        "pouring in, the curtain breathing in the warm air. Death, "
        "out of business. No people.",
        "an emptied made hospital bed with dark machines and a "
        "thrown-open window breathing morning",
        "patients, staff, grief objects",
        )),
    ("p14", "n11", _p(
        "The room where it started: the Father and the Son at the "
        "dais edge — the exact composition of episode one's "
        "embrace, the hand on the shoulder — but now both faces "
        "are OPEN WITH JOY: the work behind them, the court "
        "beyond beginning to fill, the Father's smile deep in the "
        "silver beard, the Son's gladness the same as Kirtland. "
        "He told us it would work.",
        "the Father's hand on the Son's shoulder as in episode "
        "one, both faces open with finished joy, court filling "
        "beyond",
        "either face to the lens, halos, identical faces",
        era="heaven", jesus=True, ref=True, locks=["FATHER", "COURT"])),
    ("p15", ("n11", 0.3), _p(
        "The glory is us: the council court FULL again — but not "
        "with ranks now: with REUNIONS. Resurrected families "
        "streaming up the terraces into the arms of waiting "
        "hosts, children lifted and spun, old friends colliding "
        "mid-laugh, white and every-colored best clothes mingled "
        "— the homecoming at kingdom scale, seen wide from above "
        "the joy. No face toward the lens; every face toward "
        "someone.",
        "the court filled with streaming embracing reunions at "
        "kingdom scale, every face toward someone",
        "ranks, formality, faces to camera",
        era="heaven", wide=True, locks=["COURT", "HOSTS"])),
    ("p16", ("n11", 0.58), _p(
        "Your grove: in the present day, an ordinary person kneels "
        "down in an ordinary patch of trees at first light — city "
        "park or back woodlot, dew soaking through at the knees, "
        "head bowing as the morning reaches through the leaves — "
        "seen from behind at a respectful distance. Episode "
        "twenty-six's invitation, being accepted by anyone. By "
        "you.",
        "an ordinary person from behind kneeling in ordinary trees "
        "at first light, head bowing",
        "their face, others, drawn rays, church buildings",
        )),
    ("p17", ("n11", 0.82), _p(
        "The last frame: the drumlin hill at full sunrise — and "
        "for the first time in the whole series, a single person "
        "is walking UP it, small against the gold, unhurried, "
        "going to ask. The story, handed off. Roll to the card.",
        "one small figure walking up the sunlit drumlin hill at "
        "sunrise, unhurried",
        "their face, crowds, monuments, text",
        era="america-1820", wide=True)),
]
