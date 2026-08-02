#!/usr/bin/env python3
"""V2 beat map — row 18, build-18-emmaus (Luke 24:13-35).

COVERAGE: 41 pictures against V1's 8, over 232.3 s = 5.7 s/picture.

⚠️ WINDOWS WERE RE-TIMED 2026-08-01 (Claude worker 12). The inherited map ran on a
219.5 s timeline against the real 232.62 s — every window was adrift, by as much as
13 s at the end. All 38 inherited windows were recomputed from the fixed
extract_beats.py plus each segment's own phrase timings in audio/*.timing.json, and
verified contiguous with no gap or overlap from 0.28 s to the card at 232.62 s.
THREE NEW BEATS were authored to close holds that ran too long on one picture:
b02b (n0 p3b, "the end of everything"), b31b (n8 p3, "they had almost missed him")
and b39 (n10 p5, the closing line). The camera-to-back geometry sentence required by
the row-14 lesson was added to every wide beat's own scene text.

⚠️ THE STAGING PROBLEM THIS ROW HAS, AND HOW IT IS SOLVED. Luke 24:16 says
"their eyes were HOLDEN that they should not know him." The temptation is to
disguise him — a hood, a shadowed face, a different man. THAT IS FORBIDDEN: the
V2 law is that Jesus has ONE locked face, shown the same in every video, and the
old "never show his face" rule is dead. So this build takes the honest reading:

    HE LOOKS EXACTLY LIKE HIMSELF IN EVERY FRAME. The locked face, the cream
    robe, no disguise of any kind. The failure is entirely in THEM — the two
    walk beside him, look straight at him, and simply do not see it. The viewer
    recognises him immediately, and that gap between what the viewer sees and
    what the two see IS the whole first half of the video.

Never hood him, never shadow his face, never turn him away to hide it. Every
Emmaus frame keeps his face plainly visible and puts the not-seeing on the two
disciples' faces instead.

⚠️ THE VANISHING (v31) is shown as AFTERMATH, never as an effect. No fading, no
dissolve, no transparency, no light. b30 is simply the empty place at the table
with his cup and the broken bread still there, and the two men staring at it.
Restraint does the work; a special effect would cheapen it.

SCRIPTURE FACTS (Luke 24:13-35 KJV):
  v13  "threescore furlongs" — about seven miles, which the narration states.
  v15  "Jesus himself drew near, and WENT WITH THEM" — he falls into step; he
       does not appear or arrive dramatically.
  v18  Cleopas is named. The second disciple is not, so this build gives him no
       name either and simply makes him a distinct person.
  v21  "we TRUSTED that it had been he which should have redeemed Israel" — the
       heartbreak line, and the emotional centre of the first half.
  v25  "O fools, and slow of heart" — blunt words, but he has just walked seven
       miles to say them. b17 plays them warm and exasperated and affectionate,
       never contemptuous.
  v27  "beginning at MOSES and all the PROPHETS, he expounded unto them."
  v28  "he MADE AS THOUGH he would have gone further" — he does not invite
       himself in; they have to ask.
  v30  "he took bread, and BLESSED it, and BRAKE, and GAVE to them" — four
       separate actions, and the narration lists all four as separate sentences.
       They get four frames.
  v31  "their eyes were opened, and they knew him; and he VANISHED out of their
       sight."
  v33  "they rose up THE SAME HOUR" and went back — at night, the seven miles
       they had just walked.

CONTENT-CARE: row 18 is GREEN. The crucifixion is referred to but never shown —
no cross, no wounds, no flashback anywhere in this build.

TIME OF DAY, and it is stated by the text itself so it is not a defect: the road
is late AFTERNOON, arriving at Emmaus at SUNSET ("it is toward evening, and the
day is far spent"), the meal is at DUSK by lamplight, and the run back to
Jerusalem is at NIGHT under stars. That progression is the story's own clock.
"""

LOCKS = {
    "CLEOPAS": (
        "CLEOPAS LOCK: Cleopas is the same man in every shot — about fifty, lean and "
        "travel-worn, warm olive-brown skin, a greying dark beard cut short, deep "
        "lines from nose to mouth, and heavy-lidded tired eyes. He wears a "
        "road-dusted DEEP RUSSET-BROWN wool tunic with a rope belt and a satchel on "
        "one shoulder (never cream, never white). His face is shown clearly."
    ),
    "COMPANION": (
        "COMPANION LOCK: the second disciple is the same man in every shot — about "
        "thirty, shorter and stockier than Cleopas, a thick dark beard, broad "
        "cheekbones, warm tan skin, and quick expressive eyes. He wears a "
        "road-dusted DARK OLIVE-GREEN wool tunic with a leather belt and a rolled "
        "blanket over his shoulder (never cream, never white). His face is shown "
        "clearly."
    ),
    "ROAD": (
        "EMMAUS ROAD LOCK: the country road running west from Jerusalem — packed "
        "pale earth winding between dry-stone walls, terraced olive groves and "
        "vineyards on the slopes, stony hillsides with thorn scrub, and low hills "
        "opening ahead. Jerusalem is NOT part of this lock and is never added to a "
        "frame on its own — the city appears only when the beat itself puts it there. "
        "Long late-afternoon light and dust."
    ),
    "JERUSALEM": (
        "FIRST-CENTURY JERUSALEM SKYLINE LOCK: when the city is visible it is the "
        "Jerusalem of about AD 33 and nothing later. Massive pale dressed-limestone "
        "walls with square crenellated towers, and behind them a dense mass of small "
        "FLAT-ROOFED mud-and-limestone houses stepping up the hill, with the great "
        "colonnaded stone platform and the tall rectangular facade of the Second "
        "Temple standing highest. NO MINARETS, no slender pointed towers, no church "
        "steeples, campaniles, spires, crosses, domes, gilded or silver domes, "
        "basilicas, arched bell openings or red pitched tile roofs anywhere on the "
        "skyline, sharp or blurred, near or far. No modern building, aerial, dish, "
        "wire, pole, water tank, glass window, road or vehicle anywhere. Every roof "
        "inside the walls is flat."
    ),
    "OUTBOUND": (
        "OUTBOUND-ROAD LOCK: the men are travelling AWAY from Jerusalem, westward and "
        "downhill toward Emmaus. AHEAD OF THEM AND ACROSS THE WHOLE DISTANCE the road "
        "runs down into empty open country — bare terraced hillsides, olive groves, "
        "dry-stone walls and low rolling hills — and there is NO city, town, village, "
        "wall, gate, tower, rooftop or settlement of any kind visible ahead of them, at "
        "the end of the road in front of them, or anywhere on the horizon they are "
        "walking toward. THE ROAD AHEAD ENDS IN EMPTY HILLS, NOT IN A CITY. Jerusalem lies BEHIND them and "
        "appears only behind their backs, or not at all. The direction of travel must "
        "read at a glance as leaving the city, never as approaching one."
    ),
    "HOUSE": (
        "EMMAUS HOUSE LOCK: a modest village house of warm honey-coloured stone — a "
        "single low room with a beaten earth floor, a small wooden table with three "
        "stools, a stone lamp niche, a water jar, a rolled sleeping mat against the "
        "wall, and a low doorway open to the deep blue of evening. Lit warmly and "
        "unevenly by two small clay oil lamps, with deep shadow in the corners."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------- n0 — two who gave up ----
    {
        "id": "v2-r018-b01", "out": "s01-the-same-sunday.jpeg", "seg": "n0 p1-p2",
        "window": "0.28-8.01", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "JERUSALEM", "OUTBOUND"],
        "narration": ("It was the same Sunday. The tomb was empty, the rumors were "
                      "flying, and two of Jesus's followers had given up and left."),
        "must_show": "two men walking away from Jerusalem, the city's walls behind them — leaving, not arriving.",
        "must_not_show": "no tomb and no cross anywhere; the direction of travel must plainly be AWAY from the city.",
        "scene": (
            "Two men walk a dusty country road away from Jerusalem, seen from behind "
            "and to the side so both their backs and the city they are leaving are in "
            "frame. Behind them the walls and crowded rooftops of Jerusalem stand on "
            "their hill in the afternoon haze; ahead of them the road runs down into "
            "empty olive terraces and open country. Their shoulders are down and "
            "neither is looking back. Long late-afternoon light and dust. Every figure "
            "has two arms, two hands and one head."
            " THE CAMERA STANDS HIGH ON THE STONY SLOPE ABOVE AND TO THE LEFT OF THE ROAD, looking down and across at the two men, who are below it and already past it: they are seen from three-quarter BEHIND with their backs and shoulders toward the lens, walking down and away toward the lower right of the frame, and NOT ONE FACE IS TURNED TOWARD THE LENS. JERUSALEM SITS ON ITS HILL IN THE UPPER LEFT OF THE FRAME, BEHIND THEIR SHOULDERS AND BEHIND THEM ALONG THE ROAD THEY HAVE ALREADY COME DOWN — it is never at the end of the road in front of them. The road ahead of them runs down out of the bottom right of the picture into empty terraced hills. The city is the place they are leaving and the picture must read that way at a glance. Shot on a 35mm prime, deep focus, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b02", "out": "s02-going-over-it-again.jpeg", "seg": "n0 p3a",
        "window": "8.01-14.19", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("They were walking the seven miles from Jerusalem to a village "
                      "called Emmaus, heads down, going over it all again — the arrest, "
                      "the cross, the end of everything they had hoped for."),
        "must_show": "the two mid-argument on the road — one gesturing hard, the other's head down, going over it for the hundredth time.",
        "must_not_show": "no cross, no flashback, no crucifixion imagery of any kind.",
        "scene": (
            "The two men walk the empty road deep in a wearing-out argument — Cleopas "
            "has one hand thrown out sideways mid-sentence with his face turned to his "
            "companion, and the younger man is walking with his head down and his eyes "
            "on the dust, shaking it slowly from side to side. Neither is watching "
            "where he is going. The long road, the olive terraces and the dry hills "
            "stretch away around them in the afternoon light. The camera is back far "
            "enough to see both head to sandals. Every figure has two arms, two hands "
            "and one head."
            " THE CAMERA TRACKS ALONGSIDE AND SLIGHTLY BEHIND THE TWO MEN, level with their shoulders, so both are seen in three-quarter from behind and their eyes travel across the frame to each other and down to the dust, never past the camera. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, shallow depth of field, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b02b", "out": "s02b-the-end-of-everything.jpeg", "seg": "n0 p3b",
        "window": "14.19-20.39", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("going over it all again \u2014 the arrest, the cross, the end of "
                      "everything they had hoped for."),
        "must_show": "the two very small and far away on a long empty road, walked out of words \u2014 the scale of the frame carrying how finished they feel.",
        "must_not_show": "no cross, no arrest, no crucifixion imagery of any kind anywhere in the frame; no third figure yet.",
        "scene": (
            "A wide view of the long pale road running down through dry terraced "
            "hillsides in the late afternoon, with the two men very small and far off "
            "in it, walking apart from each other now with a gap between them and "
            "nothing left to say. The country is huge and empty around them and the "
            "sun is well down the sky. Dust hangs in the light. There is no other "
            "person anywhere in the frame. Every figure has two arms, two hands and "
            "one head."
            " THE CAMERA STANDS WELL BACK AND LOW ON THE ROAD BEHIND THEM AND SHOOTS PAST THEM: the two are small, seen from directly behind, walking away from the lens with their heads down, and the empty road and hills swallow them. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a wide prime, deep focus, real film grain, one photograph."
        ),
    },
    # -------------------------------------------- n1 — the stranger joins ----
    {
        "id": "v2-r018-b03", "out": "s03-fell-into-step.jpeg", "seg": "n1 p1",
        "window": "20.39-25.44", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "narration": ("As they walked and argued and grieved, a stranger came up "
                      "alongside them and fell into step."),
        "must_show": "⚠️ Jesus with his OWN LOCKED FACE plainly visible, walking up alongside them — no hood, no shadow, no disguise.",
        "must_not_show": "NEVER hood or shadow his face and never turn it away — the viewer must recognise him at once. No halo, glare or rim-light. He walks up ordinarily; he does not appear.",
        "scene": (
            "Jesus has come up alongside the two men on the road and fallen into step "
            "with them, walking at their pace on the outside of the pair. His face is "
            "plainly and fully visible in the afternoon light — bare-headed, entirely "
            "himself, nothing covering or shadowing him — and he is looking across at "
            "them with easy interest. The two men are still mid-argument and have "
            "barely registered him. Dust rises from three sets of feet. The camera is "
            "back far enough to see all three head to sandals. Every figure has two "
            "arms, two hands and one head."
            " THE CAMERA WALKS BEHIND AND TO THE LEFT OF THE THREE MEN AND SHOOTS PAST THEM: the two disciples are seen from three-quarter behind with their backs to the lens, and Jesus is on the far side in profile with his gaze going across to them and out of the frame past the camera's right. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, deep focus, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b04", "out": "s04-their-eyes-were-held.jpeg", "seg": "n1 p2",
        "window": "25.44-32.16", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("And Luke tells us something strange and deliberate: their eyes "
                      "were held, so that they did not recognize him."),
        "must_show": "⚠️ THE CENTRAL IDEA: both men looking DIRECTLY at his clearly visible face — and nothing registering. Blank, polite, unrecognising.",
        "must_not_show": "his face must be lit and unobstructed; the failure is entirely in THEIR faces. No halo, glare or rim-light.",
        "scene": (
            "Close on the three of them walking abreast. Jesus's face is turned toward "
            "the two men, fully lit and completely unobscured. Both of them are looking "
            "straight back at him — and there is nothing in either face at all: "
            "Cleopas's expression is merely polite and preoccupied, the younger man's "
            "is blank and incurious, both of them looking directly at him and simply "
            "not seeing. Afternoon light on all three faces. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r018-b05", "out": "s05-they-had-no-idea.jpeg", "seg": "n1 p3",
        "window": "32.16-38.59", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("It was Jesus himself — walking right beside them — and they had "
                      "no idea."),
        "must_show": "the three walking together down the open road, entirely ordinary, the two talking across him as if he were nobody.",
        "must_not_show": "no halo, glare or rim-light; nothing in the frame marks him out — that ordinariness is the point.",
        "scene": (
            "A wide view of the three walking together down the long dusty road "
            "between the olive terraces, side by side, entirely unremarkable — the two "
            "disciples talking across to each other with Jesus between them, one of "
            "them gesturing past him without a glance. Nothing whatever in the frame "
            "sets him apart: same dust, same light, same road. The hills and the "
            "lowering sun stretch away ahead. Every figure has two arms, two hands and "
            "one head."
            " THE CAMERA STANDS FAR BACK ON THE ROAD BEHIND THE THREE AND SHOOTS PAST THEM down the long road: all three are seen from behind, walking away from the lens between the terraces, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a wide prime, deep focus, real film grain, one photograph."
        ),
    },
    # ---------------------------------------------------- n2 — what happened ----
    {
        "id": "v2-r018-b06", "out": "s06-what-are-you-talking-about.jpeg", "seg": "n2 p1-p2",
        "window": "38.59-44.44", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("He asked them what they were talking about that had them so "
                      "heavy. They stopped in the road, faces stricken."),
        "must_show": "all three halted dead in the road — the two men stopped mid-step, faces gone raw at being asked.",
        "must_not_show": "no halo, glare or rim-light; the stopping must be abrupt.",
        "scene": (
            "The three have stopped dead in the middle of the road. Jesus stands "
            "easily with one hand open in a plain question. Both disciples have halted "
            "mid-step and turned to him, and their faces have come apart — Cleopas's "
            "mouth open and his brows drawn up, the younger man's eyes wet and "
            "blinking hard, both of them stricken at simply being asked. Dust settles "
            "around their feet. Long afternoon light. The camera holds all three head "
            "to sandals. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS OFF THE SIDE OF THE ROAD, LEVEL WITH THE THREE, AND SHOOTS ACROSS THEM in profile: Jesus faces the two men and the two men face him, so every eyeline runs from left to right across the picture and exits the frame at the edges, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, deep focus, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b07", "out": "s07-are-you-the-only-one.jpeg", "seg": "n2 p3",
        "window": "44.44-52.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("One of them, Cleopas, said: are you the only visitor to Jerusalem "
                      "who doesn't know what has happened these last few days?"),
        "must_show": "close on Cleopas, incredulous — a man who cannot believe anyone alive has missed it.",
        "must_not_show": "not hostile; disbelief and grief together. Do not put Jesus in this frame.",
        "scene": (
            "Close on Cleopas's lined face on the road, staring at the man in front of "
            "him with open incredulity — his head has come forward and slightly to one "
            "side, his brows are up, one hand has lifted halfway in a baffled gesture. "
            "Under the disbelief his eyes are red-rimmed and exhausted. Late afternoon "
            "light across his greying beard. He has one head."
        ),
    },
    {
        "id": "v2-r018-b08", "out": "s08-art-thou-only-a-stranger.jpeg", "seg": "s18",
        "window": "52.76-60.46", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "JERUSALEM", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("Art thou only a stranger in Jerusalem, and hast not known the "
                      "things which are come to pass there in these days? (Luke 24:18)"),
        "must_show": "Cleopas gesturing back down the road toward Jerusalem as he says it, the city small on its hill in the distance behind them.",
        "must_not_show": "no halo, glare or rim-light; still no recognition on either face.",
        "scene": (
            "Cleopas has flung one arm back down the road toward Jerusalem, whose "
            "walls and rooftops stand small and pale on their distant hill behind "
            "them, and he is speaking hard at the stranger. The younger man stands "
            "beside him nodding grimly. Jesus listens with his head inclined, his face "
            "open and plainly visible, and neither man's expression has changed toward "
            "him at all. Long light, long shadows on the road. The camera is back far "
            "enough to hold the three and the distant city. Every figure has two arms, "
            "two hands and one head."
            " THE CAMERA STANDS OFF THE SIDE OF THE ROAD AND SHOOTS ACROSS ALL THREE IN PROFILE, with Jesus nearest the lens seen from three-quarter behind: his shoulder and the back of his head are the near frame, the two men face him across the picture, and Cleopas's flung-out arm and his gaze both travel to the far side of the frame. JERUSALEM LIES SMALL AND PALE ON ITS DISTANT HILL IN THE FAR BACKGROUND BEYOND THE TWO MEN, back along the road they came down, never at the end of the road they are walking toward. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    # -------------------------------------------------- n3 — it poured out ----
    {
        "id": "v2-r018-b09", "out": "s09-it-all-poured-out.jpeg", "seg": "n3 p1-p2",
        "window": "60.46-68.88", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("And it all poured out. Jesus of Nazareth — a prophet mighty in "
                      "word and deed — handed over and crucified."),
        "must_show": "both men talking at once, hands moving, the story spilling out of them on the road.",
        "must_not_show": "no cross, no crucifixion imagery, no flashback of any kind. No halo or rim-light.",
        "scene": (
            "Both disciples are talking at once on the road, hands going, words falling "
            "over each other — Cleopas counting something off on his fingers, the "
            "younger man cutting in with both palms up. Jesus stands between them "
            "simply listening, unhurried, letting it come. Their faces are flushed and "
            "wet with the telling. Long afternoon light and dust. The camera holds all "
            "three. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS BESIDE THE ROAD AND SHOOTS ACROSS THE GROUP in three-quarter, with the younger disciple's back nearest the lens: every gaze runs between the three of them and out of the frame at the left and right edges. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b10", "out": "s10-we-had-hoped.jpeg", "seg": "n3 p3",
        "window": "68.88-75.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("And then the line that holds all their heartbreak: we had hoped "
                      "that he was the one who would rescue Israel."),
        "must_show": "⚠️ THE EMOTIONAL CENTRE OF THE FIRST HALF: close on the two faces as the sentence comes out — the fight going out of them, past tense on their faces.",
        "must_not_show": "no anger left in the frame; this is grief and defeat. Do not put Jesus in this frame.",
        "scene": (
            "Close on the two disciples' faces side by side. All the argument has gone "
            "out of both of them at once — Cleopas's hand has dropped to his side and "
            "his mouth has come shut, his eyes gone unfocused down the road; the "
            "younger man's chin has crumpled and he is looking at the ground with his "
            "jaw working. It is the exact look of people saying a hope out loud in the "
            "past tense. Long low light on their faces. Every figure has one head."
        ),
    },
    {
        "id": "v2-r018-b11", "out": "s11-but-nobody-had-seen-him.jpeg", "seg": "n3 p4-p5",
        "window": "75.97-83.87", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("Now some women were saying the tomb was empty and angels said he "
                      "was alive. But nobody had seen him."),
        "must_show": "⚠️ THE IRONY: one of them shrugging off the rumour with a hopeless gesture — while saying nobody has seen him, straight at the man he is looking at.",
        "must_not_show": "no tomb, no angels, no flashback; do NOT paint the empty tomb. No halo or rim-light.",
        "scene": (
            "The younger disciple has both hands turned up in a hopeless empty shrug "
            "as he says it, his face bitter and tired, and he is looking directly at "
            "Jesus while he says it. Cleopas beside him has his eyes on the ground. "
            "Jesus stands looking back at the younger man with the faintest change "
            "beginning at the corner of his mouth. The empty road runs away behind "
            "them. Long low afternoon light. Every figure has two arms, two hands and "
            "one head."
            " THE CAMERA STANDS BEHIND CLEOPAS AND SHOOTS PAST HIM: his shoulder and greying head fill the near frame, the younger man is turned toward Jesus with his eyes travelling clearly across the frame to Jesus's face, and Jesus's eyes go back to him — every eyeline crosses the picture and none of it comes toward the lens. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, shallow depth of field, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b12", "out": "s12-we-trusted.jpeg", "seg": "s21",
        "window": "83.87-89.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("But we trusted that it had been he which should have redeemed "
                      "Israel. (Luke 24:21)"),
        "must_show": "very close on Cleopas saying the line — the whole loss of it in one face.",
        "must_not_show": "do not put Jesus in this frame; no anger, only loss.",
        "scene": (
            "Very close on Cleopas's face, filling the frame. His eyes are wet and "
            "fixed on nothing, his mouth is barely moving on the words, and every line "
            "in the weathered face has gone slack and heavy. There is no anger left in "
            "it at all — only a man saying out loud that the thing he built his life "
            "on is over. Low golden light across one side of his face."
        ),
    },
    # --------------------------------------------------- n4a / j1 — the answer ----
    {
        "id": "v2-r018-b13", "out": "s13-the-stranger-listened.jpeg", "seg": "n4a",
        "window": "89.30-93.20", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "The stranger listened to all of it. And then he answered them:",
        "must_show": "close on Jesus having heard it all — his face full of something enormous held back, about to speak.",
        "must_not_show": "no halo, glare or rim-light; he is not smug or amused at their expense.",
        "scene": (
            "Close on Jesus's face on the road in the low golden light, having listened "
            "to all of it. His expression is full and complicated — warmth, and grief "
            "for them, and something enormous being held just behind his eyes. His "
            "mouth is opening to answer. There is nothing smug or superior in it. The "
            "blurred road and olive terraces behind him."
        ),
    },
    {
        "id": "v2-r018-b14", "out": "s14-slow-of-heart.jpeg", "seg": "j1 a",
        "window": "93.20-98.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("O fools, and slow of heart to believe all that the prophets have "
                      "spoken: (Luke 24:25)"),
        "must_show": "⚠️ TONE: warm exasperation, not contempt. He has walked seven miles to say this — head shaking, a rueful half-smile, affection under the bluntness.",
        "must_not_show": "NOT scorn, NOT sneering, NOT anger. If his face reads as contempt the whole road scene curdles. No halo or rim-light.",
        "scene": (
            "Jesus has turned to face the two men on the road, shaking his head slowly "
            "with a rueful half-smile pulling at one corner of his mouth and his "
            "eyebrows raised — exasperated and completely fond, the way you speak to "
            "people you have gone a long way out of your way for. Both hands have come "
            "open in front of him. The two disciples are blinking at him, taken aback. "
            "Long low light. The camera holds all three. Every figure has two arms, "
            "two hands and one head."
            " THE CAMERA STANDS BEHIND THE TWO DISCIPLES AND SHOOTS PAST THEM at Jesus: their backs and shoulders frame the near edges of the picture, dark and out of focus, and Jesus is beyond them turned to them, his eyes going to their faces and exiting the frame below the camera. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b15", "out": "s15-ought-not-christ-to-have-suffered.jpeg", "seg": "j1 b",
        "window": "98.04-104.65", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Ought not Christ to have suffered these things, and to enter into "
                      "his glory? (Luke 24:26)"),
        "must_show": "close on Jesus asking it — the question genuinely put, urgent and warm.",
        "must_not_show": "no halo, glare or rim-light; nothing triumphant.",
        "scene": (
            "Close on Jesus's face asking the question, leaning slightly in toward the "
            "men out of frame. His eyes are urgent and warm and his hand has come up "
            "open between them, fingers spread — a man putting a real question to "
            "people he wants to understand it. Low golden light along his cheek and "
            "beard. His hand has five fingers."
        ),
    },
    # --------------------------------------------- n4b — he opened the scriptures ----
    {
        "id": "v2-r018-b16", "out": "s16-beginning-at-moses.jpeg", "seg": "n4b p1a",
        "window": "104.65-112.16", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("And then, starting all the way back at Moses, walking through "
                      "prophet after prophet, he opened the scriptures to them —"),
        "must_show": "the three walking on together while he teaches — his hands working as he explains, the two men now watching him instead of the road.",
        "must_not_show": "no scroll or book — they are walking a road from memory; no halo or rim-light.",
        "scene": (
            "The three are walking on down the road again, but everything has changed "
            "about the shape of them: Jesus is in the middle with both hands moving as "
            "he explains, laying one point after another in the air, and the two "
            "disciples have closed in on either side of him with their heads turned "
            "toward his face, no longer watching where they are going. There is no "
            "book or scroll anywhere. Long shadows stretch ahead. The camera is back "
            "far enough to see all three head to sandals. Every figure has two arms, "
            "two hands and one head."
            " THE CAMERA WALKS BACKWARD DOWN THE ROAD AHEAD OF THE THREE BUT OFF TO ONE SIDE, shooting them in three-quarter profile so their heads are turned to each other across the frame and every eyeline exits past the camera's right without one of them squaring up to the lens. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, deep focus, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b17", "out": "s17-broken-before-crowned.jpeg", "seg": "n4b p1b",
        "window": "112.16-119.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("showing them every place the whole story had been pointing to a "
                      "rescuer who had to be broken before he could be crowned."),
        "must_show": "the two men's faces as it goes in — concentration, then the first flicker of something rearranging behind their eyes.",
        "must_not_show": "they still do not recognise him; this is comprehension, not recognition. Do not put Jesus in this frame.",
        "scene": (
            "Close on the two disciples' faces as they walk and listen. Cleopas's brows "
            "have drawn hard together and his lips are parted, following it closely; "
            "the younger man's eyes have gone wide and are moving quickly as pieces "
            "start dropping into place behind them. Neither has recognised anything "
            "about the man himself — this is only the argument landing. Low golden "
            "light on both faces. Every figure has one head."
        ),
    },
    {
        "id": "v2-r018-b18", "out": "s18-it-was-the-plan.jpeg", "seg": "n4b p2-p3",
        "window": "119.66-124.51", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": "The cross was not the collapse of the plan. It was the plan.",
        "must_show": "the three small on the long road under a wide evening sky — a lesson still going as the sun drops.",
        "must_not_show": "no cross imagery; no halo or rim-light.",
        "scene": (
            "A wide view of the three figures small on the long pale road as it winds "
            "down through the olive terraces, the sun now low and the sky opening gold "
            "and enormous above them. Jesus is still mid-explanation with a hand "
            "raised, the two men still walking close on either side with their heads "
            "turned to him. Their shadows run long across the road. Every figure has "
            "two arms, two hands and one head."
            " THE CAMERA STANDS HIGH ON THE TERRACE ABOVE AND BEHIND THE THREE AND SHOOTS DOWN AND PAST THEM as they walk away from the lens down the winding road: they are small, seen from behind, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a wide prime, deep focus, real film grain, one photograph."
        ),
    },
    # ------------------------------------------------- n5 — abide with us ----
    {
        "id": "v2-r018-b19", "out": "s19-they-reached-emmaus.jpeg", "seg": "n5 p1",
        "window": "124.51-130.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "HOUSE", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("They reached Emmaus as the sun was going down, and the stranger "
                      "acted as if he would keep walking on into the night."),
        "must_show": "SCRIPTURE-EXACT (v28): at the village edge the two are turning off toward a doorway while Jesus keeps walking on down the road — he does not invite himself in.",
        "must_not_show": "he must NOT stop or angle toward the house; his body is still committed to the road. No halo or rim-light. NOTE: sunset is CORRECT here — the text says so.",
        "scene": (
            "At the edge of a small village of honey-coloured stone at sunset. The two "
            "disciples have turned aside off the road toward a low doorway, and Jesus "
            "has kept walking straight on past the turning, his body and his feet still "
            "committed to the road ahead, already a pace or two beyond them. The two "
            "have half-turned back after him. The sun is right down on the hills and "
            "the sky is gold and rose. The camera is back far enough to hold the "
            "doorway, the road and all three. Every figure has two arms, two hands and "
            "one head."
            " THE CAMERA STANDS BACK ALONG THE ROAD BEHIND ALL THREE AND SHOOTS PAST THEM toward the village: the two disciples are seen from behind turning aside to the doorway, and Jesus is beyond them walking on away from the lens with his back to the camera, so the picture reads at a glance as him continuing and them stopping. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, deep focus, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b20", "out": "s20-they-couldnt-let-him-go.jpeg", "seg": "n5 p2-p3",
        "window": "130.76-138.68", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("But they couldn't let him go. Stay with us, they said — it's "
                      "nearly evening, the day is almost gone."),
        "must_show": "a hand actually catching his arm to stop him — them pressing him to stay, physically.",
        "must_not_show": "no halo, glare or rim-light; the initiative is entirely theirs.",
        "scene": (
            "Cleopas has come after him and caught Jesus by the forearm to stop him "
            "going, and the younger disciple is beside them with both hands out toward "
            "the doorway, urging. Both their faces are lit with the last of the sunset "
            "and openly pleading. Jesus has half turned back to them, his face warm. "
            "The road beyond runs on into the dusk. The camera holds all three head to "
            "sandals. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS BEHIND JESUS ON THE ROAD AND SHOOTS PAST HIM at the two men: his back and the hand on his forearm are in the near frame, and both disciples' eyes go up to his face, exiting the picture past the camera's left. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b21", "out": "s21-abide-with-us.jpeg", "seg": "s29 + n5 p4",
        "window": "138.68-146.55", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "HOUSE"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("So he went in to stay. — Abide with us: for it is toward evening, "
                      "and the day is far spent. (Luke 24:29)"),
        "must_show": "him stepping in through the low doorway with the two ushering him, warm lamplight inside and deep blue dusk outside.",
        "must_not_show": "no halo, glare or rim-light; the only light is lamplight and the last of the sky.",
        "scene": (
            "Jesus is stepping in through the low stone doorway of the house with "
            "Cleopas's hand at his back and the younger disciple already inside "
            "beckoning him on. Warm orange lamplight spills out around them from the "
            "small room and the sky behind has gone deep blue with the last rose gone "
            "off the hills. The camera is outside looking in, holding the doorway and "
            "all three. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS OUTSIDE IN THE LANE BEHIND THE GROUP AND SHOOTS PAST THEM into the lit doorway: the men are seen from behind moving away from the lens into the house, dark shapes against the warm interior light, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    # ---------------------------------------------------- n6 — the bread ----
    {
        "id": "v2-r018-b22", "out": "s22-they-sat-down-to-the-table.jpeg", "seg": "n6 p1-p2",
        "window": "146.55-151.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "HOUSE"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("They sat down to the table. And then their guest did the one thing "
                      "only the host of the house should do."),
        "must_show": "the three at the small table by lamplight — and Jesus, the guest, reaching for the loaf that is not his to take.",
        "must_not_show": "no halo, glare or rim-light; the two must not have noticed yet.",
        "scene": (
            "The three are seated at the small wooden table in the lamplit room, a "
            "round flat loaf, a jug and three clay cups between them. Jesus, seated in "
            "the guest's place, has reached out and put his hands to the loaf — the "
            "host's act, done by the visitor. Cleopas is still talking with his cup "
            "half raised and the younger man is turned to him; neither has noticed "
            "yet. Two small lamps throw warm uneven light and deep shadow. The camera "
            "holds the table and all three. Every figure has two arms, two hands and "
            "one head."
            " THE CAMERA SITS LOW AT THE NEAR EDGE OF THE TABLE BEHIND CLEOPAS AND SHOOTS PAST HIS SHOULDER across the table: his back and cup are in the near frame out of focus, and every gaze in the room runs between the men and the loaf and exits the frame at the sides. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, shallow depth of field, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b23", "out": "s23-he-took-the-bread.jpeg", "seg": "n6 p3",
        "window": "151.77-153.22", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "He took the bread.",
        "must_show": "close on his two hands lifting the loaf off the table.",
        "must_not_show": "no halo, glare or rim-light; no light on or from the bread.",
        "scene": (
            "Close on two hands lifting a round flat loaf of bread up off the wooden "
            "table in the warm lamplight, fingers spread underneath it, the crust "
            "catching the low orange light. Nothing is shining. The blurred table and "
            "cups are beyond. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r018-b24", "out": "s24-he-blessed-it.jpeg", "seg": "n6 p4",
        "window": "153.22-154.35", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "He blessed it.",
        "must_show": "close on his face and the held loaf — head slightly bowed over it, eyes closed, giving thanks.",
        "must_not_show": "no halo, glare or rim-light; nothing supernatural in the air or on the bread.",
        "scene": (
            "Close on Jesus holding the loaf in both hands at the table, his head "
            "inclined a little over it and his eyes closed, his lips moving in a short "
            "blessing. The lamplight is warm on his lowered face and the crust of the "
            "bread. Nothing is happening in the air. The dim room is soft behind him."
        ),
    },
    {
        "id": "v2-r018-b25", "out": "s25-he-broke-it.jpeg", "seg": "n6 p5",
        "window": "154.35-155.12", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "He broke it.",
        "must_show": "⚠️ THE BREAKING, caught mid-action: the loaf tearing apart between his two hands, crumbs falling.",
        "must_not_show": "no halo, glare or rim-light; no wounds shown on the hands — Luke does not mention them here and CONTENT-CARE keeps them out.",
        "scene": (
            "Very close on the loaf being torn apart between two hands, caught exactly "
            "mid-break — the crust splitting, the soft inside pulling open in strands, "
            "a few crumbs falling toward the table. The hands are strong and ordinary "
            "and unmarked. Warm lamplight rakes across the torn bread. Each hand has "
            "five fingers."
        ),
    },
    {
        "id": "v2-r018-b26", "out": "s26-he-held-it-out.jpeg", "seg": "n6 p6",
        "window": "155.12-157.52", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": "And he held it out to them.",
        "must_show": "his hands extending the broken halves across the table toward the two men — and their heads beginning to come round.",
        "must_not_show": "no halo, glare or rim-light; recognition has not landed yet, it is arriving.",
        "scene": (
            "Jesus's hands are extended across the small table holding out the two "
            "broken halves of the loaf toward the men. Both disciples are turning "
            "toward the offered bread, and something has just begun to happen in their "
            "faces — Cleopas's cup has stopped halfway to his mouth, the younger man's "
            "head has come round sharply. Warm lamplight over the table. The camera "
            "holds all three. Every figure has two arms, two hands and one head."
            " THE CAMERA SITS BEHIND JESUS AT THE TABLE AND SHOOTS PAST HIS SHOULDER AND HIS OUTSTRETCHED HANDS toward the two men: his back is the near frame, and both disciples' eyes are on the broken bread in the middle of the picture, not on the lens. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, shallow depth of field, real film grain, one photograph."
        ),
    },
    # ------------------------------------------------ n7 — they knew him ----
    {
        "id": "v2-r018-b27", "out": "s27-their-eyes-were-opened.jpeg", "seg": "n7 p1",
        "window": "157.52-165.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("And in that motion — the taking, the blessing, the breaking of the "
                      "bread — their eyes were opened, and they knew him."),
        "must_show": "⚠️ THE PAYOFF OF b04: the same two faces, and now recognition detonating across both of them at once.",
        "must_not_show": "do not put Jesus in this frame — this beat belongs entirely to their faces, and it must plainly answer the blank frame from the road.",
        "scene": (
            "Very close on the two disciples' faces side by side across the table, and "
            "recognition has gone off in both at the same instant. Cleopas's eyes have "
            "flown wide and his whole face has come up and open, his cup forgotten and "
            "tipping in his hand; the younger man has recoiled back with his mouth "
            "wide and one hand half risen toward his own chest. Warm lamplight full on "
            "both faces. Every figure has one head."
        ),
    },
    {
        "id": "v2-r018-b28", "out": "s28-it-was-jesus.jpeg", "seg": "n7 p2",
        "window": "165.23-167.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "HOUSE"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": "It was Jesus.",
        "must_show": "the last frame he is in — sitting at the table, entirely himself, looking back at them with the bread still held out.",
        "must_not_show": "no halo, glare or rim-light and NO fading or transparency — he is completely solid and present in this frame.",
        "scene": (
            "Jesus sits at the small table in the lamplight, completely solid and "
            "present and entirely himself, the broken bread still held out in his "
            "hands, looking back at the two men with a warm, quiet, unmistakable "
            "expression. Both disciples are frozen staring at him. Nothing about him "
            "is faded, transparent or altered in any way. Warm uneven lamplight. The "
            "camera holds all three. Every figure has two arms, two hands and one head."
            " THE CAMERA SITS BEHIND THE TWO DISCIPLES AND SHOOTS PAST THEIR SHOULDERS across the table at Jesus: their backs and heads are the dark near frame, and Jesus's eyes go to them and exit the picture below the camera, never into the lens. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, shallow depth of field, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b29", "out": "s29-the-empty-place.jpeg", "seg": "n7 p3",
        "window": "167.28-176.19", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "HOUSE"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("And in the very instant they recognized him, he was gone — "
                      "vanished from the table, the bread still warm in their hands."),
        "must_show": "⚠️ THE VANISHING AS AFTERMATH ONLY: the empty stool, his untouched cup, the broken bread now in THEIR hands, and the two staring at nothing.",
        "must_not_show": "NO fading figure, NO transparency, NO dissolve, NO light, NO after-image, NO empty outline. He is simply not in the frame. A special effect here cheapens the whole build.",
        "scene": (
            "The small lamplit room, and the third stool at the table is EMPTY. His "
            "clay cup sits untouched where he left it and the two broken halves of the "
            "loaf are now in the two disciples' own hands. Both men are staring at the "
            "empty place with their mouths open, Cleopas half risen off his seat with "
            "one hand out toward nothing at all. There is no figure, no outline and no "
            "light anywhere in the frame — only an empty stool. Warm lamplight, deep "
            "shadow. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS BEHIND AND TO THE SIDE OF CLEOPAS AND SHOOTS PAST HIM ACROSS THE TABLE at the empty stool, which sits alone in the middle of the picture: his shoulder and half-risen back are the near frame, and both men's eyes are locked on the vacant stool at the far side of the table, travelling away from the lens. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    # ------------------------------------------------ n8 — our hearts burned ----
    {
        "id": "v2-r018-b30", "out": "s30-they-turned-to-each-other.jpeg", "seg": "n8 p1",
        "window": "176.19-177.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": "They turned to each other, stunned.",
        "must_show": "the two grabbing at each other across the table — hands on arms, faces inches apart, both talking at once.",
        "must_not_show": "do not put Jesus in this frame.",
        "scene": (
            "The two disciples have seized each other across the small table — "
            "Cleopas's hand clamped on the younger man's forearm and the younger man's "
            "hand gripping his shoulder, their faces inches apart, both of them "
            "talking at once with their eyes enormous and their mouths going. The "
            "bread is still in their other hands. Warm lamplight. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r018-b31", "out": "s31-he-was-with-us-the-whole-way.jpeg", "seg": "n8 p2",
        "window": "177.75-185.61", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "HOUSE"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("Weren't our hearts burning inside us, they said, the whole time he "
                      "was talking to us on the road, while he opened the scriptures to "
                      "us? He had been with them the entire way, and they had almost "
                      "missed him."),
        "must_show": "one of them pointing back out through the open doorway toward the dark road — putting together where he was the whole time.",
        "must_not_show": "do not put Jesus in this frame; no flashback imagery of the road.",
        "scene": (
            "Both men are on their feet now, and the younger disciple is pointing out "
            "through the open low doorway into the night toward the road they came "
            "along, his arm fully extended, his face astonished. Cleopas has both hands "
            "on his own head, staring at the doorway. The empty stool and the abandoned "
            "cup sit at the table between them. Warm lamplight inside, black night in "
            "the doorway. The camera holds the room. Every figure has two arms, two "
            "hands and one head."
            " THE CAMERA STANDS IN THE CORNER OF THE ROOM BEHIND AND TO THE SIDE OF BOTH MEN AND SHOOTS PAST THEM toward the open doorway: they are seen in three-quarter from behind, both faces turned away toward the black night outside, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b31b", "out": "s31b-they-had-almost-missed-him.jpeg", "seg": "n8 p3",
        "window": "185.61-190.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "HOUSE"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("He had been with them the entire way, and they had almost missed "
                      "him."),
        "must_show": "the two gone quiet at the realisation \u2014 the noise has dropped out of them and they are simply looking at each other, winded by how close they came to missing it.",
        "must_not_show": "no Jesus in the frame; no glow, light or figure at the empty stool; nothing supernatural.",
        "scene": (
            "The two men stand facing each other in the small lamplit room and all the "
            "noise has just gone out of them. Cleopas's hands have come down and the "
            "younger man has gone completely still, and they are looking at each other "
            "with the same winded expression \u2014 people who have just understood how "
            "nearly they walked past it. Between them the table holds the empty stool, "
            "the untouched clay cup and the broken bread exactly where they were left. "
            "Two small clay saucer lamps with single wick flames give all the light in "
            "the room, warm and uneven, with deep shadow in the corners and black night "
            "in the low doorway; there is no glass chimney, no metal lantern, no hanging "
            "fixture and nothing manufactured anywhere in the room. Every figure has two "
            "arms, two hands and one head."
            " THE CAMERA STANDS BEHIND THE ABANDONED TABLE AND SHOOTS PAST THE EMPTY STOOL at the two men standing beyond it: the stool and the untouched cup are the near frame, both men are in three-quarter looking at each other, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, shallow depth of field, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b32", "out": "s32-did-not-our-heart-burn.jpeg", "seg": "s32",
        "window": "190.77-197.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("Did not our heart burn within us, while he talked with us by the "
                      "way, and while he opened to us the scriptures? (Luke 24:32)"),
        "must_show": "close on Cleopas with his hand pressed flat to his own chest as he says it — naming what he felt and did not understand.",
        "must_not_show": "no light or effect at the chest; do not put Jesus in this frame.",
        "scene": (
            "Close on Cleopas in the lamplight with one hand pressed flat against his "
            "own chest, his other hand open in the air, his face lit up and streaming "
            "and half laughing as he says it. His eyes are wide and shining. Nothing "
            "is happening at his chest — it is simply his hand on it. Warm uneven "
            "light. He has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n9 — the run back ----
    {
        "id": "v2-r018-b33", "out": "s33-they-did-not-wait-for-morning.jpeg", "seg": "n9 p1",
        "window": "197.81-199.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "HOUSE"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": "They did not wait for morning.",
        "must_show": "the two bolting out through the doorway into the dark — the meal abandoned mid-table behind them.",
        "must_not_show": "do not put Jesus in this frame; the abandoned table must be visible.",
        "scene": (
            "Both men are bolting out through the low doorway into the black night, "
            "one already through it and the other coming behind with a hand on the "
            "frame, a stool knocked over behind them. On the table left in the "
            "lamplight sit the untouched cup, the jug and the broken bread. Nobody has "
            "put anything away. Warm light inside, deep night outside. Every figure "
            "has two arms, two hands and one head."
            " THE CAMERA STANDS INSIDE THE ROOM BEHIND THE TWO MEN AND SHOOTS PAST THEM at the doorway they are going through: both are seen from behind, moving away from the lens into the night, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b34", "out": "s34-seven-dark-miles.jpeg", "seg": "n9 p2a",
        "window": "199.22-203.91", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "JERUSALEM"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("That same hour they got up and ran the seven dark miles back to "
                      "Jerusalem,"),
        "must_show": "⚠️ THE INVERSE OF b01: the two running BACK toward Jerusalem, at night, under stars — the same road, the opposite direction.",
        "must_not_show": "do not put Jesus in this frame; the direction must plainly be toward the city now.",
        "scene": (
            "The two men are running hard along the pale night road toward Jerusalem, "
            "whose walls and scattered lamplights stand on the distant hill ahead of "
            "them. The road, the dry-stone walls and the olive terraces are silver and "
            "black under a wide sky full of stars. Both are running flat out, one a "
            "little ahead, robes flying, their breath visible. It is the same road they "
            "walked down and they are going the other way. The camera is back far "
            "enough to see them and the city ahead. Every figure has two arms, two "
            "hands and one head."
            " THE CAMERA RUNS ON THE ROAD BEHIND THE TWO MEN AND SHOOTS PAST THEM toward the distant city: both are seen from directly behind, running away from the lens up the pale road, and NOT ONE FACE IS TURNED TOWARD THE LENS. Their backs face the camera and the lamplit city lies ahead of them, so the direction of travel reads unmistakably as back toward Jerusalem. Shot on a 35mm prime at night, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b35", "out": "s35-they-found-the-eleven.jpeg", "seg": "n9 p2b",
        "window": "203.91-209.94", "wide": True, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("found the eleven, and said the words the whole world had been "
                      "aching to hear: the Lord is risen."),
        "must_show": "the two bursting into a shuttered lamplit upper room full of grieving disciples — every head snapping toward the door.",
        "must_not_show": "do not put Jesus in this frame; the room must have been in mourning before they came in.",
        "scene": (
            "A shuttered upper room at night, lit by two lamps, with a dozen men and "
            "women sitting slumped and silent in their grief around the walls — and "
            "the door has just been flung open. Cleopas and his companion have burst "
            "in, filthy with dust and gasping, both talking at once with their arms up. "
            "Every head in the room has snapped toward them and people are starting up "
            "off the floor. Warm lamplight, black night in the doorway. The camera "
            "holds the room. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS IN THE FAR CORNER OF THE UPPER ROOM BEHIND THE SEATED MOURNERS AND SHOOTS PAST THEIR BACKS toward the flung-open door: the near figures are seen from behind, and every head in the room is turned away from the lens toward the two men in the doorway. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 35mm prime, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b36", "out": "s36-we-have-seen-him.jpeg", "seg": "n9 p3-p4",
        "window": "209.94-213.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLEOPAS", "COMPANION"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": "It's true. We have seen him.",
        "must_show": "close on the two of them saying it — filthy, gasping, faces blazing with certainty.",
        "must_not_show": "do not put Jesus in this frame.",
        "scene": (
            "Close on the two disciples' faces in the lamplit room, still heaving for "
            "breath, dust and sweat streaked over both of them, hair wild from the run. "
            "Cleopas has one hand gripping the younger man's shoulder and both of their "
            "faces are absolutely blazing — eyes wide and wet, mouths open, utterly "
            "certain. Warm lamplight. Every figure has one head."
        ),
    },
    # ------------------------------------------------- n10 — how he spent it ----
    {
        "id": "v2-r018-b37", "out": "s37-not-with-kings.jpeg", "seg": "n10 p1-p3",
        "window": "213.05-218.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": ("Notice how the risen Jesus spent that first afternoon. Not with "
                      "kings. Not with crowds."),
        "must_show": "the empty country road at night — the ordinary, unimportant place he chose.",
        "must_not_show": "no people at all; no palace, no crowd, no temple. Do not put Jesus in this frame.",
        "scene": (
            "A wide view of the empty country road under the stars — pale dust winding "
            "between dry-stone walls, olive terraces black on the slopes, hills rolling "
            "away, and not one person anywhere in the frame. It is a small, ordinary, "
            "unimportant road in the middle of nowhere. Starlight and deep blue "
            "darkness."
            " THE CAMERA STANDS LOW IN THE MIDDLE OF THE EMPTY ROAD ITSELF AND SHOOTS AWAY FROM THE LENS down its length, so the road runs from the bottom of the frame into the dark hills. There is nobody in the picture at all. Shot on a wide prime at night, deep focus, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b38", "out": "s38-walking-with-the-ones-who-lost-hope.jpeg", "seg": "n10 p4",
        "window": "218.66-228.25", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLEOPAS", "COMPANION", "ROAD", "OUTBOUND"],
        "char_refs": ["assets/s01-the-same-sunday.jpeg", "assets/s03-fell-into-step.jpeg"],
        "narration": ("On a dusty road, with two heartbroken people who had already quit "
                      "— walking at their pace, patiently opening the scriptures, until "
                      "the moment they could see. He is still in the habit of walking "
                      "with the ones who have lost hope."),
        "must_show": "the closing frame: the three walking the road together again in the low golden light, at their pace, side by side.",
        "must_not_show": "no halo, glare or rim-light; nothing grand — the whole point is how ordinary and patient it looks.",
        "scene": (
            "A wide closing view of the three walking together down the long pale road "
            "in warm low light, side by side and unhurried, Jesus in the middle "
            "matching their pace exactly with one hand mid-gesture and both men "
            "turned toward him listening. The olive terraces and the open hills "
            "stretch away and their three shadows run long across the dust. There is "
            "nothing grand about it at all. The camera is well back. Every figure has "
            "two arms, two hands and one head."
            " THE CAMERA STANDS FAR BACK ON THE ROAD BEHIND THE THREE AND SHOOTS PAST THEM: all three are seen from behind walking away from the lens into the low warm light, their backs to the camera and their long shadows thrown toward it, and NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a wide prime, deep focus, real film grain, one photograph."
        ),
    },
    {
        "id": "v2-r018-b39", "out": "s39-walking-with-you.jpeg", "seg": "n10 p5",
        "window": "228.25-232.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD", "OUTBOUND"],
        "narration": ("He is still in the habit of walking with the ones who have lost "
                      "hope."),
        "must_show": "Jesus alone on the open road, mid-stride and unhurried, still going \u2014 an ordinary man still walking, which is the whole closing thought.",
        "must_not_show": "no halo, glow or rim-light; no crowd, no throne, nothing grand; he is not posed and not standing still.",
        "scene": (
            "Jesus walks alone along the pale country road in the last warm light of "
            "the afternoon, caught mid-stride with the dust lifting off his sandals and "
            "his mantle moving. The olive terraces and the low hills open away on both "
            "sides and the road runs on ahead of him out of the frame. His face is "
            "plainly visible in three-quarter, turned a little toward the empty road "
            "ahead. There is nothing grand about the picture at all \u2014 a man on a road, "
            "still going. Every figure has two arms, two hands and one head."
            " THE CAMERA STANDS AT THE ROADSIDE AND SHOOTS ACROSS HIM in profile as he passes, so he moves from one side of the frame to the other and his eyeline runs across the picture and out past its far edge. NOT ONE FACE IS TURNED TOWARD THE LENS. Shot on a 50mm prime, shallow depth of field, real film grain, one photograph."
        ),
    },
]
