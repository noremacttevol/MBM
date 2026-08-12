#!/usr/bin/env python3
"""V2 beat map — row 94, build-94-father-forgive-them (Luke 23:33-34).

COVERAGE: 12 pictures over 66.3 s = 5.5 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 23:33-34 KJV):
  v33   "when they were come to the place, which is called CALVARY,
        there they crucified him, and the malefactors, one on the
        right hand, and the other on the left." — three crosses on a
        bare rise outside the wall.
  v34   "Then said Jesus, FATHER, FORGIVE THEM; FOR THEY KNOW NOT WHAT
        THEY DO. And they PARTED HIS RAIMENT, and CAST LOTS." — the
        prayer is his FIRST word from the cross; the dice game happens
        directly beneath him.

CRUCIFIXION RENDERING LAW (CONTENT-CARE — governs every frame): the
violence itself is OFF-SCREEN. No nails or hammering ever shown or in
progress; no blood, no wounds detailed, no gore anywhere; the crosses
shown RAISED and complete, at distance in wides, and in closes only
from the chest or face up, with dignity absolute. On the cross Jesus
wears a plain undyed cream linen wrap (his robe is the soldiers'
spoil below). The suffering is carried by sky, distance, and his
face — never by anatomy.

TIME OF DAY: a bleak, cold, grey-overcast morning throughout — thin
colorless light (the great darkness of v44 belongs to a later row).

CHANGING CONDITION (kept OUT of the locks): his raiment — worn, then
a folded spoil under the dice; the prayer — rising against the
mockery and the game beneath.
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
    "SOLDIERS": (
        "SOLDIERS LOCK: the Roman execution detail — four soldiers "
        "in dark iron helmets and OXBLOOD-BROWN leather over DARK "
        "TUNICS (never cream, never white); bored, workmanlike, "
        "just following orders — never leering caricatures."
    ),
}

REF = True

# STALE-V1-FINAL fix (AUDIO-FIX 2026-08-06, Machine A): narration mp3s are newer
# than the V1 mp4 (recency gate fails), so the packet-copy AUDIO LOCK would ship
# stale voices. Rebuild from this build's own mp3 segments — $0.
AUDIO_FROM_V1_SEGMENTS = True

# === C-FIX 2026-08-12 (Machine A `Dev`, Opus runner) — Cameron re-opened the
# 08-11 fix: "he needs a crown of thorns when he is on the cross so all of these
# pictures need to be redone … You didnt fix anything try again same compliants."
# AUTOPSY: no Jesus-on-cross beat ever named a crown of thorns (IGNORED) — every
# readable cross frame showed a BARE head, while sibling row 96 was given a
# mandatory crown on 08-11. The prior 08-11 fix only touched b09/b10 smile/eyes/
# plaque, so the crown was never added → "same complaints." FIX = port row 96's
# proven CRUCIFIX_LOOK / CRUCIFIX_REJECT and apply it to every readable Jesus
# frame (b02/b06/b08/b09/b10). Distant wides b11/b12 keep Jesus a speck (crown
# imperceptible) → left untouched (cost law). These strings render AFTER the
# shared JESUS lock in v2_prompt.assemble(), so they override the robe for THIS
# row only. `scene` is prefixed with CRUCIFIX_LOOK; `must_not_show` suffixed with
# CRUCIFIX_REJECT. The prior 08-11 gains (titulus present, eyes open, no smile,
# loincloth) are RE-ASSERTED here so they stay locked while the crown is added.
CRUCIFIX_LOOK = (
    "CRUCIFIXION APPEARANCE — IDENTICAL in every crucifixion frame: on the cross "
    "Jesus is STRIPPED of the cream robe — the soldiers have already cast lots for "
    "his garments (their dice lie on the rock below) — so he wears ONLY a plain, "
    "rough, undyed knee-length cloth loincloth; his torso and arms are bare. He is "
    "NOT in the cream robe, mantle, tunic or shawl here and is never fully clothed "
    "on the cross. On his head is a dark CROWN OF WOVEN THORNS pressed into the "
    "brow — present and clearly visible in this frame. The rough wooden UPRIGHT of "
    "the cross rises directly behind his head and shoulders, and fixed to it just "
    "above his head is a plain weathered wooden TITLE-BOARD (the titulus, Luke "
    "23:38) whose ancient painted lettering is worn and indistinct — an aged "
    "placard, no modern type. His EYES are warm, living and clear — reverent, "
    "lifted to the cold grey sky or lowered in peace; NEVER white, blank, milky or "
    "rolled back, and NEVER looking into the camera lens. His expression is solemn "
    "and heavy with pain, NEVER smiling, grinning or showing bared teeth. His face "
    "and identity remain exactly the attached Jesus reference man. Still NO nails, "
    "blood, wounds or gore anywhere — dignity absolute. "
)
CRUCIFIX_REJECT = (
    " ALSO REJECT: any cream robe, mantle, tunic or shawl on his body; a fully "
    "clothed Jesus on the cross; a MISSING crown of thorns or a bare head; any "
    "smile, grin, cheerful look or bared teeth; white, blank or rolled-back eyes; "
    "his gaze into the camera lens; a bare studio-style portrait with no cross "
    "behind his head; small cross shapes floating in the sky; MORE THAN THREE "
    "crosses anywhere in the frame or a SECOND separate group of crosses on a "
    "background hill or horizon — there are ONLY THREE crosses in the whole scene: "
    "Jesus's cross and the two thieves' crosses beside it, and no others anywhere "
    "behind; any legible modern or Latin-alphabet word on the title-board (it is an "
    "aged placard with worn, indistinct ancient marks, never a readable word); any "
    "nails, blood, wounds or gore."
)


def _crucify(beat):
    """Apply the C-FIX crucifixion look to a readable Jesus beat in place."""
    beat["scene"] = CRUCIFIX_LOOK + beat["scene"]
    beat["must_not_show"] = beat.get("must_not_show", "") + CRUCIFIX_REJECT
    return beat


BEATS = [
    {
        "id": "v2-r094-b01", "out": "s01-and-when-they-were-come.jpeg", "seg": "s33",
        "window": "0.28-9.71", "wide": True, "jesus": False, "ref": False,
        "locks": ["HILL"],
        "narration": (
            "And when they were come to the place, which is called Calvary, "
            "there they crucified him, and the malefactors, one on the right "
            "hand, and the other on the left."
        ),
        "must_show": "SCRIPTURE-EXACT at merciful distance — the bare rise under the cold grey sky with the THREE raised crosses in far silhouette, the centre one between the two; watchers small on the slope.",
        "must_not_show": "ABSOLUTE: no nails, hammering, blood or wounds — the crosses already raised, seen far off; the distance itself the mercy.",
        "scene": (
            "From down the slope, the camera behind the scattered "
            "watchers' backs, the place "
            "called The Skull holds its "
            "terrible geometry against the "
            "cold grey sky: three raised "
            "crosses far off on the bare "
            "rock crown — the centre one "
            "between the other two, exactly "
            "as the sentence says — small "
            "knots of watchers held back on "
            "the scrub slope, the city wall "
            "low and distant behind, and "
            "over everything the thin "
            "colorless morning light of the "
            "worst day the world ever "
            "survived. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r094-b02", "out": "s02-every-right-to-call-down.jpeg", "seg": "n1",
        "window": "21.45-24.22", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "Every right to call down judgment.",
        "must_show": "the withheld right — close on Jesus's face on the cross, chest-up, grey sky behind: pain endured with dignity, and NO anger anywhere in the features.",
        "must_not_show": "ABSOLUTE: no blood or wounds in frame — face and shoulders only; the suffering in the drawn features, never the anatomy.",
        "scene": (
            "Close on the face that holds "
            "every right in the universe "
            "and uses none of it: chest-up "
            "against the cold grey sky, "
            "the features drawn deep with "
            "what the body is bearing, "
            "breath coming hard — and in "
            "the warm brown eyes, searched "
            "from corner to corner, not "
            "one spark of the judgment he "
            "could call down with a word "
            "— power held perfectly still "
            "at the exact moment it has "
            "the most reason to move. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r094-b03", "out": "s03-they-brought-him-to-a.jpeg", "seg": "n0",
        "window": "11.20-19.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "SOLDIERS"],
        "narration": (
            "They brought him to a place called Calvary, and there they "
            "crucified him — between two criminals, at the hands of soldiers "
            "just following orders."
        ),
        "must_show": "the scene established — mid-distance: the three raised crosses on the crown, the soldier detail at their duties below on the rock; ordinary men at a terrible routine.",
        "must_not_show": "ABSOLUTE: no nails, hammers, blood or wounds — the work already done, the detail at its aftermath duties only.",
        "scene": (
            "Mid-slope the frame takes in "
            "the working summit: the three "
            "crosses standing dark against "
            "the overcast, and beneath "
            "them the execution detail at "
            "its routine — one soldier "
            "planting the squad's spears "
            "point-down, another sorting "
            "the prisoners' effects into "
            "a pile, a third simply "
            "standing his watch with his "
            "back to everything — ordinary "
            "men moving through a terrible "
            "morning's checklist, orders "
            "doing their thinking for "
            "them. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r094-b04", "out": "s04-he-had-every-reason-to.jpeg", "seg": "n1",
        "window": "19.67-21.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["HILL", "SOLDIERS"],
        "narration": "He had every reason to curse them.",
        "must_show": "the reasons — the soldiers beneath the centre cross seen from above-behind its beam line: the men with every curse coming to them, going about their work unbothered.",
        "must_not_show": "ABSOLUTE: no wounds or violence; the soldiers ORDINARY — the point is their obliviousness, not menace.",
        "scene": (
            "From high behind the centre "
            "beam's line the frame looks "
            "down on the reasons: four "
            "helmeted men moving about "
            "their business on the rock "
            "below — trading a joke by "
            "the spear-stack, passing a "
            "waterskin, one yawning into "
            "the cold — every curse in "
            "the language coming to them "
            "by every law of earth, and "
            "not one of them feeling the "
            "weight of the gaze from "
            "above, or knowing whose it "
            "is. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r094-b05", "out": "s05-and-they-parted-his-raiment.jpeg", "seg": "s34b",
        "window": "24.68-27.52", "wide": False, "jesus": False, "ref": False,
        "locks": ["SOLDIERS"],
        "narration": "And they parted his raiment, and cast lots.",
        "must_show": "SCRIPTURE-EXACT: the parting — close on the soldiers' hands over the folded cream robe: the garment divided, the knucklebone dice coming out.",
        "must_not_show": "ABSOLUTE: no blood on the garment or anywhere; the robe folded and whole — plunder, not evidence.",
        "scene": (
            "Close on the morning's small "
            "plunder: the plain cream robe "
            "folded on the rock between "
            "four kneeling soldiers, dark "
            "hands already parting the "
            "lesser garments into shares — "
            "and over the one good piece, "
            "too fine to tear, the "
            "knucklebone dice coming out "
            "of a belt pouch — a dead "
            "man's clothes on the table "
            "and the game beginning, "
            "business as usual at the "
            "bottom of the cross. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r094-b06", "out": "s06-while-he-hung-there-the.jpeg", "seg": "n2b",
        "window": "29.05-35.63", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILL", "SOLDIERS"],
        "narration": (
            "While he hung there, the soldiers divided up his clothes and "
            "threw dice for them, right at the foot of the cross."
        ),
        "must_show": "SCRIPTURE-EXACT: the geometry of it — the wide frame: the dice game in progress at the cross's very foot, and above the players the crucified Jesus, chest-up and distant-dignified against the grey.",
        "must_not_show": "ABSOLUTE: no wounds or blood; Jesus rendered from chest up at the frame's top, the game below — the vertical distance the picture's meaning.",
        "scene": (
            "One vertical frame holds, the camera at the hill's "
            "side so cross-foot and dice game read in profile, the "
            "whole obscene arrangement: at "
            "its bottom the four soldiers "
            "hunched over their dice game "
            "on the rock, a toss going up, "
            "a shoulder shoved in mock "
            "outrage, the folded cream "
            "robe as the pot — and above "
            "their bent helmets, high "
            "against the cold grey sky, "
            "the man himself, chest and "
            "face in the thin light, "
            "watching heaven while they "
            "play for his clothes at his "
            "feet. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r094-b07", "out": "s07-that-is-what-was-going.jpeg", "seg": "n2b",
        "window": "35.63-38.29", "wide": False, "jesus": False, "ref": False,
        "locks": ["SOLDIERS"],
        "narration": "That is what was going on underneath him.",
        "must_show": "the game close — the dice mid-tumble on the rock, the reaching hands, a laugh caught on one face; callousness at its most casual.",
        "must_not_show": "ABSOLUTE: no blood anywhere; the callousness CASUAL, not cruel-theatrical — men numb to the day, which is worse. NO cross, cross-beam or timber leaning, tilting, tipping or falling toward the men; NO X-shaped crossing beams above their heads and NO jumble of angled crosses in the frame — the crosses stand UPRIGHT and vertical; at most the plain vertical foot of a single upright rises quietly at the edge or back of the frame, never overhead and never toppling. NO bright sunshine, warm golden daylight or blue sunny sky; NO village, houses, courtyard, stone buildings or town walls close behind the men — the light is the same cold colorless grey overcast as the rest of the hill and the ground is bare pale execution rock.",
        "scene": (
            "Close and low on the rock floor "
            "beneath the cross: the "
            "knucklebones mid-tumble "
            "between the kneeling men, one "
            "soldier's hand already "
            "reaching, another's head back "
            "in an easy laugh at the "
            "throw — the small ordinary "
            "sounds of a game men have "
            "played a thousand slow "
            "afternoons, played this once "
            "at the foot of the cross, out on "
            "the bare pale rock of the "
            "execution hill under the same "
            "cold, colorless grey-overcast "
            "morning light as every other "
            "frame — no sunshine, no village, "
            "no buildings behind them, only "
            "open grey ground and heavy sky. "
            "The "
            "only cross timber in view is "
            "the plain VERTICAL foot of the "
            "upright standing quietly at the "
            "back edge of the frame — nothing "
            "overhead, nothing tilted, nothing "
            "leaning or falling toward them; "
            "the beam is steady and straight. "
            "Not one face lifts to "
            "see whose foot it is. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r094-b08", "out": "s08-and-instead-of-a-curse.jpeg", "seg": "n2",
        "window": "38.89-45.48", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": (
            "And instead of a curse, the first words out of his mouth on the "
            "cross were a prayer — for the very people driving the nails."
        ),
        "must_show": "the prayer forming — close on Jesus's face, chest-up against the grey: lips beginning to move, eyes lifted; the first words gathering, and they are FOR them.",
        "must_not_show": "ABSOLUTE: no nails, wounds or blood in frame — face and sky only; the prayer's direction upward, its subject below.",
        "scene": (
            "Close against the cold sky "
            "the first words of the cross "
            "gather: the drawn face "
            "lifting, the cracked lips "
            "beginning to move — and any "
            "watcher bracing for the "
            "curse earned a hundred times "
            "over this morning would "
            "watch the mouth shape "
            "something else entirely: a "
            "prayer, aimed upward, "
            "spent downward — on the "
            "dice-players, the "
            "order-followers, the whole "
            "oblivious apparatus beneath "
            "his feet. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r094-b09", "out": "s09-father-forgive-them-for-they.jpeg", "seg": "j1",
        "window": "46.09-48.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL", "SOLDIERS"],
        "narration": "Father, forgive them; for they know not what they do.",
        "must_show": "SCRIPTURE-EXACT: the prayer itself — the hill under the words: at the top of the centre cross the lifted face, his eyes open and calm and turned upward to heaven in solemn pain, and FIXED TO THE VERY TOP OF THE UPRIGHT BEAM DIRECTLY ABOVE HIS HEAD a small weathered wooden placard (the written charge over him), its worn lettering indistinct; the unknowing soldiers at their game below, watchers on the slope; mercy covering the whole frame.",
        "must_not_show": "ABSOLUTE: no wounds or blood; NO SMILE and no bared teeth — the face solemn and sorrowful, never cheerful; his eyes natural and lifted, never rolled back and never showing only the whites; the placard PRESENT above his head, never a bare cross-top; the composition HOLDS everyone the prayer covers — executioners, gamblers, watchers.",
        "scene": (
            "The prayer goes up over "
            "everyone it covers: the "
            "grey hill with the lifted "
            "face at the top of the "
            "centre cross, his eyes open "
            "and calm and turned upward "
            "to heaven, the expression "
            "solemn and heavy with pain "
            "and never smiling — and "
            "fixed to the very top of the "
            "upright beam directly above "
            "his head a small weathered "
            "wooden placard bearing the "
            "written charge, its lettering "
            "worn almost away — FATHER, "
            "FORGIVE THEM — and below "
            "and around it every unknowing "
            "head the words are spent on: "
            "the soldiers over their "
            "dice, the watch leaning on "
            "his spear, the far knots of "
            "watchers on the slope — THEY "
            "KNOW NOT WHAT THEY DO — "
            "mercy thrown wide as the "
            "sky over a hill that has no "
            "idea it is being prayed "
            "for. Every figure has two "
            "arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r094-b10", "out": "s10-not-forgive-them-later-if.jpeg", "seg": "n3",
        "window": "50.41-55.80", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": (
            "Not, forgive them later, if they're sorry. Forgive them now — "
            "while it's still happening."
        ),
        "must_show": "the NOW — the praying face lifted, solemn and heavy with pain, the lips parted in prayer (NOT a smile), and a small weathered placard fixed to the top of the upright beam directly above his head; the game's motion visible far below at frame's bottom edge: forgiveness and offense simultaneous in one image.",
        "must_not_show": "ABSOLUTE: no wounds or blood; NO SMILE, no grin, no bared teeth and no cheerful expression — the face solemn and sorrowful; he is stripped to a plain loincloth on the cross and is NOT wearing a full robe; the placard PRESENT above his head; the simultaneity the point — the prayer DURING, not after.",
        "scene": (
            "One frame holds the tense of "
            "the miracle: at its top the "
            "praying face against the "
            "grey, lifted and solemn and "
            "heavy with pain, the lips "
            "still moving with the words "
            "but never smiling — his body "
            "stripped to a plain loincloth "
            "on the cross, and directly "
            "above his head a small "
            "weathered wooden placard "
            "fixed to the top of the "
            "beam, its lettering worn "
            "away — and at its "
            "bottom edge, small and "
            "in-focus, the dice still "
            "tumbling, the shares still "
            "being divided, the offense "
            "still in full progress — "
            "forgiveness issued not after "
            "the wound and not upon "
            "apology, but DURING: mercy "
            "running ahead of repentance "
            "with the crime still warm. "
            "Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r094-b11", "out": "s11-that-is-how-far-his.jpeg", "seg": "n4a",
        "window": "56.38-61.49", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HILL", "SOLDIERS"],
        "narration": (
            "That is how far his mercy reaches. If it covered the ones "
            "killing him,"
        ),
        "must_show": "the reach measured — the whole hill wide beneath the centre cross: every figure on it, nearest executioner to farthest watcher, inside the one prayer's span.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the wide INCLUSIVE — nobody on the hill outside the frame's embrace.",
        "scene": (
            "The wide frame measures, the camera far off taking "
            "the whole hill from the side, the "
            "reach: from the centre cross "
            "the hill falls away in every "
            "direction — the soldiers at "
            "its foot, the watch at his "
            "spear, the huddled watchers "
            "down the scrub slope, the "
            "distant wall with its distant "
            "city — and every soul in the "
            "cold grey picture stands "
            "inside the span of the words "
            "just spoken over them, the "
            "nearest hands that did the "
            "work included first — mercy "
            "with a radius that starts at "
            "the hammer. Every figure has "
            "two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r094-b12", "out": "s12-there-is-no-one-and.jpeg", "seg": "n4b",
        "window": "62.16-65.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HILL"],
        "narration": "there is no one, and nothing you've done, it can't cover.",
        "must_show": "the closing image — the centre cross against the vast grey sky, the hill's figures small below; the prayer's cover extended past the frame toward the viewer.",
        "must_not_show": "ABSOLUTE: no wounds or blood; the composition OPEN at its foreground edge — room in the mercy for whoever is looking.",
        "scene": (
            "The closing frame opens the "
            "circle outward: the centre "
            "cross high and steady against "
            "the vast cold sky, the hill's "
            "small figures scattered "
            "below it — and at the "
            "picture's near edge, empty "
            "ground: bare grey rock in "
            "the foreground with room on "
            "it, deliberately unfilled — "
            "space held open inside the "
            "prayer's reach for the one "
            "person every telling of this "
            "story is aimed at: whoever "
            "is looking at it. Every "
            "figure has two arms, two "
            "hands and one head."
        ),
    },
]


# C-FIX 2026-08-12: enforce the ONE crucifixion depiction (crown of thorns +
# loincloth + titulus + open reverent eyes + no smile) on every READABLE Jesus
# beat. The distant establishing wides b11/b12 keep Jesus a speck, so a crown is
# imperceptible and they are left untouched (cost law). b01/b03/b04/b05/b07 have
# no on-cross Jesus face and are unaffected.
_CRUCIFY_IDS = {
    "v2-r094-b02", "v2-r094-b06", "v2-r094-b08", "v2-r094-b09", "v2-r094-b10",
}
for _b in BEATS:
    if _b["id"] in _CRUCIFY_IDS:
        _crucify(_b)


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "HILL": "PLACE-REF/hill.jpeg",  # build-94-father-forgive-them s01-and-when-they-were-come (manual)
    "SOLDIERS": "PLACE-REF/soldiers.jpeg",  # build-15-centurion v2-r015-b01b (manual)
}
# === end PLACE-PLATES ===
