#!/usr/bin/env python3
"""V2 beat map — row 172, build-172-gospel-preached-to-the-dead (1 Peter 4:6 +
the anchor verses 1 Peter 3:18-19, 'he went and preached unto the spirits in
prison').

COVERAGE: 11 pictures over 49.64 s (card_start) = ~4.5 s/picture (lesson 12
movie-coverage). Short row (49.6 s), so the beat count is scaled down with it.
ONE establishing wide per place (b01 graveside, b02 the waiting place); every
other beat is a single, a close or an over-shoulder two-shot.

NO OPEN CAMERON COMPLAINT — `v2_outline.py 172` shows none. This is a fresh
authoring of the picture map on the already-authored SPEAKER-LAW narration.

SPEAKER LAW: Peter's epistle — NO red-letter and NO God-voice anywhere. s1
('For for this cause was the gospel preached also to them that are dead…') and
s19 (1 Peter 3:18-19) are the SCRIPTURE voice → LIGHT-BLUE captions, never red.
Jesus IS embodied (the risen, quickened Lord) on the four s19 beats b06-b09,
because 'he went and preached' is the concrete act Peter names; only Jesus wears
cream and the caption on those beats stays scripture-blue, never red.

CONTENT-CARE (the subject is the DEAD → restraint governs every frame):
  - The departed are shown with DIGNITY and HOPE, never as corpses, bones, gore
    or open biers; the grave is plain and closed.
  - The 'spirits in prison' are REAL, SOLID, FULLY-CLOTHED people standing on
    real ground — NEVER ghosts, mist, translucent figures, floating shades or
    apparitions.
  - 'Prison' is a place of WAITING, not a dungeon: NO bars, cell, chains,
    shackles, iron, torment, fire, flame, chasm or gulf; NO devil/monster; and
    equally NO medieval-heaven kitsch (cloud floor, pearly gate, golden street,
    throne, harp, wings). It is a vast dim quiet expanse of real ground into
    which a warm daylight breaks. This deliberately avoids the Luke-16
    SPIRIT-WORLD lock (two regions + a gulf + a place of torment) and the earthly
    ANCIENT-PRISON lock (a real jail with timber bars and irons) — neither fits
    what 1 Peter says or what Cameron's church teaches about the departed.
  - The light that arrives is REAL DIRECTIONAL DAYLIGHT from an opening — never a
    halo, glow or rim-light on any person, least of all Jesus.

THE HUMAN SPINE (one restrained through-line so the doctrine lands on a person,
not an abstraction): a believing man has died. His widow mourns at his grave
(GRAVESIDE-MORNING). In the waiting place of the departed (SPIRIT-PRISON) that
same man waits until Christ comes down, brings him to God, and preaches to the
spirits who waited. Death did not close the door; the message crossed over.
  GRAVESIDE-MORNING  the widow at the plain grave (b01, b04, b10)
  SPIRIT-PRISON      the waiting dead + the risen Christ preaching (b02, b03,
                     b05, b06-b09, b11)

NEW places (runner promotes each from its first good NON-Jesus frame, lesson 11):
  GRAVESIDE-MORNING  promote b01
  SPIRIT-PRISON      promote b02 (the establishing wide of the waiting place —
                     NOT b06-b09, which are Jesus frames)
Steps in QC.md.
"""

# LOCKS: all build-local. Setting/person locks NEVER conflict; only Jesus wears
# cream, and Jesus is carried by jesus=True + ref=True (the shared lock and the
# JESUS-MASTER-REF are injected automatically, same as rows 169/171).
LOCKS = {
    "GRAVESIDE-MORNING": (
        "GRAVESIDE-MORNING LOCK: the same place in every frame — a quiet "
        "first-century burial ground on a low stony hillside, plain rock-cut "
        "tombs and simple undressed stone markers among a few olive trees, dry "
        "grass and pale earth, soft early-morning light and long gentle shadows, "
        "low hills and an open sky beyond. The same hillside, tombs and trees "
        "throughout — never modern masonry, metal, railing, sign or fixture, no "
        "carved or painted lettering anywhere, and no rendered writing of any "
        "kind."
    ),
    "SPIRIT-PRISON": (
        "SPIRIT-PRISON LOCK: this is the waiting place of the departed, and it is "
        "a REAL PLACE WITH REAL GROUND, REAL AIR, REAL DISTANCE and REAL "
        "DIRECTIONAL LIGHT casting REAL SHADOWS — photographed exactly like the "
        "living world, not a void, dream, mist or symbol. It is a vast, still, "
        "dim expanse of level bare earth and worn pale stone running back to a "
        "far horizon under a deep dusk-blue sky, quiet and unhurried and "
        "comfortless-but-not-cruel. The people there are the DEAD who wait: they "
        "are REAL, SOLID, WHOLE, HEALTHY people of every age, FULLY CLOTHED in "
        "ordinary hand-woven earth-toned wool and linen, standing and sitting on "
        "the real ground and casting real shadows — they are ordinary living-"
        "looking human beings, never translucent, never mist, never floating, "
        "never faded or ghostly. Into this dim place a WARM DAYLIGHT breaks in "
        "low from one open side, a real shaft of morning light lying across the "
        "ground, and the nearest faces turn toward it. THIS IS NOT A JAIL AND NOT "
        "A HELL: nowhere in it is there any bar, cell, cage, wall of confinement, "
        "chain, shackle, iron, rope-binding or prisoner in irons; no fire, flame, "
        "coal, smoke, torment, torture, wound, blood, corpse, skull or bone; no "
        "chasm, gulf, pit or canyon; no devil, demon, monster or beast. AND IT IS "
        "NOT A PAINTED HEAVEN: no cloud floor or sky-city, no gate, arch or pearly "
        "gate, no golden street or shining architecture, no throne, harp, trumpet, "
        "crown, wing or shaft of divine light from above. The whole of the idea is "
        "REAL PEOPLE WAITING IN A DIM PLACE INTO WHICH A REAL LIGHT COMES."
    ),
    "MOURNER": (
        "MOURNER LOCK: the widow of the departed man, remembering him at his "
        "grave — one ordinary first-century woman of middle years, a lined "
        "gentle face, dark hair going grey under a plain earth-toned head-cloth, "
        "sober deep-toned wool robes (never cream), grief carried with dignity "
        "and a growing hope. The SAME woman in every graveside frame, never "
        "twinned, never a cloned face."
    ),
    "DEPARTED-MAN": (
        "DEPARTED-MAN LOCK: the believing man who has died — the soul the video "
        "follows in the waiting place. One ordinary first-century man of middle "
        "years, a weathered, kind, work-worn face, dark hair and a short dark "
        "beard both going grey, a plain earth-toned wool tunic (never cream), and "
        "he is REAL, SOLID and WHOLE — never a ghost, never translucent, never "
        "faded. The SAME man in every frame he appears, never twinned, never a "
        "cloned face."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r172-b01", "out": "s01-a-believer-had-died.jpeg", "seg": "n0",
        "window": "0.400-5.916", "wide": True, "jesus": False, "ref": False,
        "locks": ["GRAVESIDE-MORNING", "MOURNER"],
        "narration": "Some who heard the good news had already died before they could finish their lives in the body.",
        "must_show": "the ONE establishing wide of the graveside — the camera stands back behind the widow's shoulder as she stands at a plain closed rock tomb in the soft morning light, mourning a man who had believed and has now died; a real loss in a real place.",
        "must_not_show": "no corpse, open bier, body, bones or gore — the grave is closed and plain; no scroll, parchment, writing, lettering, numerals or panel of any kind along any edge; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "On a low stony hillside of plain rock-cut tombs and olive trees the "
            "camera stands back behind the shoulder of an ordinary middle-aged "
            "woman in a plain head-cloth and sober robes, who stands at a low "
            "closed tomb in the soft early-morning light, her head bowed in grief "
            "for the man buried there — a believer who died before his years were "
            "full. Dry grass, pale earth and long gentle shadows lie around her, "
            "low hills beyond. She is an ordinary-sized person with two hands and "
            "one head, not in cream, her gaze on the grave and not the camera; "
            "nothing is written anywhere and no light rings her head."
        ),
    },
    {
        "id": "v2-r172-b02", "out": "s02-preached-to-the-dead.jpeg", "seg": "s1",
        "window": "5.916-11.463", "wide": True, "jesus": False, "ref": False,
        "locks": ["SPIRIT-PRISON", "BACKGROUND-CAST"],
        "narration": "For this cause was the gospel preached also to them that are dead,",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the ONE establishing wide of the waiting place: the camera behind a gathering of ordinary, solid, fully-clothed departed people standing in a vast dim quiet expanse, the nearest faces beginning to turn toward a warm daylight breaking in low from one open side; the good news reaching those who have died.",
        "must_not_show": "these are REAL solid people, NEVER ghosts, mist, translucent, floating or faded; no bar, cell, chain, shackle or prisoner in irons; no fire, flame, torment, corpse, skull, bone or gore; no chasm or gulf; no devil or monster; no cloud floor, gate, golden street, throne, harp or wings; no scroll, writing or panel; no Jesus and no cream here; no halo, glare or rim-light; no modern object; no posed line to the lens.",
        "scene": (
            "The camera stands back behind the backs of a gathering of the "
            "departed in a vast, still, dim expanse of level bare earth and worn "
            "pale stone under a deep dusk-blue sky — ordinary, solid, whole people "
            "of every age in earth-toned wool, standing and waiting and casting "
            "real shadows on the real ground. Away to one side a warm shaft of "
            "morning light breaks in low across the ground, and the nearest of "
            "them are beginning to turn their faces toward it. Every figure is an "
            "ordinary-sized, distinct, living-looking person with two hands and "
            "one head, none in cream and none turned to the camera; nothing is "
            "written anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r172-b03", "out": "s03-alive-in-the-spirit.jpeg", "seg": "s1",
        "window": "11.463-17.011", "wide": False, "jesus": False, "ref": False,
        "locks": ["SPIRIT-PRISON", "DEPARTED-MAN"],
        "narration": "that they might be judged according to men in the flesh, but live according to God in the spirit.",
        "must_show": "SCRIPTURE-EXACT — a close on the departed man the video follows: an ordinary weathered face, a man the world counted dead in the flesh, standing whole and quietly alive in the growing warm light; judged in the flesh, alive in the spirit.",
        "must_not_show": "he is a REAL solid man, NEVER a ghost, translucent, faded or floating; no bar, chain or iron; no fire, corpse, skull, bone or gore; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "Close in the dim waiting place: the departed man — a work-worn, kind "
            "face, dark hair and short beard going grey, in a plain earth-toned "
            "tunic — stands whole and steady as the warm shaft of morning light "
            "reaches his face, a man the world buried yet plainly alive and "
            "aware. The dim expanse falls away soft behind him. He is an "
            "ordinary-sized, solid person with two hands and one head, not in "
            "cream, his gaze toward the light and not the camera; nothing is "
            "written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r172-b04", "out": "s04-not-in-vain.jpeg", "seg": "n1b",
        "window": "17.011-20.087", "wide": False, "jesus": False, "ref": False,
        "locks": ["GRAVESIDE-MORNING", "MOURNER"],
        "narration": "Not in vain, not too late.",
        "must_show": "back at the grave — a close on the widow, a fragile hope breaking through her grief as she looks up from the tomb; the loss not in vain, the hope not too late.",
        "must_not_show": "no corpse, body, bones or grave-gore; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "Close by the plain tomb in the soft morning light: the widow lifts "
            "her lined face a little from the grave, the grief easing as a "
            "fragile, quiet hope breaks through — the look of a woman daring to "
            "believe her loss is not the end of him. Olive branches and pale "
            "earth sit soft behind her. She is an ordinary-sized woman with two "
            "hands and one head, not in cream, her eyes lifting past the camera "
            "in hope and not to it; nothing is written anywhere and no light "
            "rings her head."
        ),
    },
    {
        "id": "v2-r172-b05", "out": "s05-two-measures.jpeg", "seg": "n2",
        "window": "20.087-27.068", "wide": False, "jesus": False, "ref": False,
        "locks": ["SPIRIT-PRISON", "DEPARTED-MAN"],
        "narration": "They might be judged by men's measure in the flesh — and yet be alive by God's measure in the spirit.",
        "must_show": "the two measures on one dignified figure — the departed man standing whole and alive in the soft light of the waiting place: counted lost by the world's measure, living by God's.",
        "must_not_show": "he is a REAL solid man, never a ghost, translucent or faded; no bar, chain or iron; no fire, corpse, skull, bone or gore; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object; no face posed to the lens.",
        "scene": (
            "In the dim waiting place the departed man stands full-length in the "
            "warm shaft of morning light, whole and quietly alive — a man the "
            "living measured and buried, standing here by a truer measure, "
            "waiting and aware. The still dim expanse runs back soft behind him. "
            "An ordinary-sized, solid person with two hands and one head, not in "
            "cream, his gaze into the light and not the camera; nothing is "
            "written anywhere and no light rings his head."
        ),
    },
    {
        "id": "v2-r172-b06", "out": "s06-the-just-for-the-unjust.jpeg", "seg": "s19",
        "window": "27.068-31.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["SPIRIT-PRISON"],
        "narration": "For Christ also hath once suffered for sins, the just for the unjust,",
        "must_show": "SCRIPTURE-EXACT (light-blue) — the risen Lord coming down into the waiting place after his own suffering: Christ stepping in from the warm opening of light among the departed, compassion on his face; the just come for the unjust.",
        "must_not_show": "no wound-gore, blood, nails or cross; the risen Lord is warm and solid, NOT a ghost, apparition or glare; no halo, glow or rim-light; only Jesus in cream; no bar, chain, iron, fire, corpse, skull or bone; no chasm or gulf; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Into the dim waiting place, from the warm shaft of morning light at "
            "one open side, the risen Christ steps in among the departed — a warm, "
            "solid, breathing man in a plain cream robe, deep compassion on his "
            "face, the light lying on the ground behind him where he entered. The "
            "waiting people stand near, ordinary and solid in earth-toned wool. He "
            "is an ordinary-sized man with two hands and one head, his gaze on the "
            "people and not the camera; nothing is written anywhere and no light "
            "rings his head."
        ),
    },
    {
        "id": "v2-r172-b07", "out": "s07-bring-us-to-god.jpeg", "seg": "s19",
        "window": "31.500-35.700", "wide": False, "jesus": True, "ref": True,
        "locks": ["SPIRIT-PRISON", "DEPARTED-MAN"],
        "narration": "that he might bring us to God,",
        "must_show": "SCRIPTURE-EXACT — Christ reaching out a hand to the departed man, drawing him up and toward the warm light; that he might bring him to God.",
        "must_not_show": "no wound-gore or blood; Christ warm and solid, not a ghost or glare; no halo, glow or rim-light; only Jesus in cream; the departed man solid and real, never translucent; no bar, chain, fire, corpse or bone; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "In the warm light Christ reaches out an open hand to the departed "
            "man and the man takes it, Christ drawing him gently up and toward the "
            "bright opening — a real man in cream leading a real man in earth-"
            "toned wool out of the dim toward God. The still expanse falls away "
            "behind. Two ordinary-sized, solid people with two hands and one head "
            "each, only Christ in cream, their eyes on each other and not the "
            "camera; nothing is written anywhere and no light rings either head."
        ),
    },
    {
        "id": "v2-r172-b08", "out": "s08-quickened-by-the-spirit.jpeg", "seg": "s19",
        "window": "35.700-39.500", "wide": False, "jesus": True, "ref": True,
        "locks": ["SPIRIT-PRISON"],
        "narration": "being put to death in the flesh, but quickened by the Spirit:",
        "must_show": "SCRIPTURE-EXACT — Christ standing alive and full of life in the waiting place: put to death in the flesh yet made alive, the living Lord warm and solid among the departed.",
        "must_not_show": "no wound-gore, blood or cross; the living Lord is warm and real, NOT a ghost, apparition, spirit-figure or glare; no halo, glow or rim-light; only Jesus in cream; no bar, chain, fire, corpse, skull or bone; no scroll, writing or panel; no modern object; no face posed to the lens.",
        "scene": (
            "Christ stands full-length in the warm shaft of light in the midst of "
            "the dim place, alive and unhurried, a solid, breathing man in a plain "
            "cream robe — put to death in the flesh and yet plainly living, the "
            "warm light lying on the ground around his feet. The waiting people "
            "stand soft behind him in earth-toned wool. He is an ordinary-sized "
            "man with two hands and one head, his gaze calm across the place and "
            "not the camera; nothing is written anywhere and no light rings his "
            "head."
        ),
    },
    {
        "id": "v2-r172-b09", "out": "s09-preached-to-the-spirits.jpeg", "seg": "s19",
        "window": "39.500-43.295", "wide": False, "jesus": True, "ref": True,
        "locks": ["SPIRIT-PRISON", "BACKGROUND-CAST"],
        "narration": "By which also he went and preached unto the spirits in prison;",
        "must_show": "SCRIPTURE-EXACT — Christ preaching to the waiting dead: the camera past the shoulders of the listening departed toward Christ mid-word in the warm light, the gospel carried to the spirits who waited, hope breaking across their faces.",
        "must_not_show": "the listeners are REAL solid people, never ghosts, mist or translucent; no wound-gore; Christ warm and real, not a glare; no halo, glow or rim-light; only Jesus in cream; no bar, cell, chain, iron, fire, corpse, skull or bone; no chasm or gulf; no scroll, writing or panel; no modern object; no posed line to the lens.",
        "scene": (
            "The camera stands past the shoulders of a group of the departed and "
            "looks toward Christ, who stands in the warm shaft of light speaking "
            "to them mid-word — a solid man in a plain cream robe teaching the "
            "waiting dead, and the faces turned toward him lifting with a waking "
            "hope. The dim expanse runs back soft beyond. Ordinary-sized, "
            "distinct, solid people with two hands and one head each, only Christ "
            "in cream, their eyes on him and not the camera; nothing is written "
            "anywhere and no light rings any head."
        ),
    },
    {
        "id": "v2-r172-b10", "out": "s10-death-did-not-close-the-door.jpeg", "seg": "n3a",
        "window": "43.295-46.608", "wide": False, "jesus": False, "ref": False,
        "locks": ["GRAVESIDE-MORNING"],
        "narration": "Death did not close the door.",
        "must_show": "back at the grave — a close on the plain tomb's low doorway with the stone set aside and warm morning light lying across the open threshold; death did not close the door.",
        "must_not_show": "no body, bones or gore inside — the tomb is quiet and plainly empty; no figure or vision in the doorway; no scroll, writing or panel; no Jesus and no cream; no halo, glare or rim-light; no modern object.",
        "scene": (
            "A close on the low rock tomb in the morning light: its plain stone "
            "set aside from the dark doorway and the warm early light lying across "
            "the open threshold and a little way in over bare stone — an opened "
            "door, not a sealed one, quiet and empty. Dry grass and pale earth "
            "sit soft around it, olive branches above. Nothing is written "
            "anywhere, no body lies within, and no light rings anything — only "
            "the opened tomb and the morning light on its threshold."
        ),
    },
    {
        "id": "v2-r172-b11", "out": "s11-the-message-crossed-over.jpeg", "seg": "n3b",
        "window": "46.608-49.641", "wide": False, "jesus": False, "ref": False,
        "locks": ["SPIRIT-PRISON", "DEPARTED-MAN", "BACKGROUND-CAST"],
        "narration": "The message crossed over.",
        "must_show": "the warm light now full on the faces of the waiting dead — the departed man and those near him lit and lifted, receiving the message that has reached them; the message crossed over.",
        "must_not_show": "REAL solid people, never ghosts, mist or translucent; no bar, chain, fire, corpse, skull or bone; no chasm or gulf; no scroll, writing or panel; no Jesus required here and no cream on the people; no halo, glare or rim-light; no modern object; no posed line to the lens.",
        "scene": (
            "The warm shaft of morning light now lies full across the near part of "
            "the waiting place, and the departed man stands in it with several "
            "others of different ages — distinct, solid faces lit and lifting, "
            "hope waking in them as the message that crossed over reaches them at "
            "last. The dim expanse eases back soft beyond the light. Ordinary-"
            "sized, distinct people with two hands and one head each, none in "
            "cream, their faces lifted into the light and not to the camera; "
            "nothing is written anywhere and no light rings any head."
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

# No image REFS: every person is carried by a byte-identical text lock (no face
# sheets exist for this build's characters), and Jesus is carried by the shared
# JESUS-MASTER-REF auto-attached on the jesus=True beats.
REFS = {
}
