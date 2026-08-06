#!/usr/bin/env python3
"""V2 beat map — row 62, build-62-ephphatha (Mark 7:31-37).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 34 pictures over 194.3 s narration = 5.7 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 7:31-37 KJV):
  v31  departing from the coasts of Tyre and Sidon, he came THROUGH THE
       MIDST OF THE COASTS OF DECAPOLIS — the same region as row 60's
       healed Gerasene, whose one-man mission (Mark 5:20) explains the
       changed welcome: last visit they begged him to leave; this visit
       they bring him their broken.
  v32  they bring unto him one that was DEAF, and had an IMPEDIMENT IN HIS
       SPEECH; and they beseech him to PUT HIS HAND UPON HIM.
  v33  he TOOK HIM ASIDE FROM THE MULTITUDE — private, personal — and PUT
       HIS FINGERS INTO HIS EARS, and TOUCHED HIS TONGUE — sign language
       to a deaf man: each touch an explanation in the only language the
       man can receive (the narration reads it this way; the beats do too).
  v34  LOOKING UP TO HEAVEN, HE SIGHED, and saith "EPHPHATHA," that is,
       Be opened — THE SIGH comes before the word; the build's stunning
       detail (b17) — grief for a world this broken, felt before fixing.
  v35  STRAIGHTWAY his ears were OPENED, and the string of his tongue was
       LOOSED, and he SPAKE PLAIN.
  v36  he charged them to tell no man: but the more he charged them, so
       much the more a great deal THEY PUBLISHED IT.
  v37  "He hath done all things well: he maketh both the deaf to hear,
       and the dumb to speak."

CONTENT-CARE: row 62 is not in the §3 flag table = GREEN. Dignity framing
throughout: the deaf man's isolation is shown as exclusion and aloneness,
never as mockery played straight; his healing scenes honour his
intelligence — he is a grown man handed the world, not a spectacle.

TIME-OF-DAY ARC: bright day on the Decapolis road and shore for the
arrival and bringing; the aside and the healing in the softer light of an
olive-shaded spot off the road, same afternoon; the telling and the verdict
in golden late afternoon; the closing two-shot as the light goes long.

CAST-REF NOTE: when the first still with the deaf man's face is ACCEPTED at
QC, copy it to CAST-REF-V2/deafman-ref.jpeg and add
"char_refs": ["CAST-REF-V2/deafman-ref.jpeg"] to every later legible-face
beat — the whole build is his face learning to hear. Text locks alone do
not hold a face.
"""

LOCKS = {
    "DEAFMAN": (
        "DEAF MAN LOCK: the man is the same man in every shot — about "
        "thirty, a labourer's solid build, warm olive skin, short dark "
        "hair, a close-trimmed dark beard, and watchful, intelligent "
        "dark eyes that read the world the way other men listen — always "
        "moving, always a half-second behind the room. He wears a plain "
        "DARK RUST-BROWN wool tunic with a rope belt and dusty sandals; "
        "never cream, never white. His face is shown clearly. He is "
        "dignified in every frame — never a figure of fun, never "
        "helpless."
    ),
    "DECAPOLIS": (
        "DECAPOLIS LOCK: the Gentile lake country of the ten cities — "
        "dry hills above the eastern shore of the Sea of Galilee, a "
        "columned town on a rise, market lanes with Greek touches, "
        "the blue water below. Its people wear SATURATED DEEP earth "
        "colours with Gentile banded borders — dark chocolate brown, "
        "deep russet, burnt ochre, dark olive and dusty indigo wool — "
        "every garment plainly darker than the sunlit stone; no one "
        "wears cream, off-white, ivory or any pale near-white cloth."
    ),
    "ASIDE": (
        "ASIDE LOCK: the private place — a small olive-shaded hollow "
        "off the road behind a low stone wall, out of sight of the "
        "crowd: grey-green olive shade, a flat stone or two, the "
        "crowd's noise left visibly behind. Room for exactly two men "
        "and quiet."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r062-b01", "out": "s01-the-long-road-back.jpeg", "seg": "n0 p1-p2",
        "window": "0.28-8.79", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DECAPOLIS"],
        "narration": ("Jesus came back from the coast by a long road — "
                      "down through the Decapolis, the ten Gentile "
                      "cities. Remember that name."),
        "must_show": "v31 — the return route: Jesus on the high road into the ten-cities country, a columned Gentile town ahead, the lake below.",
        "must_not_show": "no crowd yet — the road is the subject; the welcome comes two beats later.",
        "scene": (
            "The camera off the road takes the walk in profile: "
            "Jesus walks the high dusty road down into the lake "
            "country of the ten cities, a few disciples strung "
            "behind him — ahead, a columned Gentile town stands on "
            "its rise in the bright day, and far below the Sea of "
            "Galilee lies blue and familiar: the same eastern shore "
            "he was once asked to leave. An upright vertical "
            "photograph, the ground at the bottom of the frame and "
            "the sky at the top, the horizon level — the picture is "
            "the right way up. Every figure has two arms, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r062-b02", "out": "s02-one-man-still-telling-it.jpeg", "seg": "n0 p3",
        "window": "8.79-14.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["DECAPOLIS"],
        "narration": ("It is the same region where the man from the tombs "
                      "had been telling his story to anyone who would "
                      "listen."),
        "must_show": "the seed already sown — a weathered man mid-story in a market lane, listeners leaning in; the testimony at work.",
        "must_not_show": "he is a teller among neighbours now, at home — the region's one-man mission in mid-sentence.",
        "scene": (
            "In a Gentile market lane a tall weathered man with "
            "long black hair and a full tangled beard stands "
            "telling a story with both arms wide — and the lane "
            "has stopped for it: a potter leaning over his wheel, "
            "two women with jars set down, a boy cross-legged in "
            "the dust at the teller's feet — a story the whole "
            "region has been hearing for months and still stops "
            "for. Bright day. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r062-b03", "out": "s03-now-they-come-running.jpeg", "seg": "n0 p4-p5",
        "window": "14.59-22.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DECAPOLIS"],
        "narration": ("Last time Jesus was on this side of the sea, the "
                      "people asked him to leave. Now they come running, "
                      "bringing him their broken."),
        "must_show": "the reversal — people streaming TOWARD Jesus on the road from every direction, carrying and leading their sick.",
        "must_not_show": "the bringing is the point: litters, led elders, carried children — a region's broken, in motion toward him.",
        "scene": (
            "Down every path to the road, the camera behind his "
            "shoulder so the streams converge into the frame, they "
            "come toward Jesus — "
            "two men jogging with a litter between them, a woman "
            "leading her blind father by the wrist, a boy carried "
            "high on a shoulder, whole family knots hurrying "
            "cross-country — all the lines of the frame converging "
            "on the one figure who stands still on the road to "
            "receive what the region is bringing him. Bright day. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b04", "out": "s04-one-testimony-changed-it.jpeg", "seg": "n0 p6",
        "window": "22.76-27.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DECAPOLIS"],
        "narration": ("One man's testimony had changed the whole "
                      "neighborhood."),
        "must_show": "the connection made visible — the weathered teller at the crowd's edge pointing Jesus out to newcomers; witness handing people on.",
        "must_not_show": "his gesture and the newcomers' turning faces draw the line from testimony to arrival.",
        "scene": (
            "At the swelling crowd's edge the tall weathered "
            "storyteller stands with one arm thrown out, pointing "
            "Jesus out to a knot of newcomers — that is him, the "
            "gesture says — and their faces turn along his arm one "
            "after another, wonder catching from man to man, while "
            "out at the centre of it all Jesus is already bending "
            "over the first of the brought. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b05", "out": "s05-they-brought-him-a-man.jpeg", "seg": "n1 p1",
        "window": "27.30-31.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "DECAPOLIS"],
        "narration": ("And they brought him a man who was deaf, and whose "
                      "speech was tangled because of it."),
        "must_show": "v32 — the bringing: two friends steering the deaf man forward through the crowd toward Jesus; his wary, reading eyes.",
        "must_not_show": "he comes willingly but blind to the why — his eyes hunt faces for the explanation nobody can give him.",
        "scene": (
            "Two friends bring the solid rust-brown-clad man "
            "forward through the parting crowd, each with a hand "
            "on one of his arms — and he comes willingly but "
            "watchfully, his intelligent dark eyes jumping from "
            "his friends' faces to the stranger ahead to the "
            "turning crowd, reading everything and hearing "
            "nothing, a man being led into a story no one can "
            "tell him. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r062-b06", "out": "s06-no-way-in.jpeg", "seg": "n1 p2-p3",
        "window": "31.75-39.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN", "DECAPOLIS"],
        "narration": ("Think about what deafness meant in that world. No "
                      "writing tablets for the poor, no signing schools, "
                      "no way in."),
        "must_show": "the memory of exclusion — the man in a market full of moving mouths, all of it sealed away from him.",
        "must_not_show": "nobody mocks him — the world simply talks past him; indifference is the wall.",
        "scene": (
            "A memory in bright market light: the man stands in "
            "the middle of a busy lane while commerce roars "
            "around him — a seller's mouth wide mid-cry beside "
            "his ear, two friends arguing prices across his "
            "shoulder, a woman laughing at something behind him — "
            "every mouth in the frame open and moving, and his "
            "still watchful face at the centre of it like a stone "
            "in a river, passed on every side. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b07", "out": "s07-outside-the-joke.jpeg", "seg": "n1 p4a",
        "window": "39.39-44.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN"],
        "narration": ("Every conversation, every joke, every warning, "
                      "every kind word —"),
        "must_show": "the evening fire — friends rocking with laughter at a story; him at the circle's edge, smiling a half-beat late at a joke he never heard.",
        "must_not_show": "the late smile is the heartbreak — he fakes belonging, and the frame catches him doing it.",
        "scene": (
            "Around a small evening fire a circle of workmates "
            "rocks with laughter at the end of somebody's story — "
            "heads thrown back, a knee slapped — and at the "
            "circle's edge the man in rust-brown watches their "
            "faces and assembles his own smile a half-beat too "
            "late, laughing at the shape of laughter, his eyes "
            "doing the work his ears cannot. Firelight on every "
            "face. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r062-b08", "out": "s08-the-warning-he-never-heard.jpeg", "seg": "n1 p4b",
        "window": "44.50-48.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN", "DECAPOLIS"],
        "narration": "all of it happened on the other side of a wall he could not cross.",
        "must_show": "the danger of the wall — a loaded cart bearing down; shouted warnings he cannot hear; a friend's arm yanking him back.",
        "must_not_show": "ACTION-LOGIC: the cart, the shouting mouths, the yank — every element aimed correctly; he is saved, not struck.",
        "scene": (
            "In the market lane a heavy ox-cart stacked with "
            "timber bears down from behind the man — three "
            "bystanders' mouths are torn wide with shouted "
            "warnings he cannot hear — and in the last instant a "
            "friend's hand has seized his shoulder and is hauling "
            "him back out of the wheel's path, his face jerking "
            "around in blank alarm at a rescue arriving before "
            "any danger he knew of. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b09", "out": "s09-surrounded-and-alone.jpeg", "seg": "n1 p5",
        "window": "48.98-53.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN"],
        "narration": "He was surrounded by people, and utterly alone.",
        "must_show": "the thesis close — his face sharp amid a blurred crowd; company everywhere, connection nowhere.",
        "must_not_show": "only he is in focus; the world is present and unreachable around him.",
        "scene": (
            "Close on the man's face, pin-sharp, while the whole "
            "market swirls soft and blurred around him — shapes "
            "of talkers, hagglers, friends at every distance, all "
            "of them dissolved into coloured silence — and in the "
            "one sharp face, the settled, practised loneliness of "
            "a man who long ago stopped expecting the world to "
            "let him in. Exactly one person is in focus, with one "
            "head."
        ),
    },
    {
        "id": "v2-r062-b10", "out": "s10-they-begged-a-touch.jpeg", "seg": "n2 p1-p2",
        "window": "53.84-58.46", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "DECAPOLIS"],
        "narration": ("His friends begged Jesus just to touch him. Jesus "
                      "did something better."),
        "must_show": "v32 — the friends' plea: hands urging Jesus toward the man, miming the touch they ask for; Jesus looking past them at the man himself.",
        "must_not_show": "Jesus's gaze goes to the MAN, not the petitioners — the 'something better' is already forming.",
        "scene": (
            "The two friends crowd Jesus with their plea — one "
            "gripping his own ear and pointing at their companion, "
            "the other miming a hand laid on a head, both faces "
            "urgent — while Jesus listens with his eyes gone past "
            "them entirely, resting steady on the watchful deaf "
            "man standing just beyond, meeting the one gaze in the "
            "crowd that reads everything. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b11", "out": "s11-he-took-him-by-the-hand.jpeg", "seg": "n2 p3",
        "window": "58.46-64.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "DECAPOLIS", "ASIDE"],
        "narration": ("He took the man by the hand and led him away from "
                      "the crowd — completely alone, just the two of "
                      "them."),
        "must_show": "v33 — the leading away: hand in hand, Jesus walking the man out of the crowd toward the olive shade; the multitude left at the wall.",
        "must_not_show": "the crowd does not follow — it stays banked behind the low wall; the two walk into quiet.",
        "scene": (
            "The camera holds the withdrawal from the side, both "
            "figures in profile: Jesus leads the man away by the hand — a plain firm "
            "grip, the man following with his eyes fixed on the "
            "back of this stranger who communicates in the one "
            "channel he has, touch — the two of them passing "
            "through a gap in the low stone wall into the "
            "olive-shaded hollow beyond, while the whole crowd "
            "banks up behind the wall and stays. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b12", "out": "s12-no-audience.jpeg", "seg": "n2 p4-p6",
        "window": "64.04-70.85", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "ASIDE"],
        "narration": ("No audience. No spectacle. This healing was going "
                      "to be private, personal, his."),
        "must_show": "the privacy — the two alone in the olive shade, face to face; the crowd a distant murmur beyond the wall.",
        "must_not_show": "no faces peer over the wall; the aloneness is complete and deliberate.",
        "scene": (
            "In the grey-green olive shade the two men stand alone "
            "face to face, an arm's length apart — the crowd "
            "nothing now but a soft band of colour far beyond the "
            "low wall — and the deaf man waits with his hands "
            "loose and his eyes locked on the stranger's face, "
            "given for the first time in his life a room with only "
            "one other person in it and that person entirely "
            "turned toward him. Exactly two people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b13", "out": "s13-squarely-in-front-of-him.jpeg", "seg": "n3 p1-p2",
        "window": "70.85-77.19", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "ASIDE"],
        "narration": ("Then Jesus did something beautiful. He could not "
                      "explain anything with words — the man could not "
                      "hear them."),
        "must_show": "the setup of the kindness — Jesus positioning himself squarely in the man's sightline, deliberate, making his whole body visible.",
        "must_not_show": "the deliberateness is the beauty — Jesus arranges HIMSELF to be readable.",
        "scene": (
            "Jesus has set himself squarely in front of the man at "
            "reading distance — shoulders square to him, face "
            "full-on in the olive light, hands lifting slowly into "
            "the space between them where they can be watched — a "
            "man deliberately making his whole body legible, the "
            "way you stand for someone who reads instead of "
            "hears, and the deaf man's eyes lock onto the rising "
            "hands. Exactly two people are in the frame; each has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b14", "out": "s14-the-only-language.jpeg", "seg": "n3 p3",
        "window": "77.19-80.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN"],
        "narration": ("So he spoke the only language the man could "
                      "receive."),
        "must_show": "the hands beginning — Jesus's two hands open in the space between them, mid-gesture; the man reading them like text.",
        "must_not_show": "the man's eyes on the hands, not the face — he is READING; the frame honours his literacy.",
        "scene": (
            "Close between the two men: Jesus's hands hang open "
            "and deliberate in the air at chest height, "
            "mid-gesture, fingers beginning to shape the first "
            "sign of the sentence — and below the frame's top edge "
            "the deaf man's intent eyes track the hands with the "
            "focused hunger of a man being spoken to, at last, in "
            "his own tongue. Each visible hand has five fingers. "
            "Exactly two people are in the frame."
        ),
    },
    {
        "id": "v2-r062-b15", "out": "s15-fingers-to-his-ears.jpeg", "seg": "n3 p4",
        "window": "80.38-85.66", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN"],
        "narration": ("He put his fingers gently to the man's ears: I see "
                      "exactly what is wrong."),
        "must_show": "v33 — the first sign: Jesus's fingertips resting gently at both the man's ears; eye contact held over the touch.",
        "must_not_show": "gentleness is the register — fingertips, not pressure; the man steady under it, understood.",
        "scene": (
            "Jesus's hands are raised to either side of the man's "
            "head, fingertips resting gently just at his ears — "
            "and over the touch the two faces hold each other, "
            "Jesus's eyes saying the sentence his fingers are "
            "spelling, and the deaf man's eyes flooding with the "
            "shock of being diagnosed in his own language: I see "
            "exactly what is wrong. Olive shade, quiet light. "
            "Exactly two people are in the frame; each visible "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r062-b16", "out": "s16-and-this-too.jpeg", "seg": "n3 p5",
        "window": "85.66-88.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN"],
        "narration": "He touched the man's mouth: and this too.",
        "must_show": "the second sign — Jesus's fingertips touching gently at the man's lips/chin; the inventory continuing.",
        "must_not_show": "the same gentle register; the man's trust visibly total now.",
        "scene": (
            "The sign continues: Jesus's hand has come down to "
            "touch two fingertips gently against the man's lips "
            "and chin — 'and this too' — while his other hand "
            "still rests at the man's ear, the whole broken "
            "apparatus named touch by touch — and the man stands "
            "utterly still under the naming, his breath visible, "
            "his trust gone total. Exactly two people are in the "
            "frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r062-b17", "out": "s17-he-looked-up-to-heaven.jpeg", "seg": "n3 p6-p7",
        "window": "88.62-98.32", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "ASIDE"],
        "narration": ("Then he looked up to heaven: what happens next "
                      "comes from God. Sign language, from the Son of "
                      "God, to one deaf man."),
        "must_show": "the third sign — Jesus's face lifted to the sky; the man's eyes FOLLOWING the look upward: the source, pointed at.",
        "must_not_show": "both gazes go up — the man reads the sign and follows it; that following is the whole beat.",
        "scene": (
            "Jesus lifts his face full to the sky above the olive "
            "branches, holding the man's hand against his own "
            "chest as he does it — and the deaf man's eyes follow "
            "the look up, from the stranger's raised face to the "
            "bright sky and back, reading the third sentence of "
            "the sign: what happens next comes from up there — "
            "two men in the shade, one conversation, no sound "
            "anywhere in it. Exactly two people are in the frame; "
            "each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b18", "out": "s18-the-small-stunning-detail.jpeg", "seg": "n4",
        "window": "98.32-107.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN"],
        "narration": ("And then Mark records a small, stunning detail — "
                      "one that has nothing to do with the healing at "
                      "all. Listen to exactly how he writes it."),
        "must_show": "the held instant before the sigh — everything ready, nothing yet moving; the hush before Mark's detail.",
        "must_not_show": "pure suspension — two faces, the sign finished, the air still.",
        "scene": (
            "The moment hangs: Jesus's face has come back down "
            "level from the sky and stopped, his hand still "
            "holding the man's against his chest, everything in "
            "the olive shade gone perfectly still — the signing "
            "done, the word not yet come, two men and a held "
            "breath in the grey-green light, and something moving "
            "far back in Jesus's eyes that has nothing to do with "
            "mechanics of ears. Exactly two people are in the "
            "frame; each has one head."
        ),
    },
    {
        "id": "v2-r062-b19", "out": "s19-he-sighed.jpeg", "seg": "s34a",
        "window": "107.83-112.41", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("And looking up to heaven, he sighed, and saith "
                      "unto him, (Mark 7:34)"),
        "must_show": "THE SIGH — close on Jesus alone: eyes lifted, chest falling through a deep sigh; grief for the whole broken world in one breath.",
        "must_not_show": "not weariness — grief; the weight of a world where a man never hears his name, felt before it is fixed.",
        "scene": (
            "Very close on Jesus's face and shoulders against the "
            "olive shade: his eyes are lifted to heaven and his "
            "whole chest is falling through a long visible sigh — "
            "the breath of a man feeling the full weight of a "
            "world broken enough to seal one of its people in "
            "silence for thirty years — grief passing through him "
            "on its way to becoming a word. Exactly one person is "
            "in the frame, with one head."
        ),
    },
    {
        "id": "v2-r062-b20", "out": "s20-ephphatha.jpeg", "seg": "j1",
        "window": "112.41-114.80", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN"],
        "narration": "Ephphatha. (Mark 7:34)",
        "must_show": "the word — Jesus's face come down to the man's, speaking it; the deaf man watching the lips shape it.",
        "must_not_show": "one word only — the mouth mid-syllable, the man reading it off the lips as it is spoken.",
        "scene": (
            "Jesus's face has come down level with the man's, "
            "close, and the word is on his lips — mouth caught "
            "mid-syllable, deliberate and shaped to be read — and "
            "the deaf man's eyes are on those lips doing what they "
            "have done all his life, reading, in the very last "
            "second that reading will ever be all he has. Exactly "
            "two people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r062-b21", "out": "s21-the-sigh-came-first.jpeg", "seg": "n5 p1-p3",
        "window": "114.80-124.68", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN"],
        "narration": ("He sighed. Before the word, he sighed. He felt the "
                      "weight of it — a world so broken that a man could "
                      "go a whole lifetime without hearing his own name."),
        "must_show": "the two-shot of the weight — the sigh's aftermath on Jesus's face and the man before him, the word landed between them.",
        "must_not_show": "the frame is emotionally heavy and physically still; the opening has not burst yet.",
        "scene": (
            "The two faces close in the olive shade, the word "
            "just spoken between them: Jesus's face still carries "
            "the sigh's gravity — moved, grieved, resolved — and "
            "the man before him has gone very still, his eyes "
            "wide on the stranger's, standing on the last second "
            "of the silence he has lived in since birth without "
            "knowing it is the last. Nothing else moves. Exactly "
            "two people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r062-b22", "out": "s22-be-opened.jpeg", "seg": "n5 p4-p6",
        "window": "124.68-133.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN"],
        "narration": ("The sigh came first. Then one word, in his own "
                      "Aramaic mother tongue. It means: be opened. And "
                      "everything opened."),
        "must_show": "the instant of opening — close on the man's face as sound arrives for the first time: eyes flying wide, the world flooding in.",
        "must_not_show": "no effect, no light — one human face registering the arrival of an entire sense.",
        "scene": (
            "Very close on the man's face at the instant it "
            "happens: his eyes fly wide and his head tips a "
            "fraction as if struck softly from every direction at "
            "once — the first sound of his life arriving not as "
            "one thing but as everything, wind and leaves and his "
            "own heartbeat and a man's voice, all at once, "
            "flooding into thirty years of nothing — his lips "
            "parting around a breath he can suddenly hear himself "
            "take. Exactly one person is in the frame, with one "
            "head."
        ),
    },
    {
        "id": "v2-r062-b23", "out": "s23-hands-to-his-ears.jpeg", "seg": "n5 p7",
        "window": "133.02-134.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN"],
        "narration": "And everything opened.",
        "must_show": "the reflex — both his hands flying up to his own ears, holding his head as sound pours in.",
        "must_not_show": "wonder, not pain — the hands cradle, they do not clutch in distress.",
        "scene": (
            "The man's both hands have flown up to cradle his own "
            "head, palms over his ears then off again, testing — "
            "on, off, on — his face between his own hands blazing "
            "with disbelieving laughter as the sound cuts in and "
            "out under his palms, a man playing with hearing like "
            "a child with a lamp, unable to stop switching it. "
            "Exactly one person is in the frame, with two hands "
            "of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r062-b24", "out": "s24-sound-rushed-in.jpeg", "seg": "n5 p8a",
        "window": "134.64-139.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "ASIDE"],
        "narration": ("Sound rushed in where there had been a lifetime of "
                      "nothing — birdsong, footsteps, voices,"),
        "must_show": "the cataloguing — the man turning bodily toward each sound: up at a bird in the olive, around at the crowd's far murmur.",
        "must_not_show": "each turn aimed at a real visible source — the bird IS in the tree, the crowd IS beyond the wall.",
        "scene": (
            "The man turns in the olive shade like a compass "
            "needle gone free — head snapping up toward a small "
            "brown bird singing plainly on the olive branch above "
            "him, then around toward the low wall where the "
            "crowd's murmur rolls over from beyond, then down at "
            "his own sandal grinding the gravel — each new sound "
            "spinning him toward its source while Jesus stands "
            "back and watches him meet the world. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b25", "out": "s25-his-own-name.jpeg", "seg": "n5 p8b",
        "window": "139.00-143.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN", "ASIDE"],
        "narration": "his own name.",
        "must_show": "the name — a friend at the wall's gap calling to him; the man wheeling toward the call, struck through.",
        "must_not_show": "the caller's mouth open mid-name, the man's face answering it — the first hearing of the sound that means HIM.",
        "scene": (
            "At the gap in the low wall one of his two friends "
            "has pushed through and stands with a hand cupped at "
            "his mouth, calling to him — mouth wide mid-name — "
            "and the man has wheeled toward the call and stopped "
            "dead, one hand rising slowly toward his own chest: "
            "the sound coming across the hollow is the one that "
            "means him, and he has never once heard it before. "
            "Exactly two people are in the frame; each has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b26", "out": "s26-the-first-plain-words.jpeg", "seg": "n5 p9",
        "window": "143.19-149.45", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN"],
        "narration": ("The knot in his tongue came loose, and the first "
                      "plain words of his life came out."),
        "must_show": "v35 — the loosed tongue: the man mid-speech, one hand at his own throat feeling the words come; Jesus's glad face receiving them.",
        "must_not_show": "the words visibly cost and amaze him — hand at throat, tears, and speech pouring anyway.",
        "scene": (
            "The man is speaking — plainly, loudly, the words "
            "tumbling — with one hand pressed flat to his own "
            "throat feeling them buzz out of him for the first "
            "time in his life, his face streaming and laughing "
            "around the pouring speech — and before him Jesus "
            "listens to the first plain sentence the man ever "
            "made with open unhidden gladness, the audience of "
            "one it was all for. Exactly two people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b27", "out": "s27-keep-it-quiet.jpeg", "seg": "n6 p1-p2",
        "window": "149.45-152.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "DECAPOLIS"],
        "narration": "Jesus asked them to keep it quiet. They could not.",
        "must_show": "v36 — the charge: Jesus's quieting gesture to the arriving friends; their faces already bursting past any possibility of obeying.",
        "must_not_show": "the comedy is gentle — he asks knowing; they fail lovingly.",
        "scene": (
            "The two friends have burst through the wall's gap "
            "and seized their speaking companion, and Jesus turns "
            "to them with one hand raised in a mild quieting "
            "gesture — say nothing — while both their faces are "
            "already ruined for secrecy: mouths open, arms around "
            "the man, joy visibly outrunning obedience before the "
            "request is even finished. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b28", "out": "s28-how-do-you-keep-it-secret.jpeg", "seg": "n6 p3",
        "window": "152.38-159.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN", "DECAPOLIS"],
        "narration": ("The more he asked, the more they told everyone — "
                      "and honestly, how do you keep a man's first words "
                      "a secret?"),
        "must_show": "the impossibility — back among the crowd: the man SPEAKING to people who have known him mute all his life; the ripple detonating.",
        "must_not_show": "the crowd's faces do the telling — neighbours who know exactly what his voice means.",
        "scene": (
            "Back on the road the man stands in the middle of the "
            "crowd TALKING — and the crowd is coming apart around "
            "the sound of him: an old neighbour with both hands "
            "over her mouth, a workmate gripping his arm and "
            "making him say it again, people at the back shoving "
            "in shouting his name to hear him answer to it — a "
            "town trying and failing to be quiet about a voice "
            "it has never heard. Golden late-afternoon light. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b29", "out": "s29-the-verdict-forming.jpeg", "seg": "n6 p4",
        "window": "159.26-162.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["DECAPOLIS"],
        "narration": "The whole region came to one verdict about him:",
        "must_show": "the verdict brewing — town elders and neighbours conferring gladly, nodding toward the unseen centre.",
        "must_not_show": "glad deliberation — a community agreeing on something good for once.",
        "scene": (
            "A knot of grey town elders and neighbours stands "
            "conferring in the golden light — but gladly: heads "
            "nodding, hands turned up, one old man ticking points "
            "off on his fingers while the others agree, every few "
            "words a glance back over their shoulders toward the "
            "commotion where the healed man is still talking — a "
            "region writing its verdict out loud. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b30", "out": "s30-done-all-things-well.jpeg", "seg": "s37",
        "window": "162.48-168.98", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DECAPOLIS"],
        "narration": ("He hath done all things well: he maketh both the "
                      "deaf to hear, and the dumb to speak. (Mark 7:37)"),
        "must_show": "v37 — the acclamation: the crowd's praise breaking over Jesus from every side; he stands quiet in it.",
        "must_not_show": "no halo/glow; astonishment 'beyond measure' carried by faces and lifted hands converging on him.",
        "scene": (
            "The crowd's verdict breaks over Jesus like surf, the "
            "camera behind the nearest lifted arms — "
            "hands lifted all around him, faces shining, an old "
            "woman reaching just to touch his sleeve, the healed "
            "man's voice still ringing somewhere in the middle of "
            "it — and at the centre of the acclamation Jesus "
            "stands quiet and almost withdrawn, receiving 'he "
            "hath done all things well' with the stillness of a "
            "man whose mind is already partly elsewhere. Golden "
            "light. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r062-b31", "out": "s31-his-friends-embrace.jpeg", "seg": "n6b p1-p2",
        "window": "168.98-175.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["DEAFMAN", "DECAPOLIS"],
        "narration": ("He has done everything well, they said. He makes "
                      "the deaf hear, and he gives the speechless their "
                      "voice."),
        "must_show": "the human sum — the healed man buried in his friends' embrace, talking through it; the wall of b07 gone.",
        "must_not_show": "he is INSIDE the circle now — the fire-circle outsider, centre of the arms.",
        "scene": (
            "The two friends have the man crushed in a double "
            "embrace and he is STILL TALKING through it, words "
            "pouring over their shoulders while they laugh and "
            "thump his back — the man who smiled half a beat late "
            "at the edge of every circle now buried at the warm "
            "centre of one, his voice, of all things, the loudest "
            "in it. Golden light. Exactly three people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r062-b32", "out": "s32-the-region-that-asked-him-to-leave.jpeg", "seg": "n6b p3",
        "window": "175.36-180.91", "wide": True, "jesus": True, "ref": REF,
        "locks": ["DECAPOLIS"],
        "narration": ("Not a bad verdict from a region that had asked him "
                      "to leave the last time he came."),
        "must_show": "the callback wide — the same eastern-shore country, now thronged around Jesus instead of pointing him to his boat.",
        "must_not_show": "the lake visible — the geography of the expulsion, hosting the embrace.",
        "scene": (
            "A wide golden frame of the eastern shore country, the "
            "camera high on the ridge behind the thronged road: "
            "the crowd spread thick around Jesus on the road "
            "above the blue lake — the same water his boat was "
            "once asked to take away, glittering below a hillside "
            "now covered with the people of the region pressing "
            "IN toward him — a coastline's verdict reversed, "
            "photographed from far enough back to see both. An "
            "upright vertical photograph, the ground at the "
            "bottom of the frame and the sky at the top, the "
            "horizon level — the picture is the right way up."
        ),
    },
    {
        "id": "v2-r062-b33", "out": "s33-what-kind-of-healer.jpeg", "seg": "n7 p1-p2",
        "window": "180.91-184.51", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Notice what kind of healer he is. He did not shout "
                      "over the crowd."),
        "must_show": "the thesis close — Jesus quiet amid the jubilation blur; the unshouting centre of a loud day.",
        "must_not_show": "the noise blurred around a still, warm, spent face.",
        "scene": (
            "Close on Jesus amid the soft-blurred jubilation, the "
            "only still thing in the frame: his face quiet and "
            "warm and a little tired in the golden light, eyes "
            "resting somewhere past the celebration — the healer "
            "who works one man at a time, standing unshouting in "
            "the middle of the loudest afternoon this road has "
            "ever had. Exactly one person is in focus, with one "
            "head."
        ),
    },
    {
        "id": "v2-r062-b34", "out": "s34-he-gave-him-back-the-world.jpeg", "seg": "n7 p3",
        "window": "184.51-193.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DEAFMAN", "ASIDE"],
        "narration": ("He took one man aside, met him inside his silence, "
                      "explained everything in the man's own language "
                      "before asking anything of him — and gave him back "
                      "the world."),
        "must_show": "the closing echo — the olive hollow again: Jesus and the healed man face to face in the long light, hands clasped; the aside-place, revisited whole.",
        "must_not_show": "the frame rhymes with b12 — same place, same two men, everything changed.",
        "scene": (
            "The olive-shaded hollow in the last long light, one "
            "more time: Jesus and the healed man stand face to "
            "face where the silence was broken, the man's hand "
            "clasped in both of Jesus's, talking — of course, "
            "still talking — and Jesus listening to him with "
            "complete attention, the first and best listener of "
            "the man's speaking life, in the little room off the "
            "world where the world was handed back. Exactly two "
            "people are in the frame; each has two arms, two "
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
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "DEAFMAN": "CAST-REF-V2/deafman.jpeg",
}
