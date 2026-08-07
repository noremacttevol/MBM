#!/usr/bin/env python3
"""V2 beat map — row 169, build-169-fulfil-righteousness (Matthew 3:13-17).

COVERAGE: 28 pictures over 127.46 s (card_start) = ~4.6 s/picture (matches the
library density set by rows 161-168; lesson 12 movie-coverage — every physical
verb and turn its own frame, an action a frame per action).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 169` shows no prior
review). Fresh authoring — the job is the LEARNING/COST laws in the positive.

SAME EVENT AS ROW 69 (build-69-baptism, Matthew 3:1-17). This is the Baptism of
Jesus told again as its own short lesson (the Godhead standing plain to see +
"fulfil all righteousness" + the invitation). Cross-video consistency (lesson
2/11): the BAPTIST person lock, the JORDAN place lock, the CROWD lock and the
DOVE lock are BYTE-IDENTICAL to row 69, John's canonical face reference
(CAST-REF-V2/baptist.jpeg) and the JORDAN plate (PLACE-REF/jordan.jpeg) are the
SAME assets copied from row 69 so John and the river read as the same man and the
same bend across both videos.

SCRIPTURE FACTS (Matthew 3:13-17 KJV, split across the red-letter beats):
  s14   "I have need to be baptized of thee, and comest thou to me?"  -> SCRIPTURE
        voice reading JOHN's words: the beat sits on JOHN's face, never Jesus
        (the row-39 lesson — a quoted line belongs on the man who says it).
  kv15  "And Jesus answering said unto him,"                          -> SCRIPTURE
        attribution — the PICTURE shows Jesus about to answer (jesus=True), the
        CAPTION is light-blue, not red.
  kv15b "Suffer it to be so now: for thus it becometh us to fulfil
         all righteousness."                                          -> JESUS
        red-letter, on Jesus's own face (jesus=True + ref=True, cream).
  kv15c "Then he suffered him."                                       -> SCRIPTURE
        John consents.

THE FATHER IS NEVER EMBODIED (CONTENT-CARE, same as row 69): gv17 is the GOD
voice ("This is my beloved Son, in whom I am well pleased") and its caption is
GREEN — but the Father has NO form, NO face, NO figure and NO light-source in the
sky. The words land on the upturned faces and on the beloved Son himself; the
opened heaven is painted as a great NATURAL bright break in the cloud (no rays,
no beams, no figure in the rift). kv17/gv17 beats therefore sit on Jesus's face
and the empty bright sky, never on a painted Father.

THE DOVE IS SCRIPTURAL HERE — SHOW IT (the opposite of the Holy-Ghost gate on
rows 165/166/168). Matthew 3:16 states the Spirit descending "like a dove, and
lighting upon him," and the narration says so plainly ("came down gently, like a
dove", "the Spirit resting as the dove"). So the DOVE is a REAL white bird,
painted plainly per scripture (DOVE lock, byte-identical to row 69) — descending
through the opened heaven (b15) and at rest on Jesus (b16, b21, b22). It is never
radiant or haloed; its plain realism IS the reverence.

TIME OF DAY: one bright morning at the Jordan throughout (V1 stills agree) — clean
river light; the opened-heaven beats keep daylight logic (a cloud-break's
brightness, not supernatural glow). No sunset anywhere.

PLACE + REF ASSETS (copied from row 69, committed with this row):
  JORDAN   PLACE-REF/jordan.jpeg   (build-69 s01, cross-video plate)
  BAPTIST  CAST-REF-V2/baptist.jpeg (build-69 canonical John face, black hair —
           the row-69 C-FIX corrected John's hair from orange to black; this is
           that corrected anchor)
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must NEVER
# name a character. Clothing colours stated POSITIVELY and dark — only Jesus
# wears cream. BAPTIST/JORDAN/CROWD/DOVE are BYTE-IDENTICAL to row 69.
LOCKS = {
    "BAPTIST": (
        "JOHN THE BAPTIST LOCK: John is the same man in every shot — "
        "mid-thirties, lean and burned dark by the desert, with a great "
        "mane of sun-shot black hair and a wild beard, fierce clear "
        "eyes and a voice's force visible in his throat and stance. He "
        "wears the locked raiment: a rough coat of CAMEL'S HAIR bound "
        "with a wide LEATHER girdle, bare weathered arms (never cream, "
        "never white). His face is shown clearly."
    ),
    "JORDAN": (
        "JORDAN LOCK: the baptizing bend of the Jordan — a slow green "
        "river between reed-lined banks, a trodden entry slope of pale "
        "mud, tamarisk and willow shade on the far side, and the "
        "wilderness hills pale beyond. The same bend, slope and reeds "
        "in every river beat."
    ),
    "CROWD": (
        "BANK CROWD LOCK: the countryside come out — farmers, "
        "tradesmen, mothers, soldiers off-duty, tax men, elders, in "
        "SATURATED DEEP earth colours: dark browns, deep russet, dark "
        "olive, burnt ochre, dusty indigo (never cream, never white; "
        "only Jesus wears cream). Faces shown clearly — penitents with "
        "dignity."
    ),
    "DOVE": (
        "DOVE LOCK: the Spirit's descent is one REAL white dove — a "
        "plain rock dove, pure white, painted exactly as a living bird "
        "in flight and at rest; never radiant, never translucent, with "
        "no ring of light about it; its realism IS the reverence."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r169-b01", "out": "s01-down-at-the-jordan.jpeg", "seg": "n1",
        "window": "0.280-2.920", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN", "CROWD"],
        "narration": "Something startling happens at the very start of it all.",
        "must_show": "the ONE establishing wide — the camera on the far bank, shooting across and past the waiting line's backs: John waist-deep at the green bend baptizing a penitent, the bank lined with people, the wilderness hills pale beyond; the morning's work already going.",
        "must_not_show": "no Jesus and no cream anywhere yet; no halo, glare or rim-light; no posed line facing the lens; no modern object; no panel, border or text.",
        "scene": (
            "At the green bend of the Jordan the camera stands back on the far "
            "bank and shoots across the water and past the backs and shoulders "
            "of the waiting line: John, lean and desert-burned in his coat of "
            "camel's hair, stands waist-deep lowering a penitent farmer under the "
            "slow green surface, while up the trodden mud slope the countryside "
            "waits its turn along the reed-bank and the pale wilderness hills "
            "stand behind the whole morning's business of beginning again. Every "
            "figure is an ordinary-sized person with two arms, two hands and one "
            "head, none turned to the camera."
        ),
    },
    {
        "id": "v2-r169-b02", "out": "s02-jesus-walks-down.jpeg", "seg": "n1",
        "window": "2.920-8.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["JORDAN"],
        "narration": "Jesus, who had no sin to wash away, walks down to the river Jordan",
        "must_show": "the deliberate arrival — Jesus alone coming down the trodden entry slope toward the water, road-dust of the journey on his hem; purpose in the stride, aimed at one river.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; not posed to the lens; nothing distinguishing him but the viewer's knowledge; no modern object; no panel or text.",
        "scene": (
            "Jesus comes down the pale trodden slope toward the green Jordan in "
            "the clean morning light — an ordinary-sized man in a plain cream wool "
            "robe travel-stained at the hem, staff in hand, his face set calm "
            "toward the water ahead. The reed-lined bend and the pale wilderness "
            "hills stand beyond. He walks with the purpose of a man who came a "
            "long way for this one river; his gaze is on the water, not the "
            "camera, and nothing rings his head."
        ),
    },
    {
        "id": "v2-r169-b03", "out": "s03-asks-john-to-baptize.jpeg", "seg": "n1",
        "window": "8.000-13.838", "wide": False, "jesus": True, "ref": True,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "and asks John to baptize him — the sinless One, lining up for the sinner's ordinance.",
        "must_show": "the request — a two-shot at the water's edge: Jesus standing before John in the shallows, asking; the sinless One come to the same water and the same hands as every penitent.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; John in camel's hair; no gap opening around Jesus; faces on each other, not the lens; no modern object; no panel or text.",
        "scene": (
            "At the water's edge the two men stand close over the shallows: Jesus "
            "in his plain cream robe steps to John and quietly asks, and John, "
            "lean and desert-burned in his camel's-hair coat, turns from the line "
            "to face him — the sinless one come to the very water and the very "
            "hands that have washed sinners all morning. The green river slides "
            "past their waists, the reed-bank behind. Both are ordinary-sized men "
            "with two hands and one head, their eyes on each other, not the "
            "camera; no light rings either head."
        ),
    },
    {
        "id": "v2-r169-b04", "out": "s04-john-was-stunned.jpeg", "seg": "n2",
        "window": "13.838-15.760", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "John was stunned, and tried to stop him.",
        "must_show": "close on John — the fearless desert prophet staggered, both weathered hands coming up to stop the request; the wild man's first and only balk.",
        "must_not_show": "Jesus not the subject of this frame; no cream on John; no halo, glare or rim-light; no face posed to the lens; no modern object; no panel or text.",
        "scene": (
            "Close on John in the river light: the great mane of sun-shot black "
            "hair, the wild beard, the fierce eyes suddenly wide — both burned "
            "hands lifting between himself and the man before him to stop what is "
            "being asked, the trumpet of his voice caught in his working throat. "
            "The green water slides past his waist and the reed-bank stands soft "
            "behind. He is an ordinary-sized man in camel's hair with two hands "
            "and one head, his gaze on the unseen Jesus, not the camera; no light "
            "rings his head."
        ),
    },
    {
        "id": "v2-r169-b05", "out": "s05-the-whole-thing-backwards.jpeg", "seg": "n2",
        "window": "15.760-23.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "He felt the whole thing backwards: surely he was the one who needed to be baptized by Jesus, not Jesus by him.",
        "must_show": "the reversal held — a two-shot in the shallows: John's hand sweeping from his own chest toward Jesus and back, baffled; the direction of grace disputed by its own herald, Jesus quiet opposite him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; John in camel's hair; both faces on each other, not the lens; no modern object; no panel or text.",
        "scene": (
            "Over the green water John draws the argument in the air — his burned "
            "hand sweeping from his own camel-hair chest toward the calm man in "
            "cream before him, then reversing, palm up and baffled — the traffic "
            "of worthiness diagrammed the wrong way and the right way, while "
            "Jesus stands quiet and certain opposite him. The reed-bank and pale "
            "hills sit beyond. Both are ordinary-sized men with two hands and one "
            "head, their eyes on each other, not the camera; no light rings "
            "either head."
        ),
    },
    {
        "id": "v2-r169-b06", "out": "s06-who-was-he.jpeg", "seg": "n2",
        "window": "23.000-25.912", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "Who was he to baptize the Lord?",
        "must_show": "the protest's heart — close on John's hand pressed flat to his own camel-hair chest, his face humbled: who was HE for this; the pronoun made gesture.",
        "must_not_show": "Jesus not the subject here; no cream on John; no halo, glare or rim-light; no face posed to the lens; no modern object; no panel or text.",
        "scene": (
            "Close in the river light: John's burned hand presses flat against "
            "his own camel-hair chest, the wild face gone humble under its mane — "
            "the HE of his protest made physical, fingers spread over the rough "
            "coat and the heart under it, a prophet indicating the one man in "
            "Israel he is certain has no business at his hands. The green water "
            "and reed-bank stand quiet behind. An ordinary-sized man with two "
            "hands and one head, his eyes down and toward the unseen Lord, not "
            "the camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r169-b07", "out": "s07-i-have-need-to-be-baptized.jpeg", "seg": "s14",
        "window": "25.912-30.796", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "I have need to be baptized of thee, and comest thou to me?",
        "must_show": "SCRIPTURE-EXACT (John's own words) — the frame is on JOHN, the man speaking: his staggered face naming his own need aloud, humility from the loudest voice in Israel.",
        "must_not_show": "Jesus not the subject (John's line sits on John); no cream on John; no halo, glare or rim-light; no face posed to the lens; no modern object; no panel or text.",
        "scene": (
            "Close on John's staggered face in the river light: the wild mane "
            "framing features stripped of all their thunder — the fierce eyes "
            "suddenly a debtor's eyes, the trumpet throat working around a "
            "confession of his own — the man who calls all Israel to the water "
            "naming, out loud, the one baptism he cannot perform: his own. The "
            "green water slides past, the reed-bank soft behind. An "
            "ordinary-sized man in camel's hair with two hands and one head, his "
            "gaze on the unseen Jesus, not the camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r169-b08", "out": "s08-and-jesus-answering.jpeg", "seg": "kv15",
        "window": "30.796-34.625", "wide": False, "jesus": True, "ref": True,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "And Jesus answering said unto him,",
        "must_show": "SCRIPTURE-ATTRIBUTION — Jesus turning to John and drawing breath to answer, the moment just before he speaks; the two close in the shallows.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; John in camel's hair; faces on each other, not the lens; no modern object; no panel or text.",
        "scene": (
            "The pause before the answer: Jesus turns fully toward John in the "
            "green shallows, his face lifting and steadying as he draws breath to "
            "speak, one hand beginning to open. John waits close beside him, the "
            "wild mane still, the reed-bank and pale hills beyond. Both are "
            "ordinary-sized men in the clean river light — only Jesus in cream, "
            "John in camel's hair — their eyes meeting, not the camera; two hands "
            "and one head each, no ring of light on either."
        ),
    },
    {
        "id": "v2-r169-b09", "out": "s09-suffer-it-to-be-so.jpeg", "seg": "kv15b",
        "window": "34.625-41.376", "wide": False, "jesus": True, "ref": True,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "Suffer it to be so now: for thus it becometh us to fulfil all righteousness.",
        "must_show": "SCRIPTURE-EXACT (Jesus's red-letter) — Jesus's hand coming to rest on John's raised forearm, gently lowering the protest as he speaks; the words and the touch together, warm and immovable.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; John in camel's hair; faces on each other, not the lens; no modern object; no panel or text.",
        "scene": (
            "Over the green water Jesus's hand comes to rest on John's raised "
            "forearm and gently lowers it as he speaks — the protest yielding "
            "under the touch, John's hand sinking toward the surface, his wild "
            "face beginning its surrender — permission asked and granted in one "
            "motion between the only two men in Israel who understand what is "
            "about to happen. The reed-bank stands soft behind. Both are "
            "ordinary-sized men with two hands and one head, only Jesus in cream, "
            "their eyes holding each other, not the camera; no light rings "
            "either head."
        ),
    },
    {
        "id": "v2-r169-b10", "out": "s10-then-he-suffered-him.jpeg", "seg": "kv15c",
        "window": "41.376-44.299", "wide": False, "jesus": True, "ref": True,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "Then he suffered him.",
        "must_show": "SCRIPTURE-EXACT — John's consent arrived: his hands rising now to their office, the two men squaring to each other in the river to do the thing together.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; John in camel's hair; faces on each other, not the lens; no modern object; no panel or text.",
        "scene": (
            "In the slow green water the two men square to each other — John's "
            "consent arrived at last in his steadied shoulders and his weathered "
            "hands rising to their office, Jesus turning calmly to stand ready "
            "before him — the desert's roughest prophet and Galilee's carpenter "
            "taking up together the task neither can refuse. The reed-bank and "
            "pale hills stand beyond. Both are ordinary-sized men with two hands "
            "and one head, only Jesus in cream, their eyes on each other, not the "
            "camera; no light rings either head."
        ),
    },
    {
        "id": "v2-r169-b11", "out": "s11-went-down-into-the-water.jpeg", "seg": "n3",
        "window": "44.299-47.160", "wide": False, "jesus": True, "ref": True,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "So even the perfect One went down into the water.",
        "must_show": "SCRIPTURE-EXACT: the baptism itself — John's hands lowering Jesus back beneath the green surface, the immersion mid-act, the Jordan closing over the cream robe.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; the going-under real and complete; whole hands and natural contact; no modern object; no panel or text.",
        "scene": (
            "In the slow green Jordan the act itself: John's weathered hands firm "
            "at shoulder and clasped wrists, lowering Jesus backward beneath the "
            "surface — the cream robe darkening as the water takes it, the face "
            "going under calm and open, the river folding over him the way it has "
            "folded over every penitent all morning. The reed-bank stands behind. "
            "Both are ordinary-sized men with two hands and one head, only Jesus "
            "in cream; neither turned to the camera, no light rings either head."
        ),
    },
    {
        "id": "v2-r169-b12", "out": "s12-not-because-he-needed-cleansing.jpeg", "seg": "n3",
        "window": "47.160-53.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["JORDAN"],
        "narration": "Not because he needed cleansing, but to fulfil all righteousness — to walk the path himself,",
        "must_show": "the clean one in the water — close on Jesus's face just before or as he goes under: nothing to shed, everything to begin; purpose without penitence, obedience as its own reason.",
        "must_not_show": "no halo, glare or rim-light; only Jesus in cream; no penitent weight in the face — only calm willingness; no modern object; no panel or text.",
        "scene": (
            "Close on Jesus's face above the green water in the instant of the "
            "going-under: none of the morning's penitent weight anywhere in it — "
            "no ledger closing behind the eyes, no relief pre-gathering — only "
            "the calm forward willingness of a man walking a path himself so that "
            "others may walk it after him, carrying nothing to the water but "
            "obedience. The reed-bank sits soft behind. An ordinary-sized man in "
            "cream with two hands and one head, his gaze inward and forward, not "
            "the camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r169-b13", "out": "s13-the-way-in-for-everyone.jpeg", "seg": "n3",
        "window": "53.000-58.809", "wide": False, "jesus": True, "ref": True,
        "locks": ["JORDAN", "CROWD"],
        "narration": "and leave us an example that this gate is the way in, for everyone.",
        "must_show": "the doorway doctrine — Jesus standing in the water where every penitent has stood, the waiting line visible up the bank behind him: his baptism composed as one of many, the way in kept in frame for all.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; the crowd in deep earth colours, never cream; the 'everyone' visible; no modern object; no panel or text.",
        "scene": (
            "The camera stands a little behind Jesus's shoulder and looks past "
            "him up the bank: he stands in the river at the exact worn entry "
            "every penitent has used all morning — and up the trodden slope the "
            "waiting line is plain in frame, a soldier, a tax man, an old praying "
            "woman among the countryside's honest variety in their deep earth "
            "colours — one baptism composed among the day's many, the way in left "
            "open for everyone. Only Jesus is in cream. Every figure is an "
            "ordinary-sized person with two hands and one head, none turned to "
            "the lens; no light rings any head."
        ),
    },
    {
        "id": "v2-r169-b14", "out": "s14-came-up-heaven-answered.jpeg", "seg": "n4",
        "window": "58.809-62.580", "wide": False, "jesus": True, "ref": True,
        "locks": ["JORDAN"],
        "narration": "And as he came up out of the water, heaven itself answered.",
        "must_show": "SCRIPTURE-EXACT: the rising and the opening together — Jesus coming straight up out of the river streaming, face lifted, and above the valley the grey cloud deck breaking into a great bright rift of clear sky.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO rays, NO beams, NO figure in the rift — a magnificent NATURAL cloud-break's brightness; only Jesus in cream; no modern object; no panel or text.",
        "scene": (
            "Jesus comes straight up out of the green Jordan — water streaming "
            "from his hair and beard, the wet cream robe clinging, his face "
            "lifted — and above the whole valley the grey cloud deck is breaking "
            "open as he rises: a great rift of clean bright sky tearing wide, the "
            "daylight doubling on the water, a man surfacing and a sky unsealing "
            "in one shared instant. The reed-bank and pale hills stand beyond. An "
            "ordinary-sized man in cream with two hands and one head, his gaze up "
            "and forward, not the camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r169-b15", "out": "s15-spirit-came-down-like-a-dove.jpeg", "seg": "n4",
        "window": "62.580-66.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOVE", "JORDAN"],
        "narration": "The skies opened, and the Spirit of God came down gently, like a dove,",
        "must_show": "SCRIPTURE-EXACT: the descent — the one white dove descending through the bright cloud-rift in a long gentle glide toward the standing Jesus; a real bird, unmistakable and plain, per scripture.",
        "must_not_show": "the dove NEVER radiant, translucent or haloed — pure white feathers in real light; NO rays following it; no halo, glare or rim-light on Jesus; only Jesus in cream; no modern object; no panel or text.",
        "scene": (
            "Down through the great bright rift the white dove comes — a real bird "
            "in a long unhurried glide, wings set, descending the height of the "
            "opened sky toward the man standing wet in the river — its whiteness "
            "plain feather-white in the doubled daylight, its path a single soft "
            "diagonal from the sky's tear toward a human shoulder. Jesus stands "
            "streaming below, face lifting to it. The reed-bank sits beyond. An "
            "ordinary-sized man in cream with two hands and one head, not turned "
            "to the camera; no light rings his head and none rings the bird."
        ),
    },
    {
        "id": "v2-r169-b16", "out": "s16-rested-upon-him.jpeg", "seg": "n4",
        "window": "66.500-70.598", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOVE", "JORDAN"],
        "narration": "and rested upon him in the warm light.",
        "must_show": "the dove at rest — close on the white dove settling on Jesus's wet shoulder, wings folding, a real bird's small weight visibly upon the cream wool; the Spirit come to rest.",
        "must_not_show": "the dove NEVER radiant, translucent or haloed; no halo, glare or rim-light on Jesus; only Jesus in cream; whole natural contact of bird on shoulder; no modern object; no panel or text.",
        "scene": (
            "Close on the shoulder in the warm morning light: the white dove "
            "settles upon Jesus's wet cream wool, wings folding, its small real "
            "weight plainly resting there — feathers, folded pinions, a living "
            "bird come to rest on a man just risen from the water. Jesus holds "
            "still beneath it, his face easing. The reed-bank sits soft behind. "
            "An ordinary-sized man in cream with two hands and one head, not "
            "turned to the camera; no light rings his head and none rings the "
            "bird."
        ),
    },
    {
        "id": "v2-r169-b17", "out": "s17-a-voice-from-heaven.jpeg", "seg": "kv17",
        "window": "70.598-74.582", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOVE", "BAPTIST", "JORDAN", "CROWD"],
        "narration": "And lo a voice from heaven, saying,",
        "must_show": "SCRIPTURE-ATTRIBUTION: the voice arriving — the dove at rest on Jesus, and every face on the bank lifting at once toward the opened bright sky; the hearing painted, the speaker never shown.",
        "must_not_show": "NO source of the voice — no form, no figure, no light-source in the rift; the words exist ONLY in the upturned faces and the empty brightness; no halo, glare or rim-light on anyone; only Jesus in cream; no panel or text.",
        "scene": (
            "The dove sits at rest on Jesus's wet shoulder — and along the whole "
            "riverbank every face lifts at once: John's mane falling back as his "
            "chin rises, a soldier's helmet sliding from under his arm, an old "
            "woman's prayer stopping open-mouthed — a crowd of ordinary people in "
            "deep earth colours hearing the same thing from the same empty "
            "brightness, which the picture, rightly, shows as bright sky and "
            "nothing else. Only Jesus is in cream. Every figure has two hands and "
            "one head; no light rings any head and none rings the bird."
        ),
    },
    {
        "id": "v2-r169-b18", "out": "s18-this-is-my-beloved-son.jpeg", "seg": "gv17",
        "window": "74.582-80.252", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOVE", "JORDAN"],
        "narration": "This is my beloved Son, in whom I am well pleased.",
        "must_show": "SCRIPTURE-EXACT (the Father's voice): the sentence landing on its subject — close on Jesus's streaming face as the words arrive from the bright emptiness above, belovedness received, the white dove plain at his shoulder.",
        "must_not_show": "THE FATHER IS NEVER SHOWN — no form, no face, no figure, no light-source in the sky; no halo, glare or rim-light on Jesus; only Jesus in cream; the reception is on the human face, never on a painted speaker; no panel or text.",
        "scene": (
            "Close on Jesus's streaming face as the words arrive from the bright "
            "emptiness above: the warm brown eyes closing briefly, the wet "
            "beard's jaw steadying, something settling through the features like "
            "bread reaching the hungry — the dove's plain white at his shoulder — "
            "a Son being told, before one sermon or one miracle, in the hearing "
            "of a whole riverbank, exactly whose and exactly how loved. The sky "
            "above him is bright and empty of any shape. An ordinary-sized man in "
            "cream with two hands and one head, not turned to the camera; no "
            "light rings his head and none rings the bird."
        ),
    },
    {
        "id": "v2-r169-b19", "out": "s19-look-closely.jpeg", "seg": "n5",
        "window": "80.252-84.760", "wide": True, "jesus": True, "ref": True,
        "locks": ["DOVE", "BAPTIST", "JORDAN", "CROWD"],
        "narration": "Look closely at that one moment, because it opens a window into who God is.",
        "must_show": "the witness's wide view — the camera among the watchers on the bank, behind their shoulders: the Son standing wet in the river, the white dove upon him, the great bright rift open above the valley, the crowd hearing; the whole moment a bystander saw.",
        "must_not_show": "NO figure or light-source in the rift (the Father never shown); NO rays linking sky, bird and man; no merging; no halo, glare or rim-light; only Jesus in cream; no posed line to the lens; no panel or text.",
        "scene": (
            "From the trodden bank the camera stands among the witnesses, behind "
            "their shoulders and to the side, taking the whole moment as they saw "
            "it: the green river's breadth, and standing in it — wet, real, "
            "distinct — the Son in his water-dark cream robe, the white dove at "
            "rest on his shoulder, the great bright rift standing open in the "
            "cloud above the valley, and around the water the lifted faces of the "
            "crowd in their deep earth colours. Only Jesus is in cream. Every "
            "figure is an ordinary-sized person with two hands and one head, none "
            "turned to the lens; no light rings any head."
        ),
    },
    {
        "id": "v2-r169-b20", "out": "s20-the-son-standing-in-the-river.jpeg", "seg": "n5",
        "window": "84.760-90.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["JORDAN"],
        "narration": "Three were there at once, and each was distinct: the Son standing in the river,",
        "must_show": "the FIRST Person located — a clear medium on Jesus alone, standing wet and real in the green water, distinct and locatable: there, in the river.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; the Son shown plainly as one distinct person, not merged with sky or bird; no modern object; no panel or text.",
        "scene": (
            "A clear medium on the Son alone: Jesus stands wet and real in the "
            "green Jordan, the cream robe dark with river water, his face calm and "
            "lifted, an ordinary-sized man plainly located exactly where a "
            "bystander's finger could point — there, in the water. The reed-bank "
            "and pale hills sit beyond in the clean morning light. Two hands and "
            "one head, his gaze up and forward, not the camera; no light rings "
            "his head."
        ),
    },
    {
        "id": "v2-r169-b21", "out": "s21-spirit-dove-father-heaven.jpeg", "seg": "n5",
        "window": "90.000-95.498", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOVE", "JORDAN"],
        "narration": "the Spirit resting as the dove, and the Father speaking from the opened heaven.",
        "must_show": "the SECOND and THIRD located, each distinct — close: the white dove wholly a bird at rest on the Son's shoulder, and above it the bright opened rift the frame keeps empty; Spirit resting, Father heard.",
        "must_not_show": "NO merging, no symbol-fusion; the bird distinctly a bird, the Father distinctly ABSENT from view — no form, no face, no figure, no light-source in the rift; no halo, glare or rim-light; only Jesus in cream; no panel or text.",
        "scene": (
            "Close on the shoulder and the lifted face: the white dove wholly "
            "itself — feathers, folded wings, a bird's small real weight settled "
            "on the wet cream wool — and above it the Son's face turned up toward "
            "a height the frame keeps bright and empty of any shape — Spirit "
            "resting, Father heard, Son standing: three realities, one moment, "
            "nothing blended. The reed-bank sits soft behind. An ordinary-sized "
            "man in cream with two hands and one head, not turned to the camera; "
            "no light rings his head and none rings the bird."
        ),
    },
    {
        "id": "v2-r169-b22", "out": "s22-not-changing-costumes.jpeg", "seg": "n6",
        "window": "95.498-99.900", "wide": False, "jesus": True, "ref": True,
        "locks": ["DOVE", "JORDAN"],
        "narration": "Here is the quiet study gem. This was not one person changing costumes.",
        "must_show": "the distinctness held — close on the Son with the dove distinctly a bird at his shoulder and the bright empty height above: three real facts at once, not one figure in three guises.",
        "must_not_show": "NO merging or morphing of the three; no figure or light-source in the sky; the bird a plain bird; no halo, glare or rim-light; only Jesus in cream; no panel or text.",
        "scene": (
            "Close again on the Son in the river light, the plain white dove a "
            "distinct bird resting at his wet shoulder and the sky above him "
            "bright and empty of any shape — the picture holding all three as "
            "separate, real facts of the one moment, never one person slipping "
            "between three costumes. The reed-bank sits behind. An ordinary-sized "
            "man in cream with two hands and one head, his face lifted, not "
            "turned to the camera; no light rings his head and none rings the "
            "bird."
        ),
    },
    {
        "id": "v2-r169-b23", "out": "s23-three-distinct-persons.jpeg", "seg": "n6",
        "window": "99.900-107.990", "wide": True, "jesus": True, "ref": True,
        "locks": ["DOVE", "BAPTIST", "JORDAN", "CROWD"],
        "narration": "It was three distinct persons, together, each doing his own part — the Godhead, standing plain to see.",
        "must_show": "SCRIPTURE-DOCTRINE: the whole moment in one true frame as the bank saw it — the Son wet in the water, the dove upon him, the great bright opened sky above, the hearing crowd around; three distinct Persons' evidence in a single real scene.",
        "must_not_show": "NO triangle symbols, NO rays linking sky, bird and man, NO merging; NO figure or light-source in the rift (the Father never shown); no halo, glare or rim-light; only Jesus in cream; no posed line to the lens; no panel or text.",
        "scene": (
            "One frame holds the whole moment as the bank saw it, the camera at "
            "the water's side taking river and watchers in profile: the Son "
            "standing wet and real in the green Jordan, the white dove at rest "
            "upon his shoulder, the great bright rift standing open in the cloud "
            "above the valley, and around the water the lifted faces of the crowd "
            "in their deep earth colours, John foremost — three Persons present "
            "to one riverbank, each exactly where scripture put them, nothing "
            "merged and nothing symbolized. Only Jesus is in cream. Every figure "
            "is an ordinary-sized person with two hands and one head, none turned "
            "to the lens; no light rings any head."
        ),
    },
    {
        "id": "v2-r169-b24", "out": "s24-even-he-was-baptized.jpeg", "seg": "n6",
        "window": "107.990-111.808", "wide": False, "jesus": True, "ref": True,
        "locks": ["BAPTIST", "JORDAN"],
        "narration": "And notice: even He was baptized.",
        "must_show": "the point made plain — Jesus standing wet in the river just after his baptism, John a pace off with his hands still half-raised; even the sinless One went down into this same water.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; John in camel's hair; the two ordinary-sized and proportionate; no modern object; no panel or text.",
        "scene": (
            "In the green Jordan Jesus stands wet from the baptism just given, the "
            "cream robe dark and clinging, and a pace off John steadies himself, "
            "his weathered hands still half-raised from the work — even the "
            "sinless One come up out of this same water like every penitent of "
            "the morning. The reed-bank and pale hills stand beyond. Both are "
            "ordinary-sized men with two hands and one head, only Jesus in cream, "
            "their gaze on the moment, not the camera; no light rings either "
            "head."
        ),
    },
    {
        "id": "v2-r169-b25", "out": "s25-settles-it-for-the-rest-of-us.jpeg", "seg": "n7",
        "window": "111.808-113.630", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "JORDAN"],
        "narration": "And that settles it for the rest of us.",
        "must_show": "the 'us' — ordinary people of the countryside at the water's edge, the waiting line of honest need; the rest of us for whom the way is now settled.",
        "must_not_show": "no Jesus and no cream here; no halo, glare or rim-light; the crowd in deep earth colours, dignified; no modern object; no panel or text.",
        "scene": (
            "Along the trodden bank the day's line waits its turn at the green "
            "water: a soldier with his eyes down, a farm couple holding hands, an "
            "old woman praying silently mid-queue — the countryside's honest "
            "variety in their deep earth colours, the ordinary people for whom the "
            "matter is now settled. The reed-bank and pale hills stand behind. "
            "Every figure is an ordinary-sized person with two hands and one "
            "head, none in cream and none turned to the camera; no light rings "
            "any head."
        ),
    },
    {
        "id": "v2-r169-b26", "out": "s26-the-one-man-went-down.jpeg", "seg": "n7",
        "window": "113.630-118.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["JORDAN"],
        "narration": "If the one man who never needed it still went down into the water to fulfil all righteousness,",
        "must_show": "the founding image recalled — Jesus in the green river at the entry point, the one who never needed it having gone down into the water himself; the reason held up.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; nobody a giant; no modern object; no panel or text.",
        "scene": (
            "Jesus stands wet at the river's worn entry in the clean morning "
            "light, the cream robe dark with Jordan water, calm and settled — the "
            "one man who never needed the washing having gone down into it "
            "anyway, to fulfil all righteousness and open the way. The reed-bank "
            "and pale hills sit beyond. An ordinary-sized man in cream with two "
            "hands and one head, his face calm and forward, not the camera; no "
            "light rings his head."
        ),
    },
    {
        "id": "v2-r169-b27", "out": "s27-the-way-open-and-good-for-you.jpeg", "seg": "n7",
        "window": "118.500-122.920", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "JORDAN"],
        "narration": "then the way is surely open, and good, for you.",
        "must_show": "the open way — an ordinary person coming up out of the same green water, washed and relieved, the door plainly in use; open and good for the one watching.",
        "must_not_show": "no Jesus and no cream here; no halo, glare or rim-light; the relief real and dignified; no modern object; no panel or text.",
        "scene": (
            "Mid-water an ordinary penitent comes up out of the green Jordan "
            "streaming, eyes opening, a breath drawn, relief breaking over the "
            "wet face — an everyday person of the countryside in a plain "
            "earth-toned tunic, the same water still receiving as it received "
            "this morning, the way plainly open and good. The reed-bank and pale "
            "hills stand behind. An ordinary-sized person with whole hands and "
            "one head, not in cream, face lifted to the light, not the camera; no "
            "light rings the head."
        ),
    },
    {
        "id": "v2-r169-b28", "out": "s28-will-you-go-down-into-it.jpeg", "seg": "n7",
        "window": "122.920-127.461", "wide": False, "jesus": False, "ref": False,
        "locks": ["CROWD", "JORDAN"],
        "narration": "When you come to that same water, will you go down into it?",
        "must_show": "the invitation handed over — an ordinary person (the viewer's stand-in) standing at the water's edge, seen from behind and the side, on the verge of stepping down into the green river; the question left open and hopeful.",
        "must_not_show": "no Jesus and no cream; no halo, glare or rim-light; not posed to the lens; no modern object; no panel or text.",
        "scene": (
            "At the trodden entry an ordinary person stands right at the edge of "
            "the green Jordan, seen from behind and a little to the side so the "
            "gaze goes to the water and not the camera — one foot at the pale mud "
            "slope, poised on the verge of stepping down into the same river "
            "where the sinless One went first. The reed-bank and pale hills stand "
            "quiet in the morning light, the water open ahead. A plain "
            "earth-toned person of ordinary height with whole hands and one head, "
            "not in cream; no light rings the head, the way ahead simply open."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (art); PLACE-WIRING.json is the
# committed record. JORDAN reuses row 69's plate (build-69 s01) for cross-video
# place consistency (lesson 11) — the same bend of the river in both videos.
PLACE_REFS = {
    "JORDAN": "PLACE-REF/jordan.jpeg",  # build-69-baptism s01 (cross-video, manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, carried by IMAGE not wording (lesson 2). John the
# Baptist reuses row 69's corrected canonical face (black hair, per the row-69
# C-FIX) so he is the same man across both baptism videos.
REFS = {
    "BAPTIST": "CAST-REF-V2/baptist.jpeg",
}
