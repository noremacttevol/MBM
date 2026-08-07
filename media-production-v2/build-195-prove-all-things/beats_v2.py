#!/usr/bin/env python3
"""V2 beat map — row 195, build-195-prove-all-things (1 Thessalonians 5:20-22 — "Despise not
prophesyings. Prove all things; hold fast that which is good. Abstain from all appearance of
evil.").

COVERAGE: 14 pictures over 48.190 s (card_start) = ~3.44 s/picture (lesson 12 movie-coverage).
Three places: PAUL-ROOM (Paul writing the letter — the epistle source), the MARKET (a
first-century marketplace where a representative BELIEVER PROVES / tests / weighs things, holds
the good up to the daylight, and turns from a shadowed doorway at the market's edge — "abstain
from all appearance of evil"), and the GATHERING (an assembly where a human PROPHET speaks
God's word and the believer weighs it rather than despising it — "despise not prophesyings").
Human spine: ONE BELIEVER who tests everything and holds fast the good; PAUL frames it.

=====================================================================
No open Cameron complaint (v2_outline.py 195). Fresh V2 beat map; Board Audio = OK.
=====================================================================

SPEAKER LAW (Paul's epistle):
  s1  1 Thess 5:21  "Prove all things; hold fast that which is good."  = SCRIPTURE → LIGHT-BLUE.
  s2  1 Thess 5:22  "Abstain from all appearance of evil."            = SCRIPTURE → LIGHT-BLUE.
Every other segment (n0, n1, n1b, n2, n3, n4, card) is the NARRATOR → white. There is NO
red-letter and NO God-voice in this row: **every beat jesus=False and NO ONE wears cream or
white** (cream is reserved for Jesus, who is absent — this is an epistle).

**HARD GATE — GOD / THE HOLY SPIRIT / THE VOICE OF GOD IS NEVER EMBODIED.** "Prophesyings",
"God's voice" and "how you recognize it" are NEVER shown as a divine figure, face, dove, beam,
hand-from-sky, ring or symbol. Prophesying is carried by an ORDINARY HUMAN PROPHET speaking to
the assembly (a real man, no divine light on or around him) and by the believer's face of
recognition as he weighs the words. "Hold it up to the light" is ordinary DAYLIGHT / sunlight
through a window or open sky, never a supernatural beam. Drift-word gate: no halo / glow /
rim-light / beam anywhere.

CONTENT-CARE: "Prove all things" is honest, patient TESTING — a merchant assaying goods on a
balance, holding cloth or a coin up to the daylight — never suspicion, sneering or contempt.
"Despise not prophesyings" shows the believer LISTENING and weighing, never mocking the
prophet. "Abstain from all appearance of evil" is a quiet TURNING AWAY from a shadowed
doorway at the market's edge — restraint and clean conscience, never violence, gore or
anything lurid shown in the doorway (it stays dark and unspecified).

TIME-OF-DAY: warm ordinary daylight throughout (PAUL-ROOM soft daylight; MARKET bright day;
GATHERING daylight through the openings). The one shadow is the doorway the believer turns
FROM — a dark alley off the bright square, contrast within daylight, never night, never divine
light.

PLACES / LOCKS:
  PAUL-ROOM  Paul's writing room (b01) — reused BYTE-IDENTICAL to build-184/186/194 (recurring
             place); runner may --wire the existing PAUL-ROOM plate.
  MARKET     the first-century marketplace where the believer proves, weighs, holds fast, and
             turns from the shadowed doorway (b02-b06, b09-b14). NEW build-local place; runner
             promotes from b02.
  GATHERING  the assembly where the human prophet speaks and the believer weighs it (b07/b08).
             NEW build-local place; runner promotes from b07.
People locks: PAUL (BYTE-IDENTICAL to build-184/186/194 — recurring cast), BELIEVER (the
representative person who tests everything and holds fast the good — recurring across the
frames), PROPHET (an ordinary aged human messenger speaking God's word in the gathering — a
real man, NOT a divine figure), HEARERS (the assembly weighing the prophesying), TRADERS (the
market people). None wear cream or white.

AUDIO: default AUDIO LOCK stream-copy (no re-voice; no open complaint). Board Audio = OK.
card_start = 48.190 s. Picture-only — do NOT re-voice.
"""

# PAUL + PAUL-ROOM are reused BYTE-IDENTICAL to build-184/186/194 (recurring cast/place). MARKET
# and GATHERING are NEW build-local places the runner promotes. Jesus is absent (every beat
# jesus=False); no image REFS; only text locks. No one wears cream/white; God / the Holy Spirit
# / the voice of God is never embodied.
LOCKS = {
    "PAUL-ROOM": (
        "PAUL-ROOM LOCK: the same place in every frame — a humble first-century room "
        "where Paul writes his letters: plain lime-plastered stone walls, a low wooden "
        "writing table with a sheet of parchment, a reed pen and a small clay oil lamp, "
        "a simple stool and a floor mat, and one plain rectangular window opening to "
        "soft daylight. Ancient, spare, real; no modern object anywhere; any parchment "
        "is blank with no legible or rendered writing. The same room and warm plain "
        "daylight throughout."
    ),
    "MARKET": (
        "MARKET LOCK: the same place in every frame — an ordinary first-century "
        "marketplace on a bright day: worn stone paving and low mud-brick stalls, woven "
        "awnings, baskets of grain, figs and cloth, a money-changer's low table with a "
        "small hand balance and its brass weights, a stone well-head at one side, and at "
        "the market's far edge a narrow dark alley with one shadowed doorway. Ancient and "
        "real; no modern object anywhere; nothing legible or rendered is written on any "
        "surface. The same square and warm daylight throughout, the alley doorway always "
        "dark and unspecified."
    ),
    "GATHERING": (
        "GATHERING LOCK: the same place in every frame — a plain first-century meeting "
        "room where believers assemble: bare plastered stone walls, a few low benches and "
        "floor mats, plain wooden shutters open to warm daylight, no ornament. Ancient and "
        "real; no modern object anywhere; nothing legible or rendered is written on any "
        "surface. The same room and warm daylight throughout."
    ),
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact and wiry, about "
        "fifty, balding with a fringe of dark hair, a full pointed dark beard, keen "
        "deep-set eyes, in a plain DARK RUST-BROWN travel robe (never cream, never "
        "white); a tentmaker's strong hands; earnest fire without anger."
    ),
    "BELIEVER": (
        "BELIEVER LOCK: the same person in every frame they appear — a representative "
        "first-century man of about thirty-five who tests everything and keeps the good, "
        "warm olive-brown skin, dark hair, a short dark beard, keen steady discerning "
        "eyes, in a plain muted OLIVE-GREEN-AND-BROWN wool tunic and mantle (never cream, "
        "never white). Careful, honest, unhurried — the one who weighs a thing before he "
        "holds to it. The same face and clothing throughout."
    ),
    "PROPHET": (
        "PROPHET LOCK: an ordinary aged human messenger who speaks God's word in the "
        "assembly — about sixty-five, weathered face, a long grey beard, plain undyed "
        "GREY-BROWN wool robe (never cream, never white), an open earnest hand raised as "
        "he speaks. He is a REAL MAN and nothing more — no divine light on him or around "
        "him, no halo, no beam, no symbol. The same man wherever he appears."
    ),
    "HEARERS": (
        "HEARERS LOCK: the believers of the assembly — a mixed group of ordinary "
        "first-century men, women and a child in plain earth-toned wool (never cream, "
        "never white), listening and weighing the prophet's words. Distinct individual "
        "faces, not twins. The same kind of people throughout."
    ),
    "TRADERS": (
        "TRADERS LOCK: the ordinary people of the marketplace — first-century merchants, "
        "buyers and a money-changer in plain earth-toned wool (never cream, never white), "
        "going about honest trade. Distinct individual faces, not twins. The same kind of "
        "people throughout."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r195-b01", "out": "s01-paul-writes.jpeg", "seg": "n0",
        "window": "0.000-2.700", "wide": True, "jesus": False, "ref": False,
        "locks": ["PAUL-ROOM", "PAUL"],
        "narration": "Paul gave the early church a short, sharp command",
        "must_show": "the establishing frame, NON-Jesus (the PAUL-ROOM plate) — Paul at his low writing table in soft daylight, reed pen over a blank parchment, writing earnestly to the churches.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure, dove or beam; no legible or rendered writing on the parchment; no halo, glare or rim-light; no modern object; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing shot of Paul's humble writing room in soft daylight, camera "
            "set low and behind Paul's shoulder looking past him to the sunlit window, so "
            "his back is three-quarters to the lens and his gaze goes down onto the "
            "parchment and out to the window, never to the camera: Paul — compact, "
            "dark-bearded, in a dark rust-brown travel robe (not cream) — sits at his low "
            "table, reed pen over a blank parchment, writing earnestly. A small clay lamp "
            "and the plain window. Ancient and spare; the parchment carries nothing "
            "legible; warm daylight rests on him, not around his head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b02", "out": "s02-the-market.jpeg", "seg": "n0",
        "window": "2.700-6.050", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER", "TRADERS"],
        "narration": "about what to believe and what to keep.",
        "must_show": "the establishing MARKET frame (NON-Jesus, this is the plate the runner promotes) — the bright marketplace, the believer stepping in among the stalls where he must decide what is true and worth keeping.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure, dove or beam; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "An establishing wide of the bright marketplace, camera at eye level set "
            "behind a foreground trader whose back is to the lens, looking across the "
            "stalls, so the figures face into the market and their gazes travel to the "
            "goods and to one another, never to the camera. The believer (muted "
            "olive-green-and-brown wool, not cream) steps in "
            "among the stalls, traders busy at their baskets and the money-changer's low "
            "table with its small hand balance. This is a real place, not a stage: nobody "
            "is lined up facing the lens. Ordinary-sized people on one ground plane; warm "
            "daylight over the square, not around any head; nothing is written anywhere; "
            "no divine figure."
        ),
    },
    {
        "id": "v2-r195-b03", "out": "s03-prove-all-things.jpeg", "seg": "s1",
        "window": "6.050-8.700", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER"],
        "narration": "Prove all things;",
        "must_show": "BLUE caption (SCRIPTURE) — the proving itself: an insert two-shot of the believer's hands weighing a coin against the brass weights on the money-changer's small hand balance, testing whether it is true.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure, dove or beam; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A tight insert in the market daylight over the money-changer's low table: the "
            "believer's careful hands (muted olive-and-brown sleeve, not cream) set a coin "
            "in one pan of the small hand balance against the brass weights in the other, "
            "the beam tipping as he tests whether it is true — proving the thing before he "
            "trusts it. Ordinary daylight on the balance and hands, not a ring of light "
            "anywhere; nothing is written; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b04", "out": "s04-hold-fast-the-good.jpeg", "seg": "s1",
        "window": "8.700-10.660", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER"],
        "narration": "hold fast that which is good.",
        "must_show": "BLUE caption (SCRIPTURE) — holding fast the good: a close on the believer closing his hand firmly around the one true coin (or a good measure of grain), keeping it, having proved it good.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close in the market daylight on the believer (not cream): having proved it, "
            "he closes his hand firmly around the one good, true coin, drawing it in to "
            "keep — holding fast that which is good. His gaze is down on his own closed "
            "hand, settled and sure, not to the camera; warm daylight on his hand and "
            "face, not around his head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b05", "out": "s05-test-everything.jpeg", "seg": "n1",
        "window": "10.660-13.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER", "TRADERS"],
        "narration": "Test everything, he said.",
        "must_show": "the believer testing another thing — turning from the coin to examine a bolt of cloth or a measure of grain a trader offers, checking it carefully before he accepts it.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon; no sneering or contempt.",
        "scene": (
            "A shot in the market daylight: the believer (not cream) takes a bolt of woven "
            "cloth a trader holds out and turns it over in his hands, feeling the weave, "
            "checking it honestly before he accepts it — testing everything, not swallowing "
            "it whole. The trader beside him ordinary-sized, one head each, their gazes on "
            "the cloth between them, not to the camera; warm daylight on them, not around "
            "any head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b06", "out": "s06-held-to-the-light.jpeg", "seg": "n1",
        "window": "13.200-16.570", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER"],
        "narration": "Don't swallow every voice — weigh it, hold it up to the light.",
        "must_show": "holding it up to the daylight — a close of the believer lifting the cloth (or a thin coin) up against the bright open sky to inspect it, ordinary daylight passing through the weave.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure, dove or beam; no supernatural or divine light; no halo, glow or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the believer (not cream) raising the woven cloth up against the "
            "bright open daytime sky, ordinary sunlight passing through the weave as he "
            "inspects it — weighing it, holding it up to the light before he trusts it. "
            "The light is plain daylight from the sky, never a supernatural beam and never "
            "a ring around his head; his eyes are on the cloth against the sky, not to the "
            "camera; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b07", "out": "s07-despise-not-prophesyings.jpeg", "seg": "n1b",
        "window": "16.570-21.700", "wide": True, "jesus": False, "ref": False,
        "locks": ["GATHERING", "PROPHET", "HEARERS", "BELIEVER"],
        "narration": "despise not prophesyings.",
        "must_show": "the GATHERING (NON-Jesus, the plate the runner promotes) — an ordinary human prophet standing to speak God's word to the seated assembly, the believer among the hearers giving him honest attention, not scorn.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure, dove, beam, halo or symbol on or around the prophet — he is a plain man; no mockery or sneering from the hearers; no modern object; nothing written; not a cartoon.",
        "scene": (
            "An establishing wide of the plain meeting room in warm daylight, camera at "
            "the back of the assembly looking toward the standing prophet, so the hearers' "
            "backs and three-quarter faces turn toward him and every gaze travels to him, "
            "never to the camera. The aged prophet (grey-brown wool, not cream) stands, "
            "one open hand raised, speaking God's word plainly; the believer sits among "
            "the seated hearers giving him honest, weighing attention. This is a real "
            "gathering, not a staged line. The prophet is only a man — no divine light on "
            "or around him, no ring or shaft of light, no symbol. Ordinary-sized people on "
            "one floor; warm daylight through the shutters, not around any head; nothing "
            "is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b08", "out": "s08-recognize-the-voice.jpeg", "seg": "n1b",
        "window": "21.700-27.660", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATHERING", "BELIEVER"],
        "narration": "The testing was never for shutting God's voice out — it is how you recognize it.",
        "must_show": "recognition — a close on the believer among the hearers, his face lighting with quiet recognition as he weighs the prophet's words and knows them to be true; testing is how he recognizes the voice, not how he shuts it out.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure, dove or beam; no supernatural light; no halo, glow or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the believer (not cream) seated among the hearers, listening "
            "intently, his face settling into quiet recognition as he weighs the prophet's "
            "words and knows them true — the testing is how he recognizes the voice, not "
            "how he shuts it out. His gaze is toward the unseen speaker off-frame, not to "
            "the camera; warm ordinary daylight on his face, not around his head; nothing "
            "is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b09", "out": "s09-find-the-genuine-good.jpeg", "seg": "n2",
        "window": "27.660-30.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER", "TRADERS"],
        "narration": "And when you find what is genuinely good, cling to it.",
        "must_show": "finding the genuine good — back in the market, the believer's face brightening as he settles on the one truly good thing among the stalls, reaching to take it.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the market daylight: among the many stalls the believer (not cream) "
            "settles on the one truly good thing — a sound measure of grain, a good loaf, "
            "an honest cloth — his face brightening with recognition as he reaches to take "
            "it. Ordinary-sized, one head, gaze on the good thing before him, not to the "
            "camera; warm daylight on him, not around his head; nothing is written "
            "anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b10", "out": "s10-dont-let-it-slip.jpeg", "seg": "n2",
        "window": "30.400-33.140", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER"],
        "narration": "Don't let it slip.",
        "must_show": "not letting it slip — a close on the believer drawing the good thing in against his chest with both hands, holding it securely so it cannot be lost.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the believer (not cream) drawing the good thing in against his "
            "chest with both hands and holding it securely, guarding it so it cannot slip "
            "away — keeping what he has proved good. His gaze is down over what he holds, "
            "settled and resolved, not to the camera; warm daylight on his hands and face, "
            "not around his head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b11", "out": "s11-the-warning.jpeg", "seg": "n3",
        "window": "33.140-38.020", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER"],
        "narration": "He paired it with a warning — the shortest fence he ever built:",
        "must_show": "the warning — the believer pausing at the market's edge, having noticed the narrow dark alley and its shadowed doorway ahead of him, weighing it.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; nothing lurid or violent shown in the doorway (it stays dark and unspecified); no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot at the market's edge in daylight: the believer (not cream) stops on the "
            "bright paving where the square narrows into a dark alley, one shadowed doorway "
            "ahead of him, and he studies it — warned, weighing whether to go near. The "
            "doorway stays dark and unspecified, nothing shown inside it. Ordinary-sized, "
            "one head, gaze toward the shadowed doorway, not to the camera; bright daylight "
            "on him against the shadow, not around his head; nothing is written anywhere; "
            "no divine figure."
        ),
    },
    {
        "id": "v2-r195-b12", "out": "s12-abstain-from-evil.jpeg", "seg": "s2",
        "window": "38.020-42.030", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER"],
        "narration": "Abstain from all appearance of evil.",
        "must_show": "BLUE caption (SCRIPTURE) — abstaining: the believer deliberately turning his back on the shadowed doorway and stepping back into the bright open square, a clean and settled conscience.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; nothing lurid or violent in the doorway (it stays dark and unspecified); no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot at the market's edge in daylight: the believer (not cream) turns his "
            "back on the dark alley doorway and steps deliberately back into the bright "
            "open square, leaving the shadow behind him — abstaining from even the "
            "appearance of evil, his face clean and settled. The doorway stays dark and "
            "unspecified behind him. Ordinary-sized, one head, gaze forward into the "
            "sunlit square, not to the camera; bright daylight ahead of him, not around "
            "his head; nothing is written anywhere; no divine figure."
        ),
    },
    {
        "id": "v2-r195-b13", "out": "s13-a-faith-that-checks.jpeg", "seg": "n4",
        "window": "42.030-45.100", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER"],
        "narration": "The same word fits now: a faith that checks,",
        "must_show": "a faith that checks — the believer back at the balance, calmly and thoughtfully weighing one more thing, unhurried and clear-eyed, not gullible.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A shot in the market daylight: the believer (not cream) stands again at the "
            "money-changer's balance, calmly weighing one more thing with a clear, "
            "thoughtful eye — a faith that checks first, steady and never gullible. "
            "Ordinary-sized, one head, gaze down on the balance, not to the camera; warm "
            "daylight on him, not around his head; nothing is written anywhere; no divine "
            "figure."
        ),
    },
    {
        "id": "v2-r195-b14", "out": "s14-then-commits.jpeg", "seg": "n4",
        "window": "45.100-48.190", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARKET", "BELIEVER", "TRADERS"],
        "narration": "then commits — that's steady, not gullible.",
        "must_show": "the closing image — having checked, the believer commits: he clasps hands on the honest trade / carries the good thing away through the square, resolved and steady; a faith that checks, then commits.",
        "must_not_show": "no Jesus and no one in cream or white; no God, Spirit or divine figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing shot in the sunlit market square: having checked it, the believer "
            "(not cream) commits — clasping hands on the honest trade with the trader, or "
            "carrying the proved-good thing away through the square, resolved and steady. "
            "Ordinary-sized people on one ground plane, one head each, their gazes on the "
            "trade and the way ahead, not to the camera; warm daylight over the square, "
            "not around any head; nothing is written anywhere; no divine figure."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # MARKET is intentionally NOT auto-wired to build-60's frame: that "market" is the
    # gerasene town where the healed man testifies and carries NO money-changer's balance and
    # NO shadowed alley doorway — both of which beats b03 (weigh a coin) and b11/b12 (turn from
    # the doorway) depend on. Runner promotes MARKET from b02 (which establishes the balance
    # table + the alley doorway); GATHERING from b07; PAUL-ROOM from b01 (no Paul row is built
    # yet, so no committed PAUL-ROOM plate exists — the first built Paul row seeds it).
}
# === end PLACE-PLATES ===

# No image REFS: all places and people are carried by the build-local text locks above (PAUL
# and PAUL-ROOM byte-identical to build-184/186/194). Jesus does not appear in this row (every
# beat jesus=False); no one wears cream or white; God / the Holy Spirit / the voice of God is
# never embodied.
REFS = {
}
