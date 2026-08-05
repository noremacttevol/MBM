#!/usr/bin/env python3
"""V2 beat map — row 103, build-103-peters-confession (Matthew 16:13-18).

COVERAGE: 20 pictures over 115.4 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 16:13-18 KJV):
  v13   "when Jesus came into the coasts of CAESAREA PHILIPPI" — far
        north, under the great pale rock cliff with its springs; away
        from the crowds; "WHOM DO MEN SAY that I the Son of man am?"
  v14   the survey: "John the Baptist: some, Elias; and others,
        Jeremias, or one of the prophets."
  v15   the turn: "But WHOM SAY YE that I am?"
  v16   "Simon Peter answered... THOU ART THE CHRIST, THE SON OF THE
        LIVING GOD."
  v17   "BLESSED art thou, Simon Barjona: for FLESH AND BLOOD hath
        not revealed it unto thee, but MY FATHER which is in heaven."
  v18   "thou art PETER, and upon THIS ROCK I will build MY CHURCH;
        and the GATES OF HELL shall not prevail against it." — spoken
        under a literal cliff of rock.

CONTENT-CARE: no flags. NO hell imagery anywhere (v18 is words only —
the permanence is carried by the cliff's mass, never by fire or
gates); the pagan grotto of the site is not depicted.

TIME OF DAY: one clear bright northern afternoon throughout — green
spring-fed glade under the pale cliff, clean high light.

CHANGING CONDITION (kept OUT of the locks): the question — public
survey, then personal point-blank; Peter — listening, then standing
alone in his answer, then blessed and renamed.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER, ANDREW, JOHN and JAMES-Z come from CAST_LOCKS.
LOCKS = {
    "CLIFF": (
        "CLIFF LOCK: the Caesarea Philippi glade — a GREAT PALE ROCK "
        "CLIFF rising sheer above a green spring-fed hollow: clear "
        "water breaking from the rock's base, poplars and grass, "
        "cool shade at the cliff foot, clean northern light. The "
        "same cliff, springs and glade throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r103-b01", "out": "s01-jesus-had-brought-his-disciples.jpeg", "seg": "n1",
        "window": "0.28-8.16", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN", "ANDREW"],
        "narration": (
            "Jesus had brought his disciples a long way north, to a quiet "
            "place far from the crowds, up under a great cliff of pale rock."
        ),
        "must_show": "SCRIPTURE-EXACT: the setting — the small company arriving in the green glade beneath the towering pale cliff, springs breaking from its base; quiet, remote, deliberate.",
        "must_not_show": "no halo, glare or rim-light; NO crowds — the twelve and their teacher alone with the rock.",
        "scene": (
            "Far north of every crowd, the camera at the glade's "
            "edge taking arrival and cliff from the side, the "
            "little company comes into the "
            "quiet: a green hollow under a "
            "great pale cliff that goes up "
            "sheer into the northern "
            "light, spring water breaking "
            "cold from the rock's base "
            "and threading away through "
            "the grass — Jesus leading "
            "them in under the stone's "
            "cool shadow with the "
            "unhurried purpose of a man "
            "who chose this classroom "
            "years ago, for this exact "
            "lesson. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r103-b02", "out": "s02-and-there-he-asked-them.jpeg", "seg": "n1",
        "window": "8.16-12.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF"],
        "narration": (
            "And there he asked them a question he had never asked so "
            "plainly before."
        ),
        "must_show": "the question gathering — close on Jesus settling to face the ring, something new and deliberate in his manner; a threshold about to be crossed.",
        "must_not_show": "no halo, glare or rim-light; the newness FELT — a teacher about to ask the real one.",
        "scene": (
            "Close on the moment the "
            "lessons change register: "
            "Jesus turning from the "
            "spring to face them all, "
            "settling onto a low stone "
            "with a deliberateness they "
            "have learned to read — "
            "the warm eyes moving man to "
            "man around the ring, "
            "gathering their attention "
            "the way you gather kindling "
            "— three years of parables "
            "and roads narrowing toward "
            "one plain question he has "
            "never yet asked out loud. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r103-b03", "out": "s03-whom-do-men-say-that.jpeg", "seg": "jv13",
        "window": "12.95-15.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN"],
        "narration": "Whom do men say that I the Son of man am?",
        "must_show": "SCRIPTURE-EXACT: the survey question — Jesus asking it easily to the seated ring in the glade; an opening question, wide and safe.",
        "must_not_show": "no halo, glare or rim-light; the ease REAL — the hard question still hidden behind this one.",
        "scene": (
            "The first question goes out "
            "easy as skipped stone: WHOM "
            "DO MEN SAY THAT I AM — "
            "asked with a half-smile "
            "around the seated ring in "
            "the glade's green light, "
            "the kind of question that "
            "costs nobody anything — "
            "market gossip, road talk, "
            "other people's opinions — "
            "and the ring relaxes into "
            "it comfortably, no one yet "
            "hearing the second question "
            "crouched behind the first. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r103-b04", "out": "s04-it-was-an-easy-question.jpeg", "seg": "n2",
        "window": "17.18-20.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "ANDREW"],
        "narration": "It was an easy question at first. What are people saying?",
        "must_show": "the ease — disciples leaning in comfortably, hands already rising to answer; the pleasure of reporting what OTHERS think.",
        "must_not_show": "no halo, glare or rim-light; the comfort VISIBLE — no stakes yet on any face.",
        "scene": (
            "The ring warms to the easy "
            "work: Andrew's hand already "
            "up with a report, Peter "
            "leaning back on his elbows "
            "with a fisherman's grin, "
            "two others trading what "
            "they heard in the last "
            "village — the simple "
            "pleasure of being asked "
            "what OTHER people think, "
            "everyone an expert, nobody "
            "on the hook, the safest "
            "conversation the twelve "
            "have had in weeks. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r103-b05", "out": "s05-some-say-that-thou-art.jpeg", "seg": "s14",
        "window": "23.28-30.06", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN", "ANDREW"],
        "narration": (
            "Some say that thou art John the Baptist: some, Elias; and "
            "others, Jeremias, or one of the prophets."
        ),
        "must_show": "SCRIPTURE-EXACT: the answers offered — the ring animated with the reporting: fingers counting the names, voices overlapping; Jesus listening quietly at the centre.",
        "must_not_show": "no halo, glare or rim-light; the reports EAGER — a market of borrowed opinions, cheerfully traded.",
        "scene": (
            "The answers tumble in from "
            "every side: JOHN THE "
            "BAPTIST, counted off on one "
            "man's fingers — ELIAS, "
            "insists another, leaning "
            "in — JEREMIAS, or one of "
            "the old prophets, offers a "
            "third with a shrug — the "
            "glade cheerful with the "
            "traffic of secondhand "
            "opinion while Jesus sits "
            "quiet at the centre of it, "
            "listening to a nation "
            "guess respectfully around "
            "the truth without once "
            "landing on it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r103-b06", "out": "s06-some-say-elijah-come-back.jpeg", "seg": "n3",
        "window": "31.50-33.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["ANDREW"],
        "narration": "Some say Elijah come back.",
        "must_show": "one report close — a disciple mid-report, earnest: the Elijah theory offered with its weight; borrowed conviction on a friendly face.",
        "must_not_show": "no halo, glare or rim-light; the offering EARNEST — the theory respectable and sincerely relayed.",
        "scene": (
            "Close on one report given "
            "its full weight: Andrew's "
            "earnest face relaying the "
            "Elijah theory — the fire-"
            "caller come back, the "
            "chariot-taken prophet "
            "returned — offered "
            "seriously, as serious "
            "people say it in serious "
            "places, his hands shaping "
            "the bigness of the claim — "
            "the highest compliment the "
            "market knows how to pay, "
            "and still a category short. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r103-b07", "out": "s07-others-jeremiah-or-one-of.jpeg", "seg": "n3",
        "window": "33.16-38.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN"],
        "narration": (
            "Others, Jeremiah, or one of the old prophets. All respectful. "
            "All safe."
        ),
        "must_show": "the safety of the list — the ring at ease with its respectable catalogue, Jesus's listening face carrying the one thing the list lacks: none of them said it.",
        "must_not_show": "no halo, glare or rim-light; his listening UNREADABLE-patient — the gap in the answers his alone to see.",
        "scene": (
            "The catalogue completes "
            "itself and hangs there: "
            "prophet, forerunner, "
            "greatest-of-the-old — every "
            "answer respectful, every "
            "answer safe, every answer "
            "somebody else's — and at "
            "the ring's centre Jesus "
            "listens with a patience "
            "that gives nothing away, "
            "the one person in the "
            "glade who can hear what "
            "the whole respectful list "
            "is carefully walking "
            "around. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r103-b08", "out": "s08-all-what-other-people-thought.jpeg", "seg": "n3 + jv15",
        "window": "38.94-44.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN", "ANDREW"],
        "narration": (
            "All second-hand — what other people thought. But whom say ye "
            "that I am?"
        ),
        "must_show": "SCRIPTURE-EXACT: the turn — Jesus leaning forward, the question changing aim: BUT WHOM SAY YE; the ring's ease dying mid-breath.",
        "must_not_show": "no halo, glare or rim-light; the pivot PHYSICAL — his lean, their stillness; the safety gone from the air.",
        "scene": (
            "And then the question turns "
            "its head: Jesus leaning "
            "forward off his stone, the "
            "half-smile folding away, "
            "the warm eyes suddenly "
            "point-blank — BUT WHOM SAY "
            "YE THAT I AM — and the "
            "glade's comfortable air "
            "goes out like a snuffed "
            "lamp: hands stopping "
            "mid-gesture, the easy "
            "reporting dead in every "
            "throat, twelve men "
            "discovering at once that "
            "the first question was "
            "only the door held open "
            "for this one. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r103-b09", "out": "s09-and-there-it-was-not.jpeg", "seg": "n4",
        "window": "46.05-50.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF"],
        "narration": (
            "And there it was. Not what have you heard. Not what is the "
            "crowd saying."
        ),
        "must_show": "the question bared — close on Jesus's direct waiting face: the personal question standing naked between him and them; no crowd to hide in.",
        "must_not_show": "no halo, glare or rim-light; the directness TOTAL — eyes that will not be deflected to a third party.",
        "scene": (
            "Close on the face that will "
            "not accept a forwarded "
            "answer: the warm brown eyes "
            "steady and utterly direct, "
            "waiting — not for the "
            "crowd's verdict, not for "
            "the market's consensus, "
            "not for one more prophet "
            "off one more respectable "
            "list — the question bared "
            "down to its live wire and "
            "held out, person to "
            "person, with nowhere in "
            "the whole green glade to "
            "hide from it. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r103-b10", "out": "s10-but-you-who-do-you.jpeg", "seg": "n4",
        "window": "50.87-58.96", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN", "ANDREW"],
        "narration": (
            "But you — who do you say that I am? The question stopped them "
            "cold. This one you cannot borrow from anybody else."
        ),
        "must_show": "the stopped ring — the whole company frozen under the cliff: eyes down, eyes sideways, nobody volunteering; the unborrowable question doing its work.",
        "must_not_show": "no halo, glare or rim-light; the silence LONG — every posture avoiding the answer's cost.",
        "scene": (
            "The silence under the cliff, the camera outside the "
            "ring behind the frozen shoulders, "
            "gets long: eyes finding the "
            "grass, the springs, the "
            "pale rock — anywhere but "
            "the asking face — Andrew's "
            "report-ready hands gone "
            "still in his lap, John "
            "glancing at Peter, Peter "
            "staring at the water with "
            "his jaw working — twelve "
            "men discovering the one "
            "question in the world that "
            "cannot be answered with "
            "anyone else's opinion, and "
            "feeling it wait. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r103-b11", "out": "s11-and-simon-peter-answered-him.jpeg", "seg": "np + sp16",
        "window": "59.54-64.54", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN", "ANDREW"],
        "narration": (
            "And Simon Peter answered him. Thou art the Christ, the Son of "
            "the living God."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — Peter on his feet, the answer out of him full-voice: THE CHRIST, THE SON OF THE LIVING GOD; the ring stunned around his standing figure.",
        "must_not_show": "no halo, glare or rim-light; Peter STANDING ALONE in the saying — the others still seated, the risk all his.",
        "scene": (
            "And Peter stands up into "
            "it: the big fisherman on "
            "his feet under the pale "
            "cliff with the answer "
            "coming out of him full "
            "voice and unhedged — THOU "
            "ART THE CHRIST, THE SON OF "
            "THE LIVING GOD — the words "
            "too large for the glade "
            "and said anyway, while the "
            "seated ring stares up at "
            "him and the springs keep "
            "running and the thing "
            "eleven men half-dared to "
            "hope stands spoken in the "
            "open air at last. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r103-b12", "out": "s12-not-a-prophet-not-a.jpeg", "seg": "n5",
        "window": "66.12-68.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Not a prophet. Not a teacher.",
        "must_show": "the category broken — close on Peter's face holding the claim: the leap past every safe title visible in the blazing certainty.",
        "must_not_show": "no halo, glare or rim-light; the certainty COSTLY — a man aware of the size of what he just said.",
        "scene": (
            "Close on the face that just "
            "broke the catalogue: "
            "Peter's blazing certainty "
            "with the fear still wet "
            "underneath it — the safe "
            "titles all left burning "
            "behind him, prophet and "
            "teacher and Elijah-come-"
            "back abandoned in one "
            "leap — a man standing in "
            "the open on the far side "
            "of the biggest sentence of "
            "his life, aware of exactly "
            "how far past safety he "
            "just jumped, and not "
            "taking one word back. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r103-b13", "out": "s13-peter-said-out-loud-the.jpeg", "seg": "n5",
        "window": "68.23-72.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "JOHN", "ANDREW"],
        "narration": (
            "Peter said out loud the thing the others had only half-dared "
            "to hope."
        ),
        "must_show": "the half-hopes surfacing — the seated faces around standing Peter: recognition dawning that he said THEIR secret; relief and awe mixing.",
        "must_not_show": "no halo, glare or rim-light; the faces CONFESSING silently — yes, that; what we didn't dare.",
        "scene": (
            "Around the standing "
            "fisherman the seated faces "
            "give themselves away: "
            "John's young features "
            "flooding with a relief "
            "that looks like tears "
            "coming, Andrew nodding "
            "before he knows he is "
            "nodding, another's hand "
            "over his mouth — eleven "
            "private half-hopes hearing "
            "themselves said out loud "
            "at last by the one throat "
            "reckless enough — the "
            "secret of the whole "
            "company, standing in the "
            "open wearing Peter's "
            "voice. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r103-b14", "out": "s14-blessed-art-thou-simon-barjona.jpeg", "seg": "jv17",
        "window": "72.73-81.18", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER"],
        "narration": (
            "Blessed art thou, Simon Barjona: for flesh and blood hath not "
            "revealed it unto thee, but my Father which is in heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the blessing — Jesus risen, hands on Peter's shoulders, face alight: BLESSED ART THOU; the answer received with joy under the great rock.",
        "must_not_show": "no halo, glare or rim-light; Jesus's JOY the register — the gladdest his face has been in the row.",
        "scene": (
            "Jesus comes off his stone "
            "with his face alight: both "
            "hands landing strong on the "
            "fisherman's shoulders — "
            "BLESSED ART THOU, SIMON "
            "BARJONA — the gladdest "
            "words of the northern "
            "journey ringing off the "
            "pale cliff — and the "
            "source named in the same "
            "breath: not flesh and "
            "blood, not cleverness, not "
            "the market's list, but MY "
            "FATHER — a heart's answer "
            "traced home to heaven in "
            "front of everyone. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r103-b15", "out": "s15-you-did-not-work-this.jpeg", "seg": "n6",
        "window": "82.70-85.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": "You did not work this out on your own, Jesus told him.",
        "must_show": "the source named — close on the two faces: Jesus's gladness, Peter's dawning wonder at where his own answer came from.",
        "must_not_show": "no halo, glare or rim-light; Peter's wonder HUMBLE — a man surprised by his own mouth.",
        "scene": (
            "Close on a man being told "
            "the provenance of his own "
            "sentence: Peter's face "
            "under the blessing going "
            "from triumph to wonder as "
            "the words land — not "
            "worked out, not reasoned "
            "to, not his — the big "
            "fisherman looking faintly "
            "backward at his own answer "
            "like a man shown the "
            "watermark in a page he "
            "wrote, humbled by the "
            "discovery of whose ink it "
            "was. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r103-b16", "out": "s16-this-kind-of-knowing-does.jpeg", "seg": "n6",
        "window": "85.38-92.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN"],
        "narration": (
            "This kind of knowing does not come from clever thinking. It is "
            "given, quietly, from God, to a heart ready to receive it."
        ),
        "must_show": "the gift explained — the glade's quiet around teacher and ring: springs running from the rock as the visual echo of given-not-earned knowing.",
        "must_not_show": "no halo, glare or rim-light; the springs the METAPHOR — water given from rock, unworked-for.",
        "scene": (
            "The glade itself preaches "
            "the point: at the cliff's "
            "base the springs break "
            "cold and endless from "
            "solid rock — water no man "
            "dug for, rising given from "
            "stone — while Jesus's "
            "words move over the quiet "
            "ring: this kind of knowing "
            "arrives the same way, "
            "unearned, unengineered, "
            "welling up in a heart "
            "that is simply ready — "
            "revelation running like "
            "spring water, free to "
            "whoever kneels. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r103-b17", "out": "s17-and-they-had-plenty-of.jpeg", "seg": "n2",
        "window": "20.27-22.71", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "ANDREW", "JOHN"],
        "narration": "And they had plenty of answers ready.",
        "must_show": "the eager inventory — disciples' animated faces mid-recall, fingers rising with reports to give; the easy question's harvest.",
        "must_not_show": "no halo, glare or rim-light; the eagerness LIGHT — opinion-trading at its most comfortable.",
        "scene": (
            "Close on the comfortable "
            "plenty: fingers rising "
            "around the ring with "
            "reports queued behind them, "
            "Andrew half-standing with "
            "his first name ready, two "
            "men comparing village "
            "rumors in a hurry to get "
            "theirs in — the cheerful "
            "abundance of answers that "
            "cost nothing, everyone "
            "rich in other people's "
            "opinions, the easy "
            "question's harvest coming "
            "in from every side at "
            "once. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r103-b18", "out": "s18-and-i-say-also-unto.jpeg", "seg": "jv18",
        "window": "93.24-102.94", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER"],
        "narration": (
            "And I say also unto thee, That thou art Peter, and upon this "
            "rock I will build my church; and the gates of hell shall not "
            "prevail against it."
        ),
        "must_show": "SCRIPTURE-EXACT: the renaming under the rock — Jesus's hand on Peter, his other arm taking in the great cliff: THOU ART PETER — THIS ROCK — the sermon and its object in one frame.",
        "must_not_show": "ABSOLUTE: no hell imagery, no gates, no fire — the permanence carried entirely by the cliff's mass; no halo.",
        "scene": (
            "The renaming happens, the camera at the side so hand, "
            "man and cliff line up in one profile, under "
            "its own illustration: "
            "Jesus's hand firm on the "
            "fisherman's shoulder — "
            "THOU ART PETER — and his "
            "other arm sweeping up the "
            "whole towering face of "
            "pale stone above them — "
            "UPON THIS ROCK I WILL "
            "BUILD — the words backed "
            "by a million tons of "
            "cliff that no siege in "
            "history has moved an "
            "inch — a church founded in "
            "a glade, on a confession, "
            "against which nothing "
            "downward shall ever "
            "prevail. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r103-b19", "out": "s19-on-this-on-knowing-who.jpeg", "seg": "n7",
        "window": "104.43-110.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["CLIFF"],
        "narration": (
            "On this — on knowing who he really is — he would build "
            "something that hell itself could never tear down."
        ),
        "must_show": "the foundation itself — the great cliff face filling the frame in full light: mass, permanence, unshakeable footing; the church's foundation as pure rock.",
        "must_not_show": "ABSOLUTE: no hell imagery of any kind — the frame is ROCK and light only.",
        "scene": (
            "The frame gives the whole "
            "sermon to the stone: the "
            "great pale cliff filling "
            "it edge to edge in the "
            "clean northern light — "
            "buttress over buttress of "
            "living rock going up out "
            "of frame, seams older "
            "than nations, the spring "
            "still running undiminished "
            "at its foot — footing that "
            "has shrugged off every "
            "storm, siege and century "
            "thrown at it — the kind of "
            "thing you build on when "
            "you intend the building "
            "to outlast the world. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r103-b20", "out": "s20-everything-else-in-the-gospel.jpeg", "seg": "n7",
        "window": "110.94-115.06", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CLIFF", "PETER", "JOHN", "ANDREW"],
        "narration": "Everything else in the gospel is built on top of this one answer.",
        "must_show": "the closing image — the company small at the great cliff's foot in the late clean light, Jesus and Peter at their centre; the confession and its rock, resting together.",
        "must_not_show": "no halo, glare or rim-light; the SCALE the meaning — small men, one answer, immovable stone.",
        "scene": (
            "The closing frame, the camera far off behind the "
            "small company toward the great face, steps "
            "back and lets the scale "
            "speak: the little company "
            "small at the foot of the "
            "enormous pale cliff, Jesus "
            "and the newly named Peter "
            "at their centre in the "
            "late clean light, the "
            "springs running on — one "
            "answer spoken in a green "
            "hollow, and everything "
            "that will ever be called "
            "the gospel stacked, storey "
            "on storey and century on "
            "century, on top of it. "
            "Every figure has two arms, "
            "two hands and one head."
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
