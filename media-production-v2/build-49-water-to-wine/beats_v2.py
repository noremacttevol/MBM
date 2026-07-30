#!/usr/bin/env python3
"""V2 beat map — row 49, build-49-water-to-wine (John 2:1-11).

COVERAGE: 40 pictures over 230.4 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (John 2:1-11 KJV):
  v1-2  "a marriage in CANA of Galilee; and the MOTHER of Jesus was there:
        and both Jesus was called, and his disciples" — a multi-day
        village wedding, the whole town present; Jesus IN the joy, a
        guest among guests, never apart from it.
  v3    "they have NO WINE" — a quiet social catastrophe: to that family
        a public shame carried for years. Mary NOTICES FIRST and goes
        straight to her son with four words — no request, no plan.
  v4    "Woman, what have I to do with thee? mine hour is not yet come" —
        the narration insists this was GENTLE: 'Woman' a word of respect,
        the phrase a soft idiom of weighing, not a rebuff. Painted as
        tender mother-son privacy, never sharpness.
  v5    "Whatsoever he saith unto you, DO IT" — Mary's masterpiece: she
        hands the servants to him and STEPS BACK; her trust is the hinge
        beat of the row.
  v6-8  SIX stone waterpots for purification, 20-30 gallons each; "FILL
        the waterpots with WATER" — filled TO THE BRIM by hauling
        servants; "DRAW OUT NOW" — no gesture over the jars, no words,
        no spectacle: the change happens unseen 'somewhere between the
        jar and the cup' — NEVER any glow, light or effect on the water
        or wine; the miracle is retroactive and invisible.
  v9-10 the steward's toast: "thou hast kept the GOOD wine until now" —
        comedy and wonder; the bridegroom credited for what he never did.
  v11   "this beginning of miracles ... and his disciples BELIEVED on
        him" — the closing beat: the friends' faces, believing.

TIME OF DAY: the wedding runs from golden afternoon through lamplit
night — the crisis and miracle in the deep warm evening, the steward's
toast at the feast's lamplit height, the closing belief-beat in the
same night warmth. All one celebration's clock.

CONTENT-CARE: row 49 has no flag in §3. Wine is festal and biblical —
poured, tasted, toasted; nobody drunk, nothing coarse.

CHANGING CONDITION (kept OUT of the locks): the jars — empty, filling,
brimming, drawn from — and the feast's mood: joy, quiet panic among the
family, restored and doubled joy. Stated per-beat.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MARY": (
        "MARY LOCK: the mother of Jesus is the same woman in every shot — "
        "about fifty, small and straight, with a serene deeply kind face, "
        "olive skin finely lined at the eyes, and dark hair silvering at "
        "the temples under her veil. She wears a DEEP INDIGO-BLUE mantle "
        "over a DARK MADDER-ROSE dress, modest and worn soft with years "
        "(never cream, never white). Her face is shown clearly — quiet "
        "certainty is its resting state."
    ),
    "STEWARD": (
        "FEAST STEWARD LOCK: the governor of the feast is the same man in "
        "every shot — about fifty-five, round and expansive, with a "
        "curled grey-streaked beard, a napkin over one shoulder and a "
        "taster's confident palate. He wears a festive DARK PLUM robe "
        "with a DEEP GOLD sash (never cream, never white). His face is "
        "shown clearly — born to preside, easily delighted."
    ),
    "BRIDEGROOM": (
        "BRIDEGROOM LOCK: the young bridegroom is the same man in every "
        "shot — early twenties, slight and earnest, with a soft first "
        "beard and worried gentle eyes. He wears a DARK WINE-RED festal "
        "robe with a myrtle circlet (never cream, never white). His "
        "face is shown clearly."
    ),
    "SERVANTS": (
        "SERVANTS LOCK: the wedding servants are the same three in every "
        "shot — a stout older woman with capable arms; a tall thin man "
        "with a long careful face; and a quick boy of fifteen. They "
        "wear plain DARK OLIVE and UMBER working clothes with cloth "
        "belts (never cream, never white). Faces shown clearly."
    ),
    "COURT": (
        "CANA COURTYARD LOCK: the wedding courtyard — a vine-shaded "
        "village courtyard strung with small oil lamps, long tables "
        "down two sides, a musicians' corner with pipe and drum, a low "
        "stone wall to the lane, and in a shaded alcove by the water "
        "door, the STONE JARS' place. Warm gold-to-lamplit light."
    ),
    "JARS": (
        "STONE JARS LOCK: six great stone purification jars in a row in "
        "the shaded alcove — waist-high, pale limestone, wide-mouthed, "
        "each holding twenty to thirty gallons, their rims worn smooth "
        "by generations of ritual use. Always six, always the same row."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r049-b01", "out": "s01-the-very-first-miracle-he.jpeg", "seg": "n1",
        "window": "0.28-5.62", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The very first miracle he ever did was not what you would guess. "
            "Not a healing."
        ),
        "must_show": "the guess declined — a quiet still of NOT-scenes: a folded sickbed mat and a walking staff leaned unused against a wall; the expected first miracles, absent.",
        "must_not_show": "no halo, glare or rim-light; the objects at rest — no drama pending anywhere.",
        "scene": (
            "A quiet still in plain morning light: against a "
            "honey-stone wall a sickbed mat lies rolled and "
            "bound, unneeded, and a walking staff leans "
            "unclaimed beside a door — the standard "
            "furniture of the miracles everyone would have "
            "guessed first, sitting quietly unused at the "
            "edge of a story that starts somewhere much "
            "stranger: a party. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b02", "out": "s02-not-calming-a-storm-he.jpeg", "seg": "n1",
        "window": "5.62-10.26", "wide": True, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": (
            "Not calming a storm. He saved a village wedding from falling "
            "apart."
        ),
        "must_show": "the actual stage — the Cana courtyard dressed for the wedding in golden afternoon: lamps strung, tables laid, garlands up; joy's venue introduced.",
        "must_not_show": "no halo, glare or rim-light; festivity in preparation — the least miraculous-looking setting in scripture.",
        "scene": (
            "The vine-shaded courtyard stands dressed for "
            "its wedding in the golden afternoon — little "
            "oil lamps strung on cords between the posts, "
            "the long tables laid down both sides, myrtle "
            "garlands over the doorways, the musicians "
            "tuning in their corner — a small town's whole "
            "capacity for joy assembled in one yard, "
            "waiting for evening. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b03", "out": "s03-he-was-there-as-a.jpeg", "seg": "n2",
        "window": "10.75-17.96", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARY", "COURT"],
        "narration": (
            "He was there as a guest, with his mother and his friends. A "
            "wedding in a small town like Cana ran for days, and the whole "
            "village came."
        ),
        "must_show": "SCRIPTURE-EXACT: the guest — Jesus seated among the wedding crowd at table, Mary near him, disciples along the bench; IN the joy, indistinguishable from it.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a guest among guests — no space around him, no deference; Mary's nearness natural.",
        "scene": (
            "At the long table in the golden light Jesus "
            "sits wedged happily among the wedding guests — "
            "laughing at a neighbour's story with a piece "
            "of bread in his hand, his mother two places "
            "down in her deep blue mantle talking with the "
            "women, his friends along the bench beyond — "
            "the whole village packed in shoulder to "
            "shoulder, and him simply, fully in it. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b04", "out": "s04-it-was-pure-ordinary-joy.jpeg", "seg": "n2",
        "window": "17.96-22.64", "wide": True, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": "It was pure, ordinary joy, and he was right in the middle of it.",
        "must_show": "the joy at height — the courtyard dancing as evening comes: the ring of dancers, the lamps taking over from the sky, Jesus clapping the rhythm from the bench.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his participation ordinary — clapping, delighting; joy needs no miracle yet.",
        "scene": (
            "Evening arrives and the courtyard dances — the "
            "ring of dancers turning to the pipe and drum "
            "as the strung lamps take over from the "
            "fading sky, children weaving between the "
            "tables — and on the bench Jesus claps the "
            "rhythm with the rest, head back with laughter "
            "at the old men attempting the young men's "
            "steps, joy running through him on its way "
            "around the yard. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b05", "out": "s05-and-then-quietly-disaster-the.jpeg", "seg": "n3",
        "window": "23.15-27.50", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERVANTS", "COURT"],
        "narration": "And then, quietly, disaster. The wine ran out.",
        "must_show": "SCRIPTURE-EXACT: the discovery — behind the feast: the stout servant woman tipping the last amphora over a jug and getting a trickle; the crisis born backstage.",
        "must_not_show": "no halo, glare or rim-light; the quiet of it — the feast roaring on unaware beyond her shoulder.",
        "scene": (
            "In the storeroom's lamplight behind the feast "
            "the stout servant woman tips the last "
            "amphora over the serving jug — and gets a "
            "trickle, then drops, then nothing, the vessel "
            "sounding hollow as she rocks it — her eyes "
            "meeting the tall thin servant's over its "
            "empty mouth while the party's noise rolls in "
            "warm and oblivious through the doorway "
            "behind them. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r049-b06", "out": "s06-to-that-family-it-was.jpeg", "seg": "n3",
        "window": "29.41-33.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["BRIDEGROOM", "COURT"],
        "narration": "To that family it was a public shame they would carry for years.",
        "must_show": "the stakes — the young bridegroom being quietly told at the feast's edge, his festal joy draining as the whisper lands; ruin arriving in a murmur.",
        "must_not_show": "no halo, glare or rim-light; the shame social and real — a family's name failing in real time on a boy's face.",
        "scene": (
            "At the feast's lamplit edge the tall thin "
            "servant bends to the young bridegroom's ear — "
            "and the boy's festal joy drains as the "
            "whisper lands: the soft first beard suddenly "
            "young on a face gone pale under its myrtle "
            "circlet, his eyes flicking across his own "
            "wedding counting cups — a family's honour "
            "beginning to fail quietly in the middle of "
            "its best night. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b07", "out": "s07-the-feast-and-their-good.jpeg", "seg": "n3 + n4",
        "window": "33.58-40.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY", "COURT"],
        "narration": (
            "The feast, and their good name, were about to collapse. His mother "
            "noticed before anyone else did."
        ),
        "must_show": "SCRIPTURE-EXACT: Mary noticing — across the busy feast, her still face reading the servants' faces, the bridegroom's pallor, the empty jug; the first to see.",
        "must_not_show": "no halo, glare or rim-light; noticing as a skill — her stillness amid the noise, eyes doing the arithmetic.",
        "scene": (
            "Amid the feast's rolling noise Mary has gone "
            "still — her serene face turned from the "
            "women's talk, reading the far side of the "
            "courtyard the way mothers read rooms: the "
            "servants' stiff shoulders at the storeroom "
            "door, the bridegroom's pallor, the jug "
            "carried empty against the woman's hip — the "
            "whole quiet disaster assembled in her eyes "
            "before anyone else has seen a single piece "
            "of it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r049-b08", "out": "s08-and-she-did-not-go.jpeg", "seg": "n4",
        "window": "40.26-46.88", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MARY", "COURT"],
        "narration": (
            "And she did not go to the host, or the kitchen. She went straight "
            "to her son and told him the plain truth."
        ),
        "must_show": "the straight line — Mary crossing the busy courtyard directly to Jesus at the table, her path unhesitating through the celebration.",
        "must_not_show": "no halo, glare or rim-light on Jesus; her trajectory the beat — past host, past kitchen, to one person.",
        "scene": (
            "Through the lamplit celebration Mary walks a "
            "perfectly straight line — past the presiding "
            "steward with his napkin, past the kitchen "
            "door's worried light, between the dancers — "
            "small and unhurried in her deep blue mantle, "
            "bound for the one seat at the long table "
            "where her son is turning already at her "
            "approach, a lifetime of knowing each other "
            "closing the distance ahead of her. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b09", "out": "s09-they-have-no-wine-four.jpeg", "seg": "w3 + n4b",
        "window": "47.34-51.16", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": "They have no wine. Four words.",
        "must_show": "SCRIPTURE-EXACT: the four words — Mary and Jesus close, her face lifted to his, the sentence just placed between them; mother and son in a bubble of privacy inside the noise.",
        "must_not_show": "no halo, glare or rim-light on Jesus; no pleading in her — a fact, laid down with perfect economy.",
        "scene": (
            "Close in the lamplight's warm privacy: Mary's "
            "lifted face a hand's breadth from her son's, "
            "the four words just laid down between them "
            "plain as bread on a table — no plea in her "
            "serene eyes, no plan, no pressure, only the "
            "fact and the faith that facts are enough "
            "between them — while the feast's noise closes "
            "around their stillness like water around a "
            "stone. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r049-b10", "out": "s10-she-did-not-tell-him.jpeg", "seg": "n4b",
        "window": "52.12-56.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": (
            "She did not tell him what to do about it, and she did not ask him "
            "for anything."
        ),
        "must_show": "the restraint — close on Mary's hands: folded, still, empty of gesture; the ask that never becomes an ask, told in hands.",
        "must_not_show": "no halo, glare or rim-light; hands at perfect rest — no pointing, no clasping, no supplication.",
        "scene": (
            "Close in the warm light: Mary's small worn "
            "hands folded quietly at her waist against "
            "the deep blue mantle — not clasped in "
            "pleading, not lifted to direct, not touching "
            "her son's sleeve to steer him — hands doing "
            "the hardest thing hands ever learn, which is "
            "nothing at all, while everything they care "
            "about hangs in the air above them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b11", "out": "s11-she-simply-put-it-in.jpeg", "seg": "n4b + jv4",
        "window": "56.16-62.43", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": (
            "She simply put it in front of him and left the deciding to him. "
            "Woman, what have I to do with thee?"
        ),
        "must_show": "SCRIPTURE-EXACT: the gentle idiom — Jesus's answer given SOFTLY: his head tipped toward his mother, warmth unbroken between the two faces even as the weighing words come.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO sharpness anywhere — tenderness carrying a question; their bond visibly untouched by the words.",
        "scene": (
            "The two faces stay close and warm as the "
            "strange words pass: Jesus's head tipped "
            "gently toward his mother, his eyes soft on "
            "hers with something weighing far back in "
            "them, one hand risen lightly toward her "
            "shoulder even as the old idiom leaves him — "
            "and Mary's face receiving it without a "
            "flicker of hurt, two people so long fluent "
            "in each other that even a refusal-shaped "
            "sentence travels between them as tenderness. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r049-b12", "out": "s12-mine-hour-is-not-yet.jpeg", "seg": "jv4 + n5",
        "window": "62.43-69.10", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": (
            "mine hour is not yet come. That sounds sharp in English, but it "
            "was not."
        ),
        "must_show": "the weighing — close on Jesus's face alone: the far 'hour' standing briefly in his eyes at his own first threshold; gravity inside the party's warmth.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the hour carried as depth of gaze only — no symbols, no shadow-play.",
        "scene": (
            "Close on Jesus's face in the lamp warmth: the "
            "feast's gold on his features and his gaze "
            "gone briefly to a great distance — a man "
            "standing at the first threshold of everything, "
            "hearing far off in the word 'hour' all the "
            "hours it will one day mean — gravity and "
            "gentleness sharing the same expression while "
            "the pipe and drum play on behind him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b13", "out": "s13-woman-was-a-word-of.jpeg", "seg": "n5",
        "window": "69.10-79.96", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": (
            "Woman was a word of respect, and the phrase was a gentle old "
            "idiom, something like, is this really ours to fix, and is now the "
            "time?"
        ),
        "must_show": "the idiom's true face — the mother and son in gentle near-smile: a family's private shorthand passing between two people who love each other completely.",
        "must_not_show": "no halo, glare or rim-light on Jesus; warmth explicit — the mistranslation corrected by two faces.",
        "scene": (
            "The two faces close in the warm light, and "
            "the idiom lands as it truly was: the corner "
            "of Jesus's mouth carrying the near-smile of "
            "family shorthand, Mary's eyes answering with "
            "the same — a question asked inside a "
            "lifetime's affection, 'is this ours, is it "
            "now,' passing between mother and son in the "
            "tone reserved for people who have shared a "
            "kitchen for thirty years. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b14", "out": "s14-to-us-that-sounds-small.jpeg", "seg": "n3",
        "window": "27.50-29.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": "To us that sounds small.",
        "must_show": "the modern shrug corrected in advance — the empty wine jug standing alone on the laden table amid the plenty; small object, large fracture.",
        "must_not_show": "no halo, glare or rim-light; the jug's emptiness against the feast's fullness — the one hole in the evening.",
        "scene": (
            "On the laden table amid the bread and figs "
            "and lamplight one serving jug stands empty — "
            "tipped slightly where the last pour left it, "
            "its dark inside showing dry — a small plain "
            "object surrounded by plenty, and through it, "
            "for anyone who knows what weddings owe their "
            "guests, the first visible crack in a "
            "family's whole standing. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b15", "out": "s15-he-was-not-brushing-her.jpeg", "seg": "n5",
        "window": "79.96-86.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MARY"],
        "narration": (
            "He was not brushing her off. He was wondering out loud whether "
            "this was the moment to begin."
        ),
        "must_show": "the threshold — Jesus's gaze moving from his mother's face out over the feast: the beginning, being weighed against a whole courtyard of ordinary joy.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the wondering visible — eyes travelling from her to the party and inward.",
        "scene": (
            "From his mother's steady face Jesus's gaze "
            "lifts and travels slowly out over the "
            "lamplit feast — the dancers, the children, "
            "the young bridegroom's pale worry at the "
            "edge — and returns inward, weighing: the "
            "whole hidden life before this night on one "
            "side, and on the other a village wedding "
            "running out of wine — the first miracle "
            "choosing its own birthday in a man's quiet "
            "face. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r049-b16", "out": "s16-and-his-mother-who-knew.jpeg", "seg": "n6",
        "window": "86.59-91.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": (
            "And his mother, who knew him better than anyone alive, did not "
            "argue with him."
        ),
        "must_show": "the knowing — close on Mary's face as she reads her son's weighing: no argument anywhere in her, a small settled certainty arriving instead.",
        "must_not_show": "no halo, glare or rim-light; her certainty PRIOR to any answer — she knows how this ends before he does.",
        "scene": (
            "Close on Mary's lined serene face in the "
            "lamplight: her son's weighing reflected in "
            "her watching eyes, and her whole expression "
            "already settling — not into persuasion, not "
            "into retreat, but into the small private "
            "certainty of the one person alive who has "
            "watched this heart decide things for thirty "
            "years and knows, before he does, which way "
            "it always goes. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b17", "out": "s17-she-just-turned-to-the.jpeg", "seg": "n6 + w5",
        "window": "91.24-98.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARY", "SERVANTS", "COURT"],
        "narration": (
            "She just turned to the servants and gave them the best advice in "
            "the whole Bible. Whatsoever he saith unto you, do it."
        ),
        "must_show": "SCRIPTURE-EXACT: the turn and the charge — Mary turned to the three servants, her hand indicating her son, the seven words visibly landing on their puzzled faces.",
        "must_not_show": "no halo, glare or rim-light; her authority gentle and total — three servants being reassigned to a carpenter by a guest.",
        "scene": (
            "Mary has turned from her son to the three "
            "waiting servants — the stout woman, the tall "
            "careful man, the quick boy — her small hand "
            "turned palm-open toward Jesus at the table "
            "as she gives them the seven words, and their "
            "puzzled faces taking the strangest order of "
            "the night from a guest with no standing to "
            "give it and no doubt in her voice. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b18", "out": "s18-whatever-he-tells-you-do.jpeg", "seg": "n6b",
        "window": "99.77-102.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["MARY"],
        "narration": "Whatever he tells you, do it. That is all of it.",
        "must_show": "the whole theology — close on Mary's face at the seven words: the entire school of discipleship in one serene, certain expression.",
        "must_not_show": "no halo, glare or rim-light; the simplicity absolute — no flourish, a whole faith in one plain look.",
        "scene": (
            "Close on Mary's face in the warm light as the "
            "seven words finish: serene, certain, entirely "
            "without drama — the deep-lined eyes holding a "
            "trust so old it has stopped needing reasons, "
            "the whole of discipleship's curriculum "
            "resting in one small woman's untroubled "
            "expression at a village party. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b19", "out": "s19-she-did-not-explain-and.jpeg", "seg": "n6b",
        "window": "102.73-111.33", "wide": True, "jesus": False, "ref": False,
        "locks": ["MARY", "SERVANTS", "COURT"],
        "narration": (
            "She did not explain, and she did not stay to supervise. She handed "
            "the servants over to him and stepped back, and trusted her son "
            "with the rest."
        ),
        "must_show": "the stepping back — Mary already walking away toward the women's tables, not looking back; the servants left standing oriented toward Jesus; trust with its hands off.",
        "must_not_show": "no halo, glare or rim-light; NO backward glance from Mary — the walk-away complete; supervision declined.",
        "scene": (
            "Mary is already three steps gone toward the "
            "women's tables, her deep blue back unturned, "
            "rejoining the party's talk with the ease of "
            "a woman whose errand is entirely finished — "
            "and behind her the three servants stand "
            "reoriented like compass needles toward the "
            "seated carpenter, holding the strangest "
            "instructions of their working lives, "
            "unsupervised, entrusted, waiting. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b20", "out": "s20-they-have-no-wine.jpeg", "seg": "n4b",
        "window": "51.16-52.12", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "They have no wine.",
        "must_show": "the four words as still life — the empty amphora on its side in the storeroom lamplight, its dry dark mouth toward the camera.",
        "must_not_show": "no halo, glare or rim-light; the sentence in clay — one drained vessel, plainly done.",
        "scene": (
            "In the storeroom's small lamplight the last "
            "amphora lies tipped on its side, its dark "
            "mouth toward the camera and dry to the "
            "throat, a stain of the final trickle drying "
            "on the stone below it — four words made of "
            "fired clay and emptiness, waiting for "
            "somebody to do something about them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b21", "out": "s21-standing-nearby-were-six-big.jpeg", "seg": "n7",
        "window": "111.89-120.49", "wide": True, "jesus": False, "ref": False,
        "locks": ["JARS", "COURT"],
        "narration": (
            "Standing nearby were six big stone jars, the kind kept for the "
            "washing rituals, each one holding twenty or thirty gallons."
        ),
        "must_show": "SCRIPTURE-EXACT: the six jars — the row of great waist-high stone vessels in their shaded alcove; scale shown against the doorway; ritual furniture about to be conscripted.",
        "must_not_show": "no halo, glare or rim-light; SIX, countable — pale stone, worn rims, big as barrels.",
        "scene": (
            "In the shaded alcove by the water door the six "
            "great stone jars stand in their patient row — "
            "waist-high, wide-mouthed, pale limestone gone "
            "grey at the worn rims, each one big enough "
            "to bathe a child in — the sober furniture of "
            "ritual washing lined up at the edge of a "
            "party, unaware of their promotion. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b22", "out": "s22-empty-jars-meant-for-making.jpeg", "seg": "n7",
        "window": "120.49-126.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["JARS"],
        "narration": (
            "Empty jars, meant for making things clean. Not a wine cup in "
            "sight."
        ),
        "must_show": "the emptiness and the purpose — looking down into one jar's clean dry stone hollow; made for purity, holding nothing.",
        "must_not_show": "no halo, glare or rim-light; the interior plain dry stone — capacity, waiting.",
        "scene": (
            "Looking down over a worn rim into one great "
            "jar: the clean pale hollow of its stone "
            "belly, dry to the bottom, a faint mineral "
            "ring from years of ritual water its only "
            "content — thirty gallons of holy-purpose "
            "emptiness, without one drop in it, and not a "
            "wine cup anywhere on its horizon. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b23", "out": "s23-fill-the-waterpots-with-water.jpeg", "seg": "jv7 + n8",
        "window": "127.17-131.62", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SERVANTS", "JARS", "COURT"],
        "narration": "Fill the waterpots with water. Not wine.",
        "must_show": "SCRIPTURE-EXACT: the order given — Jesus by the jars speaking quietly to the three servants, one hand indicating the row; their faces taking the anticlimax.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the order's plainness — water, of all things; the servants' puzzlement honest.",
        "scene": (
            "By the alcove Jesus speaks quietly to the "
            "three servants, one hand turned toward the "
            "row of great jars — and the order lands on "
            "their faces in three kinds of honest "
            "puzzlement: the stout woman's brows up, the "
            "tall man glancing at the jars and back, the "
            "boy already half-turned toward the well but "
            "waiting to be sure — water, requested at a "
            "wedding, by the calmest man in the courtyard. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r049-b24", "out": "s24-the-plainest-thing-there-is.jpeg", "seg": "n8",
        "window": "132.70-136.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["SERVANTS"],
        "narration": "The plainest thing there is, from the nearest well.",
        "must_show": "the plainness — the boy at the village well in lamplit dark, hauling the rope, the bucket rising with ordinary water catching the lamp.",
        "must_not_show": "no halo, glare or rim-light; water utterly ordinary — a bucket on a rope at night, nothing more.",
        "scene": (
            "At the village well in the lane's darkness the "
            "quick boy hauls the wet rope hand over hand, "
            "a small lamp set on the well's rim beside "
            "him — and the bucket rises brimming with the "
            "plainest thing there is, ordinary dark water "
            "swaying and catching the little flame — the "
            "raw material of the first miracle, drawn by "
            "a fifteen-year-old on loan from a party. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r049-b25", "out": "s25-the-servants-filled-all-six.jpeg", "seg": "n8",
        "window": "136.41-145.44", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERVANTS", "JARS"],
        "narration": (
            "The servants filled all six to the very top, hauling bucket after "
            "bucket, surely wondering what plain water had to do with the "
            "problem."
        ),
        "must_show": "SCRIPTURE-EXACT: to the brim — the bucket brigade in full labour: all three servants hauling and pouring, the last jar's surface trembling AT the rim.",
        "must_not_show": "no halo, glare or rim-light; the brim exact — water standing level with the stone lip; sweat and wondering on the faces.",
        "scene": (
            "The alcove has become a bucket brigade: the "
            "boy jogging in from the lane with two more "
            "pails, the tall man pouring careful and "
            "steady, the stout woman steadying the last "
            "jar's rim — where the water now stands "
            "trembling exactly level with the worn stone "
            "lip, brim meaning brim — three sweating "
            "servants obeying to the letter an order none "
            "of them can find the sense in yet. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b26", "out": "s26-draw-out-now-and-bear.jpeg", "seg": "jv8",
        "window": "146.01-149.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SERVANTS", "JARS"],
        "narration": "Draw out now, and bear unto the governor of the feast.",
        "must_show": "SCRIPTURE-EXACT: the second order — Jesus's quiet word as the tall servant dips the long-handled cup into the brimming jar; obedience mid-motion.",
        "must_not_show": "no halo, glare or rim-light; NOTHING done to the water — no gesture over the jars, no touch; the dip is the whole visible event.",
        "scene": (
            "At the brimming jar the tall careful servant "
            "dips the long-handled cup beneath the "
            "surface at Jesus's quiet word — Jesus "
            "standing easy an arm's length off, hands at "
            "his sides, touching nothing, commanding "
            "nothing visible — just a cup going down into "
            "water in lamplight, and an instruction to "
            "walk it across a courtyard. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b27", "out": "s27-no-lightning-no-words-spoken.jpeg", "seg": "n9",
        "window": "151.44-154.79", "wide": False, "jesus": True, "ref": REF,
        "locks": ["JARS"],
        "narration": "No lightning. No words spoken over the jars.",
        "must_show": "the non-event — the six full jars standing utterly ordinary in the alcove lamplight, Jesus already turning back toward the feast; the miracle's total lack of staging.",
        "must_not_show": "no halo, glare or rim-light; NOTHING visually miraculous — six jars of water and a man walking away; the restraint IS the beat.",
        "scene": (
            "The six jars stand brimming and completely "
            "ordinary in the alcove's small lamplight — "
            "water looking like water, stone looking like "
            "stone — and Jesus is already turning away "
            "back toward the tables, unhurried, his part "
            "apparently consisting of nothing at all — "
            "the most understated moment in the history "
            "of miracles, indistinguishable from a man "
            "checking on the washing-up. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b28", "out": "s28-no-show-at-all-he.jpeg", "seg": "n9",
        "window": "154.79-161.34", "wide": True, "jesus": False, "ref": False,
        "locks": ["SERVANTS", "COURT"],
        "narration": (
            "No show at all. He simply told them to dip a cup and carry it to "
            "the man in charge of the feast."
        ),
        "must_show": "the carry — the tall servant crossing the lamplit courtyard with the filled cup held carefully level, the feast parting around his concentration.",
        "must_not_show": "no halo, glare or rim-light; the cup's contents NOT shown glowing or changed — just a carried cup and a careful man.",
        "scene": (
            "Across the lamplit courtyard the tall servant "
            "carries the filled cup at a careful level "
            "walk — both hands to it, eyes on the surface, "
            "threading between dancers and benches with "
            "the concentration of a man transporting "
            "either a miracle or his own dismissal — the "
            "boy trailing him at two paces, unable to "
            "stay behind. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r049-b29", "out": "s29-and-somewhere-between-the-jar.jpeg", "seg": "n9",
        "window": "161.34-166.82", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And somewhere between the jar and the cup, the water quietly "
            "became something else."
        ),
        "must_show": "the unseen change — extreme close on the moving cup mid-carry: dark liquid trembling with the walk, lamplight on its surface; WHAT it now is, unannounced.",
        "must_not_show": "no halo, glare or rim-light, NO transformation effects — dark liquid in lamplight, the change complete and invisible.",
        "scene": (
            "Extreme close on the cup mid-carry: the dark "
            "liquid trembling gently with the servant's "
            "footsteps, the strung lamps' small flames "
            "riding its moving surface — deep-coloured "
            "now, catching the light the way water never "
            "quite does — the entire miracle already over, "
            "having happened nowhere anyone can point to, "
            "between a stone rim and a wooden lip. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b30", "out": "s30-the-steward-tasted-it-and.jpeg", "seg": "n10",
        "window": "167.34-173.19", "wide": False, "jesus": False, "ref": False,
        "locks": ["STEWARD"],
        "narration": (
            "The steward tasted it and had no idea where it came from. He "
            "pulled the bridegroom aside, half laughing."
        ),
        "must_show": "SCRIPTURE-EXACT: the tasting — the round steward mid-taste: eyes closing, brows flying up, the connoisseur's whole body registering the impossible vintage.",
        "must_not_show": "no halo, glare or rim-light; comedy welcome — the taste's verdict written across an expert's face.",
        "scene": (
            "Close in the lamplight: the round plum-robed "
            "steward with the cup at his lips mid-taste — "
            "and the verdict arriving through his whole "
            "body: eyes closing, brows climbing his "
            "forehead, the napkin'd shoulder rising — a "
            "professional palate meeting the best wine of "
            "its career at the tail end of a village "
            "wedding, with no idea on earth where it came "
            "from. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r049-b31", "out": "s31-water.jpeg", "seg": "n8",
        "window": "131.62-132.70", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Water.",
        "must_show": "the word as image — a close still of clear well water in a plain bucket, utterly itself; the ingredient, at its plainest.",
        "must_not_show": "no halo, glare or rim-light; clear, ordinary, unremarkable water — the point entire.",
        "scene": (
            "A close still in lamplight: a plain wooden "
            "bucket of clear well water, the surface "
            "settling from the carry, a single drip "
            "falling from the rope's end — water at its "
            "most absolutely ordinary, transparent and "
            "unpromising, the plainest noun in the "
            "language sitting in a bucket waiting to be "
            "poured into history. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b32", "out": "s32-every-man-at-the-beginning.jpeg", "seg": "s10",
        "window": "173.79-183.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["STEWARD", "BRIDEGROOM", "COURT"],
        "narration": (
            "Every man at the beginning doth set forth good wine; and when men "
            "have well drunk, then that which is worse: but thou hast kept the "
            "good wine until now."
        ),
        "must_show": "SCRIPTURE-EXACT: the toast — the steward with his arm around the baffled bridegroom, cup raised to the feast, publicly crediting the boy for the impossible.",
        "must_not_show": "no halo, glare or rim-light; the bridegroom's bafflement under the praise — credited for a miracle he knows nothing about.",
        "scene": (
            "Before the whole lamplit feast the steward "
            "stands with one expansive arm around the "
            "young bridegroom's shoulders and the cup "
            "raised high in his other hand, proclaiming "
            "the vintage to the courtyard — while under "
            "the public praise the boy's face is pure "
            "baffled gratitude, a groom receiving the "
            "credit for the one part of his wedding he "
            "had absolutely nothing to do with. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b33", "out": "s33-everybody-serves-the-good-wine.jpeg", "seg": "n10b",
        "window": "184.81-191.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["STEWARD"],
        "narration": (
            "Everybody serves the good wine first, he said, and brings out the "
            "cheap stuff once the guests have stopped paying attention."
        ),
        "must_show": "the worldly wisdom — the steward's knowing wink mid-speech, finger tapping the cup; the trade's old trick recited by its master.",
        "must_not_show": "no halo, glare or rim-light; the insider's comedy — a professional explaining the racket he polices.",
        "scene": (
            "Close on the round steward mid-oration: one "
            "eyebrow arched, a knowing finger tapping the "
            "cup's rim, the half-wink of a man revealing "
            "the catering trade's oldest arithmetic to a "
            "courtyard that has lived it at every wedding "
            "they ever attended — the worldly rule laid "
            "out in full, one sentence before the "
            "exception rewrites it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r049-b34", "out": "s34-you-have-done-it-backwards.jpeg", "seg": "n10b",
        "window": "191.41-195.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["STEWARD", "BRIDEGROOM"],
        "narration": "You have done it backwards. You saved the best for last.",
        "must_show": "the line delivered — the steward's delighted face inches from the bridegroom's, the cup between them; the sentence that names the whole gospel by accident.",
        "must_not_show": "no halo, glare or rim-light; accidental prophecy — the steward means wine; the frame lets the words mean everything.",
        "scene": (
            "Close between the two faces in the lamplight: "
            "the steward's delighted grin inches from the "
            "bridegroom's bewilderment, the wondrous cup "
            "held up between them like evidence — a "
            "catering compliment leaving his mouth and "
            "becoming, in the air between jar and heaven, "
            "the truest sentence anyone says in the whole "
            "story. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r049-b35", "out": "s35-and-that-is-the-line.jpeg", "seg": "n11",
        "window": "195.98-199.70", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": "And that is the line to hold on to. He saved the best for last.",
        "must_show": "the line's true owner — Jesus at the feast's edge, overhearing the toast, the quiet pleasure of the uncredited giver on his face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; anonymity enjoyed — the giver content to stay unnamed in his own miracle.",
        "scene": (
            "At the feast's lamplit edge Jesus stands "
            "half-turned, overhearing the steward's toast "
            "across the courtyard — and on his face the "
            "quietest pleasure of the night: the "
            "uncredited giver watching his gift praised "
            "onto somebody else, entirely content, the "
            "smallest smile inside the beard of a man "
            "whose best work just went home under another "
            "name. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r049-b36", "out": "s36-not-a-bare-rescue-not.jpeg", "seg": "n11",
        "window": "199.70-203.46", "wide": False, "jesus": False, "ref": False,
        "locks": ["JARS"],
        "narration": "Not a bare rescue, not just barely enough to get by.",
        "must_show": "the abundance measured — the six great jars in the alcove, ALL full of the dark best wine, lamplight on six brimming surfaces; oversupply as signature.",
        "must_not_show": "no halo, glare or rim-light; six full jars counted — the scale of the gift plainly beyond the party's need.",
        "scene": (
            "In the alcove the six great stone jars stand "
            "brimming still — six dark surfaces holding "
            "the lamplight, a hundred and fifty gallons "
            "of the feast's finest deep in ritual "
            "stoneware — more wine than the village could "
            "drink in a week of weddings, poured out "
            "quietly for one family's one bad evening: "
            "abundance signed in the corner of the "
            "picture. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r049-b37", "out": "s37-something-like-a-hundred-and.jpeg", "seg": "n11",
        "window": "203.46-212.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": (
            "Something like a hundred and fifty gallons of the finest wine at "
            "the party, poured out on ordinary people who would never even know "
            "who paid for it."
        ),
        "must_show": "the gift landing wide — the feast restored and doubled: cups filled down the long tables, the dance renewed, ordinary faces bright with wine they will never trace.",
        "must_not_show": "no halo, glare or rim-light; joy general and unknowing — the whole courtyard drinking anonymously given glory.",
        "scene": (
            "The courtyard runs at full joy again — cups "
            "refilled down both long tables, the dance "
            "ring doubled, the musicians sweating happily "
            "through their best set, old women laughing "
            "with the wine's warmth in their cheeks — a "
            "whole village glad on a hundred and fifty "
            "anonymous gallons, not one face in the yard "
            "knowing whose hand is under the evening. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r049-b38", "out": "s38-that-is-the-god-this.jpeg", "seg": "n12",
        "window": "212.71-220.21", "wide": False, "jesus": True, "ref": REF,
        "locks": ["COURT"],
        "narration": (
            "That is the God this story is showing you. His first move in the "
            "whole world was not to frighten anyone or settle a score."
        ),
        "must_show": "the first move's face — Jesus back at the table among the guests, joy around him, his own gladness plain; the signature under the evening.",
        "must_not_show": "no halo, glare or rim-light on Jesus; among, not above — the giver seated in his own gift.",
        "scene": (
            "Back at the long table Jesus sits among the "
            "restored celebration — a neighbour refilling "
            "his cup without knowing what he pours, the "
            "dance's light crossing his face — and his "
            "own gladness sits plain and unperformed in "
            "the middle of it: the first move of God in "
            "the world, seated shoulder to shoulder with "
            "its beneficiaries, drinking its own health "
            "anonymously. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r049-b39", "out": "s39-it-was-to-walk-into.jpeg", "seg": "n12",
        "window": "220.21-227.23", "wide": True, "jesus": False, "ref": False,
        "locks": ["BRIDEGROOM", "COURT"],
        "narration": (
            "It was to walk into a family's worst moment of the day and quietly "
            "turn it into more joy than they started with."
        ),
        "must_show": "the family saved — the bridegroom and his bride at the feast's height: shame averted, honour doubled, the young couple radiantly unaware of how close it came.",
        "must_not_show": "no halo, glare or rim-light; the couple's joy unshadowed — the rescue so complete they never felt the fall.",
        "scene": (
            "At the feast's bright centre the young "
            "bridegroom dances a slow turn with his bride "
            "under the strung lamps — his myrtle circlet "
            "crooked, her laughing face against the "
            "music — the family's name not merely saved "
            "but gilded, the worst hour of their day "
            "converted wholesale into the story their "
            "grandchildren will demand at every feast to "
            "come. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r049-b40", "out": "s40-his-friends-saw-it-and.jpeg", "seg": "n12",
        "window": "227.23-230.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["COURT"],
        "narration": "His friends saw it, and they believed him.",
        "must_show": "SCRIPTURE-EXACT (v11): the belief — close along the disciples' faces at the table's end: the ones who KNOW, looking at their teacher across the feast with the first full weight of belief arriving.",
        "must_not_show": "no halo, glare or rim-light; belief as facial weather — awe, joy and decision landing on fishermen's faces.",
        "scene": (
            "At the table's end, close along the row of "
            "the friends' faces in the lamplight: the "
            "big fisherman's cup stopped halfway to his "
            "mouth, the younger brother looking from the "
            "wine to the teacher and back, the quiet one "
            "simply staring with his eyes wet — the only "
            "men in the courtyard who know what the jars "
            "held an hour ago, watching their friend "
            "across the feast while belief arrives in "
            "them for good. Every figure has two arms, "
            "two hands and one head."
        ),
    },
]
