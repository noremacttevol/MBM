#!/usr/bin/env python3
"""THE GREAT PLAN — Episode 31: Same Two Speeches, Modern Clothes.

The war in your pocket: Nephi's twenty-five-century-early transcript of the
modern pitch ("I am no devil"), the all-is-well lullaby, heaven's written
style guide (D&C 121), and Mormon's one-test sorter for every voice in your
day. Indicts the devil only — never a group, party, or generation.
Anchors: 2 Nephi 28:21-22; D&C 121:41-42; Moroni 7:13.
"""

NARRATOR, JESUS, FATHER, SCRIPTURE, WOMAN, DEVIL = (
    "narrator", "jesus", "father", "scripture", "woman", "devil")

EP = 331
NUM = 31
SLUG = "same-two-speeches"
TITLE = "Same Two Speeches, Modern Clothes"
META = "2 Nephi 28 · D&C 121 · Moroni 7"

SEGMENTS = [
    ("n1", NARRATOR,
     "You have watched this war from before the world to the restored "
     "kingdom. Three episodes left. First: where is the war right now? "
     "Answer — in your pocket. In your feed. In your head. Same two "
     "speeches. Modern clothes."),
    ("n2", NARRATOR,
     "Refresh the originals. One voice: Father, thy will be done, and "
     "the glory be thine forever. The other: I will save them all — "
     "force them all — wherefore give me thine honor. Keep both in your "
     "ear, and listen to your day."),
    ("n3", NARRATOR,
     "The devil's speech today almost never says worship me. It says: "
     "you deserve this. Skip the cost. Everyone does it. It hurts "
     "nobody. And its masterpiece line — there is no devil; that idea "
     "is medieval. Nephi transcribed that exact pitch twenty-five "
     "centuries early:"),
    ("s1", SCRIPTURE,
     "And behold, others he flattereth away, and telleth them there is "
     "no hell; and he saith unto them: I am no devil, for there is none "
     "— and thus he whispereth in their ears, until he grasps them with "
     "his awful chains, from whence there is no deliverance."),
    ("n4", NARRATOR,
     "I am no devil, for there is none. His best trick was never "
     "possession. It is public relations."),
    ("n5", NARRATOR,
     "And there is a second track, for the comfortable:"),
    ("s2", SCRIPTURE,
     "And others will he pacify, and lull them away into carnal "
     "security, that they will say: All is well in Zion; yea, Zion "
     "prospereth, all is well — and thus the devil cheateth their "
     "souls, and leadeth them away carefully down to hell."),
    ("n6", NARRATOR,
     "Carefully. Not dramatically — carefully. No horns. No contracts "
     "at midnight crossroads. Just comfort, a closed curtain, and one "
     "degree of drift a day."),
    ("n7", NARRATOR,
     "Now the Father's speech in modern clothes. His style guide is "
     "actually written down — how power from heaven is allowed to "
     "operate, and the only way:"),
    ("s3", SCRIPTURE,
     "No power or influence can or ought to be maintained by virtue of "
     "the priesthood, only by persuasion, by long-suffering, by "
     "gentleness and meekness, and by love unfeigned."),
    ("n8", NARRATOR,
     "Persuasion. Long-suffering. Gentleness. Love unfeigned. That is "
     "not just a rule for priesthood holders — it is the signature of "
     "heaven. So when any voice pushes, panics, shames, or forces you "
     "— check the return address."),
    ("n9", NARRATOR,
     "Here is the whole field guide in one test, from Mormon. Does a "
     "thing invite you to do good, to love God, to serve? Or does it "
     "entice you to hurt, to despair, to quit? Every voice in your day "
     "sorts into those two bins — every ad, every impulse, every "
     "three-a.m. thought:"),
    ("s4", SCRIPTURE,
     "That which is of God inviteth and enticeth to do good "
     "continually; wherefore, every thing which inviteth and enticeth "
     "to do good, and to love God, and to serve him, is inspired of "
     "God."),
    ("n10", NARRATOR,
     "And the council replays daily, in small. Every time you choose "
     "the harder right with your freedom intact, you re-cast your vote "
     "from before the world. And every time something tries to control "
     "you for your own good — a manipulator, an addiction, an "
     "algorithm — that is the other speech, still hunting a throne."),
    ("n11", NARRATOR,
     "You are not watching this war on a screen. You are in the cast. "
     "And your Father's side still fights exactly the way it fought in "
     "heaven — testimony, patience, love, and never, ever force. "
     "Choose like you chose. You have done this before."),
]

CARD_SEG = ("card", NARRATOR,
            "Every ad, impulse, and three-a.m. thought sorts into two "
            "speeches. You have voted before. Vote again.")

CARD_TEXT = ("Same two speeches.\n"
             "Modern clothes.\n"
             "\n"
             "THE GREAT PLAN\n"
             "Episode Thirty-One — Same Two Speeches")

SPOKEN = {}

LOCKS = {}
REFS = {}


def _p(scene, must_show, must_not_show, **kw):
    d = dict(era="modern")
    d.update(scene=scene, must_show=must_show, must_not_show=must_not_show)
    d.update(kw)
    return d


PICTURES = [
    ("p01", "n1", _p(
        "The war's current address: a crowded evening subway car, every "
        "face washed in the cold blue undersides of held devices — "
        "except ONE passenger mid-car who has looked UP, face turned to "
        "the window where the last daylight is running along the "
        "tunnel's mouth, lit warm and different. No screen contents "
        "visible anywhere; no face toward the lens.",
        "a device-lit subway car with one upturned face caught in warm "
        "window light",
        "readable screens, brand marks, faces to camera, caricature",
        wide=True)),
    ("p02", "n2", _p(
        "The originals: the premortal court reprised — the warm bright "
        "dais-side at the frame's left with the white-robed hosts "
        "gathered, and the frame's right third gone cold and dim and "
        "EMPTY, its boundary one smooth formless fade. The two "
        "speeches, staged the way episode one staged them. Camera high "
        "behind the crowd; no face back.",
        "the split court reprise — warm gathered left, cold empty "
        "dim right, smooth formless boundary",
        "any shape in the dim, faces to camera, weapons",
        era="heaven", devil=True, wide=True, locks=["COURT", "HOSTS"])),
    ("p03", "n3", _p(
        "You deserve this: a night-lit luxury storefront window of "
        "watches and leather without one readable brand — and hovering "
        "in the glass, the transparent reflection of a longing face "
        "gazing in, ghost-faint over the goods, streetlight rain-sheen "
        "on the pavement. The whisper, in retail.",
        "an anonymous luxury window with a ghost-faint longing "
        "reflection hovering over the goods",
        "readable brands or prices, the person solid, faces to lens",
        devil=True)),
    ("p04", "s1", _p(
        "The PR campaign: a huge street-corner billboard at dusk that "
        "is simply BLACK — a clean unmarked void over the busy "
        "sidewalk, no message, no image, nothing — while the crowd "
        "streams beneath it unbothered, nobody looking up. The best "
        "trick, rendered: a presence with no face, advertising its own "
        "absence.",
        "a clean unmarked black billboard over an unbothered "
        "streaming crowd at dusk",
        "any text or logo on the board, any figure in its black, "
        "faces to lens",
        devil=True, wide=True)),
    ("p05", ("s1", 0.6), _p(
        "The awful chains, house edition: a nightstand at three a.m. — "
        "a phone face-down still leaking cold light at its edges, and "
        "its charging cord coiled around itself in tight loops across "
        "the wood like a small white chain — a glass of water "
        "untouched, the sleeper's blurred shape beyond. Domestic. "
        "Quiet. Holding.",
        "a face-down leaking phone with its cord coiled chain-like "
        "on a 3 a.m. nightstand, sleeper blurred beyond",
        "readable screen, brand marks, horror styling",
        devil=True)),
    ("p06", "s2", _p(
        "All is well: a beautiful comfortable living room at NOON — "
        "deep sofa, feet in wool socks up on the ottoman, steam off a "
        "mug, soft lamplight — and every curtain DRAWN SHUT, the "
        "blazing midday edging the fabric in thin gold lines the room "
        "has chosen not to receive. Prosperity, with the light shut "
        "out.",
        "a cozy noon living room with feet up and every curtain "
        "shut, daylight edging the fabric",
        "squalor, screens readable, people's faces, gloom styling",
        devil=True)),
    ("p07", "n6", _p(
        "Carefully down: a gleaming mall escalator descending — one "
        "relaxed man riding it down, coffee in hand, jacket open, "
        "perfectly at ease, the polished chrome and warm retail light "
        "carrying him smoothly lower — seen from the floor below at "
        "the escalator's foot. Nothing sinister in frame; that is the "
        "point.",
        "one at-ease coffee-holding man descending a gleaming "
        "escalator, seen from below",
        "readable storefronts, crowds, his face to the lens, "
        "darkness",
        devil=True)),
    ("p08", "s3", _p(
        "Heaven's style guide: a grandmother's floured hands guide a "
        "child's small hands INTO bread dough on a wooden table — "
        "teaching by covering, not gripping, her patience visible in "
        "the lightness of the touch, morning kitchen light, flour in "
        "the air like weather. Persuasion, gentleness, love "
        "unfeigned — in one lesson.",
        "a grandmother's light floured hands guiding a child's "
        "hands into dough, morning kitchen light",
        "faces to camera, mess played for chaos, brand marks",
        )),
    ("p09", ("s3", 0.6), _p(
        "Long-suffering, live: a father KNEELS to toddler height in a "
        "hallway before his mid-tantrum child — his arms open and "
        "resting on his knees, not grabbing, not looming, his face "
        "calm and level with the small red furious one — waiting out "
        "the storm at eye level with the storm. Power, declining to "
        "be used.",
        "a father kneeling eye-level to a tantruming toddler, arms "
        "open and ungrabbing, calm",
        "anger in the father, spanking, faces to camera",
        )),
    ("p10", "n8", _p(
        "Check the return address: two envelopes side by side on a "
        "doormat — one printed in shouting red blocks and urgent "
        "stamps, all of it unreadable; one plain cream paper with a "
        "few lines of soft unreadable handwriting — morning light "
        "across both. Same mat. Different senders. You can tell "
        "before you open them.",
        "a shouting red unreadable envelope beside a plain "
        "handwritten one on a doormat",
        "readable words, addresses, hands",
        )),
    ("p11", "s4", _p(
        "Mormon's sorter: at a farm table by warm lamplight, a "
        "woman's practiced hands sort a heap of apples into two "
        "baskets — the sound one going right, a bruised one going "
        "left, one apple held mid-judgment in her palm — the "
        "evening's harvest becoming two clean bins. Every voice in "
        "your day, in fruit.",
        "hands sorting apples into two baskets by lamplight, one "
        "apple held mid-judgment",
        "her face prominent, rot graphic, text",
        )),
    ("p12", "n10", _p(
        "The harder right, made physical: five a.m. — a runner "
        "sliding their phone into a dresser drawer and pushing it "
        "SHUT with a knuckle, running shoes already laced in the "
        "lamplight, the window behind still night-black. The vote, "
        "re-cast before sunrise. Face unseen.",
        "a hand pushing a phone into a drawer at 5 a.m., laced "
        "running shoes waiting, face unseen",
        "readable screen, brand marks, faces",
        )),
    ("p13", ("n10", 0.5), _p(
        "The other speech, hunting: a bank of slot machines' "
        "carnival light washing over one slack motionless face — "
        "eyes reflecting the spin, hand resting on the button out "
        "of habit rather than hope, the rest of the room falling "
        "to black around the machine's embrace. No brands, no "
        "readable reels. A throne, being sat on.",
        "slot-light washing a slack motionless face, habitual "
        "hand on the button, room falling to black",
        "readable machines, other patrons, mockery",
        devil=True)),
    ("p14", ("n10", 0.8), _p(
        "The vote as a doorbell: a casserole dish balanced on one "
        "arm while the other hand presses a neighbor's doorbell — "
        "evening porch light warming the foil and the knuckle, a "
        "welcome mat below, the door a breath from opening. "
        "Service: the oldest ballot there is.",
        "a casserole balanced on one arm while a finger presses a "
        "porch doorbell at evening",
        "faces, house numbers, brand marks",
        )),
    ("p15", "n11", _p(
        "In the cast: the hallway mirror from episode two — but now "
        "the person stands square to it and the reflection is "
        "CLEAR: an ordinary face meeting its own eyes calmly, chin "
        "level, morning light even across the glass. The veil-"
        "washed stranger of episode two, replaced by somebody who "
        "knows their name.",
        "a person square to the hallway mirror with a CLEAR calm "
        "reflection meeting their own eyes",
        "the reflection looking at the camera instead, bathroom "
        "clutter, brand marks",
        )),
    ("p16", ("n11", 0.55), _p(
        "Heaven's way, working: in a warm living room, two men "
        "stand behind a seated young woman with their hands "
        "resting gently together on her head in blessing — her "
        "eyes closed, her mother's hand in hers, a grandfather "
        "watching with wet eyes from the sofa arm — priesthood "
        "operating exactly per the style guide. Reverent, plain, "
        "quiet.",
        "two men's gentle hands together on a seated woman's head "
        "in blessing, family close, eyes closed",
        "vestments, faces to camera, theatrics",
        )),
    ("p17", ("n11", 0.85), _p(
        "The daily truce: a city skyline at first light — the "
        "night's window-lights going out block by block as the "
        "sunrise takes over the job, the sky clean, the streets "
        "still. The war pauses for no one; the light still wins "
        "the morning, every morning. No people.",
        "city window-lights going out block by block as sunrise "
        "takes over, clean sky",
        "billboards readable, traffic, drawn rays",
        wide=True)),
]
