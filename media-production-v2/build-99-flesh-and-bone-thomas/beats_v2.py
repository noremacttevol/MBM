#!/usr/bin/env python3
"""V2 beat map — row 99, build-99-flesh-and-bone-thomas (Luke 24:36-43;
John 20:24-29).

COVERAGE: 14 pictures over 79.2 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  John 20:19  "the DOORS WERE SHUT where the disciples were assembled
        FOR FEAR... came Jesus and STOOD IN THE MIDST." — a locked
        evening room, sudden presence.
  Luke 24:37  "they were terrified... supposed that they had seen a
        SPIRIT."
  Luke 24:39  "BEHOLD MY HANDS AND MY FEET, that it is I MYSELF:
        HANDLE ME, and see; for a spirit hath not FLESH AND BONES, as
        ye see me have."
  John 20:24-25 THOMAS was not there; "Except I shall see... I will
        not believe."
  John 20:26  "after EIGHT DAYS... then came Jesus, the doors being
        shut, and stood in the midst."
  John 20:27  "REACH HITHER THY FINGER... and be not FAITHLESS, but
        BELIEVING."
  John 20:28  Thomas answered: "MY LORD AND MY GOD." — he never
        touches; the offer is enough.
  John 20:29  "BLESSED are they that have NOT SEEN, and yet have
        believed."

RENDERING: the risen Jesus NATURAL and warm — cream robe, real flesh;
his hands presented open in gesture, NO graphic wounds, no gore, no
shining effects; the marks never detailed. His appearing is sudden
presence — no materialization effects.

TIME OF DAY: lamplit EVENING in the locked room for both appearances
(correct story interior, not the row-11 defect).

CHANGING CONDITION (kept OUT of the locks): the room's fear — locked
terror, then joy; Thomas — absent, then refusing, then face to face,
then confessing; the door — barred throughout, and irrelevant twice.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. PETER and JOHN come from the shared CAST_LOCKS.
LOCKS = {
    "ROOM": (
        "ROOM LOCK: the hiding room — an upper chamber with ONE heavy "
        "door BARRED with a wooden beam, shuttered windows, a low "
        "table with oil lamps, cloaks hung on pegs; lamplit evening "
        "dimness. The same barred door, lamps and walls throughout."
    ),
    "THOMAS": (
        "THOMAS LOCK: Thomas is the same man in every shot — about "
        "thirty-five, dark curly hair and a short dark beard, a "
        "squared practical face with sceptical brows, in a DEEP "
        "TEAL-BLUE robe (never cream, never white); honest to the "
        "bone, doubt worn openly."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): narration mp3s are newer
# than the V1 mp4 (recency gate fails) and |Δ|>1.0, so the packet-copy AUDIO LOCK
# would ship stale voices. Rebuild from this build's own mp3 segments — $0.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r099-b01", "out": "s01-the-disciples-were-hiding-behind.jpeg", "seg": "n0",
        "window": "0.28-5.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": (
            "The disciples were hiding behind locked doors, afraid, when "
            "Jesus suddenly stood among them."
        ),
        "must_show": "SCRIPTURE-EXACT: doors shut, stood in the midst — the barred room's huddled fear, and Jesus simply STANDING at its centre; the beam still in its brackets behind.",
        "must_not_show": "no halo, glare or rim-light, no materialization effects — he is simply, solidly THERE; the bar visibly still in place.",
        "scene": (
            "The barred room is mid-fear, the camera at the wall "
            "behind the nearest shoulders — "
            "men huddled low around the "
            "lamps, voices kept under the "
            "shutters, the heavy beam "
            "seated hard in its brackets — "
            "and then the centre of the "
            "room is occupied: Jesus "
            "standing among them, solid "
            "and warm and simply THERE, "
            "with the locked door still "
            "locked behind him and every "
            "face around the lamplight "
            "snapping up in a single "
            "instant of perfect terror. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r099-b02", "out": "s02-they-thought-they-were-seeing.jpeg", "seg": "n0",
        "window": "5.76-8.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": "They thought they were seeing a ghost.",
        "must_show": "SCRIPTURE-EXACT: supposed a spirit — close on the terrified faces: recoil, a knocked-over cup, backs to the wall; the ghost-fear naked.",
        "must_not_show": "no halo, glare or rim-light; NOTHING ghostly actually shown — the fear lives in the faces only.",
        "scene": (
            "Close on the terror doing "
            "its arithmetic: Peter's back "
            "hitting the wall with a "
            "thud, a cup going over and "
            "rolling, John's knuckles "
            "white on another man's "
            "sleeve — dead men do not "
            "stand in barred rooms, "
            "therefore this is no man — "
            "the oldest fear in the "
            "world flooding a lamplit "
            "chamber where the most "
            "solid good news in history "
            "is standing patiently at "
            "the centre. Every figure "
            "has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r099-b03", "out": "s03-he-calmed-them-and-showed.jpeg", "seg": "n1",
        "window": "8.62-13.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": (
            "He calmed them and showed them it was really him — flesh and "
            "bone, not a spirit."
        ),
        "must_show": "the calming proof — Jesus's open unhurried hands extended to the room, warm and real in the lamplight; the terror beginning to thaw around him.",
        "must_not_show": "no halo, glare or rim-light; NO graphic wounds — the hands presented open, ordinary, alive.",
        "scene": (
            "The proof begins with "
            "gentleness: Jesus's two "
            "hands opening out into the "
            "lamplight, unhurried, palms "
            "up — real hands with real "
            "weight and warmth in them, "
            "held where every wide eye "
            "in the room can look their "
            "fill — his voice low and "
            "familiar under the panic, "
            "and around the walls the "
            "terror beginning its slow "
            "thaw into something no one "
            "dares name yet. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r099-b04", "out": "s04-behold-my-hands-and-my.jpeg", "seg": "j1",
        "window": "14.07-24.47", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "PETER", "JOHN"],
        "narration": (
            "Behold my hands and my feet, that it is I myself: handle me, "
            "and see; for a spirit hath not flesh and bones, as ye see me "
            "have."
        ),
        "must_show": "SCRIPTURE-EXACT: handle me and see — the invitation full: hands offered to be grasped, the nearest disciples reaching trembling to touch; solidity proven skin to skin.",
        "must_not_show": "no halo, glare or rim-light; NO graphic wounds — the touching of real warm hands, the proof in the contact.",
        "scene": (
            "The invitation goes further "
            "than any ghost could follow: "
            "HANDLE ME, AND SEE — and "
            "trembling hands reach out of "
            "the lamplight to take his: "
            "Peter's big fingers closing "
            "around a wrist and finding "
            "pulse and warmth and bone, "
            "John's palm flat against a "
            "solid forearm — flesh "
            "answering flesh all around "
            "the circle while the barred "
            "door looks on, the most "
            "empirical miracle ever "
            "offered, passing every "
            "test. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r099-b05", "out": "s05-but-thomas-there.jpeg", "seg": "n2",
        "window": "25.93-27.44", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "THOMAS"],
        "narration": "But Thomas wasn't there.",
        "must_show": "the absence — Thomas alone elsewhere that evening: the empty seat at the lamplit table behind, or Thomas out in the dark street; the one who missed it.",
        "must_not_show": "no halo, glare or rim-light; the missing MATTER-of-fact — an empty place, an absent friend.",
        "scene": (
            "One man is missing from the "
            "miracle: out in the dark "
            "street Thomas walks alone "
            "with his grief, deep "
            "teal-blue shoulders bowed "
            "under the night, taking the "
            "long way nowhere the way "
            "the freshly bereaved do — "
            "while behind a barred door "
            "somewhere above him the "
            "room he left is filling "
            "with the one joy he will "
            "refuse secondhand. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r099-b06", "out": "s06-and-when-they-told-him.jpeg", "seg": "n2",
        "window": "27.44-31.55", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROOM", "THOMAS", "PETER", "JOHN"],
        "narration": "And when they told him what they had seen, he would not have it.",
        "must_show": "SCRIPTURE-EXACT: the refusal — the room alive with telling, every hand gesturing the story at Thomas; and Thomas planted, arms crossed, head shaking NO.",
        "must_not_show": "no halo, glare or rim-light; the doubt HONEST — grief guarding itself, not cynicism sneering.",
        "scene": (
            "The room throws its joy at "
            "him and it bounces: friends "
            "crowding Thomas from every "
            "side with the story — hands "
            "shaping the standing-there, "
            "the touching, the eating — "
            "and the practical face "
            "under the dark curls "
            "shaking slowly, arms "
            "crossed like a gate: a man "
            "whose heart has been broken "
            "once this week and will "
            "not lend it out again on "
            "anyone's testimony but his "
            "own ten fingers. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r099-b07", "out": "s07-it-was-eight-days-later.jpeg", "seg": "n3",
        "window": "32.00-41.19", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "THOMAS", "PETER", "JOHN"],
        "narration": (
            "It was eight days later when Jesus appeared again — and he "
            "turned straight to Thomas, and offered him that exact proof, in "
            "almost the same words Thomas had used."
        ),
        "must_show": "SCRIPTURE-EXACT: the second standing-in-the-midst — the barred room again, Jesus present at its centre, and his face turned DIRECTLY to Thomas first; the room watching the collision.",
        "must_not_show": "no halo, glare or rim-light, no materialization effects; the turn IMMEDIATE — Thomas the first business of the visit.",
        "scene": (
            "Eight days later, the camera behind the circle's "
            "near backs, the centre "
            "of the room is occupied "
            "again — the beam still in "
            "its brackets, the lamps "
            "mid-flicker — and this time "
            "the visitor's face goes one "
            "place first: straight to "
            "Thomas, across the frozen "
            "room, warm and direct — a "
            "man who was not present for "
            "the doubting, quoting it — "
            "while the doubter stands "
            "pinned by the impossible "
            "courtesy of being the whole "
            "reason for the call. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r099-b08", "out": "s08-that-is-all-thomas-said.jpeg", "seg": "n4a",
        "window": "53.32-54.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["THOMAS"],
        "narration": "That is all Thomas said.",
        "must_show": "the confession's aftermath — close on Thomas's face just after MY LORD AND MY GOD: emptied of doubt, filled to the brim; nothing more to say.",
        "must_not_show": "no halo, glare or rim-light; the fullness QUIET — five words were the whole flood.",
        "scene": (
            "Close on a face with "
            "nothing left to argue: the "
            "sceptical brows unknotted "
            "at last, the practical eyes "
            "shining wet in the "
            "lamplight, the mouth still "
            "half-open from the five "
            "words that emptied it — MY "
            "LORD AND MY GOD — the "
            "biggest confession in the "
            "gospels hanging spent in "
            "the air, and its speaker "
            "standing hollowed and "
            "filled at once, done "
            "talking forever about "
            "proof. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r099-b09", "out": "s09-reach-hither-thy-finger-and.jpeg", "seg": "j2",
        "window": "41.74-51.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["THOMAS"],
        "narration": (
            "Reach hither thy finger, and behold my hands; and reach hither "
            "thy hand, and thrust it into my side: and be not faithless, but "
            "believing."
        ),
        "must_show": "SCRIPTURE-EXACT: the offer — Jesus's open hands held out to Thomas at close range, the invitation total; Thomas's raised hand trembling, NOT touching.",
        "must_not_show": "ABSOLUTE: no graphic wounds or gore — the hands open and alive, the offer carried in gesture and words; Thomas's hand stops short.",
        "scene": (
            "The offer is made at "
            "point-blank range: Jesus's "
            "two hands open before "
            "Thomas's face, near enough "
            "that the lamp-warmth of "
            "them touches his skin — "
            "REACH HITHER — every test "
            "the doubter demanded, "
            "handed over unasked-for and "
            "unresented — and Thomas's "
            "own hand rising, trembling, "
            "toward the proof he swore "
            "he needed... and stopping "
            "in the air, because the "
            "face above the hands has "
            "already finished the "
            "argument. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r099-b10", "out": "s10-he-never-did-reach-out.jpeg", "seg": "n4a",
        "window": "54.79-57.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["THOMAS"],
        "narration": "He never did reach out and touch anything.",
        "must_show": "the untaken test — the trembling hand sinking back down unused, Thomas's eyes on Jesus's face instead; sight of HIM outweighing every demanded proof.",
        "must_not_show": "no halo, glare or rim-light; the hand's descent the picture — the finger never landing.",
        "scene": (
            "The frame watches the "
            "famous test go untaken: "
            "Thomas's raised hand "
            "sinking slowly back down "
            "through the lamplight, "
            "finger uncurled and unused, "
            "the whole demanded "
            "experiment abandoned in "
            "mid-air — because his eyes "
            "have gone up from the "
            "offered hands to the "
            "offering face, and found "
            "there a proof no fingertip "
            "could improve on — the "
            "sceptic's checklist, "
            "outloved. Every figure has "
            "two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r099-b11", "out": "s11-jesus-scold-him-for-doubting.jpeg", "seg": "n4a",
        "window": "57.27-63.39", "wide": True, "jesus": True, "ref": REF,
        "locks": ["ROOM", "THOMAS", "PETER", "JOHN"],
        "narration": (
            "Jesus didn't scold him for doubting — he met the doubt with his "
            "own hands, and the doubt was over."
        ),
        "must_show": "the meeting — the wide room: Jesus and Thomas face to face at its centre, the offered hands between them, the watching circle; doubt ended by approach, not rebuke.",
        "must_not_show": "no halo, glare or rim-light; NO scolding anywhere in his posture — the whole answer was stepping closer.",
        "scene": (
            "The wide lamplit room holds, the camera at the side "
            "so doubter and doubted read in one profile, "
            "the method: at its centre "
            "the doubter and the doubted "
            "face to face, the offered "
            "hands still open between "
            "them, the circle of friends "
            "watching from the walls — "
            "and nowhere in the picture "
            "one grain of rebuke: no "
            "raised finger, no "
            "shamed-you tilt of the "
            "head — a doubt handled the "
            "way he handles everything "
            "broken: by stepping toward "
            "it with his hands open. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r099-b12", "out": "s12-you-believed-because-you-saw.jpeg", "seg": "n4b",
        "window": "63.98-66.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["THOMAS"],
        "narration": "You believed because you saw me, he told him.",
        "must_show": "the gentle verdict — close on the two faces: Jesus's warm summary given to Thomas's undone one; fact stated without sting.",
        "must_not_show": "no halo, glare or rim-light; the verdict WARM — no demotion in it, a hand on the shoulder register.",
        "scene": (
            "Close on the gentle "
            "bookkeeping: Jesus's face "
            "warm over the words — THOU "
            "HAST SEEN, AND BELIEVED — a "
            "fact laid on Thomas's "
            "undone features without one "
            "grain of sting, his hand "
            "coming to rest on the "
            "teal-blue shoulder as he "
            "says it — the seeing-first "
            "believer received whole and "
            "gladly, even as the sentence "
            "turns to face everyone who "
            "will never get to see. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r099-b13", "out": "s13-blessed-are-the-ones-who.jpeg", "seg": "n4b",
        "window": "66.41-73.23", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM", "THOMAS", "PETER", "JOHN"],
        "narration": (
            "Blessed are the ones who have not seen, and believe anyway. "
            "That last line was not about Thomas."
        ),
        "must_show": "SCRIPTURE-EXACT: the blessing beyond the room — Jesus speaking past the circle, his gaze lifting over their heads toward the door and the world beyond; the beatitude aimed outward.",
        "must_not_show": "no halo, glare or rim-light; the gaze's DIRECTION the point — past every face present, toward the unseen future.",
        "scene": (
            "The blessing leaves the "
            "room even as it is spoken: "
            "Jesus's gaze lifting past "
            "Thomas, past Peter and "
            "John, over the heads of "
            "everyone present towards "
            "the barred door and the "
            "dark city and the twenty "
            "centuries beyond it — "
            "BLESSED ARE THEY THAT HAVE "
            "NOT SEEN — a beatitude "
            "addressed over the shoulder "
            "of every eyewitness in the "
            "room, to everyone who will "
            "only ever have the story. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r099-b14", "out": "s14-that-one-was-about-you.jpeg", "seg": "n4b",
        "window": "73.23-78.93", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROOM"],
        "narration": (
            "That one was about you. And that's what he does with honest "
            "doubt — he steps toward it."
        ),
        "must_show": "the closing image — Jesus at the room's centre facing the viewer's direction, hands open in the same offering gesture; the step-toward extended out of the frame.",
        "must_not_show": "no halo, glare or rim-light; the composition ADDRESSED outward — the open hands offered to whoever is looking.",
        "scene": (
            "The closing frame turns the "
            "method on its viewer: Jesus "
            "at the centre of the "
            "lamplit room, facing "
            "outward now, his two hands "
            "open in exactly the gesture "
            "that ended Thomas's doubt — "
            "offered past the lamps, "
            "past the barred door, out "
            "of the picture entirely — "
            "the standing answer to "
            "every honest doubt there "
            "has ever been: not an "
            "argument, an approach; not "
            "a scolding, a step toward. "
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
    "ROOM": "PLACE-REF/room.jpeg",  # build-99-flesh-and-bone-thomas s01-the-disciples-were-hiding-behind (manual)
}
# === end PLACE-PLATES ===
