#!/usr/bin/env python3
"""V2 beat map — row 40, build-40-the-friend-at-midnight (Luke 11:1-13).

COVERAGE: 56 pictures over 312.3 s = 5.6 s/picture (matches the library density).

LESSON-12 PASS (2026-08-05): movie coverage, not group portraits. Six true
wides remain, each stating camera-to-back geometry in its own scene text:
b01 (grove establish), b03 (the watchers' reverse), b19 (neighbour-house
establish), b22 (the refusal), b25 (the lane waking), b38 (rooftop scale).
Every other beat is a single, two-shot, over-shoulder or insert containing
only the people its moment is about. b56 was added so the payoff's RISE has
its own frame before the giving (a frame per verb — the John 21 standard).
Token split: NEIGHBOR-DOOR (street face) vs NEIGHBOR-HOUSE (interior), plus
COURTYARD and LIT-HOUSE, so each recurring place can carry one plate.

SCRIPTURE FACTS (Luke 11:1-13 KJV):
  v1    "as he was PRAYING in a certain place, when he CEASED, one of his
        disciples said unto him, Lord, TEACH US TO PRAY" — the frame is a
        DAWN prayer place: Jesus finishing prayer apart among olive trees,
        the disciples waiting at a respectful distance, then asking. A
        staging no earlier row has used.
  v2-4  the Lord's Prayer given — "Our FATHER" — the child's word; the
        narration leans hard on the audacity of that first word.
  v5-8  the friend at midnight: travel happened at night (heat); a guest
        at midnight was a real event and feeding him a village-wide duty.
        "Friend, lend me THREE LOAVES" — he begs bread HE will not eat.
        The house behind the door is ONE ROOM: family on one sleeping
        platform, one blanket, a heavy bar — the refusal is REAL and
        REASONABLE ("my children are with me in bed").
        v8's word (anaideia) = SHAMELESSNESS, not persistence — the knocker
        is willing to look like a fool; shutters bang open, dogs bark.
        "he will rise and give him AS MANY AS HE NEEDETH" — an armful,
        more than asked.
  KEY INTERPRETIVE LAW (b34-b38): the sleeping neighbour is the CONTRAST
        to God, not the picture of him — 'he was never asleep at all.'
        The closing beats hang on a house whose lamp is already lit.
  v11-13 bread/stone, fish/serpent, egg/scorpion — each pair is a
        LOOKALIKE (flat river stone like a loaf; pale curled scorpion like
        an egg); the father-child beats are warm and domestic, and no
        father ever hands the counterfeit. "HOW MUCH MORE shall your
        heavenly Father give..."

TIME OF DAY: frame beats are DAWN (the prayer place) and morning. The
parable is FULL MIDNIGHT throughout — moonless lanes, one clay lamp, deep
blue darkness (scripture-required; not a defect). The father-child beats
are warm ordinary daylight. The closing beats are night again — but with
one WINDOW ALREADY LIT, the row's final image.

CONTENT-CARE: row 40 has no flag in §3. The serpent and scorpion appear
ONLY in the father's refusing hand-beats as compared objects — never
threatening a child.

CHANGING CONDITION (kept OUT of the locks): the bread — none on the
asker's shelf, three loaves begged, an ARMFUL given; and the neighbour's
door — barred, cracked, opened wide. Both stated per-beat.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "ASKER": (
        "ASKER LOCK: the man who knocks is the same man in every shot — "
        "mid-thirties, lean and earnest, with a short curly black beard, "
        "expressive worried brows and quick warm eyes. He wears a plain "
        "DARK RUST-BROWN tunic with a rope belt, and carries a small "
        "single-flame clay lamp in the night beats (never cream, never "
        "white). His face is shown clearly."
    ),
    "NEIGHBOR": (
        "NEIGHBOUR LOCK: the man behind the door is the same man in every "
        "shot — about fifty, heavy-set and bone-tired, with a flattened "
        "sleep-creased face, a thick dark beard going grey and hair "
        "pushed up on one side from the pillow. He wears a rumpled DARK "
        "OLIVE-GREY night tunic (never cream, never white). His face is "
        "shown clearly — exhausted and decent, never a villain."
    ),
    "TRAVELER": (
        "TRAVELLER LOCK: the midnight guest is the same man in every "
        "shot — about forty, dust-caked and hollow with hunger, with a "
        "matted dark beard, sun-scoured skin and road-sore feet. He "
        "wears a travel-stained DUSTY INDIGO cloak over a worn tunic, "
        "with a flat empty provision bag on his shoulder (never cream, "
        "never white). His face is shown clearly."
    ),
    "LANE": (
        "VILLAGE NIGHT LOCK: the sleeping village at midnight — a narrow "
        "packed-earth lane between shuttered honey-stone houses, heavy "
        "plank doors, a low stone water trough, and deep moonless "
        "blue-black darkness broken only by whatever single lamp a beat "
        "carries. The same lane, doors and trough in every night beat."
    ),
    "ASKER-HOUSE": (
        "ASKER'S HOUSE LOCK: the asker's one-room house — a low doorway, "
        "a single room with a bread shelf on the wall, a water jar, a "
        "rush mat by the hearth's banked coals, and one small window to "
        "the lane. The same shelf, jar and window throughout."
    ),
    "NEIGHBOR-HOUSE": (
        "NEIGHBOUR'S HOUSE LOCK: the neighbour's one-room house — a "
        "heavy plank door with a thick wooden bar across iron staples, "
        "and within, one raised sleeping platform where a whole family "
        "lies under one broad dark blanket, small children between the "
        "parents, and on the wall shelf a row of round loaves under a "
        "cloth. The same door, bar, platform and shelf throughout."
    ),
    "NEIGHBOR-DOOR": (
        "NEIGHBOUR'S DOOR LOCK: the neighbour's street door is the same in "
        "every shot — heavy vertical planks of dark old wood, a thick wooden "
        "bar seated in black iron staples visible through any gap, a worn "
        "stone step below, and at hand height a patch of the planks worn "
        "smooth and pale by long knocking. The same planks, staples, step "
        "and worn patch throughout."
    ),
    "FATHER-SON": (
        "FATHER AND SON LOCK: the father of the comparison beats is the "
        "same man in every shot — broad and gentle, about forty, with a "
        "full brown beard and patient crinkled eyes, in a DARK "
        "CHESTNUT-BROWN tunic; his son is the same boy — about six, "
        "curly dark hair, huge dark eyes, in a little DUSTY-BLUE tunic "
        "(never cream, never white). Both faces shown clearly."
    ),
    "GROVE": (
        "PRAYER PLACE LOCK: a quiet olive grove on a hillside at dawn — "
        "old gnarled trunks, dew-grey grass, a flat prayer stone apart "
        "from the path, and the disciples' waiting place lower down the "
        "slope. The disciples wear SATURATED DEEP earth colours (never "
        "cream, never white; only Jesus wears cream). Faces shown "
        "clearly."
    ),
    "COURTYARD": (
        "FAMILY COURTYARD LOCK: the father-and-son beats share one sunlit "
        "family courtyard — low honey-stone walls, a worn timber house "
        "door, a small fig tree in one corner, a stone bench and a water "
        "jar by the wall, a packed-earth floor. The same walls, door, "
        "tree, bench and jar in every courtyard beat."
    ),
    "LIT-HOUSE": (
        "THE WAKEFUL HOUSE LOCK: the one lit house is the same in every "
        "shot — a modest honey-stone house at the lane's turning, one "
        "warm-lit leaded window beside a timber door with NO bar and no "
        "staples, a worn stone step, and lamplight laid in a long "
        "rectangle on the packed earth outside. The same window, door and "
        "step throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r040-b01", "out": "s01-and-it-came-to-pass.jpeg", "seg": "s1",
        "window": "0.28-11.29", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "And it came to pass, that, as he was praying in a certain place, "
            "when he ceased, one of his disciples said unto him, Lord, teach us "
            "to pray, as John also taught his disciples."
        ),
        "must_show": "SCRIPTURE-EXACT: the ask — Jesus rising from the prayer stone in the dawn grove, and one disciple stepping up from the waiting group below with the request already on his face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the disciples kept their distance while he prayed — that respect is in the geometry.",
        "scene": (
            "In the grey-gold first light of the olive grove Jesus "
            "rises from the flat prayer stone apart from the path, "
            "stillness still on him — and up the dew-grey slope "
            "from the little knot of waiting disciples one man has "
            "come forward ahead of the rest, hands open, the "
            "request already forming on his earnest face while his "
            "brothers watch from below among the old trunks. The "
            "camera stands level on the slope's flank and holds "
            "the whole ask in profile — Jesus high at the stone, "
            "the climbing man mid-slope, the waiting group low — "
            "every gaze in the group running one way, up the hill "
            "to Jesus, the path falling away out of the frame's "
            "lower corner. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r040-b02", "out": "s02-he-knocks-again.jpeg", "seg": "n10",
        "window": "136.01-137.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR-DOOR"],
        "narration": "He knocks again.",
        "must_show": "the second knock — a close shot of the asker's knuckles against the heavy plank door in the lamplit dark, jaw set.",
        "must_not_show": "no halo, glare or rim-light; one small lamp's light only; determination hardening on his face.",
        "scene": (
            "Close at the heavy plank door in the deep night: the "
            "asker's knuckles caught mid-rap against the wood, his "
            "little clay lamp held up in the other hand throwing "
            "its small warm circle on the door's grain and the "
            "iron staples of the bar beyond — and his lean face "
            "beside the light with its jaw newly set, embarrassment "
            "losing to need. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r040-b03", "out": "s03-his-disciples-had-watched-him.jpeg", "seg": "n1",
        "window": "12.79-17.46", "wide": True, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "His disciples had watched him pray for years, and watched him come "
            "back from it different."
        ),
        "must_show": "the watching — from the disciples' waiting place: Jesus apart at the prayer stone in the dawn distance, the watchers' faces studying him with longing.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the difference they see is stillness and bearing — nothing visual beyond posture and light of dawn.",
        "scene": (
            "From the waiting place lower on the slope: the "
            "camera sits low behind the nearest disciple's "
            "shoulder, the two men beside him in three-quarter "
            "with their cloaks pulled against the dawn chill, and "
            "every visible face is turned up the hill to where Jesus "
            "kneels apart at the flat stone, a still cream-clad "
            "figure small in the grey-gold light — the watchers' "
            "faces holding the particular longing of men looking "
            "at something they want and do not know how to reach, "
            "the slope climbing out of the frame's top edge toward "
            "him. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r040-b04", "out": "s04-so-one-morning-they-asked.jpeg", "seg": "n1",
        "window": "17.46-20.69", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "So one morning they asked him for the thing they wanted most.",
        "must_show": "the ask up close — the forward disciple's face making the request, hope and shyness together; Jesus's attention turned fully on him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the disciple's courage visible — asking for this cost something.",
        "scene": (
            "A close two-shot in the dawn light: the forward "
            "disciple's weathered face caught mid-request, hope "
            "and shyness fighting in it like a boy asking a "
            "master craftsman for his trade — and Jesus turned "
            "fully toward him, head slightly tipped, receiving "
            "the question with the whole of his attention as the "
            "grove lightens behind them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b05", "out": "s05-so-he-gave-them-a.jpeg", "seg": "n2",
        "window": "23.26-24.81", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "must_show": "the giving — an over-shoulder shot: Jesus leaning in with his forearms on his knees, handing the words over; the nearest listener's profile mouthing each phrase after him.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a gift being handed over, intimate and unhurried — not a staged class.",
        "narration": "So he gave them a prayer.",
        "scene": (
            "Over the shoulder of one seated disciple in the "
            "strengthening light: Jesus leans in close with his "
            "forearms on his knees, giving them the words slowly, "
            "and at the frame's near edge the listener's profile "
            "mouths each phrase after him, eyes shut to hold "
            "them — a treasure changing hands in the early "
            "morning under the olive trunks. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b06", "out": "s06-it-was-the-word-a.jpeg", "seg": "n2",
        "window": "28.62-31.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER-SON", "COURTYARD"],
        "narration": "It was the word a small child uses.",
        "must_show": "the word itself pictured — a small child running with lifted arms to a father who is already crouching to catch him; 'Abba' in one image.",
        "must_not_show": "no halo, glare or rim-light; pure domestic instinct — the run and the crouch, both already happening.",
        "scene": (
            "In a sunlit courtyard a small barefoot child runs "
            "full-tilt with both arms lifted high, mouth open in "
            "a call — and three steps away his father is already "
            "down in a crouch with his arms spread, already "
            "braced, already smiling, the catch as certain as the "
            "ground — the whole meaning of one small word painted "
            "in the space between them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b07", "out": "s07-when-ye-pray-say-our.jpeg", "seg": "j0",
        "window": "32.02-37.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "When ye pray, say, Our Father which art in heaven, Hallowed be thy "
            "name."
        ),
        "must_show": "SCRIPTURE-EXACT: the first words given — a medium shot of Jesus speaking them with his eyes lifted; one bowed head soft at the frame's lower edge as the prayer begins to exist in the world.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the moment's weight carried in his unhurried face — the world's most-prayed words at their first hearing.",
        "scene": (
            "A medium shot in the full gold of risen dawn: Jesus "
            "speaks with his face lifted toward the light between "
            "the olive branches, unhurried, giving each word its "
            "own room — and soft at the frame's lower edge one "
            "disciple's head has bowed over folded hands as the "
            "first prayer any of them will teach their own "
            "children enters the world in a grove before "
            "breakfast. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r040-b08", "out": "s08-he-taught-them-to-walk.jpeg", "seg": "n3",
        "window": "38.56-41.38", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER-SON", "COURTYARD"],
        "narration": "He taught them to walk up to God and call him Father.",
        "must_show": "the audacity pictured — the courtyard child now standing at his father's knee mid-conversation, one small hand flat on the big forearm, utterly unafraid.",
        "must_not_show": "no halo, glare or rim-light; access without ceremony — the child interrupts and is welcome.",
        "scene": (
            "Close in the warm courtyard light: the small boy "
            "stands at his seated father's knee, one little hand "
            "laid flat and possessive on the big forearm, face "
            "tipped up mid-sentence in the middle of the man's "
            "work — and the father has set his tool down and bent "
            "his head to listen as though no other appointment "
            "exists — the door that is never barred, painted "
            "small. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r040-b09", "out": "s09-people-travelled-at-night-there.jpeg", "seg": "n4",
        "window": "49.16-53.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["TRAVELER"],
        "narration": (
            "People travelled at night there, because the daytime heat could "
            "kill you."
        ),
        "must_show": "night travel established — the dusty traveller on the dark road under thick stars, walking by moonless starlight, the land holding the day's heat.",
        "must_not_show": "no halo, glare or rim-light; deep night correct and required; the traveller small on a long dark road.",
        "scene": (
            "Under a moonless sky thick with stars the lone "
            "traveller walks the pale ribbon of road through dark "
            "country, small and full-length in the wide black "
            "land, his indigo cloak grey with dust, the flat "
            "provision bag hanging empty at his side — the hills "
            "black around him and the night air still shimmering "
            "faintly with the day's stored heat off the stones. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b10", "out": "s10-so-a-friend-really-could.jpeg", "seg": "n4",
        "window": "53.34-59.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "TRAVELER", "ASKER-HOUSE", "LANE"],
        "narration": (
            "So a friend really could turn up at midnight, starving — and you "
            "did not send him away."
        ),
        "must_show": "SCRIPTURE-EXACT: the arrival — the traveller swaying in the asker's low doorway at midnight, and the asker already pulling him inside by both arms.",
        "must_not_show": "no halo, glare or rim-light; the welcome instant and total — no hesitation at the threshold.",
        "scene": (
            "A tight two-shot at the low doorway in the deep "
            "night: the dust-caked traveller stands swaying with "
            "exhaustion, one hand "
            "braced on the jamb — and the asker, night tunic "
            "half-tied, is already pulling him in over the "
            "threshold by both forearms, his lean face all "
            "welcome and alarm at once, the little clay lamp on "
            "the floor throwing both their shadows huge up the "
            "wall. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r040-b11", "out": "s11-feeding-a-guest-was-a.jpeg", "seg": "n4",
        "window": "59.41-62.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["TRAVELER", "ASKER-HOUSE"],
        "narration": "Feeding a guest was a duty the whole village shared.",
        "must_show": "the guest seated — the traveller settled on the rush mat with his feet being poured water over, the courtesy of the whole culture in one basin.",
        "must_not_show": "no halo, glare or rim-light; hospitality as law — done properly even in a house with no bread.",
        "scene": (
            "Inside the one small room the traveller sits eased "
            "down onto the rush mat by the banked coals, head "
            "tipped back against the wall with exhaustion — while "
            "the asker kneels before him pouring a thin stream of "
            "water from the jar over the man's cracked and "
            "road-sore feet into a clay basin, the full ancient "
            "courtesy paid first, in a house whose bread shelf "
            "hangs empty behind them. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b12", "out": "s12-so-a-man-opens-his.jpeg", "seg": "n5",
        "window": "63.29-67.09", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "TRAVELER", "ASKER-HOUSE"],
        "narration": (
            "So a man opens his door at midnight to a friend who has walked all "
            "day."
        ),
        "must_show": "the friendship — a close two-shot: the traveller's hollow dust-caked face and the asker's worried warm one, forehead near forehead in the lamplight; old friends, bad hour.",
        "must_not_show": "no halo, glare or rim-light; the history between them visible — grip on the shoulder, relief and worry mixed.",
        "scene": (
            "A close lamplit two-shot on the rush mat: the "
            "traveller's hollow, dust-grimed face sagging with "
            "the day's miles, and the asker's face a hand's width "
            "away, worried and glad at once, his hand gripped "
            "hard on his friend's shoulder — two men whose "
            "friendship is old enough that midnight needs no "
            "apology. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r040-b13", "out": "s13-then-he-looks-at-his.jpeg", "seg": "n5",
        "window": "67.09-70.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "ASKER-HOUSE"],
        "narration": "Then he looks at his own shelf, and there is nothing on it.",
        "must_show": "SCRIPTURE-EXACT: 'I have nothing to set before him' — the asker's lamp raised to the bread shelf: bare boards, a scatter of crumbs, an empty basket.",
        "must_not_show": "no halo, glare or rim-light; the emptiness plain in the small lamp's circle — nothing means nothing.",
        "scene": (
            "The asker holds his little clay lamp up to the wall "
            "shelf and the light finds it bare: scrubbed boards, "
            "a fine scatter of old crumbs, one empty tipped "
            "basket, the cloth that should cover loaves folded "
            "flat and useless — and beneath the raised lamp his "
            "face falls into the particular dismay of a host "
            "with a guest and a shelf with nothing. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b14", "out": "s14-so-he-picks-up-his.jpeg", "seg": "n6",
        "window": "72.51-79.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "LANE"],
        "narration": (
            "So he picks up his little clay lamp and walks out into a sleeping "
            "village, toward the one door he knows still has bread behind it."
        ),
        "must_show": "SCRIPTURE-EXACT: the midnight walk — the asker alone in the black lane with his one small flame, every house shuttered and dark, heading somewhere specific.",
        "must_not_show": "no halo, glare or rim-light; one lamp against a whole sleeping village — the smallness of the light is the picture.",
        "scene": (
            "Down the narrow blue-black lane between shuttered "
            "houses the asker walks quickly with his little clay "
            "lamp cupped against the night air, its single flame "
            "the only light in the entire street, throwing his "
            "hurrying shadow along the shuttered doors and the "
            "stone trough — a small determined fire moving "
            "through a village lying fast asleep under the "
            "stars. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r040-b15", "out": "s15-which-of-you-shall-have.jpeg", "seg": "jv5",
        "window": "80.40-85.88", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Which of you shall have a friend, and shall go unto him at "
            "midnight, and say unto him,"
        ),
        "must_show": "the teller mid-tale — Jesus with a storyteller's raised hand and one eyebrow up on 'which of you'; the two nearest listeners grinning at the frame's edge; the question aimed at them.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the humour of the setup visible — this parable begins as a joke on the listeners.",
        "scene": (
            "Past the shoulders of two grinning disciples in the "
            "bright morning grove: Jesus tells it with a "
            "storyteller's lifted hand and one eyebrow raised on "
            "'which of you' — and the two listeners at the "
            "frame's near edge are already trading looks, one "
            "jabbing a thumb at his neighbour in mock accusation "
            "— a story that has clearly happened to somebody "
            "here, landing exactly where he aimed it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b16", "out": "s16-louder.jpeg", "seg": "n10",
        "window": "137.46-138.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR-DOOR"],
        "narration": "Louder.",
        "must_show": "the escalation — the asker's whole flat hand now banging the door, lamp set down on the step, both hands committed.",
        "must_not_show": "no halo, glare or rim-light; the lamp on the step frees both hands — shamelessness beginning in earnest.",
        "scene": (
            "At the heavy door the knock has become a bang: the "
            "asker's little lamp now sits on the stone step and "
            "both his hands are at the wood, one flat palm "
            "mid-slap and the other fisted, his lean body leaned "
            "into the noise he is making in a street where noise "
            "is a scandal — the door's iron staples rattling "
            "faintly in the small light. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b17", "out": "s17-friend-lend-me-three-loaves.jpeg", "seg": "j1",
        "window": "87.41-95.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR-DOOR", "LANE"],
        "narration": (
            "Friend, lend me three loaves; for a friend of mine in his journey "
            "is come to me, and I have nothing to set before him."
        ),
        "must_show": "SCRIPTURE-EXACT: the first ask — the asker at the barred door, face close to the wood, calling low and holding up three fingers to the night; polite still, hopeful still.",
        "must_not_show": "no halo, glare or rim-light; three fingers ARE the count and are wanted here; the first ask is quiet — courtesy not yet spent.",
        "scene": (
            "A medium close single at the neighbour's door in the "
            "small lamplight: the asker leans his face close to "
            "the plank seam, "
            "calling low and courteous through the wood, three "
            "fingers of one hand held up against the dark as if "
            "the door could see the number — his other palm flat "
            "and gentle on the wood, everything about him still "
            "polite, still certain this will be quick. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b18", "out": "s18-notice-who-he-is-asking.jpeg", "seg": "n7",
        "window": "96.92-103.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "LANE"],
        "narration": (
            "Notice who he is asking for. He is standing out there in the dark, "
            "begging for bread he will not eat."
        ),
        "must_show": "the intercession named — the asker alone in the dark lane looking back toward his own far lit window where his guest waits; begging as a middleman of mercy.",
        "must_not_show": "no halo, glare or rim-light; the glance BACK is the beat — the need he carries is somebody else's.",
        "scene": (
            "In the black lane the asker has turned from the door "
            "a moment, and his eyes travel back down the row of "
            "dark houses to the one small window at the lane's "
            "end where his own lamp burns faint — the window with "
            "a hungry friend behind it — a man standing in the "
            "cold night between an empty shelf and a barred door, "
            "asking for bread that will pass straight through his "
            "hands. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r040-b19", "out": "s19-on-the-other-side-of.jpeg", "seg": "n8",
        "window": "103.53-107.10", "wide": True, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR", "NEIGHBOR-HOUSE"],
        "narration": "On the other side of that door, a village house was one room.",
        "must_show": "SCRIPTURE-EXACT: the inside — the one-room house in near-darkness: the barred door, and the single sleeping platform with the whole family under one blanket.",
        "must_not_show": "no halo, glare or rim-light; the bar across its staples prominent — the architecture of the refusal.",
        "scene": (
            "Inside the neighbour's house the darkness is nearly "
            "total: the camera holds the whole room from the side "
            "wall, so the barred door and the sleeping platform "
            "face each other across the frame — faint starlight "
            "from one high slit window shows the heavy bar seated "
            "across the door's iron staples, and the raised "
            "sleeping platform where the whole family lies as one "
            "shape under one broad dark blanket, a small child's "
            "arm flung out, the father's heavy form at the edge, "
            "every sleeper turned away from the door — one room, "
            "one bed, one bar, one knock away from chaos. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b20", "out": "s20-the-whole-family-slept-on.jpeg", "seg": "n8",
        "window": "107.10-115.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR", "NEIGHBOR-HOUSE"],
        "narration": (
            "The whole family slept on one platform under one blanket, behind a "
            "heavy bar. Getting up meant waking every child in the house."
        ),
        "must_show": "the cost of rising — close on the sleeping platform: two small children tucked between the parents, the father's eyes just opened at the knocking, doing the terrible arithmetic.",
        "must_not_show": "no halo, glare or rim-light; his open eyes in the dark are the whole beat — a decent man calculating what the door will cost.",
        "scene": (
            "Close on the sleeping platform in the near-dark: two "
            "small children burrowed between their sleeping "
            "mother and the father's broad back, all sharing the "
            "one blanket's warmth — and the father's eyes have "
            "just come open at the sound from the door, staring "
            "flat at the ceiling, doing the silent arithmetic of "
            "a man weighing one friend's loaves against three "
            "sleepers' peace. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r040-b21", "out": "s21-people-hear-it-and-think.jpeg", "seg": "n14a",
        "window": "193.13-196.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR", "NEIGHBOR-DOOR"],
        "narration": "People hear it and think God is the man behind the door.",
        "must_show": "the misreading pictured — the neighbour's sleep-crumpled face at the cracked door, lit by the asker's lamp; the false portrait people carry.",
        "must_not_show": "no halo, glare or rim-light; the face is grumpy and human — the point is that this is what people wrongly think prayer is knocking against.",
        "scene": (
            "The heavy door has cracked a hand's width and the "
            "neighbour's face fills the gap in the lamp's small "
            "light: sleep-flattened, creased, hair pushed up "
            "sideways, eyes half shut, jaw set in weary "
            "protest — the exact tired, reluctant face that half "
            "the world mistakenly pastes on heaven when they "
            "think about asking for anything. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b22", "out": "s22-trouble-me-not-the-door.jpeg", "seg": "j2",
        "window": "115.91-124.31", "wide": True, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR", "NEIGHBOR-HOUSE"],
        "narration": (
            "Trouble me not: the door is now shut, and my children are with me "
            "in bed; I cannot rise and give thee."
        ),
        "must_show": "SCRIPTURE-EXACT: the refusal — both sides of the door in one frame: the neighbour turned away inside with the bar still seated, the asker's lamplit shape waiting beyond the plank wall.",
        "must_not_show": "no halo, glare or rim-light; a REAL and reasonable no — the sleeping children visible as the reason; no villainy.",
        "scene": (
            "One frame holds the door's two worlds, the camera at "
            "the room's side wall catching the heavy neighbour in "
            "three-quarter: he stands turned half away from the "
            "barred door with one hand still on the bar he has "
            "decided not to lift, his eyes going back to the "
            "platform where his children sleep tangled in the "
            "one blanket — and through the gap at the plank's "
            "edge, thin as a knife of warm light, the waiting "
            "lamp-lit presence of the man in the lane. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b23", "out": "s23-that-is-a-no-and.jpeg", "seg": "n9",
        "window": "125.81-129.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR", "NEIGHBOR-HOUSE"],
        "narration": "That is a no. And it is not a lazy no.",
        "must_show": "the no's honesty — close on the neighbour back on the platform's edge, head in his hands, torn; a good man who said no for good reasons.",
        "must_not_show": "no halo, glare or rim-light; sympathy for him — the refusal cost him something too.",
        "scene": (
            "Close in the dark room: the heavy neighbour sits "
            "slumped on the platform's edge with his head in "
            "both hands, elbows on his knees, the knocking still "
            "faint through the wood behind him — a decent tired "
            "man who has just told a friend no in the middle of "
            "the night and is discovering that keeping the "
            "children asleep does not keep the conscience "
            "asleep. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r040-b24", "out": "s24-that-is-a-tired-man.jpeg", "seg": "n9 + n10",
        "window": "129.10-136.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR-DOOR", "LANE"],
        "narration": (
            "That is a tired man with sleeping children and a real reason. So "
            "the man outside does the thing nobody expected."
        ),
        "must_show": "the pivot — the asker in the lane stepping BACK UP to the refused door instead of away from it, shoulders squaring, lamp lifted again.",
        "must_not_show": "no halo, glare or rim-light; the turn-back is the beat — refusal received, and answered with return.",
        "scene": (
            "In the black lane the asker has taken two steps away "
            "from the shut door — and stopped: caught now in the "
            "instant of turning back, shoulders squaring around, "
            "the little lamp coming back up in his fist, his "
            "lean face setting into something past politeness — "
            "a man deciding, against every custom of the "
            "street, that no is not where this ends. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b25", "out": "s25-shutters-bang-open-up-the.jpeg", "seg": "n10",
        "window": "138.26-141.89", "wide": True, "jesus": False, "ref": False,
        "locks": ["ASKER", "LANE"],
        "narration": "Shutters bang open up the street. Dogs start barking.",
        "must_show": "the village waking — shutters flung open down the dark lane with tousled heads leaning out, a dog mid-bark at a gate, the asker still at the door in the middle of the gathering scandal.",
        "must_not_show": "no halo, glare or rim-light; comedy and scandal together — the whole street entering the story against its will.",
        "scene": (
            "Up and down the narrow lane the night is coming "
            "apart, the camera looking along the street from "
            "behind the asker's stubborn figure at the barred "
            "door: two sets of shutters banged open with tousled "
            "heads thrust out and every face turned down the lane "
            "toward him, an old woman's voice visibly scolding "
            "from a doorway, a rangy dog barking at a gate with "
            "its hackles up — the whole waking street converging "
            "on the small lamplit man who keeps his place at the "
            "door, still knocking. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r040-b26", "out": "s26-and-he-keeps-knocking-the.jpeg", "seg": "n10 + n11",
        "window": "141.89-147.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR-DOOR"],
        "narration": (
            "And he keeps knocking. The word Luke uses here shows up nowhere "
            "else in the whole New Testament."
        ),
        "must_show": "the knocking that will not stop — close on both the asker's fists on the wood, rhythm visible in the blur, his forehead nearly against the door.",
        "must_not_show": "no halo, glare or rim-light; endurance in the wrists — knocking become a kind of prayer.",
        "scene": (
            "Very close at the door: both the asker's fists "
            "against the planks, one caught mid-blow and softly "
            "blurred with the rhythm, his forehead bowed almost "
            "to the wood between them, lamplight from below "
            "carving his set face — knocking that has stopped "
            "being a request and become a fact of the night, as "
            "regular as a heartbeat. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b27", "out": "s27-most-bibles-turn-it-into.jpeg", "seg": "n11",
        "window": "147.86-153.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "LANE"],
        "narration": (
            "Most Bibles turn it into the word persistence. It does not mean "
            "persistence."
        ),
        "must_show": "more than persistence — the asker glancing up at the neighbours' watching heads and NOT stopping; the watchers' judgment landing on him and sliding off.",
        "must_not_show": "no halo, glare or rim-light; his awareness of the audience is the point — he sees them seeing him, and knocks on.",
        "scene": (
            "From across the lane: the asker at the door glances "
            "up and sideways at the lit rectangle of a neighbour's "
            "opened shutter where two heads watch him with open "
            "disapproval — and his fist does not pause on the "
            "wood, the knock rolling on through their judgment "
            "like rain through an open window, a man fully seen "
            "and entirely unstopped. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b28", "out": "s28-it-means-shamelessness-he-was.jpeg", "seg": "n11",
        "window": "153.37-158.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR-DOOR", "LANE"],
        "narration": "It means shamelessness. He was not too proud to look like a fool.",
        "must_show": "shamelessness embodied — the asker now CALLING UP at the house's high window, arms wide, lamp at his feet, dignity entirely spent and entirely unmissed.",
        "must_not_show": "no halo, glare or rim-light; foolishness embraced — arms open to the whole street's opinion.",
        "scene": (
            "The asker has stepped back from the door and stands "
            "calling up at the house's high dark window with "
            "both arms spread wide, head back, lamp burning on "
            "the step below him — a grown man serenading a "
            "barred house at midnight for three loaves, every "
            "scrap of dignity cheerfully spent, his shadow flung "
            "huge and ridiculous up the plank door behind him. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b56", "out": "s56-he-will-rise.jpeg", "seg": "j3",
        "window": "158.65-165.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR", "NEIGHBOR-HOUSE"],
        "narration": (
            "I say unto you, Though he will not rise and give him, because he "
            "is his friend, yet because of his importunity he will rise"
        ),
        "must_show": "SCRIPTURE-EXACT: the give-in — the neighbour up off the platform mid-rise, his side of the blanket thrown back, one hand already reaching toward the bar; the children undisturbed.",
        "must_not_show": "no halo, glare or rim-light; no anger — a worn-down decent man surrendering; the children stay asleep.",
        "scene": (
            "Inside the dark house the refusal breaks: the heavy "
            "neighbour is up off the platform's edge mid-rise, "
            "his side of the blanket thrown back, one bare foot "
            "planted on the floor and one hand already reaching "
            "toward the barred door, his sleep-creased face "
            "folded into rueful surrender — while behind him the "
            "children sleep on undisturbed in the one blanket's "
            "warmth, the knocking's steady rhythm all but "
            "sounding through the wood. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b29", "out": "s29-i-say-unto-you-though.jpeg", "seg": "j3",
        "window": "165.30-169.79", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR", "NEIGHBOR-DOOR", "NEIGHBOR-HOUSE"],
        "narration": "and give him as many as he needeth.",
        "must_show": "SCRIPTURE-EXACT: the door opens — the bar lifted, the door swung wide, the rumpled neighbour loading loaves into the asker's arms; MORE than three.",
        "must_not_show": "no halo, glare or rim-light; 'as many as he needeth' — the count visibly exceeds the ask; the neighbour gives grudgingly and generously at once.",
        "scene": (
            "A tight two-shot in the doorway at last: the heavy "
            "door stands wide, the bar hanging "
            "from the neighbour's fist — and in the doorway's "
            "lamplight the rumpled big man stacks round loaves "
            "into the asker's outstretched arms, three, four, "
            "five, a sixth balanced on top from the shelf behind "
            "him, muttering and giving in the same motion — while "
            "the asker's face over the growing stack breaks into "
            "disbelieving thanks. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r040-b30", "out": "s30-teach-us-how-to-do.jpeg", "seg": "n1",
        "window": "20.69-22.69", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "Teach us how to do that.",
        "must_show": "the request's heart — close on the asking disciple's open upturned hands between himself and Jesus; the learner's posture, empty and ready.",
        "must_not_show": "no halo, glare or rim-light on Jesus; hands and faces only — the oldest posture of apprenticeship.",
        "scene": (
            "Close in the dawn light between the two figures: the "
            "disciple's weathered hands held open and upturned in "
            "the space between himself and Jesus, empty and "
            "asking — and above them the two faces, the "
            "disciple's lifted and hungry to learn, Jesus's bent "
            "toward him already consenting — the whole trade of "
            "master and learner sealed in the shape of two open "
            "palms. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r040-b31", "out": "s31-he-went-for-enough-bread.jpeg", "seg": "n12",
        "window": "171.34-175.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "LANE"],
        "narration": (
            "He went for enough bread to feed one man. He came home with an "
            "armful."
        ),
        "must_show": "the abundance walking home — the asker down the dark lane with the stacked loaves piled to his chin, lamp hooked awkwardly on one finger, almost laughing.",
        "must_not_show": "no halo, glare or rim-light; the armful visibly MORE than the errand — abundance with a comic edge.",
        "scene": (
            "Down the middle of the dark lane the asker walks "
            "home with the loaves stacked from his belt to his "
            "chin, steadying the top one with his jaw, the little "
            "lamp swinging hooked over one strained finger — "
            "half-laughing at his own armful as the last "
            "scandalized shutter bangs shut behind him and the "
            "dog gives up — a man who asked for three and is "
            "carrying a bakery. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r040-b32", "out": "s32-and-notice-why-the-neighbour.jpeg", "seg": "n12",
        "window": "175.39-179.93", "wide": False, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR", "NEIGHBOR-DOOR", "LANE"],
        "narration": (
            "And notice why. The neighbour did not get up because they were "
            "friends."
        ),
        "must_show": "the reason examined — the neighbour in his doorway watching the asker go, rebarring the door with a rueful head-shake; friendship didn't do this.",
        "must_not_show": "no halo, glare or rim-light; his face says it plainly — beaten, not softened; the head-shake half a laugh.",
        "scene": (
            "In his lamplit doorway the big rumpled neighbour "
            "leans watching the loaf-laden figure recede down "
            "the lane, one hand already lifting the bar back "
            "toward its staples — and shaking his head slowly as "
            "he does it, the defeated half-laugh of a man who "
            "knows exactly what got him out of bed, and knows "
            "it was not affection. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b33", "out": "s33-he-got-up-because-the.jpeg", "seg": "n12 + n13",
        "window": "179.93-189.76", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "TRAVELER", "ASKER-HOUSE"],
        "narration": (
            "He got up because the man outside would not stop asking. And in a "
            "dark house at midnight, a tired stranger ate a meal he never knew "
            "somebody had to go knocking for."
        ),
        "must_show": "SCRIPTURE-EXACT: the meal — the traveller eating by the small lamp, colour returning to his face, while the asker watches him eat with quiet satisfaction; the bread's secret cost invisible to its eater.",
        "must_not_show": "no halo, glare or rim-light; the traveller must NOT know — no gratitude drama; he just eats, and that is the victory.",
        "scene": (
            "In the small room the traveller sits cross-legged on "
            "the mat tearing into a round loaf with both hands, "
            "a second loaf waiting in his lap, colour coming "
            "back into his hollow face by the lamp's warm light — "
            "while across the coals the asker sits with his "
            "chin on his fist watching his friend eat, saying "
            "nothing about the street, the shutters, the dogs, "
            "or the door — the whole midnight war folded away "
            "inside an ordinary supper. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b34", "out": "s34-here-is-where-almost-everybody.jpeg", "seg": "n14a",
        "window": "190.33-193.13", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "Here is where almost everybody gets this story wrong.",
        "must_show": "the correction coming — close on Jesus in the grove with one hand raised in gentle warning, the disciples caught mid-nod and stopping.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the raised hand catches the listeners' agreement before it settles wrong.",
        "scene": (
            "Close in the morning grove: Jesus's hand has come up "
            "gently, palm out, catching the story just before it "
            "lands askew — and around the frame's edge two "
            "disciples are caught mid-nod, their agreement "
            "arrested halfway, faces turning puzzled — the "
            "teacher stopping the class at the exact line where "
            "everyone always takes the wrong turn. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b35", "out": "s35-annoyed-asleep.jpeg", "seg": "n14a",
        "window": "196.26-198.15", "wide": False, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR", "NEIGHBOR-DOOR"],
        "narration": "Annoyed. Asleep.",
        "must_show": "the false picture, itemized — the neighbour's sleep-crushed annoyed face at the door crack once more, the two wrong adjectives in one image.",
        "must_not_show": "no halo, glare or rim-light; a reprise of the misreading — grumpy and groggy, the portrait to be torn up.",
        "scene": (
            "The door-crack portrait once more in the small "
            "lamplight: the neighbour's face wedged in the gap, "
            "eyes at half mast and crusted with sleep, mouth "
            "dragged down in pure annoyance, the pillow's crease "
            "still printed down one cheek — annoyed and asleep, "
            "the two words made one face, held up one last time "
            "before being thrown away. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b36", "out": "s36-somebody-you-have-to-wear.jpeg", "seg": "n14a + n14b",
        "window": "198.15-203.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["NEIGHBOR-DOOR"],
        "narration": (
            "Somebody you have to wear down. That is the opposite of what he "
            "said."
        ),
        "must_show": "the picture torn up — the barred door alone in close-up, and across the image the sense of dismissal: this door is NOT the face of God; the bar is the wrong symbol.",
        "must_not_show": "no halo, glare or rim-light; the barred door held one beat longer as the thing being denied.",
        "scene": (
            "A close still shot of the heavy plank door in the "
            "dark: the thick wooden bar seated hard across its "
            "iron staples, the grain scarred by the night's "
            "knocking, the lamp's small light making the bar's "
            "shadow into a black stripe across the wood — the "
            "wrong picture of heaven, photographed once, "
            "plainly, so it can be put down forever. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b37", "out": "s37-the-neighbour-is-not-a.jpeg", "seg": "n14b",
        "window": "203.06-207.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": "The neighbour is not a picture of God — he is the contrast.",
        "must_show": "the correction landed — over the eldest disciple's shoulder: Jesus sweeping one hand aside (clearing the wrong picture); the old man's profile catching the reversal as it lands.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the sweeping-aside gesture reads plainly; understanding kindling on the near face.",
        "scene": (
            "Over the eldest disciple's shoulder in the bright "
            "grove: Jesus sweeps one hand flat and sideways "
            "through the air — the gesture of clearing a table — "
            "and at the frame's near edge the old man's profile "
            "catches the reversal as it lands, brows flying up, "
            "a slow grin starting — the whole story turning over "
            "in front of him like a coin. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b38", "out": "s38-if-even-a-man-behind.jpeg", "seg": "n14b",
        "window": "207.41-216.77", "wide": True, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR", "NEIGHBOR-DOOR", "LANE"],
        "narration": (
            "If even a worn-out man behind a barred door will get up for you in "
            "the end, what will your Father do, when he was never asleep at "
            "all?"
        ),
        "must_show": "the how-much-more — the open door and given loaves once more, but framed small; and above the lane, the wide waiting night sky suggesting the greater Giver the story points past.",
        "must_not_show": "no halo, glare or rim-light; no figure in the sky, no face in the stars — the 'how much more' is carried by scale alone.",
        "scene": (
            "From high above the lane's rooftops the camera "
            "looks down the street's length: small below, the "
            "lamplit doorway where the loaves pass from the "
            "rumpled neighbour's hands into the asker's arms, "
            "both tiny figures in profile over the little warm "
            "transaction — and around and over it, the enormous "
            "clear night sky standing wide awake over the "
            "sleeping village, thick with stars from roofline to "
            "roofline, the story's small kindness set inside "
            "something immeasurably larger and already "
            "listening. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r040-b39", "out": "s39-ask-and-it-shall-be.jpeg", "seg": "j4",
        "window": "217.30-224.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Ask, and it shall be given you; seek, and ye shall find; knock, "
            "and it shall be opened unto you."
        ),
        "must_show": "SCRIPTURE-EXACT: the triple promise — close on Jesus giving the three verbs on three raised fingers; the asking disciple's lips moving at the frame's edge, memorizing.",
        "must_not_show": "no halo, glare or rim-light on Jesus; three fingers for three verbs — wanted here; the brightest frame of the grove sequence.",
        "scene": (
            "Close on Jesus in the grove's fullest morning "
            "light: he counts the promise onto three raised "
            "fingers, one verb at a time, his face open and "
            "certain, the hand held where every listener can "
            "see it — and just past his shoulder at the frame's "
            "edge the first questioner's lips move, memorizing, "
            "a man being handed keys. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b40", "out": "s40-and-the-first-word-of.jpeg", "seg": "n2",
        "window": "24.81-28.62", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "And the first word of it was not Lord, and it was not God.",
        "must_show": "the withheld titles — a quiet still image: a mezuzah-marked doorpost and threshold of a family home at dawn; the word that opens the prayer belongs to houses like this.",
        "must_not_show": "no halo, glare or rim-light; domestic, not templar — the prayer's first word lives at home.",
        "scene": (
            "A quiet close shot at first light: the worn "
            "doorpost of a family home with its small carved "
            "scripture case fixed at a hand's height, the "
            "threshold stone beneath it hollowed by generations "
            "of the same family's feet, a child's small sandal "
            "left beside the step — the kind of door behind "
            "which the prayer's astonishing first word is an "
            "everyday sound. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r040-b41", "out": "s41-in-the-greek-none-of.jpeg", "seg": "n15",
        "window": "226.38-231.62", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER", "NEIGHBOR-DOOR"],
        "narration": (
            "In the Greek, none of those is a one-time act. Every one of them "
            "means keep coming back."
        ),
        "must_show": "keep-coming-back made visible — the asker's fist on the door in a soft multiple-exposure feel: the same knock at the same door, worn smooth at the knocking spot.",
        "must_not_show": "no halo, glare or rim-light; the door's knocking-spot visibly polished by repetition — time compressed into wood.",
        "scene": (
            "Close on the door's plank face in lamplight: at "
            "hand height one patch of the old wood is worn "
            "smooth and pale, polished by uncounted knocks — and "
            "against it the asker's fist rests mid-knock once "
            "more, landing exactly inside the worn place, one "
            "more coming-back added to a spot the size of a "
            "hand that repetition has turned almost soft. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b42", "out": "s42-if-a-son-shall-ask.jpeg", "seg": "jv11",
        "window": "232.06-237.45", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER-SON", "COURTYARD"],
        "narration": (
            "If a son shall ask bread of any of you that is a father, will he "
            "give him a stone?"
        ),
        "must_show": "SCRIPTURE-EXACT: bread or stone — the small son asking up at his father, and in the father's two hands the choice visible: a round loaf in one, a flat river stone in the other — the stone already tipping away.",
        "must_not_show": "no halo, glare or rim-light; the lookalike matters — the stone is genuinely loaf-like; and the father's face makes the question absurd.",
        "scene": (
            "A medium two-shot in the warm courtyard light: the "
            "small boy stands "
            "with both hands cupped up at his father's waist, "
            "asking — and the broad father holds the two "
            "lookalikes at his sides: a round crusted loaf in "
            "his right hand, and in his left a flat pale river "
            "stone of exactly the same size, already tipping to "
            "drop behind him, his patient face bent to the boy "
            "with the very idea of the stone dying on it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b43", "out": "s43-or-if-he-ask-a.jpeg", "seg": "jv11",
        "window": "237.45-242.43", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER-SON", "COURTYARD"],
        "narration": "or if he ask a fish, will he for a fish give him a serpent?",
        "must_show": "SCRIPTURE-EXACT: fish or serpent — close at the father's hands: a fresh fish passing down into the boy's grip while a grey eel-like snake shape lies rejected on the cleaning board, well apart.",
        "must_not_show": "no halo, glare or rim-light; the serpent NEVER near the child — inert on the board, plainly not chosen; no menace.",
        "scene": (
            "Close over the stone cleaning-table in daylight: "
            "the father's big hand passes a fresh silver fish "
            "down into his son's eager two-handed grip — while "
            "at the table's far corner, well apart and pointedly "
            "unchosen, lies the grey eel-like river snake the "
            "morning's net dragged up with the catch, inert on "
            "the wet stone — the counterfeit sorted out before "
            "the boy ever reached the table. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b44", "out": "s44-or-if-he-shall-ask.jpeg", "seg": "jv11",
        "window": "242.43-246.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER-SON", "COURTYARD"],
        "narration": "Or if he shall ask an egg, will he offer him a scorpion?",
        "must_show": "SCRIPTURE-EXACT: egg or scorpion — the boy's cupped hands receiving a brown egg, while nearby on the wall-top a pale scorpion curled egg-round sits ignored; the lookalike pair complete.",
        "must_not_show": "no halo, glare or rim-light; the scorpion distant, curled and still — a comparison, never a threat to the child.",
        "scene": (
            "In the warm light by the courtyard wall the boy's "
            "small cupped hands close carefully around the brown "
            "egg his father lowers into them like a coin of "
            "great value — and along the wall-top an arm's "
            "length away, pale against the stone and curled "
            "nearly round, a sand-coloured scorpion sits ignored "
            "in the sun, its egg-like disguise fooling nobody "
            "who loves anybody. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r040-b45", "out": "s45-then-he-asked-them-if.jpeg", "seg": "n16a",
        "window": "248.39-257.17", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "Then he asked them: if your son asked for bread, would you put a "
            "rock in his hand? If he asked for a fish, would you hand him a "
            "snake?"
        ),
        "must_show": "the absurdity offered — past two laughing listeners: Jesus spreading both hands in open comic disbelief; fathers being won by the ridiculous.",
        "must_not_show": "no halo, glare or rim-light on Jesus; laughter is correct here — the argument works BY being ridiculous.",
        "scene": (
            "Past the shoulders of two laughing disciples in the "
            "bright grove: Jesus spreads both hands in open "
            "comic disbelief as he puts the question — and at "
            "the frame's near edges the grey-bearded father of "
            "five waves the very idea away while the big "
            "fisherman snorts — grown men being won by the "
            "sheer absurdity of the alternative. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b46", "out": "s46-and-then-to-show-them.jpeg", "seg": "n3",
        "window": "41.38-48.69", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "And then, to show them what kind of Father he meant, he told a "
            "story about a man banging on a door in the middle of the night."
        ),
        "must_show": "the parable launched — a medium shot of Jesus miming a knock on the air with one fist; one listener settling in at the frame's edge with the pleasure of a story beginning.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the mimed knock is the hinge from prayer-lesson to story.",
        "scene": (
            "A medium shot in the morning grove: Jesus raps his "
            "fist twice on the empty air before him — the "
            "universal mime of a knock — one eyebrow up, the "
            "story's door already standing in everyone's "
            "imagination — while soft at the frame's lower edge "
            "one listener settles himself on the grass, drawing "
            "his knees up with the unhurried pleasure of a man "
            "at the start of a good tale. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b47", "out": "s47-every-pair-is-a-lookalike.jpeg", "seg": "n16b",
        "window": "257.61-267.27", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Every pair is a lookalike — a river stone the size of a flat loaf, "
            "a scorpion curled pale and round like an egg. A father handing his "
            "hungry child a fake."
        ),
        "must_show": "the lookalikes laid out — a still-life: loaf beside flat stone, egg beside curled pale scorpion, fish beside grey snake, in two quiet rows on a board; the counterfeits named by proximity.",
        "must_not_show": "no halo, glare or rim-light; a specimen-table calm — nothing alive threatens anything; the resemblance is the whole subject.",
        "scene": (
            "A still-life on a plain wooden board in even "
            "daylight: laid out in two quiet rows, each real "
            "thing beside its counterfeit — the round crusted "
            "loaf beside the flat pale river stone, the brown "
            "egg beside the pale scorpion curled to the same "
            "size, the silver fish beside the grey slack river "
            "snake — six objects, three gifts, three lies, "
            "close enough in shape to fool a hungry child and "
            "no one else. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r040-b48", "out": "s48-not-one-of-you-he.jpeg", "seg": "n16b",
        "window": "267.27-270.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER-SON", "COURTYARD"],
        "narration": "Not one of you, he said, would ever do it.",
        "must_show": "the verdict of instinct — the father's hand closed protectively over his son's small hands around the bread; the counterfeit unthinkable.",
        "must_not_show": "no halo, glare or rim-light; protection as reflex — the enclosing hand says it without a face needed.",
        "scene": (
            "A close shot in the warm light: the boy's two small "
            "hands wrapped around his round loaf, and folded "
            "entirely over them, the father's one broad hand, "
            "enclosing bread and hands together the way a roof "
            "encloses a room — the old reflex of every ordinary "
            "father, resting quietly on top of everything a "
            "child holds. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r040-b49", "out": "s49-if-ye-then-being-evil.jpeg", "seg": "j5",
        "window": "271.08-280.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "If ye then, being evil, know how to give good gifts unto your "
            "children: how much more shall your heavenly Father give the Holy "
            "Spirit to them that ask him?"
        ),
        "must_show": "SCRIPTURE-EXACT: the summit of the argument — close on Jesus, both hands lifted open and rising through the sentence, the 'how much more' carried in the opening arms.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the rising open hands are the whole crescendo — no sky effects.",
        "scene": (
            "Close on Jesus at the teaching's summit: his two "
            "hands rise open through the sentence, lifting from "
            "the level of a father's gift to the width of the "
            "morning sky between the olive branches, his face "
            "going up with them — the laughter of the last "
            "question stilled out of his voice into something "
            "wide and certain, the arithmetic of 'how much "
            "more' outrunning anything a man can count. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b50", "out": "s50-not-a-crumb.jpeg", "seg": "n5",
        "window": "70.46-71.97", "wide": False, "jesus": False, "ref": False,
        "locks": ["ASKER-HOUSE"],
        "narration": "Not a crumb.",
        "must_show": "the emptiness absolute — an extreme close of the bare shelf boards: old crumb-dust and the empty basket's shadow; nothing else.",
        "must_not_show": "no halo, glare or rim-light; the barest frame in the row — boards, dust, shadow.",
        "scene": (
            "An extreme close shot inside the lamp's small "
            "circle: the bread shelf's scrubbed boards filling "
            "the frame, a fine grey dust of long-gone crumbs in "
            "the wood's grain, the tipped basket's woven shadow "
            "lying across the emptiness — a shelf photographed "
            "the way a dry well is photographed, for what is "
            "not in it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r040-b51", "out": "s51-you-already-know-how-to.jpeg", "seg": "n17",
        "window": "282.32-291.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["FATHER-SON"],
        "narration": (
            "You already know how to be good to your kids — and you are not "
            "half as good as he is. That is the whole argument: God does not "
            "have to be worn down, because he is a better Father than you on "
            "your best day."
        ),
        "must_show": "the best day pictured — the father at evening carrying his sleeping son home on his shoulder, the boy's loaf still crumbed in his slack hand; ordinary paternal goodness at full height.",
        "must_not_show": "no halo, glare or rim-light; the tenderness is the argument — and the narration says even this is the LESSER goodness.",
        "scene": (
            "Seen from the side in medium-full: in the deep warm "
            "gold of evening the broad father "
            "walks the lane home with his son asleep over one "
            "shoulder, the small head heavy against his neck, "
            "one big hand spread across the boy's back — and in "
            "the child's slack fist, half a loaf still crumbed "
            "from supper rides home with him — the everyday "
            "summit of human fathering, which the story says is "
            "the SMALLER of the two loves. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b52", "out": "s52-he-was-never-asleep.jpeg", "seg": "n17",
        "window": "291.16-292.86", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE", "LIT-HOUSE"],
        "narration": "He was never asleep.",
        "must_show": "the contrast's collapse — in the sleeping midnight lane, ONE window burning steady and bright while every other house lies dark; the light that was on the whole time.",
        "must_not_show": "no halo, glare or rim-light; one lit window in a dark street — lamplight through a window, nothing supernatural.",
        "scene": (
            "The narrow lane at dead midnight, every shutter "
            "dark, the houses folded into the blue-black — "
            "except one: a single window burning steady and "
            "warm at the lane's turning, its lamplight laid in a "
            "long quiet rectangle across the packed earth — one "
            "house in the whole sleeping street where somebody "
            "is up, has been up, was always up. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b53", "out": "s53-the-man-in-the-story.jpeg", "seg": "n18",
        "window": "293.31-298.30", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE", "LIT-HOUSE"],
        "narration": (
            "The man in the story was knocking on a door with somebody asleep "
            "behind it. You are not."
        ),
        "must_show": "the corrected picture — the lit-window house's door standing AJAR onto the dark lane, warm light spilling through the gap; a door already opening before the knock.",
        "must_not_show": "no halo, glare or rim-light; no bar, no staples on THIS door — ajar, warm, waiting.",
        "scene": (
            "At the lit house the door stands ajar onto the "
            "midnight lane — no bar, no staples, a hand's width "
            "of warm lamplight spilling through the gap and down "
            "the step onto the dark earth — the door of the one "
            "house that was awake, open a little in advance, "
            "the way a door stands when someone inside is "
            "listening for footsteps. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r040-b54", "out": "s54-whatever-you-quit-asking-for.jpeg", "seg": "n18",
        "window": "298.30-306.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["LANE", "LIT-HOUSE"],
        "narration": (
            "Whatever you quit asking for — too small, too late, too much — the "
            "light in that house is already on."
        ),
        "must_show": "the invitation personal — close at the lit window from outside: the lamp within, a chair pulled near the sill, bread and a second cup already set out on the table inside.",
        "must_not_show": "no halo, glare or rim-light; the second cup is the detail — provision made in advance for an expected guest.",
        "scene": (
            "Close at the warm window from the dark lane: "
            "through the leaded gap of the shutters the room "
            "shows golden — a lamp trimmed and burning, a chair "
            "drawn up ready near the sill, and on the table a "
            "round loaf already broken and TWO cups set out, "
            "one filled and one waiting — a room provisioned for "
            "a guest who has not knocked yet and is expected "
            "anyway. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r040-b55", "out": "s55-and-the-best-thing-he.jpeg", "seg": "n18",
        "window": "306.95-312.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["GROVE"],
        "narration": (
            "And the best thing he has to give was never bread. It is himself."
        ),
        "must_show": "the closing image — a warm medium shot: Jesus with his arms open and the two nearest friends already moving in; the giver himself the gift; warmth without spectacle.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the gift is presence — open arms among friends in ordinary morning light.",
        "scene": (
            "A warm medium shot in the grove's full morning: "
            "Jesus rises with both arms opening, and the two "
            "nearest friends are already inside them — the first "
            "questioner reaching to grip his forearm, the "
            "youngest ducking in under one arm — the prayer "
            "taught, the story told, and the answer to both of "
            "them standing with his friends in his arms in the "
            "plain light of day. Every figure has two arms, two "
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
    "ASKER-HOUSE": "PLACE-REF/asker-house.jpeg",  # build-40-the-friend-at-midnight s11-feeding-a-guest-was-a (manual)
    "COURTYARD": "PLACE-REF/courtyard.jpeg",  # build-40-the-friend-at-midnight s06-it-was-the-word-a (manual)
    "GROVE": "PLACE-REF/grove.jpeg",  # build-40-the-friend-at-midnight s01-and-it-came-to-pass (manual)
    "LANE": "PLACE-REF/lane.jpeg",  # build-31-ten-virgins v2-r031-b02
    "LIT-HOUSE": "PLACE-REF/lit-house.jpeg",  # build-40-the-friend-at-midnight s53-the-man-in-the-story (manual)
    "NEIGHBOR-DOOR": "PLACE-REF/neighbor-door.jpeg",  # build-40-the-friend-at-midnight s02-he-knocks-again (manual)
    "NEIGHBOR-HOUSE": "PLACE-REF/neighbor-house.jpeg",  # build-40-the-friend-at-midnight s19-on-the-other-side-of (manual)
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "ASKER": "CAST-REF-V2/asker.jpeg",
    "NEIGHBOR": "CAST-REF-V2/neighbor.jpeg",
    "TRAVELER": "CAST-REF-V2/traveler.jpeg",
    "FATHER-SON": "CAST-REF-V2/father-son.jpeg",
}
