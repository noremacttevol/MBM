#!/usr/bin/env python3
"""V2 beat map — row 57, build-57-jairus-daughter (Mark 5:22-24, 35-43).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 27 pictures over 156.7 s narration = 5.8 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 5 KJV; this narration skips
the vv.25-34 interlude):
  v22  JAIRUS, ONE OF THE RULERS OF THE SYNAGOGUE — a man of standing — SAW
       him, and FELL AT HIS FEET: public self-abasement by a dignitary.
  v23  "My little daughter lieth at the point of death: I pray thee, come
       and lay thy hands on her, that she may be healed; and she shall
       live." (s23) Luke 8:42: his ONLY daughter, about TWELVE.
  v24  Jesus WENT WITH HIM; much people FOLLOWED and THRONGED him.
  v35  messengers from the house: "Thy daughter is dead: why troublest thou
       the Master any further?" (s35)
  v36  AS SOON AS Jesus heard the word spoken — he answers BEFORE Jairus
       can speak — "Be not afraid, only believe." (jv36)
  v37  he suffered no man to follow, save PETER, JAMES and JOHN.
  v38  at the house: a TUMULT — they WEPT and WAILED GREATLY (hired
       mourners' loud grief).
  v39  "Why make ye this ado, and weep? the damsel is not dead, but
       sleepeth." v40: they LAUGHED HIM TO SCORN. He PUT THEM ALL OUT,
       took the FATHER and MOTHER and the three, and entered in where the
       damsel was lying.
  v41  he TOOK THE DAMSEL BY THE HAND: "TALITHA CUMI" — his own everyday
       Aramaic — "Damsel, I say unto thee, arise."
  v42  STRAIGHTWAY the damsel AROSE, and WALKED; she was TWELVE years old.
  v43  he charged them straitly, and commanded that SOMETHING SHOULD BE
       GIVEN HER TO EAT — the tender ordinary ending; the build closes
       there.

CONTENT-CARE — FLAG G, THE GRIEF-CARE LAW (§3 table: "Jairus's dead
daughter — grief-care card; 'fear not, only believe'"): the child is shown
the way scripture shows it — the small SLEEPING FORM, the parents' faces —
NEVER anything a bereaved parent could not bear to see. No pallor played
for horror, no death imagery beyond stillness. The raising reveals who God
is toward the grieving; nothing in the frames may read as a promised refund
of the same miracle today.

CHARACTER CONSISTENCY ACROSS ROWS: Peter (Simon), James and John carry the
SAME descriptions as rows 51/53 so the same men read across the library.

TIME-OF-DAY ARC: one afternoon — bright crowded afternoon at the shore road,
hurrying light on the way, the house reached late afternoon; the child's
room shuttered and dim; the closing meal in warm early-evening lamp-and-window
light.

CAST-REF NOTE: when the first still with Jairus's face is ACCEPTED at QC,
copy it to CAST-REF-V2/jairus-ref.jpeg and add
"char_refs": ["CAST-REF-V2/jairus-ref.jpeg"] to every later legible-face
beat. Same for the girl (girl-ref.jpeg: b19b-b27) and the mother
(mother-ref.jpeg). Text locks alone do not hold a face.
"""

LOCKS = {
    "JAIRUS": (
        "JAIRUS LOCK: Jairus is the same man in every shot — about "
        "forty-five, a synagogue ruler's dignity in his bearing even when "
        "it is breaking, olive skin, neat dark beard going grey at the "
        "chin, short dark hair under a DARK WINE-BROWN head covering. He "
        "wears a fine DEEP WINE-BROWN wool robe with a DARK INDIGO woven "
        "border and a wide dark sash — a dignitary's clothing, plainly "
        "darker than sunlit stone, never cream, never white. His face is "
        "shown clearly."
    ),
    # She is raised at v42; the lock fixes face and build, each beat states
    # her condition (still form -> eyes open -> walking -> eating).
    "GIRL": (
        "GIRL LOCK: the daughter is the same child in every shot — twelve "
        "years old, small and fine-boned, her father's olive skin, long "
        "dark wavy hair loose around her face. On the bed she lies in a "
        "plain DARK MADDER-ROSE wool shift under a DARK OLIVE-BROWN "
        "blanket, her face still and peaceful as deep sleep; nothing on "
        "or around her is cream, off-white or any pale near-white cloth. "
        "Her face is shown clearly."
    ),
    "MOTHER": (
        "MOTHER LOCK: the girl's mother is the same woman in every shot — "
        "about thirty-eight, dark hair bound under a DUSTY DARK INDIGO "
        "head covering, a fine-featured face worn transparent by days of "
        "fear. She wears a DEEP RUSSET wool dress with a dark shawl; "
        "never cream, never white. Her face is shown clearly."
    ),
    "THREE": (
        "THE THREE LOCK: Peter, James and John are the same three men in "
        "every shot — Peter about thirty-five, thick-set and powerful, "
        "dark curly hair, full dark beard, in a coarse DARK CHARCOAL-BROWN "
        "wool tunic; James about thirty, square-built with a full dark "
        "beard and heavy forearms, in a DEEP RUSSET-BROWN wool tunic; "
        "John about twenty, the youngest, clean-jawed with only the first "
        "shadow of a beard, dark hair to the ears, in a DUSTY DARK INDIGO "
        "wool tunic. Plain leather belts; none of them wears cream, "
        "off-white or any pale near-white cloth."
    ),
    "HOUSE": (
        "HOUSE LOCK: Jairus's house — a synagogue ruler's fine limestone "
        "house with a walled courtyard and heavy wooden door, patterned "
        "wool hangings in deep madder and indigo, bronze oil lamps, a "
        "small shuttered sleeping room off the court where the child "
        "lies. The household and the hired mourners wear SATURATED DEEP "
        "earth colours — dark browns, deep russet, burnt ochre, dark "
        "olive, dusty indigo, the mourners in the darkest greys and "
        "charcoals; no one in the house wears cream, off-white, ivory or "
        "any pale near-white cloth."
    ),
    "ROAD": (
        "ROAD LOCK: the shore road of Capernaum and the lanes to Jairus's "
        "house, packed with an afternoon crowd of ordinary Galileans in "
        "SATURATED DEEP earth colours — dark chocolate brown, deep "
        "russet, burnt ochre, dark olive and dusty indigo wool; no one "
        "in the crowd wears cream, off-white or any pale near-white "
        "cloth."
    ),
}

REF = True

# Identity law: THREE = Peter, James and John — pin the global sheets
# (token names never auto-attach; the Lazarus trap).
REFS = {
    "THREE": ["../CAST-V2-REF/peter-front.jpeg", "../CAST-V2-REF/james-z-front.jpeg", "../CAST-V2-REF/john-front.jpeg"],
}

BEATS = [
    {
        "id": "v2-r057-b01", "out": "s01-jairus-fell-at-his-feet.jpeg", "seg": "n1 p1",
        "window": "0.28-7.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["JAIRUS", "ROAD"],
        "narration": ("A man named Jairus, a leader of the synagogue, "
                      "pushed through the crowd and fell down at Jesus' "
                      "feet, and begged him:"),
        "must_show": "v22 — the dignitary DOWN in the road dust at Jesus's feet, fine robes and all; the crowd's shock at seeing him there.",
        "must_not_show": "no halo/glow; the crowd parts around the fallen ruler — everyone knows who this man is.",
        "scene": (
            "In the thronged afternoon road, the camera at the crowd's "
            "edge taking the fall in profile, the fine-robed synagogue "
            "ruler has thrown himself down at Jesus's feet — knees in "
            "the dust, his wine-brown robe pooled around him, his "
            "hands gripping toward Jesus's ankles — while the packed "
            "crowd pulls back in a ring of astonishment at the sight "
            "of the town's most dignified man face-down in the road, "
            "and Jesus is already bending toward him. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b02", "out": "s02-my-little-daughter.jpeg", "seg": "s23 p1a",
        "window": "7.28-11.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAIRUS"],
        "narration": ("My little daughter lieth at the point of death: "
                      "(Mark 5:23)"),
        "must_show": "the plea's face — close on Jairus looking up from the dust, a ruler's composure gone, only the father left.",
        "must_not_show": "no performance in it — raw, cracked, specific.",
        "scene": (
            "A tight shot of Jairus's upturned face from above: the "
            "neat greying beard and fine head covering of a man of "
            "standing, and beneath them a face cracked wide open — "
            "eyes flooded, brow buckled, lips shaking through the "
            "words — every year of dignity spent in one sentence "
            "about a twelve-year-old girl. Exactly one person is in "
            "the frame, with one head."
        ),
    },
    {
        "id": "v2-r057-b03", "out": "s03-lay-thy-hands-on-her.jpeg", "seg": "s23 p1b",
        "window": "11.50-17.21", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JAIRUS"],
        "narration": ("I pray thee, come and lay thy hands on her, that "
                      "she may be healed; and she shall live. (Mark 5:23)"),
        "must_show": "the ask with its faith — Jairus's hands lifted clasped toward Jesus; Jesus bent low over him, hand reaching to raise him.",
        "must_not_show": "Jesus is already answering with his body — the reach down begins before any word.",
        "scene": (
            "Jairus kneels with both hands lifted and clasped toward "
            "Jesus, the whole sentence of his faith in the gesture — "
            "and Jesus has bent low over him, one hand already "
            "closing around the ruler's clasped hands, the other "
            "coming to his shoulder, lifting the man up out of the "
            "dust as the plea is still leaving his mouth. Afternoon "
            "sun. Exactly two people are in the frame; each visible "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r057-b04", "out": "s04-only-a-father.jpeg", "seg": "n1b p1-p2",
        "window": "17.21-23.45", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JAIRUS"],
        "narration": ("My little girl is dying, he said. Please come and "
                      "lay your hands on her, so she'll be healed and "
                      "live."),
        "must_show": "the two faces close — the father emptied of rank, Jesus's full attention already given.",
        "must_not_show": "no crowd detail in this frame — it narrows to the two men.",
        "scene": (
            "A close two-shot, the crowd blurred away: Jairus on his "
            "feet now but bent toward Jesus, gripping the front of "
            "his own robe with one fist, saying it again the plain "
            "way — and Jesus's face close before his, still and "
            "wholly given over, a man who has already decided and is "
            "simply letting the father finish. Exactly two people "
            "are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r057-b05", "out": "s05-slipping-away-at-home.jpeg", "seg": "n1b p3",
        "window": "23.45-29.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["GIRL", "MOTHER", "HOUSE"],
        "narration": ("His only daughter, twelve years old, slipping away "
                      "at home while he stood in the road begging."),
        "must_show": "meanwhile — the shuttered room: the small girl fever-flushed and shallow-breathing in the bed, her mother keeping the vigil.",
        "must_not_show": "G-law: she is gravely ill, never corpse-like here — she still breathes; the mother's face carries the danger.",
        "scene": (
            "In the shuttered dim of the small sleeping room the girl "
            "lies under the dark olive-brown blanket, her small face "
            "fever-flushed and damp among her loose dark hair, breath coming "
            "shallow — and her mother kneels against the bed with her "
            "daughter's limp hand pressed to her own mouth, eyes "
            "closed, rocking almost imperceptibly, a woman bargaining "
            "silently with heaven. One line of afternoon light "
            "through the shutter. Exactly two people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b06", "out": "s06-jesus-went-with-him.jpeg", "seg": "n2 p1",
        "window": "29.42-31.15", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JAIRUS", "ROAD"],
        "narration": "So Jesus went with him.",
        "must_show": "v24 — the setting out: the two men striding off together, the crowd wheeling to follow.",
        "must_not_show": "no hesitation anywhere in Jesus's stride.",
        "scene": (
            "Jesus and Jairus stride off down the road side by side — "
            "the ruler half a step ahead, urgent, one arm pointing the "
            "way through the lanes, Jesus matching his pace exactly — "
            "while behind them the whole afternoon crowd wheels and "
            "surges to follow, the road narrowing ahead of them into "
            "the town. Every figure has two arms, two legs and one "
            "head."
        ),
    },
    {
        "id": "v2-r057-b07", "out": "s07-the-crowd-pressed-in.jpeg", "seg": "n2 p2",
        "window": "31.15-40.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["JAIRUS", "ROAD"],
        "narration": ("A great crowd pressed in on every side as they "
                      "hurried toward the house, the desperate father "
                      "leading the way, praying there was still time."),
        "must_show": "v24 — the throng: bodies pressing from every side, progress fought for; Jairus dragging the pace forward.",
        "must_not_show": "the crowd is friendly but SLOW — every body in the way is a stolen minute, and Jairus's face knows it.",
        "scene": (
            "The narrow lane is choked wall to wall, the camera low "
            "behind the pressing shoulders: the crowd "
            "presses in on every side of Jesus, hands reaching, "
            "neighbours calling, bodies wedged shoulder to shoulder — "
            "and at the front Jairus hauls the way open with both "
            "arms, throwing agonized looks back over his shoulder, a "
            "father watching minutes bleed away into the crush while "
            "his girl slips further with each one. Late-afternoon "
            "light between the walls. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r057-b08", "out": "s08-messengers-from-the-house.jpeg", "seg": "n3 p1",
        "window": "40.24-45.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAIRUS", "ROAD"],
        "narration": ("But before they arrived, messengers came from the "
                      "house with the worst news a father can hear."),
        "must_show": "v35 — the meeting: two household men coming up the lane with lowered eyes; Jairus stopping dead at the sight of their faces.",
        "must_not_show": "the news is legible in the messengers' posture BEFORE any word — that is what stops him.",
        "scene": (
            "Two household men in dark earth-brown wool have come up "
            "the lane and stopped a few paces short — heads lowered, "
            "one twisting his belt in both hands, neither able to "
            "meet the master's eyes — and Jairus has stopped dead in "
            "the middle of the crowd, gone absolutely rigid, reading "
            "the message in their bowed heads before either can open "
            "his mouth. Exactly three people are in the frame in "
            "focus; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b09", "out": "s09-thy-daughter-is-dead.jpeg", "seg": "s35",
        "window": "45.31-51.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAIRUS"],
        "narration": ("Thy daughter is dead: why troublest thou the "
                      "Master any further? (Mark 5:35)"),
        "must_show": "the sentence landing — close on Jairus's face in the instant the world ends.",
        "must_not_show": "not a scream — the soundless caving of a face; the crowd noise dying around it.",
        "scene": (
            "Very close on Jairus's face as the words land: his eyes "
            "lose their focus mid-blink, his mouth opens on nothing, "
            "and the strong composed architecture of the face simply "
            "gives way from inside — the soundless caving-in of a "
            "man hearing the one sentence he ran all this way to "
            "outrun. The messenger's bowed head blurs at the frame's "
            "edge. Exactly two people are in the frame; each has one "
            "head."
        ),
    },
    {
        "id": "v2-r057-b10", "out": "s10-broke-in-the-road.jpeg", "seg": "n3b p1-p2",
        "window": "51.12-55.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAIRUS", "ROAD"],
        "narration": ("Why bother the Teacher any further? And Jairus' "
                      "heart broke in the middle of the road."),
        "must_show": "the breaking — Jairus buckled where he stands, gripped by a messenger; the crowd hushed in a ring.",
        "must_not_show": "grief honored, not rushed — nobody hurries him in this frame.",
        "scene": (
            "Jairus has buckled in the middle of the lane — bent "
            "double over his own knees, one fist pressed against his "
            "chest, the older messenger gripping his arm to hold him "
            "upright — while the crowd that was pressing a moment ago "
            "has fallen back into a hushed ring around the broken "
            "man, and the light down the lane goes long and late. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b11", "out": "s11-jesus-heard-it-too.jpeg", "seg": "n3b p3",
        "window": "55.64-61.24", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JAIRUS"],
        "narration": ("But Jesus heard it too, and he spoke before the "
                      "father could say anything at all."),
        "must_show": "v36 — the interception: Jesus already turned and moving to Jairus in the same instant, arriving before despair can finish its sentence.",
        "must_not_show": "the timing is the doctrine — Jesus is mid-turn, mouth already opening, while the news is still in the air.",
        "scene": (
            "Jesus has already turned — caught mid-motion, closing "
            "the space to the buckled ruler in one stride, his hand "
            "reaching for the man's arm and his mouth already opening "
            "to speak — moving with the swiftness of someone "
            "intercepting a falling thing before it strikes the "
            "ground, while the messenger's last words still hang in "
            "the air. Exactly three people are in the frame; each "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b12", "out": "s12-be-not-afraid.jpeg", "seg": "jv36",
        "window": "61.24-64.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JAIRUS"],
        "narration": "Be not afraid, only believe. (Mark 5:36)",
        "must_show": "the words at close hold — both of Jesus's hands on Jairus's shoulders, faces a hand-span apart, the command that is a lifeline.",
        "must_not_show": "no easy comfort in Jesus's face — gravity and certainty together.",
        "scene": (
            "Jesus grips the broken man by both shoulders and holds "
            "him squarely in front of himself, their faces a "
            "hand-span apart — Jairus's face wrecked and swimming, "
            "barely able to hold the gaze, and Jesus's face utterly "
            "grave and utterly certain, giving him the two commands "
            "like handholds over a drop: no fear; keep believing. "
            "Exactly two people are in the frame; each visible hand "
            "has five fingers."
        ),
    },
    {
        "id": "v2-r057-b13", "out": "s13-keep-believing-anyway.jpeg", "seg": "n3c p1-p2",
        "window": "64.73-71.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAIRUS"],
        "narration": "Don't be afraid. Just keep believing.",
        "must_show": "the fight on Jairus's face — despair and the commanded faith wrestling in real time; the decision to keep walking.",
        "must_not_show": "not serene faith — faith with its teeth gritted, which is the only kind available to him now.",
        "scene": (
            "Close on Jairus's ruined face as the two commands work "
            "on it: the grief is all still there — flooded eyes, "
            "shaking jaw — but through the middle of it something is "
            "gripping hold, the brows steadying, one long shuddering "
            "breath being taken and held — a father choosing, "
            "muscle by muscle, to keep believing for the length of "
            "one more walk home. Exactly one person is in the frame, "
            "with one head."
        ),
    },
    {
        "id": "v2-r057-b14", "out": "s14-the-walk-resumed.jpeg", "seg": "n3c p3",
        "window": "71.00-78.06", "wide": True, "jesus": True, "ref": REF,
        "locks": ["JAIRUS", "THREE", "ROAD"],
        "narration": ("The worst thing had already happened, and Jesus "
                      "told him to keep believing anyway — not that it "
                      "would be undone, but that he should not stop "
                      "trusting him now."),
        "must_show": "v37 — the reduced company walking on: Jesus, Jairus, and only Peter, James and John; the crowd left behind.",
        "must_not_show": "the crowd stays back — five figures walk forward alone; the thinning is visible.",
        "scene": (
            "SHOT FROM BEHIND THE FIVE as they walk away up the "
            "emptying lane toward the house — Jesus beside the "
            "unsteady ruler with a hand at his back, Peter, James "
            "and John following close — all of their backs to the "
            "camera, faced the way they are going, while behind them "
            "at the frame's near edge the great crowd stands halted "
            "where it was told to stay, watching the five grow "
            "smaller. Late light down the lane. Every figure has two "
            "arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r057-b15", "out": "s15-weeping-and-wailing.jpeg", "seg": "n4 p1",
        "window": "78.06-83.67", "wide": True, "jesus": False, "ref": False,
        "locks": ["HOUSE"],
        "narration": ("At the house the mourning had already begun, "
                      "people weeping and wailing loudly for the little "
                      "girl."),
        "must_show": "v38 — the tumult: the courtyard full of loud mourners, wailing women, the din of formal grief.",
        "must_not_show": "loud communal mourning, real in its way — but its LOUDNESS contrasts the quiet room to come.",
        "scene": (
            "The walled courtyard of the fine house, the camera at "
            "the gate taking it from the side, is a storm of "
            "grief: dark-clothed mourning women wail with arms "
            "thrown up, a circle of neighbours weep and sway, a "
            "grey-bearded man cries the lament with both hands at "
            "his temples — the loud, crowded, public din of a "
            "household announcing its loss to the whole lane, oil "
            "lamps being lit against the failing afternoon. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b16", "out": "s16-not-dead-but-sleepeth.jpeg", "seg": "n4 p2 + j39",
        "window": "83.67-92.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": ("And Jesus said to them: Why make ye this ado, and "
                      "weep? the damsel is not dead, but sleepeth. "
                      "(Mark 5:39)"),
        "must_show": "v39 — Jesus in the courtyard gateway addressing the tumult; the wailing faltering around his calm.",
        "must_not_show": "he does not shout over them — his stillness cuts through their noise.",
        "scene": (
            "Jesus stands just inside the courtyard gate, still and "
            "plain amid the storm of mourners, one hand lifted "
            "palm-out as he speaks — and the wailing is faltering "
            "around him in rings, arms lowering, faces turning, the "
            "din losing its rhythm against a calm it cannot absorb — "
            "while Jairus and the three wait behind him in the "
            "gateway. Early-evening light, first lamps lit. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b17", "out": "s17-they-laughed-at-him.jpeg", "seg": "n4b",
        "window": "92.83-101.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": ("Why all this noise and crying, he asked. The child "
                      "is not dead. She's asleep. And they laughed at "
                      "him, certain that she was gone."),
        "must_show": "v40 — the scorn: mourners' grief flipped into derisive laughter aimed at him; Jesus unmoved in the middle of it.",
        "must_not_show": "the laughter is scornful, not joyful — heads thrown back, contempt; and it does not touch him.",
        "scene": (
            "The courtyard's grief has curdled into scorn: mourners "
            "laugh in his face — a woman with her head thrown back, "
            "a man jabbing a finger toward the shuttered room, "
            "another elbowing his neighbour, the hired grief "
            "dissolving into contempt for the man who said "
            "'sleeping' — while Jesus stands quiet at the centre of "
            "the mockery, entirely unmoved, already looking toward "
            "the door of the room where the child lies. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b18", "out": "s18-he-put-them-all-out.jpeg", "seg": "n5 p1",
        "window": "101.84-103.28", "wide": False, "jesus": True, "ref": REF,
        "locks": ["HOUSE"],
        "narration": "He put them all outside.",
        "must_show": "v40 — the clearing: Jesus's arm extended, moving the whole scornful crowd out through the gate; the courtyard emptying.",
        "must_not_show": "authority without violence — they go because the arm and the face are not negotiable.",
        "scene": (
            "Jesus stands with one arm extended full length toward "
            "the courtyard gate, his face quiet and absolute — and "
            "the mourners are going: a dark stream of them pressing "
            "out through the gateway, some still smirking, some "
            "suddenly uncertain, herded out by nothing but the "
            "extended arm and the face behind it — the courtyard "
            "emptying by the second. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r057-b19", "out": "s19-five-went-in-quietly.jpeg", "seg": "n5 p2a",
        "window": "103.28-107.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JAIRUS", "MOTHER", "THREE", "HOUSE"],
        "narration": ("Then he took the girl's father and mother, and "
                      "three of his closest friends,"),
        "must_show": "the small company at the door — six souls entering quietly where a hundred were shut out.",
        "must_not_show": "the hush is total — after the courtyard's din, this doorway is another world.",
        "scene": (
            "At the low door of the sleeping room the small company "
            "gathers in the sudden hush of the emptied courtyard: "
            "Jesus lifts the curtain aside, the mother pressed "
            "against Jairus with her hand knotted in his sleeve, "
            "Peter, James and John close behind with their heads "
            "bowed under the lintel — six people entering on their "
            "quietest feet where a hundred mourners were just shut "
            "out. First lamplight from within. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b20", "out": "s20-small-and-still.jpeg", "seg": "n5 p2b",
        "window": "107.50-111.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GIRL", "JAIRUS", "MOTHER", "HOUSE"],
        "narration": ("and went in quietly to where the child was lying, "
                      "small and still."),
        "must_show": "G-law's frame — the child as scripture shows her: the small sleeping form on the bed, the parents' faces at the threshold carrying everything.",
        "must_not_show": "NOTHING a bereaved parent could not bear: she is a sleeping child in lamplight, peaceful, beloved.",
        "scene": (
            "The small room in low lamplight: the girl lies still "
            "and small under the dark olive-brown blanket, her face "
            "peaceful among her loose dark hair, one small hand "
            "resting open on the cover — utterly a sleeping child — "
            "while at the threshold her parents stand pressed "
            "together, the mother's knuckles at her mouth, and Jesus "
            "steps softly toward the bed ahead of them. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b21", "out": "s21-talitha-cumi.jpeg", "seg": "jtal",
        "window": "111.73-114.63", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GIRL"],
        "narration": "Talitha cumi. (Mark 5:41)",
        "must_show": "v41 — THE picture: her small hand taken in his, his face bent low over the sleeping child, the Aramaic on his lips.",
        "must_not_show": "no light effect; a hand holding a child's hand in lamplight is the whole miracle's grammar.",
        "scene": (
            "Close at the bedside in the lamp's warm circle: Jesus "
            "kneels by the low bed with the girl's small limp hand "
            "held gently inside his own, his face bent near hers, "
            "the words just leaving him — soft, familiar, his own "
            "everyday tongue — while her still face lies turned "
            "toward him on the pillow as if listening in her sleep. "
            "Exactly two people are in the frame; each visible hand "
            "has five fingers."
        ),
    },
    {
        "id": "v2-r057-b22", "out": "s22-damsel-arise.jpeg", "seg": "s41i + jv41",
        "window": "114.63-122.26", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GIRL"],
        "narration": ("which is, being interpreted, Damsel, I say unto "
                      "thee, arise. (Mark 5:41)"),
        "must_show": "the summons finishing — his face over hers; her eyelids just beginning to stir.",
        "must_not_show": "the stir is TINY — lashes, a first small breath deepening; the frame holds its own breath.",
        "scene": (
            "The two faces close in the lamplight: Jesus's face bent "
            "over the child's, finishing the gentle summons — and on "
            "the pillow the first almost-nothing of an answer: her "
            "dark lashes trembling, her small chest lifting on a "
            "breath deeper than sleep has been taking, colour "
            "beginning at her lips — a picture holding perfectly "
            "still around the smallest movement in the world. "
            "Exactly two people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r057-b23", "out": "s23-a-school-morning.jpeg", "seg": "n6 p1-p2",
        "window": "122.26-130.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GIRL"],
        "narration": ("Two words in his own everyday Aramaic — little "
                      "girl, get up. It is the kind of thing a parent "
                      "says on a school morning."),
        "must_show": "her eyes OPEN — the child awake, blinking up at the stranger holding her hand; his face warm above her.",
        "must_not_show": "no fear on her face — she wakes the way children wake, unaware anything was ever wrong.",
        "scene": (
            "The girl's eyes are open: she blinks up from the pillow "
            "at the warm-eyed stranger holding her hand, her small "
            "face creased with ordinary waking confusion — a child "
            "surfacing on a school morning, entirely unafraid — and "
            "Jesus looks down at her with the smile already begun, "
            "his hand steady around hers, drawing her up toward "
            "sitting. Lamplight warm on both faces. Exactly two "
            "people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r057-b24", "out": "s24-she-got-up-and-walked.jpeg", "seg": "n6 p3",
        "window": "130.58-134.91", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GIRL", "JAIRUS", "MOTHER", "THREE", "HOUSE"],
        "narration": ("He took her by the hand, and immediately she got "
                      "up, and began to walk."),
        "must_show": "v42 — the child ON HER FEET and WALKING across the room, her hand in his; the witnesses against the walls.",
        "must_not_show": "she walks steadily — a healthy twelve-year-old's steps, nothing tentative or eerie.",
        "scene": (
            "The girl is up and walking: barefoot across the lamplit "
            "floor with her hand swinging in Jesus's hand, steady "
            "twelve-year-old steps, her dark hair loose down the "
            "madder-rose shift — while around the small room the "
            "witnesses have flattened themselves against the walls: "
            "Peter's hand over his mouth, James and John gripping "
            "each other's shoulders, and her parents frozen at the "
            "threshold in the first instant before the dam breaks. "
            "Every figure has two arms, two hands, two legs and one "
            "head."
        ),
    },
    {
        "id": "v2-r057-b25", "out": "s25-beside-themselves.jpeg", "seg": "n6 p4-p5",
        "window": "134.91-143.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GIRL", "JAIRUS", "MOTHER", "HOUSE"],
        "narration": ("She was twelve years old. Her parents were beside "
                      "themselves with wonder, holding the daughter they "
                      "had already grieved as lost."),
        "must_show": "the dam breaking — both parents on their knees around the standing child, holding her; the grief of an hour ago transmuted whole.",
        "must_not_show": "Jesus stands back from the family knot, glad and unclaiming.",
        "scene": (
            "The parents have crashed to their knees around their "
            "standing daughter and wrapped her whole — the mother's "
            "face pressed into the girl's dark hair, Jairus's big "
            "arms around them both with his ruined face lifted to "
            "the ceiling, laughing and weeping in the same breath — "
            "while the girl pats her mother's shoulder in mild "
            "twelve-year-old bewilderment, and Jesus stands back in "
            "the lamplight, watching what he came for. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b26", "out": "s26-give-her-to-eat.jpeg", "seg": "n7 p1",
        "window": "143.25-148.12", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GIRL", "MOTHER", "HOUSE"],
        "narration": ("And then Jesus said the most tender, ordinary "
                      "thing: give her something to eat."),
        "must_show": "v43 — the instruction mid-gesture: Jesus nodding toward the kitchen, the mother already turning for food through her tears.",
        "must_not_show": "the holiest room in Galilee pivoting to supper — the ordinariness IS the tenderness.",
        "scene": (
            "Jesus, half-smiling, tips his head toward the doorway "
            "and the kitchen beyond with one open hand — the "
            "practical instruction visibly landing — and the mother "
            "is already up and turning through her tears, wiping her "
            "hands on her dress out of pure habit, a woman handed "
            "back the ordinary mercy of feeding her child — while "
            "the girl looks up hopefully at the word 'eat'. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r057-b27", "out": "s27-a-growing-girl.jpeg", "seg": "n7 p2-p3",
        "window": "148.12-156.39", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GIRL", "JAIRUS", "MOTHER", "HOUSE"],
        "narration": ("He had just raised her from death, and his very "
                      "next thought was that a growing girl would be "
                      "hungry. The small things mattered to him too."),
        "must_show": "the closing frame — the girl eating hungrily at the low table, family around her, Jesus watching with plain warmth; supper as doxology.",
        "must_not_show": "warm, low, domestic — no crowd, no spectacle; the miracle ends in a kitchen.",
        "scene": (
            "At the low table in warm lamplight, the camera behind "
            "Jesus's quiet shoulder at the room's edge, the girl eats like a "
            "healthy twelve-year-old — tearing bread, cheeks full, "
            "reaching for the dish of stew — while her mother hovers "
            "unable to stop touching her hair and Jairus sits close "
            "with his hand resting on his daughter's back as if "
            "checking she is real — and Jesus watches from across "
            "the table with open unhurried warmth, a guest at the "
            "supper he made possible. Every figure has two arms, two "
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
    "HOUSE": "PLACE-REF/house.jpeg",  # build-57-jairus-daughter s15-weeping-and-wailing (manual)
    "ROAD": "PLACE-REF/road.jpeg",  # build-38-persistent-widow v2-r038-b39
}
# === end PLACE-PLATES ===
