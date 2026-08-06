#!/usr/bin/env python3
"""V2 beat map — row 56, build-56-widow-of-nain (Luke 7:11-17).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 22 pictures over 117.6 s narration = 5.3 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Luke 7:11-17 KJV):
  v11  he went into a city called NAIN; many of his disciples went with him,
       and MUCH PEOPLE — two crowds are in this story.
  v12  when he came nigh to THE GATE of the city, behold, a DEAD MAN CARRIED
       OUT, the ONLY SON of his MOTHER, and she was A WIDOW: and MUCH PEOPLE
       OF THE CITY was with her — the two processions MEET at the gate;
       life's crowd walking in, death's crowd walking out.
  v13  when the Lord SAW HER, he had COMPASSION ON HER, and said unto her,
       "WEEP NOT." — she never asks; she never speaks; HE SEES HER. That is
       the Seed of the whole build (CONTENT-CARE G: *he saw HER, he stopped,
       he felt it*).
  v14  he came and TOUCHED THE BIER: and THEY THAT BARE HIM STOOD STILL.
       "Young man, I say unto thee, Arise."
  v15  he that was dead SAT UP, and BEGAN TO SPEAK. And he DELIVERED HIM TO
       HIS MOTHER — the handover is its own beat; he does not keep him.
  v16  there came A FEAR ON ALL: and they GLORIFIED GOD: "a great prophet is
       risen up among us"; "God hath visited his people."
  v17  this RUMOUR of him went forth throughout ALL the region.

CONTENT-CARE — FLAG G, THE GRIEF-CARE LAW (this story is §3 table's "widow's
dead son" entry): the dead young man is shown the way scripture shows it —
the still SLEEPING FORM on the open bier, wrapped to the chest, face
peaceful; NEVER anything a bereaved parent could not bear to see. No decay,
no pallor played for horror. The build's emotional centre is v13 — he saw
HER — and the closing never implies a promised refund of the same miracle
today; the raising reveals WHO GOD IS toward the grieving.

TIME-OF-DAY ARC: one bright late morning at the gate of Nain (funerals went
out by day); the closing news-beat runs into the same day's golden evening.

CAST-REF NOTE: when the first still with the widow's face is ACCEPTED at QC,
copy it to CAST-REF-V2/widow-ref.jpeg and add
"char_refs": ["CAST-REF-V2/widow-ref.jpeg"] to every later legible-face beat.
Same for the son (son-ref.jpeg: b17-b20). Text locks alone do not hold a face.
"""

LOCKS = {
    "WIDOW": (
        "WIDOW LOCK: the mother is the same woman in every shot — about "
        "fifty-five, small and worn thin by two bereavements, olive skin "
        "lined deep around the eyes, grey-streaked dark hair under a DARK "
        "CHARCOAL-GREY mourning veil and head covering. She wears mourning "
        "clothes: a DEEP CHARCOAL-BROWN wool dress, RENT at the collar in "
        "the mourner's tear, and a dark ash-grey shawl; never cream, never "
        "white. Her face is shown clearly."
    ),
    # He is raised at v15; the lock fixes face and build, each beat states
    # his condition (still form -> sitting, speaking, alive).
    "SON": (
        "SON LOCK: the young man is the same in every shot — about "
        "eighteen, slight, his mother's fine features, thick dark curly "
        "hair, the first soft young beard on his jaw. On the bier he lies "
        "wrapped to the chest in a DARK MADDER-RED burial cloth over a "
        "plain dark tunic, his face uncovered and peaceful as sleep; "
        "nothing on or around him is cream, off-white or any pale "
        "near-white cloth. His face is shown clearly."
    ),
    "NAIN": (
        "NAIN LOCK: the town of Nain on its hillside — a small Galilean "
        "town of flat-roofed limestone houses behind a low wall, one "
        "arched stone GATE opening onto the dusty road, dry hills and "
        "field walls beyond. Both crowds — the travellers with Jesus and "
        "the townspeople with the funeral — wear SATURATED DEEP earth "
        "colours: dark chocolate brown, deep russet, burnt ochre, dark "
        "olive and dusty indigo wool, the mourners of the town in the "
        "darkest of them; every garment plainly darker than the sunlit "
        "stone; no one in either crowd wears cream, off-white, ivory or "
        "any pale near-white cloth."
    ),
    "BIER": (
        "BIER LOCK: the bier is an OPEN flat wooden pallet with two long "
        "carrying poles, borne shoulder-high by FOUR bearers in dark "
        "earth-brown wool; the young man lies on it in plain view, "
        "wrapped to the chest in the dark madder-red cloth, face "
        "uncovered. Every bearer's hands grip the poles; the poles rest "
        "on their shoulders; nothing floats."
    ),
}

REF = True

# The committed V1 luke-7_widow-of-nain.mp4 is a STALE longer render (190.798s)
# than the re-voiced segment mp3s actually sum to (139.697s timeline). Per the
# assembler's prescribed in-file fix (documented in v2_assemble.py; used on row
# 53), rebuild the authoritative track from the verified V1 segment mp3s at the
# extract_beats offsets and hash-verify. Nothing is re-voiced; V1 stays read-only.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r056-b01", "out": "s01-nearing-nain.jpeg", "seg": "n1 p1",
        "window": "0.28-4.39", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NAIN"],
        "narration": ("As Jesus came near the town of Nain, a great crowd "
                      "walked along with him."),
        "must_show": "v11 — the travelling crowd on the road, Jesus among them, the town on its hill ahead.",
        "must_not_show": "no halo/glow; an ordinary good-spirited road crowd — nobody knows what is at the gate.",
        "scene": (
            "On the dusty uphill road in bright late-morning light, "
            "the camera off the verge taking the column from the side, "
            "Jesus walks in the midst of a large travelling crowd — "
            "disciples close around him, families with bundles, talk "
            "and easy movement all through the column — while ahead of "
            "them, up the road, the limestone town of Nain sits on its "
            "hillside behind its low wall, its arched gate facing them. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b02", "out": "s02-something-at-the-gate.jpeg", "seg": "n1 p2",
        "window": "4.39-12.21", "wide": True, "jesus": False, "ref": False,
        "locks": ["NAIN"],
        "narration": ("It was an ordinary day on an ordinary road, until "
                      "they reached the town gate and met something coming "
                      "the other way."),
        "must_show": "the collision course — from behind the travellers: the dark funeral procession just emerging from the arched gate ahead.",
        "must_not_show": "the two crowds have not met yet — the gap between them is closing and is the frame's subject.",
        "scene": (
            "THE CAMERA STANDS BEHIND THE TRAVELLING CROWD, over their heads up "
            "the road: the arched stone gate of Nain stands open ahead "
            "of them, and out of its shadow a second procession is "
            "emerging — dark-clothed, slow, close-packed — spilling "
            "down onto the same road, coming the other way. The bright "
            "walking crowd and the dark slow one face each other down "
            "one dusty stretch of road. Every figure has two arms and "
            "one head."
        ),
    },
    {
        "id": "v2-r056-b03", "out": "s03-out-came-a-funeral.jpeg", "seg": "n2 p1",
        "window": "12.21-13.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["SON", "BIER", "NAIN"],
        "narration": "Out of the gate came a funeral.",
        "must_show": "v12 — the bier in the gateway: four bearers, the open pallet shoulder-high, the still form on it.",
        "must_not_show": "G-law: the young man reads as SLEEPING — peaceful face, wrapped to the chest; nothing a bereaved parent could not bear.",
        "scene": (
            "Through the arched stone gate the funeral comes: four "
            "bearers in dark earth-brown wool carry the open bier "
            "shoulder-high into the sunlight, and on it the young man "
            "lies still, wrapped to the chest in the dark madder-red "
            "cloth, his face uncovered, peaceful, tipped slightly to "
            "one side like a sleeper's — the crowd of the town pressing "
            "dark and slow through the gate behind him. Every bearer's "
            "hands grip the poles. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r056-b04", "out": "s04-behind-him-his-mother.jpeg", "seg": "n2 p2",
        "window": "13.81-21.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW", "SON", "BIER", "NAIN"],
        "narration": ("A young man had died, carried out on an open bier, "
                      "and behind him walked his mother, a widow, "
                      "grieving."),
        "must_show": "v12 — the composition of the sorrow: the bier ahead, and immediately behind it the small veiled woman walking alone at the front of the town's crowd.",
        "must_not_show": "she walks in the place of chief mourner — first behind the bier, a step apart from everyone; the gap around her is her widowhood.",
        "scene": (
            "The procession in the bright road: the bier with its "
            "still burden borne ahead, and directly behind it, in the "
            "chief mourner's place, the small woman in charcoal "
            "mourning walks alone — her torn collar, her veil low, her "
            "eyes on the pallet's edge — with the whole crowd of the "
            "town following a respectful step behind her, so that a "
            "small moat of empty road surrounds the one person the "
            "sorrow belongs to most. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r056-b05", "out": "s05-her-only-son.jpeg", "seg": "n2 p3",
        "window": "21.27-24.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW"],
        "narration": "He was her only son, and now she had no one.",
        "must_show": "close on the widow's face under the veil — grief past weeping; the arithmetic of 'no one' in her eyes.",
        "must_not_show": "not wailing in this frame — the mourners wail; SHE is hollowed quiet, which is worse.",
        "scene": (
            "Close under the dark veil: the widow's lined face in the "
            "hard late-morning light, dry-eyed and hollowed out, her "
            "lips pressed to nothing, her gaze fixed on the bier ahead "
            "of her with the flat exhausted stare of a woman who has "
            "done this walk before — for her husband — and now walks "
            "it for the last person she had. Exactly one person is in "
            "the frame, with one head."
        ),
    },
    {
        "id": "v2-r056-b06", "out": "s06-the-town-walked-with-her.jpeg", "seg": "n2 p4",
        "window": "24.98-29.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW", "NAIN"],
        "narration": ("A large crowd from the town walked with her in her "
                      "sorrow."),
        "must_show": "the town's grief around her — mourners weeping and keening, a community carrying its saddest funeral.",
        "must_not_show": "their grief is real, not performance; and none of it can reach her.",
        "scene": (
            "Around and behind the lone widow the town's crowd fills "
            "the road — women keening with hands lifted, an old "
            "neighbour weeping openly into her shawl, men with heads "
            "bowed and jaws working, a child carried on a shoulder "
            "staring without understanding — a whole town grieving "
            "with one woman who walks alone inside it, untouched by "
            "any of it. Bright pitiless daylight. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b07", "out": "s07-she-never-asks.jpeg", "seg": "n3 p1-p2",
        "window": "29.73-35.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["WIDOW"],
        "narration": ("Here is what Luke does not record: a single word "
                      "from her. She never asks him for anything."),
        "must_show": "the not-asking — she walks head down, wholly inside the grief; the other crowd exists somewhere she is not looking.",
        "must_not_show": "no glance toward Jesus's crowd, no awareness of it at all.",
        "scene": (
            "The widow walks with her head down, the veil's edge "
            "cutting the world to a strip of road and the heels of "
            "the bearers ahead of her — her hands hang open and empty "
            "at her sides, past even wringing — a woman with no "
            "requests left in her, walking the only direction the day "
            "has, entirely unaware of the crowd halting on the road "
            "ahead. Exactly one person is in the frame, with two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b08", "out": "s08-the-processions-met.jpeg", "seg": "n3 p3-p4",
        "window": "35.29-41.02", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WIDOW", "SON", "BIER", "NAIN"],
        "narration": ("She does not know who he is. She is simply walking "
                      "behind her son's body."),
        "must_show": "v12 — the two crowds met and halted face to face outside the gate: life's procession and death's, stopped on one road.",
        "must_not_show": "nobody has spoken yet; the halt itself is the drama.",
        "scene": (
            "The wide frame holds both processions stopped face to "
            "face, the camera off to the side so the meeting reads "
            "in profile, on the sunlit road outside the gate: on one side the "
            "travelling crowd gone quiet around Jesus at its front, on "
            "the other the dark funeral bunched behind the bier and "
            "the lone veiled woman — a few paces of empty dust between "
            "the two worlds, and Jesus's eyes already fixed past the "
            "bier on the widow who has not yet looked up. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b09", "out": "s09-he-saw-her.jpeg", "seg": "s13a",
        "window": "41.02-46.89", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WIDOW"],
        "narration": ("And when the Lord saw her, he had compassion on "
                      "her, and said unto her, (Luke 7:13)"),
        "must_show": "THE Seed of the build — v13: Jesus's face SEEING her; compassion arriving on it like weather; her small veiled figure the object of the look.",
        "must_not_show": "his eyes go to HER, not the bier — the aim of the gaze is doctrine here.",
        "scene": (
            "Close past the edge of the bier: Jesus's face in the "
            "foreground, and his eyes have gone past the still form "
            "and the bearers to find the small veiled woman beyond "
            "it — and what crosses his face as he finds her is open, "
            "unguarded compassion, grief answering grief, the look of "
            "someone whose chest has just been struck — while she, "
            "soft in the background of the frame, still walks with "
            "her head down, unaware of being seen. Exactly two people "
            "are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r056-b10", "out": "s10-weep-not.jpeg", "seg": "jv13",
        "window": "46.89-49.31", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WIDOW"],
        "narration": "Weep not. (Luke 7:13)",
        "must_show": "the two words — Jesus stepped close before her, bent slightly to her height, the gentlest sentence in Luke.",
        "must_not_show": "he does not touch her; the words alone reach first.",
        "scene": (
            "Jesus has crossed the empty dust and stands close before "
            "the widow, bent slightly toward her smallness, his face "
            "low and near hers, saying it — and her head is just "
            "beginning to lift, the veil's shadow sliding back off "
            "her hollowed face, the words arriving somewhere so "
            "far inside her grief that her eyes have not yet found "
            "his. Bright daylight, the two processions blurred and "
            "waiting around them. Exactly two people are in the "
            "frame; each has one head."
        ),
    },
    {
        "id": "v2-r056-b11", "out": "s11-the-one-no-one-could-comfort.jpeg", "seg": "n3b p1-p2",
        "window": "49.31-54.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WIDOW"],
        "narration": ("Don't cry. Two words, to the one woman in that "
                      "whole procession nobody could comfort."),
        "must_show": "her face lifting fully — meeting the stranger's eyes for the first time; incomprehension, and underneath it, something being reached.",
        "must_not_show": "no recognition — she does not know who he is; only that someone has walked into her sorrow instead of around it.",
        "scene": (
            "The widow's face has come up under the veil and her "
            "eyes, red-rimmed and hollow, meet the eyes of this "
            "stranger who has stopped a whole road for her — her brow "
            "folding with incomprehension, lips parting on a question "
            "she does not have the strength to ask — while his face "
            "holds hers with a steadiness that no one has aimed at "
            "her in years. Exactly two people are in the frame; each "
            "has one head."
        ),
    },
    {
        "id": "v2-r056-b12", "out": "s12-he-could-not-walk-past.jpeg", "seg": "n3b p3-p4",
        "window": "54.27-60.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WIDOW", "SON", "BIER", "NAIN"],
        "narration": ("No one there had asked him to do a single thing. "
                      "He simply could not walk past her sorrow."),
        "must_show": "the wider stillness — the whole road stopped around the two of them; unasked mercy already in motion.",
        "must_not_show": "both crowds watch and wait; nobody understands yet, including his own disciples.",
        "scene": (
            "A wide frame of the halted road: at its centre Jesus "
            "stands with the tiny veiled widow, the two of them the "
            "only stillness with meaning in it — around them both "
            "processions hold their breath, disciples exchanging "
            "glances, mourners' keening faltering off, the bearers "
            "shifting under the bier's weight — an entire noon "
            "stopped in its tracks because one man would not walk "
            "past one woman's grief. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r056-b13", "out": "s13-what-no-one-does.jpeg", "seg": "n4 p1",
        "window": "60.53-63.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SON", "BIER"],
        "narration": "Then he did something no one does at a funeral.",
        "must_show": "the turn toward the bier — Jesus stepping from the widow toward the pallet, hand rising; the bearers' alarm beginning.",
        "must_not_show": "touching a bier makes a man unclean — the mourners' faces must register that something forbidden is coming.",
        "scene": (
            "Jesus has turned from the widow and steps toward the "
            "bier, his hand already rising toward its wooden edge — "
            "and the nearest bearer's eyes have gone wide over his "
            "shoulder, a mourner's hand flies up in half-protest, "
            "because every soul on that road knows what touching a "
            "dead man's bier costs — and he is not slowing down. "
            "Bright noon light on the still young face on the "
            "pallet. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r056-b14", "out": "s14-he-touched-the-bier.jpeg", "seg": "s14a",
        "window": "63.53-70.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SON", "BIER"],
        "narration": ("And he came and touched the bier: and they that "
                      "bare him stood still. And he said, (Luke 7:14)"),
        "must_show": "v14 — the hand flat on the bier's edge; the four bearers frozen mid-stride under their load.",
        "must_not_show": "the bearers do not set it down — they STAND STILL, shoulder-high, caught.",
        "scene": (
            "Jesus's hand lies flat and firm on the wooden edge of "
            "the bier, stopping it the way a hand stops a swinging "
            "door — and the four bearers have frozen mid-stride with "
            "the poles still on their shoulders, feet planted, "
            "knuckles whitening, four strong men held motionless by "
            "one touch — while the young man's peaceful face lies in "
            "the sun at the centre of the stillness. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b15", "out": "s15-young-man-arise.jpeg", "seg": "jv14",
        "window": "70.28-74.06", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SON", "BIER"],
        "narration": "Young man, I say unto thee, Arise. (Luke 7:14)",
        "must_show": "the address — Jesus bent over the bier, speaking DOWN to the still face as to a person, not a body.",
        "must_not_show": "no gesture of power — no raised arm; he talks to him, and that is all.",
        "scene": (
            "Jesus leans over the stopped bier, one hand still on its "
            "edge, his face bent close down toward the young man's "
            "sleeping face — speaking to him, plainly, directly, the "
            "way a person speaks to a person who can hear — the words "
            "already in the air between the two faces, one warm and "
            "one still. Exactly two people are in the frame; each has "
            "one head."
        ),
    },
    {
        "id": "v2-r056-b16", "out": "s16-waking-a-child.jpeg", "seg": "n4b",
        "window": "74.06-77.96", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("He said it the way you would wake a sleeping "
                      "child."),
        "must_show": "close on Jesus's face over the bier — the gentleness of the summons; death addressed in a bedtime voice.",
        "must_not_show": "no strain, no effort, no command-face; tenderness is the power on display.",
        "scene": (
            "Very close on Jesus's face bent low in the noon light: "
            "his eyes soft on the sleeping face below, the faintest "
            "lift at the corner of his mouth, his whole expression "
            "the one a father wears leaning over a child who has "
            "slept too long into the morning — infinitely gentle, "
            "entirely certain of being obeyed. Exactly one person is "
            "in the frame, with one head."
        ),
    },
    {
        "id": "v2-r056-b17", "out": "s17-he-sat-up.jpeg", "seg": "n5 p1",
        "window": "77.96-81.61", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SON", "BIER", "NAIN"],
        "narration": ("And the young man who had been dead sat up, and "
                      "began to speak."),
        "must_show": "v15 — the young man SITTING UP on the bier, eyes open, mid-word; the bearers staggering; the road detonating.",
        "must_not_show": "he sits up like a man waking — colour in his face, no horror-film stiffness anywhere.",
        "scene": (
            "The young man has sat straight up on the shoulder-high "
            "bier, the madder-red cloth fallen to his waist, his eyes "
            "open and blinking in the sun, his mouth moving — already "
            "talking, mid-question — while the four bearers stagger "
            "under the shifting weight with their faces gone white, "
            "and the front rank of both crowds recoils a full step "
            "with a gasp the picture can almost carry. Warm colour "
            "stands in his young face. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b18", "out": "s18-life-poured-back.jpeg", "seg": "n5 p2-p3",
        "window": "81.61-91.59", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SON", "BIER", "NAIN"],
        "narration": ("Life poured back into him at the sound of that "
                      "voice, as simply as morning comes. Death let go of "
                      "him, because it had no choice."),
        "must_show": "the aliveness — the young man being helped down off the bier onto his own feet, steady, alive in the plain sun.",
        "must_not_show": "no light effect; the proof is a young man's ordinary standing weight on the ordinary road.",
        "scene": (
            "The bearers have brought the bier down and the young man "
            "swings his own legs off it and takes his own weight on "
            "the road — standing, steadying, alive, the burial cloth "
            "sliding off into a bearer's stunned hands — while Jesus "
            "stands close by watching him come down the way a man "
            "watches a sunrise he ordered, and the crowds on every "
            "side press in against their own disbelief. Every figure "
            "has two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r056-b19", "out": "s19-gave-him-to-his-mother.jpeg", "seg": "n6 p1",
        "window": "91.59-94.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WIDOW", "SON"],
        "narration": ("And Jesus took him by the hand and gave him back "
                      "to his mother."),
        "must_show": "v15 — the handover: Jesus guiding the son's hand into the widow's hands; the completed gift.",
        "must_not_show": "Jesus gives him AWAY — the composition must hand the young man out of Jesus's grip into hers.",
        "scene": (
            "The handover: Jesus holds the young man's hand in his "
            "own and is placing it into his mother's two reaching "
            "hands — the widow's veil fallen back, her hollowed face "
            "cracking open, her fingers closing over her son's — the "
            "gift passing visibly from one grip to the other while "
            "the boy looks from the stranger to his mother, "
            "understanding almost none of it. Noon light. Exactly "
            "three people are in the frame; each visible hand has "
            "five fingers."
        ),
    },
    {
        "id": "v2-r056-b20", "out": "s20-back-in-her-arms.jpeg", "seg": "n6 p2",
        "window": "94.38-102.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WIDOW", "SON", "NAIN"],
        "narration": ("He did not keep him or make a spectacle of him; he "
                      "simply returned a son to the arms of the woman who "
                      "thought she had buried him."),
        "must_show": "the embrace — mother and son locked together; Jesus already stepping quietly back out of their moment.",
        "must_not_show": "Jesus recedes, claims nothing; the frame's centre belongs to the two of them.",
        "scene": (
            "The widow has her son crushed against her, her face "
            "buried in his neck, her small fists knotted in the back "
            "of his tunic, his own arms wrapped around his weeping "
            "mother — and a pace behind them Jesus is quietly "
            "stepping back, withdrawing from the centre he made, "
            "giving the moment entirely away to the two people it "
            "belongs to. The crowds close around the reunion. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b21", "out": "s21-they-glorified-god.jpeg", "seg": "n7 + s16",
        "window": "102.70-112.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WIDOW", "SON", "NAIN"],
        "narration": ("A holy fear fell on everyone there, and they "
                      "praised God, saying: That a great prophet is risen "
                      "up among us; and, That God hath visited his "
                      "people. (Luke 7:16)"),
        "must_show": "v16 — the two crowds become one congregation at the gate: hands lifted, faces awed, praise breaking out around the reunited pair.",
        "must_not_show": "fear AND praise together — awe with joy in it, not terror.",
        "scene": (
            "Outside the gate of Nain, the camera behind the mingled "
            "crowd's near shoulders, the two processions have "
            "dissolved into one rejoicing crowd: hands lifted to "
            "heaven all across the frame, an old mourner on his "
            "knees, women praising through tears, the empty bier "
            "abandoned on its side at the road's edge — and at the "
            "heart of it the mother with her arm locked around her "
            "living son, while Jesus stands among the people, one of "
            "them, the still point the praise swirls around. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r056-b22", "out": "s22-the-news-went-out.jpeg", "seg": "n7b",
        "window": "112.85-117.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["NAIN"],
        "narration": ("And the news of it went out through all the "
                      "country round about."),
        "must_show": "v17 — the story leaving Nain: runners and travellers carrying it out along the evening roads.",
        "must_not_show": "golden evening now; the town behind, the word ahead.",
        "scene": (
            "In the golden evening light the roads out of Nain carry "
            "the story: a young man runs flat-out down the hill road "
            "with the news, two travellers hurry the other way "
            "already telling it to each other with flying hands, and "
            "from the gate more townspeople stream out toward the "
            "scattered farms — while the town sits warm-lit on its hillside "
            "behind them, changed. An upright vertical photograph, "
            "the ground at the bottom of the frame and the sky at "
            "the top, the horizon level — the picture is the right "
            "way up. Every figure has two arms, two legs and one "
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

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "WIDOW": "CAST-REF-V2/widow.jpeg",
    "SON": "CAST-REF-V2/son.jpeg",
    "BIER": "CAST-REF-V2/bier.jpeg",
}
