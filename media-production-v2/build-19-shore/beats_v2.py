#!/usr/bin/env python3
"""V2 beat map — row 19, build-19-shore (John 21:1-17).

COVERAGE: 27 pictures against V1's 16, over 136.1 s = 5.0 s/picture.

⚠️ THIS IS THE STORY CAMERON NAMED AS THE BURST-COVERAGE EXAMPLE: "not knowing
it's Jesus -> being told -> realizing -> leaping out of the boat -> swimming.
Each micro-beat is its OWN frame." That chain is b10-b13 and it gets four
frames across 11 seconds — the densest stretch in the build, deliberately.

SCRIPTURE FACTS (John 21:1-17 KJV):
  v3   "I go a fishing ... and that night they caught NOTHING."
  v4   "when the morning was now come, Jesus stood on the shore: but the
       disciples KNEW NOT that it was Jesus." At b05-b08 he is a distant figure
       whose face is not readable — the not-knowing is real.
  v5   "Children, have ye any meat? They answered him, NO." One word.
  v6   "Cast the net on the RIGHT SIDE of the ship" — the side is stated, so the
       frame states it.
  v7   "that disciple whom Jesus loved saith unto Peter, IT IS THE LORD." John
       says it, not Peter — b10 puts the line in John's mouth.
  v7   "he GIRT HIS FISHER'S COAT unto him, (for he was naked,) and did CAST
       HIMSELF INTO THE SEA." He puts clothes ON to jump, which is the opposite
       of what a swimmer does, and it is what the text says.
  v9   "they saw a FIRE OF COALS there, and fish laid thereon, and bread."
  v9   The Greek word for that charcoal fire (anthrakia) appears exactly twice in
       the whole New Testament: here, and at the courtyard fire Peter warmed
       himself at while he denied him (John 18:18). The narration builds on that
       and b16/b17 are where it lands.
  v15  "Simon, son of Jonas" — his OLD name, from before he was ever called
       Peter. Three times, and never once a reference to the denial.
  v17  "Peter was GRIEVED because he said unto him the third time."

CONTENT-CARE: row 19 is GREEN. v7's "he was naked" is handled the way a working
boat handles it — he is stripped to a plain working loincloth and is PUTTING HIS
COAT ON as he goes over the side. Nothing is exposed, nothing is dwelt on, and
the frame is about the leap.

TIME OF DAY: the story turns on it. b01-b02 are the NIGHT of the denial
(torchlit courtyard). b03-b04 are the empty night on the water. From b05 to the
end it is DAWN and then early morning — "when the morning was now come" — first
grey light on the water at b05 warming to low gold by the breakfast. No midday
anywhere in this build.
"""

LOCKS = {
    "FIRE": (
        "CHARCOAL FIRE LOCK: a small fire of hot red-orange charcoal embers built in a "
        "hollow of the wet sand — no flames, only the deep orange heat of the coals "
        "under a grey crust of ash, thin smoke drifting sideways, with two fish "
        "laid across the coals on a flat stone and a round loaf of bread beside it."
    ),
    "SHORE-DAWN": (
        "SHORE-DAWN LOCK: the shingle and sand shore of the Sea of Galilee at first "
        "light — wet dark stones and packed sand at the waterline, the flat pale "
        "water going out to the low black hills of the far side, and the eastern sky "
        "just beginning to pale from grey into thin gold. The light is low, cool and "
        "sideways, throwing long soft shadows down the beach."
    ),
    "BOAT": (
        "BOAT LOCK: one open Galilean fishing boat — heavy overlapping planks dark "
        "with water, a low gunwale running around the hull, a short mast with the "
        "sail furled, long oars in leather-strapped tholes, coiled rope and folded "
        "nets on the deck timbers, and a small clay oil lamp at the bow. The deck "
        "planking is always visible under the men's feet."
    ),
    "CREW": (
        "CREW LOCK: the other fishermen in the boat are the same five or six men "
        "throughout — working Galileans between twenty and forty, tired and "
        "unshaven, hair damp, sleeves pushed back over forearms scarred by rope. "
        "They wear plain wool tunics in SATURATED DEEP colours: rust-brown, deep "
        "russet, dark olive, blue-grey and dusty indigo. None wears off-white, "
        "ivory or any near-white cloth. Their faces are shown clearly."
    ),
    "COURTYARD": (
        "COURTYARD-NIGHT LOCK: the high priest's courtyard on the night of the "
        "denial — a walled stone yard in deep darkness, a fire of coals burning in "
        "an iron brazier in the middle of it, servants and officers standing close "
        "around the heat with their faces lit orange from below, and black shadow "
        "everywhere beyond the firelight."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------- n1/n2 — the denial ----
    {
        "id": "v2-r019-b01", "out": "s01-he-swore-he-never-would.jpeg", "seg": "n1",
        "window": "0.28-3.95", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": ("Peter had sworn he would die before he would ever deny Jesus."),
        "must_show": "close on Peter swearing it — a fist against his own chest, absolutely certain, in warm indoor lamplight before everything went wrong.",
        "must_not_show": "no courtyard and no fire yet; this is earlier and he means every word. Do not put Jesus in this frame.",
        "scene": (
            "Close on Peter in warm indoor lamplight, one big fist pressed hard "
            "against his own chest, his chin up and his eyes fierce and shining with "
            "absolute conviction, mid-vow. His mouth is set. He has never been more "
            "sure of anything. Soft warm light on his face and dark shadow behind. He "
            "has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b02", "out": "s02-he-wept-bitterly.jpeg", "seg": "n2",
        "window": "4.61-13.43", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "COURTYARD"],
        "narration": ("Then, in one terrible night, he denied him three times. The "
                      "rooster crowed, Jesus turned and looked at him, and Peter went "
                      "out and wept bitterly."),
        "must_show": "Peter alone in the dark outside the courtyard, doubled over against the wall, wrecked — the coal fire and the figures small behind him.",
        "must_not_show": "do NOT show Jesus or the look itself; show only Peter afterwards. No violence, no trial scene.",
        "scene": (
            "Peter has got out of the courtyard and is alone against a black stone "
            "wall in the darkness, doubled over with one forearm braced on the stone "
            "and his forehead against it, his other hand over his face, his whole back "
            "shaking. Behind him and some way off, the coal fire in its brazier still "
            "burns orange in the courtyard with two or three figures standing around "
            "it, none of them looking his way. Deep night, hard shadow. The camera is "
            "back far enough to hold him and the distant fire. He has two arms, two "
            "hands and one head."
        ),
    },
    # --------------------------------------------- n3/n4 — back to fishing ----
    {
        "id": "v2-r019-b03", "out": "s03-back-to-the-old-life.jpeg", "seg": "n3 + n4 p1-p2",
        "window": "14.05-21.63", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT", "SHORE-DAWN"],
        "narration": ("After the resurrection, Peter went back to fishing. Back to the "
                      "old life. It is what people do with a failure they cannot carry. "
                      "They go back to what they knew before it happened."),
        "must_show": "Peter shoving the boat out into black water at night with the others — going back to the trade he left, without a word.",
        "must_not_show": "do not put Jesus in this frame; nobody is talking — the silence is the mood.",
        "scene": (
            "In the dark before dawn, Peter has his shoulder against the bow of the "
            "fishing boat pushing it off the shingle into black water, thigh deep, "
            "with two other men doing the same beside him and a third already aboard. "
            "Nobody is speaking. Their faces are set and closed. The lake is flat and "
            "black and the sky above still has stars in it. One small lamp burns at "
            "the bow. The camera is back far enough to see the men and the boat. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b04", "out": "s04-they-caught-nothing.jpeg", "seg": "n4 p3",
        "window": "21.63-26.60", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT"],
        "narration": "And that night they caught nothing.",
        "must_show": "the net hauled up over the gunwale EMPTY — dripping, slack, nothing in it — and the men's faces at the end of a wasted night.",
        "must_not_show": "not one fish anywhere in the net or the boat; do not put Jesus in this frame.",
        "scene": (
            "Inside the boat on black water, two men are hauling the wet net back in "
            "over the gunwale and it is completely EMPTY — the mesh hanging slack and "
            "dripping, folding into a wet heap on the deck timbers with nothing in it "
            "at all. Peter stands with a coil of rope in his hands staring down at it. "
            "The other faces are grey with tiredness. The bow lamp throws thin orange "
            "light and the sky beyond is beginning to lose its stars. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    # ------------------------------------------- n5 / j0a — the stranger ----
    {
        "id": "v2-r019-b05", "out": "s05-a-figure-on-the-shore.jpeg", "seg": "n5",
        "window": "27.17-31.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SHORE-DAWN"],
        "narration": ("At dawn, a figure on the shore called out across the water to the "
                      "boat."),
        "must_show": "SCRIPTURE-EXACT (v4): a lone figure standing on the distant shore in the first grey light, TOO FAR OFF for his face to be readable.",
        "must_not_show": "his face must NOT be identifiable at this distance — v4 says they knew not that it was Jesus. Do not attach a Jesus lock or ref to this beat.",
        "scene": (
            "Seen from the boat across a stretch of flat pale water at first light: a "
            "single figure stands alone on the far shingle shore, small with distance, "
            "his features not readable at all against the paling grey sky behind him. "
            "One arm is lifted as he calls out. A thin thread of smoke rises from "
            "somewhere on the beach beside him. The water between is glassy and "
            "colourless. The camera is back far enough that he reads only as a "
            "silhouette on a shore. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b06", "out": "s06-have-ye-any-meat.jpeg", "seg": "j0a",
        "window": "31.87-33.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT"],
        "narration": "Children, have ye any meat? (John 21:5)",
        "must_show": "the men in the boat turning toward the distant voice, squinting across the water, nobody recognising anything.",
        "must_not_show": "the shore figure stays distant and unreadable; do not attach a Jesus lock or ref.",
        "scene": (
            "In the boat the men have turned toward the shore at the sound of the "
            "call, several shading their eyes and squinting across the flat pale "
            "water. Their faces are blank and mildly irritated — a stranger shouting a "
            "fisherman's question at the end of a bad night. Peter has straightened up "
            "with the rope still in his hands. Far off across the water the figure on "
            "the beach is a small unreadable shape. First grey light. Every figure has "
            "two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b07", "out": "s07-their-answer-was-no.jpeg", "seg": "n5b",
        "window": "34.67-38.48", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "Their answer was only one word: no. All night, nothing.",
        "must_show": "close on Peter calling the single word back across the water — flat, tired, one hand cupped at his mouth.",
        "must_not_show": "no anger; just the flatness of a man who has nothing to report. Do not put Jesus in this frame.",
        "scene": (
            "Close on Peter in the boat, one hand cupped at the side of his mouth, "
            "calling one short word back across the water. His face is flat and worn "
            "out — no anger in it, no curiosity, just the emptiness of a man with "
            "nothing to show for a whole night. Damp hair stuck to his forehead, "
            "stubble, shadows under his eyes. Grey dawn light. He has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r019-b08", "out": "s08-cast-on-the-right-side.jpeg", "seg": "j0b",
        "window": "39.07-42.37", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT"],
        "narration": ("Cast the net on the right side of the ship, and ye shall find. "
                      "(John 21:6)"),
        "must_show": "the men reacting to the instruction — a couple exchanging a look at being told their own trade by a stranger, one already reaching for the net.",
        "must_not_show": "the shore figure stays distant and unreadable; do not attach a Jesus lock or ref.",
        "scene": (
            "In the boat the men have turned to each other at the instruction — one "
            "with his eyebrows up and his palms half raised at being told his own "
            "trade by a stranger on a beach, another already turning toward the "
            "folded net on the deck, Peter looking back out across the water at the "
            "distant figure. Grey dawn, flat pale water. The camera holds the boat and "
            "the men. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b09", "out": "s09-the-net-came-up-full.jpeg", "seg": "n5c",
        "window": "43.43-47.42", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT"],
        "narration": ("They did — and it came up so full they could not haul it in."),
        "must_show": "ACTION-LOGIC: the net over the RIGHT side of the boat, packed solid with silver fish, three men hauling and unable to lift it — the hull heeling toward it.",
        "must_not_show": "the net must not come aboard — v6 says they could not draw it; do not put Jesus in this frame.",
        "scene": (
            "The net is over the right-hand side of the boat and it is packed solid "
            "with silver fish, boiling and flashing just under the surface, so heavy "
            "that the hull has heeled right over toward it. Three men have both hands "
            "on the ropes hauling back with their whole weight, feet braced against "
            "the gunwale, and it is not coming up. Peter is at the rail staring down "
            "into it. Grey dawn light flashing off wet scales and water. The camera is "
            "back far enough to see the boat and the loaded net. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    # ------------------------------------------------------ n6 — THE BURST ----
    {
        "id": "v2-r019-b10", "out": "s10-it-is-the-lord.jpeg", "seg": "n6 p1",
        "window": "48.05-51.64", "wide": False, "jesus": False, "ref": False,
        "locks": ["JOHN", "PETER"],
        "narration": ("Then one of them went very still and said, it is the Lord."),
        "must_show": "SCRIPTURE-EXACT (v7): JOHN says it, not Peter — John gone completely still with his hand stopped on the rope, saying it quietly to Peter.",
        "must_not_show": "Peter must NOT be the one who works it out; do not put Jesus in this frame.",
        "scene": (
            "Close on John in the boat, gone completely still with both hands stopped "
            "dead on the rope he was hauling, his head turned toward the shore and his "
            "eyes wide and fixed. His mouth is barely moving on three quiet words. "
            "Beside him at the frame's edge Peter's head is beginning to come round "
            "toward him. Grey dawn light on both faces. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r019-b11", "out": "s11-it-hits-peter.jpeg", "seg": "n6 p2a",
        "window": "51.64-53.88", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "And Peter did not wait for the boat.",
        "must_show": "⚠️ THE REALIZATION, its own frame: close on Peter's face as it lands — the rope dropping out of his hands, everything arriving at once.",
        "must_not_show": "he has not moved yet — this frame is purely the face; do not put Jesus in it.",
        "scene": (
            "Very close on Peter's face at the instant it lands. His eyes have gone "
            "enormous and are locked on the shore, his mouth has fallen open, and the "
            "wet rope is visibly slipping out of his opening hands at the bottom of "
            "the frame. Everything — the denial, the fire, the look — is arriving "
            "behind his eyes at once. Grey dawn light. He has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r019-b12", "out": "s12-he-threw-himself-in.jpeg", "seg": "n6 p2b",
        "window": "53.88-56.5", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "CREW", "BOAT"],
        "narration": "He threw himself into the sea",
        "must_show": "⚠️ THE LEAP, caught MID-AIR: Peter over the gunwale with both feet off the boat, hauling his fisher's coat on as he goes — the crew grabbing at nothing behind him.",
        "must_not_show": "CONTENT-CARE — he wears a plain working loincloth and is PUTTING THE COAT ON (v7); nothing exposed, nothing dwelt on. Do not put Jesus in this frame.",
        "scene": (
            "Peter is caught in mid-air over the side of the boat, both feet already "
            "clear of the gunwale and his body committed to the water below, one arm "
            "still driving through the sleeve of his rough fisher's coat as he goes — "
            "dragging his clothes ON as he jumps. He wears a plain working loincloth "
            "beneath it. Behind him in the boat two men have lunged after him with "
            "their hands closing on empty air, faces astonished. Grey dawn, flat water "
            "rushing up. The camera is back far enough to hold the boat and the "
            "airborne man. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b13", "out": "s13-and-swam-for-shore.jpeg", "seg": "n6 p3",
        "window": "56.5-59.29", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "BOAT", "SHORE-DAWN"],
        "narration": "and swam for shore, leaving everything behind.",
        "must_show": "⚠️ THE SWIM, its own frame: Peter thrashing hard through the water toward the beach, the loaded boat and the whole catch abandoned behind him.",
        "must_not_show": "no elegant swimming — this is desperate and graceless; do not put Jesus in this frame.",
        "scene": (
            "Peter is swimming hard for the shore, low in the flat grey water with one "
            "arm thrown forward mid-stroke and white water breaking around his "
            "shoulders and kicking feet — graceless, desperate, going as fast as a "
            "heavy man can go. Well behind him the boat sits heeled over with the "
            "loaded net still in the water and the crew still aboard, all of it "
            "abandoned. Ahead of him the shingle beach and the thin thread of smoke. "
            "First light. The camera is back far enough to hold the swimmer, the water "
            "and the boat behind. He has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------ n7/n8 — the coal fire ----
    {
        "id": "v2-r019-b14", "out": "s14-he-stopped-cold.jpeg", "seg": "n7 p1",
        "window": "59.90-62.04", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": "When he waded out of the water, he stopped cold.",
        "must_show": "Peter halted dead in the shallows, streaming water, staring at something up the beach — stopped mid-stride.",
        "must_not_show": "do not put Jesus in this frame yet; whatever stopped him is out of frame.",
        "scene": (
            "Peter has come up out of the shallows onto the wet shingle and stopped "
            "dead, knee deep in the last of the water, streaming from head to foot, "
            "his sodden fisher's coat clinging to him. He is standing absolutely still "
            "and staring at something up the beach out of frame, his chest heaving, "
            "one hand half lifted and forgotten. Low grey-gold dawn light along the "
            "shore. The camera is back far enough to see him head to feet. He has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b15", "out": "s15-a-fire-with-fish-and-bread.jpeg", "seg": "n7 p2",
        "window": "62.04-67.75", "wide": True, "jesus": True, "ref": REF,
        "locks": ["FIRE", "SHORE-DAWN"],
        "narration": ("On the sand was a charcoal fire, with fish already laid over it, "
                      "and bread."),
        "must_show": "the coal fire on the sand with fish already cooking and bread beside it — and Jesus crouched over it, having made breakfast.",
        "must_not_show": "no halo, glare or rim-light; the only warm light is the coals. He is doing something completely domestic.",
        "scene": (
            "On the wet sand above the waterline a small fire of hot red-orange charcoal "
            "burns in a hollow, two fish laid across it on a flat stone and a round "
            "loaf beside them. Jesus is crouched over it on his heels, turning one of "
            "the fish with his fingers, entirely absorbed in the ordinary work of "
            "cooking breakfast. The orange of the coals lights him from below against "
            "the cool grey-gold of the dawn shore. The camera is back far enough to "
            "hold him and the fire. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b16", "out": "s16-a-charcoal-fire.jpeg", "seg": "n8 p1-p2",
        "window": "68.35-73.67", "wide": False, "jesus": False, "ref": False,
        "locks": ["FIRE"],
        "narration": ("A charcoal fire. The same kind of fire Peter had stood beside in "
                      "the courtyard the night he denied him."),
        "must_show": "⚠️ very close on the coals themselves — the exact same orange embers and grey ash as the courtyard brazier, so the rhyme is visual and unmistakable.",
        "must_not_show": "no people at all in this frame; the fire is the whole picture. Do not put Jesus in it.",
        "scene": (
            "Extremely close on the fire of charcoal in the sand — deep orange embers "
            "breathing under a crust of pale grey ash, thin blue smoke drifting "
            "sideways, one fish blistering on the flat stone above them. No flames, "
            "just heat. The light and colour of it are exactly the light and colour of "
            "a brazier in a courtyard at night. There are no people in the frame."
        ),
    },
    {
        "id": "v2-r019-b17", "out": "s17-the-whole-night-came-back.jpeg", "seg": "n8 p3",
        "window": "73.67-76.84", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": "The smell alone would have brought the whole night back.",
        "must_show": "close on Peter's face lit from below by those coals — the memory going through him, dread and shame arriving.",
        "must_not_show": "do not put Jesus in this frame; no flashback imagery — the memory is entirely on his face.",
        "scene": (
            "Close on Peter's face, lit from below by the orange of the coals exactly "
            "as it would have been lit in a courtyard at night. Water still runs from "
            "his hair. His eyes have gone somewhere else entirely, his jaw has "
            "clenched, and the blood has drained out of his face — the smell of it has "
            "put him straight back inside the worst night of his life. Cool grey dawn "
            "behind, orange firelight in front. He has one head."
        ),
    },
    # ---------------------------------------------------- n9 — breakfast ----
    {
        "id": "v2-r019-b18", "out": "s18-he-did-not-bring-it-up.jpeg", "seg": "n9 p1",
        "window": "77.41-79.44", "wide": False, "jesus": True, "ref": REF,
        "locks": ["FIRE"],
        "narration": "Jesus did not bring up the denial.",
        "must_show": "close on Jesus at the fire holding out food — warm, easy, saying nothing about any of it.",
        "must_not_show": "no halo, glare or rim-light; NOTHING knowing or significant in the look — he is just handing a man his breakfast.",
        "scene": (
            "Close on Jesus crouched at the coals, holding out a piece of grilled fish "
            "on the flat of his hand toward someone out of frame. His face is warm and "
            "completely ordinary — a small easy smile, eyebrows relaxed, no weight or "
            "significance in the expression at all. He might be any man at any fire "
            "feeding a friend who has had a long night. Orange coal light from below, "
            "cool dawn behind. His hand has five fingers."
        ),
    },
    {
        "id": "v2-r019-b19", "out": "s19-they-ate-together.jpeg", "seg": "n9 p2",
        "window": "79.44-84.52", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "CREW", "FIRE", "SHORE-DAWN"],
        "narration": ("He simply had breakfast waiting, and they ate together on the "
                      "shore in the first gold light."),
        "must_show": "the whole group sitting round the fire on the sand eating — soaked, tired, quiet, ordinary; the boat pulled up behind with the net.",
        "must_not_show": "no halo, glare or rim-light; nothing ceremonial about it — it is breakfast.",
        "scene": (
            "The men are sitting around the small coal fire on the wet sand, eating — "
            "seven or eight of them cross-legged and hunched with fish and torn bread "
            "in their hands, soaked and steaming slightly in the cool air, nobody "
            "saying much. Jesus sits among them at the same level passing bread along. "
            "Behind them the boat has been dragged up the shingle with the heavy net "
            "beside it. The eastern sky has warmed to low gold and lays long light "
            "down the beach. The camera is back far enough to hold the whole circle. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    # ---------------------------------------------- n10 / j1 — the question ----
    {
        "id": "v2-r019-b20", "out": "s20-he-turned-to-peter.jpeg", "seg": "n10 p1",
        "window": "85.11-87.65", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "FIRE"],
        "narration": "When breakfast was over, Jesus turned to Peter.",
        "must_show": "Jesus turning his attention onto Peter across the dying fire, and Peter going still under it.",
        "must_not_show": "no halo, glare or rim-light; the others fade back but nobody leaves.",
        "scene": (
            "Across the low coals Jesus has turned and settled his attention fully on "
            "Peter, who is sitting opposite with a piece of bread halfway to his mouth "
            "and has gone completely still. The other men around the fire have quieted "
            "and are looking down or away, giving them room without moving. The coals "
            "are burning down. Low gold light along the shore. The camera holds both "
            "men and the fire between them. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    {
        "id": "v2-r019-b21", "out": "s21-his-old-name.jpeg", "seg": "n10 p2",
        "window": "88.12-96.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER"],
        "narration": ("Three times, once it seems for each denial, he asked him the same "
                      "question, using Peter's old name, the name he had before any of "
                      "it:"),
        "must_show": "the two faces across the coals — Jesus asking gently, Peter braced for the accusation that is not coming.",
        "must_not_show": "no halo, glare or rim-light; no reproach anywhere in Jesus's face.",
        "scene": (
            "Close on the two of them either side of the low coals, faces lit warm "
            "from below. Jesus's expression is gentle and unhurried and entirely "
            "without reproach. Opposite him Peter is braced — shoulders up, jaw tight, "
            "eyes fixed on Jesus and waiting for a blow that does not come. The thin "
            "smoke drifts between them. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r019-b22", "out": "s22-lovest-thou-me.jpeg", "seg": "j1",
        "window": "97.08-99.64", "wide": False, "jesus": True, "ref": REF,
        "locks": [],
        "narration": "Simon, son of Jonas, lovest thou me? (John 21:16)",
        "must_show": "close on Jesus asking — quiet, direct, genuinely asking, using a name from before everything.",
        "must_not_show": "no halo, glare or rim-light; no test and no trap in the face.",
        "scene": (
            "Very close on Jesus's face across the coals, speaking. His eyes are steady "
            "and warm and completely direct, his brows lifted a little in the middle, "
            "his mouth soft — a real question asked of one person, with nothing hidden "
            "behind it. Warm coal light from below on his face and beard; the cool "
            "dawn shore soft behind."
        ),
    },
    {
        "id": "v2-r019-b23", "out": "s23-not-one-word-thrown-back.jpeg", "seg": "n11",
        "window": "100.73-106.49", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "FIRE"],
        "narration": ("Not, how could you. Not, prove it. Not one word thrown back at "
                      "him about the denial."),
        "must_show": "the two of them still sitting quietly across the fire — no confrontation, no standing, nothing raised.",
        "must_not_show": "no halo, glare or rim-light; nobody is pointing, standing, or leaning in accusingly. The absence of all that IS the frame.",
        "scene": (
            "A quiet wide frame of the two men sitting across the burnt-down coals in "
            "the low gold light, both still seated, hands loose, nothing raised and "
            "nothing tense in either body. There is no confrontation happening at all "
            "— only two people talking beside a fire on a beach in the early morning. "
            "The sea lies flat behind them. The camera is back far enough to hold "
            "both. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b24", "out": "s24-thou-knowest-that-i-love-thee.jpeg", "seg": "s16",
        "window": "107.09-109.51", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": ("Yea, Lord; thou knowest that I love thee. (John 21:16)"),
        "must_show": "close on Peter answering — raw, undefended, his voice plainly costing him.",
        "must_not_show": "do not put Jesus in this frame; no bravado left in him at all.",
        "scene": (
            "Very close on Peter's face, lit from below by the coals. Every bit of the "
            "old bluster is gone — his eyes are wet and fixed on the man across the "
            "fire, his brows drawn up in the middle, his mouth unsteady on the words. "
            "He is completely undefended. Water still in his beard from the swim. He "
            "has one head."
        ),
    },
    {
        "id": "v2-r019-b25", "out": "s25-every-answer-cost-him-more.jpeg", "seg": "n12",
        "window": "110.57-116.80", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER"],
        "narration": ("Peter answered each time. Every answer cost him more, and every "
                      "answer carried more of the truth."),
        "must_show": "SCRIPTURE-EXACT (v17): Peter GRIEVED by the third asking — his hand come up to his own face, breaking.",
        "must_not_show": "not resentful at being asked again; grieved, which is the word the text uses. Do not put Jesus in this frame.",
        "scene": (
            "Close on Peter on the third answer, one big hand come up and pressed hard "
            "over his eyes and forehead, his head bowed, his mouth open and working. "
            "His shoulders have collapsed forward. It is grief, not irritation — the "
            "asking has opened him all the way up. Warm coal light on his hunched "
            "shape. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b26", "out": "s26-feed-my-sheep.jpeg", "seg": "j2 + n13",
        "window": "117.45-126.90", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "FIRE", "SHORE-DAWN"],
        "narration": ("Feed my sheep. (John 21:17) — To the man who had failed him "
                      "worst, Jesus handed the biggest job of all. He did not only "
                      "forgive Peter. He trusted him again."),
        "must_show": "⚠️ THE COMMISSION: Jesus's hand gripping Peter's shoulder or forearm as he gives him the job — a handover, not a pardon.",
        "must_not_show": "no halo, glare or rim-light; Peter is not kneeling or grovelling — he is being given work, and the posture should say that.",
        "scene": (
            "Jesus has leaned across the burnt-down coals and taken Peter by the "
            "shoulder with one firm hand, speaking directly into his face. Peter has "
            "come up out of his hunch and is looking back at him, wet-faced and "
            "astonished, sitting upright. It reads as a job being handed over rather "
            "than a pardon being granted. Behind them the flat lake and the low gold "
            "morning. The camera is back far enough to hold both men and the fire. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r019-b27", "out": "s27-hands-you-back-your-life.jpeg", "seg": "n14",
        "window": "127.52-135.79", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "SHORE-DAWN"],
        "narration": ("That is how good he is. He takes your worst night and hands you "
                      "back your life, with a purpose bigger than the one you thought "
                      "you had thrown away."),
        "must_show": "the closing frame: the two walking together up the shore in the full gold morning, the fire and the boat behind them.",
        "must_not_show": "no halo, glare or rim-light; nothing triumphant — two men walking on a beach in the morning.",
        "scene": (
            "The two men are walking away up the shingle shore together in the full "
            "low gold of the morning, seen from behind and to one side, Jesus's hand "
            "resting on Peter's shoulder as they go and Peter's head turned toward him "
            "listening. Behind them the little fire is a thread of smoke on the sand "
            "and the boat lies pulled up with the heavy net beside it. The lake is "
            "flat and bright and the beach runs on ahead of them. The camera is well "
            "back. Every figure has two arms, two hands and one head."
        ),
    },
]
