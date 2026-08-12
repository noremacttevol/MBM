#!/usr/bin/env python3
"""V2 beat map — row 66, build-66-malchus-ear (Luke 22:47-51; John 18:10;
Matthew 26:51-54).

COVERAGE: 29 pictures over 167.0 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS:
  Luke 22:47-51 — NIGHT in Gethsemane; the multitude with "swords and
        staves"; "Lord, shall we smite with the sword?"; the strike;
        "Suffer ye thus far. And he TOUCHED HIS EAR, and HEALED him."
  John 18:10 — the swordsman is PETER; the servant's NAME is MALCHUS;
        it was the RIGHT ear.
  Matthew 26:52-53 — "Put up again thy sword ... all they that take the
        sword shall perish with the sword"; "more than TWELVE LEGIONS of
        angels" — legions NEVER painted (row-21 no-angels precedent);
        the offer exists only in Jesus's words and the night sky.
  ⚑ RESTRAINED VIOLENCE (R-law, Gethsemane class): the sword-swing is
        shown as arrested motion and aftermath ONLY — Malchus with his
        hand CLAMPED to the side of his head, face shocked; NO severed
        ear depicted, NO blood, NO wound detail ever. The healing is
        Jesus's palm laid over the clamped hand's place, and then the
        man's own astonished fingers finding wholeness.
  NIGHT THROUGHOUT — torchlight and a low moon are the only sources
        (scripture-required; not the row-11 defect). No warm domestic
        light anywhere: torch-orange against olive-dark.

TIME OF DAY: one continuous midnight — the prayer's end, the torches
coming up the hill, the arrest circle, the strike, the healing, the mob
closing, and Malchus walking back down whole. The closing beats hold
the same night, quieter.

CONTENT-CARE: the arrest is the passion's threshold — gravity total,
violence minimal and instantly reversed; Judas appears only as a dark
leading figure at the mob's head (no kiss beat in this narration).
Peter's swing is love-shaped error, never villainy.

CHANGING CONDITION (kept OUT of the locks): Malchus's state — armed
functionary, struck and clamped, HEALED and stunned, descending whole;
and the night's temperature: hush, violence-brink, stopped, stilled.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MALCHUS": (
        "MALCHUS LOCK: the high priest's servant is the same man in every "
        "shot — about thirty, neat and capable, with a short black beard, "
        "an official's careful bearing and quick intelligent eyes. He "
        "wears a good DARK CHARCOAL-BLUE servant's tunic with the high "
        "priest's household sash in DEEP OXBLOOD, and carries a torch, "
        "not a weapon (never cream, never white). His face is shown "
        "clearly — a functionary, not a thug."
    ),
    "MOB": (
        "MOB LOCK: the arrest party — temple guards in DARK LEATHER over "
        "IRON-GREY tunics with short swords and wooden staves, servants "
        "with raised torches, a few fine-robed observers at the rear in "
        "NEAR-BLACK INDIGO (never cream, never white). At their head "
        "walks a cloaked DARK-ROBED figure who knows the way. Faces "
        "shown clearly in the torchlight — men on orders, tense, not "
        "monsters."
    ),
    "GARDEN": (
        "GETHSEMANE LOCK: the olive garden at midnight — ancient "
        "wide-trunked olive trees on a terraced slope, a low rock where "
        "someone has been praying, matted spring grass, and below "
        "through the trees the far lamps of the city; a low moon "
        "silvering the leaves. Night throughout: torch-orange and "
        "moon-silver are the only lights."
    ),
}

REF = True

# CONTINUITY-LOCK for the 0:00-0:35 arrest approach (b01-b07). Cameron re-opened
# this row a THIRD time: "people keep disappearing quickly and coming back and
# the army is going the wrong way." The prior two fixes only re-rolled the same
# beat text and reproduced the flicker. This clause is appended to every beat in
# the approach block so the SAME people, the SAME count and ONE approach
# direction are pinned frame-to-frame — no vanish in the tight beats, no
# reversed column.
ARREST_CONT = (
    " CONTINUITY-LOCK (identical in EVERY frame of the arrest's approach, from "
    "the torches' first appearance through the swing): the arrest party is ONE "
    "single unbroken torch-lit column climbing the terraced slope from the "
    "LOWER-LEFT up toward the UPPER-RIGHT where Jesus stands — always advancing "
    "toward him, the torch-flames and the men's faces pointed up-slope, NEVER "
    "receding, never turned away, never marching downhill or off to the side; "
    "the cloaked leader stays at its head with the temple guards in the same "
    "order behind him, and from one frame to the next the column only ever "
    "grows CLOSER and larger, never smaller, never farther. The defenders are "
    "always the SAME three men — Peter the big fisherman foremost with two "
    "companions at his shoulders, no more and no fewer — planted between the "
    "column and Jesus. No soldier and no disciple appears from nowhere or "
    "vanishes between consecutive frames; even in a tight close-up the same "
    "torch-column still burns at the LOWER-LEFT of the background so the scene "
    "never empties."
)

BEATS = [
    {
        "id": "v2-r066-b01", "out": "s01-it-was-the-middle-of.jpeg", "seg": "n0",
        "window": "0.28-8.45", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GARDEN"],
        "narration": (
            "It was the middle of the night, in a garden called Gethsemane. "
            "Jesus had just finished praying — and now torchlight was coming up "
            "the hill."
        ),
        "must_show": "SCRIPTURE-EXACT: the threshold — Jesus risen from the prayer rock in the moon-silvered garden, and below through the olive trunks the snake of torchlight climbing the hill toward him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; night correct and required — moon-silver above, torch-orange threading up from below.",
        "scene": (
            "In the moon-silvered olive garden, the camera among "
            "the trunks behind the waking disciples, Jesus "
            "stands just risen from the low prayer rock, "
            "the night's agony still in the set of his "
            "shoulders — and down the slope, threading "
            "between the ancient trunks, a broken line of "
            "torch-flames climbs steadily toward him, "
            "their orange crawling up through the "
            "silver-dark leaves — a man watching his own "
            "arrest ascend the hill, and not moving from "
            "its path. Every figure has two arms, two "
            "hands and one head."
        ) + ARREST_CONT,
    },
    {
        "id": "v2-r066-b02", "out": "s02-lord-should-we-fight.jpeg", "seg": "n1b",
        "window": "29.62-31.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "Should we fight?",
        "must_show": "the question's face — a disciple's torch-lit face asking it: fear and loyalty at war, a hand already at a sword hilt.",
        "must_not_show": "no halo, glare or rim-light; the hand AT the hilt, not drawn — the question still a question.",
        "scene": (
            "Close in the mixed torch and moonlight: a "
            "disciple's face turned back toward his "
            "teacher, fear and fierce loyalty fighting "
            "across it — and at the frame's lower edge "
            "his hand already closed hard on the HILT of "
            "a sword STILL FULLY SHEATHED in its scabbard "
            "beneath his cloak — the weapon UNDRAWN, NO "
            "blade showing yet, only the white-knuckled "
            "grip; the question asked with "
            "his mouth while his grip answers it — the "
            "night one word from two different endings. "
            "Every figure has two arms, two hands and one "
            "head."
        ) + ARREST_CONT,
    },
    {
        "id": "v2-r066-b03", "out": "s03-a-mob-sent-by-the.jpeg", "seg": "n0",
        "window": "8.45-19.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOB", "GARDEN"],
        "narration": (
            "A mob, sent by the chief priests, armed with swords and clubs, led "
            "by one of his own friends, come to arrest him. This was the moment "
            "everything had been building toward."
        ),
        "must_show": "SCRIPTURE-EXACT: the arrivals — the torch-lit arrest party breaking into the garden's terrace: guards, staves, swords, and at their head the dark-cloaked figure who knows the way.",
        "must_not_show": "no halo, glare or rim-light; the leader's face shadowed under his hood's edge — known and not dwelt on; the mob tense, ordered, human.",
        "scene": (
            "The camera looks DOWN-slope from just behind "
            "Jesus and his three companions, out over the "
            "terrace toward the advancing torches: the "
            "arrest party climbs the terrace from the "
            "lower-left, ascending straight toward Jesus "
            "and the camera — a dozen "
            "torches throwing wild orange over the "
            "silver leaves, temple guards in dark "
            "leather with staves and short swords, "
            "servants crowding behind — and walking at "
            "their head, sure of every turn in the dark, "
            "a cloaked figure whose face the torchlight "
            "keeps finding and losing: a guide who has "
            "prayed on this ground himself. The whole "
            "column faces UP the slope toward Jesus, "
            "closing the distance, never receding. Every figure "
            "has two arms, two hands and one head."
        ) + ARREST_CONT,
    },
    {
        "id": "v2-r066-b04", "out": "s04-and-his-friends-could-not.jpeg", "seg": "n1",
        "window": "19.62-21.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "And his friends could not stand it.",
        "must_show": "the friends' surge — the disciples bunching in front of Jesus as the torches close: bodies interposing, the instinct to shield made visible.",
        "must_not_show": "no halo, glare or rim-light; the interposition the beat — love arranging itself between the threat and its object.",
        "scene": (
            "As the torchlight closes from the lower-left, "
            "the same three disciples "
            "surge and bunch — Peter the big fisherman "
            "foremost with his feet planted wide and two "
            "companions at his shoulders, shouldering "
            "in front of their teacher in the silver "
            "dark, arms half-spread — a "
            "living wall assembling itself out of tired "
            "loyal men, between the swords and the one "
            "man in the garden not looking for cover. "
            "Every figure has two arms, two hands and "
            "one head."
        ) + ARREST_CONT,
    },
    {
        "id": "v2-r066-b05", "out": "s05-luke-says-they-saw-what.jpeg", "seg": "n1 + s49",
        "window": "21.93-28.55", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GARDEN"],
        "narration": (
            "Luke says they saw what was about to happen, and they asked him "
            "first: Lord, shall we smite with the sword?"
        ),
        "must_show": "SCRIPTURE-EXACT: the asking — the three disciples ON THEIR FEET and ALARMED, turned to Jesus in the torch-glare, the question hanging; his answer not yet come.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOBODY seated, reclining, lying down, dozing or asleep — every disciple is standing, wide awake and alarmed; the mob is CLOSE and large, never a distant little torch-line down the hill; the un-answered instant — permission sought and the night not waiting.",
        "scene": (
            "A TIGHT reaction shot, waist-up, filling the "
            "frame with THREE STANDING disciples and Jesus "
            "— every one of them ON HIS FEET, wide awake, "
            "bodies tense and alarmed, faces snapped up "
            "toward Jesus close beside them as the question "
            "leaves them; his own face steady, beginning "
            "its answer. The arrest mob has ALREADY ARRIVED "
            "and stands CLOSE right behind and among them — "
            "big near torch-flames and helmeted faces "
            "crowding in at arm's length, filling the "
            "background wall-to-wall — NOT a distant column, "
            "NOT a thin torch-line snaking away down the "
            "hill. This is a close, crowded, alarmed moment, "
            "NOT the wide establishing view of Jesus standing "
            "over seated men. Absolutely no one is sitting, "
            "kneeling, reclining or resting on the ground. "
            "Night, torch-orange and moon-silver only. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b06", "out": "s06-they-said-and-then-they.jpeg", "seg": "n1b",
        "window": "31.29-34.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": "they said. And then they did not wait for the answer.",
        "must_show": "the answer outrun — ONE ordinary short sword clearing its sheath in the torchlight, the blade half-drawn; decision jumping the queue.",
        "must_not_show": "no halo, glare or rim-light; ONE single weapon only — no second sword, dagger or spare hilt in the other hand; the blade is a normal, believable short-sword length, NOT an oversized or grotesquely long blade, NOT bent or mis-shapen; one hand grips the hilt, the other steadies the scabbard — both hands reading correctly; ANY torch in frame is an ancient hand-held wooden torch or pitch brand — NEVER a modern segmented BAMBOO TIKI-TORCH, garden flare, patio/luau torch or metal-canister torch; the draw itself — steel catching torch-orange, permission left behind.",
        "scene": (
            "Close in the torch-orange dark on ONE man's "
            "hands and a SINGLE ordinary short sword — a "
            "plain, normally proportioned iron blade about "
            "forearm-length, half-drawn from its leather "
            "scabbard, catching the flame-light cleanly "
            "down its length. One hand grips the hilt, "
            "knuckles white; the other holds the scabbard "
            "steady. Just one sword, one clean draw — no "
            "second weapon, no spare dagger or extra hilt "
            "anywhere in frame, the blade a plausible real "
            "length and shape, never giant, never warped. "
            "The question asked two seconds ago already "
            "abandoned behind the metal, loyalty outrunning "
            "its own request for permission into the worst "
            "idea of the night. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b07", "out": "s07-impulsive-loyal-terrified-peter-grabbed.jpeg", "seg": "n1b",
        "window": "34.45-42.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "MALCHUS", "MOB", "GARDEN"],
        "narration": (
            "Impulsive, loyal, terrified Peter grabbed a sword and swung — "
            "meaning, surely, to defend the man he loved."
        ),
        "must_show": "⚑ RESTRAINED: the swing as arrested motion — Peter mid-swing in the torchlight, blade a blur, Malchus recoiling with the torch falling from his hand; contact NEVER shown.",
        "must_not_show": "NO contact, NO wound, NO blood — the swing and the recoil only, the moment cut before the blade arrives; no halo, glare or rim-light.",
        "scene": (
            "In the torch-broken dark the swing is one "
            "arrested blur: Peter's whole big frame "
            "thrown into it, the blade a streak of "
            "orange light, his face a mask of terrified "
            "love — and before him the neat charcoal-"
            "clad servant recoiling, his torch already "
            "falling from his hand in an arc of sparks — "
            "the frame ending where the story's mercy "
            "insists it end, a half-second before "
            "anything lands. Every figure has two arms, "
            "two hands and one head."
        ) + ARREST_CONT,
    },
    {
        "id": "v2-r066-b08", "out": "s08-he-caught-the-servant-of.jpeg", "seg": "n1b",
        "window": "42.20-47.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["MALCHUS", "GARDEN"],
        "narration": (
            "He caught the servant of the high priest, a man named Malchus, and "
            "cut off his ear."
        ),
        "must_show": "⚑ RESTRAINED: the aftermath ONLY — Malchus on one knee with his hand CLAMPED hard to the right side of his head, face white with shock, his fallen torch guttering on the grass.",
        "must_not_show": "NO severed ear, NO blood, NO wound visible — the clamped hand covers everything; the shock in the face carries the fact.",
        "scene": (
            "Malchus is down on one knee in the matted "
            "grass, his whole hand clamped hard over the "
            "right side of his head, fingers spread and "
            "white-knuckled — his careful official's face "
            "gone paper-pale with shock, mouth open on "
            "no sound — while his fallen torch gutters "
            "in the grass beside his knee and throws "
            "climbing shadows over the frozen circle. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r066-b09", "out": "s09-in-one-second-the-whole.jpeg", "seg": "n1b",
        "window": "47.69-51.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "MOB", "GARDEN"],
        "narration": "In one second, the whole night was about to become a massacre.",
        "must_show": "the brink — TWO OPPOSED LINES: on one side the mob's guards, swords clearing sheaths and staves coming up; FACING THEM, the disciples braced, the big fisherman's blade out and pointed ACROSS the gap AT THE MOB; every body cocked toward the space BETWEEN the two lines.",
        "must_not_show": "no halo, glare or rim-light; the fisherman is PETER — a big, DARK-HAIRED, DARK-CURLY, dark-bearded man in his prime, NEVER grey-haired, white-haired, bald or elderly; his drawn blade points OUTWARD toward the enemy mob or the empty ground between the lines, its tip NEVER toward Jesus and never toward any friend — no disciple's weapon is aimed at Jesus or at the cream-robed man; if Jesus is visible he stands BEHIND and among his own men, shielded, well clear of every blade's edge; the violence PENDING everywhere and delivered nowhere.",
        "scene": (
            "The clearing cocks itself in one breath, shot "
            "square-on across the narrow gap between two "
            "opposed lines. On the far side the mob's "
            "front rank: a dozen short swords clearing "
            "sheaths, staves swinging level, torches "
            "lofted. On the near side the disciples brace "
            "shoulder to shoulder — PETER the big "
            "dark-curly-haired fisherman foremost, his "
            "single blade out and levelled ACROSS the gap "
            "toward the advancing mob, pointed at the "
            "enemy and the empty ground, NEVER back at his "
            "own people. Any figure in a cream robe stands "
            "safely BEHIND the disciples' line, no blade "
            "anywhere near him. Two lines of frightened men "
            "one shout from butchery, in a garden planted "
            "for oil and prayer. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b10", "out": "s10-understand-math-twelve-tired-men.jpeg", "seg": "n2",
        "window": "52.13-56.43", "wide": True, "jesus": False, "ref": False,
        "locks": ["MOB", "GARDEN"],
        "narration": "Understand Peter's math. Twelve tired men against an armed mob.",
        "must_show": "the arithmetic visible — the two forces in one frame: the small knot of disciples against the torch-line's depth; hopeless numbers, honestly counted.",
        "must_not_show": "no halo, glare or rim-light; the disparity plain — a courage problem, not a strategy.",
        "scene": (
            "From the terrace's edge the camera holds both forces "
            "in one profile: the arithmetic "
            "lies plain in the torchlight: the "
            "disciples a small tight knot of eleven "
            "tired men in road-worn wool, one drawn "
            "sword among them — and facing them the "
            "mob's depth, rank behind torch-lit rank "
            "back into the trees, iron and leather and "
            "orders — a sum any child could finish, "
            "being contested by one fisherman's love. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r066-b11", "out": "s11-he-was-not-being-smart.jpeg", "seg": "n2",
        "window": "56.43-62.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "GARDEN"],
        "narration": (
            "He was not being smart — he was being brave and wrong, ready to "
            "die swinging for Jesus."
        ),
        "must_show": "brave-and-wrong — close on Peter's torch-lit face over the levelled blade: terror mastered by love, error in full commitment.",
        "must_not_show": "no halo, glare or rim-light; no villainy and no mockery — a magnificent mistake wearing a fisherman's face.",
        "scene": (
            "Close on Peter's face above the levelled "
            "sword in the torch-orange dark: the terror "
            "plainly there and plainly mastered, the "
            "thick jaw set, wild curls stuck to his "
            "brow — a man who has done the sum from the "
            "last beat, got the same hopeless answer, "
            "and planted his feet anyway — courage and "
            "error, indistinguishable at this light "
            "level, both total. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b12", "out": "s12-and-most-leaders-in-that.jpeg", "seg": "n2",
        "window": "62.69-69.59", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "GARDEN"],
        "narration": (
            "And most leaders, in that moment, would have let him. But Jesus "
            "stopped everything. First, he stopped Peter:"
        ),
        "must_show": "the stopping — Jesus stepping BETWEEN Peter and the mob, one open palm toward each side; Peter's sword FALTERING and DROPPING toward the ground; the whole night's violence halted on Jesus's two open hands.",
        "must_not_show": "no halo, glare or rim-light on Jesus; Peter's blade must be LOWERING, its tip angled DOWN toward the ground or held out to Peter's own side AWAY from Jesus — the sword's point is NEVER aimed at Jesus, never across his body, never level with his chest; Peter (dark-haired, dark-curly, dark-bearded) is stopped and yielding, NOT menacing Jesus; no weapon of any kind points at the cream-robed man; the interposition his — body between the armies, calm against both currents.",
        "scene": (
            "Into the cocked half-second Jesus steps — "
            "planting his body between his own men and "
            "the mob's drawn line, one open palm turned "
            "toward each side, cream robe torch-lit in "
            "the middle of the iron. On Jesus's near "
            "side Peter checks: his sword-arm falters and "
            "the blade DROPS, its point sinking toward "
            "the ground at Peter's own side, turned well "
            "AWAY from Jesus — never leveled at him, "
            "never crossing his body. On the far side the "
            "guards are checked mid-step. The whole night "
            "stops on Jesus's two open hands: violence "
            "hanging unfinished on either side of one "
            "unarmed man, and not a single blade pointed "
            "his way. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r066-b13", "out": "s13-put-up-again-thy-sword.jpeg", "seg": "j1",
        "window": "70.23-76.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": (
            "Put up again thy sword into his place: for all they that take the "
            "sword shall perish with the sword."
        ),
        "must_show": "SCRIPTURE-EXACT: the command to Peter — the two faces close: Jesus's grave order, Peter's anguished obedience beginning; the blade turning downward between them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the sword DESCENDING — obedience visible in the blade's angle.",
        "scene": (
            "Close between the two faces in the "
            "torchlight: Jesus's grave and utterly "
            "certain, the command still leaving him — "
            "and Peter's anguished, wet-eyed, the fight "
            "draining out of his big frame as his "
            "sword-arm turns the blade slowly down "
            "between them, steel sinking out of the "
            "firelight — a will being overruled by a "
            "voice it loves more than its own logic. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r066-b14", "out": "s14-put-it-away-peter-this.jpeg", "seg": "n3",
        "window": "77.52-80.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "GARDEN"],
        "narration": "Put it away, Peter. This is not that kind of kingdom.",
        "must_show": "the sheathing — Peter's sword going home into its sheath, his head bowed over the act; the kingdom's arsenal closing.",
        "must_not_show": "no halo, glare or rim-light; the sheathing complete and costly — surrender of the only plan he had.",
        "scene": (
            "Close on the sheathing: Peter's big hands "
            "guiding the blade home into its leather, "
            "the hilt seating with a finality his bowed "
            "head confirms — the fisherman's whole "
            "hopeless brave plan going back into "
            "storage unused — while the torch-glare "
            "plays over his bent shoulders and the "
            "kingdom declines, forever, its one drawn "
            "sword. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r066-b15", "out": "s15-he-said-he-could-call.jpeg", "seg": "n3",
        "window": "80.89-89.14", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GARDEN"],
        "narration": (
            "He said he could call down more than twelve legions of angels this "
            "instant if rescue were the plan — but rescue was not the plan."
        ),
        "must_show": "the unsummoned help — a CLOSE portrait of Jesus's face and shoulders tipped up to the night sky, the stars plain and empty above him; power declined rendered as one quiet upward glance.",
        "must_not_show": "NO angels, NO legions, NO light in the sky — stars only (no-angels law); do NOT repeat the wide establishing view — this is NOT the full-figure shot of Jesus standing over seated disciples, and there is NO thin torch-line snaking away down the hill; the olive branches frame the sky softly and naturally, NOT chopped or cropped into a jarring hard hole; the declining visible in the gaze's return to earth.",
        "scene": (
            "A CLOSE, intimate shot — Jesus from the "
            "chest up, his face and throat tipped back "
            "to look up into the deep night sky above "
            "the olive crowns: the sky thick with plain "
            "cold stars, empty of everything except its "
            "own distance, a soft scatter of olive "
            "leaves at the edges of the frame catching "
            "the moonlight naturally. His expression is "
            "the calm of a man who has just declined the "
            "largest reinforcement in existence by simply "
            "not asking. This is a tight upward-glance "
            "portrait, NOT the wide establishing view, "
            "NOT a full-figure stand among seated men, "
            "and there is no long torch-line running off "
            "down the hillside behind him. Torch-orange "
            "warms one side of his face, moon-silver the "
            "other. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r066-b16", "out": "s16-he-was-not-being-overpowered.jpeg", "seg": "n3",
        "window": "89.14-91.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MOB"],
        "narration": "He was not being overpowered in a garden.",
        "must_show": "the power's true direction — Jesus standing unbound amid the ring of armed men, straighter than any of them; captivity visibly voluntary.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the guards GRIP their own hilts at their sides — no sword blade is leveled or pointed AT Jesus, no tip aimed at his chest or body; their tension is in their grips, not in any thrust toward him; his unbound stillness against their armed tension — who holds whom, inverted.",
        "scene": (
            "Amid the ring of drawn iron Jesus stands "
            "unbound and unbent — the only unarmed man "
            "in the clearing and visibly its stillest "
            "point, the guards' knuckles tight on their "
            "hilts while his hands hang open — a "
            "circle of armed men gripping their weapons "
            "around a captive who is holding the entire "
            "night together by consent. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b17", "out": "s17-he-was-laying-his-life.jpeg", "seg": "n3",
        "window": "91.67-98.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GARDEN"],
        "narration": (
            "He was laying his life down on purpose, and he would not spill one "
            "drop of someone else's blood to save his own."
        ),
        "must_show": "the policy of the cross — close on Jesus's face: the purpose settled, the refusal absolute; a life being laid down with both hands, no one else's included.",
        "must_not_show": "no halo, glare or rim-light on Jesus; resolve without grimness — the gravest generosity in the row.",
        "scene": (
            "Close on Jesus's face in the mixed torch "
            "and moonlight: the purpose long settled "
            "behind the warm eyes — no flinch toward "
            "escape, no glance at the sheathed sword's "
            "option — a man walking to his own death by "
            "choice and drawing the line of that choice "
            "around himself alone, tight enough that "
            "not one other drop of anyone falls inside "
            "it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r066-b18", "out": "s18-and-then-he-did-the.jpeg", "seg": "n4",
        "window": "99.27-102.22", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MALCHUS", "GARDEN"],
        "narration": "And then he did the most extraordinary thing in the whole arrest.",
        "must_show": "the turn — Jesus turning AWAY from his own crisis toward the kneeling clamped-handed Malchus; attention crossing enemy lines.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the direction the beat — away from self, toward the hurt man who came to seize him.",
        "scene": (
            "With the mob's hands already reaching for "
            "him Jesus turns — away from his own "
            "arrest, his whole attention crossing the "
            "trampled grass to where the neat "
            "charcoal-clad servant kneels with his hand "
            "still clamped to the side of his head — "
            "the seized man moving toward the injured "
            "seizer while the night stands confused "
            "around the wrong direction of his concern. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r066-b19", "out": "s19-with-the-mob-closing-in.jpeg", "seg": "n4",
        "window": "102.22-109.23", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MALCHUS", "MOB", "GARDEN"],
        "narration": (
            "With the mob closing in to seize him, with his own death now "
            "minutes away, Jesus turned to the injured man."
        ),
        "must_show": "the clock and the kindness — the guards' hands actually ON Jesus's arms as he leans TOWARD the kneeling Malchus; mercy performed inside the arrest itself.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the seizure and the compassion simultaneous — grip on his arms, his focus on the hurt man.",
        "scene": (
            "The arrest and the mercy share one frame: "
            "two guards' hands already gripping Jesus's "
            "arms from behind — and he leaning forward "
            "against their hold, toward the kneeling "
            "servant, his attention bent entirely on "
            "the clamped hand and the white face below "
            "him — a man being taken and giving, in the "
            "same motion, in the same second, with his "
            "own death already holding his sleeves. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r066-b20", "out": "s20-not-his-friend-his-enemy.jpeg", "seg": "n4",
        "window": "109.23-114.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["MALCHUS"],
        "narration": (
            "Not his friend. His enemy — one of the very people who had come "
            "for him."
        ),
        "must_show": "the recipient's colours — close on Malchus: the high priest's oxblood sash plain on the charcoal tunic, the enemy's uniform on the mercy's addressee.",
        "must_not_show": "no halo, glare or rim-light; the sash the beat — whose man he is, and to whom kindness is coming anyway.",
        "scene": (
            "Close on the kneeling Malchus in the "
            "torchlight: the deep oxblood sash of the "
            "high priest's household crossing his "
            "charcoal tunic plain as a banner — the "
            "livery of the very house that ordered "
            "tonight — worn by the one man in the "
            "clearing about to receive the last free "
            "kindness of the man it came to take. Every "
            "figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r066-b21", "out": "s21-and-he-said-suffer-ye.jpeg", "seg": "n4 + j2 + n5",
        "window": "114.69-121.05", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MALCHUS", "MOB"],
        "narration": "And he said: Suffer ye thus far. Let me do this one last thing.",
        "must_show": "SCRIPTURE-EXACT: the permission asked — Jesus, held, speaking calmly to his captors: the request to be allowed one act; the guards' grips uncertainly loosening.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the courtesy surreal and real — a prisoner asking leave, captors granting it without understanding why.",
        "scene": (
            "Held by both arms, Jesus speaks calmly "
            "past his captors' shoulders — the request "
            "plain in his level face — and the grip on "
            "him loosens by confused degrees, one "
            "guard glancing at the other, the mob's "
            "machinery pausing around a courtesy it "
            "has no procedure for: a prisoner asking "
            "permission to finish being himself, one "
            "more time. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b22", "out": "s22-and-he-reached-out-touched.jpeg", "seg": "n5",
        "window": "121.05-125.47", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MALCHUS", "GARDEN"],
        "narration": (
            "And he reached out, touched the side of the man's head, and made "
            "him whole."
        ),
        "must_show": "SCRIPTURE-EXACT: THE healing — Jesus's palm laid gently over the place where Malchus's hand was clamped, the servant's own hand fallen away; the touch, and the making whole.",
        "must_not_show": "NO wound shown at any point — the palm covers the place entirely; no halo, glare or rim-light; the miracle as a hand's warmth.",
        "scene": (
            "Freed to the length of one arm, Jesus lays "
            "his palm gently over the side of the "
            "kneeling man's head — Malchus's own "
            "clamped hand fallen away to his knee, his "
            "white face tipped up in blank shock under "
            "the touch — the healer's fingers curved "
            "warm against the dark hair, the whole "
            "miracle happening in the private darkness "
            "under one palm, in front of forty torches. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r066-b23", "out": "s23-the-last-miracle-jesus-performed.jpeg", "seg": "n5",
        "window": "125.47-133.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["MALCHUS", "GARDEN"],
        "narration": (
            "The last miracle Jesus performed as a free man was healing an "
            "injury done by his own defender, to one of the men arresting him."
        ),
        "must_show": "the wholeness found — Malchus's own astonished fingers exploring the healed side of his head: whole skin, whole ear, no mark; disbelief conducting its audit.",
        "must_not_show": "no halo, glare or rim-light; this stays IN THE OLIVE GARDEN at night — olive trees, terrace grass and the distant city lamps behind him, NEVER a stone city wall or masonry fortress background; ANY torch in frame is an ancient hand-held wooden torch or pitch brand — NEVER a modern segmented BAMBOO TIKI-TORCH, garden flare, patio/luau torch or metal-canister torch; the audit's result perfect — fingers finding nothing but wholeness; the face doing the arithmetic.",
        "scene": (
            "Close on Malchus, still in the moonlit olive "
            "garden with the ancient olive trunks and the "
            "far city lamps soft behind him: his own "
            "trembling fingers moving over the right side "
            "of his head — tracing the whole unmarked "
            "skin, the whole present ear, again, and again "
            "from a different angle — his careful "
            "official's face abandoned to open-mouthed "
            "audit, checking a ledger whose one "
            "catastrophic entry has been erased by hand. "
            "The background is the garden at night, not a "
            "wall. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r066-b24", "out": "s24-think-about-what-malchus-carried.jpeg", "seg": "n6",
        "window": "134.24-136.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["MALCHUS", "GARDEN"],
        "narration": "Think about what Malchus carried home that night.",
        "must_show": "the carrying — Malchus standing apart from the mob's business, hand still at the side of his head, staring at the bound man being led away; a functionary rearranged.",
        "must_not_show": "no halo, glare or rim-light; his apartness the beat — the arrest proceeding without his attention.",
        "scene": (
            "While the mob's business closes around its "
            "prisoner, Malchus stands apart at the "
            "clearing's edge — his hand drifted back up "
            "to touch the healed side of his head, his "
            "quick eyes following the bound figure "
            "being led down through the torches — a "
            "capable man standing completely still in "
            "the middle of his own completed errand, "
            "carrying something the arrest report will "
            "have no column for. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b25", "out": "s25-he-had-come-with-a.jpeg", "seg": "n6",
        "window": "136.81-141.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["MALCHUS"],
        "narration": "He had come with a mob to seize a man — and that man healed him.",
        "must_show": "the inversion held — close on Malchus's face working through it: the errand's logic and the touch's fact refusing to reconcile.",
        "must_not_show": "no halo, glare or rim-light; the incompatibility visible — two truths grinding in one expression.",
        "scene": (
            "Close on Malchus's torch-lit face as the "
            "two facts grind: the errand — seize him — "
            "still filed in the official's eyes, and "
            "the touch — he healed me — resident now in "
            "the hand that keeps returning to the side "
            "of his head — a man's whole working "
            "cosmology jammed between one order and "
            "one kindness that cannot both be right. "
            "Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r066-b26", "out": "s26-whatever-he-had-believed-walking.jpeg", "seg": "n6",
        "window": "141.29-148.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["MALCHUS", "GARDEN"],
        "narration": (
            "Whatever he had believed walking up that hill, he walked back down "
            "it whole, touched by the very person he came to hurt."
        ),
        "must_show": "the descent changed — Malchus walking down the hill path behind the torch line, lagging, his hand at his healed ear, the city's lamps below; the same hill, a different man.",
        "must_not_show": "no halo, glare or rim-light; the lag the beat — last in the column, slowest, rearranged.",
        "scene": (
            "Down the moon-silvered hill path the "
            "torch line descends toward the city's far "
            "lamps — and at its tail Malchus walks "
            "slower than all of them, falling behind "
            "by degrees, his hand rising once more to "
            "the side of his head, his face turned "
            "half back up the slope toward the garden — "
            "a man descending the exact hill he "
            "climbed an hour ago, in a different "
            "world. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r066-b27", "out": "s27-you-do-not-forget-a.jpeg", "seg": "n6",
        "window": "148.89-151.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["MALCHUS"],
        "narration": "You do not forget a thing like that.",
        "must_show": "the permanence — extreme close: Malchus's fingers resting at his whole right ear, eyes far away; the touch installed for life.",
        "must_not_show": "no halo, glare or rim-light; the gesture already habitual — a lifelong reflex being born.",
        "scene": (
            "Extreme close in the night's edge-light: "
            "Malchus's fingers resting lightly against "
            "his whole right ear, barely touching, the "
            "way a man touches a scar that isn't "
            "there — and his quick intelligent eyes "
            "aimed at nothing, all their attention "
            "turned inward on one hand's remembered "
            "warmth — the first performance of a "
            "gesture he will repeat, unthinking, for "
            "the rest of his life. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b28", "out": "s28-this-is-who-he-is.jpeg", "seg": "n7",
        "window": "152.26-159.97", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOB", "GARDEN"],
        "narration": (
            "This is who he is, even at his own arrest, even on the worst night "
            "of his life: he will not let the moment be about violence."
        ),
        "must_show": "the character summed — Jesus bound and led down through the torches, upright and unbroken, the garden quieting behind; the arrest owned by his peace, not their iron.",
        "must_not_show": "no halo, glare or rim-light on Jesus; bound wrists, unbowed bearing — the night's meaning carried by his calm.",
        "scene": (
            "Down through the torch line, the camera behind the "
            "descending column, Jesus is led "
            "with his wrists bound before him — and the "
            "procession's meaning has quietly changed "
            "hands: the guards grip and hurry, but the "
            "bound man walks upright and unhurried at "
            "their centre, his peace setting the pace, "
            "the trampled garden stilling behind them — "
            "an arrest being conducted, unmistakably, "
            "on the prisoner's terms. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r066-b29", "out": "s29-he-heals-the-hand-raised.jpeg", "seg": "n7",
        "window": "159.97-166.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["GARDEN"],
        "narration": (
            "He heals the hand raised against him. There is no one on the wrong "
            "side of the sword he is unwilling to reach toward."
        ),
        "must_show": "the closing image — the emptied garden at deep night: the trampled grass, a dropped stave, Malchus's guttering fallen torch — and the low prayer rock quiet under the moon; mercy's battlefield, swordless.",
        "must_not_show": "no halo, glare or rim-light; no figures — the aftermath still; the fallen torch's last ember the only warmth.",
        "scene": (
            "The garden stands emptied under the low "
            "moon: trampled spring grass, a dropped "
            "wooden stave, Malchus's fallen torch "
            "guttering its last ember in the green — "
            "and beyond them, silver and quiet, the "
            "low prayer rock where the night began — "
            "the whole battlefield of the kingdom's "
            "one drawn sword, holding nothing by "
            "morning but grass, ash, and the mark of "
            "knees. Every figure has two arms, two "
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
    "GARDEN": "PLACE-REF/garden.jpeg",  # build-66-malchus-ear s01-it-was-the-middle-of (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "MALCHUS": "CAST-REF-V2/malchus.jpeg",
}
