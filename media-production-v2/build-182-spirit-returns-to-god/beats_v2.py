#!/usr/bin/env python3
"""V2 beat map — row 182, build-182-spirit-returns-to-god (Ecclesiastes 12:1,7 — the
Teacher, Solomon, on the end of life: "Remember now thy Creator in the days of thy
youth... Then shall the dust return to the earth as it was: and the spirit shall
return unto God who gave it.").

COVERAGE: 16 pictures over 65.378 s (card_start) = ~4.0 s/picture (lesson 12
movie-coverage). The row runs a plain human life-arc so every beat clearly fits the
narrated moment: SOLOMON the aged Teacher who wrote it (frame), a YOUNG person in the
morning of life ("the days of thy youth"), an OLD person at the quiet close of life
("the evil days"), and the RETURN of the spirit as warm light to the unseen God. One
establishing wide per place (b01 chamber, b02 elder's home, b03 the morning hillside,
b10 the opening heaven); everything else is singles/closes/inserts.

NO OPEN CAMERON COMPLAINT (v2_outline.py 182 shows none). Fresh authored map.

AUDIO: default AUDIO LOCK stream-copy (no flag). Board Audio = OK. Picture-only
rebuild — do NOT re-voice. card_start = 65.378 s; total with card = 72.199 s.

SPEAKER LAW (see make_narration.py — both s0 and s1 are marked SCRIPTURE):
  s0  Ecclesiastes 12:1  "Remember now thy Creator in the days of thy youth, while the
      evil days come not, nor the years draw nigh, when thou shalt say, I have no
      pleasure in them;"                                            SCRIPTURE → light-blue
  s1  Ecclesiastes 12:7  "Then shall the dust return to the earth as it was: and the
      spirit shall return unto God who gave it."                    SCRIPTURE → light-blue
The narration itself frames these as Solomon's WRITTEN words ("The Teacher, Solomon,
wrote", "That is how he opens it", "he says"), NOT God speaking — so there is NO
red-letter and NO God-voice in this row. Everything else is the NARRATOR (white). NO
Jesus and NO cream anywhere (Old Testament wisdom).

**HARD GATE — GOD IS NEVER EMBODIED (default gate; no complaint asks otherwise here).**
On every RETURN-LIGHT beat (b10, b12, b13, b14, b15) the spirit returns to God, but
God is NEVER shown: no figure, face, hand, mouth, throne or beam-being, and no
halo/ring/rim-light around anything (the drift-word gate also bans those literal words
— word the light as radiant / luminous / brilliant / warm in the sky, never a ring
around a head). The Giver who receives the spirit is carried by warm welcoming
radiance in the heavens alone; the source stays unseen.

CONTENT-CARE (death → restraint, per CONTENT-CARE + rubric lesson 15's grey-corpse
sense): the old man's passing is shown as peaceful sleep, dignified and covered, warm
light on him — NEVER a corpse pallor, grey death, wounds, sores, decay, skeleton or
bones, and never any gore. The whole turn is hopeful comfort, not fear ("rest, not
terror"). THE SPIRIT that returns is warm rising LIGHT / luminous breath — NEVER a
ghost, a translucent person, a mist-figure or a floating body (spirits are not ghosts,
rows 171/172). No rendered/legible text or scripture-as-art anywhere (Solomon's scroll
is blank parchment).

TIME OF DAY (intentional, three registers so the arc reads at a glance): SOLOMON and
the ELDER live in the long warm GOLD light of evening (a life drawing to its close);
the YOUTH lives in fresh clear MORNING light (the beginning of a life); the RETURN is
a radiant break of warm light high in the evening-to-dawn heaven. No ordinary flat
sunset that reads as mere scenery (row-11 caution).

PLACES (all NEW — no stash plate exists for any; runner promotes each from its first
good frame, lesson 11; steps in QC.md):
  SOLOMON-CHAMBER  the aged Teacher's evening chamber where he wrote (b01, b08).
  ELDER-EVENING    a humble Judean home at golden evening where an old life closes and
                   comes to rest (b02, b04, b06, b09, b11, b16).
  YOUTH-MORNING    a sunlit Judean hillside/courtyard in fresh morning, the vigor of
                   youth turning toward God (b03, b05, b07).
  RETURN-LIGHT     the vast opening heaven of warm radiant light to which the spirit
                   returns; no figure of any kind (b10, b12, b13, b14, b15).
NEW-place promote plan (runner):
  SOLOMON-CHAMBER  promote b01 (establishing wide of the chamber).
  ELDER-EVENING    promote b02 (establishing wide of the elder's home at evening).
  YOUTH-MORNING    promote b03 (establishing wide of the morning hillside).
  RETURN-LIGHT     promote b10 (establishing wide of the opening heaven — no figure).
"""

# LOCKS: all build-local. No Jesus / no cream (OT). State clothing colours POSITIVELY
# and never cream/white-fine; only Jesus wears cream and he is not in this row.
LOCKS = {
    "SOLOMON-CHAMBER": (
        "SOLOMON-CHAMBER LOCK: the same place in every frame — the private evening "
        "chamber of an ancient Israelite king and sage: warm honey-coloured dressed "
        "stone walls, a low carved cedar writing table with a clay oil lamp and rolled "
        "parchments, deep-dyed cushions and a rich wine-and-indigo wall hanging, and a "
        "carved lattice opening onto a deep-blue dusk sky. The long warm gold light of "
        "evening fills the room from a single lamp and the fading window. Quiet, "
        "reflective, ancient; no modern object anywhere; any parchment is blank with "
        "no legible or rendered writing. The same chamber and evening light throughout."
    ),
    "ELDER-EVENING": (
        "ELDER-EVENING LOCK: the same place in every frame — a humble ancient Judean "
        "home at the long golden light of evening: plain lime-washed stone walls, a "
        "low bed-mat with a folded woollen blanket, a simple clay lamp, a worn wooden "
        "stool, and an open doorway giving onto a dimming amber-and-violet evening sky "
        "over the town. Warm, peaceful, humble; the place where an old life quietly "
        "draws to its close. No modern object anywhere; nothing is written anywhere. "
        "The same home and warm evening light throughout."
    ),
    "YOUTH-MORNING": (
        "YOUTH-MORNING LOCK: the same place in every frame — an open sunlit hillside "
        "and courtyard on the edge of an ancient Judean town in fresh clear morning "
        "light: young olive trees and green grass still wet with dew, pale warm stone "
        "walls, the bright unclouded light of the beginning of the day. Vigorous, "
        "hopeful, new; no modern object anywhere; nothing is written anywhere. The "
        "same hillside and clear morning light throughout."
    ),
    "RETURN-LIGHT": (
        "RETURN-LIGHT LOCK: the same vision-sky in every frame — a vast open heaven "
        "at the turn from evening to first light, opening high above into a warm, "
        "radiant, welcoming brilliance of soft luminous light, gentle veils and shafts "
        "of warm light rising and pouring through the deep sky. Reverent, immense, "
        "peaceful. There is NO building, NO ground detail, NO person and NO figure of "
        "any kind anywhere in it; the source of the light is never shown. Nothing is "
        "written anywhere. The same opening heaven of warm radiant light throughout."
    ),
    "SOLOMON": (
        "SOLOMON LOCK: the same man in every shot — an aged Israelite king and sage of "
        "about seventy, weathered olive-brown skin, a long well-kept grey-and-white "
        "beard and grey hair, a deeply lined, wise, reflective face. He wears a rich "
        "deep-indigo and wine-red robe with a narrow band of muted gold at the hem and "
        "a plain simple circlet — dignified but NEVER cream, never white, never a "
        "glaring bright robe. Ordinary-sized, one head, two hands. The SAME man "
        "throughout, never twinned or cloned."
    ),
    "YOUTH": (
        "YOUTH LOCK: the same young person in every shot — a young Israelite of about "
        "eighteen, warm olive-brown skin, dark brown hair, a smooth unlined youthful "
        "face full of health and hope. Plain earth-toned undyed tunic and belt (NEVER "
        "cream, never white-fine). Ordinary-sized, one head, two hands. The SAME young "
        "person throughout, never twinned or cloned; the same age in every frame."
    ),
    "ELDER": (
        "ELDER LOCK: the same man in every shot — a very old Israelite of about "
        "seventy-eight, weathered olive-brown skin, deep gentle lines, thin white hair "
        "and a soft white beard, a peaceful, dignified, kindly face. He wears a plain "
        "undyed muted earth-brown robe of a humble man (NEVER cream, never white-fine). "
        "His age and passing read as peaceful weariness and quiet rest only — NEVER "
        "any wound, sore, lesion, grey death-pallor, decay or gore. Ordinary-sized, "
        "one head, two hands. The SAME man throughout, never twinned or cloned."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r182-b01", "out": "s01-solomon-wrote-of-lifes-end.jpeg", "seg": "n0",
        "window": "0.400-3.120", "wide": True, "jesus": False, "ref": False,
        "locks": ["SOLOMON-CHAMBER", "SOLOMON"],
        "narration": "The Teacher, Solomon, wrote honestly about the end of life.",
        "must_show": "the ONE establishing wide of the chamber — aged Solomon at his low writing table in the long warm evening light, an unrolled blank parchment before him, his lined face grave and honest as he sets down hard truths about the end of life.",
        "must_not_show": "no legible or rendered writing on the parchment; no Jesus, no cream; no God figure; no halo, ring or rim-light; no modern object; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A wide of the aged king Solomon seen from behind and to the side as he sits "
            "at his low cedar writing table in the warm gold evening light of his stone "
            "chamber, his back three-quarters to the camera, an unrolled blank parchment "
            "and a clay lamp before him. His weathered face is turned down to the work, "
            "grave and honest, an old man writing plainly about the end of life. The "
            "single lamp and the fading lattice window light the room. Camera set behind "
            "and beside him looking past him to the table; ordinary-sized, one head; "
            "nothing legible is written on the parchment."
        ),
    },
    {
        "id": "v2-r182-b02", "out": "s02-the-body-grows-old.jpeg", "seg": "n0",
        "window": "3.120-7.965", "wide": True, "jesus": False, "ref": False,
        "locks": ["ELDER-EVENING", "ELDER"],
        "narration": "The body grows old, the days grow dim, and then — the breath leaves.",
        "must_show": "the ONE establishing wide of the elder's home — a very old man at the dimming close of a long day, sitting worn and quiet in the fading amber evening light of his humble home, the last of the day going out of the doorway; the body grown old, the breath soon to leave.",
        "must_not_show": "no wound, sore, grey death-pallor, decay or gore; no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A wide of the very old man seen from the side and slightly behind as he "
            "sits worn and still on the low stool near the open doorway of his humble "
            "stone home, his profile to the camera, the last dim amber light of evening "
            "fading through the door behind him. His shoulders are bowed with age and "
            "the day is going dark around him; his passing is only weariness and quiet, "
            "no distress. Camera to the side and behind him in profile; ordinary-sized, "
            "one head; the warm light rests on him, not around his head."
        ),
    },
    {
        "id": "v2-r182-b03", "out": "s03-remember-in-thy-youth.jpeg", "seg": "s0",
        "window": "7.965-12.500", "wide": True, "jesus": False, "ref": False,
        "locks": ["YOUTH-MORNING", "YOUTH"],
        "narration": "Remember now thy Creator in the days of thy youth,",
        "must_show": "SCRIPTURE, light-blue caption — the ONE establishing wide of the morning hillside: a young person in the fresh clear light of morning, in the full vigor of youth, pausing on the dewy green hillside to lift a hopeful face toward the bright open heaven, remembering the God who made them while life is still young.",
        "must_not_show": "God is never shown — no God figure, face or beam-being; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A wide of the young Israelite seen from behind and to the side, standing on "
            "a green dew-wet hillside among young olive trees in the fresh clear light "
            "of early morning, their back three-quarters to the camera as they lift a "
            "hopeful young face up toward the bright open morning sky. The vigor of "
            "youth and the beginning of the day are everywhere; they remember the One "
            "who made them while life is still full and new. Camera behind and beside "
            "them looking past them up the hill to the sky; ordinary-sized, one head; "
            "no figure in the sky and nothing written anywhere."
        ),
    },
    {
        "id": "v2-r182-b04", "out": "s04-before-the-evil-days.jpeg", "seg": "s0",
        "window": "12.500-18.196", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELDER-EVENING", "ELDER"],
        "narration": "while the evil days come not, nor the years draw nigh, when thou shalt say, I have no pleasure in them;",
        "must_show": "SCRIPTURE, light-blue caption — the hard years arriving: a close on the same kind of life grown very old, the old man sitting spent in the dim evening, the joy gone out of his days, weary of years that hold no more pleasure for him.",
        "must_not_show": "no wound, sore, grey death-pallor, decay or gore; no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the very old man in the dim amber evening light of his home, "
            "sitting spent and heavy, his lined face turned toward the fading window "
            "with the pleasure gone out of it — the hard years have come and there is "
            "no more delight left in them for him. Quiet, weary, dignified; his age is "
            "only tiredness, no distress or hurt. Ordinary-sized, one head, gaze off to "
            "the fading light and not to the camera; nothing written anywhere."
        ),
    },
    {
        "id": "v2-r182-b05", "out": "s05-remember-while-young.jpeg", "seg": "n0b",
        "window": "18.196-24.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["YOUTH-MORNING", "YOUTH"],
        "narration": "That is how he opens it. Remember your Maker while you are still young, he says —",
        "must_show": "a close on the young person in the bright morning, turning wholeheartedly toward the open sky, remembering their Maker now while they are still young and strong.",
        "must_not_show": "God is never shown — no God figure or beam-being; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the young Israelite on the sunlit morning hillside, their "
            "youthful face lifted and open toward the bright clear sky, turning "
            "wholeheartedly toward the God who made them while they are still young and "
            "full of life. The clean morning light is warm on their face. "
            "Ordinary-sized, one head, gaze lifted upward and not to the camera; no "
            "figure in the sky and nothing written anywhere."
        ),
    },
    {
        "id": "v2-r182-b06", "out": "s06-before-the-hard-years.jpeg", "seg": "n0b",
        "window": "24.800-29.780", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELDER-EVENING", "ELDER"],
        "narration": "before the hard years arrive, before you get to the age where you say there is nothing in this for me anymore.",
        "must_show": "the same warning made plain — a close on the old man in the dim evening, staring out empty and tired, at the age where a person says there is nothing left in this for them; the hard years have arrived.",
        "must_not_show": "no wound, sore, grey death-pallor, decay or gore; no God figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the very old man in the failing amber light of his home, "
            "staring out through the doorway empty and tired, the years heavy on him — "
            "he has reached the age where a person feels there is nothing left in life "
            "for them. Weary and quiet, not in pain, only worn down by the hard years. "
            "Ordinary-sized, one head, gaze distant and not to the camera; nothing "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r182-b07", "out": "s07-do-not-wait.jpeg", "seg": "n0b",
        "window": "29.780-33.577", "wide": False, "jesus": False, "ref": False,
        "locks": ["YOUTH-MORNING", "YOUTH"],
        "narration": "He is not being grim. He is telling you not to wait.",
        "must_show": "the tender urgency answered — a close on the young person in the morning light choosing now, stepping forward with a resolved, warm, unafraid face; not waiting, turning to their Maker today while life is young.",
        "must_not_show": "God is never shown — no God figure or beam-being; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the young Israelite on the bright hillside stepping forward with "
            "a warm, resolved, unafraid face into the clear morning light, choosing now "
            "and not later — taking Solomon's counsel to heart and turning to their "
            "Maker today while life is still young. Hopeful and decided, not grim. "
            "Ordinary-sized, one head, face forward toward the morning light; nothing "
            "written anywhere."
        ),
    },
    {
        "id": "v2-r182-b08", "out": "s08-he-pointed-where-breath-goes.jpeg", "seg": "n1",
        "window": "33.577-38.560", "wide": False, "jesus": False, "ref": False,
        "locks": ["SOLOMON-CHAMBER", "SOLOMON"],
        "narration": "He did not leave it there in the dark. He pointed plainly to where the breath goes.",
        "must_show": "aged Solomon in his evening chamber lifting his eyes and a hand plainly upward toward the heaven beyond the lattice — not leaving the matter in the dark but pointing clearly to where the breath goes when a person dies.",
        "must_not_show": "no legible or rendered writing; no God figure, face or beam-being in the sky; no Jesus, no cream; no halo, ring or rim-light; no modern object; not a cartoon.",
        "scene": (
            "A close on aged Solomon in the warm lamp-and-dusk light of his chamber, "
            "his lined face lifted and one open hand raised plainly toward the deep "
            "evening sky beyond the carved lattice — he does not leave the matter in "
            "the dark but points clearly upward to where the breath goes when a life "
            "ends. Calm, certain, hopeful. Ordinary-sized, one head, gaze and hand "
            "toward the window sky and not to the camera; no figure in the sky and "
            "nothing legible is written anywhere."
        ),
    },
    {
        "id": "v2-r182-b09", "out": "s09-the-dust-returns.jpeg", "seg": "s1",
        "window": "38.560-41.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELDER-EVENING", "ELDER"],
        "narration": "Then shall the dust return to the earth as it was:",
        "must_show": "SCRIPTURE, light-blue caption — the body coming to rest: the old man now at peaceful rest on his bed-mat as if fallen gently asleep, a folded blanket drawn over him, warm evening light on his serene face; the dust returning to the earth, dignified and calm.",
        "must_not_show": "no corpse pallor, grey death, wound, sore, decay, skeleton or gore; his face is peaceful and warm, not grey; no God figure; no ghost or spirit-figure yet; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A quiet close on the very old man at peaceful rest on his low bed-mat, as "
            "if he has gently fallen asleep, a folded woollen blanket drawn to his "
            "chest and his lined face serene and warm in the last amber evening light. "
            "His long life has come to its rest and the dust returns to the earth it "
            "came from — calm, dignified, reverent, without any distress. "
            "Ordinary-sized, one head; the warm light rests softly on his peaceful "
            "face; nothing written anywhere."
        ),
    },
    {
        "id": "v2-r182-b10", "out": "s10-the-spirit-returns-to-god.jpeg", "seg": "s1",
        "window": "41.800-45.530", "wide": True, "jesus": False, "ref": False,
        "locks": ["RETURN-LIGHT"],
        "narration": "and the spirit shall return unto God who gave it.",
        "must_show": "SCRIPTURE, light-blue caption — the ONE establishing wide of the opening heaven: a vast sky opening high above into warm radiant welcoming brilliance, and a gentle rising veil of warm luminous light ascending toward it — the spirit returning to the God who gave it; the Giver never shown.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand, throne or beam-being; the rising spirit is warm light only, NEVER a ghost, translucent person, mist-figure or floating body; no Jesus, no cream; no halo, ring or rim-light around anything; no modern object; nothing written; not a cartoon; not a posed figure facing the lens.",
        "scene": (
            "A vast establishing wide looking upward, the camera tilted up away from the "
            "earth into an immense evening-to-dawn heaven that opens high above into a "
            "warm, radiant, welcoming brilliance of soft luminous light. A gentle "
            "rising veil of warm light ascends through the deep sky toward that opening "
            "— the spirit going home to the God who gave it. The heaven is empty of any "
            "figure and the source of the light is never shown, so no one's face or "
            "back is toward the lens. Reverent and immense; nothing written anywhere "
            "and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r182-b11", "out": "s11-body-back-to-the-ground.jpeg", "seg": "n2",
        "window": "45.530-48.160", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELDER-EVENING", "ELDER"],
        "narration": "The body, made from dust, goes back to the ground.",
        "must_show": "a reverent insert of the old man's still, peaceful form at rest in the warm earth-toned evening light, the body made from dust returning quietly to the ground — dignified and calm, hands folded at rest.",
        "must_not_show": "no corpse pallor, grey death, wound, sore, decay, skeleton, bones or gore; no open grave horror; no God figure; no ghost or spirit-figure; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A reverent low insert of the very old man's peaceful still hands folded at "
            "rest and his serene covered form on the bed-mat, warm earth-toned evening "
            "light across the plain woollen cloth and the packed-earth floor of the "
            "humble home. The body, formed from dust, returns quietly and with dignity "
            "to the ground it came from. Calm, restful, warm; nothing distressing. "
            "Ordinary-sized; the warm light rests on the cloth; nothing written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r182-b12", "out": "s12-goes-home-to-him.jpeg", "seg": "n2",
        "window": "48.160-51.842", "wide": False, "jesus": False, "ref": False,
        "locks": ["RETURN-LIGHT"],
        "narration": "But the part of you that is from God goes home to Him.",
        "must_show": "the rising warm light continuing upward, a soft luminous ascent climbing higher through the opening heaven toward the radiant welcoming brilliance above — the part that is from God going home to Him.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; the rising spirit is warm light only, NEVER a ghost, translucent person, mist-figure or floating body; no Jesus, no cream; no halo, ring or rim-light around anything; no modern object; nothing written; not a cartoon.",
        "scene": (
            "The gentle rising veil of warm luminous light climbs higher up through the "
            "deep opening heaven, drawing toward the warm radiant welcoming brilliance "
            "high above — the part of a person that is from God going home to Him. Soft, "
            "peaceful, ascending; no figure of any kind anywhere and the source of the "
            "light never shown. Nothing written anywhere and no ring of light rings "
            "anything."
        ),
    },
    {
        "id": "v2-r182-b13", "out": "s13-not-the-end.jpeg", "seg": "n3",
        "window": "51.842-53.970", "wide": False, "jesus": False, "ref": False,
        "locks": ["RETURN-LIGHT"],
        "narration": "Death is not the end of the story.",
        "must_show": "the hope made plain — the opening heaven brightening into a warm first break of light, the darkness giving way, showing that death is not the end of the story but a threshold into light.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure or beam-being; no ghost or translucent person; no Jesus, no cream; no halo, ring or rim-light around anything; no modern object; nothing written; not a cartoon.",
        "scene": (
            "The deep opening heaven brightens as a warm first break of light spreads "
            "across it and the last of the dark gives way — an image of threshold and "
            "hope, showing that death is not the end of the story but an opening into "
            "warm light. Peaceful, dawning, unafraid; no figure of any kind and the "
            "source of the light never shown. Nothing written anywhere and no ring of "
            "light rings anything."
        ),
    },
    {
        "id": "v2-r182-b14", "out": "s14-quiet-return.jpeg", "seg": "n3",
        "window": "53.970-57.841", "wide": False, "jesus": False, "ref": False,
        "locks": ["RETURN-LIGHT"],
        "narration": "It is the spirit's quiet return to the One who lent it.",
        "must_show": "the quiet return completed — the rising warm light drawing softly and peacefully into the radiant welcoming brilliance of the heaven, a gentle homecoming; the spirit's quiet return to the One who lent it, the One never shown.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand or beam-being; no ghost or translucent person; no Jesus, no cream; no halo, ring or rim-light around anything; no modern object; nothing written; not a cartoon.",
        "scene": (
            "The gentle rising light draws softly and quietly up into the warm radiant "
            "welcoming brilliance high in the heaven, a peaceful homecoming — the "
            "spirit's quiet return to the One who first lent it. Tender, calm, "
            "unhurried; no figure of any kind anywhere and the source of the light "
            "never shown. Nothing written anywhere and no ring of light rings anything."
        ),
    },
    {
        "id": "v2-r182-b15", "out": "s15-the-giver-who-first-breathed.jpeg", "seg": "n4a",
        "window": "57.841-62.982", "wide": False, "jesus": False, "ref": False,
        "locks": ["RETURN-LIGHT"],
        "narration": "And the Giver who receives it back is the same Giver who first breathed it into you —",
        "must_show": "the welcoming radiance receiving — the warm radiant brilliance of the heaven opening a little wider and warmer to receive the returning light, the same warm Giver who first breathed life into a person now receiving the spirit back; the Giver Himself never shown.",
        "must_not_show": "GOD IS NEVER SHOWN — no God figure, face, hand, throne or beam-being; no ghost or translucent person; no Jesus, no cream; no halo, ring or rim-light around anything; no modern object; nothing written; not a cartoon.",
        "scene": (
            "The warm radiant welcoming brilliance high in the heaven opens a little "
            "wider and warmer as the gentle rising light is received into it — the same "
            "warm Giver who first breathed life into a person now quietly receiving the "
            "spirit back home. Warm, welcoming, tender; no figure of any kind anywhere "
            "and the Giver Himself never shown. Nothing written anywhere and no ring of "
            "light rings anything."
        ),
    },
    {
        "id": "v2-r182-b16", "out": "s16-with-mercy-not-anger.jpeg", "seg": "n4b",
        "window": "62.982-65.378", "wide": False, "jesus": False, "ref": False,
        "locks": ["ELDER-EVENING", "ELDER"],
        "narration": "— with mercy, not anger.",
        "must_show": "mercy made plain on a human face — a close on the old man's serene, peaceful, resting face bathed in warm merciful evening light, the picture of rest and not terror; received with mercy, not anger.",
        "must_not_show": "no corpse pallor, grey death, wound, sore, decay or gore; no fear or torment on the face; no God figure; no ghost; no Jesus, no cream; no halo, ring or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A gentle close on the very old man's serene resting face, at complete "
            "peace as if in a deep untroubled sleep, warm merciful evening light "
            "resting softly upon him — the very picture of rest and not terror, of a "
            "life received home with mercy and not anger. Calm, warm, comforted. "
            "Ordinary-sized, one head; the warm light rests on his peaceful face, not "
            "around his head; nothing written anywhere."
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

# No image REFS: SOLOMON, YOUTH and ELDER are each carried by a byte-identical text
# lock (no face sheet exists). NO Jesus and NO cream in this row.
REFS = {
}
