#!/usr/bin/env python3
"""V2 beat map — row 168, build-168-born-water-spirit (John 3:1-5).

COVERAGE: 28 pictures over 127.21 s (card_start) = ~4.5 s/picture (matches the
library density set by rows 161-167; lesson 12 movie-coverage — a dialogue plus
its illustrations, every physical idea its own frame, an action a frame per
action).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 168` shows no prior
review). Fresh authoring — the job is the LEARNING/COST laws in the positive.

SCRIPTURE FACTS (John 3 KJV, split across the red-letter beats):
  kv3   "Jesus answered and said unto him,"                    -> scripture voice
  kv3b  "Verily, verily, I say unto thee, Except a man be
         born again, he cannot see the kingdom of God."        -> JESUS
  s4    "How can a man be born when he is old? can he enter
         the second time into his mother's womb, and be born?" -> scripture voice
                                                                  (Nicodemus's words)
  kv5   "Jesus answered,"                                       -> scripture voice
  kv5b  "Verily, verily, I say unto thee, Except a man be born
         of water and of the Spirit, he cannot enter into the
         kingdom of God."                                       -> JESUS

SPEAKER LAW (the row-39 lesson): John's gospel, RED-LETTER. Only kv3b (b08/b09)
and kv5b (b21/b22) are the JESUS voice and they sit on **Jesus's own face**
(jesus=True + ref=True, cream). kv3 and kv5 ("Jesus answered...") are the
SCRIPTURE-voice attributions — the PICTURE shows Jesus about to answer (jesus=
True), the CAPTION is light-blue, not red. **s4 is the SCRIPTURE voice reading
NICODEMUS'S question** — so its beats sit on NICODEMUS's face (jesus=False), the
man who actually asks it, never on Jesus. Jesus is ALSO embodied through the
night dialogue (the narrator beats in the room) because he is physically there
teaching; he is never shown for scale and never haloed.

THE HOLY GHOST IS NEVER EMBODIED (hard gate, same as rows 165/166): "born of the
Spirit... the gift of the Holy Ghost... a birth from above, life breathed into
the soul by heaven" (b17-b19) is warm light and a breath of air coming DOWN from
above the top edge of the frame ONLY — never a dove, never a flame, never a
figure or face in the sky. The Father is likewise never embodied.

TWO TIME-OF-DAY REGISTERS (intentional, and stated so it is not read as a
continuity error): the DIALOGUE is literally at NIGHT — "came to Jesus by night",
"slipped through the dark streets", "came to the light" — so the street and the
room are NIGHT-LAMPLIGHT (real darkness, one small clay oil lamp, flame low and
in front so no head is ever haloed). The metaphors Jesus explains are NOT
happening in that night room, so the video cuts to them as their own daytime
illustrations: the new birth of WATER as a real river BAPTISM in bright day
(b15/b16), the new birth of the SPIRIT as warm light from above on the same new
believer (b17-b19), and the GATE as a doorway open to warm dawn light
(b25-b28). The V1 stills chose the same split.

FOUR NEW PLACES (runner promotes each from its first good NON-Jesus frame,
lesson 11; never promote a Jesus frame):
  NIGHT-STREET  promote b01, wire b02          (+ names NIGHT-LAMPLIGHT)
  NIGHT-ROOM    promote the first NON-Jesus room frame b10, wire b11/b12/b13/b24
                (the many Jesus room beats carry their own Jesus lock over the
                 same prose)               (+ names NIGHT-LAMPLIGHT)
  RIVER         promote b15, wire b16/b17/b18/b19
  GATE          promote b25, wire b26/b27/b28
Full steps in QC.md.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER
# name a character. The shared JESUS lock + REF come from v2_prompt.py via the
# jesus/ref flags — never written here. NIGHT-LAMPLIGHT is a SHARED lock (named
# in each night beat's `locks`), so it is not redefined here.
LOCKS = {
    "NIGHT-STREET": (
        "NIGHT-STREET LOCK: the same place in every frame — a narrow "
        "first-century town street at genuine night, pale mud-brick and "
        "dressed-stone houses close on either side with plain square dark "
        "doorways, a worn bare-earth way underfoot, a deep blue-black sky with "
        "real stars above the rooflines. The same close street and houses "
        "throughout — never a lit window of modern glass, never a lamp-post, "
        "never a wire or pole, never any modern structure."
    ),
    "NIGHT-ROOM": (
        "NIGHT-ROOM LOCK: the same place in every frame — a plain first-century "
        "room at night, walls of dressed limestone and pale mud-plaster, a low "
        "stone bench and a floor mat of hand-woven wool, a small shallow clay "
        "oil lamp standing on a stone ledge, and one plain square opening giving "
        "onto deep night. The same modest room throughout — never a chair or "
        "raised table, never glass, never a hanging fixture, never any modern "
        "object."
    ),
    "RIVER": (
        "RIVER LOCK: the same place in every frame — a first-century river in "
        "bright warm daylight, clear moving water waist-deep over a pale gravel "
        "bed, green reeds and low brush along the banks, dun hills beyond under "
        "an open sky. The same river and banks throughout — never a modern weir, "
        "bridge, pipe, rail or building, and nothing manufactured in or by the "
        "water."
    ),
    "GATE": (
        "GATE LOCK: the same place in every frame — a single plain first-century "
        "doorway cut through a low wall of dressed limestone and sun-dried mud "
        "brick, square-topped under one flat stone lintel, standing OPEN with "
        "warm dawn light spilling through from the bright ground beyond; a worn "
        "hollowed stone threshold, bare packed earth before it. The same one "
        "open doorway throughout — never wrought or cast iron, never a bar, "
        "grille, hinge, latch or lock of manufactured metal, never a modern gate "
        "of any later century, never a sign or lettering."
    ),
    "NICODEMUS": (
        "NICODEMUS LOCK: an older dignified first-century ruler and teacher of "
        "the Jews, near sixty, a full well-kept grey-streaked dark beard, "
        "deep-set thoughtful brown eyes, a high lined brow; sober robes of rich "
        "deep indigo and umber wool with a fringed mantle (a tasselled prayer "
        "shawl) over the shoulders (never cream — only Jesus wears cream); a man "
        "of rank and learning, earnest, humble and searching. The SAME man in "
        "every frame he appears in, never twinned, never a cloned face."
    ),
    "NEW-BELIEVER": (
        "NEW-BELIEVER LOCK: one ordinary first-century person of middle years "
        "who is born again in the illustrations — a plain sun-browned face, dark "
        "hair, a simple earth-toned wool tunic (never cream — only Jesus wears "
        "cream), the same person wet at the river, then dry at the gate. The "
        "SAME person in every illustration frame, never twinned, never a cloned "
        "face."
    ),
    "BAPTIZER": (
        "BAPTIZER LOCK: one plain older first-century man who performs the "
        "baptism, standing in the river in a simple wet earth-toned tunic (never "
        "cream), a short grey beard, steady and reverent; the SAME man across "
        "the river frames, never twinned, never a cloned face."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r168-b01", "out": "s01-nicodemus-by-night.jpeg", "seg": "n1",
        "window": "0.280-5.480", "wide": True, "jesus": False, "ref": False,
        "locks": ["NIGHT-STREET", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Nicodemus was a ruler and a respected teacher, a man near the top of his world.",
        "must_show": "the ONE establishing wide — the camera stands back down the dark street behind Nicodemus, shooting PAST his back as he moves alone at night, a small clay oil lamp low in his hand; a dignified ruler out in the dark, seen from behind.",
        "must_not_show": "no Jesus and no cream anywhere; not posed to the lens; no bright ring or halo around his head — the lamp is low and in front; no lit modern window, lamp-post, wire or pole; no panel, border or text.",
        "scene": (
            "The film opens in the dark: the camera stands a few steps behind "
            "Nicodemus, down the narrow night street, and shoots PAST his back "
            "and shoulders — his back to us — as this dignified older ruler in a "
            "fringed deep-indigo mantle moves alone between the close pale "
            "houses, a small shallow "
            "clay oil lamp carried low in one hand throwing its little light up "
            "onto the front of his face and the wall beside him. Stars stand in "
            "the blue-black sky above the rooflines. His back is to us, his gaze "
            "ahead down the street, an ordinary-sized man with two hands and one "
            "head; the crown and back of his head stay dark."
        ),
    },
    {
        "id": "v2-r168-b02", "out": "s02-a-man-of-standing.jpeg", "seg": "n1",
        "window": "5.480-9.700", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHT-STREET", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "And yet, one night, he slipped quietly through the dark streets",
        "must_show": "closer on Nicodemus in the dark street — his careful, weighty, high-born face lit low by the lamp he carries, glancing to be sure he is unseen; a man of standing moving in secret.",
        "must_not_show": "no Jesus and no cream; not posed to the lens; no light behind or above his head, no halo — the flame is low and in front; the crown of the head dark; no modern object; no panel or text.",
        "scene": (
            "A man of rank moving in secret: closer now, Nicodemus pauses in the "
            "dark street and turns his lined, thoughtful face a little to the "
            "side to be sure the way is empty, his small clay lamp held low at "
            "his chest so its warm light climbs only the underside of his brow, "
            "nose and grey-streaked beard while the top and back of his head stay "
            "in night. His deep-toned mantle is fine but sober. His eyes travel "
            "off past the camera; an ordinary-sized man, two hands, one head, no "
            "ring of light anywhere on him."
        ),
    },
    {
        "id": "v2-r168-b03", "out": "s03-humble-enough-to-learn.jpeg", "seg": "n1",
        "window": "9.700-13.875", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "to ask his questions in private, humble enough to come and learn.",
        "must_show": "Nicodemus at a lamplit doorway, pausing on the threshold, head slightly bowed — a high teacher humbling himself to come and learn, about to enter the light of the room.",
        "must_not_show": "no Jesus yet and no cream; not posed to the lens; no halo — lamplight low and in front; the crown dark; no modern door, glass or fitting; no panel or text.",
        "scene": (
            "Humility on the threshold: Nicodemus stands at the plain square "
            "doorway of a modest house, one hand on the stone jamb, his head "
            "dipped a little, the warm low light of a lamp inside the room "
            "reaching out onto the front of his face and his fringed mantle from "
            "below — a learned ruler lowering himself to come and ask and learn. "
            "The night is black around the doorway. He looks in and down, not at "
            "the camera; an ordinary-sized man, two hands, one head, the top of "
            "his head unlit."
        ),
    },
    {
        "id": "v2-r168-b04", "out": "s04-came-to-the-light.jpeg", "seg": "n2",
        "window": "13.875-19.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "He came to the light and listened.",
        "must_show": "Nicodemus seated across from Jesus in the lamplit room, leaning in to listen; the small oil lamp low between them lighting both faces from below — the ruler come to the light.",
        "must_not_show": "no halo or ring of light around either head — the lamp is low and in front; Jesus ordinary-sized, only Jesus in cream; Nicodemus in his deep-toned mantle; no face posed to the lens; no panel or text.",
        "scene": (
            "The ruler at the light: Nicodemus sits on a low stone bench leaning "
            "forward to listen, and across the small shallow clay oil lamp set "
            "low between them sits Jesus in his plain cream wool robe, calm and "
            "warm. The single flame stands low and in front of both men so its "
            "light climbs the undersides of their faces while the crowns and "
            "backs of their heads stay dark and merge into the night room. Their "
            "eyes are on each other, not the lens. Both are ordinary-sized men "
            "with two hands and one head; nothing rings either head."
        ),
    },
    {
        "id": "v2-r168-b05", "out": "s05-world-turned-over.jpeg", "seg": "n2",
        "window": "19.000-23.050", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "And what he heard turned his careful world upside down. It was not a small adjustment or one more rule to keep.",
        "must_show": "Nicodemus's face startled and unsettled as he listens, Jesus's open hand gesturing gently across the lamp — the careful ruler's world tipping over at what he hears.",
        "must_not_show": "no halo — lamp low and in front; the crowns dark; ordinary-sized; only Jesus in cream; distinct faces; no face posed to the lens; no panel or text.",
        "scene": (
            "The careful world tips: in the low lamplight Nicodemus draws back a "
            "little, his high brow furrowing and his eyes widening at what he is "
            "hearing, while Jesus across the lamp lifts one open hand in a calm "
            "unhurried gesture. The single flame between them lights their faces "
            "from below and leaves the tops of their heads in darkness. Nicodemus "
            "in deep indigo, Jesus in cream; their gazes hold each other, not the "
            "camera. Both ordinary-sized, two hands and one head, no light "
            "ringing either head."
        ),
    },
    {
        "id": "v2-r168-b06", "out": "s06-a-whole-new-beginning.jpeg", "seg": "n2",
        "window": "23.050-28.153", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "It was a whole new beginning — a person must be born all over again.",
        "must_show": "Jesus speaking earnestly and gently to Nicodemus across the lamp, Nicodemus taking it in — the weight of a whole new beginning settling between them.",
        "must_not_show": "no halo — lamp low and in front; the crowns dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The heart of it spoken quietly: Jesus leans a little toward "
            "Nicodemus in the lamplight, his warm brown eyes steady and his hands "
            "open in earnest explanation, and Nicodemus holds still, taking in "
            "the weight of a wholly new beginning. The lamp low between them "
            "lights the fronts of their faces and leaves their crowns dark. Jesus "
            "in cream, Nicodemus in his fringed deep-toned mantle; their eyes are "
            "on each other. Both ordinary-sized men, two hands and one head, "
            "nothing rings either head."
        ),
    },
    {
        "id": "v2-r168-b07", "out": "s07-jesus-answered.jpeg", "seg": "kv3",
        "window": "28.153-31.839", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Jesus answered and said unto him,",
        "must_show": "SCRIPTURE-ATTRIBUTION — Jesus turning toward Nicodemus and drawing breath to answer, the moment just before he speaks; both lit low by the lamp.",
        "must_not_show": "no halo — lamp low and in front; the crowns dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The pause before the answer: Jesus turns fully toward Nicodemus in "
            "the lamplight, his face lifting and steadying as he draws breath to "
            "speak, one hand beginning to open. The single low flame lights the "
            "front of his face and Nicodemus's beside it and leaves the tops of "
            "their heads in the dark of the room. Jesus in cream, Nicodemus "
            "attentive in deep indigo, their eyes meeting, not the lens. Both "
            "ordinary-sized, two hands and one head, no ring of light on either."
        ),
    },
    {
        "id": "v2-r168-b08", "out": "s08-except-a-man-be-born-again.jpeg", "seg": "kv3b",
        "window": "31.839-36.700", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Verily, verily, I say unto thee, Except a man be born again,",
        "must_show": "SCRIPTURE-EXACT (Jesus's red-letter) — Jesus speaking with warm gravity to Nicodemus, one hand raised gently in solemn teaching: except a man be born again.",
        "must_not_show": "no halo or ring around Jesus's head — lamp low and in front, crown dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The great saying, first half: Jesus speaks to Nicodemus with warm "
            "solemn weight, one hand lifted a little in earnest teaching, his "
            "brown eyes fixed on the ruler across the lamp. The low flame lights "
            "the underside of his face and his lifted hand and leaves the crown "
            "and back of his head in darkness. He is an ordinary-sized man in "
            "plain cream wool; Nicodemus listens in deep indigo. Their gazes "
            "hold, not the lens; two hands and one head each, nothing ringing "
            "Jesus's head."
        ),
    },
    {
        "id": "v2-r168-b09", "out": "s09-cannot-see-the-kingdom.jpeg", "seg": "kv3b",
        "window": "36.700-41.326", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "he cannot see the kingdom of God.",
        "must_show": "SCRIPTURE-EXACT — Jesus finishing the saying, Nicodemus's face grave and stirred as the words land; the two close in the lamplight.",
        "must_not_show": "no halo — lamp low and in front, crowns dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The saying lands: Jesus completes the words with quiet finality, his "
            "gaze holding Nicodemus, and the ruler's grave face registers the "
            "weight of them across the low lamp. The flame lights both faces from "
            "below and leaves their crowns dark in the night room. Jesus in "
            "cream, Nicodemus in his fringed mantle; their eyes on each other, "
            "not the camera. Both ordinary-sized men, two hands and one head, no "
            "light ringing either head."
        ),
    },
    {
        "id": "v2-r168-b10", "out": "s10-how-can-a-man-be-born.jpeg", "seg": "s4",
        "window": "41.326-45.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "How can a man be born when he is old?",
        "must_show": "SCRIPTURE-EXACT (Nicodemus's own words) — Nicodemus leaning in, brow furrowed, genuinely puzzled, asking; the frame is on HIM, the man speaking, not on Jesus.",
        "must_not_show": "Jesus NOT the subject of this frame (Nicodemus's question sits on Nicodemus); no cream on Nicodemus; no halo — lamp low and in front, crown dark; no face posed to the lens; no panel or text.",
        "scene": (
            "The ruler's honest puzzle: Nicodemus leans forward into the lamp "
            "light, his high brow deeply furrowed and one hand half-lifted in "
            "genuine bafflement, asking how a man can possibly be born when he is "
            "old. The single low flame lights the front of his lined face and "
            "grey-streaked beard and leaves the top of his head dark. He is in "
            "his deep-indigo mantle, an ordinary-sized man, two hands and one "
            "head, his eyes on the unseen Jesus across the lamp, not the camera; "
            "no light rings his head."
        ),
    },
    {
        "id": "v2-r168-b11", "out": "s11-enter-a-second-time.jpeg", "seg": "s4",
        "window": "45.500-49.366", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "can he enter the second time into his mother's womb, and be born?",
        "must_show": "SCRIPTURE-EXACT — Nicodemus opening both hands in incredulous disbelief at the plain literal impossibility; still the man asking, alone in the lamplight.",
        "must_not_show": "no Jesus subject here and no cream on Nicodemus; no halo — lamp low and in front, crown dark; no face posed to the lens; no modern object; no panel or text.",
        "scene": (
            "Incredulity spread on open hands: Nicodemus spreads both hands wide "
            "in the lamplight, shaking his head slightly at the plain "
            "impossibility of a grown man entering again to be born, his face "
            "caught between respect and disbelief. The low flame lights the "
            "underside of his face and his open hands and leaves the top of his "
            "head in darkness. He is in deep indigo, an ordinary-sized man with "
            "whole hands and one head, eyes toward the unseen teacher, not the "
            "lens; nothing rings his head."
        ),
    },
    {
        "id": "v2-r168-b12", "out": "s12-took-it-literally.jpeg", "seg": "n3",
        "window": "49.366-53.340", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Nicodemus took it literally, and was baffled. He could not picture it.",
        "must_show": "Nicodemus baffled — a hand to his furrowed brow, eyes down, unable to picture the thing; the learned man stuck on the literal.",
        "must_not_show": "no Jesus subject and no cream on Nicodemus; no halo — lamp low and in front, crown dark; no face posed to the lens; no panel or text.",
        "scene": (
            "Stuck on the literal: Nicodemus lowers his eyes and lifts one hand "
            "to his furrowed brow in the lamplight, unable to picture what he has "
            "heard, the careful teacher baffled by a thing his learning cannot "
            "hold. The low flame lights the front of his face and hand and leaves "
            "his crown dark. He is in his deep-toned mantle, an ordinary-sized "
            "man, two hands and one head, gaze down and inward, not at the "
            "camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r168-b13", "out": "s13-no-one-could-start-over.jpeg", "seg": "n3",
        "window": "53.340-57.849", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Surely no one could climb back and start his life over from the beginning.",
        "must_show": "Nicodemus giving a slight, certain shake of the head — sure that no one could climb back and begin life again; still reading it as flesh, not spirit.",
        "must_not_show": "no Jesus subject and no cream on Nicodemus; no halo — lamp low and in front, crown dark; no face posed to the lens; no panel or text.",
        "scene": (
            "Certain of the impossible: Nicodemus gives a small, sure shake of "
            "his head in the lamplight, convinced no living man could climb back "
            "and begin his whole life over from the start, his mind still on "
            "flesh and not on spirit. The low flame lights the underside of his "
            "grave face and leaves the top of his head dark. He is in deep "
            "indigo, an ordinary-sized man, two hands and one head, his eyes off "
            "to the side in thought, not the lens; nothing rings his head."
        ),
    },
    {
        "id": "v2-r168-b14", "out": "s14-never-meant-physical.jpeg", "seg": "n4",
        "window": "57.849-62.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "But the new birth was never meant to be physical.",
        "must_show": "Jesus gently correcting across the lamp — a calm open-handed gesture, turning Nicodemus from the literal flesh toward what he really means; the pivot into the illustrations.",
        "must_not_show": "no halo — lamp low and in front, crowns dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The gentle correction: Jesus lifts a calm open hand toward Nicodemus "
            "across the lamp, his face patient and kind, turning the ruler away "
            "from the picture of flesh toward the true meaning of the new birth. "
            "The low flame lights the fronts of both faces and leaves their "
            "crowns dark in the night room. Jesus in cream, Nicodemus attentive "
            "in deep indigo; their eyes meet, not the lens. Both ordinary-sized, "
            "two hands and one head, no ring of light on either head."
        ),
    },
    {
        "id": "v2-r168-b15", "out": "s15-down-into-the-water.jpeg", "seg": "n4",
        "window": "62.000-66.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["RIVER", "NEW-BELIEVER", "BAPTIZER"],
        "narration": "To be born again is first to be born of water — to go down into the water of baptism",
        "must_show": "a DAYTIME river baptism, the DOWN action — the new believer being lowered back into the clear river water in the baptizer's steady hands; going down into the water.",
        "must_not_show": "no Jesus and no cream (illustration, Jesus not in this frame); no modern object in or by the water; whole hands, natural contact; no halo on anyone; no panel or text.",
        "scene": (
            "The water birth, going down: in bright warm daylight the new "
            "believer is being lowered backward into the clear waist-deep river, "
            "steadied by the reverent baptizer's two hands, the believer's eyes "
            "closing and the water rising to receive them — the going-down of "
            "baptism. Green reeds line the bank, dun hills stand beyond under an "
            "open sky. Both are ordinary earth-toned people of ordinary height "
            "with whole hands and one head each, neither looking at the camera; "
            "nothing modern is in or near the water."
        ),
    },
    {
        "id": "v2-r168-b16", "out": "s16-come-up-new.jpeg", "seg": "n4",
        "window": "66.400-70.806", "wide": False, "jesus": False, "ref": False,
        "locks": ["RIVER", "NEW-BELIEVER", "BAPTIZER"],
        "narration": "and come up new, the old life washed away and left behind.",
        "must_show": "the UP action — the new believer rising up out of the river water, streaming and gasping, face lifted, made new; a frame per action after the going-down.",
        "must_not_show": "no Jesus and no cream; no modern object; whole hands; no halo — bright natural daylight; no face posed to the lens; no panel or text.",
        "scene": (
            "The water birth, coming up: the new believer rises straight up out "
            "of the clear river, water streaming off face and hair and shoulders, "
            "eyes opening and breath drawn, the reverent baptizer's hands still "
            "steadying them — the old life washed away and left in the water "
            "behind. Bright daylight glints off the running water; the reeds and "
            "dun hills stand beyond. Both are ordinary earth-toned people of "
            "ordinary height, whole hands, one head each, faces lifted to the "
            "light and the sky, not the camera; nothing modern anywhere."
        ),
    },
    {
        "id": "v2-r168-b17", "out": "s17-not-water-only.jpeg", "seg": "n5",
        "window": "70.806-74.290", "wide": False, "jesus": False, "ref": False,
        "locks": ["RIVER", "NEW-BELIEVER"],
        "narration": "And there was a second half to it, not water only.",
        "must_show": "the same new believer now standing on the riverbank, still wet, a quiet pause — water alone was not the whole of it; the believer waiting, looking up, ready for the second half.",
        "must_not_show": "no Jesus and no cream; NO dove, flame or figure anywhere (Holy Ghost never embodied); no halo on the believer; no modern object; no panel or text.",
        "scene": (
            "A pause between the halves: the new believer stands on the reedy "
            "riverbank in the warm day, tunic and hair still dripping, hands "
            "loose and open at their sides, face lifting a little as if aware "
            "that the water alone is not the whole of the new birth — waiting for "
            "what comes next. The clear river runs behind, dun hills beyond. An "
            "ordinary earth-toned person of ordinary height, whole hands, one "
            "head, eyes lifted off past the camera; no dove, flame or figure "
            "anywhere, no light ringing the head."
        ),
    },
    {
        "id": "v2-r168-b18", "out": "s18-born-of-the-spirit.jpeg", "seg": "n5",
        "window": "74.290-79.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["RIVER", "NEW-BELIEVER"],
        "narration": "To be born of the Spirit is to receive the gift of the Holy Ghost —",
        "must_show": "the new believer receiving from above — warm light and a stir of air coming DOWN from the top of the frame onto the upturned face and open hands; the gift of the Spirit given from heaven.",
        "must_not_show": "the Holy Ghost NEVER embodied — NO dove, NO flame, NO figure, NO face in the sky; only warm light and moved air from the top edge; no halo or ring around the head; no cream; no panel or text.",
        "scene": (
            "The Spirit given, shown as light from above: the new believer stands "
            "with face upturned and hands opening, and warm light comes down from "
            "beyond the top edge of the frame across the face and open palms, a "
            "stir of air lifting the wet hair — the gift of the Spirit received "
            "from heaven. The light stays high at the frame's edge and never "
            "becomes a bird, a flame, a shape or a face. The river and dun hills "
            "sit soft behind. An ordinary earth-toned person of ordinary height, "
            "whole open hands, one head, no ring of light on it."
        ),
    },
    {
        "id": "v2-r168-b19", "out": "s19-a-birth-from-above.jpeg", "seg": "n5",
        "window": "79.000-83.740", "wide": False, "jesus": False, "ref": False,
        "locks": ["RIVER", "NEW-BELIEVER"],
        "narration": "a birth from above, life breathed into the soul by heaven itself.",
        "must_show": "the believer transformed — the warm light from above fuller now, the face eased and alive, a breath drawn in; life breathed into the soul from heaven, shown wholly on the person, not by any effect.",
        "must_not_show": "NO dove, flame, figure or face in the sky; only warm light from the top edge; no halo around the head; no cream; nobody a giant; no panel or text.",
        "scene": (
            "Life breathed in from above: the warm light from beyond the top of "
            "the frame falls fuller across the new believer's upturned face and "
            "shoulders, the eyes softening and a slow breath drawn in, the whole "
            "person coming alive with a birth from above — the change read "
            "entirely on the human face, never as a special effect. The light "
            "stays high and becomes no shape. The river runs behind in the day. "
            "An ordinary earth-toned person of ordinary height, whole hands, one "
            "head, nothing ringing it."
        ),
    },
    {
        "id": "v2-r168-b20", "out": "s20-jesus-answered.jpeg", "seg": "kv5",
        "window": "83.740-86.568", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Jesus answered,",
        "must_show": "SCRIPTURE-ATTRIBUTION — back in the night room, Jesus turning again to Nicodemus and drawing breath to answer; both lit low by the lamp.",
        "must_not_show": "no halo — lamp low and in front, crowns dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "Back to the lamplight for the answer: Jesus turns once more toward "
            "Nicodemus and lifts his face to speak, one hand beginning to open, "
            "the small low flame lighting the fronts of both faces and leaving "
            "their crowns dark in the night room. Jesus in cream, Nicodemus "
            "attentive in deep indigo, eyes meeting across the lamp, not the "
            "lens. Both ordinary-sized men, two hands and one head, no ring of "
            "light on either head."
        ),
    },
    {
        "id": "v2-r168-b21", "out": "s21-born-of-water-and-spirit.jpeg", "seg": "kv5b",
        "window": "86.568-91.800", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Verily, verily, I say unto thee, Except a man be born of water and of the Spirit,",
        "must_show": "SCRIPTURE-EXACT (Jesus's red-letter) — Jesus naming the two births together with warm gravity, perhaps two fingers or an open hand marking water and Spirit; Nicodemus listening intently.",
        "must_not_show": "no halo — lamp low and in front, crown dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The two births named together: Jesus speaks the great saying with "
            "warm solemn weight, one hand open and marking the pairing of water "
            "and Spirit, his brown eyes fixed on Nicodemus across the low lamp. "
            "The single flame lights the underside of his face and hand and "
            "leaves his crown and the back of his head dark. He is an "
            "ordinary-sized man in cream; Nicodemus listens gravely in deep "
            "indigo. Their gazes hold, not the camera; two hands and one head "
            "each, nothing ringing Jesus's head."
        ),
    },
    {
        "id": "v2-r168-b22", "out": "s22-cannot-enter-the-kingdom.jpeg", "seg": "kv5b",
        "window": "91.800-96.882", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "he cannot enter into the kingdom of God.",
        "must_show": "SCRIPTURE-EXACT — Jesus finishing with quiet finality, Nicodemus's grave face taking the full weight; the two close in the lamplight.",
        "must_not_show": "no halo — lamp low and in front, crowns dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The gate stated plainly: Jesus closes the saying with quiet "
            "finality, his gaze steady on Nicodemus, and the ruler's grave face "
            "receives the whole weight of it across the low lamp. The flame "
            "lights both faces from below and leaves their crowns in the dark of "
            "the night room. Jesus in cream, Nicodemus in his fringed mantle; "
            "their eyes on each other, not the lens. Both ordinary-sized men, two "
            "hands and one head, no light ringing either head."
        ),
    },
    {
        "id": "v2-r168-b23", "out": "s23-not-one-option-among-many.jpeg", "seg": "n6",
        "window": "96.882-102.480", "wide": False, "jesus": True, "ref": True,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "Here is the quiet study gem. Notice he did not say this was one good option among many.",
        "must_show": "Jesus's quiet emphasis — one hand or a single raised finger marking that this is not one choice among many but the one way; the calm certainty of it in the lamplight.",
        "must_not_show": "no halo — lamp low and in front, crown dark; ordinary-sized; only Jesus in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "The one way, not one of many: Jesus holds up a single steady hand in "
            "the lamplight, his warm face calm and certain, marking that he has "
            "named not one option among several but the single way in, while "
            "Nicodemus watches gravely. The low flame lights the fronts of their "
            "faces and the raised hand and leaves their crowns dark. Jesus in "
            "cream, Nicodemus in deep indigo; their eyes on each other, not the "
            "lens. Both ordinary-sized, two hands and one head, no ring of light "
            "on either head."
        ),
    },
    {
        "id": "v2-r168-b24", "out": "s24-the-same-for-everyone.jpeg", "seg": "n6",
        "window": "102.480-106.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["NIGHT-ROOM", "NIGHT-LAMPLIGHT", "NICODEMUS"],
        "narration": "He said a person cannot enter without it. The gate is the gate —",
        "must_show": "Nicodemus, the learned upright ruler, quietly humbled in the lamplight — realizing the one gate is the same for him too, no exception for rank or learning.",
        "must_not_show": "no Jesus subject here and no cream on Nicodemus; no halo — lamp low and in front, crown dark; no face posed to the lens; no panel or text.",
        "scene": (
            "The ruler measured by the same gate: Nicodemus sits quiet and "
            "humbled in the lamplight, his high learned face softened as he takes "
            "in that the one gate is the same for everyone, himself included, "
            "with no exception for his rank or his learning. The low flame lights "
            "the front of his lined face and grey-streaked beard and leaves the "
            "top of his head dark. He is in his fringed deep-toned mantle, an "
            "ordinary-sized man, two hands and one head, eyes down in thought, "
            "not the camera; no light rings his head."
        ),
    },
    {
        "id": "v2-r168-b25", "out": "s25-even-a-learned-ruler.jpeg", "seg": "n6",
        "window": "106.500-111.530", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATE"],
        "narration": "the same for everyone, even a learned and upright ruler like Nicodemus.",
        "must_show": "the GATE illustration introduced — a single plain first-century doorway standing OPEN with warm dawn light beyond, one way in for all, no matter their standing; empty and open, waiting.",
        "must_not_show": "no Jesus and no cream; no iron, bar, hinge or lock of manufactured metal; no sign or lettering; no halo or ring of light — natural dawn beyond; no panel or text.",
        "scene": (
            "The one gate shown plain: a single square-topped doorway cut through "
            "a low wall of dressed limestone and mud brick stands open, warm dawn "
            "light spilling through from the bright ground beyond onto the worn "
            "hollowed stone threshold — one plain way in, the same for anyone who "
            "would come, high or low. Bare packed earth lies before it. There is "
            "no person in the frame yet, nothing modern, no metal fitting, and no "
            "light that becomes a shape — only the open door and the dawn behind "
            "it."
        ),
    },
    {
        "id": "v2-r168-b26", "out": "s26-the-gate-still-open.jpeg", "seg": "n7",
        "window": "111.530-117.930", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATE", "NEW-BELIEVER"],
        "narration": "And that same single gate still stands open before you: born of water, and born of the Spirit.",
        "must_show": "the new believer (the viewer's stand-in) standing before the open gate in the dawn light, the way plainly open ahead of them — water and Spirit both behind them, the door before them.",
        "must_not_show": "no Jesus and no cream; no metal fitting, bar or lock; no halo — natural dawn; not posed to the lens; no panel or text.",
        "scene": (
            "The way open before the one watching: the new believer stands a few "
            "steps back from the open stone doorway, seen from behind and the "
            "side, the warm dawn light beyond the threshold laid out plainly "
            "ahead of them — the same single gate still standing open, water and "
            "Spirit both already behind them. The believer's gaze is on the "
            "opening, not the camera. A plain earth-toned person of ordinary "
            "height, whole hands, one head; nothing modern, no metal on the door, "
            "no ring of light anywhere."
        ),
    },
    {
        "id": "v2-r168-b27", "out": "s27-simply-the-way-in.jpeg", "seg": "n7",
        "window": "117.930-123.710", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATE"],
        "narration": "The door is not hidden and it is not narrow with pride — it is simply the way in.",
        "must_show": "the open doorway plainly welcoming — full, clear, unbarred, warm light straight through, nothing hiding it and nothing forbidding; simply the way in.",
        "must_not_show": "no Jesus and no cream; nothing barring or crowding the opening; no metal gate, bar or lock; no sign or lettering; no halo — natural dawn; no panel or text.",
        "scene": (
            "The door as pure welcome: the open stone doorway fills the frame "
            "square and clear, the warm dawn light coming straight through it "
            "onto the threshold, nothing hiding it and nothing set across it to "
            "forbid the way — plainly and simply the way in. The low walls sit "
            "quiet on either side, bare earth before. No person, nothing modern, "
            "no metal fitting, no light that becomes a shape — only the open way "
            "and the light beyond."
        ),
    },
    {
        "id": "v2-r168-b28", "out": "s28-will-you-go-through.jpeg", "seg": "n7",
        "window": "123.710-127.212", "wide": False, "jesus": False, "ref": False,
        "locks": ["GATE", "NEW-BELIEVER"],
        "narration": "When you stand before it, will you go through?",
        "must_show": "the new believer at the very threshold, one foot at the open door, on the edge of stepping through into the warm light — the invitation handed to the viewer, left open and hopeful.",
        "must_not_show": "no Jesus and no cream; no metal fitting, bar or lock on the door; no halo — natural dawn light; not posed to the lens; no panel or text.",
        "scene": (
            "The question at the threshold: the new believer stands right at the "
            "open stone doorway, one foot lifting toward the worn threshold and "
            "the warm dawn light beyond, poised on the edge of stepping through — "
            "the choice handed across to the one watching. Seen from behind and "
            "the side so the gaze goes through the door, not to the camera. A "
            "plain earth-toned person of ordinary height, whole hands, one head; "
            "nothing modern, no metal on the door, no ring of light anywhere, the "
            "light ahead warm and open."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
#
# EMPTY BY DESIGN. All four recurring places are NEW. The runner PROMOTES each
# from this build's first good NON-Jesus frame (never a Jesus frame — lesson 11):
#   NIGHT-STREET  promote b01, wire b02
#   NIGHT-ROOM    promote the first NON-Jesus room frame b10, wire b11/b12/b13/b24
#                 (b04-b09, b14, b20-b23 are Jesus frames — prose place text)
#   RIVER         promote b15, wire b16/b17/b18/b19
#   GATE          promote b25, wire b26/b27/b28
# Full steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
