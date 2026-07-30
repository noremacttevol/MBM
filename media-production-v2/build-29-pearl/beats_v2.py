#!/usr/bin/env python3
"""V2 beat map — row 29, build-29-pearl (Matthew 13:45-46).

COVERAGE: 18 pictures over 103.9 s = 5.8 s/picture (matches the library density).

SCRIPTURE FACTS (Matthew 13:45-46 KJV):
  v45   "Again, the kingdom of heaven is like unto a MERCHANT MAN, SEEKING
        goodly pearls" — a professional, a connoisseur, a lifelong seeker.
        Spoken IN THE HOUSE to the disciples (Matthew 13:36; v45 follows).
        Rows 25 and 28 staged that room wide-from-outside-the-circle and
        close-past-a-shoulder — so THIS build's frame beat (b01) looks from
        BESIDE Jesus along his eyeline to the listening faces. Different
        composition, no repeat.
  v46   "when he had found ONE pearl of great price, went and SOLD ALL THAT
        HE HAD, and BOUGHT IT."
        — like row 28 the selling is total, and it is GLAD (the narration
          hammers 'not grieving, not robbed').
        — the narration's closing turn (b15-b18) reads the parable the
          other way: JESUS is the merchant and YOU are the pearl — he gave
          everything, his own life, to buy you back. The Jesus beats there
          are quiet and tender, never theatrical.

TIME OF DAY: frame beats are warm afternoon window light (the Matthew 13
house). The merchant's search runs varied and long on purpose — bright
morning roads, dim lamplit dealer's stalls, harbour dusk — a LIFE of
looking; each searching beat may pick its own hour. The find itself is in
a dim shop lit by one shaft of window light. The selling is plain daylight;
the final possession beat is warm evening calm.

CONTENT-CARE: row 29 has no flag in §3. Nothing sensitive.

CHANGING CONDITION (kept OUT of the locks): the merchant's wealth — rings,
fine outer robe, goods, pearl trays — leaves him across the selling beats
until he owns one thing only. His base garments stay; the ornaments go.

THE PEARL: one great round sea pearl, smooth silver-white, the size of a
thumb-tip — always the same pearl, always resting on dark cloth or skin so
its pale perfection reads. Never faceted, never a gem, never oversized.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "MERCHANT": (
        "MERCHANT LOCK: the pearl merchant is the same man in every shot — "
        "about sixty, spare and upright, with a neat pointed silver-grey "
        "beard, an intelligent lined face and calm appraising dark eyes. He "
        "wears a DEEP WINE-RED wool robe over a DARK CHARCOAL under-tunic "
        "with a DARK TEAL sash (never cream, never white). In the early "
        "beats he also wears two gold rings and a fine DARK INDIGO "
        "travelling cloak; these ornaments are gone after the selling "
        "beats. His face is shown clearly."
    ),
    "PEARL": (
        "PEARL LOCK: the pearl of great price is the same in every shot — "
        "one large perfectly round sea pearl the size of a man's thumb-tip, "
        "smooth silver-white with the faintest warm blush, flawless, always "
        "shown against dark cloth or skin. Never faceted, never a gemstone, "
        "never larger than a thumb-tip."
    ),
    "MARKET-ROADS": (
        "TRADE ROADS LOCK: the merchant's world of the search — dusty "
        "caravan roads between walled towns, arcaded market lanes hung "
        "with dark awnings, dealers' low tables spread with dark cloth, "
        "brass hand-scales and small shallow trays, and harbour quays with "
        "moored trading boats. Traders and buyers wear SATURATED DEEP "
        "earth colours — dark browns, deep russet, dark olive, dusty "
        "indigo (never cream, never white; only Jesus wears cream)."
    ),
    "MERCHANT-HOUSE": (
        "MERCHANT HOUSE LOCK: the merchant's fine town house — a paved "
        "inner courtyard with a small fig tree, carved cedar doors, "
        "patterned dark rugs, brass lamps, cedar chests with iron "
        "fittings, and shelves of fine vessels. Prosperous, tasteful, "
        "orderly."
    ),
    "HOUSE-ROOM": (
        "HOUSE ROOM LOCK: the main room of a Capernaum house — thick "
        "honey-stone walls, one deep-set window throwing a broad slant of "
        "warm afternoon light, rush mats and low cushions on a "
        "beaten-earth floor, and a shelf of clay vessels in shadow."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r029-b01", "out": "s01-jesus-told-one-more-short.jpeg", "seg": "n1",
        "window": "0.28-3.11", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": "Jesus told one more short story, only two lines long.",
        "must_show": "the frame — from just BESIDE the seated Jesus, along his eyeline, the ring of listening disciples' faces in the warm window light.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the listeners' faces carry the frame — his profile is near-edge, theirs are the light.",
        "scene": (
            "From just beside and a little behind Jesus's shoulder, his "
            "profile soft at the frame's near edge: along his eyeline the "
            "faces of five disciples sit ranged in the broad slant of "
            "afternoon window light on the rush mats — a young one "
            "cross-legged and rapt, an older one with his head tilted, "
            "each face open and waiting for the little story just begun. "
            "The honey-stone wall warms behind them. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b02", "out": "s02-again-the-kingdom-of-heaven.jpeg", "seg": "j1",
        "window": "3.80-9.00", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MARKET-ROADS"],
        "narration": (
            "Again, the kingdom of heaven is like unto a merchant man, seeking "
            "goodly pearls:"
        ),
        "must_show": "SCRIPTURE-EXACT: the seeker introduced — the fine-robed merchant bent over a dealer's dark-cloth table in a market lane, a small pearl held up to his eye between finger and thumb.",
        "must_not_show": "no halo, glare or rim-light; a professional at work — precise, practised appraisal, not shopping.",
        "scene": (
            "In an arcaded market lane under dark awnings the spare "
            "silver-bearded merchant in his deep wine-red robe bends over "
            "a dealer's low table spread with dark cloth, holding one "
            "small pearl up between finger and thumb at his eye, his "
            "gold-ringed hand steady, his appraising gaze narrowed with "
            "forty years of practice. The seated dealer watches him "
            "hopefully across the brass hand-scales. Broken bright light "
            "through the awnings. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r029-b03", "out": "s03-he-spent-his-whole-life.jpeg", "seg": "n2",
        "window": "10.07-17.55", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MARKET-ROADS"],
        "narration": (
            "He spent his whole life traveling and searching, handling the "
            "finest pearls in the world, always hunting for something better."
        ),
        "must_show": "the LIFE of searching — the merchant on the dusty road with a laden pack-donkey, a walled town behind, another far ahead; distance in his eyes.",
        "must_not_show": "no halo, glare or rim-light; a traveller's patience and wear — this is decades, not an errand.",
        "scene": (
            "On a long dusty caravan road in early morning light the "
            "merchant walks beside his laden pack-donkey, his dark indigo "
            "travelling cloak over the wine-red robe and a staff in his "
            "hand — the walled town he has finished with lying small "
            "behind him, and far down the road ahead another town's "
            "rooftops just visible in the haze he is already measuring "
            "with his eyes. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r029-b04", "out": "s04-he-had-seen-a-lot.jpeg", "seg": "n3",
        "window": "18.16-21.98", "wide": False, "jesus": False, "ref": False,
        "locks": ["MERCHANT"],
        "narration": "He had seen a lot of beautiful pearls. Good ones. Costly ones.",
        "must_show": "a close shot over the merchant's shoulder of a shallow tray of many good pearls on dark cloth — genuinely fine, and his face unmoved above them.",
        "must_not_show": "no halo, glare or rim-light; the tray pearls are GOOD — the point is that good is not enough; his face is politely unimpressed.",
        "scene": (
            "Over the merchant's shoulder, close: a shallow wooden tray "
            "lined with dark cloth holds two dozen fine pearls of "
            "honest quality — round, pale, costly — and his ringed hand "
            "hovers above them without descending, while his lined face "
            "in the lamplight of the dealer's stall stays courteous and "
            "entirely unmoved. He has seen a thousand trays like this "
            "one. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b05", "out": "s05-but-he-kept-looking-because.jpeg", "seg": "n3 + n4",
        "window": "21.98-27.93", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MARKET-ROADS"],
        "narration": (
            "But he kept looking, because not one of them was the one. And then "
            "one day, he found it."
        ),
        "must_show": "the threshold moment — the merchant stopped dead in a dim shop doorway, eyes fixed on something off-frame on the dealer's table, everything in him arrested.",
        "must_not_show": "no halo, glare or rim-light; the pearl itself NOT yet shown — his stopped body and changed face carry the beat.",
        "scene": (
            "In the doorway of a dim harbour-lane shop the merchant has "
            "stopped mid-step, one hand still holding the door curtain "
            "aside, his whole spare frame gone motionless — and his "
            "practised, unimpressible eyes are fixed wide on something "
            "low and off-frame on the dealer's table inside, his lips "
            "just parting. Behind him the bright lane goes on with its "
            "noise; inside, one shaft of window light crosses the dark "
            "little room toward what he is looking at. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b06", "out": "s06-a-single-pearl-more-perfect.jpeg", "seg": "n4",
        "window": "27.93-35.40", "wide": False, "jesus": False, "ref": False,
        "locks": ["PEARL"],
        "narration": (
            "A single pearl, more perfect and more precious than anything he "
            "had ever held. The pearl he had been looking for his whole life."
        ),
        "must_show": "SCRIPTURE-EXACT: the pearl itself, alone — one great round silver-white pearl on dark cloth in a single shaft of window light, filling the frame's attention.",
        "must_not_show": "no halo, glare or rim-light; the pearl is thumb-tip sized and REAL — no sparkle effects, no rays; its perfection is quiet.",
        "scene": (
            "A close still shot in the dim shop: on a square of "
            "near-black cloth, alone in the centre of a single shaft of "
            "soft window light, rests one great round pearl — smooth "
            "silver-white with the faintest warm blush, flawless, the "
            "size of a thumb-tip, its pale curve holding the light the "
            "way still water holds the morning. Everything around it "
            "falls away into shadow. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r029-b07", "out": "s07-and-he-knew-the-moment.jpeg", "seg": "n5",
        "window": "35.95-40.18", "wide": False, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "PEARL"],
        "narration": (
            "And he knew, the moment he saw it, exactly what he was going to "
            "do."
        ),
        "must_show": "the decision on his face — a close shot of the merchant holding the pearl in his open palm for the first time, his lifetime of appraisal collapsing into certainty.",
        "must_not_show": "no halo, glare or rim-light; his face is not greed and not surprise — it is RECOGNITION, and the decision already made.",
        "scene": (
            "A close shot in the shop's shaft of light: the great pearl "
            "rests in the merchant's open palm, his gold rings dull "
            "beside its pale perfection — and above it his lined face "
            "has changed entirely, the appraiser's narrowness gone wide "
            "and still, an old seeker looking at the end of his search "
            "with his mind already and completely made up. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b08", "out": "s08-who-when-he-had-found.jpeg", "seg": "j2",
        "window": "40.83-47.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MARKET-ROADS", "PEARL"],
        "narration": (
            "Who, when he had found one pearl of great price, went and sold all "
            "that he had, and bought it."
        ),
        "must_show": "SCRIPTURE-EXACT: the purchase — the pearl passing into the merchant's keeping as a great heap of coins, his rings and his fine cloak pass the other way across the dealer's table.",
        "must_not_show": "no halo, glare or rim-light; the exchange must be visibly TOTAL — coins, rings, cloak all on the dealer's side; the pearl alone on his.",
        "scene": (
            "At the dealer's dark-cloth table the trade is made: on the "
            "dealer's side lies a poured heap of coins, the merchant's "
            "two gold rings set on top and his fine dark indigo "
            "travelling cloak folded beside them — and into the "
            "merchant's cupped, now-bare hands the seated dealer lowers "
            "the one great pearl. The merchant's wine-red robe is plain "
            "of every ornament. Window light crosses the table between "
            "them. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b09", "out": "s09-he-went-home-and-sold.jpeg", "seg": "n6",
        "window": "48.89-50.50", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MERCHANT-HOUSE"],
        "narration": "He went home and sold everything.",
        "must_show": "the emptying begun — the merchant's fine courtyard with buyers carrying out rugs, chests and lamps past him, and him directing it all briskly.",
        "must_not_show": "no halo, glare or rim-light; he is the ENGINE of the sale, not its victim — brisk, decided, almost cheerful.",
        "scene": (
            "In the paved courtyard of his fine town house, under the "
            "small fig tree, the merchant briskly waves through a "
            "procession of buyers — one shouldering a rolled dark rug, "
            "two carrying an iron-fitted cedar chest between them, a "
            "woman with brass lamps gathered in her apron — while he "
            "stands at the carved cedar doors directing the emptying of "
            "his own house with the energy of a younger man. Plain "
            "daylight over the courtyard. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b10", "out": "s10-his-house-his-goods-every.jpeg", "seg": "n6",
        "window": "50.50-56.74", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MERCHANT-HOUSE"],
        "narration": (
            "His house, his goods, every other pearl he owned. All of it, gone, "
            "to buy the one."
        ),
        "must_show": "the last and sharpest sale — his own trade stock, trays of good pearls, sliding across a table into another dealer's hands; the tools of his life's work, released.",
        "must_not_show": "no halo, glare or rim-light; the sold pearls are the GOOD ones from his life's collecting — and his face releases them without a flicker.",
        "scene": (
            "At a table in the emptied courtyard the merchant slides his "
            "own shallow trade trays — row upon row of good pearls on "
            "dark cloth, his life's collection — across into the "
            "receiving hands of a younger dealer, whose face cannot "
            "believe its luck; the merchant's own face is easy and "
            "unclouded, one hand already resting, without thinking, over "
            "the small cloth bag at his own chest where the one pearl "
            "waits. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b11", "out": "s11-and-here-is-the-thing.jpeg", "seg": "n7",
        "window": "57.38-62.09", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MERCHANT-HOUSE"],
        "narration": (
            "And here is the thing. He did not do it grieving. He did not feel "
            "robbed."
        ),
        "must_show": "the merchant standing in his stripped, echoing courtyard — bare walls, empty shelves — completely at peace, almost amused.",
        "must_not_show": "no halo, glare or rim-light; the emptiness around him against the peace in him is the whole composition.",
        "scene": (
            "The fine courtyard stands stripped and echoing — bare paving, "
            "empty shelves, pale patches on the wall where the rugs hung, "
            "the little fig tree the only ornament left — and in the "
            "middle of it the merchant stands quite still in his plain "
            "wine-red robe, hands folded, looking around at the emptiness "
            "with a light, almost amused peace, like a man who has set "
            "down a heavy load at the right door. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b12", "out": "s12-he-gave-up-everything-he.jpeg", "seg": "n7",
        "window": "62.09-69.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "PEARL"],
        "narration": (
            "He gave up everything he had, gladly, because what he was getting "
            "was worth more than all of it put together."
        ),
        "must_show": "the possession — a close shot of the merchant seated on the bare courtyard step at evening, the one pearl in his two cupped hands, his old face wholly content.",
        "must_not_show": "no halo, glare or rim-light; contentment, not triumph — a lifetime settled.",
        "scene": (
            "In warm evening light the merchant sits on the bare stone "
            "step of his emptied house, elbows on his knees, the one "
            "great silver-white pearl cradled in his two cupped hands "
            "just below his gaze — and his lined face above it is "
            "settled into a contentment so complete it looks like rest "
            "after a long journey. The bare courtyard behind him has "
            "gone soft and gold. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r029-b13", "out": "s13-that-is-what-finding-the.jpeg", "seg": "n8",
        "window": "69.72-77.64", "wide": True, "jesus": False, "ref": False,
        "locks": ["MERCHANT", "MARKET-ROADS", "PEARL"],
        "narration": (
            "That is what finding the real thing does. When you finally find "
            "what your whole life was looking for, letting go of the rest is "
            "not a loss."
        ),
        "must_show": "the whole trade in one look back — the merchant walking away down the harbour quay at evening with nothing but the staff in his hand and the pearl-bag at his chest, unburdened and light.",
        "must_not_show": "no halo, glare or rim-light; he carries almost NOTHING — the lightness of his figure against the laden porters around him is the picture.",
        "scene": (
            "Along the harbour quay in soft evening light the merchant "
            "walks away from the moored trading boats carrying nothing "
            "but his staff and the small cloth bag resting at his chest, "
            "his step long and light — while around him porters bend "
            "under bales and merchants haggle over stacked goods, every "
            "other figure on the quay loaded down except him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b14", "out": "s14-it-is-the-easiest-trade.jpeg", "seg": "n8",
        "window": "77.64-80.68", "wide": False, "jesus": False, "ref": False,
        "locks": ["MERCHANT"],
        "narration": "It is the easiest trade you will ever make.",
        "must_show": "a close portrait of the merchant's face — the deep ease of a man who regrets nothing; the smile mostly in the eyes.",
        "must_not_show": "no halo, glare or rim-light; quiet ease, not laughter — the smile lives mostly in the eyes.",
        "scene": (
            "A close portrait of the merchant's spare, lined face in the "
            "warm evening light, the neat silver-grey beard and the calm "
            "dark eyes — and in those eyes, more than on the faintly "
            "curved mouth, the deep unhurried ease of a man who has "
            "weighed his whole life against one thing and knows past all "
            "argument that he chose well. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r029-b15", "out": "s15-and-there-is-one-more.jpeg", "seg": "n9",
        "window": "81.24-87.76", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": (
            "And there is one more wonder hidden in this little story. Some "
            "have read it the other way around, and it is just as true."
        ),
        "must_show": "back in the house — Jesus pausing at the story's turn, the disciples' faces caught leaning in for it, the room very still.",
        "must_not_show": "no halo, glare or rim-light on Jesus; a held-breath pause — stillness, attention, nothing moving.",
        "scene": (
            "The warm stone room has gone very still: Jesus sits with "
            "both hands at rest, holding the pause at the turn of the "
            "story, his face quiet with something kept back a moment "
            "longer — and around him the disciples have all leaned in "
            "without knowing it, one with a question dying on his lips, "
            "the window light lying long and low across the mats between "
            "them. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b16", "out": "s16-that-to-jesus-you-are.jpeg", "seg": "n9",
        "window": "87.76-90.62", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PEARL"],
        "narration": "That to Jesus, you are the pearl.",
        "must_show": "the reversal made visible — a close shot of the one great pearl cradled in Jesus's two cupped hands, held the way something beloved is held.",
        "must_not_show": "no halo, glare or rim-light on Jesus; only his hands and cream sleeves in frame with the pearl — tenderness in the hold, no drama.",
        "scene": (
            "A close shot filled by two cupped hands in plain cream wool "
            "sleeves — Jesus's hands, work-worn and gentle — holding the "
            "one great silver-white pearl in the hollow of the palms the "
            "way a man holds water he will not spill, thumbs resting "
            "lightly at its sides. Warm window light falls over hands "
            "and pearl against a soft dark ground. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r029-b17", "out": "s17-that-he-is-the-merchant.jpeg", "seg": "n10",
        "window": "91.23-99.48", "wide": True, "jesus": True, "ref": REF,
        "locks": ["HOUSE-ROOM"],
        "narration": (
            "That he is the merchant who went looking, who found you, and who "
            "gave up everything he had, his own life, gladly, to buy you back."
        ),
        "must_show": "Jesus saying it to THEM — leaning forward into the circle, his open hand extended palm-up toward the listeners, the cost and the gladness together in his face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; tender gravity, no theatrics — the extended open hand is the whole gesture.",
        "scene": (
            "Jesus leans forward from his cushion into the circle of "
            "disciples, one open hand extended palm-up toward them "
            "across the window light, his face carrying grief and "
            "gladness in the same look — the look of a merchant naming "
            "a price he has already decided to pay. The disciples' "
            "faces around him have gone from listening to being looked "
            "at, and they know it. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r029-b18", "out": "s18-that-is-how-good-he.jpeg", "seg": "n10",
        "window": "99.48-103.54", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PEARL"],
        "narration": "That is how good he is. You were worth all of it to him.",
        "must_show": "the closing image — the pearl held close against the cream wool at Jesus's chest, one hand curved around it; kept, treasured, home.",
        "must_not_show": "no halo, glare or rim-light on Jesus; frame is chest, hand and pearl only — intimacy, not spectacle.",
        "scene": (
            "A close still frame: against the plain cream wool of "
            "Jesus's chest, one of his hands curves around the great "
            "silver-white pearl, holding it close over his heart the "
            "way a man carries the one thing he crossed the world for "
            "— fingers gentle, grip sure. The warm light of the room "
            "rests on hand, wool and pearl. Every figure has two arms, "
            "two hands and one head."
        ),
    },
]
