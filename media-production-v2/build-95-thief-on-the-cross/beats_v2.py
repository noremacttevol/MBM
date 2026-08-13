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

CRUCIFIXION RENDERING LAW (REWRITTEN 2026-08-12 — C-FIX, Cameron:
"he should be staked to the cross ... they are not facing each other
and Jesus should be on the cross also. All should have their shirts
off. All should be pinned to the cross. All should be in line
parallel not across from one another ... Jesus has a crown of thorns
on and they all have plaques above their heads"): the THREE crosses
stand in a straight PARALLEL ROW along the crest, evenly spaced, ALL
facing the same way toward the viewer — NEVER angled in toward each
other, NEVER two men standing free on the ground facing off across a
gap. Each of the three men is STRIPPED to a plain loincloth — bare
torso, bare shoulders — and AFFIXED to his own cross: arms stretched
along the crossbeam and bound/fixed at the wrists, the body hanging
and sagging from the beam, unable to stand free. A small rough wooden
PLAQUE (titulus) is fixed to the upright above EVERY man's head. The
centre man is Jesus, a woven CROWN OF THORNS on his brow. When one man
speaks to another only his HEAD turns along the row; the pinned body
never pivots to face across. Reverence is kept the RIGHT way — no
gushing blood, no gore, no nail driven through flesh shown in
close-up; the weight of it is in the posture, not splatter. The two
criminals are human beings at their last hour — never caricatures.

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
        "crosses standing in a straight PARALLEL ROW along the crest, "
        "evenly spaced and all facing the same way, against a cold "
        "grey-overcast sky; a rough wooden plaque fixed to the upright "
        "above each cross; the city wall low in the distance, small "
        "knots of watchers held back on the slope. The same rise, the "
        "same three parallel crosses and sky throughout."
    ),
    "MOCKER": (
        "MOCKER LOCK: the railing criminal is the same man in every "
        "shot — AFFIXED to the cross to the LEFT of centre, stripped "
        "to a plain loincloth with bare torso and bare shoulders, "
        "wrists bound along the crossbeam, a rough wooden plaque above "
        "his head: about thirty-five, gaunt and sharp-faced with a "
        "thin dark beard and a bitter twisted mouth, his pain curdled "
        "to spite."
    ),
    "THIEF": (
        "THIEF LOCK: the penitent thief is the same man in every "
        "shot — AFFIXED to the cross to the RIGHT of centre, stripped "
        "to a plain loincloth with bare torso and bare shoulders, "
        "wrists bound along the crossbeam, a rough wooden plaque above "
        "his head: about forty, a broad worn face, grey-shot dark "
        "beard, deep tired eyes, honesty arriving at his last hour."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): narration mp3s are newer
# than the V1 mp4 (recency gate fails), so the packet-copy AUDIO LOCK would ship
# stale voices. Rebuild from this build's own mp3 segments — $0.
AUDIO_FROM_V1_SEGMENTS = True

# DESYNC RE-TIME (AUTHOR-FIX 2026-08-11, Machine A `Dev`) — QC-BLOCK fix, $0.
# The 2026-08-07 cut ran the whole back half ~4s BEHIND the pictures: Jesus spoke
# "today shalt thou be with me in paradise" while the picture was the thief ALONE.
# ROOT: audio + captions come from extract_beats(95) (the V1 timeline — its n0b.mp3
# carries the redundant modern paraphrase "if you're really the Christ, save
# yourself and us", ~3.5s the v2 map never budgeted, plus a "lord remember me"
# paraphrase in n3). The picture-switch WINDOWS below were authored against a
# paraphrase-free reading, so they drifted behind the audio that actually plays.
# The AUDIO LOCK only checks TOTAL duration, so a per-segment slip sails through.
# FIX (no re-voice, no Gemini spend, V1 stays read-only): the windows below are
# now set from a faster-whisper transcription of the DELIVERED audio — every
# picture switches ~0.2s before its own spoken line lands, contiguous, no gaps.
# Verified by re-transcribing the re-assembled mp4 (see QC.md). Do NOT restore the
# old windows: the audio is the sole timing authority; pictures must follow it.

BEATS = [
    {
        "id": "v2-r095-b01", "out": "s01-two-criminals-were-crucified-with.jpeg", "seg": "n0a + s39",
        "window": "0.00-8.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILL"],
        # GIANT-COMPOSITE FIX (AUTHOR-LANE 2026-08-11, Machine A `Dev`): the prior
        # b01 attached the Jesus + MOCKER + THIEF face-crop REF portraits onto this
        # OPENING WIDE (jesus:True, ref:REF, three character locks). On an establishing
        # wide those tight portraits paste in as giant chest-up foreground figures over
        # a miniature crowd — the "giant/composite" complaint class (3 rerolls came back
        # worse, one with the REFs as literal framed rectangles on the crosses). FIX =
        # mirror the row-94 b01 that PRODUCED this exact HILL plate: a person-free,
        # plate-driven DISTANT establish — jesus:False, ref:False, HILL only, no character
        # portraits. The three men read as far silhouettes on their crosses; the sneer
        # and every face are covered in the singles that follow (b02+), never here.
        "narration": (
            "Two criminals were crucified with Jesus, one on each side. If "
            "thou be Christ, save thyself and us."
        ),
        "must_show": "SCRIPTURE-EXACT — the bare rise under the cold grey sky with THREE raised crosses in a straight PARALLEL ROW on the crest, evenly spaced and all facing the viewer, each cross bearing its own AFFIXED man stripped to a loincloth with a wooden plaque above his head, the centre one Jesus with a crown of thorns exactly between the two; small knots of watchers held back on the scrub slope, the city wall low and distant behind. ONE coherent photograph at a single consistent scale.",
        "must_not_show": "ABSOLUTE — NO giant or chest-up foreground figures, NO portrait-scale faces, NO collage / composite / double-perspective / haze seam; NO empty cross without its man, NO crosses angled toward each other, NO clothed/robed torsos on the crucified men, NO man standing free on the ground. No gushing blood or gore — seen far off, the distance itself the mercy.",
        "scene": (
            "From far down the slope, the camera behind the "
            "scattered watchers' backs, the "
            "bare rock crown holds its "
            "terrible geometry against the "
            "cold grey sky: three raised "
            "crosses in one straight parallel "
            "row on the hill's crest, evenly "
            "spaced and all facing the same "
            "way — each cross bearing its own "
            "man, stripped to a loincloth and "
            "hanging from the crossbeam, a "
            "small wooden plaque above every "
            "head — the centre one Jesus, a "
            "crown of thorns dark on his brow, "
            "exactly between the other two as "
            "the sentence says. Small knots of "
            "watchers held back on the scrub "
            "slope, the city wall low and "
            "distant behind. The first mocking "
            "words are already carrying up the "
            "hill, but the men are small and "
            "far, one coherent scene under the "
            "thin colorless morning light. "
            "Every figure is at the same "
            "distance, two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r095-b02", "out": "s02-that-was-one-of-them.jpeg", "seg": "n0b",
        "window": "8.00-16.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOCKER"],
        "narration": "That was one of them, sneering at him from the next cross over.",
        "must_show": "the sneer — the mocker AFFIXED to the left cross, stripped to a loincloth with bare torso and shoulders, wrists bound along the crossbeam and body sagging from it, a wooden plaque above his head; his twisted bitter face turned sideways toward the centre cross while his pinned body still faces forward; pain turned outward as spite.",
        "must_not_show": "ABSOLUTE: NO robe or shirt on him, NO man standing free on the ground, NO leaning against the wood — he HANGS from the cross, fixed; no gushing blood or gore; the bitterness HUMAN — agony curdled, not cartoon villainy.",
        "scene": (
            "Close on the left cross: the "
            "mocker hangs from it, stripped "
            "to a loincloth, bare shoulders "
            "and chest dragged down by his "
            "own weight, wrists lashed along "
            "the crossbeam, a rough plaque "
            "nailed above his head — and his "
            "gaunt face twists sideways along "
            "his pinned body toward the centre, "
            "every line of it curdled, the "
            "thin beard jerking with the effort "
            "of each mocking breath, the eyes "
            "bright with a bitterness that has "
            "decided, at the end of everything, "
            "to spend its last strength on "
            "scorn — a man drowning, using his "
            "final air to spit at the lifeboat. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r095-b03", "out": "s03-dost-not-thou-fear-god.jpeg", "seg": "s40",
        "window": "16.10-20.90", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILL", "MOCKER", "THIEF"],
        "narration": "Dost not thou fear God, seeing thou art in the same condemnation?",
        "must_show": "SCRIPTURE-EXACT: the rebuke down the row — all THREE crosses standing in a parallel line facing the viewer, each man affixed and shirtless in his loincloth with a plaque above his head, Jesus on the CENTRE cross with his crown of thorns hanging silent between them; the right-hand thief's HEAD turned along the row past the centre toward the mocker on the left while his pinned body stays facing forward: the same-condemnation argument thrown down the line of crosses.",
        "must_not_show": "ABSOLUTE: NO two men standing on the ground facing each other, NO figures turned body-to-body across a gap, NO cross empty of its man, NO robed/clothed torsos, NO crosses angled inward — the three uprights are a straight parallel row seen from the FRONT; no gushing blood or gore.",
        "scene": (
            "The rebuke travels down the row of crosses, the camera "
            "set in FRONT of the parallel line so all three uprights "
            "stand side by side facing the "
            "viewer — each man hanging from "
            "his own cross, stripped to a "
            "loincloth, a plaque above every "
            "head, the crown-of-thorns "
            "centre man silent between them: "
            "the broad worn thief on the "
            "right cross turns only his HEAD "
            "along the line toward the left, "
            "his fixed body never pivoting, "
            "voice grinding up from a failing "
            "chest — DOST NOT THOU FEAR GOD — "
            "one condemned man calling another "
            "to account past the one hanging "
            "between them, the same sentence "
            "nailed over all three and only "
            "two of them earning it. The few "
            "watchers on the slope behind are "
            "seen from the camera's side with "
            "their backs and shoulders to the "
            "lens, faces turned up toward the "
            "crosses, none looking at the "
            "camera. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r095-b04", "out": "s04-and-we-indeed-justly-for.jpeg", "seg": "s40",
        "window": "20.90-29.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["THIEF"],
        "narration": (
            "And we indeed justly; for we receive the due reward of our "
            "deeds: but this man hath done nothing amiss."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — the thief AFFIXED to the right cross, stripped to a loincloth with bare torso and shoulders, wrists bound along the crossbeam, a plaque above his head; his worn face saying the hardest word: JUSTLY; guilt owned without excuse, and the centre man cleared in the same breath.",
        "must_not_show": "ABSOLUTE: NO robe or shirt on him, NO standing free on the ground, NO leaning — he HANGS from the cross; no gushing blood or gore; the honesty TOTAL — no self-pity, no bargaining in the face.",
        "scene": (
            "Close on a man performing "
            "the rarest act on the hill — "
            "and doing it nailed up: he "
            "hangs from the right cross, "
            "stripped to a loincloth, bare "
            "shoulders sagging on the beam, "
            "a plaque above his head, "
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
        "window": "29.45-31.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "MOCKER", "THIEF"],
        "narration": "But the other one stopped him.",
        "must_show": "the silencing — the three crosses in their parallel row seen from the front, each man affixed and shirtless in his loincloth with a plaque above his head, Jesus centre with his crown of thorns: the mocker's face turned up and away silenced, the thief's face still lifted; the railing ended.",
        "must_not_show": "ABSOLUTE: NO man on the ground, NO crosses angled toward each other, NO robed torsos, NO empty cross; no gushing blood or gore; the mocker SILENCED, not destroyed — his face turned to the grey sky.",
        "scene": (
            "The hill goes quiet along "
            "its terrible parallel line of "
            "three crosses, seen from the "
            "front — three men hanging from "
            "them, stripped to their "
            "loincloths, a plaque above each "
            "head: on the left the gaunt "
            "face turned up and away at last, "
            "the spite run out of it, eyes "
            "gone to the empty grey sky — on "
            "the right the broad face still "
            "lifted, breathing hard from the "
            "spending of the rebuke — and "
            "between them the centre man in "
            "his crown of thorns, silent, "
            "listening, as he has been all "
            "along. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r095-b06", "out": "s06-getting-what-we-deserve-he.jpeg", "seg": "n1 + n2",
        "window": "31.90-39.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["THIEF"],
        "narration": (
            "We're getting what we deserve, he said. Then he turned his head "
            "toward Jesus and asked for the smallest thing he could think "
            "of."
        ),
        "must_show": "the turn — the thief affixed to his cross, shirtless in his loincloth, wrists bound to the beam, a plaque above his head; his HEAD turning along the row from the mocker toward Jesus on the centre cross (crown of thorns), his pinned body facing forward: the face changing from rebuke to asking; the request gathering.",
        "must_not_show": "ABSOLUTE: NO man on the ground, NO body pivoting to face across, NO robed torso, NO empty cross; no gushing blood or gore; the turn's HOPE fragile — a man deciding to ask for almost nothing.",
        "scene": (
            "The worn head turns its last "
            "turn along the line of crosses: "
            "away from the silenced mocker, "
            "past the grey air, toward the "
            "man hanging on the centre cross "
            "in his crown of thorns — the "
            "thief's own body still fixed to "
            "his beam, bare and sagging, a "
            "plaque above his head — and the "
            "face changes as it travels: the "
            "rebuker's hardness draining, "
            "something fragile and enormous "
            "rising under it — a lifetime's "
            "last request being sized down "
            "and down in his eyes until it "
            "is small enough to dare asking. "
            "Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r095-b07", "out": "s07-lord-remember-me-when-thou.jpeg", "seg": "s42",
        "window": "39.05-43.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL", "THIEF"],
        "narration": "Lord, remember me when thou comest into thy kingdom.",
        "must_show": "SCRIPTURE-EXACT: the request — two neighbouring crosses in the parallel row, both men affixed and shirtless in their loincloths with plaques above their heads, Jesus in his crown of thorns: the thief's HEAD turned along the row asking his smallest thing, Jesus's head already turning toward him, both bodies pinned facing forward.",
        "must_not_show": "ABSOLUTE: NO man on the ground, NO two figures facing body-to-body across a gap, NO robed torsos, NO empty cross; no gushing blood or gore; the request HUMBLE — remember me, nothing more; both faces dignified.",
        "scene": (
            "Down the line between two "
            "neighbouring crosses the "
            "smallest prayer ever prayed "
            "goes over — both men hanging "
            "from their beams, bare and "
            "spent, a plaque above each "
            "head, only their heads turned "
            "toward one another along the "
            "row: LORD — REMEMBER ME — not "
            "save me, not take me down, not "
            "even forgive me: just don't "
            "forget I existed, when you "
            "come into whatever is yours — "
            "and the crown-of-thorns face "
            "on the centre cross is already "
            "turning toward the asker, as "
            "if it had been waiting the "
            "whole morning for exactly this "
            "voice. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r095-b08", "out": "s08-no-good-deeds-to-offer.jpeg", "seg": "n3",
        "window": "43.75-48.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["THIEF"],
        "narration": "No good deeds to offer. No time left to fix his life.",
        "must_show": "the empty hands — close on the thief AFFIXED to his cross, stripped to a loincloth with bare torso and shoulders, wrists bound to the crossbeam, a plaque above his head: a man with absolutely nothing to bring, and the asking done anyway.",
        "must_not_show": "ABSOLUTE: NO robe or shirt on him, NO standing free, NO leaning against the wood — he HANGS from the cross; no gushing blood or gore; the poverty SPIRITUAL and total — nothing to trade, visible in the worn face.",
        "scene": (
            "Close on the man with "
            "nothing, and nailed up with "
            "it: he hangs from his cross, "
            "stripped to a loincloth, bare "
            "shoulders dragged down on the "
            "beam, a plaque above his "
            "head — no purse ever again, "
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
        "window": "48.05-56.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["THIEF"],
        "narration": (
            "Just a dying man asking. Verily I say unto thee, today shalt "
            "thou be with me in paradise."
        ),
        "must_show": "SCRIPTURE-EXACT: the answer — close on Jesus AFFIXED to the centre cross, the crown of thorns on his brow, stripped to a loincloth with bare torso and shoulders, wrists bound to the crossbeam; his face turned along the row toward the thief, the promise given with absolute certainty: TODAY, WITH ME, PARADISE.",
        "must_not_show": "ABSOLUTE: NO robe or shirt on him, NO standing free, NO cream garment, NO halo or glow; he HANGS from the cross; no gushing blood or gore; the certainty TOTAL — a dying king issuing the surest sentence ever spoken.",
        "scene": (
            "The answer comes back bigger "
            "than the ask: Jesus hangs from "
            "the centre cross, stripped to a "
            "loincloth, the crown of thorns "
            "dark on his brow, his face "
            "turned along the row toward the "
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
        "window": "56.70-60.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["THIEF"],
        "narration": "Today. Not someday, not after you've earned it.",
        "must_show": "the word landing — close on the thief AFFIXED to his cross, stripped to a loincloth with bare shoulders, wrists bound to the beam, a plaque above his head; his face receiving TODAY: disbelief breaking into peace; a dying man handed a same-day appointment.",
        "must_not_show": "ABSOLUTE: NO robe or shirt on him, NO standing free, NO leaning — he HANGS from the cross; no gushing blood or gore; the peace ARRIVING — the change readable across the worn features.",
        "scene": (
            "Close on the word arriving "
            "where no good news ever "
            "came — and arriving on a man "
            "nailed up: the thief hangs "
            "from his cross, bare and "
            "spent, a plaque above his "
            "head, as TODAY lands on his "
            "face — the disbelief of a man "
            "checking the promise for the "
            "catch and finding none, then "
            "the breaking, then, spreading "
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
        "window": "60.40-64.65", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL", "THIEF"],
        "narration": "Today. The last-minute faith of a criminal was enough.",
        "must_show": "the closing image — the centre and right crosses standing as PARALLEL UPRIGHTS seen from the FRONT, side by side in the row against the grey, both men affixed and shirtless in their loincloths with plaques above their heads, Jesus in his crown of thorns; both pinned bodies squared to the viewer, each face lifted and at rest looking outward (at most a gentle head-tilt), the promise standing between them — NEVER the two faces turned toward each other across the gap; enough, made visible.",
        "must_not_show": "ABSOLUTE: NO man on the ground, NO crosses angled toward each other, NO two faces turned toward each other in a mutual profile gaze, NO figures body-to-body across a gap, NO robed torsos, NO empty cross, NO halo or glow; no gushing blood or gore; NO modern fence / railing / guardrail / handrail / metal bars, NO modern metal bolts or hardware on the crosses — the hill is ancient bare-rock ground with only the distant stone city wall behind; both crosses are straight parallel uprights seen from the FRONT, both bodies facing the viewer — the covenant of the hill's two neighbours complete.",
        "scene": (
            "The closing frame keeps the "
            "two neighbours in the parallel "
            "row: the centre cross and the "
            "right one side by side against "
            "the cold grey sky, both men "
            "hanging from their beams, "
            "stripped to their loincloths, a "
            "plaque above each head, the "
            "crown of thorns on the centre "
            "brow — both crosses standing as "
            "straight parallel uprights seen "
            "from the front, both pinned "
            "bodies squared to the viewer, "
            "each face lifted and, now, at "
            "rest looking outward, never the "
            "two faces turned toward each "
            "other across the gap — "
            "between them nothing but a few "
            "feet of morning air and a "
            "finished promise — the "
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
