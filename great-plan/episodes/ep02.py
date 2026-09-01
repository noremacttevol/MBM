#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 2: We Were There.

Who was standing in the council room: us. Spirit children of God, known
before the womb, shouting for joy at the foundations of the world.
Anchors: Jeremiah 1:5; Job 38:4,7; Abraham 3:22-23; Acts 17:28.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, DEVIL = ("narrator", "jesus", "father",
                                             "scripture", "devil")

EP = 302
NUM = 2
SLUG = "we-were-there"
TITLE = "We Were There"
META = "Abraham 3 · Job 38 · Jeremiah 1"

SEGMENTS = [
    ("n1", NARRATOR,
     "Last time, you watched two speeches decide the fate of the world. "
     "This time, something harder to believe. You were in the room."),
    ("n2", NARRATOR,
     "Scripture is not shy about this. When God needed to steady a "
     "frightened young prophet, He reminded Jeremiah where he came from:"),
    ("g1", FATHER,
     "Before I formed thee in the belly I knew thee; and before thou "
     "camest forth out of the womb I sanctified thee, and I ordained thee "
     "a prophet unto the nations."),
    ("n3", NARRATOR,
     "Known before the womb. Not manufactured at birth — known. And when "
     "Job hit the floor of his suffering, God lifted his chin with a "
     "memory:"),
    ("g2", FATHER,
     "Where wast thou when I laid the foundations of the earth? When the "
     "morning stars sang together, and all the sons of God shouted for "
     "joy?"),
    ("n4", NARRATOR,
     "All the sons of God, shouting for joy, while the earth was being "
     "built. That shout was ours. We watched the foundations poured — and "
     "we cheered, because that world was being built for us."),
    ("s1", SCRIPTURE,
     "Now the Lord had shown unto me, Abraham, the intelligences that "
     "were organized before the world was; and among all these there were "
     "many of the noble and great ones."),
    ("g3", FATHER,
     "Abraham, thou art one of them; thou wast chosen before thou wast "
     "born."),
    ("n6", NARRATOR,
     "Chosen before you were born. And that is not poetry reserved for "
     "Abraham — it is the family truth. Paul stood in the middle of "
     "Athens and said it to strangers:"),
    ("s2", SCRIPTURE,
     "For in him we live, and move, and have our being; as certain also "
     "of your own poets have said, For we are also his offspring."),
    ("n7", NARRATOR,
     "Offspring. Not inventions. Not accidents of chemistry. Children — "
     "of glorified Parents — with eternity behind us, and their kind of "
     "life ahead of us, if we want it."),
    ("n8", NARRATOR,
     "Which means the stranger you pass in traffic is older than the "
     "earth. The child asleep in your arms watched the foundations of the "
     "world. And the face in your mirror belongs to someone who stood in "
     "that council — and shouted for joy."),
    ("n9", NARRATOR,
     "The devil needs you to forget every word of this. You're worthless. "
     "You're an animal. You're alone. You're an accident. Every one of "
     "those lies is aimed at a single target: your memory of who you "
     "are."),
    ("n10", NARRATOR,
     "And God's first move, in every age, is the opposite. He tells His "
     "children who they are. Because a person who knows they are a child "
     "of God — chosen before birth — is very, very hard to enslave."),
    ("n11", NARRATOR,
     "You are not a body that happens to have a soul. You are an eternal "
     "being who wanted this life so much you shouted when it was "
     "announced. Live like someone who chose to be here. Because you "
     "did."),
]

CARD_SEG = ("card", NARRATOR,
            "You are older than the earth. You are a child of God. And you "
            "chose to be here.")

CARD_TEXT = ("You chose to be here.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Two — We Were There")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="heaven")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The premortal council court again, re-established from a new "
        "high angle: the ocean of white-robed men and women of every "
        "ancestry filling the descending luminous terraces, all facing "
        "the distant bright dais, the camera high behind the rear ranks "
        "shooting down past their heads and shoulders. Dawn-gold light "
        "over everything; not one face toward the lens.",
        "the vast white-robed council seen from high behind toward the "
        "distant bright dais",
        "any face to camera, wings, cream robes in the crowd, beams",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p02", "n2", _p(
        "Young Jeremiah alone at night: a thin young man in rough "
        "prophet's wool sits against a mud-brick wall by a single clay "
        "lamp, knees drawn up, face lifted from his hands as if a voice "
        "just said his name — three-quarter profile, lamplight warm on "
        "a face too young for the call it is receiving.",
        "a very young man by lamplight against mud-brick, face lifting "
        "in three-quarter, startled awe",
        "his eyes on the lens, scrolls with readable text, halo",
        era="ancient")),
    ("p03", "g1", _p(
        "Known before the womb: a close, reverent frame of an ancient "
        "mother's hands resting on her heavily pregnant belly, warm "
        "lamplight raking the woven earth-tone cloth of her dress, one "
        "thumb moving in a slow caress. No face in frame — just the "
        "hands, the curve, and the light.",
        "two hands resting warm on a pregnant belly in lamplight, close",
        "faces, jewellery, modern fabric, text",
        era="ancient")),
    ("p04", "n3", _p(
        "Job on the ash heap: a ruined man kneeling in grey dust outside "
        "a broken wall at dusk, garments torn, and his head RISING — "
        "caught in the exact moment his downcast face begins to lift "
        "toward the sky, seen in profile from beside him. The last light "
        "catches the tear tracks and the first flicker of remembering.",
        "a devastated kneeling man in profile, head caught mid-lift "
        "toward the sky at dusk",
        "his eyes on the lens, boils overdone, comforters present",
        era="ancient")),
    ("p05", "g2", _p(
        "The foundations of the earth, watched from heaven: far below "
        "an immense vantage, a world half-made — dark ocean sheets and "
        "seams of new stone spreading under slow veils of cloud, morning "
        "light flooding across the curve of it — vast, silent, mid-"
        "creation. No figures anywhere; pure scale and birth.",
        "a half-formed world of new ocean and stone seen from far above, "
        "morning light crossing it",
        "any figure, modern continents recognizable, text, rays",
        )),
    ("p06", ("g2", 0.58), _p(
        "The shout at the foundations: along the court's outer "
        "balustrade, a great rank of white-robed spirits with arms "
        "flung high, caught mid-cheer — seen from behind and beside so "
        "the joy sweeps away from the camera and out toward the bright "
        "deep beyond the rail where the new world is being built below. "
        "Not one face turns back; the jubilation is aimed outward.",
        "a rank of spirits from behind with arms flung high toward the "
        "bright deep beyond the balustrade",
        "faces to camera, wings, the earth visible in detail, beams",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p07", "n4", _p(
        "The joy up close: five or six young faces of different "
        "ancestries mid-cheer — laughing, tears bright, arms half-"
        "raised, every gaze aimed up and left past the camera toward "
        "the unseen new world. Real teeth, real tears, real joy; "
        "nobody looks at the lens.",
        "five or six cheering tearful joyful faces aimed up-left past "
        "the camera",
        "anyone facing the lens, wings, glowing skin, cream robes",
        locks=["HOSTS"])),
    ("p08", "s1", _p(
        "Abraham under the desert stars: the aged patriarch stands "
        "outside his tent at full night, head back, face washed in "
        "starlight as the whole sweep of the heavens burns above the "
        "black horizon — seen from behind and beside, his silver beard "
        "and mantle edge-lit by a low fire out of frame.",
        "an aged patriarch from behind-beside, head back under an "
        "immense starry sky, tent and fire-warmth at the edge",
        "his eyes on the lens, telescope, city light, beams",
        era="ancient", wide=True)),
    ("p09", "s1", _p(
        "What Abraham was shown: ranks upon ranks of white-robed "
        "spirits standing in ordered assembly, receding row after row "
        "into brilliant distance — and EVERY VISIBLE PERSON IS A "
        "DIFFERENT INDIVIDUAL: different faces, heights, builds and "
        "ancestries in every row, no repeated face, no mirrored or "
        "duplicated rows, no tiling pattern — a real crowd, not a "
        "pattern, dissolving into light "
        "— seen from a raised angle along the front rank's profile so "
        "the endless organization of them is the subject. Among the "
        "nearest rows, a scattering of faces carry unmistakable "
        "gravity and command — the noble and great ones — every gaze "
        "aimed forward, none at the lens.",
        "ordered ranks of spirits receding into brilliant distance, "
        "nearest rows carrying visible gravity, seen along the profile",
        "faces to camera, wings, military uniforms, banners",
        wide=True, locks=["COURT", "HOSTS"])),
    ("p10", "g3", _p(
        "Chosen before birth: the Father stands before a small group "
        "of a dozen spirits at the court's edge, His hand extended "
        "palm-up toward ONE young man at the group's front — a "
        "commission, not a summons — seen from beside the group in "
        "three-quarter so the Father's warm profile and the young "
        "man's awed profile face each other across the open hand. The "
        "others watch the exchange; nobody faces the lens.",
        "the Father's open palm-up hand extended to one awed young "
        "spirit before a small watching group, profiles facing across "
        "the gesture",
        "either face to the lens, kneeling, crowns, wings, halos",
        locks=["FATHER", "COURT", "HOSTS"])),
    ("p11", "n6", _p(
        "Paul in Athens: the apostle mid-stride on the stone of Mars "
        "Hill, one arm sweeping toward the marble city and its temples "
        "below, his weathered bearded face in profile fired with "
        "conviction — the camera behind his listeners' shoulders so "
        "the gesture carries out over Athens. Bright Mediterranean "
        "light.",
        "a bearded apostle mid-gesture over marble Athens from behind "
        "his listeners' shoulders",
        "faces to camera, readable inscriptions, togas in cream",
        era="first-century", wide=True)),
    ("p12", "s2", _p(
        "The listeners on Mars Hill: a tight group of Athenian faces — "
        "an old philosopher, a young sceptic, a woman at the edge — "
        "caught at the moment the words land: offspring of God. "
        "Furrowed brows loosening, eyes fixed left past the camera on "
        "the unseen speaker. Marble and bright sky soft behind.",
        "struck Athenian faces aimed left past the camera, scepticism "
        "loosening into wonder",
        "anyone facing the lens, laughter, scrolls with readable text",
        era="first-century")),
    ("p13", "n7", _p(
        "The family truth, now: three generations on a porch at golden "
        "hour — a grandmother mid-laugh, parents leaning on the rail, "
        "kids sprawled on the steps — every face turned into the "
        "conversation or the sunset, none toward the camera, which "
        "watches from the yard past a porch post. Warm, ordinary, "
        "eternal.",
        "a three-generation family on a golden-hour porch, all faces "
        "into the conversation or the light",
        "anyone facing the lens, phones, brand logos, readable text",
        era="modern")),
    ("p14", "n8", _p(
        "Traffic, re-seen: a city crosswalk at golden hour, a stream "
        "of ordinary people mid-stride crossing away from and across "
        "the camera — a nurse, a workman, an old man with a cane, a "
        "student — long warm light throwing their shadows, every face "
        "in profile or turned away. Older than the earth, all of "
        "them.",
        "ordinary crosswalk crowd mid-stride in long golden light, "
        "faces away or in profile",
        "anyone facing the lens, readable signs or screens, brand "
        "logos",
        era="modern", wide=True)),
    ("p15", ("n8", 0.4), _p(
        "A child asleep in a parent's arms in a dim modern living "
        "room, evening lamp warm behind them — the parent's cheek "
        "resting on the small head, both faces soft, eyes closed, "
        "close frame. The one in the arms watched the foundations of "
        "the world.",
        "a sleeping child against a parent's shoulder, both eyes "
        "closed, warm lamp light, close",
        "open eyes to the lens, screens, brand marks",
        era="modern")),
    ("p16", ("n8", 0.72), _p(
        "The mirror: a person stands in a morning hallway facing a "
        "wall mirror, seen from behind their shoulder — and the "
        "reflected face is dissolved in the window light flooding "
        "across the glass, a bright soft shape no one could identify. "
        "It could be anyone. It is the viewer.",
        "a person from behind facing a mirror whose reflection is "
        "washed unidentifiable by window light",
        "an identifiable reflected face, bathroom clutter, brand "
        "marks",
        era="modern")),
    ("p17", "n9", _p(
        "A young man sits on the FLOOR of a dark modern bedroom, his "
        "back against the side of his bed, knees drawn up — seen "
        "FULL-LENGTH from the front-side at floor level, the whole "
        "VERTICAL of the dark room above him filling the top half "
        "of the frame. The only light is a cold blue-white spill "
        "rising from an unseen screen at his knees, hollowing his "
        "down-turned face. The darkness above and around him is "
        "FORMLESS — bare dim wall and ceiling shadow, empty of any "
        "shape. His gaze is down at the light.",
        "a young face hollowed by cold screen-light in pressing "
        "formless dark, gaze down, shoulders sunk",
        "ANY shape or figure in the darkness, a readable screen, his "
        "eyes on the lens",
        era="modern", devil=True)),
    ("p18", "n10", _p(
        "The counter-move: a different young woman throws open heavy "
        "curtains and morning light floods over her — caught from "
        "beside the window so the light crosses the frame onto her "
        "lifted face and the room wakes up behind her: plants, books, "
        "colour. Her eyes are closed into the warmth; the darkness is "
        "simply gone.",
        "a young woman opening curtains, morning light flooding her "
        "closed-eyed lifted face and waking the room",
        "her eyes on the lens, halo effects, brand marks, screens",
        era="modern")),
    ("p19", "n11", _p(
        "The choice, remembered: back in the premortal court — one "
        "young spirit with SHORT dark hair, seen from directly "
        "behind, stepping forward out of the front rank toward a "
        "broad even warm brightness that fills the whole horizon "
        "ahead — never a circle, burst or disc of light, and nothing "
        "bright centred behind his head. His robe is the hosts' "
        "bright pure WHITE, unmistakably not cream. Face never "
        "visible. The same step every person on earth once took.",
        "one spirit from directly behind mid-step toward immense warm "
        "light, face never visible",
        "his face or profile, anyone else near the lens, beams",
        locks=["COURT", "HOSTS"])),
    ("p20", ("n11", 0.55), _p(
        "The choice, arriving: a newborn lifted wet and crying into "
        "warm lamplight by its father's two careful hands in a dim "
        "home birth room, the mother's exhausted radiant face soft in "
        "the background blur — first breath of the life that was "
        "chosen before the world.",
        "a father's two hands lifting a crying newborn into warm "
        "light, mother's soft radiant blur beyond",
        "clinical equipment, graphic detail, anyone facing the lens",
        era="modern")),
    ("p21", ("n11", 0.82), _p(
        "Living like you chose it: a man steps out his front door "
        "into full morning sun, jacket over one shoulder, seen from "
        "behind at the threshold as the light takes him — the door "
        "frame dark around the camera, the world ahead bright and "
        "wide open.",
        "a man from behind stepping through his front door into wide "
        "bright morning",
        "his face, house numbers or readable mail, brand marks",
        era="modern")),
]
