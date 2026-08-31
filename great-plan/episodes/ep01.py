#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 1: The Two Wills.

The council in heaven. The Father presents the plan; two voices answer; the
whole war begins. Anchors: Moses 4:1-4; Abraham 3:24-28; Job 38:7.

Sacred-voice law: everything except NARRATOR is verbatim scripture (Moses 4,
Abraham 3 — Pearl of Great Price). The devil is a VOICE ONLY — he is never
rendered in any picture (Cameron's DEVIL LAW, 2026-08-31).
"""

NARRATOR, JESUS, FATHER, DEVIL = "narrator", "jesus", "father", "devil"

EP = 301          # reviewer card id (300 + episode number)
NUM = 1
SLUG = "two-wills"
TITLE = "The Two Wills"
META = "Moses 4 · Abraham 3"

SEGMENTS = [
    ("n1", NARRATOR,
     "Before this world had a sunrise — before there was an ocean, or a "
     "mountain, or a single beating heart — you were alive."),
    ("n2", NARRATOR,
     "You stood in a council of glory, a spirit child of God, among more "
     "brothers and sisters than any man can number. And your Father stood "
     "before you all."),
    ("n3", NARRATOR,
     "He laid out a plan. His children would receive bodies of flesh and "
     "bone. They would walk a world where they could truly choose. They "
     "would fall. They would feel. And they could become like Him."),
    ("n4", NARRATOR,
     "But real freedom meant real danger. All of us would stumble. Some "
     "would wander far. Someone would have to pay the price to bring us "
     "home."),
    ("g1", FATHER,
     "And the Lord said: Whom shall I send?"),
    ("n5", NARRATOR,
     "Two voices answered. All of eternity hangs on the difference between "
     "them."),
    ("j1", JESUS,
     "Father, thy will be done, and the glory be thine forever."),
    ("n6", NARRATOR,
     "That was the first voice — the Beloved Son. No conditions. No demands. "
     "The rescue would cost Him everything, and He asked to keep nothing."),
    ("d1", DEVIL,
     "Behold, here am I, send me, I will be thy son, and I will redeem all "
     "mankind, that one soul shall not be lost, and surely I will do it; "
     "wherefore give me thine honor."),
    ("n7", NARRATOR,
     "Listen to that second voice carefully. Not one soul lost — it sounds "
     "like mercy. But no soul can be lost only where no soul is free. He was "
     "not offering to save you. He was offering to own you."),
    ("n8", NARRATOR,
     "And there is the price tag, at the end: give me thine honor. He did "
     "not want to rescue the family. He wanted the throne."),
    ("g2", FATHER,
     "Wherefore, because that Satan rebelled against me, and sought to "
     "destroy the agency of man, which I, the Lord God, had given him, and "
     "also, that I should give unto him mine own power; by the power of mine "
     "Only Begotten, I caused that he should be cast down."),
    ("n9", NARRATOR,
     "Hold on to this. Your Father would not trade your freedom for your "
     "safety. Not then. Not now. Not ever. He chose the plan that would cost "
     "His Son everything — because it was the only plan where you could "
     "become anything."),
    ("n10", NARRATOR,
     "Every battle in this story — the garden, the flood, the cross, the "
     "long centuries of silence, the fight going on inside you today — is "
     "these two speeches, still colliding."),
    ("n11", NARRATOR,
     "And you already know which side you took. You are here. You have a "
     "body. Once, before the world, you looked at both of them — and you "
     "chose Him."),
]

CARD_SEG = ("card", NARRATOR,
            "He has been asking ever since. And He will never force you. "
            "That is how you know which voice is His.")

CARD_TEXT = ("He will never force you.\n"
             "That is how you know\n"
             "which voice is His.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode One — The Two Wills")

SPOKEN = {}

COURT = (
    "COUNCIL-COURT LOCK: the setting is always the same premortal council "
    "court — wide terraces of luminous white and gold-veined stone descending "
    "like broad steps toward a distant raised dais that stands in the "
    "brightest natural light, under an open endless sky of deep dawn colours "
    "(indigo overhead melting to warm gold at the horizon). No earth, no "
    "moon, no vegetation — polished stone, light and sky only. The light on "
    "the court is environmental daylight from the sky and the bright distance "
    "around the dais, never rays or beams radiating from any person."
)

HOSTS = (
    "HOSTS LOCK: the assembled spirits are countless real, solid men and "
    "women of every ancestry — Middle Eastern, African, East Asian, South "
    "Asian, European, Pacific — young-adult in bearing, each in a simple "
    "radiant WHITE robe of real woven cloth (bright pure white, never cream "
    "— only the Son wears cream). Every robe is a ONE-PIECE, LONG-SLEEVED, "
    "ankle-length tailored garment, the same cut on everyone — never a "
    "wrapped sheet, toga, shawl, towel, sash-wrap or any draping that "
    "leaves a shoulder or chest bare. They are photographed people with "
    "weight and shadow: never translucent, never glowing, never winged, "
    "never floating."
)

LOCKS = {"COURT": COURT, "HOSTS": HOSTS}

REFS = {}

_common = dict(era="heaven")


def _p(scene, must_show, must_not_show, **kw):
    d = dict(_common)
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "An immense empty expanse before creation: deep indigo darkness "
        "above, and along a vast level horizon far below, the first warm "
        "gold light of an eternal dawn beginning to rise, its warmth washing "
        "up into the dark like slow silent fire. Nothing else exists — no "
        "earth, no stars' familiar constellations, no figures, no ground. "
        "Only depth, darkness, and arriving light.",
        "a vast pre-creation expanse, darkness above and warm dawn light "
        "rising along the far horizon, no people, no earth",
        "any planet, moon, landscape, human figure, text, lens flare "
        "streaks, or light rays in visible beams")),
    ("p02", ("n1", 0.55), _p(
        "The same eternal dawn, nearer and stronger: towering soft curtains "
        "of warm gold and rose light climbing into the indigo deep, like the "
        "first morning of eternity, filling the frame with quiet immensity. "
        "Still no figures, no ground, no world — light and depth only.",
        "towering warm light filling a dark immensity, no figures, no world",
        "any planet, landscape, figure, halo shape, ring of light, or "
        "visible beam edges")),
    ("p03", "n2", _p(
        "The premortal council, seen from far behind the outermost rows: an "
        "ocean of white-robed men and women of every ancestry covering the "
        "descending stone terraces, all facing away from the camera toward "
        "the distant bright dais far below. The camera stands behind and "
        "above the last row and shoots past their backs and shoulders down "
        "the whole court; not one face is turned toward the lens. The "
        "distant dais is a point of warm brightness; the crowd is beyond "
        "counting, filling the frame to its edges.",
        "an uncountable multitude of white-robed people seen from behind, "
        "terraced luminous stone descending to one distant bright dais",
        "any face turned to camera, wings, floating figures, translucent "
        "bodies, cream-coloured robes in the crowd, beams of light",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p04", ("n2", 0.5), _p(
        "Inside the standing multitude, at head height: a young man and a "
        "young woman spirit stand side by side SHOULDER TO SHOULDER, both "
        "seen from behind in three-quarter, and BOTH faces are turned the "
        "SAME direction — away from the camera toward the warm brightness "
        "far ahead of them all. They do NOT face each other; they do not "
        "look at each other; their gazes run parallel toward the distant "
        "light, expectancy visible only at the edge of each profile. "
        "Around them, rows of other white-robed men and women of many "
        "ancestries stand the same way, all attention forward, soft depth "
        "of field beyond.",
        "two near spirits shoulder to shoulder from behind, BOTH gazes "
        "parallel toward the same distant warm light ahead",
        "the two facing each other, any embrace or romantic framing, "
        "anyone looking at the camera, wings, cream robes",
        locks=["COURT", "HOSTS"])),
    ("p05", ("n2", 0.78), _p(
        "The Father on the raised dais, addressing His children: a "
        "glorified, dignified Father with long silver-white hair and beard "
        "in a radiant pure-white robe, arms opened wide in welcome, seen "
        "from a reverent distance in three-quarter view from his left side "
        "so his gaze travels out over the sea of white-robed spirits below "
        "and past the right edge of the frame — never into the lens. The "
        "nearest rows of listening spirits stand soft-focused in the "
        "foreground bottom of the frame, backs to camera.",
        "the Father standing on the dais with open arms, seen three-quarter "
        "from the side, multitude soft in the foreground with backs to "
        "camera",
        "the Father looking into the lens, any halo or radiance from his "
        "body, cream colouring on his robe, wings",
        locks=["FATHER", "COURT", "HOSTS"])),
    ("p06", "n3", _p(
        "Faces of the listening hosts, close: five or six young men and "
        "women of visibly different ancestries in white robes, lit warmly "
        "from the direction of the unseen dais ahead and to the left, every "
        "gaze aimed left past the camera toward the speaker, eyes wide with "
        "wonder, lips parted. Real skin texture, real cloth weave; nobody "
        "looks into the lens.",
        "five or six wondering listening faces of different ancestries, all "
        "gazes aimed left past the camera",
        "anyone looking into the lens, tears, fear, wings, glowing skin",
        locks=["HOSTS"])),
    ("p07", ("n3", 0.55), _p(
        "A close, quiet detail inside the crowd: a young spirit man in his "
        "long-sleeved white robe holds his two open hands FAR APART — the "
        "right hand raised near his shoulder, the left hand low at his "
        "waist, both palms turned up — and his head is bent DOWN toward "
        "the low left hand, studying the back and palm of it with open "
        "wonder, turning it slightly, as if hearing for the first time "
        "that real flesh and bone await it. The wide vertical gap between "
        "the two hands makes prayer impossible to read: this is a man "
        "examining his own hand. Beside him a companion bends to look at "
        "the same low hand. Both faces angle down and away from the lens.",
        "one hand held high and one low with a wide gap, the owner and a "
        "companion both studying the LOW hand, heads bent down",
        "hands near each other, cupped or joined hands, praying posture, "
        "wrapped shawls or bare shoulders, anyone facing the lens",
        locks=["HOSTS"])),
    ("p08", "n4", _p(
        "The mood turns grave inside the multitude: a tight shot of three "
        "listening faces — a young woman centred between two men — their "
        "wonder now weighted with sober understanding, brows drawn, one "
        "man's jaw set, the woman's eyes glistening but not weeping, every "
        "gaze still aimed forward past the left of the camera toward the "
        "unseen speaker. The warm light on them is steady; the gravity is "
        "in the faces alone.",
        "three sober listening faces, gazes forward past the camera, quiet "
        "gravity without fear",
        "weeping, terror, darkness in the frame, anyone facing the lens",
        locks=["HOSTS"])),
    ("p09", "g1", _p(
        "The Father alone in the frame, near profile facing left: the "
        "question hangs in the stillness. His silver-white head is high, "
        "his expression majestic and tender at once, eyes searching out "
        "across his children who blur into soft warm bokeh beyond the "
        "dais edge. His radiant white robe falls still; his hands rest "
        "open at his sides — a Father asking, not a king commanding.",
        "the Father in near profile, tender majesty, multitude blurred "
        "beyond",
        "his eyes on the lens, halo, rays, cream tint on the robe",
        locks=["FATHER", "COURT"])),
    ("p10", "n5", _p(
        "From high behind the assembly, the whole terraced court in one "
        "frame, its stone floor running unbroken to the bright dais in "
        "the upper LEFT of the frame: out of the front rank on that "
        "bright left side, ONE white-clad figure has stepped clearly "
        "forward into the open floor toward the dais, seen tiny and "
        "entirely from behind, mid-stride, alone in the open. Across the "
        "court in the frame's RIGHT third, the same stone floor lies in "
        "a broad COLD DIM patch — a soft-edged failing of the light like "
        "the shadow of a cloud, with the crowd's edge there leaning and "
        "stepping AWAY from it. The dim patch is EMPTY stone: no figure, "
        "no shape, no outline stands in it. The camera shoots down past "
        "the back rows' heads and shoulders; every face is away from "
        "the lens.",
        "ONE lone figure mid-stride in the open floor toward the bright "
        "dais at upper left, and a soft-edged empty dim patch of floor "
        "at the right with the crowd leaning away from it",
        "ANY figure, shape, silhouette, wing or face inside the dim "
        "patch; a sea or water; a second walker; anyone facing the "
        "lens",
        wide=True, devil=True, locks=["COURT", "HOSTS"])),
    ("p11", "j1", _p(
        "The Son steps into the light before the dais: Jesus in his plain "
        "cream wool robe, the only cream in the frame, seen from a "
        "three-quarter angle behind his right shoulder so his face shows "
        "in gentle profile turned up toward the Father's direction off the "
        "left frame edge. His posture is complete surrender and complete "
        "strength — head slightly bowed, hands open at his sides. The "
        "white-robed front ranks stand behind him, soft, their faces "
        "toward him.",
        "Jesus in cream seen three-quarter from behind, face in profile "
        "turned up-left toward the unseen Father, hands open",
        "his eyes on the lens, halo, glow, any other cream cloth, the "
        "Father's face in this frame",
        jesus=True, ref=True, locks=["COURT", "HOSTS"])),
    ("p12", "n6", _p(
        "Close on the Son's face in three-quarter view, gaze steady and "
        "upward past the right frame edge toward the unseen Father: "
        "perfect peace with fire behind the eyes — the look of someone "
        "volunteering for a price he fully understands. Warm environmental "
        "light models his face; the court blurs to gold behind him.",
        "a close three-quarter of Jesus's face, gaze up and right past "
        "the frame edge, peace and resolve together",
        "eyes on the lens, tears, halo, glow, hard rim of light",
        jesus=True, ref=True, locks=["COURT"])),
    ("p13", "d1", _p(
        "The far side of the court while the second voice speaks: a broad "
        "COLD DIMNESS spreads across the luminous stone floor — its "
        "boundary ONE single smooth SHALLOW ARC running straight across "
        "the frame like the edge of an unseen cloud's shadow, a gradual "
        "fade with NO bumps, NO protrusions, NO lobes, NO outline, NO "
        "silhouette, nothing along the whole edge that could read as a "
        "head, profile, wing, claw, bird, creature or man. The white-robed spirits nearest the "
        "fading light step back from it, their faces lit warm from the "
        "bright side, alarm and fascination mixed, every gaze on the "
        "dimming floor — none toward the lens. The dim region itself is "
        "EMPTY cooled stone.",
        "a soft-edged formless cloud-shadow dimming spreading over the "
        "stone, spirits stepping back, faces warm-lit and aimed at the "
        "floor",
        "ANY recognizable outline in or of the shadow — wing, claw, "
        "bird, creature, figure, profile; a hard shadow edge; horns; "
        "anyone facing the lens",
        devil=True, locks=["COURT", "HOSTS"])),
    ("p14", ("d1", 0.62), _p(
        "Low angle at floor level: the cold dimness creeps across "
        "gold-veined white stone toward the camera as a SMOOTH, SOFT "
        "gradient — warm dawn-lit stone on one side melting into cold "
        "grey-blue dimness on the other, the boundary a gentle fade with "
        "no jagged, toothed or serrated edge and no recognizable shape. "
        "Just ahead of the fading light, several pairs of sandaled feet "
        "are caught MID-STEP BACKWARD — heels lifted, weight shifting "
        "away, robe hems swinging with the movement. The dim side is "
        "empty floor running back into darkening air.",
        "a smooth soft-gradient dimming crossing the stone, sandaled "
        "feet caught mid-step backward with heels lifted, empty dimness "
        "beyond",
        "a jagged or toothed shadow edge, any outline or shape in the "
        "dimness, static planted feet, anyone facing the lens",
        devil=True, locks=["COURT", "HOSTS"])),
    ("p15", "n7", _p(
        "The multitude divided by pull, not yet by line: in a tight group "
        "of listening spirits, most faces stay turned toward the warm "
        "bright dais-side of the frame — but two among them have turned "
        "their heads the OTHER way, toward the cold dim side, listening "
        "to it, expressions half-drawn, tempted. The two directions of "
        "gaze split the group visibly. Warm light on one side of each "
        "face, cool dimness on the other.",
        "a group of spirits with gazes split between the warm side and "
        "the cold side of the frame, two visibly drawn toward the dark",
        "anyone facing the lens, any figure in the dim side, sneering "
        "or villainous faces",
        devil=True, locks=["COURT", "HOSTS"])),
    ("p16", "n8", _p(
        "The Father hears the demand: a medium shot of the Father on the "
        "dais, His face in three-quarter turned toward the cold far side "
        "of the court off the right frame edge — majesty unmoved, and an "
        "unmistakable deep sorrow in the set of His eyes and mouth. The "
        "light around the dais holds steady and warm while the far "
        "distance behind Him carries the faint cold tinge at the frame "
        "edge. His hands are still at his sides.",
        "the Father in three-quarter, unmoved majesty with deep sorrow, "
        "warm light near him and a cold tinge at the far frame edge",
        "anger, a raised fist, lightning, his eyes on the lens, halo",
        devil=True, locks=["FATHER", "COURT"])),
    ("p17", "g2", _p(
        "The judgment lands — and the darkness LOSES: the court's stone "
        "floor is already back in FULL warm dawn light from the camera to "
        "the far rim, and the sky above stands clean and bright; the only "
        "darkness left in the frame is a low, formless grey remnant "
        "SLIDING DOWN over the court's far outer rim, three-quarters "
        "gone, draining off the edge like water over a fall — visibly "
        "LEAVING, below the crowd's eye line, never overhead. The "
        "assembled spirits stand in the restored light looking down "
        "toward that far rim where it disappears; the camera stands "
        "behind their near rank and shoots past their backs, not one "
        "face toward the lens.",
        "a fully re-lit warm court and clean sky, with the last formless "
        "grey remnant sliding DOWN over the far rim, spirits watching it "
        "go from behind",
        "darkness overhead or looming above the court, a storm cloud "
        "over the people, any figure or wing shape in the remnant, "
        "anyone facing the lens",
        wide=True, devil=True, locks=["COURT", "HOSTS"])),
    ("p18", ("g2", 0.62), _p(
        "Aftermath, wide and quiet from the side of the court: where a "
        "third of the multitude once stood, a broad region of the terraced "
        "stone now lies EMPTY, and the remaining white-robed hosts have "
        "drawn instinctively closer together at its border, some heads "
        "bowed, some arms around a neighbour's shoulders — the camera "
        "stands to the side and shoots past them so all are seen from the "
        "side or behind in full-length, no face toward the lens. The dawn light lies full and "
        "warm again across the whole court, gentle on the empty space.",
        "a broad empty region of stone beside the gathered remaining "
        "hosts, comfort between neighbours, full warm light restored",
        "any dark stain remaining, any figure in the empty region, "
        "anyone facing the lens",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p19", "n9", _p(
        "The Father and the Son together at the dais edge: the Father "
        "standing behind and beside his Son, one hand resting on the "
        "Son's shoulder, both seen from a three-quarter side angle so "
        "both faces show in profile-to-three-quarter looking out over "
        "the court toward the left frame edge — the Son in his cream "
        "robe, the Father in radiant white, two distinct persons, one "
        "will between them. The hosts blur warm and golden below.",
        "the Father's hand on the Son's shoulder, both in "
        "three-quarter-profile gazing left over the court, cream robe "
        "beside white robe",
        "either face turned to the lens, identical faces, halos, glow, "
        "a merged single figure",
        jesus=True, ref=True, locks=["FATHER", "COURT", "HOSTS"])),
    ("p20", "n10", _p(
        "From the court's outer balustrade: a rank of white-robed spirits "
        "stands at the carved stone rail with their backs and shoulders "
        "to the camera, gazing out into the vast unformed deep beyond the "
        "court — and that deep is ABSOLUTELY EMPTY: only indigo immensity "
        "and rising dawn-fire filling all the space beyond the rail, from "
        "the opening frames, waiting like an unbuilt future. Nothing "
        "stands in the deep: no building, no palace, no temple, no city, "
        "no island, no floating structure of any kind — pure depth, "
        "light and open sky. The camera shoots past their backs into "
        "the emptiness; not one face turns toward the lens.",
        "spirits at a stone balustrade from behind, gazing into a vast "
        "COMPLETELY EMPTY dawn-lit deep — light and sky only",
        "ANY structure, building, palace, island, cloud-city or object "
        "in the deep; any planet or earth; anyone turning to the "
        "camera; wings; beams",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p21", "n11", _p(
        "One young spirit — seen from directly behind, head and shoulders "
        "filling the lower frame — takes a decided step toward the warm "
        "bright dais-side of the court, away from the camera. Ahead and "
        "above, the light he walks toward is gold and immense; his white "
        "robe catches it along the shoulders. His face is never seen. "
        "It could be anyone. It is the viewer.",
        "one spirit from directly behind stepping away from camera "
        "toward immense warm light, face never visible",
        "his face or profile visible, anyone else near the lens, glow "
        "outlining his body",
        locks=["COURT", "HOSTS"])),
    ("p22", ("n11", 0.6), _p(
        "The joy of the hosts, wide: across the terraces the white-robed "
        "multitude lifts arms and faces toward the bright sky in a "
        "single shout of joy — the morning stars singing together — seen "
        "from behind and beside the near ranks so the celebration sweeps "
        "away from the camera down the court toward the radiant dais. "
        "Warm dawn-gold light floods every terrace; not one face is "
        "turned back toward the lens.",
        "a multitude with lifted arms in joy sweeping away from the "
        "camera toward the bright dais, full warm light",
        "anyone facing the lens, wings, halos, beams of light, cream "
        "robes in the crowd",
        wide=True, locks=["COURT", "HOSTS"])),
]
