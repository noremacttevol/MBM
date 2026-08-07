#!/usr/bin/env python3
"""V2 beat map — row 166, build-166-baptized-properly (Acts 19:1-6).

COVERAGE: 24 pictures over 121.22 s = ~5.0 s/picture (matches rows 161-165
library density; lesson-12 movie coverage).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 166` shows no prior
review). Fresh authoring — LEARNING/COST laws in the positive.

SCRIPTURE FACTS (Acts 19 KJV, the passage this row narrates):
  19:2  "He said unto them, Have ye received the Holy Ghost since ye
        believed? And they said unto him, We have not so much as heard
        whether there be any Holy Ghost."                              -> s2
  19:4  "Then said Paul, John verily baptized with the baptism of
        repentance, saying unto the people, that they should believe on
        him which should come after him, that is, on Christ Jesus."    -> s4
  19:5  "When they heard this, they were baptized in the name of the
        Lord Jesus."                                                   -> kv5
  19:6  "And when Paul had laid his hands upon them, the Holy Ghost came
        on them; and they spake with tongues, and prophesied."        -> kv6

SPEAKER LAW (the row-39 lesson): Luke narrating Acts — NO Jesus red-letter in
the passage. s2, s4, kv5 and kv6 are ALL the SCRIPTURE voice (light blue); s2/s4
are PAUL's quoted words (still scripture voice in Acts, NOT Jesus red). Jesus is
only NAMED ("Christ Jesus" / "the Lord Jesus") and is NOT present in the Ephesus
scene — so there is NO Jesus beat in this row (jesus=False, ref=False on every
beat). Nobody wears cream.

ROW INTENT: RESTORATION-leaning milk, strictly in the Bible's own frame, church
NEVER named. The Ephesian disciples were sincere and already believed — yet they
had only John's preparatory baptism and had never received the Holy Ghost. Paul
sets the ordinance right: baptism in the name of the Lord Jesus, THEN the laying
on of hands, and the gift comes. Sincerity did not replace authority; it was
completed by it. The close offers the viewer that same careful pattern. (Direct
companion to row 165.)

THE HOLY GHOST IS NEVER EMBODIED (lesson 8 / CONTENT-CARE, treated like the
Father): where the gift comes (b17) it is warm light down from above the top of
the frame onto the men's faces. "They spake with tongues, and prophesied" (b18)
is shown as the MEN'S OWN fervent response — mouths open in praise, a hand
lifted in prophecy, faces alight — NOT tongues of FLAME (that is Pentecost, a
different event — do not import flame or a dove or any figure). DRIFT_WORDS
glow/halo/rim-light are banned and the scene text avoids them.

CAST (locked): PAUL uses the byte-identical canonical PAUL lock already in
builds 138 and 155 (same man across all 200). The EPHESIAN-DISCIPLES are the
small group of about twelve men (Acts 19:7) — a build-local people lock. The
baptism (b14) is shot on the WATER and the BELIEVER, the baptizer's hands only,
so no extra face is boarded.

MOVIE COVERAGE (lesson 12): the establishing wide is b01 and ONLY b01;
everything else is a single, two-shot, or insert. The disciples are a SMALL band
of distinct faces, never a nameless crowd. The correcting ordinance is covered
as a SEQUENCE — the wrong-baptism question, the right baptism, the laying on of
hands, the gift, the tongues — never one frame for the whole thing.

ONE NEW PLACE (the runner promotes from a first good frame, lesson 11):
EPHESUS-ROOM. No beat bears Jesus, so any frame is safe to promote. Steps in
QC.md.

TIME OF DAY ARC: the meeting and questioning in steady warm lamplight indoors;
the baptism (b14) in bright outdoor morning at the water; the laying on of hands
and the gift in strengthening warm light; the close settled and warm.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. PAUL is a build-local lock (not in the global cast);
# its text is byte-identical to builds 138/155 so Paul is the same man library-
# wide.
LOCKS = {
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact and wiry, "
        "about fifty, balding with a fringe of dark hair, a full pointed dark "
        "beard, keen deep-set eyes, in a plain DARK RUST-BROWN travel robe "
        "(never cream, never white); a tentmaker's strong hands; earnest fire "
        "without anger."
    ),
    "EPHESIAN-DISCIPLES": (
        "EPHESIAN-DISCIPLES LOCK: the small group of about twelve disciples "
        "Paul found at Ephesus — first-century working men of varied ages, "
        "distinct real sun-browned faces, dark hair and beards of differing "
        "lengths, plain earth-toned wool of brown, rust, ochre, olive and grey "
        "(never cream — only Jesus wears cream); sincere, earnest, open faces; "
        "distinct individuals, never twinned, never a cloned face, never a "
        "uniform crowd."
    ),
    "EPHESUS-ROOM": (
        "EPHESUS-ROOM LOCK: the same plain meeting room in Ephesus in every "
        "frame — a modest first-century room of dressed pale stone and heavy "
        "timber ceiling beams, a low table, clay oil lamps, woven earth-toned "
        "hangings, a doorway opening to a stone street; steady warm lamplight "
        "with daylight from the doorway. The same room throughout — never a "
        "temple sanctuary, never a pagan idol niche, never modern glass or "
        "metal."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r166-b01", "out": "s01-paul-at-ephesus.jpeg", "seg": "n1",
        "window": "0.280-5.240", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES", "EPHESUS-ROOM"],
        "narration": (
            "Paul came through the inland country and arrived at Ephesus, where "
            "he found a small group of disciples."
        ),
        "must_show": "the ONE establishing wide — camera inside the Ephesus room a little behind and to the side of a small group of disciples, looking past their shoulders toward Paul just arrived in the doorway, road-dust on him; a real meeting room, a SMALL band, not a crowd.",
        "must_not_show": "not a large crowd — about a dozen men at most; no temple or idol; distinct faces, not a uniform crowd; no faces posed to the lens; no panel, border or text.",
        "scene": (
            "An arrival that finds a waiting few: the camera stands inside the "
            "plain Ephesus meeting room a little behind and to the side of a "
            "small group of disciples, looking past their shoulders toward Paul "
            "— compact, wiry, balding, dark-bearded, road-dust on his rust-brown "
            "robe — just come through the doorway from the stone street. The "
            "men's faces turn away from the lens toward him. Warm lamplight and "
            "daylight from the door; distinct sun-browned men of ordinary "
            "height, each with two hands and one head."
        ),
    },
    {
        "id": "v2-r166-b02", "out": "s02-they-were-sincere.jpeg", "seg": "n1",
        "window": "5.240-8.240", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": "They were sincere. They already believed.",
        "must_show": "a close on two or three of the disciples' faces — honest, earnest, plainly sincere believing men; the goodness of them is the subject.",
        "must_not_show": "not a crowd; distinct real faces, never twinned; no cream; no posing at the lens; no panel or text.",
        "scene": (
            "The goodness of them shown up close: two or three of the Ephesian "
            "disciples stand together, their weathered faces honest and earnest, "
            "eyes steady with real belief — plainly sincere men who already "
            "believe. Distinct sun-browned features, dark beards of differing "
            "lengths, plain earth-toned wool, warm lamplight; each has two hands "
            "and one head, none looking at the camera."
        ),
    },
    {
        "id": "v2-r166-b03", "out": "s03-fully-in.jpeg", "seg": "n1",
        "window": "8.240-12.856", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "By every outward sign they looked like people who were fully in."
        ),
        "must_show": "a two/three-shot of the disciples standing together settled and committed, the easy bearing of men who by every outward sign belong — nothing visibly wrong or lacking.",
        "must_not_show": "not a crowd; distinct faces; no cream; nothing to signal a problem yet; no panel or text.",
        "scene": (
            "Every outward sign in order: the small band of disciples stands "
            "together in the warm room, easy and settled among themselves, the "
            "unforced bearing of men who by every visible mark are fully in and "
            "belong — nothing about them yet showing what is missing. Distinct "
            "earth-toned men of ordinary height, warm lamplight, two hands and "
            "one head each."
        ),
    },
    {
        "id": "v2-r166-b04", "out": "s04-received-the-holy-ghost.jpeg", "seg": "s2",
        "window": "12.856-16.790", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "He said unto them, Have ye received the Holy Ghost since ye "
            "believed?"
        ),
        "must_show": "SCRIPTURE-EXACT, PAUL speaking — an over-shoulder two-shot past the disciples to Paul asking his searching question directly, keen and kind; the question live on his face.",
        "must_not_show": "not a crowd; Paul recognizable (compact, balding, dark-bearded, rust-brown robe); no cream; no panel or text.",
        "scene": (
            "The searching question, on the man asking it: shot over the "
            "disciples' shoulders to Paul, who leans in a little and puts it to "
            "them directly — keen deep-set eyes, earnest without edge — asking "
            "whether they have received the Holy Ghost since they believed. He "
            "is compact and wiry in his rust-brown robe, the lamplight warm on "
            "him; two hands and one head, the disciples' backs soft in the "
            "foreground."
        ),
    },
    {
        "id": "v2-r166-b05", "out": "s05-never-heard.jpeg", "seg": "s2",
        "window": "16.790-23.895", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "And they said unto him, We have not so much as heard whether there "
            "be any Holy Ghost."
        ),
        "must_show": "SCRIPTURE-EXACT — a close two-shot of the disciples answering, honest and a little at a loss, one with open hands and lifted brows — men who have not so much as heard of the Holy Ghost.",
        "must_not_show": "not a crowd; distinct honest faces; no cream; the look is candid puzzlement, not shame; no panel or text.",
        "scene": (
            "The startling answer, honest and unashamed: a close on two of the "
            "Ephesian disciples answering Paul, one with open hands and lifted "
            "brows, the other shaking his head slightly — plainly telling him "
            "they have not so much as heard whether there be any Holy Ghost. "
            "Their faces are candid and searching, not shamed. Distinct "
            "sun-browned features, earth-toned wool, warm lamplight, two hands "
            "and one head each."
        ),
    },
    {
        "id": "v2-r166-b06", "out": "s06-a-searching-question.jpeg", "seg": "n2",
        "window": "23.895-28.242", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES", "EPHESUS-ROOM"],
        "narration": (
            "But Paul asked them a searching question: And their answer was "
            "startling."
        ),
        "must_show": "a medium in the room — Paul reading their startling answer, his expression sharpening with understanding of what is missing, the disciples watching him; the pivot of the scene.",
        "must_not_show": "not a crowd; Paul recognizable; distinct disciple faces; no cream; no panel or text.",
        "scene": (
            "The moment he understands: a medium shot in the warm room, Paul "
            "taking in their startling answer, his keen face sharpening as he "
            "grasps exactly what these good men are missing, the disciples "
            "gathered watching him for what comes next. Paul compact and "
            "dark-bearded in rust-brown; distinct earth-toned disciples of "
            "ordinary height; warm lamplight, two hands and one head each."
        ),
    },
    {
        "id": "v2-r166-b07", "out": "s07-johns-baptism.jpeg", "seg": "s4",
        "window": "28.242-34.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "Then said Paul, John verily baptized with the baptism of "
            "repentance,"
        ),
        "must_show": "SCRIPTURE-EXACT, PAUL teaching — Paul explaining to the attentive disciples, one hand open in patient instruction, naming John's baptism of repentance; teaching, not rebuking.",
        "must_not_show": "not a crowd; Paul recognizable; no cream; no scroll text legible; no panel or text.",
        "scene": (
            "Paul begins to set it straight, gently: he stands among the "
            "attentive disciples with one hand open in patient explanation, his "
            "earnest face teaching rather than rebuking as he names the baptism "
            "of repentance that John gave. The men lean in to listen. Paul "
            "compact, balding, dark-bearded in rust-brown; distinct earth-toned "
            "disciples; warm lamplight, two hands and one head each."
        ),
    },
    {
        "id": "v2-r166-b08", "out": "s08-on-christ-jesus.jpeg", "seg": "s4",
        "window": "34.000-40.091", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "saying unto the people, that they should believe on him which "
            "should come after him, that is, on Christ Jesus."
        ),
        "must_show": "SCRIPTURE-EXACT — Paul pointing the disciples' attention forward, hand gesturing onward, drawing John's message to its point: believe on the one who came after, Christ Jesus; the disciples following his gesture.",
        "must_not_show": "Christ NOT embodied — no Jesus figure appears (he is named, not shown); not a crowd; Paul recognizable; no cream; no panel or text.",
        "scene": (
            "The message drawn to its point: Paul gestures onward with an open "
            "hand as he tells them John's baptism pointed the people forward — "
            "to believe on the one who should come after him, Christ Jesus — and "
            "the disciples' eyes follow the line of his gesture into the middle "
            "distance. No figure appears there; the Lord is named, not shown. "
            "Paul compact and dark-bearded in rust-brown; distinct earth-toned "
            "disciples; warm lamplight, two hands and one head each."
        ),
    },
    {
        "id": "v2-r166-b09", "out": "s09-what-baptism.jpeg", "seg": "n3",
        "window": "40.091-46.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "So Paul asked what baptism they had been given. They had known "
            "only the baptism of John —"
        ),
        "must_show": "a two-shot — Paul asking, and a disciple answering that they had known only John's baptism; the plain exchange that surfaces what they had received.",
        "must_not_show": "not a crowd; Paul and the disciples distinct; no cream; no panel or text.",
        "scene": (
            "The plain question and its plain answer: a two-shot of Paul turned "
            "to a disciple who answers him openly, telling that the only baptism "
            "they had ever known was John's. Paul listens, weighing it. Both are "
            "distinct and earnest — Paul compact and dark-bearded in rust-brown, "
            "the disciple a sun-browned working man in earth-toned wool — in warm "
            "lamplight, two hands and one head each."
        ),
    },
    {
        "id": "v2-r166-b10", "out": "s10-a-preparation.jpeg", "seg": "n3",
        "window": "46.500-53.042", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "a real and honest baptism of repentance, but a preparation, meant "
            "to point people forward to the one who was still to come."
        ),
        "must_show": "the disciples turned and looking the same way toward a doorway of open daylight ahead — their honest baptism a real preparation that pointed forward to the one still to come.",
        "must_not_show": "no figure in the doorway (the one to come is not shown); not a crowd; distinct faces; no cream; no panel or text.",
        "scene": (
            "Preparation drawn as looking-forward: the Ephesian disciples turn "
            "together toward the room's doorway where plain morning daylight "
            "opens onto the street, their faces lifted the same way — their "
            "baptism of repentance real and honest, but a preparation that "
            "pointed them forward to the one who was still to come. No figure "
            "stands in the light. Distinct earth-toned men of ordinary height, "
            "two hands and one head each."
        ),
    },
    {
        "id": "v2-r166-b11", "out": "s11-something-missing.jpeg", "seg": "n4",
        "window": "53.042-59.600", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "Here is the tender thing: these were good, believing people, and "
            "yet something was genuinely missing."
        ),
        "must_show": "a tender two-shot — Paul looking on these good believing men with real warmth and a trace of concern, one hand toward them; good people, and something honestly lacking.",
        "must_not_show": "no rebuke or coldness — tenderness; not a crowd; Paul recognizable; no cream; no panel or text.",
        "scene": (
            "Tenderness over a real lack: Paul looks on the small band of "
            "good, believing disciples with plain warmth and a trace of concern, "
            "one hand half-extended toward them — men whose sincerity is not in "
            "question and who are yet genuinely missing something. Their faces "
            "are open and trusting. Paul compact and dark-bearded in rust-brown; "
            "distinct earth-toned disciples; warm lamplight, two hands and one "
            "head each."
        ),
    },
    {
        "id": "v2-r166-b12", "out": "s12-not-the-full-ordinance.jpeg", "seg": "n4",
        "window": "59.600-65.270", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "Their baptism had prepared them, but it had not been the full "
            "ordinance done under the authority now given."
        ),
        "must_show": "a believer's face caught between what he has and what he lacks — settled from an honest baptism yet plainly waiting; the sense of a preparation not yet completed by the full ordinance.",
        "must_not_show": "no light or Spirit descending yet; distinct face; no cream; no panel or text.",
        "scene": (
            "A preparation, not yet a completion: a close on one Ephesian "
            "disciple, his face settled by an honest baptism and yet still "
            "waiting, eyes searching — a man prepared but not yet brought "
            "through the full ordinance done under the authority now given. The "
            "air around him is plain and ordinary; nothing has come to him yet. "
            "A distinct sun-browned face, earth-toned wool, warm lamplight, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r166-b13", "out": "s13-paul-set-it-right.jpeg", "seg": "n4",
        "window": "65.270-67.718", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL"],
        "narration": "So Paul set it right.",
        "must_show": "a close on Paul, decided — the earnest resolve of a man about to put the ordinance right; purpose fresh on his keen face.",
        "must_not_show": "no crowd this beat; Paul recognizable; no cream; no panel or text.",
        "scene": (
            "The turn to act: a close on Paul, his keen deep-set eyes settling "
            "into decision, the earnest fire in him turned now to purpose — a "
            "man about to put right what these good people were missing. Compact "
            "and dark-bearded in his rust-brown robe, warm lamplight plain on "
            "his face, two hands and one head."
        ),
    },
    {
        "id": "v2-r166-b14", "out": "s14-baptized-in-his-name.jpeg", "seg": "kv5",
        "window": "67.718-72.710", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "When they heard this, they were baptized in the name of the Lord "
            "Jesus."
        ),
        "must_show": "SCRIPTURE-EXACT — a disciple baptized at the water in bright morning: waist-deep, eyes closed, a baptizer's hands (only) lowering him; the proper baptism now given in the name of the Lord Jesus.",
        "must_not_show": "the baptizer shown only as hands/back, no locked face; no font or modern pool — a natural stone-lined pool or river; no light descending (this is the baptism, not yet the gift); no cream; no panel.",
        "scene": (
            "The right baptism given: outside at a stone-lined pool in bright "
            "morning, an Ephesian disciple stands waist-deep with head tipped "
            "back and eyes closed, while a baptizer — hands and turned shoulder "
            "only — lowers him at the moment of baptism, water running from his "
            "hair. Others wait at the water's edge. Real stone and water, warm "
            "daylight; the disciple a distinct ordinary man with two hands and "
            "one head, nothing yet coming down from above."
        ),
    },
    {
        "id": "v2-r166-b15", "out": "s15-not-the-final-step.jpeg", "seg": "n5",
        "window": "72.710-77.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": "And baptism was not the final step.",
        "must_show": "the newly-baptized disciple risen from the water, still and expectant, the plain air above him unchanged — baptism done, and yet a step still remaining.",
        "must_not_show": "no light or Spirit descending yet; distinct face; no cream; no panel or text.",
        "scene": (
            "Done, and yet not finished: the newly-baptized disciple has risen "
            "from the water and stands dripping at its edge, still and "
            "expectant, his face turned up — the baptism plainly complete, and "
            "yet the air above him ordinary and unchanged, one step still to "
            "come. A distinct sun-browned face, wet hair, earth-toned wool, warm "
            "daylight, two hands and one head; nothing descends."
        ),
    },
    {
        "id": "v2-r166-b16", "out": "s16-one-thing-more.jpeg", "seg": "n5",
        "window": "77.500-83.274", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "There was one thing more, the same step we have seen before: the "
            "laying on of hands by one who held the authority to give the gift."
        ),
        "must_show": "a two-shot — Paul stepping to a kneeling disciple, hands beginning to rise toward his bowed head — the one remaining step, the laying on of hands by one with authority, about to happen.",
        "must_not_show": "hands not laid yet this beat; no light descending; Paul recognizable; distinct kneeling disciple; no cream; no panel or text.",
        "scene": (
            "The remaining step, begun: Paul steps in close to a kneeling "
            "Ephesian disciple, his strong tentmaker's hands beginning to lift "
            "toward the man's bowed head — the one thing more, the laying on of "
            "hands by one who holds the authority to give the gift. The disciple "
            "kneels with eyes closing, expectant. Paul compact and dark-bearded "
            "in rust-brown; both distinct, two hands and one head each, warm "
            "light, nothing yet coming down."
        ),
    },
    {
        "id": "v2-r166-b17", "out": "s17-the-holy-ghost-came.jpeg", "seg": "kv6",
        "window": "83.274-87.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "And when Paul had laid his hands upon them, the Holy Ghost came "
            "on them;"
        ),
        "must_show": "SCRIPTURE-EXACT — Paul's hands laid firmly on a kneeling disciple's bowed head as warm light comes down from above the top of the frame onto the man's lifting, joy-struck face; the gift coming under the laid-on hands.",
        "must_not_show": "the Holy Ghost NEVER embodied — no dove, no figure, NO tongues of flame; ONLY warm light from above the frame edge; no light ringing the head; Paul recognizable; no cream; no panel.",
        "scene": (
            "The gift comes under the hands: Paul's strong hands are laid firmly "
            "on the bowed head of a kneeling Ephesian disciple, and warm light "
            "comes down onto the man's lifting face from above the top of the "
            "frame as joy and awe break across it — the Holy Ghost come on them "
            "at the laying on of hands. The light stays at the upper edge and "
            "becomes no dove, flame or figure. Paul compact and dark-bearded in "
            "rust-brown; a distinct radiant disciple face, two hands and one "
            "head each."
        ),
    },
    {
        "id": "v2-r166-b18", "out": "s18-tongues-and-prophesied.jpeg", "seg": "kv6",
        "window": "87.500-91.566", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": "and they spake with tongues, and prophesied.",
        "must_show": "SCRIPTURE-EXACT — the filled disciples' OWN response: mouths open in fervent praise, one man's hand lifted in prophecy, faces alight with joy; the tongues and prophesying shown as the men speaking, warm light resting from above.",
        "must_not_show": "the tongues are NOT flames — no fire, no flame over any head; no dove, no figure; the Spirit is warm light from above only; distinct faces; no cream; no panel or text.",
        "scene": (
            "The gift overflowing in the men themselves: the newly-filled "
            "Ephesian disciples are caught mid-response — mouths open in fervent "
            "praise, one man's hand lifted and face turned up in prophecy, "
            "another with eyes shut and arms opening — speaking with tongues and "
            "prophesying, warm light resting down over them from above the top "
            "of the frame. The tongues are their speech, not fire; nothing "
            "burns over their heads and no figure appears. Distinct sun-browned "
            "faces, earth-toned wool, two hands and one head each."
        ),
    },
    {
        "id": "v2-r166-b19", "out": "s19-the-study-gem.jpeg", "seg": "n6",
        "window": "91.566-96.500", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Here is the quiet study gem. Their sincerity was never in doubt, "
            "and it was never enough on its own."
        ),
        "must_show": "a quiet study insert — an open first-century scroll of the book of Acts lit by a small clay oil lamp, a reader's hand resting on the lines; the turn to careful reading of what happened.",
        "must_not_show": "no modern book, paper or print; NO legible modern letters or numbers on the scroll; warm lamp light, nothing ringing anything; no panel, border or text overlay.",
        "scene": (
            "The turn to close reading: an insert looking down at an open "
            "first-century papyrus scroll on a plain wooden table, a small clay "
            "oil lamp beside it laying warm low light across the lines, a "
            "reader's weathered hand resting quietly on the words as if pausing "
            "on something just weighed. The room is still and dim around the "
            "lamp. The scroll bears only plain ancient ink strokes, nothing "
            "legible or modern; the hand is whole with five fingers."
        ),
    },
    {
        "id": "v2-r166-b20", "out": "s20-done-right-by-one-sent.jpeg", "seg": "n6",
        "window": "96.500-101.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES"],
        "narration": (
            "The ordinance still had to be done right, by one who was sent."
        ),
        "must_show": "a clean two-shot reprise — Paul's authoritative laid-on hands on a disciple's head — stating plainly that the ordinance had to be done right, by one who was sent.",
        "must_not_show": "no dove, flame or figure; warm light from above only if any; ordinary hands, five fingers; Paul recognizable; no cream; no panel.",
        "scene": (
            "Authority restated cleanly: a close two-shot of Paul's strong, "
            "authoritative hands laid on a kneeling disciple's head, the "
            "disciple calm beneath them — the ordinance done right, by one who "
            "was sent to do it. Paul compact and dark-bearded in rust-brown; a "
            "distinct disciple face; warm light, real hands whole with five "
            "fingers, two hands and one head each."
        ),
    },
    {
        "id": "v2-r166-b21", "out": "s21-completed-by-authority.jpeg", "seg": "n6",
        "window": "101.000-105.817", "wide": False, "jesus": False, "ref": False,
        "locks": ["PAUL", "EPHESIAN-DISCIPLES", "EPHESUS-ROOM"],
        "narration": (
            "Sincerity did not replace authority — it was completed by it."
        ),
        "must_show": "a settled two/three-shot — Paul standing with the newly-filled disciples around him, hands still near shoulders, every face glad and settled — sincerity and authority held together, one completing the other.",
        "must_not_show": "not a crowd; no Spirit embodied; Paul recognizable; distinct disciple faces; no cream; no panel or text.",
        "scene": (
            "Sincerity and authority resting together: Paul stands among the "
            "newly-filled Ephesian disciples in the warm room, a hand still near "
            "a disciple's shoulder, every face glad and settled — the sincerity "
            "that was never in doubt now completed by the authority that carried "
            "the gift. Paul compact and dark-bearded in rust-brown; distinct "
            "earth-toned disciples of ordinary height, warm lamplight, two hands "
            "and one head each."
        ),
    },
    {
        "id": "v2-r166-b22", "out": "s22-the-same-pattern.jpeg", "seg": "n7",
        "window": "105.817-111.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "And the same careful pattern is offered to you: not a vague good "
            "feeling, but a real baptism by proper authority,"
        ),
        "must_show": "a single believer — the viewer's stand-in — at the water's edge, damp from a real baptism, upturned and ready; the pattern offered now to the one watching, a real baptism, not a vague feeling.",
        "must_not_show": "no Spirit descending yet in this beat; distinct open face; no cream; no panel or text.",
        "scene": (
            "The pattern turned toward the viewer: a single believer stands at "
            "the water's edge, hair and shoulders damp from a real baptism, his "
            "face upturned and ready — the viewer's own place in the story, "
            "offered not a vague good feeling but a real baptism by proper "
            "authority. His face is honest and settled in warm morning light; a "
            "distinct ordinary man with two hands and one head, the air above "
            "still plain."
        ),
    },
    {
        "id": "v2-r166-b23", "out": "s23-gift-by-laying-on-hands.jpeg", "seg": "n7",
        "window": "111.000-117.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "and then the gift of the Spirit by the laying on of hands."
        ),
        "must_show": "the same believer now kneeling under authoritative laid-on hands with warm light resting from above onto his peaceful face — the gift of the Spirit given by the laying on of hands, completing the pattern for the viewer.",
        "must_not_show": "the Spirit NEVER a dove, flame or figure — warm light from above only; ordinary hands, five fingers; no cream; no light ringing the head; no panel.",
        "scene": (
            "The pattern completed on the viewer's stand-in: the believer kneels "
            "under a pair of authoritative laid-on hands, and warm light rests "
            "down onto his peaceful, lifted face from above the top of the frame "
            "— the gift of the Spirit given, as it always was, by the laying on "
            "of hands. The light stays at the upper edge and becomes no dove, "
            "flame or figure. A distinct calm face, earth-toned wool, whole "
            "hands, one head."
        ),
    },
    {
        "id": "v2-r166-b24", "out": "s24-will-you-follow-it-in.jpeg", "seg": "n7",
        "window": "117.000-121.218", "wide": False, "jesus": False, "ref": False,
        "locks": ["EPHESIAN-DISCIPLES"],
        "narration": (
            "When that pattern is offered to you, will you follow it in?"
        ),
        "must_show": "the closing invitation — a close on the believer's open, upturned face and slightly opened hands in warm light, the question left hopeful and unhurried: will you follow it in?",
        "must_not_show": "no grasping or clenched hands — open and receiving; no dove, flame or figure; no light ringing the head; no cream; no panel or text.",
        "scene": (
            "The film hands the question across: a close on the believer's open, "
            "upturned face and hands loosening at his sides as if ready to "
            "follow the pattern all the way in, warm light gentle on him — the "
            "same careful pattern offered, the question left hopeful and "
            "unhurried. Nothing is grasped; the hands are open. A distinct "
            "ordinary face, earth-toned wool, two whole hands and one head, no "
            "figure and nothing ringing his head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# EMPTY BY DESIGN. EPHESUS-ROOM is a NEW recurring place with no stash match, so
# there is no plate to wire at author time. The runner promotes it from this
# build's first good frame — b01 (or the calmer b06) — then generates the rest
# of the room beats with the plate attached. No beat in this row bears Jesus, so
# any frame is safe to promote. Full steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
