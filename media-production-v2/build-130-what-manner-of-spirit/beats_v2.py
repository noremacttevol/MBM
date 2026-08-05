#!/usr/bin/env python3
"""V2 beat map — row 130, build-130-what-manner-of-spirit (Luke 9:51-56).

COVERAGE: 10 pictures over 58.8 s = 5.9 s/picture (matches the library density).

SCRIPTURE FACTS (Luke 9 KJV):
  9:51-53 "he stedfastly set his face to go to JERUSALEM... and they
        did not receive him, because his face was as though he would
        go to Jerusalem." — a SAMARITAN village refuses lodging.
  9:54  "when his disciples JAMES AND JOHN saw this, they said, Lord,
        wilt thou that we COMMAND FIRE to come down from heaven, and
        consume them, even as Elias did?"
  9:55  "he turned, and REBUKED THEM, and said, YE KNOW NOT WHAT
        MANNER OF SPIRIT YE ARE OF."
  9:56  "For the Son of man is NOT COME TO DESTROY men's lives, but
        TO SAVE THEM. And they went to ANOTHER VILLAGE."

RENDERING LAWS:
  - NO FIRE IS EVER DEPICTED FALLING OR THREATENING — the fire
    exists only in the brothers' INTENT (raised arms, burning
    faces). The only flame ever in frame is the village's own
    peaceful hearth-smoke (b07). Any render with fire from heaven,
    smoke of judgment, or a scorched village is an automatic reject.
  - JAMES-Z and JOHN are the shared cast tokens — same two faces as
    every other build; their anger is HOT ZEAL (young thunder-sons),
    never villainy; their calming by b10 must read.
  - The Samaritan village is NEVER punished and never villainous —
    ordinary wary villagers at their gate; the refusal is a turned
    hand and a closed gate, not hostility theatre.
  - The rebuke (b05) aims at HIS OWN — Jesus's back is to the
    village, his correcting hand toward the disciples; direction
    law makes the sermon: the village is behind him, already
    forgiven.
  - The row ends on the ROAD — walking on, no answer to the insult;
    the non-event IS the doctrine.

TIME OF DAY ARC (intentional): late afternoon into golden evening
along one road — the refusal in slanting afternoon light, the
walking-on into warm evening gold; the village's hearth-smoke at
dusk (b07) is deliberate.

CHANGING CONDITION (kept OUT of the locks): the brothers — burning,
then rebuked, then quieted and walking; the village — behind them,
untouched, at peace.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Only Jesus wears cream; the shared JESUS lock and
# REF come from v2_prompt.py via the jesus/ref flags. JAMES-Z and JOHN come
# from the shared CAST_LOCKS — do not redefine them here.
LOCKS = {
    "VILLAGE": (
        "VILLAGE LOCK: the Samaritan village — pale stone houses "
        "clustered on a low slope with a wooden gate at the road, "
        "terraced gardens, hearth-smoke rising thin from the roofs. "
        "The same village and gate throughout, always intact and at "
        "peace."
    ),
    "ROAD": (
        "ROAD LOCK: the Jerusalem road — a pale dusty highland road "
        "running past the village slope and on through open hills "
        "toward the south, dry-stone walls in stretches. The same "
        "road throughout."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r130-b01", "out": "s01-as-jesus-traveled-toward-jerusalem.jpeg", "seg": "n0",
        "window": "0.28-4.74", "wide": True, "jesus": True, "ref": REF,
        "locks": ["VILLAGE", "ROAD"],
        "narration": (
            "As Jesus traveled toward Jerusalem, a Samaritan village refused "
            "to welcome Him."
        ),
        "must_show": "the refusal — at the village gate, wary elders with a turned-away hand; Jesus and his small band on the road below, travel-worn; the closed welcome in one frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the villagers WARY, not hostile — a closed gate, not a confrontation.",
        "scene": (
            "The day's lodging falls through at the gate, the "
            "camera looking past the travellers' dusty backs up "
            "the slope: at the village's wooden gate two wary "
            "elders stand with a hand turned politely, "
            "immovably away — no room here for pilgrims whose "
            "faces are set toward Jerusalem — while on the road "
            "below Jesus and his small travel-worn band take "
            "the refusal in the slanting afternoon light, a "
            "long evening's walk suddenly added to a long day. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r130-b02", "out": "s02-the-disciples-james-and-john.jpeg", "seg": "n0 + s54",
        "window": "4.74-14.63", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": (
            "The disciples James and John were hot with anger. Lord, wilt "
            "thou that we command fire to come down from heaven, and consume "
            "them, even as Elias did?"
        ),
        "must_show": "SCRIPTURE-EXACT: the thunder-sons — James and John hot-faced, one arm flung up at the sky, the other pointing back at the village; the terrible offer being made. NO fire anywhere.",
        "must_not_show": "ABSOLUTE: no fire, no smoke, no darkened sky — the fire lives ONLY in their faces and gesture.",
        "scene": (
            "The sons of thunder file their motion: James with "
            "his arm flung straight up at the clean afternoon "
            "sky, John's finger aimed hard back at the village "
            "on its slope — faces hot, jaws set, two young men "
            "volunteering to be the storm — the offer hanging "
            "in the air between the pointing arm and the "
            "peaceful rooftops with all the terrible confidence "
            "of zeal that has not yet asked what spirit it is "
            "of — and the sky above them staying exactly as "
            "blue as before. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r130-b03", "out": "s03-the-fire-in-the-disciples.jpeg", "seg": "n3",
        "window": "39.49-42.63", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "The fire in the disciples' hearts was the wrong kind.",
        "must_show": "the wrong fire — close on the two brothers' burning faces: zeal, hurt pride and anger tangled; the heat all internal. NO literal fire.",
        "must_not_show": "ABSOLUTE: no flame imagery — the burn is in the eyes and jaws only.",
        "scene": (
            "The only fire on the road is behind two pairs of "
            "eyes: close on the brothers' faces side by side — "
            "James's jaw knotted, John's brows down, the hurt "
            "of the insult and the thrill of the remedy burning "
            "together in the young features — real heat, real "
            "zeal, aimed with real love for their Lord at "
            "exactly the wrong target in exactly the wrong "
            "spirit — the kind of fire that feels like "
            "faithfulness right up until somebody asks where "
            "it came from. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r130-b04", "out": "s04-they-asked-if-they-should.jpeg", "seg": "n1",
        "window": "16.13-21.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE", "ROAD"],
        "narration": (
            "They asked if they should call down fire from heaven to burn "
            "the place. They wanted judgment."
        ),
        "must_show": "the wanted judgment — the brothers' raised arms against the wide sky, and beyond them the village standing peaceful and whole on its slope; the gap between intent and target.",
        "must_not_show": "ABSOLUTE: no fire, no scorch, no storm — the village serene; the judgment exists only in the gesture.",
        "scene": (
            "What they asked for is measured against what "
            "stands there: the brothers' arms raised high "
            "against the wide clean sky — calling on it, "
            "offering to be its instruments — and beyond the "
            "raised arms the village itself, whole and small "
            "and peaceful on its terraced slope, washing on "
            "the lines, a donkey at a wall, hearth-smoke "
            "thin over the roofs — the entire gentle target "
            "of all that requested judgment, going about its "
            "evening unaware. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r130-b05", "out": "s05-jesus-turned-and-rebuked-them.jpeg", "seg": "n2 + j1",
        "window": "22.12-29.76", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "Jesus turned and rebuked them — not the village, but His own "
            "disciples' hearts. Ye know not what manner of spirit ye are of."
        ),
        "must_show": "SCRIPTURE-EXACT: the rebuke — Jesus TURNED, his back to the village, his raised correcting hand and grave face toward his own two disciples; the direction of the rebuke unmistakable.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION LAW — village BEHIND him, correction aimed at his OWN; grief in the gravity, no fury.",
        "scene": (
            "The rebuke goes the direction nobody expected: "
            "Jesus turns his back fully on the village that "
            "refused him and faces his own two men — one hand "
            "raised in level correction, the grave eyes on "
            "James and John and nowhere else — ye know not "
            "what SPIRIT ye are of — the offended party "
            "shielding the offenders' target with his own "
            "turned back, and spending the only rebuke of the "
            "whole affair on the two hearts he actually has "
            "charge of. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r130-b06", "out": "s06-for-the-son-of-man.jpeg", "seg": "j1",
        "window": "29.76-35.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "For the Son of man is not come to destroy men's lives, but to "
            "save them."
        ),
        "must_show": "SCRIPTURE-EXACT: the mission stated — Jesus's open hand sweeping from the spared village to his own chest; destroy set aside, save affirmed; the brothers listening, arms lowering.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the brothers' arms visibly COMING DOWN — the offer withdrawn.",
        "scene": (
            "The mission statement is delivered on the spot: "
            "Jesus's open hand moves in one slow arc from the "
            "village on its slope — spared, included, loved — "
            "back to his own chest, where the actual purpose "
            "lives: not to destroy men's lives but to SAVE "
            "them — and before the sentence is even finished "
            "the brothers' raised arms are coming down, the "
            "terrible offer withdrawing finger by finger, two "
            "storms being talked quietly back into disciples. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r130-b07", "out": "s07-he-come-to-burn-he.jpeg", "seg": "n3",
        "window": "36.87-39.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE"],
        "narration": "He didn't come to burn. He came to rescue.",
        "must_show": "the only fire he permits — the village at dusk with its peaceful HEARTH-smoke rising thin from the roofs, lamplight in windows; the place utterly safe.",
        "must_not_show": "ABSOLUTE: no judgment imagery — the hearth-smoke and lamplight the only fire in the whole row.",
        "scene": (
            "The only fire that ever touches the village is its "
            "own: dusk settles over the terraced slope and the "
            "hearth-smoke rises thin and homely from the "
            "rooftops, lamplight warming window after window, "
            "suppers cooking for people who will never know "
            "what was asked for them this afternoon — the "
            "whole place folded safe into its evening — burn "
            "was never on the itinerary; the smoke over this "
            "village will only ever smell of bread. No people "
            "are needed in this frame."
        ),
    },
    {
        "id": "v2-r130-b08", "out": "s08-and-then-they-simply-walked.jpeg", "seg": "n3b",
        "window": "43.24-47.04", "wide": False, "jesus": True, "ref": REF,
        "locks": ["VILLAGE", "ROAD"],
        "narration": "And then they simply walked on to the next village. No fire.",
        "must_show": "the walking-on — the whole band on the road again, moving AWAY past the village slope toward the next hills; the village whole behind them; the non-event itself.",
        "must_not_show": "no halo, glare or rim-light on Jesus; DIRECTION — away down the road, backs to the village; nobody looking back in anger.",
        "scene": (
            "The whole answer to the insult is a road being "
            "used: the small band walks on down the pale "
            "highland way, Jesus at the front with his face "
            "set south, the brothers folded quiet into the "
            "line behind him — and back on its slope the "
            "village stands entirely whole in the evening "
            "light, refusing them still, unpunished forever — "
            "no fire, no word, no gesture spent on it: just "
            "sandals on dust, and somewhere else to be. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r130-b09", "out": "s09-no-answer-to-the-insult.jpeg", "seg": "n3b",
        "window": "47.04-52.76", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "No answer to the insult at all — just the road, and somewhere "
            "else to be."
        ),
        "must_show": "the long view — the band small on the long evening road through the open hills, the village a distant untouched cluster behind; the insult answered with miles.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the village TINY and intact in the far distance.",
        "scene": (
            "The insult's full reply is measured in distance: "
            "the travellers small on the long gold road as it "
            "curves through the open evening hills, dust "
            "rising soft behind their sandals — and far back "
            "along the way, already shrinking, the village "
            "cluster sits untouched on its slope, keeping the "
            "grudge nobody came to collect — the mightiest "
            "answer never given, walking quietly out of range "
            "of its own vindication with somewhere better to "
            "be. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r130-b10", "out": "s10-anger-that-wants-to-destroy.jpeg", "seg": "n4",
        "window": "53.37-58.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["ROAD"],
        "narration": (
            "Anger that wants to destroy isn't from Him. The spirit He "
            "brings saves."
        ),
        "must_show": "the close — golden evening on the road: Jesus walking ahead, and behind him James and John quieted, faces calmed, following; the right spirit restored to the sons of thunder.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the brothers' calm VISIBLE — the burn gone from the same two faces as b03.",
        "scene": (
            "The lesson walks itself into the sunset: Jesus "
            "ahead on the golden road with his face set toward "
            "Jerusalem, and behind him the two brothers "
            "follow changed — the same young faces that burned "
            "at noon now quiet, the zeal still in them but "
            "banked and redirected, thunder-sons learning what "
            "their thunder is actually for — the spirit that "
            "destroys left behind on the road with the "
            "grudge, and the spirit that saves walking on in "
            "front of them, showing the way. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    # ROAD: build-38 b39 auto-match REJECTED (road-through-a-doorway frame)
    # — third rejection of this same frame. Promote-first from b08.
    # VILLAGE: build-38 b46 auto-match REJECTED (single doorway corner, not
    # a village on a slope with a gate). Promote-first from b01.
}
# === end PLACE-PLATES ===
