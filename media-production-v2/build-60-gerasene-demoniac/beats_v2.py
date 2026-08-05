#!/usr/bin/env python3
"""V2 beat map — row 60, build-60-gerasene-demoniac (Mark 5:1-20).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE: 39 pictures over 226.0 s narration = 5.8 s/picture, inside the
4.6-6.0 band rows 1-11 shipped at.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Mark 5:1-20 KJV):
  v1   the OTHER SIDE of the sea — Gentile Decapolis country; arrival at
       first light after the night storm of Mark 4 (row 11).
  v2   IMMEDIATELY out of the ship, there met him OUT OF THE TOMBS a man.
  v3   his dwelling AMONG THE TOMBS; no man could bind him, no, not with
       CHAINS; v4: chains PLUCKED ASUNDER, fetters BROKEN IN PIECES.
  v5   night and day, in the mountains and in the tombs, CRYING — (the
       same verse's self-cutting is NEVER depicted: flag law below).
  v6   when he saw Jesus AFAR OFF, HE RAN and WORSHIPPED him — he runs TO
       Jesus, not at him; the man's own last shred steering.
  v7   "What have I to do with thee, Jesus, thou Son of the most high God?
       I adjure thee by God, that thou torment me not." (s7)
  v8   "Come out of the man, thou unclean spirit." (j1)
  v9   "What is thy name?" "My name is LEGION: for we are many." (j2/s9)
  v11  a great herd of swine feeding NIGH UNTO THE MOUNTAINS — about TWO
       THOUSAND (v13).
  v12  "Send us into the swine." v13: Jesus GAVE THEM LEAVE; the herd ran
       VIOLENTLY DOWN A STEEP PLACE INTO THE SEA.
  v14  the swineherds FLED and told it in the city and country.
  v15  they see him that was possessed SITTING, CLOTHED, and IN HIS RIGHT
       MIND: and THEY WERE AFRAID. v17: they began to PRAY HIM TO DEPART.
  v18  the healed man PRAYED HIM THAT HE MIGHT BE WITH HIM.
  v19  Jesus suffered him not: "GO HOME TO THY FRIENDS, and tell them how
       great things the Lord hath done for thee, and hath had COMPASSION
       on thee." — the only recorded 'no' to a would-be follower.
  v20  he published in DECAPOLIS how great things Jesus had done: and ALL
       MEN DID MARVEL.

CONTENT-CARE — FLAGS A + R (§3 table: "Gerasene — no embodied devils,
self-harm NEVER depicted; before/after dignity"):
  A — the adversary NEVER gets a face, body, shadow-shape, smoke or any
      visible form; the possession shows ONLY in the man's condition, and
      nothing visible leaves him at the deliverance.
  self-harm — the cutting with stones (v5) is NEVER depicted, referenced,
      or implied by props; no wounds, no scars rendered as focus.
  R — the pigs' end is one WIDE beat (b25): the herd pouring down the bank
      into the water; no animal suffering in close-up, no carcasses shown.
  Dignity — BEFORE: a human being in torment, pitiable, never a monster.
      AFTER: clothed, calm, seated — the picture the whole build aims at.

TIME-OF-DAY ARC: v1 fixes the start — FIRST LIGHT after the night storm:
grey-gold dawn on the shore for the arrival and the encounter; the memory
beats among the tombs (b06-b09) may go colder/darker including one night
memory; full morning by the herd and the town's coming; warm mid-morning
for the sending; day for the Decapolis close.

CAST-REF NOTE: when the first still with the man's face is ACCEPTED at QC,
copy it to CAST-REF-V2/gerasene-ref.jpeg and add
"char_refs": ["CAST-REF-V2/gerasene-ref.jpeg"] to every later legible-face
beat — his before/after arc rides entirely on one recognizable face. Text
locks alone do not hold a face.
"""

LOCKS = {
    # His CONDITION and CLOTHING change at v15 (ragged -> clothed); the lock
    # fixes face and build only, and each beat states state and dress.
    "MAN": (
        "GERASENE LOCK: the man is the same man in every shot — about "
        "forty, tall and big-boned but starved gaunt, deep-set haunted "
        "dark eyes, long matted black hair and a wild tangled black "
        "beard (after his healing the same hair and beard, cleaner but "
        "the same). Before the healing he wears only torn rags of DARK "
        "GREY-BROWN cloth; after it he wears a plain borrowed DARK "
        "OLIVE-BROWN wool tunic with a rope belt. Never cream, never "
        "white. His face is shown clearly. He is a human being in "
        "torment and then in peace — pitiable and dignified, never a "
        "monster, never made frightening for its own sake. No wounds or "
        "scars are ever rendered."
    ),
    "SHORE": (
        "SHORE LOCK: the eastern shore of the Sea of Galilee at first "
        "light — a narrow stony beach under steep barren hills, "
        "grey-gold dawn water, the dark fishing boat drawn up at the "
        "waterline with its sail furled. The disciples near the boat "
        "wear plain work tunics in deep saturated earth wools — dark "
        "charcoal-brown, deep russet, dark olive, dusty indigo; none of "
        "them wears cream, off-white or any pale near-white cloth."
    ),
    "TOMBS": (
        "TOMBS LOCK: the tomb hills above the shore — pale limestone "
        "slopes honeycombed with black cave-tomb mouths, some sealed "
        "with rolling stones, dry thorn and scree between them, broken "
        "grave-markers; a place of the dead in Gentile country, empty "
        "of all living company."
    ),
    "TOWN": (
        "TOWN LOCK: the Gentile town of the Gadarenes — flat-roofed "
        "stone houses with foreign touches: a small columned shrine, "
        "carved thresholds. Its people wear SATURATED DEEP earth "
        "colours with Gentile patterning — dark chocolate brown, deep "
        "russet, burnt ochre, dark olive and dusty indigo wool with "
        "banded borders; no one wears cream, off-white, ivory or any "
        "pale near-white cloth."
    ),
    "HERD": (
        "HERD LOCK: the pig herd is vast — about two thousand dark and "
        "pink-grey swine spread feeding across the steep hillside "
        "pasture above the sea, tended by a handful of herdsmen in "
        "rough DARK EARTH-BROWN wool with staffs."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r060-b01", "out": "s01-the-far-shore-at-first-light.jpeg", "seg": "n0 p1",
        "window": "0.28-8.08", "wide": True, "jesus": True, "ref": REF,
        "locks": ["SHORE"],
        "narration": ("The boat touched the far shore of the Sea of "
                      "Galilee at first light — the disciples still "
                      "shaking from the storm that had nearly sunk them "
                      "in the night."),
        "must_show": "v1 — the landfall: the boat grounding on the stony beach in grey-gold dawn; storm-wrung disciples; Jesus composed.",
        "must_not_show": "the sea behind is calm NOW — the storm is over; its cost shows only in the men.",
        "scene": (
            "The dark fishing boat grinds up onto the stony beach, "
            "the camera along the waterline taking hull and shore "
            "in profile, in "
            "the grey-gold of first light — the disciples inside it "
            "drenched, hollow-eyed and storm-wrung, one still gripping "
            "the mast, another slumped over an oar — while Jesus "
            "stands composed in the bow looking up at the barren "
            "hills, and behind them the sea that tried to kill them "
            "in the night lies flat as poured metal. Everyone is "
            "fully inside the hull. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r060-b02", "out": "s02-gentile-country.jpeg", "seg": "n0 p2-p4",
        "window": "8.08-15.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHORE", "HERD"],
        "narration": ("This was the other side. Gentile country. Foreign "
                      "gods, foreign food, herds of pigs on the hills."),
        "must_show": "the foreignness — the pig herds dotting the high pasture, a small columned shrine; everything a Galilean would not keep.",
        "must_not_show": "the pigs alone announce the country — unmistakable and many, up on the slopes.",
        "scene": (
            "From the beach the land tells what it is: the steep "
            "barren hills climb into the dawn light with a vast herd "
            "of dark and pink-grey pigs spread feeding across the "
            "high pasture — hundreds visible, more behind the "
            "ridge — and on a spur above the shore stands a small "
            "foreign shrine of squat columns, grey in the early "
            "light. Nothing about the place keeps the law of the "
            "other shore. An upright vertical photograph, the ground "
            "at the bottom of the frame and the sky at the top, the "
            "horizon level — the picture is the right way up."
        ),
    },
    {
        "id": "v2-r060-b03", "out": "s03-no-rabbi-came-here.jpeg", "seg": "n0 p5",
        "window": "15.80-18.87", "wide": False, "jesus": False, "ref": False,
        "locks": ["SHORE"],
        "narration": "No rabbi took his students here on purpose.",
        "must_show": "the disciples' wariness — faces at the gunwale reading the foreign shore, nobody eager to step out.",
        "must_not_show": "not fear of danger — the deep unease of devout men somewhere they should not be.",
        "scene": (
            "Close along the boat's gunwale: three disciples' faces "
            "in a row, weather-beaten and storm-tired, reading the "
            "foreign hillside — one with his jaw set sideways, one "
            "glancing at the shrine and away as if the look itself "
            "were unclean, one watching the distant pigs with open "
            "disbelief — devout Galilean men measuring exactly how "
            "far from home the night has brought them. Exactly "
            "three people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r060-b04", "out": "s04-he-crossed-a-storm-for-this.jpeg", "seg": "n0 p6",
        "window": "18.87-22.94", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE"],
        "narration": "Jesus had crossed the whole sea in a storm to reach it.",
        "must_show": "the purpose — Jesus stepping over the bow onto the foreign stones, first ashore, unhesitating; the deliberate arrival.",
        "must_not_show": "no halo/glow; his certainty against the disciples' hanging back is the picture.",
        "scene": (
            "Jesus steps down over the bow onto the wet foreign "
            "stones, first out of the boat, landing with the "
            "unhesitating weight of a man arriving exactly where he "
            "meant to be — his eyes already lifted to the pale tomb "
            "hills above the beach — while behind him the disciples "
            "are only beginning to climb stiffly over the gunwale "
            "into a country none of them would have chosen. Dawn "
            "gold on the water behind. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b05", "out": "s05-among-the-tombs.jpeg", "seg": "n1 p1-p2",
        "window": "22.94-33.03", "wide": True, "jesus": False, "ref": False,
        "locks": ["MAN", "TOMBS"],
        "narration": ("Because one man lived there — if you could call it "
                      "living. He made his home among the tombs, the "
                      "caves where the dead were laid, because the town "
                      "had driven him out."),
        "must_show": "the dwelling — the honeycombed tomb slope, and one small ragged human figure among the black cave mouths.",
        "must_not_show": "FLAG A: nothing inhuman anywhere — one man, alone, housed with the dead; the loneliness is the horror allowed.",
        "scene": (
            "The pale limestone slope rises out of the dawn shadow, "
            "the camera far off, taking the slope from the side so the one small "
            "figure reads against the whole honeycombed face, "
            "pocked with black cave-tomb mouths and broken "
            "grave-markers — and in the middle of them, small "
            "against a sealed tomb's rolling stone, the ragged "
            "figure of a man sits with his knees drawn up and his "
            "matted head bowed, at home in the one neighbourhood "
            "that could not drive him out. No other living thing "
            "on the hill. An upright vertical photograph, the "
            "ground at the bottom of the frame and the sky at the "
            "top, the horizon level — the picture is the right way "
            "up. Exactly one person is in the frame."
        ),
    },
    {
        "id": "v2-r060-b06", "out": "s06-something-had-hold-of-him.jpeg", "seg": "n1 p3",
        "window": "33.03-36.85", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": ("Something had hold of him that no one could fix."),
        "must_show": "the man close — gaunt, ragged, hunted eyes; a human being worn to the bone by an occupation nobody can see.",
        "must_not_show": "FLAG A: the 'something' is visible ONLY as its toll on a human face; no wounds, no scars, nothing inhuman.",
        "scene": (
            "Close on the man in the grey dawn light: gaunt cheeks "
            "under the wild black beard, skin grey with exposure, "
            "and the deep-set eyes doing all the telling — hunted, "
            "exhausted, flinching at nothing visible, the eyes of a "
            "man who has not been alone inside his own head for "
            "years and cannot make anyone understand that. Rags of "
            "dark grey-brown cloth at his shoulders. Exactly one "
            "person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r060-b07", "out": "s07-they-had-tried-chains.jpeg", "seg": "n1 p4-p5",
        "window": "36.85-40.06", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN", "TOMBS"],
        "narration": "They had tried chains. He tore them apart.",
        "must_show": "v4 — the failed bindings: snapped chain lengths and burst fetters lying rusted among the rocks; a broken shackle ring still on his wrist.",
        "must_not_show": "no wounds at the wrist — the iron failed, the arm is whole; the strength is the point, not injury.",
        "scene": (
            "Close on the evidence in the thorn and scree: lengths "
            "of snapped chain gone orange with rust, a leg-fetter "
            "burst open at its rivet, and the man's forearm resting "
            "across his knee with a single broken shackle-ring "
            "still riding loose on the unmarked wrist — iron that "
            "men trusted, torn like bread. His ragged figure sits "
            "half in frame above the wreckage. Each visible hand "
            "has five fingers."
        ),
    },
    {
        "id": "v2-r060-b08", "out": "s08-crying-among-the-graves.jpeg", "seg": "n1 p6",
        "window": "40.06-43.13", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN", "TOMBS"],
        "narration": "Night and day he cried out among the graves.",
        "must_show": "v5 — the night memory: the lone figure crying out on the tomb slope under the moon; misery, not menace.",
        "must_not_show": "FLAG A + self-harm law: no stones in his hands, nothing visible tormenting him — a man howling at nothing anyone can see.",
        "scene": (
            "Night on the tomb hill under a high cold moon: the "
            "ragged man stands small among the black cave mouths "
            "with his head thrown back and his arms wrapped around "
            "his own chest, mid-cry — the long grey moonlit slope "
            "utterly empty around him, the sound going out over "
            "the dark water below to nobody — misery with no "
            "audience, night after night. Exactly one person is in "
            "the frame, with two arms and one head."
        ),
    },
    {
        "id": "v2-r060-b09", "out": "s09-he-was-a-warning.jpeg", "seg": "n1 p7-p8",
        "window": "43.13-48.21", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN", "TOMBS", "TOWN"],
        "narration": ("To his town he was no longer a name. He was a "
                      "warning."),
        "must_show": "the town's practised avoidance — travellers on the road below giving the tomb hill its wide berth; a mother turning a child's face away.",
        "must_not_show": "the man is a distant figure on his slope; the avoidance is habitual, worn smooth — crueller than fear.",
        "scene": (
            "On the morning road below the tomb hill a farm family "
            "passes with their donkey — the father's eyes fixed "
            "hard ahead, the mother turning her small son's face "
            "away with one hand while he cranes to look — their "
            "path bending in a long practised arc away from the "
            "slope where, far up among the tombs, the ragged "
            "figure stands watching them not look at him. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b10", "out": "s10-he-ran.jpeg", "seg": "n2 p1",
        "window": "48.21-53.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MAN", "TOMBS", "SHORE"],
        "narration": ("And when that man saw Jesus step out of the boat, "
                      "far down the shore, he ran."),
        "must_show": "v6 — the run: the ragged man tearing DOWN the slope TOWARD the tiny figures at the boat; direction unmistakable.",
        "must_not_show": "SHOT FROM BEHIND AND ABOVE him — his back to us, the beach and Jesus far below IN THE DIRECTION HE RUNS.",
        "scene": (
            "THE CAMERA IS BEHIND AND ABOVE THE MAN, his back to the "
            "camera as he plunges AWAY from us down the steep tomb "
            "slope at a headlong run — rags streaming, arms wide "
            "for balance on the scree — and far below him, small "
            "on the dawn beach and squarely IN THE DIRECTION HE IS "
            "RUNNING, Jesus stands by the grounded boat with the "
            "disciples. The whole slope runs him at one point. "
            "Every figure has two arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r060-b11", "out": "s11-he-fell-at-his-feet.jpeg", "seg": "n2 p2-p4",
        "window": "53.34-60.27", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SHORE"],
        "narration": ("Not to attack him. He ran and fell down at his "
                      "feet. And the thing inside him cried out:"),
        "must_show": "v6 — the arrival: the wild man crashed to his knees at Jesus's feet on the stones; disciples recoiled; Jesus unmoved.",
        "must_not_show": "worship, not assault — the fall is AT his feet, head down; the disciples' fear frames Jesus's stillness.",
        "scene": (
            "The ragged man has crashed onto his knees on the wet "
            "stones at Jesus's feet, his matted head down almost "
            "to the ground, chest heaving from the run — the "
            "disciples have scattered back against the boat's hull "
            "with an oar half-raised between them — and Jesus "
            "stands over the kneeling wreck of a man exactly where "
            "he stood, looking down at him without a flicker of "
            "retreat. Dawn light along the beach. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b12", "out": "s12-torment-me-not.jpeg", "seg": "s7",
        "window": "60.27-68.72", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN"],
        "narration": ("What have I to do with thee, Jesus, thou Son of "
                      "the most high God? I adjure thee by God, that "
                      "thou torment me not. (Mark 5:7)"),
        "must_show": "the cry — the man's upturned anguished face before Jesus: terror and plea from a mouth saying words that are not his.",
        "must_not_show": "FLAG A: a human face in anguish, nothing more — present human eyes watching their own mouth speak.",
        "scene": (
            "Close from beside Jesus's knee: the kneeling man's "
            "face turned up, wrenched with a terror that is "
            "begging — the cords of his neck standing, his eyes "
            "wet and terribly present, a passenger behind the "
            "words tearing out of his own mouth — while the hem "
            "and still hands of Jesus hold the frame's edge, "
            "unmoved. Exactly two people are in the frame; each "
            "visible hand has five fingers."
        ),
    },
    {
        "id": "v2-r060-b13", "out": "s13-the-darkness-knew-him.jpeg", "seg": "n2b p1-p3",
        "window": "68.72-76.33", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN"],
        "narration": ("Swear to me you won't torture me. Hear what just "
                      "happened. The man's own town had given up on him "
                      "and did not know who Jesus was."),
        "must_show": "the two-shot of the irony — the wreck the town abandoned, kneeling before the visitor the town cannot name, who is fully known here.",
        "must_not_show": "Jesus's face carries recognition-received calmly — the truest title of the morning came from the darkness.",
        "scene": (
            "A close two-shot in the strengthening light: the "
            "kneeling man spent against the stones, trembling, and "
            "Jesus bent slightly over him — his face calm and "
            "grave, receiving the title 'Son of the most high God' "
            "from the one mouth on this whole coast that knows it, "
            "with the unstartled stillness of a man being told his "
            "own name. Exactly two people are in the frame; each "
            "has one head."
        ),
    },
    {
        "id": "v2-r060-b14", "out": "s14-it-knew-it-was-finished.jpeg", "seg": "n2b p4",
        "window": "76.33-82.43", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("The darkness holding him knew exactly who had "
                      "just stepped onto that beach, and knew it was "
                      "finished."),
        "must_show": "close on Jesus alone — the settled authority: no battle coming, only an eviction already decided.",
        "must_not_show": "no anger, no strain — the face of an outcome, not a contest.",
        "scene": (
            "Close on Jesus's face in the full dawn light: utterly "
            "quiet, the warm eyes level and unhurried on the "
            "kneeling man below the frame — not the face of a man "
            "entering a fight but of one announcing its result, "
            "authority worn as calmly as the morning behind him. "
            "Exactly one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r060-b15", "out": "s15-he-did-not-step-back.jpeg", "seg": "n3",
        "window": "82.43-89.70", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MAN", "SHORE"],
        "narration": ("Jesus did not step back. He was not afraid of "
                      "him. He spoke straight past the man, to the thing "
                      "that held him."),
        "must_show": "the geometry of fearlessness — everyone else at maximum distance, Jesus a pace from the kneeling man; the address beginning.",
        "must_not_show": "the disciples' distance measures the courage; Jesus's feet are planted close.",
        "scene": (
            "A wide beach frame that tells it in distances, the "
            "camera off to the side so every gap reads in profile: the "
            "disciples pressed far back along the boat's hull, "
            "half-shielded behind it — and in the open middle of "
            "the stones Jesus stands one single pace from the "
            "kneeling ragged man, feet planted, head bent toward "
            "him, already speaking — the only human being on the "
            "shore inside twenty paces of the man everyone chains "
            "and flees. Dawn gold on the still water. Every figure "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b16", "out": "s16-come-out-of-the-man.jpeg", "seg": "j1",
        "window": "89.70-93.19", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Come out of the man, thou unclean spirit. "
                      "(Mark 5:8)"),
        "must_show": "the command — close on Jesus speaking it: quiet, final, aimed past the man at what holds him.",
        "must_not_show": "no shout in the face — the same terrible quietness as the synagogue; one sentence, already law.",
        "scene": (
            "Close on Jesus as the command leaves him: his face "
            "bent toward the kneeling man but his eyes aimed "
            "somehow past the man's eyes, deeper, addressing the "
            "occupant and not the house — the jaw barely moving, "
            "the voice plainly quiet, one hand risen only to "
            "waist height with the palm turned down, evicting "
            "with less effort than a man waves off a fly. Exactly "
            "one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r060-b17", "out": "s17-one-sentence.jpeg", "seg": "n4 p1-p2",
        "window": "93.19-101.16", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN"],
        "narration": ("Come out of him. Not a negotiation, not a ritual "
                      "— one sentence, aimed past the man at the thing "
                      "wearing him."),
        "must_show": "the word landing — the man shuddering under it, gripped and bowed; Jesus steady above; no contest visible.",
        "must_not_show": "FLAG A: the shudder is a man's body under strain, nothing more; nothing visible fights back.",
        "scene": (
            "The kneeling man has bowed under the sentence like a "
            "tree taking wind — head down, fists knotted against "
            "the stones, a long shudder running visibly through "
            "the starved shoulders — while Jesus stands over him "
            "unmoved, his hand still at waist height, waiting out "
            "the obedience with the patience of someone watching "
            "water find its level. Exactly two people are in the "
            "frame; each has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b18", "out": "s18-what-is-thy-name.jpeg", "seg": "n4 p3 + j2",
        "window": "101.16-106.35", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN"],
        "narration": ("And then he asked it a question. What is thy "
                      "name? (Mark 5:9)"),
        "must_show": "the question at eye level — Jesus crouched down to the kneeling man's height, face to face, asking.",
        "must_not_show": "the crouch is the mercy — he comes DOWN to the man no one comes near.",
        "scene": (
            "Jesus has crouched down onto his heels in front of "
            "the kneeling man, bringing his face level with the "
            "wrecked gaunt one — closer than chains, closer than "
            "the town ever came — and asks the question directly "
            "into it, his forearms resting easy on his knees, "
            "while the man's hunted eyes stare back from a "
            "hand-span away. Dawn light on both faces. Exactly "
            "two people are in the frame; each has one head."
        ),
    },
    {
        "id": "v2-r060-b19", "out": "s19-my-name-is-legion.jpeg", "seg": "s9",
        "window": "106.35-109.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": "My name is Legion: for we are many. (Mark 5:9)",
        "must_show": "the answer — close on the man's face: one present human being and the crowdedness behind his eyes; anguish, not effect.",
        "must_not_show": "FLAG A: no distortion, no double-exposure trickery — the 'many' reads only in the exhausted human eyes.",
        "scene": (
            "Very close on the gaunt face as the answer comes out "
            "of it: the mouth forms the word and the eyes above "
            "it are the testimony — layered, teeming, exhausted, "
            "the look of a single man standing in a doorway "
            "holding back a crowd, and under all of it, faint and "
            "human and still there, the man himself, listening to "
            "his own name being taken. Exactly one person is in "
            "the frame, with one head."
        ),
    },
    {
        "id": "v2-r060-b20", "out": "s20-outnumbered-inside.jpeg", "seg": "n5 p1-p2",
        "window": "109.80-117.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": ("Legion was a Roman army word — thousands of "
                      "soldiers. That is how outnumbered this one man "
                      "was on the inside."),
        "must_show": "the arithmetic of his suffering — the small kneeling figure alone on the wide stones; one man against a word that means thousands.",
        "must_not_show": "no soldiers, no imagery of armies — the smallness of one kneeling man carries the number.",
        "scene": (
            "A pulled-back shot down the empty dawn beach: the "
            "kneeling man alone and small on the wide grey "
            "stones, folded over his own knees with his arms "
            "wrapped around himself — one starved human frame "
            "photographed with all that emptiness around it, the "
            "visual arithmetic of a single man who has been "
            "outnumbered thousands to one inside his own skin "
            "for years. Exactly one person is in the frame."
        ),
    },
    {
        "id": "v2-r060-b21", "out": "s21-the-thousands-were-begging.jpeg", "seg": "n5 p3",
        "window": "117.41-122.71", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SHORE"],
        "narration": ("And standing in front of Jesus, the thousands "
                      "were the ones begging."),
        "must_show": "the reversal staged — the kneeling man's hands lifted in plea toward the one standing figure; power inverted.",
        "must_not_show": "the begging posture belongs to the 'legion' — and Jesus receives it standing, calm, unimpressed.",
        "scene": (
            "On the brightening beach the whole balance of the "
            "morning stands inverted: the kneeling man's hands "
            "are lifted up in open plea toward Jesus — the "
            "gesture of the conquered before the conqueror — and "
            "Jesus stands over the supplication calm and "
            "unimpressed, arms at rest, a man listening to a "
            "surrendered army ask for terms. The disciples watch "
            "frozen from the boat. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b22", "out": "s22-two-thousand-pigs.jpeg", "seg": "n6 p1",
        "window": "122.71-132.46", "wide": True, "jesus": False, "ref": False,
        "locks": ["HERD"],
        "narration": ("On the hillside above them, a herd of about two "
                      "thousand pigs was feeding — remember, this was "
                      "Gentile land; no Jewish town keeps pigs."),
        "must_show": "v11 — the herd itself: the vast spread of swine across the steep pasture above the sea; herdsmen small among them.",
        "must_not_show": "the steep bank down to the water must be visible in this frame — the geography the next beats need.",
        "scene": (
            "The great herd fills the steep morning hillside, the "
            "camera below the pasture behind a herdsman's distant "
            "figure — "
            "about two thousand dark and pink-grey pigs rooting "
            "and feeding across the high pasture in loose "
            "rivers, a few herdsmen with staffs small among "
            "them — and below the pasture the slope breaks over "
            "a steep scree bank that drops straight down to the "
            "deep blue water of the sea. An upright vertical "
            "photograph, the ground at the bottom of the frame "
            "and the sky at the top, the horizon level — the "
            "picture is the right way up."
        ),
    },
    {
        "id": "v2-r060-b23", "out": "s23-send-us-into-the-swine.jpeg", "seg": "n6 p2 + s12",
        "window": "132.46-139.03", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SHORE", "HERD"],
        "narration": ("And the spirits begged him: Send us into the "
                      "swine, that we may enter into them. (Mark 5:12)"),
        "must_show": "the plea with its object — the kneeling man's arm flung up toward the distant herd on the hill; Jesus following the gesture.",
        "must_not_show": "FLAG A: the plea comes through the man's own mouth and arm; nothing else visible asks.",
        "scene": (
            "The kneeling man's arm is flung up and out, one "
            "shaking finger pointing high at the herd spread "
            "across the hillside pasture above the beach, his "
            "face wrenched sideways with the begging — and Jesus "
            "stands with his eyes following the pointing arm up "
            "to the pigs, listening to the petition with the "
            "level face of a judge who has already ruled. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b24", "out": "s24-he-gave-them-leave.jpeg", "seg": "n6b p1-p3",
        "window": "139.03-144.25", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": ("Send us into the pigs, they said. Let us go into "
                      "them. And Jesus gave them leave."),
        "must_show": "the permission — close on Jesus: a single small nod, the sovereign economy of it; no gesture bigger than needed.",
        "must_not_show": "no wave of the arm, no drama — a nod that costs him nothing settles two thousand fates.",
        "scene": (
            "Close on Jesus's face in the morning light: the "
            "single, small, almost inaudible nod of permission — "
            "chin dipping once, eyes never leaving the kneeling "
            "man — sovereignty spending less motion on an army's "
            "eviction than other men spend on agreeing to lunch. "
            "Exactly one person is in the frame, with one head."
        ),
    },
    {
        "id": "v2-r060-b25", "out": "s25-down-the-steep-place.jpeg", "seg": "n6b p4",
        "window": "144.25-150.64", "wide": True, "jesus": False, "ref": False,
        "locks": ["HERD"],
        "narration": ("In an instant the whole herd stampeded down the "
                      "steep bank into the sea, and the water closed "
                      "over them."),
        "must_show": "v13, ONE WIDE beat — the stampede: the herd pouring over the steep bank toward the water in a single dark torrent; distance keeps it restrained.",
        "must_not_show": "R-law: WIDE only — no animal suffering close-up, no carcasses; the far white churn of water is as near as the frame goes.",
        "scene": (
            "From well down the shore the camera takes the bank in "
            "profile: the whole vast herd "
            "pours over the lip of the steep bank in one dark "
            "living torrent — a river of pigs plunging down the "
            "scree in full stampede, dust boiling up behind "
            "them — and at the slope's foot the sea churns white "
            "where the torrent meets it, the far water already "
            "closing over. The herdsmen stand frozen on the "
            "pasture above, staffs dropped. An upright vertical "
            "photograph, the ground at the bottom of the frame "
            "and the sky at the top, the horizon level — the "
            "picture is the right way up."
        ),
    },
    {
        "id": "v2-r060-b26", "out": "s26-they-ran-for-town.jpeg", "seg": "n6b p5",
        "window": "150.64-155.35", "wide": False, "jesus": False, "ref": False,
        "locks": ["HERD", "TOWN"],
        "narration": ("The men tending the pigs ran for town with the "
                      "story of their lives."),
        "must_show": "v14 — the herdsmen in full flight toward the town, staffs abandoned; the empty pasture behind them.",
        "must_not_show": "SHOT FROM THE SIDE so their direction toward the distant town reads at a glance.",
        "scene": (
            "SHOT FROM THE SIDE: the handful of herdsmen run "
            "flat-out from left to right across the frame along "
            "the hill path, robes hitched in their fists, arms "
            "pumping, staffs left lying in the emptied pasture "
            "behind them — and far ahead of them, IN THE "
            "DIRECTION THEY ARE RUNNING, the flat roofs of the "
            "Gentile town wait on its rise, about to hear the "
            "story of their lives. Every figure has two arms, "
            "two legs and one head."
        ),
    },
    {
        "id": "v2-r060-b27", "out": "s27-the-town-came-out.jpeg", "seg": "n7 p1",
        "window": "155.35-157.02", "wide": True, "jesus": False, "ref": False,
        "locks": ["TOWN", "SHORE"],
        "narration": "The whole town came out to see.",
        "must_show": "v14 — the outpouring: the town's people streaming down the road toward the shore in numbers.",
        "must_not_show": "curiosity and dread mixed — they come fast, but not gladly.",
        "scene": (
            "Down the road from the town, the camera at the road's "
            "side so the stream crosses in profile, the people pour toward "
            "the shore in a long hurrying stream — men striding "
            "grim, women with shawls clutched, elders hobbling "
            "to keep up, boys running ahead — a whole town "
            "emptied downhill by one impossible story, dread and "
            "curiosity driving the same feet. Mid-morning light. "
            "Every figure has two arms, two legs and one head."
        ),
    },
    {
        "id": "v2-r060-b28", "out": "s28-sitting-at-his-feet.jpeg", "seg": "n7 p2",
        "window": "157.02-164.45", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SHORE", "TOWN"],
        "narration": ("And what they found was the man they had chained "
                      "and lost and buried in their memory — sitting "
                      "quietly at the feet of Jesus."),
        "must_show": "v15 — THE after picture: the man SEATED at Jesus's feet, clothed in the borrowed tunic, still; the arriving town stopping dead at the sight.",
        "must_not_show": "before/after dignity: calm posture, ordinary clothing, quiet hands — the town's shock frames how complete it is.",
        "scene": (
            "On the stones by the boat the man sits quietly at "
            "Jesus's feet — clothed now in a plain dark "
            "olive-brown tunic, knees drawn up easy, his hands "
            "still in his lap, his wild hair pushed back from a "
            "settled face — and the front of the arriving crowd "
            "has stopped dead in mid-stride at the sight of him, "
            "a whole town's certainty failing at once. Jesus "
            "stands beside the seated man like a friend. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b29", "out": "s29-clothed-calm-right-mind.jpeg", "seg": "n7 p3-p5",
        "window": "164.45-167.96", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": "Clothed. Calm. In his right mind.",
        "must_show": "the restored face close — the same face from b06 with the occupation ended: quiet eyes, stillness, himself.",
        "must_not_show": "the echo of b06 must be recognizable — same man, same features, the hunted look simply gone.",
        "scene": (
            "Close on the man's face in the clean morning light: "
            "the same gaunt bones and black tangled beard as "
            "before — and everything else changed: the deep-set "
            "eyes quiet and single and his own, resting steady on "
            "something in the middle distance without flinching, "
            "the face of a house with one tenant again after "
            "years of the crowd. Exactly one person is in the "
            "frame, with one head."
        ),
    },
    {
        "id": "v2-r060-b30", "out": "s30-and-they-were-afraid.jpeg", "seg": "n7 p6-p7",
        "window": "167.96-176.67", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "TOWN", "SHORE"],
        "narration": ("And the scripture says a strange thing: they were "
                      "afraid. Power like that, standing on their beach, "
                      "had just cost them two thousand pigs."),
        "must_show": "v15-16 — the town's fear: faces measuring the healed man against the empty hillside; awe curdling into cost-counting.",
        "must_not_show": "no carcasses anywhere — the emptied pasture and the calm sea say what it cost; the fear is of the POWER.",
        "scene": (
            "The townspeople stand in a wary crescent on the "
            "stones, and their eyes do the arithmetic the frame "
            "shows: flicking from the clothed, quiet man sitting "
            "at Jesus's feet, up to the high pasture standing "
            "empty in the morning sun, and back to the still "
            "stranger at the centre of it all — awe going hard "
            "and cold in their faces as it turns into a sum of "
            "pigs. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r060-b31", "out": "s31-they-asked-him-to-leave.jpeg", "seg": "n7 p8",
        "window": "176.67-179.64", "wide": False, "jesus": True, "ref": REF,
        "locks": ["TOWN", "SHORE"],
        "narration": "So they asked Jesus to leave.",
        "must_show": "v17 — the request: a town elder's outstretched arm pointing back at the boat; regret and resolve mixed in the crowd.",
        "must_not_show": "not a mob — a formal, almost apologetic banishment; some faces in the crowd are ashamed of it.",
        "scene": (
            "A grey-bearded town elder stands a careful pace "
            "forward of the crowd, one arm stretched out stiffly "
            "toward the beached boat behind Jesus — the formal "
            "gesture of a request nobody is proud of — while "
            "behind him the crowd holds itself in a knot, some "
            "faces hard, several turned down and away, ashamed "
            "already of the asking. Jesus receives it without "
            "argument. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r060-b32", "out": "s32-he-never-argues-his-way-in.jpeg", "seg": "n8 p1-p2",
        "window": "179.64-183.73", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SHORE", "TOWN"],
        "narration": ("And he did. He never argues his way in where he "
                      "is not wanted."),
        "must_show": "the departure begun — Jesus turned and walking to the boat, no bitterness in his frame; the town watching him go.",
        "must_not_show": "no reproach in his posture — sorrow maybe; the going is as free as the coming.",
        "scene": (
            "Jesus walks the last stones to the boat — his back "
            "half-turned to the silent crowd, his stride "
            "unhurried and entirely without anger, one hand "
            "already on the gunwale — an invited-out guest "
            "leaving with more grace than the asking deserved, "
            "while the disciples steady the hull and the town "
            "watches him go in a stillness it does not "
            "understand yet. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r060-b33", "out": "s33-let-me-come-with-you.jpeg", "seg": "n8 p3",
        "window": "183.73-187.93", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SHORE"],
        "narration": ("But as he climbed into the boat, the healed man "
                      "begged to come with him."),
        "must_show": "v18 — the plea at the gunwale: the healed man gripping the boat's side, begging up at Jesus as it readies to push off.",
        "must_not_show": "desperation of love, not fear — he is begging TOWARD something for the first time in years.",
        "scene": (
            "At the waterline the healed man has both hands "
            "clamped on the boat's gunwale, knee-deep beside it, "
            "his settled new face broken open again — begging "
            "this time, urgent and human, to go where the boat "
            "goes — while Jesus, one foot up on the stern, turns "
            "back to the grip on his boat and the plea behind "
            "it. Morning sun on the water. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b34", "out": "s34-the-only-no.jpeg", "seg": "n8 p4-p5",
        "window": "187.93-196.06", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN"],
        "narration": ("It is the only time in the gospels someone asks "
                      "to follow Jesus and is told no. Listen to what he "
                      "was given instead."),
        "must_show": "the kind refusal — Jesus's hand on the man's shoulder over the gunwale, faces close: a no with a commission inside it.",
        "must_not_show": "the no must read WARM — a door redirected, not shut; both faces carry it.",
        "scene": (
            "Close over the gunwale: Jesus's hand rests firm on "
            "the healed man's shoulder, their faces near — the "
            "man's plea still standing in his eyes, and Jesus "
            "answering it with a steady warmth that is refusing "
            "and giving in the same look, the gentlest no in the "
            "gospels already turning into a sending. Exactly two "
            "people are in the frame; each visible hand has five "
            "fingers."
        ),
    },
    {
        "id": "v2-r060-b35", "out": "s35-go-home-to-thy-friends.jpeg", "seg": "j3",
        "window": "196.06-204.10", "wide": False, "jesus": True, "ref": REF,
        "locks": ["MAN", "SHORE", "TOWN"],
        "narration": ("Go home to thy friends, and tell them how great "
                      "things the Lord hath done for thee, and hath had "
                      "compassion on thee. (Mark 5:19)"),
        "must_show": "v19 — the commission: Jesus's arm extended past the man toward the town on its rise; the man turned to follow the pointing.",
        "must_not_show": "arm, man's facing, and town must line up — the geometry of a sending.",
        "scene": (
            "SHOT FROM THE SIDE at the waterline: Jesus stands in "
            "the stern with his arm extended full length, "
            "pointing past the healed man's shoulder toward the "
            "flat-roofed town on its rise — and the man has "
            "turned within the pointing, his body coming around "
            "to face the town he was chained in, the commission "
            "and its destination lined up along one line of the "
            "frame. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r060-b36", "out": "s36-to-the-town-that-chained-you.jpeg", "seg": "n9 p1-p3",
        "window": "204.10-212.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN", "TOWN"],
        "narration": ("To the town that chained you. To the people who "
                      "gave up on you. Tell them what God did for you, "
                      "and how he had compassion on you."),
        "must_show": "the resolve — the man alone on the road facing the town gate, squaring himself for the hardest audience on earth.",
        "must_not_show": "SHOT FROM BEHIND him — his back to us, the town ahead; the boat already small on the water behind.",
        "scene": (
            "SHOT FROM BEHIND THE MAN on the road up from the "
            "shore: his back and shoulders to the camera, faced "
            "squarely at the town gate ahead of him, one breath "
            "visibly being taken and set — and far behind him, "
            "small out on the bright water at the frame's lower "
            "edge, the boat is already pulling away east. An "
            "upright vertical photograph, the ground at the "
            "bottom of the frame and the sky at the top, the "
            "horizon level — the picture is the right way up. "
            "Exactly one person is in the frame on the road."
        ),
    },
    {
        "id": "v2-r060-b37", "out": "s37-the-first-one-sent.jpeg", "seg": "n9 p4a",
        "window": "212.57-218.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN", "TOWN"],
        "narration": ("The man everyone had written off became the "
                      "first person Jesus ever sent out with his story —"),
        "must_show": "the telling begun — the man inside the town, speaking to a stunned gathering knot of the very people who avoided him.",
        "must_not_show": "recognition on the townspeople's faces — they KNOW him; that is what stuns them.",
        "scene": (
            "In the town's stone lane the man stands telling it — "
            "clothed, calm, his scarred-free hands open in the "
            "middle of the story — while around him a knot of "
            "townspeople thickens by the second: a woman who "
            "crossed streets to avoid him gripping her neighbour, "
            "an old man peering as if at a ghost, a boy pushed "
            "forward to see — the town's warning, standing in "
            "the market telling them about compassion. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r060-b38", "out": "s38-a-one-man-mission.jpeg", "seg": "n9 p4b",
        "window": "218.00-222.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": ("a one-man mission to the ten Gentile cities of "
                      "the Decapolis."),
        "must_show": "the scale of the sending — the man small on a high road between cities, columned Gentile skylines far ahead and behind.",
        "must_not_show": "SHOT FROM BEHIND — his back to us, walking his mission road toward the next city.",
        "scene": (
            "SHOT FROM BEHIND AND HIGH: the man walks alone AWAY "
            "from us along a broad high road through open "
            "country, staff swinging, steady — and far ahead of "
            "him, IN THE DIRECTION HE IS WALKING, a columned "
            "Gentile city stands on the plain, while the roofs "
            "of the one he has just finished with lie small "
            "behind him at the frame's edge — one healed man, "
            "ten cities, on foot. An upright vertical "
            "photograph, the ground at the bottom of the frame "
            "and the sky at the top, the horizon level — the "
            "picture is the right way up. Exactly one person is "
            "on the road."
        ),
    },
    {
        "id": "v2-r060-b39", "out": "s39-all-men-did-marvel.jpeg", "seg": "n9 p5",
        "window": "222.57-225.65", "wide": False, "jesus": False, "ref": False,
        "locks": ["MAN"],
        "narration": "And everywhere he went, people were amazed.",
        "must_show": "v20 — the closing frame: the man mid-story in a city square, a big Gentile crowd caught in open amazement around him.",
        "must_not_show": "his face carries the whole gospel of the build: the man from the tombs, believed.",
        "scene": (
            "In a columned Gentile market square the man stands "
            "at the centre of a large listening crowd — porters "
            "with loads set down, merchants leaned out over "
            "their stalls, women with jars parked on hips, every "
            "face open in plain amazement — while he tells it "
            "with his arms wide and his settled face alight, the "
            "man from the tombs, standing in a city that has "
            "never seen Jesus, making them marvel at him anyway. "
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
    "TOMBS": "PLACE-REF/tombs.jpeg",  # build-37-rich-man-lazarus v2-r037-b45
    "TOWN": "PLACE-REF/town.jpeg",  # build-38-persistent-widow v2-r038-b46
}
# === end PLACE-PLATES ===
