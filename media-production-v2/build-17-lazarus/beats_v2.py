#!/usr/bin/env python3
"""V2 beat map — row 17, build-17-lazarus (John 11:1-44).

COVERAGE: 61 pictures over 316.5 s = 5.2 s/picture (matches the library
density). Authored 2026-08-05 directly to lessons 11-12 (movie coverage).

LESSON-12 SHAPE: five true wides, each stating camera-to-back geometry in
its own scene text: b01 (Bethany-house establish), b15 (tomb establish),
b21 (Martha's run), b33 (the road dissolved in grief), b55 (the frozen
crowd). Everything else is a single, two-shot, over-shoulder or insert
containing only the people its moment is about. The raising is covered a
frame per action (the John 21 standard): the call formed (b49), the shout
(b50), first sight in the dark (b51), the emergence (b52), standing bound
(b53), the wrapped face in light (b54), the frozen crowd (b55), the
release command (b56), the unwrapping (b57).

SCRIPTURE FACTS (John 11 KJV):
  v1-3   Bethany, the town of Mary and Martha; "Lord, behold, he whom thou
         lovest is sick" — the sisters SEND word; the message travels.
  v4     "This sickness is not unto death, but for the glory of God."
  v6     "he abode two days still in the same place where he was" — the
         deliberate stillness is the story's scandal; he was beyond Jordan
         (John 10:40), an outdoor riverside place.
  v17    Lazarus "had lain in the grave four days already" — past the
         folk belief that a soul lingered three days: the door is shut.
  v20    "Martha, as soon as she heard that Jesus was coming, went and met
         him: but Mary sat still in the house." Martha RUNS; the meeting
         is on the road OUTSIDE town.
  v21-27 grief and faith in one breath; "I AM the resurrection, and the
         life"; Martha's confession.
  v32-35 Mary falls at his feet; the mourners weep; "JESUS WEPT" — he
         weeps KNOWING what he is about to do; grief honoured, not
         skipped.
  v38-39 "It was a cave, and a stone lay upon it. Jesus said, Take ye
         away the stone." Martha: "by this time he stinketh."
  v40-41 "Said I not unto thee..."; THEY took away the stone (men roll
         it — a real heave, not magic).
  v41-43 he prays ALOUD for the crowd's sake, then "he cried with a loud
         voice, Lazarus, come forth."
  v44    "he that was dead came forth, BOUND hand and foot with
         graveclothes: and his face was bound about with a napkin. Jesus
         saith unto them, Loose him, and let him go." The unwrapping is
         done by OTHERS at his command.

TIME OF DAY: full daylight throughout (the crowds, the visible action,
and the narration's own line — "the dark mouth of the grave stood open to
the daylight"). b13 (the sisters watching the empty road) is dusk at the
house; b01-b05 are ordinary warm daylight before the sickness turns.

CAST LINEAGE (face-board law): MARTHA and MARY are the SAME two women as
build-16-mary-martha — their locks below are byte-identical copies of
build-16's, and the runner must face-match both against build-16's
approved stills before assembly. Jesus is the global JESUS-V2-REF.
LAZARUS, MESSENGER and the mourners are new to this row.

CHANGING CONDITION (kept OUT of the locks): Lazarus's state — well
(b01-b03), fevered (b04), a bound wrapped form (b51-b54), unwrapped and
alive in loosened grave-linen with a borrowed dark mantle (b57-b61); and
the tomb stone — SEALED (b15, b16, b37, b41), mid-roll (b46), OPEN from
b47 on. Both stated per-beat.

CONTENT-CARE: sickness and death are shown with dignity — no gore, no
decay, no horror styling on the bound figure (clean linen, upright
stance, full daylight). Grief is real and honoured; Jesus's weeping is
reverent, never staged.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream. MARTHA and MARY are byte-identical to build-16.
LOCKS = {
    "MARTHA": (
        "MARTHA LOCK: Martha is the same woman in every shot — about "
        "thirty-five, the older sister, strong-boned and capable, broader "
        "through the shoulders, warm olive-brown skin, dark hair bound back "
        "tightly under a practical DARK-OCHRE headcloth with loose strands "
        "stuck to her damp forehead, level dark brows and a direct, "
        "intelligent face. She wears a hard-wearing DEEP RUSSET-BROWN wool "
        "dress with the sleeves pushed back and a work-stained apron-cloth "
        "at her waist (never cream, never white). Her hands are strong and "
        "red from work. Her face is shown clearly and is never shrewish. "
        "HER HAIR IS ALWAYS BOUND UP AND COVERED BY THE DARK-OCHRE "
        "HEADCLOTH — it never hangs loose or flows over her shoulders. Her "
        "skin is WARM OLIVE-BROWN and sun-worked, the same tone in every "
        "shot. Her clothing is first-century hand-woven wool: a simple "
        "pull-over dress with no buttons, no fastenings and no tailoring, "
        "a plain rectangle of coarse cloth tied at the waist as an apron, "
        "and plain leather sandals or bare feet — never a bib apron, never "
        "closed shoes or boots."
    ),
    "MARY": (
        "MARY LOCK: Mary is the same woman in every shot — about "
        "twenty-eight, the younger sister, plainly related to Martha with "
        "the same warm olive-brown skin and the same dark brows, but "
        "slighter, narrower-featured and quieter. Her dark hair is loosely "
        "gathered and falling over one shoulder, uncovered. She wears a "
        "soft DUSTY-INDIGO wool dress with a plain sash (never cream, "
        "never white). HER HEAD IS ALWAYS UNCOVERED — she wears no "
        "headscarf, veil, hood or head covering of any kind in any shot, "
        "and her dark hair is plainly visible. Her skin is the same WARM "
        "OLIVE-BROWN as her sister's in every shot. Her face is shown "
        "clearly and is calm and absorbed."
    ),
    "LAZARUS": (
        "LAZARUS LOCK: Lazarus is the same man in every shot — about "
        "thirty, the younger brother, lean and open-faced with deep smile "
        "lines, warm olive-brown skin like his sisters', thick black hair "
        "and a close-trimmed black beard. When clothed and well he wears a "
        "DARK OLIVE-GREEN tunic with a plain sash (never cream, never "
        "white). His face is shown clearly — a man people are glad to sit "
        "beside."
    ),
    "MESSENGER": (
        "MESSENGER LOCK: the sisters' runner is the same youth in every "
        "shot — about sixteen, wiry and long-legged, sun-darkened, with "
        "short black curls and no beard, in a knee-length DUSTY "
        "CHARCOAL-GREY tunic cinched with a cord (never cream, never "
        "white), road dust on his shins and plain flat sandals."
    ),
    "MOURNERS": (
        "MOURNERS LOCK: the mourners of Bethany are distinct individual "
        "men and women of every age — no two share a face — all in DEEP "
        "MOURNING DARKS: charcoal, near-black brown, deep umber and "
        "grey-indigo wool, several of the women with dark head-cloths "
        "drawn low over their brows. Grief is carried in real, varied "
        "postures — a fist pressed to a mouth, a bowed head, a supported "
        "elder. Not one of them wears cream, off-white or any pale cloth."
    ),
    "BETHANY-HOUSE": (
        "BETHANY HOUSE LOCK: the family home in Bethany — a comfortable "
        "village house of warm honey-coloured stone with a walled "
        "courtyard, a low timber gate to the road, a shading fig tree, a "
        "stone bench against the house wall, and inside, one main room "
        "with a beaten-earth floor, woven rush mats, a low table with "
        "cushions, a small cooking hearth and shelves of clay jars. The "
        "same walls, gate, tree, bench and room throughout."
    ),
    "JORDAN-CAMP": (
        "JORDAN CAMP LOCK: the place beyond Jordan where the news "
        "arrives — a dry open riverside with the shallow green-brown "
        "river sliding past reed beds, a few grey tamarisks and worn "
        "limestone shelves for sitting, a small blackened cook-fire ring, "
        "and the bare Judean hills standing far off across the water. The "
        "same bank, stones and skyline throughout."
    ),
    "BETHANY-ROAD": (
        "BETHANY ROAD LOCK: the road outside the village — a pale "
        "packed-dirt and loose-stone road curving along a dry hillside of "
        "scrub, thistle and grey field-stone walls, with the flat-roofed "
        "honey-stone edge of the village visible at one end and open "
        "country at the other. The same road, walls and hillside "
        "throughout."
    ),
    "TOMB": (
        "TOMB LOCK: the family tomb outside Bethany — a burial cave cut "
        "into a low limestone hillside, its squared dark doorway reached "
        "by a shallow worn ramp, closed by ONE great round-edged "
        "wheel-like stone slab that rolls in a cut channel across the "
        "mouth, with dry grass, thistle and grey field-stone terracing on "
        "the slope around it and open daylight country beyond. The same "
        "cave, channel, stone and slope throughout."
    ),
}

REF = True

# Canonical face anchors (face-board law). MARTHA/MARY have no CAST-V2-REF
# sheets (their GLOBAL_CAST stems are None), so without these the sisters
# would render from text only — guaranteed identity drift across 40 beats.
# Author's canonical picks from build-16's approved stills (2026-08-05):
# s18 for Martha (largest sharpest face, dark-ochre headcloth matches her
# lock exactly); s10 for Mary (the only front-facing open-eyed view — the
# frontal geometry is what carries identity). These two frames ARE the
# sisters from now on.
REFS = {
    "MARTHA": "../build-16-mary-martha/assets/s18-martha-martha.jpeg",
    "MARY": "../build-16-mary-martha/assets/s10-the-place-a-student-sat.jpeg",
    # Runner-merged 2026-08-05: v2_story_cast generated CAST-REF-V2/lazarus.jpeg
    # from the LAZARUS lock but could not auto-append it (the manual MARTHA/MARY
    # REFS above already existed, so its append-if-absent write was skipped).
    # Wiring it here completes the author's stated intent ("story_cast handles
    # LAZARUS"). Holds Lazarus's face across b01-b04 (alive) and b57-b60 (raised).
    "LAZARUS": "CAST-REF-V2/lazarus.jpeg",
}

# Runner-set 2026-08-05 (Machine A), same pattern as build-25. The AUDIO LOCK
# stale-V1 guard fired: the V1 render john-11_lazarus.mp4 on disk is 184.5s, but
# the authoritative narration (the re-voiced V1 segment mp3s that these 61 beats
# were authored to) is ~314s — and the reviewer card already lists this row as
# 5:14. The V1 MP4 is simply an out-of-date render from before the re-voice; the
# assembler rebuilds the audio track from the V1 mp3 segments (new-voice, the
# AUTHOR-BOARD Audio=OK set) and hash-verifies it. This is exactly the tool's
# prescribed FIX for this guard.
AUDIO_FROM_V1_SEGMENTS = True

BEATS = [
    {
        "id": "v2-r017-b01", "out": "s01-in-a-village-called-bethany.jpeg", "seg": "n0",
        "window": "0.28-9.01", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "LAZARUS", "BETHANY-HOUSE"],
        "narration": (
            "In a village called Bethany, close enough to Jerusalem to walk, "
            "there lived two sisters, Martha and Mary, and their brother "
            "Lazarus."
        ),
        "must_show": "the family established — all three siblings alive and ordinary in the sunlit courtyard: Martha carrying a basin, Mary shelling something on the bench, Lazarus at the gate with firewood on his shoulder.",
        "must_not_show": "no halo, glare or rim-light; no sickness yet — an ordinary golden working day; exactly three people.",
        "scene": (
            "Warm ordinary daylight fills the walled courtyard: "
            "the camera stands at the courtyard's edge and sees "
            "the household from the side, all three in profile "
            "or three-quarter about their work — Martha crossing "
            "the packed earth with a water basin at her hip, "
            "Mary on the stone bench under the fig tree with a "
            "bowl in her lap, and Lazarus swinging the low "
            "timber gate open with a bundle of firewood on one "
            "shoulder — each absorbed in their task, the road "
            "running out of the frame's edge behind him toward "
            "Jerusalem. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r017-b02", "out": "s02-jesus-loved-this-family.jpeg", "seg": "n0",
        "window": "9.01-11.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LAZARUS", "BETHANY-HOUSE"],
        "narration": "Jesus loved this family.",
        "must_show": "the friendship — a close two-shot: Jesus and Lazarus mid-laugh, forearms clasped in greeting at the gate.",
        "must_not_show": "no halo, glare or rim-light on Jesus; real friendship — two men glad to see each other, nothing staged.",
        "scene": (
            "A close two-shot at the courtyard gate in warm "
            "daylight: Jesus and Lazarus with forearms clasped "
            "in greeting, both mid-laugh, Lazarus's free hand "
            "landing on Jesus's shoulder — the easy, practised "
            "gladness of two men who have done exactly this "
            "many times before. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b03", "out": "s03-their-home-was-the-one.jpeg", "seg": "n0",
        "window": "11.27-18.61", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY", "LAZARUS", "BETHANY-HOUSE"],
        "narration": (
            "Their home was the one place on the whole road where he could stop "
            "being a public figure and simply be a friend."
        ),
        "must_show": "the refuge — inside the main room: Jesus at ease on the cushions, sandals off, Lazarus pouring for him, Martha setting down a dish, Mary seated near listening; a friend, not a public figure.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no crowd, no strangers — only the four of them; ease visible in his shoulders. CAMERON GATES (open complaint at 0:12): (1) the set-aside sandals are EMPTY — no toes, feet or foot-shapes inside them, plain empty leather; (2) every clay oil lamp burns ONLY at its wick/spout — a small flame at the spout, NEVER fire rising from the middle of the lamp's body or bowl.",
        "scene": (
            "Inside the main room's warm lamplike daylight: "
            "Jesus reclines at ease against the cushions at the "
            "low table with his sandals set EMPTY by the mat — "
            "plain empty leather, nothing inside them — mid-"
            "sentence in some unhurried story — Lazarus pouring "
            "water into his cup, Martha leaning in to set a "
            "dish of olives down, Mary settled on her heels "
            "near the table's end, chin on her hand, listening "
            "— the one room on earth where nothing at all is "
            "required of him. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b04", "out": "s04-and-now-their-brother-was.jpeg", "seg": "n0",
        "window": "18.61-20.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "LAZARUS", "BETHANY-HOUSE"],
        "narration": "And now their brother was dying.",
        "must_show": "the turn — close on Lazarus fevered on his sleeping mat, eyes shut, sweat-sheened; Martha's hand pressing a damp cloth to his brow.",
        "must_not_show": "no halo, glare or rim-light; dignity in the sickness — no gore, no wasting horror; her hand steady, her face afraid.",
        "scene": (
            "Close in the dim main room: Lazarus lies on his "
            "sleeping mat with his eyes shut and his black hair "
            "wet at the temples, breath shallow, the daylight "
            "from the doorway lying weakly across him — and "
            "Martha's strong red-knuckled hand presses a folded "
            "damp cloth to his brow, her face above him set and "
            "steady in the way of a woman refusing to let her "
            "fear into the room. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b05", "out": "s05-so-the-sisters-sent-word.jpeg", "seg": "n0",
        "window": "20.99-26.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "MESSENGER", "BETHANY-HOUSE"],
        "narration": (
            "So the sisters sent word to Jesus — not a demand, just a few "
            "aching words:"
        ),
        "must_show": "the dispatch — at the courtyard gate: Martha charging the young runner with the message, his hand already on the gate; Mary just behind with both hands pressed together at her mouth.",
        "must_not_show": "no halo, glare or rim-light; no written scroll needed — a spoken charge; urgency without panic.",
        "scene": (
            "At the low timber gate the wiry young runner "
            "stands with one hand on the latch, leaning in to "
            "take the charge — Martha before him, gripping his "
            "shoulder, giving him the words with her level "
            "direct face doing its best to stay level — and a "
            "step behind her Mary stands with both hands "
            "pressed together against her mouth, watching the "
            "message leave. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b06", "out": "s06-lord-behold-he-whom-thou.jpeg", "seg": "w3",
        "window": "27.52-30.36", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "BETHANY-HOUSE"],
        "narration": "Lord, behold, he whom thou lovest is sick.",
        "must_show": "SCRIPTURE-EXACT: the words themselves — a close two-shot of the sisters as the message is spoken: Martha's mouth forming the words, Mary's hand on her sister's arm.",
        "must_not_show": "no halo, glare or rim-light; a few aching words, not a wail — the restraint IS the love.",
        "scene": (
            "A close two-shot of the sisters in the courtyard "
            "light: Martha's direct face caught mid-word, the "
            "message costing her visibly and being paid anyway "
            "— and beside her Mary's slighter face bowed near "
            "her sister's shoulder, one hand curled around "
            "Martha's forearm — two women fitting their whole "
            "fear into one small sentence. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b07", "out": "s07-you-would-expect-him-to.jpeg", "seg": "n1",
        "window": "31.81-35.47", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MESSENGER", "JORDAN-CAMP"],
        "narration": (
            "You would expect him to drop everything and run. He did the "
            "opposite."
        ),
        "must_show": "the news arriving — the dusty breathless runner delivering the message to Jesus seated by the river; Jesus receiving it with unhurried calm.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the contrast is the beat — the boy urgent, Jesus still.",
        "scene": (
            "By the reed-lined river in plain afternoon light "
            "the young runner stands road-dusted and heaving "
            "for breath, the message just out of his mouth — "
            "and before him Jesus sits on a worn limestone "
            "shelf, forearms on his knees, receiving the words "
            "with a stillness that does not move a muscle "
            "toward the road — the urgency arriving and "
            "breaking against something deeper than urgency. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r017-b08", "out": "s08-he-stayed-where-he-was.jpeg", "seg": "n1",
        "window": "35.47-39.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN-CAMP"],
        "narration": "When the news reached him, he stayed where he was two more days.",
        "must_show": "the staying — Jesus deliberately remaining: seated by the small cook-fire at the river's edge in a different light, unhurried, while the water slides past.",
        "must_not_show": "no halo, glare or rim-light on Jesus; not indifference — deliberateness; nobody packs, nobody moves.",
        "scene": (
            "In the long gold of a later hour Jesus sits by "
            "the small blackened fire-ring at the river's "
            "edge, feeding a stick to the low flame, his face "
            "quiet and resolved over the water sliding past "
            "the reeds — a man staying put on purpose, with "
            "the road south lying open behind him and not "
            "taken. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b09", "out": "s09-but-listen-to-what-he.jpeg", "seg": "n1",
        "window": "39.70-41.71", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN-CAMP"],
        "narration": "But listen to what he said about it:",
        "must_show": "the explanation coming — close on Jesus turning his head to speak, the reason already in his eyes.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the turn of the head is the whole beat.",
        "scene": (
            "Close at the riverside: Jesus turns his head to "
            "speak, the light catching the side of his face, "
            "his expression carrying something settled and "
            "certain that has not yet been said out loud — the "
            "look of a man about to explain a choice he never "
            "doubted. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b10", "out": "s10-this-sickness-is-not-unto.jpeg", "seg": "j1",
        "window": "42.24-49.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN-CAMP"],
        "narration": (
            "This sickness is not unto death, but for the glory of God, that "
            "the Son of God might be glorified thereby."
        ),
        "must_show": "SCRIPTURE-EXACT: the saying — a medium shot of Jesus speaking it with calm certainty by the river, the young runner's profile at the frame's edge taking the answer in.",
        "must_not_show": "no halo, glare or rim-light on Jesus; certainty without theatrics — a quiet verdict, not a proclamation.",
        "scene": (
            "A medium shot at the river's edge: Jesus speaks "
            "the sentence evenly, his eyes steady on the "
            "middle distance where the bare hills stand across "
            "the water, one hand open on his knee — and at the "
            "frame's near edge the young runner's dusty "
            "profile hangs on the words, hearing an answer he "
            "does not yet understand and will never forget. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r017-b11", "out": "s11-he-was-not-being-careless.jpeg", "seg": "n1b",
        "window": "50.97-53.46", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN-CAMP"],
        "narration": "He was not being careless with the people he loved.",
        "must_show": "the cost visible — close on Jesus's face: love and resolve held together; the waiting is costing him too.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no serenity-mask — the faint tightness of a man carrying what the delay costs.",
        "scene": (
            "Very close on Jesus's face in the riverside "
            "light: the calm still there, but honest — a faint "
            "tightness at the eyes and the jaw, the look of a "
            "man holding a course that hurts the people he "
            "loves and hurts him with them, and holding it "
            "anyway. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b12", "out": "s12-he-was-reaching-for-something.jpeg", "seg": "n1b",
        "window": "53.46-60.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JORDAN-CAMP"],
        "narration": (
            "He was reaching for something deeper than a quick rescue — "
            "something that would show everyone who he really was."
        ),
        "must_show": "the reach pictured — Jesus on his feet at the water's edge in three-quarter from behind, mantle stirring, eyes gone south down the river toward the far Judean hills.",
        "must_not_show": "no halo, glare or rim-light on Jesus; nothing mystical in the sky — the direction of his gaze carries everything.",
        "scene": (
            "At the river's edge Jesus stands in three-quarter "
            "from behind, his cream mantle stirring at the hem "
            "in the water-wind, his face turned south along "
            "the valley where the bare hills of Judea stack "
            "away into haze — a man looking past a rescue "
            "toward something on the far side of it, the river "
            "running out of the frame toward everything that "
            "is coming. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r017-b13", "out": "s13-and-it-would-cost-those.jpeg", "seg": "n1b",
        "window": "60.55-65.32", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "BETHANY-HOUSE"],
        "narration": (
            "And it would cost those two sisters four days of grief to see it."
        ),
        "must_show": "the cost falling on them — from behind the sisters at the courtyard gate at dusk: both looking down the empty road, and no one on it.",
        "must_not_show": "no halo, glare or rim-light; the road must be visibly EMPTY to its end; their stillness says everything.",
        "scene": (
            "Dusk at the courtyard gate, seen from behind the "
            "two sisters: Martha with both hands set on the "
            "gate's top rail, Mary a half-step back with her "
            "arms wrapped around herself, both faces turned "
            "away down the pale road that runs empty to the "
            "darkening horizon — nothing moving on it at all, "
            "and the two of them standing there anyway. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b14", "out": "s14-by-the-time-jesus-started.jpeg", "seg": "n2",
        "window": "65.84-71.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BETHANY-ROAD", "ANCIENT-ROAD"],
        "narration": (
            "By the time Jesus started for Bethany, the message had changed. "
            "Lazarus was not sick anymore."
        ),
        "must_show": "the journey — Jesus walking the hill road toward Bethany at a purposeful stride, seen full-length from the side, a few companions a pace behind.",
        "must_not_show": "no halo, glare or rim-light on Jesus; travel direction consistent — he moves LEFT to RIGHT in every road beat of this build.",
        "scene": (
            "On the pale stony road along the dry hillside "
            "Jesus walks at a long purposeful stride, seen "
            "full-length from the side moving left to right, "
            "his staff striking the dust, mantle swinging — "
            "two travel-worn companions keep a pace behind "
            "him, matching him with effort — a man no longer "
            "waiting for anything. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b15", "out": "s15-lazarus-was-dead-and-had.jpeg", "seg": "n2",
        "window": "71.70-75.67", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOMB", "MOURNERS"],
        "narration": (
            "Lazarus was dead, and had been sealed in the tomb four days."
        ),
        "must_show": "SCRIPTURE-EXACT: the tomb established — the burial cave in the hillside with the great stone SEALED across its mouth, a scatter of small dark mourning figures on the slope below keeping their distance.",
        "must_not_show": "no halo, glare or rim-light; the stone fully seated in its channel — sealed, final; mourners distant and small.",
        "scene": (
            "Full daylight on the dry limestone hillside: the "
            "camera stands across the slope and takes the "
            "burial cave from the side, its squared doorway "
            "stopped by the great round-edged stone seated "
            "hard in its cut channel — and lower on the "
            "terraced slope a loose scatter of small dark-"
            "clad figures keeps the mourners' distance, faces "
            "turned toward the sealed mouth, the open country "
            "falling away out of the frame's lower edge. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r017-b16", "out": "s16-that-number-is-in-the.jpeg", "seg": "n2",
        "window": "75.67-83.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": (
            "That number is in the story on purpose. People of that time held "
            "that a soul might linger near the body for three days."
        ),
        "must_show": "the finality up close — an insert of the sealed stone itself: the seam packed tight, dust settled in the channel, a dried sprig of mourning herbs at its base; nothing has moved in days.",
        "must_not_show": "no halo, glare or rim-light; no people in frame; no symbols invented — stillness and settled dust carry the meaning.",
        "scene": (
            "A close still insert on the great stone in flat "
            "daylight: its rounded rim seated dead tight in "
            "the cut channel, the seam between stone and rock "
            "packed with wind-blown dust that lies unbroken, "
            "a small dried sprig of grave herbs wilted at its "
            "base — a door photographed for how long it has "
            "not moved. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r017-b17", "out": "s17-four-days-meant-the-door.jpeg", "seg": "n2",
        "window": "83.13-89.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["BETHANY-HOUSE"],
        "narration": (
            "Four days meant the door was shut — no lingering, no hope, no "
            "loophole left."
        ),
        "must_show": "the finality at home — an insert inside the house: Lazarus's sleeping mat rolled and stood against the wall, his cloak folded on it, his sandals set together unworn.",
        "must_not_show": "no halo, glare or rim-light; no people in frame; the tidied absence is the picture — nothing dramatic added.",
        "scene": (
            "Inside the quiet main room a thin blade of "
            "daylight lies across the wall where Lazarus's "
            "sleeping mat stands rolled and upright, his "
            "dark olive tunic folded square on top of it and "
            "his worn sandals set together at its foot, "
            "straps tucked in — the small terrible tidiness "
            "of a house where somebody is not coming back. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r017-b18", "out": "s18-everyone-in-bethany-knew-exactly.jpeg", "seg": "n2",
        "window": "89.63-93.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "MOURNERS", "BETHANY-HOUSE", "BACKGROUND-CAST"],
        "narration": "Everyone in Bethany knew exactly how final four days was.",
        "must_show": "the mourning house — through the doorway: the sisters seated low among dark-clad mourners in the main room, heads bowed, the village keeping grief with them.",
        "must_not_show": "no halo, glare or rim-light; grief postures varied and real; the sisters distinct among the mourners.",
        "scene": (
            "Seen through the house doorway: the main room "
            "sits full of mourning — Martha and Mary seated "
            "low on the mats at the centre, Martha upright "
            "with her red hands knotted in her lap, Mary "
            "folded small against her sister's shoulder — and "
            "around them the dark-clad neighbours of Bethany "
            "keep the old vigil, one woman rocking slowly, an "
            "old man with his head bowed to his chest, the "
            "room's daylight dimmed by the bodies at the "
            "door. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b19", "out": "s19-lord-if-thou-hadst-been.jpeg", "seg": "w21",
        "window": "94.50-98.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD", "ANCIENT-ROAD"],
        "narration": "Lord, if thou hadst been here, my brother had not died.",
        "must_show": "SCRIPTURE-EXACT: Martha's grief spoken to his face — over Jesus's shoulder onto Martha, tear-streaked, the words half accusation and half collapse.",
        "must_not_show": "no halo, glare or rim-light on Jesus; her grief honest — not shrewish, not screaming; the words cost her.",
        "scene": (
            "Over Jesus's shoulder on the pale road: Martha's "
            "direct strong face fills the frame beyond him, "
            "streaked and exhausted under her dark-ochre "
            "headcloth, her chin trembling through the words "
            "as her open hand cuts the air between them — "
            "grief that has waited four days for somewhere to "
            "land, landing. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b20", "out": "s20-but-i-know-that-even.jpeg", "seg": "w21",
        "window": "98.02-104.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "But I know, that even now, whatsoever thou wilt ask of God, God "
            "will give it thee."
        ),
        "must_show": "the faith half of the breath — close on Martha alone: chin lifting through the tears, the desperate stubborn hope arriving mid-sentence.",
        "must_not_show": "no halo, glare or rim-light; the turn from grief to faith must be visible IN her face — same tears, new set of the jaw.",
        "scene": (
            "Close on Martha in the road's plain daylight: "
            "the tears still standing on her cheeks, but her "
            "chin coming up and her level brows steadying as "
            "the second half of her breath finds its footing "
            "— a practical woman placing her last hope, "
            "carefully and completely, on the man in front of "
            "her. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b21", "out": "s21-martha-heard-he-was-finally.jpeg", "seg": "n3",
        "window": "105.61-111.43", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD", "ANCIENT-ROAD"],
        "narration": (
            "Martha heard he was finally near and ran out to meet him on the "
            "road, before he even reached the town."
        ),
        "must_show": "SCRIPTURE-EXACT: the run — Martha full-length running down the road from the village edge toward Jesus and his companions approaching from the open-country end; both travels readable.",
        "must_not_show": "no halo, glare or rim-light on Jesus; she RUNS — skirts caught up in one fist, real stride; the two groups clearly closing on each other.",
        "scene": (
            "The camera holds the curving road from the side, "
            "both travels in profile: from the frame's right "
            "the flat-roofed village edge lets Martha out at "
            "a full graceless run, skirts caught up in one "
            "fist, headcloth pressed to her head with the "
            "other — and entering from the open-country left, "
            "still small, Jesus and his two companions come "
            "on steadily to meet her — the distance between "
            "them shrinking across the dry hillside. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b22", "out": "s22-what-she-said-was-grief.jpeg", "seg": "n3",
        "window": "111.90-116.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "What she said was grief and faith tangled together in one breath:"
        ),
        "must_show": "the tangle — close on Martha mid-word before Jesus's listening profile: grief and faith in the same face at the same instant.",
        "must_not_show": "no halo, glare or rim-light on Jesus; not two expressions in sequence — BOTH at once, tangled.",
        "scene": (
            "Close on the two faces in the road light: "
            "Martha caught mid-word, her brows in grief's "
            "knot while her eyes already hold faith's "
            "stubborn light, the two things sharing her face "
            "without resolving — and at the frame's edge "
            "Jesus's profile is bent toward her, receiving "
            "both at once, refusing neither. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b23", "out": "s23-jesus-told-her-your-brother.jpeg", "seg": "n4",
        "window": "116.91-119.81", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": "Jesus told her, your brother will rise again.",
        "must_show": "the promise given gently — a two-shot: Jesus speaking it plainly to Martha, his steadiness against her exhaustion.",
        "must_not_show": "no halo, glare or rim-light on Jesus; plain speech, not performance — comfort with weight behind it.",
        "scene": (
            "A quiet two-shot on the road: Jesus speaks the "
            "promise plainly, his head inclined to hers, one "
            "hand half-raised in the small open gesture of a "
            "man handing something over — and Martha stands "
            "in it, spent and upright, hearing words she has "
            "heard at funerals all her life from a mouth that "
            "says them differently. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b24", "out": "s24-martha-nodded-the-way-we.jpeg", "seg": "n4",
        "window": "119.81-128.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "Martha nodded the way we nod at things we believe but cannot feel "
            "— yes, at the end of the world, on the last day, I know."
        ),
        "must_show": "the hollow nod — single on Martha: nodding with her eyes down, agreeing with a doctrine that is true and no comfort at all.",
        "must_not_show": "no halo, glare or rim-light; not despair — the specific flatness of belief without feeling; eyes DOWN, not at him.",
        "scene": (
            "Single on Martha in the flat road light: she "
            "nods slowly with her eyes down on the dust "
            "between them, mouth pressed into the polite "
            "line of agreement, hands hanging — the nod of "
            "every mourner who has ever assented to the last "
            "day while the first day without their person "
            "stretches out in front of them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b25", "out": "s25-and-jesus-took-the-whole.jpeg", "seg": "n4",
        "window": "128.72-136.22", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "And Jesus took the whole promise out of the far-off future and set "
            "it down in the person standing right in front of her:"
        ),
        "must_show": "the turn — Jesus stepping in closer and drawing her eyes up from the dust to his face; the moment before the claim.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the physical closing of distance IS the theology — her eyes coming UP.",
        "scene": (
            "The two-shot tightens: Jesus has stepped in "
            "close and bent his head to catch her downcast "
            "eyes, and Martha's face is just lifting, pulled "
            "up almost against her will to meet a gaze "
            "already waiting for her — the far-off last day "
            "being carried across the space between them and "
            "set down where she is standing. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b26", "out": "s26-i-am-the-resurrection-and.jpeg", "seg": "j2",
        "window": "136.78-143.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "I am the resurrection, and the life: he that believeth in me, "
            "though he were dead, yet shall he live:"
        ),
        "must_show": "SCRIPTURE-EXACT: the claim — over Martha's shoulder onto Jesus's face as he says I AM: quiet, total authority in open daylight on a dusty road.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the biggest sentence ever spoken on a country road, said like a fact.",
        "scene": (
            "Over Martha's shoulder, filling the frame beyond "
            "her: Jesus's face as he speaks the claim, level "
            "and unhurried, his remarkable eyes holding hers "
            "with the calm of a man stating what he is rather "
            "than arguing it — road dust drifting through the "
            "plain daylight between them, as if the setting "
            "itself refuses to dress the sentence up. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b27", "out": "s27-and-whosoever-liveth-and-believeth.jpeg", "seg": "j2",
        "window": "143.60-148.13", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "And whosoever liveth and believeth in me shall never die."
        ),
        "must_show": "the reverse — over Jesus's shoulder onto Martha receiving 'shall never die': the words landing on a woman four days into death's finality.",
        "must_not_show": "no halo, glare or rim-light on Jesus; her face does the work — the sentence arriving somewhere it has never been allowed before.",
        "scene": (
            "The reverse, over Jesus's shoulder: Martha's "
            "strong face taking the words as they land, her "
            "level brows lifting apart, lips parting, the "
            "exhaustion in her features cracking around "
            "something entering underneath it — a woman "
            "standing in the wreckage of four final days "
            "being told that final is not a word he answers "
            "to. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b28", "out": "s28-believest-thou-this.jpeg", "seg": "j2",
        "window": "148.13-150.34", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": "Believest thou this?",
        "must_show": "the question — close on Jesus: the direct, personal ask; nowhere for her to hide from it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; gentle and absolutely direct at once — a real question awaiting a real answer.",
        "scene": (
            "Close on Jesus in the road light, Martha's "
            "blurred shoulder at the frame's edge: his head "
            "tips slightly with the question, eyes steady on "
            "hers, the gentleness in his face making the "
            "directness more escapable-proof, not less — a "
            "question placed in her hands with nothing "
            "propping it up. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b29", "out": "s29-yea-lord-i-believe-that.jpeg", "seg": "w27",
        "window": "151.83-157.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "Yea, Lord: I believe that thou art the Christ, the Son of God, "
            "which should come into the world."
        ),
        "must_show": "SCRIPTURE-EXACT: the confession — close on Martha: tears standing, voice steadied, the great confession spoken plainly by a grieving practical woman on a road.",
        "must_not_show": "no halo, glare or rim-light; no rapture-face — conviction, simple and enormous, through tears.",
        "scene": (
            "Close on Martha in the plain daylight: her chin "
            "level now, the standing tears ignored, her "
            "direct intelligent face laying the confession "
            "down word by word like stones set in a wall — a "
            "woman who has cooked for him and argued with "
            "him and buried her brother, saying out loud who "
            "she has concluded he is. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b30", "out": "s30-he-did-not-offer-her.jpeg", "seg": "n5",
        "window": "159.43-166.68", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "BETHANY-ROAD"],
        "narration": (
            "He did not offer her a doctrine to file away until the last day. "
            "He offered her himself, right there in the dust of the road."
        ),
        "must_show": "himself, not doctrine — a medium two-shot: his hands closed warm over hers in the road dust, the exchange complete.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the contact reverent and human — hands over hands, nothing more needed.",
        "scene": (
            "A medium two-shot in the road's honest light: "
            "Jesus's hands closed warm around Martha's "
            "work-reddened hands between them, her headcloth "
            "bowed a moment over the grip, his head bent "
            "toward hers — the dust of the ordinary road "
            "standing around their feet while the largest "
            "gift there is changes hands in silence. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b31", "out": "s31-then-mary-came-and-fell.jpeg", "seg": "n5",
        "window": "166.68-172.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY", "BETHANY-ROAD"],
        "narration": (
            "Then Mary came — the quieter sister — and she fell at his feet and "
            "wept,"
        ),
        "must_show": "SCRIPTURE-EXACT: the fall — from behind Jesus looking down: Mary collapsed at his feet, hands at the hem of his robe, her uncovered dark hair spilled forward, weeping.",
        "must_not_show": "no halo, glare or rim-light on Jesus; her collapse total — knees in the dust, no composure kept; his feet and hem in frame.",
        "scene": (
            "From behind Jesus's shoulder, looking down: Mary "
            "has fallen at his feet in the road dust, knees "
            "down, both hands gripping the hem of his cream "
            "robe, her uncovered dark hair spilled forward "
            "over her dusty-indigo shoulders as the weeping "
            "shakes her — the quieter sister with nothing "
            "quiet left, holding onto the edge of him like a "
            "drowning woman holds a rope. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b32", "out": "s32-and-every-mourner-who-had.jpeg", "seg": "n5",
        "window": "172.20-175.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY", "MOURNERS", "BETHANY-ROAD", "BACKGROUND-CAST"],
        "narration": "and every mourner who had followed her out wept too.",
        "must_show": "the grief spreading — behind kneeling Mary: the dark-clad mourners arriving from the village and breaking into weeping around her.",
        "must_not_show": "no halo, glare or rim-light; varied real grief postures — no chorus-line of identical criers.",
        "scene": (
            "Behind Mary's kneeling form the road fills with "
            "the mourners who followed her out: a dozen dark-"
            "clad villagers arriving mid-grief — a woman "
            "pressing her head-cloth to her mouth, an old man "
            "leaning hard on a younger one's arm, a girl "
            "openly sobbing — the weeping catching from one "
            "to the next like fire in dry grass. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b33", "out": "s33-the-whole-road-dissolved-into.jpeg", "seg": "n5",
        "window": "175.68-178.42", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARY", "MOURNERS", "BETHANY-ROAD", "ANCIENT-ROAD", "BACKGROUND-CAST"],
        "narration": "The whole road dissolved into grief.",
        "must_show": "the whole road grieving — a wide from behind Jesus: Mary at his feet, the weeping crowd filling the road beyond, the village edge behind them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; every gaze and posture bends toward the centre — nobody looking at the camera.",
        "scene": (
            "The camera stands behind Jesus and shoots past "
            "his shoulder down the road: at his feet Mary "
            "kneels folded in the dust, and beyond her the "
            "pale road is full of dark-clad mourners in "
            "every posture of grief, every face turned "
            "toward the still cream-clad figure of Jesus at "
            "the frame's near edge, the flat-roofed village "
            "shimmering at the road's far end — one man "
            "standing upright in a river of weeping. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b34", "out": "s34-lord-if-thou-hadst-been-mary.jpeg", "seg": "w32",
        "window": "178.99-182.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY", "BETHANY-ROAD"],
        "narration": "Lord, if thou hadst been here, my brother had not died.",
        "must_show": "SCRIPTURE-EXACT: the same words again — close on Mary's upturned tear-flooded face from low at his feet, the echo of her sister's sentence.",
        "must_not_show": "no halo, glare or rim-light; the SAME sentence as Martha's — the echo is the point; her face upturned, wrecked and open.",
        "scene": (
            "Close and low in the road dust: Mary's slight "
            "face turned up from his feet, flooded and "
            "shining, her dark hair stuck to her wet cheeks "
            "as she says the exact sentence her sister said "
            "— the same wound in two voices — her hands "
            "still knotted in the hem she has not let go "
            "of. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b35", "out": "s35-jesus-wept.jpeg", "seg": "n6",
        "window": "184.19-190.44", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BETHANY-ROAD"],
        "narration": (
            "And then comes the shortest verse in the whole Bible, and one of "
            "the most staggering. Jesus wept."
        ),
        "must_show": "SCRIPTURE-EXACT: JESUS WEPT — close on his face as the tears break and fall; the Son of God crying openly at a grave.",
        "must_not_show": "no halo, glare or rim-light on Jesus; REAL weeping — wet eyes, tears on the cheeks, grief unhidden; never staged or serene.",
        "scene": (
            "Close on Jesus's face in the open daylight: his "
            "eyes have filled and broken, tears running "
            "openly down into his beard, his jaw unsteady — "
            "no composure performed and none kept — the "
            "strongest face in the story undone the same way "
            "every other face on this road is undone. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b36", "out": "s36-sit-with-that.jpeg", "seg": "n6",
        "window": "190.44-191.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["BETHANY-ROAD"],
        "narration": "Sit with that.",
        "must_show": "the hold — an extreme close: one tear tracking down into his beard, his eyes closing.",
        "must_not_show": "no halo, glare or rim-light on Jesus; stillness — the single held detail, nothing else moving.",
        "scene": (
            "An extreme close-up held still: one bright tear "
            "tracking slowly down Jesus's cheek into the "
            "dark of his beard as his eyes close, the "
            "lashes wet — one second of the story asked to "
            "stand still, and standing. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b37", "out": "s37-the-one-man-there-who.jpeg", "seg": "n6",
        "window": "191.75-200.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY", "TOMB"],
        "narration": (
            "The one man there who knew — knew — that in a few minutes Lazarus "
            "would be breathing again, stood at the grave of his friend and "
            "cried."
        ),
        "must_show": "weeping at the grave — from the side: Jesus standing before the SEALED stone crying openly, the two sisters a pace behind him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the stone still SEALED; his grief and his knowledge in the same body — upright AND weeping.",
        "scene": (
            "From the side at the foot of the tomb ramp: "
            "Jesus stands before the great sealed stone with "
            "the tears still coming, upright, arms loose at "
            "his sides, weeping at a door he already intends "
            "to open — and a pace behind him Martha and Mary "
            "stand together, Mary's face pressed to her "
            "sister's shoulder, watching him grieve their "
            "brother. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r017-b38", "out": "s38-not-because-he-had-run.jpeg", "seg": "n6",
        "window": "200.90-203.40", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB"],
        "narration": "Not because he had run out of options.",
        "must_show": "grief without despair — close on his wet face: the jaw setting THROUGH the tears; sorrow with power intact underneath it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no helplessness in the eyes — grief and resolve occupying the same face.",
        "scene": (
            "Close on Jesus's wet face before the stone: the "
            "tears unhidden on his cheeks while the jaw "
            "beneath them sets hard and the remarkable eyes "
            "come up to the sealed rock — sorrow and "
            "authority standing in the one face without "
            "cancelling each other, a man crying who has "
            "absolutely not run out of options. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b39", "out": "s39-he-cried-because-the-people.jpeg", "seg": "n6",
        "window": "203.40-211.22", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "MARY", "TOMB"],
        "narration": (
            "He cried because the people he loved were broken, and death is a "
            "horror, and he would not stand there pretending it wasn't."
        ),
        "must_show": "THE TOMB IS STILL SEALED: the great round stone sits IN the doorway groove, flush, completely covering the opening - NO dark doorway visible anywhere in this frame. shared grief — a three-shot of contact: his hand gripping Martha's shoulder, Mary's bowed head close against his arm, all three grieving together.",
        "must_not_show": "NEVER an open or dark tomb doorway and never the stone standing beside an opening - the stone is NOT taken away until later in the story. no halo, glare or rim-light on Jesus; he grieves WITH them, not over them — contact warm, heads close.",
        "scene": (
            "A close three-shot at the tomb ramp: Jesus's "
            "hand gripped firm on Martha's shoulder, her own "
            "hand risen to cover it, and Mary's bowed head "
            "leaned in against his other arm, her hair "
            "hiding her face — three people holding one "
            "grief between them in the plain daylight, "
            "nobody pretending anything. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b40", "out": "s40-he-did-not-skip-the.jpeg", "seg": "n6",
        "window": "211.22-216.10", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOURNERS", "TOMB", "BACKGROUND-CAST"],
        "narration": (
            "He did not skip the grief. He walked all the way into it with "
            "them."
        ),
        "must_show": "THE TOMB IS STILL SEALED: the great round stone sits IN the doorway groove, flush, completely covering the opening - NO dark doorway visible anywhere in this frame. Jesus is IN MOTION, mid-stride through the weeping crowd toward the sealed tomb. walking into it — Jesus moving through the midst of the weeping mourners toward the tomb, one hand touching a bowed shoulder in passing.",
        "must_not_show": "ONE SINGLE CONTINUOUS PHOTOGRAPH ONLY - NEVER panels, never a comic strip, never multiple stacked frames or a storyboard grid. NEVER an open or dark tomb doorway and never the stone standing beside an opening - the stone is NOT taken away until later in the story. NEVER a stationary private moment with one man - no stopped counseling pose; he moves THROUGH the mourners. no halo, glare or rim-light on Jesus; he moves THROUGH the crowd, not around it; the touch in passing is the beat.",
        "scene": (
            "In medium-full from the side Jesus walks "
            "forward through the middle of the weeping "
            "mourners toward the sealed tomb, not around "
            "them but among them, his hand pressing one "
            "bowed dark shoulder in passing — the grieving "
            "faces lifting one after another as he passes "
            "up the shallow ramp with the tears still wet "
            "on his own. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b41", "out": "s41-the-tomb-was-a-cave.jpeg", "seg": "n7",
        "window": "216.68-220.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": (
            "The tomb was a cave with a heavy stone rolled across its mouth."
        ),
        "must_show": "THE TOMB IS STILL SEALED: the great round stone sits IN the doorway groove, flush, completely covering the opening - NO dark doorway visible anywhere in this frame. the door itself — the cave mouth and the great stone filling the frame: its mass, its channel, the finality of its fit.",
        "must_not_show": "NEVER an open or dark tomb doorway and never the stone standing beside an opening - the stone is NOT taken away until later in the story. no halo, glare or rim-light; no people in frame — architecture only; the stone's WEIGHT must read.",
        "scene": (
            "The cave mouth fills the frame in hard "
            "daylight: the great round-edged stone seated in "
            "its cut channel across the squared doorway, its "
            "surface pocked and massive, the shadow line "
            "under its curve showing the full thickness of "
            "rock a dead man's door is made of — a door "
            "built to be final. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b42", "out": "s42-jesus-said-take-away-the.jpeg", "seg": "n7",
        "window": "220.48-223.51", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB"],
        "narration": "Jesus said, take away the stone.",
        "must_show": "THE TOMB IS STILL SEALED: the great round stone sits IN the doorway groove, flush, completely covering the opening - NO dark doorway visible anywhere in this frame. SCRIPTURE-EXACT: the command — Jesus in profile, arm fully extended, pointing at the stone; the order given plainly.",
        "must_not_show": "NEVER an open or dark tomb doorway and never the stone standing beside an opening - the stone is NOT taken away until later in the story. no halo, glare or rim-light on Jesus; the arm and the stone in one frame — the command's target unmistakable.",
        "scene": (
            "From the side in medium shot: Jesus stands with "
            "his arm fully extended toward the great stone, "
            "the pointing hand steady at the end of it, his "
            "tear-tracked face set — the command travelling "
            "down the line of his arm to the rock it names, "
            "plain as a workman directing work. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b43", "out": "s43-practical-careful-martha-panicked.jpeg", "seg": "n7",
        "window": "223.98-227.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "TOMB"],
        "narration": "Practical, careful Martha panicked:",
        "must_show": "THE TOMB IS STILL SEALED: the great round stone sits IN the doorway groove, flush, completely covering the opening - NO dark doorway visible anywhere in this frame. the panic — close on Martha: one hand flying up in protest, alarm breaking through the grief; the practical woman hitting the practical horror.",
        "must_not_show": "NEVER an open or dark tomb doorway and never the stone standing beside an opening - the stone is NOT taken away until later in the story. no halo, glare or rim-light; not anger — alarm; the same direct face thrown into protest.",
        "scene": (
            "Close on Martha at the ramp's edge: her hand "
            "flown up palm-out in instinctive protest, her "
            "level brows sprung apart, mouth already open — "
            "the household manager of every feast in Bethany "
            "colliding with the one practical fact nobody at "
            "a graveside says out loud. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b44", "out": "s44-lord-by-this-time-he.jpeg", "seg": "w39",
        "window": "228.06-232.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "TOMB"],
        "narration": (
            "Lord, by this time he stinketh: for he hath been dead four days."
        ),
        "must_show": "THE TOMB IS STILL SEALED: the great round stone sits IN the doorway groove, flush, completely covering the opening - NO dark doorway visible anywhere in this frame. SCRIPTURE-EXACT: the protest — a two-shot: Martha between Jesus and the stone, her hand thrown toward it, dread plain; Jesus receiving the objection unmoved.",
        "must_not_show": "NEVER an open or dark tomb doorway and never the stone standing beside an opening - the stone is NOT taken away until later in the story. no halo, glare or rim-light on Jesus; her dread is reasonable and must look it — four days is four days.",
        "scene": (
            "A two-shot at the foot of the ramp: Martha "
            "stands half between Jesus and the sealed stone "
            "with her arm thrown back toward it, her face a "
            "map of reasonable dread as the words come out "
            "— and Jesus hears her with his eyes steady "
            "past her shoulder on the stone itself, "
            "unmoved, the objection landing on a decision "
            "already made. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b45", "out": "s45-said-i-not-unto-thee.jpeg", "seg": "j3",
        "window": "234.07-239.78", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARTHA", "TOMB"],
        "narration": (
            "Said I not unto thee, that, if thou wouldest believe, thou "
            "shouldest see the glory of God?"
        ),
        "must_show": "SCRIPTURE-EXACT: the reminder — close two-shot: Jesus's face turned full on Martha, kind and immovable, holding her to her own confession.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no rebuke-face — kindness with steel in it; her face beginning to yield.",
        "scene": (
            "A close two-shot in the hard daylight: Jesus's "
            "face turned full on Martha, gentle and "
            "immovable at once, one brow lifted with the "
            "reminder — and Martha's protest visibly "
            "draining as her own confession comes back to "
            "her, her thrown-back arm sinking slowly to her "
            "side. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r017-b46", "out": "s46-so-they-leaned-into-the.jpeg", "seg": "n7b",
        "window": "241.30-245.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOURNERS", "TOMB"],
        "narration": (
            "So they leaned into the great stone and rolled it back,"
        ),
        "must_show": "THE SLIDE, not a cartwheel: the great disc stays edge-in its cut stone groove against the tomb face and the men push it SIDEWAYS along the groove, the dark doorway just beginning to appear behind its trailing edge. SCRIPTURE-EXACT: the heave — three village men shoulder-deep into the stone's edge mid-roll, feet dug into the ramp, the dark seam of the doorway beginning to open.",
        "must_not_show": "NEVER the stone trundled across open ground away from the tomb like a wheel, never fully open yet - it is mid-slide in its groove against the rock face. no halo, glare or rim-light; the physics must read at a glance — all three pushing the SAME direction along the channel, weight believable, the gap only beginning.",
        "scene": (
            "At the cave mouth three dark-clad village men "
            "drive their shoulders into the great stone's "
            "edge, bodies at forty-five degrees, sandalled "
            "feet dug hard into the worn ramp, every back "
            "and arm pushing the stone one single direction "
            "along its cut channel — and behind their strain "
            "the first hand's-width of the doorway's "
            "blackness has opened to the day. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b47", "out": "s47-and-the-dark-mouth-of.jpeg", "seg": "n7b",
        "window": "245.20-247.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOURNERS", "TOMB"],
        "narration": (
            "and the dark mouth of the grave stood open to the daylight."
        ),
        "must_show": "SCRIPTURE-EXACT: OPEN — the stone rolled clear in its channel, the doorway a total black rectangle in the sunlit rock face, the men stepping back winded.",
        "must_not_show": "no halo, glare or rim-light; the interior must be TRUE BLACK — daylight does not reach in; nothing visible inside yet.",
        "scene": (
            "The great stone stands rolled clear at the end "
            "of its channel and the tomb's mouth is a total "
            "black rectangle cut in the bright limestone, "
            "exhaling its dark at the daylight — the three "
            "men stepping back off the ramp winded, hands "
            "on knees, dust still hanging where the stone "
            "ground past — an open grave and a silence "
            "nobody fills. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b48", "out": "s48-he-lifted-his-eyes-and.jpeg", "seg": "n8",
        "window": "248.16-256.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOURNERS", "TOMB", "BACKGROUND-CAST"],
        "narration": (
            "He lifted his eyes and prayed out loud — not because heaven was "
            "hard of hearing, but because he wanted the crowd to know exactly "
            "where the power came from."
        ),
        "must_show": "SCRIPTURE-EXACT: the public prayer — a medium shot of Jesus before the open black doorway, face and open palms lifted to the sky, praying aloud; the crowd's heads soft at the frame's edges.",
        "must_not_show": "no halo, glare or rim-light on Jesus; nothing descends, nothing shines — an audible prayer in plain daylight; the black doorway stays black behind him.",
        "scene": (
            "A medium shot before the open tomb: Jesus "
            "stands with his face lifted full to the sky "
            "and both palms open at shoulder height, "
            "praying aloud in the hearing of everyone, the "
            "black doorway gaping behind his shoulder — and "
            "soft at the frame's edges the nearest mourners' "
            "faces hang between dread and hope, hearing a "
            "man talk to heaven the way a son reports to a "
            "father. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r017-b49", "out": "s49-and-then-he-called-into.jpeg", "seg": "n8",
        "window": "257.21-261.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB"],
        "narration": (
            "And then he called into the dark, in a voice they said was loud "
            "enough to wake the dead:"
        ),
        "must_show": "the call forming — past Jesus's shoulder INTO the black doorway: his chest filled, arm rising toward the dark, the shout a half-second from leaving him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the doorway pure black; the wind-up of the voice visible in the body.",
        "scene": (
            "Past Jesus's shoulder the black doorway fills "
            "the frame's centre: he has drawn a full chest "
            "of air, one arm rising toward the dark mouth, "
            "head lowering like a man about to put his "
            "whole body into a shout — the stillness of the "
            "instant before a voice goes somewhere no voice "
            "has ever usefully gone. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b50", "out": "s50-lazarus-come-forth.jpeg", "seg": "j4",
        "window": "262.16-263.88", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB"],
        "narration": "Lazarus, come forth.",
        "must_show": "SCRIPTURE-EXACT: THE SHOUT — tight close on Jesus mid-command: mouth open, cords of the neck standing, absolute authority aimed into the tomb.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no light effects from mouth or eyes — pure human-frame authority at full voice.",
        "scene": (
            "Tight close on Jesus mid-shout: mouth open on "
            "the great command, the cords of his neck "
            "standing, brows driven down over the blazing-"
            "alive eyes, the tear tracks still on his "
            "cheeks — all the grief and all the authority "
            "of the story leaving him in one voice aimed "
            "straight into the dark. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b51", "out": "s51-and-the-dead-man-came.jpeg", "seg": "n9",
        "window": "265.37-266.77", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": "And the dead man came out.",
        "must_show": "SCRIPTURE-EXACT: first sight — deep inside the black doorway, a linen-bound upright form at the far edge of the light, barely resolved, coming forward.",
        "must_not_show": "no halo, glare or rim-light; no horror styling — clean linen, upright dignity; the figure mostly swallowed in dark, just entering the light's reach.",
        "scene": (
            "The black doorway almost fills the frame — and "
            "deep inside it, at the farthest edge of the "
            "daylight's reach, a pale linen-bound form "
            "stands upright and has begun to come forward, "
            "half-dissolved in the dark, its wrapped head "
            "and shoulders just catching the light — the "
            "first sight of the thing nobody in four "
            "thousand years of graves has ever seen. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b52", "out": "s52-bound-hand-and-foot-in.jpeg", "seg": "n9",
        "window": "266.77-271.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": (
            "Bound hand and foot in strips of grave-linen, his face still "
            "wrapped,"
        ),
        "must_show": "SCRIPTURE-EXACT: the emergence — the bound figure mid-step at the threshold, arms wrapped to his sides, face covered by the napkin, shuffling out of the dark into full sun.",
        "must_not_show": "no halo, glare or rim-light; the binding accurate — strips of linen, arms held close, small constrained steps; clean cloth, no decay.",
        "scene": (
            "At the tomb's threshold the bound figure takes "
            "a small constrained step into the sunlight: "
            "wrapped head to foot in clean strips of grave-"
            "linen, arms bound close to his sides, the face "
            "covered by its folded napkin, the whole form "
            "upright and moving in short shuffling steps out "
            "of the black — daylight climbing the linen as "
            "he comes. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r017-b53", "out": "s53-lazarus-stood-in-the-mouth.jpeg", "seg": "n9",
        "window": "271.50-275.22", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": (
            "Lazarus stood in the mouth of his own tomb — alive."
        ),
        "must_show": "SCRIPTURE-EXACT: standing — the bound figure fully out, upright and still in the mouth of the tomb, full-length, the black doorway framing him from behind.",
        "must_not_show": "no halo, glare or rim-light; STILLNESS — no motion now; the impossible tableau held: a bound dead man standing in daylight.",
        "scene": (
            "Full-length and dead centre: the linen-bound "
            "figure stands entirely still in the mouth of "
            "the tomb, the black rectangle of the doorway "
            "exactly framing him from behind, the full sun "
            "hard on the white strips — upright, unmoving, "
            "unmistakably standing under his own life — a "
            "tableau the eye refuses twice before accepting. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r017-b54", "out": "s54-four-days-gone-and-standing.jpeg", "seg": "n9",
        "window": "275.22-278.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOMB"],
        "narration": "Four days gone, and standing in the light.",
        "must_show": "the close hold — the wrapped head and shoulders in full sun: the napkin over the face, linen bright, absolutely still.",
        "must_not_show": "no halo, glare or rim-light; reverent, not eerie — clean bright linen in honest daylight; no face visible yet.",
        "scene": (
            "Close on the wrapped head and shoulders in the "
            "full sun: the folded napkin lying smooth over "
            "the face, the linen strips crossing the "
            "shoulders bright and clean against the black "
            "doorway behind — a covered face with morning "
            "light full on it, standing where light has no "
            "business finding anything standing. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b55", "out": "s55-nobody-moved-nobody-breathed.jpeg", "seg": "n9",
        "window": "278.53-282.09", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "MOURNERS", "TOMB", "BACKGROUND-CAST"],
        "narration": "Nobody moved. Nobody breathed.",
        "must_show": "the frozen crowd — a wide of the mourners rooted on the slope, hands over mouths, every gaze locked on the tomb mouth; the sisters gripping each other at the front.",
        "must_not_show": "no halo, glare or rim-light; total arrest — no one mid-stride, no one turned away; every gaze converges on the one point.",
        "scene": (
            "The camera stands at the cave's flank and takes "
            "the crowd from the side: a slope of dark-clad "
            "mourners gone absolutely still, hands frozen "
            "over mouths, a dropped water jar lying "
            "unregarded at one woman's feet — Martha and "
            "Mary at the front gripping each other's arms — "
            "and every single gaze in the picture aimed "
            "past the frame's edge at the tomb mouth just "
            "out of view, a whole hillside of people "
            "forgetting to breathe in one direction. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b56", "out": "s56-loose-him-and-let-him.jpeg", "seg": "j5",
        "window": "282.60-284.23", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB"],
        "narration": "Loose him, and let him go.",
        "must_show": "SCRIPTURE-EXACT: the release — a two-shot: Jesus's open hand extended toward the bound standing figure, the command bridging the space between them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gesture opens and frees — palm up, ordinary and enormous.",
        "scene": (
            "A two-shot across the ramp: Jesus with his "
            "open hand extended palm-up toward the bound "
            "white figure standing in the tomb mouth, his "
            "tear-tracked face steady and warm now, the "
            "command crossing the sunlit space between "
            "them like a hand held out — the first order "
            "ever given about a man on this side of his "
            "own grave. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r017-b57", "out": "s57-unwrap-him-take-the-grave.jpeg", "seg": "n10",
        "window": "285.76-291.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAZARUS", "MOURNERS", "TOMB"],
        "narration": (
            "Unwrap him. Take the grave-linen off a living man and let him "
            "walk home to dinner."
        ),
        "must_show": "the unwrapping — close on hands unwinding the linen from his face: Lazarus's living face emerging, eyes blinking hard in the light, the napkin falling away.",
        "must_not_show": "no halo, glare or rim-light; the emerging face healthy and alive — colour in the skin, no pallor of death; the unwrappers' hands trembling is welcome.",
        "scene": (
            "Close at the tomb mouth: two pairs of village "
            "hands unwind the linen from the standing "
            "man's head, the napkin just fallen away — and "
            "out of the loosening strips Lazarus's face "
            "emerges alive, warm-skinned and whole, eyes "
            "screwed half-shut and blinking hard against "
            "the first daylight, lips parting around a "
            "first long breath — a man being unwrapped "
            "back into the world. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b58", "out": "s58-this-was-the-last-great.jpeg", "seg": "n10",
        "window": "291.11-298.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARTHA", "MARY", "LAZARUS", "MOURNERS", "TOMB", "BACKGROUND-CAST"],
        "narration": (
            "This was the last great sign before Jesus turned toward his own "
            "cross — and he did it in the open, at a marked grave, in front of "
            "a crowd,"
        ),
        "must_show": "the open proof — the sisters embracing the freed Lazarus, loosened linen at his feet, the crowd pressing around in broad daylight at the marked grave; joy in the open, witnessed.",
        "must_not_show": "no halo, glare or rim-light; public and undeniable — full daylight, many witnesses, the open tomb plainly in view.",
        "scene": (
            "In full daylight before the open tomb the "
            "sisters have their brother: Martha's strong "
            "arms locked around Lazarus's neck, Mary "
            "pressed into his side with both fists holding "
            "his loosened linen as if he might be taken "
            "back, his own freed arm around her — the "
            "unwound strips heaped white at their feet — "
            "and around the family the crowd presses in a "
            "ring of stunned upturned faces, the black "
            "doorway standing open and empty behind them "
            "for everyone to see. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r017-b59", "out": "s59-so-that-no-one-could.jpeg", "seg": "n10",
        "window": "298.50-303.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB"],
        "narration": (
            "so that no one could ever call it a trick of the light."
        ),
        "must_show": "the cost in his face — a medium single: Jesus apart from the celebration, his eyes gone south toward Jerusalem, the joy behind him and the cross ahead of him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the celebration soft and out of focus behind — his face carries what this sign will cost him.",
        "scene": (
            "A medium single at the slope's edge: Jesus "
            "stands a few paces apart with the soft blur of "
            "the rejoicing crowd behind his shoulder, his "
            "face quiet amid the joy, eyes gone away south "
            "along the hills toward Jerusalem — a man "
            "watching the far-off price of what he has "
            "just done, and not turning from that either. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r017-b60", "out": "s60-looked-death-full-in-the.jpeg", "seg": "n10",
        "window": "303.98-311.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["LAZARUS", "TOMB"],
        "narration": (
            "The one who stands over every grave you have ever wept beside "
            "looked death full in the face and called a friend home."
        ),
        "must_show": "the friends — a two-shot: Lazarus, unwrapped and alive in loosened linen with a dark mantle thrown over his shoulders, gripping Jesus's forearm, foreheads nearly touching.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a reunion of friends, fierce and warm — not worship posture; both faces visible and glad.",
        "scene": (
            "A close two-shot in the day's warm light: "
            "Lazarus — alive, unwrapped, a borrowed dark "
            "mantle thrown over the loosened linen — grips "
            "Jesus's forearm bone-hard with both hands, "
            "foreheads leaned nearly together, and Jesus's "
            "free hand comes up behind his friend's head — "
            "two men laughing and weeping in the same "
            "breath on the doorstep of an empty grave. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r017-b61", "out": "s61-he-is-the-resurrection.jpeg", "seg": "n10",
        "window": "311.24-316.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOMB"],
        "narration": (
            "He does not merely explain the resurrection. He is the "
            "resurrection."
        ),
        "must_show": "the closing statement — a medium-close of Jesus, calm and certain, the open empty tomb soft behind his shoulder; his gaze carrying past the frame with quiet finality.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no gaze into the lens — eyes carried past the camera's edge; the empty black doorway must be visible behind.",
        "scene": (
            "A medium-close closing frame: Jesus stands "
            "calm in the late daylight with the open, empty "
            "black doorway of the tomb soft over his "
            "shoulder, his remarkable eyes carried steady "
            "past the frame's edge toward something beyond "
            "it, his expression the settled certainty of a "
            "man who is himself the thing he has just "
            "proved — the grave behind him open, and "
            "staying open. Every figure has two arms, two "
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
    "ANCIENT-ROAD": "PLACE-REF/ancient-road.jpeg",  # build-38-persistent-widow v2-r038-b39
    "BETHANY-HOUSE": "PLACE-REF/bethany-house.jpeg",  # build-17-lazarus s01-in-a-village-called-bethany (manual)
    "BETHANY-ROAD": "PLACE-REF/bethany-road.jpeg",  # build-17-lazarus s21-martha-heard-he-was-finally (manual)
    "JORDAN-CAMP": "PLACE-REF/jordan-camp.jpeg",  # build-17-lazarus s07-you-would-expect-him-to (manual)
    "TOMB": "PLACE-REF/tomb.jpeg",  # build-37-rich-man-lazarus v2-r037-b45
}
# === end PLACE-PLATES ===
