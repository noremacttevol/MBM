#!/usr/bin/env python3
"""V2 beat map — row 171, build-171-baptized-for-the-dead (1 Corinthians 15:29 +
the resurrection anchor, vv. 20-22).

COVERAGE: 15 pictures over 73.43 s (card_start) = ~4.9 s/picture (lesson 12
movie-coverage). Shorter row (73 s), so the beat count is scaled down with it.

OPEN CAMERON COMPLAINT (MUST FIX — LEARNING LAW): `v2_outline.py 171` shows
[OPEN]: "First picture is weird there are no scripture that roll like that on 2
edges." The V1 first still put a SCROLL with rendered scripture text CURLING on
two edges into frame — it read as a fake panel/generated-text artifact. FIX: the
new first picture (b01) is PEOPLE — Paul debating the Corinthians — and its
must_not_show HARD-BANS any scroll with visible writing, any curling/rolling
parchment edge, any rendered lettering, and any panel/border. NO frame in this
build renders scripture text as part of the art (captions are added later, in the
bottom band only). See the COMPLAINT LEDGER in QC.md.

SPEAKER LAW: Paul's epistle. s1 ("Else what shall they do which are baptized for
the dead…"), s20 ("But now is Christ risen from the dead…") and s22 ("For as in
Adam all die…") are all the SCRIPTURE voice → LIGHT-BLUE captions, never red.
There is NO Jesus-red and NO God-voice. Jesus IS embodied (risen Lord, locked
face + REF, cream) on the two resurrection-anchor beats b09 and b11 — the picture
shows him because "Christ risen" is the concrete fact Paul builds on; the caption
stays scripture-blue (s20) / narrator.

CONTENT-CARE: row 171 is GREEN (not in the flag table), but the subject is the
DEAD, so restraint governs: the departed are shown with DIGNITY and HOPE — a
mourner's remembering face, a covered bier or plain grave at a distance, warm
dawn light. NEVER a corpse, never gore, never rising bodies / open graves with
figures climbing out ("the grave loses its grip" is DAWN LIGHT and an EMPTY tomb,
not zombies). "Across the veil" is soft light, never literal ghosts.

THE DOCTRINE, MADE CONCRETE (realistic biblical photography, not abstract V1
metaphors): baptism for the dead is a LIVING believer (the PROXY) baptized in
water on behalf of one who has died, done in love while the departed's family
(the MOURNER) remembers them. The video anchors in three real settings:
  CORINTH-PORTICO  Paul teaching the Corinthians (b01, b02)
  BAPTISM-WATER    the proxy baptism + the remembering family (b03-b08, b14, b15)
  RISEN-DAWN       the empty tomb + the risen Christ, the resurrection anchor
                   (b09-b13)

NEW places (runner promotes each from its first good NON-Jesus frame, lesson 11):
  CORINTH-PORTICO  promote b01
  BAPTISM-WATER    promote b03
  RISEN-DAWN       promote b10 (the empty tomb — NOT b09, which is a Jesus frame)
Steps in QC.md.
"""

# LOCKS: PAUL is BYTE-IDENTICAL to rows 138/155/166 (cross-video same man; his
# face is carried by this text lock — no face sheet exists yet, same as those
# rows). Setting/person locks NEVER conflict; only Jesus wears cream.
LOCKS = {
    "PAUL": (
        "PAUL LOCK: Paul is the same man in every shot — compact and wiry, "
        "about fifty, balding with a fringe of dark hair, a full pointed dark "
        "beard, keen deep-set eyes, in a plain DARK RUST-BROWN travel robe "
        "(never cream, never white); a tentmaker's strong hands; earnest fire "
        "without anger."
    ),
    "CORINTH-PORTICO": (
        "CORINTH-PORTICO LOCK: the same place in every frame — a plain "
        "first-century Greek-Roman colonnaded portico in a port city, pale "
        "dressed-stone columns and a worn stone floor, a bright Mediterranean "
        "day beyond, low city rooftops and a strip of harbour sea in the "
        "distance. The same columns and floor throughout — never modern glass, "
        "signage, wire, pole or fixture, and no rendered writing anywhere."
    ),
    "BAPTISM-WATER": (
        "BAPTISM-WATER LOCK: the same place in every frame — a quiet "
        "first-century immersion at a slow clear stream between low reed-lined "
        "banks, a pale worn entry slope of mud, gentle green country and low "
        "hills beyond under an open sky. The same stream, banks and slope "
        "throughout — never a modern weir, pipe, rail or building, and nothing "
        "manufactured in or by the water."
    ),
    "RISEN-DAWN": (
        "RISEN-DAWN LOCK: the same place in every frame — the mouth of a "
        "first-century rock-cut tomb in a garden at first light, a great round "
        "stone rolled back from the low dark doorway, dew on the grass, warm "
        "dawn breaking over low hills beyond. The same tomb, stone and garden "
        "throughout — never modern stonework, metal, sign or fixture, and no "
        "rendered writing anywhere."
    ),
    "PROXY": (
        "PROXY LOCK: the living believer baptized on behalf of the dead — one "
        "ordinary first-century person of middle years, a plain sun-browned "
        "face, dark hair, a simple earth-toned wool tunic (never cream — only "
        "Jesus wears cream), the same person going down into the water and "
        "rising from it. The SAME person in every baptism frame, never twinned, "
        "never a cloned face."
    ),
    "MOURNER": (
        "MOURNER LOCK: a family member remembering a departed loved one — one "
        "ordinary first-century woman of middle years, a lined gentle face, dark "
        "hair under a plain earth-toned head-cloth, sober deep-toned wool robes "
        "(never cream), grief carried with dignity and a growing hope. The SAME "
        "woman in every remembrance frame, never twinned, never a cloned face."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r171-b01", "out": "s01-pauls-question.jpeg", "seg": "n0",
        "window": "0.400-3.940", "wide": True, "jesus": False, "ref": False,
        "locks": ["CORINTH-PORTICO", "PAUL", "BACKGROUND-CAST"],
        "narration": "Some in Corinth were arguing as though resurrection might not be real.",
        "must_show": "the ONE establishing wide — the camera behind the listeners' shoulders in a Corinth portico: Paul standing among a knot of skeptical Corinthians mid-debate, some doubting, arms folded; a real argument between real people.",
        "must_not_show": "FIX THE OPEN COMPLAINT — absolutely NO scroll, NO parchment or paper with visible writing, NO curling or rolling edges, NO rendered scripture, letters, numerals or lettering of any kind, NO panel, border, frame or scroll-edge along any side of the image; no Jesus and no cream; no halo, glare or rim-light; no modern object.",
        "scene": (
            "In a pale colonnaded Corinth portico the camera stands back behind "
            "the shoulders of a small knot of listeners and looks toward Paul, a "
            "compact wiry balding man in a dark rust-brown robe, speaking with "
            "earnest fire among skeptical townsmen — one with folded arms, one "
            "shaking his head, one leaning in unsure — a real argument in a real "
            "place, the bright harbour city beyond the columns. There is nothing "
            "written or drawn anywhere in the frame and no edge or border of any "
            "kind. Every figure is an ordinary-sized person with distinct face, "
            "two hands and one head, none turned to the camera; no light rings "
            "any head."
        ),
    },
    {
        "id": "v2-r171-b02", "out": "s02-pressed-the-contradiction.jpeg", "seg": "n0",
        "window": "3.940-10.325", "wide": False, "jesus": False, "ref": False,
        "locks": ["CORINTH-PORTICO", "PAUL"],
        "narration": "Paul pointed to a practice already familiar to them and pressed the contradiction.",
        "must_show": "closer on Paul — an open-handed pressing gesture toward the listeners as he names a practice they already know; the contradiction driven home, earnest not angry.",
        "must_not_show": "no scroll, writing, lettering or panel of any kind; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "Closer in the portico light: Paul turns an open, pressing hand "
            "toward the doubters, his keen deep-set eyes steady and his pointed "
            "dark beard set, driving home a contradiction they cannot dodge — "
            "earnest fire without anger. A column stands beside him, the bright "
            "day and the strip of harbour beyond. An ordinary-sized man in "
            "rust-brown with two hands and one head, his gaze on the listeners, "
            "not the camera; nothing written anywhere, no light rings his head."
        ),
    },
    {
        "id": "v2-r171-b03", "out": "s03-baptized-for-the-dead.jpeg", "seg": "s1",
        "window": "10.325-14.610", "wide": True, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "PROXY", "MOURNER", "BACKGROUND-CAST"],
        "narration": "Else what shall they do which are baptized for the dead, if the dead rise not at all?",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the establishing wide of the practice: the camera from the bank behind the family, a living believer being baptized in the stream while a mourning family stands at the water's edge, watching in love; the ordinance done FOR the dead.",
        "must_not_show": "no corpse and no body in the water — the person baptized is a LIVING proxy; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no posed line to the lens.",
        "scene": (
            "The camera stands on the reedy bank behind a small mourning family "
            "and looks across the slow clear stream: a living believer in a plain "
            "earth-toned tunic stands waist-deep with a reverent older baptizer's "
            "hands ready at shoulder and wrist, about to go under — the ordinance "
            "carried out in love on behalf of one who has died, while the family "
            "watches from the pale entry slope. Green country and low hills stand "
            "beyond. Every figure is an ordinary-sized, distinct person with two "
            "hands and one head, none in cream and none turned to the camera; "
            "nothing written anywhere, no light rings any head."
        ),
    },
    {
        "id": "v2-r171-b04", "out": "s04-why-baptized-for-them.jpeg", "seg": "s1",
        "window": "14.610-19.862", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "MOURNER"],
        "narration": "why are they then baptized for the dead?",
        "must_show": "SCRIPTURE-EXACT — close on the mourning family member at the water's edge, watching the proxy baptism with quiet love; the question made human on her face.",
        "must_not_show": "no corpse or body; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "Close on the mourner at the edge of the stream: an ordinary "
            "middle-aged woman in a plain head-cloth and sober deep-toned robes, "
            "her lined gentle face watching the baptism in the water with a love "
            "that reaches past it — grief carried with dignity and a question "
            "held quietly in her eyes. The reeds and low hills sit soft behind. "
            "An ordinary-sized person with two hands and one head, not in cream, "
            "her gaze on the water, not the camera; nothing written anywhere, no "
            "light rings her head."
        ),
    },
    {
        "id": "v2-r171-b05", "out": "s05-the-dead-not-gone-forever.jpeg", "seg": "n1",
        "window": "19.862-25.937", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "MOURNER"],
        "narration": "The only reason to do such a thing is the quiet hope that the dead are not gone forever.",
        "must_show": "the quiet hope — the mourner's face lifting a little, a fragile hope breaking through the grief as she watches; the dead not gone forever.",
        "must_not_show": "no corpse, grave-gore or morbid imagery; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "Close in the soft daylight by the stream: the mourner's face lifts a "
            "little, the grief easing as a fragile, quiet hope breaks through — "
            "the look of someone daring to believe that the one she has lost is "
            "not gone forever. The reeds and the pale entry slope sit behind, the "
            "water bright beyond. An ordinary-sized woman with two hands and one "
            "head, not in cream, her eyes lifting past the camera in hope, not to "
            "it; nothing written anywhere, no light rings her head."
        ),
    },
    {
        "id": "v2-r171-b06", "out": "s06-new-life-a-beginning.jpeg", "seg": "n2",
        "window": "25.937-31.180", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "PROXY"],
        "narration": "Baptism stands for new life — a beginning, not an end.",
        "must_show": "the rising — the living proxy coming up out of the stream streaming, face lifted and breath drawn, made new; baptism as a beginning.",
        "must_not_show": "no corpse; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "The living believer rises straight up out of the clear stream, water "
            "streaming from face and hair and shoulders, eyes opening and a "
            "breath drawn, the baptizer's steadying hands still at the arm — "
            "baptism as new life, a beginning and not an end. Bright day glints "
            "off the running water; reeds and low hills stand beyond. An "
            "ordinary-sized person in a plain wet tunic with whole hands and one "
            "head, not in cream, face lifted to the light, not the camera; "
            "nothing written anywhere, no light rings the head."
        ),
    },
    {
        "id": "v2-r171-b07", "out": "s07-work-for-those-who-passed.jpeg", "seg": "n3",
        "window": "31.180-35.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "PROXY", "MOURNER"],
        "narration": "So the work done for those who've passed",
        "must_show": "the ordinance in love — the proxy and the mourning family together at the water afterward, the work done on behalf of a departed one; love made an act.",
        "must_not_show": "no corpse or grave-gore; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "At the edge of the stream the newly-baptized proxy, still wet, turns "
            "to the mourning woman with a quiet steadiness, the two of them close "
            "in the soft daylight — the work just done carried out in love on "
            "behalf of one who has passed, an act of hope between the living for "
            "the dead. The reeds and hills sit beyond. Ordinary-sized, distinct "
            "people with whole hands and one head each, none in cream, their eyes "
            "on each other, not the camera; nothing written anywhere, no light "
            "rings any head."
        ),
    },
    {
        "id": "v2-r171-b08", "out": "s08-death-not-the-last-word.jpeg", "seg": "n3",
        "window": "35.200-38.370", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "MOURNER"],
        "narration": "is built on one promise: that death is not the last word.",
        "must_show": "the promise held — the mourner's face lifted toward the bright open sky over the water, hope firming into conviction; death is not the last word.",
        "must_not_show": "no figure or vision in the sky — only bright natural light; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object.",
        "scene": (
            "The mourner lifts her face to the bright open sky above the stream, "
            "the fragile hope of a moment ago firming into quiet conviction — the "
            "look of someone resting her weight on a single promise, that death "
            "is not the last word. Only clean daylight is in the sky, no figure "
            "and no shape. Reeds and low hills sit soft behind. An ordinary-sized "
            "woman with two hands and one head, not in cream, her eyes lifted "
            "past the camera, not to it; nothing written anywhere, no light rings "
            "her head."
        ),
    },
    {
        "id": "v2-r171-b09", "out": "s09-christ-risen-firstfruits.jpeg", "seg": "s20",
        "window": "38.370-45.845", "wide": False, "jesus": True, "ref": True,
        "locks": ["RISEN-DAWN"],
        "narration": "But now is Christ risen from the dead, and become the firstfruits of them that slept.",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the resurrection anchor made concrete: the risen Christ standing alive and real at the mouth of the empty tomb in the dawn light, the great stone rolled back behind him; the firstfruits, risen first.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only Jesus in cream; no wound-gore; the risen Lord warm and real, NOT a ghost or a shining apparition; no scroll, writing or panel; no modern object.",
        "scene": (
            "In the first warm light of morning the risen Christ stands alive and "
            "real at the mouth of the rock-cut tomb, the great round stone rolled "
            "back from the low dark doorway behind him, dew bright on the garden "
            "grass — a warm, solid, breathing man in a plain cream robe, the "
            "first to rise, not a ghost and not a glare. The dawn breaks over low "
            "hills beyond. An ordinary-sized man with two hands and one head, his "
            "gaze calm toward the new day, not the camera; nothing written "
            "anywhere, no light rings his head."
        ),
    },
    {
        "id": "v2-r171-b10", "out": "s10-not-a-metaphor.jpeg", "seg": "n4a",
        "window": "45.845-51.163", "wide": False, "jesus": False, "ref": False,
        "locks": ["RISEN-DAWN"],
        "narration": "That is Paul's foundation — not a metaphor or a wish.",
        "must_show": "the concrete fact — a close on the empty tomb itself: the rolled-back stone and the low dark doorway with the folded grave-clothes within; a real, solid foundation, not a metaphor.",
        "must_not_show": "no body and no bones in the tomb — it is EMPTY; no scroll, writing or panel; no Jesus in this frame and no cream; no halo, glare or rim-light; no modern object.",
        "scene": (
            "A close in the dawn light on the empty tomb: the great round stone "
            "rolled aside from the low dark doorway, and within, on the stone "
            "shelf, the plain linen grave-clothes lying folded and empty — a "
            "real, solid, ordinary fact of stone and cloth, a foundation you "
            "could put your hand on, not a metaphor or a wish. Dew glints on the "
            "garden grass, the hills soft beyond. Nothing written anywhere, no "
            "body, no light rings anything — only the opened tomb and the folded "
            "cloth."
        ),
    },
    {
        "id": "v2-r171-b11", "out": "s11-the-grave-loses-its-grip.jpeg", "seg": "n4b",
        "window": "51.163-55.000", "wide": False, "jesus": True, "ref": True,
        "locks": ["RISEN-DAWN"],
        "narration": "And because He rose, the grave loses its grip —",
        "must_show": "the risen Lord in the full dawn — the risen Christ stepping out from the tomb into the morning light, alive and unbound; the grave's grip broken, shown as light and life, not opened graves.",
        "must_not_show": "NO rising corpses, NO figures climbing from graves, no gore; no halo, glare or rim-light on Jesus; only Jesus in cream; the risen Lord warm and real; no scroll, writing or panel; no modern object.",
        "scene": (
            "The risen Christ steps clear of the tomb's mouth into the full warm "
            "dawn, alive and unbound, the rolled-back stone behind him and the "
            "garden brightening around — the grip of the grave broken, shown "
            "entirely as light and a living man, never as opened graves or rising "
            "bodies. An ordinary-sized man in cream with two hands and one head, "
            "his face lifted to the morning, not the camera; nothing written "
            "anywhere, no light rings his head."
        ),
    },
    {
        "id": "v2-r171-b12", "out": "s12-for-all-who-belong.jpeg", "seg": "n4b",
        "window": "55.000-59.124", "wide": False, "jesus": False, "ref": False,
        "locks": ["RISEN-DAWN"],
        "narration": "for Him first, and then for all who belong to Him.",
        "must_show": "the hope spreading to His people — the warm dawn light reaching across the garden toward a small group of ordinary people standing in it, faces lifting in hope; His rising becoming theirs.",
        "must_not_show": "NO rising corpses or opened graves; no scroll, writing or panel; no Jesus required in this frame and no cream on the people; no halo, glare or rim-light; no modern object; no posed line to the lens.",
        "scene": (
            "The warm dawn light spreads across the garden from the opened tomb "
            "toward a small group of ordinary people standing in the morning — "
            "distinct faces of different ages lifting into the light, hope waking "
            "in them, His rising becoming the promise of their own. Low hills "
            "stand soft in the morning light beyond. Ordinary-sized, distinct people in earth-toned "
            "wool with two hands and one head each, none in cream, eyes lifted "
            "past the camera into the light, not to it; nothing written anywhere, "
            "no light rings any head."
        ),
    },
    {
        "id": "v2-r171-b13", "out": "s13-in-christ-made-alive.jpeg", "seg": "s22",
        "window": "59.124-65.489", "wide": False, "jesus": False, "ref": False,
        "locks": ["RISEN-DAWN", "MOURNER"],
        "narration": "For as in Adam all die, even so in Christ shall all be made alive.",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the turn from death to life: the mourner now standing in the risen dawn light among the hopeful people, her grief transfigured into life; all made alive in Christ.",
        "must_not_show": "no corpse, opened grave or gore; no scroll, writing or panel; no Jesus required and no cream on the people; no halo, glare or rim-light; no modern object.",
        "scene": (
            "In the risen dawn light the mourning woman stands among the hopeful "
            "people at the garden, her sober robes warm now in the morning, her "
            "lined face lifted and alive — the same grief that began at the water "
            "turned toward life, the whole scene tipping from death to living "
            "hope. The opened tomb sits soft behind, low hills beyond. "
            "Ordinary-sized, distinct people with two hands and one head each, "
            "none in cream, faces lifted into the light, not the camera; nothing "
            "written anywhere, no light rings any head."
        ),
    },
    {
        "id": "v2-r171-b14", "out": "s14-reaches-across-the-veil.jpeg", "seg": "n5a",
        "window": "65.489-69.972", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "PROXY", "MOURNER"],
        "narration": "The ordinance done in love reaches across the veil.",
        "must_show": "back at the water — the proxy and the mourner together, a soft warm light reaching beyond them as if across a distance; love made an ordinance reaching toward the departed.",
        "must_not_show": "NO ghost, spirit-figure or apparition — the veil is soft light only; no corpse or grave-gore; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object.",
        "scene": (
            "By the stream again the newly-baptized proxy and the mourning woman "
            "stand quietly together, and a soft warm light lies out across the "
            "water beyond them into a gentle distance — the ordinance done in "
            "love reaching outward, toward one who cannot be seen. No figure and "
            "no shape stands in that light; it is only light. Reeds and low hills "
            "sit soft behind. Ordinary-sized, distinct people with whole hands "
            "and one head each, none in cream, their eyes toward the far light, "
            "not the camera; nothing written anywhere, no light rings any head."
        ),
    },
    {
        "id": "v2-r171-b15", "out": "s15-every-soul-the-chance.jpeg", "seg": "n5b",
        "window": "69.972-73.427", "wide": False, "jesus": False, "ref": False,
        "locks": ["BAPTISM-WATER", "BACKGROUND-CAST"],
        "narration": "Offering every soul the chance to choose.",
        "must_show": "the invitation to all — several ordinary, distinct faces of different ages turned toward the soft light over the water, each offered the chance to choose; the door held open for every soul.",
        "must_not_show": "no ghosts or apparitions; no corpse or grave-gore; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no posed line to the lens.",
        "scene": (
            "Along the reedy bank several ordinary people of different ages stand "
            "turned toward the soft warm light lying over the water — a young "
            "man, an old woman, a worker, a child — each distinct face open and "
            "considering, every soul offered the same free chance to choose. The "
            "stream runs bright, low hills beyond. Ordinary-sized, distinct "
            "people with two hands and one head each, none in cream, their eyes "
            "toward the light, not the camera; nothing written anywhere, no light "
            "rings any head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# EMPTY BY DESIGN. All three recurring places are NEW; the runner PROMOTES each
# from this build's first good NON-Jesus frame (lesson 11 — never a Jesus frame):
#   CORINTH-PORTICO  promote b01
#   BAPTISM-WATER    promote b03
#   RISEN-DAWN       promote b10 (the empty tomb — NOT b09/b11, Jesus frames)
# Full steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# Paul's face is carried by the byte-identical text lock (no face sheet exists
# yet — same as rows 138/155/166). No image REFS.
REFS = {
}
