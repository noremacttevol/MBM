#!/usr/bin/env python3
"""V2 beat map — row 61, build-61-syrophoenician-woman (Mark 7:24-30).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 31 pictures over 178.4 s narration = 5.8 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 7:24-30 KJV):
  v24  he went into the BORDERS OF TYRE AND SIDON — Gentile coast; entered
       into AN HOUSE, and WOULD HAVE NO MAN KNOW IT: but HE COULD NOT BE
       HID.
  v25  a certain woman, whose YOUNG DAUGHTER had an unclean spirit, HEARD
       OF HIM, and came and FELL AT HIS FEET.
  v26  the woman was a GREEK, a SYROPHENICIAN BY NATION; she BESOUGHT him
       that he would cast forth the devil out of her daughter.
  v27  "Let the children first be filled: for it is not meet to take the
       children's bread, and to cast it unto the dogs." (j1) — the Greek
       word is kunaria: the little HOUSE-PUPS under a family's own table,
       not street curs; he paints a household with a place in it.
  v28  "Yes, Lord: yet the dogs under the table eat of the children's
       crumbs." (w28) — she answers INSIDE his picture; the only exchange
       in the gospels anyone wins.
  v29  "For this saying go thy way; the devil is gone out of thy
       daughter." (j2) — healed across distance, on the word alone; no
       visit, no touch.
  v30  she came to her house and found the devil GONE OUT, and her
       daughter LAID UPON THE BED — resting, quiet, whole.

CONTENT-CARE — FLAG A BY STORY-KIND (a devil cast out of a child): the
adversary NEVER gets any visible form; the girl's affliction shows ONLY in
her worn condition (b07 — restless, exhausted, gripping the blanket; never
convulsing, never horror), and the deliverance shows ONLY as rest and
wholeness (b28+). Nothing visible leaves her; no deliverance moment is
depicted at all — the text itself heals her off-stage.

TIME-OF-DAY ARC: arrival and hiding in late afternoon; the woman's hearing
and resolve toward evening; the house exchange by warm lamplight that same
evening; her walk home in early night under a clear moon; the homecoming
and the whole-daughter beats in the same night's lamplight; the closing
loaf in next-day morning light.

CAST-REF NOTE: when the first still with the woman's face is ACCEPTED at
QC, copy it to CAST-REF-V2/syro-woman-ref.jpeg and add
"char_refs": ["CAST-REF-V2/syro-woman-ref.jpeg"] to every later
legible-face beat — the build rides on her face. Same for the daughter
(syro-girl-ref.jpeg: b07, b28-b31). Text locks alone do not hold a face.
"""

LOCKS = {
    "WOMAN": (
        "WOMAN LOCK: the mother is the same woman in every shot — a Greek "
        "Syrophoenician of about thirty-five, olive-gold Phoenician skin, "
        "strong clear features, dark eyes quick with intelligence, black "
        "hair dressed back under a DEEP SEA-BLUE head scarf edged with a "
        "dark violet band. She wears a DEEP SEA-BLUE wool dress with a "
        "DARK VIOLET-PURPLE bordered mantle in the Phoenician manner and "
        "small bronze earrings — plainly a Gentile woman of Tyre, plainly "
        "darker than any sunlit wall, never cream, never white. Her face "
        "is shown clearly."
    ),
    # Her condition changes at v29-30; the lock fixes face and build only.
    "GIRL": (
        "DAUGHTER LOCK: the little girl is the same child in every shot — "
        "about seven, small, her mother's olive-gold skin and black hair "
        "in loose curls, fine dark brows. She wears a small DARK "
        "MADDER-ROSE wool shift and lies under a DARK TEAL-BLUE blanket; "
        "nothing on or around her is cream, off-white or any pale "
        "near-white cloth. Her face is shown clearly. Her affliction is "
        "shown only as exhaustion and restlessness — she is never made "
        "frightening or pitiful past what a mother could bear to see."
    ),
    "TYRE": (
        "TYRE LOCK: the borders of Tyre — a Phoenician coastal town of "
        "close-set stone houses on a headland over a bright hard-blue "
        "sea, purple-dyed cloth drying on lines, cedar beams, steep "
        "stepped lanes. Its people wear SATURATED DEEP Mediterranean "
        "colours — deep sea-blue, dark violet-purple, dark teal, deep "
        "russet and dark umber wool — every garment plainly darker than "
        "the sunlit limestone; no one wears cream, off-white, ivory or "
        "any pale near-white cloth."
    ),
    "HOUSE": (
        "BORROWED HOUSE LOCK: the house where Jesus stays — a plain "
        "Phoenician stone house: one main room with a low wooden dining "
        "table, floor cushions in deep teal and umber, a clay oil lamp "
        "on a stand, a heavy plank door onto the stepped lane, one small "
        "window toward the sea. Nothing in the room is cream, off-white "
        "or any pale near-white cloth."
    ),
    "HERHOME": (
        "HER HOME LOCK: the woman's own small house higher in the town — "
        "a single warm room with the child's low bed against the wall, "
        "a small hearth, herbs hung from a beam, a low table with two "
        "stools; poor, clean and loved. Nothing in it is cream, "
        "off-white or any pale near-white cloth."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r061-b01", "out": "s01-north-to-the-coast.jpeg", "seg": "n0 p1-p2",
        "window": "0.28-7.46", "wide": True, "jesus": True, "ref": REF,
        "locks": ["TYRE"],
        "narration": ("Jesus went north — out of Jewish land entirely, up "
                      "to the coast around Tyre. Gentile country."),
        "must_show": "v24 — the arrival: Jesus on the coast road above the hard-blue sea, the Phoenician town on its headland ahead.",
        "must_not_show": "no crowd with him — he travels quiet; the foreign coast does the announcing.",
        "scene": (
            "The camera off the road's seaward side takes the walk in "
            "profile: Jesus walks the high coast road in late-afternoon light, "
            "travel-dusty and alone but for two disciples a few paces "
            "behind — and ahead of him the Phoenician town stacks down "
            "its headland to a hard-blue sea, lines of purple-dyed "
            "cloth drying between the stone houses, a coast no "
            "Galilean rabbi's sandals were expected on. An upright "
            "vertical photograph, the ground at the bottom of the "
            "frame and the sky at the top, the horizon level — the "
            "picture is the right way up. Every figure has two arms, "
            "two legs and one head."
        ),
    },
    {
        "id": "v2-r061-b02", "out": "s02-he-wanted-no-one-to-know.jpeg", "seg": "n0 p3",
        "window": "7.46-10.59", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TYRE", "HOUSE"],
        "narration": ("He slipped into a house and wanted no one to know "
                      "he was there."),
        "must_show": "the hiding — Jesus stepping in at the plank door of the plain house, quiet, the lane behind him empty.",
        "must_not_show": "the seeking of rest must read — a tired man closing a door on the world.",
        "scene": (
            "In the steep stepped lane at dusk Jesus ducks in under "
            "the low lintel of the plain stone house, one hand on the "
            "heavy plank door, glancing once back down the empty lane "
            "before drawing it to — the unmistakable body language of "
            "a man hoping, this once, to be nobody — while the first "
            "lamplight warms the crack of the closing door. Exactly "
            "one person is in the frame, with two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r061-b03", "out": "s03-he-could-not-be-hidden.jpeg", "seg": "n0 p4-p5",
        "window": "10.59-18.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["TYRE"],
        "narration": ("But Mark says it plainly: he could not be hidden. "
                      "Word about him had crossed the border long before "
                      "he did."),
        "must_show": "the word travelling — neighbours' heads together in the lane, eyes toward the house door; the secret already public.",
        "must_not_show": "Jesus is NOT in this frame — his absence and the pointed glances tell it.",
        "scene": (
            "In the blue evening lane the word is already moving: two "
            "women with water jars have stopped with their heads "
            "together, one nodding toward the plank door down the "
            "steps; a fish-seller leans from his doorway to a "
            "neighbour with his hand cupped at his mouth; a boy runs "
            "past them all carrying the news somewhere else — a "
            "secret dying in real time in a small town. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b04", "out": "s04-one-woman-heard.jpeg", "seg": "n1 p1",
        "window": "18.39-19.53", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TYRE"],
        "narration": "And one woman heard it.",
        "must_show": "the hearing — close on her face in the market lane as the name reaches her; everything in her stopping.",
        "must_not_show": "the news lands like a rope thrown to a drowning woman — hope with teeth in it.",
        "scene": (
            "Close on the woman at a market stall in the last light: "
            "she has stopped dead in the middle of paying for a "
            "measure of barley, coins forgotten in her open palm, her "
            "quick dark eyes fixed sideways on the two whispering "
            "neighbours from whom one name has just crossed the lane "
            "to her — hope hitting an exhausted face like weather. "
            "Exactly one person is in the frame in focus, with one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b05", "out": "s05-not-one-of-us.jpeg", "seg": "n1 p2",
        "window": "19.53-26.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TYRE"],
        "narration": ("A Greek, born in that country — a Syrophoenician, "
                      "which is Mark's way of saying: not one of us."),
        "must_show": "who she is — the Phoenician woman whole in her own town: the dress, the sea, the foreignness that is home to her.",
        "must_not_show": "she is dignified IN her difference — the frame honours the very identity the label dismisses.",
        "scene": (
            "The woman stands in the stepped lane with her barley "
            "basket on her hip, upright and self-possessed — the deep "
            "sea-blue dress and violet-bordered mantle of Tyre, the "
            "bronze earrings, the headland sea bright behind the "
            "rooftops below her — a Greek woman of Phoenicia at home "
            "in every stone of the frame, and a foreigner to the one "
            "door she needs. Exactly one person is in the frame, with "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b06", "out": "s06-no-claim-at-all.jpeg", "seg": "n1 p3",
        "window": "26.01-31.08", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TYRE"],
        "narration": ("Wrong nation, wrong religion, no claim at all on a "
                      "Jewish rabbi."),
        "must_show": "the invisible wall — her stopped at the head of the lane that leads down to the house, the distance she has no right to cross.",
        "must_not_show": "the barrier is social, not physical — an empty lane she cannot walk down, yet.",
        "scene": (
            "At the head of the stepped lane, the camera behind her "
            "shoulder so the whole distance falls away in frame, "
            "the woman stands looking "
            "down its empty length toward the plank door of the house "
            "at the bottom — nothing between her and it but forty "
            "paces of worn stone and every rule of two nations — her "
            "basket gripped in both hands, her jaw working, a woman "
            "measuring a wall no one can see. Evening light down the "
            "steps. Exactly one person is in the frame, with two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b07", "out": "s07-her-little-girl.jpeg", "seg": "n1 p4",
        "window": "31.08-35.25", "wide": False, "jesus": False, "ref": False,
        "locks": ["GIRL", "HERHOME"],
        "narration": ("But her little girl was sick with something dark "
                      "that no one could fix."),
        "must_show": "the reason — the small daughter worn and restless on her bed; the affliction as exhaustion, not spectacle.",
        "must_not_show": "FLAG A: nothing visible torments her — a small girl turned to the wall, gripping her blanket, worn hollow; bearable and heartbreaking.",
        "scene": (
            "In the small lamplit room the little girl lies curled "
            "tight on her low bed, turned in toward the wall, her "
            "small fists knotted in the dark teal blanket and her "
            "black curls damp against her temple — not asleep, only "
            "worn out from whatever the nights here are — while the "
            "hearth's low light moves on the wall above her and the "
            "hung herbs of remedies already tried. Exactly one person "
            "is in the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b08", "out": "s08-a-mother-and-a-border.jpeg", "seg": "n1 p5",
        "window": "35.25-39.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "HERHOME"],
        "narration": ("And a mother with a sick child does not care about "
                      "borders."),
        "must_show": "the decision — her pulling the mantle over her head at her own door, jaw set, going.",
        "must_not_show": "no tears here — resolve; the face of a woman who has finished weighing.",
        "scene": (
            "At her own doorway the woman pulls the violet-bordered "
            "mantle up over her head with both hands, her face set "
            "hard and clear under it — one last glance back at the "
            "small bed in the lamplight behind her — and her body "
            "already turned to the dark stepped lane outside, a "
            "mother finished with borders. Exactly one person is in "
            "the frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b09", "out": "s09-she-found-the-house.jpeg", "seg": "n2 p1",
        "window": "39.88-40.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TYRE", "HOUSE"],
        "narration": "She found the house.",
        "must_show": "the arrival — her at the plank door, hand already pushing it, past asking.",
        "must_not_show": "no knock — v25's momentum: she goes IN.",
        "scene": (
            "The woman stands at the plank door in the lamplit lane "
            "with her palm flat against it and it already giving "
            "inward — no knock, no pause, the light from inside "
            "cracking across her set face — a mother arriving at the "
            "one door in the world with her whole life on the other "
            "side of it. Exactly one person is in the frame, with two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b10", "out": "s10-she-fell-at-his-feet.jpeg", "seg": "n2 p2",
        "window": "40.99-47.38", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "HOUSE"],
        "narration": ("She came in uninvited, fell down at his feet, and "
                      "begged him — cast this thing out of my daughter."),
        "must_show": "v25-26 — the fall: the Gentile woman down at Jesus's feet on the floor of the borrowed room, begging; the room caught mid-shock.",
        "must_not_show": "no halo/glow; Jesus looks down at her with attention, not surprise.",
        "scene": (
            "In the lamplit room the woman has thrown herself down at "
            "Jesus's feet where he sits by the low table — her mantle "
            "spilled forward on the floorboards, her hands gripping "
            "toward his ankles, the begging already pouring out of "
            "her — while the household's startled faces hang "
            "half-risen around the lamp and Jesus looks down at her "
            "with full unhurried attention. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b11", "out": "s11-she-asked-anyway.jpeg", "seg": "n2 p3-p4",
        "window": "47.38-53.49", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "HOUSE"],
        "narration": ("Every social rule in the room said she had no "
                      "right to ask. She asked anyway."),
        "must_show": "the room's rules made visible — disapproval on the bystanders' faces ringing the kneeling woman; and her asking through it.",
        "must_not_show": "the disapproval is real but ordinary — propriety offended, not cruelty; she simply outweighs it.",
        "scene": (
            "Around the kneeling foreign woman the room's propriety "
            "stiffens: the householder half-risen with a hand out as "
            "if to usher her back, a disciple's face gone tight at "
            "the intrusion, another looking to Jesus for the "
            "signal to remove her — and in the middle of all that "
            "offended order she stays down and keeps asking, her "
            "face lifted only to the one face that has not hardened. "
            "Lamplight. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b12", "out": "s12-the-pause.jpeg", "seg": "n3",
        "window": "53.49-58.75", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": ("What Jesus said next sounds harsh — until you hear "
                      "it the way she heard it."),
        "must_show": "the held moment before the hard saying — Jesus regarding her; something deliberate assembling behind his eyes.",
        "must_not_show": "no coldness — the look of a teacher choosing a test he believes the student will pass.",
        "scene": (
            "A close two-shot across the lamplight: the woman's "
            "lifted, waiting face — and Jesus regarding her steadily "
            "before he speaks, his head very slightly tilted, "
            "something deliberate and measuring and not unkind "
            "assembling behind his warm eyes: the look of a man "
            "about to hand someone a locked door with the key "
            "plainly in it. Exactly two people are in the frame; "
            "each has one head."
        ),
    },
    {
        "id": "v2-r061-b13", "out": "s13-the-childrens-bread.jpeg", "seg": "j1",
        "window": "58.75-67.31", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "HOUSE"],
        "narration": ("Let the children first be filled: for it is not "
                      "meet to take the children's bread, and to cast it "
                      "unto the dogs. (Mark 7:27)"),
        "must_show": "the saying with its furniture — Jesus speaking beside the low table with bread on it; the household image physically present in the room.",
        "must_not_show": "his gesture indicates the TABLE, not the door — the picture he paints is domestic, and the frame must be too.",
        "scene": (
            "Jesus speaks with one open hand turned toward the low "
            "wooden table beside him — flat bread and a dish sitting "
            "plainly on it in the lamplight — building the household "
            "picture in the air between himself and the kneeling "
            "woman, whose eyes have followed his hand to the bread "
            "and gone very still, listening the way the drowning "
            "listen. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b14", "out": "s14-israel-first.jpeg", "seg": "n4 p1-p2",
        "window": "67.31-75.39", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Here is the why. Let the children be fed first — "
                      "that was his mission order: Israel first, then the "
                      "whole world."),
        "must_show": "close on Jesus mid-saying — gravity without coldness; an order of operations, not a rejection.",
        "must_not_show": "nothing dismissive in the face — the 'first' must read as sequence, with 'then' already alive in it.",
        "scene": (
            "Close on Jesus's face in the lamplight as the hard "
            "sentence stands in the room: grave, steady, entirely "
            "without contempt — the face of a man stating his "
            "marching orders, not his heart's limits — and in the "
            "warm eyes, unhidden from anyone looking as closely as "
            "the woman is, something that waits and wants to be "
            "found. Exactly one person is in the frame, with one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b15", "out": "s15-the-house-pups.jpeg", "seg": "n4 p3-p4",
        "window": "75.39-82.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": ("And the word he chose was not the word for street "
                      "dogs. It was the word for the little pups a family "
                      "keeps under its own table."),
        "must_show": "the picture he painted, literally — under the low table: two small house-pups waiting on the floor by the family's feet, inside the lamplight.",
        "must_not_show": "INSIDE the household warmth — well-fed little pups under a family table, nothing mangy or shut out.",
        "scene": (
            "Low at floor level, under the edge of the low wooden "
            "table in the warm lamplight: two small sleek house-pups "
            "sit on the floorboards among the family's cushions, "
            "ears up, eyes on the table's edge above them with the "
            "patient certainty of pups who have never once been "
            "forgotten at supper — inside the room, inside the "
            "lamplight, inside the household. A crumb already lies "
            "between the front paws of the nearest one."
        ),
    },
    {
        "id": "v2-r061-b16", "out": "s16-a-place-left-in-it.jpeg", "seg": "n4 p5-p6",
        "window": "82.64-89.90", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": ("He had not slammed a door. He had painted a "
                      "picture of a household — and left her a place in "
                      "it, if she could see it."),
        "must_show": "the offered door — the two faces: his steady over the finished saying, hers working at the picture, hunting the gap he left.",
        "must_not_show": "the frame is a riddle mid-solve — her eyes narrowed in thought, not wounded.",
        "scene": (
            "The two faces across the lamplight, close: Jesus "
            "holding the finished saying between them with perfect "
            "stillness, giving her nothing more — and the woman's "
            "face not crumpling but WORKING, her quick dark eyes "
            "moving as if around the inside of the picture he "
            "painted, testing its walls, hunting the place in it "
            "that she can already half-feel was left for her. "
            "Exactly two people are in the frame; each has one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b17", "out": "s17-she-saw-it-instantly.jpeg", "seg": "n4 p7",
        "window": "89.90-92.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "She saw it instantly.",
        "must_show": "the flash — close on her face at the instant the door in the riddle opens: eyes lighting, breath caught.",
        "must_not_show": "joy with wit in it — the look of a mind striking flint, not just a heart hoping.",
        "scene": (
            "Very close on the woman's face at the instant of "
            "seeing it: her eyes flare wide and bright, her chin "
            "lifts half an inch, the breath catches visibly at her "
            "lips — hope and intelligence striking together like "
            "flint and steel — a mother who has just found the "
            "unlocked gate in the middle of the wall. Exactly one "
            "person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r061-b18", "out": "s18-she-stepped-into-the-picture.jpeg", "seg": "n5",
        "window": "92.88-98.54", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "HOUSE"],
        "narration": ("She did not argue with him. She stepped right into "
                      "the picture he had painted, and answered him:"),
        "must_show": "the posture change — up off her face, kneeling upright now, composed, meeting his eyes as an interlocutor.",
        "must_not_show": "begging has become answering — spine, chin and hands must all say it.",
        "scene": (
            "The woman has come up from the floor onto her knees, "
            "spine straight, the mantle fallen back from her face, "
            "her hands folded quiet in her lap — no longer a "
            "supplicant clutching at feet but a woman kneeling "
            "upright in the lamplight meeting Jesus eye to level "
            "eye, composed, about to answer a rabbi inside his own "
            "parable while the room holds its breath. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b19", "out": "s19-yet-the-dogs-eat-the-crumbs.jpeg", "seg": "w28",
        "window": "98.54-104.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("Yes, Lord: yet the dogs under the table eat of the "
                      "children's crumbs. (Mark 7:28)"),
        "must_show": "the answer itself — her face mid-sentence: steady, bright, respectful and unbeatable all at once.",
        "must_not_show": "no defiance — she concedes the whole order and wins inside it; the tone lives in her face.",
        "scene": (
            "Close on the woman's face as the answer leaves her: "
            "steady dark eyes holding their aim, the ghost of "
            "something almost like a smile at one corner of her "
            "mouth, every word placed like a stone in an arch — "
            "yielding the children their table and claiming the "
            "floor beneath it in the same breath — the face of "
            "faith doing theology at speed. Exactly one person is "
            "in the frame, with one head."
        ),
    },
    {
        "id": "v2-r061-b20", "out": "s20-food-under-the-table-too.jpeg", "seg": "n5b p1-p2",
        "window": "104.02-108.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "HOUSE"],
        "narration": ("She did not ask him to change the order. She just "
                      "pointed out that there is food under a table too."),
        "must_show": "the point landed — her open hand turned low toward the table's under-space; Jesus's face beginning to give way to gladness.",
        "must_not_show": "the first crack of his delight must be visible — the loss is already becoming a joy.",
        "scene": (
            "The woman's open hand has turned palm-up, low, toward "
            "the shadowed space beneath the bread-laden table where "
            "the little pups wait — the whole argument in one small "
            "domestic gesture — and across from her Jesus's gravity "
            "is visibly failing at the edges, the beginning of an "
            "enormous gladness breaking through the test's stern "
            "face like light under a door. Exactly two people are "
            "in the frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r061-b21", "out": "s21-the-room-astonished.jpeg", "seg": "n5b p3",
        "window": "108.94-116.07", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "HOUSE"],
        "narration": ("Bible students love this moment: it is the only "
                      "time in the gospels anyone wins an exchange with "
                      "Jesus."),
        "must_show": "the upset registered — the disciples' stunned faces around the lamplight; the Gentile woman kneeling at the centre, having just won.",
        "must_not_show": "their disapproval of b11 flipped to open astonishment — the same faces, rearranged.",
        "scene": (
            "Around the lamplit room the watchers have forgotten "
            "their propriety: the householder frozen halfway to "
            "sitting, one disciple's eyebrows somewhere near his "
            "hairline, another mouthing something silently to the "
            "man beside him — every stiff face of a few minutes ago "
            "rearranged into pure astonishment around the kneeling "
            "foreign woman who has just, unmistakably, won. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b22", "out": "s22-glad-to-lose.jpeg", "seg": "n5b p4",
        "window": "116.07-120.02", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("And you can almost hear how glad he was to lose "
                      "it."),
        "must_show": "THE face of the build — Jesus's open, delighted, defeated smile; gladness without reservation.",
        "must_not_show": "no halo/glow; the warmest face in the whole video, and nothing but expression makes it so.",
        "scene": (
            "Close on Jesus's face in the full lamplight, and it has "
            "gone entirely open: the test's gravity swept away by a "
            "broad, warm, delighted smile — eyes bright, the lines "
            "at their corners deep — the face of a man who has just "
            "lost an argument he built to be lost, to exactly the "
            "faith he hoped would beat it, and could not be more "
            "glad. Exactly one person is in the frame, with one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b23", "out": "s23-for-this-saying.jpeg", "seg": "n6 + j2",
        "window": "120.02-127.13", "wide": False, "jesus": True, "ref": REF,
        "locks": ["WOMAN"],
        "narration": ("He answered her: For this saying go thy way; the "
                      "devil is gone out of thy daughter. (Mark 7:29)"),
        "must_show": "v29 — the grant: Jesus speaking it to her directly, one hand opening toward the door and the town beyond; the yes, given whole.",
        "must_not_show": "FLAG A: nothing depicted at any distance — the healing is entirely inside the sentence.",
        "scene": (
            "Jesus speaks the grant straight into the kneeling "
            "woman's face, his smile settled now into warm "
            "finality, one hand opening easily toward the plank "
            "door and the night town beyond it where her daughter "
            "lies — the whole miracle passing from his mouth to her "
            "ears with nothing else in the room so much as "
            "stirring. Her face is halfway between the answer and "
            "the running. Exactly two people are in the frame; each "
            "has one head."
        ),
    },
    {
        "id": "v2-r061-b24", "out": "s24-it-is-already-done.jpeg", "seg": "n7 p1-p2",
        "window": "127.13-131.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("Because you said that — go on home. It is already "
                      "done."),
        "must_show": "the word received — close on her face taking the grant whole: relief arriving like a physical weight leaving.",
        "must_not_show": "belief, not doubt — her face must show a woman who will simply go home now.",
        "scene": (
            "Close on the woman's face as the sentence finishes "
            "landing: her eyes close for one long second, the "
            "breath she has been holding since the market lane "
            "leaves her all at once, and the fierce set of her jaw "
            "melts into something that is done fighting — a mother "
            "handed 'already done' and, visibly, believing it to "
            "the bone. Exactly one person is in the frame, with one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b25", "out": "s25-across-the-distance.jpeg", "seg": "n7 p3-p6",
        "window": "131.28-142.13", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "TYRE", "HOUSE"],
        "narration": ("Notice what he did not do. He did not walk to her "
                      "house. He did not touch the girl. He simply said "
                      "it was finished, across the distance, on his word "
                      "alone."),
        "must_show": "the distance itself — from the house door: the woman stepping out into the night lane, the town rising dark toward her far home; the word crossing what he does not.",
        "must_not_show": "no visual travels the gap — just night air, stone lanes and moonlight between the door and the far upper town.",
        "scene": (
            "From inside the doorway the camera looks out from "
            "behind his shoulder: Jesus stands at "
            "the open plank door in the spill of lamplight as the "
            "woman steps away up into the night lane — and beyond "
            "her the town climbs in moonlit terraces toward the "
            "small far lights of the upper streets where her "
            "daughter lies, the whole uncrossed distance of stone "
            "and night hanging between this doorway and that "
            "window, with nothing travelling it but a sentence. "
            "Every figure has two arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r061-b26", "out": "s26-holding-nothing-but-a-word.jpeg", "seg": "n7 p7-p9",
        "window": "142.13-150.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "TYRE"],
        "narration": ("And she believed him enough to just... go home. "
                      "That walk home, holding nothing but his word, was "
                      "the faith he praised."),
        "must_show": "the faith-walk — her climbing the moonlit stepped lanes home, steady and unhurried; no proof in her hands.",
        "must_not_show": "SHOT FROM BEHIND — her back to us, faced up the lane toward home; she does not run in panic, she WALKS in trust.",
        "scene": (
            "SHOT FROM BEHIND THE WOMAN in the moonlit lane, her "
            "back and mantled head to the camera as she climbs the "
            "worn steps AWAY from us toward the upper town — her "
            "pace steady, almost calm, her hands empty and loose at "
            "her sides — a mother walking home through the dark "
            "with nothing to carry but one sentence, carrying it "
            "like the whole loaf. An upright vertical photograph, "
            "the ground at the bottom of the frame and the sky at "
            "the top, the horizon level — the picture is the right "
            "way up. Exactly one person is in the frame."
        ),
    },
    {
        "id": "v2-r061-b27", "out": "s27-she-came-to-her-door.jpeg", "seg": "n8 p1a",
        "window": "150.79-154.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "HERHOME"],
        "narration": ("She came to her door and found her daughter lying "
                      "on the bed, resting —"),
        "must_show": "v30 — the threshold: her stopped in her own doorway, the firelit room beyond, the quiet bed in view.",
        "must_not_show": "the QUIET is the first evidence — a house that has stopped bracing itself.",
        "scene": (
            "The woman stands stopped in her own doorway, one hand "
            "on the frame, the mantle sliding back from her head — "
            "and before her the small firelit room holds a silence "
            "it has not held in months: the low bed against the "
            "wall with its small still shape breathing slow and "
            "even under the teal blanket, the hearth settled, "
            "nothing wrong anywhere in the warm air. Exactly two "
            "people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r061-b28", "out": "s28-quiet-and-whole.jpeg", "seg": "n8 p1b-p3",
        "window": "154.50-162.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "GIRL", "HERHOME"],
        "narration": ("quiet, and whole. The dark thing was gone. It had "
                      "left at the exact moment he spoke."),
        "must_show": "v30 — the proof: the little girl at true rest, face loose and peaceful; the mother kneeling at the bedside seeing it.",
        "must_not_show": "FLAG A: nothing left, nothing shown leaving — peace on a child's face is the entire evidence.",
        "scene": (
            "The mother kneels at the low bed with both hands "
            "pressed over her own mouth, looking: her small "
            "daughter lies unwound at last — fists open on the "
            "blanket, face loose and smooth in true sleep, the "
            "damp curls pushed back from a forehead gone cool — a "
            "child simply resting, in a room where rest was "
            "impossible yesterday. Firelight breathes on the wall "
            "above them. Exactly two people are in the frame; each "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r061-b29", "out": "s29-gathered-into-her-arms.jpeg", "seg": "n9 p1a",
        "window": "162.41-169.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "GIRL", "HERHOME"],
        "narration": ("The first outsider in Mark's gospel to be told yes "
                      "was a Gentile mother with no credentials, no "
                      "standing, and no appointment —"),
        "must_show": "the reunion — the sleeping girl gathered up into her mother's arms; the embrace of a war ended.",
        "must_not_show": "the girl half-wakes into it and settles — safety, not startle.",
        "scene": (
            "The mother has gathered her daughter up off the bed "
            "into her arms, blanket and all — the little girl "
            "stirring half-awake against her shoulder and settling "
            "straight back into sleep there, one small arm looping "
            "her mother's neck by pure habit — while the woman "
            "holds the whole weight of her, eyes shut, cheek on the "
            "black curls, breathing again. Firelight. Exactly two "
            "people are in the frame; each has two arms and one "
            "head."
        ),
    },
    {
        "id": "v2-r061-b30", "out": "s30-faith-that-would-not-leave.jpeg", "seg": "n9 p1b",
        "window": "169.00-175.70", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "GIRL"],
        "narration": ("just a stubborn, clear-eyed faith that would not "
                      "leave without the crumbs."),
        "must_show": "the two faces at rest — mother and sleeping child cheek to cheek in the firelight; the argument won made flesh.",
        "must_not_show": "stillness — after all the motion of the build, this frame does not move.",
        "scene": (
            "Very close in the firelight: the mother's face and "
            "the sleeping child's cheek to cheek — the woman's "
            "quick fierce eyes finally quiet, wet and shining over "
            "her daughter's loose peaceful face — the stubborn, "
            "clear-eyed faith of the lamplit room now holding its "
            "crumbs, which were the whole loaf all along, asleep "
            "in her arms. Exactly two people are in the frame; "
            "each has one head."
        ),
    },
    {
        "id": "v2-r061-b31", "out": "s31-the-whole-loaf.jpeg", "seg": "n9 p2",
        "window": "175.70-178.02", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN", "GIRL", "HERHOME"],
        "narration": "He gave her the whole loaf.",
        "must_show": "the closing image — next morning: mother and daughter at their small table, a whole loaf between them, the girl bright and eating.",
        "must_not_show": "morning light through the door; ordinary breakfast as doxology — the metaphor set on the table, literal.",
        "scene": (
            "Morning light falls through the open door of the small "
            "house onto the low table, where a whole round loaf "
            "sits broken open between the two of them — the little "
            "girl kneeling up on her stool, bright-eyed and "
            "talking with her mouth full, one fist already reaching "
            "for more, while her mother sits across from her doing "
            "nothing at all but watching her eat, her chin on her "
            "hand, the morning entirely unremarkable and entirely "
            "new. Exactly two people are in the frame; each has "
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
}
# === end PLACE-PLATES ===
