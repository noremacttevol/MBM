#!/usr/bin/env python3
"""V2 beat map — row 136, build-136-healed-in-two-touches (Mark 8:22-26).

COVERAGE: 10 pictures over 56.3 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 8 KJV):
  8:22  "they bring a BLIND MAN unto him, and BESOUGHT him to touch
        him" — at BETHSAIDA.
  8:23  "he took the blind man BY THE HAND, and LED HIM OUT OF THE
        TOWN; and when he had spit on his eyes, and put his hands
        upon him, he asked him if he saw ought."
  8:24  "I see men AS TREES, WALKING." — the half-sight.
  8:25  "he put his hands AGAIN upon his eyes, and made him look up:
        and he was restored, and saw every man CLEARLY."
  8:26  "Neither go into the town, nor tell it to any in the town."

RENDERING LAWS:
  - THE BLIND MAN with full dignity (row-15 class): warm living
    skin, clouded unfocused eyes early, no disfigurement; his
    blindness carried by the reaching hands and guided walk.
  - THE SPITTING IS NEVER RENDERED AS FLUID: b03's moistening is
    implied entirely by posture — Jesus's thumbs at the closed
    eyelids, head bent close; discreet, tender, scripture-exact
    without literalism.
  - THE TREES-WALKING BEAT (b04) is the row's famous image: the
    background figures are SOFTLY BLURRED, tall and swaying,
    deliberately tree-like — intentional blur, not a phantom-people
    defect (state it: the blur is the man's half-vision, painted).
  - The two touches must be the SAME gesture repeated (b03/b06) —
    prop-board the hand positions; the second touch is the rhyme.
  - Jesus never scolds the honest half-report (b05) — warmth at the
    man's exact truthfulness.
  - Direction law: b02 leads OUT of the village (away from gate);
    b10 sends him HOME by the away-road, not back through town.

TIME OF DAY ARC (intentional): one soft clear morning throughout —
the kind of light where every leaf reads; the close in full
mid-morning clarity (the light itself mirrors the healing).

CHANGING CONDITION (kept OUT of the locks): the man's eyes —
clouded, then half-clear, then fully clear; his hands — reaching,
then steady at his sides.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "VILLAGE": (
        "VILLAGE LOCK: Bethsaida's edge — a fishing village's last "
        "lane and low gate, pale stone houses, nets drying on "
        "walls, the lake glinting beyond rooftops; outside the "
        "gate, an open path between fig trees and tall grass. The "
        "same gate, path and trees throughout."
    ),
    "BLINDMAN": (
        "BLINDMAN LOCK: the blind man is the same man in every "
        "shot — about forty-five, sturdy, a short dark beard, in a "
        "DARK TEAL-BLUE tunic with a brown cloth belt (never cream, "
        "never white); warm living skin, dignity total; his eyes "
        "clouded and unfocused until healed."
    ),
    "FRIENDS": (
        "FRIENDS LOCK: the friends — two loyal neighbours, one "
        "stocky in DARK RUST, one lean in DARK OLIVE (no cream); "
        "earnest working men, protective of their friend."
    ),
}

REF = True

# STALE-V1 fix (audio lane, 2026-08-11): rebuild the audio track from the V1
# segment mp3s at the extract_beats offsets instead of copying the stale V1
# mp4's AAC (which fails assert_v1_final_is_current). Re-voices nothing ($0).
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r136-b01", "out": "s01-friends-brought-a-blind-man.jpeg", "seg": "n0",
        "window": "0.28-5.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["VILLAGE", "BLINDMAN", "FRIENDS"],
        "narration": (
            "Friends brought a blind man to Jesus in Bethsaida and begged "
            "Him just to touch him."
        ),
        "must_show": "the bringing — the two friends guiding the blind man by the arms through the village lane to Jesus, their begging visible; his trust in their hands.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the man's dignity total — guided, not dragged; the friends' plea earnest.",
        "scene": (
            "Friendship does the seeing for him, the camera "
            "looking down the lane past the little group's "
            "backs: the two neighbours guide the blind man "
            "between them through Bethsaida's last lane — one "
            "steadying each arm, his feet trusting their "
            "steering completely — and bring him to a stop "
            "before Jesus with their plea already pouring out: "
            "just TOUCH him, Master — two working men spending "
            "their morning and their boldness on a friend's "
            "darkness. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r136-b02", "out": "s02-jesus-took-the-man-by.jpeg", "seg": "n1a",
        "window": "5.92-9.18", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VILLAGE", "BLINDMAN"],
        "narration": "Jesus took the man by the hand and walked him outside the village.",
        "must_show": "SCRIPTURE-EXACT: the hand-in-hand walk — Jesus leading the blind man by the hand OUT through the low gate onto the open path; the personal, unhurried leading.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION — outward through the gate, away from town; the handhold the picture.",
        "scene": (
            "The healer takes the patient's hand like a friend "
            "leaving a party: Jesus leads the blind man out "
            "through the low village gate onto the open path — "
            "fingers wrapped warm around the reaching hand, "
            "pace set to the shuffling careful feet, fig "
            "trees and tall grass opening around them as the "
            "village noise falls away behind — no crowd "
            "invited, no audience kept: one man being walked "
            "into his healing by the hand, at exactly his own "
            "speed. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r136-b03", "out": "s03-he-spit-on-the-eyes.jpeg", "seg": "n1b",
        "window": "9.85-15.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VILLAGE", "BLINDMAN"],
        "narration": (
            "He spit on the man's eyes and laid His hands on him, then asked "
            "if he could see anything yet."
        ),
        "must_show": "SCRIPTURE-EXACT, DISCREET — the first touch: Jesus's head bent close, thumbs resting gently at the man's closed eyelids, the question forming; the moistening implied by posture ONLY.",
        "must_not_show": "ABSOLUTE: no fluid rendered — the act carried by the bent head and thumbs at the lids; tenderness total.",
        "scene": (
            "The first touch is closer than medicine ever "
            "gets: Jesus's head bent near, his thumbs resting "
            "with feather care on the man's closed eyelids, "
            "the strong carpenter's hands cradling the "
            "trusting face between them — the old remedy "
            "given the intimate way, nothing hurried, "
            "nothing clinical — and then the low question, "
            "asked against the closed eyes like a knock at a "
            "shuttered window: anything? do you see anything "
            "yet? Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r136-b04", "out": "s04-the-man-looked-up-and.jpeg", "seg": "n2",
        "window": "15.63-22.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BLINDMAN"],
        "narration": (
            "The man looked up and said the strangest thing — he could see, "
            "but only halfway. People looked like trees walking around."
        ),
        "must_show": "SCRIPTURE-EXACT: the trees-walking — the man squinting toward the path where distant figures stand DELIBERATELY soft-blurred, tall and swaying like trees; his half-vision painted as intentional blur.",
        "must_not_show": "no halo; the blur INTENTIONAL (his half-sight, not a render defect) — the distant figures softly tree-like, the near world crisp.",
        "scene": (
            "What half a miracle looks like from the inside: "
            "the man's newly opened eyes squint down the "
            "path, wonder and confusion sharing his face — "
            "and there in the middle distance the figures of "
            "passing villagers stand deliberately soft and "
            "blurred, tall swaying shapes with their edges "
            "feathered into the light, more like fig trees "
            "given legs than men — sight, real sight, "
            "arrived at half-focus — and the honest mouth "
            "reporting exactly that: trees, walking. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r136-b05", "out": "s05-his-first-glimpse-was-real.jpeg", "seg": "n2",
        "window": "22.76-28.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": (
            "His first glimpse was real, but unfinished. Jesus did not scold "
            "him for saying so."
        ),
        "must_show": "the unscolded honesty — Jesus's face warm and unhurried at the man's exact truthful report; no disappointment anywhere; the man's half-focused eyes still searching.",
        "must_not_show": "no halo, glare or rim-light on Jesus; ZERO impatience — the warmth at honesty is the frame.",
        "scene": (
            "The honest report gets the warmest reception of "
            "the morning: Jesus listens to trees-walking with "
            "his whole unhurried attention, and nothing in "
            "the deep brown eyes flickers toward "
            "disappointment — no wince at the incomplete "
            "result, no correction of the strange words — "
            "only the settled warmth of a healer who prefers "
            "a true half-report to a polite whole one, "
            "already lifting his hands for the rest of the "
            "work. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r136-b06", "out": "s06-so-jesus-put-his-hands.jpeg", "seg": "n3",
        "window": "29.09-33.82", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VILLAGE", "BLINDMAN"],
        "narration": (
            "So Jesus put His hands on the man's eyes a second time and told "
            "him to look up again."
        ),
        "must_show": "SCRIPTURE-EXACT: the second touch — the SAME gesture repeated: hands at the eyes again, the man's face lifted per the instruction; the rhyme of touches exact.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hand positions MATCHING b03's — same touch, second application.",
        "scene": (
            "The same touch comes back to finish its "
            "sentence: Jesus's hands return to the man's "
            "eyes in exactly the first gesture — thumbs at "
            "the lids, palms warm along the temples — and "
            "this time the instruction tilts the trusting "
            "face upward toward the bright morning: look UP, "
            "look again — the second application of a mercy "
            "that was never in doubt, only in progress, "
            "administered with the patience of a workman who "
            "always intended two coats. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r136-b07", "out": "s07-and-this-time-he-saw.jpeg", "seg": "n4",
        "window": "34.45-39.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BLINDMAN"],
        "narration": "And this time he saw everything clearly — every face, every leaf.",
        "must_show": "the clear sight — the man's face blazing with detail-joy: a fig leaf held close in his fingers, every vein sharp; beyond it the path's figures now CRISP; the world in focus.",
        "must_not_show": "no halo; EVERYTHING crisp now — the contrast with b04's blur total; his joy specific, not generic.",
        "scene": (
            "The world arrives in full resolution all at "
            "once: the man holds a fig leaf up close in his "
            "trembling fingers and reads it like scripture — "
            "every vein, every serration, the green of it "
            "almost too much — while past the leaf the path "
            "stands crisp to the last pebble, the villagers "
            "walking it now unmistakably PEOPLE, faces and "
            "hands and individual eyes — creation handed "
            "over detail by detail to a man drinking it in "
            "leaf-first, the way the newly seeing do. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r136-b08", "out": "s08-the-second-touch-finished-what.jpeg", "seg": "n4",
        "window": "39.22-42.54", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BLINDMAN"],
        "narration": "The second touch finished what the first had started.",
        "must_show": "the finishing — Jesus's hands lowering from the healed face, both men's eyes meeting CLEARLY for the first time; quiet completion, shared warmth.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the FIRST clear eye-contact between them — the healed eyes seeing their healer.",
        "scene": (
            "The first thing the finished eyes focus on is "
            "their craftsman: Jesus's hands lower slowly from "
            "the healed face, and the man's clear new eyes "
            "find his — the first true eye-contact of the "
            "whole story, patient and healer regarding each "
            "other in the bright morning with the work "
            "complete between them — no fanfare for the "
            "finish, just two men and a quiet warmth, one "
            "job done thoroughly by Someone who never leaves "
            "a healing half-painted. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r136-b09", "out": "s09-the-story-never-explains-why.jpeg", "seg": "n4",
        "window": "42.54-51.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "BLINDMAN"],
        "narration": (
            "The story never explains why healing came in stages. It simply "
            "shows that an unfinished beginning was not the end."
        ),
        "must_show": "the meaning — the man standing tall on the open path looking FAR down its length toward the horizon: half-sight remembered, full sight forward; unfinished-was-not-the-end in one gaze.",
        "must_not_show": "no halo; his stance CHANGED — steady, unguided, hands free; the long clear view the doctrine.",
        "scene": (
            "The moral stands on the path looking as far as "
            "light goes: the man upright and unguided, hands "
            "free at his sides for the first time in years, "
            "his clear eyes running the whole open road to "
            "its horizon — hills sharp, sky deep, distance "
            "itself given back to him — a man who half an "
            "hour ago saw walking trees, now seeing to the "
            "edge of the world, living proof that an "
            "unfinished beginning was never once the end of "
            "the story. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r136-b10", "out": "s10-neither-go-into-the-town.jpeg", "seg": "j1",
        "window": "51.74-55.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VILLAGE", "BLINDMAN"],
        "narration": "Neither go into the town, nor tell it to any in the town.",
        "must_show": "SCRIPTURE-EXACT: the quiet sending — Jesus's gentle directing hand pointing the man to the HOME-ward path away from the village gate; the man setting off that way; secrecy as kindness.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION — the man's steps aimed AWAY from the town gate, along the home path.",
        "scene": (
            "The healing ends with a quiet map: Jesus's hand "
            "directs gently PAST the village gate toward the "
            "farther path that runs home through the fig "
            "trees — not into the town, not to the telling — "
            "and the man sets off the way he is sent, "
            "walking his first unguided road with the "
            "morning bright around him and his miracle "
            "folded private in his chest — sight for the "
            "road, silence for the town, and home, seen "
            "clearly, waiting at the path's far end. Every "
            "figure has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # VILLAGE: build-38 b46 auto-match REJECTED yet again (doorway corner,
    # arid hills — not a lakeside fishing village with nets and gate).
    # FRIENDS --take from build-13 also REJECTED (roof-story friends are
    # different characters). Promote-first VILLAGE from b01.
}
# === end PLACE-PLATES ===
