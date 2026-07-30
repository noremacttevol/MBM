#!/usr/bin/env python3
"""V2 beat map — row 31, build-31-ten-virgins (Matthew 25:1-13).

COVERAGE: 25 pictures over 141.0 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 25:1-13 KJV):
  Setting of the telling: the Mount of Olives discourse (Matthew 24:3 "as he
  sat upon the mount of Olives, the disciples came unto him PRIVATELY") — so
  the frame beats put Jesus seated with the disciples on the evening
  hillside with Jerusalem's walls and temple across the valley. A setting no
  earlier row has used.
  v1    "ten virgins, which took their lamps, and went forth to meet the
        bridegroom" — clay oil lamps, going OUT at dusk to wait.
  v2-4  five WISE ("took oil in their vessels with their lamps"), five
        FOOLISH ("took no oil with them") — the small extra jar is the whole
        visible difference between the groups.
  v5    "the bridegroom TARRIED, they ALL slumbered and slept" — all ten
        sleep; sleeping is not the failure.
  v6    "at MIDNIGHT there was a cry made" — the arrival is deep night,
        torches and lamps the only light.
  v7-9  trimming; the foolish lamps "are GONE OUT"; the wise CANNOT share —
        "lest there be not enough for us and you" — said in distress, not
        smugness.
  v10   "they that WERE READY went in with him to the marriage: and the
        DOOR WAS SHUT."
  v11-12 "Lord, Lord, open to us ... I know you not."
  v13   "WATCH therefore, for ye know neither the day nor the hour."

  ⚑ Flags J,L (CONTENT-CARE §3 row 31): 'the shut door — mercy: the
  bridegroom WANTED them all there; oil = witness, not worthiness contest.'
  HOW THAT GOVERNS THE PICTURES: the shut-door beats are GRIEF, never
  gloating — no smug faces inside, no triumphant wise; the bridegroom is
  painted joyful at every arrival beat (he came to gather, not to exclude);
  the wise refuse the oil in visible distress; and the closing narration
  beats (b24-b25, 'the door is still open NOW') get the warmest frames in
  the row — the door OPEN and a lamp being filled tonight.

TIME OF DAY: frame beats are deep gold evening on the Mount of Olives. The
parable is DUSK into FULL NIGHT throughout — lamplight, torchlight and
moonless dark are correct and required (v6 midnight); nothing in the
parable happens in daylight. This is scripture-driven, not the row-11
defect.

CHANGING CONDITION (kept OUT of the locks): the LAMPS — full and steady,
burning low, sputtering out, dead and smoking, re-trimmed — change beat by
beat. The wise five always have their small jars; after the midnight beats
the foolish five's lamps are visibly dead.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "WISE": (
        "WISE FIVE LOCK: the five wise young women are the same five in "
        "every shot — Galilean women in their late teens and twenties with "
        "dark hair braided or bound under head-cloths, dressed in DEEP WARM "
        "colours: dark madder-red, deep russet, burnt sienna, dark plum and "
        "warm chestnut-brown wool with darker shawls (never cream, never "
        "white). EACH carries a clay oil lamp AND a small round-bellied "
        "clay oil jar stoppered with cloth. Their faces are shown clearly."
    ),
    "FOOLISH": (
        "FOOLISH FIVE LOCK: the five foolish young women are the same five "
        "in every shot — Galilean women in their late teens and twenties "
        "with dark hair braided or bound under head-cloths, dressed in COOL "
        "DUSTY colours: dusty indigo, slate blue-grey, grey-green, faded "
        "teal and dark charcoal wool with darker shawls (never cream, never "
        "white). Each carries ONLY a clay oil lamp — never any oil jar. "
        "Their faces are shown clearly — likeable, ordinary girls, never "
        "mocked by the framing."
    ),
    "GROOM": (
        "BRIDEGROOM LOCK: the bridegroom is the same man in every shot — "
        "about thirty, tall and glad-faced, with a trimmed dark beard and "
        "bright dark eyes, dressed in a festive DEEP WINE-RED robe with a "
        "DARK GOLD-EMBROIDERED sash and a garland circlet of green myrtle "
        "leaves (never cream, never white). His face is shown clearly and "
        "it is JOYFUL in every appearance — he comes to gather people in."
    ),
    "STREET": (
        "VILLAGE STREET LOCK: the village at night — a packed-earth street "
        "between honey-stone houses, a low stone wall where the road "
        "widens, the dark shapes of rooftops against the night sky, and at "
        "the street's end the feast house: a large house with a heavy "
        "double wooden door up three stone steps, warm lamplight in its "
        "windows."
    ),
    "FEAST-DOOR": (
        "FEAST DOOR LOCK: the feast house entrance — a heavy double wooden "
        "door with iron hinge-straps at the top of three worn stone steps, "
        "flanked by two bracket torches, warm light spilling from the "
        "windows beside it. The same door, steps and brackets in every "
        "door beat."
    ),
    "OLIVET": (
        "MOUNT OF OLIVES LOCK: the western slope of the Mount of Olives at "
        "evening — dry grass and grey stone between old gnarled olive "
        "trees, and across the deep Kidron valley the walls and rooftops "
        "of Jerusalem with the great temple courts catching the last "
        "light. Deep gold evening sky."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r031-b01", "out": "s01-jesus-told-a-story-about.jpeg", "seg": "n0",
        "window": "0.28-3.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": "Jesus told a story about ten young women waiting for a wedding.",
        "must_show": "SCRIPTURE-EXACT (Matt 24:3 — privately on the mount): Jesus seated on the evening hillside among a handful of disciples, Jerusalem across the valley behind them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a private evening circle on the grass, not a crowd.",
        "scene": (
            "On the dry grass of the Mount of Olives in deep gold evening "
            "light, Jesus sits on a low grey stone among four disciples "
            "settled close around him between the gnarled olive trunks — "
            "and across the shadowed valley behind them the walls and "
            "rooftops of Jerusalem hold the last of the sun, the great "
            "temple courts pale above them. He is mid-word, one hand "
            "raised in the first gesture of a story. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b02", "out": "s02-in-those-days-a-whole.jpeg", "seg": "n1",
        "window": "4.15-11.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["STREET"],
        "narration": (
            "In those days, a whole village would wait for the bridegroom to "
            "come, late in the evening, and lead everyone in to the feast."
        ),
        "must_show": "the custom itself — the village street at dusk dressed for a wedding: garlands over doorways, the feast house lit and waiting, villagers gathering with lamps.",
        "must_not_show": "no halo, glare or rim-light; anticipation everywhere — a village leaning toward a celebration that has not started yet.",
        "scene": (
            "The village street at deep dusk, dressed for a wedding: "
            "green garlands hung over doorways, neighbours gathering in "
            "twos and threes with small clay lamps already lit, children "
            "leaning out of windows to watch the dark end of the road — "
            "and at the street's head the feast house stands ready, warm "
            "lamplight in its windows and its heavy double door thrown "
            "wide. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b03", "out": "s03-so-ten-young-women-took.jpeg", "seg": "n2",
        "window": "11.87-16.14", "wide": True, "jesus": False, "ref": False,
        "locks": ["WISE", "FOOLISH", "STREET"],
        "narration": (
            "So ten young women took their oil lamps and went out into the dusk "
            "to meet him."
        ),
        "must_show": "SCRIPTURE-EXACT: all ten going OUT together — lamps lit, walking down the street toward the dark road, warm and cool clothing mingled, all friends tonight.",
        "must_not_show": "no halo, glare or rim-light; no division yet — the ten walk as one glad group; ten lamps, ten flames.",
        "scene": (
            "Down the dusk street the ten young women walk out together "
            "in one glad, chattering group, each carrying a small lit "
            "clay lamp cupped against the evening air — warm madder-reds "
            "and russets mingled in among dusty indigos and slate blues, "
            "shawls pulled up, faces bright with the occasion — heading "
            "toward the dark open road at the village edge where the "
            "bridegroom will appear. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r031-b04", "out": "s04-five-of-them-were-wise.jpeg", "seg": "n3",
        "window": "16.71-18.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE"],
        "narration": "Five of them were wise.",
        "must_show": "the wise five together — lamps in one hand, and the small stoppered oil jars held plainly in the other; the jars are the picture.",
        "must_not_show": "no halo, glare or rim-light; nothing superior in their faces — simply prepared.",
        "scene": (
            "A closer shot of the five wise young women paused under a "
            "garlanded doorway in the lamplit dusk, warm reds and "
            "russets and plums together: each holds her lit clay lamp "
            "in one hand — and in the other, resting against her hip, a "
            "small round-bellied clay jar stoppered with cloth, five "
            "little jars plainly in the frame. Their faces are easy and "
            "unhurried. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r031-b05", "out": "s05-the-other-five-were-foolish.jpeg", "seg": "n4",
        "window": "22.97-27.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOOLISH"],
        "narration": (
            "The other five were foolish. They brought their lamps — but no "
            "extra oil at all."
        ),
        "must_show": "SCRIPTURE-EXACT: the foolish five — lamps lit and lovely, both hands visibly free of any jar; nothing else different about them.",
        "must_not_show": "no halo, glare or rim-light; they are NOT painted as vain or silly — ordinary likeable girls whose only difference is the missing jar.",
        "scene": (
            "A closer shot of the five foolish young women laughing "
            "together in the dusk in their dusty indigos and slate "
            "blues, each holding up her lit clay lamp so the little "
            "flames lean together — and every second hand is empty, "
            "tucking a shawl, taking a friend's arm, carrying nothing: "
            "not one jar among the five of them. Their faces are as "
            "bright and likeable as the others'. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b06", "out": "s06-the-bridegroom-was-delayed-hour.jpeg", "seg": "n5",
        "window": "28.37-35.57", "wide": True, "jesus": False, "ref": False,
        "locks": ["WISE", "FOOLISH", "STREET"],
        "narration": (
            "The bridegroom was delayed. Hour after hour slipped by, and one by "
            "one, all ten women grew drowsy and fell asleep."
        ),
        "must_show": "SCRIPTURE-EXACT: ALL TEN asleep by the low wall at the village edge, lamps burning low beside them, the road beyond empty and fully dark.",
        "must_not_show": "no halo, glare or rim-light; all ten sleep — wise and foolish alike; the lamps still burn but LOW; deep night now.",
        "scene": (
            "Full night at the village edge: the ten young women lie "
            "and lean asleep along the low stone wall in a soft heap of "
            "shawls — heads on shoulders, one curled on a folded cloak, "
            "warm reds and cool blues mingled without difference — and "
            "along the wall their ten clay lamps sit burning low, small "
            "tired flames against the dark. Beyond them the road runs "
            "empty into blackness. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r031-b07", "out": "s07-behold-the-bridegroom-cometh-go.jpeg", "seg": "j2",
        "window": "36.03-39.38", "wide": True, "jesus": False, "ref": False,
        "locks": ["GROOM", "STREET"],
        "narration": "Behold, the bridegroom cometh; go ye out to meet him.",
        "must_show": "SCRIPTURE-EXACT: the midnight arrival — the glad bridegroom coming up the dark road with his torch-bearing companions, joy in his face and stride.",
        "must_not_show": "no halo, glare or rim-light; ⚑ Flag J: he arrives JOYFUL, arms already opening — a man coming to gather everyone in.",
        "scene": (
            "Out of the midnight dark the bridegroom comes up the road "
            "at a glad half-run, wine-red robe swinging and the myrtle "
            "circlet in his dark hair, his arms already beginning to "
            "open wide — flanked by three companions whose raised "
            "torches throw warm leaping light up the walls of the "
            "street ahead. His face is pure celebration. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b08", "out": "s08-then-at-midnight-a-cry.jpeg", "seg": "n6",
        "window": "40.90-45.91", "wide": True, "jesus": False, "ref": False,
        "locks": ["WISE", "FOOLISH", "STREET"],
        "narration": (
            "Then, at midnight, a cry rang out: The bridegroom is coming! Come "
            "out to meet him!"
        ),
        "must_show": "the waking — the ten starting up from sleep at the wall, a caller with a torch at the street corner, hands flying to lamps.",
        "must_not_show": "no halo, glare or rim-light; the burst of waking motion — shawls falling, lamps snatched up — against deep night.",
        "scene": (
            "At the low wall the ten young women start up out of sleep "
            "all at once — one on her feet already, shawl sliding from "
            "her shoulder, others pushing up on their hands, every face "
            "turned toward the street corner where a boy with a raised "
            "torch leans shouting the news into the dark. Hands reach "
            "for the low-burning lamps along the wall. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b09", "out": "s09-they-all-woke-and-reached.jpeg", "seg": "n7",
        "window": "46.52-51.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE"],
        "narration": (
            "They all woke and reached for their lamps. The wise trimmed "
            "theirs, and they burned warm and bright."
        ),
        "must_show": "SCRIPTURE-EXACT: the trimming — a wise woman pouring from her small jar into her lamp, the flame standing up strong; her four sisters' lamps already burning tall around her.",
        "must_not_show": "no halo, glare or rim-light; the pour from jar to lamp is the visible action — preparation paying off.",
        "scene": (
            "Close in the midnight dark: one of the wise young women "
            "steadies her clay lamp on the wall and pours a thin bright "
            "stream of oil into it from her small round-bellied jar, "
            "the flame standing up tall and steady as it drinks — while "
            "around her the other four wise women lift their own "
            "freshly-fed lamps, five strong warm flames pushing the "
            "night back off their faces. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r031-b10", "out": "s10-but-the-foolish-looked-down.jpeg", "seg": "n8",
        "window": "52.31-54.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOOLISH"],
        "narration": "But the foolish looked down in dismay.",
        "must_show": "the dismay — the five foolish faces lit from below by their guttering lamps, eyes down at the dying flames.",
        "must_not_show": "no halo, glare or rim-light; real dismay, tenderly framed — the viewer should ache for them, not laugh at them.",
        "scene": (
            "Close on the five foolish young women in the dark, their "
            "faces lit weakly from below by lamps whose flames have "
            "shrunk to trembling blue-edged points — five pairs of eyes "
            "looking down into the dying light, one girl's hand cupped "
            "helplessly around her flame, another's lips parted as the "
            "understanding arrives. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r031-b11", "out": "s11-their-lamps-were-sputtering-out.jpeg", "seg": "n8 + j3",
        "window": "54.57-62.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOOLISH"],
        "narration": (
            "Their lamps were sputtering out — they had no oil left. Give us of "
            "your oil; for our lamps are gone out."
        ),
        "must_show": "SCRIPTURE-EXACT: gone out — a dead lamp held up with a thin curl of smoke where the flame was, a foolish woman turning to plead past the camera.",
        "must_not_show": "no halo, glare or rim-light; the wisp of smoke from the dead wick is the picture; the pleading face is desperate, not scheming.",
        "scene": (
            "Close in the near-dark: one foolish young woman holds her "
            "clay lamp up between herself and the night — its flame "
            "gone, one thin grey curl of smoke rising off the dead "
            "wick — while her face turns past it toward friends beyond "
            "the frame, brows lifted in open desperate asking. Behind "
            "her a second dead lamp tips forgotten in another girl's "
            "hand. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b12", "out": "s12-please-they-cried-out-to.jpeg", "seg": "n9",
        "window": "64.05-67.95", "wide": True, "jesus": False, "ref": False,
        "locks": ["WISE", "FOOLISH", "STREET"],
        "narration": "Please, they cried out to the others — give us some of your oil!",
        "must_show": "the plea — the two groups face to face in the torch-lit street, foolish hands stretched out toward the wise women's jars.",
        "must_not_show": "no halo, glare or rim-light; urgency on both sides — the wise faces already show the ache of what they must answer.",
        "scene": (
            "In the street the two groups stand face to face in the "
            "mixed light of five strong lamps and distant torches: the "
            "foolish five pressing close with hands stretched out toward "
            "the small jars at the wise women's hips, one girl gripping "
            "a friend's sleeve, all five faces urgent — while the wise "
            "five hold their burning lamps between them, and there is "
            "no triumph anywhere, only the first shadow of a terrible "
            "arithmetic on their faces. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r031-b13", "out": "s13-not-so-lest-there-be.jpeg", "seg": "j4",
        "window": "68.47-76.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE", "FOOLISH"],
        "narration": (
            "Not so; lest there be not enough for us and you: but go ye rather "
            "to them that sell, and buy for yourselves."
        ),
        "must_show": "SCRIPTURE-EXACT: the refusal in DISTRESS — a wise woman clutching her small jar to her chest with both hands, her face grieved as she says it; a foolish friend's face falling before her.",
        "must_not_show": "no halo, glare or rim-light; ⚑ Flag L: NO smugness, no lecture-face — the wise woman suffers the refusal she has to give.",
        "scene": (
            "A close two-shot in lamplight: a wise young woman in deep "
            "madder-red holds her little stoppered jar pressed to her "
            "chest with both hands, her brows knotted and her eyes "
            "grieving even as her mouth shapes the refusal — and inches "
            "away the foolish friend's face is falling, hope going out "
            "of it like the lamps. Two girls who love each other, "
            "caught by an arithmetic neither can change. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b14", "out": "s14-but-the-wise.jpeg", "seg": "n10",
        "window": "78.63-79.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE"],
        "narration": "But the wise couldn't.",
        "must_show": "the impossibility itself — a close shot of one small jar tipped to show how little remains, barely enough for the one lamp beside it.",
        "must_not_show": "no halo, glare or rim-light; the jar is nearly empty — the refusal is physics, not selfishness.",
        "scene": (
            "A very close shot in lamplight: a small round-bellied clay "
            "jar tipped on its side in a young woman's hands, showing "
            "the thin last measure of oil pooled inside its curve — a "
            "few swallows, no more — beside her one clay lamp burning "
            "steadily, exactly the flame that little oil must keep "
            "alive until the feast. There is nothing to spare and the "
            "frame proves it. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r031-b15", "out": "s15-there-enough-for-all-of.jpeg", "seg": "n10",
        "window": "79.76-84.57", "wide": True, "jesus": False, "ref": False,
        "locks": ["WISE", "FOOLISH", "STREET"],
        "narration": (
            "There isn't enough for all of us, they said. Hurry — go and buy "
            "your own."
        ),
        "must_show": "the parting — the foolish five turning to run into the dark toward the oil-seller's lane, the wise five watching them go with grief, pointing the way to help.",
        "must_not_show": "no halo, glare or rim-light; the wise POINT THE WAY — actively helping the only way left; both groups in motion.",
        "scene": (
            "In the torch-broken dark the group tears in two: the five "
            "foolish young women are already running up the side lane, "
            "shawls streaming, dead lamps clutched to their chests — "
            "while behind them one wise woman stands with her arm flung "
            "out pointing them toward the oil-seller's doorway deeper "
            "in the village, and the other four watch them go with "
            "open grief on their lamplit faces. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b16", "out": "s16-and-while-the-foolish-rushed.jpeg", "seg": "n11",
        "window": "85.15-90.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["GROOM", "WISE", "STREET"],
        "narration": (
            "And while the foolish rushed off into the dark to find oil, the "
            "bridegroom arrived."
        ),
        "must_show": "SCRIPTURE-EXACT: the meeting — the glad bridegroom reaching the five wise women, their lamps around his welcome, the procession forming toward the feast house.",
        "must_not_show": "no halo, glare or rim-light; ⚑ Flag J: his gladness at the five who ARE there — and his head turning toward the empty lane, missing the ones who are not.",
        "scene": (
            "The bridegroom has reached the five wise women in the "
            "street and his arms are spread wide in welcome, torchlight "
            "and their five lamp flames warming the whole meeting — the "
            "young women laughing with relief around him, his "
            "companions already turning the procession toward the "
            "feast house — while the bridegroom's own glad face is "
            "caught half-turned toward the dark side lane, looking for "
            "five more who are not there. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b17", "out": "s17-the-ones-who-were-ready.jpeg", "seg": "n12",
        "window": "90.54-94.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["GROOM", "WISE", "FEAST-DOOR"],
        "narration": (
            "The ones who were ready went in with him to the wedding feast. And "
            "the door was shut."
        ),
        "must_show": "SCRIPTURE-EXACT: the entering and the shutting in one frame — the last wise woman stepping over the threshold into the warm light with the bridegroom, the heavy door already swinging to.",
        "must_not_show": "no halo, glare or rim-light; the door closes on WARMTH — the grief is that anyone is outside it, not that inside is grim.",
        "scene": (
            "At the top of the three worn steps the heavy double door "
            "stands half-swung closed: through the narrowing gap the "
            "last of the wise young women steps over the threshold into "
            "deep warm light where the bridegroom waits with his hand "
            "out to her, music and moving figures behind him — while "
            "the bracket torches flank the closing door and the empty "
            "dark street lies below the steps. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b18", "out": "s18-lord-lord-open-to-us.jpeg", "seg": "j5 + j6",
        "window": "95.37-101.20", "wide": True, "jesus": False, "ref": False,
        "locks": ["FOOLISH", "FEAST-DOOR"],
        "narration": "Lord, Lord, open to us. Verily I say unto you, I know you not.",
        "must_show": "SCRIPTURE-EXACT: the five at the shut door — hands flat on the wood, lamps dead at their feet, the warm light seeping under the door they cannot open.",
        "must_not_show": "no halo, glare or rim-light; ⚑ Flag J: pure grief, no monster door, no gloating from within — the tragedy is the nearness of the warmth.",
        "scene": (
            "The five foolish young women crowd the top of the stone "
            "steps at the shut double door in the deep night — two with "
            "their palms flat against the iron-strapped wood, one with "
            "her forehead resting on it, their dead lamps set down at "
            "their feet — and along the bottom of the door a thin line "
            "of warm feast light seeps out over the threshold stone, "
            "close enough to touch. The bracket torches gutter low. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b19", "out": "s19-later-the-others-came-back.jpeg", "seg": "n13",
        "window": "102.71-107.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["FOOLISH", "FEAST-DOOR"],
        "narration": (
            "Later the others came back, knocking. Lord, they called, open the "
            "door for us!"
        ),
        "must_show": "the knocking — close on a small fist against the heavy wood, a tear-streaked face beside it calling upward at the silent door.",
        "must_not_show": "no halo, glare or rim-light; desperation framed with tenderness — the camera grieves with them.",
        "scene": (
            "Close at the shut door in the torch-gutter light: one "
            "young woman's small fist caught mid-knock against the "
            "heavy iron-strapped planks, her tear-streaked face lifted "
            "beside it calling up at the blank wood, her slate-blue "
            "shawl slid back off her hair — and behind her shoulder a "
            "second face, spent from running, waiting for an answer "
            "the door does not give. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r031-b20", "out": "s20-but-the-answer-came-from.jpeg", "seg": "n13",
        "window": "107.54-111.21", "wide": True, "jesus": False, "ref": False,
        "locks": ["FOOLISH", "FEAST-DOOR", "STREET"],
        "narration": "But the answer came from inside: I do not know you.",
        "must_show": "the answer landing — the five turning away from the door down the steps, the feast light warm in the windows above them, the street dark and long below.",
        "must_not_show": "no halo, glare or rim-light; no one visible inside — the answer is only a fact now; the five carry it down the steps.",
        "scene": (
            "From the dark street looking up: the five young women come "
            "down the three worn steps away from the shut door, heads "
            "bowed, one steadying another by the arm, their dead lamps "
            "hanging loose from their fingers — while above and behind "
            "them the feast house windows hold their deep warm light "
            "and the muffled shape of the celebration goes on inside. "
            "The night street receives them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b21", "out": "s21-then-jesus-told-them-why.jpeg", "seg": "n14 + j1",
        "window": "111.79-121.53", "wide": True, "jesus": True, "ref": REF,
        "locks": ["OLIVET"],
        "narration": (
            "Then Jesus told them why he had shared this story. Watch "
            "therefore, for ye know neither the day nor the hour wherein the "
            "Son of man cometh."
        ),
        "must_show": "SCRIPTURE-EXACT: back on the darkening mount — Jesus grave and gentle among the disciples, Jerusalem's lights beginning across the valley, the warning laid down like a gift.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gravity with warmth — a friend's urgent counsel, not a threat.",
        "scene": (
            "The Mount of Olives gone to deep blue dusk: Jesus leans "
            "toward the four disciples with his forearms on his knees, "
            "face grave and very kind, the story's point passing from "
            "him to them — and across the black valley the first small "
            "lamps of Jerusalem are being lit along the walls, tiny "
            "warm points under the last banded light of the sky. The "
            "disciples' faces are sober and awake. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b22", "out": "s22-along-with-their-lamps-they.jpeg", "seg": "n3",
        "window": "18.17-22.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE"],
        "narration": (
            "Along with their lamps, they each carried a small jar of extra "
            "oil."
        ),
        "must_show": "the jars themselves — a close shot of the five small stoppered clay jars held or slung at five hips, the quiet habit of readiness.",
        "must_not_show": "no halo, glare or rim-light; the jars are humble and small — preparation looks unimpressive, and that is the point.",
        "scene": (
            "A close shot along the line of the five wise women in the "
            "dusk lamplight, framed at waist height: five small "
            "round-bellied clay jars, cloth-stoppered and no bigger "
            "than a cupped hand, held against hips and slung from "
            "shoulder cords over the warm reds and plums of their "
            "dresses — the plainest, least remarkable objects on the "
            "whole festive street. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r031-b23", "out": "s23-the-oil-is-the-one.jpeg", "seg": "n15",
        "window": "123.06-133.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["WISE"],
        "narration": (
            "The oil is the one thing you cannot borrow at the last minute — a "
            "heart that is truly ready, a faith that is really your own, a lamp "
            "you filled yourself."
        ),
        "must_show": "the meaning in one image — a close shot of a young woman's two hands pouring oil from her own small jar into her own lamp, unhurried, in quiet lamplight.",
        "must_not_show": "no halo, glare or rim-light; intimacy and ownership — HER jar, HER lamp, HER hands; nobody else in frame.",
        "scene": (
            "A quiet close shot: a young woman's two hands alone in "
            "warm lamplight, one tipping her own small clay jar so a "
            "fine thread of oil runs down into the lamp cupped in her "
            "other palm, the flame steadying and rising as it is fed — "
            "the filling of one's own lamp, done by no one else's "
            "hands, in no one else's light. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r031-b24", "out": "s24-and-here-is-the-good.jpeg", "seg": "n16",
        "window": "133.56-136.51", "wide": True, "jesus": False, "ref": False,
        "locks": ["GROOM", "FEAST-DOOR"],
        "narration": "And here is the good news: the door is still open now.",
        "must_show": "⚑ Flags J,L — the warmest frame of the row: the feast door standing WIDE OPEN in the night, deep warm light flooding the steps, and the bridegroom standing in it looking out and beckoning down the street.",
        "must_not_show": "no halo, glare or rim-light; the door is unmistakably OPEN and the bridegroom WANTS whoever is out there — arm extended in open invitation.",
        "scene": (
            "The feast house door stands thrown fully open into the "
            "night, deep warm light flooding down the three worn steps "
            "and across the dark street stones — and in the doorway "
            "the bridegroom stands looking OUT into the dark, one arm "
            "extended down the empty street in open unhurried "
            "invitation, the myrtle circlet in his hair and the feast "
            "alive and golden behind him. He is not closing anything "
            "tonight. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r031-b25", "out": "s25-tonight-your-lamp-can-be.jpeg", "seg": "n16",
        "window": "136.51-140.76", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Tonight, your lamp can be filled. He is worth being ready for.",
        "must_show": "the closing image — a single clay lamp on a dark sill being filled from a small jar by two hands, the flame rising bright and new against the night.",
        "must_not_show": "no halo, glare or rim-light; one lamp, filling NOW — present-tense hope; the flame grows strong as the oil reaches it.",
        "scene": (
            "A close final frame in the dark: on a rough stone "
            "windowsill a single clay lamp is being filled by two "
            "steady hands tipping a small round-bellied jar, the "
            "bright thread of oil still falling — and the lamp's flame, "
            "caught in the moment of being fed, stands up taller and "
            "warmer against the deep blue night beyond the sill, "
            "pushing its light out across the stone. There is still "
            "oil, and there is still time. Every figure has two arms, "
            "two hands and one head."
        ),
    },
]
