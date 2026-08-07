#!/usr/bin/env python3
"""V2 beat map — row 95, build-95-thief-on-the-cross (Luke 23:39-43).

COVERAGE: 11 pictures over 60.4 s = 5.5 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 23:39-43 KJV):
  v39   "one of the malefactors which were hanged RAILED on him... If
        thou be Christ, save thyself and us." — mockery from the next
        cross.
  v40-41 the other REBUKES him: "Dost not thou fear God, seeing thou
        art in the same condemnation? And we indeed JUSTLY... but this
        man hath done NOTHING AMISS."
  v42   "Lord, REMEMBER ME when thou comest into thy kingdom." — the
        smallest possible request.
  v43   "Verily I say unto thee, TODAY shalt thou be with me in
        PARADISE." — grace with a same-day date on it.

CRUCIFIXION RENDERING LAW (as row 94, same hill, same morning): all
violence OFF-SCREEN — no nails, blood, wounds or gore anywhere; the
three crosses shown raised, at distance in wides, chest-or-face-up in
closes, dignity absolute for all three men. The two criminals are
human beings at their last hour — never caricatures.

TIME OF DAY: the same bleak grey-overcast morning as row 94 — thin
colorless light throughout.

CHANGING CONDITION (kept OUT of the locks): the second thief — railing
witness, then rebuker, then asker, then answered; the exchange turning
head by head across the three crosses.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "HILL": (
        "HILL LOCK: Calvary — a bare rounded rock rise outside the "
        "city wall: grey stone and thin scrub, THREE raised wooden "
        "crosses against a cold grey-overcast sky, the city wall low "
        "in the distance, small knots of watchers held back on the "
        "slope. The same rise, crosses and sky throughout."
    ),
    "MOCKER": (
        "MOCKER LOCK: the railing criminal is the same man in every "
        "shot — on the cross to the LEFT of centre: about thirty-"
        "five, gaunt and sharp-faced with a thin dark beard and a "
        "bitter twisted mouth; shown chest-up, no wounds, his pain "
        "curdled to spite."
    ),
    "THIEF": (
        "THIEF LOCK: the penitent thief is the same man in every "
        "shot — on the cross to the RIGHT of centre: about forty, a "
        "broad worn face, grey-shot dark beard, deep tired eyes; "
        "shown chest-up, no wounds, honesty arriving at his last "
        "hour."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): narration mp3s are newer
# than the V1 mp4 (recency gate fails), so the packet-copy AUDIO LOCK would ship
# stale voices. Rebuild from this build's own mp3 segments — $0.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r095-b01", "out": "s01-two-criminals-were-crucified-with.jpeg", "seg": "n0a + s39",
        "window": "0.28-6.92", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILL", "MOCKER", "THIEF"],
        "narration": (
            "Two criminals were crucified with Jesus, one on each side. If "
            "thou be Christ, save thyself and us."
        ),
        "must_show": "SCRIPTURE-EXACT: the three at distance — the raised crosses against the grey: Jesus centre, the gaunt mocker left, the broad-faced thief right; the railing begun from the left.",
        "must_not_show": "ABSOLUTE: no nails, blood, wounds or gore — crosses raised and complete, all three men chest-up with dignity.",
        "scene": (
            "The grey morning holds, the camera down the slope "
            "behind the scattered watchers, the "
            "three of them against its "
            "cold sky: the centre cross "
            "and its two companions, one "
            "either side exactly as the "
            "sentence orders — and from "
            "the left-hand beam the first "
            "words are already flying, "
            "the gaunt man's head twisted "
            "toward the centre with his "
            "bitter mouth working — IF "
            "THOU BE CHRIST — three dying "
            "men on one bare hill, and "
            "the talking not done yet. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r095-b02", "out": "s02-that-was-one-of-them.jpeg", "seg": "n0b",
        "window": "8.43-12.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOCKER"],
        "narration": "That was one of them, sneering at him from the next cross over.",
        "must_show": "the sneer — close on the mocker chest-up: the twisted bitter face aimed sideways at the centre cross; pain turned outward as spite.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the bitterness HUMAN — agony curdled, not cartoon villainy.",
        "scene": (
            "Close on the left cross, "
            "chest-up: the gaunt face "
            "twisted sideways toward the "
            "centre, every line of it "
            "curdled — the thin beard "
            "jerking with the effort of "
            "each mocking breath, the "
            "eyes bright with a bitterness "
            "that has decided, at the "
            "end of everything, to spend "
            "its last strength on scorn — "
            "a man drowning, using his "
            "final air to spit at the "
            "lifeboat. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r095-b03", "out": "s03-dost-not-thou-fear-god.jpeg", "seg": "s40",
        "window": "12.86-16.92", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILL", "MOCKER", "THIEF"],
        "narration": "Dost not thou fear God, seeing thou art in the same condemnation?",
        "must_show": "SCRIPTURE-EXACT: the rebuke across — the right-hand thief's head turned hard past the centre toward the mocker: the same-condemnation argument thrown cross to cross.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the geometry CLEAR — the rebuke crossing IN FRONT of the silent centre cross.",
        "scene": (
            "The rebuke crosses the hill, the camera off the "
            "cross-line's side so all three read in one profile, "
            "in front of the silent "
            "centre: the broad worn face "
            "on the right cross turned "
            "hard toward the left, voice "
            "grinding up from a failing "
            "chest — DOST NOT THOU FEAR "
            "GOD — one condemned man "
            "calling another to account "
            "over the head of the one "
            "hanging between them, the "
            "same sentence nailed over "
            "all three and only two of "
            "them earning it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r095-b04", "out": "s04-and-we-indeed-justly-for.jpeg", "seg": "s40",
        "window": "16.92-24.56", "wide": False, "jesus": False, "ref": False,
        "locks": ["THIEF"],
        "narration": (
            "And we indeed justly; for we receive the due reward of our "
            "deeds: but this man hath done nothing amiss."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — close on the thief's worn face saying the hardest word: JUSTLY; guilt owned without excuse, and the centre man cleared in the same breath.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the honesty TOTAL — no self-pity, no bargaining in the face.",
        "scene": (
            "Close on a man performing "
            "the rarest act on the hill: "
            "telling the truth about "
            "himself — WE, INDEED, JUSTLY "
            "— the word coming off the "
            "broad worn face without "
            "flinch or excuse, a whole "
            "criminal life signed for in "
            "one breath — and in the "
            "next, the same failing voice "
            "spending itself on someone "
            "else's defence: THIS MAN "
            "HATH DONE NOTHING AMISS — "
            "honesty's last two duties, "
            "both discharged. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r095-b05", "out": "s05-but-the-other-one-stopped.jpeg", "seg": "n1",
        "window": "26.04-27.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "MOCKER", "THIEF"],
        "narration": "But the other one stopped him.",
        "must_show": "the silencing — the wide three-cross line: the mocker's face turned away silenced, the thief's still lifted; the railing ended.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the mocker SILENCED, not destroyed — his face turned to the grey sky.",
        "scene": (
            "The hill goes quiet along "
            "its terrible line: on the "
            "left the gaunt face turned "
            "away at last, the spite run "
            "out of it, eyes gone to the "
            "empty grey sky — on the "
            "right the broad face still "
            "lifted, breathing hard from "
            "the spending of the rebuke — "
            "and between them the centre "
            "cross in its silence, "
            "listening, as it has been "
            "all along. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r095-b06", "out": "s06-getting-what-we-deserve-he.jpeg", "seg": "n1 + n2",
        "window": "27.39-34.91", "wide": False, "jesus": True, "ref": REF,
        "locks": ["THIEF"],
        "narration": (
            "We're getting what we deserve, he said. Then he turned his head "
            "toward Jesus and asked for the smallest thing he could think "
            "of."
        ),
        "must_show": "the turn — the thief's head turning from the mocker toward the centre cross: the face changing from rebuke to asking; the request gathering.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the turn's HOPE fragile — a man deciding to ask for almost nothing.",
        "scene": (
            "The worn head turns its last "
            "turn: away from the silenced "
            "mocker, across the little "
            "distance of grey air, toward "
            "the man on the centre cross — "
            "and the face changes as it "
            "travels: the rebuker's "
            "hardness draining, something "
            "fragile and enormous rising "
            "under it — a lifetime's last "
            "request being sized down and "
            "down in his eyes until it "
            "is small enough to dare "
            "asking. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r095-b07", "out": "s07-lord-remember-me-when-thou.jpeg", "seg": "s42",
        "window": "35.48-38.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL", "THIEF"],
        "narration": "Lord, remember me when thou comest into thy kingdom.",
        "must_show": "SCRIPTURE-EXACT: the request — the two faces across the gap between their crosses: the thief asking his smallest thing, Jesus's face already turning toward him.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the request HUMBLE — remember me, nothing more; both faces dignified.",
        "scene": (
            "Across the gap between two "
            "crosses the smallest prayer "
            "ever prayed goes over: LORD — "
            "REMEMBER ME — not save me, "
            "not take me down, not even "
            "forgive me: just don't "
            "forget I existed, when you "
            "come into whatever is yours — "
            "and the centre face is "
            "already turning toward the "
            "asker, as if it had been "
            "waiting the whole morning "
            "for exactly this voice. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r095-b08", "out": "s08-no-good-deeds-to-offer.jpeg", "seg": "n3",
        "window": "40.23-43.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["THIEF"],
        "narration": "No good deeds to offer. No time left to fix his life.",
        "must_show": "the empty hands — close on the thief's face and bound frame chest-up: a man with absolutely nothing to bring, and the asking done anyway.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the poverty SPIRITUAL and total — nothing to trade, visible in the worn face.",
        "scene": (
            "Close on the man with "
            "nothing: no purse ever again, "
            "no years left to be better "
            "in, no deed anywhere behind "
            "him fit to mention at a "
            "gate — the broad face worn "
            "down to its last hour "
            "holding not one bargaining "
            "chip, not one credential, "
            "not one good day to point "
            "to — the emptiest hands on "
            "the hill, and the only ones "
            "that reached out. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r095-b09", "out": "s09-just-a-dying-man-asking.jpeg", "seg": "n3 + j1",
        "window": "43.80-51.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["THIEF"],
        "narration": (
            "Just a dying man asking. Verily I say unto thee, today shalt "
            "thou be with me in paradise."
        ),
        "must_show": "SCRIPTURE-EXACT: the answer — close on Jesus's face turned full to the thief, the promise given with absolute certainty: TODAY, WITH ME, PARADISE.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the certainty TOTAL — a dying king issuing the surest sentence ever spoken.",
        "scene": (
            "The answer comes back bigger "
            "than the ask: Jesus's face "
            "turned full toward the "
            "worn-out asker, the drawn "
            "features gathering for the "
            "cost of speech and spending "
            "it royally — VERILY — TODAY — "
            "WITH ME — IN PARADISE — a "
            "man three hours from death "
            "issuing the most certain "
            "promise in the language, "
            "with the calm of a king "
            "signing papers at his own "
            "table. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r095-b10", "out": "s10-today-not-someday-not-after.jpeg", "seg": "n4",
        "window": "52.64-55.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["THIEF"],
        "narration": "Today. Not someday, not after you've earned it.",
        "must_show": "the word landing — close on the thief's face receiving TODAY: disbelief breaking into peace; a dying man handed a same-day appointment.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the peace ARRIVING — the change readable across the worn features.",
        "scene": (
            "Close on the word arriving "
            "where no good news ever "
            "came: the thief's face as "
            "TODAY lands on it — the "
            "disbelief of a man checking "
            "the promise for the catch "
            "and finding none, then the "
            "breaking, then, spreading "
            "slow across the broad worn "
            "features like morning over "
            "water, a peace with a date "
            "on it — this very day — "
            "settling into eyes that "
            "expected nothing again, "
            "ever. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r095-b11", "out": "s11-today-the-faith-of-a.jpeg", "seg": "n4",
        "window": "55.86-60.17", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL", "THIEF"],
        "narration": "Today. The last-minute faith of a criminal was enough.",
        "must_show": "the closing image — the centre and right crosses together against the grey: the two faces at peace, the promise standing between them; enough, made visible.",
        "must_not_show": "ABSOLUTE: no wounds or blood; BOTH faces at rest — the covenant of the hill's two neighbours complete.",
        "scene": (
            "The closing frame keeps the "
            "two neighbours: the centre "
            "cross and the right one "
            "side by side against the "
            "cold grey sky, the two "
            "faces turned each other's "
            "way and both, now, at rest — "
            "between them nothing but a "
            "few feet of morning air and "
            "a finished promise — the "
            "last-minute faith of a "
            "criminal, weighed on the "
            "only scale that matters and "
            "found, forever, enough. "
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
    "HILL": "PLACE-REF/hill.jpeg",  # build-94-father-forgive-them v2-r094-b01 (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "MOCKER": "CAST-REF-V2/mocker.jpeg",
    "THIEF": "CAST-REF-V2/thief.jpeg",
}
