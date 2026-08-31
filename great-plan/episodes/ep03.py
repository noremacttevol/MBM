#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 3: War in Heaven.

The first war: fought over freedom, won by testimony, lost by a third who
chose a guarantee over agency. Anchors: Revelation 12:7-11; D&C 29:36-37.

Casting note (doctrinally exact): Michael the archangel IS premortal Adam
(D&C 27:11; 107:54), so Michael wears the ADAM reference sheet. The war is
testimony against deception — NO swords, NO wings, and the devil's side is
darkness only (Devil Law).
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, DEVIL = ("narrator", "jesus", "father",
                                             "scripture", "devil")

EP = 303
NUM = 3
SLUG = "war-in-heaven"
TITLE = "War in Heaven"
META = "Revelation 12 · D&C 29"

SEGMENTS = [
    ("n1", NARRATOR,
     "The first war in history was not fought over land, or gold, or "
     "borders. It was fought in heaven — over whether God's children would "
     "be free."),
    ("s1", SCRIPTURE,
     "And there was war in heaven: Michael and his angels fought against "
     "the dragon; and the dragon fought and his angels, and prevailed not; "
     "neither was their place found any more in heaven."),
    ("n2", NARRATOR,
     "No swords. No blood. What do spirits fight with? Listen to how the "
     "winners won:"),
    ("s2", SCRIPTURE,
     "And they overcame him by the blood of the Lamb, and by the word of "
     "their testimony; and they loved not their lives unto the death."),
    ("n3", NARRATOR,
     "The blood of the Lamb — trust in the Redeemer who had already been "
     "chosen. And the word of their testimony — they stood up and said "
     "what they knew. That is the whole arsenal of heaven. It still is."),
    ("n4", NARRATOR,
     "And understand what made this war so strange. Every soldier on both "
     "sides could see God. Nobody doubted He existed. This was never a war "
     "about whether God is real. It was a war about whether He should be "
     "trusted."),
    ("n5", NARRATOR,
     "The dragon's recruiting pitch was safety. Follow me and you cannot "
     "fail. Cannot fall. Cannot be lost. Hand over your freedom, and I "
     "will guarantee your outcome."),
    ("n6", NARRATOR,
     "And a third of our family — brothers and sisters we knew — took the "
     "deal. Standing in the light of heaven itself, they chose the "
     "guarantee over the freedom."),
    ("g1", FATHER,
     "A third part of the hosts of heaven turned he away from me because "
     "of their agency; and they were thrust down, and thus came the devil "
     "and his angels."),
    ("n7", NARRATOR,
     "Because of their agency. Even the ones who marched against freedom "
     "were free to do it. God would not force them to stay. The whole war "
     "was about never forcing anyone — and He did not make an exception "
     "even to win it."),
    ("n8", NARRATOR,
     "Think about what that cost Him. He is a Father. He watched a third "
     "of His children walk out — and the door He refused to lock behind "
     "them was the same open door that made the rest of the plan "
     "possible."),
    ("n9", NARRATOR,
     "Michael and the faithful drove the rebellion out — with testimony, "
     "not terror. And the accuser was cast down to the earth. The same "
     "earth we were all about to be born on."),
    ("n10", NARRATOR,
     "That was not an accident. The war did not end that day. It moved. "
     "Same two speeches. Same recruiter. Same weapon that beats him — "
     "carried down to a world where the soldiers cannot see the General, "
     "and have to fight from memory."),
    ("n11", NARRATOR,
     "You were in that first fight. And you know which side you held, "
     "because you are here, wearing a body. You have beaten him before. "
     "The word of your testimony did it once. It will do it again."),
]

CARD_SEG = ("card", NARRATOR,
            "You have beaten him before. Testimony is how. It still "
            "works.")

CARD_TEXT = ("You have beaten him before.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Three — War in Heaven")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="heaven")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The council court under a divided sky: the terraces of luminous "
        "stone run from warm dawn-gold light on the frame's left into a "
        "cold grey-blue dimming on the frame's right — one court, two "
        "weathers, the boundary between them a single smooth soft fade "
        "with no shape in it. White-robed hosts stand gathered in the "
        "warm side; the dim side lies empty. The camera looks down the "
        "court from high behind the gathered ranks; no face turns back.",
        "one court split between warm gold light and cold empty dimness "
        "by a smooth formless boundary, hosts gathered in the light",
        "any figure in the dim side, any shape in the boundary, faces "
        "to camera, weapons",
        wide=True, devil=True, locks=["COURT", "HOSTS"])),
    ("p02", "s1", _p(
        "Michael at the front: a strong-built spirit commander — the "
        "same FACE as the attached reference, but clothed like every "
        "spirit in heaven in the hosts' bright pure-white one-piece "
        "long-sleeved robe (never brown, never a mortal work tunic) — "
        "stands at the head of deep ranks of white-robed hosts, his arm raised straight out, "
        "palm open toward the cold dim end of the court in the "
        "unmistakable gesture of HALT — no weapon anywhere, his face in "
        "fierce calm profile. Behind him the ranks hold their line. The "
        "camera stands off his shoulder, shooting past him down the "
        "line of his arm toward the empty dimness.",
        "a commander's open-palm HALT aimed at empty dimness, deep "
        "ranks holding behind him, fierce calm profile",
        "swords, spears, shields, armor, wings, any figure in the dim, "
        "faces to camera",
        wide=True, devil=True, locks=["ADAM", "COURT", "HOSTS"])),
    ("p03", "n2", _p(
        "Down the front rank: a row of white-robed men and women "
        "shoulder to shoulder in three-quarter profile, every mouth "
        "OPEN mid-speech — not shouting in rage but declaring, chins "
        "level, eyes bright and wet — the strange sight of a battle "
        "line whose only motion is words. Warm light on their faces "
        "from the left; none looks at the lens.",
        "a battle line of faces mid-declaration, mouths open, chins "
        "level, eyes bright",
        "rage-contorted faces, fists, weapons, anyone facing the lens",
        locks=["HOSTS"])),
    ("p04", "s2", _p(
        "One testimony up close: a young woman, hand pressed flat over "
        "her heart, face lifted in three-quarter, speaking — fierce "
        "and unafraid, tear-tracks bright, the words visibly costing "
        "and worth it. The ranks blur warm behind her.",
        "a young woman's close three-quarter testimony, hand flat on "
        "heart, fierce wet eyes aimed past the lens",
        "her eyes on the lens, a microphone-stance, weapons, wings",
        locks=["HOSTS"])),
    ("p05", ("s2", 0.6), _p(
        "Another: a young man mid-sentence, one step ahead of his row, "
        "both hands open at his sides palms forward — nothing hidden, "
        "nothing held — his jaw set and his gaze aimed hard left past "
        "the camera toward the dark he is answering. Behind him an "
        "older spirit's hand rests on his shoulder.",
        "a young man testifying with open empty palms, an older hand "
        "on his shoulder, hard steady gaze off-frame left",
        "his eyes on the lens, clenched fists, weapons, wings",
        locks=["HOSTS"])),
    ("p06", "n3", _p(
        "The Lamb they trust: from within the faithful ranks, the "
        "view down the court to the distant dais — where the Son "
        "stands small and unmistakable in his cream robe in the "
        "brightest of the light, the only cream in the frame, hosts' "
        "heads and shoulders soft in the near foreground all turned "
        "toward him. The camera shoots past the near heads; his "
        "figure is distant but his identity is instant.",
        "the distant Son in cream at the bright dais seen past the "
        "faithful's heads, every near head turned toward him",
        "his face large or close, halo, anyone facing the lens, a "
        "second cream garment",
        jesus=True, ref=True, wide=True, locks=["COURT", "HOSTS"])),
    ("p07", "n4", _p(
        "Both sides can see God: at the court's cold boundary, a "
        "scatter of white-robed figures stand INSIDE the dim edge "
        "with their backs to the bright dais light — and the light "
        "plainly reaches them, laying long warm streaks across the "
        "dim stone to their heels — while they hold their faces "
        "turned away from it into the grey. Seen from the warm side "
        "at rank height, every figure in profile or from behind.",
        "figures inside the dimness with warm dais-light reaching "
        "their heels, faces deliberately turned away from it",
        "any non-human shape in the dim, faces to camera, weapons, "
        "anyone shielding eyes theatrically",
        devil=True, locks=["COURT", "HOSTS"])),
    ("p08", "n5", _p(
        "The pitch: a loose STANDING cluster of eight spirits at the "
        "boundary line — every figure upright on their feet, nobody "
        "kneeling or bowing — heads tilted a few degrees toward the "
        "empty dimness as if catching a voice on the air, faces "
        "soothed, shoulders loosening, the warm light behind them "
        "and the cold ahead — one woman's face caught half-lit at "
        "the exact seam, wanting to believe the guarantee. Nobody "
        "faces the lens; the dim they listen to is empty.",
        "listeners leaning toward empty dimness as toward a voice, "
        "soothed loosening faces half-lit at the seam",
        "any figure or mouth-shape in the dim, sneering, anyone "
        "facing the lens",
        devil=True, locks=["COURT", "HOSTS"])),
    ("p09", "n6", _p(
        "The third leaves: a broad column of white-robed figures "
        "walks AWAY down the court into the cold grey end, backs to "
        "the camera and to the light, rank after rank receding into "
        "the dimness until the farthest are pale outlines — while in "
        "the near foreground the faithful stand still at the edge of "
        "the warm light watching them go. The camera stands behind "
        "the faithful and shoots past their shoulders after the "
        "leaving column. No face anywhere turns back.",
        "a column of backs receding into cold dimness while the "
        "faithful watch from the warm edge in the near frame",
        "any face turned back, any figure IN the darkness beyond the "
        "column, weapons, wings",
        wide=True, devil=True, locks=["COURT", "HOSTS"])),
    ("p10", ("n6", 0.55), _p(
        "Watching them go: faces among the faithful — grief without "
        "hate: an older man's jaw trembling, a young man's eyes "
        "closed, and at the centre a young woman with her whole arm "
        "outstretched after someone in the leaving column, fingers "
        "open, her face broken with a name she is calling. Every gaze "
        "aimed right past the camera after the departed; none at the "
        "lens.",
        "grieving faithful faces, one woman's arm fully outstretched "
        "after someone leaving, all gazes aimed right past the lens",
        "hate or triumph in any face, anyone facing the lens",
        locks=["HOSTS"])),
    ("p11", "g1", _p(
        "Thrust down: at the court's far cold rim the last of the "
        "leaving column and the dimness itself DRAIN together down "
        "over the edge and out of sight — a grey formless tide "
        "sliding below the stone rim, three-quarters gone — while "
        "warm dawn light re-floods the emptied terraces behind it. "
        "The faithful stand far back in the restored gold. Nothing "
        "in the draining grey has any shape.",
        "the last grey formless tide draining DOWN over the far rim "
        "with light re-flooding the emptied court",
        "falling bodies, any figure or wing in the grey, darkness "
        "overhead, faces to camera",
        wide=True, devil=True, locks=["COURT", "HOSTS"])),
    ("p12", "n7", _p(
        "After: the court stands half-empty in full restored light — "
        "the faithful still in their ranks, unmoving, the wide "
        "vacated terraces bare and bright beside them — seen from "
        "the side at rank height, the camera shooting along the "
        "front line's profiles past them into the emptiness their "
        "family left. Quiet like held breath.",
        "the faithful in ranks beside wide emptied bright terraces, "
        "profiles along the line, held-breath stillness",
        "celebration, banners, anyone facing the lens, any dimness "
        "left",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p13", "n8", _p(
        "The Father's cost: the Father alone at the dais edge, seen "
        "entirely FROM BEHIND — the radiant white robe, the "
        "silver-white hair — facing out over the emptied end of the "
        "court where they went, His head lowered a degree, His "
        "hands still at His sides. Majesty, carrying grief. The "
        "camera keeps a reverent distance; His face is never seen.",
        "the Father from behind at the dais edge facing the emptied "
        "court, head lowered a degree",
        "His face visible, slumped shoulders overdone, halo, anyone "
        "else in frame",
        locks=["FATHER", "COURT"])),
    ("p14", ("n8", 0.55), _p(
        "His profile: close on the Father in near-profile — the deep "
        "sorrow held inside perfect steadiness, eyes fixed far away "
        "toward where a third of His children vanished, mouth firm, "
        "the light warm on the lines of His face. A Father who let "
        "them go because love without freedom is not love.",
        "the Father's near-profile close, deep contained sorrow, "
        "eyes fixed far off-frame",
        "His eyes on the lens, tears streaming, halo, hardness",
        locks=["FATHER"])),
    ("p15", "n9", _p(
        "Standing down: Michael — the same face as the attached reference, in the hosts' bright pure-white long-sleeved robe, never brown — at the front of the ranks lowers his "
        "outstretched arm — caught mid-descent at chest height, palm "
        "still open — his face in three-quarter carrying victory "
        "with no joy in it, the ranks behind him easing from their "
        "line. The cold is gone from the court; the light is whole.",
        "the commander's halting arm caught mid-lowering, victory "
        "without joy, ranks easing behind",
        "weapons, cheering, wings, faces to camera",
        locks=["ADAM", "COURT", "HOSTS"])),
    ("p16", ("n9", 0.6), _p(
        "Where he was cast: from the court's balustrade the deep "
        "beyond is no longer empty — a blue-white world hangs far "
        "below in the darkness, finished and beautiful, oceans and "
        "cloud-swirls bright in the void — and along the rail the "
        "white-robed hosts stand looking down at it in silence, "
        "backs to the camera. The war's next address.",
        "the finished blue-white earth hanging in the deep below the "
        "balustrade, hosts from behind looking down at it",
        "faces to camera, recognizable modern continents, any dark "
        "figure falling, text",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p17", "n10", _p(
        "The contested ground, close: the earth filling the frame "
        "from heaven's vantage — its night side crawling with storm "
        "systems, lightning flickering inside the cloud banks like "
        "distant artillery, the dawn terminator a burning gold line "
        "across the middle of the world. Beautiful and embattled at "
        "once. No figures.",
        "the earth close from above, storms and lightning inside the "
        "night side, a burning dawn line across it",
        "any figure, satellites, text, recognizable country shapes",
        )),
    ("p18", "n11", _p(
        "The veteran: one young spirit's face close and steady — jaw "
        "set, quiet fire behind the eyes, the face of someone who "
        "has already stood a war and held — gaze level past the "
        "camera's left shoulder, warm court light modelling the "
        "face. This is the viewer, before.",
        "one steady close young face with quiet fire, level gaze "
        "past the lens",
        "eyes on the lens, tears, wings, glow",
        locks=["HOSTS"])),
    ("p19", ("n11", 0.58), _p(
        "The body you fought for: in the present day, a pair of "
        "ordinary human hands held open palms-up in a shaft of "
        "morning window light — work-lined, real, warm — the frame "
        "close and plain. The prize of the first war, worn daily.",
        "two ordinary open upturned hands in morning window light, "
        "close and plain",
        "faces, jewellery, brand marks, text",
        era="modern")),
]
