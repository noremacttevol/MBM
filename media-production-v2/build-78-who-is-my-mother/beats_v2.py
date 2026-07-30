#!/usr/bin/env python3
"""V2 beat map — row 78, build-78-who-is-my-mother (Mark 3:31-35).

COVERAGE: 12 pictures over 66.4 s = 5.5 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 3:31-35 KJV):
  v31   "There came then his brethren and his mother, and, STANDING
        WITHOUT, sent unto him, calling him." — they stand OUTSIDE the
        house; the message travels IN through the packed crowd.
  v32   "the multitude SAT ABOUT HIM" — a seated ring around Jesus,
        wall to wall; "Behold, thy mother and thy brethren without seek
        for thee" — the relayed words, quoted exactly.
  v33   "Who is my mother, or my brethren?" — the question nobody
        expected; teaching does not stop.
  v34   "he LOOKED ROUND ABOUT ON THEM WHICH SAT ABOUT HIM" — the slow
        circular look at ordinary seated people, then: "Behold my
        mother and my brethren!"
  v35   "whosoever shall do the will of God, the same is my brother,
        and my sister, and mother." — the circle opened, not the
        family rejected.

FRAME-STAGING: a Capernaum-house interior row — DISTINCT from row 13
(roof, paralytic lowered): here the drama is the seated RING and the
doorway relay, no roof business; compositions built on the circle and
the bright doorway.

TIME OF DAY: one bright midday throughout — hard daylight in the street
outside the door; the packed interior dim and warm, lit by the doorway
and two small windows.

CONTENT-CARE: no flags. Mary and the brothers rendered with full
dignity — concerned family, never scolds; the closing beats carry the
mercy IN the text: the circle OPENED to include, nothing pushed away.

CHANGING CONDITION (kept OUT of the locks): the message — travelling
hand to shoulder through the crowd; and the room's expectation —
certain, then overturned, then rewritten.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "HOUSE": (
        "HOUSE LOCK: a small one-room Capernaum house packed to the "
        "walls — low dark roof beams, rough plastered stone walls, two "
        "small high windows, a floor of seated listeners shoulder to "
        "shoulder, and ONE open doorway blazing with the bright street "
        "outside. The same beams, windows and doorway throughout."
    ),
    "MOTHER": (
        "MOTHER LOCK: Jesus's mother is the same woman in every shot — "
        "about fifty, a gentle worn face with warm brown eyes, dressed "
        "in a DEEP INDIGO-BLUE dress and shawl over dark hair going "
        "grey (never cream, never white). Her concern is love, not "
        "scolding; her dignity absolute."
    ),
    "BROTHERS": (
        "BROTHERS LOCK: the brothers — three grown men with dark hair "
        "and short dark beards, in plain DARK EARTH-BROWN and "
        "CHARCOAL-GREY working robes (never cream, never white), "
        "standing with the settled patience of family on an errand."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r078-b01", "out": "s01-jesus-was-inside-a-packed.jpeg", "seg": "n0",
        "window": "0.28-4.92", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "Jesus was inside a packed house, teaching, when word came in from "
            "the edge of the crowd."
        ),
        "must_show": "SCRIPTURE-EXACT: the packed house mid-teaching — Jesus at the ring's centre, the multitude SEATED about him wall to wall; at the bright doorway, a stir beginning.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the crowd SEATED in a ring (v32), not standing rows.",
        "scene": (
            "The one-room house is full to its "
            "plastered walls — a ring of seated "
            "listeners packed shoulder to shoulder "
            "under the low dark beams, every face "
            "turned inward to Jesus teaching at "
            "the circle's centre in the warm dim "
            "light — while at the blazing doorway "
            "behind them a stir starts at the "
            "crowd's edge: a head turning outward, "
            "a hand touching a shoulder, word "
            "beginning its journey in. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r078-b02", "out": "s02-his-mother-and-his-brothers.jpeg", "seg": "n1a",
        "window": "5.60-8.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["HOUSE", "MOTHER", "BROTHERS"],
        "narration": "His mother and his brothers were standing outside, asking for him.",
        "must_show": "SCRIPTURE-EXACT: STANDING WITHOUT — the mother and brothers in the bright street outside the packed doorway, asking a man at the door's edge to pass word in; they cannot get through.",
        "must_not_show": "no halo, glare or rim-light; the family's manner concerned and patient — an errand of love, not a scolding delegation.",
        "scene": (
            "In the hard bright street the family "
            "stands before the doorway they cannot "
            "enter — the mother small in her deep "
            "indigo-blue, one hand raised in quiet "
            "asking toward a man wedged at the "
            "door's packed edge, the three brothers "
            "behind her in their dark working "
            "browns, patient on the errand — the "
            "house before them so full that even "
            "his own mother must send her name in "
            "like a message in a bottle. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r078-b03", "out": "s03-the-people-sitting-around-him.jpeg", "seg": "n1b + s32",
        "window": "9.44-18.16", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "The people sitting around him passed it forward, and Mark writes "
            "down exactly what they said: Behold, thy mother and thy brethren "
            "without seek for thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the relay — the message travelling inward through the seated ring, hand to shoulder, lean to ear, from the bright doorway toward Jesus at the centre.",
        "must_not_show": "no halo, glare or rim-light; the relay VISIBLE as a chain — each link leaning to the next, the words crossing the room without anyone standing.",
        "scene": (
            "The message swims inward through the "
            "seated crowd: a chain of leaning "
            "figures from the bright doorway to "
            "the room's centre — hand on shoulder, "
            "mouth to ear, head inclining to the "
            "next — the words passing link by link "
            "over the packed floor until the last "
            "man leans toward Jesus with the "
            "family's whole errand balanced on his "
            "whisper — a room become one long ear. "
            "Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r078-b04", "out": "s04-look-your-mother-and-your.jpeg", "seg": "n1c",
        "window": "19.67-23.30", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "Look — your mother and your brothers are outside, and they're "
            "asking for you."
        ),
        "must_show": "the delivery — close on the last relayer speaking into Jesus's ear, his thumb hooked back toward the doorway; Jesus's face receiving it, calm.",
        "must_not_show": "no halo, glare or rim-light; the messenger's certainty visible — obviously expecting the teaching to stop now.",
        "scene": (
            "Close at the ring's centre: the last "
            "man in the chain leans to Jesus's ear "
            "with the message, his thumb hooking "
            "back over his own shoulder toward the "
            "blazing doorway — his face carrying "
            "the easy certainty of a man reporting "
            "the obvious, already half-shifting to "
            "clear a path — while Jesus receives "
            "the words with a stillness that has "
            "not yet decided what the room "
            "assumes it has. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r078-b05", "out": "s05-everyone-in-that-room-knew.jpeg", "seg": "n1c",
        "window": "23.30-28.96", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "Everyone in that room knew what happens next. You stop teaching, "
            "and you go out to your family."
        ),
        "must_show": "the expectation — the whole ring's faces on Jesus, several bodies already shifting to open him a lane to the door; a room certain of the next move.",
        "must_not_show": "no halo, glare or rim-light; the lane to the doorway PARTLY opened — the crowd's assumption made physical.",
        "scene": (
            "The room performs its certainty: "
            "along the packed floor a lane is "
            "already half-opening toward the "
            "bright doorway — seated bodies "
            "swaying aside, knees drawn in, a man "
            "rising to a crouch to make way — "
            "every face turned to Jesus with the "
            "settled knowledge of what a son does "
            "when his mother calls — the whole "
            "house holding the door open for a "
            "departure that is not coming. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r078-b06", "out": "s06-who-is-my-mother-or.jpeg", "seg": "j1",
        "window": "29.57-32.03", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": "Who is my mother, or my brethren?",
        "must_show": "SCRIPTURE-EXACT: the question — close on Jesus asking it, unmoved from his place at the centre; gentle, deliberate, aimed at the whole room.",
        "must_not_show": "no halo, glare or rim-light; NO harshness — the question warm and genuinely asked, not a rebuke.",
        "scene": (
            "Close on Jesus at the circle's "
            "centre, unmoved from his place: the "
            "warm brown eyes lifted to the whole "
            "room, the question leaving him "
            "gently and deliberately — not a "
            "refusal, not a rebuke, but a real "
            "question laid down in the middle of "
            "the floor for a hundred certain "
            "people to trip over — the lane to "
            "the doorway still open behind them, "
            "unused. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r078-b07", "out": "s07-nobody-expected-that.jpeg", "seg": "n2",
        "window": "33.55-34.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": "Nobody expected that.",
        "must_show": "the room's surprise — close on a cluster of seated listeners: brows up, a glance exchanged, the messenger frozen mid-shift; certainty overturned.",
        "must_not_show": "no halo, glare or rim-light; surprise, not offence — a room recalculating, leaning IN.",
        "scene": (
            "Close on a knot of seated faces in "
            "the warm dim light: brows lifted, "
            "two neighbours exchanging a sideways "
            "glance, the messenger stopped "
            "mid-shift with his helpful lane "
            "suddenly pointless — a roomful of "
            "certainty recalculating at once, and "
            "every body's lean turning not toward "
            "the door but inward, toward the "
            "question. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r078-b08", "out": "s08-then-he-looked-slowly-around.jpeg", "seg": "n2",
        "window": "34.87-46.09", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "Then he looked slowly around at the ordinary people sitting in a "
            "circle right in front of him — farmers, fishermen, mothers, a "
            "child — and answered his own question."
        ),
        "must_show": "SCRIPTURE-EXACT: the round-about look (v34) — Jesus's gaze travelling the seated ring: a sun-worn farmer, a fisherman, a mother with a child on her lap; ordinary faces receiving the look one by one.",
        "must_not_show": "no halo, glare or rim-light; the ring's ORDINARINESS the point — work-worn, plain-clothed, unremarkable people.",
        "scene": (
            "Jesus's gaze makes its slow circuit "
            "of the seated ring — passing from a "
            "sun-creased farmer with earth still "
            "on his hands, to a fisherman's "
            "salt-stiff shoulders, to a young "
            "mother in dark russet with a small "
            "child drowsing on her lap — each "
            "plain face holding the look for its "
            "moment and feeling, visibly, chosen "
            "by it — an inventory of nobodies "
            "taken with the care of a man "
            "counting family. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r078-b09", "out": "s09-behold-my-mother-and-my.jpeg", "seg": "j2",
        "window": "46.72-48.90", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": "Behold my mother and my brethren!",
        "must_show": "SCRIPTURE-EXACT: the declaration — Jesus's open hand sweeping the seated circle itself; the ring of ordinary people presented as his family.",
        "must_not_show": "no halo, glare or rim-light; the gesture INCLUDES the whole ring — no single person singled out.",
        "scene": (
            "From the centre Jesus's open hand "
            "sweeps the whole seated circle — the "
            "gesture travelling the ring like his "
            "gaze just did, presenting farmers "
            "and fishermen and drowsy children to "
            "themselves as the answer — and the "
            "faces it passes over change as it "
            "passes: startled, then warmed from "
            "within by the oldest hunger there "
            "is, the hunger to be claimed. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r078-b10", "out": "s10-for-whosoever-shall-do-the.jpeg", "seg": "j3",
        "window": "50.42-56.51", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "For whosoever shall do the will of God, the same is my brother, "
            "and my sister, and mother."
        ),
        "must_show": "SCRIPTURE-EXACT: the law of the new family — close on Jesus speaking it steadily; nearest listeners' faces receiving brother-sister-mother like an adoption read aloud.",
        "must_not_show": "no halo, glare or rim-light; WHOSOEVER carried in the delivery — a door thrown open, not a bar raised.",
        "scene": (
            "Close on Jesus speaking the terms "
            "steadily, like a man reading an "
            "adoption deed aloud — brother, and "
            "sister, and mother — and on the "
            "nearest faces in the warm dim light "
            "the words land one by one: the "
            "farmer hearing brother, the young "
            "mother hearing sister, an old woman "
            "by the wall hearing mother and "
            "pressing her hand to her own collar "
            "— WHOSOEVER, flung wide as the "
            "doorway's light. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r078-b11", "out": "s11-he-pushing-his-family-away.jpeg", "seg": "n3",
        "window": "58.02-59.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["MOTHER", "BROTHERS"],
        "narration": "He wasn't pushing his family away.",
        "must_show": "the family honoured — outside in the bright street: the mother's face gentle and unwounded, listening at the doorway's edge; nothing rejected in her.",
        "must_not_show": "no halo, glare or rim-light; NO hurt or offence on the mother — her dignity and his love both intact.",
        "scene": (
            "Outside in the hard bright street the "
            "mother stands near the doorway's "
            "edge, her indigo shawl still, her "
            "worn gentle face tilted toward the "
            "voice carrying out over the packed "
            "heads — and what the light finds "
            "there is not a wound: the small "
            "beginning of a smile of a woman who "
            "has known since Nazareth that this "
            "son belongs to more than one house, "
            "the brothers quiet behind her. Every "
            "figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r078-b12", "out": "s12-he-was-opening-the-circle.jpeg", "seg": "n3",
        "window": "59.68-66.10", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": (
            "He was opening the circle — telling a room full of nobodies they "
            "could belong to him like blood."
        ),
        "must_show": "the closing image — the whole ring wide: Jesus at the centre of the seated circle of ordinary people, the composition itself one unbroken ring; belonging made visible.",
        "must_not_show": "no halo, glare or rim-light; the circle UNBROKEN and complete — nobody outside its line inside the room, the doorway's light falling in on family.",
        "scene": (
            "The closing frame holds the whole "
            "room as one shape: the unbroken ring "
            "of seated ordinary people — farmers, "
            "fishermen, mothers, the drowsing "
            "child — with Jesus at its centre in "
            "the warm dim light, the bright "
            "doorway pouring its daylight across "
            "the circle's edge like a welcome "
            "left permanently open — a room full "
            "of nobodies, sitting inside the word "
            "family as if it had been built "
            "around them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
]
