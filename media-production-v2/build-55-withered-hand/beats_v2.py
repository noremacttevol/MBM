#!/usr/bin/env python3
"""V2 beat map — row 55, build-55-withered-hand (Mark 3:1-6).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 23 pictures over 133.0 s narration = 5.8 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 3:1-6 KJV):
  v1   he entered AGAIN into the synagogue; a man there had a WITHERED HAND
       (Luke 6:6 adds it was his RIGHT hand — honored here: the working
       hand, so his trade and livelihood went with it).
  v2   they WATCHED HIM, whether he would heal on the sabbath day; THAT THEY
       MIGHT ACCUSE HIM — the watchers watch JESUS, not the man; the man is
       invisible to them except as bait.
  v3   "Stand forth" — he moves the overlooked man to the CENTRE of the room;
       no corner-healing.
  v4   "Is it lawful to do good on the sabbath days, or to do evil? to save
       life, or to kill?" — and they HELD THEIR PEACE.
  v5   he LOOKED ROUND ABOUT ON THEM WITH ANGER, being GRIEVED for the
       HARDNESS OF THEIR HEARTS — anger and grief together in one face; the
       only recorded anger of Jesus at persons, and it is grief-shaped.
       "Stretch forth thine hand." He stretched it out: RESTORED WHOLE AS
       THE OTHER.
  v6   the Pharisees went forth and STRAIGHTWAY took counsel WITH THE
       HERODIANS against him, HOW THEY MIGHT DESTROY HIM.

CONTENT-CARE: row 55 is not in the §3 flag table = GREEN. The withered hand
is rendered restrained: shrunken, stiff, drawn-in — pitiable, never grotesque.

TIME-OF-DAY ARC: one sabbath morning in the synagogue, bright high side-light
from the windows throughout; the walkout and plot fall in the same late
morning outside.

CAST-REF NOTE: when the first still with the man's face is ACCEPTED at QC,
copy it to CAST-REF-V2/hand-man-ref.jpeg and add
"char_refs": ["CAST-REF-V2/hand-man-ref.jpeg"] to every later legible-face
beat. Same for the three watchers (watchers-ref.jpeg). Text locks alone do
not hold a face.
"""

LOCKS = {
    # The hand is healed at v5, so the lock fixes face, build and clothing
    # only; each beat states the hand's condition.
    "MAN": (
        "HAND-MAN LOCK: the man is the same man in every shot — about "
        "fifty, a stonemason's build gone soft from years without work, "
        "grizzled short grey-brown hair and a close grey-streaked beard, "
        "a patient worn face used to being overlooked. His RIGHT hand is "
        "the afflicted one. He wears a plain DARK WALNUT-BROWN wool tunic "
        "with a DARK OLIVE mantle he keeps folded over his right side, "
        "and a plain leather belt; never cream, never white. His face is "
        "shown clearly."
    ),
    "WATCHERS": (
        "WATCHERS LOCK: the religious watchers are the same three men in "
        "every shot — older scribes with long grey-streaked beards, in "
        "DARK CHARCOAL-BROWN and DEEP UMBER scholarly robes. Their prayer "
        "shawls are woven from the SAME SATURATED DARK wool as their "
        "robes — deep charcoal, dark umber and near-black, with dark "
        "indigo stripes and dark fringe — so that every shawl is plainly "
        "DARKER than the sunlit stone wall behind them. They sit together "
        "on the chief bench, faces closed and watchful."
    ),
    "SYNAGOGUE": (
        "SYNAGOGUE LOCK: a Galilean synagogue on a sabbath morning — a "
        "rectangular hall of pale limestone block with two rows of plain "
        "stone columns, stepped stone benches along the walls, woven rush "
        "mats on an open central floor, the wooden scroll chest at the "
        "far end, bright morning light in shafts from small high windows. "
        "The congregation are ordinary Galilean families in SATURATED "
        "DEEP earth colours — dark chocolate brown, deep russet, burnt "
        "ochre, dark olive and dusty indigo wool — every garment plainly "
        "darker than the sunlit stone; no one in the hall wears cream, "
        "off-white, ivory or any pale near-white cloth."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r055-b01", "out": "s01-another-sabbath.jpeg", "seg": "n1 p1a",
        "window": "0.28-6.00", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MAN", "SYNAGOGUE", "WATCHERS"],
        "narration": ("On another sabbath Jesus went into the synagogue to "
                      "teach, and there in the crowd was a man"),
        "must_show": "the sabbath room assembled, Jesus teaching; the man with the folded-over right side seated unnoticed among the rest.",
        "must_not_show": "no halo/glow; the man is NOT visually singled out yet — he is one face among many.",
        "scene": (
            "The camera at the side aisle takes the room from the side: "
            "the sabbath congregation fills the pillared limestone hall "
            "in bright shafted morning light, Jesus standing at the "
            "teaching place mid-word — and somewhere in the middle "
            "benches, given no more of the frame than anyone else, sits "
            "the grey-bearded man in walnut-brown with his dark olive "
            "mantle folded over his right side, listening like all the "
            "rest. The three watchers hold the chief bench. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b02", "out": "s02-the-withered-hand.jpeg", "seg": "n1 p1b",
        "window": "6.00-11.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": ("whose hand was withered, shrunken and useless, a "
                      "hand that could not work or grip or hold."),
        "must_show": "the hand itself — close: the right hand shrunken and drawn in against his chest under the mantle's edge.",
        "must_not_show": "restrained rendering: stiff, thin, curled — pitiable, never grotesque; his good left hand nearby for contrast.",
        "scene": (
            "A close shot at the man's lap and chest: his right hand "
            "lies curled and shrunken against his body under the edge "
            "of the dark olive mantle — the fingers thin, stiff, drawn "
            "half-closed, the forearm wasted — while his broad healthy "
            "left hand rests over it, half-covering, half-guarding, the "
            "old habit of years. The contrast between the two hands "
            "tells the whole sentence. Exactly one person is in the "
            "frame; each hand has five fingers."
        ),
    },
    {
        "id": "v2-r055-b03", "out": "s03-the-shame-of-years.jpeg", "seg": "n1 p2",
        "window": "11.11-15.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN", "SYNAGOGUE"],
        "narration": "He had carried it, and the shame of it, for years.",
        "must_show": "the shame — his face and posture: angled so the right side is toward the wall, the practised making-small of a man used to being looked past.",
        "must_not_show": "no one mocking him — the shame is internal and habitual, not inflicted in this frame.",
        "scene": (
            "The man sits at the end of a bench with his right shoulder "
            "turned in toward the stone wall, his mantle draped to hide "
            "the arm, his patient worn face angled down and away — the "
            "whole body-language of a big man who has spent years "
            "folding himself smaller, taking the seat by the wall, "
            "keeping the dead hand out of everyone's sight and mind, "
            "including his own. Morning light falls past him. Exactly "
            "one person is in the frame, with two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r055-b04", "out": "s04-they-watched-him.jpeg", "seg": "n2 p1",
        "window": "15.15-19.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["WATCHERS", "SYNAGOGUE"],
        "narration": ("But others in the room were watching — not the man, "
                      "but Jesus."),
        "must_show": "v2 — the watchers' fixed stare, aimed past everything at Jesus; the man does not exist to them.",
        "must_not_show": "their eyes do NOT rest on the afflicted man in any way — the aim of the stare is the point.",
        "scene": (
            "Close along the chief bench: the three grey-bearded "
            "watchers sit shoulder to shoulder in their dark scholarly "
            "robes, and all three pairs of eyes are locked hard on one "
            "unseen point across the room — narrowed, unblinking, the "
            "stare of men watching a trap they have already set — while "
            "the congregation between them and their target is nothing "
            "to them but foreground. Exactly three people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b05", "out": "s05-hoping-to-catch-him.jpeg", "seg": "n2 p2a",
        "window": "19.15-24.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["WATCHERS"],
        "narration": ("Some of the religious leaders felt sure he would "
                      "try to heal on the sabbath,"),
        "must_show": "the conspiracy at whisper range — two of the watchers' heads tilted together, the third keeping the stare.",
        "must_not_show": "no cartoon villainy — these are devout, certain men; that is the tragedy.",
        "scene": (
            "Two of the watchers have leaned their grey heads together, "
            "one murmuring behind a half-raised hand, his eyes never "
            "leaving their target across the room — while the third "
            "sits forward over his knees, fingers laced, keeping the "
            "watch with the patient certainty of a man who believes "
            "God shares his opinion. Morning light edges their dark "
            "shawls. Exactly three people are in the frame; each has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b06", "out": "s06-the-trap-waiting.jpeg", "seg": "n2 p2b",
        "window": "24.00-29.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MAN", "WATCHERS", "SYNAGOGUE"],
        "narration": ("and they waited, hoping to catch him breaking the "
                      "law, so they could accuse him."),
        "must_show": "the whole trap in one frame — the watchers' sightline to Jesus, the unnoticed man between, the room unaware.",
        "must_not_show": "three-way geometry must read: watchers stare at Jesus; nobody looks at the man; Jesus teaches on.",
        "scene": (
            "A wide frame of the hall that draws the trap, the camera "
            "at the side wall so the sightline crosses in profile: on one side "
            "the three watchers stare fixed at Jesus where he teaches "
            "in the light at the scroll chest; between the two, lost in "
            "the congregation's middle benches, the man in walnut-brown "
            "sits with his right side folded away, looked at by no one "
            "— bait that does not know it is bait. The morning shafts "
            "cut the room into light and shadow. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b07", "out": "s07-he-knew-their-hearts.jpeg", "seg": "n3 p1",
        "window": "29.04-31.39", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "Jesus knew exactly what was in their hearts.",
        "must_show": "close on Jesus — his teaching paused, his eyes moved level onto the watchers; he sees the whole trap.",
        "must_not_show": "no anger yet — that comes at v5; here it is clear-eyed knowing.",
        "scene": (
            "Close on Jesus's face in the window light: he has stopped "
            "mid-teaching, and his warm eyes have moved — level, "
            "unhurried, absolutely clear — onto the men at the chief "
            "bench, with the unstartled look of someone reading a page "
            "he has already read; he knows what they are waiting for, "
            "and he is going to do it in the middle of the room. "
            "Exactly one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r055-b08", "out": "s08-not-in-a-corner.jpeg", "seg": "n3 p2-p3",
        "window": "31.39-37.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SYNAGOGUE"],
        "narration": ("He did not hide the moment away in a corner. He "
                      "said to the man with the withered hand:"),
        "must_show": "the turn — Jesus turned fully toward the man's bench, hand opening in invitation; the man realizing he is the one being addressed.",
        "must_not_show": "the man's disbelief that ANYONE is speaking to him, let alone this teacher.",
        "scene": (
            "Jesus has turned his whole body from the watchers toward "
            "the middle benches, one open hand extended in invitation "
            "toward the man in walnut-brown — and the man has gone "
            "rigid, half-looking over his own shoulder in case someone "
            "behind him is meant, his good hand tightening on the "
            "mantle over his dead one, while the neighbours around him "
            "begin to turn. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r055-b09", "out": "s09-stand-forth.jpeg", "seg": "j3 + n3b p1",
        "window": "37.11-40.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN", "SYNAGOGUE"],
        "narration": "Stand forth. (Mark 3:3) / Stand up.",
        "must_show": "the man rising — pushed up off the bench by the command, unsteady, clutching the mantle over his arm.",
        "must_not_show": "his neighbours make room; nobody helps him — he rises alone, and that is right.",
        "scene": (
            "The man is on his feet in the middle of the benches, risen "
            "so fast the bench scraped, his dark olive mantle clutched "
            "over his right arm with his good hand, his patient face "
            "stripped open with alarm — a man summoned out of thirty "
            "years of invisibility by two words — while the neighbours "
            "on either side draw their knees back to give him a path "
            "to the open floor. Morning light. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b10", "out": "s10-to-the-centre.jpeg", "seg": "n3b p2-p3",
        "window": "40.86-50.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MAN", "WATCHERS", "SYNAGOGUE"],
        "narration": ("Come out here, into the middle, where everyone can "
                      "see you. The man everybody in that room had learned "
                      "to look past was moved to the center of the floor."),
        "must_show": "the reversal — the overlooked man standing alone at the exact centre of the open floor, every eye in the room ON him for the first time in his life; Jesus near.",
        "must_not_show": "he stands in the brightest shaft of light — the staging is deliberate and the frame must show it is Jesus's doing.",
        "scene": (
            "The camera looks over the congregation's shoulders from behind: "
            "the man in walnut-brown stands alone in the centre of the "
            "open rush-matted floor, squarely inside the brightest "
            "shaft of morning light, his mantle still clutched over "
            "his right arm — and the entire room is turned to him: the "
            "congregation on every bench, the three watchers rigid on "
            "theirs, and Jesus standing a few paces off, calm, having "
            "placed the man exactly where nobody would ever again "
            "look past him. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r055-b11", "out": "s11-is-it-lawful.jpeg", "seg": "jv4",
        "window": "50.24-57.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "WATCHERS", "SYNAGOGUE"],
        "narration": ("Is it lawful to do good on the sabbath days, or to "
                      "do evil? to save life, or to kill? (Mark 3:4)"),
        "must_show": "v4 — the question thrown at the watchers: Jesus's arm open toward the standing man, his face turned to the bench, demanding.",
        "must_not_show": "the question is aimed at THEM; the man is the exhibit — the geometry of arm, face and stare must carry it.",
        "scene": (
            "Jesus stands with one arm swept open toward the man in "
            "the shaft of light and his face turned hard toward the "
            "watchers on the chief bench, mid-question, his eyes "
            "pinning them to the wall — the man stands in the light "
            "with his head down under the weight of the room, and the "
            "three watchers sit like stones under a question that "
            "leaves them nowhere to stand. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b12", "out": "s12-no-real-love.jpeg", "seg": "n4 p1-p2",
        "window": "57.55-66.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["WATCHERS"],
        "narration": ("It was a simple question, and it left them no "
                      "answer. They had no real love for the law, or for "
                      "the man; they only wanted a reason to condemn him."),
        "must_show": "the exposure — close on the three faces refusing to answer: eyes dropped, jaws set, hands gone still.",
        "must_not_show": "no shame on their faces — that would be hope; only the hard blankness of men who will not be moved.",
        "scene": (
            "Close along the chief bench under the question: the first "
            "watcher stares at the floor between his own feet, the "
            "second has fixed his eyes on the far wall above every "
            "head, the third looks straight back with his jaw set and "
            "his mouth a flat line — three learned men with one "
            "answer between them and no intention of saying it. Their "
            "hands lie utterly still on their dark robes. Exactly "
            "three people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r055-b13", "out": "s13-they-said-nothing.jpeg", "seg": "n4 p3",
        "window": "66.35-69.09", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "WATCHERS", "SYNAGOGUE"],
        "narration": "So they said nothing at all.",
        "must_show": "the silence as a picture — the whole held-breath room: Jesus waiting, the man in the light, the bench mute.",
        "must_not_show": "nobody moves anywhere in the frame; the stillness IS the content.",
        "scene": (
            "A wide, motionless frame of the whole hall in the silence "
            "after the question: Jesus stands waiting with his arm "
            "still open toward the man, the man stands unmoving in "
            "his shaft of light, the watchers sit rigid on their "
            "bench, and along every wall the congregation holds its "
            "breath — dust drifting in the light shafts is the only "
            "thing in the room that dares to move. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b14", "out": "s14-anger-and-grief.jpeg", "seg": "s5a",
        "window": "69.09-77.51", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("And when he had looked round about on them with "
                      "anger, being grieved for the hardness of their "
                      "hearts, he saith unto the man, (Mark 3:5)"),
        "must_show": "v5 — THE face of this build: anger and grief in the same look, sweeping the bench; the only anger the Gospels give him at persons, and it is grief-shaped.",
        "must_not_show": "no rage, no curled lip — the anger is banked and sorrowing; if it reads as fury alone the frame fails.",
        "scene": (
            "Close on Jesus mid-turn, his gaze sweeping slowly along "
            "the unseen bench: his brows are drawn and his jaw is hard "
            "with real anger — and his eyes, inside the anger, are "
            "grieving, wet at the rims, the look of a man furious at a "
            "wall because of what it is doing to the people who built "
            "it. The two things live in the one face at once. Exactly "
            "one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r055-b15", "out": "s15-stretch-forth-thine-hand.jpeg", "seg": "jv5",
        "window": "77.51-80.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN"],
        "narration": "Stretch forth thine hand. (Mark 3:5)",
        "must_show": "the command — Jesus turned from the bench to the man, the words landing; the man's eyes going down to his own dead hand.",
        "must_not_show": "no touch in this story — the healing rides on the word and the man's own obedience.",
        "scene": (
            "Jesus has turned from the bench fully to the man, close "
            "now, his face cleared into pure steady warmth, giving the "
            "command — and the man's eyes drop from Jesus's face to "
            "his own curled right hand under the mantle, the impossible "
            "instruction settling on him: to do the one thing he has "
            "not been able to do for years. Exactly two people are in "
            "the frame; each has one head."
        ),
    },
    {
        "id": "v2-r055-b16", "out": "s16-hard-under-his-gaze.jpeg", "seg": "n4b p1",
        "window": "80.84-87.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["WATCHERS"],
        "narration": ("He looked around at every one of them, angry, and "
                      "grieved to the heart at how hard they had let "
                      "themselves become."),
        "must_show": "the bench under the gaze — the watchers enduring it: one looks away, one closes his eyes, one stares back unmoved.",
        "must_not_show": "three different failures to soften — variety in the refusal, not one repeated pose.",
        "scene": (
            "The three watchers under the weight of the look they will "
            "not meet: the eldest has turned his face away toward the "
            "shadowed wall; the second sits with his eyes shut and his "
            "knuckles white on his knee; the third stares straight "
            "back across the room, unblinking, hard as the bench "
            "beneath him — three men being given a last chance and "
            "declining it in three different ways. Exactly three "
            "people are in the frame; each has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r055-b17", "out": "s17-he-turned-to-the-man.jpeg", "seg": "n4b p2",
        "window": "87.12-91.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "WATCHERS", "SYNAGOGUE"],
        "narration": ("And then he turned away from them, to the man, and "
                      "said:"),
        "must_show": "the pivot — Jesus's back half-turned on the bench, his face and body given wholly to the man; the choice of person over quarrel, staged.",
        "must_not_show": "the watchers now behind his shoulder, out of his sight — the geometry is the sermon.",
        "scene": (
            "In the wide frame Jesus has turned his back half-toward "
            "the chief bench, the watchers now behind his shoulder and "
            "dismissed from his attention, and his whole face and "
            "frame are given to the man in the shaft of light — while "
            "the man has straightened to meet what is coming, his "
            "good hand slowly releasing its grip on the mantle over "
            "the dead one. The congregation leans in from every "
            "bench. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r055-b18", "out": "s18-the-reach.jpeg", "seg": "n5 p1a",
        "window": "91.00-96.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": ("And the man stretched out the hand he could not "
                      "use —"),
        "must_show": "the obedience mid-act — the withered right arm extending out from under the fallen mantle, still curled, reaching anyway.",
        "must_not_show": "the hand is NOT healed yet in this frame — the reach comes first; that order is the faith.",
        "scene": (
            "The dark olive mantle slides from the man's right "
            "shoulder as he stretches the withered arm out before him "
            "into the shaft of light — the thin wasted forearm "
            "extending, the stiff curled fingers still curled, "
            "reaching out in front of the whole watching room on "
            "nothing but a word — his face clenched with the effort "
            "and the enormity of it. Exactly one person is in the "
            "frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b19", "out": "s19-made-whole.jpeg", "seg": "n5 p1b",
        "window": "96.50-101.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": ("and as he reached, it was made whole, restored, "
                      "strong and alive again, exactly like his other "
                      "hand."),
        "must_show": "v5 — the restoration seen close: the right hand OPEN in the light, fingers spread full and strong; his face beyond it breaking open.",
        "must_not_show": "no glow, no effect — a working man's whole strong hand where the curled one was, and daylight.",
        "scene": (
            "Close down the length of the outstretched arm: the right "
            "hand stands OPEN in the shaft of morning light, fingers "
            "spread wide and full, the forearm filled and strong — a "
            "stonemason's hand again — and past it, out of focus, the "
            "man's face is coming apart with disbelief turning into "
            "joy as he watches his own fingers answer him for the "
            "first time in years. Exactly one person is in the frame; "
            "each hand has five fingers."
        ),
    },
    {
        "id": "v2-r055-b20", "out": "s20-back-to-life.jpeg", "seg": "n5 p2",
        "window": "101.59-106.39", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SYNAGOGUE"],
        "narration": ("The thing that had been dead came back to life at "
                      "a single word."),
        "must_show": "the proof held up — both hands raised together before his face, matching; the congregation rising off the benches around him.",
        "must_not_show": "the watchers are NOT in this frame — this beat belongs to the man and the room's joy.",
        "scene": (
            "The man holds both hands up side by side before his own "
            "face in the light, turning them together — two matched, "
            "strong, living hands — laughing and weeping at once, "
            "while around him the congregation surges up off the "
            "benches, a neighbour gripping his shoulder, a woman's "
            "hands flying to her mouth, and Jesus watches from a pace "
            "away with quiet gladness. Every figure has two arms, two "
            "hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r055-b21", "out": "s21-they-walked-out.jpeg", "seg": "n6 p1-p2",
        "window": "106.39-115.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["WATCHERS", "SYNAGOGUE"],
        "narration": ("But the leaders were not amazed; they were furious. "
                      "They walked out and began, that very day, to plot "
                      "together how they might destroy him."),
        "must_show": "v6 — the walkout: the three pushing out through the doorway against the joy, robes gathered, faces black.",
        "must_not_show": "the celebrating room behind them makes the frame's argument — they leave a miracle angry.",
        "scene": (
            "The three watchers push out through the synagogue doorway "
            "in a tight dark knot, robes gathered up in their fists, "
            "faces shut and black with fury — while behind them, "
            "framed in the doorway they are abandoning, the hall is "
            "all light and celebration around the man with his two "
            "raised hands. They are the only three people moving away "
            "from it. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r055-b22", "out": "s22-it-only-hardened-them.jpeg", "seg": "n6 p3",
        "window": "115.30-119.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["WATCHERS"],
        "narration": ("He had done nothing but good, and it only hardened "
                      "them."),
        "must_show": "the plot beginning — the three in the bright street, heads bent together, already at the work of destroying him.",
        "must_not_show": "broad daylight, ordinary street — evil planned at noon by respectable men.",
        "scene": (
            "In the bright late-morning street outside, the three "
            "watchers stand bent together against a limestone wall, "
            "grey heads almost touching, one making a low flat gesture "
            "with the edge of his hand while the others nod — three "
            "respectable scholars opening the work of destroying a man "
            "who has just made a dead hand live, in full sun, on the "
            "sabbath. Exactly three people are in the frame; each has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r055-b23", "out": "s23-mercy-over-rule.jpeg", "seg": "n7",
        "window": "119.61-132.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SYNAGOGUE"],
        "narration": ("Faced with a rule on one side and a suffering man "
                      "on the other, Jesus never wavered. He will always "
                      "move toward the person. Mercy, to him, was never a "
                      "breaking of the sabbath; it was the whole reason "
                      "for it."),
        "must_show": "the closing image — Jesus and the healed man face to face in the emptying hall, the restored right hand clasped in both of Jesus's hands.",
        "must_not_show": "warm, quiet, held — the noise has passed; two men and a healed hand in the sabbath light.",
        "scene": (
            "In the quieting hall, the morning light long across the "
            "rush mats, Jesus stands face to face with the healed man "
            "and holds the restored right hand clasped in both of his "
            "own — the stonemason's new-made fingers gripping back, "
            "strong — the man's worn face level with his for once, "
            "unbowed, streaked and shining, while the last of the "
            "congregation lingers in the doorway light behind them. "
            "The sabbath, being what it was always for. Exactly two "
            "people are in the frame in focus; each has two arms, two "
            "hands of five fingers each and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "SYNAGOGUE": "PLACE-REF/synagogue.jpeg",  # build-05-bent-woman v2-r005-b28
}
# === end PLACE-PLATES ===
