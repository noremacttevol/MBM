#!/usr/bin/env python3
"""V2 beat map — row 19, build-19-shore (John 21:1-17), realistic rebuild.

COVERAGE: 37 pictures against V1's 16, over 149.30 s = 4.0 s/picture.

⚠️ WINDOWS WERE RE-TIMED FROM SCRATCH 2026-08-01 (Claude worker 13). The inherited
27-beat map ran on a **136.1 s** timeline against the real **157.76 s** (the story
ends and the closing card starts at 149.583 s) — every window after the first was
adrift, by more than 13 s at the end. It also named a `PETER` and a `JOHN` lock the
build never defined, and it was written against a STALE narration script: the copy of
`make_narration.py` sitting in this V2 folder (2026-07-28) predates the authoritative
one in the V1 build folder (2026-07-29) and is missing the retellings that were added
to n5b / n5c / n11 / n12 so no KJV line lands unexplained. VERIFY THE ARTEFACT, NEVER
THE PROSE: every window below was recomputed from the fixed `extract_beats.py` reading
the V1 build, then split on each segment's own phrase boundaries in
`audio/*.timing.json`. Contiguous 0.28 s → 149.583 s, zero gaps, zero overlaps.

The AUTHORITATIVE audio is `media-production/build-19-shore/audio/` — 44.1 kHz /
128 kbps ElevenLabs, the same files the shipped V1 mp4 carries, so REDO-ALL is already
satisfied and nothing is re-voiced. `v2_assemble.py` copies that AAC stream
packet-for-packet.

⚠️ THE SETTING IS WHERE THE MONEY GOES ON THIS ROW. Row 19 is the first V2 build whose
whole second half is an open BOAT, a SHORE and a CHARCOAL FIRE. Those three invite
first-time defects that no earlier build's locks cover: modern boat hardware (machined
cleats, screws, nylon rope, a painted or fibreglass hull, an outboard), the wrong fire
(a leaping camp fire or a metal grill instead of a bed of charcoal embers), the wrong
net (monofilament mesh and moulded plastic floats), and the wrong light (midday sun or
a sunset palette where the text says first light). Every one of those is stated
POSITIVELY and up front — in the shared LOCKS below and in the PERIOD-MATERIALS block
promoted into `v2_prompt.py` — never in one beat's prose.

⚠️ TIME OF DAY IS THE STORY'S OWN CLOCK AND IT IS NOT NEGOTIABLE:
  b01              warm indoor lamplight, before everything (the vow)
  b02-b03          the NIGHT of the denial, courtyard coals and black shadow
  b04-b06          the empty NIGHT on the water, one clay lamp at the bow
  b07-b18          "when the morning was now come" — flat grey-blue first light,
                   the eastern sky just paling, the sun not yet up, no colour in it
  b19-b37          the sun clearing the eastern hills — low, level, warming gold
NO MIDDAY ANYWHERE. NO SUNSET PALETTE ANYWHERE: this is sunrise, the light comes up
and never goes down, and the warm light always arrives LOW FROM THE EAST, across the
water toward the shore.

SCRIPTURE FACTS (John 21:1-17 KJV):
  v2   Seven men are in the boat: Simon Peter, Thomas, Nathanael, the two sons of
       Zebedee, and two other disciples. Seven, and the frames keep seven.
  v3   "I go a fishing ... and that night they caught NOTHING."
  v4   "when the morning was now come, Jesus stood on the shore: but the disciples
       KNEW NOT that it was Jesus." The not-knowing is done by DISTANCE and by the
       flat grey light, never by a hood, a shadowed face or a disguise — the V2 law
       is one locked face, shown. The gap between what the viewer sees and what they
       see is the first half of the video.
  v5   "Children, have ye any meat? They answered him, No." One word.
  v6   "Cast the net on the RIGHT SIDE of the ship" — the side is stated, so the
       picture states it: the net goes over the starboard rail.
  v7   "that disciple whom Jesus loved saith unto Peter, IT IS THE LORD." John says
       it, not Peter. b14 puts the line in John's mouth and Peter only reacts.
  v7   "he GIRT HIS FISHER'S COAT unto him, (for he was naked,) and did CAST HIMSELF
       INTO THE SEA." He puts clothes ON to jump — the opposite of what a swimmer
       does, and it is what the text says.
  v9   "they saw a FIRE OF COALS there, and fish laid thereon, and bread."
  v9   The word for that charcoal fire (anthrakia) appears exactly twice in the whole
       New Testament: here, and at the courtyard fire Peter warmed himself at while he
       denied him (John 18:18). The narration is built on that; b20-b21 are where it
       lands, and b02's brazier is deliberately the same bed of coals so the rhyme is
       visible.
  v15  "Simon, son of Jonas" — his OLD name, from before he was ever called Peter.
  v17  "Peter was GRIEVED because he said unto him the third time." That is b32.

CONTENT-CARE: row 19 is GREEN. v7's "for he was naked" is handled the way a working
boat handles it — he is stripped to a plain knee-length working loincloth and is
PULLING HIS COAT ON as he goes over the side. Nothing is exposed and nothing is dwelt
on; the frame is about the leap. The denial is shown only as Peter's face and Peter's
grief — no violence, no trial, no cross anywhere in this build.
"""

LOCKS = {
    "SEA-NIGHT": (
        "SEA-OF-GALILEE-NIGHT LOCK: the open lake in the dark hours before dawn — "
        "flat black water moving in long slow swells with faint starlight broken on "
        "it, the low hills of the far shore only a slightly darker band against a "
        "deep blue-black sky, and no other light on the whole lake. The ONLY light in "
        "the frame is the small warm flame of one clay saucer lamp at the boat's bow "
        "and the cold blue of the night sky itself; every face is lit either by that "
        "one small warm flame from below or by dim blue skylight. There is no moon "
        "bright enough to read by, no lit town, no lamp on the shore, no glow on the "
        "horizon, and no other boat's light anywhere."
    ),
    "SHORE-DAWN": (
        "SHORE-AT-FIRST-LIGHT LOCK: the shingle and sand shore of the Sea of Galilee "
        "as the morning comes — wet dark stones and packed damp sand at the "
        "waterline, dry pale sand and coarse grass higher up, the flat pale water "
        "reaching out to the low bare brown hills of the far side, and the eastern "
        "sky over those hills paling from grey into thin gold. The light is LOW, "
        "LEVEL AND FROM THE EAST, coming in across the water toward the beach and "
        "throwing long soft shadows up the sand. This is SUNRISE and the light is "
        "rising: cool grey-blue washing to clear pale gold, never the heavy orange, "
        "red or purple of a sunset, and never the short hard shadows of midday. The "
        "shore is empty country — no harbour, no jetty, no pier, no dock, no mooring "
        "post, no building, no wall, no road and no town anywhere on it."
    ),
    "BOAT": (
        "GALILEAN-BOAT LOCK: one open first-century fishing boat about eight paces "
        "long, built entirely of hand-hewn cedar and oak — thick overlapping planks "
        "dark and swollen with water, joined with wooden pegs and hand-forged iron "
        "nails hammered flat, caulked with pitch, the grain and the adze marks plainly "
        "visible. A low solid gunwale runs unbroken around the whole hull, with open "
        "deck planking laid across the frames so the deck is always visible under the "
        "men's bare feet. A short stepped mast with a coarse linen sail furled and "
        "lashed to its yard, long wooden oars resting in leather-strapped tholes, "
        "coiled hand-twisted flax rope, a wooden bailing scoop, clay jars wedged "
        "against the frames, and one small clay saucer oil lamp at the bow. Every "
        "fitting is wood, hand-forged iron, leather or rope. The hull is bare "
        "weathered wood, never painted, never varnished, never white."
    ),
    "NET": (
        "NET LOCK: a large hand-knotted fishing net of natural flax and hemp cord — "
        "coarse ropey twine the colour of straw and wet tea, hand-tied knots at every "
        "crossing, the mesh irregular and visibly made by hand, weighted along one "
        "edge with small pierced grey stones and drilled lead sinkers and floated "
        "along the other with pieces of shaped cork bark and hollow gourd. Soaked "
        "sections are dark and heavy and drip; dry sections are pale and stiff. The "
        "net is never fine transparent monofilament, never bright synthetic mesh, and "
        "carries no moulded, coloured or manufactured float of any kind."
    ),
    "CREW": (
        "CREW LOCK: exactly SEVEN men are aboard this boat and no eighth — Peter, "
        "John, and five other working Galilean fishermen between twenty-five and "
        "forty. The five are the same five men in every frame: tired, unshaven, hair "
        "damp with spray, sleeves pushed back over forearms scarred by rope, bare feet "
        "on the deck. They wear plain rough wool tunics in SATURATED DEEP colours — "
        "rust brown, deep russet, dark olive, blue-grey, dusty indigo — with rope "
        "belts. NONE OF THEM WEARS CREAM, OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH "
        "anywhere on his body, in focus or out of focus. Their faces are shown "
        "clearly, each man a different face, and no face is cloned from another."
    ),
    "FIRE": (
        "CHARCOAL-FIRE LOCK: a small fire of CHARCOAL EMBERS burnt down in a shallow "
        "hollow scooped in the damp sand and ringed with a few beach stones — a bed of "
        "glowing red-orange coals under a soft grey crust of ash, breathing heat, with "
        "only the smallest blue-edged flickers licking up between the lumps and a thin "
        "grey smoke leaning sideways in the morning air. It is a bed of embers, not a "
        "camp fire: no leaping yellow flames, no burning logs, no branches, no "
        "bonfire. Two whole fish lie cooking directly across the coals on a flat "
        "blackened stone, their skin blistering, and a round flat loaf of dark "
        "hand-baked bread sits on a second stone at the fire's edge. There is no metal "
        "grill, grate, grid, tripod, skewer, pan or pot of any kind — the food rests "
        "on stone and coals only."
    ),
    "COURTYARD": (
        "COURTYARD-NIGHT LOCK: the high priest's courtyard on the night of the denial "
        "— a walled yard of large pale dressed stone blocks standing in deep darkness, "
        "with a bed of charcoal coals burning low and red in a plain hand-forged iron "
        "brazier in the middle of it. Servants, a doorkeeper girl and temple officers "
        "stand close in around that heat in dark wool cloaks, their faces lit orange "
        "FROM BELOW by the coals, and everything beyond the reach of that small red "
        "light is black. THE COALS ARE THE ONLY LIGHT SOURCE IN THE FRAME: no torch "
        "flame, no lamp on a wall, no lantern, no glass, no moonlight, no fill light "
        "from anywhere, and no lit window behind them."
    ),
}

OUTPUT_VIDEO_NAME = "john-21_breakfast-on-the-shore-realistic-v2.mp4"

REF = True

BEATS = [
    # ------------------------------------------- n1 — the vow, before it all ----
    {
        "id": "v2-r019-b01", "out": "s01-he-swore-he-never-would.jpeg", "seg": "n1",
        "window": "0.28-4.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Peter had sworn he would die before he would ever deny Jesus.",
        "must_show": "Peter mid-vow, one fist against his own chest, absolutely certain, in warm indoor lamplight before any of it happened.",
        "must_not_show": "no courtyard, no fire of coals, no boat, no shore, no night sky. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime lens wide open, shallow depth of field, fine "
            "film grain. Close on Peter indoors at night, lit only by one clay saucer "
            "lamp standing on a table just out of frame at his right, its small warm "
            "flame raking across his cheek and leaving the room behind him in soft "
            "brown darkness. He is mid-vow: his own big fist pressed hard against his "
            "chest, his chin lifted, his brows drawn, his eyes fierce and shining with "
            "total conviction, mouth open on the word. He is speaking to someone "
            "seated below and to his left, and his eyes travel down and out of the "
            "left edge of the frame, well off the camera axis. He has one head, two "
            "arms and two complete hands."
        ),
    },
    # ---------------------------------------- n2 — the denial and the grief ----
    {
        "id": "v2-r019-b02", "out": "s02-he-denied-him-three-times.jpeg", "seg": "n2 p1",
        "window": "4.66-7.79", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "COURTYARD"],
        "narration": "Then, in one terrible night, he denied him three times.",
        "must_show": "Peter at the courtyard coals denying it — his palm up and out, pushing the accusation away, half turned from the servant girl who is pointing at him.",
        "must_not_show": "no violence, no soldiers striking anyone, no trial, no cross, no rooster. Jesus is not in this frame.",
        "scene": (
            "One photograph, 35mm lens, handheld, high ISO grain. THE CAMERA STANDS "
            "BEHIND AND JUST BEYOND THE CIRCLE OF SERVANTS AND SHOOTS PAST THEIR BACKS "
            "ACROSS THE BRAZIER: two dark cloaked backs fill the near left of the "
            "frame, out of focus and lit red along their edges, and Peter is beyond "
            "the coals on the far side, half turned away, caught in the act of "
            "denying. His right palm is up and out, pushing the accusation away, his "
            "head is turned sharply to his own left toward a young servant girl whose "
            "arm is raised pointing at him, and his eyeline exits the left edge of the "
            "frame. NOT ONE FACE IS TURNED TOWARD THE LENS. His face is lit orange "
            "from below by the coals and his eyes are wide and frightened under it. "
            "Black night above and behind everyone."
        ),
    },
    {
        "id": "v2-r019-b03", "out": "s03-he-wept-bitterly.jpeg", "seg": "n2 p2",
        "window": "7.79-14.25", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "COURTYARD"],
        "narration": ("The rooster crowed, Jesus turned and looked at him, and Peter "
                      "went out and wept bitterly."),
        "must_show": "Peter alone outside in the dark, doubled over against a black stone wall, wrecked — the courtyard coals small and red far behind him.",
        "must_not_show": "do NOT show Jesus or the look itself. No trial scene, no soldiers, no rooster on a wall, no dawn light yet.",
        "scene": (
            "One photograph, 40mm lens, very high ISO, heavy grain, almost no light. "
            "THE CAMERA IS OUT IN THE DARK ALLEY BESIDE PETER AND SHOOTS ALONG THE "
            "WALL PAST HIS SHOULDER, so he is seen from behind and in three-quarter "
            "from behind and no part of his face is turned to the lens. He has got out "
            "of the courtyard and is alone against a black stone wall, doubled over, "
            "one forearm braced flat on the stone with his forehead pressed against "
            "it, his other hand clamped over his face, his whole back and shoulders "
            "shaking. Far behind him through the gateway the bed of coals still burns "
            "small and red with two dark figures standing around it, neither of them "
            "looking his way. Deep night and hard black shadow; the only light is the "
            "distant red of the coals and a faint cold blue along the top of the wall. "
            "He has one head, two arms and two complete hands."
        ),
    },
    # --------------------------------- n3 / n4 — back to the old life, at sea ----
    {
        "id": "v2-r019-b04", "out": "s04-back-to-the-old-life.jpeg", "seg": "n3",
        "window": "14.25-19.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT", "NET", "SEA-NIGHT"],
        "narration": ("After the resurrection, Peter went back to fishing. Back to the "
                      "old life."),
        "must_show": "the seven men putting out from an empty beach in the dark, Peter shoving the boat off the shingle, going back to the work he knew.",
        "must_not_show": "no daylight, no dawn colour yet, no fire on the beach, no other boats, no harbour or jetty. Jesus is not in this frame.",
        "scene": (
            "One photograph, 35mm lens, long-exposure grain, almost monochrome blue. "
            "THE CAMERA STANDS ON THE BEACH BEHIND THE MEN AND SHOOTS OUT OVER THEIR "
            "BACKS TOWARD THE OPEN BLACK WATER: their backs and shoulders fill the "
            "near frame in silhouette, every man is seen from behind or in profile, "
            "and NOT ONE FACE IS TURNED TOWARD THE LENS. Peter is nearest, thigh deep "
            "in the shallows with both hands on the stern shoving the loaded boat off "
            "the shingle, his back to us and his head turned in profile toward the "
            "lake. Two men are already aboard hauling the folded net over the gunwale "
            "and the others are wading out alongside. The one clay lamp at the bow is "
            "the only warm point of light in the whole picture; everything else is the "
            "cold blue-black of the middle of the night."
        ),
    },
    {
        "id": "v2-r019-b05", "out": "s05-they-worked-all-night.jpeg", "seg": "n4 p1-p2",
        "window": "19.80-25.28", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT", "NET", "SEA-NIGHT"],
        "narration": ("It is what people do with a failure they cannot carry. They go "
                      "back to what they knew before it happened."),
        "must_show": "the middle of the night out on the black water — the men hauling the wet net back aboard hand over hand, working the way men work when they are trying not to think.",
        "must_not_show": "no fish in the net. No dawn, no shore, no light on the horizon. Jesus is not in this frame.",
        "scene": (
            "One photograph, 35mm lens, high ISO, heavy grain. THE CAMERA IS LOW IN "
            "THE BOTTOM OF THE BOAT ITSELF, BEHIND THE MEN, SHOOTING FORWARD PAST "
            "THEIR BACKS over the gunwale to the black water: the deck planking runs "
            "away from the lens under their bare feet, three men stand with their "
            "backs to us hauling the streaming net in hand over hand, and Peter is "
            "beyond them in hard profile against the night sky, both fists closed on "
            "the wet cord, his jaw set and his eyes down on the water rather than on "
            "the work. NOT ONE FACE IS TURNED TOWARD THE LENS. The single bow lamp "
            "lights their arms and the wet rope from one side only and leaves the rest "
            "of the lake completely black. Water runs off the net onto the deck."
        ),
    },
    {
        "id": "v2-r019-b06", "out": "s06-they-caught-nothing.jpeg", "seg": "n4 p3",
        "window": "25.28-28.27", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "NET", "BOAT"],
        "narration": "And that night they caught nothing.",
        "must_show": "the empty net — a heap of soaked hand-knotted cord in Peter's hands with nothing in it at all, and his face above it, beaten.",
        "must_not_show": "not one fish anywhere in the frame, not even a small one. No dawn light, no shore. Jesus is not in this frame.",
        "scene": (
            "One photograph, 50mm prime, shallow depth of field, grain. Close and low "
            "on the sodden net heaped in the bottom of the boat, lit dimly from one "
            "side by the bow lamp — every wet knot and strand sharp in the foreground, "
            "water still running out of it across the deck planking, and the mesh "
            "completely and obviously EMPTY. Peter's two big rope-scarred hands hang "
            "open in it, still holding a fold of cord he has stopped pulling. Above "
            "and behind, softly out of focus, his face is tipped down toward the empty "
            "mesh, exhausted and blank; his eyes are on the net, low and well below "
            "the camera, and his head is turned off the camera axis."
        ),
    },
    # ------------------------------- n5 / j0a — the figure on the shore ----
    {
        "id": "v2-r019-b07", "out": "s07-a-figure-on-the-shore.jpeg", "seg": "n5",
        "window": "28.27-32.69", "wide": True, "jesus": True, "ref": True,
        "locks": ["CREW", "BOAT", "SHORE-DAWN"],
        "narration": "At dawn, a figure on the shore called out across the water to the boat.",
        "must_show": "seen from the boat: the morning has come, and a man stands alone at the far waterline, small with distance — near enough to hail, too far for the men to know him.",
        "must_not_show": "he is NOT hooded, NOT in shadow, NOT turned away and NOT disguised in any way — the distance alone does the not-knowing. No halo, no glow, no light coming off him. No sunset colour.",
        "scene": (
            "One photograph, 50mm lens, deep focus, grain. THE CAMERA IS IN THE BOAT "
            "BEHIND TWO OF THE MEN AND SHOOTS PAST THEM TOWARD THE LAND: their dark "
            "backs and shoulders stand out of focus across the bottom and left of the "
            "frame, seen entirely from behind, and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. Beyond them lies a hundred paces of flat pale water, and then the "
            "empty beach, where Jesus stands alone at the waterline. He is SMALL WITH "
            "DISTANCE — a whole standing figure perhaps a tenth of the frame's height "
            "— facing out over the water toward the boat with his face plainly open to "
            "the morning and completely unhidden, but far too distant for the men to "
            "read. His cream robe is the palest thing on the beach. Behind him the low "
            "brown hills, and above them the eastern sky just paling from grey to thin "
            "gold; the sun is not up yet and the light is flat, cool and colourless."
        ),
    },
    {
        "id": "v2-r019-b08", "out": "s08-children-have-ye-any-meat.jpeg", "seg": "j0a",
        "window": "32.69-35.50", "wide": False, "jesus": True, "ref": True,
        "locks": ["SHORE-DAWN"],
        "narration": "Children, have ye any meat?",
        "must_show": "Jesus mid-call at the waterline, calling out across the water to the boat — an easy, almost domestic question shouted over open water.",
        "must_not_show": "no halo, no glow, no rim-light, no beam of light. Not a solemn posed portrait — he is in the middle of shouting. No sunset colour, no midday sun.",
        "scene": (
            "One photograph, 135mm lens from far out on the water, compressed "
            "perspective, shallow focus, grain. A medium shot of Jesus standing "
            "ankle-deep at the waterline on the wet sand, caught mid-call: his weight "
            "on his front foot, his chest open, his head lifted and turned out across "
            "the lake to his left, his mouth open on the word and one hand raised "
            "loosely beside his mouth. His whole face is clear and unshadowed and "
            "there is warmth and humour in it, as though he already knows the answer. "
            "His eyeline runs far out over the water and exits the LEFT edge of the "
            "frame, nowhere near the lens. Flat cool grey-gold first light from the "
            "east across the water; the far hills and the sky behind him are soft and "
            "out of focus. Thin smoke from something low behind him drifts at the "
            "right edge of the frame."
        ),
    },
    # ----------------------------------------- n5b — the one-word answer ----
    {
        "id": "v2-r019-b09", "out": "s09-they-had-to-say-it-out-loud.jpeg", "seg": "n5b p1-p2",
        "window": "35.50-40.65", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT", "NET", "SHORE-DAWN"],
        "narration": ("Have you caught anything, he called. And they had to say it out "
                      "loud to a stranger — no."),
        "must_show": "the men in the boat calling one word back across the water to a stranger they cannot place — the small humiliation of having to say it out loud.",
        "must_not_show": "no fish. No warm gold light yet — the sun is still behind the hills. Jesus is not in this frame.",
        "scene": (
            "One photograph, 35mm lens, deep focus, grain. THE CAMERA IS AT THE STERN "
            "OF THE BOAT BEHIND ALL SEVEN MEN AND SHOOTS FORWARD PAST THEM TOWARD THE "
            "DISTANT SHORE: their backs and the backs of their heads fill the middle "
            "of the frame, the deck planking and the coiled flax rope run away under "
            "them, and NOT ONE FACE IS TURNED TOWARD THE LENS. Peter stands at the "
            "gunwale in three-quarter from behind with one hand cupped at the side of "
            "his mouth, shouting the single word back over the water; his head is "
            "turned away toward the far shore and his eyeline exits the top left of "
            "the frame. Another man beside him has both hands open and empty in a flat "
            "shrug. The empty net lies heaped and dripping at their feet. Cool flat "
            "grey-blue first light, the eastern sky just going gold behind the far "
            "hills."
        ),
    },
    {
        "id": "v2-r019-b10", "out": "s10-nothing-all-night-nothing.jpeg", "seg": "n5b p3-p4",
        "window": "40.65-44.05", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "NET", "BOAT"],
        "narration": "Nothing. All night, nothing.",
        "must_show": "close on Peter's face in the grey first light — a whole night's work for nothing, on top of everything else he is already carrying.",
        "must_not_show": "no fish, no shore, no warm gold light. Not a posed portrait. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime wide open, very shallow depth of field, grain. "
            "Tight on Peter's face and one shoulder in the flat cool light of first "
            "morning, three-quarter from the side, his head turned away from the "
            "camera toward the water so his eyeline exits the right edge of the frame "
            "well past the lens. Salt dried white in his beard, wet hair stuck to his "
            "forehead, dark hollows under his eyes, his mouth a flat tired line. It is "
            "not only the fish. Out of focus below him the pale straw-coloured cord of "
            "the empty net is bunched over the gunwale, and beyond him the water and "
            "the far shore melt into a soft grey blur."
        ),
    },
    # ------------------------------- j0b / n5c — cast on the right side ----
    {
        "id": "v2-r019-b11", "out": "s11-cast-on-the-right-side.jpeg", "seg": "j0b",
        "window": "44.05-48.12", "wide": True, "jesus": True, "ref": True,
        "locks": ["SHORE-DAWN"],
        "narration": "Cast the net on the right side of the ship, and ye shall find.",
        "must_show": "Jesus on the beach calling the instruction out over the water, his arm extended, pointing clearly to one particular side of the distant boat.",
        "must_not_show": "no halo, glow, rim-light or light coming off him. He is not standing on the water — he is on wet sand. No sunset colour.",
        "scene": (
            "One photograph, 50mm lens, deep focus, grain. THE CAMERA STANDS UP THE "
            "BEACH BEHIND AND TO ONE SIDE OF JESUS AND SHOOTS PAST HIS SHOULDER OUT "
            "OVER THE WATER, so he is seen in three-quarter from behind and his face "
            "is turned away toward the lake: the back and side of his head, his dark "
            "hair moving in the offshore air, and his right arm out straight and level "
            "pointing across the water to the far side of the small distant boat. His "
            "eyeline runs out to the boat and exits the top left of the frame. Beyond "
            "his pointing hand, far out on the flat pale water, the boat sits small "
            "with seven tiny figures aboard, all of them turned toward him. Wet sand "
            "and dark stones under his sandals in the near foreground. Flat cool first "
            "light coming in low from the east across the water."
        ),
    },
    {
        "id": "v2-r019-b12", "out": "s12-over-the-right-side.jpeg", "seg": "n5c p1",
        "window": "48.12-51.83", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT", "NET", "SHORE-DAWN"],
        "narration": ("Put the net over the right side, he told them, and you will find "
                      "some."),
        "must_show": "the men doing it — the heavy hand-knotted net swinging out and away over the RIGHT-HAND rail of the boat, mid-throw, the water not yet broken.",
        "must_not_show": "no fish yet, this is the moment before. No warm gold light yet. Jesus is not in this frame.",
        "scene": (
            "One photograph, 24mm lens close in, deep focus, grain, a fast shutter "
            "freezing the water drops. THE CAMERA IS INSIDE THE BOAT AT THE MAST, "
            "BEHIND THE MEN, SHOOTING ACROSS THE DECK AND OUT OVER THE RIGHT-HAND "
            "GUNWALE: two backs are large in the near frame, seen entirely from "
            "behind, and NOT ONE FACE IS TURNED TOWARD THE LENS. The net is in the "
            "air, mid-throw, thrown open in a wide arc out over the starboard rail "
            "with its stone weights swinging below the spread edge and drops flying "
            "off the wet cord; the far edge of it is just about to touch the flat pale "
            "water. Peter is at the rail in profile with his arms still following the "
            "throw through, his eyes down on the water where the net will land. Deck "
            "planking under everyone's bare feet, the gunwale running unbroken past "
            "them. Cool grey-gold first light from the east."
        ),
    },
    {
        "id": "v2-r019-b13", "out": "s13-so-full-they-could-not-haul-it.jpeg", "seg": "n5c p2",
        "window": "51.83-56.88", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT", "NET", "SHORE-DAWN"],
        "narration": "They did — and it came up so full they could not haul it in.",
        "must_show": "the net so packed with fish that grown men leaning back on it cannot lift it — the water boiling with silver, the boat heeling toward the load.",
        "must_not_show": "the net is not in the boat and is not emptied out on the deck; it is still in the water and still winning. Jesus is not in this frame.",
        "scene": (
            "One photograph, 28mm lens, deep focus, fast shutter, spray in the air, "
            "grain. THE CAMERA IS IN THE BOTTOM OF THE BOAT BEHIND THE STRAINING MEN "
            "AND SHOOTS FORWARD PAST THEM AND OVER THE RIGHT-HAND GUNWALE: four backs, "
            "shoulders and braced legs fill the near frame, every man seen from behind "
            "or in hard profile, feet skidding on the wet deck planking, and NOT ONE "
            "FACE IS TURNED TOWARD THE LENS. They are leaning back almost horizontal "
            "with the wet cord biting into their palms and it is not moving. Beyond "
            "the rail the water is boiling white and silver with fish packed solid "
            "inside the strained mesh, backs and tails breaking the surface, the whole "
            "hull heeled over toward the load and water lipping at the gunwale. Peter "
            "is nearest, in profile, both fists locked on the rope, his mouth open "
            "shouting to the others, his eyes down on the net. Cool gold-grey first "
            "light, the spray lit from the east."
        ),
    },
    # ------------------------------- n6 — the recognition and the leap ----
    {
        "id": "v2-r019-b14", "out": "s14-it-is-the-lord.jpeg", "seg": "n6 p1",
        "window": "56.88-60.10", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOHN", "PETER", "BOAT", "SHORE-DAWN"],
        "narration": "Then one of them went very still and said, it is the Lord.",
        "must_show": "John gone completely still in the middle of all that work, staring at the far shore, saying the words quietly — and Peter beside him beginning to turn.",
        "must_not_show": "John is clean-shaven and about twenty; he is never given a beard. Nobody is shouting or excited yet — the stillness is the point. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime wide open, very shallow depth of field, grain. "
            "A tight two-shot in the boat. John is sharp in the near frame in "
            "three-quarter profile, the rope forgotten and slack in his hands, "
            "absolutely motionless, his young clean-shaven face lifted toward the "
            "distant shore with his lips just parted on the words; his eyeline runs "
            "far out past the left edge of the frame, nothing near the lens. Behind "
            "him and softly out of focus, Peter has heard it and is beginning to turn "
            "his head the same way, his hands still on the wet net. Cool first light "
            "on both their faces from the east; the water and the far shore behind "
            "them are a pale grey-gold blur."
        ),
    },
    {
        "id": "v2-r019-b15", "out": "s15-it-hits-peter.jpeg", "seg": "n6 p2a",
        "window": "60.10-62.08", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "And Peter did not wait for the boat.",
        "must_show": "the instant it lands on Peter — recognition and terror and longing all at once, already coming up off his heels.",
        "must_not_show": "no smile, no calm. Not a posed portrait. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime wide open, extremely shallow depth of field, "
            "grain, a fast shutter freezing him mid-move. Very tight on Peter's face "
            "and shoulders, turned three-quarter away toward the shore, his head "
            "already swinging round so his eyeline shoots hard out of the upper left "
            "corner of the frame and nowhere near the lens. His eyes are wide and wet "
            "and enormous, his mouth open, his whole face breaking open at once with "
            "recognition, fear and want. His weight is already coming forward off his "
            "heels and his wet hair swings with the turn. Cool pale first light from "
            "the east; everything behind him is a soft blur of water."
        ),
    },
    {
        "id": "v2-r019-b16", "out": "s16-he-threw-himself-in.jpeg", "seg": "n6 p2b",
        "window": "62.08-64.80", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT", "SHORE-DAWN"],
        "narration": "He threw himself into the sea",
        "must_show": "Peter going over the gunwale into the water, still pulling his fisher's coat on as he goes — the coat half over one shoulder, mid-air, the crew left holding the net.",
        "must_not_show": "nothing exposed and nothing dwelt on: he wears a plain knee-length working loincloth and is PUTTING CLOTHES ON, not taking them off. No nudity. Jesus is not in this frame.",
        "scene": (
            "One photograph, 24mm lens, fast shutter freezing the spray, deep focus, "
            "grain. THE CAMERA IS IN THE BOAT BEHIND PETER SHOOTING PAST HIM OVER THE "
            "SIDE, so he is seen entirely from behind and above: his broad back, the "
            "rough dun fisher's coat dragged half on over one shoulder with the other "
            "arm still finding its sleeve, a plain knee-length working loincloth "
            "belted at his waist, both bare legs already out over the low gunwale and "
            "off the deck, his body committed to the air above the water. His face is "
            "away from us toward the distant shore. In the near frame the other men "
            "are still braced against the loaded net, seen from behind, one head "
            "turning after him; NOT ONE FACE IS TURNED TOWARD THE LENS. Below him the "
            "flat pale water waits, unbroken. Cool low gold first light from the east."
        ),
    },
    {
        "id": "v2-r019-b17", "out": "s17-and-swam-for-shore.jpeg", "seg": "n6 p3",
        "window": "64.80-67.86", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "BOAT", "SHORE-DAWN"],
        "narration": "and swam for shore, leaving everything behind.",
        "must_show": "Peter swimming hard for the beach with the loaded boat and the whole catch left behind him — the biggest catch of his life abandoned without a thought.",
        "must_not_show": "he is not walking on the water and not standing on it — he is swimming in it. Jesus is not in this frame.",
        "scene": (
            "One photograph, 35mm lens low to the surface, deep focus, water drops on "
            "the front element, grain. THE CAMERA IS DOWN AT WATER LEVEL BEHIND AND TO "
            "THE SIDE OF PETER, SHOOTING PAST HIM TOWARD THE BEACH, so he is seen from "
            "behind: his soaked head and one driving shoulder breaking the surface in "
            "the near frame with the wet coat clinging to his back, one arm flung "
            "forward mid-stroke, white water churning behind his kick, his face turned "
            "away toward the land. Well behind him the boat sits low and heavy with "
            "the bulging net still over its right side and the small figures of the "
            "other men working it, growing smaller. Ahead of him the empty beach. Low "
            "level gold-grey first light coming across the water from the east."
        ),
    },
    # ------------------------------ n7 — what was waiting on the sand ----
    {
        "id": "v2-r019-b18", "out": "s18-he-stopped-cold.jpeg", "seg": "n7 p1",
        "window": "67.86-70.31", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": "When he waded out of the water, he stopped cold.",
        "must_show": "Peter stopped dead in the shallows, streaming wet, halfway out of the water, staring at something up the beach.",
        "must_not_show": "he is not running any more and not smiling. Jesus is not in this frame yet.",
        "scene": (
            "One photograph, 50mm lens, shallow focus, grain. Peter is knee deep in "
            "the shallows seen in hard profile from the side, stopped dead in "
            "mid-stride with one foot still lifted and water streaming off the soaked "
            "coat, his hair plastered flat, his chest heaving. Everything about him "
            "has stopped except his breathing. His head is up and turned away from the "
            "camera toward the top of the beach and his eyeline exits the right edge "
            "of the frame; his face is open and stunned. Behind him the flat pale "
            "water and the small far boat, out of focus. Low gold-grey first light "
            "coming in from the east across the water and striking his wet shoulder. "
            "Out of focus at the right edge, a thin line of grey smoke rises from the "
            "sand."
        ),
    },
    {
        "id": "v2-r019-b19", "out": "s19-a-fire-with-fish-and-bread.jpeg", "seg": "n7 p2",
        "window": "70.31-76.38", "wide": True, "jesus": True, "ref": True,
        "locks": ["FIRE", "SHORE-DAWN"],
        "narration": ("On the sand was a charcoal fire, with fish already laid over it, "
                      "and bread."),
        "must_show": "the fire of coals waiting on the sand with fish cooking on it and bread beside it — and Jesus crouched over it, tending it, having got there first and made breakfast.",
        "must_not_show": "no leaping camp fire, no logs, no metal grill or pan. No halo, glow or rim-light on him. He is dry — he has not been in the water.",
        "scene": (
            "One photograph, 35mm lens, deep focus, low camera, grain. THE CAMERA IS "
            "DOWN ON THE WET SAND BEHIND THE FIRE AND SHOOTS ACROSS IT UP THE BEACH: "
            "the bed of red coals fills the near foreground, close and slightly out of "
            "focus, with the two fish blistering on their flat stone and the round "
            "loaf on the stone beside them, and thin grey smoke leaning across the "
            "frame. Beyond the coals Jesus is crouched on one knee in the sand in "
            "three-quarter view, entirely dry, sleeves pushed back, calmly turning one "
            "of the fish with a short stick; his head is bent down to the work and his "
            "eyeline goes down into the coals, far below the lens. His face is lit "
            "warm from below by the embers and cool from the side by the morning. His "
            "cream robe is the only cream in the frame. Behind him the pale empty "
            "beach runs up to coarse grass, and the eastern sky over the far hills is "
            "going from grey to low gold."
        ),
    },
    # ------------------------------------ n8 — the same kind of fire ----
    {
        "id": "v2-r019-b20", "out": "s20-a-charcoal-fire.jpeg", "seg": "n8 p1-p2",
        "window": "76.38-82.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIRE"],
        "narration": ("A charcoal fire. The same kind of fire Peter had stood beside in "
                      "the courtyard the night he denied him."),
        "must_show": "the coals themselves, filling the frame — the exact same bed of glowing charcoal a man stands beside on a cold night, so the rhyme with the courtyard is unmistakable.",
        "must_not_show": "no flames, no logs, no grill, no faces, no second panel or inset. Jesus is not in this frame.",
        "scene": (
            "One photograph, 100mm macro lens, very shallow depth of field, grain. "
            "Extreme close on the bed of charcoal embers itself, filling almost the "
            "whole frame: individual lumps of charcoal burning deep red-orange under "
            "a soft grey crust of ash, heat shimmer above them, one small blue-edged "
            "flicker between two coals, thin smoke drawn sideways. The blackened flat "
            "stone and the blistering skin of a fish cross the top of the frame. At "
            "the very edge, far out of focus, two bare wet feet stand in the sand a "
            "pace back from the heat. No face and no whole figure is visible anywhere. "
            "The picture is lit almost entirely by the coals themselves, with a thin "
            "cool morning light on the sand at the edges."
        ),
    },
    {
        "id": "v2-r019-b21", "out": "s21-the-whole-night-came-back.jpeg", "seg": "n8 p3",
        "window": "82.73-86.89", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "FIRE"],
        "narration": "The smell alone would have brought the whole night back.",
        "must_show": "Peter's face over those coals — the smell of charcoal putting him straight back in the courtyard, shame surfacing before a word has been said.",
        "must_not_show": "no courtyard flashback in the frame, no second panel, no vignette or inset. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime wide open, extremely shallow depth of field, "
            "grain. Very tight and low on Peter's face as he stands over the fire, lit "
            "orange from below by the coals exactly as he was lit in that courtyard, "
            "and cool blue-grey from the side by the morning. He is looking down into "
            "the embers and his eyeline drops steeply out of the bottom of the frame, "
            "nowhere near the lens; his head is turned slightly off the camera axis. "
            "Salt water still runs out of his hair and down his cheek, his beard is "
            "soaked, his jaw is clenched, and his eyes are stricken with something "
            "that has nothing to do with this morning. The coals are a red blur across "
            "the bottom of the frame."
        ),
    },
    # -------------------------------- n9 — breakfast on the shore ----
    {
        "id": "v2-r019-b22", "out": "s22-he-did-not-bring-it-up.jpeg", "seg": "n9 p1",
        "window": "86.89-89.06", "wide": False, "jesus": True, "ref": True,
        "locks": ["FIRE"],
        "narration": "Jesus did not bring up the denial.",
        "must_show": "Jesus's hands and face at the fire, entirely occupied with breaking bread and the cooking fish — no reckoning, no confrontation, just breakfast.",
        "must_not_show": "no accusing look, no pointing, no confrontation. No halo, glow or rim-light.",
        "scene": (
            "One photograph, 50mm prime wide open, shallow depth of field, grain. "
            "Close on Jesus at the fire in three-quarter view, crouched with his "
            "forearms on his knees, tearing the round loaf open in his two hands; the "
            "torn crumb of the bread is sharp in the near frame and his hands are "
            "working, ordinary and unhurried. His head is bent down over the bread and "
            "his eyeline goes down and out of the bottom right of the frame, well off "
            "the camera axis. His face is quiet, warm and entirely without reproach, "
            "lit from below by the coals and from the east by the low morning. His "
            "cream sleeve is pushed back to the elbow. The coals and the fish are a "
            "warm blur behind his hands."
        ),
    },
    {
        "id": "v2-r019-b23", "out": "s23-they-ate-together.jpeg", "seg": "n9 p2",
        "window": "89.06-94.47", "wide": True, "jesus": True, "ref": True,
        "locks": ["PETER", "CREW", "FIRE", "SHORE-DAWN"],
        "narration": ("He simply had breakfast waiting, and they ate together on the "
                      "shore in the first gold light."),
        "must_show": "the seven of them and Jesus sitting around the coals on the sand eating fish and bread with their hands, wet and tired and quiet, the boat drawn up behind them.",
        "must_not_show": "nobody but Jesus in cream. No table, no plates, no glass or metal vessels. Not a posed group facing the camera.",
        "scene": (
            "One photograph, 28mm lens, deep focus, low camera on the sand, grain. THE "
            "CAMERA SITS IN THE SAND BEHIND TWO OF THE MEN AND SHOOTS PAST THEM ACROSS "
            "THE FIRE: their backs and wet shoulders fill the near left and right of "
            "the frame, seen entirely from behind and out of focus, and NOT ONE FACE "
            "IS TURNED TOWARD THE LENS. Between and beyond them, eight men sit in a "
            "loose ring on the sand around the low bed of coals, eating torn bread and "
            "flakes of hot fish with their fingers, everyone in three-quarter or "
            "profile, all of them turned inward toward the fire and toward Jesus, who "
            "sits among them on the sand and hands a piece of fish across to the man "
            "beside him. Peter sits nearest the fire in soaked clothes with his knees "
            "drawn up, looking at the coals. Behind the group the boat is drawn up on "
            "the shingle with the heavy net still over its side. The sun has just "
            "cleared the far hills: low level gold light comes in from the east "
            "straight across the water and lays long shadows up the beach."
        ),
    },
    # ------------------------------ n10 / j1 — the question ----
    {
        "id": "v2-r019-b24", "out": "s24-he-turned-to-peter.jpeg", "seg": "n10 p1",
        "window": "94.47-97.54", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "FIRE"],
        "narration": "When breakfast was over, Jesus turned to Peter.",
        "must_show": "the moment the conversation narrows to two — Jesus turning his head to Peter across the dying fire while the others are still eating.",
        "must_not_show": "no anger, no severity, no pointing. No halo, glow or rim-light.",
        "scene": (
            "One photograph, 50mm lens, shallow depth of field, grain. A two-shot "
            "across the low coals from one side: Jesus is in the near left of the "
            "frame in three-quarter from behind, his head just turning toward Peter so "
            "we see the line of his cheek and his beard and the beginning of his "
            "expression, his eyeline crossing the frame to Peter and out of the right "
            "edge. Peter is beyond the coals, sharp, sitting back on his heels in the "
            "sand with a piece of bread still in his hand, looking down and to one "
            "side, not yet aware he is being looked at. Out of focus behind them the "
            "other men are still eating. Low gold morning light from the east rakes "
            "across the sand between them and thin smoke rises between their faces."
        ),
    },
    {
        "id": "v2-r019-b25", "out": "s25-the-same-question-three-times.jpeg", "seg": "n10 p2a",
        "window": "97.54-101.60", "wide": True, "jesus": True, "ref": True,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": ("Three times, once it seems for each denial, he asked him the "
                      "same question,"),
        "must_show": "the two of them a little apart from the others now, walking slowly at the waterline, the question being asked and asked again.",
        "must_not_show": "no crowd around them, no fire between them. No halo, glow or rim-light. Not a posed pair facing the camera.",
        "scene": (
            "One photograph, 35mm lens, shallow depth of field, grain. THE CAMERA "
            "STANDS UP THE BEACH WELL BEHIND BOTH MEN AND SHOOTS DOWN PAST THEM TOWARD "
            "THE BRIGHT WATER, so both are seen from behind and in three-quarter from "
            "behind and NEITHER FACE IS TURNED TOWARD THE LENS. They walk slowly at "
            "the waterline a little apart from the others, Jesus on the left with his "
            "head turned toward Peter, Peter on the right with his head down. Their "
            "long shadows run back up the beach toward the camera from the low eastern "
            "sun ahead of them. Far behind them at the top of the frame the fire "
            "smokes and the other men are small dark shapes around it. Low level gold "
            "morning light off the water."
        ),
    },
    {
        "id": "v2-r019-b26", "out": "s26-his-old-name.jpeg", "seg": "n10 p2b",
        "window": "101.60-106.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": "using Peter's old name, the name he had before any of it:",
        "must_show": "Peter's face at the sound of his old name — Simon, the fisherman's name he had before he was ever called the rock.",
        "must_not_show": "no smiling, no relief yet. Jesus is not in this frame.",
        "scene": (
            "One photograph, 105mm prime wide open, very shallow depth of field, "
            "grain. Very tight on Peter's face in three-quarter profile, wet hair "
            "drying in loose curls, salt on his skin, his head half turned away and "
            "tipped slightly down so his eyeline leaves the frame past the lower left "
            "corner, well off the camera axis. He has just heard the old name and his "
            "brows have drawn together; his eyes are wet and very still and his mouth "
            "is closed hard. Low gold morning light from the east on one side of his "
            "face and cool shadow on the other. Behind him the water and the far hills "
            "melt into a bright soft blur."
        ),
    },
    {
        "id": "v2-r019-b27", "out": "s27-lovest-thou-me.jpeg", "seg": "j1",
        "window": "106.00-109.47", "wide": False, "jesus": True, "ref": True,
        "locks": ["SHORE-DAWN"],
        "narration": "Simon, son of Jonas, lovest thou me?",
        "must_show": "Jesus asking it — his whole attention on Peter, gentle and completely direct, the question offered rather than demanded.",
        "must_not_show": "no severity, no accusation, no raised hand. No halo, glow or rim-light. Not a posed portrait down the lens.",
        "scene": (
            "One photograph, 85mm prime wide open, extremely shallow depth of field, "
            "grain. Close on Jesus at the waterline in three-quarter view, caught "
            "mid-question: his head inclined slightly toward Peter, his lips parted on "
            "the words, his brows raised in a real question and not a judgement, his "
            "eyes steady and warm and utterly attentive. His eyeline crosses the frame "
            "to Peter and exits through the LEFT edge, clearly past the camera. Low "
            "level gold morning light from the east across his cheek and through the "
            "loose ends of his hair; the bright water behind him is an out-of-focus "
            "wash of gold and pale grey. One plain cream wool robe, and no other cream "
            "in the frame."
        ),
    },
    # ------------------------------- n11 — no word thrown back ----
    {
        "id": "v2-r019-b28", "out": "s28-not-one-word-thrown-back.jpeg", "seg": "n11 p1-p3",
        "window": "109.47-114.93", "wide": True, "jesus": True, "ref": True,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": ("Not, how could you. Not, prove it. Not one word thrown back at "
                      "him about the denial."),
        "must_show": "the two of them stopped at the waterline facing each other, Jesus's posture open and unhurried — a man who is not going to bring up the worst thing you ever did.",
        "must_not_show": "no accusing finger, no folded arms, no hard face. Nobody but Jesus in cream. No halo, glow or rim-light.",
        "scene": (
            "One photograph, 35mm lens, deep focus, low camera in the wet sand, grain. "
            "THE CAMERA IS DOWN IN THE SHALLOWS OUT ON THE WATER SIDE OF BOTH MEN AND "
            "SHOOTS ALONG THE WATERLINE PAST THEM, so both are held in clean profile "
            "against the pale beach and NEITHER FACE IS TURNED TOWARD THE LENS. They "
            "stand a pace apart at the edge of the water, facing each other, ankle "
            "deep. Jesus's hands hang open and easy at his sides and his weight is "
            "settled; there is nothing braced or accusing in him. Peter is half turned "
            "away with his head down, unable to hold the look. Their reflections lie "
            "in the wet sand between them. Long shadows run inland from the low "
            "eastern sun. Far up the beach the fire smokes and the boat sits on the "
            "shingle."
        ),
    },
    {
        "id": "v2-r019-b29", "out": "s29-only-do-you-love-me.jpeg", "seg": "n11 p4",
        "window": "114.93-117.47", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Only: do you love me.",
        "must_show": "Peter listening — the question landing on a man who expected to be destroyed by it and is being asked something else entirely.",
        "must_not_show": "no smile yet, no relief yet. Jesus is not in this frame.",
        "scene": (
            "One photograph, 105mm prime wide open, extremely shallow depth of field, "
            "grain. Very tight on Peter's eyes and the bridge of his nose, his head "
            "lifted a little and turned in three-quarter, his eyeline going up and out "
            "past the upper left corner of the frame toward someone standing close and "
            "off camera. His eyes are brimming and he is not blinking. Every line of "
            "the last three days is in his face. Low gold morning light from the east "
            "on the wet skin under his eye; everything behind him is a bright "
            "featureless blur of water."
        ),
    },
    # --------------------------------- s16 / n12 — the answer ----
    {
        "id": "v2-r019-b30", "out": "s30-thou-knowest-that-i-love-thee.jpeg", "seg": "s16",
        "window": "117.47-121.07", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Yea, Lord; thou knowest that I love thee.",
        "must_show": "Peter saying it out loud — plainly, without defending himself, the first honest thing he has been able to say since that night.",
        "must_not_show": "no dramatic gesture, no kneeling yet, no theatrics. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime wide open, very shallow depth of field, grain. "
            "Close on Peter in three-quarter view, caught mid-sentence, his mouth open "
            "on the words and one hand half lifted from his side. He is looking "
            "straight at the man in front of him — his eyeline crosses the frame and "
            "exits through the RIGHT edge, past the camera and clearly not into it. "
            "There is no defence left in his face, only a plain steady raw honesty and "
            "wet eyes. Low gold morning light from the east on his cheek, salt still "
            "drying white in his beard, and the pale water an out-of-focus blur "
            "behind."
        ),
    },
    {
        "id": "v2-r019-b31", "out": "s31-three-times-peter-answered.jpeg", "seg": "n12 p1",
        "window": "121.07-124.68", "wide": True, "jesus": True, "ref": True,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": ("Three times Peter answered him, yes, Lord, you know that I love "
                      "you."),
        "must_show": "the exchange going round again — the same two men, the same waterline, the same question and the same answer, for the third time.",
        "must_not_show": "no third figure, no crowd, nobody but Jesus in cream. No halo, glow or rim-light.",
        "scene": (
            "One photograph, 50mm lens, deep focus, grain, shot from a distance. THE "
            "CAMERA IS FAR UP THE BEACH BEHIND THEM AND SHOOTS DOWN PAST THEM TOWARD "
            "THE BRIGHT WATER, so the two men are small in the middle of a wide empty "
            "shore and both are seen from behind and in three-quarter from behind, "
            "with NEITHER FACE TURNED TOWARD THE LENS. Jesus stands at the water's "
            "edge with his head turned to Peter; Peter faces him with both hands "
            "opened outward from his chest, in the middle of answering. Their two long "
            "shadows stretch back up the sand toward the camera from the low eastern "
            "sun. Wet sand, dark stones, the flat gold water beyond them and the far "
            "hills, and nothing else on the whole beach but their two figures."
        ),
    },
    {
        "id": "v2-r019-b32", "out": "s32-every-answer-cost-him-more.jpeg", "seg": "n12 p2",
        "window": "124.68-129.41", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Each time it cost him more, and each time he meant it more.",
        "must_show": "the third time — Peter grieved, his face coming apart, one fist against his own chest exactly as he held it the night he swore he never would.",
        "must_not_show": "not despair and not shame — this is grief with the truth in it. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime wide open, very shallow depth of field, grain. "
            "Close on Peter, his head bowed and turned aside so his eyeline drops out "
            "of the bottom left of the frame far off the camera axis, his eyes screwed "
            "half shut and spilling over, his mouth open and pulled down at the "
            "corners, his breath caught. His own big fist is pressed hard against his "
            "chest in exactly the gesture he used the night he swore he never would — "
            "the same hand in the same place, and it costs him everything now. Low "
            "gold morning light from the east on his wet face and in his beard; the "
            "bright shore behind him is a soft blur."
        ),
    },
    # ------------------------------- j2 / n13 — the commission ----
    {
        "id": "v2-r019-b33", "out": "s33-feed-my-sheep.jpeg", "seg": "j2",
        "window": "129.41-131.91", "wide": False, "jesus": True, "ref": True,
        "locks": ["SHORE-DAWN"],
        "narration": "Feed my sheep.",
        "must_show": "Jesus giving him the work — the words spoken plainly and finally, an instruction handed over, not a consolation.",
        "must_not_show": "no halo, glow or rim-light, no raised finger, no severity. Not a portrait staring into the lens.",
        "scene": (
            "One photograph, 85mm prime wide open, extremely shallow depth of field, "
            "grain. Close on Jesus in three-quarter view, speaking: his chin level, "
            "his mouth shaping the last word, his eyes fixed steadily on Peter with "
            "complete seriousness and complete warmth together. His eyeline crosses "
            "the frame and exits the LEFT edge, past the camera. One hand has come up "
            "open and level at chest height with the palm turned slightly up, giving "
            "something rather than commanding it. Low level gold morning light from "
            "the east across his face and in the loose ends of his hair; the water "
            "behind him is a bright out-of-focus wash. One plain cream wool robe, and "
            "no other cream anywhere in the frame."
        ),
    },
    {
        "id": "v2-r019-b34", "out": "s34-the-biggest-job-of-all.jpeg", "seg": "n13 p1",
        "window": "131.91-135.65", "wide": False, "jesus": True, "ref": True,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": ("To the man who had failed him worst, Jesus handed the biggest "
                      "job of all."),
        "must_show": "Jesus's hand closing on Peter's shoulder — the failure handed the work anyway, contact made first by the one who was denied.",
        "must_not_show": "no kneeling, no crowd, no halo, glow or rim-light. Nobody but Jesus in cream.",
        "scene": (
            "One photograph, 50mm prime wide open, very shallow depth of field, grain. "
            "Tight and low on the point of contact: Jesus's hand and forearm come in "
            "from the left of the frame and his hand closes firmly on Peter's soaked "
            "shoulder, the cream sleeve pushed back, the fingers gripping the wet wool "
            "of Peter's blue-grey tunic. Both men are cropped so that we see Jesus's "
            "jaw, beard and chest at the left edge and Peter's shoulder, neck and the "
            "lower part of his bowed face at the right; both heads are turned toward "
            "each other and inward, so neither face is toward the lens. Low gold "
            "morning light from the east rakes across the two hands, the wet cloth and "
            "the drying salt. The bright beach behind them is out of focus."
        ),
    },
    {
        "id": "v2-r019-b35", "out": "s35-he-trusted-him-again.jpeg", "seg": "n13 p2-p3",
        "window": "135.65-140.15", "wide": True, "jesus": True, "ref": True,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": "He did not only forgive Peter. He trusted him again.",
        "must_show": "Peter straightened up and steady on his feet in front of Jesus — the shape of a man who has just been given something back.",
        "must_not_show": "no halo, glow or rim-light. Nobody but Jesus in cream. Not a posed pair facing the camera.",
        "scene": (
            "One photograph, 35mm lens, deep focus, grain. THE CAMERA STANDS OFF TO "
            "ONE SIDE OF BOTH MEN AND SHOOTS ALONG THE WATERLINE, so they are held in "
            "clean profile against the bright water and NEITHER FACE IS TURNED TOWARD "
            "THE LENS. Peter stands square and straight now, head up, shoulders back, "
            "his hands loose at his sides and his face turned to Jesus; every line of "
            "him has stopped apologising. Jesus stands facing him, relaxed, one hand "
            "still resting on Peter's arm, looking at him with an unmistakable and "
            "settled confidence. Between and behind them the flat gold water and the "
            "far hills. Long shadows run inland from the low eastern sun."
        ),
    },
    # ------------------------------------------- n14 — the close ----
    {
        "id": "v2-r019-b36", "out": "s36-that-is-how-good-he-is.jpeg", "seg": "n14 p1",
        "window": "140.15-145.00", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": "That is how good he is.",
        "must_show": "Peter's face in the full morning — the grief gone through and out the other side, a man who has been forgiven and knows it.",
        "must_not_show": "no grin, no triumph — this is quiet. Jesus is not in this frame.",
        "scene": (
            "One photograph, 85mm prime wide open, very shallow depth of field, grain. "
            "Close on Peter's face in three-quarter view, lifted into the low eastern "
            "sun with his eyes half closed against it and his head turned away from "
            "the lens so his eyeline goes up and out through the upper right corner. "
            "His face is wet and worn out and completely at rest; the mouth has come "
            "loose and there is the beginning of something like peace in it. Drying "
            "salt in his beard, his damp hair going to curl in the warmth. Behind him "
            "the pale gold water and the far hills are a soft bright blur."
        ),
    },
    {
        "id": "v2-r019-b37", "out": "s37-hands-you-back-your-life.jpeg", "seg": "n14 p2",
        "window": "145.00-149.583", "wide": True, "jesus": True, "ref": True,
        "locks": ["PETER", "CREW", "BOAT", "FIRE", "SHORE-DAWN"],
        "narration": ("He takes your worst night and hands you back your life, with a "
                      "purpose bigger than the one you thought you had thrown away."),
        "must_show": "the whole shore in full morning light — the boat, the dying fire, the men, and the two figures walking up the beach together away from the water.",
        "must_not_show": "nobody but Jesus in cream. No halo, glow or rim-light. No sunset palette — the sun is climbing in the east behind the camera.",
        "scene": (
            "One photograph, 24mm lens, deep focus, grain, camera low on the sand. THE "
            "CAMERA STANDS DOWN AT THE WATERLINE BEHIND EVERYONE AND SHOOTS UP THE "
            "BEACH AWAY FROM THE LAKE, so every figure is seen from behind, walking or "
            "sitting away from the lens, and NOT ONE FACE IS TURNED TOWARD THE CAMERA. "
            "In the middle distance Jesus and Peter walk side by side up the sand away "
            "from the water, both seen from directly behind, Peter's soaked coat dark "
            "across his shoulders and the one cream robe beside him. To the right the "
            "boat is drawn up on the shingle with the heavy net still hanging over its "
            "side; to the left the fire has burnt down to a last red eye with thin "
            "smoke going straight up, and the other men sit around it in twos, all "
            "turned inward or away. Their long shadows stretch ahead of them up the "
            "beach. Full low gold morning light comes in from the east behind the "
            "camera and the eastern sky over the far hills is clear and pale."
        ),
    },
]
