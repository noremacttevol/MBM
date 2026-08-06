#!/usr/bin/env python3
"""V2 beat map — row 54, build-54-the-leper (Mark 1:40-45).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 24 pictures over 135.7 s narration = 5.7 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 1:40-45 KJV; law: Lev 13:45-46):
  v40  there came a leper to him, BESEECHING him, and KNEELING DOWN to him:
       "If thou wilt, thou canst make me clean." (s40) — he doubts the WILL,
       never the POWER.
  law  Lev 13:45-46: clothes rent, head bare, a covering upon his upper lip,
       crying "Unclean, unclean"; he dwells ALONE, WITHOUT THE CAMP — the
       loneliness beats (b01-b04) rest on this.
  v41  Jesus, MOVED WITH COMPASSION, PUT FORTH HIS HAND, and TOUCHED him:
       "I will; be thou clean." (jv41) — THE TOUCH LANDS BEFORE THE HEALING;
       the untouchable man is touched while still a leper. That order is the
       gospel of this build and beats b12-b15 must keep it.
  v42  AS SOON AS he had spoken, IMMEDIATELY the leprosy departed, and he
       was CLEANSED.
  v43-44 he straitly charged him: "say nothing to any man: but go thy way,
       shew thyself to the priest, and offer for thy cleansing those things
       which Moses commanded, for a testimony unto them." (j44)
  v45  but he went out and began to PUBLISH IT MUCH, and to BLAZE ABROAD the
       matter, insomuch that Jesus could NO MORE OPENLY ENTER INTO THE CITY,
       but was WITHOUT IN DESERT PLACES: and THEY CAME TO HIM FROM EVERY
       QUARTER.

CONTENT-CARE: row 54 is not in the §3 flag table = GREEN. Restraint applied
anyway: the leprosy shows as ashen, scaled, wasted patches on hands, forearms
and brow — pitiable, never grotesque or gory; no open wounds rendered in
detail. The dignity framing (like row 87's D-flag spirit): he is a man first,
a disease second, in every frame including the worst ones.

TIME-OF-DAY ARC (the text states none; self-consistent single day, then the
aftermath): grey early morning for the outcast beats (his cold hour) ·
mid-morning for the approach, the touch and the healing · noon for the
sending · afternoon for the road and the telling · a golden crowded evening
for the from-every-quarter close.

CAST-REF NOTE: when the first still with the leper's face is ACCEPTED at QC,
copy it to CAST-REF-V2/leper-ref.jpeg and add
"char_refs": ["CAST-REF-V2/leper-ref.jpeg"] to every later legible-face beat —
his face carries the before/after arc, so lock it early. Text locks alone do
not hold a face.
"""

LOCKS = {
    # His SKIN changes at v42 (that is the miracle), so the lock fixes only
    # face-structure, build and clothing; each beat states the skin's state.
    "LEPER": (
        "LEPER LOCK: the man is the same man in every shot — about "
        "thirty-five, tall but stooped, large-framed and half-starved, "
        "matted dark hair and a ragged dark beard, strong deep-set dark "
        "eyes. He wears torn, RENT layers of ragged DARK GREY-BROWN and "
        "DEEP UMBER wool wraps, a frayed cloth that can cover his lower "
        "face, bare feet wrapped in rags — never cream, never white. His "
        "face is shown clearly. He is a human being to pity and honour, "
        "never a horror to recoil from."
    ),
    "WILDS": (
        "WILDERNESS LOCK: the empty country outside a Galilean town — "
        "broken rocky slopes with thorn scrub and grey boulders, a rough "
        "lean-to shelter of sticks and stones against an outcrop, the "
        "town's flat roofs and its road visible FAR OFF below, always at "
        "a distance. The distance between the man and the town is the "
        "picture of his sentence."
    ),
    "ROADSIDE": (
        "ROADSIDE LOCK: the dusty road outside the town where the crowd "
        "walks with Jesus — packed dirt, low field walls, olive trees. "
        "The crowd are ordinary Galileans in SATURATED DEEP earth "
        "colours — dark chocolate brown, deep russet, burnt ochre, dark "
        "olive and dusty indigo wool — every garment plainly darker than "
        "the pale dust; no one in the crowd wears cream, off-white, "
        "ivory or any pale near-white cloth."
    ),
    "VILLAGE": (
        "VILLAGE LOCK: a small Galilean town of flat-roofed limestone "
        "houses around a market lane and a stone gate. Its people wear "
        "the same SATURATED DEEP earth colours as every crowd — dark "
        "browns, russet, ochre, olive, dusty indigo; no one wears cream, "
        "off-white or any pale near-white cloth."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r054-b01", "out": "s01-the-loneliest-life.jpeg", "seg": "n1 p1",
        "window": "0.28-3.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER", "WILDS"],
        "narration": ("In those days there was no lonelier life than a "
                      "leper's."),
        "must_show": "the sentence in one frame — one man utterly alone in broken country, the living town far beyond his reach.",
        "must_not_show": "no other person anywhere near him; the emptiness is the subject.",
        "scene": (
            "In grey early-morning light the man sits alone on a boulder "
            "beside his rough lean-to shelter high on the rocky slope, "
            "ragged wraps pulled around him against the cold, ashen "
            "scaled patches visible on the backs of his hands — and far "
            "below and beyond him, small with distance, the town lies "
            "warm in the first sun with smoke rising from its roofs, a "
            "whole world he is not allowed to enter. An upright vertical "
            "photograph, the ground at the bottom of the frame and the "
            "sky at the top, the horizon level — the picture is the "
            "right way up. Exactly one person is in the frame, with two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r054-b02", "out": "s02-kept-apart.jpeg", "seg": "n1 p2a",
        "window": "3.46-9.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["LEPER", "WILDS"],
        "narration": ("The disease wasted his skin, and the law kept him "
                      "apart from everyone he loved —"),
        "must_show": "the apartness enforced — a family passing on the far road while he stands off among the rocks, the gap between them the width of the frame.",
        "must_not_show": "the family does not jeer or flee in terror — they simply keep the distance everyone keeps; that ordinariness is the cruelty.",
        "scene": (
            "The camera holds both planes from the side, the road and "
            "the rocks in one profile: the man stands motionless among the grey boulders well off "
            "the road, his frayed cloth drawn up over his lower face — "
            "and across the whole width of the frame, on the far side of "
            "the morning road, a family walks toward the town: a father "
            "with a donkey, a mother with a child on her hip, giving the "
            "rocks their practised wide berth without even looking up. "
            "The empty ground between him and them is the widest thing "
            "in the picture. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r054-b03", "out": "s03-crying-unclean.jpeg", "seg": "n1 p2b",
        "window": "9.50-15.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER", "WILDS"],
        "narration": ("no home, no temple, no touch, made to cry out "
                      "'unclean' if anyone drew near."),
        "must_show": "Lev 13:45 — the law performed: his arm thrown up to warn off an approaching traveller, the cloth at his mouth, the word visibly leaving him.",
        "must_not_show": "the traveller is already turning aside; no confrontation, just the daily ritual of self-banishment.",
        "scene": (
            "A traveller with a staff has crested the rise too close, "
            "and the man has scrambled up off his boulder with one arm "
            "thrown out stiff in warning, his other hand pressing the "
            "frayed cloth over his upper lip, his eyes above it doing "
            "the shouting — while the traveller, twenty paces off, is "
            "already swerving wide off the path with his head down. "
            "Morning light, long cold shadows between them. Exactly two "
            "people are in the frame; each has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r054-b04", "out": "s04-no-kind-hand.jpeg", "seg": "n1 p3",
        "window": "15.79-19.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER"],
        "narration": "He had not felt a kind hand in years.",
        "must_show": "the hunger for touch — close on his own two hands holding each other, the only touch he gets.",
        "must_not_show": "restrained rendering of the disease: ashen scaled patches, wasted knuckles — pitiable, never gory.",
        "scene": (
            "Close on the man's hands in the grey light, one cradling "
            "the other in his lap — ashen, scaled patches across the "
            "wasted knuckles, rag-wrapped wrists — his own left hand "
            "gently rubbing warmth into his own right, the small "
            "unconscious gesture of a man who has been his own only "
            "comfort for years. Above them, out of focus, his bowed "
            "head. Exactly one person is in the frame; each visible "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r054-b05", "out": "s05-he-heard-jesus-was-near.jpeg", "seg": "n2 p1",
        "window": "19.44-23.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER", "WILDS", "ROADSIDE"],
        "narration": ("When he heard that Jesus was near, he did the "
                      "forbidden thing: he came close."),
        "must_show": "the decision in motion — him descending from his rocks TOWARD the distant crowd on the road, breaking his life's one rule.",
        "must_not_show": "SHOT FROM BEHIND him — his back to us, faced toward the crowd he is approaching; the direction must read at a glance.",
        "scene": (
            "SHOT FROM BEHIND THE MAN AND ABOVE, his back to the camera "
            "as he picks his way DOWN the rocky slope AWAY from us, his "
            "ragged wraps loose around him, one hand out on the "
            "boulders for balance — and below him, IN THE DIRECTION HE "
            "IS MOVING, the mid-morning road carries a knot of distant "
            "figures around one centre, the crowd he is forbidden to "
            "enter and is entering anyway. Exactly the crowd is far; "
            "he is near; the slope runs him straight at them. Every "
            "figure has two arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r054-b06", "out": "s06-he-fell-on-his-knees.jpeg", "seg": "n2 p2",
        "window": "23.57-26.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER", "ROADSIDE"],
        "narration": "He fell on his knees and begged him.",
        "must_show": "v40 — the leper DOWN on his knees in the road dust before Jesus; the crowd breaking backward away from him; Jesus not moving.",
        "must_not_show": "no halo/glow; the crowd's recoil frames the one man who stands still.",
        "scene": (
            "The ragged man has thrown himself onto his knees in the "
            "dust of the road at Jesus's feet, hands clasped up toward "
            "him, the cloth fallen from his marked face — and the "
            "crowd has burst backward off the road in every direction "
            "like water from a dropped stone, mothers snatching "
            "children, men stumbling over the field wall — while at "
            "the still centre Jesus stands exactly where he stood, "
            "looking down at the kneeling man. Mid-morning sun. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r054-b07", "out": "s07-if-thou-wilt.jpeg", "seg": "s40",
        "window": "26.33-30.57", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER"],
        "narration": "If thou wilt, thou canst make me clean. (Mark 1:40)",
        "must_show": "the sentence on his face — upturned, pleading, the ashen marks plain; Jesus's presence at the frame edge receiving it.",
        "must_not_show": "his eyes hold no doubt of the POWER — only the terrible question of the WILL.",
        "scene": (
            "A tight shot from beside Jesus's shoulder, down onto the "
            "kneeling man's upturned face: ashen scaled patches at his "
            "brow and jaw, tears cutting through the grime, and in his "
            "strong deep-set eyes a strange steady certainty — a man "
            "who knows perfectly well this stranger CAN, asking only "
            "whether he WILL. His clasped hands reach up into the "
            "bottom of the frame. Exactly two people are in the frame; "
            "each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r054-b08", "out": "s08-never-doubted-the-power.jpeg", "seg": "n2b p1-p2",
        "window": "30.57-35.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER"],
        "narration": ("If you are willing, he said, you can make me clean. "
                      "He never doubted the power."),
        "must_show": "the two-shot — the kneeling man's plea held in the air, Jesus's face bent down toward him, already answering before the words.",
        "must_not_show": "no recoil anywhere in Jesus's posture — he has leaned TOWARD the man everyone leans away from.",
        "scene": (
            "A close two-shot in the bright morning light: the kneeling "
            "man's marked face lifted, the plea just spoken — and Jesus "
            "bent slightly down toward him, his face open and grave, "
            "his whole posture inclined toward the man like a listener "
            "drawing nearer, the crowd a scattered blur of earth "
            "colours far behind them. Exactly two people are in the "
            "frame; each has one head."
        ),
    },
    {
        "id": "v2-r054-b09", "out": "s09-would-he-bother.jpeg", "seg": "n2b p3",
        "window": "35.40-41.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER"],
        "narration": ("He only wondered about the will — whether a man "
                      "like him was someone Jesus would want to bother "
                      "with."),
        "must_show": "the real wound — close on his eyes: hope fighting years of learned worthlessness.",
        "must_not_show": "nothing else in frame competes with the eyes.",
        "scene": (
            "Very close on the kneeling man's face, the road and light "
            "gone soft around it: his eyes flick upward and hold, and "
            "in them the whole war is visible — the flinch of a man "
            "braced for one more turned back, and underneath it, "
            "refusing to die, the hope that this once the answer might "
            "be yes. The ashen patch at his brow is plain and does not "
            "matter. Exactly one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r054-b10", "out": "s10-he-did-not-step-back.jpeg", "seg": "n3 p1",
        "window": "41.98-45.08", "wide": True, "jesus": True, "ref": REF,
        "locks": ["LEPER", "ROADSIDE"],
        "narration": ("He did not step back from the man everyone else "
                      "stepped back from."),
        "must_show": "the geometry of compassion — the whole crowd at maximum distance, Jesus at minimum; one step closer, even.",
        "must_not_show": "Jesus's feet have visibly closed the gap — dust marks, his shadow falling over the kneeling man.",
        "scene": (
            "A wide frame that tells it in distances, the camera off "
            "to the side so every gap reads in profile: the scattered "
            "crowd holds the far edges of the picture, pressed against "
            "walls and trees, a ring of fear with a hole in it — and "
            "in the hole, Jesus has stepped IN toward the kneeling "
            "leper, close enough that his shadow falls across the "
            "man's ragged shoulders, the only human being inside ten "
            "paces of him and standing there like it is the most "
            "natural ground in Galilee. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r054-b11", "out": "s11-he-reached-out.jpeg", "seg": "n3 p2",
        "window": "45.08-49.32", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER", "ROADSIDE"],
        "narration": ("He reached out his hand toward the very thing no "
                      "one would touch."),
        "must_show": "the hand mid-reach — extended toward the kneeling man, not landed yet; the crowd's horror at its edges.",
        "must_not_show": "the touch has NOT happened yet in this frame; the reach itself is the beat.",
        "scene": (
            "Jesus's arm is extended full length, his open hand "
            "reaching toward the kneeling man's marked shoulder and "
            "almost there — the leper's eyes have gone wide watching "
            "the hand come, his whole ragged body frozen, unable to "
            "believe its path — while at the frame's edges the nearest "
            "onlookers press hands to mouths, one man half-turned "
            "away, watching a rule older than any of them about to "
            "break. Bright mid-morning sun on the reaching arm. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r054-b12", "out": "s12-and-touched-him.jpeg", "seg": "s41a",
        "window": "49.32-56.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER"],
        "narration": ("And Jesus, moved with compassion, put forth his "
                      "hand, and touched him, and saith unto him, "
                      "(Mark 1:41)"),
        "must_show": "THE TOUCH — his hand landed full and firm on the leper's marked shoulder/neck, skin on ruined skin, BEFORE any healing; the man's face breaking at being touched.",
        "must_not_show": "no glow, no effect, no healing yet — the skin under the hand is still ashen; the touch is the miracle of this frame.",
        "scene": (
            "The hand has landed: Jesus's palm rests full and firm on "
            "the side of the kneeling man's neck and shoulder, fingers "
            "curled around it, skin against ashen scaled skin with "
            "nothing held back — and the man has broken, his eyes "
            "squeezed shut and his mouth twisted with a sob, leaning "
            "his marked cheek a half-inch toward the first human hand "
            "in years while it is still touching a leper. Jesus's face "
            "above is moved and unafraid. Exactly two people are in "
            "the frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r054-b13", "out": "s13-i-will.jpeg", "seg": "jv41",
        "window": "56.02-59.76", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "I will; be thou clean. (Mark 1:41)",
        "must_show": "close on Jesus's face saying it — the answer to the man's only question; warmth, will, zero hesitation.",
        "must_not_show": "no halo, no glow, no rim-light; the will is in the face alone.",
        "scene": (
            "Close on Jesus's face in the full morning light as he "
            "answers: his warm eyes are steady on the man below him, "
            "his brow gentle, and the words sit visibly on his lips "
            "with the plain gladness of a man granting the thing he "
            "wanted to grant all along — the will, answered out loud, "
            "with his hand still gripping the leper's shoulder at the "
            "bottom of the frame. Exactly one face fills the frame, "
            "with one head."
        ),
    },
    {
        "id": "v2-r054-b14", "out": "s14-touched-before-healed.jpeg", "seg": "n4 p1-p3",
        "window": "59.76-64.06", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER"],
        "narration": ("I will. Two words, and the wondering was over. And "
                      "he touched him."),
        "must_show": "the order of mercy held — the hand still on still-marked skin, the man's eyes open now, meeting Jesus's; the healing has not yet come and the touch already has.",
        "must_not_show": "skin still ashen in this frame — the touch precedes the cleansing by one whole beat.",
        "scene": (
            "The two faces close together over the joined "
            "hand-and-shoulder: the man's eyes have opened and lifted, "
            "wet and astonished, to Jesus's — and Jesus holds his gaze "
            "and his shoulder both, the grip unhurried, the ashen "
            "patches still plain under his fingers — one long heartbeat "
            "in which the man is still a leper and already no longer "
            "untouchable. Exactly two people are in the frame; each "
            "has one head."
        ),
    },
    {
        "id": "v2-r054-b15", "out": "s15-the-leprosy-departed.jpeg", "seg": "n4 p4",
        "window": "64.06-73.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER", "ROADSIDE"],
        "narration": ("Before the healing had even come, the untouchable "
                      "man was touched; and then, at once, the leprosy "
                      "left him, and his skin was made new."),
        "must_show": "v42 — the cleansing visible: his bared forearms CLEAR, warm and whole, and him staring at them; Jesus's hand just lifting away.",
        "must_not_show": "no light-beam, no shimmer, no effect — clean skin where marked skin was, and a man's face trying to catch up.",
        "scene": (
            "The man has thrust both his own forearms out in front of "
            "himself, the ragged sleeves fallen back — and the skin on "
            "them is new: warm, smooth, whole, the ashen scaling "
            "simply gone — and he stares at his own arms like they "
            "belong to a stranger, chest heaving, while Jesus's hand "
            "lifts gently from his shoulder and the nearest of the "
            "crowd lean in from the edges, fear forgetting itself into "
            "awe. Bright late-morning sun on healthy skin. Every "
            "figure has two arms, two hands of five fingers each and "
            "one head."
        ),
    },
    {
        "id": "v2-r054-b16", "out": "s16-like-a-child-skin.jpeg", "seg": "n5 p1-p2",
        "window": "73.29-79.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER"],
        "narration": ("The sores were gone. The pale, wasted skin was warm "
                      "and whole again, like the skin of a young child."),
        "must_show": "close proof — his hands turned over and over before his own face, backs then palms, whole; his face behind them undone.",
        "must_not_show": "the same hands from b04, transformed — the echo must be recognizable.",
        "scene": (
            "Close on the man's two hands held up before his own face, "
            "turning slowly over and back in the sunlight — knuckles, "
            "palms, wrists all warm smooth living skin, the rag "
            "wrappings hanging loose and pointless from his wrists — "
            "and past them, out of focus, his eyes flooding as he "
            "watches his own hands being shown to him. Exactly one "
            "person is in the frame; each hand has five fingers."
        ),
    },
    {
        "id": "v2-r054-b17", "out": "s17-a-man-who-could-go-home.jpeg", "seg": "n5 p3",
        "window": "79.95-86.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER", "ROADSIDE"],
        "narration": ("In a moment he was clean, and more than clean; he "
                      "was a man who could go home."),
        "must_show": "the standing-up — him risen to his full height for the first time in the build, unbowed, facing the town; the crowd seeing a man, not a leper.",
        "must_not_show": "the stoop from b01 is GONE — posture is the proof this frame carries.",
        "scene": (
            "The man stands at his full height in the road — taller "
            "than anyone near him, shoulders back, the stoop of years "
            "gone — his face turned past the crowd toward the distant "
            "flat roofs of the town, the word HOME arriving visibly "
            "behind his eyes, while Jesus watches him rise with quiet "
            "gladness and the crowd, no longer scattered, has begun "
            "to edge back in around them both. Late morning sun. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r054-b18", "out": "s18-strict-instructions.jpeg", "seg": "n6 p1",
        "window": "86.34-89.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER"],
        "narration": "Then Jesus sent him away with strict instructions.",
        "must_show": "v43 — the straight charge: Jesus close, both hands on the man's shoulders, face earnest, the joy tempered with urgency.",
        "must_not_show": "not stern anger — the seriousness of a friend giving directions that matter.",
        "scene": (
            "Jesus has taken the healed man by both shoulders at arm's "
            "length, holding his eyes, his face earnest and close — a "
            "man making very sure of being understood — while the "
            "healed man, still lit up from his own skin, steadies "
            "under the grip and listens with dawning attention. Noon "
            "light. Exactly two people are in the frame; each has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r054-b19", "out": "s19-shew-thyself.jpeg", "seg": "j44a",
        "window": "89.67-96.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER"],
        "narration": ("See thou say nothing to any man: but go thy way, "
                      "shew thyself to the priest, (Mark 1:44)"),
        "must_show": "the instruction itself — Jesus mid-word, one finger lifted in gentle emphasis; the man nodding.",
        "must_not_show": "no scolding posture; the finger is counsel, not warning.",
        "scene": (
            "Close on the two of them: Jesus speaks with one hand "
            "still on the man's shoulder and the other lifted between "
            "them, finger raised in gentle emphasis on the charge — "
            "and the healed man nods along, quick and fervent, a man "
            "agreeing to anything while barely hearing it over the "
            "roar of his own new life. Exactly two people are in the "
            "frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r054-b20", "out": "s20-the-way-to-the-priest.jpeg", "seg": "j44b",
        "window": "96.00-102.81", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LEPER", "ROADSIDE", "VILLAGE"],
        "narration": ("and offer for thy cleansing those things which "
                      "Moses commanded, for a testimony unto them. "
                      "(Mark 1:44)"),
        "must_show": "the sending — Jesus's arm extended pointing the man down the road toward the town; the man turned to go, caught between the pointing arm and the destination.",
        "must_not_show": "the direction geometry must read at a glance: the arm, the man's facing, and the town all agree.",
        "scene": (
            "SHOT FROM THE SIDE: Jesus stands at the left of the frame "
            "with his arm extended full length, pointing RIGHT, down "
            "the road toward the town's stone gate visible in the "
            "distance — and the healed man stands mid-turn in the "
            "middle of the frame, his body already faced RIGHT toward "
            "the town in the exact direction of the pointing arm, one "
            "last look back over his shoulder at Jesus. Arm, man and "
            "town line up along one line of the picture. Noon light. "
            "Exactly two people are in the frame; each has two arms, "
            "two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r054-b21", "out": "s21-given-back-his-life.jpeg", "seg": "n6b",
        "window": "102.81-115.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER", "VILLAGE"],
        "narration": ("Say nothing to anyone, he told him. Just go and "
                      "show yourself to the priest, and make the offering "
                      "Moses commanded — and be given back, quietly and "
                      "legally, the whole life that had been taken from "
                      "you."),
        "must_show": "the road home — the man striding toward the town gate with everything ahead of him; the gate stands open.",
        "must_not_show": "SHOT FROM BEHIND — his back to us, faced at the gate; nobody in the frame knows yet.",
        "scene": (
            "SHOT FROM BEHIND THE MAN on the afternoon road, his back "
            "and shoulders to the camera as he strides AWAY from us "
            "toward the town's open stone gate ahead of him — his "
            "ragged wraps flying loose around a body that walks like "
            "a free man, the rag bindings pulled from his wrists and "
            "clenched in one fist — and through the gate ahead, IN THE "
            "DIRECTION HE IS WALKING, the market lane and its "
            "unsuspecting everyday crowd. An upright vertical "
            "photograph, the ground at the bottom of the frame and "
            "the sky at the top, the horizon level — the picture is "
            "the right way up. Every figure has two arms, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r054-b22", "out": "s22-he-could-not-hold-it-in.jpeg", "seg": "n7",
        "window": "115.68-125.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEPER", "VILLAGE"],
        "narration": ("But the man could not hold it in. He went out and "
                      "told everyone, freely, everywhere; how could he "
                      "not? The mercy was far too great to keep to "
                      "himself."),
        "must_show": "v45 — the telling: him in the market lane, arms flung wide mid-story, sleeves pushed back showing clean arms; a crowd gathering around him.",
        "must_not_show": "pure joy, no defiance — he is not disobeying so much as overflowing.",
        "scene": (
            "In the town's market lane in the golden afternoon the man "
            "stands at the centre of a swelling ring of neighbours, "
            "both arms flung wide mid-sentence, sleeves shoved to the "
            "elbows to show clean whole skin to people who knew his "
            "marks for years — an old woman gripping his forearm to "
            "see for herself, a potter abandoning his wheel, children "
            "wriggling to the front — the story pouring out of him "
            "like water over a broken dam. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r054-b23", "out": "s23-no-more-openly.jpeg", "seg": "n8 p1a",
        "window": "125.19-130.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WILDS"],
        "narration": ("And so the news ran ahead of him, until he could "
                      "hardly walk into a town in the open,"),
        "must_show": "v45 — the cost of the telling: Jesus withdrawn to the empty desert places, outside the towns.",
        "must_not_show": "not sad exile — a chosen quiet; but the towns are now closed to open entry, and the frame says so.",
        "scene": (
            "In the last of the afternoon light Jesus walks alone "
            "through the empty broken country between towns, out in "
            "the rocks and thorn scrub where the leper used to live — "
            "the roofs of a town small and far off to one side, its "
            "road already dotted with people coming out — a man whose "
            "mercy has made the cities too loud for him to enter. "
            "Exactly one person is in the frame, with two arms, two "
            "legs and one head."
        ),
    },
    {
        "id": "v2-r054-b24", "out": "s24-from-every-quarter.jpeg", "seg": "n8 p1b",
        "window": "130.00-135.41", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WILDS"],
        "narration": ("and people came to him from every direction, out "
                      "of every corner of the land."),
        "must_show": "v45's last clause — the wide closing image: streams of people converging on the one figure in the open country from every direction at once.",
        "must_not_show": "no halo/glow; he is found by the lines of the land — every path in the frame bends toward him.",
        "scene": (
            "A very wide golden-hour frame of the open country, the "
            "camera high on the ridge behind the near stream of "
            "walkers: at its "
            "centre, small but unmistakable, Jesus stands waiting on a "
            "low rise — and from every corner of the picture the "
            "people come, thin streams of walkers converging along "
            "every path and wadi and hillside at once, families and "
            "stretcher-bearers and lone hurrying figures, all of their "
            "long evening shadows pointing the way they are going, "
            "toward him. An upright vertical photograph, the ground at "
            "the bottom of the frame and the sky at the top, the "
            "horizon level — the picture is the right way up. Every "
            "figure has two arms, two legs and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "ROADSIDE": "PLACE-REF/roadside.jpeg",  # build-38-persistent-widow v2-r038-b39
    "VILLAGE": "PLACE-REF/village.jpeg",  # build-38-persistent-widow v2-r038-b46
    "WILDS": "PLACE-REF/wilds.jpeg",  # build-54-the-leper s01-the-loneliest-life (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "LEPER": "CAST-REF-V2/leper.jpeg",
}
