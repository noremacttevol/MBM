#!/usr/bin/env python3
"""V2 beat map — row 190, build-190-faith-without-works (James 2:14-26 — "faith, if it
hath not works, is dead, being alone"; the brother/sister with no clothes or food; Abraham
offering Isaac; Rahab hiding the spies; "faith without works is dead also").

COVERAGE: 12 pictures over 45.480 s (card_start) = ~3.79 s/picture (lesson 12
movie-coverage). Cut like a short film — no group portraits. JAMES writing the letter is
the frame; his teaching is illustrated by everyday need (the poor brother and sister), by
Abraham on the altar, and by Rahab at the window; ONE believer carries the human arc from
DEAD faith (idle, gives nothing) to LIVING faith (rises and serves).

=====================================================================
OPEN CAMERON COMPLAINT (v2_outline.py 190): NONE. COMPLAINT LEDGER below is empty.
=====================================================================

SPEAKER LAW (see make_narration.py — James's epistle, NOT a Gospel):
  s1   James 2:17  "Even so faith, if it hath not works, is dead, being alone."  SCRIPTURE → BLUE
  s26  James 2:26  "For as the body without the spirit is dead, so faith without works is dead also."  SCRIPTURE → BLUE
Every other segment (n0, n1, n2, n3, n4a, n4b, card) is the NARRATOR → white. There is NO
red-letter and NO God-voice in this row — James quotes no words of Jesus and God never
speaks. **JESUS IS NOT IN THIS STORY: every beat jesus=False, and NO ONE wears cream or
white** (cream is reserved for Jesus, who is absent here).

**HARD GATE — GOD / THE FATHER IS NEVER EMBODIED.** Abraham's obedience and Rahab's
deliverance are carried by the PEOPLE and their acts and by warm natural light — never by
any divine figure, face, hand, throne, beam-as-person, dove or symbol. No halo, ring or
rim-light around anyone (drift-word gate — word light as warm / plain daylight).

CONTENT-CARE — ABRAHAM & ISAAC (b06/b07): this is reverent OBEDIENCE and faith, NOT
horror. Isaac is bound but calm and trusting, unharmed; Abraham is grave, obedient and
loving with his eyes lifted to heaven. NEVER a knife at a throat, NEVER blood, NEVER a
terrified child, NEVER a wound. The willing faith-act only. RAHAB (b08/b09): concealment
and rescue, no violence, no threat to her shown; the scarlet cord at the window is the
saving act.

TIME-OF-DAY: warm plain daylight for James's room, the town, and Rahab's window; Moriah is
a clear high-country morning. No night scenes.

PLACES / LOCKS (all NEW build-local places — no committed plate yet; runner promotes each
from its first NON-Jesus frame, all frames are NON-Jesus here):
  JAMES-ROOM      the letter-writing frame (b01/b02) — promote from b01.
  TOWN-DOORWAY    everyday town where believers meet the needy (b03/b04/b05 = the
                  non-giving; b10/b11/b12 = the living service) — promote from b03.
  MORIAH-ALTAR    Abraham's altar of stones on the high place (b06/b07) — promote from
                  b06. (Runner may --wire an existing Moriah/altar plate from build-114/115
                  if the stash has one; else promote b06.)
  JERICHO-WINDOW  Rahab's house on the wall (b08/b09) — promote from b08.
People locks: JAMES (writer), BELIEVER (the "you" — idle→serving arc), NEEDY-PAIR (poor
brother & sister), ABRAHAM, ISAAC, RAHAB, SPIES. None wear cream or white.

AUDIO: default AUDIO LOCK stream-copy (no re-voice). Board Audio = OK. card_start =
45.480 s. Picture-only build — do NOT re-voice.
"""

# NEW build-local places + people are declared as text LOCKS here; PLACE_REFS stays empty
# and the runner promotes each place from its first NON-Jesus frame (see QC.md). No one
# wears cream/white (Jesus is absent).
LOCKS = {
    "JAMES-ROOM": (
        "JAMES-ROOM LOCK: the same place in every frame — a humble first-century room "
        "where James writes to the early church: plain lime-plastered stone walls, a low "
        "wooden writing table with a sheet of parchment, a reed pen and a small clay oil "
        "lamp unlit in warm daylight, a simple stool and a floor mat, one plain window "
        "opening to soft daylight. Ancient, spare and real; no modern object anywhere; any "
        "parchment is blank with no legible or rendered writing. The same room and warm "
        "daylight throughout."
    ),
    "TOWN-DOORWAY": (
        "TOWN-DOORWAY LOCK: the same place in every frame — an ordinary first-century town "
        "lane by the doorway of a modest stone house: dressed-stone walls, a worn timber "
        "door, a few clay jars and a basket on the threshold, a strip of dusty street and "
        "a low wall beyond, all in warm plain daylight. A plain everyday place where "
        "neighbours pass and the poor sit. Ancient and real; no modern object anywhere, "
        "and nothing legible or rendered is written on any surface. The same lane and "
        "daylight throughout."
    ),
    "MORIAH-ALTAR": (
        "MORIAH-ALTAR LOCK: the same place in every frame — a rough altar of unhewn stones "
        "stacked on a bare high place of Moriah, dry grass and scattered rock around it, "
        "a few sticks of wood laid on top, distant hills and a clear high-country morning "
        "sky beyond. Reverent, austere and open. Ancient and real; no modern object "
        "anywhere, and nothing written. The same high place and clear morning throughout."
    ),
    "JERICHO-WINDOW": (
        "JERICHO-WINDOW LOCK: the same place in every frame — the interior of Rahab's "
        "house built against the wall of Jericho: rough mud-brick and stone walls, stalks "
        "of drying flax stacked on the flat roof, a single deep window opening high over "
        "the city wall to the country outside, warm daylight slanting in. Ancient and real; "
        "no modern object anywhere, and nothing written. The same house and daylight "
        "throughout."
    ),
    "JAMES": (
        "JAMES LOCK: the same man in every frame he appears — James, an earnest "
        "first-century elder of the church of about fifty, warm olive-brown skin, dark "
        "hair greying at the temples, a full dark-grey beard, steady grave eyes, in a "
        "plain undyed brown-and-grey wool robe (never cream, never white). A plain-spoken "
        "teacher, sober and warm. The same face, beard and robe throughout."
    ),
    "BELIEVER": (
        "BELIEVER LOCK: the same man in every frame he appears — the ordinary believer the "
        "letter addresses, about thirty-five, warm olive-brown skin, short dark hair, a "
        "neat short dark beard, in a plain undyed tan-and-brown wool tunic and mantle "
        "(never cream, never white). Early he is idle and comfortable; later he rises and "
        "serves. The same face, beard, build and clothing throughout."
    ),
    "NEEDY-PAIR": (
        "NEEDY-PAIR LOCK: the same poor brother and sister in every frame they appear — "
        "two thin, cold, hungry first-century poor people, a man and a woman of about "
        "thirty, in worn threadbare grey rags too little for the weather, barefoot, "
        "hollow-cheeked but dignified, not grotesque. The same two people throughout; "
        "never cream or white."
    ),
    "ABRAHAM": (
        "ABRAHAM LOCK: an aged first-century patriarch, about a hundred, deeply lined "
        "sun-browned face, long white beard and white hair, grave loving eyes, in a plain "
        "weathered earth-brown robe (never cream, never white). Obedient, sorrowful and "
        "faithful. The same man throughout."
    ),
    "ISAAC": (
        "ISAAC LOCK: Abraham's son, a gentle young man of about fifteen, olive-brown skin, "
        "dark hair, no beard or a first faint beard, calm and trusting, in a plain "
        "undyed tan tunic (never cream, never white). Unharmed and serene throughout."
    ),
    "RAHAB": (
        "RAHAB LOCK: the same woman in every frame she appears — a resourceful "
        "first-century Canaanite woman of Jericho, about thirty, warm tan skin, dark hair "
        "bound in a coloured headscarf, keen brave eyes, in a modest russet-and-ochre robe "
        "(never cream, never white). Brave and quick. The same woman throughout."
    ),
    "SPIES": (
        "SPIES LOCK: two Israelite spies, ordinary travel-worn men of about thirty-five in "
        "dusty grey-brown travelling cloaks (never cream, never white); wary and grateful. "
        "The same two men in both frames they appear."
    ),
}

REF = False

BEATS = [
    {
        "id": "v2-r190-b01", "out": "s01-james-writes.jpeg", "seg": "n0",
        "window": "0.000-3.200", "wide": True, "jesus": False, "ref": False,
        "locks": ["JAMES-ROOM", "JAMES"],
        "narration": "James wrote plainly to the early church:",
        "must_show": "the establishing frame, NON-Jesus (the JAMES-ROOM plate) — James seated at his low writing table in warm daylight, reed pen in hand over a blank parchment, writing plainly and earnestly to the early church.",
        "must_not_show": "no Jesus and no one in cream or white; no God or Father figure; no legible or rendered writing on the parchment; no halo, glare or rim-light; no modern object; not a cartoon; not a posed line facing the lens.",
        "scene": (
            "An establishing shot of James's humble writing room in warm daylight, camera "
            "set low and behind James's shoulder looking past him toward the sunlit window, "
            "so his back is three-quarters to the lens and his gaze goes down onto the "
            "parchment and out to the window, never to the camera: James — an earnest "
            "grey-bearded elder in plain brown-grey wool (not cream) — sits at his low "
            "wooden table, reed pen in hand over a blank parchment, writing plainly to the "
            "early church. A small unlit clay lamp and a window of soft daylight. Ancient "
            "and spare; the parchment carries nothing legible; warm daylight rests on him, "
            "not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b02", "out": "s02-faith-only-in-the-head.jpeg", "seg": "n0",
        "window": "3.200-5.906", "wide": False, "jesus": False, "ref": False,
        "locks": ["JAMES-ROOM", "BELIEVER"],
        "narration": "a faith that stays only in the head is already dead.",
        "must_show": "a close on the BELIEVER seated idle and comfortable, nodding along in agreement but doing nothing — a faith that stays only in the head, unmoving; hands folded and still.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A close on the believer — an ordinary man in plain tan-brown wool (not cream) "
            "— seated idle and comfortable in the warm daylit room, nodding along in quiet "
            "agreement yet doing nothing, his hands folded and still: a faith that stays "
            "only in the head, unmoving. Ordinary-sized, one head, gaze inward and not to "
            "the camera; warm daylight on him, not around his head; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r190-b03", "out": "s03-no-clothes-no-food.jpeg", "seg": "n1",
        "window": "5.906-10.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN-DOORWAY", "NEEDY-PAIR"],
        "narration": "He asked the sharp question — if a brother or sister has no clothes and no food,",
        "must_show": "the NEEDY-PAIR (the TOWN-DOORWAY plate, NON-Jesus) — a poor brother and sister sitting cold and hungry by the town doorway, thinly clad in worn rags, no clothes to warm them and no food, dignified in their need.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no grotesque or degrading depiction; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "In the warm daylit town lane, a poor brother and sister — thin, cold and "
            "hungry in worn threadbare grey rags, barefoot, hollow-cheeked but dignified — "
            "sit together by the modest stone doorway with an empty basket, plainly "
            "without clothes to warm them or food to eat. Ancient and real; ordinary-sized, "
            "one head each, gazes low and weary and not to the camera; warm daylight on "
            "them, not around their heads; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b04", "out": "s04-wish-them-well-give-nothing.jpeg", "seg": "n1",
        "window": "10.500-15.879", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN-DOORWAY", "BELIEVER", "NEEDY-PAIR"],
        "narration": "and you wish them well but give nothing, what good is that?",
        "must_show": "a two-shot — the comfortable BELIEVER pausing to speak a kind blessing to the needy pair but turning away with full hands and giving nothing; his mouth kind, his hands closed; the poor still cold behind him.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A two-shot in the town lane: the comfortable believer in tan-brown wool (not "
            "cream) pauses by the poor brother and sister to speak a warm, kind blessing — "
            "but he holds a full basket close and turns to go, his hands closed, giving "
            "them nothing; the two poor people remain cold and empty-handed behind him. "
            "Ordinary-sized people on one street, one head each, the believer's gaze "
            "turning away and the poor watching, none to the camera; warm daylight, no "
            "ring of light around any head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b05", "out": "s05-faith-alone-is-dead.jpeg", "seg": "s1",
        "window": "15.879-21.056", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN-DOORWAY", "BELIEVER"],
        "narration": "Even so faith, if it hath not works, is dead, being alone.",
        "must_show": "BLUE caption (SCRIPTURE — James 2:17) — the believer standing alone in the empty lane after giving nothing, his kind words hanging empty, the poor gone unhelped; his open hand held out but empty — faith alone, and dead.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A quiet shot of the believer standing alone in the now-empty town lane, his "
            "kind words spent and the poor gone unhelped — one hand held open but empty at "
            "his side, his face troubled. Plain tan-brown wool (not cream). The emptiness "
            "of the lane says it: faith alone, and dead. Ordinary-sized, one head, gaze "
            "down and not to the camera; warm daylight, not a ring of light around his "
            "head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b06", "out": "s06-abraham-obeys.jpeg", "seg": "n2",
        "window": "21.056-24.300", "wide": False, "jesus": False, "ref": False,
        "locks": ["MORIAH-ALTAR", "ABRAHAM"],
        "narration": "Then he pointed to Abraham, who showed his faith by what he did —",
        "must_show": "ABRAHAM (the MORIAH-ALTAR plate, NON-Jesus) — the aged patriarch on the bare high place, laying wood on the rough stone altar with grave, obedient resolve; showing his faith by what he does, not merely says.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure, hand or beam; no violence, no knife, no blood; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "On the bare high place of Moriah in clear morning light, aged Abraham — white "
            "beard, weathered earth-brown robe (not cream) — lays sticks of wood on a rough "
            "altar of unhewn stones with grave, obedient resolve, showing his faith by what "
            "he does. Distant hills beyond. No divine figure appears. Ordinary-sized, one "
            "head, gaze on his work and lifted toward heaven, not to the camera; clear "
            "morning light on him, not around his head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b07", "out": "s07-offering-his-son.jpeg", "seg": "n2",
        "window": "24.300-27.228", "wide": False, "jesus": False, "ref": False,
        "locks": ["MORIAH-ALTAR", "ABRAHAM", "ISAAC"],
        "narration": "offering his son on the altar.",
        "must_show": "reverent OBEDIENCE (content-care) — Isaac calm and trusting, bound but unharmed, resting on the wood of the altar; Abraham beside him, one hand gentle on his son and his eyes lifted to heaven in obedient faith. The willing offering, never harm.",
        "must_not_show": "NO knife at a throat, NO raised blade striking, NO blood, NO wound, NO terror on the boy; no Jesus and no one in cream or white; no God figure, hand or beam; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "On the Moriah altar in clear morning light, Isaac — a gentle trusting youth in "
            "a plain tan tunic (not cream) — lies calm and unharmed on the wood, loosely "
            "bound; aged Abraham stands beside him, one hand resting gently and lovingly on "
            "his son, his grave face and eyes lifted to heaven in obedient faith, offering "
            "his son to God. There is no blade raised, no violence, no blood — only "
            "reverent obedience. No divine figure appears. Ordinary-sized figures on one "
            "high place, one head each, gazes to heaven and to the son, not to the camera; "
            "morning light on them, not around their heads; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b08", "out": "s08-rahab-hides-the-spies.jpeg", "seg": "n3",
        "window": "27.228-30.400", "wide": False, "jesus": False, "ref": False,
        "locks": ["JERICHO-WINDOW", "RAHAB", "SPIES"],
        "narration": "And to Rahab, who hid the spies",
        "must_show": "RAHAB (the JERICHO-WINDOW plate, NON-Jesus) — Rahab quickly hiding the two Israelite spies under the stalks of drying flax on her roof, glancing back toward the door; concealment and courage.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no violence or threat shown; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "Inside Rahab's house against the Jericho wall, warm daylight slanting in: "
            "Rahab — a brave woman in a russet-and-ochre robe and coloured headscarf (not "
            "cream) — quickly draws stalks of drying flax over the two travel-worn "
            "Israelite spies crouched low on the flat roof, hiding them, glancing back "
            "toward the door. Ancient and real; ordinary-sized people, one head each, "
            "gazes wary and not to the camera; warm daylight, no ring of light around any "
            "head; nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b09", "out": "s09-righteous-by-her-action.jpeg", "seg": "n3",
        "window": "30.400-33.488", "wide": False, "jesus": False, "ref": False,
        "locks": ["JERICHO-WINDOW", "RAHAB", "SPIES"],
        "narration": "and was counted righteous by her action, not just her words.",
        "must_show": "Rahab's saving ACT — letting the two spies down safely by a scarlet cord from the deep window over the city wall; her deed, not merely her words, counts her righteous.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no violence; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "At Rahab's deep window high over the Jericho wall in warm daylight, Rahab "
            "braces and lowers the two spies to safety on a scarlet cord down the outer "
            "wall to the country below — her brave deed, not just her words. Russet robe "
            "(not cream). Ordinary-sized figures, one head each, gazes on the cord and the "
            "descent, not to the camera; warm daylight, no ring of light around any head; "
            "nothing is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b10", "out": "s10-faith-and-works-alive.jpeg", "seg": "s26",
        "window": "33.488-39.403", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN-DOORWAY", "BELIEVER", "NEEDY-PAIR"],
        "narration": "For as the body without the spirit is dead, so faith without works is dead also.",
        "must_show": "BLUE caption (SCRIPTURE — James 2:26) — the LIVING answer: the believer now kneeling to give a warm cloak and bread to the poor brother and sister, faith and works joined and alive; his hands doing what his words believed.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "Back in the warm daylit town lane, the believer — plain tan-brown wool (not "
            "cream) — now kneels before the poor brother and sister and lays a warm cloak "
            "over the shivering sister's shoulders and sets bread into the brother's hands; "
            "faith and works joined and alive. The poor pair look up with relief. "
            "Ordinary-sized people on one street, one head each, gazes on the giving and "
            "not to the camera; warm daylight, no ring of light around any head; nothing "
            "is written anywhere."
        ),
    },
    {
        "id": "v2-r190-b11", "out": "s11-belief-that-moves.jpeg", "seg": "n4a",
        "window": "39.403-42.968", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN-DOORWAY", "BELIEVER"],
        "narration": "Belief that never moves a muscle isn't belief yet.",
        "must_show": "the believer risen and in motion — up off the ground and turning to keep serving, belief that has become action; his whole body engaged, not idle.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "In the warm daylit lane, the believer rises to his feet and turns, sleeves "
            "pushed back, already reaching to help further — belief that has moved from the "
            "head into the hands and feet, no longer idle. Plain tan-brown wool (not "
            "cream). Ordinary-sized, one head, gaze toward the work ahead and not to the "
            "camera; warm daylight on him, not around his head; nothing is written "
            "anywhere."
        ),
    },
    {
        "id": "v2-r190-b12", "out": "s12-faith-and-life-together.jpeg", "seg": "n4b",
        "window": "42.968-45.480", "wide": False, "jesus": False, "ref": False,
        "locks": ["TOWN-DOORWAY", "BELIEVER", "NEEDY-PAIR"],
        "narration": "Faith and life belong together.",
        "must_show": "the closing image — the believer and the once-poor pair now side by side in ordinary life, warmed and fed, the believer's faith and daily life joined and whole; quiet gladness.",
        "must_not_show": "no Jesus and no one in cream or white; no God figure; no halo, glare or rim-light; no modern object; nothing written; not a cartoon.",
        "scene": (
            "A closing warm shot in the daylit lane: the believer stands with the brother "
            "and sister he has clothed and fed, now warmed and steadier, the three together "
            "in ordinary life — his faith and his daily living joined and whole. Plain "
            "wool robes, none cream or white. Ordinary-sized people on one street, one head "
            "each, gazes easy and toward one another, not to the camera; warm daylight, no "
            "ring of light around any head; nothing is written anywhere."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# JAMES-ROOM, TOWN-DOORWAY, MORIAH-ALTAR and JERICHO-WINDOW are all NEW places — no
# committed plate yet. The runner promotes each from its first NON-Jesus frame (all frames
# here are NON-Jesus): JAMES-ROOM from b01, TOWN-DOORWAY from b03, MORIAH-ALTAR from b06,
# JERICHO-WINDOW from b08. MORIAH-ALTAR may instead reuse an existing Moriah/altar plate
# from the stash (build-114/115) via `v2_stash.py --wire` if one is suggested. Steps in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===

# No image REFS: all places and people are carried by the build-local text locks above.
# Jesus does not appear in this row (every beat jesus=False); no one wears cream or white.
REFS = {
}
