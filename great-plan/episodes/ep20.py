#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 20: All Power.

The empty tomb, death made temporary for everyone, and the appointment at
Bountiful — twenty-five hundred people, one by one — before keys are handed
to apostles in both hemispheres.
Anchors: Luke 24:5-6; 1 Corinthians 15:22; 3 Nephi 11; Matthew 28:18-19.

Note: the Father's Bountiful introduction (3 Nephi 11:7) is the same
introduction he gives in the Grove in 1820 — the film lets the rhyme land.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 320
NUM = 20
SLUG = "all-power"
TITLE = "All Power"
META = "Luke 24 · 3 Nephi 11 · Matthew 28"

SEGMENTS = [
    ("n1", NARRATOR,
     "Forty hours of the devil's best silence. And then, the third day — "
     "and a dawn that redefined every ending in history."),
    ("n2", NARRATOR,
     "Before sunrise, the women came with spices to finish a burial. "
     "They found the stone rolled away, the linen folded — and two men "
     "in shining garments, holding the greatest question ever asked:"),
    ("s1", SCRIPTURE,
     "Why seek ye the living among the dead? He is not here, but is "
     "risen."),
    ("n3", NARRATOR,
     "Risen. Not resuscitated. Not remembered. Risen — body and spirit "
     "reunited forever, death running backward. Thomas touched the "
     "marks. For forty days, hundreds watched him eat, and walk, and "
     "teach."),
    ("n4", NARRATOR,
     "Understand what broke that morning. Death — the devil's oldest, "
     "surest, hundred-percent weapon — became a temporary condition for "
     "every human being who ever lived. No faith required. No fee. A "
     "free gift to all, because one man walked out of a grave."),
    ("s2", SCRIPTURE,
     "For as in Adam all die, even so in Christ shall all be made "
     "alive."),
    ("n6", NARRATOR,
     "Then he kept an appointment six hundred years in the making. In "
     "the land of the other sheep, twenty-five hundred people stood "
     "gathered at a temple in the land Bountiful — and heard a voice "
     "out of heaven:"),
    ("g1", FATHER,
     "Behold my Beloved Son, in whom I am well pleased, in whom I have "
     "glorified my name — hear ye him."),
    ("n7", NARRATOR,
     "Remember that introduction. The Father will give it once more, in "
     "a grove of trees, eighteen centuries later. And then — he came "
     "down."),
    ("j1", JESUS,
     "Behold, I am Jesus Christ, whom the prophets testified shall come "
     "into the world."),
    ("n8", NARRATOR,
     "And he did not just preach to them. He invited every single "
     "person there to come, one at a time, and feel the prints in his "
     "hands and his side. It took hours. He stayed."),
    ("s3", SCRIPTURE,
     "And the multitude went forth, and thrust their hands into his "
     "side, and did feel the prints of the nails in his hands and in "
     "his feet; and this they did do, going forth one by one until "
     "they had all gone forth."),
    ("n10", NARRATOR,
     "And in both hemispheres, before he left, he did the same thing: "
     "he organized his church, and he handed men the keys — apostles, "
     "prophets, the authority to baptize and to bind. The kingdom now "
     "had stewards. Hear the commission:"),
    ("j2", JESUS,
     "All power is given unto me in heaven and in earth. Go ye "
     "therefore, and teach all nations, baptizing them in the name of "
     "the Father, and of the Son, and of the Holy Ghost."),
    ("n11", NARRATOR,
     "So read the scoreboard. The tomb is empty. Death is temporary. "
     "Both hemispheres hold apostles with keys. The devil's checkmate "
     "piece is off the board forever — so watch him closely now. He is "
     "about to change strategies. Next: the long theft."),
]

CARD_SEG = ("card", NARRATOR,
            "The grave has been temporary for two thousand years. He "
            "made it free.")

CARD_TEXT = ("Death is temporary.\n"
             "He made it free.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Twenty — All Power")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="first-century")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The last dark: the sealed garden tomb in deepest pre-dawn "
        "grey — the stone flush in its channel, dew heavy on the "
        "olive leaves, the east behind the garden wall holding the "
        "very first paleness. Stillness stretched to breaking. No "
        "figures.",
        "the sealed tomb in pre-dawn grey with first paleness "
        "building behind the garden wall",
        "guards, light from the tomb, figures, drawn rays",
        )),
    ("p02", "n2", _p(
        "The mourners' errand: three women walk the garden path in "
        "half-light, seen from behind — spice jars and folded cloths "
        "held close, shawls drawn, their pace the heavy pace of a "
        "task nobody wants to finish. The path bends toward the "
        "tomb's rise ahead.",
        "three shawled women from behind carrying spice jars up a "
        "half-lit garden path",
        "faces, guards, the tomb visible yet",
        )),
    ("p03", ("n2", 0.5), _p(
        "Rolled away: the tomb's mouth stands OPEN — the great disc "
        "stone hurled back off its channel and resting aslant against "
        "the rock face, the doorway a rectangle of deep interior "
        "shadow with the folded linen catching first light on the "
        "shelf within — and dawn's gold just breaking over the wall "
        "behind the camera, laying warmth on the stone.",
        "the tomb's open mouth with its stone flung aslant and "
        "folded linen catching light on the inner shelf",
        "figures yet, angels, drawn rays, guards",
        )),
    ("p04", "s1", _p(
        "The question: the women recoiled at the tomb's mouth, jars "
        "set hastily down — and before them TWO men in garments so "
        "white they hold their own light, both feet on the ground, "
        "faces calm and joyful, one with a hand lifted gently in the "
        "asking gesture — the women's faces caught between terror "
        "and impossible hope.",
        "two white-clad wingless messengers with feet on the ground "
        "and the women caught between terror and hope",
        "wings, halos, hovering, drawn rays, faces to camera",
        )),
    ("p05", "n3", _p(
        "Her own name: Mary Magdalene mid-turn in the morning "
        "garden — her tear-streaked face BREAKING into recognition, "
        "one hand flying toward her mouth — and beyond her, "
        "soft-focused in the risen light, Jesus standing whole among "
        "the trees. The first name spoken from the far side of "
        "death was hers.",
        "Mary mid-turn breaking into recognition, hand flying to "
        "her mouth, the risen Jesus soft beyond",
        "embrace yet, halo, gardeners' tools, faces to camera",
        jesus=True, ref=True)),
    ("p06", ("n3", 0.6), _p(
        "Thomas's finger: close on Jesus's offered wrist and hand — "
        "the small healed print plain in the palm — with Thomas's "
        "trembling finger a breath away from touching it, and "
        "Thomas's face beyond crumbling from doubt into worship. "
        "Gentle light; the proof, offered without reproach.",
        "Thomas's trembling finger a breath from the healed print "
        "in the offered palm, doubt crumbling to worship",
        "gore, open wounds, his eyes on the lens, halo",
        jesus=True, ref=True)),
    ("p07", "n4", _p(
        "The disarmed weapon: inside the tomb looking outward — the "
        "burial linen lying FOLDED and neat on the stone shelf in "
        "the foreground, and past it, through the open doorway, the "
        "garden blazing with risen morning. The grave, converted "
        "into a doorway. No figures.",
        "folded linen on the tomb shelf with the open doorway "
        "framing blazing garden morning beyond",
        "bodies, angels, guards, darkness dominant",
        )),
    ("p08", "s2", _p(
        "All made alive: on a wide dawn hillside, people of every "
        "age stand facing the rising light — an old man, a young "
        "mother with her infant, children, a bent grandmother "
        "straightening — dozens of them, all seen from behind or "
        "profile, the gold flooding their faces from ahead. The "
        "word ALL, cast in people.",
        "an all-ages crowd from behind and profile facing flooding "
        "dawn gold on a wide hillside",
        "graves, faces to camera, wings, drawn rays",
        wide=True)),
    ("p09", "n6", _p(
        "Bountiful: the stepped new-world stone temple in bright "
        "morning, its wide courtyard filling with a gathering "
        "multitude — families streaming in, white and earth-tone "
        "garments, a murmur of expectation readable in the leaning "
        "clusters — seen from the courtyard's edge past shoulders "
        "and heads. Twenty-five hundred people, about to be sure.",
        "a stepped stone temple courtyard filling with an expectant "
        "gathering multitude, seen past near shoulders",
        "Old-world architecture, idols, faces to camera",
        era="ancient", wide=True)),
    ("p10", "g1", _p(
        "The voice out of heaven: the whole multitude's faces "
        "turned UPWARD at once — hundreds of upturned faces washed "
        "in a brilliance building above the frame's top edge, "
        "hands rising unbidden, a child gripping a father's neck — "
        "the light's source never in frame, the sound of it "
        "visible only in the faces.",
        "hundreds of upturned faces washed in brilliance from "
        "above the frame, hands rising",
        "any figure in the light, drawn rays, faces to camera",
        era="ancient", wide=True)),
    ("p11", "n7", _p(
        "The descent: Jesus descending through the bright air "
        "above the courtyard — upright, calm, his cream robe "
        "stirring, both feet plainly OFF the ground with open air "
        "beneath them, arms slightly out in greeting — the "
        "multitude below frozen mid-gasp, every face up. The "
        "film's second Person in the air; the Grove will rhyme "
        "with this.",
        "Jesus upright in the air with open space beneath his "
        "feet, arms slightly out, the frozen multitude below",
        "wings, halo, aura outline, drawn rays, feet touching "
        "ground",
        era="ancient", jesus=True, ref=True, wide=True)),
    ("p12", "j1", _p(
        "I am Jesus Christ: landed now at the courtyard's heart, "
        "he addresses them — one arm raised mid-declaration, the "
        "cream robe still, the nearest ranks kneeling in a wave "
        "around him — seen from well back in the multitude, past "
        "a hundred heads and shoulders, his figure small and "
        "absolutely central.",
        "Jesus mid-declaration at the courtyard's heart seen past "
        "a hundred heads, near ranks kneeling in a wave",
        "faces to camera, halo, banners",
        era="ancient", jesus=True, ref=True, wide=True)),
    ("p13", "n8", _p(
        "The invitation: Jesus extends both hands forward, palms "
        "up, toward the first hesitant approachers — an old man "
        "and a young woman a step away, their hands half-lifted, "
        "their faces asking permission — his face open, patient, "
        "utterly unhurried. Come, and know.",
        "Jesus's both palms offered forward to hesitant "
        "approachers with half-lifted hands",
        "crowd crush, halo, tears yet, faces to camera",
        era="ancient", jesus=True, ref=True)),
    ("p14", "s3", _p(
        "One by one: an old woman's worn fingers rest ON the "
        "healed print in Jesus's offered hand — her other hand "
        "pressed to her own heart, her lined face wet and "
        "certain — while behind her the line curves away across "
        "the courtyard, person after person after person, "
        "waiting their turn to KNOW. His face above hers holds "
        "complete attention, as if she were the only one.",
        "an old woman's fingers on the healed print, her wet "
        "certain face, the line curving far behind her",
        "gore, hurry, guards, faces to camera",
        era="ancient", jesus=True, ref=True)),
    ("p15", ("s3", 0.6), _p(
        "The smallest witnesses: a father lifts his small "
        "daughter so her tiny hand can reach the healed print — "
        "her face solemn with borrowed courage, Jesus bending "
        "slightly to bring his hand to her reach, the father's "
        "eyes shining above her shoulder. Knowledge, sized for "
        "children.",
        "a lifted small girl's hand reaching the print, Jesus "
        "bending to her reach, the father's shining eyes",
        "crying children, crush, halo, faces to camera",
        era="ancient", jesus=True, ref=True)),
    ("p16", ("n8", 0.6), _p(
        "He stayed: the courtyard in late gold light now — "
        "shadows long across the stones, and the line STILL "
        "moving, still curving to him at its centre, unhurried "
        "as morning — the passage of hours told entirely by the "
        "light. Seen wide from the temple steps.",
        "the courtyard gone late-gold with long shadows and the "
        "line still moving to him at centre",
        "torches, impatience, dispersal, faces to camera",
        era="ancient", jesus=True, ref=True, wide=True)),
    ("p17", "n10", _p(
        "The keys, old world: on a Galilean mountainside the "
        "eleven kneel in a rough arc before the risen Jesus — "
        "seen from behind and above the kneeling arc so their "
        "bowed heads and his standing figure compose the "
        "commission — his hands lifted over them in bestowal, "
        "the sea of Galilee grey-bright far below.",
        "the eleven kneeling in an arc from behind with Jesus's "
        "hands lifted over them, Galilee far below",
        "faces to camera, halo, crowds, doves",
        jesus=True, ref=True, wide=True)),
    ("p18", "j2", _p(
        "Go ye therefore: Jesus's face in strong three-quarter, "
        "the commission leaving him — warmth and command fused, "
        "his arm sweeping out toward the horizon of nations "
        "beyond the frame — the face of a King deploying his "
        "kingdom. Wind off the mountain in his hair.",
        "Jesus's strong three-quarter face mid-commission, arm "
        "sweeping to the unseen horizon",
        "his eyes on the lens, halo, maps, banners",
        jesus=True, ref=True)),
    ("p19", "n11", _p(
        "The scoreboard: the empty tomb's open doorway in full "
        "confident morning — the aslant stone gone green at its "
        "base with new growth, songbirds crossing the garden, "
        "the folded linen just visible pale on the inner shelf. "
        "An empty grave, two thousand years young. No figures.",
        "the open tomb doorway in full morning, stone greening "
        "at its base, songbirds crossing",
        "guards, mourners, drawn rays, text",
        )),
    ("p20", ("n11", 0.7), _p(
        "One light for both hemispheres: the sun rising out of "
        "a vast sea horizon — the gold road of it running "
        "straight across the water toward the camera, sky "
        "clean, the same risen light heading for every shore "
        "there is. No figures, no ships.",
        "sunrise over open sea with its gold road running "
        "toward the camera",
        "ships, birds in flocks, drawn rays, text",
        wide=True)),
]
