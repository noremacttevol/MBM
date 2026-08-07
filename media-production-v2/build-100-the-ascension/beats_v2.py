#!/usr/bin/env python3
"""V2 beat map — row 100, build-100-the-ascension (Acts 1:6-11).

COVERAGE: 17 pictures over 97.6 s = 5.7 s/picture (matches the library density).
(The V1 build's orphaned n4 beat — echo-delete cleanup b39d30a19 — is skipped
by extract_beats.py; the timeline above is the 9-segment truth.)

SCRIPTURE FACTS (Acts 1:6-12 KJV):
  v6    "Lord, wilt thou at this time RESTORE AGAIN THE KINGDOM to
        Israel?" — the last question they asked him.
  v7    "It is NOT FOR YOU TO KNOW the times or the seasons, which the
        Father hath put in his own power."
  v8    "ye shall receive POWER, after that the Holy Ghost is come
        upon you: and ye shall be WITNESSES unto me both in Jerusalem,
        and in all Judaea, and in Samaria, and unto the UTTERMOST PART
        OF THE EARTH."
  v9    "while they BEHELD, he was TAKEN UP; and a CLOUD RECEIVED HIM
        out of their sight." — bodily, watched, into a cloud.
  v10   "TWO MEN stood by them IN WHITE APPAREL" — rendered per the
        angel law as the pale silver-grey pair.
  v11   "Ye men of Galilee, why stand ye GAZING UP into heaven? this
        SAME JESUS... SHALL SO COME IN LIKE MANNER as ye have seen him
        go."
  v12   the place: the mount called OLIVET, a sabbath day's journey
        from Jerusalem.

ANGEL RENDERING (CONTENT-CARE law): the two are real, plain-robed
figures in PALE SILVER-GREY — NO wings, no ring of light, nothing
outlining the bodies.

ASCENSION RENDERING: bodily and natural — Jesus rising with the calm
of a man lifted by unseen strength, cream robe stirring, feet leaving
the summit grass; then a great BRIGHT CLOUD folding around him. No
beams, no shining outlines, never the word glow.

TIME OF DAY: one clear bright morning throughout — high spring sky
over Olivet, the city small across the valley.

CHANGING CONDITION (kept OUT of the locks): Jesus — among them, then
lifted, then received; the sky — empty, then holding him, then cloud;
the eleven — asking, listening, staring up, then turned to their
mission.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER and JOHN come from the shared CAST_LOCKS.
LOCKS = {
    "MOUNT": (
        "MOUNT LOCK: the summit of Olivet — a rounded grassy crown "
        "above the olive terraces, scattered pale stones, a high "
        "clear spring sky, and across the valley the small distant "
        "city with its temple. The same summit, sky and skyline "
        "throughout."
    ),
    "ELEVEN": (
        "ELEVEN LOCK: the gathered disciples — eleven travel-worn "
        "men in DARK EARTH-BROWN, CHARCOAL, DEEP OLIVE and SLATE "
        "robes (never cream, never white); weathered, devoted faces."
    ),
    "TWO": (
        "TWO LOCK: the two messengers are the same pair in every "
        "shot — tall, real human figures in plain PALE SILVER-GREY "
        "robes — NO wings, no ring of light above any head, nothing "
        "outlining the bodies; calm, strong, ageless faces; feet on "
        "the ground."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): narration mp3s are newer
# than the V1 mp4 (recency gate fails) and |Δ|>1.0, so the packet-copy AUDIO LOCK
# would ship stale voices. Rebuild from this build's own mp3 segments — $0.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r100-b01", "out": "s01-in-his-last-moments-with.jpeg", "seg": "n0",
        "window": "0.33-7.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "ELEVEN", "PETER", "JOHN"],
        "narration": (
            "In his last moments with them, the disciples asked Jesus if he "
            "was going to restore the kingdom right then."
        ),
        "must_show": "SCRIPTURE-EXACT: the last question — the eleven gathered close around Jesus on the summit, faces eager with the kingdom question; the morning bright, nobody knowing it is the last hour.",
        "must_not_show": "no halo, glare or rim-light; the eagerness POLITICAL-hopeful — men still dreaming of thrones.",
        "scene": (
            "On the grassy crown of Olivet, the camera outside "
            "the ring behind the nearest shoulders, "
            "the eleven crowd their teacher "
            "one more time with the old "
            "question: faces eager in the "
            "bright morning, Peter's hands "
            "already shaping the restored "
            "kingdom in the air, the "
            "distant city shining across "
            "the valley as if posing for "
            "its own coronation — LORD, "
            "WILT THOU AT THIS TIME — the "
            "last question they will ever "
            "ask him on the earth, and "
            "still the wrong one. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r100-b02", "out": "s02-he-turned-them-toward-something.jpeg", "seg": "n0",
        "window": "7.62-10.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "He turned them toward something bigger.",
        "must_show": "the turning — close on Jesus's face beginning the redirect: patient warmth over the eager question, his gaze lifting past their kingdom toward horizons.",
        "must_not_show": "no halo, glare or rim-light; the redirect GENTLE — no rebuke of the dream, an enlargement of it.",
        "scene": (
            "Close on the gentle pivot: "
            "Jesus's face over the eager "
            "question, warm and patient, "
            "the warm brown eyes lifting "
            "from their huddle toward the "
            "horizon past their shoulders — "
            "not swatting the little "
            "kingdom down but visibly "
            "trading it in, the way a "
            "father takes a child's toy "
            "boat and turns them toward "
            "the actual sea. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r100-b03", "out": "s03-it-is-not-for-you.jpeg", "seg": "j0",
        "window": "10.84-18.47", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "ELEVEN"],
        "narration": (
            "It is not for you to know the times or the seasons, which the "
            "Father hath put in his own power."
        ),
        "must_show": "SCRIPTURE-EXACT: not for you to know — Jesus speaking it steadily to the ring, one hand lifted skyward at THE FATHER'S OWN POWER; the calendar taken gently off their hands.",
        "must_not_show": "no halo, glare or rim-light; the withholding KIND — a burden removed, not a door slammed.",
        "scene": (
            "The calendar is taken gently "
            "out of their hands: NOT FOR "
            "YOU TO KNOW — Jesus's voice "
            "steady around the ring, his "
            "hand turning upward at THE "
            "FATHER'S OWN POWER, the "
            "whole heavy question of "
            "when lifted off eleven sets "
            "of shoulders and filed "
            "where it always belonged — "
            "faces around him working "
            "through disappointment "
            "toward the strange relief "
            "of not being in charge of "
            "the clock. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r100-b04", "out": "s04-that-is-not-a-no.jpeg", "seg": "n1",
        "window": "35.83-37.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELEVEN"],
        "narration": "That is not a no.",
        "must_show": "the not-no — close on listening faces catching it: the answer reparsing behind their eyes; hope adjusting, not dying.",
        "must_not_show": "no halo, glare or rim-light; the recalibration VISIBLE — brows easing, heads tilting.",
        "scene": (
            "Close on the reparsing: "
            "listening faces around the "
            "circle catching what the "
            "answer is NOT — not a no, "
            "not a never, not a "
            "forget-the-kingdom — brows "
            "easing, a glance traded, "
            "Peter's head tilting as the "
            "sentence turns over in him "
            "and shows its other side: "
            "the thing is still coming; "
            "only the schedule was ever "
            "above their pay. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r100-b05", "out": "s05-but-ye-shall-receive-power.jpeg", "seg": "j1",
        "window": "19.30-35.03", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "ELEVEN"],
        "narration": (
            "But ye shall receive power, after that the Holy Ghost is come "
            "upon you: and ye shall be witnesses unto me both in Jerusalem, "
            "and in all Judaea, and in Samaria, and unto the uttermost part "
            "of the earth."
        ),
        "must_show": "SCRIPTURE-EXACT: the commission's map — Jesus's arm sweeping from the near city outward across the whole horizon: Jerusalem, Judaea, Samaria, the uttermost; the world assigned in one gesture.",
        "must_not_show": "no halo, glare or rim-light; the sweep GEOGRAPHIC — near to far, city to horizon's edge.",
        "scene": (
            "The commission is drawn, the camera at the group's "
            "side so the sweeping arm crosses in profile over the "
            "real distances, on "
            "the actual landscape: "
            "Jesus's arm beginning at the "
            "shining city across the "
            "valley — JERUSALEM — then "
            "sweeping the brown hills — "
            "ALL JUDAEA — the northern "
            "haze — SAMARIA — and on out "
            "over the world's blue rim "
            "to THE UTTERMOST PART OF "
            "THE EARTH — eleven pairs of "
            "eyes travelling the whole "
            "arc of it, watching their "
            "future assigned in one "
            "unhurried gesture. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r100-b06", "out": "s06-go-tell-everyone-everywhere-starting.jpeg", "seg": "n1",
        "window": "51.11-55.76", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "ELEVEN"],
        "narration": "Go tell everyone, everywhere, starting right where you're standing.",
        "must_show": "the starting-here — the ring of witnesses-to-be on the summit grass, the near city below them: the mission's first mile visible from where their sandals stand.",
        "must_not_show": "no halo, glare or rim-light; the HERE emphasized — their own feet on the grass, the first assignment within sight.",
        "scene": (
            "The frame drops to where the "
            "mission starts: eleven pairs "
            "of worn sandals planted on "
            "the summit grass, and past "
            "them, down the slope and "
            "across the valley, the city "
            "where it all begins — no "
            "ship to build, no border to "
            "cross for the first mile — "
            "everyone, everywhere, "
            "starting at the exact patch "
            "of ground under their own "
            "feet, which is where every "
            "uttermost journey has ever "
            "started. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r100-b07", "out": "s07-it-is-a-redirection.jpeg", "seg": "n1",
        "window": "37.17-38.86", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT"],
        "narration": "It is a redirection.",
        "must_show": "the redirect embodied — Jesus's two hands in one frame: one gently lowering the when-question, the other opening outward to the work; the trade visible.",
        "must_not_show": "no halo, glare or rim-light; BOTH gestures readable — the setting-down and the handing-over.",
        "scene": (
            "Close on the trade made "
            "with two hands: one turning "
            "palm-down in a gentle "
            "settling motion — the "
            "when-question laid to rest — "
            "while the other opens "
            "outward toward the waiting "
            "world, offering — the whole "
            "answer of the morning "
            "carried in the grammar of "
            "his hands: not yours to "
            "know; entirely yours to "
            "do. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r100-b08", "out": "s08-the-timing-belongs-to-the.jpeg", "seg": "n1",
        "window": "38.86-49.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "ELEVEN", "PETER", "JOHN"],
        "narration": (
            "The timing belongs to the Father, he told them, and it is not "
            "yours to work out — but the power is yours, and so is the "
            "work."
        ),
        "must_show": "the division of labor — Jesus among the eleven, the teaching landing: burdened faces clearing as the right load settles on the right shoulders.",
        "must_not_show": "no halo, glare or rim-light; the relief EARNED — men receiving a job they can actually do.",
        "scene": (
            "Around the ring the division "
            "of labor settles where it "
            "belongs: the timing filed "
            "upward, forever out of their "
            "hands — and the work and "
            "the power laid squarely into "
            "them — and the faces show "
            "the exchange: the "
            "calendar-anxiety draining "
            "out of Peter's brow, John's "
            "shoulders squaring under a "
            "load that finally fits, "
            "eleven men traded from "
            "waiting into working in one "
            "sentence. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r100-b09", "out": "s09-he-was-handing-them-the.jpeg", "seg": "n1",
        "window": "49.07-51.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": "He was handing them the mission.",
        "must_show": "the handing — Jesus's hand gripping Peter's shoulder, eye to eye: the mission passing person to person like a weight set into hands.",
        "must_not_show": "no halo, glare or rim-light; the grip REAL — commissioning as physical trust.",
        "scene": (
            "Close on the handover at "
            "its most physical: Jesus's "
            "hand closing firm on "
            "Peter's shoulder, eye "
            "level with eye, the "
            "mission passing through "
            "the grip the way weight "
            "passes into hands that are "
            "trusted with it — the "
            "fisherman's face taking "
            "the charge steady under "
            "the morning sky, a man "
            "being handed the keys in "
            "front of the whole crew. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r100-b10", "out": "s10-and-then-something-happened-they.jpeg", "seg": "n1",
        "window": "55.76-58.79", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "ELEVEN"],
        "narration": "And then something happened they would never forget.",
        "must_show": "the hinge — the summit's ordinary morning going still: Jesus stepping back a pace from the ring, something changing in the air; every face beginning to fix on him.",
        "must_not_show": "no halo, glare or rim-light; the stillness PREGNANT — the moment before, not the event.",
        "scene": (
            "The morning goes strange and "
            "still: Jesus stepping back "
            "one quiet pace from the "
            "ring onto the open grass, "
            "the breeze dropping, the "
            "birdsong thinning — nothing "
            "visibly different yet and "
            "everything about to be — "
            "eleven conversations dying "
            "mid-word as every face on "
            "the summit fixes on him "
            "with the animal certainty "
            "that the next minute will "
            "be carried to their "
            "graves. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r100-b11", "out": "s11-while-they-watched-he-was.jpeg", "seg": "n2a",
        "window": "59.39-62.04", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNT", "ELEVEN"],
        "narration": "While they watched, he was lifted up,",
        "must_show": "SCRIPTURE-EXACT: taken up while they beheld — Jesus risen bodily a man's height above the summit grass, robe stirring, calm; the eleven's faces tilting up after him.",
        "must_not_show": "no halo, glare or rim-light, no beams — the lift NATURAL and serene, feet clear of the grass, gravity simply excused.",
        "scene": (
            "And then the ground lets him go, the camera low "
            "behind the beholding ring's backs, "
            "go: while they watch — "
            "every eye open, no one "
            "blinking — Jesus rises "
            "bodily from the summit "
            "grass, a man's height and "
            "climbing, the cream robe "
            "stirring in the moving air, "
            "his face calm as morning "
            "and his hands still open "
            "toward them in blessing — "
            "eleven chins tilting back "
            "in perfect unison, gravity "
            "excused from one man "
            "quietly and for good. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r100-b12", "out": "s12-and-a-cloud-received-him.jpeg", "seg": "n2b",
        "window": "62.55-69.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNT", "ELEVEN"],
        "narration": (
            "and a cloud received him out of their sight. They stood there "
            "staring into the sky, stunned."
        ),
        "must_show": "SCRIPTURE-EXACT: the cloud receiving — high above the summit a great bright cloud folding closed around the small ascending figure; below, eleven statues staring up.",
        "must_not_show": "no halo, glare or rim-light, no beams; the figure SMALL and nearly gone within the cloud's fold — the receiving, not a vanishing effect.",
        "scene": (
            "High over the summit the sky "
            "does the receiving: a great "
            "bright spring cloud folding "
            "slow around the small "
            "rising figure — cream wool "
            "and blessing hands going "
            "gently from sight into the "
            "white the way a boat goes "
            "into fog — and on the grass "
            "below, eleven men turned to "
            "statues, heads full back, "
            "mouths open, staring into "
            "the closing brightness that "
            "just took their whole world "
            "up into itself. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r100-b13", "out": "s13-then-two-figures-in-white.jpeg", "seg": "n3",
        "window": "69.60-73.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNT", "ELEVEN", "TWO"],
        "narration": "Then two figures in white stood beside them with a promise:",
        "must_show": "SCRIPTURE-EXACT: the two in white apparel — the silver-grey pair standing suddenly among the sky-staring men; calm presence beside stunned stillness.",
        "must_not_show": "ABSOLUTE: no wings, no ring of light, nothing outlining the figures; the eleven still mid-stare as the two arrive.",
        "scene": (
            "While every eye is still "
            "aimed at the closed cloud, "
            "the grass gains two more "
            "figures: the tall pair in "
            "plain silver-grey standing "
            "suddenly among the "
            "sky-staring men — calm as "
            "noon, feet in the summit "
            "grass, ageless faces "
            "carrying something between "
            "amusement and tenderness at "
            "eleven bent-back necks — "
            "messengers arrived with the "
            "one sentence that will "
            "unfreeze the whole "
            "hilltop. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r100-b14", "out": "s14-ye-men-of-galilee-why.jpeg", "seg": "s11",
        "window": "74.50-79.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["TWO", "ELEVEN"],
        "narration": "Ye men of Galilee, why stand ye gazing up into heaven?",
        "must_show": "SCRIPTURE-EXACT: the gentle question — close on the nearer messenger addressing the upturned faces: WHY STAND YE GAZING; the necks beginning to lower.",
        "must_not_show": "no wings, no ring of light, no outline; the question KIND — a nudge from watching to working.",
        "scene": (
            "Close on the kindest "
            "interruption in Acts: the "
            "nearer messenger's calm "
            "face bent toward the "
            "upturned ones — YE MEN OF "
            "GALILEE, WHY STAND YE "
            "GAZING — the question "
            "landing like a hand on the "
            "shoulder of the whole "
            "group, bent-back necks "
            "beginning to lower one by "
            "one, eyes coming down out "
            "of the empty brightness to "
            "meet a message aimed at "
            "their feet, not their "
            "necks. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r100-b15", "out": "s15-this-same-jesus-which-is.jpeg", "seg": "s11",
        "window": "79.19-88.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOUNT", "ELEVEN", "TWO"],
        "narration": (
            "this same Jesus, which is taken up from you into heaven, shall "
            "so come in like manner as ye have seen him go into heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the promise — the two messengers with arms lifted toward the bright cloud-sky: SHALL SO COME IN LIKE MANNER; the eleven's faces turning from loss toward promise.",
        "must_not_show": "no wings, no ring of light, no outline; the sky PROMISED, not empty — the gesture writes the return on it.",
        "scene": (
            "The promise is written on "
            "the very sky that took him: "
            "the two silver-grey figures "
            "with arms lifted toward "
            "the bright towering cloud — "
            "THIS SAME JESUS — SHALL SO "
            "COME, IN LIKE MANNER — and "
            "around them the eleven "
            "faces change register, "
            "grief's gravity loosening "
            "as the empty blue overhead "
            "is converted, in one "
            "sentence, from the place "
            "they lost him into the "
            "direction he is coming "
            "back from. Every figure "
            "has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r100-b16", "out": "s16-he-did-not-abandon-them.jpeg", "seg": "n5",
        "window": "89.86-91.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELEVEN", "PETER", "JOHN"],
        "narration": "He did not abandon them.",
        "must_show": "the not-abandoned — close on the eleven's faces come back down to earth: loss transmuted into charged purpose; men left WITH something, not left.",
        "must_not_show": "no halo, glare or rim-light; NO orphan-grief — fullness, resolve, the mission warm in them.",
        "scene": (
            "Close on faces that have "
            "just done the arithmetic of "
            "the morning and come out "
            "rich: Peter's jaw set with "
            "purpose instead of grief, "
            "John's young eyes shining "
            "with the promise still in "
            "them, weather-worn features "
            "all around carrying the "
            "same settled fact — a "
            "teacher gone up is not a "
            "teacher gone: they stand "
            "on a summit stuffed with "
            "mission, power promised, "
            "and a return date held in "
            "heaven. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r100-b17", "out": "s17-he-left-them-a-mission.jpeg", "seg": "n5",
        "window": "91.53-97.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOUNT", "ELEVEN"],
        "narration": (
            "He left them a mission, a promise, and the sure word that he's "
            "coming again."
        ),
        "must_show": "the closing image — the eleven starting down the slope toward the city together, the bright cloud still high behind them; the walk from watching into witness begun.",
        "must_not_show": "no halo, glare or rim-light; the movement DOWNHILL and purposeful — toward Jerusalem, the mission's first mile underway.",
        "scene": (
            "The closing frame walks off the mountain, the camera "
            "behind the descending eleven toward the city, "
            "the mountain with them: "
            "eleven figures starting "
            "down the slope path "
            "together toward the shining "
            "city, strides lengthening, "
            "heads up — behind and above "
            "them the great bright "
            "cloud still standing in "
            "the blue like a seal on a "
            "letter — a mission in "
            "their hands, a promise at "
            "their backs, and the first "
            "mile of the uttermost "
            "part of the earth going by "
            "under their sandals. Every "
            "figure has two arms, two "
            "hands and one head."
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
