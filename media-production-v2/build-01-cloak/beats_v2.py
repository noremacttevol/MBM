#!/usr/bin/env python3
"""V2 beat map — row 1, build-01-cloak (Mark 5:25-34).

Consumed by media-production-v2/v2_prompt.py, which prepends STYLE-V2, the
forced-wide defense line, the anti-panel clause and JESUS LOCK v4 so those blocks
are byte-identical in every prompt by construction.

COVERAGE (STORY-COVERAGE-LAW): 20 pictures, against V1's 11. The two that V1 most
clearly missed:
  * w28 — her ONE spoken line in the whole chapter shared V1's s4 with n3a. It gets
    its own frame here (b08).
  * "reached out to touch the edge of his cloak" — V1 covered pressing through the
    crowd AND the touch on one still. The touch is the hinge of the story; it gets
    its own frame (b11).

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 5:21-34 KJV):
  v21  he is beside the sea, much people gathered — a lakeside town, daytime.
  v22  Jairus, a ruler of the synagogue, falls at his feet and begs for his daughter.
  v25-26  twelve years; suffered many things of many physicians; spent all she had;
          nothing bettered, but rather grew worse.
  v27  she came IN THE PRESS BEHIND and touched his garment — she approaches from
       BEHIND him, never face-on. Every reaching shot obeys this.
  v29  she felt in her body that she was healed.
  v30  he turned him about in the press.
  v31  the disciples push back.
  v32  he looked round about to see her.
  v33  she came FEARING AND TREMBLING and FELL DOWN BEFORE HIM.
  v34  Daughter, thy faith hath made thee whole; go in peace.

CONTENT-CARE: row 1 is not in the §3 flag table = GREEN. Even so, her illness is an
issue of blood: it is carried entirely by her face, her frailty and the way people
step away from her. No blood, no medical detail, nothing of her body exposed.
"""

# ---- locks local to this video (byte-identical everywhere they appear) ----
LOCKS = {
    "WOMAN": (
        "WOMAN LOCK: the same woman in every shot of this video — a Middle Eastern "
        "woman of about forty, thin and hollowed by twelve years of illness, high "
        "cheekbones, deep-set dark brown eyes, dark brown hair pulled back under a "
        "faded DUST-ROSE head cloth, a patched ash-grey-brown wool tunic and a darker "
        "charcoal-brown mantle, worn leather sandals, modestly covered from neck to "
        "ankle (she never wears cream). Her face is shown clearly."
    ),
    "JAIRUS": (
        "JAIRUS LOCK: Jairus is the same man in every shot — a synagogue ruler of "
        "about fifty, well-kept, a greying dark beard trimmed square, a deep "
        "INDIGO-BLUE robe with a woven border and a dark blue head covering (never "
        "cream). His face is shown clearly."
    ),
    # SETTING LOCK v3 (2026-07-28). Two failures produced this wording:
    #   v1 said the crowd wore "earth-toned wool" and trusted the sentence "no one
    #   but Jesus in cream" to do the separating. The model read the whole street as
    #   one pale sand palette and dressed the CROWD in cream, so the one man who may
    #   wear cream did not read as different from anybody (s05, HARD FAIL).
    #   v2 fixed the colours but NAMED Jesus inside the setting description — and the
    #   model duly painted him into b03, a beat that happens seven seconds before the
    #   narration introduces him, standing in the background in cream (s03, story
    #   accuracy FAIL).
    # A setting lock describes the STREET and the VILLAGERS. It must never name a
    # character, because naming one puts him in the frame. The cream contrast is
    # carried by JESUS LOCK v4's own "(only he wears cream)", which is present in
    # exactly the shots he belongs in.
    "SETTING": (
        "SETTING LOCK: a crowded lakeside town street in Galilee — pale dressed "
        "limestone walls, packed dust underfoot, the Sea of Galilee showing in gaps "
        "between the buildings, bright honest midday light and hard clean shadows. "
        "The villagers are a dense press of ordinary Galileans dressed in SATURATED, "
        "DEEP, DARK earth colours — dark chocolate brown, deep russet red, burnt "
        "ochre, dark olive green, and dusty indigo blue wool. Every villager is "
        "clearly DARKER in tone than pale cream: no villager wears cream, off-white, "
        "oatmeal, ivory, sand or any pale near-white cloth."
    ),
}

REF = True  # every Jesus shot attaches JESUS-V2-REF/jesus-v2-face.jpeg

# Reviewer-only realistic replacement. The approved app/V1 media remains untouched.
OUTPUT_ASSET_DIR = "assets-realistic-v3"
OUTPUT_VIDEO_NAME = "mark-5_woman-touches-his-cloak-realistic-v3.mp4"

BEATS = [
    {
        "id": "v2-r001-b01", "out": "s01-twelve-years.jpeg", "seg": "n1",
        "window": "0.00-4.33", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "There was a woman who had been suffering for twelve years.",
        "must_show": "one woman, alone, worn down by long illness; nobody else.",
        "must_not_show": "no blood, no medical detail, no crowd, no Jesus yet.",
        "scene": (
            "She sits alone in the corner of a plain bare stone room, thin shoulders "
            "bowed, one hand pressed to her side in long-worn weariness, a folded "
            "blanket and an empty clay cup on the floor beside her. Soft grey daylight "
            "falls from one small high window; the rest of the room is dim and quiet. "
            "Her tired face carries twelve long years. Exactly one person is in the "
            "frame, with two arms, two hands of five fingers each, two legs, two feet "
            "and one head."
        ),
    },
    {
        "id": "v2-r001-b02", "out": "s02-physicians.jpeg", "seg": "n2 p1",
        "window": "4.33-7.68", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "She had spent everything on doctors. Nothing helped.",
        "must_show": "money leaving her hands to physicians; she is no better.",
        "must_not_show": "no examination, no blood, no exposed body, no modern medicine.",
        "scene": (
            "Standing in a physician's dim stone room, she holds out an open worn "
            "leather purse in both thin hands, the last small coins going from her palm "
            "into the hand of (1) an older physician in a dark olive-brown robe, while "
            "(2) a second physician in a muted ochre robe turns away to a shelf of small "
            "clay medicine jars, already finished with her. Her head is bowed and her "
            "face is drained. Exactly three people are in the frame; each has two arms, "
            "two hands of five fingers each, two legs and one head."
        ),
    },
    {
        "id": "v2-r001-b03", "out": "s03-untouchable.jpeg", "seg": "n2 p2",
        "window": "7.68-15.11", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "SETTING"],
        "narration": ("She was exhausted, desperate — and by the rules of her time, "
                      "considered untouchable."),
        "must_show": "people deliberately drawing away from her in the street; her isolation.",
        "must_not_show": "no cruelty or jeering, no blood, no shaming gestures.",
        "scene": (
            "She walks alone down the middle of the sunlit street, and the villagers on "
            "both sides step back from her and pull their children in close, leaving a "
            "clear empty gap of dust all around her. Nobody touches her and nobody meets "
            "her eyes; their faces are wary rather than cruel. She is the clear focus in "
            "the centre of the frame, small inside that empty space, exhausted. Everyone "
            "in this frame is an ordinary villager. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r001-b04", "out": "s04-jairus-urging.jpeg", "seg": "n2b p1",
        "window": "15.11-22.39", "wide": True, "jesus": True, "ref": REF,
        "locks": ["JAIRUS", "SETTING"],
        "narration": ("That day, Jesus was already on his way to save someone else — a "
                      "ruler's daughter, twelve years old, and dying."),
        "must_show": "Jairus urgently leading Jesus somewhere; both moving with purpose.",
        "must_not_show": "the sick girl is not in this frame; no woman with the issue yet.",
        "scene": (
            "Jesus strides through the crowded street with purpose, and Jairus walks "
            "half a step ahead of him, turned back toward him, one hand outstretched to "
            "urge him on, his face tight with a father's fear. Villagers give way around "
            "them. Both men are shown full-length and in motion, walking the same "
            "direction together. Bright midday light on pale stone. Exactly two men are "
            "in the foreground; each has two arms, two hands of five fingers each, two "
            "legs and one head."
        ),
    },
    {
        "id": "v2-r001-b05", "out": "s05-crowd-pressing.jpeg", "seg": "n2b p2",
        "window": "22.39-25.10", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SETTING"],
        "narration": "The crowd pressed around him on every side.",
        "must_show": "a dense crowd closing in on Jesus from all directions, gazes on him.",
        "must_not_show": "no violence; nobody detached at the frame edge; Jesus not small or lost.",
        "scene": (
            "The crowd closes around Jesus from every direction at once — villagers "
            "reaching toward him, calling to him, shoulders and arms pressing in on all "
            "sides. He is at the centre of the frame at natural human scale among them, "
            "and every face in the crowd is visibly turned toward him. Bright midday "
            "light, dust hanging in the air. Every figure has two arms, two hands and "
            "one head, and all of them stand on the same street at the same scale."
        ),
    },
    {
        "id": "v2-r001-b06", "out": "s06-woman-at-edge.jpeg", "seg": "n2b p3",
        "window": "25.10-29.84", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SETTING"],
        "narration": "Almost no one would have noticed one more sick woman at its edge.",
        "must_show": "her at the outer edge of the crowd, unnoticed; Jesus deep in the press beyond.",
        "must_not_show": "nobody is looking at her; she does not reach yet.",
        "scene": (
            "At the outer edge of the packed crowd the woman stands alone against a "
            "limestone wall, half hidden behind the backs and shoulders of villagers who "
            "are all facing away from her toward Jesus, who is further off deep inside "
            "the press. Not one person has noticed her. She is small in the frame but in "
            "sharp focus, her eyes fixed on the crowd ahead. Bright midday light. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r001-b07", "out": "s07-she-hears.jpeg", "seg": "n3a",
        "window": "29.84-38.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("She heard Jesus was nearby. She did not ask permission. She did "
                      "not make a speech. She said only one thing, and she said it to "
                      "herself."),
        "must_show": "the moment the news reaches her — her head lifting, hope arriving.",
        "must_not_show": "she is not moving yet; no crowd detail, no Jesus.",
        "scene": (
            "Close on the woman standing in the shade of a doorway, her head lifting and "
            "turning toward a sound off to one side, eyes widening as the news reaches "
            "her — the first hope in twelve years breaking across a tired face. Her hand "
            "tightens on the edge of her charcoal-brown mantle. Bright street light "
            "falls across her face from the side. Exactly one person is in the frame, "
            "with two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r001-b08", "out": "s08-she-says-it.jpeg", "seg": "w28",
        "window": "38.66-42.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": "If I may touch but his clothes, I shall be whole.",
        "must_show": "her own words, spoken to herself — resolve settling on her face.",
        "must_not_show": "she speaks to no one; nobody else in frame; no Jesus.",
        "scene": (
            "A tight portrait of the woman alone in the crowd's shadow, lips just parted "
            "as she says it under her breath to herself, eyes lowered and fixed on "
            "nothing, her whole face gathering into resolve. Her hands are drawn "
            "together against her chest. Bright midday light rakes across one side of "
            "her face. Exactly one person is in the frame, with two arms, two hands of "
            "five fingers each and one head."
        ),
    },
    {
        "id": "v2-r001-b09", "out": "s09-her-plan.jpeg", "seg": "n3b p1",
        "window": "42.82-49.46", "wide": True, "jesus": False, "ref": False,
        "locks": ["WOMAN", "SETTING"],
        "narration": ("If I can just touch his clothes, she told herself, I will be "
                      "well. That was the whole of her plan."),
        "must_show": "she commits — steps off the wall and into the outer crowd.",
        "must_not_show": "she has not reached Jesus; he is not in this frame.",
        "scene": (
            "The woman pushes off the limestone wall and takes her first step into the "
            "outer ring of the crowd, drawing her dust-rose head cloth close around her "
            "face with one hand so she will not be recognised, quiet determination "
            "replacing hesitation. The villagers around her are all facing away toward "
            "something ahead and none of them notice her. Everyone in this frame is an "
            "ordinary villager. Bright midday light on pale "
            "stone. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r001-b10", "out": "s10-pressing-through.jpeg", "seg": "n3b p2",
        "window": "49.46-51.00", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SETTING"],
        "narration": "She pressed through the crowd",
        "must_show": "her forcing her way forward between bodies, Jesus's back ahead of her.",
        "must_not_show": "she is BEHIND him (v27) — never approaching him face-on; she has not touched him yet.",
        "scene": (
            "Low and close among the bodies, the woman forces her way forward between "
            "the shoulders and backs of the crowd, one arm raised to shield her face, "
            "her eyes locked ahead on Jesus, who is several steps in front of her seen "
            "from BEHIND, walking away from her through the press. She is nearly through "
            "but has not reached him and touches nothing yet. Bright midday light, dust "
            "in the air. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r001-b11", "out": "s11-touches-hem.jpeg", "seg": "n3b p3",
        "window": "51.00-53.96", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SETTING"],
        "narration": "and reached out to touch the edge of his cloak.",
        "must_show": ("the hinge of the story: her fingertips just grazing the very "
                      "bottom hem of his robe, from behind, near his ankles."),
        "must_not_show": ("no gripping, clutching, pulling or bunching of the cloth; he "
                          "has not turned yet; she is behind him."),
        "scene": (
            "The woman has sunk low behind Jesus and stretches one thin trembling arm "
            "out to his robe. HOW SHE TOUCHES IT: only the tips of two or three "
            "outstretched fingers barely graze the tasselled fringe at the very bottom "
            "hem of his robe, down near his ankles; her hand is open and her fingers are "
            "extended, the lightest and most reverent possible contact, and the cloth "
            "hangs straight and undisturbed. Jesus is a step ahead of her seen from "
            "behind and to the side, still walking, not yet turned toward her. Villagers "
            "press past on both sides, unaware. Bright midday light. Every figure has "
            "two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r001-b12", "out": "s12-he-stops.jpeg", "seg": "n4a p1",
        "window": "53.96-58.03", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SETTING"],
        "narration": "He stopped. He had felt it — power had gone out of him.",
        "must_show": "Jesus halted mid-stride while the crowd keeps moving around him.",
        "must_not_show": "no halo, glow or rim-light; he has not turned around yet.",
        "scene": (
            "Jesus has stopped dead in the middle of the moving street, one foot still "
            "forward from the stride he broke off, his head lifting and his face alert "
            "and moved, one hand opening slightly at his side as he feels that power has "
            "gone out of him. The crowd around him is still flowing past, blurred with "
            "motion, and he is the one still point in the frame. Bright midday light on "
            "pale stone. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r001-b13", "out": "s13-healed-in-her-body.jpeg", "seg": "n4a p2",
        "window": "58.03-62.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("The healing was already hers, given the moment she touched him."),
        "must_show": "she feels in her body that she is healed — the change on her face.",
        "must_not_show": "no blood, no light effect, no glow on her body, no medical detail.",
        "scene": (
            "Close on the woman low in the crowd, her outstretched hand still open in "
            "the air where the cloth was, her other hand pressed flat to her side — and "
            "her face changing, twelve years of pain going out of it, breath caught "
            "between disbelief and knowing. The change is entirely in her face and "
            "posture, with no light or effect anywhere on her body. Bright midday light. "
            "Exactly one person is in sharp focus in the frame, with two arms, two hands "
            "of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r001-b14", "out": "s14-who-touched.jpeg", "seg": "j0",
        "window": "62.17-64.73", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SETTING"],
        "narration": "Who touched my clothes?",
        "must_show": "he has turned about in the press and is asking the crowd.",
        "must_not_show": "not angry — searching and gentle; no halo or glow.",
        "scene": (
            "Jesus has turned all the way about in the press and looks back over the "
            "crowd behind him, asking who touched him, his face shown clearly and his "
            "expression searching and gentle rather than angry. The villagers nearest "
            "him glance at one another, puzzled, their faces turned toward him. Bright "
            "midday light on pale stone. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r001-b15", "out": "s15-disciples-protest.jpeg", "seg": "s31 + n4c p1",
        "window": "64.73-77.21", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "JOHN", "ANDREW", "SETTING"],
        "narration": ("Thou seest the multitude thronging thee, and sayest thou, Who "
                      "touched me? / His disciples thought the question made no sense. "
                      "The whole crowd was pressing against him — who hadn't touched him?"),
        "must_show": "the disciples gesturing at the packed crowd, honestly baffled. Jesus's EYES natural and correct: both eyes open, symmetrical, aligned on the same point in the crowd, natural warm brown — inspect them at full resolution before accepting.",
        "must_not_show": "no mockery or disrespect; nobody but Jesus in cream. CAMERON GATE (open complaint at 1:10): NO weird eyes on Jesus — no wall-eye, cross-eye, mismatched pupils, dead stare, or misaligned gaze; if his eyes read wrong at a glance the frame fails.",
        "scene": (
            "Peter stands at Jesus's shoulder with both arms opened wide toward the "
            "packed crowd in honest exasperated puzzlement — the whole street is "
            "touching him, how can he ask who? — while Andrew beside him turns a "
            "questioning look on Jesus and John looks from the crowd back to Jesus's "
            "face. Jesus stands calm and unmoved among them, still scanning the people. "
            "Bright midday light on pale stone. Exactly four men are in the foreground "
            "with the crowd behind them; every figure has two arms, two hands of five "
            "fingers each and one head."
        ),
    },
    {
        "id": "v2-r001-b16", "out": "s16-searching.jpeg", "seg": "n4c p2",
        "window": "77.21-82.47", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SETTING"],
        "narration": ("He ignored them. He was already needed somewhere else, and he "
                      "stopped anyway."),
        "must_show": "he looks round about to see her (v32) — searching face by face.",
        "must_not_show": "he has not found her yet; no impatience.",
        "scene": (
            "Jesus stands still in the middle of the street and looks slowly round about "
            "over the heads of the crowd, searching face after face for the one person "
            "who touched him, patient and entirely unhurried, ignoring the men at his "
            "shoulder. The crowd around him has begun to quiet and turn toward him. "
            "Bright midday light on pale stone. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r001-b17", "out": "s17-found-her.jpeg", "seg": "n4b",
        "window": "82.47-84.91", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SETTING"],
        "narration": "He looked for her until he found her.",
        "must_show": ("the moment their eyes meet across the crowd — she is found; she "
                      "comes fearing and trembling (v33)."),
        "must_not_show": "no fear of punishment on his face; he is warm, not stern.",
        "scene": (
            "Across a gap that has opened in the crowd, Jesus's searching gaze has "
            "landed on the woman and stopped, and her eyes have met his — she is caught "
            "and known. She has half risen from where she crouched, trembling, her "
            "dust-rose head cloth slipping back from her face; his face is turned "
            "directly to her and is full of gentle warmth, not anger. The villagers "
            "between them have drawn back on both sides so the line between his eyes and "
            "hers is clear and unbroken. Bright midday light. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r001-b18", "out": "s18-daughter.jpeg", "seg": "j1",
        "window": "84.91-91.53", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SETTING"],
        "narration": ("Daughter, thy faith hath made thee whole; go in peace, and be "
                      "whole of thy plague."),
        "must_show": ("she has fallen down before him (v33) and he speaks to her; the "
                      "crowd's attention on the two of them."),
        "must_not_show": "no halo, glow or rim-light; nobody else in cream; he is not looming over her.",
        "scene": (
            "The woman has fallen to her knees on the pale stone before Jesus, her face "
            "turned up to him, and he has crouched down low to meet her at her own "
            "level, speaking to her, one hand open toward her and his other hand resting "
            "on his knee. His face is shown clearly and is full of warmth. The crowd "
            "stands back in a ring around them, faces turned toward the two of them, "
            "quiet. Bright midday light on pale stone. Exactly two people are at the "
            "centre of the frame; every figure has two arms, two hands of five fingers "
            "each and one head."
        ),
    },
    {
        "id": "v2-r001-b19", "out": "s19-it-lands.jpeg", "seg": "n5 p1",
        "window": "91.53-96.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["WOMAN"],
        "narration": ("Be whole of thy plague — be free of what has been hurting you. "
                      "Twelve years of it."),
        "must_show": "the word landing on her face — relief breaking through.",
        "must_not_show": "no light effect on her; she is not yet standing.",
        "scene": (
            "A close portrait of the woman still on her knees, looking up, tears "
            "standing in her eyes without running, her mouth open slightly as twelve "
            "years let go of her all at once and her whole face loosens into relief. "
            "Bright midday light falls full on her face. Exactly one person is in sharp "
            "focus in the frame, with two arms, two hands of five fingers each and one "
            "head."
        ),
    },
    {
        "id": "v2-r001-b20", "out": "s20-goes-in-peace.jpeg", "seg": "n5 p2",
        "window": "96.76-101.11", "wide": True, "jesus": True, "ref": REF,
        "locks": ["WOMAN", "SETTING"],
        "narration": ("Over, in a sentence. And the first word he chose was daughter."),
        "must_show": "she goes in peace — upright, whole, walking away; he watches her go.",
        "must_not_show": "no sickness left in her posture; no crowd shunning her now.",
        "scene": (
            # "head uncovered" was in the first draft and CONTRADICTED the WOMAN LOCK,
            # which gives her a dust-rose head cloth in every shot. The model obeyed the
            # lock and ignored the scene text — the right call — but a prompt must never
            # argue with its own lock, so the scene text was corrected to match.
            "The woman walks away up the sunlit street with her back straight and her "
            "head lifted, strong and unhurried, her face calm — and behind "
            "her Jesus stands watching her go, his face shown clearly and kind. The "
            "villagers on both sides no longer step away from her; several watch her "
            "pass. Bright midday light on pale stone, long clean shadows. Every figure "
            "has two arms, two hands of five fingers each, two legs and one head."
        ),
    },
]
