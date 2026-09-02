#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 18: The Same Old Trade.

The wilderness temptation heard as the council offer re-run — every kingdom
without a cross — answered three times with the written word; then a
ministry of power spent downward, and the rich young ruler allowed to walk
away. Anchors: Matthew 4:1-11; Mark 10:21-22; John 6:38.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 318
NUM = 18
SLUG = "same-old-trade"
TITLE = "The Same Old Trade"
META = "Matthew 4 · Mark 10"

SEGMENTS = [
    ("n1", NARRATOR,
     "Before His ministry began, Jesus walked into the wilderness to "
     "fast for forty days. And someone was waiting for Him out there. "
     "Round two, of a very old fight."),
    ("d1", DEVIL,
     "If thou be the Son of God, command that these stones be made "
     "bread."),
    ("n3", NARRATOR,
     "IF thou be the Son of God. There is the tell — shrink the title "
     "first, then sell the shortcut. Bread, for a body forty days "
     "empty. Reasonable. Small. And a hook."),
    ("j1", JESUS,
     "It is written, Man shall not live by bread alone, but by every "
     "word that proceedeth out of the mouth of God."),
    ("n4", NARRATOR,
     "Strike one — answered with scripture, not a debate. Then the "
     "temple's pinnacle: throw yourself down, let angels catch you. "
     "Prove it with a spectacle."),
    ("j2", JESUS,
     "It is written again, Thou shalt not tempt the Lord thy God."),
    ("n5", NARRATOR,
     "Strike two. So the recruiter stopped pretending. He took Him to "
     "an exceeding high mountain, showed Him all the kingdoms of the "
     "world and the glory of them — and made the offer he had been "
     "building toward all along:"),
    ("d2", DEVIL,
     "All these things will I give thee, if thou wilt fall down and "
     "worship me."),
    ("n6", NARRATOR,
     "Do you hear it now? That is the council offer. The throne "
     "without the cross. Every kingdom, no Gethsemane — just transfer "
     "the worship. He offered Jesus the exact trade he offered heaven: "
     "all the glory, in exchange for the plan."),
    ("j3", JESUS,
     "Get thee hence, Satan: for it is written, Thou shalt worship the "
     "Lord thy God, and him only shalt thou serve."),
    ("n7", NARRATOR,
     "Strike three — and the recruiter left. Notice that Jesus answered "
     "all three the same way: the written word, and a settled will. The "
     "same two weapons you have. That is the point of the story."),
    ("n8", NARRATOR,
     "Then He went and spent three years doing the opposite of the "
     "shortcut. Touching lepers nobody would touch. Feeding crowds. "
     "Forgiving the unforgivable. Power, spent downward — always "
     "downward."),
    ("n9", NARRATOR,
     "And when a rich young ruler turned and walked away from Him — "
     "scripture says Jesus looked on him, and loved him — He let him "
     "go. He would not chase a soul with force. He never has."),
    ("s1", SCRIPTURE,
     "Then Jesus beholding him loved him. And he was sad at that "
     "saying, and went away grieved: for he had great possessions."),
    ("n10", NARRATOR,
     "Watch the pattern. The devil's power grabs. God's power gives. "
     "One voice still sells the shortcut. The other still says follow "
     "me — and lets you walk away if you must."),
    ("n11", NARRATOR,
     "Why does He do it that way? He told us — and you have heard this "
     "sentence before, in a council before the world:"),
    ("j4", JESUS,
     "For I came down from heaven, not to do mine own will, but the "
     "will of him that sent me."),
    ("n12", NARRATOR,
     "Same sentence as the council. Some things never change. And that "
     "is the best news in the universe."),
]

CARD_SEG = ("card", NARRATOR,
            "He was offered every kingdom without a cross. He chose you "
            "instead.")

CARD_TEXT = ("He chose you instead.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Eighteen — The Same Old Trade")

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
        "The Judean wilderness at dawn: fold after fold of bone-dry "
        "badlands running to a pale horizon, wadis in deep blue "
        "shadow, one thread of goat-track winding into the emptiness. "
        "Vast, hostile, silent. No figures yet.",
        "vast dawn badlands with one empty goat-track winding in",
        "vegetation lush, buildings, figures, drawn rays",
        wide=True)),
    ("p02", ("n1", 0.55), _p(
        "Forty days in: Jesus sits on a flat rock in the wilderness "
        "shade, gaunt and wind-burned, forearms on his knees, cream "
        "robe dusty at the hem — his face in three-quarter carrying "
        "hunger's hollows and a completely unshaken steadiness. The "
        "heat shimmers on the rocks behind him.",
        "a gaunt steady Jesus seated on rock in three-quarter, dusty "
        "hem, heat shimmer",
        "his eyes on the lens, halo, food, water",
        jesus=True, ref=True)),
    ("p03", "d1", _p(
        "The first offer: a scatter of smooth round desert stones in "
        "sharp foreground focus — each one exactly the size and "
        "colour of a baked loaf — and beyond them, soft, Jesus's "
        "seated figure with his gaze resting down on the stones, "
        "unmoved; at the frame's far edge the light has gone faintly "
        "COLD, a formless dimming with nothing in it.",
        "loaf-like stones sharp in front, Jesus's soft unmoved gaze "
        "beyond, a faint formless cold at one edge",
        "any figure in the cold dim, bread actual, his eyes on the "
        "lens",
        jesus=True, ref=True, devil=True)),
    ("p04", "j1", _p(
        "The first answer: Jesus's face close in three-quarter, "
        "mid-word — hunger plain in the cheeks and utterly outranked "
        "by the calm in the eyes, which hold steady on the middle "
        "distance past the camera's left. Scripture, spoken like a "
        "planted flag.",
        "Jesus's gaunt close three-quarter face mid-word, calm "
        "outranking hunger",
        "his eyes on the lens, anger, halo, spittle",
        jesus=True, ref=True)),
    ("p05", "n4", _p(
        "The pinnacle: exactly ONE figure in the frame — Jesus "
        "alone, FULL FIGURE seen from BEHIND and slightly above, "
        "standing still at the very lip of the temple's highest "
        "parapet corner, cream robe stirred by the height's wind — "
        "and far below him, the courts and colonnades and tiny "
        "crowds of the temple mount dropping away in dizzying "
        "verticality. The drop is the subject; his stillness at "
        "its lip is the answer coming.",
        "ONE full-figure Jesus from behind at the parapet lip over "
        "dizzying temple courts far below",
        "a second figure of Jesus anywhere, first-person feet, any "
        "other person on the parapet, his face, angels, falling",
        jesus=True, ref=True, wide=True)),
    ("p06", "j2", _p(
        "The second answer: Jesus in calm three-quarter at the "
        "pinnacle's edge, the wind off the drop moving his hair — "
        "no fear, no theatre, the quiet refusal of a Son with "
        "nothing to prove. The city's haze soft and far below "
        "behind him.",
        "calm three-quarter Jesus at the windy edge, city haze far "
        "below, nothing to prove",
        "his eyes on the lens, halo, vertigo drama on his face",
        jesus=True, ref=True)),
    ("p07", "n5", _p(
        "The exceeding high mountain: Jesus stands at a summit's "
        "edge seen from behind, and below him the whole night-dawn "
        "world is laid out — kingdom after kingdom of lamplit "
        "cities threading the dark plains to the curve of the "
        "horizon, gold and distant and endless. At the frame's "
        "near corner the air holds a formless cold. The offer, "
        "spread out.",
        "Jesus from behind on a summit over endless lamplit "
        "kingdoms threading dark plains, formless cold at a "
        "corner",
        "any figure in the cold, modern cities, his face",
        jesus=True, ref=True, wide=True, devil=True)),
    ("p08", "d2", _p(
        "The glory of them: the kingdoms alone, closer — marble "
        "capitals and torch-lit palaces, harbours of ships, "
        "granaries and gold-lit windows, an empire's wealth "
        "glittering under the last night-blue — beautiful the way "
        "a hook is beautiful. No figures near; the world as "
        "merchandise.",
        "torch-lit palaces, harbours and gold windows glittering "
        "under night-blue — the world as merchandise",
        "recognizable landmarks, modern light, figures close",
        wide=True, devil=True)),
    ("p09", "j3", _p(
        "GET THEE HENCE: Jesus turned from the vista, caught "
        "mid-command — his arm swept out and down in absolute "
        "dismissal toward the frame's cold edge, his face set "
        "like flint, the summit wind hard in his robe. The "
        "third answer, with an edge on it.",
        "Jesus mid-command, arm swept in dismissal toward the "
        "cold edge, face set like flint",
        "his eyes on the lens, lightning, any figure receiving "
        "the command",
        jesus=True, ref=True, devil=True)),
    ("p10", ("j3", 0.6), _p(
        "The recruiter leaves: the cold formless dimness TEARS "
        "away down the mountainside — draining over the summit's "
        "far lip like a ripped tide, three-quarters gone — while "
        "clean dawn floods back across the rocks and the lamplit "
        "kingdoms below fade into honest morning haze. Jesus "
        "stands small at the frame's top, unmoved.",
        "formless dimness draining over the summit lip while "
        "dawn floods back, Jesus small and unmoved above",
        "any shape in the leaving dark, wings, fire",
        wide=True, devil=True, jesus=True, ref=True)),
    ("p11", "n7", _p(
        "Ministered to: on the quiet summit after, a folded cloth "
        "spread on the rock bears a round loaf, dates and a clay "
        "water jar — placed, not foraged — morning warmth across "
        "the small mercy, the wilderness gone gentle behind. No "
        "figures; provision as presence.",
        "bread, dates and a water jar on a spread cloth on summit "
        "rock in morning warmth",
        "angels visible, hands, halo light",
        )),
    ("p12", "n8", _p(
        "Power spent downward: Jesus's hand laid FULL AND FIRM on "
        "the ruined shoulder of a kneeling leper — the man's "
        "bandaged face lifted in shattering disbelief at being "
        "TOUCHED, tears cutting through the grime, Jesus bent "
        "close over him, cream sleeve against grey rags. The "
        "touch is the sermon.",
        "Jesus's firm hand on a kneeling leper's shoulder, the "
        "man's bandaged tear-cut face in disbelief at the touch",
        "sores graphic, halo, crowd recoil sharp, faces to "
        "camera",
        jesus=True, ref=True)),
    ("p13", ("n8", 0.4), _p(
        "The multiplying: close on Jesus's hands breaking a "
        "barley loaf over a woven basket already impossibly "
        "full — more broken bread beneath than the loaf could "
        "hold, another waiting basket at the frame's edge, "
        "grass and seated crowds soft beyond. Abundance leaving "
        "his hands.",
        "hands breaking bread over a basket impossibly full, "
        "second basket waiting, seated crowds soft beyond",
        "faces, fish rotting, coins, halo",
        jesus=True, ref=True)),
    ("p14", ("n8", 0.75), _p(
        "The forgiving: Jesus's hand clasps a woman's forearm, "
        "lifting her from the pavement where she knelt — her "
        "tear-streaked face rising toward his, disbelief becoming "
        "dawn — and on the stones around them, DROPPED STONES, "
        "five or six of them, lying where accusers' hands let "
        "them go. The accusers themselves are gone from the "
        "frame.",
        "Jesus lifting a kneeling woman by the forearm, dropped "
        "stones lying abandoned on the pavement around them",
        "accusers in frame, her shame graphic, faces to camera",
        jesus=True, ref=True)),
    ("p15", "n9", _p(
        "Beholding him, loved him: Jesus and the rich young "
        "ruler face each other in a street of better houses — "
        "the young man's fine embroidered robes and ringed "
        "hands, his face caught between longing and arithmetic; "
        "Jesus's face toward him carrying open, unguarded LOVE "
        "with no leverage in it. Both in profile; the space "
        "between them charged.",
        "Jesus's unguarded love in profile toward a fine-robed "
        "young man whose face weighs longing against wealth",
        "anger, contempt, coins shown, faces to camera",
        jesus=True, ref=True)),
    ("p16", "s1", _p(
        "He let him go — OVER-THE-SHOULDER SHOT: the camera sits "
        "close behind Jesus's right shoulder, so his cream-robed "
        "shoulder and the back of his dark hair fill the frame's "
        "near left third, softly OUT OF FOCUS — and the empty "
        "evening street runs straight away from the lens, where "
        "the young ruler is ALREADY FAR DOWN it: a SMALL receding "
        "figure, back fully to the camera, mid-stride onward, "
        "fine cloak swaying, one more step from being gone. He is "
        "DISTANT — no larger than a fifth of the frame's height — "
        "so his face could not be seen even if he turned, and he "
        "does not turn. The widening gap is the subject.",
        "over Jesus's out-of-focus near shoulder: the ruler's "
        "small distant back receding down the empty street",
        "the ruler near or large in frame, the ruler's face or "
        "profile or chest visible, anyone walking toward the "
        "camera, Jesus's face, reaching, crowds",
        jesus=True, ref=True, wide=True)),
    ("p17", "n10", _p(
        "The King kneels: Jesus on his knees with a disciple's "
        "bare foot cradled over the basin, water bright on his "
        "wrists, towel at his waist — the disciple's hands "
        "half-raised in protest above — the whole hierarchy of "
        "heaven inverted in one lamplit act.",
        "Jesus kneeling with a disciple's foot over the basin, "
        "towel at his waist, protesting hands above",
        "faces to camera, halo, the table prominent",
        jesus=True, ref=True)),
    ("p18", "j4", _p(
        "The sentence from before the world: Jesus at night "
        "prayer on a hillside, kneeling upright, face lifted "
        "and eyes closed, the settled stillness of a will long "
        "since given — olive branches black against the "
        "star-field behind him. The council's answer, still "
        "being kept.",
        "Jesus kneeling upright in night prayer, face lifted, "
        "eyes closed, olive branches against stars",
        "sweat or blood, angels, halo, his eyes open on lens",
        jesus=True, ref=True)),
    ("p19", ("n12", 0.4), _p(
        "The wilderness, disarmed: the same badlands from the "
        "opening frame now in full soft morning — the folds "
        "gold instead of bone, the wadis holding gentle shadow, "
        "the goat-track bright — the battlefield after the "
        "battle, at peace. No figures.",
        "the same badlands gone gold and gentle in full "
        "morning, the track bright",
        "figures, storm, drawn rays, text",
        wide=True)),
]
