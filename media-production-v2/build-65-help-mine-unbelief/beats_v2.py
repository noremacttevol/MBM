#!/usr/bin/env python3
"""V2 beat map — row 65, build-65-help-mine-unbelief (Mark 9:14-29).

COVERAGE: 36 pictures over 207.7 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 9:14-29 KJV):
  v14-15 Jesus comes DOWN FROM THE MOUNTAIN (the transfiguration's morrow)
        into an arguing crowd — the disciples cornered by scribes, a
        public failure in progress.
  v17-18 the father's account: a son "which hath a DUMB SPIRIT" tormented
        since childhood.
        ⚑ Flags A,R (CONTENT-CARE §3 row 65): NO EMBODIED SPIRIT is ever
        painted — no creature, no shadow-being, no distortion; the
        affliction exists only in its effects and the family's telling.
        SELF-HARM / seizure-harm is NEVER depicted mid-act: the boy's
        suffering is shown as the father HOLDING him safe, the family's
        watchful arrangements (the screened hearth, the avoided well),
        and the boy's spent, held aftermath. Before/after DIGNITY is
        absolute — the boy is a person throughout, never a spectacle.
  v22   "IF thou canst do any thing, have compassion on us, and help US"
        — the plural 'us': the whole family is the patient.
  v23-24 "IF thou canst believe ... Lord, I BELIEVE; HELP THOU MINE
        UNBELIEF" — the row's summit: honest, cracked faith offered
        whole; the father's face is the story's centre.
  v25-27 the command ("enter NO MORE into him"), the stillness "as one
        dead" (painted as held quiet, the crowd's whisper), and the HAND:
        "Jesus took him by the hand, and LIFTED HIM UP" — the row's
        tenderest beat.
  v28-29 in the house: "this kind ... by nothing, but by PRAYER and
        FASTING" — dependence, not technique.

TIME OF DAY: one day — bright late morning at the hill's foot for the
argument and the healing, warm afternoon for the restoration, lamplit
evening in the house for the disciples' question. The mountain stands
in the background of the early beats.

CHANGING CONDITION (kept OUT of the locks): the boy's state — guarded,
spent-and-held, still-as-dead, LIFTED, restored and standing; and the
father's face — worn hope, honest crack, amazed joy. All per-beat.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "FATHER": (
        "FATHER LOCK: the father is the same man in every shot — about "
        "forty-five, big-framed and worn thin by years of vigilance, "
        "with a dark beard early-greyed at the chin, bruised-tired eyes "
        "and gentle enormous hands. He wears a DARK PEAT-BROWN tunic "
        "with a patched DEEP OLIVE mantle (never cream, never white). "
        "His face is shown clearly — love and exhaustion sharing every "
        "line."
    ),
    "BOY": (
        "BOY LOCK: the son is the same boy in every shot — about twelve, "
        "thin and pale, with his father's dark hair, large quiet eyes "
        "and a stillness that is watchful rather than empty. He wears a "
        "small DUSTY INDIGO tunic (never cream, never white). His face "
        "is shown clearly and with complete dignity in every state — a "
        "person always, a spectacle never."
    ),
    "SCRIBES": (
        "SCRIBES LOCK: the arguing scribes are the same three men in "
        "every shot — fine NEAR-BLACK INDIGO robes, fringed shawls, "
        "confident forensic faces (never cream, never white). Faces "
        "shown clearly — debaters scoring points, not monsters."
    ),
    "HILLFOOT": (
        "HILL FOOT LOCK: the open ground at the mountain's foot — a "
        "stony meadow where paths meet, scattered boulders, a spring "
        "trough, and the great grey mountain rising steep behind with "
        "cloud still on its shoulder. The crowd here wears SATURATED "
        "DEEP earth colours (never cream, never white; only Jesus "
        "wears cream). Faces shown clearly."
    ),
    "HOUSE": (
        "EVENING HOUSE LOCK: a plain rented room at day's end — rush "
        "mats, a low table with bread and a lamp, packs against the "
        "wall, one small window going blue with dusk. The same room "
        "for the disciples' question."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r065-b01", "out": "s01-jesus-came-down-from-the.jpeg", "seg": "n0",
        "window": "0.28-5.03", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLFOOT"],
        "narration": (
            "Jesus came down from the mountain and walked straight into a mess. "
            "A crowd was arguing."
        ),
        "must_show": "SCRIPTURE-EXACT: the descent into the argument — Jesus coming down the last of the mountain path toward a knotted, gesturing crowd at the hill's foot; calm walking into noise.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the mountain's grey shoulder behind him; the crowd's agitation legible at distance.",
        "scene": (
            "Down the last turns of the stony mountain path, the "
            "camera on the slope's side taking the descent in "
            "profile toward the arguing knot below, "
            "path Jesus descends into the bright late "
            "morning — and below him at the hill's foot "
            "the mess is visible from fifty paces: a "
            "knotted crowd around the spring trough, "
            "arms gesturing over heads, the particular "
            "churn of an argument feeding on itself — "
            "calm coming down the mountain with cloud "
            "still on its shoulder, noise waiting at the "
            "bottom. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b02", "out": "s02-his-own-disciples-were-in.jpeg", "seg": "n0",
        "window": "5.03-14.15", "wide": True, "jesus": False, "ref": False,
        "locks": ["SCRIBES", "HILLFOOT", "FATHER", "BOY"],
        "narration": (
            "His own disciples were in the middle of it, cornered and "
            "embarrassed — because a desperate father had brought them his son, "
            "and for once, they could not help."
        ),
        "must_show": "the cornering — two disciples backed against a boulder under the scribes' pressing questions, while at the crowd's edge the father stands with his boy gathered under one arm; failure with its audience.",
        "must_not_show": "no halo, glare or rim-light; the disciples' embarrassment human — good men out of their depth; the boy safe under the father's arm.",
        "scene": (
            "Against a big boulder, the camera outside the ring "
            "behind the scribes' dark shoulders, two disciples stand "
            "cornered — one with his palms up in "
            "defence, the other's jaw set on nothing to "
            "say — while the three fine-robed scribes "
            "press their points with forensic fingers "
            "and the crowd banks around them for the "
            "sport — and at the circle's edge, "
            "half-forgotten by everyone, the big worn "
            "father stands with his thin son gathered "
            "close under one arm, watching the argument "
            "that was supposed to be a healing. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r065-b03", "out": "s03-they-had-tried-nothing-happened.jpeg", "seg": "n0",
        "window": "14.15-16.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILLFOOT"],
        "narration": "They had tried. Nothing happened.",
        "must_show": "the failure's residue — a disciple's open empty hands looked at by their owner: the tools that worked before, inert; bafflement in the palms.",
        "must_not_show": "no halo, glare or rim-light; no shame theatrics — honest bafflement at hands that have healed before.",
        "scene": (
            "Close in the crowd's noise: a disciple's "
            "two open hands held up before his own "
            "face, turned slowly — hands that have "
            "rested on the sick and felt them mend, "
            "examined now like tools that have "
            "inexplicably stopped — their owner's "
            "bearded face behind them carrying the "
            "particular bafflement of power that worked "
            "last week. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b04", "out": "s04-and-everyone-was-watching-them.jpeg", "seg": "n0 + n1",
        "window": "16.66-22.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER", "HILLFOOT"],
        "narration": (
            "And everyone was watching them fail. The father pushed through to "
            "Jesus and told him the whole story."
        ),
        "must_show": "SCRIPTURE-EXACT: the push-through — the big father shouldering through the crowd toward the arrived Jesus, desperation clearing his path; the story already spilling as he comes.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the father's momentum the beat — a man done waiting his turn.",
        "scene": (
            "Through the packed crowd the big father "
            "comes shouldering — not rough, just "
            "unstoppable, the crowd's bodies turning "
            "aside from his momentum like water — his "
            "bruised-tired eyes locked on the newly "
            "arrived figure in cream at the path's "
            "foot, his mouth already moving with the "
            "story he has told a hundred experts, "
            "spilling it while he is still five paces "
            "out. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r065-b05", "out": "s05-his-only-son-had-been.jpeg", "seg": "n1",
        "window": "22.64-32.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER", "BOY"],
        "narration": (
            "His only son had been tormented since he was little — thrown down, "
            "unable to speak, hurt again and again by something the family "
            "could not fight."
        ),
        "must_show": "⚑ Flags A,R: the torment told RESTRAINED — the family's remembered life: the father holding the spent boy safely on his lap by their hearth, the mother's hand on the small head; harm never shown, guarding always.",
        "must_not_show": "NO embodied spirit, NO seizure depicted, NO fire/water peril shown in progress — only the held aftermath and the family's vigilance; dignity total.",
        "scene": (
            "In the remembered lamplight of their small "
            "home the father sits on the floor holding "
            "his spent son gathered whole against his "
            "chest — the thin boy limp and safe in the "
            "big arms, breathing, eyes half-open and "
            "far away — while the mother kneels close "
            "with her hand cupped on the small dark "
            "head, and behind them the hearth stands "
            "screened with a propped board: a family's "
            "whole architecture of watchfulness, "
            "photographed between storms. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b06", "out": "s06-years-of-it.jpeg", "seg": "n1",
        "window": "32.77-34.34", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Years of it.",
        "must_show": "time's evidence — a close still: the boy's small sleeping mat placed between his parents' two mats; a decade of nights told in floor plan.",
        "must_not_show": "no halo, glare or rim-light; the arrangement the whole sentence — the child never left alone, for years.",
        "scene": (
            "A close still in dim home light: three "
            "sleeping mats on a beaten-earth floor — "
            "the small one laid exactly between the "
            "two larger, close enough that a parent's "
            "hand could land on it without rising — "
            "the wool of all three worn to the same "
            "age, a floor plan that has not changed "
            "in ten years telling the whole cost in "
            "one look. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b07", "out": "s07-a-father-who-had-watched.jpeg", "seg": "n1",
        "window": "34.34-39.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER"],
        "narration": (
            "A father who had watched his boy suffer his entire childhood and "
            "could do nothing."
        ),
        "must_show": "the helplessness portrait — close on the father's face at the crowd's edge: the specific exhaustion of ten years of vigilant love that could guard but never fix.",
        "must_not_show": "no halo, glare or rim-light; the exhaustion loving — worn BY devotion, not past it.",
        "scene": (
            "A close portrait of the father in the "
            "bright hill light: the early-greyed "
            "beard, the bruised-tired eyes with their "
            "decade of half-slept nights, the gentle "
            "enormous hands hanging ready at his "
            "sides even now — a face worn exactly the "
            "way a doorstep is worn, by the same "
            "faithful weight arriving on it every "
            "single day. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b08", "out": "s08-and-then-he-said-the.jpeg", "seg": "n2",
        "window": "40.38-47.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER"],
        "narration": (
            "And then he said the most honest thing in the story. He looked at "
            "Jesus, and this is exactly how Mark writes down what he said:"
        ),
        "must_show": "the look before the words — the father's eyes meeting Jesus's directly, honesty gathering; a man about to say the true thing instead of the right thing.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the meeting of eyes level — desperation choosing truth over performance.",
        "scene": (
            "Close between the two men in the crowd's "
            "hush: the father's bruised eyes come up "
            "and meet Jesus's directly — no rehearsed "
            "supplicant's posture, no performed "
            "certainty, just ten years of the truth "
            "gathering behind a working man's face on "
            "its way to his mouth — while Jesus holds "
            "the look with complete, level attention. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r065-b09", "out": "s09-if-thou-canst-do-anything.jpeg", "seg": "s22",
        "window": "48.57-52.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER", "BOY", "HILLFOOT"],
        "narration": "If thou canst do anything, have compassion on us, and help us.",
        "must_show": "SCRIPTURE-EXACT: the plea — the father before Jesus with one arm around his boy and one hand open toward the healer: the 'us' visible, the 'if' audible in his braced face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the plural painted — father and son as one patient; hope offered with flinch built in.",
        "scene": (
            "Before Jesus in the bright hill light the "
            "father stands with his thin son gathered "
            "under one arm and his free hand open and "
            "trembling toward the healer — the word "
            "'us' made flesh in the huddle of the two "
            "of them — his face braced around its own "
            "hope like a man offering a coin he "
            "cannot afford to lose, the little word "
            "IF sitting visibly in the flinch of his "
            "brows. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b10", "out": "s10-if-you-can-do-anything.jpeg", "seg": "n2b",
        "window": "53.52-58.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER"],
        "narration": (
            "If you can do anything — anything at all — have compassion on us, "
            "and help us."
        ),
        "must_show": "the IF up close — the father's face at the word: hope so bruised it qualifies itself mid-plea; the flinch and the asking in one expression.",
        "must_not_show": "no halo, glare or rim-light; the qualification tender — self-protection learned from years of nothing.",
        "scene": (
            "Extreme close on the father's face at the "
            "word: the plea in full flight and the "
            "flinch already built into it — brows "
            "guarding the eyes, the mouth shaping "
            "'anything' with the caution of a man who "
            "has spent ten years watching 'anything' "
            "come to nothing — hope with its own "
            "insurance policy written into every "
            "line. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b11", "out": "s11-if-after-all-those-years.jpeg", "seg": "n2b",
        "window": "58.78-64.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER", "BOY"],
        "narration": (
            "If. After all those years of disappointment, hope had gotten "
            "expensive."
        ),
        "must_show": "hope's price — the father's hand resting on his son's dark head: the treasury the years drew down; each hope's cost recorded in the tenderness.",
        "must_not_show": "no halo, glare or rim-light; the touch the whole economy — love intact, expectation bankrupted.",
        "scene": (
            "Close in the bright light: the father's "
            "enormous gentle hand at rest on his "
            "son's dark head, thumb moving once in an "
            "old unconscious stroke — a decade of "
            "healers, remedies and roadside experts "
            "all paid for from the same account — the "
            "hand of a man whose love never ran out, "
            "resting on the reason his hope nearly "
            "did. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b12", "out": "s12-listen-to-how-jesus-answered.jpeg", "seg": "n2b",
        "window": "65.15-69.22", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "Listen to how Jesus answered that trembling little word IF:",
        "must_show": "the answer coming — close on Jesus's face taking the 'if' and turning it: gentle challenge kindling, the word about to be handed back transformed.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the kindling gentle — a challenge issued as a gift.",
        "scene": (
            "Close on Jesus's face in the hill light: "
            "the father's trembling IF just landed, "
            "and something kindling in the warm brown "
            "eyes as he takes the little word up — "
            "not offence, not correction, but the "
            "particular bright gentleness of a "
            "teacher about to hand a man's own word "
            "back to him turned right side out. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r065-b13", "out": "s13-if-thou-canst-believe-all.jpeg", "seg": "j1",
        "window": "69.83-74.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER"],
        "narration": (
            "If thou canst believe, all things are possible to him that "
            "believeth."
        ),
        "must_show": "SCRIPTURE-EXACT: the word returned — the two faces close as the IF comes back across: Jesus steady, the father's expression cracking open at where the question has landed.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the transfer visible — doubt's address changed from the healer to the asker, kindly.",
        "scene": (
            "The two faces close in the bright light: "
            "Jesus's steady and kind as the sentence "
            "crosses — the little word IF picked up, "
            "reversed and set gently down on the "
            "father's own doorstep — and the father's "
            "face cracking open around its arrival: "
            "the question he aimed at heaven come "
            "home to the one place he never thought "
            "to point it. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b14", "out": "s14-and-now-comes-the-moment.jpeg", "seg": "n3",
        "window": "75.42-80.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER"],
        "narration": (
            "And now comes the moment this whole story is remembered for. The "
            "father did not pretend."
        ),
        "must_show": "the refusal to perform — the father's face at the crossroads: the brave religious mask available, and visibly being set aside; truth chosen in real time.",
        "must_not_show": "no halo, glare or rim-light; the choice legible — performance declined, honesty braced.",
        "scene": (
            "Close on the father's face at its "
            "crossroads: the learned mask of pious "
            "confidence hovering available — every "
            "poor man knows it — and being set aside "
            "in real time: the jaw loosening out of "
            "its brave set, the eyes coming up "
            "undefended, a man electing, before a "
            "crowd, to be exactly as believing as he "
            "actually is. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b15", "out": "s15-he-did-not-put-on.jpeg", "seg": "n3",
        "window": "80.55-86.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["FATHER", "HILLFOOT"],
        "narration": (
            "He did not put on a brave religious face and claim a faith he did "
            "not fully have."
        ),
        "must_show": "the watching stakes — the crowd's expectant faces ringed around the father: the audience before whom pretending would be easy and truth costs.",
        "must_not_show": "no halo, glare or rim-light; the crowd not hostile — just MANY; publicity as the price of honesty.",
        "scene": (
            "Around the father, the camera low behind the ring's "
            "near backs, the crowd's faces bank "
            "close and expectant in the bright light — "
            "scribes with their forensic attention, "
            "neighbours who know his story, strangers "
            "come for the argument — dozens of "
            "witnesses before whom a rehearsed 'I "
            "believe' would cost nothing and the "
            "truth costs everything, all waiting on "
            "one worn man's next sentence. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r065-b16", "out": "s16-he-did-something-braver-he.jpeg", "seg": "n3",
        "window": "86.30-94.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER"],
        "narration": (
            "He did something braver. He cried out the truest prayer in the "
            "Bible for anyone who has ever wanted to believe and struggled to:"
        ),
        "must_show": "the cry gathering — the father's chest filling, head lifting, the truest sentence of his life rising through him; the instant before the famous words.",
        "must_not_show": "no halo, glare or rim-light; the gathering physical — breath, lift, commitment; the cry a bodily act.",
        "scene": (
            "Close on the father as the cry gathers: "
            "his big chest filling, his grey-flecked "
            "head coming up, both hands rising open "
            "from his sides — the whole worn frame of "
            "the man organizing itself around one "
            "sentence the way a wave gathers before a "
            "shore — ten years of wanting-to-believe "
            "arriving at its voice. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b17", "out": "s17-lord-i-believe-help-thou.jpeg", "seg": "fv1",
        "window": "95.27-98.10", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER", "BOY", "HILLFOOT"],
        "narration": "Lord, I believe; help thou mine unbelief.",
        "must_show": "SCRIPTURE-EXACT: THE prayer — the father crying it full-voiced before Jesus, tears free, one hand on his son and one open to the healer; the whole Bible's honest prayer at full volume.",
        "must_not_show": "no halo, glare or rim-light on Jesus; both halves in the one cry — belief and its crack, offered together, hidden from no one.",
        "scene": (
            "In the bright hill light the father cries "
            "it out full-voiced — head back, tears "
            "running free into the early-grey beard, "
            "one enormous hand anchored on his son's "
            "thin shoulder and the other flung open "
            "toward Jesus — belief and the crack in "
            "it delivered together at the top of a "
            "worn man's lungs, in front of everyone, "
            "hiding nothing — while Jesus receives "
            "the whole broken offering with his face "
            "already answering. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b18", "out": "s18-help-me-where-i-he.jpeg", "seg": "n3b",
        "window": "99.16-102.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER"],
        "narration": "Help me where I don't. He did not hand Jesus a finished faith.",
        "must_show": "the offering's shape — the father's two cupped hands held out open: carrying something visibly incomplete and offered anyway; faith's honest inventory.",
        "must_not_show": "no halo, glare or rim-light; the hands empty-and-full — the gesture of giving what one has, cracks included.",
        "scene": (
            "Close on the father's two cupped hands "
            "held out open before him in the bright "
            "light — enormous, work-scarred, trembling "
            "slightly, and carrying nothing the eye "
            "can see — the exact posture of a man "
            "handing over the entire contents of his "
            "believing, quantity unverified, condition "
            "as-is — an unfinished faith, tendered in "
            "full. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b19", "out": "s19-he-handed-him-a-cracked.jpeg", "seg": "n3b + n4",
        "window": "102.90-108.84", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "He handed him a cracked one, and asked him to hold it anyway. "
            "Think about what he just did."
        ),
        "must_show": "the cracked gift — a close still metaphor: a cracked clay lamp, still burning, being passed carefully from one pair of hands into another's; damage and flame together.",
        "must_not_show": "no halo, glare or rim-light beyond the lamp's own small flame; the crack visible AND the light alive — both facts held.",
        "scene": (
            "A close still in warm light: a small clay "
            "lamp with a visible crack running down "
            "its side — and still burning, its flame "
            "steady — passing carefully from one pair "
            "of rough hands into another pair that "
            "receives it without hesitation, fingers "
            "closing around crack and warmth "
            "together: a damaged thing, alight, "
            "handed over whole. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b20", "out": "s20-he-brought-jesus-the-little.jpeg", "seg": "n4",
        "window": "108.84-116.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER"],
        "narration": (
            "He brought Jesus the little bit of faith he had AND the unbelief "
            "he was ashamed of — and laid both of them down."
        ),
        "must_show": "both parcels received — Jesus's hands closing around the father's offered cupped hands: everything brought, everything accepted, nothing sorted first.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the acceptance total — no inspection between offering and receiving.",
        "scene": (
            "In the bright light Jesus's two hands "
            "close warm around the father's offered "
            "cupped ones — the whole unsorted cargo "
            "of the man's believing and not-believing "
            "received in one grip, no inventory taken "
            "first, no crack examined before "
            "acceptance — four hands holding one "
            "honest mess between them, and none of "
            "them letting go. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b21", "out": "s21-he-did-not-wait-to.jpeg", "seg": "n4",
        "window": "116.27-122.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER"],
        "narration": (
            "He did not wait to believe perfectly before he asked. He asked for "
            "help WITH his believing."
        ),
        "must_show": "the order corrected — the father mid-ask, imperfection undisguised on his wet face: asking AS the believing, not after it.",
        "must_not_show": "no halo, glare or rim-light; the sequence the doctrine — no polish preceding the plea.",
        "scene": (
            "Close on the father's wet, unguarded face "
            "mid-ask: nothing finished about it — the "
            "doubt still visibly resident, the hope "
            "still trembling, the whole imperfect "
            "apparatus of the man's believing out in "
            "the open and ASKING anyway — prayer as "
            "the workshop where faith gets built, not "
            "the shop window where it gets displayed. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r065-b22", "out": "s22-and-that-that-honest-faith.jpeg", "seg": "n4",
        "window": "122.26-128.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER"],
        "narration": (
            "And that — that cracked-open, honest, half-full faith — was "
            "enough."
        ),
        "must_show": "the verdict — Jesus's face answering the cracked offering: acceptance complete, action already deciding itself; enough, ruled visibly.",
        "must_not_show": "no halo, glare or rim-light on Jesus; 'enough' as expression — no further requirement anywhere in his face.",
        "scene": (
            "Close on Jesus's face above the four "
            "joined hands: the verdict already "
            "rendered in it — the warm eyes settled, "
            "the head beginning its turn toward the "
            "boy, action gathering — a cracked, "
            "half-full, completely honest faith being "
            "ruled sufficient by the only court that "
            "was ever going to hear the case. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r065-b23", "out": "s23-jesus-saw-the-crowd-rushing.jpeg", "seg": "n5",
        "window": "129.11-132.73", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLFOOT"],
        "narration": "Jesus saw the crowd rushing in to gawk, and he did not wait.",
        "must_show": "SCRIPTURE-EXACT: the crowd converging — people running in from the paths at the news, and Jesus turning to act BEFORE the audience assembles; mercy outrunning spectacle.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his turn already toward the boy — the healing refusing to be a show.",
        "scene": (
            "From the meeting paths, the camera beside the trail "
            "so every runner crosses in profile, the crowd comes "
            "running — figures converging at a jog "
            "from three directions, drawn by the "
            "argument's rumour — and at the centre "
            "Jesus has already turned away from all "
            "of them toward the father and son, his "
            "decision moving faster than their feet: "
            "a mercy timed deliberately to beat its "
            "own audience. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b24", "out": "s24-he-spoke-directly-to-the.jpeg", "seg": "n5",
        "window": "133.21-139.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER", "BOY", "HILLFOOT"],
        "narration": (
            "He spoke directly to the thing that had stolen this boy's whole "
            "childhood, and commanded it, once and for all:"
        ),
        "must_show": "⚑ Flag A: the address WITHOUT an addressee shown — Jesus standing over the held boy speaking with command into the air above him; authority aimed at something never painted.",
        "must_not_show": "NO embodied spirit, NO shadow, NO distortion anywhere — the command's target absolutely invisible; the boy held safe in his father's arms.",
        "scene": (
            "Jesus stands over the boy — who is "
            "gathered safe against his father's chest "
            "— and speaks with quiet total command "
            "into the air above the small dark head: "
            "his face set, his words visibly aimed at "
            "something no eye in the crowd can see "
            "and no frame will ever show — authority "
            "addressing an emptiness that has run a "
            "household for ten years, and giving it "
            "notice. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b25", "out": "s25-thou-dumb-and-deaf-spirit.jpeg", "seg": "j2",
        "window": "140.36-145.38", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "Thou dumb and deaf spirit, I charge thee, come out of him, and "
            "enter no more into him."
        ),
        "must_show": "SCRIPTURE-EXACT: the charge — close on Jesus's face alone delivering it: absolute authority without volume; a sentence with no appeal built into every feature.",
        "must_not_show": "NO spirit shown, no target visible; no halo, glare or rim-light — the command carried entirely by one face's certainty.",
        "scene": (
            "Extreme close on Jesus's face as the "
            "charge is given: the warm eyes gone "
            "flint-steady, the jaw set, the words "
            "leaving at conversational volume with "
            "the weight of a closing door — no "
            "strain, no shout, no visible adversary — "
            "a verdict being read by the one judge "
            "whose rulings the invisible obeys. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r065-b26", "out": "s26-never-again.jpeg", "seg": "n5b",
        "window": "155.85-157.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["BOY"],
        "narration": "Never again.",
        "must_show": "the permanence — a close still of the boy's quiet resting face, held; the two words as a state, not an event.",
        "must_not_show": "no halo, glare or rim-light; stillness as promise — the storm-free face.",
        "scene": (
            "A close still: the boy's thin face at "
            "rest against his father's dark tunic — "
            "eyes closed, lashes down, the small "
            "features holding a quiet they have never "
            "once been left alone with — a "
            "ten-year-old face wearing, for the first "
            "time in memory, absolutely nothing but "
            "sleep's own weather. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b27", "out": "s27-you-spirit-that-has-kept.jpeg", "seg": "n5b",
        "window": "146.53-155.85", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER", "BOY", "HILLFOOT"],
        "narration": (
            "You spirit that has kept him silent and shut his ears — I command "
            "you: come out of him, and never come back into him again. Not for "
            "a while. Not ever."
        ),
        "must_show": "⚑ Flag A: the command completed over the held boy — the crowd frozen at a distance, the father's arms tight, Jesus's hand extended over the small head; the target still and forever unshown.",
        "must_not_show": "NO embodied anything; no convulsion depicted — the boy held close through the unseen departure; no halo, glare or rim-light.",
        "scene": (
            "Over the boy held tight in his father's "
            "arms Jesus's hand extends open — the "
            "command finishing above the small dark "
            "head while the frozen crowd holds its "
            "distance in a wide ring — the whole "
            "visible world just a man's steady hand, "
            "a father's grip, a boy gathered close, "
            "and an eviction proceeding in a realm "
            "the picture rightly refuses to show. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r065-b28", "out": "s28-it-left-the-boy-went.jpeg", "seg": "n6a",
        "window": "157.95-162.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER", "BOY", "HILLFOOT"],
        "narration": "It left. The boy went so still that people whispered he was dead.",
        "must_show": "SCRIPTURE-EXACT, RESTRAINED: the stillness — the boy lying utterly quiet on the ground on his father's spread mantle, the crowd's ring leaning in, hands over mouths; stillness read two ways.",
        "must_not_show": "no halo, glare or rim-light; the stillness PEACEFUL to the eye — the whisper of death carried by the crowd's faces, not by the boy's.",
        "scene": (
            "On his father's spread olive mantle the "
            "boy lies utterly still in the bright "
            "light — limbs loose, face quiet, a "
            "sleeper's slackness that the ring of "
            "leaning watchers reads darker: a woman's "
            "hand over her mouth, a man's slow "
            "head-shake beginning, the whisper "
            "travelling the circle — one stillness, "
            "two readings, and the father on his "
            "knees between them. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b29", "out": "s29-but-jesus-reached-down-took.jpeg", "seg": "n6a",
        "window": "162.40-169.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BOY", "HILLFOOT"],
        "narration": (
            "But Jesus reached down, took him by the hand, and lifted him up — "
            "and the boy stood, quiet and whole."
        ),
        "must_show": "SCRIPTURE-EXACT: THE HAND — Jesus bent low, his hand closed around the boy's small one, the lift in progress: the boy coming up from the mantle onto his own feet, eyes open.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the lift the row's tenderest mechanics — big hand, small hand, rising.",
        "scene": (
            "Jesus bends low over the still boy and "
            "his hand closes whole around the small "
            "thin one — and the lift is in motion: "
            "the boy rising from the spread mantle, "
            "his large quiet eyes open and clear, "
            "his bare feet finding the ground under "
            "him for the first weight of his new "
            "life — one hand pulling one child up "
            "out of ten years, in front of everyone. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r065-b30", "out": "s30-and-he-gave-him-back.jpeg", "seg": "n6b",
        "window": "169.96-173.95", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FATHER", "BOY", "HILLFOOT"],
        "narration": (
            "And he gave him back to his father. The tormented childhood was "
            "over."
        ),
        "must_show": "SCRIPTURE-EXACT: the giving back — Jesus guiding the standing boy the two steps into his father's opening arms; the transfer of a whole restored life.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the handover the beat — the healer's part ending where the father's embrace begins.",
        "scene": (
            "With one hand light on the boy's "
            "shoulder Jesus guides him the two steps "
            "across the trampled grass — and the "
            "father is already down on his knees with "
            "both enormous arms opening, his wet face "
            "breaking apart — the boy walking, "
            "WALKING, into the embrace, and the big "
            "arms closing around a childhood's worth "
            "of catches that will never be needed "
            "again. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r065-b31", "out": "s31-it-ended-with-a-hand.jpeg", "seg": "n6b",
        "window": "173.95-178.46", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "It ended with a hand reaching down into the dust to pull a son to "
            "his feet."
        ),
        "must_show": "the image distilled — close on the two clasped hands alone, large around small, at the top of the lift; the whole story's mechanism in one grip.",
        "must_not_show": "no halo, glare or rim-light; hands only — the ending as grip and rise.",
        "scene": (
            "Close against the bright ground: the two "
            "hands alone — a man's, closed whole and "
            "warm around a boy's thin one, both at "
            "the top of the lift's arc with the dust "
            "still falling away beneath them — the "
            "entire story compressed into its working "
            "part: one hand down into the dust, one "
            "hand rising out of it, holding on. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r065-b32", "out": "s32-later-alone-in-the-house.jpeg", "seg": "n7",
        "window": "179.01-185.00", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "Later, alone in the house, the disciples asked him why they had "
            "failed. And Jesus gave them one sentence:"
        ),
        "must_show": "SCRIPTURE-EXACT: the private question — the lamplit rented room: the disciples around Jesus, the day's failure finally askable; humility in the closeness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the room safe for the question — no audience, no shame.",
        "scene": (
            "In the small lamplit room at day's end "
            "the disciples sit close around Jesus on "
            "the rush mats — packs down, bread "
            "broken, the window going blue — and the "
            "question comes at last from the one who "
            "was cornered at the boulder, asked low "
            "and honest in the safety of the lamp's "
            "small circle: why couldn't we. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r065-b33", "out": "s33-this-kind-can-come-forth.jpeg", "seg": "j3",
        "window": "185.66-189.56", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": "This kind can come forth by nothing, but by prayer and fasting.",
        "must_show": "SCRIPTURE-EXACT: the one sentence — close on Jesus in the lamplight giving it: gently, without reproach; the answer a redirection, not a grade.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no rebuke in the delivery — dependence taught kindly.",
        "scene": (
            "Close on Jesus in the lamp's warm circle: "
            "the one sentence given quietly across "
            "the bread, his face without a grain of "
            "reproach — not an examiner returning a "
            "failed paper but a craftsman naming the "
            "one tool the job wanted — the answer "
            "landing soft and going deep. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r065-b34", "out": "s34-nothing-gets-this-out-except.jpeg", "seg": "n7b",
        "window": "190.69-196.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": (
            "Nothing gets this out except prayer and fasting, he told them — "
            "meaning this was never about their technique."
        ),
        "must_show": "technique retired — the disciples' faces around the lamp receiving it: the day's failure reframing itself from skill-gap to source-gap in real time.",
        "must_not_show": "no halo, glare or rim-light; relief and humility mixing — a burden lifted by being renamed.",
        "scene": (
            "Around the lamp the disciples' faces work "
            "through the sentence: the cornered one's "
            "shoulders coming down as the day's shame "
            "reclassifies itself, the big fisherman "
            "nodding slowly at something he half-"
            "suspected on the hill, the youngest "
            "mouthing the two words over — failure "
            "being gently rebuilt into a lesson about "
            "where power actually lives. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b35", "out": "s35-it-was-about-who-they.jpeg", "seg": "n7b",
        "window": "196.88-199.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": "It was about who they were leaning on.",
        "must_show": "dependence pictured — a close still in the lamplit room: a walking staff leaned into the corner, bearing an angle it cannot hold alone; leaning as theology.",
        "must_not_show": "no halo, glare or rim-light; the lean literal — weight transferred to what holds.",
        "scene": (
            "A quiet close still in the lamp's edge-"
            "light: a travel-worn walking staff leaned "
            "into the room's corner at its steep "
            "trusting angle — an object that stands "
            "all night precisely because it has given "
            "its weight to something stronger than "
            "itself — the evening's whole lesson "
            "parked against the wall in one line of "
            "olive wood. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r065-b36", "out": "s36-the-father-got-it-right.jpeg", "seg": "n7b",
        "window": "199.18-207.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER", "BOY"],
        "narration": (
            "The father got it right without knowing the rules: he stopped "
            "trying to be strong, and just brought his weakness to the only one "
            "who could carry it."
        ),
        "must_show": "the closing image — the father and son walking home together in the warm dusk, the boy's hand in his father's, both lighter than they have ever been.",
        "must_not_show": "no halo, glare or rim-light; the ordinary walk extraordinary — a father and son going home like any other, for the first time.",
        "scene": (
            "Down the dusk-gold path from the hill the "
            "father and son walk home hand in hand — "
            "the boy's step light and curious, "
            "stopping once to look at something in "
            "the grass the way children do, the big "
            "man letting him, in no hurry at all — "
            "two people doing the most ordinary thing "
            "in the world, an evening walk home, "
            "which for them has never once been "
            "ordinary until now. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "HILLFOOT": "PLACE-REF/hillfoot.jpeg",  # build-65-help-mine-unbelief s01-jesus-came-down-from-the (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "FATHER": "CAST-REF-V2/father.jpeg",
    "BOY": "CAST-REF-V2/boy.jpeg",
}
