#!/usr/bin/env python3
"""V2 beat map — row 52, build-52-demoniac-synagogue (Mark 1:21-28).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 24 pictures over 139.8 s narration = 5.8 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 1:21-28 KJV):
  v21  they went into Capernaum; straightway ON THE SABBATH he entered into
       the SYNAGOGUE and TAUGHT.
  v22  they were ASTONISHED at his doctrine: he taught them as one that had
       AUTHORITY, and NOT AS THE SCRIBES.
  v23  there was IN THEIR SYNAGOGUE a man with an unclean spirit; and he
       CRIED OUT — the man is a worshipper among them, not an intruder.
  v24  "Let us alone; what have we to do with thee, thou Jesus of Nazareth?
       art thou come to destroy us? I know thee who thou art, the Holy One
       of God." (s24)
  v25  "Hold thy peace, and come out of him." (jv25)
  v26  the unclean spirit TORE him and CRIED WITH A LOUD VOICE, and CAME OUT
       of him — one convulsion, then freedom.
  v27  they were ALL AMAZED, QUESTIONED AMONG THEMSELVES: "What thing is
       this? what new doctrine is this? for with authority commandeth he
       even the unclean spirits, and they do obey him." (s27)
  v28  immediately his FAME SPREAD ABROAD throughout ALL THE REGION ROUND
       ABOUT GALILEE.

CONTENT-CARE — FLAG A, THE ADVERSARY LAW (this story is the §3 table's
"synagogue demoniac" entry): **the adversary is NEVER given a face, body,
figure, shadow-creature, smoke, or any visible form in any frame.** No
horror-genre imagery. The affliction shows ONLY in the man's own condition —
posture, eyes, the cry — and the deliverance shows ONLY in his freedom. The
convulsion of v26 gets ONE restrained beat (b15): he buckles and is caught by
the men beside him; nothing visible leaves him. The freed man calm and whole
among the congregation is the picture the whole build aims at.

TIME-OF-DAY ARC: one sabbath morning, bright eastern light through the
synagogue's high windows throughout; the spreading news (b23-b24) runs into
the same day's full daylight.

CAST-REF NOTE: when the first still with the afflicted man's face is ACCEPTED
at QC, copy it to CAST-REF-V2/freedman-ref.jpeg and add
"char_refs": ["CAST-REF-V2/freedman-ref.jpeg"] to every later legible-face
beat (b06-b22) — his face carries the whole arc, so face-consistency matters
more here than anywhere. Text locks alone do not hold a face.
"""

LOCKS = {
    # His clothing never changes; only his CONDITION changes, and that is
    # stated per beat (bound -> crying out -> convulsed -> freed).
    "FREEDMAN": (
        "AFFLICTED MAN LOCK: the man is the same man in every shot — about "
        "forty to forty-five, gaunt and hollow-cheeked, sun-browned skin "
        "gone sallow, unkempt MID-LENGTH DARK BROWN-BLACK hair (dishevelled "
        "when afflicted, the SAME dark hair when freed — never grey, never "
        "white-streaked, never bald or thinning, never short-cropped or "
        "shaved), a full ragged DARK brown-black beard (never clean-shaven, "
        "never stubble-only, never grey), deep-set dark brown eyes. "
        "He wears a plain worn DARK GREY-BROWN wool tunic with "
        "a frayed hem and a simple rope belt — an ordinary poor "
        "worshipper's clothing, plainly darker than the sunlit stone, "
        "never cream, never white. His face is shown clearly. He is a "
        "human being in torment and then in freedom — never a monster, "
        "never made frightening to look at."
    ),
    "SYNAGOGUE": (
        "SYNAGOGUE LOCK: the synagogue at Capernaum on a sabbath morning — "
        "a rectangular hall of dark basalt block walls with plastered "
        "upper courses, two rows of plain stone columns, stepped stone "
        "benches along the walls, woven rush mats on the floor, a wooden "
        "chest for the scrolls at the far end, bright morning light "
        "falling in shafts from small high windows. The congregation are "
        "ordinary Galilean families and elders in SATURATED DEEP earth "
        "colours — dark chocolate brown, deep russet, burnt ochre, dark "
        "olive and dusty indigo wool, the elders' prayer shawls woven in "
        "the SAME dark saturated wools with dark indigo stripes — every "
        "garment plainly darker than the sunlit plaster; no one in the "
        "hall wears cream, off-white, ivory or any pale near-white cloth."
    ),
    "ELDERS": (
        "ELDERS LOCK: the three synagogue elders are the same three men in "
        "every shot — grey-bearded men of sixty in DARK CHARCOAL-BROWN and "
        "DEEP UMBER scholarly robes with dark-striped prayer shawls over "
        "their heads or shoulders, seated on the chief stone bench near "
        "the scroll chest; never cream, never white."
    ),
}

REF = True

# CAST-REF WIRING (C-FIX 2026-08-07, Machine A). The A-auto build shipped
# WITHOUT executing the CAST-REF NOTE above, so the afflicted man's face was
# held by text alone and flipped shot to shot (Cameron complaint: "The
# demoniac face kept changing. Beard to no beard to old man and his looks kept
# flipping."). RE-OPEN 2026-08-09: the first C-FIX still flipped — its own anchor
# note said "dark hair streaked grey", and that grey/age ambiguity kept birthing
# an OLD-MAN face (s08 wild grey mane + grey beard) alongside near-bald (s14) and
# C-FIX #3 (2026-08-11) — 3rd re-open. Cameron: "The demoniac face kept changing
# shaved, to not shaved. Beard to no beard to old man and his looks kept flipping.
# 0:50 the demoniac looks normal but Jesus doesnt. 1:02 no beard again. 1:23 no
# beard same with 1:29. Just redo every picture ... none match each other."
# ROOT CAUSE of the loop: freedman-ref-a (s18) and -c (s11) are WIDE SHOTS in which
# the man's face is ~30px — useless as a face lock. Only -b (s17) carried real face
# detail, so every gen got weak/averaged face signal and the beard/hair drifted.
# FIX: one razor-sharp TIGHT FACE CROP off s17 (freedman-face.jpeg) as the primary
# anchor + the s17 full frame; the two wide shots are DROPPED. Every drifting
# FREEDMAN frame is regenerated with rough_ref = its own composition so identity
# conforms to the crop WITHOUT changing the (good) blocking. ONE gaunt man ~40-45,
# MID-LENGTH DARK BROWN-BLACK wavy hair, FULL DARK beard — NEVER grey, bald,
# short-cropped or clean-shaven.
REFS = {
    "FREEDMAN": [
        "CAST-REF-V2/freedman-face.jpeg",
        "CAST-REF-V2/freedman-ref-b.jpeg",
    ],
}
# Composition-preserving edit sources for the C-FIX #3 regen batch (identity comes
# from the FREEDMAN crop above, blocking from these; see rough-src/).
ROUGH = {
    "v2-r052-b06": "rough-src/s06-the-nearness-stirred-it.jpeg",
    "v2-r052-b07": "rough-src/s07-he-rose-up.jpeg",
    "v2-r052-b08": "rough-src/s08-not-his-own-voice.jpeg",
    "v2-r052-b09": "rough-src/s09-let-us-alone.jpeg",
    "v2-r052-b10": "rough-src/s10-i-know-thee.jpeg",
    "v2-r052-b11": "rough-src/s11-the-room-frozen.jpeg",
    "v2-r052-b12": "rough-src/s12-the-darkness-said-it-first.jpeg",
    "v2-r052-b15": "rough-src/s15-it-tore-him-and-left.jpeg",
    "v2-r052-b16": "rough-src/s16-it-had-to-go.jpeg",
}

BEATS = [
    {
        "id": "v2-r052-b01", "out": "s01-sabbath-synagogue.jpeg", "seg": "n1 p1",
        "window": "0.28-5.84", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "ELDERS"],
        "narration": ("On the sabbath day, Jesus went into the synagogue at "
                      "Capernaum and stood up to teach."),
        "must_show": "v21 — Jesus rising to teach in the crowded sabbath hall; the room still settling, unaware of what is coming.",
        "must_not_show": "no halo/glow; he stands as a guest teacher among them, not enthroned.",
        "scene": (
            "In the bright shafted morning light of the crowded "
            "stone hall, the camera at the side aisle taking the "
            "room from the side, "
            "Jesus has risen to his feet near the scroll chest to teach, "
            "calm and plain among them, while the sabbath congregation "
            "settles along the stepped stone benches and the rush mats — "
            "families shoulder to shoulder, the three grey elders in their "
            "place, faces just beginning to turn toward the visitor. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b02", "out": "s02-as-they-always-did.jpeg", "seg": "n1 p2",
        "window": "5.84-12.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE", "ELDERS"],
        "narration": ("The people had gathered as they always did, to hear "
                      "the scriptures taught and explained by the teachers "
                      "they knew."),
        "must_show": "the ordinary sabbath — the settled congregation, an elder with an open scroll, routine and familiar.",
        "must_not_show": "Jesus is NOT the focus of this frame; this is the ordinariness he is about to interrupt.",
        "scene": (
            "A wide view down the pillared hall: the congregation sits in "
            "its long-accustomed places in the morning light, children "
            "leaning on parents, old men with eyes closed in familiar "
            "half-listening, while at the far end one grey elder reads "
            "from an open scroll in the unhurried voice of a thousand "
            "identical sabbaths. Everything about the room says nothing "
            "new ever happens here. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r052-b03", "out": "s03-taught-with-authority.jpeg", "seg": "n2 p1-p2",
        "window": "12.80-20.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "ELDERS"],
        "narration": ("But this was different. He taught them as one who had "
                      "authority of his own, not leaning on teacher after "
                      "teacher the way the scribes did."),
        "must_show": "v22 — Jesus mid-teaching, direct and sure; the difference visible in how the room leans toward him.",
        "must_not_show": "no scroll in his hands — he speaks from himself; the elders' faces uncertain, not hostile.",
        "scene": (
            "Jesus teaches standing, his hands open and moving with the "
            "words, speaking straight into the faces before him with "
            "nothing to read from — and the whole hall has come forward "
            "off the wall benches, listeners leaning in on their knees, "
            "while the three elders by the scroll chest watch this "
            "empty-handed authority with a wary stillness they cannot "
            "name. Morning shafts of light between the columns. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b04", "out": "s04-the-room-astonished.jpeg", "seg": "n2 p3",
        "window": "20.34-26.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE"],
        "narration": ("His words carried a quiet weight, and the whole room "
                      "felt it, and was astonished."),
        "must_show": "the astonishment on the listeners' faces — a reaction frame, the teaching landing.",
        "must_not_show": "no fear yet — wonder; the trouble has not begun.",
        "scene": (
            "A close row of listening faces along the stone bench in the "
            "window light: a young mother with her child gone still in "
            "her lap, a broad farmer with his mouth slightly open, an old "
            "man with tears standing in his eyes and not falling — each "
            "face caught in the same astonishment, the look of people "
            "hearing the scriptures sound alive for the first time. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b05", "out": "s05-a-man-in-the-congregation.jpeg", "seg": "n3 p1",
        "window": "26.35-30.16", "wide": True, "jesus": False, "ref": False,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("There in the congregation was a man held by an "
                      "unclean spirit."),
        "must_show": "v23 — the man IN the congregation, one of them, but alone in the middle of everyone; the wrongness only in him.",
        "must_not_show": "FLAG A: no shadow, no dark shape, no visual of the spirit — only a hunched man; nobody looks at him yet.",
        "scene": (
            "Among the seated congregation, the camera low behind "
            "the back rows' shoulders, half in the shadow between "
            "two light shafts, the gaunt man sits hunched over his own "
            "knees, his ragged grey-brown tunic pulled tight around him, "
            "arms wrapped across his chest, staring at the floor — an "
            "ordinary worshipper in his ordinary place, except that a "
            "hand's width of empty bench has opened on either side of "
            "him, the way it always quietly does. Nobody is looking at "
            "him. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b06", "out": "s06-the-nearness-stirred-it.jpeg", "seg": "n3 p2",
        "window": "30.16-35.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN"],
        "narration": ("Something dark had bound him for a long time, and the "
                      "nearness of Jesus stirred it."),
        "must_show": "the stirring — close on the man's fight to hold still: whitened knuckles, sweat, jaw clenched.",
        "must_not_show": "FLAG A: nothing visible acts on him; the struggle is entirely inside a human face and hands.",
        "scene": (
            "Close on the hunched man: his knuckles have gone white where "
            "his fingers dig into his own forearms, sweat stands on his "
            "sallow temple, his jaw is clamped and trembling with the "
            "effort of holding something down, and his deep-set eyes, "
            "fixed on the floor, are wide with a fight no one around him "
            "can see. The teaching voice carries on softly beyond him. "
            "Exactly one person is in the frame, with two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r052-b07", "out": "s07-he-rose-up.jpeg", "seg": "n3 p3",
        "window": "35.51-40.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": "Unable to stay silent any longer, he suddenly cried out.",
        "must_show": "the eruption beginning — the man surging to his feet mid-congregation, the first heads snapping around.",
        "must_not_show": "restrained: he rises rigid, fists clenched — no flailing, no contortion.",
        "scene": (
            "The gaunt man has surged rigidly to his feet in the middle "
            "of the seated congregation, fists clenched at his sides, "
            "spine arched taut, head thrown back with his mouth coming "
            "open — and around him the sabbath calm tears: the nearest "
            "families flinch away along the benches, a child is pulled "
            "close, every head in the frame snapping toward the standing "
            "man. Morning light shafts down on him. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b08", "out": "s08-not-his-own-voice.jpeg", "seg": "n4 p1",
        "window": "40.44-44.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN"],
        "narration": "And the voice that broke out of him was not his own.",
        "must_show": "the cry — tight on his anguished face mid-shout; a man being spoken THROUGH, and hating it.",
        "must_not_show": "FLAG A: human face only — no distortion beyond anguish, no effects, nothing inhuman visible.",
        "scene": (
            "A tight shot of the man's upturned face mid-cry: the cords "
            "of his neck stand out, his mouth is torn wide with a shout, "
            "and his eyes are the terrible part — present, human, "
            "terrified, watching the words leave his own mouth like a "
            "passenger, wet with the misery of a man who has not chosen "
            "a word of it. Exactly one person is in the frame, with one "
            "head."
        ),
    },
    {
        "id": "v2-r052-b09", "out": "s09-let-us-alone.jpeg", "seg": "s24 p1",
        "window": "44.09-48.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("Let us alone; what have we to do with thee, thou "
                      "Jesus of Nazareth? (Mark 1:24)"),
        "must_show": "the confrontation opens — the crying man and, across the hall, Jesus turned calmly to face him; the room between them emptying.",
        "must_not_show": "Jesus unmoved, unhurried — no defensive posture, no raised hands.",
        "scene": (
            "Down the length of the pillared hall, the camera at the "
            "side wall holding the whole axis in profile, the two of them now "
            "face each other: the rigid man mid-cry with the congregation "
            "shrinking back off the benches around him, and Jesus standing "
            "quite still in the morning light at the teaching place, "
            "turned fully toward him, his face calm and level as if the "
            "shout were a question politely asked. The floor between them "
            "has emptied. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r052-b10", "out": "s10-i-know-thee.jpeg", "seg": "s24 p2-p3",
        "window": "48.28-56.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("art thou come to destroy us? I know thee who thou "
                      "art, the Holy One of God. (Mark 1:24)"),
        "must_show": "the naming — the man's arm thrust out pointing at Jesus as the title is forced out of him.",
        "must_not_show": "the pointing arm is rigid and human; Jesus receives the true title with absolute stillness.",
        "scene": (
            "The gaunt man's whole arm is thrust out straight, one "
            "shaking finger pointing across the emptied floor at Jesus, "
            "his face a knot of terror and compulsion as the words tear "
            "out of him — and Jesus stands in the shaft of window light "
            "receiving the truest sentence spoken in that synagogue all "
            "year, his eyes steady on the man, entirely without fear. "
            "The elders grip their bench. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r052-b11", "out": "s11-the-room-frozen.jpeg", "seg": "n4b p1-p2",
        "window": "56.11-61.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN", "SYNAGOGUE", "ELDERS"],
        "narration": ("Leave us alone. And then, almost trembling: Sit with "
                      "that for a second."),
        "must_show": "the frozen room — the congregation pressed back, elders half-risen, the lone man standing in the cleared space.",
        "must_not_show": "fear on every face EXCEPT the direction Jesus stands in — their eyes flick between man and teacher.",
        "scene": (
            "The whole hall holds its breath: worshippers pressed back "
            "against the basalt walls and one another, a mother's hand "
            "over her child's eyes, the three elders half-risen from the "
            "chief bench with their prayer shawls slid to their "
            "shoulders — and in the cleared centre of the rush-matted "
            "floor the gaunt man stands rigid and alone in the light "
            "shaft, trembling, every eye in the room going between him "
            "and the unseen teacher beyond the frame's edge. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b12", "out": "s12-the-darkness-said-it-first.jpeg", "seg": "n4b p3",
        "window": "61.65-69.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("In a room full of religious people, the first one to "
                      "say out loud exactly who he was, was the darkness."),
        "must_show": "the irony framed — the trembling man who just told the truth, the religious room that never had, and Jesus between them.",
        "must_not_show": "no mockery of the congregation — they are not villains, just silent.",
        "scene": (
            "A wide, still composition: Jesus stands at one side in the "
            "window light, calm; the trembling gaunt man stands opposite "
            "across the cleared floor, spent from the cry, held up by "
            "rigidity alone; and packed along the benches between and "
            "behind them the whole religious assembly — elders, scribes, "
            "devout families — watches in a silence that has just been "
            "shown up. Nobody in the room but the tormented man has said "
            "who the visitor is. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r052-b13", "out": "s13-hold-thy-peace.jpeg", "seg": "jv25",
        "window": "69.73-73.25", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "Hold thy peace, and come out of him. (Mark 1:25)",
        "must_show": "v25 — close on Jesus speaking the command: quiet, final, no effort in it.",
        "must_not_show": "no raised voice in his face, no anger, no dramatic gesture — the authority IS the quietness.",
        "scene": (
            "Close on Jesus's face in the shaft of morning light as he "
            "gives the command: his voice is plainly quiet — the jaw "
            "barely moves, the brow is smooth, the warm eyes are steady "
            "and utterly certain — a man telling something to leave with "
            "less effort than a shepherd calls a dog. One hand is lifted "
            "only slightly at his side, palm down, stilling the room. "
            "Exactly one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r052-b14", "out": "s14-no-battle.jpeg", "seg": "n5 p1-p3",
        "window": "73.25-80.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("Be quiet, and come out of him. Just a few short "
                      "words. There was no long battle, no struggle of "
                      "equals."),
        "must_show": "the mismatch — Jesus at rest, the word already spoken; the man gone rigid in the cleared space; no contest anywhere.",
        "must_not_show": "FLAG A: nothing visible fights back; the frame is still — stillness against rigidity.",
        "scene": (
            "Across the cleared floor Jesus stands entirely at rest, his "
            "hand already lowered, the command finished — and the gaunt "
            "man has gone rigid as a post in the light shaft, head bowed, "
            "fists locked, the last grip of the thing visible only as "
            "tension in a human body. The congregation watches from the "
            "walls without breathing. There is no contest in the frame; "
            "one side of it has already won. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b15", "out": "s15-it-tore-him-and-left.jpeg", "seg": "n5 p4",
        "window": "80.36-87.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("At his word the spirit shook the man one last time, "
                      "cried out with a loud voice, and came out of him."),
        "must_show": "v26, ONE restrained beat — the man buckling mid-cry, caught under the arms by two men beside him.",
        "must_not_show": "FLAG A: NOTHING visible leaves him — no smoke, no shadow, no shape, no effect; the convulsion is human and brief, never horror.",
        "scene": (
            "The man buckles — knees giving, back bowing forward, one "
            "final cry leaving him with his face screwed shut — and two "
            "broad-shouldered worshippers in dark russet and olive wool "
            "have lunged from the bench and caught him under the arms "
            "before he reaches the floor, holding the shaking man up "
            "between them. The air above and around him is plain sunlit "
            "dust and nothing else; whatever left him cannot be seen. "
            "Exactly three people are in the frame; each has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b16", "out": "s16-it-had-to-go.jpeg", "seg": "n5 p5",
        "window": "87.48-92.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN"],
        "narration": ("The thing that had held him for so long simply had "
                      "to go."),
        "must_show": "the immediate after — the man slack and quiet in the helpers' grip, the storm audibly over.",
        "must_not_show": "not unconscious, not lifeless — emptied and breathing, eyes just reopening.",
        "scene": (
            "Held gently under the arms by the two worshippers, the gaunt "
            "man hangs slack and utterly quiet, chest rising and falling "
            "in deep slow breaths, sweat-soaked hair against his brow — "
            "and his eyes are just coming open, unfocused and washed, "
            "like a man surfacing from deep water into morning light. "
            "The helpers' faces above him are wide with cautious wonder. "
            "Exactly three people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r052-b17", "out": "s17-and-he-was-free.jpeg", "seg": "n6 p1",
        "window": "92.25-93.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN"],
        "narration": "And the man was free.",
        "must_show": "close on the freed face — the same face from b06, with the fight gone out of it.",
        "must_not_show": "no tears of drama; peace, the first in years.",
        "scene": (
            "Close on the man's face in the full window light, and it is "
            "transformed by subtraction: the clamped jaw loose, the "
            "hunted deep-set eyes clear and quiet and his own, the sallow "
            "skin already less grey — the same gaunt face as before with "
            "the torment simply gone from it, the way a room changes when "
            "a noise that ran for years finally stops. Exactly one person "
            "is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r052-b18", "out": "s18-himself-again.jpeg", "seg": "n6 p2a",
        "window": "93.40-98.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("The torment had drained from his face, and he stood "
                      "there quiet and whole,"),
        "must_show": "the freed man ON HIS OWN FEET — standing straight and unaided in the light where he buckled.",
        "must_not_show": "the helpers have stepped back; he needs no holding now.",
        "scene": (
            "In the same shaft of morning light where he fell, the man "
            "now stands upright on his own feet, unaided, his shoulders "
            "down and level for the first time, hands open and loose at "
            "his sides — the two helpers have stepped back a pace and "
            "stand looking at him, and the nearest congregation members "
            "are rising slowly from the benches, staring at a neighbour "
            "they have never once seen stand like this. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b19", "out": "s19-like-waking-from-a-dream.jpeg", "seg": "n6 p2b",
        "window": "98.50-103.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["FREEDMAN", "SYNAGOGUE"],
        "narration": ("himself again, like someone waking gently from a "
                      "long and terrible dream."),
        "must_show": "the return to the human circle — a neighbour's hand arriving on his shoulder; the empty bench-space around him closing.",
        "must_not_show": "no crowd-crush; the touch is tentative, the first in a long time.",
        "scene": (
            "An older worshipper in deep russet wool has crossed the "
            "space no one used to cross and set a weathered hand on the "
            "freed man's shoulder — and the man has turned his cleared "
            "eyes to him with the faint unpractised beginning of a smile, "
            "while behind them others come near, the empty circle that "
            "always surrounded him quietly closing for good. Morning "
            "light. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b20", "out": "s20-they-turned-to-each-other.jpeg", "seg": "n7 p1",
        "window": "103.84-107.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE", "ELDERS"],
        "narration": ("The people were amazed, and they turned to one "
                      "another asking:"),
        "must_show": "v27 — the hall erupting into questions: heads together, hands moving, amazement everywhere.",
        "must_not_show": "not fear now — astonishment; the sabbath order is gone and nobody minds.",
        "scene": (
            "The stone hall has come alive: worshippers turned to one "
            "another all along the benches, hands mid-gesture, questions "
            "flying — a farmer gripping his neighbour's arm, two women "
            "with their heads together, an old man shaking his in slow "
            "wonder — the ordinary sabbath hush replaced everywhere by "
            "the loud amazement of people who have just watched the "
            "impossible. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r052-b21", "out": "s21-what-thing-is-this.jpeg", "seg": "s27",
        "window": "107.69-118.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SYNAGOGUE", "ELDERS"],
        "narration": ("What thing is this? what new doctrine is this? for "
                      "with authority commandeth he even the unclean "
                      "spirits, and they do obey him. (Mark 1:27)"),
        "must_show": "the question with its object — the debating congregation and elders, and beyond them Jesus, calm, the still centre of the storm.",
        "must_not_show": "no halo/glow; their gestures and glances converge on him.",
        "scene": (
            "In the foreground the elders and the men around them argue "
            "it out with open hands — one pointing back at the scroll "
            "chest, one at the freed man, voices visibly raised — and "
            "every few words their eyes and gestures return to the same "
            "point: Jesus, standing calm and unhurried in the light "
            "between the columns beyond them, the still centre every "
            "line of the frame leads to. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r052-b22", "out": "s22-an-ordinary-sabbath.jpeg", "seg": "n7b",
        "window": "118.33-127.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FREEDMAN", "SYNAGOGUE", "ELDERS"],
        "narration": ("What is this? A new teaching, and it comes with "
                      "authority behind it. They had come to synagogue that "
                      "morning expecting an ordinary sabbath."),
        "must_show": "the CONTENT-CARE target picture — the freed man seated calm among the congregation near Jesus, the service resuming around a changed room.",
        "must_not_show": "nothing broken, nothing fled — the man BELONGS in the room now; that is the whole image.",
        "scene": (
            "The hall has begun to settle into something new: the freed "
            "man now SITS calm and upright on the stone bench in the "
            "middle of the congregation — neighbours pressed close on "
            "either side of him where the gap used to be — his clear "
            "eyes fixed forward on Jesus, who stands at the teaching "
            "place in the morning light, ready to go on; the elders "
            "watch from their bench, their old certainties visibly "
            "rearranging. An ordinary sabbath, permanently changed. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b23", "out": "s23-the-news-went-out.jpeg", "seg": "n8 p1",
        "window": "127.34-132.52", "wide": True, "jesus": False, "ref": False,
        "locks": ["SYNAGOGUE"],
        "narration": ("And right away the news of him went out everywhere, "
                      "through all the country round about Galilee."),
        "must_show": "v28 — the news leaving the building: worshippers spilling from the synagogue door into the street, already telling it.",
        "must_not_show": "midday now; the sabbath crowd disperses in every direction with the story.",
        "scene": (
            "Outside the synagogue's basalt doorway in full midday "
            "light, the camera across the street watching the "
            "spill from the side, "
            "the congregation spills down the steps into the Capernaum "
            "street in knots of animated talk — a young man already "
            "trotting away up the lane, a woman calling the story across "
            "to a neighbour in a doorway, two fishermen heading for the "
            "shore with their heads together — the news dispersing in "
            "every direction at once like water from a tipped jar. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r052-b24", "out": "s24-through-all-galilee.jpeg", "seg": "n8 p2",
        "window": "132.52-139.60", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": ("Wherever the story was carried, people heard that "
                      "one had come whose word even the darkness could not "
                      "resist."),
        "must_show": "the story travelling the region — a road between villages, the telling in motion, Galilee wide beyond.",
        "must_not_show": "no map graphics, no montage tricks — one real road doing the work.",
        "scene": (
            "On a pale road winding between terraced Galilean hills, "
            "the camera above the verge taking the walkers in "
            "profile, in "
            "the afternoon light, a traveller has stopped a family coming "
            "the other way and is telling it — arms wide in the middle of "
            "the story — while beyond them the road runs on past olive "
            "groves toward a further village on its hilltop, and further "
            "hills beyond that, all the country round about waiting to "
            "hear. An upright vertical photograph, the ground at the "
            "bottom of the frame and the sky at the top, the horizon "
            "level — the picture is the right way up. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]

# C-FIX #3: attach the composition-preserving edit source to each regen beat.
for _b in BEATS:
    if _b["id"] in ROUGH:
        _b["rough_ref"] = ROUGH[_b["id"]]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "SYNAGOGUE": "PLACE-REF/synagogue.jpeg",  # build-05-bent-woman v2-r005-b28
}
# === end PLACE-PLATES ===
