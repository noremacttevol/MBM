#!/usr/bin/env python3
"""V2 beat map — row 6, build-06-two-sons (Matthew 21:28-32).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 15 pictures against V1's 8 unique stills. This is
the shortest row so far — 73.1 s — so the law's "~15 per 100 seconds" puts it at
11-15 and the narration pushes it to the top of that band, because 73 seconds
here contain more location changes than row 5 contained in 223: the video cuts
between the temple and the vineyard eight separate times. Every one of those
cuts must land on its own frame or the viewer loses which place he is in.

THE STRUCTURAL PROBLEM THIS BUILD HAS TO SOLVE (read before touching a beat):
the V1 audio has NO voice segments for the two sons. The narration says "The
first answer was blunt" and "The answer from the other son sounded much better"
and then moves on — the actual KJV answers ("I will not" / "I go, sir") are
never spoken aloud. So THE PICTURES CARRY BOTH ANSWERS ENTIRELY. b02 must read
as a flat refusal and b03 as a courteous agreement at a glance, with no words to
help them. That is ACTION-LOGIC LAW at its strictest, and it is why those two
frames are staged as plainly as they are: a turned back and a raised flat palm
for the no, a bow and a hand on the heart for the yes.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Matthew 21 KJV):
  21:23  the frame story is IN THE TEMPLE at Jerusalem — "when he was come into
         the temple ... the CHIEF PRIESTS and the ELDERS of the people came unto
         him as he was teaching." Not a Galilean synagogue, not a hillside. The
         great paved outer court, the colonnade, the temple facade beyond.
  21:28  "Son, go work TO DAY in my vineyard" — the whole parable is one day,
         and the narration confirms it ("all morning ... stayed empty all day").
         Arc: early morning ask -> mid-morning struggle -> the first son works
         through the day -> late-afternoon empty row.
  21:29  the first son: "I will not: but afterward he REPENTED, and WENT."
  21:30  the second son: "I GO, SIR: and went NOT." He is not a villain and must
         never be painted as one — he is polite, likeable and absent.
  21:31  Jesus asks; the CROWD answers "The first"; then the verdict lands on
         the leaders — "the publicans and the harlots go into the kingdom of God
         before you."

CONTENT-CARE: row 6 is not in the §3 flag table = GREEN. The D-flag restraint
(rows 87/88) is applied voluntarily anyway at b15, the only frame touching the
word "harlots": the people Jesus names are shown as poor women and a tax
collector standing at the outer margin of the court with their heads covered and
their dignity intact. Nothing suggests the trade, and nothing is sexualised. The
narration carries the label; the picture carries the dignity. Cameron's QUEUE
note on this row ("could explain in modern terms what a publican and a harlot
are") is a NARRATION change and the audio is preserved untouched — it is logged
to the ledger for the re-voice pass, not fixed here.

TWO FATHERS, DELIBERATELY DIFFERENT: row 2's prodigal father is a dignified
landowner in deep indigo with a full silver beard. This father is a working
vinedresser — wiry, sun-scorched, short grizzled beard, dark olive tunic and a
leather apron. They must never read as the same man; two parables, two fathers.

TIME OF DAY: one working day. Temple frames are bright mid-morning under open
sky. Vineyard: early morning for the two answers, hard mid-morning for the
struggle, full working day for the labour, long low afternoon light on the empty
row. No night anywhere in this build.
"""

LOCKS = {
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect).
    "TEMPLE": (
        "TEMPLE LOCK: the great outer court of the temple at Jerusalem — a vast "
        "courtyard of worn pale limestone paving under open sky, a long colonnade of "
        "massive fluted stone columns running down one side, broad stone steps, and "
        "the huge dressed-stone facade of the temple rising beyond with its high "
        "gateway. Pilgrims and city people fill the court in SATURATED DEEP earth "
        "colours — dark chocolate brown, deep russet, burnt ochre, dark olive, dusty "
        "indigo and faded plum wool. No one in the crowd wears off-white, ivory or "
        "any near-white cloth."
    ),
    "VINEYARD": (
        "VINEYARD LOCK: a terraced hillside vineyard above a small stone farmhouse — "
        "dry-stone terrace walls stepping up the slope, long rows of low staked vines "
        "heavy with green leaf, a rough watchtower of piled stone at the top, a wine "
        "press cut into the bedrock, dusty paths of pale earth between the rows, "
        "pruning hooks and reed baskets set about, dry Judean hills and olive terraces "
        "beyond."
    ),
    "PRIESTS": (
        "CHIEF PRIESTS LOCK: the chief priests and elders are the same four men in "
        "every shot — older men of settled authority, long carefully combed beards in "
        "grey and iron-grey, heavy brows, watchful unhurried eyes. They wear finely "
        "woven, DEEPLY DYED robes — NEAR-BLACK indigo and DARK UMBER with woven "
        "dark-red borders — and prayer shawls of that SAME saturated near-black and "
        "dark-indigo wool with dark stripes and dark fringe, plainly DARKER than the "
        "sunlit limestone around them. They stand together, still and composed. Their "
        "faces are shown clearly."
    ),
    "FATHER": (
        "VINEDRESSER FATHER LOCK: the father is the same man in every shot — a "
        "working vine-grower of about fifty-five, wiry and sun-scorched, a SHORT "
        "grizzled iron-grey beard, close-cropped greying hair, deep crow's feet, "
        "big cracked working hands. He wears a DARK OLIVE-GREEN wool tunic with a "
        "worn leather apron and a plain leather belt, sleeves pushed back (never "
        "cream, never white). His face is shown clearly."
    ),
    # The first son's clothing does not change, but his HANDS do — clean at the
    # refusal, stained and cut by the day's end. That is stated per beat, not in
    # the lock, so the lock can never argue with a frame.
    "FIRST-SON": (
        "FIRST SON LOCK: the first son is the same young man in every shot — early "
        "twenties, stocky and strong-shouldered, thick dark curly hair, heavy dark "
        "brows over deep-set brown eyes, a short rough dark beard, a stubborn set to "
        "the jaw. He wears a faded RUST-BROWN work tunic with a rope belt and bare "
        "forearms (never cream, never white). His face is shown clearly."
    ),
    "SECOND-SON": (
        "SECOND SON LOCK: the second son is the same young man in every shot — mid "
        "twenties, taller and slighter than his brother, neatly trimmed dark beard, "
        "tidy dark hair, a pleasant open likeable face and easy manners. He wears a "
        "clean well-kept DUSTY-INDIGO tunic with a woven sash and good sandals "
        "(never cream, never white). His hands are clean and uncalloused. His face is "
        "shown clearly."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------- n0 — the temple frame story ----
    {
        "id": "v2-r006-b01", "out": "s01-he-told-it-to-them.jpeg", "seg": "n0",
        "window": "0.28-8.31", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PRIESTS", "TEMPLE"],
        "narration": ("Jesus told this story to religious leaders — people who were "
                      "sure they had already said yes to God. He told it so they "
                      "would hear themselves in it."),
        "must_show": "the temple court: Jesus mid-story with an open storyteller's hand, the four chief priests standing before him composed and entirely certain of themselves.",
        "must_not_show": "no halo, glare or rim-light; Jesus is not detached at the frame edge — the priests and the nearby crowd are all facing him.",
        "scene": (
            "In the great outer court of the temple under bright mid-morning sky, "
            "Jesus stands on the worn limestone paving with one hand open in the easy "
            "gesture of a man beginning a story. Directly in front of him the four "
            "chief priests and elders stand together in their dark robes, arms folded "
            "or hands clasped, chins level, completely composed and sure of "
            "themselves. Behind and around them ordinary city people have stopped to "
            "listen, and every face in the frame is turned toward him. The colonnade "
            "of massive columns runs down one side and the temple facade rises "
            "beyond. The camera is back far enough to hold Jesus and the four men "
            "head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n1 — the blunt refusal ----
    {
        "id": "v2-r006-b02", "out": "s02-i-will-not.jpeg", "seg": "n1",
        "window": "8.90-10.52", "wide": True, "jesus": False, "ref": False,
        "locks": ["FATHER", "FIRST-SON", "VINEYARD"],
        "narration": "The first answer was blunt.",
        "must_show": "A FLAT NO, readable with no words: the father asking with a hand toward the vine rows, the first son already half turned away with his palm raised in refusal and his face shut.",
        "must_not_show": "no shouting, no shoving, no raised fist — this is a hard refusal, not a fight; nobody else in the frame.",
        "scene": (
            "Early morning at the edge of the terraced vineyard. The father stands "
            "facing his first son with one big cracked hand held out toward the long "
            "rows of vines behind him, asking. The son has already turned his "
            "shoulders and his body away toward the farmhouse, and he has thrown up "
            "one flat open palm between them without looking back — the whole shape of "
            "him says no. His jaw is set and his eyes are on the ground away from his "
            "father. Long low morning light and dew still on the leaves. Exactly two "
            "people are in the frame; each has two arms, two hands, two legs and one "
            "head."
        ),
    },
    # ------------------------------------------------ n2 — the courteous yes ----
    {
        "id": "v2-r006-b03", "out": "s03-i-go-sir.jpeg", "seg": "n2",
        "window": "11.12-13.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["FATHER", "SECOND-SON", "VINEYARD"],
        "narration": "The answer from the other son sounded much better.",
        "must_show": "A COURTEOUS YES, readable with no words: the second son with his head bowed respectfully and one hand laid on his own heart, giving his word; the father's face easing with relief.",
        "must_not_show": "he must NOT look sly, smirking or deceitful — he is warm, likeable and completely sincere in the moment; that is what makes the story work.",
        "scene": (
            "The same early morning, at the corner of the farmhouse by the vineyard "
            "path. The second son stands before his father with his head inclined in "
            "respect and one clean hand laid flat on his own chest, giving his word, "
            "his pleasant face lifted in a warm agreeable smile. The father has "
            "half-relaxed, one hand come up in acknowledgement, the tightness going "
            "out of his shoulders. Behind them the vine rows run away up the terraces "
            "in the low morning light. Exactly two people are in the frame; each has "
            "two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r006-b04", "out": "s04-it-never-became-obedience.jpeg", "seg": "n2b",
        "window": "14.20-18.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["SECOND-SON", "VINEYARD"],
        "narration": "The promise sounded respectful, but it never became obedience.",
        "must_show": "the second son comfortable in the shade doing nothing, his pruning hook and basket still leaning untouched against the wall, the vine rows waiting behind him.",
        "must_not_show": "he is not sneering or gloating — he is simply at ease and has let it go; nothing suggests he decided against it, only that he never started.",
        "scene": (
            "Later in the morning. The second son sits comfortably in the shade of the "
            "farmhouse wall with his back against the warm stone, one knee up, "
            "entirely at ease and doing nothing at all. A pruning hook and an empty "
            "reed basket lean against the wall beside him exactly where they were "
            "left, the blade clean and unused. Beyond him the long rows of vines run "
            "up the sunlit terraces, untouched and waiting. The camera is back far "
            "enough to hold him, the idle tools and the waiting rows in one frame. He "
            "has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------ n2c — the no that wouldn't hold ----
    {
        "id": "v2-r006-b05", "out": "s05-it-kept-pulling-at-him.jpeg", "seg": "n2c",
        "window": "18.74-25.24", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRST-SON", "VINEYARD"],
        "narration": ("The first son meant his no. But it wouldn't leave him alone. "
                      "All morning, the vineyard kept pulling at him."),
        "must_show": "the argument going on inside him: sitting apart on a terrace wall with his arms folded and his jaw hard, but his head turned and his eyes dragged back to the vine rows.",
        "must_not_show": "he is not sad or sorry yet; he is still stubborn — the tell is only that he cannot stop looking at the rows.",
        "scene": (
            "Hard mid-morning light. The first son sits alone on a dry-stone terrace "
            "wall some way off from the vines, elbows on his knees and his thick arms "
            "crossed hard in front of him, his jaw clamped and his mouth a flat line — "
            "a young man holding a position. But his head is turned away from where he "
            "meant to be looking, back toward the long rows of vines climbing the "
            "terraces, and his eyes are fixed on them. A pruning hook lies in the dust "
            "at his feet where he dropped it. The camera is back far enough to hold "
            "him and the rows he is staring at in one frame. He has two arms, two "
            "hands and one head."
        ),
    },
    # ------------------------------------------ n2d — he went (the burst) ----
    {
        "id": "v2-r006-b06", "out": "s06-so-he-got-up.jpeg", "seg": "n2d p1-p2",
        "window": "25.86-27.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIRST-SON", "VINEYARD"],
        "narration": "So he got up. And he went.",
        "must_show": "THE MOMENT OF TURNING — caught mid-rise off the wall, weight already forward, one hand pushing off the stone, his eyes already on the rows.",
        "must_not_show": "not standing and not sitting — this frame exists only to catch the middle of the movement; nobody is watching him.",
        "scene": (
            "Close on the first son CAUGHT MID-RISE from the terrace wall — his weight "
            "already thrown forward off the stone, one broad hand still pressing down "
            "on the wall behind him as he comes up, the other reaching down for the "
            "pruning hook in the dust. His head is already up and turned toward the "
            "vine rows and his eyes have gone hard with decision. Dust and bright "
            "mid-morning sun. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r006-b07", "out": "s07-and-he-worked.jpeg", "seg": "n2d p3-p4",
        "window": "27.78-33.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRST-SON", "VINEYARD"],
        "narration": ("No announcement, no apology. He went back to the vineyard, and "
                      "he worked."),
        "must_show": "him deep in the rows actually working — pruning hook in hand, sleeves back, sweat and vine sap, a filled basket behind him — and NOBODY in the frame to see him do it.",
        "must_not_show": "no father watching, no brother, no witness of any kind — the whole point is that he told nobody.",
        "scene": (
            "Full working daylight, deep among the staked vines on the terrace. The "
            "first son is at work — one hand pulling a heavy leafy cane aside, the "
            "pruning hook cutting in the other, his forearms scratched and streaked "
            "with dust and vine sap, his tunic dark with sweat between the shoulders. "
            "A reed basket behind him is already half filled with cut wood, and a "
            "long stretch of rows behind him is visibly finished and clean. There is "
            "no one else anywhere in the frame. The camera is back far enough to see "
            "him head to sandals among the rows. He has two arms, two hands and one "
            "head."
        ),
    },
    # ---------------------------------------------------- n3 — the empty row ----
    {
        "id": "v2-r006-b08", "out": "s08-the-row-stayed-empty.jpeg", "seg": "n3 p1",
        "window": "33.70-36.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "The row the second son promised to work stayed empty all day.",
        "must_show": "the untouched row at the end of the day — overgrown unpruned vines, the clean unused pruning hook and empty basket still leaning where they were left, long low shadows, nobody there.",
        "must_not_show": "no people at all in this frame; the emptiness is the picture. Do not make it sinister — just a job not done.",
        "scene": (
            "Late afternoon, low golden light raking across the terraces. One long row "
            "of vines stands untouched and overgrown — canes sprawling off their "
            "stakes, dead wood still on the vines, the earth between them unbroken and "
            "unmarked by any footprint. At the head of the row a clean unused pruning "
            "hook and an empty reed basket lean against the dry-stone wall exactly "
            "where they were set down that morning. Long shadows stretch down the "
            "empty row. There is not a single person in the frame."
        ),
    },
    {
        "id": "v2-r006-b09", "out": "s09-a-question-for-the-crowd.jpeg", "seg": "n3 p2",
        "window": "36.89-40.02", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PRIESTS", "TEMPLE"],
        "narration": "Then Jesus asked the crowd a question.",
        "must_show": "back in the temple court — Jesus turning from the priests to put a question to the wider crowd, heads coming up all around.",
        "must_not_show": "no halo, glare or rim-light; he is among the people, not standing apart at the frame edge.",
        "scene": (
            "Back in the bright temple court. Jesus has turned away from the four "
            "chief priests toward the wider crowd of city people gathered around him, "
            "his hand lifting to put a question to them. Heads are coming up all "
            "across the court and people are turning in toward him to hear it. The "
            "four priests stand off to one side in their dark robes, still composed, "
            "watching. The colonnade and the temple facade rise behind. The camera is "
            "back far enough to hold Jesus, the priests and the near crowd head to "
            "sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r006-b10", "out": "s10-whether-of-them-twain.jpeg", "seg": "j1",
        "window": "40.66-43.44", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": "Whether of them twain did the will of his father? (Matthew 21:31)",
        "must_show": "close on Jesus asking it — open hand, level and unhurried, genuinely waiting for their answer.",
        "must_not_show": "no halo, glare or rim-light; no trap in his face — the question is asked plainly and he means it.",
        "scene": (
            "Close on Jesus in the sunlit temple court, mid-question, one hand open "
            "and lifted in front of him, his head slightly tilted as he waits. His "
            "face is calm and unhurried and completely open — a man who has asked a "
            "real question and is willing to stand there for the answer. The blurred "
            "shapes of the crowd and the massive pale columns of the colonnade are "
            "soft behind him. His hand has five fingers."
        ),
    },
    # ----------------------------------------- n4 — what they finally DID ----
    {
        "id": "v2-r006-b11", "out": "s11-what-they-finally-did.jpeg", "seg": "n4 p1",
        "window": "44.58-48.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["FIRST-SON", "VINEYARD"],
        "narration": ("The difference was not what the sons said; it was what they "
                      "finally did."),
        "must_show": "ONE CONTINUOUS VIEW at day's end holding both outcomes: the first son straightening up tired at the end of his finished rows, and further along the same hillside the one row still overgrown and untouched.",
        "must_not_show": "NOT a split screen, NOT a before-and-after pair, NOT two panels — one single hillside seen in one shot, with both things in it.",
        "scene": (
            "One single continuous view across the terraced hillside in long "
            "late-afternoon light. In the near ground the first son straightens up "
            "from the last of his work, one hand pressed to the small of his back, his "
            "forearms filthy and scratched, the rows behind him pruned clean and their "
            "cut wood stacked. Further along the same slope, unmistakably part of the "
            "same hillside and the same moment, the second son's row stands sprawling "
            "and overgrown with its clean tools still leaning at the head of it. No "
            "dividing line and no second frame — one hillside, one photograph. He has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r006-b12", "out": "s12-the-crowd-knew.jpeg", "seg": "n4 p2",
        "window": "48.84-51.03", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": "The crowd knew the answer.",
        "must_show": "the crowd answering — an ordinary working man speaking up with his hand half raised, heads nodding around him, the answer obvious to everyone.",
        "must_not_show": "no halo or rim-light on Jesus; nobody is arguing — this is the easy part and their faces show it.",
        "scene": (
            "In the temple court the crowd have answered. An ordinary weathered "
            "working man near the front has spoken up with his hand half lifted, and "
            "all around him people are nodding, a woman saying it to her neighbour, an "
            "old man gesturing as if it hardly needed asking. Jesus stands facing them "
            "listening, unsurprised. The whole court has the look of a question that "
            "answered itself. The camera is back far enough to hold the near crowd and "
            "Jesus head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------ n5 — it turns on the leaders ----
    {
        "id": "v2-r006-b13", "out": "s13-their-own-answer.jpeg", "seg": "n5 p1-p2",
        "window": "51.63-59.03", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIESTS", "TEMPLE"],
        "narration": ("Their answer condemned their own confidence. The son who began "
                      "in rebellion had changed direction; the polite son had not."),
        "must_show": "the four priests' faces close, as the answer they just heard turns around on them — the certainty cracking, one working it out, one already stiffening.",
        "must_not_show": "do not put Jesus in this frame; no cartoon outrage — the change is small and internal and shows mostly in the eyes.",
        "scene": (
            "Close on the four chief priests and elders standing together in their "
            "dark robes in the sunlit court. The composure is coming apart by degrees "
            "— the nearest man's eyes have narrowed and moved sideways as he works out "
            "where the story has gone, the one behind him has gone very still with his "
            "mouth pressed shut, a third has begun to stiffen and lift his chin, and "
            "the fourth is looking at the paving. Not one of them is looking at "
            "anyone. Bright open daylight and the pale columns soft behind them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r006-b14", "out": "s14-he-turned-to-them.jpeg", "seg": "n5 p3",
        "window": "59.03-65.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PRIESTS", "TEMPLE"],
        "narration": ("Then Jesus turned to the religious leaders — the ones who were "
                      "sure they were the second son."),
        "must_show": "Jesus turning bodily away from the crowd to face the four priests directly, the people falling back to leave open paving between them.",
        "must_not_show": "no halo, glare or rim-light; no anger in his posture — he is squared up and steady, and the crowd is not being used against them.",
        "scene": (
            "Jesus has turned his whole body away from the crowd to face the four "
            "chief priests and elders directly across a clear space of pale limestone "
            "paving. The people nearest have drawn back on both sides, opening the "
            "ground between him and the four men, and gone quiet. The priests stand "
            "shoulder to shoulder in their dark robes holding their position, faces "
            "guarded. His posture is steady and unhurried, one hand loose at his side. "
            "The colonnade runs away behind them under the bright sky. The camera is "
            "back far enough to hold Jesus and all four men head to sandals. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------------------- j2 — verdict ----
    {
        "id": "v2-r006-b15", "out": "s15-before-you.jpeg", "seg": "j2 p1a",
        "window": "65.88-69.0", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": ("Verily I say unto you, That the publicans and the harlots go "
                      "into the kingdom of God (Matthew 21:31)"),
        "must_show": "close on Jesus saying it directly to them — level, certain, entirely without cruelty.",
        "must_not_show": "no halo, glare or rim-light; no scorn or triumph on his face; this is told as plain fact, not as a taunt.",
        "scene": (
            "Close on Jesus in the bright temple court, speaking straight ahead at the "
            "men in front of him. His face is level and certain and there is no cruelty "
            "anywhere in it — no scorn in the mouth, no heat in the eyes, only a man "
            "saying something true that costs the hearer everything. The blurred dark "
            "shapes of the listening priests are at the very edge of frame and the "
            "sunlit limestone is soft behind him."
        ),
    },
    {
        "id": "v2-r006-b16", "out": "s16-the-ones-he-meant.jpeg", "seg": "j2 p1b",
        "window": "69.0-72.24", "wide": True, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": "before you. (Matthew 21:31)",
        "must_show": "the people he is talking about, at the far outer margin of the court — a tax collector at his small table and two poor women standing back near the colonnade, listening from a distance.",
        "must_not_show": "CONTENT-CARE: nothing whatever suggests the women's trade, nothing is sexualised, no jewellery, paint or bare shoulders — they are poor, covered, ordinary and dignified. Nobody is shown shaming them. Do not put Jesus in this frame.",
        "scene": (
            "At the far outer edge of the temple court, back in the shade of the "
            "colonnade where people who feel unwelcome stand. A tax collector sits at "
            "a small wooden table with his coin box and tally, half turned on his "
            "stool to listen across the court. A few steps from him two poor women "
            "stand close together against a column, heads and shoulders covered by "
            "worn dark shawls, their plain mended robes drawn about them, hands folded "
            "— listening, holding very still, their tired faces lit with something "
            "careful that is almost hope. Nobody is speaking to them and nobody is "
            "driving them off. Far across the sunlit paving behind them the crowd is a "
            "distant blur. Every figure has two arms, two hands and one head."
        ),
    },
]
