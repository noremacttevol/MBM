#!/usr/bin/env python3
"""V2 beat map — row 5, build-05-bent-woman (Luke 13:10-17) — REALISTIC REBUILD.

Consumed by media-production-v2/v2_prompt.py (--check/--dump) and
media-production-v2/v2_gen_api.py (generation). STYLE-V2, the QUALITY LOCK, the
anti-panel clause and JESUS LOCK v5 are prepended by the assembler so they stay
byte-identical across every prompt.

REALISTIC REBUILD (Session 8, 2026-08-01). The 37 stills in `assets/` are the
2026-07-29 set that falls under the Session 6 blanket rejection of the old V2
look (3 of them additionally 1K undersized). They are kept untouched as
ROUGH-DRAFT composition references — their staging, camera angles and travel
directions were bought with the 2026-07-29 authoring pass (the ROTATION-TRAP
lesson at b02 among them) — while the realistic set generates fresh at native
2K into `assets-realistic/`. Per the Session 6 root-cause list, every prompt
now carries the byte-identical CAMERA lock: light from ONE believable
direction, real lens depth of field, people caught MID-ACTION, and NOBODY
looking at the camera.

TIMING: windows recomputed 2026-08-01 from the fixed extract_beats.py (reads
this build's own timeline formulas) — absolute audio phrase times, card at
236.68 s, total 247.69 s, matching the authoritative V1 cut (247.77 s). The
previous windows drifted up to ~13 s by the end (the storm-11 defect) and were
all replaced.

COVERAGE (STORY-COVERAGE-LAW): 36 pictures against V1's 11 unique stills.
Runtime is 223 s (3.7 min), so the law's "~15 per 100 seconds, scaled by runtime"
lands at ~33-36. That is where this sits, at ~6.2 s per picture — the same
density row 2 shipped at (24 stills / 158 s = 6.6 s). Nothing here is padding:
the two places the count rises are the two places the narration itself bursts —
Jesus noticing her (stopped / looked down the room / saw her) and the healing
itself (hands laid / the unfolding / fully straight), which V1 told in one still
each.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Luke 13:10-17 KJV):
  v10    "teaching in one of the synagogues on the SABBATH" — the whole story
         happens INSIDE a synagogue, in daylight. Never outdoors, never night.
  v11    "a woman ... bowed together, and could IN NO WISE lift up herself" for
         EIGHTEEN YEARS. Bent double at the waist, face toward the floor. Her
         eyes cannot reach another person's face; this is the engine of the
         whole video and the reason the closing frame lands.
  v12    "when Jesus SAW her, he CALLED her to him" — she never asks. He sees
         her first, he speaks first. Every frame in the first half must protect
         that order: she is passive, he initiates.
  v13    "he LAID HIS HANDS on her: and IMMEDIATELY she was made straight, and
         GLORIFIED GOD." The praise is hers and it is immediate and out loud.
  v14    the ruler of the synagogue "answered with indignation ... and SAID UNTO
         THE PEOPLE." He does NOT confront Jesus — he turns his back on him and
         scolds the congregation. b21/b22 stage exactly that.
  v15    "doth not each one of you on the sabbath LOOSE his ox or his ass FROM
         THE STALL, and LEAD HIM AWAY TO WATERING?" Two separate actions —
         untying at the post, then leading to water. They get separate frames
         (b26, b28) because the narration separates them too.
  v16    "this woman, being a DAUGHTER OF ABRAHAM, whom Satan hath bound ... be
         LOOSED FROM THIS BOND on the sabbath day."
  v17    "all his ADVERSARIES were ASHAMED: and all the PEOPLE REJOICED" — the
         room splits two ways at the end, and both halves get a frame.

CONTENT-CARE: row 5 is not in the §3 flag table = GREEN. One law still binds it
anyway — the ADVERSARY LAW (§1 A). Jesus's own words at j2 say "whom Satan hath
bound," and Satan is NEVER given a face, body, figure or shadow in any frame.
The binding is shown only as her condition and its end: the years in her spine,
and afterwards the walking stick lying on the floor where she no longer needs
it (b27). Nothing is painted that we do not know.

POSTURE ARC — the one thing QC must check on every frame of this build:
  b01-b13  bent double, face toward the ground, both hands on the stick
  b15      still bent, his hands on her back
  b16      MID-UNFOLD — halfway up, one hand off the stick, face rising
  b17-b36  FULLY STRAIGHT, shoulders back, chin level, eyes on faces
The WOMAN lock therefore fixes only her face, hair, build and clothing and says
NOTHING about posture — same reason row 2's YOUNGER SON lock said nothing about
clothing. A lock must never argue with a beat.

TIME OF DAY: one sabbath morning into midday. Hard clean shafts of daylight from
the synagogue's high windows; the three farmyard cutaways are the same morning
outdoors. No lamps, no torches, no evening anywhere in this build.
"""

from pathlib import Path

OUTPUT_ASSET_DIR = "assets-realistic"
OUTPUT_VIDEO_NAME = "luke-13_bent-woman-realistic-v2.mp4"

# Identity anchors by IMAGE (CAST-BIBLE principle; row-2 CAST-DRIFT lesson —
# text locks alone do not hold a recurring face across 20+ shots). Each
# recurring character has ONE canonical anchor; every beat naming the lock
# attaches it automatically. The anchors are neutral bust portraits (upright —
# the WOMAN lock says nothing about posture, so the anchor must not either;
# posture comes from each beat, same reason the lock omits it).
REFS = {
    "WOMAN": "CAST-REF-V2/woman-ref.jpeg",
    "RULER": "CAST-REF-V2/ruler-ref.jpeg",
    # The farmer drifted between the three farmyard cutaways (s14 salt-and-pepper
    # vs s26 white-bearded elder). The accepted s14 take is his canonical anchor;
    # any beat naming STALL now carries it (rubric: one canonical anchor per
    # recurring person, anchored by IMAGE not prose).
    "STALL": "assets-realistic/s14-untied-from-the-stall.jpeg",
}

LOCKS = {
    # Realistic-cinematography lock, byte-identical wherever named (build-02
    # pattern): the Session 6 rejection was flat noon light, posed extras and
    # camera-gaze on every frame.
    "CAMERA": (
        "CAMERA LOCK: photographed like a real film still on location with a real "
        "cinema lens — light arrives from ONE believable direction and models "
        "faces with true shadow, shallow depth of field holds the subject sharp "
        "while the background falls gently away, and every person is caught "
        "mid-action in a truthful candid instant, never posed, never lined up, "
        "and NEVER looking at the camera."
    ),
    # Posture is deliberately absent — see the POSTURE ARC note above.
    "WOMAN": (
        "WOMAN LOCK: the woman is the same person in every shot — a Galilean Jewish "
        "woman of about fifty-five, small and thin, a deeply weathered sun-browned "
        "face with fine lines around the eyes and mouth, dark eyes, dark hair heavily "
        "streaked with grey pulled back under a faded DUSTY-PLUM headcloth. She wears "
        "a worn DARK BROWN wool robe, much mended, with a plain cord belt and old "
        "leather sandals (never cream, never white, never any near-white cloth). Her "
        "hands are thin and work-hardened. She carries a short worn olive-wood walking "
        "stick, polished smooth at the grip. Her face is shown clearly."
    ),
    "RULER": (
        "RULER LOCK: the ruler of the synagogue is the same man in every shot — a "
        "Jewish elder of about sixty, heavy-set and well-fed, a long carefully combed "
        "grey beard, thick grey brows over hard narrow eyes, an accustomed air of "
        "authority. His clothing is finely woven and DEEPLY DYED — a NEAR-BLACK "
        "indigo robe with a woven dark-red border, and over it a prayer shawl of the "
        "SAME saturated near-black and dark-indigo wool with dark fringe, plainly "
        "DARKER than the sunlit limestone wall behind him. His face is shown clearly."
    ),
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect). These describe the
    # room and the crowd only. The congregation's colours are stated POSITIVELY
    # and dark, not as a negation — row 2 paid for that lesson at the PHARISEES
    # lock, where "never cream" produced a room full of white shawls.
    "SYNAGOGUE": (
        "SYNAGOGUE LOCK: a small first-century Galilean synagogue of pale dressed "
        "limestone — tiered stone benches running along the side walls, a worn stone "
        "floor, two short rows of plain stone columns, a low raised reading platform "
        "with a wooden stand, and a curtained niche for the scrolls at the far end. "
        "High small windows throw hard clean shafts of sabbath morning daylight down "
        "through drifting dust. The congregation are ordinary Galilean villagers in "
        "SATURATED DEEP earth colours — dark chocolate brown, deep russet, burnt "
        "ochre, dark olive, dusty indigo and faded plum wool; the men's prayer shawls "
        "are woven from that same dark wool with dark stripes and dark fringe. No one "
        "in the congregation wears off-white, ivory or any near-white cloth."
    ),
    "VILLAGE": (
        "VILLAGE LOCK: a small Galilean village street — packed dirt and worn paving "
        "stones, low flat-roofed limestone houses with heavy wooden doors, clay water "
        "jars and reed baskets set out along the walls, a stone well at the corner, "
        "dry hills and olive terraces beyond the rooftops. The villagers wear "
        "SATURATED DEEP earth colours — dark chocolate brown, deep russet, burnt "
        "ochre, dark olive and dusty indigo wool. No villager wears off-white, ivory "
        "or any near-white cloth."
    ),
    "STALL": (
        "STALL LOCK: a small Galilean farmyard on the edge of the village — a "
        "stone-and-timber animal stall roofed with brush, a stout wooden post worn "
        "smooth by years of rope, trodden straw and dust underfoot, a long hollowed "
        "stone water trough beside a low wall, olive trees and dry hills behind. The "
        "farmer is an ordinary weathered village man in a DARK EARTH-BROWN wool tunic "
        "with a leather belt and a dusty head cloth of the same dark wool; he wears no "
        "off-white, ivory or near-white cloth."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------ n0 — eighteen years ----
    {
        "id": "v2-r005-b01", "out": "s01-bent-eighteen-years.jpeg", "seg": "n0 p1-p2",
        "window": "0.28-5.46", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "VILLAGE"],
        "narration": ("There was a woman who had been bent over for eighteen years. "
                      "She could not straighten up at all."),
        "must_show": "her bent DOUBLE at the waist, face toward the ground, both hands on the stick, moving through an ordinary village morning.",
        "must_not_show": "not merely stooped or hunched — she is folded over, and cannot lift herself; no crowd staring, this is just her ordinary day.",
        "scene": (
            "The woman makes her way along the village street in the clear light of "
            "morning, BENT COMPLETELY DOUBLE at the waist so that her back is nearly "
            "level with the ground and her face is turned down toward the paving "
            "stones. Both her thin hands grip the worn olive-wood stick planted ahead "
            "of her, taking her weight. Two or three villagers go about their own "
            "business further down the street without looking at her. The camera is "
            "far enough back to see her whole small folded shape against the low "
            "houses. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b02", "out": "s02-sandals-instead-of-faces.jpeg", "seg": "n0 p3-p4",
        "window": "5.46-12.20", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "VILLAGE"],
        "narration": ("Eighteen years of looking at the ground. Eighteen years of "
                      "knowing people by their sandals instead of their faces."),
        "must_show": "THE WORLD SHE ACTUALLY SEES — a low camera near the street stones: passing sandals, dusty feet and robe hems, and her own downturned face at the frame edge.",
        "must_not_show": "no faces of the passers-by visible — the whole point is that she cannot see them; not a first-person camera trick, a real low camera angle.",
        # ROTATION TRAP (Machine A, 2026-07-29). The first version of this scene said
        # "the camera is set LOW, close to the paving stones, at the exact height her
        # eyes have been" — and the model answered by ROLLING THE WHOLE FRAME 90
        # degrees, so the street ran up the left edge and every figure lay on its
        # side. A picture that has to be turned to be read is unusable in a 9:16 cut.
        # The fix is to describe a low VIEWPOINT while stating plainly that the
        # photograph itself is upright and the ground is at the bottom. Any beat that
        # asks for a ground-level camera needs the same two sentences.
        "scene": (
            "An upright vertical photograph taken from a low viewpoint about knee "
            "height, looking along the village street. The ground is at the bottom of "
            "the frame and the sky and rooftops are at the top, and the horizon is "
            "level — the picture is the right way up. Across the lower half of the "
            "frame pass the dusty sandalled feet, bare ankles and swinging robe hems "
            "of villagers walking by, their bodies cut off at the waist by the top of "
            "the frame so that not one face is visible. At the near edge the woman's "
            "own worn sandals, the planted tip of her olive-wood stick and her thin "
            "hands are close to the camera, and her downturned weathered face is bent "
            "low toward the stones, deeply lined and patient. Warm dust hangs in the "
            "morning light. Each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r005-b03", "out": "s03-no-one-could-help.jpeg", "seg": "n0 p5",
        "window": "12.20-16.78", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "VILLAGE"],
        "narration": "And in all that time, no one had been able to help her.",
        "must_show": "the village going on all around her while she rests folded over her stick against a wall — near people, and entirely alone.",
        "must_not_show": "nobody cruel, nobody mocking — this is indifference, not persecution.",
        "scene": (
            "The woman has stopped to rest against the sunlit limestone wall of a "
            "house, still folded over her stick, her face toward the ground. Around "
            "her the village morning carries on — a woman drawing water at the corner "
            "well, two men talking in a doorway, a child running past — and not one of "
            "them is turned toward her. She is small and dark against the bright wall, "
            "surrounded by people and completely alone. The camera is far enough back "
            "to hold her and the busy street together in one frame. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    # ------------------------------------------- n1 — the sabbath synagogue ----
    {
        "id": "v2-r005-b04", "out": "s04-teaching-on-the-sabbath.jpeg", "seg": "n1 p1a",
        "window": "16.78-20.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "SYNAGOGUE"],
        "narration": "One sabbath day, Jesus was teaching in a synagogue,",
        "must_show": "the whole room: Jesus seated and teaching at the front, the congregation on the stone benches listening, sabbath light from the high windows.",
        "must_not_show": "no halo, no rim-light; he is not detached at the frame edge — every listening face is turned toward him.",
        "scene": (
            "Inside the synagogue on the sabbath morning, Jesus sits teaching on the "
            "low raised platform at the front of the room, one hand open in the middle "
            "of a sentence, entirely at ease. The congregation fill the tiered stone "
            "benches down both side walls — men, women and a few children — and every "
            "face in the room is turned toward him and listening. Hard clean shafts of "
            "daylight come down through the high windows across the dusty air between "
            "them. The camera is at the back of the room, far enough to hold the whole "
            "length of it. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b05", "out": "s05-present-and-unseen.jpeg", "seg": "n1 p1b-p4",
        "window": "20.30-35.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("and she was there — at the back, by the wall, folded over her "
                      "walking stick. She had not come to ask him for anything. She "
                      "was simply there, the way she had been there for years. "
                      "Present, and unseen."),
        "must_show": "her at the very BACK of the room against the wall, folded over her stick, in shadow — and every back in the room turned away from her toward the front.",
        "must_not_show": "she is NOT reaching, waving, or trying to get attention; no one is looking at her; do not put Jesus in this frame.",
        "scene": (
            "At the very back of the synagogue, against the shadowed limestone wall "
            "behind the last stone bench, the woman stands folded double over her "
            "walking stick, her face toward the floor, perfectly still and asking for "
            "nothing. The camera is behind her and slightly to one side, so that "
            "beyond her small dark shape the whole congregation is seen FROM BEHIND — "
            "rows of backs and shoulders, every head turned away toward the bright "
            "front of the room. A shaft of daylight falls in the middle distance and "
            "leaves her in shadow. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n2 — he sees her ----
    {
        "id": "v2-r005-b06", "out": "s06-he-stopped.jpeg", "seg": "n2 p1",
        "window": "35.89-38.33", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "SYNAGOGUE"],
        "narration": "And in the middle of his teaching, Jesus stopped.",
        "must_show": "the exact moment he goes still mid-sentence — hand still half-raised in the gesture, but his attention already gone somewhere past the front rows.",
        "must_not_show": "no alarm, no drama; a quiet stop. No halo or rim-light.",
        "scene": (
            "Jesus has stopped speaking in the middle of a sentence. His teaching hand "
            "is still lifted where it was, but he has gone completely still and his "
            "eyes have moved off the people in front of him toward something far down "
            "the length of the room. The listeners nearest him are still leaning "
            "forward waiting for the rest of the sentence, one or two beginning to "
            "notice the pause. Sabbath daylight falls in hard shafts through the high "
            "windows. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b07", "out": "s07-past-every-face.jpeg", "seg": "n2 p2",
        "window": "38.33-42.60", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": "He looked past every face in the room, all the way to the back wall.",
        "must_show": "the LENGTH of the room from behind Jesus's shoulder — rows of faces between him and the dim back wall where her small folded shape stands.",
        "must_not_show": "no halo or rim-light; his look must clearly travel PAST the near faces, not rest on them.",
        "scene": (
            "SHOT FROM BEHIND AND JUST PAST JESUS'S SHOULDER, looking down the full "
            "length of the synagogue. Between the camera and the far wall are rows of "
            "upturned listening faces on the stone benches, lit in the shafts of "
            "daylight, none of them aware of anything. Beyond all of them, small in "
            "the shadow at the very back of the room, the woman stands folded over her "
            "stick — and his line of sight runs straight past every nearer face to "
            "her. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b08", "out": "s08-he-saw-her.jpeg", "seg": "n2 p3-p4",
        "window": "42.60-45.98", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "SYNAGOGUE"],
        "narration": "He saw her. And he called her over.",
        "must_show": "HIS FACE — recognition landing, warm and certain, and his hand opening toward the back of the room in the call.",
        "must_not_show": "no halo, glare or rim-light of any kind; no pity that looks like sorrow — this is recognition and welcome; his eyes are NOT on the camera.",
        "scene": (
            "Close on Jesus IN PROFILE-TO-THREE-QUARTER VIEW from beside him, his face "
            "and shoulders turned AWAY from the camera toward the far back corner of "
            "the room, so that his gaze travels clearly PAST the camera's side of the "
            "room and never toward the lens. His expression has changed — he has found "
            "what he was looking for, and his eyes are steady, warm and completely "
            "certain, fixed on the distant back wall. His near hand has come open and "
            "lifted toward the back of the room, calling her forward. His hair is DARK "
            "BROWN with warm sun-bleached bronze lights, never black. Behind him the "
            "sunlit synagogue wall and the edge of the reading platform are soft with "
            "distance. His hand has five fingers."
        ),
    },
    # ------------------------------------------ n3 — she never asked ----
    {
        "id": "v2-r005-b09", "out": "s09-he-called-her-first.jpeg", "seg": "n3 p1-p6",
        "window": "45.98-58.26", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("Notice what did not happen. She did not push through a crowd. "
                      "She did not call out to him. She did not ask. He called her "
                      "first. Before she said one word, he had already decided."),
        "must_show": "the whole room in one frame: Jesus at the front with his hand out toward her, she still motionless at the back wall, the unmoved crowd between them.",
        "must_not_show": "she must NOT be moving, reaching or calling out yet; the crowd is not parting for her; the initiative is entirely his; she appears EXACTLY ONCE in the frame — no second bent or stick-carrying figure anywhere.",
        "scene": (
            "A wide view down the synagogue holding both ends of the room at once. At "
            "the front Jesus stands with his arm extended the full length of the room "
            "toward the back wall, palm open, waiting. At the far end, small with "
            "distance against the back wall, the woman is still folded over her stick "
            "exactly where she was, not yet moving, her face toward the floor — SHE IS "
            "THE ONLY bent figure and the ONLY person with a walking stick in the "
            "whole room, and she appears exactly once. The open middle aisle between "
            "the benches is EMPTY bare stone floor with nobody standing in it. Between "
            "them the congregation sit on their benches and heads are beginning to "
            "turn to follow his outstretched hand. Sabbath daylight crosses the room "
            "in hard shafts. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n4 — the long walk ----
    {
        "id": "v2-r005-b10", "out": "s10-the-slow-walk.jpeg", "seg": "n4 p1",
        "window": "58.26-64.47", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("She made her slow way up the middle of that room, her stick "
                      "tapping the stone floor, every eye on her."),
        "must_show": "her making her way up the open middle of the room, still folded double, stick planted ahead of her — and every face on both sides turned to watch.",
        "must_not_show": "she is not straightening yet; nobody is helping her walk; she does it herself.",
        "scene": (
            "The woman moves slowly up the open middle of the synagogue floor, still "
            "bent completely double, planting the olive-wood stick ahead of her on the "
            "worn stone with each short step. On the benches to either side every face "
            "has turned to watch her come, some kind, some uncertain. Ahead of her at "
            "the front of the room Jesus stands waiting for her, watching her the "
            "whole way. The camera is low and behind her so the length of floor still "
            "ahead of her is visible. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b11", "out": "s11-he-came-down-to-her.jpeg", "seg": "n4 p2",
        "window": "64.47-72.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("And when she finally stood in front of him — still bent, still "
                      "staring at the ground — he said this."),
        "must_show": "he has BENT DOWN to her level so his face comes into her line of sight near the floor — she cannot come up to him, so he goes down to her.",
        "must_not_show": "he does not lift her chin or pull her upright; she is still bent double; no halo or rim-light.",
        "scene": (
            "The woman has arrived and stands in front of Jesus, still folded "
            "completely double over her stick, her face toward the stone floor. Jesus "
            "has BENT LOW to meet her — knees flexed, one hand resting on his knee, "
            "his shoulders down and his head turned up and sideways so that his face "
            "comes into the narrow strip of floor her eyes can actually reach. He is "
            "looking directly into her eyes from below. The camera is low and close "
            "beside them; the sunlit room is soft behind. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    # ------------------------------------------------------ j1 — the words ----
    {
        "id": "v2-r005-b12", "out": "s12-thou-art-loosed.jpeg", "seg": "j1",
        "window": "72.58-76.44", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": "Woman, thou art loosed from thine infirmity. (Luke 13:12)",
        "must_show": "the two faces close together near the floor — he is speaking the sentence and she is hearing it, her eyes on his for the first time.",
        "must_not_show": "no halo, glare or rim-light; nothing supernatural in the air; the moment is quiet and human.",
        "scene": (
            "Very close on the two of them low near the stone floor. Jesus, still bent "
            "right down to her level, is speaking — his mouth mid-word, his face open "
            "and sure. The woman's weathered face is turned up as far as her body will "
            "let it, and her dark eyes have found his and stopped there, wide, holding "
            "his gaze while the words land. Her thin hands are still locked on the "
            "walking stick between them. Soft sunlit dust in the air behind. Each "
            "visible hand has five fingers."
        ),
    },
    # ------------------------------------------- n5a — loosed = untied ----
    {
        "id": "v2-r005-b13", "out": "s13-an-everyday-word.jpeg", "seg": "n5a p1-p2",
        "window": "76.44-80.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN"],
        "narration": ("Loosed. In their language it was an everyday word."),
        "must_show": "her hands and the stick — eighteen years of holding on, seen up close, as the word sits in the air.",
        "must_not_show": "no faces needed; keep it on the hands and the worn wood.",
        "scene": (
            "Very close on the woman's two thin work-hardened hands locked around the "
            "grip of the olive-wood walking stick, the wood polished smooth and dark "
            "by eighteen years of exactly this hold. Her knuckles stand out; the "
            "mended sleeve of her dark brown robe falls back from one wrist. The "
            "planted end of the stick and the worn stone floor are just in frame "
            "below. Warm daylight from the high windows crosses her fingers. Each hand "
            "has five fingers."
        ),
    },
    {
        "id": "v2-r005-b14", "out": "s14-untied-from-the-stall.jpeg", "seg": "n5a p3-p4",
        "window": "80.16-91.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "STALL"],
        "narration": ("It meant untied — the same word a farmer used when he untied "
                      "his animal from its stall. Something that had been knotted for "
                      "eighteen years was coming undone."),
        "must_show": "a worn rope knot at the stall post coming loose in a farmer's hands, the halter falling open, the animal's head lifting free.",
        "must_not_show": "no synagogue in this frame; no people from the story; nothing symbolic or dreamlike — an ordinary farmyard morning.",
        "scene": (
            "Close in the farmyard on a stout wooden post worn smooth with years of "
            "rope. A village farmer's brown weathered hands are working the last turn "
            "of a thick worn rope knot loose, and the halter is falling open and away "
            "from the post. Beside him the heavy warm head of a patient brown ox lifts "
            "free as the rope gives, its ear turning. Straw and dust, morning sunlight "
            "across the timber. Each hand has five fingers."
        ),
    },
    # ------------------------------------ n5b — the healing (core burst) ----
    {
        "id": "v2-r005-b15", "out": "s15-he-laid-his-hands.jpeg", "seg": "n5b p1",
        "window": "91.76-93.06", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": "He laid his hands on her.",
        "must_show": "both his hands coming to rest on her bowed back and shoulder while she is STILL bent double.",
        "must_not_show": "no light, spark, glare or rim-light at his hands — nothing supernatural is depicted; she has NOT begun to rise yet.",
        "scene": (
            "Close on the woman's bowed back and Jesus's two hands. She is still "
            "folded completely double over her stick, her face down. He has straightened "
            "a little from his crouch and laid both hands gently on her — one flat "
            "across the curve of her upper back, one on her shoulder — his own head "
            "bowed toward her. His sleeves fall back from his forearms. Ordinary "
            "sabbath daylight, nothing else in the air. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r005-b16", "out": "s16-halfway-up.jpeg", "seg": "n5b p2a",
        "window": "93.06-94.60", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": "And slowly —",
        "must_show": "MID-UNFOLD — she is HALFWAY up, spine partly opened, one hand come off the stick, her face rising past his chest toward his face.",
        "must_not_show": "not bent double any more and not yet upright — this frame exists ONLY to show the middle of the movement; no halo or rim-light.",
        "scene": (
            "The woman is CAUGHT HALFWAY UP. Her spine has opened partway so her back "
            "is at a slant instead of level, her chin has come up off her chest, and "
            "one thin hand has lifted away from the walking stick and hangs open in "
            "the air as she rises. Her face is climbing past Jesus's chest toward his "
            "face, her eyes wide and her mouth open in astonishment at her own body. "
            "Jesus stands close in front of her with his hands still lifted where they "
            "were, watching her come up. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r005-b17", "out": "s17-she-stood-up-straight.jpeg", "seg": "n5b p2b",
        "window": "94.60-98.24", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": "for the first time in eighteen years — she stood up straight.",
        "must_show": "FULLY STRAIGHT — shoulders back, chin level, standing to her true height face to face with Jesus, the stick hanging forgotten in one hand.",
        "must_not_show": "no trace of the bend left; nothing supernatural in the air; the congregation behind is frozen mid-reaction, not cheering yet.",
        "scene": (
            "The woman is STANDING COMPLETELY UPRIGHT — shoulders back, spine straight, "
            "chin level, at her full small height for the first time in eighteen years "
            "— face to face with Jesus, close enough to touch, her eyes locked on his "
            "and her whole face breaking open. The olive-wood stick hangs forgotten "
            "from one loose hand at her side. A shaft of sabbath daylight from the "
            "high window falls across the two of them. Behind and around, the "
            "congregation on the benches have half risen, faces stunned. The camera is "
            "back far enough to see both of them head to sandals. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ----------------------------------------------------- n6 — the praise ----
    {
        "id": "v2-r005-b18", "out": "s18-she-praised-god.jpeg", "seg": "n6 p1",
        "window": "98.24-101.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": "The first thing she did with a straight back was praise God.",
        "must_show": "her face lifted UP toward the high window light, both hands open and raised, praising out loud — the first thing she does with her new body.",
        "must_not_show": "she is not looking at Jesus or the crowd here — she is looking UP; no halo or rim-light on her.",
        "scene": (
            "Close on the woman standing straight with her weathered face tipped right "
            "back and UP toward the high window, eyes shut, mouth open, tears on her "
            "cheeks, both thin hands lifted open at her shoulders. The hard clean "
            "shaft of sabbath daylight from that window falls full across her upturned "
            "face and her raised palms. The walking stick is gone from her hands. Each "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r005-b19", "out": "s19-nobody-could-stop-it.jpeg", "seg": "n6 p2-p3",
        "window": "101.13-108.93", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "RULER", "SYNAGOGUE"],
        "narration": ("Out loud, right there in the middle of the meeting. Eighteen "
                      "years of silence turned into worship that nobody could stop."),
        "must_show": "the whole room: she stands straight in the middle praising aloud, the congregation on their feet in wonder — and the ruler stiff and dark at the front, the one still figure.",
        "must_not_show": "the ruler is not shouting yet, only rigid and displeased; no halo or rim-light on Jesus.",
        "scene": (
            "A wide view of the whole synagogue. In the middle of the open floor the "
            "woman stands upright with her face lifted and her hands raised, praising "
            "aloud, and all around her the congregation have come up off the stone "
            "benches — faces breaking into astonishment and joy, some with hands to "
            "their mouths, a child staring. Jesus stands near her, watching her with "
            "quiet gladness. At the front of the room, beside the reading platform, "
            "the ruler of the synagogue stands rigid and unmoving in his dark robes, "
            "the one still figure in the room, his face hard. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ------------------------------------------------------- n7 — the ruler ----
    {
        "id": "v2-r005-b20", "out": "s20-the-ruler-was-angry.jpeg", "seg": "n7 p1-p2",
        "window": "108.93-115.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "RULER", "SYNAGOGUE"],
        "narration": ("But not everyone rejoiced. The ruler of the synagogue — the "
                      "man in charge of that meeting — was angry."),
        "must_show": "the ruler's face and upper body — indignation, one hand gripping the edge of the wooden reading stand, the joy of the room shut out of him.",
        "must_not_show": "not a cartoon villain — a serious, respected man who believes he is defending the sabbath; keep him dignified.",
        "scene": (
            "Close on the ruler of the synagogue standing beside the wooden reading "
            "stand on the low platform. His face is tight with indignation — jaw set "
            "under the combed grey beard, brows down, eyes narrow and fixed across the "
            "room. One heavy hand grips the edge of the reading stand hard enough to "
            "whiten the knuckles. Behind him the curtained scroll niche and the sunlit "
            "limestone wall; the blurred joy of the standing congregation is soft in "
            "the background. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r005-b21", "out": "s21-he-turned-to-the-people.jpeg", "seg": "n7 p3-p4",
        "window": "115.49-123.35", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "RULER", "SYNAGOGUE"],
        "narration": ("In his mind, healing counted as work, and the sabbath was the "
                      "day of rest. And he said this to the people."),
        "must_show": "SCRIPTURE-EXACT: he turns his back on Jesus and addresses THE PEOPLE — arm raised to the congregation, deliberately not looking at the man he is angry with.",
        "must_not_show": "he must NOT be facing Jesus or pointing at him — Luke says he said it unto the people; no halo or rim-light on Jesus.",
        "scene": (
            "The ruler has stepped down off the platform and turned to face the "
            "congregation, his back and shoulder squarely toward Jesus, one arm raised "
            "to the room as he begins to speak to them. He is pointedly not looking at "
            "Jesus at all. Behind his shoulder, further down the room, Jesus stands "
            "quietly watching him, unhurried. The congregation nearest the front are "
            "turning back toward the ruler, the joy going uncertain on their faces. "
            "The camera is back far enough to hold the ruler, the crowd and Jesus in "
            "one frame. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- s14 — the KJV rebuke ----
    {
        "id": "v2-r005-b22", "out": "s22-six-days-to-work.jpeg", "seg": "s14",
        "window": "123.35-131.54", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "RULER", "SYNAGOGUE"],
        "narration": ("There are six days in which men ought to work: in them "
                      "therefore come and be healed, and not on the sabbath day. "
                      "(Luke 13:14)"),
        "must_show": "the rebuke landing on the room — the ruler mid-sentence to the people, faces falling, and behind him the healed woman still standing straight, her joy faltering.",
        "must_not_show": "do not put Jesus in this frame — this beat belongs to the ruler and the crowd.",
        "scene": (
            "The ruler stands before the congregation mid-sentence, both hands out to "
            "them, his voice filling the room. The faces in front of him have gone "
            "uncertain — smiles dying, eyes dropping to the floor, an older man "
            "glancing away, a woman pulling her child closer. Behind and to one side, "
            "the healed woman stands straight and alone in the shaft of window light, "
            "her raised hands lowering, the joy sliding off her face as she listens. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    # -------------------------------------------------- n7b — it had waited ----
    {
        "id": "v2-r005-b23", "out": "s23-one-more-day.jpeg", "seg": "n7b",
        "window": "131.54-137.94", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("As if her freedom could have waited one more day. As if it had "
                      "not already waited eighteen years."),
        "must_show": "close on HER — standing straight but shrinking inside, one hand come up to her own chest, hearing her freedom argued about as an inconvenience.",
        "must_not_show": "she must NOT bend or stoop again — the body stays straight while the face falls; that contrast is the whole frame.",
        "scene": (
            "Close on the woman. Her body is still upright — shoulders back, spine "
            "straight — but her face has fallen and her eyes have gone down and away, "
            "and one thin hand has come up to rest flat against her own chest. She is "
            "listening to herself being discussed. The sunlit room and the blurred "
            "shape of the ruler's dark robes are behind her. Each hand has five fingers."
        ),
    },
    # --------------------------------------------------- n8 — Jesus answers ----
    {
        "id": "v2-r005-b24", "out": "s24-he-did-not-soften-it.jpeg", "seg": "n8",
        "window": "137.94-141.42", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "SYNAGOGUE"],
        "narration": "Jesus turned to him. And he did not soften it.",
        "must_show": "Jesus turning and squaring toward the ruler — his face steady, level and completely unsparing.",
        "must_not_show": "no snarl, no glare, no clenched fist — this is immovable, not hot-tempered; no halo or rim-light.",
        "scene": (
            "Close on Jesus as he turns and squares his shoulders toward the ruler. "
            "His face is calm and absolutely level — no anger in the mouth, but "
            "nothing soft left in the eyes either, a look that is not going to move. "
            "One hand hangs open at his side. The sunlit synagogue is soft behind him "
            "and the dark shape of the ruler's shoulder is just at the edge of frame. "
            "His hand has five fingers."
        ),
    },
    # ------------------------------------------------- j2 — thou hypocrite ----
    {
        "id": "v2-r005-b25", "out": "s25-thou-hypocrite.jpeg", "seg": "j2 p1a",
        "window": "141.42-147.80", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "RULER", "SYNAGOGUE"],
        "narration": ("Thou hypocrite, doth not each one of you on the sabbath loose "
                      "his ox or his ass from the stall, (Luke 13:15)"),
        "must_show": "the confrontation across the open floor — Jesus speaking directly to the ruler, the whole congregation silent and still around them.",
        "must_not_show": "nobody is shouting; no fists; the room is dead quiet. No halo or rim-light.",
        "scene": (
            "Jesus faces the ruler across the open floor of the synagogue, speaking, "
            "one hand lifted in the plain gesture of a man stating an obvious fact. "
            "The ruler — the SAME man as the attached RULER reference: about sixty, "
            "heavy-set, THICK GREY HAIR, a LONG CAREFULLY COMBED GREY BEARD, thick "
            "grey brows, in his NEAR-BLACK INDIGO robe with the woven DARK-RED border "
            "and dark prayer shawl, never a different elder — stands squared to him "
            "now, chin up, holding his ground, his dark robes stark against the sunlit "
            "limestone. All around them the congregation have gone completely still on "
            "and around the benches, every head turned to the two men, nobody moving. "
            "Hard shafts of daylight cross the space between them. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b26", "out": "s26-loose-him-from-the-stall.jpeg", "seg": "j2 p1b",
        "window": "147.80-150.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "STALL"],
        "narration": "and lead him away to watering? (Luke 13:15)",
        "must_show": "the farmer leading his ox OUT of the stall by the loosed rope, walking it away toward the water — the ordinary sabbath thing every man in that room does.",
        "must_not_show": "no synagogue, no story characters; not the same framing as the earlier knot close-up — this one is wider and moving.",
        "scene": (
            "In the farmyard, the village farmer — the SAME man as in the attached "
            "farmyard photograph: middle-aged with a short salt-and-pepper beard and "
            "a dark head cloth, in the same dark earth-brown wool tunic, never an old "
            "white-bearded man — walks his heavy brown ox out from under the brush "
            "roof of the stall into the morning sunlight, the loosed rope halter "
            "slack in his hand, the animal following easily at his shoulder. Ahead of "
            "them the long hollowed stone water trough waits against the low wall. "
            "Straw, dust and clear morning light; the olive trees and dry hills "
            "behind. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b27", "out": "s27-a-daughter-of-abraham.jpeg", "seg": "j2 p2",
        "window": "150.00-163.02", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "RULER", "SYNAGOGUE"],
        "narration": ("And ought not this woman, being a daughter of Abraham, whom "
                      "Satan hath bound, lo, these eighteen years, be loosed from this "
                      "bond on the sabbath day? (Luke 13:16)"),
        "must_show": "his open hand held out toward HER as he says it; she stands straight in the window light; the olive-wood stick lying on the stone floor where she let it go.",
        "must_not_show": "ADVERSARY LAW — no figure, face, shadow or shape for Satan anywhere in the frame; the bond is shown ONLY as the abandoned walking stick on the floor.",
        "scene": (
            "Jesus stands with his arm stretched out toward the woman, palm open, "
            "presenting her to the whole room as he speaks. She stands upright and "
            "still in the shaft of sabbath daylight in the middle of the floor, small "
            "and straight, her eyes on him. On the worn stone between them the "
            "olive-wood walking stick lies where she let it fall. The ruler stands to "
            "one side with his face beginning to come apart, and the congregation "
            "watch from the benches. The camera is back far enough to hold all three "
            "of them head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------- n9 — every man does this ----
    {
        "id": "v2-r005-b28", "out": "s28-every-man-in-that-room.jpeg", "seg": "n9 p1",
        "window": "163.02-166.06", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "SYNAGOGUE"],
        "narration": "Every man in that room did exactly that on the sabbath.",
        "must_show": "the men of the congregation caught out — recognition on their faces, eyes dropping, one or two glancing sideways at each other.",
        "must_not_show": "no shame played for comedy; these are decent men recognising something true.",
        "scene": (
            "A row of men of the congregation on the stone benches, close enough to "
            "read every face. The recognition is going through them one by one — a "
            "grey-bearded man's eyes dropping to the floor, a younger man glancing "
            "sideways at his neighbour, another slowly sitting back, another with his "
            "mouth pressed shut. Every one of them knows exactly what he does on a "
            "sabbath morning. Sunlit dust and the limestone wall behind. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b29", "out": "s29-led-it-to-water.jpeg", "seg": "n9 p2",
        "window": "166.06-175.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "STALL"],
        "narration": ("He untied his ox or his donkey and led it to water, and the "
                      "rules allowed it — simple kindness to an animal was never "
                      "against the day of rest."),
        "must_show": "the ox drinking at the stone trough with the farmer's hand resting on its neck — plain, unremarkable sabbath kindness.",
        "must_not_show": "nothing dramatic; this frame is deliberately quiet and ordinary — that is the argument.",
        "scene": (
            "The heavy brown ox stands with its muzzle down in the long hollowed stone "
            "trough, drinking, water beading on its lip. The village farmer stands "
            "beside it with one broad weathered hand resting easily on the animal's "
            "neck and the loosed rope hanging from his other hand, looking off toward "
            "the hills, thinking about nothing in particular. Clear quiet morning "
            "light, straw and dust. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r005-b30", "out": "s30-untie-a-daughter.jpeg", "seg": "n9 p3-p4",
        "window": "175.60-185.28", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "RULER", "SYNAGOGUE"],
        "narration": ("So Jesus asked the only question left. If you will untie an "
                      "animal on the sabbath, how could it be wrong to untie a "
                      "daughter?"),
        "must_show": "the question hanging with no answer — Jesus's hand still open toward the woman, the ruler with his mouth shut and nothing to say.",
        "must_not_show": "no triumph on Jesus's face — he is not scoring a point; no halo or rim-light.",
        "scene": (
            "Jesus stands with his hand still open toward the woman, his head turned "
            "back to the ruler, waiting — the question already asked and lying in the "
            "silence. The ruler's mouth has closed, his raised hand has come down, and "
            "his eyes have gone to the floor; there is nothing left in his face to "
            "answer with. The woman stands straight in the light between them. Around "
            "them the whole congregation are silent and unmoving on the benches. The "
            "camera is back far enough to hold all three head to sandals. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------ n10 — he gave her a name ----
    {
        "id": "v2-r005-b31", "out": "s31-family-of-the-covenant.jpeg", "seg": "n10 p1-p3",
        "window": "185.28-194.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("And listen to what he called her. A daughter of Abraham. In "
                      "that room, those words were a declaration — family of the "
                      "covenant, a child of the promise."),
        "must_show": "she is no longer at the back wall — she stands in the MIDDLE of the room in the window light with the whole congregation gathered round her, inside the family instead of outside it.",
        "must_not_show": "nobody is stepping away from her any more; no halo or rim-light on anyone.",
        "scene": (
            "A wide view of the synagogue with the woman standing upright at the very "
            "centre of the floor, full in the hard shaft of sabbath daylight from the "
            "high window. The congregation are all around her now, turned inward — men "
            "on the benches, women standing, a child craning to see — the room closed "
            "around her instead of turned away. Jesus stands near her, one hand still "
            "open toward her, looking at the room. The curtained scroll niche and the "
            "reading platform are visible at the far end. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b32", "out": "s32-he-gave-her-back-her-name.jpeg", "seg": "n10 p4-p7",
        "window": "194.74-207.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("For eighteen years she had been the bent woman, the one people "
                      "stepped around. Now, in front of everyone, he gave her back "
                      "her name. And notice the order. He did not say she became a "
                      "daughter by being healed."),
        "must_show": "face to face and level — her eyes and his at the SAME HEIGHT for the first time, because she is standing straight.",
        "must_not_show": "he is not bending down to her any more — the whole point is that he no longer has to; no halo or rim-light.",
        "scene": (
            "Close on the two of them standing face to face, her upturned weathered "
            "face and his level with each other, close enough to speak quietly. Her "
            "eyes are steady on his, brimming, her chin up. His expression is warm and "
            "certain, telling her something in front of the whole room. The blurred "
            "shapes of the watching congregation and the sunlit limestone are soft "
            "behind them. Each visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r005-b33", "out": "s33-she-had-always-belonged.jpeg", "seg": "n10 p8-p10",
        "window": "207.62-216.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("She was healed because of who she already was. Her worth came "
                      "first. She belonged — she had always belonged."),
        "must_show": "the women and older men of the congregation coming to her — hands on her arms and shoulders, faces close to hers, taken back into her own people.",
        "must_not_show": "no crowding or grabbing — this is welcome, not a crush; do not put Jesus in this frame.",
        "scene": (
            "The women of the congregation have come off the benches to the woman "
            "where she stands in the light. One has both hands on her upper arms, "
            "looking straight into her face and laughing through tears; another has an "
            "arm across her shoulders; an old man beside them holds her hand in both "
            "of his. Their faces are close to hers and warm. She stands straight in "
            "the middle of them, taken back into her own people. Sunlit dust in the "
            "air above them. Every figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------- n11 + s17 — the room splits ----
    {
        "id": "v2-r005-b34", "out": "s34-adversaries-ashamed.jpeg", "seg": "n11 + s17 p1a",
        "window": "216.28-222.60", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "RULER", "SYNAGOGUE"],
        "narration": ("Luke tells us how the day ended. And when he had said these "
                      "things, all his adversaries were ashamed: (Luke 13:17)"),
        "must_show": "the ruler and the two or three men with him — heads down, faces burning, unable to look up at the room.",
        "must_not_show": "no mockery of them, nobody jeering at them; the shame is their own and it is quiet. Do not put Jesus in this frame.",
        "scene": (
            "The ruler of the synagogue stands near the reading platform with two "
            "other older men in dark robes beside him. All three have their heads "
            "down. The ruler's face is dark with blood to the ears, his eyes fixed on "
            "the stone floor; one of the men beside him has turned half away, and the "
            "other is pulling his dark shawl up over his shoulder as if to be less "
            "seen. Nobody in the room is jeering at them. Bright daylight from the "
            "high windows. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b35", "out": "s35-the-people-rejoiced.jpeg", "seg": "s17 p1b",
        "window": "222.60-228.40", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("and all the people rejoiced for all the glorious things that "
                      "were done by him. (Luke 13:17)"),
        "must_show": "the congregation rejoicing — hands up, faces bright, the sabbath meeting turned into gladness, Jesus among them and not apart.",
        "must_not_show": "no halo or rim-light on Jesus; he is IN the crowd, not standing separate at the edge; every gaze is toward him or the woman; NOBODY in the frame looks at or near the camera — not Jesus, not the woman, no one; the woman's hands are EMPTY, with NO walking stick anywhere in the frame.",
        "scene": (
            "The whole synagogue is on its feet and glad — hands lifted, faces open "
            "and shining, an old man gripping a younger man's shoulder, children up on "
            "the stone benches to see — a candid instant in the middle of the "
            "commotion, no one posed, no one aware of any camera. Jesus stands in "
            "among them, seen in three-quarter view with his face turned TOWARD THE "
            "WOMAN, laughing gladly with the people around him. The woman stands "
            "straight nearby with her empty hands lifted, her face turned to the "
            "rejoicing people around her. The hard shafts of sabbath daylight come "
            "down through the dust over all of them. The camera is back far enough to "
            "hold the whole room head to sandals. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    # ---------------------------------------------- n11b — the closing rhyme ----
    {
        "id": "v2-r005-b36", "out": "s36-faces-instead-of-sandals.jpeg", "seg": "n11b p1a",
        "window": "228.40-232.60", "wide": True, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": ("And somewhere in that crowd stood a woman seeing faces instead "
                      "of sandals"),
        "must_show": "THE DELIBERATE INVERSE OF FRAME 2 — camera at standing head height now, and she is looking around at the FACES of the people, all of them visible to her.",
        "must_not_show": "no low camera, no sandals or feet featured anywhere in this frame — the composition itself is the payoff.",
        "scene": (
            "The camera is up at standing head height in the middle of the glad crowd. "
            "The woman stands upright among them, turning her head slowly to look from "
            "one person to the next, and all around her are FACES — a laughing woman, "
            "a solemn old man, a wide-eyed child held on a shoulder, a young man "
            "grinning — every one of them clearly visible to her at her own eye level. "
            "Her expression is wonder, as if she is reading each face for the first "
            "time. Warm sunlit dust. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r005-b37", "out": "s37-straight-as-the-truth.jpeg", "seg": "n11b p1b",
        "window": "232.60-236.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["CAMERA", "WOMAN", "SYNAGOGUE"],
        "narration": "— standing as straight as the truth he had just told about her.",
        "must_show": "the final frame: her alone in the light, absolutely upright, chin level, empty hands at her sides, no stick anywhere.",
        "must_not_show": "no stick in frame at all; no bend, no lean; nothing supernatural; the crowd is soft and distant behind her.",
        "scene": (
            "The woman stands alone in the shaft of sabbath daylight, held from just "
            "below so her full height reads, absolutely upright — shoulders squared, "
            "spine straight, chin level, both empty hands open at her sides. Her "
            "weathered face is calm and lifted, her eyes steady and clear. There is no "
            "walking stick anywhere in the frame. The glad congregation are soft and "
            "out of focus behind her and the sunlit limestone wall rises past her "
            "shoulder. Each hand has five fingers."
        ),
    },
]

# ROUGH-DRAFT CONTINUITY (build-02 pattern): the rejected-look still for a
# beat, when it exists, is attached as the approved rough draft — its camera
# angle, blocking, positions and travel directions were bought with the
# 2026-07-29 authoring pass and must not be reinvented. Faces and identity
# always come from the FACE/CHARACTER lock images, never from the draft.
# A beat whose rough itself contains the defect being fixed goes in _NO_ROUGH
# (the row-2 b20 lesson: a rough carries its defects as faithfully as its
# virtues).
# b08's rough was a black-haired near-camera close-up (both defects copied on
# take 1); b09's rough contains the kneeling-woman wrong moment (copied
# faithfully, the row-2 b20 lesson); b25/b26 roughs carry the old set's OWN
# drifted ruler/farmer, which fought the identity anchors. Prose + anchors win.
_NO_ROUGH = {"v2-r005-b08", "v2-r005-b09", "v2-r005-b25", "v2-r005-b26"}
for _beat in BEATS:
    _asset = Path(__file__).resolve().parent / "assets" / _beat["out"]
    if _asset.is_file() and _beat["id"] not in _NO_ROUGH:
        _beat["rough_ref"] = str(_asset)
