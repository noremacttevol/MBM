#!/usr/bin/env python3
"""V2 beat map — row 9, build-09-rich-ruler (Mark 10:17-22).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 31 pictures against V1's 8 unique stills, over
177.4 s — 5.7 s per picture, the band rows 5-8 shipped at.

⚠️ THIS IS THE APP'S FOUNDING STORY. MBM's own CLAUDE.md ends its gospel
principles with the sentence "Jesus let the rich young ruler walk away. This app
does too." Everything MBM refuses to do — no pressure, no manipulation, no
chasing, no lowered bar — is argued from these six verses. So two frames in this
build carry more weight than any other picture in the row, and if either is
wrong the video is wrong no matter how good the rest is:

  b12 — "Jesus, looking at him, loved him." Mark says it about this man and no
        one else in his gospel. The love has to be plainly, unmistakably ON THE
        FACE. Not pity, not sadness, not disappointment: love.
  b29 — Jesus watching him go, still loving him. No anger, no relief, no
        crossed arms, no turning away first. He stands there and lets him leave.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 10:17-22 KJV):
  v17  "there came one RUNNING, and KNEELED to him" — both things are socially
       humiliating for a wealthy man, and the narration spends fourteen seconds
       on exactly that. b02-b05 are built to make a modern viewer feel it.
  v19  Jesus lists commandments from the second table — the ones about how you
       treat PEOPLE. The narration keeps that: don't cheat, don't steal, don't
       lie, honour your parents. Not one of them is about money.
  v20  "all these have I observed FROM MY YOUTH" — and the narration insists he
       meant it. He is NEVER painted as smug, boastful or hypocritical. He is a
       good man who did the work, and the story only lands if the viewer likes
       him.
  v21  "One thing thou lackest ... and come, TAKE UP THE CROSS, AND FOLLOW ME."
       The last clause is the same call the fishermen got. n3b makes that
       explicit, so b21 puts Peter, Andrew, James and John in frame — the men
       who received this identical invitation and took it.
  v22  "he was SAD at that saying, and went away GRIEVED: for he had great
       possessions." He does not argue, sneer or storm off. Grief only.

  NOT IN THIS BUILD: v18 ("Why callest thou me good?") is not in the narration,
  so it gets no frame. We picture what is narrated.

CONTENT-CARE: row 9 is not in the §3 flag table = GREEN.

TIME-OF-DAY — READ THIS BEFORE FLAGGING A SUNSET AS A DEFECT: this build ENDS
at sunset on purpose. The narration states it outright — "The road emptied. The
sun went down." So b30 and b31 are golden low light and that is CORRECT here.
This is not the row-11 storm error (Mark 4:35 is night and was rejected for
sunset colouring); there the scripture set the hour and the picture disobeyed it,
here the narration sets the hour and the picture obeys. Everything before b30 is
bright ordinary daylight.

THE ONE THING QC MUST WATCH ACROSS THIS ROW: the young man must stay LIKEABLE in
every single frame. The temptation the model will reach for is a sneering rich
villain, and that reading destroys the story — Jesus loved him, and the viewer
has to be able to see why.
"""

LOCKS = {
    "RULER": (
        "RICH YOUNG MAN LOCK: the young man is the same person in every shot — a "
        "Jewish man of about thirty-two, handsome and well-kept, warm olive skin, a "
        "neatly trimmed short dark beard, tidy dark hair, and large earnest "
        "intelligent brown eyes in an open, likeable, entirely sincere face. He is "
        "plainly wealthy: a finely woven DEEP TYRIAN-PURPLE outer robe with an "
        "embroidered dark-gold border, worn over a DEEP INDIGO tunic, a good leather "
        "belt with a silver buckle, several gold rings on his fingers and fine "
        "leather sandals (never cream, never white). His face is shown clearly and "
        "is never smug, sneering or arrogant."
    ),
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect).
    "ROAD": (
        "ROAD LOCK: a dusty road leading out of a small Judean town — packed pale "
        "earth rutted by carts, low dry-stone walls on both sides, olive terraces and "
        "fig trees on the slopes, the town's flat-roofed limestone houses and its "
        "gateway behind, and dry hills opening ahead where the road runs on. "
        "Townspeople along the road are ordinary working folk in SATURATED DEEP earth "
        "colours — dark chocolate brown, deep russet, burnt ochre, dark olive and "
        "dusty indigo wool. None of them wears off-white, ivory or any near-white "
        "cloth."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the disciples travelling with him are the same group "
        "throughout — eight or nine working Galilean men between twenty and forty, "
        "weathered and dusty from the road, with travel bags and staffs. They wear "
        "wool tunics in SATURATED DEEP colours — rust-brown, deep russet, dark olive, "
        "blue-grey and dusty indigo — belted with rope or leather. None of them wears "
        "off-white, ivory or any near-white cloth. Their faces are shown clearly."
    ),
    "POOR": (
        "POOR LOCK: the poor of the town sit along the wall by the gateway — a blind "
        "old man with a wooden bowl set in front of him, a thin mother with two small "
        "children against her, a man with a crutch, an old woman with her hand out. "
        "Their clothing is worn to threads and heavily patched, in faded dust-grey, "
        "washed-out brown and dull earth colours. They are painted with dignity and "
        "never as grotesque or pitiable spectacle."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------------ n0 — the running ----
    {
        "id": "v2-r009-b01", "out": "s01-setting-out.jpeg", "seg": "n0 p1",
        "window": "0.28-4.38", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "ROAD"],
        "narration": ("Jesus was setting out on a journey when a young man came "
                      "running down the road after him."),
        "must_show": "Jesus and the disciples already on the road out of town, and far behind them a small figure running to catch up.",
        "must_not_show": "no halo, glare or rim-light; the runner is distant and not yet identifiable as wealthy.",
        "scene": (
            "Bright mid-morning on the road out of the town. Jesus walks at the front "
            "of a loose group of disciples with their bags and staffs, already some "
            "way along the packed earth between the dry-stone walls, heading toward "
            "the open hills. Far back down the road behind them, small with distance, "
            "a lone figure is running hard to catch them up, a plume of dust behind "
            "his heels. The town gateway stands beyond him. The camera is back far "
            "enough to hold the group and the distant runner in one frame. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b02", "out": "s02-running.jpeg", "seg": "n0 p2-p3",
        "window": "4.38-7.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["RULER", "ROAD"],
        "narration": "Running. You need to understand what that looked like.",
        "must_show": "him at FULL RUN — expensive robe hauled up out of his own way, gold rings on the pumping hand, dust flying, dignity abandoned — while townspeople turn and stare.",
        "must_not_show": "not a dignified jog; he is genuinely sprinting and it looks undignified, which is the point. Do not put Jesus in this frame.",
        "scene": (
            "The young man is at a flat sprint up the middle of the road, caught "
            "mid-stride with both feet off the ground. He has dragged the skirt of his "
            "fine deep-purple robe up in one fist to free his legs, the embroidered "
            "hem swinging, his other hand pumping with the gold rings flashing on it, "
            "his tidy hair come loose and dust kicking up behind his good sandals. "
            "Along the walls on both sides townspeople have stopped what they are "
            "doing and turned to stare after him, a woman with a jar frozen halfway "
            "up. The camera is back far enough to see him head to sandals. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b03", "out": "s03-beneath-them.jpeg", "seg": "n0b p1-p3",
        "window": "8.49-17.26", "wide": True, "jesus": False, "ref": False,
        "locks": ["RULER", "ROAD"],
        "narration": ("This man was wealthy — fine robes, gold rings, a name people "
                      "knew. Men like that did not run in public. It was beneath them."),
        "must_show": "the social cost: he runs past two other well-dressed men of his own class who have stopped dead and are watching him with open disapproval, one saying something to the other.",
        "must_not_show": "the two rich men are not comic and not cruel — just embarrassed for him; and the young man does not care, which is what makes him worth loving.",
        "scene": (
            "Still running, the young man passes two other well-dressed men of his own "
            "rank standing at the roadside in good dark robes with silver at their "
            "belts and servants behind them. Both have stopped dead to watch him go "
            "by — one with his brows up and his mouth open, the other leaning in to "
            "say something to him, both plainly appalled that a man like that would "
            "run in the street. The young man is past them without a glance, his eyes "
            "fixed up the road, his purple robe still hauled up in his fist. Bright "
            "daylight and dust. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b04", "out": "s04-he-reached-him.jpeg", "seg": "n0b p4a",
        "window": "17.26-19.8", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RULER", "DISCIPLES", "ROAD"],
        "narration": "He ran anyway, in front of everyone,",
        "must_show": "he arrives — pulling up hard in front of Jesus, chest heaving, out of breath; the disciples turning in surprise.",
        "must_not_show": "no halo, glare or rim-light; he has not knelt yet.",
        "scene": (
            "The young man has pulled up hard in front of Jesus on the road, skidding "
            "the last step in the dust, one hand out to steady himself and his chest "
            "heaving for air, sweat on his face and his fine robe dishevelled and "
            "dusty at the hem. Jesus has stopped and turned to face him, unhurried and "
            "open. The disciples around them have halted mid-step and turned in, "
            "surprised, one still holding his staff half raised. Bright daylight on "
            "the pale road. The camera is back far enough to hold them all head to "
            "sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b05", "out": "s05-knees-in-the-dust.jpeg", "seg": "n0b p4b",
        "window": "19.8-22.42", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RULER", "DISCIPLES", "ROAD"],
        "narration": "and dropped to his knees in the dust at Jesus's feet.",
        "must_show": "the expensive purple robe going down into the dirt of the road — both knees in the dust at Jesus's feet, in front of everyone.",
        "must_not_show": "no halo, glare or rim-light; nobody is helping him up or pushing him down; the dust on the fine cloth must be visible and must read as costly.",
        "scene": (
            "The young man has gone down onto both knees in the dirt of the road right "
            "at Jesus's feet, his fine deep-purple robe spread and already greying with "
            "dust where it touches the ground, his face lifted. Jesus stands over him "
            "looking down, calm and attentive, not stepping back. Around them the "
            "disciples and a few townspeople have gone quiet and still, watching a "
            "wealthy man kneel in the road. Hard bright daylight, dust hanging in the "
            "air. The camera is back far enough to see the kneeling man and Jesus head "
            "to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b06", "out": "s06-good-master.jpeg", "seg": "s17",
        "window": "22.95-26.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["RULER"],
        "narration": ("Good Master, what shall I do that I may inherit eternal life? "
                      "(Mark 10:17)"),
        "must_show": "close on his upturned face from his knees — earnest, breathless, hungry; a man asking the question of his life.",
        "must_not_show": "no performance, no crowd-pleasing, nothing theatrical — he is not putting on a show; do not put Jesus in this frame.",
        "scene": (
            "Close on the young man's face from just above, looking up from his knees. "
            "He is still breathing hard from the run, damp hair on his forehead, dust "
            "on his cheek, and his large dark eyes are wide and fixed upward with "
            "complete earnestness. His hands have come together in front of his chest "
            "without his noticing. It is the face of a man asking the one question he "
            "has carried for years. The sunlit road is soft behind him. Each hand has "
            "five fingers."
        ),
    },
    # -------------------------------------------- n1 — the commandments ----
    {
        "id": "v2-r009-b07", "out": "s07-the-question-he-carried.jpeg", "seg": "n1 p1-p2",
        "window": "27.72-35.06", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RULER", "DISCIPLES", "ROAD"],
        "narration": ("He asked the question he had been carrying, maybe his whole "
                      "life. Good teacher — what do I have to do to live forever with "
                      "God?"),
        "must_show": "the two of them held in the moment after the question — Jesus looking down at him and genuinely listening, the disciples watching from a step back.",
        "must_not_show": "no halo, glare or rim-light; Jesus is not amused, not testing him, not sizing him up — he is listening.",
        "scene": (
            "Jesus stands looking down at the kneeling young man, his head slightly "
            "inclined, his hands loose at his sides, listening — completely present and "
            "in no hurry at all. The young man kneels in the dust looking up, waiting. "
            "The disciples stand a step back in a loose half circle, watching the two "
            "of them, one glancing at another. Bright daylight, the road running away "
            "behind. The camera is back far enough to hold both of them head to "
            "sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b08", "out": "s08-the-commandments.jpeg", "seg": "n1 p3-p7",
        "window": "35.06-43.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RULER"],
        "narration": ("Jesus pointed him to the commandments. Don't cheat anyone. "
                      "Don't steal. Don't lie. Honor your father and your mother."),
        "must_show": "Jesus counting them off on his fingers, plainly and without severity — and the young man's face lifting slightly with each one, nodding, recognising ground he has already covered.",
        "must_not_show": "no halo, glare or rim-light; this is not a test or an accusation — Jesus is being straightforward and the man is not being caught out.",
        "scene": (
            "Close on Jesus and the kneeling young man together. Jesus has one hand "
            "raised between them and is counting the commandments off on his fingers, "
            "two folded down and a third going, his expression plain and matter of "
            "fact with no severity in it at all. Below and in front of him the young "
            "man's upturned face is following every finger, his chin lifting slightly "
            "and his head giving small nods, recognition and something like relief "
            "coming into his eyes — this is ground he has already covered. Bright "
            "daylight. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r009-b09", "out": "s09-since-i-was-a-boy.jpeg", "seg": "n1 p8",
        "window": "43.60-49.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["RULER"],
        "narration": ("And the young man answered: Teacher, I have kept every one of "
                      "them since I was a boy."),
        "must_show": "his face answering — open, direct, meeting Jesus's eyes, telling the simple truth about his own life.",
        "must_not_show": "NOT smug and NOT boastful — the entire story depends on the viewer believing him; do not put Jesus in this frame.",
        "scene": (
            "Close on the young man's face as he answers, still on his knees, looking "
            "straight up and out of the frame at the man in front of him. His "
            "expression is completely open and simple — no pride in it, no performance, "
            "just a plain statement of fact and, underneath it, a hopeful searching "
            "look, as if he is waiting to be told it is enough. Dust on his cheek and "
            "his fine collar. The sunlit road soft behind him."
        ),
    },
    {
        "id": "v2-r009-b10", "out": "s10-he-meant-it.jpeg", "seg": "n1 p9-p12",
        "window": "49.17-59.77", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RULER", "DISCIPLES", "ROAD"],
        "narration": ("And here is the thing. He meant it. This was not a proud man "
                      "showing off. This was a student who had done all the homework, "
                      "kneeling in the dirt, asking if it was enough."),
        "must_show": "the whole picture of him: a rich man on his knees in the dust of a public road in a purple robe, humble and hopeful, with Jesus standing over him and the disciples around.",
        "must_not_show": "no halo, glare or rim-light; nobody is mocking him; he must look sympathetic and serious.",
        "scene": (
            "A wide view of the scene on the road. The wealthy young man kneels in the "
            "dust in the middle of the public way, his fine purple robe dirty at the "
            "knees and hem, his shoulders down and his face turned up — every bit of "
            "his rank set aside and nothing left but the question. Jesus stands close "
            "in front of him looking down at him steadily. The disciples stand around "
            "them in a loose ring, and a few townspeople have stopped further off to "
            "watch. Hard clean daylight, dust in the air, the road and the dry hills "
            "beyond. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b11", "out": "s11-from-my-youth.jpeg", "seg": "s20",
        "window": "60.28-62.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["RULER"],
        "narration": ("Master, all these have I observed from my youth. (Mark 10:20)"),
        "must_show": "very close on his face saying it — quiet, honest, and underneath the honesty a real fear that it still is not enough.",
        "must_not_show": "no pride and no defiance anywhere in the face; do not put Jesus in this frame.",
        "scene": (
            "Very close on the young man's face, filling the frame, as he says it. His "
            "eyes are steady and completely honest, his mouth soft, his brows drawn "
            "very slightly together — and behind the honesty there is a plain, "
            "unhidden fear that all of it still might not be enough. Dust on his skin, "
            "sweat at his temple, the gold at his collar just catching the light. The "
            "background is entirely soft."
        ),
    },
    # ------------------------------------------------ n2 — THE LOOK ----
    {
        "id": "v2-r009-b12", "out": "s12-looking-at-him-loved-him.jpeg", "seg": "n2 p1-p2",
        "window": "64.61-70.02", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Mark writes what happened next in five words. Jesus, looking at "
                      "him, loved him."),
        "must_show": "⚠️ THE MOST IMPORTANT FRAME IN THIS VIDEO. Close on Jesus's face looking down at him, and the expression is unmistakably LOVE — warm, moved, tender, his eyes soft and completely fixed on the man.",
        "must_not_show": "NOT pity. NOT sadness. NOT disappointment. NOT sternness. NOT a knowing look. If this face reads as anything other than love for the person in front of him, the frame is a hard fail and must be regenerated. No halo, glare or rim-light.",
        "scene": (
            "Very close on Jesus's face, filling the frame, looking down and slightly "
            "off camera at the man kneeling in front of him. His eyes have gone soft "
            "and warm and are completely fixed, and there is a small, moved, tender "
            "set to his mouth — the unguarded expression of someone looking at a "
            "person he has just come to love. His head is tipped a little toward the "
            "man. Nothing guarded, nothing withheld, nothing sad. Bright ordinary "
            "daylight on his skin and the road soft and out of focus behind him."
        ),
    },
    {
        "id": "v2-r009-b13", "out": "s13-the-two-of-them.jpeg", "seg": "n2 p3",
        "window": "70.02-74.80", "wide": False, "jesus": True, "ref": REF,
        "locks": ["RULER"],
        "narration": ("Of all the people in Mark's story, this is the one he says it "
                      "about, straight out."),
        "must_show": "the two of them together and held — Jesus looking down with that same love, the young man looking up, the road and everyone else forgotten.",
        "must_not_show": "no halo, glare or rim-light; nobody else's face in focus — this moment belongs to the two of them.",
        "scene": (
            "The two of them close together, Jesus standing and the young man kneeling, "
            "framed tight so that the road and the watching disciples are only soft "
            "shapes behind. Jesus is looking down into his face with that same warm "
            "steady tenderness, and the young man is looking up at him, held, his "
            "own face open and hopeful. Neither of them is moving. Bright daylight, "
            "dust hanging in the air between them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r009-b14", "out": "s14-what-jesus-saw.jpeg", "seg": "n2 p4",
        "window": "74.80-80.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["RULER"],
        "narration": ("Jesus looked at this man — his sincerity, his gold rings, his "
                      "hope — and loved him."),
        "must_show": "exactly what the narration lists, in one frame: the upturned sincere face, the gold rings on his clasped hands, and the hope in his eyes.",
        "must_not_show": "the rings are not sinister and not emphasised as greed — they are simply part of him; do not put Jesus in this frame.",
        "scene": (
            "Close on the young man from Jesus's own eye level, taking in all of him "
            "at once — his upturned earnest face with the dust on it, his hands "
            "clasped together in front of his chest with the gold rings plain on his "
            "fingers, the fine embroidered collar of his purple robe, and his eyes full "
            "of open, uncomplicated hope. Nothing about him is grasping or guarded. "
            "Warm daylight across him and the road soft behind. Each hand has five "
            "fingers."
        ),
    },
    {
        "id": "v2-r009-b15", "out": "s15-with-love-in-his-voice.jpeg", "seg": "n2 p5",
        "window": "80.17-84.86", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("And then, with love in his voice, he said the hardest sentence "
                      "in the book."),
        "must_show": "Jesus beginning to speak — the same warmth still on his face, and something costly arriving behind his eyes because of what he is about to say.",
        "must_not_show": "no hardening of the face, no sternness, no rebuke gathering — the love must still be visibly there while he says the hard thing. No halo, glare or rim-light.",
        "scene": (
            "Close on Jesus as he draws breath and begins to speak, his mouth just "
            "opening on the first word. The warmth from a moment ago is still all over "
            "his face — the soft eyes, the tender set of the mouth — but something "
            "heavy and costly has arrived behind his eyes, the look of a man who knows "
            "exactly what the next sentence is going to do to someone he cares about. "
            "One hand has started to lift. Bright daylight, the road soft behind."
        ),
    },
    # ------------------------------------------------- j1 — one thing ----
    {
        "id": "v2-r009-b16", "out": "s16-sell-whatsoever-thou-hast.jpeg", "seg": "j1 a",
        "window": "85.35-89.0", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RULER", "DISCIPLES", "ROAD"],
        "narration": ("One thing thou lackest: go thy way, sell whatsoever thou hast, "
                      "(Mark 10:21)"),
        "must_show": "Jesus speaking it down to him plainly, the disciples' heads coming up sharply as they hear the terms.",
        "must_not_show": "no halo, glare or rim-light; no anger; the disciples are startled, not smug.",
        "scene": (
            "Jesus speaks down to the kneeling young man, one hand open toward him, his "
            "expression plain and warm and entirely serious. Around them the disciples' "
            "heads have come up sharply — one has turned to stare at Jesus outright, "
            "another has stopped with his water skin halfway to his mouth, a third has "
            "looked at the ground. The young man's face has begun to change. Bright "
            "daylight on the dusty road. The camera is back far enough to hold them "
            "head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b17", "out": "s17-give-to-the-poor.jpeg", "seg": "j1 b",
        "window": "89.0-92.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["POOR", "ROAD"],
        "narration": "and give to the poor, (Mark 10:21)",
        "must_show": "who 'the poor' actually are — the beggars and poor families along the wall by the town gateway, real faces, close enough to matter.",
        "must_not_show": "CONTENT-CARE: painted with dignity, never as grotesque or as pitiable spectacle; nobody is being given anything yet; do not put Jesus in this frame.",
        "scene": (
            "Along the shaded wall beside the town gateway, the poor of the town sit "
            "where they always sit. A blind old man has his empty wooden bowl set out "
            "on the stone in front of him, his face turned up toward the sound of the "
            "street. A thin young mother sits with two small children folded against "
            "her, her patched shawl pulled around all three. A man with a crutch leans "
            "back against the wall and an old woman beside him holds out one open hand. "
            "Their faces are worn and entirely human and they are painted with dignity. "
            "The bright road runs past them. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r009-b18", "out": "s18-come-follow-me.jpeg", "seg": "j1 c",
        "window": "92.0-95.05", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RULER", "ROAD"],
        "narration": ("and thou shalt have treasure in heaven: and come, take up the "
                      "cross, and follow me. (Mark 10:21)"),
        "must_show": "THE INVITATION — Jesus's hand out toward him in open welcome, and the open road behind Jesus running away toward the hills, the way he would be going.",
        "must_not_show": "no halo, glare or rim-light; no literal cross in the frame; the gesture is welcome, never demand.",
        "scene": (
            "Jesus stands over the kneeling man with his hand stretched out toward him, "
            "palm open and turned up in plain welcome, his face warm — the same gesture "
            "a man makes to someone he wants beside him. Beyond his shoulder the road "
            "runs on away from the town toward the open hills, empty and bright, the "
            "way he is going. The young man kneels in the dust looking up at the "
            "offered hand. The camera is back far enough to hold both men and the open "
            "road behind them. Every figure has two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------- n3 — the one thing ----
    {
        "id": "v2-r009-b19", "out": "s19-one-thing-between.jpeg", "seg": "n3 p1-p5",
        "window": "96.57-105.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["RULER"],
        "narration": ("You're missing one thing. Not one more rule. One thing standing "
                      "between you and God. Sell what you have. Give it to the people "
                      "who have nothing."),
        "must_show": "it landing on him — and his own hand having gone, without his noticing, to the gold rings on his other hand and closed around them.",
        "must_not_show": "no greed on his face — it is dawning horror and grief, not avarice; do not put Jesus in this frame.",
        "scene": (
            "Close on the young man kneeling. His face has changed completely — the "
            "hope has gone out of it and his eyes have widened and gone unfocused as "
            "the size of what has been asked arrives on him, his mouth slightly open. "
            "And without any sign that he knows he is doing it, one of his hands has "
            "come across and closed tightly around the gold rings on the fingers of "
            "the other, holding them. Bright daylight, the sunlit road soft behind "
            "him. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r009-b20", "out": "s20-and-then-come.jpeg", "seg": "n3 p6",
        "window": "105.66-108.69", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "And then — come, follow me.",
        "must_show": "close on Jesus's open offered hand held steady in the air, waiting, and his face above it still warm.",
        "must_not_show": "no halo, glare or rim-light; the hand is not withdrawn and not insistent — it simply waits.",
        "scene": (
            "Close on Jesus's outstretched hand held steady and open in the sunlit air, "
            "palm up, fingers relaxed, waiting — and above it his face, still warm, "
            "still looking down at the man, patient and unhurried. The offer is simply "
            "standing there in the air between them. The dusty road is soft and out of "
            "focus beyond. His hand has five fingers."
        ),
    },
    # ------------------------------------------- n3b — the same call ----
    {
        "id": "v2-r009-b21", "out": "s21-the-same-words.jpeg", "seg": "n3b p1-p4",
        "window": "109.24-119.01", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "ANDREW", "JOHN", "JAMES-Z", "ROAD"],
        "narration": ("Hear that last part. It was an invitation. The same words Jesus "
                      "used to call Peter, and Andrew, and James, and John. He was "
                      "being invited into the inner circle."),
        "must_show": "the four men who got this identical call and took it — Peter, Andrew, James and John standing together on the road watching, with an open gap among them where a fifth man could stand.",
        "must_not_show": "they are not smug or possessive about their place — they are watching with real sympathy; do not put Jesus in this frame.",
        "scene": (
            "Four of the disciples stand together at the roadside watching what is "
            "happening — Peter with his arms folded and his heavy brows down, Andrew "
            "beside him, James tall behind them, and young John at the end with his "
            "face open and troubled. All four are dusty from the road with their bags "
            "on their shoulders, ordinary working men who once heard these same words "
            "and followed. Between Peter and John there is a clear open gap in their "
            "line, room enough for one more man to stand. Their faces carry sympathy, "
            "not satisfaction. Bright daylight on the road. The camera is back far "
            "enough to see all four head to sandals. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r009-b22", "out": "s22-could-not-put-it-down.jpeg", "seg": "n3b p5",
        "window": "119.01-122.90", "wide": True, "jesus": False, "ref": False,
        "locks": ["RULER", "ROAD"],
        "narration": ("It just came wrapped in the one thing this man could not put "
                      "down."),
        "must_show": "his eyes gone away from Jesus and back down the road toward the town — toward the house, the land, the life that is already pulling at him.",
        "must_not_show": "he is not sneaking a look; it is involuntary and sad. Do not put Jesus in this frame.",
        "scene": (
            "The young man is still on his knees in the road, but his head has turned "
            "and his eyes have gone away down the road behind him toward the town — "
            "past the gateway, to where the flat roofs and the walled houses and the "
            "olive terraces of everything he owns lie spread out in the sunlight. His "
            "face is stricken. One hand is still closed around the rings on the other. "
            "The camera is behind and beside him so both his turned face and the town "
            "he is looking at are in the same frame. He has two arms, two hands and "
            "one head."
        ),
    },
    # --------------------------------------------------- n4 — he grieves ----
    {
        "id": "v2-r009-b23", "out": "s23-his-face-fell.jpeg", "seg": "n4 p1-p2",
        "window": "123.51-128.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["RULER"],
        "narration": ("His face fell. And he walked away grieved — because he was very "
                      "rich."),
        "must_show": "THE EXACT MOMENT his face falls — the light going out of it, his eyes dropping, the beginning of the turn away.",
        "must_not_show": "no anger, no scowl, no bitterness — grief only; do not put Jesus in this frame.",
        "scene": (
            "Very close on the young man's face as it falls. His eyes have dropped away "
            "from the man in front of him to the dust, his mouth has come closed and "
            "gone slack at the corners, and every bit of the hope that was in his face "
            "a moment ago has drained out of it. His shoulders have come down. There "
            "is no anger anywhere in it — only grief, and a kind of shame. He has "
            "begun to shift his weight to rise. The sunlit road is soft behind him."
        ),
    },
    {
        "id": "v2-r009-b24", "out": "s24-he-did-not-argue.jpeg", "seg": "n4 p3-p5",
        "window": "128.64-135.40", "wide": True, "jesus": True, "ref": REF,
        "locks": ["RULER", "DISCIPLES", "ROAD"],
        "narration": ("Notice what the text does not say. It does not say he stopped "
                      "believing. It does not say he argued."),
        "must_show": "him back on his feet, standing in front of Jesus with his head down and nothing to say — no argument, no defence, no protest.",
        "must_not_show": "no pointing, no raised voice, no confrontation of any kind; no halo, glare or rim-light on Jesus.",
        "scene": (
            "The young man has got back to his feet and stands in front of Jesus with "
            "his head down and his hands empty at his sides, saying nothing at all. "
            "There is no argument in his posture anywhere — no jabbing finger, no "
            "squared shoulders, no lifted chin. He simply cannot answer. Jesus stands "
            "facing him, quiet, not pressing him. The disciples around them have gone "
            "still and silent. Dust in the bright air, the road running both ways. The "
            "camera is back far enough to hold both men head to sandals. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b25", "out": "s25-he-believed-every-word.jpeg", "seg": "n4b p1",
        "window": "135.99-141.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["RULER"],
        "narration": ("He grieved — because he believed every word, and the price was "
                      "the thing he loved most."),
        "must_show": "close on his face as he turns to go — wet eyes, mouth working, belief and loss on him at the same time.",
        "must_not_show": "no bitterness, no rolling eyes, no resentment — he believed it, and that is why it hurts; do not put Jesus in this frame.",
        "scene": (
            "Close on the young man's face as he turns away, caught in profile and "
            "half-turned back. His eyes are wet and blinking hard, his jaw is tight and "
            "his mouth is working with nothing coming out of it. It is the face of "
            "someone who believes every word he has just been told and cannot pay for "
            "it — grief and conviction on him at the same moment. Dust and bright "
            "daylight; the road beyond him is soft."
        ),
    },
    {
        "id": "v2-r009-b26", "out": "s26-back-down-that-road.jpeg", "seg": "n4b p2",
        "window": "141.67-145.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["RULER", "ROAD"],
        "narration": ("He turned around, and he walked back down that road toward "
                      "everything he owned."),
        "must_show": "SHOT FROM BEHIND HIM: the young man walking away down the road toward the town, seen from the back, his face hidden, already small with distance.",
        "must_not_show": "he must NOT look back in this frame; do not put Jesus in it; nobody follows him.",
        "scene": (
            "SHOT FROM BEHIND THE YOUNG MAN, the camera on the road looking down its "
            "length toward the town. He walks away from us with his back and heels "
            "toward the camera and HIS FACE ENTIRELY HIDDEN because he is facing away, "
            "his shoulders down and his fine purple robe dusty and hanging loose, "
            "already some way off and getting smaller. Ahead of him the town gateway "
            "and the flat roofs of everything he owns stand in the afternoon sun. The "
            "road is empty around him. He has two arms, two hands and one head."
        ),
    },
    # -------------------------------------- n5 — and Jesus let him go ----
    {
        "id": "v2-r009-b27", "out": "s27-he-let-him-go.jpeg", "seg": "n5 p1-p2",
        "window": "146.46-149.73", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": "And Jesus let him go. He did not lower the bar.",
        "must_show": "Jesus standing completely still on the road where he was, not moving, not calling out — watching.",
        "must_not_show": "no halo, glare or rim-light; he does NOT reach after him, does not open his mouth, does not take a step; his arms are not crossed.",
        "scene": (
            "Jesus stands still on the road exactly where he was, facing the way the "
            "young man has gone. He has not moved a step and his arms hang loose and "
            "open at his sides — not folded, not reaching. He is simply standing there "
            "watching, his weight settled, making no move to follow and saying nothing. "
            "The dusty road runs away from him toward the distant town. The camera is "
            "back far enough to see him head to sandals with the empty road ahead. He "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b28", "out": "s28-he-did-not-chase-him.jpeg", "seg": "n5 p3-p4",
        "window": "149.73-153.99", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DISCIPLES", "ROAD"],
        "narration": "He did not soften the terms. He did not chase him down the road.",
        "must_show": "the disciples looking at Jesus — one half-turned as if to ask whether they should go after him — and Jesus not moving.",
        "must_not_show": "no halo, glare or rim-light; nobody actually sets off after the man; Jesus is not defensive or explaining himself.",
        "scene": (
            "On the road, the disciples have turned from watching the departing figure "
            "to look at Jesus. One has taken half a step after the young man and "
            "stopped, his hand out and his face turned back questioningly; Peter's "
            "brows are down; another has his hands open in a plain unspoken question. "
            "Jesus stands among them completely unmoved, still looking down the road, "
            "answering none of them. Nobody goes after the man. Bright afternoon light "
            "and dust. The camera is back far enough to hold the group head to "
            "sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r009-b29", "out": "s29-loved-him-the-whole-time.jpeg", "seg": "n5 p5",
        "window": "153.99-159.51", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("He stood there, and he watched him walk away — and he loved him "
                      "the whole time."),
        "must_show": "⚠️ THE SECOND MOST IMPORTANT FRAME IN THIS VIDEO. Close on Jesus's face watching him go: the SAME love as b12 still plainly on it, now carrying grief of his own.",
        "must_not_show": "NOT anger. NOT relief. NOT a knowing 'I told you so'. NOT a face that has already let go. He is losing someone he loves and letting him leave anyway — if the love is not visible here, regenerate. No halo, glare or rim-light.",
        "scene": (
            "Very close on Jesus's face, filling the frame, watching down the road. His "
            "eyes are following the man he cannot see any more, and they are still soft "
            "and warm with exactly the same love as before — but wet now, and his mouth "
            "has come together with the weight of it. This is the face of someone "
            "losing a person he loves and letting him go anyway, without a word of "
            "protest. There is no anger in it, no relief, and nothing that says he "
            "expected this. Warm afternoon light on his skin; the road behind him "
            "entirely soft."
        ),
    },
    # ---------------------------------------------- n6 — the road empties ----
    {
        "id": "v2-r009-b30", "out": "s30-the-road-emptied.jpeg", "seg": "n6 p1-p4",
        "window": "160.10-169.85", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": ("The road emptied. The sun went down. And the story just ends "
                      "there — Mark leaves it exactly that sad, on purpose. Sit with it."),
        "must_show": "an EMPTY road at sunset — nobody on it at all, the town small and far off, long shadows, the day ending.",
        "must_not_show": "not one person anywhere in this frame — the emptiness is the whole picture. NOTE: sunset IS correct here; the narration states 'the sun went down'.",
        "scene": (
            "A wide view straight down the empty road at sunset. There is not a single "
            "person anywhere in the frame — only the packed pale earth rutted with "
            "cart tracks, the dry-stone walls on both sides throwing long shadows "
            "across it, the olive terraces going dark on the slopes, and the small "
            "flat roofs of the distant town under a low burning sky. The last of the "
            "sun is right down on the hills and the light is long and gold and going. "
            "Dust hangs in the still air over an empty road."
        ),
    },
    {
        "id": "v2-r009-b31", "out": "s31-a-love-that-will-not-force-you.jpeg", "seg": "n6 p5-p6",
        "window": "169.85-177.09", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": ("A love that will not force you. Is that weakness — or is it the "
                      "deepest respect you have ever been shown?"),
        "must_show": "the closing image: Jesus alone on the road in the last of the light, still looking the way the man went, having let him.",
        "must_not_show": "no halo, glare or rim-light; nobody else in the frame; no resolution and no comfort — the story ends unresolved and the picture must too.",
        "scene": (
            "The last of the sunset. Jesus stands alone on the empty road, seen from "
            "some way back and slightly to the side, a single small figure against the "
            "long gold light, still turned toward the distant town and still looking "
            "the way the young man went. His hands hang open at his sides. The road, "
            "the walls and the dark olive terraces run away from him in both "
            "directions and there is nobody else anywhere in the frame. Nothing is "
            "resolved. The camera is back far enough to see him head to sandals "
            "against the wide emptying road. He has two arms, two hands and one head."
        ),
    },
]
