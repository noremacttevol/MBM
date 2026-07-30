#!/usr/bin/env python3
"""V2 beat map — row 7, build-07-peter-water (Matthew 14:22-33).

Consumed by media-production-v2/v2_prompt.py. STYLE-V2, the forced-wide defense
line, the anti-panel clause and JESUS LOCK v4 are prepended by the assembler so
they stay byte-identical across every prompt.

COVERAGE (STORY-COVERAGE-LAW): 37 pictures against V1's 12 unique stills, over
202.1 s — 5.5 s per picture, the same band as rows 5 and 6. The count sits where
it does because this row is almost entirely PHYSICAL EVENTS rather than
commentary, and each one is a separate thing happening: the sighting chain, the
leg over the gunwale, the walk, the look down, the surface giving, the sink, the
catch, the walk back, the sea going flat. Ken Burns cannot fake any of those.

⚠️ THIS ROW IS THE MOST-REJECTED STORY IN V1. It was rebuilt FOUR times. Every
defect it was rejected for is written into the beats below as an explicit
must_show / must_not_show, because prose alone did not hold them last time:

  1. FEET ON THE SURFACE (Standing Law, V1 rejection #1 and #3). A figure walking
     on the sea must have BOTH FEET RESTING ON TOP OF UNBROKEN WATER with ripple
     rings spreading from each sole — never ankle-deep, never calf-deep, never
     "wading". Every water beat states it in full. The ONLY figure ever in the
     water is Peter after he begins to sink (b21-b24), and even there Jesus's own
     feet stay on the surface.
  2. WALK DIRECTION LOCKED BY SIDE-VIEW GEOMETRY (V1 fix, Machine C 2026-07-17).
     A head-on shot cannot tell the viewer who is moving toward whom. So the two
     travelling shots are staged from the side with the frame positions named:
     b16 Peter on the LEFT moving right toward Jesus; b29 both moving left to
     right toward the boat. Never re-stage these head-on.
  3. FIGURES STAY INSIDE THE BOAT (Standing Law j). In every boat frame the deck
     is under their feet and the gunwale runs around behind them. Nobody stands
     on water unless the scripture puts him there — which here is Jesus, and
     Peter for exactly nine beats.
  4. TIME-OF-DAY LAW (Cameron, 2026-07-10 — the rejection that killed storm V2).
     Matthew 25 says THE FOURTH WATCH — 3 to 6 in the morning — and the
     narration itself ends "lay down flat UNDER THE STARS". So from b04 to the
     last frame it is NIGHT: broken moonlight through torn cloud, stars in the
     gaps, white foam, one guttering lamp in the bow. There is NO sunrise, NO
     dawn band on the horizon and NO warm sky anywhere in this build. The
     SEA-NIGHT lock states that as a positive description, not as a negation,
     because negations do not hold (row 2's PHARISEES lesson).
  5. Peter is BAREFOOT in every water shot, for continuity across the sequence.

SCRIPTURE FACTS THAT GOVERN THE PICTURES (Matthew 14 KJV):
  v22-23 he CONSTRAINED them into the ship and sent the multitudes away, then
         went up into a mountain APART to pray; "when the evening was come, he
         was there alone."
  v24    the ship was in the MIDST of the sea, tossed, "for the wind was contrary."
  v25    "in the FOURTH WATCH of the night Jesus went unto them, WALKING ON THE SEA."
  v26    "It is a SPIRIT; and they CRIED OUT for fear."
  v28-29 Peter asks to be bidden; "COME"; "when Peter was come DOWN OUT OF THE
         SHIP, he WALKED ON THE WATER, to go to Jesus." He gets out of the boat
         himself — nobody helps him over.
  v30    "when he saw the wind boisterous, he was AFRAID; and BEGINNING to sink"
         — beginning. He goes down by degrees, not straight under.
  v31    "IMMEDIATELY Jesus stretched forth his hand, and CAUGHT him" — the whole
         point of the narration's middle section. No pause, no lesson first.
  v32    "when they were come INTO the ship, the wind ceased" — the calm arrives
         only after both men are aboard, so b31/b32 come after b30, never before.
  v33    "they that were in the ship came and WORSHIPPED him."

CONTENT-CARE: row 7 is not in the §3 flag table = GREEN. No adversary, no
violence. The one care note is emotional: the men's terror at b08 is real fear,
never horror-genre — no ghoulish figure, no supernatural distortion. What they
see is simply a man on the water in the dark, and that is frightening enough.

TIME-OF-DAY ARC: b01-b02 dusk on the shore and hillside (after the feeding,
v23) · b03 full night on the mountain · b04 to the end THE FOURTH WATCH, deep
night. The sea goes flat under STARS at b32 and stays night through the last
frame.
"""

LOCKS = {
    # SETTING LOCKS NAME NO CHARACTER (STRAY-JESUS defect).
    "SEA-NIGHT": (
        "SEA-NIGHT LOCK: the Sea of Galilee in the fourth watch of the night, hours "
        "before any dawn. The sky is NIGHT — torn fast-moving storm cloud with hard "
        "black gaps where cold white stars show through, and a high broken moon "
        "throwing silver edges onto the cloud and hard white crests onto the water. "
        "The sea is deep blue-black, running in steep short waves with white foam "
        "tearing off the tops, and cold spray hangs in the air. The far shore is a "
        "black line of hills with no light on it. Every colour in the frame is cold "
        "— silver, black, blue-black and foam white."
    ),
    "BOAT": (
        "BOAT LOCK: one open first-century Galilean fishing boat about eight paces "
        "long — heavy overlapping wooden planks dark with water, a low gunwale "
        "running right around the hull, a short mast with its small square sail "
        "reefed down hard, long oars through leather-strapped tholes along both "
        "sides, coiled rope, folded nets and a stone anchor stowed on the deck "
        "timbers, and one small clay oil lamp guttering in a shelter at the bow. The "
        "deck planking is always visible under the men's feet."
    ),
    # Cameron, 2026-07-30: "the boat must always have a mast and look the same and it
    # needs to have all of his disciples in it and how they look should come from the
    # reference book, and it shouldn't change much."
    # v1 said "the same seven or eight throughout", which let both the COUNT and the
    # faces move between frames. The crew is now a fixed, stated number.
    #
    # Peter also had NO lock at all in this build, so nothing held HIS face still —
    # in the story where he is the second lead. Naming PETER in a beat's locks also
    # makes the API engine attach his CAST-V2-REF sheets, which is what actually holds
    # a face (the lesson row 2 paid for when the elder son came back as three men).
    "PETER": (
        "PETER LOCK: Peter is the same man in every shot — a sturdy Galilean fisherman "
        "in his late thirties, broad and powerfully built, thick dark curly hair "
        "plastered flat with water, a full dark beard, weathered warm-olive skin, deep "
        "brown eyes, heavy honest features. He wears a soaked BLUE-GREY wool tunic "
        "with a plain rope belt and is BAREFOOT (never cream, never off-white). His "
        "face is shown clearly and does not change between frames."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the boat carries ELEVEN other men besides Peter — the same "
        "eleven in every single frame, never more and never fewer, so the crew never "
        "changes size between pictures. Each man keeps the SAME face, the same hair "
        "and the same tunic colour in every frame he appears in. They are "
        "Galilean fishermen and working men between twenty and forty, "
        "dark hair and beards plastered flat with water, weathered olive skin, big "
        "rope-scarred hands. They wear soaked wool tunics in SATURATED DEEP colours "
        "— rust-brown, deep russet, dark olive, blue-grey and dusty indigo — belted "
        "with rope or leather. EVERY SINGLE TUNIC IN THE BOAT IS PLAINLY AND OBVIOUSLY "
        "DARKER THAN THE ONE CREAM ROBE JESUS WEARS, so that he is the only pale figure "
        "anywhere in the picture — none of them wears off-white, ivory, cream, beige, "
        "tan or any near-white cloth. Their faces are shown clearly."
    ),
    "SHORE": (
        "SHORE LOCK: the grassy north-east shore of the lake at dusk — trodden green "
        "grass running down to a shingle beach, reed baskets set about, a second "
        "boat drawn up on the stones, the dark water beginning beyond, and bare "
        "hills rising behind."
    ),
    "MOUNTAIN": (
        "MOUNTAIN LOCK: a bare rocky hillside high above the lake — shelves and "
        "outcrops of pale limestone, low thorn scrub, a thin goat path winding up "
        "through the stones, and the wide dark sheet of the lake spread out far "
        "below with the black hills of the far shore beyond it."
    ),
}

REF = True

BEATS = [
    # ------------------------------------------------ n0 — before the storm ----
    {
        "id": "v2-r007-b01", "out": "s01-he-sent-them-ahead.jpeg", "seg": "n0 p1-p2",
        "window": "0.28-11.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "SHORE", "BOAT"],
        "narration": ("Jesus had just fed more than five thousand people with a few "
                      "loaves of bread and two small fish. And when it was done, he "
                      "told his disciples to take the boat and cross the lake ahead "
                      "of him."),
        "must_show": "the shore just after the feeding — full baskets of broken bread still standing on the grass — and the disciples pushing the boat off the shingle at Jesus's word.",
        "must_not_show": "no halo, glare or rim-light; not night yet — this is dusk; nobody is on the water yet.",
        "scene": (
            "Dusk on the lake shore just after the feeding. Twelve heaped reed baskets "
            "of broken bread still stand on the trodden grass in the foreground and "
            "the last of an enormous crowd is thinning away up the slope behind. At "
            "the water's edge Peter and three other disciples have their shoulders "
            "against the bow of the fishing boat, shoving it off the shingle into the "
            "shallows, one man already swinging a leg over the gunwale. Jesus stands "
            "on the grass a few paces up the beach with one hand lifted toward the "
            "far side of the lake, sending them. The light is the last cold blue of "
            "evening. The camera is back far enough to hold the boat, the men and "
            "Jesus head to sandals. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b02", "out": "s02-alone-up-the-hill.jpeg", "seg": "n0 p3-p4",
        "window": "11.34-16.50", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN"],
        "narration": ("He sent the crowds home. And then he climbed a mountain, "
                      "alone, to pray."),
        "must_show": "the crowd streaming away far below while he climbs the goat path up the bare hillside alone, going the opposite way from everybody else.",
        "must_not_show": "no halo, glare or rim-light; nobody accompanying him — the aloneness is the picture.",
        "scene": (
            "Last light. Jesus climbs alone up the thin goat path through the "
            "limestone outcrops of the hillside, seen from partway up the slope so "
            "that the whole valley opens behind him. Far below, the long dark thread "
            "of the crowd is winding away from the shore toward the villages, "
            "hundreds of small figures all moving the other way. He is the only "
            "person on the hill. The sky has gone deep blue and the first stars are "
            "showing. The camera is back far enough to see him head to sandals "
            "against the slope. He has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b03", "out": "s03-talking-with-his-father.jpeg", "seg": "n0 p5-p7",
        "window": "16.50-22.80", "wide": True, "jesus": True, "ref": REF,
        "locks": ["MOUNTAIN", "BOAT", "DISCIPLES"],
        "narration": ("That is where the night found him. Not in the boat. On the "
                      "mountain, talking with his Father."),
        "must_show": "him kneeling in prayer high on the rock at night — and far below in the same frame, the black lake with one tiny point of lamplight on it where the boat is.",
        "must_not_show": "no halo, glare or rim-light of any kind; no beam of light from the sky; the only light is moon and stars.",
        "scene": (
            "Full night on the mountain. Jesus kneels on a shelf of bare limestone "
            "near the top of the slope, his head bowed and his hands resting open on "
            "his knees, entirely still, speaking. Cold moonlight comes through breaks "
            "in the moving cloud and lays silver along the rock and his shoulders. "
            "Far below and far out, the lake is a black sheet, and on it there is one "
            "tiny lonely point of orange lamplight — the boat, already a long way "
            "out. Stars show in the gaps of the cloud. The camera is well back so the "
            "whole hillside, the man and the lake below are in one frame. He has two "
            "arms, two hands and one head."
        ),
    },
    # ----------------------------------------------------- n1 — all night ----
    {
        "id": "v2-r007-b04", "out": "s04-the-wind-was-contrary.jpeg", "seg": "n1 p1-p3",
        "window": "23.36-34.57", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": ("Out on the water, the wind turned against the boat. The waves "
                      "rose. The disciples — several of them fishermen who had worked "
                      "this lake their whole lives — rowed against it for hours."),
        "must_show": "ACTION-LOGIC: the men are ROWING — oar blades biting the water outside the hull, both hands on each loom, bodies leaning back into the stroke, feet braced on the deck timbers.",
        "must_not_show": "no oar held in the air doing nothing; nobody standing on the water; nobody outside the hull; no dawn or sunset colour anywhere in the sky.",
        "scene": (
            "The boat is deep in the black open water, heeled hard over as a steep "
            "wave lifts the bow. Four men are at the oars along both sides — each "
            "with both hands locked on the loom, shoulders and backs hauled right "
            "back into the stroke, feet braced against the deck timbers, the oar "
            "blades biting into the water outside the hull and throwing white. Two "
            "more crouch low amidships hauling a line on the reefed sail. Every man "
            "is soaked and inside the boat with the gunwale running behind them. The "
            "small lamp in the bow shelter is bent flat by the wind. Cold spray "
            "across the whole frame. Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b05", "out": "s05-the-fourth-watch.jpeg", "seg": "n1 p4-p6",
        "window": "34.57-45.09", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": ("Matthew tells us it was the fourth watch of the night when help "
                      "came. That means between three and six in the morning. They had "
                      "been fighting that sea nearly all night."),
        "must_show": "exhaustion at the far end of a night — heads down, raw hands still on the looms, one man looking up at the stars through a break in the cloud to read the hour.",
        "must_not_show": "NO hint of dawn — not a warm band on the horizon, not a paling sky; it is the middle of the night and the stars are the only clock they have.",
        "scene": (
            "The boat wallows in the black troughs, further out and lower in the "
            "water. The men are at the end of their strength — one has his forehead "
            "down on the loom of his oar between strokes, another is flexing a raw "
            "bleeding palm open and shut, Peter sits back on the thwart with his "
            "chest heaving and his soaked hair flat to his skull. One man has his "
            "head tipped right back, looking up through a hard black gap in the "
            "racing cloud at the cold stars to read how much of the night is left. "
            "The horizon all around is black on black. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    # --------------------------------------------- n2 — the sighting burst ----
    {
        "id": "v2-r007-b06", "out": "s06-something-out-there.jpeg", "seg": "n2 p1-p3",
        "window": "45.59-53.59", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": ("And then, through the spray and the dark, they saw something "
                      "that made grown fishermen scream. A figure. Walking toward them."),
        "must_show": "the men in the boat frozen mid-stroke, one half risen and pointing out over the water — and far out in the dark a small upright human shape, indistinct through the spray, clearly OUT ON the open water and clearly coming nearer.",
        "must_not_show": "the distant figure must be an ordinary man-shape, never a ghoul, never glowing, never distorted; his face is not readable yet at this distance; do not attach a Jesus lock or ref to this beat — he is deliberately unrecognisable here.",
        "scene": (
            "In the boat every oar has stopped mid-stroke. One man is half risen off "
            "the thwart with his arm flung straight out over the gunwale, pointing; "
            "the others have turned to follow his hand, faces white and mouths open. "
            "Far out beyond the bow, small with distance and half lost in the flying "
            "spray, a single upright human shape is moving across the open black "
            "water toward them — plainly a man, plainly standing, plainly out where "
            "there is nothing to stand on. He is too far off for his face to be made "
            "out. Broken moonlight on the crests between him and the boat. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b07", "out": "s07-on-top-of-the-water.jpeg", "seg": "n2 p4",
        "window": "53.59-55.22", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SEA-NIGHT"],
        "narration": "On top of the water.",
        "must_show": "THE FEET. Low and close on the water surface: both of Jesus's feet resting ON TOP of unbroken water, taking his weight, with a ring of ripples spreading out from each sole.",
        "must_not_show": "NOT ankle-deep, NOT calf-deep, NOT wading, NOT standing on a rock or a sandbar — the surface is whole and unbroken beneath his soles; no glare, glow or light on the water.",
        "scene": (
            "An upright vertical photograph taken from a low viewpoint just above the "
            "sea, looking across it — the water is at the bottom of the frame and the "
            "night sky is at the top, and the horizon is level; the picture is the "
            "right way up. Both "
            "of Jesus's bare feet are resting ON TOP OF THE WATER, the surface whole "
            "and unbroken beneath his soles, taking his full weight — the skin of the "
            "water dimpling slightly under each heel and a clean ring of ripples "
            "spreading outward from each foot across the swell. No part of his feet "
            "or ankles is below the surface. The wet hem of his robe swings just "
            "above the water. Around and beyond, black waves run past with white foam "
            "tearing off them under broken moonlight. Each foot has five toes."
        ),
    },
    {
        "id": "v2-r007-b08", "out": "s08-they-cried-out.jpeg", "seg": "n2 p5",
        "window": "55.22-59.74", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": "They cried out that it was a ghost — because nobody walks on the sea.",
        "must_show": "pure terror inside the boat — men shouting, recoiling backwards over the thwarts, one throwing an arm up in front of his face, an oar dropped and swinging loose.",
        "must_not_show": "no horror-film imagery of any kind and nothing supernatural in the frame — the fear is entirely on the men's faces; do not show the figure in this shot at all. Nobody leaves the hull.",
        "scene": (
            "Inside the boat, terror. Three men are shouting at once with their mouths "
            "wide, scrambling backwards over the thwarts away from the bow; one has "
            "thrown a forearm up across his own face; another has let go of his oar "
            "entirely and it swings loose in the thole. Peter is half up on one knee "
            "on the deck timbers, gripping the gunwale, staring out past the bow with "
            "his whole face open in fright. Everyone is inside the hull with the "
            "gunwale running behind them and the deck under them. The lamp in the bow "
            "throws hard shaking orange up under their chins against the black night. "
            "Every figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b09", "out": "s09-a-voice-they-knew.jpeg", "seg": "n2 p6",
        "window": "59.74-64.03", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": "But the voice that came back across the water was one they knew.",
        "must_show": "the recognition landing — the shape is close enough now to be plainly Jesus, both feet on the surface, and in the boat the shouting has stopped dead.",
        "must_not_show": "no halo, glare or rim-light; his feet are not in the water at any depth; the men are not yet glad, only stunned into silence.",
        "scene": (
            "Jesus is close in now, standing on the open water off the boat's bow "
            "with both bare feet ON TOP of the unbroken surface, ripple rings "
            "spreading from each foot, his dry robe and hair driven sideways by "
            "the wind, his face plainly and unmistakably his own in the lamplight and "
            "the broken moonlight. In the boat every man has gone completely still — "
            "mouths still open from shouting but no sound left in them, one man's "
            "pointing arm frozen halfway down. Peter is up at the gunwale staring. "
            "The camera is back far enough to hold Jesus on the water and the boat "
            "with its men in one frame. Every figure has two arms, two hands and one "
            "head."
        ),
    },
    {
        "id": "v2-r007-b10", "out": "s10-be-not-afraid.jpeg", "seg": "j1",
        "window": "64.61-67.53", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT", "BOAT", "DISCIPLES"],
        "narration": "Be of good cheer; it is I; be not afraid. (Matthew 14:27)",
        "must_show": "close on Jesus out on the water speaking across to them — calm, steady, entirely ordinary in the middle of a storm.",
        "must_not_show": "no halo, glare or rim-light; no strain or shouting in his face; his feet are not in frame here, so nothing about them can go wrong.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "Close on Jesus from the chest up, out on the open water in the dark, "
            "speaking toward the boat. Water runs off his hair and beard and the wind "
            "drags his dry robe sideways, and his face is completely calm — level "
            "eyes, an easy mouth, a man saying something reassuring in the middle of "
            "a gale as though it cost him nothing. One hand is lifted a little in "
            "front of him. Black water and white foam run past behind him under "
            "broken moonlight."
        ),
    },
    # ---------------------------------------------- n3 / s28 — Peter asks ----
    {
        "id": "v2-r007-b11", "out": "s11-what-peter-wanted.jpeg", "seg": "n3",
        "window": "69.09-76.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": ("Think about what Peter was asking for. Not for the storm to "
                      "stop. To come out into it — to where Jesus stood."),
        "must_show": "close on Peter at the gunwale, both hands locked on the rail, leaning out into the wind and looking off at the water — the want plain on his face.",
        "must_not_show": "he is NOT frightened here and NOT climbing out yet; he stays inside the hull with the deck under him. Do not put Jesus in this frame.",
        "scene": (
            "Close on Peter inside the boat, both big hands clamped on the wet "
            "gunwale, leaning his weight forward and out into the wind with the deck "
            "timbers under his braced feet. Spray is hitting him full in the face and "
            "he is not flinching from it. He is looking out and away across the black "
            "water, and his expression is not fear — it is longing, and something "
            "close to recklessness, a man already deciding. The lamp behind him picks "
            "out his soaked beard and the water running off his jaw. Each hand has "
            "five fingers."
        ),
    },
    {
        "id": "v2-r007-b12", "out": "s12-bid-me-come.jpeg", "seg": "s28",
        "window": "77.23-80.48", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": ("Lord, if it be thou, bid me come unto thee on the water. "
                      "(Matthew 14:28)"),
        "must_show": "Peter standing up in the boat calling out across the water to Jesus, the other men staring at him as if he has lost his mind.",
        "must_not_show": "no halo, glare or rim-light; Peter is still INSIDE the boat, deck under his feet; Jesus's feet stay on top of the surface.",
        "scene": (
            "Peter has come to his feet on the deck timbers in the pitching boat, one "
            "hand still on the gunwale for balance and the other cupped to his mouth, "
            "shouting out across the water. Out on the black sea a few boat-lengths "
            "off, Jesus stands with both bare feet ON TOP of the unbroken surface, "
            "ripple rings around them, listening. In the boat behind Peter the other "
            "men have turned to stare up at him, one gripping his arm to pull him "
            "back down, every face saying he has gone mad. The camera is back far "
            "enough to hold the boat and Jesus in one frame. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b13", "out": "s13-come.jpeg", "seg": "j2 + n4 p1",
        "window": "82.05-85.06", "wide": False, "jesus": True, "ref": REF,
        "locks": ["SEA-NIGHT", "BOAT", "DISCIPLES"],
        "narration": "Come. (Matthew 14:29) — One word.",
        "must_show": "close on Jesus saying the single word, one hand come open and out toward the boat in the same movement — welcome, not command.",
        "must_not_show": "no halo, glare or rim-light; nothing dramatic in the gesture; it is small and easy, which is the point.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "A WIDE SIDE-ON view across the open sea, the camera at a distance and "
            "level with the horizon. Jesus stands FAR OUT on the open water, well "
            "clear of the boat with many paces of black water between them, seen full "
            "length from his head down to his feet on the surface. He has just spoken "
            "one short word. HIS HEAD IS TURNED TOWARD THE BOAT AND HIS EYES ARE "
            "LOOKING DIRECTLY AT PETER — straight at the man in the boat, NOT at the "
            "camera and NOT out to sea. His face and shoulders are angled toward the "
            "boat, and his near hand is open and low, palm upward, reaching toward "
            "Peter in an unhurried invitation. His face is warm and certain and "
            "quietly glad. "
            "The fishing boat sits to one side of the frame with its mast up, and "
            "ELEVEN other men are CLEARLY VISIBLE crowded inside it along the gunwale "
            "— faces lit by the lamp, all of them staring out at the water — while "
            "Peter is swinging one leg over the side to come down to him. The boat is "
            "never empty. Black waves and white foam run past "
            "under the broken moon. His hand has five fingers."
        ),
    },
    # ------------------------------------------------- n4 — out of the boat ----
    {
        "id": "v2-r007-b14", "out": "s14-leg-over-the-side.jpeg", "seg": "n4 p2a",
        "window": "85.06-87.4", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": "And Peter put his leg over the side of that pitching boat,",
        "must_show": "the physical act: one bare leg swung right over the gunwale, both hands white-knuckled on the rail taking his weight, his bare foot reaching down toward the water surface below.",
        "must_not_show": "nobody is helping or lifting him — v29 says he came down out of the ship himself; his foot has not touched the water yet.",
        "scene": (
            "Close and low. Peter has swung one bare leg right over the wet gunwale of "
            "the pitching boat and is straddling it, both hands white-knuckled on the "
            "rail carrying his whole weight, his soaked tunic dragged up over the "
            "planking. His bare foot hangs down below the hull, reaching toward the "
            "black water still a hand's breadth beneath it, toes spread. Nobody else's "
            "hands are on him. The dark planks of the hull, the rope and the loom of "
            "an oar fill the frame around him. Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r007-b15", "out": "s15-stood-up-on-the-sea.jpeg", "seg": "n4 p2b",
        "window": "87.4-89.73", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": "and stood up on the sea.",
        "must_show": "both of Peter's bare feet ON TOP of the unbroken water taking his weight, ripple rings spreading from each sole, one hand still hanging onto the boat's rail behind him.",
        "must_not_show": "NOT ankle-deep, NOT knee-deep, NOT wading — the surface is whole beneath both soles; he has not let go of the boat yet.",
        "scene": (
            "Peter is standing OUT ON THE WATER beside the hull. Both his bare feet "
            "rest ON TOP of the unbroken surface, taking his full weight — the water "
            "dimpling under his soles and clean rings of ripple spreading outward from "
            "each foot across the swell — with no part of his feet or ankles below the "
            "surface. His knees are bent and braced like a man on a moving deck. One "
            "big hand is still hooked hard over the boat's gunwale behind him, not "
            "ready to let go, and his face is somewhere between terror and disbelief "
            "as he looks down at his own feet. Black water, white foam, broken "
            "moonlight. Each foot has five toes."
        ),
    },
    # ------------------------------------------------------ n4b — the walk ----
    {
        "id": "v2-r007-b16", "out": "s16-step-after-step.jpeg", "seg": "n4b p1-p2",
        "window": "90.31-95.89", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT", "BOAT", "DISCIPLES"],
        "narration": ("And he was doing it. Step after step on the moving water, his "
                      "eyes fixed on Jesus."),
        "must_show": "SIDE VIEW, camera level with the sea. PETER IS ON THE LEFT OF THE FRAME AND JESUS ON THE RIGHT, and Peter is walking LEFT TO RIGHT toward Jesus, mid-stride, both men's feet on top of the water.",
        "must_not_show": "NEVER stage this head-on — a head-on shot cannot tell the viewer who is walking toward whom, which is exactly what got V1 rejected. Peter has let go of the boat and his hands are free.",
        "scene": (
            "A SIDE VIEW with the camera down at the level of the sea. PETER IS ON THE "
            "LEFT of the frame and JESUS STANDS ON THE RIGHT, and Peter is walking "
            "LEFT TO RIGHT across the open water toward him, caught mid-stride with "
            "one bare foot lifted and swinging forward and the other planted. Both of "
            "Peter's feet, planted and lifting, are ON TOP of the unbroken surface "
            "with ripple rings spreading from them; Jesus's bare feet ahead of him are "
            "the same. Peter's arms are out from his sides for balance, both hands "
            "free and away from anything, and his eyes are locked straight ahead on "
            "Jesus's face. The boat is a dark shape far behind him on the left. "
            "Neither man is submerged to any depth at all. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b17", "out": "s17-where-only-god-can-walk.jpeg", "seg": "n4b p3",
        "window": "95.89-100.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": ("For a moment, an ordinary fisherman walked where only God can "
                      "walk."),
        "must_show": "a wide, pulled-right-back view: two small human figures standing out on an enormous black sea under torn cloud, the boat small behind them — the scale of what is happening.",
        "must_not_show": "no halo, glare or rim-light; both men's feet stay on top of the surface even at this distance; no dawn colour in the sky.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "The camera is pulled far back and slightly up. Two small human figures "
            "stand out on an enormous running black sea — Peter mid-stride and Jesus "
            "waiting a little ahead of him — both plainly ON TOP of the water with "
            "pale ripple rings around their feet, and the huge torn cloud and cold "
            "stars filling the sky above them. The fishing boat is a small dark shape "
            "with one orange lamp some way behind, its men's faces just pale specks "
            "along the gunwale. White crests run everywhere between them. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    # ------------------------------------------------- n5 — he looks down ----
    {
        "id": "v2-r007-b18", "out": "s18-the-wind-tearing-at-him.jpeg", "seg": "n5 p1",
        "window": "100.93-102.66", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": "Then he noticed the wind tearing at him.",
        "must_show": "the wind hitting him — hair and soaked tunic dragged hard sideways, spray across his face, his head just beginning to turn away from straight ahead.",
        "must_not_show": "he has not looked down yet and has not begun to sink; his feet are still on the surface. Do not put Jesus in this frame.",
        "scene": (
            "Close on Peter alone out on the water. The wind has him — his soaked "
            "tunic is dragged flat and streaming off one shoulder, his hair and beard "
            "torn sideways, a sheet of cold spray breaking across his face and chest. "
            "His eyes have narrowed against it and his head has just started to turn "
            "off the line it was holding. His bare feet below him are still on top of "
            "the unbroken surface with ripple rings around them. Black water and hard "
            "white foam all around."
        ),
    },
    {
        "id": "v2-r007-b19", "out": "s19-he-looked-down.jpeg", "seg": "n5 p2",
        "window": "102.66-106.18", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": "He looked down at the waves instead of ahead at Jesus.",
        "must_show": "SIDE VIEW again, Peter LEFT and Jesus RIGHT: Peter's head and eyes are turned DOWN at the water at his feet, and Jesus is still ahead of him, out of his eyeline.",
        "must_not_show": "he has not begun to sink in this frame — his feet are still on top of the surface; the failure is in where he is looking, and that must be unmistakable.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "The same SIDE VIEW at sea level, PETER ON THE LEFT and JESUS ON THE "
            "RIGHT. Peter has stopped mid-stride and his head has dropped — his chin "
            "is down on his chest and his eyes are fixed straight down at the steep "
            "black water running past his own feet, his arms come up and out in "
            "alarm. His feet are still resting on top of the unbroken surface. Ahead "
            "of him on the right Jesus still stands waiting with his hand out, "
            "completely outside the line of Peter's lowered eyes. The gap of black "
            "water between them is clear. Every figure has two arms, two hands and "
            "one head."
        ),
    },
    # ---------------------------------------------------- n5b — he sinks ----
    {
        "id": "v2-r007-b20", "out": "s20-the-water-stopped-holding.jpeg", "seg": "n5b p1",
        "window": "106.75-109.57", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": "And the moment his eyes moved, the water stopped holding him.",
        "must_show": "THE SURFACE GIVING WAY: one foot has broken through and gone in to the shin, the other still on top, the water torn open around the sinking leg.",
        "must_not_show": "he is not to the waist yet — v30 says BEGINNING to sink, and this frame is the beginning; do not put Jesus in this frame.",
        "scene": (
            "An upright vertical photograph, low and close on Peter's legs and lower "
            "body, with the sea at the bottom of the frame and the night sky at the "
            "top and the horizon level — the picture is the right way up. The surface "
            "has GIVEN WAY "
            "under one foot — that leg has punched through and gone into the black "
            "water to the shin, torn white water flying up around it — while his other "
            "bare foot is still up on the unbroken surface behind him, taking the last "
            "of his weight. His body has pitched forward and sideways off balance and "
            "his arms are flying up. The exact edge where the surface breaks is clear "
            "and violent. Black sea, hard white foam, broken moonlight."
        ),
    },
    {
        "id": "v2-r007-b21", "out": "s21-down-to-his-waist.jpeg", "seg": "n5b p2",
        "window": "109.57-114.50", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": ("He dropped to his waist, mid-stride, and cried out the shortest "
                      "prayer in the Bible."),
        "must_show": "Peter IN the water to the waist, caught mid-stride, one arm thrown up out of the sea toward Jesus — and Jesus still standing ON TOP of the surface a stride away.",
        "must_not_show": "Peter is the ONLY figure in the water; Jesus's feet must stay on the unbroken surface even here — that contrast is the whole frame. No halo, glare or rim-light.",
        "scene": (
            "Peter has gone down into the black sea to the waist, caught in the middle "
            "of the stride he was taking, the water closed around him and a wave "
            "breaking over his shoulder. One arm is flung straight up out of the water "
            "toward Jesus and his face is turned up and open, shouting. A stride away "
            "from him Jesus is still standing ON TOP of the unbroken surface with "
            "ripple rings around his bare feet, already moving toward him. Peter is "
            "the only figure in the water. The camera is close enough to read both "
            "faces and wide enough to hold both men. Every figure has two arms, two "
            "hands and one head."
        ),
    },
    {
        "id": "v2-r007-b22", "out": "s22-lord-save-me.jpeg", "seg": "s30",
        "window": "115.07-116.37", "wide": False, "jesus": False, "ref": False,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": "Lord, save me. (Matthew 14:30)",
        "must_show": "close on Peter's face in the water — mouth open on the shout, sea streaming off him, his one hand reaching straight up out of frame.",
        "must_not_show": "no dignity-posing — this is a drowning man; do not put Jesus in this frame.",
        "scene": (
            "Very close on Peter's face and lifted arm in the black water. Sea is "
            "streaming off his hair and beard and pouring down his upturned face, his "
            "eyes are wide and his mouth is open on a shout, and his one big hand is "
            "stretched straight up above him, fingers spread, reaching out of the top "
            "of the frame. A wave is breaking white right behind his shoulder. His "
            "hand has five fingers."
        ),
    },
    # ---------------------------------------------------- n6/n7 — the catch ----
    {
        "id": "v2-r007-b23", "out": "s23-and-jesus-caught-him.jpeg", "seg": "n6",
        "window": "117.93-120.58", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": "And Jesus caught him. Immediately.",
        "must_show": "THE CATCH — Jesus's hand clamped hard around Peter's forearm, wrist to wrist, the grip visibly taking his whole weight out of the sea.",
        "must_not_show": "no halo, glare or rim-light; no light at the point of contact; it is a plain hard physical grab, and it has already happened.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "Close on two forearms locked together above the black water. Jesus's hand "
            "is clamped hard around Peter's wrist and Peter's hand around his, the "
            "grip so tight the knuckles have gone pale and the tendons stand out along "
            "both arms, sea water streaming off them. Peter's arm comes up out of the "
            "torn white water at the bottom of the frame; the whole weight of a heavy "
            "man is plainly hanging on that one grip. Nothing else is in focus. Each "
            "hand has five fingers."
        ),
    },
    {
        "id": "v2-r007-b24", "out": "s24-there-was-no-pause.jpeg", "seg": "n7 p1-p5",
        "window": "121.14-131.49", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": ("Matthew uses that exact word. There was no pause. No lesson "
                      "first. No letting him go under to teach him something. The hand "
                      "was there before the prayer was finished."),
        "must_show": "Peter's face looking up out of the water at Jesus while the grip holds him — held, not yet lifted, and not sinking any further.",
        "must_not_show": "he must NOT be going under; the water level on him does not rise past the waist from here on; no halo, glare or rim-light.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "Close on Peter held in the water, the sea around him at his waist and "
            "going no higher, his face turned right up out of it. He is soaked and "
            "gasping and his eyes are fixed up on Jesus with something breaking open "
            "behind them. Jesus's forearm comes down into the frame from above, the "
            "hand still locked around Peter's wrist, absolutely steady, holding him "
            "exactly where he is. The black water is still tearing past them both. "
            "Each hand has five fingers."
        ),
    },
    {
        "id": "v2-r007-b25", "out": "s25-holding-him-above-it.jpeg", "seg": "n7 p6",
        "window": "131.49-137.25", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT", "BOAT", "DISCIPLES"],
        "narration": ("And from that grip — holding him above the water — Jesus asked "
                      "him one question."),
        "must_show": "Jesus has pulled him up so Peter is out of the sea and standing again — the two of them face to face on the surface, the grip still unbroken between them.",
        "must_not_show": "no halo, glare or rim-light; both men's feet are back ON TOP of the unbroken surface with ripple rings; they are NOT in the boat yet.",
        "scene": (
            "Jesus has hauled Peter clear. The two men stand face to face out on the "
            "open water, close enough to touch, with Jesus's hand still locked around "
            "Peter's forearm between them and Peter's other hand gripping Jesus's "
            "shoulder. Both men's bare feet are back ON TOP of the unbroken surface "
            "with ripple rings spreading around them; neither is submerged. Peter is "
            "streaming with water and unsteady, his head down and coming up; Jesus is "
            "steady, holding him. The dark boat is far off behind them. The camera is "
            "back far enough to see both men head to feet. Every figure has two arms, "
            "two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b26", "out": "s26-wherefore-didst-thou-doubt.jpeg", "seg": "j3",
        "window": "137.82-140.84", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": ("O thou of little faith, wherefore didst thou doubt? "
                      "(Matthew 14:31)"),
        "must_show": "close on Jesus's face asking it — genuinely asking, warm, almost puzzled; a real question and not a rebuke.",
        "must_not_show": "NO scolding, NO disappointment, NO hard eyes — the whole narration hangs on how this is asked; get this face wrong and the video's point is lost. No halo, glare or rim-light.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "Very close on Jesus's face out on the dark water, streaming wet, speaking "
            "to the man he is holding. His expression is warm and open and very "
            "slightly puzzled — brows lifted rather than drawn down, the mouth soft, "
            "the eyes steady and kind — the face of someone asking a real question he "
            "actually wants the answer to. There is no anger and no disappointment "
            "anywhere in it. Peter's soaked shoulder is just in frame in front of him. "
            "Black water and white foam behind."
        ),
    },
    # ------------------------------------- n8 — where the question was asked ----
    {
        "id": "v2-r007-b27", "out": "s27-not-from-the-shore.jpeg", "seg": "n8 p1-p6",
        "window": "142.34-153.67", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": ("Why did you doubt? Hear how he asked it. Not from the shore. "
                      "Not after pulling him into the boat. From the hand already "
                      "holding him. It isn't a scolding."),
        "must_show": "a very wide view proving WHERE this is happening: the two men still out in the middle of the black sea, hands still joined, with the boat and the far shore both a long way off.",
        "must_not_show": "they must NOT be at the boat or anywhere near land — the distance from both is the entire argument of this beat; no dawn colour in the sky.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "A very wide view, the camera far back and a little above the sea. The two "
            "men stand together far out in the middle of an enormous black running "
            "sea, small against it, their hands still joined — and both the fishing "
            "boat with its one orange lamp and the black line of the far shore are a "
            "very long way off in the distance behind them. Torn cloud and cold stars "
            "fill the sky. White crests run in every direction across the water "
            "between them and everything else. Every figure has two arms, two hands "
            "and one head."
        ),
    },
    {
        "id": "v2-r007-b28", "out": "s28-you-were-doing-it.jpeg", "seg": "n8 p7-p8",
        "window": "153.67-162.50", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "SEA-NIGHT"],
        "narration": ("It's a real question, from someone who had already caught him — "
                      "as if to say: you were doing it. What made you stop trusting me?"),
        "must_show": "the two faces close together, both soaked — Jesus asking with kindness, Peter's face beginning to break with the answer he does not have.",
        "must_not_show": "no halo, glare or rim-light; nobody is angry and nobody is grovelling.",
        "scene": (
            "JESUS IS STANDING ON TOP OF THE WATER: his bare feet rest ON the "
            "unbroken surface taking his full weight, with clean rings of ripple "
            "spreading outward from each sole, and NO part of his feet, ankles, "
            "shins or robe hem is below the surface. He never sinks, never wades "
            "and is never submerged. "

            "Close on the two faces near together in the dark, both streaming with "
            "sea water. Jesus is looking directly into Peter's eyes with that same "
            "warm, unhurried, genuinely questioning expression, waiting. Peter's face "
            "is coming apart — his mouth working with no words in it, his eyes wet and "
            "fixed on Jesus, the shame and the wonder arriving at the same time. Their "
            "joined hands are just visible at the bottom of the frame. Black water and "
            "white foam behind them."
        ),
    },
    # ------------------------------------------ n9 / n9b — back and calm ----
    {
        "id": "v2-r007-b29", "out": "s29-back-to-the-boat-together.jpeg", "seg": "n9 p1",
        "window": "163.08-165.84", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": "The two of them came back to the boat across the water together.",
        "must_show": "SIDE VIEW, camera level with the sea: BOTH men walking LEFT TO RIGHT toward the boat, which sits on the RIGHT of the frame — Jesus's hand still on Peter's arm, all four feet on top of the water.",
        "must_not_show": "NEVER head-on — the direction of travel must be unmistakable, which is what V1 was rebuilt to fix. Nobody is in the water.",
        "scene": (
            "A SIDE VIEW with the camera down at sea level. THE TWO MEN ARE ON THE "
            "LEFT AND THE BOAT IS ON THE RIGHT, and both men are walking LEFT TO "
            "RIGHT across the open water toward it, in step, caught mid-stride. "
            "Jesus's hand is still on Peter's arm as they come. All four bare feet are "
            "ON TOP of the unbroken surface with ripple rings spreading behind them, "
            "and neither man is submerged at all. Ahead on the right the boat waits "
            "with its lamp and the pale faces of the men lining the gunwale. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b30", "out": "s30-they-climbed-in.jpeg", "seg": "n9 p2",
        "window": "165.84-169.11", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": "And the moment they climbed in, the wind stopped.",
        "must_show": "the two of them coming in over the gunwale with the disciples' hands gripping their arms to haul them aboard — everyone ending up INSIDE the hull.",
        "must_not_show": "no halo, glare or rim-light; the sea has NOT gone flat yet in this frame — v32 says the wind ceased once they were in.",
        "scene": (
            "At the side of the boat. Peter is coming in over the wet gunwale on his "
            "belly and one knee with two disciples' hands locked around his arms "
            "hauling him aboard, water pouring off him onto the deck timbers. Jesus is "
            "stepping in over the rail behind him with another man's hand out to "
            "steady him. Every other man is inside the hull, crowded to that side, the "
            "gunwale running behind them all. The last of the wind is still driving "
            "spray across the frame and the sea is still running. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b31", "out": "s31-not-slowly.jpeg", "seg": "n9b p1-p2",
        "window": "169.52-171.39", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": "Not slowly. Not eventually.",
        "must_show": "the instant of the change caught mid-air — the last wave collapsing in on itself, thrown spray still hanging above a sea that has already gone slack beneath it.",
        "must_not_show": "not calm yet and not stormy either — this frame is the exact hinge; do not put Jesus in it.",
        "scene": (
            "Close on the water just off the boat's side at the instant it changes. "
            "The last steep wave is collapsing in on itself with no wind left to hold "
            "it up, its white crest slumping and tearing apart, and a sheet of thrown "
            "spray still hangs in the air above a stretch of sea that has already gone "
            "slack and glassy underneath it. The dark planking of the hull is at the "
            "edge of the frame. Cold moonlight through a widening break in the cloud."
        ),
    },
    {
        "id": "v2-r007-b32", "out": "s32-flat-under-the-stars.jpeg", "seg": "n9b p3",
        "window": "171.39-176.30", "wide": True, "jesus": False, "ref": False,
        "locks": ["BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": ("The sea that had fought them all night simply lay down flat "
                      "under the stars."),
        "must_show": "DEAD FLAT WATER under a sky full of stars — the boat sitting motionless on black glass with the stars reflected whole underneath it.",
        "must_not_show": "NO sunrise, NO dawn band, NO warm colour on the horizon — the narration says UNDER THE STARS and this frame is the one most likely to drift; it is night.",
        "scene": (
            "A wide view across water that has gone absolutely flat and still, black "
            "and polished as glass from the boat right out to the far hills. The cloud "
            "has torn open overhead and the whole sky is full of cold hard stars, and "
            "every one of them is reflected unbroken in the surface below, so that the "
            "boat sits motionless in the middle of two skies. The little bow lamp "
            "throws one long unwavering line of orange down the water. There is not a "
            "ripple anywhere and no light at all on the horizon."
        ),
    },
    # ------------------------------------------------------ n10 — worship ----
    {
        "id": "v2-r007-b33", "out": "s33-soaked-and-shaking.jpeg", "seg": "n10 p1a",
        "window": "176.90-182.0", "wide": True, "jesus": False, "ref": False,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": ("And the men in that boat — the same men who minutes earlier had "
                      "screamed that he was a ghost —"),
        "must_show": "the crew in the sudden stillness — soaked through, shaking with cold and shock, staring at each other and at the flat water, the fight gone out of them.",
        "must_not_show": "they are not worshipping yet in this frame; do not put Jesus in it; everyone stays inside the hull.",
        "scene": (
            "Inside the boat in the sudden dead calm. The men are wrecked — soaked "
            "through, shoulders shaking with cold and shock, one gripping the gunwale "
            "and staring out at the flat black water as if he cannot make it be true, "
            "another with both hands over his mouth, another looking down at his own "
            "trembling hands. Peter kneels on the deck timbers in a spreading pool of "
            "sea water, his head down. Nobody is speaking. The bow lamp burns "
            "perfectly straight up now with no wind to bend it. Every figure has two "
            "arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b34", "out": "s34-they-worshipped-him.jpeg", "seg": "n10 p1b",
        "window": "182.0-187.30", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": ("knelt down where they sat, soaked and shaking, and worshipped him."),
        "must_show": "the whole crew down on their knees on the deck timbers where they were sitting, heads bowed toward Jesus standing among them in the boat.",
        "must_not_show": "no halo, glare or rim-light; Jesus is IN the boat with them and not apart at the frame edge; every gaze and bowed head is toward him.",
        "scene": (
            "Every man in the boat has gone down onto his knees on the wet deck "
            "timbers exactly where he was sitting — heads bowed, hands flat on the "
            "planking or pressed to their chests, water still running off all of them. "
            "Jesus stands in the middle of them in the hull, soaked like they are, one "
            "hand resting on the shoulder of the nearest kneeling man, looking around "
            "at them. Peter kneels closest with his forehead almost to the deck. The "
            "flat starlit water lies dead still beyond the gunwale on every side. The "
            "camera is back far enough to hold the whole boat and all the men. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b35", "out": "s35-thou-art-the-son-of-god.jpeg", "seg": "s33",
        "window": "187.89-190.12", "wide": False, "jesus": False, "ref": False,
        "locks": ["DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": "Of a truth thou art the Son of God. (Matthew 14:33)",
        "must_show": "close on one kneeling disciple's face saying it — lifted, wet, wrecked and certain.",
        "must_not_show": "do not put Jesus in this frame; no theatrical ecstasy — this is a plain man arriving at something he cannot get around.",
        "scene": (
            "Close on the face of one kneeling disciple in the boat, lit from the side "
            "by the steady bow lamp. His face is lifted and streaming wet, his hair "
            "plastered down, his eyes fixed and shining and his mouth open in the "
            "middle of saying it — a hard practical man arriving at something he "
            "cannot get around. Behind him the bowed shoulders of the other kneeling "
            "men and the flat starlit water are soft out of focus."
        ),
    },
    # ------------------------------------------- n10b — what is remembered ----
    {
        "id": "v2-r007-b36", "out": "s36-the-storm-taught-them.jpeg", "seg": "n10b p1-p2",
        "window": "191.66-196.34", "wide": True, "jesus": True, "ref": REF,
        "locks": ["PETER", "DISCIPLES", "BOAT", "SEA-NIGHT"],
        "narration": ("The storm had taught them who he was. And notice what the story "
                      "remembers about Peter."),
        "must_show": "a wide, quiet view of the whole boat from off the water — one small lit boat with kneeling men and Jesus standing in it, alone on a black mirror under the stars.",
        "must_not_show": "no halo, glare or rim-light; no dawn anywhere; the calm is total.",
        "scene": (
            "A wide view from out on the water a little way off the boat, low to the "
            "flat surface. The single fishing boat sits motionless on a black mirror "
            "of a sea, its one small lamp burning straight, the kneeling men gathered "
            "in the hull and Jesus standing quietly among them. The whole enormous sky "
            "of hard cold stars stands above it and is reflected under it. The far "
            "hills are a low black line. There is no other light anywhere. Every "
            "figure has two arms, two hands and one head."
        ),
    },
    {
        "id": "v2-r007-b37", "out": "s37-that-he-walked-and-was-caught.jpeg", "seg": "n10b p3-p5",
        "window": "196.34-201.83", "wide": False, "jesus": True, "ref": REF,
        "locks": ["PETER", "BOAT", "SEA-NIGHT", "DISCIPLES"],
        "narration": ("Not that he sank. That he walked. And that when he fell, he was "
                      "caught."),
        "must_show": "the closing frame: Peter kneeling soaked in the boat looking back out at the flat water he crossed, and Jesus's hand resting on his shoulder.",
        "must_not_show": "no halo, glare or rim-light; no shame on Peter's face — the story remembers the walk and the catch, and his face should carry both.",
        "scene": (
            "Close on Peter kneeling on the wet deck timbers, soaked through, his big "
            "hands loose on his knees, his head turned to look back out over the "
            "gunwale at the dead flat starlit water he walked across. His face is worn "
            "out and wide open — not ashamed, but astonished, as if he is only now "
            "understanding what happened to him. Jesus's hand rests on his shoulder "
            "from beside and just behind him, and Jesus's soaked sleeve and the edge "
            "of his jaw are in frame above. The mirror-still sea and the stars lie "
            "beyond the rail. Each hand has five fingers."
        ),
    },
]
