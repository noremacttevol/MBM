#!/usr/bin/env python3
"""V2 beat map — row 45, build-45-wicked-tenants (Mark 12:1-12).

COVERAGE: 54 pictures over 305.0 s = 5.6 s/picture (matches the library density).

SCRIPTURE FACTS (Mark 12:1-12 KJV):
  Context: the temple, last week, told straight at the plotting chief
  priests (Mark 11:27, 12:12) — the frame beats stage Jesus SEATED beneath
  a temple portico with listeners around and the hunters at the circle's
  edge; a different temple composition from row 43's front-facing court.
  v1    "planted a vineyard, and set an HEDGE about it, and digged a place
        for the WINEFAT, and built a TOWER, and let it out to husbandmen,
        and went into a far country" — the owner's investment is itemized
        and painted: wall, press, tower, young vines, trust, departure.
  v2-5  the sendings: servant after servant, season after season —
        ⚑ Flag R (CONTENT-CARE §3 row 45): ALL violence OFF-SCREEN. What
        is painted: the sendings (one messenger, an empty basket, an open
        road), the shut gate, and the AFTERMATH restrained (a returned
        man, shaken, basket empty; a cloth-bound brow; an empty road where
        one did not come back). Never a blow, never blood, never a body.
        'The pattern of sent prophets is the point' — the repetition of
        the road is the row's visual spine.
  v6    "having yet therefore ONE SON, his WELLBELOVED ... They will
        reverence my son" — the father's hope spoken aloud; the son
        resembles him; the sending of the son is the row's heaviest beat
        and it is all tenderness, no dread-theatrics.
  v7-8  the murder — ENTIRELY OFF-SCREEN: the son walking up the road;
        the tenants watching from the tower; the gate shut; then the
        father receiving the news with the light gone out of him.
  v9    "he will come and destroy the husbandmen, and will give the
        vineyard unto others" — the destruction NOT depicted (off-screen
        rule); what is painted is the vineyard passing to NEW hands that
        tend it and bring the fruit back.
  v10-11 "the STONE which the builders REJECTED is become the HEAD OF THE
        CORNER" — a masons' yard image: the cast-off block raised into
        the corner's place.
  vNARR the closing mercy: 'the owner NEVER STOPPED SENDING' — the last
        beats return to the road with one more figure on it.

TIME OF DAY: temple frame is bright day. The vineyard planting is spring
morning; the sendings run SEASON AFTER SEASON — successive harvests in
successive autumn lights (the repetition across different years is the
point); the son's road is a still grey morning; the news reaches the
father at dusk; the new-tenants beats are clean spring again; the
cornerstone is masons'-yard daylight.

CHANGING CONDITION (kept OUT of the locks): the vineyard's seasons and
the tenants' hardening — wary, then insolent, then cold — move per-beat.
Each sent servant is a DIFFERENT man; only owner, son and tenants lock.
"""

# LOCKS: one entry per recurring person and per setting. Setting locks must
# NEVER name a character. Clothing colours stated POSITIVELY and dark — only
# Jesus wears cream.
LOCKS = {
    "OWNER": (
        "OWNER LOCK: the vineyard's planter is the same man in every shot "
        "— about sixty, tall and straight-backed, with a long grey-white "
        "beard, deep patient eyes and big planter's hands. He wears a "
        "DEEP FOREST-GREEN robe over a DARK EARTH-BROWN under-tunic with "
        "a plain leather belt (never cream, never white). His face is "
        "shown clearly — hope is its habit; grief will visit it."
    ),
    "SON": (
        "SON LOCK: the beloved son is the same young man in every shot — "
        "about twenty-five, with his father's straight back and deep "
        "eyes, a short dark beard and an open unguarded face. He wears a "
        "DARK OLIVE-GREEN robe of his father's cut with a DARK BROWN "
        "sash (never cream, never white). His face is shown clearly — "
        "the family resemblance to the owner must read at a glance."
    ),
    "TENANTS": (
        "TENANTS LOCK: the husbandmen are the same four men in every "
        "shot — a heavy black-bearded leader with flat calculating eyes; "
        "a lean older man with a grey-streaked beard and a twisted "
        "mouth; and two broad silent brothers with close-cropped dark "
        "hair. They wear work-stained tunics in DARK IRON-GREY, DEEP "
        "RUST, DARK UMBER and CHARCOAL-BROWN with rope belts (never "
        "cream, never white). Faces shown clearly — hard men, not "
        "monsters."
    ),
    "VINEYARD": (
        "VINEYARD LOCK: the planted vineyard — terraced vine rows inside "
        "a chest-high dry-stone wall with ONE arched wooden gate to the "
        "road, a rock-hewn winepress in the near corner, and a squat "
        "stone watchtower by the gate. The same wall, gate, press and "
        "tower in every vineyard beat, whatever the season."
    ),
    "ROAD": (
        "APPROACH ROAD LOCK: the road to the vineyard — a pale dirt road "
        "climbing the slope between low field walls to the vineyard's "
        "arched gate, one bent old carob tree at its halfway turn. The "
        "same road, walls and tree in every sending beat."
    ),
    "PORTICO": (
        "TEMPLE PORTICO LOCK: a shaded temple portico — great pale "
        "columns, a stone bench platform where a teacher sits, listeners "
        "gathered on the steps below in SATURATED DEEP earth colours, "
        "and at the crowd's edge a knot of hostile fine-robed men in "
        "NEAR-BLACK INDIGO and DARK UMBER with fringed shawls (never "
        "cream, never white; only Jesus wears cream). Faces shown "
        "clearly."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r045-b01", "out": "s01-and-he-began-to-speak.jpeg", "seg": "s1",
        "window": "0.28-2.97", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": "And he began to speak unto them by parables.",
        "must_show": "the frame — Jesus seated on the portico's stone bench, listeners banked on the steps, the hostile knot at the edge; a story opening under columns.",
        "must_not_show": "no halo, glare or rim-light on Jesus; seated teaching — a different temple geometry from any earlier row.",
        "scene": (
            "In the portico's striped shade Jesus sits on the "
            "stone bench platform with the listeners banked "
            "down the steps below him — a stonemason still "
            "dusted from work, two women with market baskets, "
            "an old Levite leaning on his staff — and at the "
            "crowd's far edge, half in the column's shadow, "
            "the knot of fine-robed men stands very still, "
            "listening the way debt collectors listen. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b02", "out": "s02-he-told-this-one-in.jpeg", "seg": "n1",
        "window": "4.53-9.13", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": (
            "He told this one in the temple, standing in front of the very men "
            "who were plotting against him."
        ),
        "must_show": "the courage of it — Jesus's steady profile and, past it, the plotters' shadowed faces; the teller and his hunters in one close frame.",
        "must_not_show": "no halo, glare or rim-light on Jesus; his steadiness against their watchfulness — no fear anywhere in his lines.",
        "scene": (
            "Close along the bench: Jesus's steady profile in "
            "the warm portico light, mid-word, utterly "
            "unhurried — and past his shoulder, deep in the "
            "column shadow at the crowd's edge, the hunters' "
            "faces hang half-lit and attentive, one leaning to "
            "murmur behind a ringed hand — a man telling a "
            "story about murdered messengers to the men "
            "pricing his own arrest. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b03", "out": "s03-about-an-owner-who-kept.jpeg", "seg": "n1",
        "window": "12.36-18.74", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": (
            "About an owner who kept giving people one more chance, long past "
            "the point anyone else would have."
        ),
        "must_show": "the protagonist named — a close portrait of the owner: patience as a face; hope worn like weather-lines.",
        "must_not_show": "no halo, glare or rim-light; the patience must look LIVED — a man whose habit of hoping shows.",
        "scene": (
            "A close portrait in warm light: the tall owner's "
            "face — the long grey-white beard, the deep steady "
            "eyes with their fans of hope-worn lines, a mouth "
            "that has said 'once more' so many times the shape "
            "of it stays — the face of a man whose patience is "
            "not softness but a chosen, repeated, expensive "
            "act. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b04", "out": "s04-then-he-handed-the-whole.jpeg", "seg": "n2",
        "window": "44.81-48.48", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "TENANTS", "VINEYARD"],
        "narration": (
            "Then he handed the whole place to the workers and trusted them "
            "with it."
        ),
        "must_show": "SCRIPTURE-EXACT: the letting out — the owner placing the vineyard gate's iron key into the tenant leader's hands at the arched gate; total trust changing hands.",
        "must_not_show": "no halo, glare or rim-light; the key given freely — no suspicion in the owner; the tenants' faces neutral, not yet dark.",
        "scene": (
            "At the vineyard's arched wooden gate in the clear "
            "spring light the owner lays the heavy iron gate-"
            "key into the black-bearded leader's cupped hands, "
            "his own big hand closing the man's fingers over "
            "it in trust — the three other tenants ranged "
            "watchful behind their leader, the young vines "
            "running green up the terraces beyond the wall — "
            "a whole living handed over on one key. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b05", "out": "s05-a-certain-man-planted-a.jpeg", "seg": "jv1",
        "window": "19.24-30.66", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "VINEYARD"],
        "narration": (
            "A certain man planted a vineyard, and set an hedge about it, and "
            "digged a place for the winefat, and built a tower, and let it out "
            "to husbandmen, and went into a far country."
        ),
        "must_show": "SCRIPTURE-EXACT: the investment itemized — the owner at work on his hillside: vines set, the wall rising, the press being hewn, the tower half-built; all four works visible in one industrious frame.",
        "must_not_show": "no halo, glare or rim-light; the owner works WITH his own hands — planter, not financier.",
        "scene": (
            "Across the spring hillside the vineyard is being "
            "born in one frame: the owner himself on his "
            "knees setting a young vine with both hands, the "
            "dry-stone wall rising course by course behind "
            "him under a labourer's hands, a mason chiselling "
            "the winepress out of the living rock in the near "
            "corner, and the squat watchtower standing half-"
            "built by the gate with its scaffold poles bare — "
            "one man's whole heart going into a hillside. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b06", "out": "s06-picture-how-much-he-put.jpeg", "seg": "n2",
        "window": "32.23-34.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER", "VINEYARD"],
        "narration": "Picture how much he put into it.",
        "must_show": "the cost personal — close on the owner's earth-black hands pressing soil around a young vine's root; investment counted in fingernails.",
        "must_not_show": "no halo, glare or rim-light; his OWN hands in the dirt — the vineyard as an act of love before it is an asset.",
        "scene": (
            "Close at the terrace's edge: the owner's big "
            "hands, earth-black to the wrist, pressing the "
            "soil firm around a young vine's slender stem with "
            "the two-thumbed tenderness of a man planting "
            "something he intends to love for thirty years — "
            "the grey-white beard hanging into the frame, the "
            "morning light on the worked ground. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b07", "out": "s07-he-broke-the-ground-and.jpeg", "seg": "n2",
        "window": "34.11-42.91", "wide": True, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "He broke the ground and set in the young vines, ringed it with a "
            "wall to guard them, hollowed out a press for the grapes, and "
            "raised a lookout tower over the whole thing."
        ),
        "must_show": "the finished works — the completed vineyard in golden evening: wall whole, press hewn and clean, tower capped, young vines in their rows; everything ready for years of fruit.",
        "must_not_show": "no halo, glare or rim-light; completion's pride — a hillside turned into a promise.",
        "scene": (
            "In the golden end of the working season the "
            "vineyard stands complete: the chest-high wall "
            "ringing the terraces unbroken to the arched "
            "gate, the rock-hewn press clean and waiting in "
            "its corner, the squat tower capped and whole "
            "above the gate, and the young vines standing "
            "their first full rows up the slope — a promise "
            "built in stone and rootstock, ready for its "
            "years. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r045-b08", "out": "s08-everything-was-ready.jpeg", "seg": "n2",
        "window": "42.91-44.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "Everything was ready.",
        "must_show": "readiness distilled — a close still: the winepress's clean-hewn basin, the first vine's tendril curling at frame's edge, the tower's shadow across both.",
        "must_not_show": "no halo, glare or rim-light; a quiet inventory frame — stone, vine, shadow, patience.",
        "scene": (
            "A quiet close still in the evening light: the "
            "winepress's fresh-hewn basin curving pale and "
            "clean out of the living rock, one young vine's "
            "first green tendril curling into the frame's "
            "corner above it, and across both, laid long by "
            "the low sun, the watchtower's steady shadow — "
            "everything a harvest needs, waiting on nothing "
            "but seasons. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r045-b09", "out": "s09-and-he-left.jpeg", "seg": "n3",
        "window": "48.98-49.78", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "ROAD", "VINEYARD"],
        "narration": "And he left.",
        "must_show": "SCRIPTURE-EXACT: the departure — the owner walking away down the pale road past the carob tree, the vineyard whole behind him; trust walking out of sight of its object.",
        "must_not_show": "no halo, glare or rim-light; no backward glance — the completeness of the trust in the set of his back.",
        "scene": (
            "Down the pale dirt road the owner walks away in "
            "the early light, staff in hand, travel bundle on "
            "his shoulder, passing the bent old carob tree at "
            "the halfway turn without a backward look — and "
            "above him on the slope the finished vineyard "
            "stands whole inside its wall, gate shut, tower "
            "watching, given entirely into other hands. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b10", "out": "s10-the-owner-is-far-away.jpeg", "seg": "n3",
        "window": "51.26-61.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["TENANTS", "VINEYARD"],
        "narration": (
            "The owner is far away, the workers have the run of the place, and "
            "all he asked for was a share of the harvest when it came in, the "
            "way any honest lease works."
        ),
        "must_show": "the arrangement running — the tenants working the maturing vineyard through a good season: pruning, tying, treading room swept; the lease honest-looking from outside.",
        "must_not_show": "no halo, glare or rim-light; the work REAL — these are able men; their competence makes their choice worse.",
        "scene": (
            "Through a ripening summer the four tenants work "
            "the vineyard with real skill — the leader tying "
            "canes along the terrace wire, the lean older man "
            "pruning with quick sure cuts, the two silent "
            "brothers hauling water up the terraces — the "
            "vines heavy-leafed and coming into their "
            "strength around them, a lease being worked "
            "exactly as leases should be, for now. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b11", "out": "s11-he-had-one-person-left.jpeg", "seg": "n8",
        "window": "163.19-164.81", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER", "SON"],
        "narration": "He had one person left.",
        "must_show": "the last card — the owner's hand resting on his grown son's shoulder in the far-country house; the one remaining sending, standing beside him.",
        "must_not_show": "no halo, glare or rim-light; the family resemblance visible — the father touching everything he has left.",
        "scene": (
            "In the far-country house's lamplight the old "
            "owner's big hand rests on the shoulder of his "
            "grown son standing beside him — the same "
            "straight back, the same deep eyes one generation "
            "younger, the short dark beard where the "
            "grey-white one will someday be — a father "
            "standing beside the whole remainder of his "
            "hope, and the hand on the shoulder already half "
            "a blessing. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r045-b12", "out": "s12-and-at-the-season-he.jpeg", "seg": "jv2",
        "window": "62.04-69.47", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "VINEYARD"],
        "narration": (
            "And at the season he sent to the husbandmen a servant, that he "
            "might receive from the husbandmen of the fruit of the vineyard."
        ),
        "must_show": "SCRIPTURE-EXACT: the first sending — a single servant climbing the road to the gate at harvest, empty basket on his arm, the vines heavy beyond the wall.",
        "must_not_show": "no halo, glare or rim-light; one man, one basket, one honest errand — the road's first innocent use.",
        "scene": (
            "Up the pale road in the first autumn's golden "
            "light a single servant climbs toward the arched "
            "gate with an empty harvest basket swinging on "
            "his arm and no more caution in his stride than "
            "a man collecting rent from neighbours — beyond "
            "the wall the vine rows hang purple-heavy with "
            "their first real crop, and the tower stands "
            "quiet over the gate he is about to knock on. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b13", "out": "s13-so-when-the-season-came.jpeg", "seg": "n4",
        "window": "70.96-74.58", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": "So when the season came, he sent a man to collect his share.",
        "must_show": "the sending's other end — the owner in the far country pressing the errand and a farewell into the servant's hands; ordinary business, warmly done.",
        "must_not_show": "no halo, glare or rim-light; the owner's ease — no premonition; a fair man expecting fairness.",
        "scene": (
            "In the far-country courtyard the owner clasps "
            "the departing servant's hand between both of "
            "his, giving the errand its farewell — a wax-"
            "sealed note tucked in the man's belt, bread for "
            "the road in his satchel, the owner's deep eyes "
            "easy and unclouded — a fair man sending for his "
            "fair share with no more ceremony than the "
            "season requires. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r045-b14", "out": "s14-not-soldiers.jpeg", "seg": "n4",
        "window": "74.58-76.15", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": "Not soldiers.",
        "must_show": "the choice of gentleness — a close still: the servant's walking staff and empty basket leaned by a door, beside them NO sword, NO spear; the armament of trust.",
        "must_not_show": "no halo, glare or rim-light; the absence is the subject — travelling gear without one edge of iron.",
        "scene": (
            "A close still by the courtyard door in morning "
            "light: a plain walking staff leaned against the "
            "stone, an empty woven harvest basket at its "
            "foot, a water-skin and a bread satchel on the "
            "bench — the complete equipment of the errand, "
            "and nowhere in it a blade, a spear-haft, or one "
            "ounce of iron meant for men — trust, packed for "
            "travel. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r045-b15", "out": "s15-one-messenger-walking-up-the.jpeg", "seg": "n4",
        "window": "76.15-83.22", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "TENANTS", "VINEYARD"],
        "narration": (
            "One messenger, walking up the road with an empty basket, expecting "
            "nothing but an honest exchange."
        ),
        "must_show": "the innocence and the watchers — the servant nearing the gate, and above him on the tower platform two tenants watching his approach with unreadable stillness.",
        "must_not_show": "no halo, glare or rim-light; menace ONLY as stillness — the watchers unmoving; nothing yet done.",
        "scene": (
            "The servant is nearly at the arched gate now, "
            "basket swinging, one hand already lifting to "
            "knock — and above him on the watchtower's "
            "platform the two silent brothers stand looking "
            "down at his approach without moving, without "
            "calling a greeting, without any of the small "
            "motions welcome makes — stillness where a wave "
            "should be, in the golden harvest light. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b16", "out": "s16-and-they-caught-him-and.jpeg", "seg": "jv3",
        "window": "83.77-86.84", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "VINEYARD"],
        "narration": "And they caught him, and beat him, and sent him away empty.",
        "must_show": "⚑ Flag R OFF-SCREEN: the aftermath ONLY — the gate shut, and the servant already down the road walking away unsteadily, basket gone, one hand pressed to his side; the violence entirely behind the wall and behind the moment.",
        "must_not_show": "no halo, glare or rim-light; NO blow shown, NO blood — the shut gate and the unsteady walk carry everything.",
        "scene": (
            "The arched gate stands shut in the harvest light "
            "— and halfway down the pale road the servant is "
            "already walking away from it, unsteadily, one "
            "hand pressed flat to his ribs and the other "
            "empty of the basket he carried up, his steps "
            "finding the road's edge and correcting — the "
            "whole event over, unseen, sealed behind stone, "
            "readable only in how a man walks. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b17", "out": "s17-they-had-handled-him-roughly.jpeg", "seg": "n5",
        "window": "92.28-95.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": "They had handled him roughly and sent him off with nothing.",
        "must_show": "the news received — the owner hearing it in his far-country room, his hand stopped mid-motion over his work; the first crack in the arrangement reaching him.",
        "must_not_show": "no halo, glare or rim-light; stillness as shock — a patient man's face doing its first recalculation.",
        "scene": (
            "In the far-country room the owner has stopped "
            "mid-motion — a ledger reed still in his lifted "
            "hand, his deep eyes fixed on the shaken servant "
            "standing before him with his side still braced "
            "and his hands still empty — the patient old face "
            "working slowly through a fact it has no drawer "
            "for, while the reed hangs unmoving over the "
            "page. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r045-b18", "out": "s18-now-here-is-where-the.jpeg", "seg": "n5",
        "window": "95.37-102.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": (
            "Now here is where the story stops making ordinary sense. Anyone "
            "else sends the law next."
        ),
        "must_show": "the fork refused — the owner at his table with a magistrate's writ half-written before him, setting the reed DOWN and pushing the page away.",
        "must_not_show": "no halo, glare or rim-light; the pushed-away writ is the whole beat — force declined in one motion.",
        "scene": (
            "At the lamplit table the sensible response lies "
            "half-written — a formal writ begun in a careful "
            "hand, the magistrate's seal-wax already warming "
            "at the lamp — and the owner sets the reed down "
            "beside it and pushes the page slowly to arm's "
            "length, his other hand rubbing his beard, his "
            "eyes gone past the lamp toward the window and "
            "the road and some other kind of answer. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b19", "out": "s19-this-owner-sent-another-messenger.jpeg", "seg": "n5",
        "window": "102.24-104.61", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "VINEYARD"],
        "narration": "This owner sent another messenger.",
        "must_show": "the road again — a SECOND, different servant climbing the same road past the carob tree toward the same gate; the pattern's second stroke.",
        "must_not_show": "no halo, glare or rim-light; the same road composition repeated deliberately — repetition as theology.",
        "scene": (
            "The pale road again, another autumn's light: a "
            "second servant — older, greyer, steadier than "
            "the first — climbs past the bent carob tree "
            "toward the arched gate with a fresh empty "
            "basket on his arm, walking the identical road "
            "the last man limped down, his eyes on the gate "
            "and his errand unchanged: the owner's share, "
            "asked for kindly, one more time. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b20", "out": "s20-and-again-he-sent-unto.jpeg", "seg": "jv4_5",
        "window": "105.18-114.16", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": (
            "And again he sent unto them another servant; and at him they cast "
            "stones, and wounded him in the head, and sent him away shamefully "
            "handled."
        ),
        "must_show": "⚑ Flag R OFF-SCREEN: aftermath only — the second servant resting at the carob tree's foot on his way down, a cloth bound around his brow, being given water by a passing traveller; no wound detail, no blood.",
        "must_not_show": "no halo, glare or rim-light; the bound brow CLEAN cloth, no red — mercy of strangers in the frame instead of violence.",
        "scene": (
            "At the carob tree's shaded foot the grey servant "
            "sits resting against the trunk, a plain cloth "
            "bound neat around his brow and his emptied "
            "basket beside him — while a passing traveller "
            "kneels to hold a water-skin to his lips, one "
            "hand steadying the older man's shoulder — the "
            "road's kindness tending what the vineyard's "
            "hardness did, out of sight, behind them both. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b21", "out": "s21-and-again-he-sent-another.jpeg", "seg": "jv4_5",
        "window": "114.16-121.90", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD", "VINEYARD"],
        "narration": (
            "And again he sent another; and him they killed, and many others; "
            "beating some, and killing some."
        ),
        "must_show": "⚑ Flag R OFF-SCREEN at its strictest: the road EMPTY at dusk — no returning figure on its whole length; the gate shut; one dropped walking staff lying at the roadside. Absence as the report.",
        "must_not_show": "no halo, glare or rim-light; NOTHING depicted — no body, no act, no mourners; the empty road and the dropped staff say what the verse says.",
        "scene": (
            "Dusk on the pale road, and the road is empty: "
            "its whole climbing length lies bare from the "
            "field walls to the shut arched gate, no figure "
            "returning on it and none to come — and at the "
            "verge by the carob tree's turn, a plain walking "
            "staff lies dropped and unclaimed in the dust, "
            "with the first stars coming out over the quiet, "
            "fruitful, terrible hillside. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b22", "out": "s22-and-they-treated-that-one.jpeg", "seg": "n6",
        "window": "123.42-125.24", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": "And they treated that one worse.",
        "must_show": "grief accumulating — the owner's face by lamplight, older by every message; a hand covering his eyes.",
        "must_not_show": "no halo, glare or rim-light; the toll on the SENDER — each report ageing him; grief without spectacle.",
        "scene": (
            "By the low lamp the owner sits with one big "
            "planter's hand covering his eyes, the fingers "
            "pressing at the brow, his grey-white beard "
            "trembling once and stilling — the face beneath "
            "the hand older than the season should have made "
            "it, a man absorbing report after report through "
            "a heart that keeps refusing to close the road. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b23", "out": "s23-and-another-after-that.jpeg", "seg": "n6",
        "window": "125.24-126.99", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": "And another after that.",
        "must_show": "the pattern relentless — yet another servant on the same road in yet another season's light: winter-grey this time, cloak drawn, walking up anyway.",
        "must_not_show": "no halo, glare or rim-light; the same framing a third time — the repetition unmistakable and deliberate.",
        "scene": (
            "The same pale road under a grey winter sky: a "
            "third servant climbs past the bare-branched "
            "carob tree with his cloak drawn tight and an "
            "empty basket on his arm, head down into the "
            "cold wind, walking a road whose stories he has "
            "certainly heard — up anyway, toward the shut "
            "gate, because the man who sent him has not "
            "stopped sending. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r045-b24", "out": "s24-message-after-message-season-after.jpeg", "seg": "n6",
        "window": "126.99-134.90", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": (
            "Message after message, season after season, and every time it came "
            "back the same, or did not come back at all."
        ),
        "must_show": "the ledger of sendings — a close still: the owner's table with a row of returned, unopened reply-scrolls and empty spaces where replies never came; years of asking, in objects.",
        "must_not_show": "no halo, glare or rim-light; the gaps in the row speak — some scrolls returned sealed, some places simply empty.",
        "scene": (
            "A close still on the owner's lamplit table: a "
            "long row of small message scrolls laid in order "
            "of their seasons — the first few returned "
            "crumpled and unanswered, the next ones returned "
            "still sealed, and then, down the row's end, "
            "empty spaces on the wood where nothing came "
            "back at all — years of patience filed in a line "
            "that keeps ending in bare table. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b25", "out": "s25-stop-and-feel-how-strange.jpeg", "seg": "n7",
        "window": "135.43-141.25", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": (
            "Stop and feel how strange that is. Every reasonable line was "
            "crossed a long time ago."
        ),
        "must_show": "the teller flags it — Jesus in the portico with one hand lifted, stopping his own story; the listeners caught mid-lean.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the pause deliberate — the story's strangeness held up for inspection.",
        "scene": (
            "On the portico bench Jesus lifts one hand and "
            "stops his own story mid-stream — the listeners "
            "caught leaning, the stonemason's brows knotted "
            "over the arithmetic of it, the old Levite "
            "shaking his head slowly — a teller making his "
            "audience stand still in the strangest spot in "
            "the tale and feel how far past sense the "
            "owner's patience has already gone. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b26", "out": "s26-he-had-every-right-to.jpeg", "seg": "n7",
        "window": "141.25-147.99", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": (
            "He had every right to come with force and end it. Instead he kept "
            "doing the one thing that left him exposed."
        ),
        "must_show": "power declined again — the owner at his window at night, the far-country city's garrison torches visible below, his back turned to them, face toward the dark horizon where the vineyard lies.",
        "must_not_show": "no halo, glare or rim-light; the garrison AVAILABLE and unused — his back to force, his face to hope.",
        "scene": (
            "At the dark window the owner stands with his "
            "back to the room — and below in the far-country "
            "city the garrison's watch-torches burn in their "
            "orderly rows, force for the asking a street "
            "away — while his face is turned the other "
            "direction entirely, out over the black horizon "
            "toward the far land where his vineyard lies, "
            "choosing again the one road that has never "
            "protected him. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r045-b27", "out": "s27-he-kept-reaching-out-to.jpeg", "seg": "n7",
        "window": "147.99-152.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": (
            "He kept reaching out to people who had already shown him exactly "
            "who they were."
        ),
        "must_show": "the exposure chosen — close on the owner's open hand extended over the row of failed message scrolls, hovering above the next blank one; the reach that keeps reaching.",
        "must_not_show": "no halo, glare or rim-light; the hand OVER the evidence — knowledge and mercy in one gesture.",
        "scene": (
            "Close over the lamplit table: the owner's open "
            "hand extended above the long row of failed and "
            "unanswered scrolls, hovering, and then settling "
            "on a fresh blank one at the row's end — the "
            "whole history of what these men are lying in "
            "order beneath his palm, and his fingers closing "
            "anyway on the makings of one more message. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b28", "out": "s28-having-yet-therefore-one-son.jpeg", "seg": "jv6",
        "window": "153.23-161.64", "wide": True, "jesus": False, "ref": False,
        "locks": ["OWNER", "SON"],
        "narration": (
            "Having yet therefore one son, his wellbeloved, he sent him also "
            "last unto them, saying, They will reverence my son."
        ),
        "must_show": "SCRIPTURE-EXACT: the last sending — the father and son at the courtyard gate at first light, the father's hands on the young man's shoulders, the hope spoken; farewell painted whole.",
        "must_not_show": "no halo, glare or rim-light; tenderness without dread-theatrics — the father BELIEVES the words he says.",
        "scene": (
            "At the courtyard gate in the first grey-gold "
            "light the father holds his son by both "
            "shoulders at arm's length, the old deep eyes "
            "moving over the young face as the hope is said "
            "aloud — and the son, travel cloak on and his "
            "father's cut of robe about him, bears the look "
            "with the small embarrassed smile grown sons "
            "give their fathers' love — two straight backs, "
            "one farewell, all the remaining eggs of an old "
            "man's heart in one basket on one road. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b29", "out": "s29-the-trust-does-not-vanish.jpeg", "seg": "n11",
        "window": "248.04-250.01", "wide": True, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "The trust does not vanish.",
        "must_show": "trust's persistence — the vineyard in new spring light, gate standing OPEN, fresh workers' tools leaned ready at the wall; the arrangement itself alive and continuing.",
        "must_not_show": "no halo, glare or rim-light; the open gate against every shut-gate beat before it — continuity, not vengeance.",
        "scene": (
            "New spring light on the old terraces: the "
            "vineyard's arched gate stands propped fully "
            "open to the road, fresh pruning hooks and a "
            "water yoke leaned ready against the wall just "
            "inside, the young season's first green breaking "
            "on the vines — the whole arrangement of trust "
            "standing intact and continuing, its gate wider "
            "than it has been in years. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b30", "out": "s30-his-son-the-one-he.jpeg", "seg": "n8",
        "window": "164.81-168.11", "wide": False, "jesus": False, "ref": False,
        "locks": ["SON"],
        "narration": "His son. The one he loved most in the world.",
        "must_show": "the beloved introduced fully — a close portrait of the son: the father's face one generation younger, open and unguarded; what is being risked.",
        "must_not_show": "no halo, glare or rim-light; the resemblance the beat's whole content — love's face, sent.",
        "scene": (
            "A close portrait in the morning light: the "
            "son's young face — his father's deep steady "
            "eyes without the grief in them yet, his "
            "father's straight bearing worn easily, the "
            "short dark beard framing a mouth quick to "
            "warmth — an open, unguarded face built from "
            "loving and being loved, photographed the "
            "morning it was spent. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b31", "out": "s31-and-he-sent-him-too.jpeg", "seg": "n8",
        "window": "168.11-176.01", "wide": True, "jesus": False, "ref": False,
        "locks": ["SON", "ROAD", "VINEYARD"],
        "narration": (
            "And he sent him too, holding on to a hope you can hear him say out "
            "loud. Surely they will respect my son."
        ),
        "must_show": "the son on the road — the young man climbing the familiar pale road past the carob tree in still grey morning light, unarmed, unhurried, the gate ahead.",
        "must_not_show": "no halo, glare or rim-light; the same sending-composition a final time — the road's last and heaviest use; no dread effects, the stillness is enough.",
        "scene": (
            "In a windless grey morning the son climbs the "
            "pale road alone — past the bent carob tree, "
            "past the place where a staff once lay — his "
            "stride his father's stride, his hands empty and "
            "open, the arched gate waiting ahead under its "
            "silent tower — the same road, the same errand, "
            "carried now by everything an old man has left, "
            "in a light that holds perfectly still around "
            "him. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r045-b32", "out": "s32-but-those-husbandmen-said-among.jpeg", "seg": "jv7",
        "window": "176.57-184.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["TENANTS", "VINEYARD"],
        "narration": (
            "But those husbandmen said among themselves, This is the heir; "
            "come, let us kill him, and the inheritance shall be ours."
        ),
        "must_show": "SCRIPTURE-EXACT: the conspiracy — the four tenants clustered on the tower platform watching the son's approach below, heads bent together, the leader's flat eyes doing the arithmetic.",
        "must_not_show": "no halo, glare or rim-light; cold counsel only — no weapons brandished; the plot is a conversation and a shared look.",
        "scene": (
            "On the watchtower platform the four tenants "
            "cluster close, heads bent together over the "
            "parapet — below and beyond them the small "
            "figure of the son climbing the last of the road "
            "— and the black-bearded leader's flat eyes move "
            "from the young man to his fellows and back, "
            "the coldest arithmetic in the story passing "
            "between four faces without one raised voice or "
            "one drawn blade. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r045-b33", "out": "s33-and-underneath-it-it-is.jpeg", "seg": "n1",
        "window": "9.13-12.36", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": "And underneath it, it is a story about patience.",
        "must_show": "the key given early — close on Jesus's face as he names the story's true subject; gentleness beneath the hard tale's surface.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the word 'patience' resting visibly in his expression.",
        "scene": (
            "Close on Jesus in the portico shade: the hard "
            "story just begun, and his face already carrying "
            "its secret — the brows even, the warm eyes "
            "steady, the whole expression resting on some "
            "deeper floor than the tale's violence — a "
            "teller entrusting his listeners, in one look, "
            "with the word the story is actually about. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b34", "out": "s34-but-when-the-workers-saw.jpeg", "seg": "n9",
        "window": "185.88-191.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["TENANTS"],
        "narration": (
            "But when the workers saw the son coming up the road, they did not "
            "see a person. They saw an opening."
        ),
        "must_show": "the dehumanizing look — close on the leader's face at the parapet: a man being looked at as a vacancy; appetite disguised as calculation.",
        "must_not_show": "no halo, glare or rim-light; the horror all interior — a face erasing a person in real time.",
        "scene": (
            "Close on the black-bearded leader's face at the "
            "tower parapet: the flat calculating eyes fixed "
            "downward on the approaching young man, and "
            "nothing in them that sees a person at all — no "
            "recognition, no enmity even, only the cool "
            "measuring gaze men give a doorway they intend "
            "to walk through — a human face doing its "
            "coldest available work. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b35", "out": "s35-if-the-heir-is-gone.jpeg", "seg": "n9",
        "window": "191.59-196.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["TENANTS", "VINEYARD"],
        "narration": (
            "If the heir is gone, they said to each other, the whole place "
            "falls to us."
        ),
        "must_show": "the coveted whole — from the tower, the tenants' view: the entire fruitful vineyard spread below their platform; the thing worth a soul to them.",
        "must_not_show": "no halo, glare or rim-light; the vineyard beautiful — the prize's genuine loveliness indicts the price.",
        "scene": (
            "From the tower platform the tenants' view "
            "spreads below: the whole walled vineyard in its "
            "morning fullness — terrace after terrace of "
            "laden vines, the clean-hewn press, the "
            "well-kept rows their own hands tended — every "
            "stone and stem of another man's love lying "
            "spread out like a table, being repriced in "
            "silence by the four men looking down at it. "
            "Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r045-b36", "out": "s36-it-is-the-coldest-arithmetic.jpeg", "seg": "n9 + jv8",
        "window": "196.17-204.18", "wide": True, "jesus": False, "ref": False,
        "locks": ["SON", "TENANTS", "VINEYARD", "ROAD"],
        "narration": (
            "It is the coldest arithmetic in any story he ever told. And they "
            "took him, and killed him, and cast him out of the vineyard."
        ),
        "must_show": "⚑ Flag R OFF-SCREEN absolutely: the LAST SIGHT — the son reaching the gate as it opens to admit him, the tenants' shapes inside the shadow; the frame ends BEFORE anything happens.",
        "must_not_show": "no halo, glare or rim-light; NOTHING of the act — the opened gate swallowing the son's welcome is the final image; the verse's words carry all the rest.",
        "scene": (
            "At the top of the pale road the arched gate has "
            "swung open at the son's knock — and he steps "
            "toward the opening with his open unguarded "
            "face, one hand raised in greeting to the "
            "figures standing back in the gateway's shadow, "
            "the tower silent above — the last the road ever "
            "sees of him: a young man walking trustingly "
            "through a gate held open by men who have "
            "already finished their arithmetic. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b37", "out": "s37-you-can-guess-what-they.jpeg", "seg": "n10",
        "window": "205.69-210.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "You can guess what they chose. The story does not linger on it and "
            "neither will we."
        ),
        "must_show": "the not-lingering — the shut gate in flat grey light, nothing else; the narration's own restraint made visual.",
        "must_not_show": "no halo, glare or rim-light; the barest frame — gate, wall, grey sky; grief by omission.",
        "scene": (
            "The arched wooden gate stands shut in a flat "
            "grey noon, the dry-stone wall running away on "
            "either side, the tower above it empty-"
            "platformed, the road below bare — no figure, no "
            "sound implied, no detail offered — a picture "
            "declining, exactly as the words decline, to "
            "look any further than the closed planks. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b38", "out": "s38-they-shut-him-out-and.jpeg", "seg": "n10",
        "window": "210.35-213.17", "wide": False, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": "They shut him out, and they took his life.",
        "must_show": "⚑ Flag R: the trace only — outside the wall at the road's edge, the son's travel cloak lying folded-fallen in the verge grass; the fact, without the act.",
        "must_not_show": "no halo, glare or rim-light; NO body, no blood — one fallen garment in the grass carries the whole verse.",
        "scene": (
            "At the road's grassy verge below the vineyard "
            "wall, the son's dark olive travel cloak lies "
            "fallen in the long grass — half-folded by its "
            "own weight, one corner moving slightly in the "
            "wind, the pale road running on past it toward a "
            "horizon nobody is walking to — a garment where "
            "a man should be, in a frame that will not say "
            "more. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r045-b39", "out": "s39-and-the-father-who-had.jpeg", "seg": "n10",
        "window": "213.17-219.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": (
            "And the father who had waited all those years, still hoping, lost "
            "the one he loved most of all."
        ),
        "must_show": "the news arriving — the father at his door at dusk as a road-worn messenger stands before him unable to speak; the old man's hand finding the doorframe.",
        "must_not_show": "no halo, glare or rim-light; grief at its first instant — the hand on the frame taking the weight the legs give up.",
        "scene": (
            "At the far-country door in the failing dusk "
            "light a road-worn messenger stands before the "
            "old owner with his head down, hat crushed in "
            "his hands, the words not coming — and the "
            "father's face has already understood: the deep "
            "eyes gone still, the colour leaving, one big "
            "planter's hand moving out to find the doorframe "
            "and hold it as the whole long patience of his "
            "life arrives at its price. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b40", "out": "s40-that-is-how-far-the.jpeg", "seg": "n10",
        "window": "219.64-224.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": "That is how far the patience went, and what it finally cost him.",
        "must_show": "the cost summed — the father seated in the dark with his son's childhood keepsake (a small carved toy vine-knife) in his two hands; patience's final invoice.",
        "must_not_show": "no halo, glare or rim-light; one small object, two old hands, total loss — nothing more asked of the frame.",
        "scene": (
            "In the unlit room the old owner sits with a "
            "small keepsake in his two cupped hands — a "
            "child's first carved wooden vine-knife, its "
            "handle worn smooth by a small grip long "
            "outgrown — his grey head bowed over it in the "
            "last blue light from the window, holding "
            "twenty-five years in eight ounces of olive "
            "wood. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r045-b41", "out": "s41-what-shall-therefore-the-lord.jpeg", "seg": "jv9",
        "window": "224.67-232.98", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": (
            "What shall therefore the lord of the vineyard do? he will come and "
            "destroy the husbandmen, and will give the vineyard unto others."
        ),
        "must_show": "SCRIPTURE-EXACT, destruction OFF-SCREEN: the question put — Jesus asking it directly at the hostile knot, the whole portico waiting; the answer's weight in the silence, nothing depicted.",
        "must_not_show": "no halo, glare or rim-light on Jesus; NO destruction imagery anywhere — the question and the hunters' faces carry the verse.",
        "scene": (
            "In the portico Jesus puts the question straight "
            "across the crowd to the fine-robed knot at its "
            "edge — his hand open toward them, the sentence "
            "hanging — and the whole gathering has turned to "
            "look where he looks: the hunters standing very "
            "still in the column shadow, the answer to the "
            "question arriving in their own faces faster "
            "than anyone can speak it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b42", "out": "s42-then-he-turned-it-into.jpeg", "seg": "n11",
        "window": "234.50-236.08", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": "Then he turned it into a question.",
        "must_show": "the question's edge — close on Jesus's lifted open hand, palm up, offering the story's ending to its own audience to finish.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the open hand as a handed-over pen.",
        "scene": (
            "Close in the portico light: Jesus's open hand "
            "lifted palm-up toward his listeners, holding "
            "the story's unfinished ending out on it like "
            "bread — his face behind the hand patient and "
            "level, a teller requiring his audience to "
            "pronounce the verdict their own hearts have "
            "already drafted. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b43", "out": "s43-what-is-the-owner-going.jpeg", "seg": "n11",
        "window": "236.08-241.78", "wide": False, "jesus": False, "ref": False,
        "locks": ["PORTICO"],
        "narration": (
            "What is the owner going to do now? And the weight of the answer is "
            "not really the punishment."
        ),
        "must_show": "the audience answering inwardly — close along the listeners' faces on the steps: the verdict forming differently in each one; a court of ordinary hearts.",
        "must_not_show": "no halo, glare or rim-light; thought visible — no spoken answer, only faces mid-verdict.",
        "scene": (
            "Close along the portico steps: the listeners' "
            "faces mid-verdict — the stonemason's jaw set "
            "hard, the old Levite's eyes closed over some "
            "inward scripture, a young mother's face gone "
            "grave above her child — a jury of ordinary "
            "hearts each arriving separately at the same "
            "heavy place, in the quiet the question left "
            "behind. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r045-b44", "out": "s44-it-is-that-the-vineyard.jpeg", "seg": "n11",
        "window": "241.78-248.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "It is that the vineyard finally passes to people who will actually "
            "tend it and give its fruit back."
        ),
        "must_show": "the vineyard's future — NEW tenants at work in the old rows in clean spring light: a young family pruning and planting together, the gate open behind them.",
        "must_not_show": "no halo, glare or rim-light; renewal, not replacement-triumph — the vineyard loved again is the whole point.",
        "scene": (
            "In clean spring light new hands work the old "
            "terraces: a young husband pruning where the "
            "lean man once pruned, his wife tying canes with "
            "quick care, their small daughter carrying a "
            "watering jar two-handed up the row — the arched "
            "gate standing open behind them and the tower "
            "keeping its watch over people who look up at "
            "it without fear. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b45", "out": "s45-it-goes-to-hands-that.jpeg", "seg": "n11",
        "window": "250.01-255.49", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": (
            "It goes to hands that will keep it. And then he reached back into "
            "their own scriptures for the last word."
        ),
        "must_show": "keeping made visible — close on the new tenants' hands at the harvest: full baskets being carried OUT the gate toward the road; the fruit finally going back.",
        "must_not_show": "no halo, glare or rim-light; the baskets heading OUT — the lease honoured at last; the road's old grief answered by traffic of fruit.",
        "scene": (
            "At the open arched gate in golden harvest light "
            "the new tenants carry the owner's share OUT to "
            "the road at last — the young husband with a "
            "brimming basket on his shoulder, his wife "
            "steadying a second on the wall, purple clusters "
            "piled past the rims — fruit moving down the "
            "pale road in the direction messengers once "
            "walked up, the whole arrangement finally "
            "flowing the way it was built to. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b46", "out": "s46-that-is-the-setup.jpeg", "seg": "n3",
        "window": "49.78-51.26", "wide": False, "jesus": False, "ref": False,
        "locks": ["VINEYARD"],
        "narration": "That is the setup.",
        "must_show": "the stage set — a clean establishing still: the whole vineyard small and perfect on its hillside under a wide sky, the road threading up to its gate.",
        "must_not_show": "no halo, glare or rim-light; the story's board laid out — vineyard, wall, tower, road, in one calm frame.",
        "scene": (
            "A calm wide still under a great morning sky: "
            "the whole vineyard lying small and perfect on "
            "its hillside — the ringed wall, the capped "
            "tower, the terraced rows, the press's pale "
            "notch in the corner — and the one pale road "
            "threading up the slope to its arched gate: "
            "every piece of the story in its place, waiting "
            "for the seasons to begin moving them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b47", "out": "s47-and-have-ye-not-read.jpeg", "seg": "jv10",
        "window": "256.11-267.86", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "And have ye not read this scripture; The stone which the builders "
            "rejected is become the head of the corner: This was the Lord's "
            "doing, and it is marvellous in our eyes?"
        ),
        "must_show": "SCRIPTURE-EXACT: the cornerstone — a masons' yard: the once-rejected block being lowered by ropes into the corner's place of a rising wall, the reject pile behind it.",
        "must_not_show": "no halo, glare or rim-light; the block visibly the SAME stone from the reject pile — scarred, once-scorned, now load-bearing.",
        "scene": (
            "In a masons' yard in working daylight a great "
            "squared block swings on ropes as four builders "
            "lower it into the corner socket of a rising "
            "wall — the block's flank still bearing the old "
            "reject-mark and a chip healed with mortar — "
            "while behind the hoist the reject pile it came "
            "from lies in the weeds, one stone lighter — the "
            "thrown-away thing settling, under every eye in "
            "the yard, into the place the whole building "
            "will lean on. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r045-b48", "out": "s48-and-the-man-came-back.jpeg", "seg": "n5",
        "window": "88.40-92.28", "wide": False, "jesus": False, "ref": False,
        "locks": ["OWNER"],
        "narration": "And the man came back with the basket still empty, and shaken.",
        "must_show": "⚑ Flag R aftermath — the first servant arriving home: dusty, steadied by a housemate's arm, the flat empty basket telling the far-country household everything.",
        "must_not_show": "no halo, glare or rim-light; shaken, not broken — the empty basket at the frame's centre.",
        "scene": (
            "In the far-country courtyard the first servant "
            "arrives home in the evening light — dust-grey, "
            "one arm steadied by a housemate who has come "
            "running, his face older by a season — and "
            "hanging flat and empty from his other hand, "
            "the harvest basket that left here full of "
            "nothing but trust, returning with less. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b49", "out": "s49-the-block-the-builders-threw.jpeg", "seg": "n12",
        "window": "269.38-277.02", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": (
            "The block the builders threw on the reject pile turned out to be "
            "the one the whole building leans its weight on. He is talking "
            "about himself."
        ),
        "must_show": "the self-identification — close on Jesus as the psalm's meaning lands on his own face: the rejected one naming himself cornerstone, quietly, among his rejecters.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the courage quiet — a man reading his own future aloud without flinching.",
        "scene": (
            "Close on Jesus in the portico shade: the psalm "
            "still on his lips and its whole meaning arrived "
            "in his face — the warm eyes steady, something "
            "both grave and utterly unafraid settling "
            "through the features — a man standing in a "
            "builders' yard of a city, naming himself the "
            "stone on the pile, and the corner, in one "
            "breath. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r045-b50", "out": "s50-the-son-they-were-ready.jpeg", "seg": "n12",
        "window": "277.02-282.23", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "The son they were ready to throw out is the foundation everything "
            "else gets built on."
        ),
        "must_show": "the metaphor sealed — the finished corner: the once-rejected stone bearing the risen wall's full weight, courses climbing true above it.",
        "must_not_show": "no halo, glare or rim-light; the wall RISEN — load visibly carried; the reject-mark still faintly readable on the bearing stone.",
        "scene": (
            "At the building's finished corner the "
            "once-rejected block sits bedded under the full "
            "weight of the risen wall — course after true "
            "course climbing away above it into the light, "
            "the whole structure's lines gathering down "
            "into that one scarred stone — and on its "
            "exposed flank, half-weathered now, the old "
            "reject-mark still faintly legible under the "
            "load it carries. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b51", "out": "s51-they-meant-it-for-an.jpeg", "seg": "n12",
        "window": "282.23-285.68", "wide": True, "jesus": False, "ref": False,
        "locks": [],
        "narration": "They meant it for an ending. It was the beginning.",
        "must_show": "the reversal wide — the whole new building rising busy and alive on its corner in morning light: scaffolds, workers, life; everything built on what was thrown away.",
        "must_not_show": "no halo, glare or rim-light; the building ALIVE with work — an ending repurposed as a foundation, at full construction pace.",
        "scene": (
            "In bright working morning the whole building "
            "rises alive on its corner — scaffold poles "
            "walking up the walls, masons calling measures, "
            "a boy hauling the water bucket, mortar smoking "
            "in its trough — course on course of busy "
            "future standing on the one stone its builders "
            "once carried to the weeds, the yard's whole "
            "noise a kind of applause. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b52", "out": "s52-the-men-he-told-it.jpeg", "seg": "n13",
        "window": "286.24-295.01", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": (
            "The men he told it to heard themselves in it, and it made them "
            "furious. But sitting right underneath their anger is the kindest "
            "fact in the whole story."
        ),
        "must_show": "the double landing — the hostile knot turning away in cold fury along the portico's edge, while Jesus watches them go with the kind fact still held out in his face.",
        "must_not_show": "no halo, glare or rim-light on Jesus; their fury contained (turned backs, gripped shawls), his face still open TOWARD them.",
        "scene": (
            "Along the portico's edge the fine-robed men "
            "are turning away in cold order — shawls "
            "gripped, backs stiffening, the young scribe's "
            "face white with contained fury as he follows "
            "his elders out of the colonnade — and behind "
            "them Jesus watches them go with his face still "
            "fully open in their direction, carrying toward "
            "their retreating backs the one fact in the "
            "story kind enough to be unbearable. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b53", "out": "s53-the-owner-never-stopped-sending.jpeg", "seg": "n13",
        "window": "295.01-297.41", "wide": True, "jesus": False, "ref": False,
        "locks": ["ROAD"],
        "narration": "The owner never stopped sending.",
        "must_show": "the road, used again — one more figure setting out up the pale road in new morning light; the sending that outlives every refusal.",
        "must_not_show": "no halo, glare or rim-light; the same road a final time — occupied, hopeful, morning-lit.",
        "scene": (
            "New morning light on the pale road: one more "
            "figure sets out up the long climb past the "
            "carob tree — staff in hand, a full satchel of "
            "bread, an empty basket riding on one arm — "
            "walking the most refused road in the story at "
            "an unhurried, undiscouraged pace, in light "
            "that looks like the first sending's light "
            "because that is exactly what it is. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r045-b54", "out": "s54-not-after-the-first-not.jpeg", "seg": "n13",
        "window": "297.41-304.77", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PORTICO"],
        "narration": (
            "Not after the first, not after the tenth, not even after the "
            "worst. That is the God this whole thing is about."
        ),
        "must_show": "the closing image — Jesus's face close in the portico light, the whole story resolved into it: the sender's patience and the son's courage in one expression, resting on the viewer.",
        "must_not_show": "no halo, glare or rim-light on Jesus; the final gaze meets the camera — the sent Son, still here, still offering.",
        "scene": (
            "A close final frame in the warm portico light: "
            "Jesus's face turned full to the camera, the "
            "warm brown eyes level and unhurried — the "
            "sender's unstoppable patience and the sent "
            "son's open courage resting together in one "
            "expression — the last messenger on the long "
            "road looking out of the story directly at "
            "whoever is standing on it. Every figure has "
            "two arms, two hands and one head."
        ),
    },
]
