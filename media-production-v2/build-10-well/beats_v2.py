#!/usr/bin/env python3
"""V2 beat map — row 10, build-10-well (John 4:1-42).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 48 pictures against V1's 9 unique stills, over
282.4 s — the longest row in the queue so far, at 5.9 s per picture, the same
band as rows 5-9. It is a long CONVERSATION, so the risk here is the opposite of
row 7's: not too many events, but two people standing at a well for four and a
half minutes. Every frame therefore has to move something — the distance between
them, where she is looking, whether she is still holding the jar.

⚠️ THIS ROW HAS A SPEAKER V1 DID NOT: the audio carries a WOMAN voice (w9, w11,
w15, w19, w25, w29) as well as narrator and Jesus. Her six KJV lines are hers,
not the narrator's, and each one gets its own frame centred on HER.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (John 4 KJV):
  v6   "Jesus therefore, being WEARIED with his journey, SAT THUS ON THE WELL:
       and it was about the SIXTH HOUR" — noon. He is genuinely exhausted, dusty
       and sitting on the well stones, not standing in composed dignity.
  v7-9 "Give me to drink" — he opens by NEEDING something from her. Her reply
       names both walls at once: he is a Jew, she is a woman of Samaria.
  v8   "his disciples were gone away unto the city to buy meat" — they are
       ABSENT for the whole conversation and return only at v27. No disciple
       appears in any frame from b07 to b43.
  v11  "thou hast NOTHING TO DRAW WITH, and the well is DEEP" — she is being
       practical, not hostile. He has no rope and no bucket, and b19 shows that.
  v12  "Art thou greater than our father Jacob?" — the well is Jacob's, ancient,
       its stone rim cut with centuries of rope grooves.
  v16-18 five husbands, and the man she has now is not her husband. He says it
       gently and does not look away — b33 is the frame that whole exchange
       exists for.
  v20  the mountain question: Gerizim, which STANDS RIGHT THERE behind the well
       and is visible in the wide frames.
  v26  "I that speak unto thee am he." The first plain declaration in John, made
       to her.
  v27  the disciples "MARVELLED that he talked with the woman: yet no man said..."
  v28  "The woman then LEFT HER WATERPOT" — the detail the narration builds to.
  v39-40 many believed because of her word; he abode two days.

CONTENT-CARE: row 10 is not in the §3 flag table = GREEN. Her marital history is
central and is handled the way the text handles it — stated plainly once, never
leered at, never illustrated. There is no depiction of any husband, no bedroom,
no implication of her trade or shame beyond averted eyes in a doorway. b05 shows
the town's whispering, not her past.

TIME OF DAY: NOON — "the sixth hour" — for everything at the well. Hard sun
almost straight overhead, very short shadows pooled directly under people, heat
shimmer off the ground, bleached washed-out light, an empty landscape. That
emptiness is the POINT: she chose the hour with nobody in it. The one deliberate
exception is b02, which shows the cool of the MORNING as the contrast the
narration explicitly draws. The last three frames move to late afternoon as the
town comes out and he stays — the narration takes it there ("by sundown").
"""

LOCKS = {
    "WOMAN": (
        "SAMARITAN WOMAN LOCK: the woman is the same person in every shot — a "
        "Samaritan woman of about thirty-five, warm olive-brown skin, a strong "
        "handsome tired face with fine lines at the eyes, dark arched brows, and "
        "watchful guarded dark eyes. Her dark hair is bound back under a faded "
        "DUSTY-OCHRE headcloth. She wears a worn DEEP TERRACOTTA-RED wool robe with "
        "a plain woven sash and old leather sandals (never cream, never white). She "
        "carries a large rounded clay water jar. Her face is shown clearly."
    ),
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect).
    "WELL": (
        "WELL LOCK: Jacob's well in the open country outside the town — an ancient "
        "round stone well head with a massive worn curb, its rim cut with deep "
        "grooves worn by centuries of rope, a long hollowed stone trough beside it, "
        "and one old olive tree throwing a small hard patch of shade. A dusty road "
        "runs past. The broad flank of Mount Gerizim rises close behind, and dry "
        "summer fields and stony ground stretch away on every side. IT IS NOON: the "
        "sun is almost straight overhead, shadows are very short and pooled directly "
        "under things, the light is hard and bleached, and heat shimmers off the "
        "stony ground. The landscape is empty."
    ),
    "TOWN": (
        "TOWN LOCK: the Samaritan town of Sychar — flat-roofed houses of rough "
        "honey-coloured stone crowded along narrow lanes, a low arched gateway, a "
        "small square with an old fig tree and a stone cistern, dry hills beyond. The "
        "townspeople are ordinary Samaritan villagers of every age in SATURATED DEEP "
        "earth colours — dark chocolate brown, deep russet, burnt ochre, dark olive, "
        "dusty indigo and faded plum wool. No villager wears off-white, ivory or any "
        "near-white cloth."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the disciples are the same group throughout — eight or nine "
        "working Galilean men between twenty and forty, dusty from the road, carrying "
        "bread, a basket of provisions and travel bags. They wear wool tunics in "
        "SATURATED DEEP colours — rust-brown, deep russet, dark olive, blue-grey and "
        "dusty indigo — belted with rope or leather. None of them wears off-white, "
        "ivory or any near-white cloth. Their faces are shown clearly."
    ),
}

REF = True

BEATS = [
    # -------------------------------------------------- n0 — the noon hour ----
    {
        "id": "v2-r010-b01", "out": "s01-a-woman-at-noon.jpeg", "seg": "n0 p1",
        "window": "0.28-5.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "WELL"],
        "narration": ("A woman walked out to a well at noon — the hottest, emptiest "
                      "hour of the day."),
        "must_show": "one woman alone on a dusty road under a straight-overhead sun, jar on her shoulder, and an entirely empty landscape around her.",
        "must_not_show": "nobody else anywhere in the frame; no long shadows — the shadow must be a short pool directly under her.",
        "scene": (
            "A single woman walks the dusty road out of town toward the well, her "
            "large clay jar balanced on one shoulder and steadied with a raised hand. "
            "The sun is almost straight overhead and her shadow is a short dark pool "
            "directly beneath her feet. The light is hard and bleached, heat shimmers "
            "off the stony ground, and the dry fields stretch away completely empty in "
            "every direction with Mount Gerizim standing behind. There is no other "
            "person anywhere. The camera is back far enough to see her head to sandals "
            "against the emptiness. She has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b02", "out": "s02-the-cool-of-the-morning.jpeg", "seg": "n0 p2-p3",
        "window": "5.30-12.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["WELL", "TOWN"],
        "narration": ("You need to understand what that hour means. Women drew their "
                      "water in the cool of the morning, together."),
        "must_show": "THE CONTRAST FRAME — the same well in the cool early morning, busy with a dozen women drawing water together, talking and laughing.",
        "must_not_show": "she is NOT in this frame; this is how the well looks when she is not there. NOTE: early-morning light is deliberate here and is not a time-of-day defect.",
        "scene": (
            "The same well in the cool early morning, long soft golden light and long "
            "shadows lying sideways across the ground. A dozen women of the town are "
            "crowded around the well head — one hauling the rope hand over hand, two "
            "steadying jars on the stone curb, others standing in twos and threes with "
            "their jars on their hips, heads together, talking and laughing. Children "
            "play at the edge of the group. It is busy, easy and companionable. The "
            "camera is back far enough to hold the whole gathering head to sandals. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b03", "out": "s03-where-the-talk-happened.jpeg", "seg": "n0 p4",
        "window": "12.07-14.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["WELL"],
        "narration": "It was where the talk happened.",
        "must_show": "close on three of the morning women with their heads together — one talking behind her hand, another's eyebrows going up, the third glancing off to the side.",
        "must_not_show": "not cartoonish gossip faces; ordinary women doing an ordinary human thing that happens to be lethal to somebody.",
        "scene": (
            "Close on three women at the morning well with their heads inclined "
            "together over their jars. One is speaking low with her hand half raised "
            "toward her mouth, another has her brows up and her lips parted in a small "
            "shocked smile, and the third has her eyes cut away sideways down the road "
            "at something out of frame. Soft early light on their faces. It is warm, "
            "ordinary, everyday talk. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r010-b04", "out": "s04-she-came-at-noon.jpeg", "seg": "n0 p5",
        "window": "14.09-16.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "WELL"],
        "narration": "She came at noon because of the talk.",
        "must_show": "close on her face on the noon road — set, closed, carrying it; a woman who has worked out exactly what hour costs her the least.",
        "must_not_show": "not weeping and not self-pitying — this is a practical arrangement she made with her own life.",
        "scene": (
            "Close on the woman's face and shoulders as she walks the noon road, the "
            "clay jar against her shoulder. Her expression is set and closed — jaw "
            "firm, eyes fixed ahead on the road and not on anything else, a face that "
            "long ago stopped expecting company. Sweat on her temple, dust on her "
            "cheek, hard white noon light straight down on her. The empty bleached "
            "fields are soft behind her."
        ),
    },
    {
        "id": "v2-r010-b05", "out": "s05-the-whole-town-knew.jpeg", "seg": "n0 p6",
        "window": "16.50-23.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TOWN"],
        "narration": ("Five marriages behind her, living now with a man who wasn't her "
                      "husband — and the whole town knew every chapter."),
        "must_show": "her walking out through the town lane with her jar while women in doorways watch her go — eyes following, a head turning aside, one saying something to another.",
        "must_not_show": "CONTENT-CARE — nothing of her past is depicted: no husband, no house, no bedroom, nothing suggestive. The cost is carried entirely by the watching eyes.",
        "scene": (
            "The woman walks out along the narrow town lane with her jar on her "
            "shoulder and her eyes fixed straight down the road ahead of her. In the "
            "doorways and at the windows on both sides, women of the town watch her "
            "pass — one has stopped grinding to follow her with her eyes, two "
            "standing together have gone quiet and turned their heads to track her, "
            "one leans to say something to the woman beside her. Nobody speaks to her. "
            "Hard noon light in the lane. The camera is back far enough to hold her "
            "and the watching doorways in one frame. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r010-b06", "out": "s06-the-hour-with-nobody-in-it.jpeg", "seg": "n0 p7-p8",
        "window": "23.80-27.71", "wide": True, "jesus": False, "ref": False,
        "locks": ["WELL"],
        "narration": "Noon was the hour with nobody in it. She chose it on purpose.",
        "must_show": "the well at noon, completely deserted — bleached stone, heat shimmer, not one person anywhere.",
        "must_not_show": "not one human figure in this frame, not even distant; the emptiness is the entire picture.",
        "scene": (
            "The well head stands alone in the glare of noon with not a single person "
            "anywhere in the frame. The massive stone curb is bleached white in the "
            "overhead sun, its rope grooves cut black with shadow, and the small hard "
            "patch of shade under the old olive tree is empty. Heat shimmers off the "
            "stony ground and the dry fields run away empty to the flank of Mount "
            "Gerizim. Nothing moves. There is no one here."
        ),
    },
    # ------------------------------------------------- n1 — the traveler ----
    {
        "id": "v2-r010-b07", "out": "s07-somebody-was-there.jpeg", "seg": "n1 p1",
        "window": "28.29-30.61", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "WELL"],
        "narration": "But this day, somebody was there.",
        "must_show": "her stopping on the rise as she catches sight of a seated figure at the well ahead — the figure small and distant, her body checking mid-step.",
        "must_not_show": "his face is not readable at this distance; do not attach a Jesus lock or ref to this beat.",
        "scene": (
            "The woman has come over a low rise in the road and stopped mid-step, her "
            "free hand still on the jar at her shoulder, her weight caught back. Ahead "
            "of her down the slope the well head stands in the glare, and on its stone "
            "curb sits a single seated figure, small with distance and too far off for "
            "his face to be made out. Her whole posture has checked. Hard noon light, "
            "very short shadows, the empty fields around. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b08", "out": "s08-worn-out-from-the-road.jpeg", "seg": "n1 p2",
        "window": "30.61-36.67", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WELL"],
        "narration": ("A traveler sat by the well, worn out from the road — a Jewish "
                      "man, resting in Samaria."),
        "must_show": "GENUINE EXHAUSTION: Jesus sitting slumped on the stone curb of the well in the noon heat, dusty, sweating, forearms on his knees — a tired man at the end of a long walk.",
        "must_not_show": "no halo, glare or rim-light; he is NOT composed, upright and dignified here — v6 says he was wearied, and the frame has to look it. Nobody else is present.",
        "scene": (
            "Jesus sits on the massive stone curb of the well in the full noon heat, "
            "worn out. His shoulders are down, his forearms rest across his knees with "
            "his hands hanging loose between them, and his head is tipped slightly "
            "back against the heat. His cream robe is grey with road dust to the knee, "
            "his hair is damp at the temples and his face is sheened with sweat. His "
            "travel bag is dropped on the stones beside him. He is entirely alone in "
            "the empty bleached landscape and there is no rope or bucket anywhere near "
            "him. The camera is back far enough to see him head to sandals. He has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b09", "out": "s09-seven-hundred-years.jpeg", "seg": "n1 p3-p4",
        "window": "36.67-44.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("That detail matters more than it sounds. Jews and Samaritans "
                      "had despised each other for seven hundred years."),
        "must_show": "her face changing as she takes in what he is — recognition, then a cold wary shutting-down.",
        "must_not_show": "not hatred and not fear exactly — the guarded look of someone who has learned what this kind of encounter costs; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman's face as she looks down the slope at the seated "
            "stranger. Recognition moves across it and then closes it — her eyes "
            "narrow slightly against the glare, her chin comes back, and her whole "
            "expression shutters into a flat wariness. Her hand has tightened on the "
            "rim of the jar at her shoulder. Hard noon light straight down on her, the "
            "bleached empty ground soft behind."
        ),
    },
    {
        "id": "v2-r010-b10", "out": "s10-everything-said-turn-around.jpeg", "seg": "n1 p5-p6",
        "window": "44.28-54.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": ("They didn't share roads if they could help it, didn't share "
                      "tables, and certainly didn't share water. Everything in her "
                      "body said: turn around."),
        "must_show": "THE GAP: a wide frame with her stopped on the road at one side and him seated at the well on the other, a long stretch of hard sunlit empty ground between them — and her shoulders already half turned back the way she came.",
        "must_not_show": "no halo, glare or rim-light; they are NOT close together yet — the distance between them is the picture, and it is the seven hundred years.",
        "scene": (
            "A wide view holding both of them with a long stretch of bleached stony "
            "ground between. On one side of the frame the woman stands checked on the "
            "road with her jar, her feet still pointed forward but her shoulders and "
            "head already turning back toward the town, on the very edge of leaving. "
            "On the other side Jesus sits slumped and dusty on the well curb, not "
            "moving. Neither has closed any of the distance. The empty road, the heat "
            "shimmer and Mount Gerizim behind. The camera is back far enough to hold "
            "both figures head to sandals. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    # ------------------------------------------------- n2 — he speaks first ----
    {
        "id": "v2-r010-b11", "out": "s11-he-asked-her-for-a-drink.jpeg", "seg": "n2 p1-p2",
        "window": "54.82-57.72", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": "Then he spoke to her. He asked her for a drink.",
        "must_show": "Jesus lifting his head and speaking to her across the ground, one hand come open toward the well — asking for something, not offering.",
        "must_not_show": "no halo, glare or rim-light; his posture must read as a REQUEST from a tired man, never as a teacher summoning someone.",
        "scene": (
            "Jesus has lifted his head from his hands and is speaking across the open "
            "ground toward the woman, one dusty hand come open and turned up toward "
            "the mouth of the well beside him — a plain request. He is still seated on "
            "the curb, still slumped and tired, asking a favour from a stranger. She "
            "stands out on the road holding her jar, arrested mid-turn, staring at "
            "him. Hard noon light. The camera is back far enough to hold both of them "
            "head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b12", "out": "s12-how-impossible.jpeg", "seg": "n2 p3-p4",
        "window": "57.72-66.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("Understand how impossible that sentence was. A rabbi did not "
                      "speak to an unknown woman in public — and no Jew asked a "
                      "Samaritan for anything."),
        "must_show": "close on her face, completely thrown — brows up, lips parted, the wariness knocked sideways by something that simply does not happen.",
        "must_not_show": "not fear and not offence — pure disbelief; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman's face. The guarded flatness has been knocked "
            "straight off it — her brows have gone up, her lips have parted, and her "
            "eyes are fixed on the man out of frame with plain uncomprehending "
            "astonishment. Her head has come forward slightly, as if to check she "
            "heard it. The jar is still up on her shoulder, forgotten. Hard noon light "
            "on her face and the bleached ground soft behind."
        ),
    },
    {
        "id": "v2-r010-b13", "out": "s13-he-needed-her-help.jpeg", "seg": "n2 p5",
        "window": "66.57-70.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WELL"],
        "narration": ("He broke both walls at once, and he did it by needing her help."),
        "must_show": "close on Jesus — the ask is genuine, he is actually thirsty, and his open empty hands prove he has nothing to draw with.",
        "must_not_show": "no halo, glare or rim-light; no strategy or cleverness on his face — he really does want the water.",
        "scene": (
            "Close on Jesus seated on the well curb, looking up and out of frame at "
            "her. His face is plain and tired and openly asking — cracked dry lips, "
            "sweat at his hairline, no cleverness or strategy anywhere in the "
            "expression. Both his hands have turned open and empty in his lap, showing "
            "he has no rope, no bucket and no means of getting anything out of the "
            "well himself. The bleached stone and hard noon light are around him. Each "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r010-b14", "out": "s14-she-almost-laughed.jpeg", "seg": "n2 p6-p7",
        "window": "70.55-74.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("She almost laughed. How is it that you, a Jew, would ask me for "
                      "water?"),
        "must_show": "a startled half-laugh breaking across her face — the first crack in the guard, disbelief turning into something almost amused.",
        "must_not_show": "not mockery and not bitterness — this is the moment she stops being purely defensive; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman as a startled breath of a laugh breaks across her "
            "face — one corner of her mouth pulled up, her head tipped back and to the "
            "side, her eyebrows high, caught between disbelief and genuine amusement. "
            "It is the first crack in her guard and it has surprised her as much as "
            "him. She has shifted the jar down off her shoulder onto her hip. Hard "
            "noon light, the empty ground behind."
        ),
    },
    {
        "id": "v2-r010-b15", "out": "s15-living-water-offered.jpeg", "seg": "n2 p8",
        "window": "74.91-82.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": ("And he answered that if she knew who was asking, she would have "
                      "asked him — and he would have given her living water."),
        "must_show": "she has come closer — the gap from b10 visibly shorter — and he is speaking with an open hand, the conversation now genuinely underway.",
        "must_not_show": "no halo, glare or rim-light; nothing supernatural about the water or the well; she has not set the jar down yet.",
        "scene": (
            "The woman has come down off the road and is standing near the well now, "
            "the jar held down against her hip, plainly closer than she was — the open "
            "ground between them nearly gone. Jesus, still seated on the curb, is "
            "speaking up to her with one hand open and turned over, offering "
            "something. Her head is tilted, listening in spite of herself. Hard noon "
            "light, short shadows, the olive tree and Gerizim behind. The camera is "
            "back far enough to hold both head to sandals. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b16", "out": "s16-a-woman-of-samaria.jpeg", "seg": "w9",
        "window": "82.82-88.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("How is it that thou, being a Jew, askest drink of me, which am "
                      "a woman of Samaria? (John 4:9)"),
        "must_show": "close on her asking it — one hand turned up and out in a plain 'look at me' gesture, naming what she is.",
        "must_not_show": "no shame in the gesture — it is challenge and honesty, not apology; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman speaking, her free hand turned palm-up and opened out "
            "toward her own chest in a plain gesture — look at what I am. Her eyebrows "
            "are raised and her mouth is mid-word, her expression direct and a little "
            "challenging, not ashamed. The clay jar rests against her hip in her other "
            "arm. Hard noon light across her face. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r010-b17", "out": "s17-the-well-is-deep.jpeg", "seg": "w11",
        "window": "89.52-96.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "WELL"],
        "narration": ("Sir, thou hast nothing to draw with, and the well is deep: from "
                      "whence then hast thou that living water? (John 4:11)"),
        "must_show": "her leaning over the well mouth and gesturing down into it — the dark shaft dropping away out of sight, and no rope or bucket anywhere near him.",
        "must_not_show": "she is being practical, not sarcastic; do not put Jesus in this frame.",
        "scene": (
            "The woman leans one hand on the massive stone curb and gestures down into "
            "the mouth of the well with the other, mid-sentence. Below her hand the "
            "shaft drops away into complete blackness, its stone throat vanishing out "
            "of sight, and the worn rope grooves are cut deep into the rim under her "
            "palm. Her expression is practical and reasonable — she is pointing out a "
            "fact. There is no rope, no bucket and no vessel anywhere on the stones. "
            "Hard noon light on the bleached curb. Each hand has five fingers."
        ),
    },
    # ------------------------------------------------ n3 — greater than Jacob ----
    {
        "id": "v2-r010-b18", "out": "s18-jacobs-well.jpeg", "seg": "n3 p1-p2",
        "window": "97.84-105.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["WELL"],
        "narration": ("She pointed out the obvious — the well is deep, sir, and you "
                      "don't even have a rope. This well came from Jacob himself."),
        "must_show": "the WELL ITSELF as the oldest thing in the frame — the massive curb worn into deep smooth rope grooves by centuries of hands.",
        "must_not_show": "no people needed in this frame; the age of the stone is the whole picture.",
        "scene": (
            "Very close on the ancient stone curb of the well in hard noon light. The "
            "limestone is worn glassy-smooth along its top edge and cut with deep "
            "rounded grooves where uncountable ropes have sawed into it over "
            "centuries, each groove filled with hard black shadow. Dust and a few "
            "scraps of old rope fibre lie in the cracks, and beyond the rim the "
            "blackness of the shaft drops away. Nothing else is in the frame."
        ),
    },
    {
        "id": "v2-r010-b19", "out": "s19-are-you-greater.jpeg", "seg": "n3 p3-p4",
        "window": "105.64-109.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "Are you greater than Jacob? She meant it as a corner.",
        "must_show": "her chin up, one brow raised, testing him — a woman who has put a question in front of someone to see what he does with it.",
        "must_not_show": "not hostile — sharp and clever; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman with her chin lifted and her head angled, one eyebrow "
            "raised and the corner of her mouth just curling — an intelligent, testing "
            "look put deliberately in front of someone to see how he answers it. Her "
            "free hand rests on the stone curb. Hard noon light on her face, the "
            "bleached ground soft behind."
        ),
    },
    {
        "id": "v2-r010-b20", "out": "s20-he-stepped-into-it.jpeg", "seg": "n3 p5",
        "window": "109.09-110.74", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WELL"],
        "narration": "He stepped right into it.",
        "must_show": "Jesus leaning forward off the curb toward the question, entirely unbothered, the beginnings of a smile — a man walking straight into the trap on purpose.",
        "must_not_show": "no halo, glare or rim-light; no smugness — warmth and interest.",
        "scene": (
            "Close on Jesus leaning forward off the well curb, elbows coming onto his "
            "knees, his head coming up toward her question. His tired face has woken "
            "up — his eyes are steady on hers and there is the beginning of a warm "
            "amused smile at the corner of his mouth, entirely unbothered by what she "
            "has just put in front of him. Hard noon light and the bleached stone "
            "around him."
        ),
    },
    # ------------------------------------------------------ j1 — living water ----
    {
        "id": "v2-r010-b21", "out": "s21-shall-thirst-again.jpeg", "seg": "j1 a",
        "window": "111.28-116.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": ("Whosoever drinketh of this water shall thirst again: (John 4:13)"),
        "must_show": "Jesus indicating the well and her jar as he says it — this water, the one she carries a jar for.",
        "must_not_show": "no halo, glare or rim-light; nothing supernatural in or above the well.",
        "scene": (
            "Jesus, still seated on the curb, has turned his open hand toward the "
            "mouth of the well and the clay jar the woman is holding, indicating them "
            "both as he speaks. She stands close by the stones now, listening, the jar "
            "in both arms. Hard noon light, very short shadows, the olive tree and the "
            "flank of Gerizim behind. The camera is back far enough to hold both head "
            "to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b22", "out": "s22-shall-never-thirst.jpeg", "seg": "j1 b",
        "window": "116.0-121.0", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("But whosoever drinketh of the water that I shall give him shall "
                      "never thirst; (John 4:14)"),
        "must_show": "close on Jesus saying it — quiet, certain, entirely serious, looking straight at her.",
        "must_not_show": "no halo, glare or rim-light; no grand oratory — this is said quietly to one person.",
        "scene": (
            "Close on Jesus's face and shoulders in the hard noon light, speaking "
            "quietly and directly to the person standing over him. His dusty face is "
            "completely serious, his eyes steady and certain, his voice plainly low — "
            "a man telling one person something enormous without raising his voice at "
            "all. His hand has come up open between them. The bleached stone of the "
            "well is soft behind him."
        ),
    },
    {
        "id": "v2-r010-b23", "out": "s23-springing-up.jpeg", "seg": "j1 c",
        "window": "121.0-125.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("but the water that I shall give him shall be in him a well of "
                      "water springing up into everlasting life. (John 4:14)"),
        "must_show": "her face as the image lands — brows drawn, eyes searching his, working to follow something just past her reach.",
        "must_not_show": "do NOT paint a spring, a fountain, light, or any supernatural water — the picture stays on her face; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman's face as she works at what she has just heard. Her "
            "brows have drawn together, her eyes are moving over the face of the man "
            "in front of her, and her lips are slightly parted — following something "
            "that is just past where she can reach, and wanting it. The jar has come "
            "down and is resting against her body, no longer being carried anywhere. "
            "Hard noon light, the empty ground behind."
        ),
    },
    # ---------------------------------------------- n4 — the thirst underneath ----
    {
        "id": "v2-r010-b24", "out": "s24-not-the-water-in-the-jar.jpeg", "seg": "n4 p1-p2",
        "window": "126.70-132.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "WELL"],
        "narration": ("A well inside you — springing up, not running dry. He wasn't "
                      "talking about the water in the jar."),
        "must_show": "the clay jar set down on the stones and forgotten, still empty, with her feet beside it — she came here for this and has stopped thinking about it.",
        "must_not_show": "the jar must be plainly EMPTY and plainly abandoned mid-errand; no faces needed.",
        "scene": (
            "Close and low on the big rounded clay jar standing on the bleached stones "
            "beside the well where she has set it down, tipped slightly against the "
            "curb, its wide mouth open and completely dry inside. Her sandalled feet "
            "and the dusty hem of her terracotta robe are just beside it, turned away "
            "toward the well. The rope grooves and the hard short shadows of noon are "
            "around them. The errand she walked out here in the heat to do has "
            "stopped."
        ),
    },
    {
        "id": "v2-r010-b25", "out": "s25-the-thirst-underneath.jpeg", "seg": "n4 p3-p4",
        "window": "132.43-138.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("He was talking about the thirst underneath the thirst. The one "
                      "you can't carry a jar big enough for."),
        "must_show": "close on her face with the guard fully down for the first time — something old and tired and wanting showing through.",
        "must_not_show": "no tears yet; this is quieter than that; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman's face with the defences finally down. Her eyes have "
            "gone unfocused and slightly wide, her mouth has softened out of its set "
            "line, and something very old and very tired is showing through the "
            "weathered face — a want she stopped naming a long time ago. She is "
            "completely still. Hard noon light on her skin, the bleached empty land "
            "soft behind her."
        ),
    },
    {
        "id": "v2-r010-b26", "out": "s26-give-me-this-water.jpeg", "seg": "w15",
        "window": "138.93-143.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("Sir, give me this water, that I thirst not, neither come hither "
                      "to draw. (John 4:15)"),
        "must_show": "her asking — leaning in, both hands come open toward him, the first thing she has genuinely wanted out loud in this conversation.",
        "must_not_show": "no sarcasm left in the face at all; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman leaning down and in toward the seated man, both thin "
            "hands come open and forward in front of her. Her face is entirely without "
            "guard now — eyebrows lifted in the middle, eyes fixed and asking, her "
            "mouth mid-word. It is a plain, undefended request. Hard noon light across "
            "her. Each hand has five fingers."
        ),
    },
    # ---------------------------------------------------- n5 — fully known ----
    {
        "id": "v2-r010-b27", "out": "s27-go-get-your-husband.jpeg", "seg": "n5 p1-p2",
        "window": "145.31-149.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": ("Then he said: go get your husband. And the whole conversation "
                      "changed.",),
        "must_show": "the simple question asked, and the temperature of the scene dropping — his face open and easy, hers going instantly still.",
        "must_not_show": "no halo, glare or rim-light; there must be NO trap or knowingness on his face — he asks it as simply as asking directions.",
        "scene": (
            "Jesus, seated on the curb, has asked something simple, one hand still "
            "loose and open, his face easy and unremarkable. Standing over him the "
            "woman has gone completely still — her forward lean arrested, her open "
            "hands stopped in the air, her face frozen between the question she was "
            "asking and the one she has just been asked. Nothing else in the frame has "
            "moved. Hard noon light, short shadows. The camera holds both of them head "
            "to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b28", "out": "s28-i-have-no-husband.jpeg", "seg": "n5 p3",
        "window": "149.76-151.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "I have no husband, she said.",
        "must_show": "close on her giving the short careful answer — eyes gone sideways off his face, chin down, the guard slamming back up.",
        "must_not_show": "she is not lying and does not look like a liar — she is giving the smallest true answer she can; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman answering. Her eyes have cut away off the man's face "
            "to the stones at her feet, her chin has come down and her mouth has "
            "closed into a short careful line. Every bit of the openness from a moment "
            "ago has gone back behind the guard. She has straightened up and away from "
            "him slightly. Hard noon light, the bleached ground soft behind her."
        ),
    },
    {
        "id": "v2-r010-b29", "out": "s29-five-husbands.jpeg", "seg": "n5 p4-p6",
        "window": "151.56-158.45", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("And he agreed with her — gently, and completely. Five husbands, "
                      "he said. And the man you have now is not one."),
        "must_show": "close on Jesus saying the hardest facts of her life — and the face saying them is GENTLE, with no accusation anywhere in it.",
        "must_not_show": "NOT stern, NOT triumphant, NOT pitying, NOT a gotcha. If this face reads as an accusation the whole story breaks. No halo, glare or rim-light.",
        "scene": (
            "Close on Jesus's face as he speaks. His expression is careful and gentle "
            "and completely level — his eyes are soft and steady on hers, his brows "
            "slightly raised in the middle, his mouth quiet between the words. There "
            "is no accusation, no triumph and no pity anywhere in it; he is saying "
            "something true about someone's life the way you would to a person you "
            "respect. Hard noon light on his dusty face, the stone soft behind him."
        ),
    },
    {
        "id": "v2-r010-b30", "out": "s30-he-already-knew.jpeg", "seg": "n5 p7-p9",
        "window": "158.45-164.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("He already knew. All of it. Every chapter the town whispered "
                      "about — he said it out loud, to her face."),
        "must_show": "her face completely exposed — stripped, braced, waiting for the disgust she has met a hundred times before.",
        "must_not_show": "no tears yet; this is the flinch before the blow that does not come; do not put Jesus in this frame.",
        "scene": (
            "Very close on the woman's face, laid completely bare. Her eyes have come "
            "back up to his and gone wide and glassy, her lips have parted, and her "
            "whole body has braced — shoulders drawn up and back, one hand come "
            "half-way to her chest. It is the face of someone waiting for the "
            "expression she has seen on every other face that ever learned this about "
            "her. Hard noon light with nowhere to hide in it."
        ),
    },
    {
        "id": "v2-r010-b31", "out": "s31-he-did-not-turn-away.jpeg", "seg": "n5 p10-p11",
        "window": "164.90-168.44", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "And he did not turn away. He stayed in the conversation.",
        "must_show": "⚠️ THE FRAME THE WHOLE EXCHANGE EXISTS FOR. Jesus still looking straight at her, unchanged — no recoil, no shift, nothing withdrawn.",
        "must_not_show": "he must NOT look away, lean back, harden, or soften into pity. He simply stays. If anything in his face has changed since b29, regenerate. No halo, glare or rim-light.",
        "scene": (
            "Close on Jesus's face, holding exactly where it was. His eyes are still "
            "level on hers, warm and completely steady, and he has not leaned back or "
            "turned a degree away — his head is still inclined toward her, his hands "
            "still open, his expression unchanged by anything he just said. There is "
            "no recoil in it and no pity either. He is simply still there, still "
            "listening, waiting for her to speak next. Hard noon light on his face."
        ),
    },
    {
        "id": "v2-r010-b32", "out": "s32-fully-known.jpeg", "seg": "n5 p12",
        "window": "168.44-173.92", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": ("She came for water, and found herself fully known — and still "
                      "spoken to with respect."),
        "must_show": "the two of them still together at the well, the conversation plainly continuing — nobody has walked away, and the empty jar sits forgotten on the stones.",
        "must_not_show": "no halo, glare or rim-light; she is not kneeling, cowering or being forgiven — she is standing in a conversation as an equal.",
        "scene": (
            "A wide view of the two of them at the well in the noon glare. The woman "
            "stands close to the stone curb, upright and steady, her arms loose at her "
            "sides; Jesus sits on the curb looking up at her, one hand open. Neither "
            "has moved away from the other. The forgotten clay jar leans empty against "
            "the stones between them. The olive tree, the empty road and the flank of "
            "Mount Gerizim stand around them and there is nobody else anywhere. The "
            "camera is back far enough to see both head to sandals. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b33", "out": "s33-thou-art-a-prophet.jpeg", "seg": "w19",
        "window": "174.47-177.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "Sir, I perceive that thou art a prophet. (John 4:19)",
        "must_show": "close on her saying it — the wariness entirely gone, replaced by careful, dawning recognition.",
        "must_not_show": "no fear and no flattery — she is working something out in front of him; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman speaking. Her head has come slightly to one side and "
            "her eyes have narrowed a little in concentration, moving over the face in "
            "front of her; her mouth is mid-word and her expression is careful and "
            "arriving at something. There is no fear left in it at all. Hard noon "
            "light across her weathered face."
        ),
    },
    # ------------------------------------------------- n6 — which mountain ----
    {
        "id": "v2-r010-b34", "out": "s34-which-mountain.jpeg", "seg": "n6 p1-p2a",
        "window": "178.68-187.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": ("She called him a prophet. She asked him her people's oldest "
                      "question — which mountain is the right one to worship on —"),
        "must_show": "her turning and gesturing up at the flank of MOUNT GERIZIM standing right there behind the well, asking the old question with the mountain itself in frame.",
        "must_not_show": "no halo, glare or rim-light; the mountain must be plainly the thing she is pointing at.",
        "scene": (
            "The woman has half turned away from the well and is gesturing up and back "
            "with one arm at the great dry flank of Mount Gerizim, which rises close "
            "behind them and fills the upper part of the frame, its terraced slopes "
            "bleached in the noon sun. She is looking back over her shoulder at Jesus "
            "as she points, asking. He sits on the curb watching her, listening. Hard "
            "overhead light and short shadows. The camera is back far enough to hold "
            "both figures and the mountain. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r010-b35", "out": "s35-god-is-spirit.jpeg", "seg": "n6 p2b",
        "window": "187.0-194.35", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("and he told her the day was coming when the question itself "
                      "would be old news: God is spirit, and what he wants is the "
                      "heart."),
        "must_show": "Jesus answering — one hand open and unhurried, his face warm, setting a centuries-old argument gently aside.",
        "must_not_show": "do NOT depict God, spirit, light from the sky, or anything supernatural — the frame stays on a man talking. No halo, glare or rim-light.",
        "scene": (
            "Close on Jesus seated on the well curb, speaking with one dusty hand "
            "turned open and lifted slightly, his other resting on the stone. His face "
            "is warm and unhurried and slightly tilted up toward her, entirely "
            "untroubled — a man setting a seven-hundred-year argument gently to one "
            "side. There is nothing in the sky and nothing in the air. Hard noon light "
            "on his face and the bleached stone behind him."
        ),
    },
    {
        "id": "v2-r010-b36", "out": "s36-when-he-comes.jpeg", "seg": "n6 p3-p4",
        "window": "194.35-201.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("Then she said, almost to herself: When he comes, he'll explain "
                      "everything. And the tired traveler at the well said:"),
        "must_show": "her looking off and away as she says it, almost to herself — the hope of her whole people said out loud without expecting anything.",
        "must_not_show": "she is NOT looking at him when she says this; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman looking away out over the bleached empty fields, not "
            "at the man beside her. Her eyes are distant and her mouth is moving on "
            "the words almost silently, her hands come together in front of her — "
            "someone saying the oldest hope she has out loud without expecting "
            "anything to come of it. Hard noon light on her profile, the dry land and "
            "heat shimmer beyond."
        ),
    },
    {
        "id": "v2-r010-b37", "out": "s37-i-know-that-messiah-cometh.jpeg", "seg": "w25",
        "window": "202.32-208.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("I know that Messiah cometh, which is called Christ: when he is "
                      "come, he will tell us all things. (John 4:25)"),
        "must_show": "close on her face saying it — quiet certainty about a thing she has believed her whole life and never expected to see.",
        "must_not_show": "no drama; this is a plain, worn, held belief; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman's face, still turned partly away, speaking quietly. "
            "Her expression is settled and certain in a worn, long-held way — the look "
            "of someone stating something she has believed since she was a child and "
            "has never once expected to live to see. Her eyes are steady on the far "
            "distance. Hard noon light across her."
        ),
    },
    {
        "id": "v2-r010-b38", "out": "s38-i-that-speak-unto-thee.jpeg", "seg": "j2",
        "window": "209.92-211.59", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "I that speak unto thee am he. (John 4:26)",
        "must_show": "⚠️ THE DECLARATION. Close on Jesus saying it — quiet, plain, certain, looking straight at her. The first time he says it plainly to anyone.",
        "must_not_show": "no halo, glare or rim-light; NO grandeur, no raised chin, no proclamation — it is said quietly by a dusty exhausted man sitting on a well. That contrast is the entire point.",
        "scene": (
            "Very close on Jesus's face, filling the frame, saying it. He is looking "
            "directly up at her, and his expression is completely quiet and completely "
            "certain — level eyes, an ordinary mouth, no lift of the chin and no "
            "performance of any kind. Sweat and road dust are still on his skin and "
            "his hair is damp at the temples. A dusty tired man on a stone well saying "
            "the largest sentence in the world in the plainest possible way. Hard noon "
            "light. Nothing else in the frame."
        ),
    },
    # ---------------------------------------------- n7 — the first to be told ----
    {
        "id": "v2-r010-b39", "out": "s39-the-first-person-told.jpeg", "seg": "n7 p1a",
        "window": "213.11-221.0", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("The first person Jesus ever told plainly that he was the "
                      "Messiah — not a king, not a priest, not even one of his twelve —"),
        "must_show": "her face receiving it — absolutely motionless, eyes enormous, everything arriving at once.",
        "must_not_show": "not collapsing and not shouting — utter stillness; do not put Jesus in this frame.",
        "scene": (
            "Very close on the woman's face, entirely motionless. Her eyes have gone "
            "wide and are fixed and brimming, her lips are parted with no sound coming "
            "out of them, and every line of her weathered face has gone slack with "
            "what she has just been handed. She has not moved a muscle. Hard noon "
            "light straight down on her, everything behind her burned out and soft."
        ),
    },
    {
        "id": "v2-r010-b40", "out": "s40-bottom-of-every-list.jpeg", "seg": "n7 p1b",
        "window": "221.0-227.98", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "WELL"],
        "narration": ("a Samaritan woman with five marriages behind her, at the bottom "
                      "of every list her world kept."),
        "must_show": "the two of them alone in an enormous empty landscape — one tired man on a well and one ordinary woman, and nobody else in the world present for it.",
        "must_not_show": "no halo, glare or rim-light; the emptiness and ordinariness are the point — no grandeur anywhere in the frame.",
        "scene": (
            "A wide view pulled well back. Two small figures at an old stone well in "
            "the middle of an enormous bleached empty country — a dusty man sitting on "
            "the curb and a woman standing beside it with her jar forgotten at her "
            "feet. The dry fields, the empty road and the great flank of Mount Gerizim "
            "surround them under a white noon sky, and there is not another living "
            "soul in any direction. Nothing about the scene looks important. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b41", "out": "s41-the-disciples-came-back.jpeg", "seg": "n7 p2-p3",
        "window": "227.98-237.25", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "DISCIPLES", "WELL"],
        "narration": ("Right then his followers came back from town, and stopped short "
                      "— stunned that he was talking with her at all. Nobody dared say "
                      "a word."),
        "must_show": "the disciples arriving up the road with the food and stopping dead in a clump — staring, mouths shut, nobody stepping forward and nobody speaking.",
        "must_not_show": "no halo, glare or rim-light; nobody confronts her or him — v27 says no man said a word, so no pointing and no talking.",
        "scene": (
            "The disciples have come up the road from town carrying bread and a basket "
            "of provisions and have stopped dead in a clump some way off, bunched "
            "together. Every one of them is staring at the well — one has halted "
            "mid-step with his foot still up, another's loaf has come down to his side "
            "forgotten, a third has turned to look at the man beside him with his "
            "eyebrows up. Not one of them is speaking or moving forward. At the well "
            "Jesus and the woman are still turned toward each other, undisturbed. Hard "
            "noon light. The camera is back far enough to hold the disciples and the "
            "well in one frame. Every figure has two arms, two hands and one head."
        ),
    },
    # ----------------------------------------------------- n8 — she runs ----
    {
        "id": "v2-r010-b42", "out": "s42-she-left-the-jar.jpeg", "seg": "n8 p1-p2",
        "window": "237.78-240.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "WELL"],
        "narration": "And look what she did. She left the jar.",
        "must_show": "her hands releasing the jar and leaving it on the stones — the moment of letting go of the thing she came for.",
        "must_not_show": "not dropping or breaking it — she sets it down and lets go; do not put Jesus in this frame.",
        "scene": (
            "Close on the woman's hands and the big clay jar. She has set it down onto "
            "the bleached stone beside the well and her fingers are just lifting away "
            "from its rim, still curved to the shape of it, leaving it standing there. "
            "The jar is empty and its mouth is open to the sky. Her terracotta sleeve "
            "and the dusty hem of her robe are already turning away out of frame. Each "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r010-b43", "out": "s43-and-she-ran.jpeg", "seg": "n8 p3",
        "window": "240.35-247.06", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "WELL"],
        "narration": ("The thing she walked all that way in the heat to fill — she "
                      "left it standing at the well, and she ran.",),
        "must_show": "the empty jar standing alone on the well stones in the foreground, and her already running away up the road toward the town in the distance.",
        "must_not_show": "do not put Jesus in this frame; she is running TOWARD the town, not away from it — the direction must be unmistakable.",
        "scene": (
            "The big clay jar stands alone and abandoned on the bleached stone curb in "
            "the near foreground, empty, its shadow a short pool beneath it. Beyond it "
            "the dusty road runs away toward the town, and well up that road the woman "
            "is running — her terracotta robe hauled up in one fist, her headcloth "
            "streaming back off her hair, dust kicking behind her heels, plainly "
            "moving away from the camera and toward the distant houses. The camera is "
            "back far enough to hold both the jar and the running figure. She has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b44", "out": "s44-toward-the-town-she-avoided.jpeg", "seg": "n8b",
        "window": "247.65-253.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TOWN"],
        "narration": ("Ran toward the town she had spent years avoiding, to the very "
                      "people she came out at noon to miss, shouting:"),
        "must_show": "her running IN through the town gateway and up the lane — into the exact doorways whose eyes she walked past at the start.",
        "must_not_show": "no shame in her posture at all; head up, going straight at them; do not put Jesus in this frame.",
        "scene": (
            "The woman comes running in through the low arched gateway and up the "
            "narrow lane of the town, her robe caught up in one hand and her other arm "
            "flung out, her head up and her mouth wide open shouting. She is going "
            "straight at the same doorways she walked past with her eyes down at the "
            "beginning of the day, and in them people are starting to turn and come "
            "out — a woman straightening up from a grindstone, a man stepping out of a "
            "shadowed doorway. Hard noon light in the lane. The camera is back far "
            "enough to see her head to sandals. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r010-b45", "out": "s45-come-see-a-man.jpeg", "seg": "w29",
        "window": "254.16-259.67", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TOWN"],
        "narration": ("Come, see a man, which told me all things that ever I did: is "
                      "not this the Christ? (John 4:29)"),
        "must_show": "her in the town square calling it out to everyone — both arms up, face blazing — and the townspeople gathering around her and actually listening.",
        "must_not_show": "nobody is turning away from her or shushing her; this is the woman they whispered about, and they are listening; do not put Jesus in this frame.",
        "scene": (
            "The woman stands in the middle of the small town square under the old fig "
            "tree with both arms up and out, her head back, shouting to everyone at "
            "once, her whole face blazing. All around her the townspeople are "
            "gathering fast and close in — men coming out of doorways, women with "
            "children on their hips, an old man rising off a bench, every face turned "
            "to her and listening hard. Nobody is turning away. Hard noon light in the "
            "square. The camera is back far enough to hold her and the crowd head to "
            "sandals. Every figure has two arms, two hands and one head."
        ),
    },
    # -------------------------------------------------- n9 — and they came ----
    {
        "id": "v2-r010-b46", "out": "s46-and-they-came.jpeg", "seg": "n9 p1-p2",
        "window": "261.18-266.76", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TOWN"],
        "narration": ("And they came. The town that whispered about her followed her "
                      "up the road to see for themselves."),
        "must_show": "the town pouring out through the gateway onto the road — a long straggling crowd of every kind of person, following her.",
        "must_not_show": "do not put Jesus in this frame; she is in FRONT, leading, not trailing behind them.",
        "scene": (
            "The townspeople stream out through the arched gateway and onto the dusty "
            "road in a long straggling crowd — men, women, children, an old man being "
            "helped along, dozens of them strung out along the road in the afternoon "
            "light. Ahead of all of them, well out in front and already up the slope, "
            "the woman in the terracotta robe is leading the way with her arm out "
            "pointing on toward the well. The camera is back far enough to hold the "
            "whole crowd and the road. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r010-b47", "out": "s47-she-met-their-eyes.jpeg", "seg": "n9 p3",
        "window": "266.76-274.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TOWN"],
        "narration": ("Many believed because of her word — the woman who wouldn't meet "
                      "their eyes at sunrise became the first missionary in that "
                      "gospel by sundown."),
        "must_show": "THE INVERSE OF b05: she has turned to face the crowd on the road and is LOOKING STRAIGHT AT THEM, talking, meeting the eyes that used to follow her — and they are listening to her.",
        "must_not_show": "no averted eyes anywhere in this frame; the composition must plainly answer the frame where they watched her walk past. Do not put Jesus in it.",
        "scene": (
            "On the open road the woman has stopped and turned back to face the crowd "
            "following her, and she is talking to them with both hands moving, her "
            "chin up and her eyes going directly from face to face — meeting every "
            "one of them. The townspeople have gathered in close around her in a half "
            "circle, heads tilted, listening to her intently; the same women who "
            "watched from their doorways are right at the front with their eyes on "
            "hers. Nobody is looking away. Warm late-afternoon light along the road. "
            "The camera is back far enough to hold her and the crowd head to sandals. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b48", "out": "s48-he-stayed-two-days.jpeg", "seg": "n9 p4",
        "window": "274.99-278.81", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOWN"],
        "narration": ("They asked him to stay, and he stayed two days — with Samaritans."),
        "must_show": "Jesus inside the Samaritan town, sitting and eating among Samaritan families in the square — completely at ease, a guest in a place no Jewish teacher would stay.",
        "must_not_show": "no halo, glare or rim-light; he is not teaching from a height or set apart — he is at the table among them.",
        "scene": (
            "Evening in the small town square under the fig tree. Jesus sits on a low "
            "bench among Samaritan families with a shared meal spread on a cloth "
            "between them — bread, olives, a clay jug — a plate being passed to him, a "
            "small child leaning against his knee, an old woman beside him mid-story. "
            "He is entirely at ease and completely among them, no space cleared around "
            "him. Warm low golden light and the first lamps lit in the doorways. The "
            "camera is back far enough to hold the whole group. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r010-b49", "out": "s49-we-have-heard-him-ourselves.jpeg", "seg": "n9 p5-p6",
        "window": "278.81-282.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TOWN"],
        "narration": ("And they told her: now we've heard him ourselves. We know.",),
        "must_show": "the closing frame: the townspeople turned to HER, telling her — hands on her arms, faces glad — and her standing among them, one of them at last.",
        "must_not_show": "do not put Jesus in this frame; she is not apart, not at the edge, and not looking down.",
        "scene": (
            "In the lamplit square at dusk the townspeople have gathered in around the "
            "woman and are telling her something — a man with both hands on her "
            "shoulders talking into her face, two women beside her with their hands on "
            "her arms, an old man nodding at her, all of them glad. She stands in the "
            "middle of them with her head up and her face open and wet, entirely "
            "inside the group. Warm low light and the first lamps. The camera is back "
            "far enough to hold the whole gathering head to sandals. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]
