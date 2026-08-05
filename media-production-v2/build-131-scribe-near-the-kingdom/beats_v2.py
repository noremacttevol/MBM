#!/usr/bin/env python3
"""V2 beat map — row 131, build-131-scribe-near-the-kingdom (Mark 12:28-34).

COVERAGE: 16 pictures over 94.9 s = 5.9 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 12 KJV):
  12:28 "one of the scribes came... perceiving that he had answered
        them well, asked him, WHICH IS THE FIRST COMMANDMENT OF ALL?"
        — a REAL question, not a trap (the narration says so).
  12:29-30 "The first of all the commandments is, HEAR, O ISRAEL;
        The Lord our God is ONE LORD: And thou shalt LOVE the Lord
        thy God with all thy heart... soul... mind... strength."
  12:31 "the second is like, namely this, Thou shalt LOVE THY
        NEIGHBOUR AS THYSELF. There is none other commandment
        greater than these."
  12:32-33 the scribe's OWN addition: "...is MORE THAN ALL WHOLE
        BURNT OFFERINGS AND SACRIFICES." — he thinks past repetition.
  12:34 "when Jesus saw that he answered DISCREETLY, he said unto
        him, THOU ART NOT FAR FROM THE KINGDOM OF GOD. And no man
        after that durst ask him any question."
  Setting: the TEMPLE COURTS during the Jerusalem questioning week.

RENDERING LAWS:
  - THE SCRIBE IS THE ROW'S HERO — an honest teacher of the law,
    open-hearted, thinking clearly. Nothing adversarial about him
    ever; his robes fine but his manner warm. He is NOT one of the
    build-06 chief-priests family and must not share their faces.
  - Jesus and the scribe meet as two men who RESPECT each other —
    the row's emotional register is mutual recognition. b11's look
    and b14's word are the twin peaks; warmth throughout.
  - The altar smoke (b09/b10) is ordinary temple sacrifice smoke at
    distance — reverent, never sinister; it is what the scribe's
    insight weighs and outweighs.
  - The threshold image (b12) is a real temple-court gate with
    light beyond — invitation architecture, standing open (no
    barred doors; rhymes with the row-125/127 door law).
  - Other questioners at the edges withdraw quietly at b16 — no
    humiliation theatre; they simply stop asking.

TIME OF DAY ARC (intentional): one bright Jerusalem morning in the
temple courts throughout; the closing frames in the court's warm
midday light.

CHANGING CONDITION (kept OUT of the locks): the surrounding
questioners — pressing at first, withdrawn by b16; the scribe —
asking, then answering, then standing at the threshold.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "TEMPLE": (
        "TEMPLE LOCK: the temple courts — broad pale limestone "
        "courts with great columned porticoes, wide steps, morning "
        "light on honey-coloured stone, the altar's thin smoke "
        "rising beyond an inner wall. The same courts throughout."
    ),
    "SCRIBE": (
        "SCRIBE LOCK: the scribe is the same man in every shot — "
        "about fifty, a thoughtful deep-lined face with keen kind "
        "eyes, a full grey-streaked beard, in a fine DEEP BLUE robe "
        "with a dark mantle and head covering (never cream, never "
        "white); earnest, warm, quick-minded — never adversarial."
    ),
    "LISTENERS": (
        "LISTENERS LOCK: the surrounding listeners — a loose ring "
        "of temple-court men: other scribes in dark robes, pilgrims "
        "in earth tones, a few elders (no cream — only Jesus wears "
        "cream); attentive, varied faces, never uniform."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r131-b01", "out": "s01-a-teacher-of-the-law.jpeg", "seg": "n0a",
        "window": "0.28-4.65", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "SCRIBE", "LISTENERS"],
        "narration": "A teacher of the law came to Jesus with a real question, not a trap —",
        "must_show": "the honest approach — the scribe stepping out of the listening ring toward Jesus in the bright temple court, his face open and genuinely asking; nothing adversarial anywhere.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the scribe's openness UNMISTAKABLE — leaning in, hands easy, no crossed arms.",
        "scene": (
            "For once the man walking up means the question, the "
            "camera looking past the listening ring's backs "
            "into the bright court: the scribe steps out from "
            "among the dark-robed questioners toward Jesus — and "
            "everything about him is different from the traps "
            "that came before: the hands easy at his sides, the "
            "keen eyes genuinely hungry, the lean of a man who "
            "wants the ANSWER and not the argument — an honest "
            "question crossing the temple stones in fine blue "
            "robes. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r131-b02", "out": "s02-which-is-the-first-commandment.jpeg", "seg": "s28",
        "window": "5.31-7.44", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": "Which is the first commandment of all?",
        "must_show": "SCRIPTURE-EXACT: the question asked — the scribe and Jesus face to face, the question leaving him with real hunger; Jesus receiving it with full attention.",
        "must_not_show": "no halo, glare or rim-light on Jesus; both faces OPEN — a real exchange beginning.",
        "scene": (
            "The best question of the whole hostile week is "
            "asked quietly: the scribe face to face with Jesus "
            "in the morning light, the words leaving him with "
            "the plain hunger of a man who has read everything "
            "and wants the one thing at the bottom of it — "
            "which commandment is FIRST? — and Jesus turns him "
            "the full attention he gives to honest askers, two "
            "students of the same Book meeting over its deepest "
            "line. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r131-b03", "out": "s03-jesus-answered-from-words-the.jpeg", "seg": "n0b",
        "window": "8.91-12.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": "Jesus answered from words the scribe had known by heart for years.",
        "must_show": "the recognition beginning — Jesus beginning the ancient answer; on the scribe's face the first light of hearing his own heart-language spoken back.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the scribe's recognition VISIBLE — lips almost moving along.",
        "scene": (
            "The answer starts on ground the asker has walked "
            "all his life: Jesus begins, and the cadence that "
            "comes is the oldest one in the scribe's memory — "
            "words he learned at his father's knee, prayed at "
            "every dawn, copied in his own careful ink a "
            "hundred times — and on the deep-lined face the "
            "recognition kindles as it arrives: his lips "
            "almost moving along with the recitation, a "
            "lifetime of knowing-by-heart meeting the Heart "
            "the words were always about. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r131-b04", "out": "s04-the-first-of-all-the.jpeg", "seg": "jv29",
        "window": "13.39-32.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "LISTENERS"],
        "narration": (
            "The first of all the commandments is, Hear, O Israel; The Lord "
            "our God is one Lord: And thou shalt love the Lord thy God with "
            "all thy heart, and with all thy soul, and with all thy mind, "
            "and with all thy strength: this is the first commandment."
        ),
        "must_show": "SCRIPTURE-EXACT: the Shema given — Jesus speaking the great commandment with full gravity, one hand at his heart; the whole listening ring stilled around the ancient words.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the stillness TOTAL — the court's noise gone from every listening face.",
        "scene": (
            "The first commandment stills the whole court to "
            "hear itself spoken: Jesus with one hand resting "
            "at his heart, giving the Shema its full unhurried "
            "weight — hear, O Israel — heart, soul, mind, "
            "strength, each word set down like a foundation "
            "stone — and around him the listening ring has "
            "gone entirely still, scribes and pilgrims alike "
            "caught inside the words their whole nation wakes "
            "to, hearing them land as if new from the mouth "
            "that means them completely. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r131-b05", "out": "s05-the-scribe-had-not-merely.jpeg", "seg": "n2",
        "window": "70.09-72.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": "The scribe had not merely repeated Jesus.",
        "must_show": "the thinking — close on the scribe mid-thought, one finger raised slightly, his own words forming; a mind working past repetition.",
        "must_not_show": "no halo; the thought LIVE — eyes bright with his own arriving insight.",
        "scene": (
            "Something better than an echo is being assembled: "
            "close on the scribe with one finger lifted "
            "slightly off his robe, eyes bright and inward, "
            "his own words visibly forming behind them — not "
            "the student's trick of handing the teacher's "
            "sentence back, but a mind taking the answer all "
            "the way into its own workshop and returning with "
            "something added — the rarest response in the "
            "temple that week: thought. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r131-b06", "out": "s06-and-the-second-is-like.jpeg", "seg": "jv29",
        "window": "32.28-38.51", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "LISTENERS"],
        "narration": (
            "And the second is like, namely this, Thou shalt love thy "
            "neighbour as thyself."
        ),
        "must_show": "SCRIPTURE-EXACT: the second commandment — Jesus's open hand sweeping toward the varied people filling the court: the neighbour made visible and present.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture lands on REAL people — pilgrims, elders, children in the court.",
        "scene": (
            "The second commandment gets pointed at its "
            "subject: Jesus's open hand sweeps from his heart "
            "out toward the court itself — the pilgrims at the "
            "steps, the old men in the shade of the portico, a "
            "child towed by her mother past the columns — thy "
            "NEIGHBOUR, the gesture says, is not a theory: he "
            "is currently everywhere, in every direction, "
            "wearing every face in this court — the second "
            "great commandment delivered with its address "
            "attached. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r131-b07", "out": "s07-there-is-none-other-commandment.jpeg", "seg": "jv29",
        "window": "38.51-42.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE"],
        "narration": "There is none other commandment greater than these.",
        "must_show": "SCRIPTURE-EXACT: the summit — Jesus holding up two fingers together, the two commandments raised as one peak; finality without sternness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the two-finger gesture CLEAR — two commandments, one summit.",
        "scene": (
            "The whole mountain of the law gets its summit "
            "marked: Jesus raises two fingers held together in "
            "the morning light — these two, love upward and "
            "love outward, one double peak above every other "
            "commandment ever counted — the gesture simple "
            "enough for the child by the column to read and "
            "final enough that the ring of listening scholars "
            "has nothing to add — no greater, the calm face "
            "says, because there is nowhere higher to go. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r131-b08", "out": "s08-the-answer-was-not-merely.jpeg", "seg": "n1",
        "window": "43.48-46.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "LISTENERS"],
        "narration": "The answer was not merely an idea to admire.",
        "must_show": "the weight landing — along the listening faces, admiration turning into something heavier: the recognition that the answer is a demand on each of them.",
        "must_not_show": "no halo; the shift SUBTLE — nodding faces going still, eyes dropping inward.",
        "scene": (
            "The applause dies in the throat and becomes "
            "something better: along the listening ring the "
            "admiring nods slow and stop — a scholar's raised "
            "brow settling, a pilgrim's smile fading into "
            "thought, eyes dropping from the speaker to the "
            "self — the answer ceasing to be a beautiful "
            "sentence about the law and becoming, face by "
            "face, a claim on the one heart each listener "
            "actually has — admiration converting into weight "
            "all around the court. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r131-b09", "out": "s09-it-measured-every-other-act.jpeg", "seg": "n1",
        "window": "46.17-49.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": "It measured every other act of devotion.",
        "must_show": "the measuring — the altar's thin sacrifice-smoke rising beyond the inner wall, seen from the court; every offering suddenly standing under the two commandments' measure.",
        "must_not_show": "no halo; the smoke REVERENT and ordinary — temple ritual at its dignified daily work, being measured, not mocked.",
        "scene": (
            "The new measure hangs over the old devotions: "
            "beyond the inner wall the altar's thin smoke "
            "climbs its steady grey line into the morning — "
            "the daily offerings ascending as they have for "
            "centuries, reverent, costly, correct — and over "
            "all of it now the two commandments stand like a "
            "surveyor's mark, measuring every ram and dove "
            "and handful of flour against heart, soul, mind, "
            "strength, and neighbour — the whole smoking "
            "apparatus of devotion suddenly standing for "
            "inspection. No people are needed in this frame."
        ),
    },
    {
        "id": "v2-r131-b10", "out": "s10-well-master-thou-hast-said.jpeg", "seg": "s32",
        "window": "49.66-68.56", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": (
            "Well, Master, thou hast said the truth: for there is one God; "
            "and there is none other but he: And to love him with all the "
            "heart, and with all the understanding, and with all the soul, "
            "and with all the strength, and to love his neighbour as "
            "himself, is more than all whole burnt offerings and sacrifices."
        ),
        "must_show": "SCRIPTURE-EXACT: the scribe's answer — the scribe speaking with earnest animation, one hand gesturing toward the distant altar smoke as he ranks love ABOVE it; Jesus listening closely.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the scribe's gesture at the SMOKE readable — love outweighing offerings.",
        "scene": (
            "The scribe answers like a man spending his life's "
            "study in one sentence: animated now, warm, his "
            "hand sweeping toward the altar's distant smoke "
            "line as he sets it on the scale — all the burnt "
            "offerings, all the sacrifices, everything his "
            "guild has weighed and recorded for generations — "
            "and love, on the other pan, outweighing the lot — "
            "his own addition, thought all the way through — "
            "while Jesus listens with the stillness he keeps "
            "for people getting it exactly right. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r131-b11", "out": "s11-jesus-looked-at-him-and.jpeg", "seg": "n3",
        "window": "75.50-79.59", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": "Jesus looked at him and saw a man thinking clearly, with an open heart.",
        "must_show": "the look — close on Jesus's face regarding the scribe with warm, discerning recognition; being fully SEEN as the row's emotional peak.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the warmth PERSONAL — one man recognizing another.",
        "scene": (
            "The look the scribe gets is the one everyone "
            "wants: close on Jesus's face turned full toward "
            "him, the deep brown eyes doing their complete "
            "unhurried seeing — past the fine robe, past the "
            "guild, into the clear-running mind and the heart "
            "standing open behind it — and finding it GOOD: "
            "the warm particular recognition of one man "
            "reading another exactly right, the rarest wage "
            "honest thinking ever earns, being paid in full in "
            "the temple court. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r131-b12", "out": "s12-understanding-had-brought-the-man.jpeg", "seg": "n4",
        "window": "87.05-91.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": "Understanding had brought the man to the threshold; now he had to enter.",
        "must_show": "the threshold — the scribe standing at a great open court gate with warm light beyond it, paused mid-step; understanding's limit and invitation's beginning in one doorway.",
        "must_not_show": "no halo; the gate OPEN (never barred); his pause WEIGHTED, hopeful — a man deciding, not refused.",
        "scene": (
            "Understanding's road ends at a doorway only feet "
            "can finish: the scribe stands at one of the "
            "court's great open gates, warm light lying through "
            "it across the threshold stone, his weight paused "
            "mid-step in the doorway's frame — every argument "
            "already won, every text already mastered, the "
            "whole distance a mind can travel completed — and "
            "the last few feet standing there open in front of "
            "him, crossable by nothing he has memorized: only "
            "entered. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r131-b13", "out": "s13-he-understood-the-weight-of.jpeg", "seg": "n2",
        "window": "72.68-74.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["SCRIBE"],
        "narration": "He understood the weight of the answer.",
        "must_show": "the weight understood — close on the scribe's face gone grave and quiet, the insight settling into him with its full cost visible.",
        "must_not_show": "no halo; gravity WITHOUT gloom — a man holding something heavy and precious.",
        "scene": (
            "What he just said out loud settles onto him with "
            "its whole weight: close on the deep-lined face "
            "gone grave, the animation of the answer subsiding "
            "into stillness — more than all offerings, he "
            "said, and he MEANT it, and meaning it "
            "re-prices everything his life is built around — "
            "the keen eyes steady under the load, a scholar "
            "discovering that the truest sentence he ever "
            "spoke has terms, and the terms are himself. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r131-b14", "out": "s14-thou-art-not-far-from.jpeg", "seg": "j1",
        "window": "80.14-82.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": "Thou art not far from the kingdom of God.",
        "must_show": "SCRIPTURE-EXACT: the word — Jesus saying it directly to the scribe, his hand nearly at the man's shoulder; nearness spoken and physically shown.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the near-touch DELIBERATE — inches, not contact; both faces moved.",
        "scene": (
            "The distance gets measured out loud, and it is "
            "almost nothing: Jesus says it straight into the "
            "scribe's eyes — not FAR from the kingdom — and "
            "his hand rises to hover a breath from the man's "
            "shoulder, the nearness spoken and enacted at "
            "once: this close, the hand says; inches; one "
            "step of the heart — and on the scribe's grave "
            "face the sentence lands as the best and most "
            "unfinished news of his entire learned life. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r131-b15", "out": "s15-that-was-both-recognition-and.jpeg", "seg": "n4",
        "window": "84.26-87.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "SCRIBE"],
        "narration": "That was both recognition and invitation.",
        "must_show": "the two-in-one — the two faces close in profile, mutual regard; the sentence hanging between them as both honour and open door.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the regard MUTUAL — two men at the closest honest distance.",
        "scene": (
            "One sentence does both jobs between two faces: "
            "the scribe and Jesus close in profile in the warm "
            "court light, the words still in the air between "
            "them — recognition, first: you have thought "
            "truly, you have come far, you are SEEN — and "
            "folded inside it the invitation that keeps the "
            "door of the sentence open: not far is not "
            "arrived; the last step stands waiting — honour "
            "and welcome sharing one breath, from the only "
            "mouth that can offer both. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r131-b16", "out": "s16-and-no-one-dared-question.jpeg", "seg": "n4",
        "window": "91.58-94.66", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TEMPLE", "LISTENERS"],
        "narration": "And no one dared question Jesus after that.",
        "must_show": "the quiet close — the other questioners withdrawing quietly along the portico, and Jesus standing at ease in the bright court; the questions finished.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO humiliation theatre — the withdrawers simply done, thoughtful, dispersing.",
        "scene": (
            "The questioning season ends without a gavel: "
            "along the shaded portico the other questioners "
            "drift quietly away in twos and threes — not "
            "routed, not shamed, just finished, their last "
            "and best question having been asked by the "
            "honest man among them and answered past "
            "improving — while Jesus stands at ease in the "
            "bright open court, the morning light on the "
            "honey stone, holding the field the way truth "
            "holds it: quietly, with room around it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "TEMPLE": "PLACE-REF/temple.jpeg",  # build-06-two-sons v2-r006-b21
}
# === end PLACE-PLATES ===
