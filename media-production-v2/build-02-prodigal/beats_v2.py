#!/usr/bin/env python3
"""V2 beat map — row 2, build-02-prodigal (Luke 15:11-32) — REALISTIC REBUILD.

Consumed by media-production-v2/v2_prompt.py (--check/--dump) and
media-production-v2/v2_gen_api.py (generation). STYLE-V2, the QUALITY LOCK, the
anti-panel clause and JESUS LOCK v5 are prepended by the assembler so they stay
byte-identical across every prompt.

REALISTIC REBUILD (Session 7, 2026-08-01). The 24 stills in `assets/` are the
2026-07-28/29 set that falls under the Session 6 blanket rejection of the old
V2 look. They are kept untouched as ROUGH-DRAFT composition references — the
row-2 reroll war fixed camera direction, travel direction and wardrobe in them,
and those lessons are preserved — while the realistic set generates fresh at
native 2K into `assets-realistic/`. Per the Session 6 root-cause list, every
beat now states: the DIRECTION its light comes from, a real-lens feel, people
caught MID-ACTION rather than posed, the ONE emotion the beat exists for, and
that NOBODY looks at the camera.

TIMING: windows recomputed 2026-08-01 from extract_beats.py (the fixed version
that reads this build's own timeline formulas) — absolute audio phrase times,
card at 146.07 s, total 157.85 s, matching the shipped V1 cut.

COVERAGE (STORY-COVERAGE-LAW): 24 pictures, against V1's 10 unique stills.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Luke 15 KJV):
  v1-2   publicans and sinners drew near to HEAR him; Pharisees and scribes
         MURMURED, "This man receiveth sinners, and eateth with them." So the
         frame-story shows Jesus at a table AMONG them, gazes on him, the
         religious men apart and displeased.
  v12    "Father, give me the portion of goods that falleth to me" — the ask.
  v13    took his journey into a FAR country; wasted his substance.
  v14    a mighty famine; he began to be in want.
  v15-16 sent into the fields to FEED SWINE; would fain have filled his belly
         with the husks the swine did eat; NO MAN GAVE UNTO HIM.
  v17    "he came to himself" — the realization is IN the pigsty.
  v18-19 the rehearsed speech (j3, red).
  v20    "when he was yet A GREAT WAY OFF, his father saw him, and had
         compassion, and RAN, and fell on his neck, and kissed him."
  v22    "the BEST ROBE ... a RING on his hand, and SHOES on his feet."
  v23    the fatted calf; merriment.
  v25    elder son was IN THE FIELD; coming near the house he HEARD MUSICK
         AND DANCING; v26 asked a SERVANT what these things meant.
  v28    "he was ANGRY, and would not go in: therefore came his father OUT,
         and INTREATED him."
  v29    the elder son's complaint (j4, red).
  v31-32 "Son, thou art ever with me..." — the story ENDS at the open door,
         unresolved; the parable never says whether he went in.

CONTENT-CARE: row 2 is not in the §3 flag table = GREEN. Restraint applied
anyway: the far-country "riotous living" is never depicted — no party scene,
nothing lewd; the squandering is carried by the departure and by the emptiness
after (money gone, famine, pigs). The pigsty shows hunger and mud, never
degradation played for spectacle.

TIME-OF-DAY ARC (self-consistent; the parable states none):
  frame story = mid-morning sun with real shadows · ask/departure = morning ·
  famine/pigs = harsh midday · road home + rehearsal = late afternoon · father
  sees / runs / embrace = golden late afternoon · robe and feast = warm evening
  lamplight · elder brother arc = dusk into night, torchlit doorway.
"""

from pathlib import Path

OUTPUT_ASSET_DIR = "assets-realistic"
OUTPUT_VIDEO_NAME = "luke-15_prodigal-son-realistic-v2.mp4"

# Identity anchors by IMAGE (CAST-BIBLE principle; row-2 CAST-DRIFT lesson —
# the elder son came back as three different men on text locks alone). These
# are the accepted row-2 identity stills; each character has ONE canonical
# anchor and every beat naming his lock attaches it automatically.
REFS = {
    "FATHER": "CAST-REF-V2/father-ref.jpeg",
    "YOUNGER": "CAST-REF-V2/younger-ref.jpeg",
    "ELDER": "CAST-REF-V2/elder-ref.jpeg",
}

LOCKS = {
    # Jesus appears ONLY in the two frame-story shots (b01, b02). Inside the
    # parable he is the storyteller, not a figure — nobody in the parable wears
    # cream (only-Jesus-cream law).
    # PHARISEES LOCK v2 (row 2 QC, CREAM-CROWD recurrence): colours stated
    # POSITIVELY and anchored against the frame. Negations do not hold.
    "PHARISEES": (
        "PHARISEES LOCK: the religious men are the same three in both shots — older "
        "scribes with long grey-streaked beards, in DARK CHARCOAL-BROWN and DEEP "
        "UMBER scholarly robes. Their prayer shawls are woven from the SAME "
        "SATURATED DARK wool as their robes — deep charcoal, dark umber and "
        "near-black, with dark indigo stripes and dark fringe — so that every shawl "
        "is plainly DARKER than the sunlit stone wall behind them. They stand "
        "stiffly together, faces tight with disapproval."
    ),
    "TABLE": (
        "TABLE LOCK: a low stone courtyard off a Galilean street in mid-morning "
        "sun that comes from ONE side and throws real shadows — a plain wooden "
        "table with bread, olives and clay cups, crowded by ordinary working men "
        "and women in SATURATED DEEP earth colours: dark chocolate brown, deep "
        "russet, burnt ochre, dark olive and dusty indigo wool. Each of them is a "
        "distinct individual caught mid-gesture — leaning in, tearing bread, "
        "setting a cup down — never a posed row of onlookers, and no one at the "
        "table looks toward the camera. No one at the table wears cream, "
        "off-white, ivory or any pale near-white cloth."
    ),
    "FATHER": (
        "FATHER LOCK: the father is the same man in every shot — a dignified "
        "landowner of about sixty, strong and upright, a full SILVER-GREY beard, "
        "deep-lined warm face, thick grey hair, dark eyes. He wears a DEEP "
        "INDIGO-BLUE wool robe with a woven border over a warm umber tunic, a wide "
        "cloth sash, leather sandals (never cream, never white). His face is shown "
        "clearly and he never looks toward the camera."
    ),
    # The story CHANGES the younger son's clothing (fine cloak -> rags -> the
    # best robe), so his lock fixes only face, hair and build; each beat states
    # his clothing and its condition. A lock must never argue with a beat.
    "YOUNGER": (
        "YOUNGER SON LOCK: the younger son is the same man in every shot — early "
        "twenties, lean, warm olive-brown skin, short DARK CURLY hair, a sparse "
        "young dark beard, expressive dark eyes, a light frame next to his father. "
        "He never wears cream or white. His face is shown clearly and he never "
        "looks toward the camera."
    ),
    "ELDER": (
        "ELDER SON LOCK: the elder son is the same man in every shot — late "
        "twenties, broader and taller than his brother, straight dark hair to the "
        "ears, a full trimmed dark beard, sun-darkened olive skin, hard-worked "
        "hands. He wears a DARK OLIVE-GREEN work tunic, dusty from the field, with "
        "a plain leather belt (never cream, never white). His face is shown "
        "clearly and he never looks toward the camera."
    ),
    "ESTATE": (
        "ESTATE LOCK: the father's farm — a broad stone farmhouse with a walled "
        "courtyard and a heavy wooden gate on a low hill, olive trees and terraced "
        "vines around it, a long pale dirt road running down the valley toward the "
        "horizon, Judean hills beyond. The household servants wear plain dark "
        "earth-brown and grey-brown wool; no one wears cream, off-white or any "
        "pale near-white cloth."
    ),
    # Realistic-cinematography lock, byte-identical wherever named: the Session 6
    # rejection was flat noon light, posed extras and camera-gaze on every frame.
    "CAMERA": (
        "CAMERA LOCK: photographed like a real film still on location with a real "
        "cinema lens — light arrives from ONE believable direction and models "
        "faces with true shadow, shallow depth of field holds the subject sharp "
        "while the background falls gently away, and every person is caught "
        "mid-action in a truthful candid instant, never posed, never lined up, "
        "and NEVER looking at the camera."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r002-b01", "out": "s01-they-murmured.jpeg", "seg": "n0 p1",
        "window": "0.28-4.88", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "PHARISEES", "TABLE"],
        "narration": ("When religious men complained that Jesus spent his time "
                      "with sinners,"),
        "must_show": "Jesus AT the table among publicans and sinners; the Pharisees apart, murmuring. The ONE emotion of this frame: the tension between the table's warmth and the wall's disapproval.",
        "must_not_show": "no halo/glow; Jesus not detached at the frame edge — the table's gazes are on him; nobody looks at the camera; not flat noon light.",
        "scene": (
            "Jesus sits at the crowded table among the publicans and sinners, at "
            "their level, at ease, caught mid-sentence with a piece of broken bread "
            "still in one hand, and every face at the table is turned toward him, "
            "listening — a tax collector leaning in on his elbows, a woman pausing "
            "with a cup half-poured. Off to one side, in the shade of the wall, the "
            "three religious men stand apart with their heads bent together, "
            "murmuring, their eyes fixed on him in disapproval. The morning sun "
            "rakes in low from beyond the wall so the table sits in warm side-light "
            "and the murmuring men stand in cool shadow. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b02", "out": "s02-he-answered-with-a-story.jpeg", "seg": "n0 p2",
        "window": "4.88-9.47", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "PHARISEES", "TABLE"],
        "narration": ("he didn't argue with them. He answered with a story, about "
                      "a father and his two sons."),
        "must_show": "Jesus beginning the story — calm, open gesture toward the religious men; the whole courtyard turning to listen, Pharisees included.",
        "must_not_show": "no anger on his face; no halo/glow; nobody looks at the camera.",
        "scene": (
            "Jesus has half-risen at the table and begun to speak, one open hand "
            "lifted mid-gesture in the easy manner of a storyteller, his face calm "
            "and warm, his eyes on the religious men across the courtyard as he "
            "speaks to them. Around him the whole table has turned mid-movement to "
            "listen — one man still chewing, another's cup stopped halfway to his "
            "mouth — and even the three religious men have gone still in their "
            "shadow, caught by the story despite themselves. The same low morning "
            "side-light models every face. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r002-b03", "out": "s03-the-ask.jpeg", "seg": "n1 p1",
        "window": "9.47-15.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "YOUNGER", "ESTATE"],
        "narration": ("The younger son asked for his inheritance early — as if to "
                      "say he wished his father were already dead."),
        "must_show": "the son demanding, palm out; the father's stricken, wounded stillness. The ONE emotion: the quiet wound landing.",
        "must_not_show": "no shouting match; the wound is quiet; morning light with real shadows; neither man looks at the camera.",
        "scene": (
            "In the farmhouse courtyard in early morning light that comes low over "
            "the wall and throws long shadows across the dust, the younger son "
            "stands before his seated father with his open palm held out, chin "
            "lifted, wearing a fine RUST-RED wool tunic and a good travel cloak — "
            "and the father sits very still on the stone bench, his hands resting "
            "on his knees, his lined face quietly stricken, looking up at his boy. "
            "A leather money chest sits open beside the father, its coins catching "
            "the morning sun. Exactly two people are in the frame; each has two "
            "arms, two hands of five fingers each, two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b04", "out": "s04-he-left.jpeg", "seg": "n1 p2",
        "window": "15.50-20.06", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "YOUNGER", "ESTATE"],
        "narration": "Then he left, and poured it all out on a life that emptied him.",
        "must_show": "the son walking away down the long road with his bag; the father watching him go from the gate. The ONE emotion: being left.",
        "must_not_show": "no party scene, nothing of the riotous living depicted; the leaving carries it; the son's face must NOT be visible — he faces away up the road.",
        "scene": (
            "SHOT FROM BEHIND THE FATHER, the camera at the courtyard gate looking "
            "DOWN the long pale dirt road as it runs away from the farm toward "
            "distant hills. In the near foreground, seen from behind and slightly "
            "to one side and softly out of the depth of field, the father stands "
            "alone in the open gateway, one hand resting on the gatepost, head and "
            "shoulders turned to watch. Far down the road ahead of him, sharp in "
            "the lens's focus, the younger son is SEEN FROM DIRECTLY BEHIND — the "
            "back of his head, the back of his shoulders and his heels toward the "
            "camera, HIS FACE ENTIRELY HIDDEN FROM US because he is facing away up "
            "the road, walking off into the distance mid-stride and never once "
            "looking back. He is already small with distance, a full travel bag "
            "over his shoulder and the heavy money pouch at his belt, his fine "
            "RUST-RED tunic and travel cloak bright with morning. He is leaving; "
            "the road carries him toward the far horizon and the farm is behind "
            "him. Morning light from the east side, long shadows across the road. "
            "Exactly two people are in the frame; each has two arms, two hands, "
            "two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b05", "out": "s05-money-gone-famine.jpeg", "seg": "n2 p1",
        "window": "20.06-22.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "YOUNGER"],
        "narration": "When the money was gone, a famine came.",
        "must_show": "alone in a strange dusty town, empty purse, want beginning. The ONE emotion: the bottom falling out.",
        "must_not_show": "no companions (no man gave unto him); no drunkenness shown; he does not look at the camera.",
        "scene": (
            "In a strange far-country town under a harsh dusty midday sky, the "
            "younger son sits alone against a mud-brick wall in its thin strip of "
            "hard shadow, his once-fine rust-red tunic now dirty and worn, holding "
            "his empty leather purse upside down in one hand — nothing left in it — "
            "his eyes down on the purse, not on us. The hard overhead sun bleaches "
            "the parched street behind him, where market stalls stand bare with "
            "famine, soft in the shallow depth of field. Nobody looks at him. "
            "Exactly one person is in the foreground, with two arms, two hands of "
            "five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b06", "out": "s06-feeding-pigs.jpeg", "seg": "n2 p2",
        "window": "22.37-26.58", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "YOUNGER"],
        "narration": ("He ended up feeding pigs, so hungry he would have eaten "
                      "what they ate."),
        "must_show": "him IN the pigsty with the swine, ragged, mid-pour, staring at the husks in the trough with real hunger. The ONE emotion: hunger that has crossed a line.",
        "must_not_show": "no degradation played for spectacle; his dignity is wrecked but he is a human being; no one else present; he does not look at the camera.",
        "scene": (
            "In a muddy stone-fenced pigsty under a hard midday sun that beats "
            "straight down and pools black shadow under the animals, the younger "
            "son stands ankle-deep among several rooting pigs, his rust-red tunic "
            "torn, faded and filthy, caught mid-motion tipping husk pods from a "
            "wooden bucket into the trough — and his hollow eyes are fixed on the "
            "husks themselves, his free hand pressed against his empty stomach. "
            "Dust and flies hang in the heat haze. He is utterly alone; no other "
            "person anywhere. Exactly one person is in the frame, with two arms, "
            "two hands of five fingers each, two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b07", "out": "s07-came-to-his-senses.jpeg", "seg": "n2 p3",
        "window": "26.58-30.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "YOUNGER"],
        "narration": "And there, in the mud, he came to his senses.",
        "must_show": "the realization — kneeling in the mire, head lifting, the thought arriving (v17 'he came to himself'). The ONE emotion: clarity arriving in the worst place.",
        "must_not_show": "no light beam, no glow; the change is on his face only; he looks up and away, never at the camera.",
        "scene": (
            "Close on the younger son sunk to one knee in the churned mud of the "
            "stone-fenced pigsty, the hard midday sun cutting across his face from "
            "one side so the new clarity in his eyes catches the light while his "
            "hollow cheek stays in shadow. He still wears the SAME torn, faded, "
            "filthy RUST-RED tunic and is barefoot, one hand braced on the low "
            "stone fence, his head just lifting, gaze gone far past the sty — the "
            "realization arriving on his gaunt dirty face: his father's hired "
            "servants have bread enough. Two dark pigs root in the mud at the soft "
            "edge of the shallow focus. The change is entirely in his face; "
            "nothing else in the frame changes. Exactly one person is in the "
            "frame, with two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b08", "out": "s08-walking-home.jpeg", "seg": "n3",
        "window": "30.34-34.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "YOUNGER"],
        "narration": "So he started walking home, rehearsing a speech the whole way.",
        "must_show": "the long road home, mid-stride, lips moving with the rehearsal. The ONE emotion: dogged, frightened resolve.",
        "must_not_show": "the farm is not visible yet; he is far away still; he does not look at the camera.",
        "scene": (
            "The younger son walks a long empty dirt road through dry hill country "
            "in late-afternoon light that comes low from his left and drags his "
            "shadow long across the ruts, ragged and barefoot in his torn faded "
            "rust-red tunic, a walking stick in one hand, caught mid-stride with "
            "his lips visibly moving as he rehearses his speech to himself, his "
            "brow working, eyes on the road ahead. The road runs on ahead of him "
            "toward far hills; no buildings anywhere yet. Exactly one person is in "
            "the frame, with two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b09", "out": "s09-the-rehearsed-speech.jpeg", "seg": "j3",
        "window": "34.80-49.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "YOUNGER"],
        "narration": ("I will arise and go to my father... make me as one of thy "
                      "hired servants. (Luke 15:18-19)"),
        "must_show": "his face carrying the whole speech — shame, resolve, the words costing him. The ONE emotion: shame saying the words anyway.",
        "must_not_show": "no tears streaming; restrained; late afternoon; he does not look at the camera.",
        "scene": (
            "A tight shot of the younger son paused at a rise in the road, the low "
            "late-afternoon sun warm on one side of his gaunt face and the other "
            "side falling into shadow, still in the SAME torn, faded, filthy "
            "RUST-RED tunic and barefoot, eyes down, jaw tight, mid-word — shame "
            "and resolve fighting in his face as he practises the hardest sentence "
            "of his life. Far behind him, small and soft in the distance haze "
            "beyond the shallow focus, the first pale line of his home valley. "
            "Exactly one person is in the frame, with two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r002-b10", "out": "s10-father-saw-him.jpeg", "seg": "n4",
        "window": "49.99-53.71", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ESTATE"],
        "narration": "He was still a long way off... when his father saw him.",
        "must_show": "v20 — the father catching sight of a tiny far figure on the road; recognition seizing him. The ONE emotion: recognition like a physical blow.",
        "must_not_show": "the son is a DISTANT small figure, not close; the father has not started running yet; the father does not look at the camera.",
        "scene": (
            "SHOT FROM BESIDE AND SLIGHTLY BEHIND THE FATHER so that his face is "
            "seen in profile and the long pale road runs away from him into the "
            "distance ALONG HIS LINE OF SIGHT. He stands at the courtyard gate in "
            "golden late-afternoon light that comes from far down the road and "
            "lights the front of his face, one hand gripping the gatepost, his "
            "whole body suddenly gone rigid mid-turn, the other hand raised to "
            "shade his eyes as he stares FAR UP THE ROAD — and there, tiny with "
            "distance and directly ahead of his gaze, a single ragged figure is "
            "walking toward the farm. The father's lined face is caught in the "
            "first instant of recognition, and every line in the frame leads from "
            "his eyes down the road to that distant figure. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b11", "out": "s11-the-father-ran.jpeg", "seg": "n5a",
        "window": "53.71-55.53", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ESTATE"],
        "narration": "The father ran.",
        "must_show": "the icon of the story — an old man in full undignified RUN down the road, robe hitched, both feet off the ground. The ONE emotion: joy that cannot wait.",
        "must_not_show": "not a jog, not a stride — a RUN; sandals kicking dust; his face is turned down the road, never toward the camera.",
        "scene": (
            "SHOT FROM BEHIND THE FATHER AND LOW, his BACK to the camera, running "
            "AWAY FROM US straight down the long dirt road as it stretches ahead of "
            "him toward distant hills. A real photograph of a real elderly man, "
            "sharp and grainy with kicked-up dust hanging in the golden light "
            "behind his heels. The father is in full run, his deep indigo-blue "
            "robe hitched up in both fists above his knees, grey beard streaming, "
            "sandals hammering up dust, caught mid-stride with both feet clear of "
            "the ground. FAR AHEAD OF HIM DOWN THE SAME ROAD, small with distance "
            "and squarely IN THE DIRECTION HE IS RUNNING, the tiny ragged figure "
            "of his son comes up the road toward him. The two of them are closing "
            "the same stretch of road, and we are watching over the father's "
            "shoulder as the gap shrinks. Golden late-afternoon sun low ahead, "
            "flaring in the dust. Every figure has two arms, two hands, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r002-b12", "out": "s12-he-ran-anyway.jpeg", "seg": "n5b",
        "window": "55.53-61.16", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ESTATE"],
        "narration": ("Old men in that world did not run. It was beneath their "
                      "dignity. He ran anyway."),
        "must_show": "the scandal of it — household servants stopped dead, staring, as he tears past. The ONE emotion: astonishment.",
        "must_not_show": "no mockery on the servants' faces — pure astonishment; nobody looks at the camera.",
        "scene": (
            "SHOT FROM THE SIDE with the camera low beside the farm's outer wall: "
            "the father tears past from left to right at a full run, motion caught "
            "mid-stride, his deep indigo-blue robe still hitched up in both fists "
            "above his knees, heading AWAY down the road toward the distant "
            "figure. Two household servants in plain dark earth-brown wool have "
            "stopped dead where they stood, a dropped water jar shattering and "
            "spilling at one servant's feet, staring open-mouthed after their "
            "master, astonished to see the old man run. He pays them no mind; his "
            "eyes are locked on the far road ahead of him. Golden late-afternoon "
            "light rakes along the wall and catches the spray of the spilling "
            "water, real skin, real dust and real wool. Exactly three people are "
            "in the frame; each has two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r002-b13", "out": "s13-the-embrace.jpeg", "seg": "n6",
        "window": "61.16-66.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "YOUNGER", "ESTATE"],
        "narration": ("He didn't wait for the speech. He wrapped his arms around "
                      "his son before a single word was said."),
        "must_show": "v20 — fell on his neck; the son's stunned face over the father's shoulder, speech dying unspoken. The ONE emotion: being held before you can earn it.",
        "must_not_show": "the son's arms hang or barely rise — he expected a servant's place, not this; neither man looks at the camera.",
        "scene": (
            "On the open road in golden late-afternoon light, the low sun behind "
            "the pair edging the hanging dust with gold, NEITHER MAN LOOKING AT "
            "THE CAMERA — this is a collision, not a posed portrait. The father "
            "has COLLAPSED FORWARD INTO HIS SON, both arms wrapped right around "
            "the young man's back and locked there, pulling him hard against his "
            "chest so the two are pressed chest to chest, his silver-grey head "
            "buried down against the boy's filthy shoulder, his face hidden in "
            "the ragged cloth and his eyes squeezed shut — and over the father's "
            "shoulder the son's gaunt face is stunned open, his rehearsed words "
            "dying on his lips, his gaze gone somewhere over his father's back, "
            "his own arms only beginning to rise, hands not yet closed on his "
            "father's back, as if he cannot believe he is allowed to return the "
            "embrace. The son is still in the SAME torn, faded, filthy RUST-RED "
            "tunic and is BAREFOOT — he has not been given shoes yet. Dust still "
            "hangs from the run. Exactly two people are in the frame; each has "
            "two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b14", "out": "s14-robe-ring-shoes.jpeg", "seg": "n7 p1",
        "window": "66.77-71.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "YOUNGER", "ESTATE"],
        "narration": ("That night the father dressed him in the finest robe, put "
                      "a ring on his hand,"),
        "must_show": "v22 — the best robe going onto his shoulders, the ring onto his hand; a servant bringing sandals. The ONE emotion: restored sonship, undeserved and unhesitating.",
        "must_not_show": "the robe is deep wine-red, NOT cream or white; nobody looks at the camera.",
        "scene": (
            "In the farmhouse's hall that evening, lit warm from one side by a "
            "cluster of oil lamps whose flames throw soft moving shadow up the "
            "stone wall, the father with his own hands settles a magnificent DEEP "
            "WINE-RED robe onto his son's washed shoulders, caught in the exact "
            "moment of sliding a gold signet ring ONTO HIS SON'S outstretched "
            "finger — the ring is held pinched in the father's fingertips, "
            "halfway onto the SON's finger; the father's own hands wear NO ring "
            "of any kind — "
            "while a servant in dark earth-brown wool kneels fastening new leather "
            "sandals onto the son's feet. The son stands overwhelmed, looking down "
            "at the ring on his hand, lamplight warm on the wet of his eyes. "
            "Exactly three people are in the frame; each has two arms, two hands "
            "of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b15", "out": "s15-my-son-was-dead.jpeg", "seg": "n7 p2 + j1",
        "window": "71.50-81.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "YOUNGER", "ESTATE"],
        "narration": ("and called for a feast — and he told everyone why. / For "
                      "this my son was dead, and is alive again; he was lost, and "
                      "is found. (Luke 15:24)"),
        "must_show": "the feast alive; the father proclaiming with his hand on the son's shoulder; every face turned to them. The ONE emotion: public, unashamed joy.",
        "must_not_show": "nobody at the feast in cream; the son in the wine-red robe; nobody looks at the camera.",
        "scene": (
            "A TALL VERTICAL FRAME with the camera upright and level at standing "
            "eye height, every figure standing upright with their feet on the "
            "floor and their head above their shoulders. The farmhouse hall is "
            "alive with lamplight — a dozen small flames throwing warm layered "
            "light and true shadow — and a feast in full life: laden tables, "
            "musicians mid-note on pipe and drum, household and neighbours in "
            "deep russet, ochre, olive and indigo wool caught mid-laugh and "
            "mid-toast, each a distinct individual, none looking at the camera. "
            "At the head of it the father stands with one hand gripping his son's "
            "shoulder, the other arm flung wide mid-proclamation, his face "
            "shining in the lamplight. The son in the deep wine-red robe stands "
            "washed and overwhelmed at his father's side, and every face in the "
            "hall is turned toward the two of them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b16", "out": "s16-elder-in-the-field.jpeg", "seg": "n9 p1-p2",
        "window": "81.93-86.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "ELDER", "ESTATE"],
        "narration": "But Jesus wasn't finished. The older son was still out in the field, like always.",
        "must_show": "v25 — the elder son at work in the field at dusk, faithful, alone. The ONE emotion: unnoticed faithfulness.",
        "must_not_show": "the house lights are distant; he doesn't know yet; he does not look at the camera.",
        "scene": (
            "In the last blue-grey light of dusk, the fading western sky the "
            "only light left, the elder son works alone in a terraced field below the "
            "farm, caught with a heavy hoe mid-swing, his dark olive-green tunic "
            "dark with sweat and dust after a full day, his eyes on the ground he "
            "is breaking — and far up the hill behind him, soft beyond the "
            "shallow focus, the farmhouse windows are just beginning to warm with "
            "lamplight he has not yet noticed. Exactly one person is in the "
            "frame, with two arms, two hands of five fingers each, two legs and "
            "one head."
        ),
    },
    {
        "id": "v2-r002-b17", "out": "s17-musick-and-dancing.jpeg", "seg": "n9 p3",
        "window": "86.22-91.25", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "ELDER", "ESTATE"],
        "narration": ("When he came near the house and heard the music, a servant "
                      "told him: your brother is home."),
        "must_show": "v25-26 — stopped near the lit house, hearing it; the servant explaining; his face beginning to harden. The ONE emotion: the news landing wrong.",
        "must_not_show": "he is OUTSIDE, near the courtyard, not at the door yet; neither man looks at the camera.",
        "scene": (
            "In full night now, near the farmhouse's outer wall, the elder son "
            "stands stopped mid-step with his hoe still over his shoulder, head "
            "turned toward the house where every window pours warm light and the "
            "sound of pipes and dancing — while a young servant in plain "
            "earth-brown wool stands facing him holding a burning torch upright "
            "in one fist, the flame sitting directly on the head of the torch and "
            "touching it, and gestures toward the house with his free hand, "
            "explaining. The torch is the only close light, warm and unsteady on "
            "both faces, and in it the elder son's dusty face is beginning to "
            "harden as he understands. Exactly two people are in the frame; each "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b18", "out": "s18-would-not-go-in.jpeg", "seg": "n9 p4",
        "window": "91.25-94.82", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "ELDER", "ESTATE"],
        "narration": "And he was so angry, he refused to go in.",
        "must_show": "v28 — turned AWAY from the lit doorway, arms locked, jaw set; the feast light on his back. The ONE emotion: cold, hurt anger.",
        "must_not_show": "not screaming — cold, hurt anger; he does not look at the camera.",
        "scene": (
            "The elder son stands in the dark courtyard with his back to the "
            "farmhouse's open door, arms crossed hard over his chest, jaw set, "
            "eyes down and burning — the warm feast light and music spilling out "
            "of the doorway behind him so that the door's warm spill lands on "
            "his back and shoulders while his face stays in the dark, lit only "
            "faintly from one side by a torch on the far wall. He has planted himself; he is not "
            "going in. Exactly one person is in the frame, with two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r002-b19", "out": "s19-father-came-out.jpeg", "seg": "n10a",
        "window": "94.82-101.11", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ELDER", "ESTATE"],
        "narration": ("So the father left his own feast, and went out again — "
                      "this time to the son who had never left."),
        "must_show": "v28 — the father coming OUT through the lit door into the dark, toward the elder son; the second going-out of the story. The ONE emotion: the same love, going out again.",
        "must_not_show": "no rebuke in the father's posture — he comes to entreat; neither man looks at the camera.",
        "scene": (
            "The father steps out through the farmhouse's lamplit doorway into "
            "the dark courtyard, leaving his own feast behind him, caught "
            "mid-step with one hand still on the doorframe and the other already "
            "reaching gently toward the elder son, who stands apart in the "
            "shadows with his arms crossed, face turned away. The doorway light "
            "spills past the father into the dark between them, laying one warm "
            "path across the ground from his feet toward his son's, and warm "
            "torchlight touches real weathered skin, real grey beard hair and "
            "real coarse wool. Exactly two people are in the frame; each has two "
            "arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r002-b20", "out": "s20-the-hurt-poured-out.jpeg", "seg": "n10b",
        "window": "101.11-111.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ELDER", "ESTATE"],
        "narration": ("The older son's hurt poured out. All these years I have "
                      "served you. I never disobeyed you. And you never gave me "
                      "even a young goat, to celebrate with my friends."),
        "must_show": "the complaint in motion — the elder son gesturing with both hands, years of hurt; the father standing in it, listening. The ONE emotion: old hurt finally spoken.",
        "must_not_show": "the father does not argue back; he listens; neither man looks at the camera — they look at each other.",
        "scene": (
            "In the torchlit courtyard the elder son has turned on his father at "
            "last, caught mid-sentence with both work-hardened hands thrown out, "
            "his dusty face cracked open with years of hurt as the words pour "
            "out of him — and the father stands close and still in the doorway "
            "light, facing him, taking every word, his lined face full of sorrow "
            "and love, making no answer yet. The torch flame gutters between "
            "them, moving real shadow across both faces. The torches are mounted "
            "on the walls; nobody carries one. Exactly two people are in the "
            "frame — the father and the elder son only, with no servant, "
            "bystander, hand or partial third figure visible at any edge of the "
            "picture; each has two arms, two hands of five fingers each and one "
            "head."
        ),
    },
    {
        "id": "v2-r002-b21", "out": "s21-lo-these-many-years.jpeg", "seg": "j4",
        "window": "111.65-124.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ELDER"],
        "narration": ("Lo, these many years do I serve thee... and yet thou never "
                      "gavest me a kid, that I might make merry with my friends. "
                      "(Luke 15:29)"),
        "must_show": "tight on the elder son's face at the rawest of the complaint; the father's hand beginning to reach for his arm. The ONE emotion: the hurt under the anger showing through.",
        "must_not_show": "no contempt on either face — hurt on one, love on the other; neither man looks at the camera.",
        "scene": (
            "A tight two-shot in warm unsteady torchlight: the elder son's face "
            "fills one side of the frame in shallow focus, eyes wet with anger "
            "and old invisible hurt, mid-word, his gaze locked on his father — "
            "and from the other side his father's weathered hand is just arriving "
            "on his forearm, the father's face soft behind it in the falloff of "
            "the light, hearing him all the way to the end. Exactly two people "
            "are in the frame; each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r002-b22", "out": "s22-the-last-words.jpeg", "seg": "n11",
        "window": "124.95-130.06", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ELDER", "ESTATE"],
        "narration": ("The father didn't argue with him, either. Jesus gave him "
                      "the last words of the story."),
        "must_show": "the two of them face to face in the doorway light, the complaint spent, the father's hands on his shoulders. The ONE emotion: held, listened to, on the edge.",
        "must_not_show": "not reconciled yet — held, listened to, on the edge; neither man looks at the camera.",
        "scene": (
            "In the spill of warm light from the open farmhouse door the father "
            "now stands square in front of his elder son with both hands resting "
            "on the young man's shoulders, their faces close and turned only to "
            "each other, the son's anger spent into raw stillness, his arms "
            "fallen to his sides — the whole courtyard dark and quiet around the "
            "two of them, the feast a warm blur of light and murmur behind the "
            "door, soft beyond the shallow focus. Exactly two people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r002-b23", "out": "s23-all-that-i-have-is-thine.jpeg", "seg": "j2a",
        "window": "130.06-135.23", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ELDER"],
        "narration": "Son, thou art ever with me, and all that I have is thine. (Luke 15:31)",
        "must_show": "close on the father's face saying the tender sentence — all warmth, no rebuke. The ONE emotion: tenderness for the faithful one.",
        "must_not_show": "no tears streaming; deep, quiet tenderness; his eyes are on his son, never on the camera.",
        "scene": (
            "Close on the father's deeply lined face in warm torchlight that "
            "falls from one side and leaves the far cheek in soft shadow, his "
            "eyes steady and shining on his elder son's, the silver-grey beard "
            "framing the gentlest expression in the whole story — a father "
            "telling his faithful boy that everything he has is already his. The "
            "elder son's shoulder and jaw are just in frame at the soft edge of "
            "the focus, listening. Each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r002-b24", "out": "s24-the-open-door.jpeg", "seg": "j2b",
        "window": "135.23-146.07", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "FATHER", "ELDER", "ESTATE"],
        "narration": ("It was meet that we should make merry, and be glad: for "
                      "this thy brother was dead, and is alive again; and was "
                      "lost, and is found. (Luke 15:32)"),
        "must_show": ("the story's unresolved end — the father gesturing toward "
                      "the open lamplit door and the feast beyond it, the elder "
                      "son at the threshold, the choice hanging. The ONE emotion: "
                      "the open door, the choice not yet made."),
        "must_not_show": "do NOT show him going in or turning away — the parable ends before he chooses; neither man looks at the camera.",
        "scene": (
            "The father — the SAME man as the attached FATHER reference: about "
            "sixty, THICK GREY HAIR and a FULL SILVER-GREY BEARD, never "
            "dark-haired, never younger — stands beside the farmhouse's "
            "wide-open door, one arm around his elder son's shoulders and the "
            "other stretched open toward "
            "the bright doorway — inside, warm and slightly soft beyond the "
            "threshold, the feast is visible and alive, the younger brother in "
            "his deep wine-red robe glimpsed among the celebrating household — "
            "and the elder son stands at the very threshold, caught in the warm "
            "light with the night at his back, his face undecided between the "
            "dark courtyard and the open door, his eyes on the room, not on us. "
            "The story ends here, with the door open. Every figure has two arms, "
            "two hands and one head."
        ),
    },
]

# ROUGH-DRAFT CONTINUITY (the storm-11 pattern): the rejected-look still for a
# beat, when it exists, is attached as the approved rough draft — its camera
# angle, blocking, positions and travel directions were bought with the row-2
# reroll war and must not be reinvented. Faces and identity always come from
# the FACE/CHARACTER lock images, never from the draft.
# b20's rough itself contains the defect being fixed (a torch-bearing partial
# third figure at the right edge, copied faithfully on two rerolls) — it gets
# no rough so the corrected prompt wins.
_NO_ROUGH = {"v2-r002-b20"}
for _beat in BEATS:
    _asset = Path(__file__).resolve().parent / "assets" / _beat["out"]
    if _asset.is_file() and _beat["id"] not in _NO_ROUGH:
        _beat["rough_ref"] = str(_asset)
