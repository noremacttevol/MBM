#!/usr/bin/env python3
"""V2 beat map — row 120, build-120-job-from-whirlwind (Job 1-2, 19, 38-42).

COVERAGE: 42 pictures over 241.8 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Job KJV):
  1:1-3  Job of UZ, "perfect and upright"; seven sons, three daughters;
         7000 sheep, 3000 camels, 500 yoke of oxen — "the greatest of
         all the men of the east."
  1:13-19 the four blows in ONE stretch: raiders take the oxen and
         asses, fire takes the sheep, Chaldeans take the camels, and a
         GREAT WIND smites the house where his children feasted.
  1:20-21 he RENT HIS MANTLE, SHAVED HIS HEAD, "and fell down upon the
         ground, AND WORSHIPPED": "the LORD gave, and the LORD hath
         taken away; blessed be the name of the LORD."
  2:7-8  sore boils; "he sat down among the ashes" with a potsherd.
  2:11-13 the three friends sat with him SEVEN DAYS "and none spake a
         word" — their best act. Then they started explaining.
  19:25  "I KNOW that my redeemer liveth, and that he shall stand at
         the latter day upon the earth."
  38:1   "the LORD answered Job OUT OF THE WHIRLWIND."
  38:4-7 "Where wast thou when I laid the foundations of the earth...
         when the MORNING STARS SANG TOGETHER?"
  38:31  "Canst thou bind the sweet influences of PLEIADES, or loose
         the bands of ORION?" — then the sea, the snow, the wild ass
         (39:5), the horse (39:19), the hawk (39:26).
  40:4-5 "Behold, I am vile... I will lay mine HAND UPON MY MOUTH."
  42:5   "I have heard of thee by the hearing of the ear: but now mine
         EYE SEETH THEE."

RENDERING LAWS:
  - GOD IS NEVER EMBODIED in this row. The whirlwind is a vast,
    majestic, slow-turning storm column; the voice is weather and
    moving air. No figure, no face, ever (Job's scripture hides him —
    same reconciliation as rows 102/104/105; the row-113 body-order
    applies only where scripture shows him).
  - The children's deaths are NEVER shown — losses are told entirely
    by aftermath: far smoke, a running messenger, the great house
    with its roof fallen at distance. No bodies, no victims.
  - Job's illness with dignity (the row-15 grey-sick lesson): the
    boils are carried by posture, ash-dust, gauntness and the
    potsherd — never rendered as gore, and his skin stays warm and
    human under the grey ash dusting, never corpse-grey.
  - The heavenly-council scenes of Job 1-2 are NOT in the narration
    and are NOT pictured. No Satan figure anywhere.
  - Creation-vision beats (b25/b26/b29/b31/b36) are PERSON-FREE
    cosmic and wild-world frames — the phantom-people trap is the
    row-11 defect; none of them carries the wide flag.

TIME OF DAY ARC (intentional): golden prosperous morning (b01); the
losses under a hardening, wind-torn noon; the ash-heap days in flat
grey overcast; the redeemer confession at DUSK with first stars
(b17-b19); the whirlwind under a bruised silver storm sky; the
creation visions outside time (world-dawn light, deep night
starfields); the ending in washed clean morning light.

CHANGING CONDITIONS (kept OUT of the locks): Job's mantle — whole,
then TORN from b05 on; his head — full-haired in prosperity (b01),
SHAVED from b05 on (the beard stays); his posture — upright overseer,
collapsed griever, seated in ashes, standing demander, kneeling
hand-on-mouth, and finally walking home; the sky — golden, torn,
grey, storm-columned, then washed clean.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark —
# only Jesus wears cream (not in this row).
LOCKS = {
    "JOB": (
        "JOB LOCK: Job is the same man in every shot — about sixty, a "
        "once-powerful weathered frame, deep-set patient eyes, a full "
        "grey-streaked dark beard, in a robe of DEEP RUSSET-BROWN with "
        "a dark sash (never cream, never white). His grief is honest "
        "and dignified, never theatrical."
    ),
    "FRIENDS": (
        "FRIENDS LOCK: the three friends are the same three in every "
        "shot — Eliphaz the eldest, silver-bearded, in DEEP UMBER; "
        "Bildad, broad and black-bearded, in DARK SLATE-BLUE; Zophar, "
        "lean and grey-templed, in DARK OLIVE. Travel-dusted robes, "
        "no cream, no white."
    ),
    "HOME": (
        "HOME LOCK: Job's estate on the plain of Uz — a great "
        "flat-roofed stone-and-mudbrick homestead with a walled "
        "courtyard, animal pens and fig trees, standing alone on a "
        "wide tawny plain with far blue hills. The same buildings, "
        "wall and skyline throughout."
    ),
    "ASHES": (
        "ASHES LOCK: the ash heap — a broad mound of pale grey ash "
        "and broken potsherds outside the settlement wall, under "
        "open sky, a low ridge on the horizon. The same mound and "
        "horizon throughout."
    ),
    "WHIRLWIND": (
        "WHIRLWIND LOCK: the whirlwind — a vast, slow-turning storm "
        "column of dark silver-grey cloud reaching from the plain to "
        "heaven, veined with quiet lightning, lit softly from within; "
        "majestic and awesome, it destroys NOTHING and approaches no "
        "closer than reverence. The same column throughout."
    ),
}

REF = True

# AUDIO-FIX 2026-08-09 (AUDIO-FIX lane, Machine A `Dev`, $0): STALE-V1 OLD-VOICE —
# the shipping V1 mp4 was committed 2026-07-24 with the OLD narration voice, but all
# 22 segment mp3s were re-recorded in ElevenLabs 2026-07-29 (44100/128k). Set this
# flag so v2_assemble renders narration from THIS build's own NEW-voice mp3s instead
# of copying the old-voice mp4 stream (REDO-ALL). Nothing re-voiced — the new voice
# already exists in the segments. See QC.md 🅿️ RUNNER PARK.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r120-b01", "out": "s01-job-was-a-good-man.jpeg", "seg": "n1",
        "window": "0.28-9.14", "wide": True, "jesus": False, "ref": False,
        "locks": ["JOB", "HOME"],
        "narration": (
            "Job was a good man — honest, generous, devoted to God — and for "
            "most of his life that goodness and a happy, prosperous home went "
            "together."
        ),
        "must_show": "SCRIPTURE-EXACT: the prosperity — the great estate at golden morning: flocks in the pens, servants at work, grown children laughing at a long courtyard table, Job overseeing it all with open hands; goodness and plenty in one frame.",
        "must_not_show": "no halo; the wealth WARM, not gaudy — a working estate, not a palace.",
        "scene": (
            "The good years stand in one golden morning, the camera "
            "looking past the household's backs into the courtyard: "
            "the great stone homestead awake — sheep pressing at the "
            "pens, servants carrying bread and water-jars, his grown "
            "sons and daughters loud and easy at the long table under "
            "the fig trees — and moving through all of it with open "
            "hands, the master everyone is glad to see coming: Job in "
            "his russet robe, full-haired and strong, the greatest man "
            "of the east and the kindest, his goodness and his "
            "blessings so long married that nobody on the plain can "
            "tell them apart. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r120-b02", "out": "s02-then-they-started-explaining.jpeg", "seg": "n4",
        "window": "70.06-71.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "FRIENDS", "ASHES"],
        "narration": "Then they started explaining.",
        "must_show": "the turn — the three friends leaning in around ash-seated Job, hands beginning to gesture, mouths opening; the good silence ending.",
        "must_not_show": "no halo; no shouting yet — the ruin arrives as REASONABLE faces.",
        "scene": (
            "The seven good days end the way comfort usually fails: "
            "around the ash-seated man the three friends lean in at "
            "once — Eliphaz's silver beard tilted with gentle "
            "authority, Bildad's thick finger already rising, Zophar "
            "drawing breath — the healing silence breaking into "
            "explanation on every side of a man who asked for none of "
            "it, and on Job's ash-dusted face, between the shaved "
            "head and the grey-streaked beard, the first weary "
            "understanding that his comforters have become a second "
            "storm. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r120-b03", "out": "s03-and-then-in-a-single.jpeg", "seg": "n2",
        "window": "9.71-13.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "HOME"],
        "narration": "And then, in a single devastating stretch, it was all taken.",
        "must_show": "the taking as AFTERMATH — far columns of smoke beyond the emptied pens, a messenger running hard up the road, wind tearing at the fig trees; Job turning toward the news.",
        "must_not_show": "ABSOLUTE: no violence enacted, no raiders, no victims — smoke, wind and a runner carry everything.",
        "scene": (
            "The day turns in one frame: beyond the suddenly empty "
            "pens two far columns of smoke lean on the hardening "
            "wind, the fig trees thrash, and up the long road a "
            "messenger runs the way men only run with terrible news — "
            "while in the courtyard Job turns from his work toward "
            "all of it at once, the wind taking his robe, the "
            "morning's gold gone to a torn and dirty light, "
            "everything he was given being carried off the edges of "
            "the picture faster than a man can even face it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b04", "out": "s04-one-of-the-oldest-hardest.jpeg", "seg": "n2",
        "window": "18.60-25.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "HOME"],
        "narration": (
            "One of the oldest, hardest questions in the world landed on the "
            "best man in it: why do good people suffer?"
        ),
        "must_show": "the question landing — Job alone in the emptied courtyard, arms open at nothing, face lifted, the devastation total and the question visible on him.",
        "must_not_show": "no halo; no answer anywhere in the frame — the emptiness IS the picture.",
        "scene": (
            "The oldest question finds its address: Job standing "
            "alone in the middle of the emptied courtyard under a "
            "torn grey sky — the long table bare, the pens silent, "
            "the smoke thinning on the horizon — his arms slightly "
            "open at all the nothing where everything was, his face "
            "lifted with the question every griever has asked since "
            "grief began written plainly across it, and no answer "
            "anywhere on the plain, in the sky, or in the frame. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b05", "out": "s05-and-this-is-what-he.jpeg", "seg": "n2",
        "window": "25.96-29.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "HOME"],
        "narration": "And this is what he said on the day it happened.",
        "must_show": "the day itself — Job on his knees on the courtyard stones, mantle freshly TORN, head newly SHAVED, gathering himself to speak.",
        "must_not_show": "no halo; the grief PHYSICAL and dignified — torn cloth, bare scalp, steady mouth.",
        "scene": (
            "On the day itself he goes to the ground to say it: Job "
            "on his knees on the courtyard stones, the russet mantle "
            "hanging torn from his own two hands' work, the newly "
            "shaved scalp pale above the grey-streaked beard — "
            "grief written on his body in the honest old language of "
            "torn cloth and bared head — and the mouth beneath the "
            "wet eyes steadying, not to curse, but to say the "
            "hardest blessed sentence in the book. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b06", "out": "s06-naked-came-i-out-of.jpeg", "seg": "s121",
        "window": "29.86-38.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "HOME"],
        "narration": (
            "Naked came I out of my mother's womb, and naked shall I return "
            "thither: the LORD gave, and the LORD hath taken away; blessed "
            "be the name of the LORD."
        ),
        "must_show": "SCRIPTURE-EXACT: the worship — Job fallen down upon the ground, brow to the stones, arms spread, torn mantle and shaved head; loss answered with worship.",
        "must_not_show": "ABSOLUTE: no figure of God, no light-shaft answer — the worship is unanswered and total.",
        "scene": (
            "The sentence is spoken face-down: Job fallen full-length "
            "on the courtyard stones, brow pressed to the ground, "
            "arms spread wide, the torn mantle pooled around the "
            "wreck of everything he owned — not collapsed but "
            "WORSHIPPING, the deliberate prostration of a man "
            "handing back what was given with the same open hands "
            "that received it — and over him only the torn grey sky, "
            "answering nothing, while he blesses the Name anyway. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b07", "out": "s07-i-have-said-my-piece.jpeg", "seg": "n7",
        "window": "195.06-198.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": "I have said my piece and I will not say it again.",
        "must_show": "the resolve — Job small and kneeling before the towering storm column, hand pressed over his own mouth, head slightly bowed; the argument laid down.",
        "must_not_show": "ABSOLUTE: no figure in the storm; his silence PEACEFUL, not crushed.",
        "scene": (
            "The argument is laid down for good: Job kneeling small "
            "on the plain before the vast slow-turning column, his "
            "hand pressed flat over his own mouth, head inclined — "
            "not a beaten man's cringe but a settled man's seal, the "
            "posture of somebody who has finally heard something "
            "better than his own case — while the great storm turns "
            "patiently above him, silver-veined and figureless, "
            "asking nothing more of him than the quiet he is already "
            "keeping. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r120-b08", "out": "s08-i-came-into-this-world.jpeg", "seg": "n2b",
        "window": "40.08-47.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB"],
        "narration": (
            "I came into this world with nothing and I will leave with "
            "nothing. God gave it and God has taken it, and I will bless him "
            "anyway."
        ),
        "must_show": "the blessing through tears — close on Job's lifted face under the storm-grey sky, tear-tracks cutting the dust on his cheeks, the mouth still shaping blessing.",
        "must_not_show": "no halo; grief and worship in the SAME face — neither erased by the other.",
        "scene": (
            "The face doing the blessing fills the frame: Job's "
            "lifted features under the storm-grey light, tear-tracks "
            "cutting clean lines through the dust on his weathered "
            "cheeks, the deep-set eyes wrecked and open, the mouth "
            "in the grey-streaked beard still moving through the "
            "words — grief and worship occupying the same face at "
            "the same moment without either one giving ground, which "
            "is the whole astonishment of the man. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b09", "out": "s09-he-is-not-calm-when.jpeg", "seg": "n2b",
        "window": "47.67-52.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB"],
        "narration": (
            "He is not calm when he says it. He has just torn his coat and "
            "shaved his head."
        ),
        "must_show": "the evidence of grief — the torn mantle gripped in his fists, the newly bare scalp, the body's honest wreckage; nothing serene about the blessing.",
        "must_not_show": "no halo; no self-harm beyond the torn cloth and shaved head scripture names.",
        "scene": (
            "The cost of the sentence is worn on the body: the "
            "russet mantle hangs in two ragged halves from Job's "
            "clenched fists, threads still trailing from the tear, "
            "the newly shaven scalp raw-pale above the dark beard, "
            "shoulders heaving with breath that has not steadied — "
            "every visible inch of the man testifying that the "
            "blessing was not spoken from calm but hauled up out of "
            "the wreckage by main strength, which is what makes it "
            "worth the book it is written in. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b10", "out": "s10-he-is-wrecked-and-still.jpeg", "seg": "n2b + n3",
        "window": "52.23-59.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": (
            "He is wrecked, and still holding on. He sat down in the ashes, "
            "sick and broken, and he did not pretend to be all right."
        ),
        "must_show": "SCRIPTURE-EXACT: the ash heap — Job seated in the pale grey mound with a potsherd in his hand, gaunt and ill, ash-dusted, under flat grey light; broken and enduring at once.",
        "must_not_show": "ABSOLUTE: illness with dignity — no gore, no detailed sores; his skin warm and human under the ash dust, never corpse-grey.",
        "scene": (
            "The greatest man of the east now holds one broken piece "
            "of pottery: Job seated deep in the pale mound outside "
            "the settlement wall, the torn robe loose on a frame "
            "gone gaunt, grey ash dusted over warm living skin, the "
            "potsherd resting in his hand between uses — sick, "
            "diminished, and not pretending otherwise to anyone — "
            "yet still upright in the ashes, still facing the flat "
            "grey horizon, a man wrecked to the waterline and "
            "somehow not sunk. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r120-b11", "out": "s11-he-grieved-out-loud-and.jpeg", "seg": "n3",
        "window": "59.88-63.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": "He grieved out loud. And scripture never once scolds him for it.",
        "must_show": "the loud grief — Job's head thrown back in the ashes, mouth open in honest lament at the sky; grief given full voice and full permission.",
        "must_not_show": "no halo; the lament HONEST, never grotesque — a man crying out, not a gargoyle.",
        "scene": (
            "The grief gets its voice: Job's head thrown back in the "
            "grey mound, the cords of his neck standing, mouth open "
            "in a lament aimed straight up at the flat sky — nothing "
            "swallowed, nothing performed, the full honest volume of "
            "a man saying exactly how much it hurts to the only One "
            "with authority over the hurting — and no scold anywhere "
            "in the frame or the book, the sky receiving the sound "
            "the way scripture receives it: without one word of "
            "rebuke. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r120-b12", "out": "s12-his-friends-came-and-at.jpeg", "seg": "n4",
        "window": "64.24-70.06", "wide": True, "jesus": False, "ref": False,
        "locks": ["JOB", "FRIENDS", "ASHES"],
        "narration": (
            "His friends came, and at first they simply sat with him — which "
            "was the best thing they did."
        ),
        "must_show": "SCRIPTURE-EXACT: the seven-day silence — the camera behind the three friends seated in a quiet arc around ash-seated Job under the open sky; presence without words, their best act.",
        "must_not_show": "no halo; no one speaking, no gestures — the stillness IS the comfort.",
        "scene": (
            "Their best hour is their quietest, the camera set low "
            "behind the three friends' seated backs: Eliphaz, Bildad "
            "and Zophar in a still arc on the ash mound's edge, "
            "travel-dust on their dark robes, and past their "
            "shoulders the shaved and broken figure of their friend "
            "seated in the grey — four men and no words under the "
            "whole flat sky, seven days of simply staying, the kind "
            "of company that asks nothing and explains nothing and "
            "is worth every speech they will ruin it with later. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b13", "out": "s13-you-must-have-sinned-they.jpeg", "seg": "n4",
        "window": "71.89-75.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "FRIENDS", "ASHES"],
        "narration": "You must have sinned, they said. This must be your fault.",
        "must_show": "the accusation — Eliphaz's raised admonishing finger, the other two nodding gravely, Job receiving the verdict with weary disbelief.",
        "must_not_show": "no halo; the cruelty COMFORTABLE — reasonable faces delivering an unreasonable verdict.",
        "scene": (
            "The verdict arrives wearing kindness: Eliphaz's finger "
            "raised in gentle silver-bearded certainty, Bildad "
            "nodding the slow nod of settled arithmetic, Zophar's "
            "lean face already composing the next point — three "
            "reasonable men explaining to the man in the ashes that "
            "suffering this size must have been earned — and on "
            "Job's dusted face the weary disbelief of the innocent "
            "listening to their own conviction, delivered by friends "
            "who mean well with every merciless word. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b14", "out": "s14-their-tidy-answers-only-deepened.jpeg", "seg": "n4 + n5",
        "window": "75.44-82.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "FRIENDS", "ASHES"],
        "narration": (
            "Their tidy answers only deepened the wound. But Job would not "
            "accept easy lies about God or about himself."
        ),
        "must_show": "the refusal — Job's flat raised hand stopping the three mid-speech, jaw set through the grief; wounded but unbending on the truth.",
        "must_not_show": "no halo; his refusal DIGNIFIED — no rage-contortion; the friends stopped, not cowed.",
        "scene": (
            "The broken man draws one line he will not let anyone "
            "cross: Job's hand comes up flat from the ashes, "
            "stopping all three explanations mid-sentence — the arm "
            "trembling with weakness and steady with conviction at "
            "once, the set of the bearded jaw saying what the hand "
            "says: not that lie — not about God, and not about me — "
            "while the three friends hang paused around his refusal, "
            "their tidy arithmetic meeting the one man honest enough "
            "to stay in the pain rather than buy their exit from it. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b15", "out": "s15-he-did-something-braver-than.jpeg", "seg": "n5",
        "window": "82.38-84.75", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": "He did something braver than pretending.",
        "must_show": "the rising — Job pushing up from the ash mound onto his feet, the potsherd dropped, weakness and resolve in the same body.",
        "must_not_show": "no halo; the effort REAL — a sick man standing, not a hero's spring.",
        "scene": (
            "The braver thing begins with getting up: Job pushing "
            "himself from the grey mound onto unsteady feet, the "
            "potsherd left where it falls, one hand braced on his "
            "own knee, the torn robe hanging off the gaunt frame — "
            "every inch of the rise costing him — and in the lifted "
            "line of the shaved head something the seated "
            "explanations around him never had: the intent of a man "
            "done arguing with middlemen, straightening to address "
            "the Owner of the storm directly. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b16", "out": "s16-he-took-his-anguish-straight.jpeg", "seg": "n5",
        "window": "84.75-90.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": (
            "He took his anguish straight to God and demanded an answer — "
            "and then, in the middle of it, he said this."
        ),
        "must_show": "the demand — Job upright in the ashes, arms flung wide at the empty grey sky, anguish and faith in one hurled posture; honest fury aimed at heaven.",
        "must_not_show": "ABSOLUTE: no answering figure or light yet — the sky stays empty and grey.",
        "scene": (
            "The complaint goes straight to the top: Job upright on "
            "the ash mound with both arms flung wide at the flat "
            "grey emptiness, head back, the torn sleeves sliding "
            "down thin arms, hurling his anguish upward with the "
            "unembarrassed directness of a man who still believes "
            "Somebody is listening — which is itself the faith — "
            "fury and trust tangled in one thrown-open posture "
            "beneath a sky that offers, for now, not one visible "
            "thing back. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r120-b17", "out": "s17-for-i-know-that-my.jpeg", "seg": "s1925",
        "window": "91.50-96.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": (
            "For I know that my redeemer liveth, and that he shall stand at "
            "the latter day upon the earth."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — dusk over the ash heap, first stars out, Job stilled with one hand on his chest, face lifted to the darkening east; certainty arriving mid-ruin.",
        "must_not_show": "ABSOLUTE: no depicted redeemer, no vision in the sky — the knowing is IN THE MAN, not the clouds.",
        "scene": (
            "In the middle of the wreckage, certainty: dusk settling "
            "violet over the ash heap, the first two or three stars "
            "out above the ridge, and Job gone suddenly still — one "
            "hand flat over his own chest, face lifted to the "
            "darkening east, the anguish parted around a sentence he "
            "does not doubt even now — nothing in the sky but "
            "evening, and everything in the man: somewhere past all "
            "this, alive right now, his redeemer — and one day, on "
            "this very dust, those feet will stand. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b18", "out": "s18-that-is-a-man-in.jpeg", "seg": "n5b",
        "window": "97.98-102.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": "That is a man in the ashes with nothing left, saying it out loud.",
        "must_show": "the scale of the saying — the small upright figure alone on the dusk ash field, speaking aloud to the sky; the confession measured against the emptiness around it.",
        "must_not_show": "no halo; his aloneness TOTAL in the frame — no audience anywhere.",
        "scene": (
            "The size of the sentence is the size of the emptiness "
            "it was said into: one small upright figure alone on the "
            "darkening ash field, torn-robed, shaved-headed, "
            "possessing exactly nothing, speaking out loud to a "
            "violet sky with no audience, no witness and no "
            "prompter — the confession hanging in the dusk air over "
            "the grey mound with nothing to hold it up except the "
            "man's own unbroken knowing, which turns out to be "
            "enough. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r120-b19", "out": "s19-he-does-not-understand-a.jpeg", "seg": "n5b",
        "window": "102.09-107.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": (
            "He does not understand a thing that is happening to him, and he "
            "still knows who is coming."
        ),
        "must_show": "the paradox in one face — close on Job at dusk: bewilderment in the lines, certainty in the eyes fixed on the eastern horizon; not-understanding and knowing together.",
        "must_not_show": "no halo; nothing on the horizon — the coming is KNOWN, not shown.",
        "scene": (
            "Both truths share the one face: close in the last "
            "violet light, Job's features carrying total "
            "bewilderment in every furrow — a man who cannot explain "
            "one hour of what has happened to him — while the "
            "deep-set eyes hold steady on the empty eastern horizon "
            "with the calm of a man watching a road he knows will be "
            "used — comprehension gone, confidence intact, the two "
            "living side by side in him the way they have lived in "
            "every honest believer since. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b20", "out": "s20-and-god-answered-though-not.jpeg", "seg": "n6",
        "window": "108.31-115.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": (
            "And God answered — though not in the way anyone expected. Out "
            "of a great whirlwind, the Maker of everything finally spoke."
        ),
        "must_show": "SCRIPTURE-EXACT: the whirlwind's arrival — the vast slow-turning storm column standing on the plain before tiny upright Job; majesty without destruction.",
        "must_not_show": "ABSOLUTE: no figure, face or form in the storm — the column is weather, and the voice is not visible.",
        "scene": (
            "The answer arrives as weather: out of the bruised "
            "silver sky a vast column of slow-turning storm comes "
            "down to stand on the plain — dark grey walls of cloud "
            "wheeling from the ground to heaven, veined with quiet "
            "lightning, lit faintly from within — and before it, "
            "tiny and upright and not running, the ash-grey figure "
            "of the man who demanded this audience, getting it at a "
            "scale no courtroom of friends ever imagined: the Maker "
            "of everything, speaking at last, in wind. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b21", "out": "s21-where-wast-thou-when-i.jpeg", "seg": "jvA",
        "window": "116.26-120.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": "Where wast thou when I laid the foundations of the earth?",
        "must_show": "SCRIPTURE-EXACT: the first question — Job braced small at the storm's skirts, dust and torn robe streaming, the moving air itself the only speaker.",
        "must_not_show": "ABSOLUTE: no mouth, face or figure in the cloud; Job awed, never harmed.",
        "scene": (
            "The first question lands with the wind leaning on him: "
            "Job braced at the great column's skirts, robe and beard "
            "streaming sideways, one foot set back to hold his "
            "ground, dust rivering past his ankles — and around him "
            "the storm turning its unhurried miles of cloud, the "
            "question arriving out of the moving air itself with no "
            "mouth to point to — a man who demanded the witness "
            "stand discovering he is the one being asked to answer "
            "for the architecture of the world. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b22", "out": "s22-declare-if-thou-hast-understanding.jpeg", "seg": "jvA + n6b",
        "window": "120.40-126.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": (
            "declare, if thou hast understanding. It sounds like a rebuke, "
            "and it is not."
        ),
        "must_show": "the listening — Job's wind-whipped face working between fear and dawning wonder as the storm speaks; the question's true tone landing.",
        "must_not_show": "ABSOLUTE: no figure in the storm; his fear TURNING, not crushed — wonder gaining.",
        "scene": (
            "The tone underneath the thunder starts to reach him: "
            "close on Job's wind-whipped face at the storm's edge, "
            "grey beard flattened along his jaw, eyes squinted "
            "against the flying grit — and in them, mid-question, "
            "the change: the flinch of a man braced for sentencing "
            "loosening into the wide look of a man beginning to "
            "suspect the voice is not angry — that what is rolling "
            "over him in miles of wind is not the prosecution he "
            "expected but something stranger and better. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b23", "out": "s23-god-is-doing-something-gentler.jpeg", "seg": "n6b",
        "window": "126.94-129.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": "God is doing something gentler than that.",
        "must_show": "the gentling — the storm's inner light softening, its skirts stilling around the small standing man; gentleness at colossal scale.",
        "must_not_show": "ABSOLUTE: no figure; the softening in LIGHT and motion, never a shape.",
        "scene": (
            "The colossus gentles: around the small standing figure "
            "the storm's skirts slow their wheeling, the dust "
            "settling out of the air in drifting veils, the dark "
            "walls of cloud easing from iron-grey toward a soft "
            "silver lit quietly from within — the whole vast "
            "apparatus of the whirlwind turning down its power "
            "around one ash-dusted man the way strength gentles "
            "around something it has no intention of breaking — "
            "gentleness performed at the scale of weather. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b24", "out": "s24-he-is-taking-a-man.jpeg", "seg": "n6b",
        "window": "129.48-135.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": (
            "He is taking a man who has shrunk down to the size of his own "
            "pain, and slowly widening the room."
        ),
        "must_show": "the widening — Job small at the frame's edge while sky and lit plain open enormous around him; the composition itself doing the doctrine.",
        "must_not_show": "no halo; Job never diminished MOCKINGLY — small in a frame that is opening, not crushing.",
        "scene": (
            "The cure is performed by the picture itself: Job stands "
            "small at the frame's lower edge, and everything else "
            "opens — the storm-silver sky climbing enormous over "
            "him, the plain running lit and vast to hills he had "
            "forgotten were there, the great column's curve pulling "
            "the eye up and out — a man who had shrunk to the size "
            "of his own wound standing inside a room being widened "
            "around him, wall by wall, horizon by horizon, until the "
            "pain is still real but no longer the whole world. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b25", "out": "s25-when-the-morning-stars-sang.jpeg", "seg": "jv387",
        "window": "136.04-141.50", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "When the morning stars sang together, and all the sons of God "
            "shouted for joy."
        ),
        "must_show": "SCRIPTURE-EXACT: the world's first dawn — a newborn earth of young mountains and mist under a sky dense with brilliant morning stars; joy rendered as light. PERSON-FREE.",
        "must_not_show": "ABSOLUTE: no figures of any kind — no sons of God depicted; the shout is the light.",
        "scene": (
            "The vision opens on the first morning there ever was: a "
            "newborn world — young sharp mountains still wearing "
            "their first mist, rivers finding their courses in "
            "silver threads, seas holding their new shorelines — "
            "under a sky impossibly dense with brilliant morning "
            "stars, thick as spray, bright as singing, the whole "
            "firmament crowded with light that behaves like joy — "
            "creation's opening day remembered by the One who was "
            "there, with the gladness still in it. No people "
            "anywhere in this frame."
        ),
    },
    {
        "id": "v2-r120-b26", "out": "s26-that-is-god-describing-the.jpeg", "seg": "n7a",
        "window": "143.03-148.65", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "That is God describing the day the world was made — and it is "
            "not a lecture about power."
        ),
        "must_show": "the gladness of making — young seas and green plains under the world-dawn sky, beauty offered as memory, not might. PERSON-FREE.",
        "must_not_show": "ABSOLUTE: no figures; nothing stern in the light — the frame is DELIGHT.",
        "scene": (
            "The memory continues, and it is fond: young seas "
            "combing their first waves onto unwalked sand, green "
            "plains rolling out their first grass toward the "
            "mist-wrapped mountains, morning light moving over all "
            "of it like a hand smoothing a finished thing — nothing "
            "in the frame flexing, nothing lecturing, the whole "
            "world simply delighted in by the light that made it — "
            "power present everywhere and pointed at nothing, the "
            "way a craftsman's strength lives quietly inside his "
            "work. No people anywhere in this frame."
        ),
    },
    {
        "id": "v2-r120-b27", "out": "s27-it-is-a-memory-and.jpeg", "seg": "n7a + jvB",
        "window": "148.65-157.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB"],
        "narration": (
            "It is a memory, and it is full of gladness. Canst thou bind the "
            "sweet influences of Pleiades, or loose the bands of Orion?"
        ),
        "must_show": "SCRIPTURE-EXACT: the star question — night over the plain, the Pleiades cluster and Orion blazing enormous, Job's small upturned face lit by starlight below.",
        "must_not_show": "ABSOLUTE: no figure in the sky; the constellations ACCURATE — the seven-star cluster, the belted hunter.",
        "scene": (
            "The questions move to the night shelf: above the dark "
            "plain the sky stands enormous and clear — the Pleiades "
            "a tight glittering handful of seven, Orion striding "
            "wide with his three-starred belt, the winter powers "
            "hung exactly where they have hung since the first "
            "morning — and far below at the frame's foot, one small "
            "upturned face taking the starlight, being asked "
            "kindly whether he can knot or unknot any of it — the "
            "sweet influences going about their vast business "
            "overhead, gloriously out of reach. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b28", "out": "s28-i-had-only-ever-heard.jpeg", "seg": "n7c",
        "window": "217.31-219.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB"],
        "narration": "I had only ever heard about you, Job says.",
        "must_show": "the before-and-after face — close on Job, ash still on him, the new SEEING quiet in his eyes; hearsay faith replaced by acquaintance.",
        "must_not_show": "no halo; the change INTERIOR — same ruined man, different eyes.",
        "scene": (
            "The difference is all in the eyes: close on Job's face "
            "with the ash still dusted in the creases and the beard "
            "still ragged from the worst months of his life — "
            "nothing about the ruin repaired yet — but the deep-set "
            "eyes hold something they did not have in all his "
            "blameless years: acquaintance — the settled quiet of a "
            "man whose God has stopped being a report and become a "
            "voice he has personally stood inside, hearsay traded "
            "for knowing at the worst possible price and counted "
            "cheap. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r120-b29", "out": "s29-can-you-tie-up-the.jpeg", "seg": "n7b",
        "window": "159.41-168.82", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Can you tie up the Pleiades, God asks, or unfasten Orion's "
            "belt? On and on it goes — the sea, the snow, the wild donkey, "
            "the horse, the hawk."
        ),
        "must_show": "the tour of wild goodness — one sweeping frame: a hawk riding wind over a plain where a wild donkey runs free and a storm-maned horse stands unowned, the grey sea and far snowline beyond. PERSON-FREE.",
        "must_not_show": "ABSOLUTE: no figures, no fences, no harness — nothing in the frame is owned or tamed.",
        "scene": (
            "The tour sweeps the unowned world in one frame: a hawk "
            "hanging on the wind high over a tawny plain where a "
            "wild donkey runs flat-out for nobody's reason but its "
            "own, a storm-maned horse standing unbridled on the "
            "rise, and beyond them the grey sea working its shore "
            "with a far white snowline in the hills — not one fence, "
            "not one harness, not one owner anywhere — the whole "
            "wild inventory doing exactly as it pleases, and every "
            "bit of it fed, held and delighted in. No people "
            "anywhere in this frame."
        ),
    },
    {
        "id": "v2-r120-b30", "out": "s30-his-wealth-his-health-and.jpeg", "seg": "n2",
        "window": "13.88-18.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "HOME"],
        "narration": (
            "His wealth, his health, and — most unbearable of all — his "
            "children."
        ),
        "must_show": "the worst news — the far feast-house with its roof FALLEN, dust still hanging, and Job collapsing to his knees on the road before it; the loss told entirely at distance.",
        "must_not_show": "ABSOLUTE: no bodies, no victims, nothing close — the fallen roof at far distance and the father's knees buckling carry everything.",
        "scene": (
            "The last messenger's news does what the others could "
            "not: far across the plain the feast-house stands with "
            "its roof fallen in, one wall leaning, the dust of the "
            "great wind still hanging over it in the ugly light — "
            "and in the near ground Job goes down, knees buckling "
            "onto the road, a hand clamped over his mouth, the "
            "distance between him and that broken far building "
            "holding everything unbearable exactly where the "
            "picture can survive it — the wealth was nothing; this "
            "is his children. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r120-b31", "out": "s31-chapter-after-chapter-of-a.jpeg", "seg": "n7b",
        "window": "168.82-177.09", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Chapter after chapter of a world far bigger and stranger and "
            "kinder than the tidy little courtroom Job's friends had built."
        ),
        "must_show": "the bigger world — rain falling on wild country where no man lives, stars over a far snowfield, green life teeming in the wet; vastness with kindness in it. PERSON-FREE.",
        "must_not_show": "ABSOLUTE: no figures, no buildings — nothing tidy, nothing walled; the courtroom nowhere.",
        "scene": (
            "The answer keeps unrolling rooms nobody's tidy theology "
            "had keys to: rain falling in silver curtains on wild "
            "country where no man has ever lived — satisfying the "
            "desolate ground, says the voice, on purpose — green "
            "life crowding the wet gullies, and far above the "
            "showers a high snowfield holding the first stars of "
            "evening — a world vaster, stranger and kinder than any "
            "courtroom, being run at full generosity in places no "
            "witness will ever bill for — which is somehow part of "
            "the comfort. No people anywhere in this frame."
        ),
    },
    {
        "id": "v2-r120-b32", "out": "s32-behold-i-am-vile-what.jpeg", "seg": "s404",
        "window": "177.59-182.92", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": (
            "Behold, I am vile; what shall I answer thee? I will lay mine "
            "hand upon my mouth."
        ),
        "must_show": "SCRIPTURE-EXACT: the hand on the mouth — Job kneeling before the storm column, one hand laid flat over his own lips, head bowed; the case withdrawn.",
        "must_not_show": "ABSOLUTE: no figure in the storm; his humility WHOLE, not humiliated — reverence, not cringe.",
        "scene": (
            "The plaintiff withdraws his case: Job sinking to his "
            "knees on the plain before the great silver column, one "
            "hand rising to lie flat across his own mouth, head "
            "inclined — the ancient gesture of a man stopping his "
            "own words at the source — not beaten down into the "
            "posture but arriving at it, the way honesty arrives at "
            "silence when it finally hears something larger than "
            "its argument — the storm turning quietly on before "
            "him, patient as it has been all along. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b33", "out": "s33-once-have-i-spoken-but.jpeg", "seg": "s404",
        "window": "182.92-188.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": (
            "Once have I spoken; but I will not answer: yea, twice; but I "
            "will proceed no further."
        ),
        "must_show": "SCRIPTURE-EXACT: the vow of silence kept — Job settled back on his heels, hand still at his lips, the storm's wind gentling around his stillness.",
        "must_not_show": "ABSOLUTE: no figure in the storm; the stillness RESTFUL — a man done striving.",
        "scene": (
            "The silence holds and turns into rest: Job settled back "
            "on his heels in the storm's soft light, the hand still "
            "resting at his lips, shoulders down from the long "
            "fight, the torn robe quiet around him at last — twice "
            "he spoke and will not go on, and the not-going-on "
            "visibly costs him nothing now — while around his "
            "stillness the great column's wind gentles to a slow "
            "breathing, two silences keeping company on the wide "
            "plain. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r120-b34", "out": "s34-i-have-nothing-to-say.jpeg", "seg": "n7",
        "window": "190.14-195.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": (
            "I have nothing to say, Job answers. I am putting my hand over "
            "my mouth."
        ),
        "must_show": "the quiet answer — close on Job's face behind his own resting hand, eyes calm above it, peace beginning where the arguments ended.",
        "must_not_show": "no halo; nothing sullen — the mouth covered gladly, the eyes at ease.",
        "scene": (
            "The last answer is given by hand: close on Job's "
            "weathered face with his own fingers resting lightly "
            "over the mouth that argued so long and so honestly — "
            "and above the hand, the eyes: not smarting, not "
            "swallowing pride, but calm, the visible ease of a man "
            "who has discovered that having nothing to say can be a "
            "form of wealth — the peace starting exactly where the "
            "case ended, in the little silence he holds against his "
            "own lips. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r120-b35", "out": "s35-not-beaten-quieted-god-never.jpeg", "seg": "n7",
        "window": "198.51-201.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": "Not beaten — quieted. God never explained why.",
        "must_show": "the difference made visible — Job upright and easy under the storm's soft silver light, shoulders unburdened; quieted, with the why still unanswered.",
        "must_not_show": "ABSOLUTE: no figure in the storm; no answer-imagery — the why stays open in the frame.",
        "scene": (
            "The difference between beaten and quieted stands up "
            "straight: Job on his feet again under the column's "
            "soft silver, shoulders down and open, hands loose at "
            "his sides, face lifted without flinching into the "
            "moving light — nothing about him crushed, everything "
            "about him stilled — and nowhere in the whole reaching "
            "sky one syllable of explanation: the why he demanded "
            "never delivered, and the man somehow standing easier "
            "without it than he ever stood while he was owed it. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b36", "out": "s36-instead-he-showed-job-the.jpeg", "seg": "n7",
        "window": "201.67-209.47", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Instead he showed Job the sea and the stars and the wild "
            "goodness of a world Job could never have made or held."
        ),
        "must_show": "the showing — one last sweep: the grey-green sea thundering at dark cliffs under a sky wheeling with stars; wild goodness at full scale. PERSON-FREE.",
        "must_not_show": "ABSOLUTE: no figures — the sea and stars carry the whole frame.",
        "scene": (
            "What he got instead of answers: the sea, taking the "
            "dark cliffs in tall grey-green processions of thunder, "
            "spray hanging silver in the night air — and above the "
            "water, wheeling clear from horizon to horizon, the "
            "stars in their uncountable stations — the two oldest "
            "wildernesses in creation running their glad enormous "
            "business the way they have since the first morning, "
            "unmakeable and unholdable by any man, and offered to "
            "one broken one as comfort — which, against all "
            "arithmetic, they were. No people anywhere in this "
            "frame."
        ),
    },
    {
        "id": "v2-r120-b37", "out": "s37-and-somehow-it-was-enough.jpeg", "seg": "n7",
        "window": "209.47-211.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": "And somehow it was enough.",
        "must_show": "the enough — the storm column thinning and lifting from the plain, light coming through, Job standing quiet beneath the opening sky.",
        "must_not_show": "ABSOLUTE: no figure revealed as the storm thins — it opens to plain SKY and light.",
        "scene": (
            "Enough arrives without a single answer in its hands: "
            "the great column thinning as it lifts, its silver walls "
            "loosening into rags of bright cloud, clean light "
            "reaching the plain in widening lanes — and under the "
            "opening sky the small figure of Job standing quiet in "
            "the first of it, robe settling as the wind leaves, "
            "watching the storm that never explained anything "
            "ascend — and visibly, in the set of him, at peace with "
            "the trade. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r120-b38", "out": "s38-i-have-heard-of-thee.jpeg", "seg": "s425",
        "window": "211.85-215.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB"],
        "narration": (
            "I have heard of thee by the hearing of the ear: but now mine "
            "eye seeth thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the seeing — Job's face turned full into the clean light where the storm was, eyes open and filled; the verse made visible.",
        "must_not_show": "ABSOLUTE: nothing seen BY THE VIEWER in the light — no form; the seeing belongs to Job.",
        "scene": (
            "The verse happens on his face: Job turned full into "
            "the washed light pouring through where the storm was, "
            "eyes wide open and filled with it, the wet bright look "
            "of a man seeing what he had only ever been told about "
            "— the light itself empty of any form the picture can "
            "show, because the seeing is his and not ours — hearing "
            "traded for sight in the space of one storm, on the "
            "face that paid full price for the upgrade. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b39", "out": "s39-now-i-have-seen-you.jpeg", "seg": "n7c",
        "window": "219.99-223.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": "Now I have seen you with my own eyes. That is the ending.",
        "must_show": "the ending as morning — the ash field gone quiet under arriving morning light, Job upright in it, the sky washed clean; an ending made of presence, not events.",
        "must_not_show": "no halo; no restored wealth yet — the ending here is the SEEING, nothing material.",
        "scene": (
            "The ending looks like nothing but morning: the ash "
            "field lying quiet under a washed clean sky, the grey "
            "mound just a place again, and Job upright in the "
            "middle of it with the new light full on him — no "
            "restored flocks in the frame, no returned wealth, "
            "nothing repaired except the one thing that was "
            "actually broken — a man who has seen with his own "
            "eyes, standing in an ordinary morning that is somehow "
            "the ending of the whole book. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r120-b40", "out": "s40-not-because-he-got-his.jpeg", "seg": "n7c",
        "window": "223.56-227.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": (
            "Not because he got his answer, but because he got God himself."
        ),
        "must_show": "the trade — close on Job at peace in the morning light, the searching gone from his face; presence received where explanation was demanded.",
        "must_not_show": "no halo; his peace UNDECORATED — plain light on a plain face, fully at rest.",
        "scene": (
            "What settled him is visible by what is missing: close "
            "on Job's face in the plain morning light, and the "
            "searching that lived in every earlier frame — the "
            "scanning, the asking, the braced waiting for a verdict "
            "— simply gone, the features at rest the way a house "
            "rests when its owner is home — a man who came "
            "demanding an explanation and walked out holding an "
            "acquaintance, wearing the unarguable peace of the "
            "better bargain. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r120-b41", "out": "s41-the-suffering-was-never-fully.jpeg", "seg": "n8",
        "window": "227.96-234.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "ASHES"],
        "narration": (
            "The suffering was never fully explained — not to Job, and not "
            "to us. But Job was no longer alone in it."
        ),
        "must_show": "the companioned grief — Job walking from the ash heap toward the settlement in morning light, the mound behind him, his carriage changed; still bereaved, no longer alone.",
        "must_not_show": "no halo; no companion FIGURE beside him — the not-alone is in his bearing, not a body.",
        "scene": (
            "He leaves the ashes differently than he sat down in "
            "them: Job walking from the grey mound toward the "
            "settlement wall in the young light, the torn robe "
            "still torn, the grief still real in the set of his "
            "shoulders — but the walk itself changed, unhurried and "
            "accompanied in some way no second figure in the frame "
            "explains — a man carrying the same unexplained sorrow "
            "out of the same ash field, and visibly not carrying it "
            "by himself anymore. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r120-b42", "out": "s42-the-god-he-thought-had.jpeg", "seg": "n8",
        "window": "234.45-241.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOB", "WHIRLWIND"],
        "narration": (
            "The God he thought had abandoned him had come near, and that "
            "nearness was the answer his grief actually needed."
        ),
        "must_show": "the closing frame — the wide morning plain with the last silver shred of the storm ascending far off, and Job small and steady walking home into the light.",
        "must_not_show": "ABSOLUTE: no figure in the departing cloud; the nearness stated by LIGHT on the road home.",
        "scene": (
            "The book closes on a plain that has been visited: "
            "morning running the whole width of the tawny land, the "
            "last high silver shred of the whirlwind ascending far "
            "off like a guest departing satisfied, and down the lit "
            "road toward home the small steady figure of Job "
            "walking into the light with the sun warm on his "
            "shaved head — nothing explained, everything answered "
            "— the nearness that came down in the storm still lying "
            "over the whole morning like weather that has decided "
            "to stay. Every figure has two arms, two hands and one "
            "head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
