#!/usr/bin/env python3
"""V2 beat map — row 96, build-96-it-is-finished (John 19:28-30; Luke 23:44-46;
Mark 15:38).

COVERAGE: 13 pictures over 72.9 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (KJV):
  John 19:28  "Jesus knowing that ALL THINGS WERE NOW ACCOMPLISHED" —
        the end approached as completion, not defeat.
  John 19:30  "IT IS FINISHED: and he bowed his head, and gave up the
        ghost." — a declaration, then the head bowed BY CHOICE.
  Luke 23:44  "a DARKNESS over all the earth" from the sixth to the
        ninth hour — the hill's light in this row is an unnatural
        heavy gloom, scriptural, NOT the row-11 defect.
  Luke 23:46  "FATHER, INTO THY HANDS I COMMEND MY SPIRIT."
  Mark 15:38  "the VEIL of the temple was RENT IN TWAIN from the TOP
        TO THE BOTTOM." — across the city, at that instant; torn from
        ABOVE.

CRUCIFIXION RENDERING LAW (as rows 94-95, same hill): all violence
OFF-SCREEN — no nails, blood, wounds or gore anywhere; closes are
chest-or-face-up with dignity absolute; the death itself is the bowed
head and stillness, nothing more. On the cross Jesus wears the plain
undyed cream linen wrap.

TIME OF DAY: the Luke 23:44 DARKNESS — a heavy unnatural gloom over
the hill, deeper than any storm-dusk, thinning only at the row's end;
the temple interior in its own lamplit dimness.

CHANGING CONDITION (kept OUT of the locks): the light — the great
darkness, then the first thinning after death; the veil — whole, then
torn top to bottom; his head — lifted for the words, then bowed.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "HILL": (
        "HILL LOCK: Calvary under the great darkness — the bare "
        "rounded rock rise with its THREE raised wooden crosses, the "
        "sky pressed low and heavy with an unnatural gloom, the city "
        "wall barely visible in the murk, small knots of watchers on "
        "the slope. The same rise, crosses and darkness throughout."
    ),
    "TEMPLE": (
        "TEMPLE LOCK: the temple's holy place — a tall dim hall of "
        "gold-sheathed cedar lit by the seven-branched lampstand, "
        "and across its full height the GREAT VEIL: a massive woven "
        "curtain of DEEP BLUE, PURPLE and SCARLET, thick as a man's "
        "hand, floor to distant ceiling. The same hall, lampstand "
        "and veil throughout."
    ),
    "PRIEST": (
        "PRIEST LOCK: the duty priest is the same man in every "
        "temple shot — about fifty, grey-bearded, in DARK BLUE "
        "priestly robes with a woven sash (never cream, never "
        "white); reverent, and utterly unprepared."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): narration mp3s are newer
# than the V1 mp4 (recency gate fails) and |Δ|>1.0, so the packet-copy AUDIO LOCK
# would ship stale voices. Rebuild from this build's own mp3 segments — $0.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r096-b01", "out": "s01-at-the-very-end-jesus.jpeg", "seg": "n0",
        "window": "0.28-3.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "At the very end, Jesus knew everything had now been accomplished.",
        "must_show": "SCRIPTURE-EXACT: knowing all accomplished — the darkened hill, the centre cross; Jesus's face lifted and lucid in the gloom: a worker surveying a finished work.",
        "must_not_show": "ABSOLUTE: no nails, blood, wounds or gore; the face CLEAR-EYED — knowledge, not delirium.",
        "scene": (
            "Under the strange heavy dark "
            "that has swallowed the "
            "afternoon, the centre cross "
            "holds a lucid face: lifted, "
            "clear-eyed in the gloom, "
            "moving slowly over the hill "
            "and the murk-hidden city "
            "like a builder's eyes over a "
            "finished roof — checking the "
            "long list one last time and "
            "finding, at the very end of "
            "strength, every single line "
            "of it done. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r096-b02", "out": "s02-he-a-victim-losing-a.jpeg", "seg": "n0",
        "window": "3.53-7.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "He wasn't a victim losing a fight — he was finishing a work.",
        "must_show": "the reframe — close on the face in the darkness: exhaustion total, defeat absent; the countenance of completion, not collapse.",
        "must_not_show": "ABSOLUTE: no wounds or blood; NOTHING of the victim in the eyes — agency held to the last.",
        "scene": (
            "Close on the distinction the "
            "whole world would misread: "
            "the face drained to its last "
            "reserves, breath shallow, "
            "the end plainly near — and "
            "in the eyes not one flicker "
            "of a man losing anything: "
            "the steady, spending look of "
            "a craftsman driving the "
            "final peg of a work begun "
            "before the foundations of "
            "the world, on schedule, on "
            "purpose, almost home. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r096-b03", "out": "s03-with-his-last-breath-he.jpeg", "seg": "n1",
        "window": "8.39-14.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": (
            "With his last breath he spoke three words that weren't a cry of "
            "defeat, but a declaration of completion."
        ),
        "must_show": "the gathering breath — the darkened hill hushing; the chest rising for the last words; watchers on the slope turning up toward the voice about to come.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the hill LISTENING — faces lifting in the gloom.",
        "scene": (
            "The darkened hill feels it "
            "coming: on the centre cross "
            "the chest rises with a "
            "gathered, deliberate breath — "
            "the kind drawn for saying, "
            "not surviving — and along "
            "the murky slope the "
            "scattered watchers turn up "
            "their faces one by one, "
            "soldiers and mourners alike, "
            "pulled by the same "
            "instinct: something is about "
            "to be said from up there, "
            "and it will matter forever. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r096-b04", "out": "s04-it-is-finished-not-i.jpeg", "seg": "n1b",
        "window": "18.19-20.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "It is finished. Not I am finished.",
        "must_show": "the distinction — close on the face at the words: IT — the work — finished; the grammar of victory readable in the steady dying features.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the emphasis VICTORIOUS — a completed object, not a failing subject.",
        "scene": (
            "Close on three words doing "
            "the opposite of what dying "
            "words do: the lips shaping "
            "IT — not I — the failing "
            "voice laying the emphasis "
            "with perfect care on the "
            "work and not the worker — a "
            "declaration filed from a "
            "cross with the precision of "
            "a signature: the debt-note "
            "cancelled, the task closed "
            "out, the object finished "
            "while its maker's eyes are "
            "still open to say so. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r096-b05", "out": "s05-the-thing-he-came-to.jpeg", "seg": "n1b",
        "window": "20.53-26.22", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": (
            "The thing he came to do was done — completed, paid in full, "
            "nothing left owing."
        ),
        "must_show": "the paid-in-full — the whole darkened hill at the declaration: stillness over slope and crosses; a ledger closed over the world.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the stillness TOTAL — the moment after the greatest receipt ever issued.",
        "scene": (
            "The declaration settles, the camera down the slope "
            "behind the stilled watchers, over "
            "the whole dark hill like a "
            "seal pressed into wax: the "
            "three crosses still against "
            "the heavy sky, the watchers "
            "stopped mid-breath on the "
            "slope, even the soldiers' "
            "dice quiet on the rock — "
            "the longest account in "
            "creation — every debt of "
            "every soul on every page — "
            "ruled off, summed, and "
            "stamped in three words: paid "
            "in full. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r096-b06", "out": "s06-father-into-thy-hands-i.jpeg", "seg": "jv46",
        "window": "26.81-29.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "Father, into thy hands I commend my spirit.",
        "must_show": "SCRIPTURE-EXACT: the commendation — close on the face lifted a last time to the dark sky: trust total, fear absent; a son handing himself home.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the words TRUST, not surrender to death — the destination is hands, not dark.",
        "scene": (
            "The last words go where all "
            "the night's words went: "
            "FATHER — the face lifting a "
            "final time into the heavy "
            "dark, and finding there, "
            "where every other eye on the "
            "hill sees only gloom, the "
            "hands he has trusted since "
            "before light existed — INTO "
            "THY HANDS — a son handing "
            "himself across the last "
            "distance with the ease of a "
            "child passed over a "
            "threshold, home. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r096-b07", "out": "s07-the-last-words-he-said.jpeg", "seg": "n1c + s30b",
        "window": "31.14-39.63", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": (
            "The last words he said were words of trust, spoken to the "
            "Father he had been talking to all night. And he bowed his head, "
            "and gave up the ghost."
        ),
        "must_show": "SCRIPTURE-EXACT: the bowed head — the centre cross in the darkness: the head lowering with deliberate grace to rest; the giving-up an ACT, and then the great stillness.",
        "must_not_show": "ABSOLUTE: no wounds, blood or death-agony — the head BOWS as a chosen motion; dignity complete in the stillness.",
        "scene": (
            "And then the hill watches a "
            "man finish: the head on the "
            "centre cross lowering — not "
            "dropping, LOWERING, with the "
            "same deliberate grace it "
            "bowed over bread and over "
            "children — coming to rest "
            "against the quiet chest — "
            "and the great stillness "
            "arriving over the darkened "
            "rise like snowfall: the "
            "life not torn from him at "
            "the end but handed, breath "
            "by counted breath, exactly "
            "where he said it was going. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r096-b08", "out": "s08-nobody-took-his-life-from.jpeg", "seg": "n2",
        "window": "41.13-44.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "Nobody took his life from him. He laid it down.",
        "must_show": "the laid-down life — the bowed head at rest against the dark, peace absolute in the stilled face; agency's last proof.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the stillness PEACE, not ruin — a life set down like a garment folded.",
        "scene": (
            "Close on the proof of the "
            "claim: the bowed head at "
            "rest against the heavy dark, "
            "and on the stilled face not "
            "one mark of the robbed — no "
            "twist of protest, no frozen "
            "fight — only the deep "
            "finished peace of a thing "
            "set down on purpose, the "
            "way a workman folds his "
            "apron at the end of the "
            "day: nobody took it; it was "
            "laid, precisely, where it "
            "was always going to be "
            "laid. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r096-b09", "out": "s09-and-behold-the-veil-of.jpeg", "seg": "s51",
        "window": "44.88-49.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": (
            "And, behold, the veil of the temple was rent in twain from the "
            "top to the bottom."
        ),
        "must_show": "SCRIPTURE-EXACT: the rending — the great blue-purple-scarlet veil splitting DOWN FROM THE TOP in the tall lamplit hall, the tear racing floorward; the moment itself.",
        "must_not_show": "no figure tearing it — the split begins at the TOP, above all reach; no halo, glare or rim-light.",
        "scene": (
            "In the tall dim hall across "
            "the city the impossible "
            "happens to the veil: high at "
            "its top edge, far above any "
            "ladder or reach, the massive "
            "weave PARTS — and the tear "
            "runs downward, fast, "
            "unstoppable, blue and purple "
            "and scarlet peeling open in "
            "a long widening line from "
            "ceiling toward floor, the "
            "lampstand's flames bending "
            "in the moved air of a "
            "curtain no hand on earth is "
            "touching. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r096-b10", "out": "s10-at-that-moment-in-the.jpeg", "seg": "n3a",
        "window": "51.15-60.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE", "PRIEST"],
        "narration": (
            "At that moment, in the temple across the city, the great veil "
            "that walled off the holiest place was torn in two, from the top "
            "down —"
        ),
        "must_show": "the witness — the duty priest fallen back a step before the torn-open veil, lamplight from the hall falling into the once-sealed dark beyond; awe and terror together.",
        "must_not_show": "no halo, glare or rim-light effects; the space BEYOND the veil shown as deep sacred dimness — no ark or objects detailed.",
        "scene": (
            "The duty priest is the one "
            "who sees it: fallen back a "
            "full step with his censer "
            "swinging, staring up the "
            "hall's height at the great "
            "curtain hanging in two "
            "sundered halves — and "
            "through the impossible gap, "
            "for the first time in his "
            "life or his father's or his "
            "father's father's, the "
            "lamplight leaning into the "
            "deep sacred dark beyond — a "
            "wall of centuries standing "
            "open like a door. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r096-b11", "out": "s11-it-is-finished.jpeg", "seg": "j1",
        "window": "15.40-16.61", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "It is finished.",
        "must_show": "SCRIPTURE-EXACT: the words themselves — close on the face speaking them into the darkness: the declaration at its instant, clear and final.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the delivery a DECLARATION — firm, not faint.",
        "scene": (
            "Close on the instant itself: "
            "the drawn face steady in "
            "the unnatural dark, the "
            "cracked lips moving once — "
            "IT IS FINISHED — three words "
            "spent with the last coin of "
            "breath and landing with the "
            "weight of a hammer on an "
            "anvil: not a whisper "
            "escaping a dying man, but a "
            "verdict pronounced by the "
            "only judge with standing to "
            "close the case of the whole "
            "world. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r096-b12", "out": "s12-as-if-torn-by-a.jpeg", "seg": "n3b + n4a",
        "window": "60.74-66.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": (
            "as if torn by a hand from above. That curtain had kept people "
            "out of God's presence for centuries."
        ),
        "must_show": "the top-down evidence — close on the veil's torn upper edge high in the lamplight: the rend clean and from above, the thick weave parted like paper.",
        "must_not_show": "no hand or figure shown doing it; no halo or light-effects — the torn edge itself the whole testimony.",
        "scene": (
            "Close on the evidence, high "
            "where no ladder reaches: the "
            "veil's torn upper edge in "
            "the lamplight, the weave "
            "thick as a man's hand parted "
            "clean as paper, the threads "
            "of blue and purple and "
            "scarlet hanging severed from "
            "the very top downward — a "
            "tear that reads its own "
            "direction: begun above, "
            "finished below, by a hand "
            "that was never on this side "
            "of the curtain at all. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r096-b13", "out": "s13-the-instant-he-died-it.jpeg", "seg": "n4a + n4b",
        "window": "66.76-72.52", "wide": True, "jesus": False, "ref": False,
        "locks": ["TEMPLE"],
        "narration": (
            "The instant he died, it was ripped open. The way in was thrown "
            "wide — for everyone."
        ),
        "must_show": "the closing image — the hall wide: the great veil hanging fully open in two halves, the way through standing unbarred, lamplight reaching in; the open way as the final picture.",
        "must_not_show": "no halo or light-effects; the gap UNGUARDED — no priest barring it, the openness the entire meaning.",
        "scene": (
            "The closing frame holds, the camera down the hall's "
            "length behind the empty court, the "
            "new architecture of the "
            "universe: the tall hall with "
            "the great curtain hanging in "
            "two stilled halves, and "
            "between them — open, "
            "unbarred, unguarded — the "
            "way in: lamplight reaching "
            "through the centuries-sealed "
            "gap into the holiest dark, "
            "and no one, ever again, "
            "standing in the doorway to "
            "ask who goes there — thrown "
            "wide at the instant of his "
            "going, for everyone, for "
            "good. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # HILL deliberately UNWIRED (see rows 94/95): the build-38 golden
    # village frame is wrong for Golgotha. Take row 94's approved HILL.
    "TEMPLE": "PLACE-REF/temple.jpeg",  # build-06-two-sons v2-r006-b21
}
# === end PLACE-PLATES ===
