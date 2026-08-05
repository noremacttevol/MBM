#!/usr/bin/env python3
"""V2 beat map — row 125, build-125-i-never-knew-you (Matthew 7:21-23).

COVERAGE: 15 pictures over 85.4 s = 5.7 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 7 KJV):
  7:21  "NOT EVERY ONE that saith unto me, LORD, LORD, shall enter
        into the kingdom of heaven; but HE THAT DOETH THE WILL of my
        Father which is in heaven."
  7:22  "Many will say to me IN THAT DAY, Lord, Lord, have we not
        PROPHESIED in thy name? and in thy name have CAST OUT DEVILS?
        and in thy name done many WONDERFUL WORKS?" — every clause
        about what THEY did.
  7:23  "And then will I profess unto them, I NEVER KNEW YOU: depart
        from me, ye that work iniquity." — the missing thing is
        acquaintance, not accomplishment.
  Setting: the close of the Sermon on the Mount — the same hillside
  as rows 121-124.

RENDERING LAWS (content-care — this is the library's most sobering
sermon row; the narration's own frame governs: "this is not a threat
to scare you. It is an invitation to be known"):
  - "THAT DAY" is rendered as a THRESHOLD OF WARM LIGHT — a great
    door and quiet radiant morning beyond it. NO fire, NO darkness
    swallowing anyone, NO wrath-face, NO falling figures, ever.
  - b12's "I never knew you" is spoken in GRIEF — Jesus's face
    carries sorrow and loss, never fury; the turning-away pleaders
    walk into ordinary dim ground, not torment. Any render with
    flames, terror faces, or an angry Jesus is an automatic reject.
  - The pleaders are EARNEST, not villains — their arms genuinely
    full of genuinely impressive works; the missing thing is only
    acquaintance. Their scroll-lists are indistinct period script,
    no readable modern text.
  - The counter-image is WALKING WITH HIM — road, conversation, a
    free hand; it appears at b11/b14 and the row ENDS on the door
    standing OPEN (b15). The last frame is invitation, full stop.
  - HILLSIDE and CROWD locks are BYTE-IDENTICAL to builds 121-124.

TIME OF DAY ARC (intentional): the hillside in the sermon's warm
late-afternoon gold; the door/threshold frames in a timeless warm
morning light (the light BEYOND the door always warmer than the
ground before it); the walking-with frames at golden hour; the close
on the open door's warmth.

CHANGING CONDITION (kept OUT of the locks): the great door — closed
through the pleading beats, OPEN at the close; the pleaders' arms —
full of works early, the one known walker's hand free.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags.
LOCKS = {
    "HILLSIDE": (
        "HILLSIDE LOCK: the teaching hillside — a green grassy slope "
        "above the Sea of Galilee, wildflowers in the grass, the "
        "blue lake and far hills below, warm late-afternoon light. "
        "The same slope and lake view throughout."
    ),
    "CROWD": (
        "CROWD LOCK: the listening crowd — ordinary Galileans seated "
        "on the grass: weathered fishermen, mothers with children, "
        "sun-browned farmers, a few elders; varied earth-toned robes "
        "of brown, rust, olive and slate (no cream — only Jesus "
        "wears cream), varied ages and faces, never uniform."
    ),
    "DOOR": (
        "DOOR LOCK: the great door — a tall double door of heavy "
        "honey-brown wood in a pale stone wall, standing alone on a "
        "quiet plain, with a warm clear morning light living beyond "
        "its seams; solemn and beautiful, never menacing. The same "
        "door and wall throughout."
    ),
    "PLEADERS": (
        "PLEADERS LOCK: the pleaders — a varied group of earnest, "
        "respectable men and women in fine dark robes of deep blue, "
        "umber and wine (no cream — only Jesus wears cream), arms "
        "laden with rolled scroll-lists and tokens of great works; "
        "sincere and impressive, never sneering, never villains."
    ),
    "ROAD": (
        "ROAD LOCK: the walking road — a pale country road through "
        "green fields at golden hour, unhurried and open, far hills "
        "soft with evening. The same road throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r125-b01", "out": "s01-jesus-warned-that-saying-the.jpeg", "seg": "n0",
        "window": "0.28-3.86", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Jesus warned that saying the right words is not the same as "
            "knowing him."
        ),
        "must_show": "the sermon's gravest turn — Jesus seated teaching on the hillside, the crowd hushed; the warmth still present but the weight unmistakable.",
        "must_not_show": "no halo, glare or rim-light on Jesus; grave WARMTH — no sternness, no fear on the faces yet.",
        "scene": (
            "The sermon arrives at its weightiest ground, the "
            "camera looking past the seated crowd's backs up the "
            "gold slope: Jesus seated above the blue lake as he "
            "has been all afternoon — but the hillside has gone "
            "quiet in a new way, fishermen still, children "
            "sensing the change in the air the way children do — "
            "the teacher's face as warm as ever and more grave "
            "than it has been, a man about to separate, gently "
            "and forever, two things everyone present has been "
            "confusing: saying his name, and knowing him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b02", "out": "s02-the-door-is-not-opened.jpeg", "seg": "n0",
        "window": "3.86-6.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["DOOR"],
        "narration": "The door is not opened by a name we repeat.",
        "must_show": "the door introduced — the great honey-wood double door closed in its pale wall, warm light living at its seams, one small figure before it, lips moving; the name alone not moving it.",
        "must_not_show": "no halo; the door SOLEMN and beautiful, never menacing; the figure earnest, not desperate.",
        "scene": (
            "The image the whole warning lives in stands closed "
            "on a quiet plain: a great double door of heavy "
            "honey-brown wood set in pale stone, warm morning "
            "light breathing at its seams from whatever country "
            "lies beyond — and before it, small against the "
            "timber, a single figure with lips moving around a "
            "name, repeating it carefully, correctly, again — "
            "the word arriving at the wood and the wood staying "
            "wood, because this door has never once in its "
            "existence been opened by pronunciation. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b03", "out": "s03-not-every-one-that-saith.jpeg", "seg": "j1",
        "window": "7.24-16.11", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILLSIDE", "CROWD"],
        "narration": (
            "Not every one that saith unto me, Lord, Lord, shall enter into "
            "the kingdom of heaven; but he that doeth the will of my Father "
            "which is in heaven."
        ),
        "must_show": "SCRIPTURE-EXACT: the warning given — Jesus level and unhurried, one hand gently setting aside (the saying) and the other affirming forward (the doing); the crowd absorbing the weight.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gravity LOVING — a rescue being attempted, not a sentence passed.",
        "scene": (
            "The two things are separated with surgical "
            "gentleness: Jesus's left hand moves in a small "
            "setting-aside — not every one that SAITH — and his "
            "right comes forward open and firm — but he that "
            "DOETH — the whole eternal sorting performed quietly "
            "between two hands in the gold light, while the "
            "crowd takes the weight of it row by row: the most "
            "religious words in the language, gently moved off "
            "the foundation, and a lived obedience set down "
            "where they stood. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r125-b04", "out": "s04-not-everyone-who-calls-me.jpeg", "seg": "n1",
        "window": "17.67-24.81", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Not everyone who calls me Lord will come into the kingdom, he "
            "said — only the one who actually does what my Father wants."
        ),
        "must_show": "saying vs doing in one street — foreground: a robed man declaiming loudly on the synagogue steps; background: a plain man quietly shouldering a widow's heavy water jars up the lane.",
        "must_not_show": "no halo; the declaimer SINCERE, not a cartoon; the doer unnoticed by everyone in the frame but the widow.",
        "scene": (
            "The difference is on display in one ordinary "
            "street: on the synagogue steps a robed man "
            "declaims with his arms lifted, the holy words loud "
            "and correct and admired by the small ring around "
            "him — while far up the lane behind, unnoticed by "
            "everyone except the bent widow beside him, a plain "
            "man has simply taken her two heavy water jars onto "
            "his own shoulders and walks her slow pace home — "
            "the same afternoon, the same street: one Lord-Lord "
            "said beautifully, one will of the Father done. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b05", "out": "s05-words-are-cheap-a-life.jpeg", "seg": "n1",
        "window": "24.81-27.92", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Words are cheap. A life is not.",
        "must_show": "the price difference — close on work-worn hands: setting down a widow's jars, a mended tool, bread halved for sharing; a life's currency in one frame of hands.",
        "must_not_show": "no halo; hands ONLY carry the frame — no faces needed; period-true objects.",
        "scene": (
            "The exchange rate is printed on a pair of hands: "
            "close on the plain man's work-worn fingers as they "
            "set the widow's jars gently down inside her door — "
            "knuckles rope-scarred, nails split from other "
            "people's mended fences and shouldered loads, a "
            "half-loaf already broken for sharing tucked in the "
            "crook of one arm — a currency that cannot be "
            "counterfeited by any accent or repetition: the "
            "kind of hands a life leaves on a person, priced "
            "accordingly. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r125-b06", "out": "s06-and-then-he-described-a.jpeg", "seg": "n1",
        "window": "27.92-32.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["DOOR", "PLEADERS"],
        "narration": (
            "And then he described a day when many will point to everything "
            "they did in his name."
        ),
        "must_show": "the day assembled — before the great closed door, the gathered pleaders in fine robes, arms full of scroll-lists, waiting in the warm strange light; solemn, not terrifying.",
        "must_not_show": "ABSOLUTE: no fire, no darkness, no fear-faces — a solemn luminous morning; the pleaders dignified and hopeful.",
        "scene": (
            "The day he described assembles in warm strange "
            "light: before the great closed door the many have "
            "gathered — men and women in fine deep-toned robes, "
            "respectable, accomplished, every pair of arms laden "
            "with rolled lists and tokens of real works — a "
            "crowd of impressive lives waiting on a quiet plain "
            "in morning light that comes from no visible sun — "
            "nothing burning, nothing dark, nothing to fear in "
            "the frame except one closed door and the question "
            "of what actually opens it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b07", "out": "s07-many-will-say-to-me.jpeg", "seg": "j2",
        "window": "33.62-38.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["DOOR", "PLEADERS"],
        "narration": (
            "Many will say to me in that day, Lord, Lord, have we not "
            "prophesied in thy name?"
        ),
        "must_show": "SCRIPTURE-EXACT: the pleading begun — the foremost pleaders with arms extended toward the door, faces earnest and confident, the first credentials offered.",
        "must_not_show": "ABSOLUTE: no fire, no terror — earnest confidence; the door unmoved.",
        "scene": (
            "The pleading opens with the strongest credentials "
            "first: the foremost of the crowd step toward the "
            "great door with their arms extended, faces lifted "
            "in earnest confidence — Lord, Lord — the words "
            "correct, the record real, the prophesying "
            "genuinely done and genuinely in that name — a case "
            "presented by people who have every reason to "
            "expect the timber to move — and the door standing "
            "exactly as it stood, warm light breathing at its "
            "seams, listening for something else. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b08", "out": "s08-and-in-thy-name-have.jpeg", "seg": "j2",
        "window": "38.45-44.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["DOOR", "PLEADERS"],
        "narration": (
            "and in thy name have cast out devils? and in thy name done many "
            "wonderful works?"
        ),
        "must_show": "the credentials mounting — pleaders lifting their bundled scroll-lists and work-tokens higher toward the door, the stack of wonderful works growing between them and the timber.",
        "must_not_show": "ABSOLUTE: no fire, no terror; the scroll script INDISTINCT — no readable text; the works impressive, the door still.",
        "scene": (
            "The case grows taller by the sentence: bundled "
            "scroll-lists lift higher toward the door, arms "
            "raising tokens of works that were, by every "
            "account, wonderful — devils truly driven out, "
            "mighty things truly done, all of it truly in that "
            "name — the evidence stacking up between the "
            "pleaders and the timber until the space before the "
            "door is a wall of accomplishment — and still the "
            "warm light breathes unhurried at the seams, "
            "unimpressed by volume, waiting for the one word "
            "the whole pile is missing. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b09", "out": "s09-lord-they-will-say-we.jpeg", "seg": "n2",
        "window": "46.12-51.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["DOOR", "PLEADERS"],
        "narration": (
            "Lord, they will say, didn't we prophesy in your name? Didn't we "
            "drive out devils in your name?"
        ),
        "must_show": "one pleader close — an earnest, genuinely good face, arms full of a life's works, pleading the list with complete sincerity; sympathy, not satire.",
        "must_not_show": "ABSOLUTE: no fire, no terror; the face SYMPATHETIC — we are meant to see ourselves, not a fool.",
        "scene": (
            "One face carries the whole crowd's case: close on "
            "a single pleader — a good face, an earnest face, "
            "the face of somebody's beloved teacher or faithful "
            "elder — arms cradling a life's worth of rolled "
            "works, eyes on the door with complete sincerity: "
            "didn't we? in YOUR name? — and there is nothing to "
            "mock in it and everything to grieve, because every "
            "word is true, and the door is not asking about "
            "any of it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r125-b10", "out": "s10-we-do-all-kinds-of.jpeg", "seg": "n2",
        "window": "51.85-57.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["PLEADERS"],
        "narration": (
            "Didn't we do all kinds of wonderful works in your name? Listen "
            "to what is missing from that list."
        ),
        "must_show": "the missing thing made visible — close on a pleader's arms stacked completely full of scroll-works: both hands occupied, no hand free; the fullness itself the problem.",
        "must_not_show": "ABSOLUTE: no fire; the composition's point EXACT — arms full to the chin, not one hand free to be held.",
        "scene": (
            "What is missing is visible in what is full: close "
            "on a pleader's arms stacked to the chin with "
            "rolled works — prophecies, rescues, wonders, the "
            "whole magnificent inventory clutched tight — both "
            "hands entirely occupied with the carrying of it, "
            "so that in all that armload there is not one "
            "finger free to be simply taken and held — a life "
            "so full of things done FOR him that no hand was "
            "ever left empty to walk WITH him. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b11", "out": "s11-every-single-sentence-is-about.jpeg", "seg": "n2",
        "window": "57.62-62.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "Every single sentence is about what they did. Not one of them "
            "is about him."
        ),
        "must_show": "the counter-image — on the golden road, Jesus walking WITH a plain companion in easy conversation, the companion's hands free and empty; acquaintance itself pictured.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the companion's hands visibly FREE — nothing carried, nothing performed.",
        "scene": (
            "What the list never mentions looks like this: the "
            "pale road at golden hour, and on it Jesus walking "
            "WITH a plain companion — matched stride, heads "
            "inclined toward each other in easy unhurried "
            "conversation, the companion's hands entirely free "
            "and empty at his sides — no works carried, no "
            "credentials presented, nothing in the frame being "
            "done in anybody's name — just the one thing every "
            "sentence at the door forgot to be about: him, "
            "known, walked with, on an ordinary road. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b12", "out": "s12-and-then-will-i-profess.jpeg", "seg": "j3",
        "window": "63.46-70.20", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DOOR"],
        "narration": (
            "And then will I profess unto them, I never knew you: depart "
            "from me, ye that work iniquity."
        ),
        "must_show": "SCRIPTURE-EXACT, GRIEF NOT WRATH — Jesus at the door speaking the sentence with visible sorrow, and the pleaders turning away across ordinary dim ground; loss, not punishment, in every face.",
        "must_not_show": "ABSOLUTE: no fire, no torment, no fury on Jesus — his face GRIEVES; the departing walk into plain dusk-dim ground, nothing more.",
        "scene": (
            "The saddest sentence in the sermon is spoken in "
            "grief: Jesus stands at the great door and his face "
            "as he says it is not fury but loss — the sorrow of "
            "a man naming an acquaintance that never happened — "
            "I never KNEW you — and before him the laden "
            "pleaders turn away across the plain's ordinary "
            "dimming ground, their armloads still magnificent "
            "and still carried, walking back the way they came "
            "under a fading light — no flames anywhere, no "
            "terror: only distance, which was the whole tragedy "
            "all along. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r125-b13", "out": "s13-he-is-not-weighing-the.jpeg", "seg": "n3",
        "window": "71.69-74.02", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "He is not weighing the size of anyone's list.",
        "must_show": "the unused scale — a merchant's balance set aside empty against the wall, and beside it two hands simply clasped, one holding the other; measurement retired, acquaintance in its place.",
        "must_not_show": "no halo; the balance EMPTY and set aside; the handclasp warm and plain.",
        "scene": (
            "The instrument everyone expected is off duty: a "
            "merchant's brass balance leans against the pale "
            "wall, pans empty, beam idle — no list weighed on "
            "it today, no works counted, the whole measuring "
            "trade retired — and beside it, filling the frame "
            "with the only arithmetic in use, two hands simply "
            "clasped: one holding the other, warm, known, "
            "familiar — the entire examination, it turns out, "
            "having always consisted of whether the hands had "
            "ever met. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r125-b14", "out": "s14-he-is-asking-whether-we.jpeg", "seg": "n3",
        "window": "74.02-79.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "He is asking whether we ever really walked with him. And this "
            "is not a threat to scare you."
        ),
        "must_show": "the walking-with again — the golden road, Jesus and the companion further along it now, the light warm on both; the question's real subject pictured as friendship.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NOTHING ominous — the frame is entirely warm.",
        "scene": (
            "The real question has a picture, and it is this "
            "one: further down the golden road the two walkers "
            "go on together — Jesus and his companion small now "
            "against the long warm light, the road unspooling "
            "easy ahead of them, a laugh visibly passing "
            "between the two figures — miles of ordinary "
            "walked-together evenings, the thing the question "
            "was always actually asking about — and not one "
            "shadow in the whole frame, because the question "
            "was never designed to frighten anybody. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r125-b15", "out": "s15-it-is-an-invitation-to.jpeg", "seg": "n3",
        "window": "79.33-85.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["DOOR"],
        "narration": (
            "It is an invitation to be known — to walk with him, not just "
            "speak his name."
        ),
        "must_show": "the closing invitation — the great door standing OPEN on warm morning country, Jesus beside it with a hand extended in welcome toward the viewer's ground; the whole warning resolved into invitation.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the door WIDE OPEN — the final image is welcome, nothing else.",
        "scene": (
            "The last frame turns the whole warning inside out: "
            "the great honey-wood door stands wide OPEN, and "
            "the warm morning country beyond it lies visible at "
            "last — green and lit and unhurried — while beside "
            "the open timber Jesus stands with one hand "
            "extended outward in plain welcome, the grief gone "
            "from his face and the invitation in its place — "
            "not a test to pass but a friendship to begin, the "
            "door never having wanted anything at all except "
            "to be walked through together. Every figure has "
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
    # ROAD: build-38 b39 auto-match REJECTED (road-through-a-doorway frame,
    # arid hills — not this row's golden green walking road) — promote-first from b11.
}
# === end PLACE-PLATES ===
