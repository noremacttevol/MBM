#!/usr/bin/env python3
"""V2 beat map — row 98, build-98-mary-her-name (John 20:11-18).

COVERAGE: 21 pictures over 121.0 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (John 20:11-18 KJV):
  v11   "Mary stood without at the sepulchre WEEPING" — she stayed
        when the others ran to tell.
  v13   "They have taken away my Lord, and I KNOW NOT WHERE they have
        laid him."
  v14-15 "she TURNED herself back, and SAW JESUS standing, and KNEW
        NOT that it was Jesus... she, SUPPOSING HIM TO BE THE
        GARDENER... Sir, if thou have borne him hence, tell me where
        thou hast laid him, and I WILL TAKE HIM AWAY."
  v16   "Jesus saith unto her, MARY. She turned herself, and saith
        unto him, RABBONI; which is to say, MASTER." — one word, her
        name; recognition instant.
  v17   "TOUCH ME NOT; for I am not yet ascended to my Father: but GO
        TO MY BRETHREN, and say unto them, I ascend unto MY FATHER,
        AND YOUR FATHER; and to MY GOD, AND YOUR GOD."
  v18   Mary "TOLD the disciples that she had SEEN THE LORD" — the
        first witness and first preacher of the resurrection.

SETTING: the SAME garden tomb as row 97 — the TOMB lock matches row
97's word for word. The risen Jesus appears NATURAL — cream robe, warm
and real, NO wounds shown or referenced visually, no shining effects.

TIME OF DAY: early risen MORNING throughout — first gold sun through
the olive trees, strengthening to full clear morning by the close.

CONTENT-CARE: no flags. Mary's grief rendered with dignity — real
weeping, never wretched; the touch-me-not gentle, never a rebuff.

CHANGING CONDITION (kept OUT of the locks): Mary — weeping and blind
with grief, then turned, then knowing, then running; the recognition —
withheld, then given whole in one name.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "TOMB": (
        "TOMB LOCK: a rock-cut garden tomb — a low doorway cut into "
        "a limestone face, a GREAT DISC STONE rolled aside from the "
        "opening, a hewn stone bench within, olive trees and spring "
        "flowers in the garden around. The same face, stone and "
        "garden throughout."
    ),
    "MARY": (
        "MARY LOCK: Mary Magdalene is the same woman in every shot — "
        "about thirty, long dark hair under a slipped DEEP "
        "MADDER-RED shawl, a plain DEEP MADDER-RED dress (never "
        "cream, never white), her face tear-streaked and utterly "
        "dignified; devotion its strongest feature."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r098-b01", "out": "s01-mary-magdalene-stayed-behind-at.jpeg", "seg": "n0",
        "window": "0.28-7.39", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOMB", "MARY"],
        "narration": (
            "Mary Magdalene stayed behind at the tomb, weeping. When she was "
            "asked why she was crying, all she had was one answer."
        ),
        "must_show": "SCRIPTURE-EXACT: the stayer — Mary alone outside the open tomb in the early gold light, bent with weeping by the doorway; the garden empty around her grief.",
        "must_not_show": "no halo, glare or rim-light; the weeping REAL and dignified — a woman who cannot leave.",
        "scene": (
            "When everyone else has run "
            "with the news, one figure "
            "stays: Mary in her madder-red "
            "at the tomb's open door, bent "
            "into her weeping with one "
            "hand against the cold "
            "limestone, the early gold "
            "light finding her alone among "
            "the olive trees — the woman "
            "who could not leave the last "
            "place he had been, even now "
            "that he is not in it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r098-b02", "out": "s02-they-have-taken-away-my.jpeg", "seg": "w13",
        "window": "7.95-12.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": (
            "They have taken away my Lord, and I know not where they have "
            "laid him."
        ),
        "must_show": "SCRIPTURE-EXACT: the one answer — close on Mary's tear-streaked face saying it: loss doubled, the not-knowing worse than the grave.",
        "must_not_show": "no halo, glare or rim-light; the words the WHOLE of her — nothing left in the face but the missing.",
        "scene": (
            "Close on the only sentence "
            "grief has left her: the "
            "tear-streaked face shaping it "
            "into the morning air — THEY "
            "HAVE TAKEN AWAY MY LORD — the "
            "possessive still hers and "
            "held onto with both hands — "
            "AND I KNOW NOT WHERE — a "
            "woman robbed twice over, of "
            "the man and then of the one "
            "poor comfort of knowing where "
            "what remained of him lay. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r098-b03", "out": "s03-she-had-lost-him-once.jpeg", "seg": "n0b",
        "window": "13.63-18.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB", "MARY"],
        "narration": (
            "She had lost him once already. Now it felt like she had lost "
            "even the place where he lay."
        ),
        "must_show": "the double loss — Mary at the tomb's doorway looking in at the empty bench and folded linen: even the anchor of a grave taken.",
        "must_not_show": "no halo, glare or rim-light; the emptiness seen THROUGH her — the bench beyond her grieving profile.",
        "scene": (
            "She stands in the low doorway "
            "and looks at the second "
            "loss: past her grieving "
            "profile the hewn bench lies "
            "bare in the slanting gold, "
            "the folded linen where the "
            "body should be — the one "
            "fixed point grief had left "
            "her, a place to bring spices "
            "and sit near, emptied out "
            "like everything else — a "
            "woman discovering you can be "
            "bereaved even of a grave. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r098-b04", "out": "s04-she-turned-and-saw-a.jpeg", "seg": "n1a + jv15",
        "window": "19.20-23.48", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": "She turned and saw a man standing there. Woman, why weepest thou?",
        "must_show": "SCRIPTURE-EXACT: the turning — Mary turned from the door to find a man standing on the garden path in the morning light; his face gentle, hers unseeing through tears.",
        "must_not_show": "no halo, glare or rim-light on him; NOTHING supernatural in his appearance — a man in the garden, unrecognized.",
        "scene": (
            "A presence turns her from the "
            "doorway: a man standing on "
            "the garden path in the gold "
            "morning light, plain and real "
            "among the olive trees — "
            "asking her, gently, WOMAN, "
            "WHY WEEPEST THOU — and Mary "
            "looking straight at the face "
            "she has loved best in the "
            "world and seeing only a "
            "stranger through the blur, "
            "grief standing between her "
            "eyes and the answer to "
            "itself. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b05", "out": "s05-whom-seekest-thou-why-are.jpeg", "seg": "jv15 + n1a2",
        "window": "23.48-27.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": "whom seekest thou? Why are you crying?",
        "must_show": "the questions — close on the two faces: his warm and knowing, hers blind with tears; the asker already the answer.",
        "must_not_show": "no halo, glare or rim-light; HIS knowing gentle — a game of love, not a test.",
        "scene": (
            "Close on the tender absurdity "
            "of the moment: his warm brown "
            "eyes resting on her with all "
            "the knowing in the world — "
            "WHOM SEEKEST THOU — the "
            "question asked by its own "
            "answer, love inquiring after "
            "itself — while her blurred "
            "eyes search past him down the "
            "path for a corpse, standing "
            "one arm's length from "
            "everything she is looking "
            "for. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b06", "out": "s06-who-is-it-looking-for.jpeg", "seg": "n1a2",
        "window": "28.84-32.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": "Who is it you're looking for? She did not know the voice yet.",
        "must_show": "the not-yet — close on Mary's face at the voice: something almost stirring at the edge of it, not yet breaking through.",
        "must_not_show": "no halo, glare or rim-light; the ALMOST readable — recognition circling, not landing.",
        "scene": (
            "Close on her face as the "
            "voice works at its locked "
            "door: something in the timbre "
            "reaching down past the grief "
            "and stirring — her brows "
            "flickering, the weeping "
            "pausing half a breath as if "
            "listening for a bird heard "
            "once long ago — and then the "
            "tears closing back over it, "
            "the voice filed as a "
            "stranger's kindness, the "
            "door's key turning and not "
            "yet turned. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b07", "out": "s07-thinking-he-was-the-gardener.jpeg", "seg": "n1b",
        "window": "36.36-39.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": "Thinking he was the gardener, she pleaded with him.",
        "must_show": "SCRIPTURE-EXACT: supposing him the gardener — Mary turned full to him in pleading, hands beginning to reach; the garden's dawn work-light making the mistake plausible.",
        "must_not_show": "no halo, glare or rim-light; the mistake HONEST — a man in a garden at dawn; her plea desperate and dignified.",
        "scene": (
            "She takes him for the only "
            "man who would be here at "
            "this hour: the gardener, "
            "standing among his olive "
            "trees in the work-light of "
            "dawn — and she turns to him "
            "with her hands beginning to "
            "reach, grief bypassing all "
            "pride, a woman ready to beg "
            "a groundskeeper for the "
            "location of a body — the "
            "Lord of the garden mistaken "
            "for its caretaker, and "
            "letting the mistake stand "
            "one moment more. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r098-b08", "out": "s08-sir-if-thou-have-borne.jpeg", "seg": "w15",
        "window": "39.80-45.83", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": (
            "Sir, if thou have borne him hence, tell me where thou hast laid "
            "him, and I will take him away."
        ),
        "must_show": "SCRIPTURE-EXACT: the plea — close on Mary mid-plea, hands open and asking: TELL ME WHERE; the offer already forming behind the words.",
        "must_not_show": "no halo, glare or rim-light; the plea COURTEOUS through devastation — SIR, from a breaking heart.",
        "scene": (
            "Close on courtesy holding a "
            "breaking heart together: SIR "
            "— the word offered properly "
            "even now, her open hands "
            "asking in front of her — IF "
            "THOU HAVE BORNE HIM HENCE, "
            "TELL ME WHERE — the whole "
            "plea structured like a "
            "business inquiry and "
            "trembling at every joint, a "
            "woman negotiating with a "
            "stranger for the one thing "
            "left she knows how to want. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r098-b09", "out": "s09-sir-if-you-carried-him.jpeg", "seg": "n1b2",
        "window": "47.34-51.91", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": (
            "Sir, if you carried him off, just tell me where you put him, "
            "and I will go and get him."
        ),
        "must_show": "the offer — Mary's small frame squared with impossible resolve: I WILL take him; the intention absolute in her stance.",
        "must_not_show": "no halo, glare or rim-light; the resolve SERIOUS — nothing cute about it; love proposing the impossible flatly.",
        "scene": (
            "The frame takes her measure "
            "as she makes the offer: a "
            "small woman, spent with "
            "weeping, shoulders squared "
            "in the dawn light — I WILL "
            "GO AND GET HIM — the "
            "arithmetic absurd and "
            "entirely settled: she will "
            "carry a grown man's body "
            "herself, in her arms, "
            "however far, to wherever "
            "honor can be done it — and "
            "every line of her stance "
            "means it. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b10", "out": "s10-she-was-a-woman-offering.jpeg", "seg": "n1b2",
        "window": "51.91-58.44", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": (
            "She was a woman offering to carry a grown man's body home by "
            "herself. That is how much she loved him."
        ),
        "must_show": "the love measured — the two figures on the garden path: her small pleading frame before the listening man; devotion's size against her smallness.",
        "must_not_show": "no halo, glare or rim-light; HIS face moved — the listener receiving the full weight of being loved like this.",
        "scene": (
            "The wide gold garden holds "
            "the measurement: the small "
            "madder-red figure with her "
            "impossible offer standing "
            "before the quiet man on the "
            "path — and on his listening "
            "face, had she eyes to see "
            "it, something moving deep: "
            "the Lord of all things "
            "being told, by a woman too "
            "small to lift him, exactly "
            "how far she would carry him "
            "— love outbidding its own "
            "strength, witnessed by its "
            "object. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b11", "out": "s11-he-said-one-word-her.jpeg", "seg": "n2 + j1",
        "window": "59.00-62.23", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": "He said one word. Her name. Mary.",
        "must_show": "SCRIPTURE-EXACT: the name — close on his face speaking the single word, all the warmth of three years in it; the word mid-air between them.",
        "must_not_show": "no halo, glare or rim-light; ONE word's weight — the frame intimate, the world reduced to two people and a name.",
        "scene": (
            "Everything narrows to one "
            "word: his face close in the "
            "morning gold, the warm brown "
            "eyes on her, and the name "
            "leaving him the way he has "
            "always said it — MARY — not "
            "loud, not urgent, just hers: "
            "the two syllables that no "
            "gardener would know and no "
            "grief could mishear, crossing "
            "the small morning air between "
            "them with three years of "
            "every kindness riding on "
            "them. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b12", "out": "s12-rabboni-mary-and-she-answered.jpeg", "seg": "w16 + n3",
        "window": "63.73-69.87", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": "Rabboni. Mary. And she answered him — Rabboni.",
        "must_show": "SCRIPTURE-EXACT: the recognition — Mary spun fully around, face blazing alive, the answer bursting from her: RABBONI; the whole garden turned to joy.",
        "must_not_show": "no halo, glare or rim-light; the turn WHOLE-BODY — grief's posture shattered, joy physical.",
        "scene": (
            "The name lands and she "
            "SPINS: the whole grieving "
            "architecture of her shattering "
            "in one turn, the shawl "
            "slipping, her face blazing "
            "alive through the half-dried "
            "tears — RABBONI — the answer "
            "bursting out of her like "
            "water from a struck rock, "
            "her feet already closing the "
            "distance — one word each, "
            "traded across a garden path, "
            "and death's whole kingdom "
            "bankrupted between them. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r098-b13", "out": "s13-it-means-master-in-her.jpeg", "seg": "n3",
        "window": "69.87-74.57", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": (
            "It means Master, in her own language, the word she had always "
            "called him."
        ),
        "must_show": "the old word — the two faces close in the gold light: her RABBONI still on her lips, his receiving it; the familiar title restored to its owner.",
        "must_not_show": "no halo, glare or rim-light; the intimacy of HABIT — a word worn smooth by daily use, home again.",
        "scene": (
            "Close on the old word coming "
            "home: RABBONI still shaping "
            "her lips — the everyday "
            "title of a thousand ordinary "
            "mornings, the word for "
            "handing him bread and asking "
            "him questions on the road — "
            "restored in one breath to "
            "its living owner, and his "
            "face receiving it the way a "
            "man receives his own name at "
            "his own door after a long "
            "journey: gladly, and as of "
            "right. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b14", "out": "s14-and-instantly-she-knew-grief.jpeg", "seg": "n3",
        "window": "74.57-84.09", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": (
            "And instantly she knew. Grief flipped to joy in a single "
            "heartbeat — he was alive, and he had come looking for HER, by "
            "name."
        ),
        "must_show": "the flip — the garden wide and golden: Mary rushing toward him, arms out, face transfigured by joy; the risen man warm and real receiving her rush.",
        "must_not_show": "no halo, glare or rim-light; the joy TOTAL — the same garden that held her weeping now holding her running.",
        "scene": (
            "The same garden that held "
            "her weeping now holds her "
            "running: Mary flying the few "
            "steps between them with her "
            "arms out and her face "
            "transfigured, the morning "
            "gold everywhere at once — "
            "alive, ALIVE, and not only "
            "alive but HERE, come to this "
            "garden at this hour for one "
            "audience: a weeping woman he "
            "wanted found first — sought, "
            "by name, before the whole "
            "world was told. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r098-b15", "out": "s15-he-asked-her.jpeg", "seg": "n1a2",
        "window": "27.96-28.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": "he asked her.",
        "must_show": "the asking held — the brief close beat: his gentle questioning face toward her bowed weeping one; the exchange mid-air.",
        "must_not_show": "no halo, glare or rim-light; the beat QUIET — one question travelling.",
        "scene": (
            "One quiet beat between "
            "question and answer: his "
            "gentle face inclined toward "
            "her bowed one in the "
            "morning light, the asking "
            "still hanging in the air "
            "between them — patient, "
            "unhurried, in no rush at "
            "all to be recognized — a "
            "kindness content to stand "
            "unknown at arm's length "
            "from the one it came for, "
            "for exactly as long as she "
            "needs. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b16", "out": "s16-touch-me-not-for-i.jpeg", "seg": "jv17",
        "window": "84.63-98.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": (
            "Touch me not; for I am not yet ascended to my Father: but go to "
            "my brethren, and say unto them, I ascend unto my Father, and "
            "your Father; and to my God, and your God."
        ),
        "must_show": "SCRIPTURE-EXACT: the gentle hold and the sending — his raised hand soft between them, the commission passing; her rush stilled into listening, mission arriving.",
        "must_not_show": "no halo, glare or rim-light; the touch-me-not TENDER — no recoil, a gentle stay; her face receiving a job, not a rejection.",
        "scene": (
            "His hand rises soft between "
            "them — not a wall, a stay: "
            "TOUCH ME NOT, FOR I AM NOT "
            "YET ASCENDED — and her rush "
            "stills into listening as "
            "something better than an "
            "embrace is handed over: GO "
            "TO MY BRETHREN — SAY UNTO "
            "THEM — MY FATHER AND YOUR "
            "FATHER — the widest words "
            "ever spoken in a garden, "
            "given first into the keeping "
            "of the woman who stayed. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r098-b17", "out": "s17-through-the-tears-she-could.jpeg", "seg": "n1a2",
        "window": "32.69-35.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": "Through the tears, she could not even see his face.",
        "must_show": "the blur — Mary's tear-flooded eyes close, the man's shape soft and unresolved beyond them; grief as a veil over the answer.",
        "must_not_show": "no halo, glare or rim-light; the blur HERS — his figure gently out of focus past her flooded eyes.",
        "scene": (
            "Close on the veil grief "
            "makes: her eyes flooded and "
            "shining in the morning "
            "light, lashes heavy with it "
            "— and beyond them, soft and "
            "unresolved as a figure seen "
            "through rain, the shape of "
            "the man on the path: near "
            "enough to touch, dear "
            "enough to die for, and "
            "unrecognizable through the "
            "very tears being wept for "
            "him. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b18", "out": "s18-hold-on-to-me-yet.jpeg", "seg": "n4a",
        "window": "99.71-103.71", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": (
            "Don't hold on to me yet, he told her — I haven't gone up to my "
            "Father."
        ),
        "must_show": "the yet — close on the gentle exchange: his face warm over the soft staying hand; the YET's promise legible — this is pause, not parting.",
        "must_not_show": "no halo, glare or rim-light; NO hurt on Mary — the yet understood as promise.",
        "scene": (
            "Close on the gentlest word "
            "in the sentence: YET — his "
            "face warm above the softly "
            "staying hand, nothing of "
            "refusal anywhere in it — "
            "not yet, which is a promise "
            "wearing work clothes — and "
            "Mary's face taking it "
            "rightly: no wound, no "
            "stepping back of the heart, "
            "just the joyful obedient "
            "recalibration of a woman "
            "who has him back and can "
            "afford to wait for the "
            "embrace. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r098-b19", "out": "s19-go-to-my-brothers-and.jpeg", "seg": "n4a",
        "window": "103.71-109.55", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TOMB", "MARY"],
        "narration": (
            "Go to my brothers and tell them I'm going to my Father and your "
            "Father, to my God and your God."
        ),
        "must_show": "the commission — his arm extended toward the city beyond the garden, Mary turning along the line of it; the message and the direction both given.",
        "must_not_show": "no halo, glare or rim-light; the sending JOYFUL — her body already leaning into the errand.",
        "scene": (
            "The commission gets its "
            "compass: his arm sweeping "
            "out past the olive trees "
            "toward the waking city where "
            "ten heartbroken men are "
            "hiding behind a locked door "
            "— GO TO MY BROTHERS — and "
            "Mary turning along the line "
            "of his arm with her whole "
            "body leaning into the "
            "errand, the message already "
            "arranging itself behind her "
            "shining eyes: my Father AND "
            "yours; my God AND yours. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r098-b20", "out": "s20-he-gave-her-the-message.jpeg", "seg": "n4a",
        "window": "109.55-113.32", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOMB", "MARY"],
        "narration": "He gave her the message, and he sent her to carry it.",
        "must_show": "the going — Mary running full-stride down the garden path toward the city in the risen morning, shawl flying; the first courier of the best news.",
        "must_not_show": "no halo, glare or rim-light; the run JOY'S — skirts gathered, feet flying, nothing held back.",
        "scene": (
            "And she RUNS: down the "
            "garden path in the full "
            "risen morning, skirts "
            "gathered in both fists, the "
            "madder shawl streaming off "
            "her shoulders, feet flying "
            "over the stones she climbed "
            "weeping in the dark — the "
            "same road, the same woman, "
            "the opposite direction and "
            "the opposite heart — the "
            "first courier in history to "
            "carry the news that outruns "
            "death, running like it. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r098-b21", "out": "s21-the-first-person-to-see.jpeg", "seg": "n4b",
        "window": "113.87-120.69", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": (
            "The first person to see the risen Lord, and the first preacher "
            "of the resurrection, was a weeping woman he called by name."
        ),
        "must_show": "the closing image — Mary arrived at the disciples' door, face alight, hand flung back toward the garden: I HAVE SEEN THE LORD; the first sermon, mid-delivery.",
        "must_not_show": "no halo, glare or rim-light; her AUTHORITY the picture — a woman believed by her own blazing face before a word lands.",
        "scene": (
            "The closing frame catches "
            "the first sermon ever "
            "preached on a risen Lord: "
            "Mary arrived breathless in "
            "the doorway of the hidden "
            "room, face blazing with "
            "what it has seen, one hand "
            "flung back toward the "
            "garden and the morning — I "
            "HAVE SEEN THE LORD — "
            "stunned bearded faces "
            "lifting all around the "
            "dim room toward a weeping "
            "woman called by name, "
            "promoted by that name to "
            "apostle of the apostles. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
]
