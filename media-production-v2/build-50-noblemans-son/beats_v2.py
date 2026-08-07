#!/usr/bin/env python3
"""V2 beat map — row 50, build-50-noblemans-son (John 4:46-54).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 27 pictures over 152.1 s narration = 5.6 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (John 4:46-54 KJV):
  v46  Jesus came AGAIN into Cana of Galilee, WHERE HE MADE THE WATER WINE.
       A certain NOBLEMAN, whose son was sick AT CAPERNAUM.
  v47  he heard Jesus was come out of Judaea into Galilee; he WENT UNTO HIM
       and besought him that he would COME DOWN and heal his son, for he was
       AT THE POINT OF DEATH. ("Come down" is literal geography: Cana sits in
       the hills, Capernaum on the lakeshore ~20 miles away and far below —
       every journey shot must respect uphill-to-Cana / downhill-to-home.)
  v48  "Except ye see signs and wonders, ye will not believe." (jv48, red)
  v49  "Sir, come down ere my child die." (s49)
  v50  "Go thy way; thy son liveth." And the man BELIEVED THE WORD and WENT
       HIS WAY. No touch, no trip — the word alone.
  v51  as he was NOW GOING DOWN, his servants MET him: "Thy son liveth." (s51)
  v52  he enquired THE HOUR he began to amend: "Yesterday at the SEVENTH HOUR
       the fever left him." (s52) Seventh hour = about ONE IN THE AFTERNOON,
       so the word was spoken under a high midday sun — and the father was
       still on the road the NEXT DAY when the servants met him.
  v53  the father KNEW it was the same hour; himself believed, and his WHOLE
       HOUSE.
  v54  the second miracle Jesus did in Galilee.

CONTENT-CARE: row 50 is not in the §3 flag table = GREEN. Restraint applied
anyway: the sick boy is fevered and weak, never corpse-like or convulsing; the
sickroom shows love and helplessness, not horror. The healing is never shown as
a light-beam or effect — the proof is faces and the servants' news.

TIME-OF-DAY ARC (anchored by the seventh hour in v52):
  Cana arrival = bright day · sickroom = lamplit night vigil · the news +
  departure = first light / dawn · the uphill road = morning · finding Jesus,
  the plea, THE WORD = high midday sun (the seventh hour) · starting home =
  afternoon · servants meet him = next morning, clear early light · the
  realization = same morning · homecoming = warm late-day light.

CAST-REF NOTE: when the first still with the nobleman's face is ACCEPTED at QC,
copy it to CAST-REF-V2/nobleman-ref.jpeg and add
"char_refs": ["CAST-REF-V2/nobleman-ref.jpeg"] to every later legible-face beat
(b04-b26). Same for the boy (boy-ref.jpeg: b03, b06, b27) and the two servants
(servants-ref.jpeg: b22-b25). Text locks alone do not hold a face.
"""

# AUDIO-FIX 2026-08-07 (Machine A `Dev`): Cana→KANE-a pronunciation fix.
# The authoritative V1 mp4 (john-4_noblemans-son.mp4, 2026-07-29) carries the
# OLD rejected "Cana"=KAH/KAY-nuh takes. n1 and n3 (the only segments that say
# Cana) were re-voiced through the SAME locked ElevenLabs NARRATOR voice
# ("Brian", 44100/128k) with the respelling "Kayna" (=/keɪnə/, long-A KANE-a)
# and atempo-matched back to the original segment durations (n1 6.870s,
# n3 13.035s) so no still-window moves. The corrected mp3s live in the V1 dir's
# audio/. This flag makes v2_assemble rebuild the narration track from the V1
# build's OWN mp3s at the extract_beats offsets (the sanctioned fix the STALE-V1
# guard itself recommends) instead of copying the stale V1 mp4 AAC — so the
# shipped cut says KANE-a. Nothing else changed: same voice, same wording, same
# timing outside n1/n3.
AUDIO_FROM_V1_SEGMENTS = True

LOCKS = {
    # The nobleman's clothing NEVER changes (the story gives him no change of
    # clothes), so his lock states it once; beats add only its condition
    # (travel dust from b08 onward).
    "NOBLEMAN": (
        "NOBLEMAN LOCK: the royal official is the same man in every shot — "
        "about forty-five, broad-shouldered and used to command, olive-brown "
        "skin, short dark hair greying at the temples, a trimmed dark beard "
        "shot with grey, deep-set dark eyes. He wears a fine DEEP INDIGO-VIOLET "
        "wool robe with a narrow gold-thread border over a dark umber tunic, a "
        "wide leather belt with a bronze clasp, and good leather sandals — "
        "clothing plainly richer than anyone around him and plainly DARKER "
        "than sunlit stone, and none of it cream, off-white or any pale "
        "near-white cloth. His face is shown clearly."
    ),
    "BOY": (
        "BOY LOCK: the son is the same child in every shot — a boy of about "
        "ten, small for the bed he lies in, warm olive-brown skin, a mop of "
        "dark curly hair stuck to his brow, his father's deep-set dark eyes. "
        "In the sickroom he lies under a DARK MADDER-RED wool blanket in a "
        "plain undyed flax-brown sleeping tunic; nothing he wears or lies "
        "under is cream, off-white or any pale near-white cloth."
    ),
    "SERVANTS": (
        "SERVANTS LOCK: the two household servants are the same two men in "
        "every shot — one older, about fifty, grizzled short grey beard, in a "
        "plain DARK EARTH-BROWN wool tunic; one young, about twenty, "
        "clean-shaven with dark curly hair, in a DARK OLIVE-BROWN wool tunic. "
        "Both wear plain leather belts and dusty sandals; neither wears cream, "
        "off-white or any pale near-white cloth."
    ),
    "CANA": (
        "CANA LOCK: a small hill-country village of low flat-roofed limestone "
        "houses on a terraced slope, narrow dusty lanes, fig trees and grape "
        "vines between the walls, dry Galilean hills all around. The "
        "villagers and travellers who crowd its lanes wear SATURATED DEEP "
        "earth colours — dark chocolate brown, deep russet, burnt ochre, dark "
        "olive and dusty indigo wool — every garment plainly darker than the "
        "sunlit limestone walls; no one in the village wears cream, off-white, "
        "ivory or any pale near-white cloth."
    ),
    "HOUSE": (
        "CAPERNAUM HOUSE LOCK: the official's fine stone house in Capernaum "
        "near the lakeshore — smooth basalt-and-limestone walls, a colonnaded "
        "inner court, patterned wool hangings in deep madder-red and indigo, "
        "bronze oil lamps on stands, glimpses of the Sea of Galilee through "
        "its openings. Household members and servants wear plain dark "
        "earth-brown, olive and russet wool; no one in the house wears cream, "
        "off-white or any pale near-white cloth."
    ),
    "ROAD": (
        "ROAD LOCK: the road between Capernaum and Cana — a pale stony dirt "
        "track climbing steadily out of the lake basin into dry terraced "
        "hills, low basalt field walls and scattered olive trees beside it. "
        "Seen from the road, the Sea of Galilee lies far BELOW and behind "
        "toward Capernaum, and the hill country rises AHEAD toward Cana — "
        "going to Jesus is uphill, going home is downhill, in every shot."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r050-b01", "out": "s01-cana-again.jpeg", "seg": "n1 p1",
        "window": "0.28-4.70", "wide": True, "jesus": True, "ref": REF,
        "locks": ["CANA"],
        "narration": ("Jesus came back to Cana, the little town where he had "
                      "turned the water into wine."),
        "must_show": "Jesus arriving into Cana's lane on foot; villagers turning, recognizing him.",
        "must_not_show": "no halo/glow; he is among them, not detached at the frame edge.",
        "scene": (
            "Jesus walks up a narrow sunlit lane into the hill "
            "village, the camera at the lane's side taking his "
            "walk in profile, "
            "travel-dusty and at ease, and the village is already turning "
            "toward him — a woman setting down her water jar mid-step, two men "
            "rising from a doorway bench, children pausing their game — every "
            "face in the lane finding him at once, because they know this man; "
            "this is the town where the water became wine. Bright honest "
            "daylight on limestone walls. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r050-b02", "out": "s02-word-spreading.jpeg", "seg": "n1 p2",
        "window": "4.70-7.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["CANA"],
        "narration": "And word of it was spreading fast.",
        "must_show": "the news in motion — villagers passing it mouth to mouth, someone already hurrying out of the village with it.",
        "must_not_show": "Jesus is NOT in this frame; the news travels, not the man.",
        "scene": (
            "At the low stone well in the village's small open square, a "
            "cluster of villagers lean in as an excited older woman tells them "
            "the news, her hands mid-gesture — and beyond them a young man is "
            "already hurrying away down the descending road out of the "
            "village, SEEN FROM BEHIND, the back of his head and shoulders to "
            "the camera as he carries the word downhill toward the lake "
            "country. Bright morning light, long lane shadows. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b03", "out": "s03-the-sick-son.jpeg", "seg": "n2 p1",
        "window": "7.65-12.01", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "BOY", "HOUSE"],
        "narration": ("About twenty miles away, in Capernaum, a royal official "
                      "sat by his son's bed."),
        "must_show": "the lamplit sickroom vigil — the great man sitting small beside a child's bed.",
        "must_not_show": "the boy is fevered and weak, never corpse-like; no physician in this frame.",
        "scene": (
            "In a lamplit room of the fine stone house at night, the official "
            "sits on a low stool drawn close against his son's bed, leaning "
            "forward with his forearms on his knees, watching the boy's "
            "flushed sleeping face. The child lies small under the dark "
            "madder-red blanket, dark curls stuck to his damp forehead, "
            "breathing shallow. One bronze oil lamp burns on its stand; the "
            "patterned hangings fade into warm shadow. Exactly two people are "
            "in the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b04", "out": "s04-a-man-of-rank.jpeg", "seg": "n2 p2",
        "window": "12.01-15.54", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "HOUSE"],
        "narration": "A man of rank, used to giving orders and being obeyed.",
        "must_show": "the rank — the fine robe, the bearing, the bronze clasp — worn by a man staring at nothing.",
        "must_not_show": "no servants being ordered; the power is idle, that is the point.",
        "scene": (
            "The official stands at a night-dark window opening of his own "
            "colonnaded court, lamplight from the sickroom behind him catching "
            "the gold-thread border of his fine indigo-violet robe and the "
            "bronze clasp of his belt — a man built for command, hands hanging "
            "empty at his sides, jaw tight, staring out at the black water of "
            "the lake. Exactly one person is in the frame, with two arms, two "
            "hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r050-b05", "out": "s05-no-use-now.jpeg", "seg": "n2 p3",
        "window": "15.54-17.59", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "BOY", "HOUSE"],
        "narration": "And none of it was any use now.",
        "must_show": "his hand on the boy's fevered brow — rank useless against a fever.",
        "must_not_show": "no weeping collapse; a strong man quietly out of moves.",
        "scene": (
            "Close at the bedside in warm lamplight: the official's broad "
            "hand, a heavy signet ring on one finger, rests gently on his "
            "small son's burning forehead, and above it the father's face is "
            "helpless — the face of a man whose orders mean nothing here. The "
            "boy's flushed cheek and damp dark curls lie against the pillow "
            "below. Exactly two people are in the frame; each visible hand "
            "has five fingers."
        ),
    },
    {
        "id": "v2-r050-b06", "out": "s06-out-of-answers.jpeg", "seg": "n2 p4",
        "window": "17.59-22.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "BOY", "HOUSE"],
        "narration": ("His boy was burning with fever, and the doctors had run "
                      "out of answers."),
        "must_show": "the physician stepping back, closing his bag — the moment medicine gives up.",
        "must_not_show": "no despairing theatrics; the mother's grief restrained; the boy alive.",
        "scene": (
            "In the lamplit sickroom an elderly physician in a dark "
            "grey-brown robe straightens up from the bed and closes his worn "
            "leather satchel of clay vials, his eyes down, unable to meet the "
            "father's stare — the official stands rigid at the foot of the "
            "bed, and behind him the boy's mother, in deep russet wool with a "
            "dark shawl, presses both hands over her mouth. The boy lies "
            "flushed and shallow-breathing under the madder-red blanket. "
            "Exactly four people are in the frame; each has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r050-b07", "out": "s07-he-heard.jpeg", "seg": "n3 p1",
        "window": "22.34-26.60", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "HOUSE", "SERVANTS"],
        "narration": ("Then he heard the healer was in Cana, a full day's walk "
                      "uphill."),
        "must_show": "the news arriving — a servant telling him, the official already half-turned to go.",
        "must_not_show": "first grey light, not full day; the lamps still burning.",
        "scene": (
            "In the colonnaded court at first grey light, the young "
            "dark-curled servant in olive-brown wool stands breathless before "
            "his master, one arm flung out pointing away toward the hills "
            "inland, mouth open mid-word — and the official has gone utterly "
            "still, gripping the servant's shoulder with one hand, his face "
            "cut between fear and the first edge of hope. A bronze lamp still "
            "burns behind them against the dawn. Exactly two people are in "
            "the frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b08", "out": "s08-dropped-everything.jpeg", "seg": "n3 p2a",
        "window": "26.60-31.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "HOUSE", "SERVANTS"],
        "narration": ("So this powerful man dropped everything and went, "
                      "hurrying on foot"),
        "must_show": "the departure — striding out the gate at dawn on foot, no litter, no horse, no escort forming up.",
        "must_not_show": "no mount, no carriage, no retinue — ON FOOT is the story.",
        "scene": (
            "The official strides out through the stone gateway of his own "
            "house into the dawn street, throwing the end of his fine "
            "indigo-violet robe over one shoulder as he goes, his face set "
            "hard toward the hills — behind him in the gateway the older "
            "grey-bearded servant stands holding a staff and water-skin out "
            "toward his master, a beat behind the man's hurry. The sky over "
            "the lake is barely light. Exactly two people are in the frame; "
            "each has two arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r050-b09", "out": "s09-uphill-road.jpeg", "seg": "n3 p2b",
        "window": "31.00-35.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "ROAD"],
        "narration": ("to find a village carpenter's son, because he had "
                      "nowhere else left to turn."),
        "must_show": "the long climb — one rich man small on a rising road, the lake far below behind him.",
        "must_not_show": "nobody with him; he travels alone and fast.",
        "scene": (
            "SHOT FROM BEHIND THE OFFICIAL, low on the stony road, his back "
            "to the camera as he climbs AWAY from us up the long pale track "
            "into the terraced hills, robe hitched clear of his ankles, "
            "leaning into the grade with a traveller's staff — and far below "
            "and behind him, filling the bottom distance of the frame, the "
            "Sea of Galilee lies flat and bright with Capernaum small on its "
            "shore. The road ahead of him runs on up toward the high country "
            "where Cana is. An upright vertical photograph, the ground at the "
            "bottom of the frame and the sky at the top, the horizon level — "
            "the picture is the right way up. Morning light. Exactly one "
            "person is in the frame, with two arms, two hands, two legs and "
            "one head."
        ),
    },
    {
        "id": "v2-r050-b10", "out": "s10-he-found-jesus.jpeg", "seg": "n4 p1",
        "window": "35.89-40.89", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN", "CANA"],
        "narration": ("He found Jesus and begged him to come down to Capernaum "
                      "and heal his boy before it was too late."),
        "must_show": "the meeting — the rich man arrived and begging, dust on his fine robe; Jesus turned fully toward him.",
        "must_not_show": "no halo/glow; the crowd's gazes converge on the two of them.",
        "scene": (
            "In Cana's small open square under a high midday sun, the "
            "official has pushed through to Jesus and stands begging — bent "
            "forward, both hands reaching out open toward him, his fine "
            "indigo-violet robe grey with road dust to the knee — and Jesus "
            "has turned fully to face him, calm and attentive, meeting the "
            "man's desperation squarely. Around them the villagers have gone "
            "quiet, every face turned in on the two men at the centre. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b11", "out": "s11-no-pride-left.jpeg", "seg": "n4 p2",
        "window": "40.89-44.93", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN"],
        "narration": "A father with no pride left, only fear.",
        "must_show": "close on the official's pleading face — rank stripped away, just a frightened father.",
        "must_not_show": "no grovelling on the ground; standing, but stripped bare.",
        "scene": (
            "A tight shot in hard midday light: the official's face fills one "
            "side of the frame, sweat cutting tracks through the road dust on "
            "his temple, his deep-set eyes wet and locked upward on Jesus in "
            "open desperation, his mouth mid-plea — and at the frame's other "
            "edge Jesus's shoulder and calm profile receive it, his eyes on "
            "the man, steady. Exactly two people are in the frame; each "
            "visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r050-b12", "out": "s12-signs-and-wonders.jpeg", "seg": "jv48",
        "window": "44.93-49.61", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN", "CANA"],
        "narration": ("Except ye see signs and wonders, ye will not believe. "
                      "(John 4:48)"),
        "must_show": "Jesus speaking it — not scolding; his eyes on the man, the crowd hearing it too.",
        "must_not_show": "no pointed finger, no anger on Jesus's face; the words search, they do not strike.",
        "scene": (
            "Jesus speaks, his face gentle and grave at once, one open hand "
            "turned slightly outward to take in the listening crowd around "
            "the square while his eyes stay steadily on the official in front "
            "of him — and the villagers exchange glances at the words, while "
            "the dust-streaked official stands holding Jesus's gaze, his "
            "hands still half-raised from his plea. High midday sun. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b13", "out": "s13-reaching-past-panic.jpeg", "seg": "n5 p1-p2",
        "window": "49.61-56.41", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN"],
        "narration": ("It can sound like a scolding, but it was not. Jesus was "
                      "reaching past the man's panic for something deeper."),
        "must_show": "the two faces close — Jesus's steady searching gaze meeting the man's frantic one.",
        "must_not_show": "no crowd in this frame; the exchange narrows to the two of them.",
        "scene": (
            "A close two-shot in bright midday light, the square's crowd "
            "fallen away to soft blur: Jesus and the official face to face at "
            "conversation distance, and the frame holds the meeting of their "
            "eyes — the official's face taut and frantic, breathing hard, and "
            "Jesus's face utterly steady, looking not at the man's fear but "
            "through it, the way a man looks for the bottom of a well. "
            "Exactly two people are in the frame; each has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r050-b14", "out": "s14-invited-to-trust.jpeg", "seg": "n5 p3",
        "window": "56.41-60.63", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("He was inviting him to trust without needing a show "
                      "first."),
        "must_show": "close on Jesus's face alone — the invitation in it, warmth without softness.",
        "must_not_show": "no halo, no glow, no rim-light; the warmth is in the expression only.",
        "scene": (
            "Close on Jesus's face under the high sun, looking very slightly "
            "past the camera at the man before him — warm brown eyes steady "
            "and open, the faint beginning of kindness at the corners of his "
            "mouth, the face of someone holding a door open and waiting to "
            "see if the other man will walk through it. Exactly one person is "
            "in the frame, with one head."
        ),
    },
    {
        "id": "v2-r050-b15", "out": "s15-he-says-it-again.jpeg", "seg": "n6",
        "window": "60.63-67.81", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN"],
        "narration": ("The father does not argue about it. He does not defend "
                      "himself. He just says it again, plain and breaking."),
        "must_show": "the official mid-word, hands open — not arguing, just asking again with everything gone but the ask.",
        "must_not_show": "no anger, no wounded pride on his face; only the child behind his eyes.",
        "scene": (
            "The official stands before Jesus with both hands open at his "
            "sides, palms turned forward and empty, his shoulders down out of "
            "their soldier's set at last — his dusty face is plain and "
            "breaking as he says it again, nothing left in it but the boy. "
            "Jesus, at the edge of the frame, is turned fully toward him, "
            "listening. High midday sun. Exactly two people are in the frame; "
            "each has two arms, two hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r050-b16", "out": "s16-ere-my-child-die.jpeg", "seg": "s49",
        "window": "67.81-71.69", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN"],
        "narration": "Sir, come down ere my child die. (John 4:49)",
        "must_show": "tight on the father's face carrying the whole sentence — the plainest prayer in the Gospel.",
        "must_not_show": "no tears streaming; dry-eyed desperation is harder and truer.",
        "scene": (
            "A very tight shot of the official's face in hard midday light, "
            "filling the frame: road dust in the grey of his beard, his jaw "
            "unsteady, his dark eyes fixed up and pleading on the man before "
            "him, lips mid-word on the only sentence he has left. Exactly one "
            "person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r050-b17", "out": "s17-the-whole-prayer.jpeg", "seg": "n6b",
        "window": "71.69-79.87", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN"],
        "narration": ("That is the whole prayer. No argument, no explaining "
                      "himself, nothing clever. Just a father running out of "
                      "hours."),
        "must_show": "the stillness after the sentence — the plea hanging in the air between the two men.",
        "must_not_show": "neither man moving yet; the answer has not come.",
        "scene": (
            "The square has gone silent around the two of them under the "
            "vertical noon light: the official stands spent, his open hands "
            "still forward from the asking, chest rising and falling — and "
            "Jesus stands close before him, head very slightly tilted, "
            "receiving the plea with his whole attention, the crowd beyond "
            "them soft and motionless. Exactly two people are in the frame in "
            "focus; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b18", "out": "s18-thy-son-liveth.jpeg", "seg": "jv50",
        "window": "79.87-83.54", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN"],
        "narration": "Go thy way; thy son liveth. (John 4:50)",
        "must_show": "Jesus saying the word — calm, certain, final; the sentence that does the miracle.",
        "must_not_show": "no raised arm, no light effect, no drama — a quiet sentence, that is the wonder.",
        "scene": (
            "Close on Jesus as he says it: his face calm and absolutely "
            "certain, eyes steady on the official's, one hand lifted only a "
            "little between them, palm easing gently downward like a man "
            "settling a frightened animal — the whole miracle carried in "
            "nothing but the certainty of his face. The official's stunned "
            "profile edges the frame, the words just landing on him. High "
            "midday sun. Exactly two people are in the frame; each visible "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r050-b19", "out": "s19-just-a-word.jpeg", "seg": "n7 p1-p3",
        "window": "83.54-90.85", "wide": True, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN", "CANA", "ROAD"],
        "narration": ("No trip to Capernaum. No hand laid on the boy. Just a "
                      "word, spoken over a sick child a day's journey away."),
        "must_show": "the distance the word must cross — the two men in Cana high up, and far country falling away below toward the unseen lake.",
        "must_not_show": "no light-beam, no visual effect travelling; the land between them is the picture.",
        "scene": (
            "A wide shot, the camera at the edge of Cana's square "
            "behind the two men's shoulders, where the village "
            "brow drops away: Jesus and the dust-streaked official stand "
            "facing each other in the near frame, the word just spoken "
            "between them — and past them the terraced hills fall away fold "
            "on fold into the hazy distance toward the low lake country, a "
            "full day's walk of empty air between this sentence and the bed "
            "it lands on. High midday sun, shadows pooled small at their "
            "feet. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b20", "out": "s20-he-turned-home.jpeg", "seg": "n7 p4",
        "window": "90.85-95.29", "wide": False, "jesus": True, "ref": REF,
        "locks": ["NOBLEMAN", "CANA", "ROAD"],
        "narration": "And the man believed him, turned, and started home.",
        "must_show": "the belief made visible — the man mid-turn AWAY from Jesus, first step onto the downhill road, no proof in his hands.",
        "must_not_show": "he does not look back over his shoulder; the turn is clean — that is the faith.",
        "scene": (
            "SHOT FROM BESIDE JESUS, over his shoulder: in the near frame "
            "Jesus stands watching, calm, and a few paces beyond him the "
            "official is caught mid-stride WALKING AWAY FROM JESUS AND AWAY "
            "FROM THE CAMERA onto the road out of the village — his back and "
            "shoulders to us, his face gone from view because he is faced "
            "squarely down the descending road toward home, staff already "
            "swinging forward, not looking back. The road drops ahead of him "
            "toward the distant lake haze. Early afternoon sun. Exactly two "
            "people are in the frame; each has two arms, two hands, two legs "
            "and one head."
        ),
    },
    {
        "id": "v2-r050-b21", "out": "s21-the-long-walk.jpeg", "seg": "n8",
        "window": "95.29-104.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "ROAD"],
        "narration": ("Think about that walk. A whole day on the road with no "
                      "proof in his hands, nothing to hold but a stranger's "
                      "word that his son was already well."),
        "must_show": "the faith-walk — one small figure descending an immense empty landscape, carrying nothing but a sentence.",
        "must_not_show": "no companions, no proof, no destination visible yet; late-afternoon light, long shadows.",
        "scene": (
            "A very wide shot of the empty hill road in late-afternoon light: "
            "the official is a small lone figure descending the pale track as "
            "it winds down through the terraced folds, SEEN FROM THE SIDE AND "
            "SLIGHTLY BEHIND so he moves across the frame and away, downhill, "
            "toward the far-off silver line of the lake just visible in the "
            "haze below — one man and twenty miles of evening between him and "
            "the answer. His long shadow walks the slope beside him. An "
            "upright vertical photograph, the ground at the bottom of the "
            "frame and the sky at the top, the horizon level — the picture is "
            "the right way up. Exactly one person is in the frame, with two "
            "arms, two hands, two legs and one head."
        ),
    },
    {
        "id": "v2-r050-b22", "out": "s22-servants-running.jpeg", "seg": "n9 p1",
        "window": "104.08-108.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "SERVANTS", "ROAD"],
        "narration": ("The next day, still on the road, he saw his own "
                      "servants running toward him."),
        "must_show": "v51 — the two servants at a full run UP the road toward him; him stopped dead at the sight of them.",
        "must_not_show": "their faces at this distance not yet readable — he cannot tell yet if they bring good news or the worst.",
        "scene": (
            "THE CAMERA STANDS BESIDE AND SLIGHTLY BEHIND THE "
            "OFFICIAL on the morning "
            "road, his travel-worn profile in the near frame stopped dead "
            "mid-stride, staff frozen against the ground — and far DOWN the "
            "road ahead of him, directly along his line of sight, two small "
            "figures in dark earth-brown and olive-brown wool are running "
            "flat-out UP the slope TOWARD him, dust kicking behind their "
            "heels, still too far for their faces to be read. Clear early "
            "morning light, the lake bright below. Exactly three people are "
            "in the frame; each has two arms, two hands, two legs and one "
            "head."
        ),
    },
    {
        "id": "v2-r050-b23", "out": "s23-thy-son-liveth-again.jpeg", "seg": "s51",
        "window": "108.59-111.42", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "SERVANTS", "ROAD"],
        "narration": "Thy son liveth. (John 4:51)",
        "must_show": "the arrival of the news — the servants reaching him, faces alight, the words bursting out of them.",
        "must_not_show": "the father's joy not landed yet — this frame is THEIR faces shining, his still mid-shock.",
        "scene": (
            "The two servants have reached their master on the stony road "
            "and all but fall against him — the young one gripping the "
            "official's forearm with both hands, face split wide with joy, "
            "mouth open mid-shout, the older grey-bearded one bent with his "
            "hands braced on his knees, heaving for breath and laughing up "
            "at his master at the same time — and the official stands rigid "
            "between them, the news striking him. Clear morning light. "
            "Exactly three people are in the frame; each has two arms, two "
            "hands of five fingers each and one head."
        ),
    },
    {
        "id": "v2-r050-b24", "out": "s24-the-same-two-words.jpeg", "seg": "n9b",
        "window": "111.42-123.34", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "SERVANTS"],
        "narration": ("Your boy is alive. The very same two words Jesus had "
                      "said to him a day before, coming back to him now from "
                      "his own servants' mouths, out of breath from running to "
                      "say them."),
        "must_show": "the words landing — close on the father's face as disbelief cracks open into joy.",
        "must_not_show": "no wailing or collapse; the joy breaks slowly, like ice going.",
        "scene": (
            "Close on the official's travel-worn face in the clear morning "
            "light, the young servant's shining face just in frame beside "
            "his shoulder: the father's eyes have gone wide and wet, his "
            "mouth is coming open, and across his dust-grimed features the "
            "disbelief is visibly breaking up into the beginning of an "
            "enormous joy — a strong man's face losing a two-day-old weight "
            "all at once. Exactly two people are in the frame; each has one "
            "head."
        ),
    },
    {
        "id": "v2-r050-b25", "out": "s25-what-hour.jpeg", "seg": "n10 + s52",
        "window": "123.34-131.61", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "SERVANTS", "ROAD"],
        "narration": ("So he asked them exactly when the boy had started to "
                      "mend. / Yesterday at the seventh hour the fever left "
                      "him. (John 4:52)"),
        "must_show": "v52 — the father gripping the servant, demanding the hour; the older servant answering, pointing back down the road toward home.",
        "must_not_show": "not a celebration yet — the father's face is fierce with the question.",
        "scene": (
            "On the bright morning road the official has seized the older "
            "grey-bearded servant by both shoulders, bent close, his face "
            "fierce and urgent with the question — and the old servant, "
            "still catching his breath, answers with one arm flung out "
            "pointing away DOWN the road toward the distant lake and home, "
            "marking the hour with his other raised hand. The young servant "
            "watches them both, grinning. Exactly three people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b26", "out": "s26-the-same-hour.jpeg", "seg": "n10b",
        "window": "131.61-141.39", "wide": False, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "SERVANTS", "ROAD"],
        "narration": ("And he knew that hour. It was the exact hour Jesus had "
                      "stood in front of him and said, thy son liveth. It had "
                      "already been done while he was still walking."),
        "must_show": "the realization — the father turned to look back UP the road toward Cana, the arithmetic landing.",
        "must_not_show": "no light effect, no vision; the wonder is entirely in his face and the empty uphill road.",
        "scene": (
            "The official has turned where he stands to look back UP the "
            "long pale road as it climbs away behind him into the hills "
            "toward Cana, one hand risen slowly to his mouth — his face, "
            "seen in profile against the high country, is naked wonder, a "
            "man understanding that the thing was already finished yesterday "
            "at midday while his sandals were still on this road. The two "
            "servants stand quiet behind him, watching their master. "
            "Morning light. Exactly three people are in the frame; each has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r050-b27", "out": "s27-his-whole-house.jpeg", "seg": "n11",
        "window": "141.39-151.88", "wide": True, "jesus": False, "ref": False,
        "locks": ["NOBLEMAN", "BOY", "HOUSE", "SERVANTS"],
        "narration": ("And that settled it. The man believed, and his whole "
                      "household believed with him. The word had been true the "
                      "entire way home, working quietly while he walked and "
                      "could not see it."),
        "must_show": "v53 — the homecoming: the boy WELL, up on his feet in his father's arms, the whole household around them.",
        "must_not_show": "no sickbed in frame; the fever is over; nobody in cream.",
        "scene": (
            "In the colonnaded court of the Capernaum house in warm "
            "late-day light, the camera behind the gathered "
            "household's shoulders, in "
            "light, the official has dropped to one knee with his small son "
            "caught up whole and laughing in his arms — the boy bright-eyed "
            "and well in a dark ochre tunic, his arms around his father's "
            "neck — and around them the whole household presses in: the "
            "mother in deep russet with both hands at her heart, the two "
            "servants, an old housekeeper in dark olive wool, every face lit "
            "with the same understanding of what has happened in this house. "
            "Every figure has two arms, two hands and one head."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
PLACE_REFS = {
    "CANA": "PLACE-REF/cana.jpeg",  # build-50-noblemans-son s01-cana-again (manual)
    "ROAD": "PLACE-REF/road.jpeg",  # build-38-persistent-widow v2-r038-b39
}
# === end PLACE-PLATES ===

# Per-story face sheets, generated by v2_story_cast.py. Identity is
# carried by IMAGE, not by wording — text locks let the elder son come
# back as three different men in row 2 (Cameron, 2026-07-30).
REFS = {
    "NOBLEMAN": "CAST-REF-V2/nobleman.jpeg",
    "BOY": "CAST-REF-V2/boy.jpeg",
}
