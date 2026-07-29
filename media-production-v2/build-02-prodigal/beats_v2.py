#!/usr/bin/env python3
"""V2 beat map — row 2, build-02-prodigal (Luke 15:11-32).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 24 pictures, against V1's 10 unique stills. V1 told
the father's run, the embrace, the robe-and-ring and the entire elder-brother arc
over five stills; every one of those moments is a beat and gets its own frame here.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Luke 15 KJV):
  v1-2   publicans and sinners drew near to HEAR him; Pharisees and scribes
         MURMURED, "This man receiveth sinners, and eateth with them." So the
         frame-story shows Jesus at a table AMONG them, gazes on him, the
         religious men apart and displeased.
  v12    "Father, give me the portion of goods that falleth to me" — the ask.
  v13    took his journey into a FAR country; wasted his substance.
  v14    a mighty famine; he began to be in want.
  v15-16 sent into the fields to FEED SWINE; would fain have filled his belly
         with the husks the swine did eat; NO MAN GAVE UNTO HIM.
  v17    "he came to himself" — the realization is IN the pigsty.
  v18-19 the rehearsed speech (j3, red).
  v20    "when he was yet A GREAT WAY OFF, his father saw him, and had
         compassion, and RAN, and fell on his neck, and kissed him."
  v22    "the BEST ROBE ... a RING on his hand, and SHOES on his feet."
  v23    the fatted calf; merriment.
  v25    elder son was IN THE FIELD; coming near the house he HEARD MUSICK
         AND DANCING; v26 asked a SERVANT what these things meant.
  v28    "he was ANGRY, and would not go in: therefore came his father OUT,
         and INTREATED him."
  v29    the elder son's complaint (j4, red).
  v31-32 "Son, thou art ever with me..." — the story ENDS at the open door,
         unresolved; the parable never says whether he went in.

CONTENT-CARE: row 2 is not in the §3 flag table = GREEN. Restraint applied anyway:
the far-country "riotous living" is never depicted — no party scene, nothing
lewd; the squandering is carried by the departure and by the emptiness after
(money gone, famine, pigs). The pigsty shows hunger and mud, never degradation
played for spectacle.

TIME-OF-DAY ARC (self-consistent; the parable states none):
  frame story = bright day · ask/departure = morning · famine/pigs = harsh
  midday · road home + rehearsal = late afternoon · father sees / runs /
  embrace = golden late afternoon · robe and feast = warm evening lamplight ·
  elder brother arc = dusk into night, torchlit doorway.
"""

LOCKS = {
    # Jesus appears ONLY in the two frame-story shots (b01, b02). Inside the
    # parable he is the storyteller, not a figure — nobody in the parable wears
    # cream (only-Jesus-cream law).
    # PHARISEES LOCK v2 (row 2 QC, CREAM-CROWD recurrence). v1 leaned on the
    # negation "never white, never cream, never pale" and the model dressed all
    # three in white striped prayer shawls anyway — the single largest pale mass in
    # the frame, standing right beside the one man allowed to wear cream. Same
    # lesson row 1 paid for at the SETTING lock: state the colours POSITIVELY and
    # anchor them against something in the frame. Negations do not hold; a stated
    # colour does.
    "PHARISEES": (
        "PHARISEES LOCK: the religious men are the same three in both shots — older "
        "scribes with long grey-streaked beards, in DARK CHARCOAL-BROWN and DEEP "
        "UMBER scholarly robes. Their prayer shawls are woven from the SAME "
        "SATURATED DARK wool as their robes — deep charcoal, dark umber and "
        "near-black, with dark indigo stripes and dark fringe — so that every shawl "
        "is plainly DARKER than the sunlit stone wall behind them. They stand "
        "stiffly together, faces tight with disapproval."
    ),
    "TABLE": (
        "TABLE LOCK: a low stone courtyard off a Galilean street in bright honest "
        "daylight — a plain wooden table with bread, olives and clay cups, crowded "
        "by ordinary working men and women in SATURATED DEEP earth colours: dark "
        "chocolate brown, deep russet, burnt ochre, dark olive and dusty indigo "
        "wool. No one at the table wears cream, off-white, ivory or any pale "
        "near-white cloth."
    ),
    "FATHER": (
        "FATHER LOCK: the father is the same man in every shot — a dignified "
        "landowner of about sixty, strong and upright, a full SILVER-GREY beard, "
        "deep-lined warm face, thick grey hair, dark eyes. He wears a DEEP "
        "INDIGO-BLUE wool robe with a woven border over a warm umber tunic, a wide "
        "cloth sash, leather sandals (never cream, never white). His face is shown "
        "clearly."
    ),
    # The story CHANGES the younger son's clothing (fine cloak -> rags -> the
    # best robe), so his lock fixes only face, hair and build; each beat states
    # his clothing and its condition. A lock must never argue with a beat.
    "YOUNGER": (
        "YOUNGER SON LOCK: the younger son is the same man in every shot — early "
        "twenties, lean, warm olive-brown skin, short DARK CURLY hair, a sparse "
        "young dark beard, expressive dark eyes, a light frame next to his father. "
        "He never wears cream or white. His face is shown clearly."
    ),
    "ELDER": (
        "ELDER SON LOCK: the elder son is the same man in every shot — late "
        "twenties, broader and taller than his brother, straight dark hair to the "
        "ears, a full trimmed dark beard, sun-darkened olive skin, hard-worked "
        "hands. He wears a DARK OLIVE-GREEN work tunic, dusty from the field, with "
        "a plain leather belt (never cream, never white). His face is shown clearly."
    ),
    "ESTATE": (
        "ESTATE LOCK: the father's farm — a broad stone farmhouse with a walled "
        "courtyard and a heavy wooden gate on a low hill, olive trees and terraced "
        "vines around it, a long pale dirt road running down the valley toward the "
        "horizon, Judean hills beyond. The household servants wear plain dark "
        "earth-brown and grey-brown wool; no one wears cream, off-white or any "
        "pale near-white cloth."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r002-b01", "out": "s01-they-murmured.jpeg", "seg": "n0 p1",
        "window": "0.28-4.6", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PHARISEES", "TABLE"],
        "narration": ("When religious men complained that Jesus spent his time "
                      "with sinners,"),
        "must_show": "Jesus AT the table among publicans and sinners; the Pharisees apart, murmuring.",
        "must_not_show": "no halo/glow; Jesus not detached at the frame edge — the table's gazes are on him.",
        "scene": (
            "Jesus sits at the crowded table among the publicans and sinners, at "
            "their level, at ease, mid-conversation, and every face at the table is "
            "turned toward him. Off to one side the three religious men stand apart "
            "in the shade of the wall, heads bent together, murmuring, their eyes "
            "fixed on him in disapproval. Bright honest daylight. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b02", "out": "s02-he-answered-with-a-story.jpeg", "seg": "n0 p2",
        "window": "4.6-9.48", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PHARISEES", "TABLE"],
        "narration": ("he didn't argue with them. He answered with a story, about "
                      "a father and his two sons."),
        "must_show": "Jesus beginning the story — calm, open gesture; the whole courtyard turning to listen, Pharisees included.",
        "must_not_show": "no anger on his face; no halo/glow.",
        "scene": (
            "Jesus has half-risen at the table and begun to speak, one open hand "
            "lifted in the easy gesture of a storyteller, his face calm and warm, "
            "looking toward the religious men as he speaks. Everyone at the table "
            "has turned to listen, and even the three religious men have gone "
            "still, caught by the story despite themselves. Bright honest daylight. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b03", "out": "s03-the-ask.jpeg", "seg": "n1 p1",
        "window": "9.48-15.6", "wide": True, "jesus": False, "ref": False,
        "locks": ["FATHER", "YOUNGER", "ESTATE"],
        "narration": ("The younger son asked for his inheritance early — as if to "
                      "say he wished his father were already dead."),
        "must_show": "the son demanding, palm out; the father's stricken, wounded stillness.",
        "must_not_show": "no shouting match; the wound is quiet; morning light.",
        "scene": (
            "In the farmhouse courtyard in early morning light, the younger son "
            "stands before his seated father with his open palm held out, chin "
            "lifted, wearing a fine RUST-RED wool tunic and a good travel cloak — "
            "and the father sits very still, his hands resting on his knees, his "
            "lined face quietly stricken, looking up at his boy. A leather money "
            "chest sits open beside the father. Exactly two people are in the "
            "frame; each has two arms, two hands of five fingers each, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r002-b04", "out": "s04-he-left.jpeg", "seg": "n1 p2",
        "window": "15.6-20.09", "wide": True, "jesus": False, "ref": False,
        "locks": ["FATHER", "YOUNGER", "ESTATE"],
        "narration": "Then he left, and poured it all out on a life that emptied him.",
        "must_show": "the son walking away down the long road with his bag; the father watching him go from the gate.",
        "must_not_show": "no party scene, nothing of the riotous living depicted; the leaving carries it.",
        "scene": (
            "SHOT FROM BEHIND THE FATHER, the camera at the courtyard gate looking "
            "DOWN the long pale dirt road as it runs away from the farm toward "
            "distant hills. In the near foreground, seen from behind and slightly "
            "to one side, the father stands alone in the open gateway, one hand "
            "resting on the gatepost, head and shoulders turned to watch. Far down "
            "the road ahead of him, WALKING AWAY FROM THE CAMERA with his back to "
            "us and never once looking back, the younger son is already small with "
            "distance, a full travel bag over his shoulder and the heavy money "
            "pouch at his belt, his fine RUST-RED tunic and travel cloak bright "
            "with morning. He is leaving; the road carries him toward the far "
            "horizon and the farm is behind him. Morning light, long shadows. "
            "Exactly two people are in the frame; each has two arms, two hands, "
            "two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b05", "out": "s05-money-gone-famine.jpeg", "seg": "n2 p1",
        "window": "20.09-24.2", "wide": False, "jesus": False, "ref": False,
        "locks": ["YOUNGER"],
        "narration": "When the money was gone, a famine came.",
        "must_show": "alone in a strange dusty town, empty purse, want beginning.",
        "must_not_show": "no companions (no man gave unto him); no drunkenness shown.",
        "scene": (
            "In a strange far-country town under a harsh dusty midday sky, the "
            "younger son sits alone against a mud-brick wall, his once-fine "
            "rust-red tunic now dirty and worn, holding his empty leather purse "
            "upside down in one hand — nothing left in it. The street behind him "
            "is parched and half-deserted, market stalls bare with famine. Nobody "
            "looks at him. Exactly one person is in the foreground, with two arms, "
            "two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b06", "out": "s06-feeding-pigs.jpeg", "seg": "n2 p2",
        "window": "24.2-27.4", "wide": True, "jesus": False, "ref": False,
        "locks": ["YOUNGER"],
        "narration": ("He ended up feeding pigs, so hungry he would have eaten "
                      "what they ate."),
        "must_show": "him IN the pigsty with the swine, ragged, staring at the husks in the trough with real hunger.",
        "must_not_show": "no degradation played for spectacle; his dignity is wrecked but he is a human being; no one else present.",
        "scene": (
            "In a muddy stone-fenced pigsty under a hard midday sun, the younger "
            "son stands ankle-deep among several rooting pigs, his rust-red tunic "
            "torn, faded and filthy, tipping husk pods from a wooden bucket into "
            "the trough — and his hollow eyes are fixed on the husks themselves, "
            "his free hand pressed against his empty stomach. He is utterly alone; "
            "no other person anywhere. Exactly one person is in the frame, with "
            "two arms, two hands of five fingers each, two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b07", "out": "s07-came-to-his-senses.jpeg", "seg": "n2 p3",
        "window": "27.4-30.39", "wide": False, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/younger-ref.jpeg"],
        "locks": ["YOUNGER"],
        "narration": "And there, in the mud, he came to his senses.",
        "must_show": "the realization — kneeling in the mire, head lifting, the thought arriving (v17 'he came to himself').",
        "must_not_show": "no light beam, no glow; the change is on his face only.",
        "scene": (
            "Close on the younger son sunk to one knee in the churned mud of the "
            "stone-fenced pigsty under a hard midday sun, still wearing the SAME "
            "torn, faded, filthy RUST-RED tunic and barefoot, one hand braced on "
            "the low stone fence, his head just lifting — and his eyes coming clear "
            "for the first time, the realization arriving on his gaunt dirty face: "
            "his father's hired servants have bread enough. Two dark pigs root in "
            "the mud at the edge of the frame. The "
            "change is entirely in his face; nothing else in the frame changes. "
            "Exactly one person is in the frame, with two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r002-b08", "out": "s08-walking-home.jpeg", "seg": "n3",
        "window": "30.39-34.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["YOUNGER"],
        "narration": "So he started walking home, rehearsing a speech the whole way.",
        "must_show": "the long road home, mid-stride, lips moving with the rehearsal.",
        "must_not_show": "the farm is not visible yet; he is far away still.",
        "scene": (
            "The younger son walks a long empty dirt road through dry hill country "
            "in late-afternoon light, ragged and barefoot in his torn faded "
            "rust-red tunic, a walking stick in one hand, his lips visibly moving "
            "as he rehearses his speech to himself, his brow working. The road "
            "runs on ahead of him toward far hills; no buildings anywhere yet. "
            "Exactly one person is in the frame, with two arms, two hands, two "
            "legs and one head."
        ),
    },
    {
        "id": "v2-r002-b09", "out": "s09-the-rehearsed-speech.jpeg", "seg": "j3",
        "window": "34.86-50.05", "wide": False, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/younger-ref.jpeg"],
        "locks": ["YOUNGER"],
        "narration": ("I will arise and go to my father... make me as one of thy "
                      "hired servants. (Luke 15:18-19)"),
        "must_show": "his face carrying the whole speech — shame, resolve, the words costing him.",
        "must_not_show": "no tears streaming; restrained; late afternoon.",
        "scene": (
            "A tight shot of the younger son paused at a rise in the road in low "
            "late-afternoon light, still in the SAME torn, faded, filthy RUST-RED "
            "tunic and barefoot, eyes down, jaw tight, mid-word — shame and "
            "resolve fighting in his gaunt face as he practises the hardest "
            "sentence of his life. Far behind him, small in the distance haze, the "
            "first pale line of his home valley. Exactly one person is in the "
            "frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b10", "out": "s10-father-saw-him.jpeg", "seg": "n4",
        "window": "50.05-53.78", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg"],
        "locks": ["FATHER", "ESTATE"],
        "narration": "He was still a long way off... when his father saw him.",
        "must_show": "v20 — the father catching sight of a tiny far figure on the road; recognition seizing him.",
        "must_not_show": "the son is a DISTANT small figure, not close; the father has not started running yet.",
        "scene": (
            "SHOT FROM BESIDE AND SLIGHTLY BEHIND THE FATHER so that his face is "
            "seen in profile and the long pale road runs away from him into the "
            "distance ALONG HIS LINE OF SIGHT. He stands at the courtyard gate in "
            "golden late-afternoon light, one hand gripping the gatepost, his whole "
            "body suddenly gone rigid, the other hand raised to shade his eyes as "
            "he stares FAR UP THE ROAD — and there, tiny with distance and directly "
            "ahead of his gaze, a single ragged figure is walking toward the farm. "
            "The father's lined face is caught in the first instant of recognition, "
            "and every line in the frame leads from his eyes down the road to that "
            "distant figure. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b11", "out": "s11-the-father-ran.jpeg", "seg": "n5a",
        "window": "53.78-55.61", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg"],
        "locks": ["FATHER", "ESTATE"],
        "narration": "The father ran.",
        "must_show": "the icon of the story — an old man in full undignified RUN down the road, robe hitched.",
        "must_not_show": "not a jog, not a stride — a RUN; sandals kicking dust.",
        "scene": (
            "SHOT FROM THE SIDE OF THE ROAD with the camera low, so the father runs "
            "ACROSS the frame from left to right and the long dirt road stretches "
            "away to the right toward distant hills. The father is in full run, his "
            "deep indigo-blue robe hitched up in both fists above his knees, grey "
            "beard streaming, sandals hammering up dust, his face blazing with "
            "urgency and joy — an old man running with everything he has, caught "
            "mid-stride with both feet clear of the ground. FAR AHEAD OF HIM TO THE "
            "RIGHT, small with distance and squarely IN THE DIRECTION HE IS "
            "RUNNING, the tiny ragged figure of his son comes up the road toward "
            "him. The two of them are closing the same stretch of road. Golden "
            "late-afternoon light. Every figure has two arms, two hands, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r002-b12", "out": "s12-he-ran-anyway.jpeg", "seg": "n5b",
        "window": "55.61-61.25", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg"],
        "locks": ["FATHER", "ESTATE"],
        "narration": ("Old men in that world did not run. It was beneath their "
                      "dignity. He ran anyway."),
        "must_show": "the scandal of it — household servants stopped dead, staring, as he tears past.",
        "must_not_show": "no mockery on the servants' faces — pure astonishment.",
        "scene": (
            "SHOT FROM THE SIDE with the camera low beside the farm's outer wall: "
            "the father tears past from left to right at a full run, his deep "
            "indigo-blue robe still hitched up in both fists above his knees, "
            "heading AWAY down the road toward the distant figure. Two household "
            "servants in plain dark earth-brown wool have stopped dead where they "
            "stood, a dropped water jar shattering and spilling at one servant's "
            "feet, staring open-mouthed after their master, astonished to see the "
            "old man run. He pays them no mind; his eyes are locked on the far road "
            "ahead of him. Golden late-afternoon light on real skin, real dust and "
            "real wool, photographed on location. Exactly three people are in the "
            "frame; each has two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b13", "out": "s13-the-embrace.jpeg", "seg": "n6",
        "window": "61.25-66.87", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/younger-ref.jpeg"],
        "locks": ["FATHER", "YOUNGER", "ESTATE"],
        "narration": ("He didn't wait for the speech. He wrapped his arms around "
                      "his son before a single word was said."),
        "must_show": "v20 — fell on his neck; the son's stunned face over the father's shoulder, speech dying unspoken.",
        "must_not_show": "the son's arms hang or barely rise — he expected a servant's place, not this.",
        "scene": (
            "On the open road in golden late-afternoon light the father has "
            "wrapped his arms fully around his ragged son and pulled him hard "
            "against his chest, his silver-grey head pressed to the boy's filthy "
            "shoulder, eyes shut — and over the father's shoulder the son's gaunt "
            "face is stunned open, his rehearsed words dying on his lips, his own "
            "arms only beginning to rise, hands not yet closed on his father's "
            "back, as if he cannot believe he is allowed to return the embrace. "
            "The son is still in the SAME torn, faded, filthy RUST-RED tunic and is "
            "BAREFOOT — he has not been given shoes yet. "
            "Dust still hangs from the run. Exactly two people "
            "are in the frame; each has two arms, two hands of five fingers each "
            "and one head."
        ),
    },
    {
        "id": "v2-r002-b14", "out": "s14-robe-ring-shoes.jpeg", "seg": "n7 p1",
        "window": "66.87-71.5", "wide": True, "jesus": False, "ref": False,
        "locks": ["FATHER", "YOUNGER", "ESTATE"],
        "narration": ("That night the father dressed him in the finest robe, put "
                      "a ring on his hand,"),
        "must_show": "v22 — the best robe going onto his shoulders, the ring onto his hand; servants bringing sandals.",
        "must_not_show": "the robe is deep wine-red, NOT cream or white.",
        "scene": (
            "In the farmhouse's warm lamplit hall that evening, the father with "
            "his own hands settles a magnificent DEEP WINE-RED robe onto his "
            "son's washed shoulders and presses a gold signet ring onto the young "
            "man's finger, while a servant in dark earth-brown wool kneels "
            "fastening new leather sandals onto the son's feet. The son stands "
            "overwhelmed, looking down at the ring on his hand. Warm oil-lamp "
            "light. Exactly three people are in the frame; each has two arms, two "
            "hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b15", "out": "s15-my-son-was-dead.jpeg", "seg": "n7 p2 + j1",
        "window": "71.5-82.05", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/younger-ref.jpeg"],
        "locks": ["FATHER", "YOUNGER", "ESTATE"],
        "narration": ("and called for a feast — and he told everyone why. / For "
                      "this my son was dead, and is alive again; he was lost, and "
                      "is found. (Luke 15:24)"),
        "must_show": "the feast alive; the father proclaiming with his hand on the son's shoulder; every face turned to them.",
        "must_not_show": "nobody at the feast in cream; the son in the wine-red robe.",
        "scene": (
            "A TALL VERTICAL FRAME with the camera upright and level at standing "
            "eye height, every figure standing upright with their feet on the floor "
            "and their head above their shoulders. "
            "The farmhouse hall blazes with lamplight and a feast in full life — "
            "laden tables, musicians with pipe and drum, household and neighbours "
            "in deep russet, ochre, olive and indigo wool — and at the head of it "
            "the father stands with one hand gripping his son's shoulder, the "
            "other arm flung wide, proclaiming to them all, his face shining. The "
            "son in the deep wine-red robe stands washed and overwhelmed at his "
            "father's side, and every face in the hall is turned toward the two "
            "of them. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b16", "out": "s16-elder-in-the-field.jpeg", "seg": "n9 p1",
        "window": "82.05-87.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["ELDER", "ESTATE"],
        "narration": "But Jesus wasn't finished. The older son was still out in the field, like always.",
        "must_show": "v25 — the elder son at work in the field at dusk, faithful, alone.",
        "must_not_show": "the house lights are distant; he doesn't know yet.",
        "scene": (
            "In the last blue-grey light of dusk the elder son works alone in a "
            "terraced field below the farm, a heavy hoe mid-swing, his dark "
            "olive-green tunic dark with sweat and dust after a full day — and "
            "far up the hill behind him the farmhouse windows are just beginning "
            "to warm with lamplight he has not yet noticed. Exactly one "
            "person is in the frame, with two arms, two hands of five fingers "
            "each, two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b17", "out": "s17-musick-and-dancing.jpeg", "seg": "n9 p2",
        "window": "87.0-91.5", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["ELDER", "ESTATE"],
        "narration": ("When he came near the house and heard the music, a servant "
                      "told him: your brother is home."),
        "must_show": "v25-26 — stopped near the lit house, hearing it; the servant explaining; his face beginning to harden.",
        "must_not_show": "he is OUTSIDE, near the courtyard, not at the door yet.",
        "scene": (
            "In full night now, near the farmhouse's outer wall, the elder son "
            "stands stopped with his hoe still over his shoulder, head turned "
            "toward the house where every window pours warm light and the sound "
            "of pipes and dancing — while a young servant in plain earth-brown "
            "wool stands facing him holding a burning torch upright in one fist, "
            "the flame sitting directly on the head of the torch and touching it, "
            "and gestures toward the house with his free hand, explaining, and the "
            "elder son's dusty face is beginning to harden as he understands. "
            "Exactly two people are in the frame; each has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r002-b18", "out": "s18-would-not-go-in.jpeg", "seg": "n9 p3",
        "window": "91.5-94.96", "wide": False, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["ELDER", "ESTATE"],
        "narration": "And he was so angry, he refused to go in.",
        "must_show": "v28 — turned AWAY from the lit doorway, arms locked, jaw set; the feast light on his back.",
        "must_not_show": "not screaming — cold, hurt anger.",
        "scene": (
            "The elder son stands in the dark courtyard with his back to the "
            "farmhouse's open door, arms crossed hard over his chest, jaw set, "
            "eyes down and burning — the warm feast light and music spilling out "
            "of the doorway behind him onto his shoulders, torch flames wavering "
            "on the wall. He has planted himself; he is not going in. Exactly one "
            "person is in the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b19", "out": "s19-father-came-out.jpeg", "seg": "n10a",
        "window": "94.96-101.19", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["FATHER", "ELDER", "ESTATE"],
        "narration": ("So the father left his own feast, and went out again — "
                      "this time to the son who had never left."),
        "must_show": "v28 — the father coming OUT through the lit door into the dark, toward the elder son; the second going-out of the story.",
        "must_not_show": "no rebuke in the father's posture — he comes to entreat.",
        "scene": (
            "The father steps out through the farmhouse's lamplit doorway into "
            "the dark courtyard, leaving his own feast behind him, one hand still "
            "on the doorframe and the other already reaching gently toward the "
            "elder son, who stands apart in the shadows with his arms crossed, "
            "face turned away. The doorway light spills past the father into the "
            "dark between them. Exactly two people are in the frame; each has two "
            "arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b20", "out": "s20-the-hurt-poured-out.jpeg", "seg": "n10b",
        "window": "101.19-111.74", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["FATHER", "ELDER", "ESTATE"],
        "narration": ("The older son's hurt poured out. All these years I have "
                      "served you. I never disobeyed you. And you never gave me "
                      "even a young goat, to celebrate with my friends."),
        "must_show": "the complaint in motion — the elder son gesturing with both hands, years of hurt; the father standing in it, listening.",
        "must_not_show": "the father does not argue back; he listens.",
        "scene": (
            "In the torchlit courtyard the elder son has turned on his father at "
            "last, both work-hardened hands thrown out mid-gesture, his dusty "
            "face cracked open with years of hurt as the words pour out of him — "
            "and the father stands close and still in the doorway light, taking "
            "every word, his lined face full of sorrow and love, making no answer "
            "yet. Exactly two people are in the frame; each has two arms, two "
            "hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b21", "out": "s21-lo-these-many-years.jpeg", "seg": "j4",
        "window": "111.74-125.05", "wide": False, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["FATHER", "ELDER"],
        "narration": ("Lo, these many years do I serve thee... and yet thou never "
                      "gavest me a kid, that I might make merry with my friends. "
                      "(Luke 15:29)"),
        "must_show": "tight on the elder son's face at the rawest of the complaint; the father's hand beginning to reach for his arm.",
        "must_not_show": "no contempt on either face — hurt on one, love on the other.",
        "scene": (
            "A tight two-shot in warm torchlight: the elder son's face fills one "
            "side of the frame, eyes wet with anger and old invisible hurt, "
            "mid-word — and from the other side his father's weathered hand is "
            "just arriving on his forearm, the father's face soft behind it, "
            "hearing him all the way to the end. Exactly two people are in the "
            "frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r002-b22", "out": "s22-the-last-words.jpeg", "seg": "n11",
        "window": "125.05-130.17", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["FATHER", "ELDER", "ESTATE"],
        "narration": ("The father didn't argue with him, either. Jesus gave him "
                      "the last words of the story."),
        "must_show": "the two of them face to face in the doorway light, the complaint spent, the father's hands on his shoulders.",
        "must_not_show": "not reconciled yet — held, listened to, on the edge.",
        "scene": (
            "In the spill of warm light from the open farmhouse door the father "
            "now stands square in front of his elder son with both hands resting "
            "on the young man's shoulders, their faces close, the son's anger "
            "spent into raw stillness, his arms fallen to his sides — the whole "
            "courtyard dark and quiet around the two of them, the feast a warm "
            "murmur behind the door. Exactly two people are in the frame; each "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b23", "out": "s23-all-that-i-have-is-thine.jpeg", "seg": "j2a",
        "window": "130.17-135.36", "wide": False, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["FATHER", "ELDER"],
        "narration": "Son, thou art ever with me, and all that I have is thine. (Luke 15:31)",
        "must_show": "close on the father's face saying the tender sentence — all warmth, no rebuke.",
        "must_not_show": "no tears streaming; deep, quiet tenderness.",
        "scene": (
            "Close on the father's deeply lined face in warm torchlight, his eyes "
            "steady and shining on his elder son's, the silver-grey beard framing "
            "the gentlest expression in the whole story — a father telling his "
            "faithful boy that everything he has is already his. The elder son's "
            "shoulder and jaw are just in frame, listening. Each visible hand has "
            "five fingers."
        ),
    },
    {
        "id": "v2-r002-b24", "out": "s24-the-open-door.jpeg", "seg": "j2b",
        "window": "135.36-146.21", "wide": True, "jesus": False, "ref": False,
        "char_refs": ["CAST-REF-V2/father-ref.jpeg", "CAST-REF-V2/elder-ref.jpeg"],
        "locks": ["FATHER", "ELDER", "ESTATE"],
        "narration": ("It was meet that we should make merry, and be glad: for "
                      "this thy brother was dead, and is alive again; and was "
                      "lost, and is found. (Luke 15:32)"),
        "must_show": ("the story's unresolved end — the father gesturing toward "
                      "the open lamplit door and the feast beyond it, the elder "
                      "son at the threshold, the choice hanging."),
        "must_not_show": "do NOT show him going in or turning away — the parable ends before he chooses.",
        "scene": (
            "The father stands beside the farmhouse's wide-open door, one arm "
            "around his elder son's shoulders and the other stretched open toward "
            "the bright doorway — inside, the feast is visible and warm, the "
            "younger brother in his deep wine-red robe glimpsed among the "
            "celebrating household — and the elder son stands at the very "
            "threshold, caught in the light, his face undecided between the dark "
            "courtyard and the open door. The story ends here, with the door "
            "open. Every figure has two arms, two hands and one head."
        ),
    },
]
