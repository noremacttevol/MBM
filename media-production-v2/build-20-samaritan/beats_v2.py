#!/usr/bin/env python3
"""V2 beat map — row 20, build-20-samaritan (Luke 10:25-37), realistic rebuild.

COVERAGE: 42 pictures against V1's EIGHT, over 179.76 s = 4.3 s/picture. V1 held a
single still on screen for as long as 22 s at a stretch; this map gives the parable a
frame per micro-beat.

⚠️ WINDOWS WERE RE-TIMED FROM SCRATCH 2026-08-02 (Claude worker 14). The inherited
30-beat map ran to **172.63 s** against the real **180.035 s** card start, and every
window in it was adrift from the first beat onward (its b01 ended at 4.46 s against
the real 4.997 s, and the error grew all the way down). Its last beat also held ONE
picture over 21.6 s of narration. Every window below was recomputed from the fixed
`extract_beats.py` reading the V1 build, then split on each segment's own phrase
boundaries in `audio/*.timing.json`. Contiguous 0.28 s → 180.035 s, zero gaps, zero
overlaps.

⚠️ THE NARRATION SCRIPT IN THE V1 FOLDER IS STALE — THE AUDIO IS NOT.
`media-production/build-20-samaritan/make_narration.py` was rewritten
programmatically AFTER the voices were cut (its string quoting changed from " to '
throughout) and the rewrite STRIPPED the plain-English retellings out of four
segments. The mp3s that ship in the approved V1 mp4 still contain them. Verified with
faster-whisper on the real audio files:

    n1b  actually opens  "Teacher, what must I do to inherit eternal life?"
    n12  actually opens  "And whatever more it costs, when I come back, I will
                          repay you myself."
    n14  is actually     "The scholar could not even say the word Samaritan. He
                          answered, the one who showed mercy. Jesus had flipped the
                          whole question, not who counts as my neighbor, but which
                          of them acted like one."
    n15  is actually     "Stop asking who you are allowed to walk past. Go and be
                          the neighbor. That is how good he is. He will not even let
                          you keep score."

`make_narration.py.pre-echo` in the V1 folder is the version that MATCHES the audio.
Because `v2_assemble.py` draws its captions from the script text, using the stale
text would have printed words nobody says over four segments and thrown their caption
timing off as well. TEXT_OVERRIDES below carries the true spoken text; V1 itself is
never edited (V2-KICKOFF hard protection #1).

⚠️ TIME OF DAY IS THE STORY'S OWN CLOCK:
  b01-b10, b21, b23,   the FRAME story — Jesus teaching in the open, warm
  b34-b41              mid-afternoon sun low in the west, long soft shadows. One
                       continuous afternoon; it never changes.
  b11-b26              the PARABLE on the Jericho road — hard high sun, white glare
                       off bare limestone, short black shadows, heat haze.
  b27                  late afternoon on the road, long shadows, the light going
                       amber as they walk toward the inn.
  b28                  NIGHT inside the inn, lit only by a clay oil lamp.
  b29-b33              early MORNING at the inn, thin level light from the east.
  b42                  the empty road again in the last warm light of the day.
No sunset palette anywhere: the story's evening is a walk, not a sky.

SCRIPTURE FACTS (Luke 10:25-37 KJV):
  v25  "a certain lawyer STOOD UP, and tempted him" — a scholar of the law, not a
       courtroom lawyer, and he STANDS to ask. b01 puts him on his feet.
  v29  "But he, willing to JUSTIFY himself" — the second question is self-defence
       dressed as humility. b06 is that face.
  v30  "went DOWN from Jerusalem to Jericho." The road descends about 3,300 feet in
       seventeen miles through bare limestone gorge. Every travel frame in the
       parable moves DOWNHILL and away from the high ground behind.
  v30  "stripped him of his raiment, and wounded him, and departed, leaving him half
       dead." CONTENT-CARE: he keeps a torn working undertunic, the wounds are dust
       and dried blood, and the violence itself is never shown.
  v31  "there came down a certain priest ... he passed by on the other side." The
       priest is going DOWN too — his temple course finished — so he is not hurrying
       toward duty. Both he and the Levite pass on the FAR side, and the frames keep
       the road's whole width between them and the man so the crossing is visible.
  v33  "a certain SAMARITAN ... when he saw him, he had COMPASSION on him." That
       word carries the story. b24 is the frame the whole video stands on and it
       must read as a man wrenched, not a man being polite.
  v34  "bound up his wounds, pouring in OIL AND WINE, and set him on HIS OWN BEAST."
       Both are stated, so both are shown: b26 the clay oil flask and the wineskin,
       b27 the Samaritan ON FOOT beside a loaded donkey.
  v35  "he took out TWO PENCE" — two denarii, about two days' wages. Exactly two
       countable silver coins, never a handful.
  v37  "He that shewed mercy on him." He cannot say the word Samaritan. b36/b37.
  v37  "Go, and do thou likewise." The story ends in motion.

CONTENT-CARE: AMBER, handled. The robbery (b13-b14) is shown as before and after —
men coming down off the rocks, then the aftermath in the dust. No blow lands on
camera, no blade touches a body, no blood pools, nothing is exposed: the stripped man
is in a torn knee-length working undertunic throughout. The Samaritan's care is shown
as hands, cloth and a poured flask.

CAST NOTE — ANCHOR-FIRST. Six beats are generated FIRST as face-showing anchors
(b02 lawyer, b11 traveller, b15 priest, b16 Levite, b24 Samaritan, b29 innkeeper);
each accepted anchor is then wired into REFS so every later frame naming that lock
gets the image attached. Row 19 paid for the lesson that a text lock does not hold a
character who is small in frame, so every beat naming a recurring person ALSO
restates his age, hair and garment colour in its own scene text.
"""

LOCKS = {
    # ------------------------------------------------------------ people ----
    "LAWYER": (
        "SCHOLAR-OF-THE-LAW LOCK: one man about forty-five, a teacher of the Jewish "
        "law — well fed and well kept next to the working people around him, of "
        "medium height, with a neatly combed and squared-off dark brown beard shot "
        "through with grey at the chin, receding dark hair under a soft folded "
        "head-cloth, and quick intelligent deep-set brown eyes. He wears a long "
        "DEEP INDIGO-BLUE fine wool robe, closely woven and clean, with a broad "
        "mantle of the same indigo bearing two narrow woven bands of dark madder "
        "red near the hem, knotted tassels at its four corners, and good leather "
        "sandals. HE IS NEVER IN CREAM, OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH. "
        "He is the same man, same face, same beard and same indigo robe in every "
        "frame he appears in, near or far, sharp or blurred, and he is never aged, "
        "greyed further, thinned or replaced by another man."
    ),
    "TRAVELLER": (
        "BEATEN-TRAVELLER LOCK: one Judean man about thirty — lean, wiry and "
        "work-hardened, with straight dark brown hair cut at the jaw, a short "
        "untrimmed dark beard, a narrow face and a long straight nose. Before the "
        "robbery he wears a plain undyed DUST-BROWN wool tunic to the knee with a "
        "twisted rope belt, a coarse brown travelling mantle over one shoulder and a "
        "small flax satchel. Afterwards he is in the SAME torn dust-brown "
        "knee-length undertunic and nothing else, the cloth ripped at the shoulder "
        "and grey with road dust, with dried blood matted in the hair at his temple "
        "and dust caked on his face and forearms. HE IS NEVER IN CREAM, OFF-WHITE OR "
        "ANY NEAR-WHITE CLOTH, and no part of his body below that knee-length tunic "
        "is uncovered or exposed. Same man, same face and same hair in every frame."
    ),
    "ROBBERS": (
        "ROBBERS LOCK: exactly THREE lean hard men of the gorge and no fourth — "
        "ragged, sun-blackened, barefoot or in worn leather sandals, in filthy "
        "patched wool tunics of dark umber, faded rust and soot grey with cloth "
        "wound around their heads and across their lower faces. Their gear is "
        "hand-forged and hand-made: a short iron blade, a wooden staff, a length of "
        "twisted flax cord. NONE OF THEM WEARS CREAM, OFF-WHITE OR ANY NEAR-WHITE "
        "CLOTH. They are shown as figures in motion at a distance, never in "
        "close-up, and no weapon is ever shown touching a body."
    ),
    "PRIEST": (
        "PRIEST LOCK: one temple priest about fifty-five returning from his course "
        "of service — tall and upright, well fed, with a full square silver-grey "
        "beard, grey hair under a wound pale head-cloth, and a smooth unweathered "
        "face. He wears a long fine DOVE-GREY linen robe with a wide woven border of "
        "deep blue at the hem and cuffs, a folded grey-blue mantle over his left "
        "shoulder, and clean leather sandals; a small pack rides on a strap at his "
        "hip. HIS ROBE IS CLEARLY GREY AND BLUE AND IS NEVER CREAM, OFF-WHITE, IVORY "
        "OR WHITE. Same man, same silver beard, same grey-and-blue robe in every "
        "frame."
    ),
    "LEVITE": (
        "LEVITE LOCK: one temple assistant about thirty-five — shorter and slighter "
        "than the priest, clean-shaven at the cheeks with a close-trimmed black beard "
        "along the jaw, black hair cropped short, an anxious tight-mouthed face. He "
        "wears a plain DARK OLIVE-GREEN wool tunic to the ankle with a rust-brown "
        "sash and a rust-brown mantle bunched in both hands, and worn leather "
        "sandals. HE IS NEVER IN CREAM, OFF-WHITE OR ANY NEAR-WHITE CLOTH. He is "
        "visibly a different, younger, smaller man than the priest and is never "
        "given the priest's face, beard or colouring. Same man in every frame."
    ),
    "SAMARITAN": (
        "SAMARITAN LOCK: one Samaritan trader about thirty-five, and he must be "
        "instantly tellable from every other man in this story — broad-shouldered "
        "and solid, sun-darkened to a deep weathered brown, with a short dense BLACK "
        "beard, black hair, heavy black brows and a broad blunt nose. He wears a "
        "distinctive travelling mantle woven in BROAD RUST-RED AND DARK OCHRE "
        "STRIPES over a plain dark brown tunic, a brown-and-black head-cloth bound "
        "with a twisted dark cord, a wide leather belt with a small leather purse "
        "hanging from it, and heavy dusty travelling sandals. HE IS NEVER IN CREAM, "
        "OFF-WHITE OR ANY NEAR-WHITE CLOTH. He is a man in his MID-THIRTIES in every "
        "frame, near, far, sharp or blurred — never grey-haired, never white-bearded, "
        "never balding, never old, never thin, never a different man from the "
        "attached reference photograph, and never given the priest's or the Levite's "
        "face."
    ),
    "INNKEEPER": (
        "INNKEEPER LOCK: one heavy-set man about fifty who keeps the roadside inn — "
        "thick through the chest and belly, balding on top with grey-streaked dark "
        "hair at the sides, a broad grizzled beard, and a shrewd unhurried face. He "
        "wears a dusty DARK BROWN wool tunic to mid-calf with the sleeves pushed "
        "back, a scuffed leather apron tied at the waist and a cloth over one "
        "shoulder. HE IS NEVER IN CREAM, OFF-WHITE OR ANY NEAR-WHITE CLOTH. Same "
        "man in every frame."
    ),
    "DONKEY": (
        "DONKEY LOCK: one small grey-brown Syrian pack donkey with a dark dorsal "
        "stripe, a pale muzzle and pale rings around the eyes, a shaggy coat and "
        "long ears. Its whole harness is hand-made: a folded woollen blanket and a "
        "wooden pack-saddle held by woven hair girths, hand-twisted flax rope reins "
        "knotted to a plain rope halter, and two woven baskets and a stoppered "
        "goatskin waterskin slung across its back. There is no metal bit, buckle, "
        "stirrup, ring or stitched leather bridle on it anywhere."
    ),
    "CROWD": (
        "LISTENING-CROWD LOCK: ordinary working Galilean and Judean people sitting "
        "and standing on the ground to listen — men, women and a few children, "
        "twenty-five to sixty years old, sunburnt, in rough-woven wool and linen "
        "tunics and head-cloths in SATURATED EARTH COLOURS: rust brown, deep russet, "
        "dark olive, umber, blue-grey, dusty indigo, madder red. NOT ONE OF THEM "
        "WEARS CREAM, OFF-WHITE, IVORY OR ANY NEAR-WHITE CLOTH anywhere on the body, "
        "in focus or out of focus, at the centre of the frame or at its edges. Each "
        "face is a different face and no face is cloned from another."
    ),
    # ---------------------------------------------------------- settings ----
    "TEACHING-PLACE": (
        "TEACHING-PLACE LOCK: open ground on the edge of a Judean village in the "
        "late afternoon — dry pale packed earth and outcrops of weathered limestone "
        "worn smooth enough to sit on, a few old olive trees with silver-grey leaves "
        "and split trunks, a low drystone field wall of unmortared limestone, and "
        "brown terraced hillsides going back into a warm hazy distance. The light is "
        "LOW, WARM AND FROM THE WEST, raking across the ground and throwing long "
        "soft shadows toward the camera. Every built thing in view is drystone, "
        "mud-brick or hewn timber; there is no road surface, no step of dressed "
        "masonry, no gate, no signpost, no tiled or domed roof, no tower and no town "
        "skyline of any kind on the horizon."
    ),
    "JERICHO-ROAD": (
        "JERICHO-ROAD LOCK: the road that goes DOWN from Jerusalem to Jericho — a "
        "bare rock-strewn track of pale dust and loose limestone rubble, barely two "
        "men wide, cut along the flank of a deep dry gorge in the Judean wilderness. "
        "On one side the ground drops away into a chalk-white ravine; on the other "
        "it climbs in broken cliffs and slabs full of black shadowed clefts. The "
        "country is bare desert rock and dust — chalk white, bone grey, pale ochre "
        "and rust — with only scattered dead thorn scrub and a few tufts of burnt "
        "yellow grass. Nothing grows tall, and there is no water, no green field, no "
        "tree, no wall, no building, no milestone, no signpost, no paving, no kerb "
        "and no wheel rut anywhere on it. THE ROAD ALWAYS DESCENDS: whenever a "
        "traveller moves along it he is walking DOWNHILL, away from the high ground "
        "behind him."
    ),
    "INN": (
        "ROADSIDE-INN LOCK: a small first-century khan on the Jericho road — a "
        "single-storey block of rough undressed limestone and mud plaster the colour "
        "of the hillside, with a low dark doorway closed by a plank door of hewn "
        "timber turning on wooden pins, small square unglazed window holes with no "
        "frame and no shutter hardware, and a flat roof of poles, brushwood and "
        "packed mud. Inside, the walls are bare mud plaster, the floor is beaten "
        "earth strewn with straw, and the sleeping place is a low mud-brick bench "
        "along one wall with a straw pallet and coarse brown blankets on it. Wooden "
        "pegs in the wall, hanging goatskins, stacked clay jars, a woven reed mat "
        "and a hand-hewn low table are the whole furnishing. EVERY LIGHT INSIDE IS "
        "THE BARE WICK OF A SHALLOW CLAY SAUCER OIL LAMP standing on the bench, the "
        "table or a niche cut in the wall, or daylight coming through the doorway "
        "and the window holes; there is no glass of any kind, no lantern, no "
        "chimney, no candle, no candlestick, no hanging fixture, no hearth, no "
        "fireplace, no mantel, no metal bracket, no hinge, no lock, no sign board "
        "and no writing anywhere on the building."
    ),
}

OUTPUT_VIDEO_NAME = "luke-10_good-samaritan-realistic-v2.mp4"

# The V1 narration script was rewritten AFTER the voices were cut and lost the
# plain-English retellings the shipped audio actually contains (see the module
# docstring — verified with faster-whisper against the real mp3s). v2_assemble draws
# caption text from the script, so these four segments are corrected here to the
# words that are genuinely spoken. Nothing in the V1 folder is modified.
TEXT_OVERRIDES = {
    "n1b": ("Teacher, what must I do to inherit eternal life? Jesus turned it "
            "straight back on him — what does the law say? And the man answered it "
            "well: love God with everything you are, and love your neighbor as "
            "yourself. Then he asked one more question. It sounds humble. It was "
            "not."),
    "n12": ("And whatever more it costs, when I come back, I will repay you myself. "
            "He did not just help and move on. He tied his own name to a stranger's "
            "recovery."),
    "n14": ("The scholar could not even say the word Samaritan. He answered, the one "
            "who showed mercy. Jesus had flipped the whole question. Not who counts "
            "as my neighbor, but which of them acted like one."),
    "n15": ("Stop asking who you are allowed to walk past. Go, and be the neighbor. "
            "That is how good he is. He will not even let you keep score."),
}

# Wired in after the anchor pass (b02, b11, b15, b16, b24, b29) is generated and
# inspected. Every later beat naming one of these locks gets the image attached.
REFS = {
    "LAWYER": "assets/s02-what-shall-i-do.jpeg",
    "TRAVELLER": "assets/s11-the-road-down.jpeg",
    "PRIEST": "assets/s15-the-priest-crossed-over.jpeg",
    "LEVITE": "assets/s16-the-levite-also.jpeg",
    "SAMARITAN": "assets/s24-moved-with-compassion.jpeg",
    "INNKEEPER": "assets/s29-two-silver-coins.jpeg",
}

REF = True

BEATS = [
    # =============================================== FRAME STORY — afternoon ====
    {
        "id": "v2-r020-b01", "out": "s01-a-scholar-stood-up.jpeg", "seg": "n1",
        "window": "0.28-4.997", "wide": True, "jesus": True, "ref": True,
        "locks": ["LAWYER", "CROWD", "TEACHING-PLACE"],
        "narration": "A scholar of the law stood up to test Jesus, and asked him a question.",
        "must_show": "the scholar in indigo ON HIS FEET among a seated crowd, addressing Jesus who sits teaching on a low limestone outcrop; every listener's attention swinging to the man who has stood up.",
        "must_not_show": "no synagogue interior, no scroll being read, no temple, no cream or off-white cloth on anybody except Jesus, and nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens, late afternoon, fine film grain. THE CAMERA "
            "STANDS BEHIND AND JUST ABOVE THE SEATED CROWD AND SHOOTS PAST THEIR "
            "BACKS toward Jesus: the near third of the frame is the backs of seated "
            "heads and shoulders, out of focus, and NOT ONE FACE IS TURNED TOWARD THE "
            "LENS. Jesus sits at the far side on a low weathered limestone outcrop, "
            "small in frame but sharp, his hands loose on his knees, his face lifted "
            "and open toward the man who has interrupted him. Between the camera and "
            "Jesus, in the middle distance and seen in three-quarter from behind, the "
            "scholar of the law has risen to his feet out of the seated crowd — a "
            "well-kept man of forty-five with a squared grey-shot dark beard and a "
            "deep indigo-blue robe and mantle, one hand lifted from the wrist in the "
            "gesture of putting a question. Every other person in the picture is "
            "sitting on the ground. Low warm sun rakes in from the right and throws "
            "long shadows across the pale dust toward the camera."
        ),
    },
    {
        "id": "v2-r020-b02", "out": "s02-what-shall-i-do.jpeg", "seg": "s25",
        "window": "4.997-9.300", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": "Master, what shall I do to inherit eternal life?",
        "must_show": "a clear, sharply readable close study of the scholar's FACE mid-question — this frame is the identity anchor for him and his features must be plainly legible.",
        "must_not_show": "Jesus is not in this frame. No crowd faces in focus, no cream or off-white cloth anywhere, no pupils on the lens.",
        "scene": (
            "One photograph, 85mm prime lens at f/2, shallow depth of field, late "
            "afternoon, fine grain. Tight on the scholar of the law from the chest "
            "up, turned three quarters to his own right so his face is fully lit and "
            "fully readable — a well-fed man of forty-five, squared dark brown beard "
            "greying at the chin, receding dark hair under a soft folded head-cloth, "
            "deep indigo-blue fine wool robe and mantle. He is mid-sentence, lips "
            "parted on the question, chin slightly raised, eyebrows up in the "
            "practised courteous expression of a man who already believes he knows "
            "the answer. His eyes are fixed on someone seated lower and further away "
            "to his right, so his gaze travels down and out through the RIGHT edge of "
            "the frame, well off the camera axis, and his pupils are nowhere near the "
            "lens. Warm low sun from his right models the cheekbone and the beard; "
            "behind him the crowd and the olive branches are a soft unreadable wash "
            "of brown and dust. He has one head and two complete hands."
        ),
    },
    {
        "id": "v2-r020-b03", "out": "s03-teacher-what-must-i-do.jpeg", "seg": "n1b p1",
        "window": "9.300-13.170", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEACHING-PLACE"],
        "narration": "Teacher, what must I do to inherit eternal life?",
        "must_show": "Jesus listening — patient, unhurried, entirely attentive to a question he can hear the motive inside.",
        "must_not_show": "no halo, glow or rim-light; he is not speaking, not teaching with a raised hand, not looking at the camera; nobody else's face is in focus.",
        "scene": (
            "One photograph, 105mm lens wide open, very shallow depth of field, late "
            "afternoon, fine grain. Close on Jesus seated on the limestone outcrop, "
            "from the chest up, turned a little to his own left. He is LISTENING: his "
            "head tilted slightly, his mouth closed and soft, his weight forward on "
            "one forearm across his knee, the whole of his attention given to "
            "somebody standing above him and to his left. His eyes are lifted and "
            "travel up and out through the LEFT edge of the frame, clearly past the "
            "camera, and his pupils are not on the lens. Warm low sun from the right "
            "crosses his cheek and the side of his beard and leaves the far side of "
            "his face in soft shadow; the light comes from the sky and nothing comes "
            "off him. An out-of-focus indigo shoulder is just visible at the extreme "
            "left edge, and the rest of the background is a soft wash of dust, olive "
            "leaves and warm hillside."
        ),
    },
    {
        "id": "v2-r020-b04", "out": "s04-what-does-the-law-say.jpeg", "seg": "n1b p2",
        "window": "13.170-17.130", "wide": False, "jesus": True, "ref": True,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": "Jesus turned it straight back on him — what does the law say?",
        "must_show": "Jesus handing the question back — an open upturned palm offered toward the scholar, the smallest knowing warmth at the corner of his mouth.",
        "must_not_show": "no rebuke, no pointing finger, no anger, no crowd in focus, no cream cloth on the scholar, and no glow or rim-light on Jesus.",
        "scene": (
            "One photograph, 50mm lens at f/2, late afternoon, fine grain. An "
            "OVER-THE-SHOULDER two-shot taken from just behind and beside the "
            "standing scholar: his indigo-blue shoulder, the back of his head-cloth "
            "and the edge of his greying dark beard fill the near left of the frame, "
            "large and out of focus, and his back is to the camera. Beyond him, sharp "
            "and seated lower, Jesus has turned the question back — his right hand "
            "come up off his knee with the palm open and upturned toward the scholar, "
            "his eyebrows lifted, the smallest amount of warmth at the corner of his "
            "mouth. HIS EYES ARE LOCKED ON THE SCHOLAR'S FACE INSIDE THE FRAME, on "
            "that out-of-focus shoulder to the left, so his gaze has a target in the "
            "picture and never reaches the lens. Low warm sun from the right; his "
            "cream robe takes the light and gives none back."
        ),
    },
    {
        "id": "v2-r020-b05", "out": "s05-he-answered-it-well.jpeg", "seg": "n1b p3",
        "window": "17.130-23.550", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "CROWD", "TEACHING-PLACE"],
        "narration": ("And the man answered it well: love God with everything you "
                      "are, and love your neighbor as yourself."),
        "must_show": "the scholar reciting the law he knows by heart — one hand flat on his own chest, chin up, fluent and completely sure of himself.",
        "must_not_show": "Jesus is not in this frame. No scroll, no book, no writing of any kind, no cream or off-white cloth on anyone, no pupils on the lens.",
        "scene": (
            "One photograph, 70mm lens at f/2.2, late afternoon, fine grain. The "
            "scholar of the law standing, framed from the waist up and turned three "
            "quarters to his own left — forty-five, squared grey-shot dark beard, "
            "folded head-cloth, deep indigo-blue robe and mantle with its two narrow "
            "madder-red bands. He is reciting: his left palm laid flat on his own "
            "chest, his right hand turned out at his side as though laying the answer "
            "down where everyone can see it, his chin lifted, his eyes half closed "
            "with the ease of a man saying words he has known since boyhood. His gaze "
            "goes down and away through the LOWER LEFT of the frame toward someone "
            "seated. Behind him, thrown well out of focus, three or four seated "
            "listeners in rust brown and dark olive; no face behind him is readable "
            "and none is turned toward the camera. Warm low sun from the right edges "
            "his beard and the folds of the indigo wool."
        ),
    },
    {
        "id": "v2-r020-b06", "out": "s06-it-was-not-humble.jpeg", "seg": "n1b p4-p6",
        "window": "23.550-29.571", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": "Then he asked one more question. It sounds humble. It was not.",
        "must_show": "the scholar's face in the half-second before the second question — the recitation gone, replaced by something calculating and self-protecting.",
        "must_not_show": "no sneer, no villain's grin, no comedy; he is defending himself, not plotting. Jesus is not in this frame. No cream cloth, no pupils on the lens.",
        "scene": (
            "One photograph, 105mm lens wide open, very shallow depth of field, late "
            "afternoon, heavy bokeh, fine grain. Very close on the scholar's face "
            "alone, three quarters to his own right, from the brow to the collar of "
            "the indigo robe. The fluency has drained out of it. His mouth has closed "
            "to a thin line, one eyebrow is fractionally lower than the other, and "
            "his eyes have narrowed and gone sideways and downward — the look of a "
            "man who has just heard his own answer come back at him and is measuring "
            "how much it is going to cost him. His gaze exits through the LOWER RIGHT "
            "corner of the frame, far off the camera axis. Warm low sun from the "
            "right catches the ridge of his nose and the grey in his beard and leaves "
            "the eye socket on the far side in shadow. The background is an "
            "unreadable wash of dust and warm hillside."
        ),
    },
    {
        "id": "v2-r020-b07", "out": "s07-and-who-is-my-neighbour.jpeg", "seg": "s29",
        "window": "29.571-32.386", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "CROWD", "TEACHING-PLACE"],
        "narration": "And who is my neighbour?",
        "must_show": "the scholar asking the second question out loud — one hand opened outward in a reasonable, almost innocent gesture, his chin lifted, the whole crowd hearing it.",
        "must_not_show": "Jesus is not in this frame. No aggression, no finger jabbed, no cream cloth on anyone, no face turned to the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.5, late afternoon, fine grain. THE "
            "CAMERA IS LOW AND OFF TO THE SCHOLAR'S LEFT, down among the seated "
            "listeners, shooting slightly upward past the out-of-focus shoulder and "
            "head-cloth of one seated man in dark olive whose BACK is to us in the "
            "near right of the frame. The scholar stands beyond him in three-quarter "
            "view, from the thigh up, mid-question: his right hand opened outward and "
            "turned palm-up in a reasonable, almost innocent gesture, his left hand "
            "gathering the indigo mantle at his waist, his chin raised. His eyes are "
            "fixed low and to his own right on the seated figure he is asking, so his "
            "eyeline crosses the frame and exits its LOWER RIGHT edge and never "
            "touches the lens. Low warm sun behind and to the right of him rakes "
            "across the dust. The only garment colours in the picture are indigo "
            "blue, dark olive and rust brown."
        ),
    },
    {
        "id": "v2-r020-b08", "out": "s08-hoping-for-limits.jpeg", "seg": "n2 p1",
        "window": "32.386-36.056", "wide": True, "jesus": False, "ref": False,
        "locks": ["CROWD", "TEACHING-PLACE"],
        "narration": ("It was the kind of question you ask when you are hoping the "
                      "answer has limits."),
        "must_show": "the seated crowd in the beat of silence after the question — ordinary faces waiting, some glancing at each other, nobody sure yet what is coming.",
        "must_not_show": "Jesus is not in this frame and neither is the scholar's face. No cream or off-white cloth on anybody. No posed line of people facing the camera.",
        "scene": (
            "One photograph, 35mm lens at f/4, late afternoon, fine grain. THE CAMERA "
            "SITS DOWN ON THE GROUND AMONG THE LISTENERS AND SHOOTS ALONG THE ROW "
            "FROM THE SIDE, so the near people are seen in profile and from behind — "
            "the back of one DARK UMBER head-cloth and one russet shoulder fill the "
            "near left, out of focus, and NOT ONE FACE IS TURNED TOWARD THE LENS. "
            "EVERY HEAD-CLOTH, SHAWL, TUNIC AND MANTLE IN THIS PICTURE — including "
            "the large out-of-focus ones in the near foreground and the ones cut off "
            "by the bottom and side edges — IS A SATURATED DARK EARTH COLOUR: umber, "
            "rust brown, deep russet, dark olive, blue-grey or dusty indigo. NOT ONE "
            "PIECE OF CLOTH ANYWHERE IN THE FRAME IS CREAM, IVORY, OFF-WHITE, PALE "
            "SAND OR ANY NEAR-WHITE COLOUR. Beyond them "
            "eight or nine ordinary working people sit on the dry pale earth and the "
            "low limestone in rust brown, dark olive, umber and dusty indigo: a "
            "grey-bearded man with his forearms across his knees, a woman with a "
            "child leaning on her, two younger men with their heads turned toward "
            "each other in the middle of a glance. Every one of them is looking "
            "across the frame to the right, toward something outside the picture, and "
            "the whole row is caught in the suspended half-second after a question. "
            "Low warm sun from the right throws their long shadows toward the camera."
        ),
    },
    {
        "id": "v2-r020-b09", "out": "s09-who-he-could-ignore.jpeg", "seg": "n2 p2",
        "window": "36.056-41.771", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": ("He wanted a line drawn, so he could know exactly who he was "
                      "allowed to ignore."),
        "must_show": "the scholar's hand — the edge of it held out level and still, the unconscious gesture of a man drawing a boundary in the air.",
        "must_not_show": "no line actually drawn in the dust, no writing, no diagram, no map. Jesus is not in this frame. No cream cloth, no face on the lens.",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, very shallow depth of field, "
            "late afternoon, fine grain. Tight and low on the scholar's right hand "
            "and forearm, held out at waist height with the fingers straight and "
            "pressed together and the little-finger edge downward — the flat, level, "
            "unconscious chopping gesture of a man setting a boundary in the air. The "
            "hand is clean, soft and well kept, with a heavy indigo cuff falling back "
            "from the wrist. It is sharp; his indigo robe, the dark shape of his "
            "beard above and the warm dust of the ground below are all thrown far out "
            "of focus, and NO FACE IS READABLE ANYWHERE IN THE PICTURE. Low warm sun "
            "from the right rims the knuckles and casts the hand's own long shadow "
            "across the pale ground beneath it. It is one complete natural hand with "
            "five fingers."
        ),
    },
    {
        "id": "v2-r020-b10", "out": "s10-he-answered-with-a-story.jpeg", "seg": "n3 p1",
        "window": "41.771-43.151", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEACHING-PLACE"],
        "narration": "Jesus answered with a story.",
        "must_show": "Jesus beginning to speak — the moment a storyteller starts, settled and warm, drawing everyone in.",
        "must_not_show": "no halo, glow or rim-light; no dramatic raised arm, no preaching pose, no pupils on the lens, nobody else in focus.",
        "scene": (
            "One photograph, 85mm lens at f/2, late afternoon, fine grain. Close on "
            "Jesus seated on the limestone, from the shoulders up, turned slightly to "
            "his own right. He has just begun to speak: his lips are parted on a "
            "first word, his eyebrows are relaxed, and there is unmistakable warmth "
            "coming up in his face — the settled ease of a man opening a story rather "
            "than winning an argument. One hand has lifted a little way off his knee "
            "into the lower edge of the frame, open and turned slightly upward. His "
            "eyes are on the people out to his right and low down, so his gaze leaves "
            "the picture through its RIGHT edge, clearly past the camera. Warm low "
            "sun from the right; his cream robe receives the light and emits none, "
            "and there is no light of any kind around his head. The hillside behind "
            "him is a soft warm blur."
        ),
    },
    # ================================================= THE PARABLE — the road ====
    {
        "id": "v2-r020-b11", "out": "s11-the-road-down.jpeg", "seg": "n3 p2a",
        "window": "43.151-47.000", "wide": False, "jesus": False, "ref": False,
        "locks": ["TRAVELLER", "JERICHO-ROAD"],
        "narration": "A man was traveling the steep, lonely road down to Jericho,",
        "must_show": "a clear, sharply readable study of the traveller's FACE and upper body as he walks the descending road alone — this frame is the identity anchor for him.",
        "must_not_show": "no robbers yet, no wounds, no blood, no other traveller, no cream or off-white cloth, no pupils on the lens, no green fields or trees.",
        "scene": (
            "One photograph, 85mm prime lens at f/2.5, hard high sun, heat haze, fine "
            "grain. A medium shot of the traveller from the thighs up as he walks "
            "DOWNHILL along the bare rubble track, turned three quarters toward the "
            "camera so his face is fully lit and completely readable — a lean wiry "
            "Judean man of about thirty, straight dark brown hair cut at the jaw, a "
            "short untrimmed dark beard, a narrow face and a long straight nose, in a "
            "plain undyed dust-brown knee-length wool tunic with a twisted rope belt, "
            "a coarse brown mantle over one shoulder and a small flax satchel on a "
            "cord. He is the ONLY PERSON IN THE PICTURE. His eyes are up and out to "
            "his own left, reading the broken cliffs above the road, so his gaze "
            "leaves the frame through its UPPER LEFT corner well off the camera axis. "
            "White glare comes almost straight down and puts a short black shadow "
            "under his jaw and at his feet; behind him the pale rubble track climbs "
            "away into chalk-white rock and black shadowed clefts, thrown soft by the "
            "long lens."
        ),
    },
    {
        "id": "v2-r020-b12", "out": "s12-the-way-of-blood.jpeg", "seg": "n3 p2b",
        "window": "47.000-51.862", "wide": True, "jesus": False, "ref": False,
        "locks": ["TRAVELLER", "JERICHO-ROAD"],
        "narration": "a road so full of robbers that people called it the Way of Blood.",
        "must_show": "the scale and menace of the gorge — one small lone figure far down the track, dwarfed by chalk cliffs full of black clefts a man could be hiding in.",
        "must_not_show": "no robbers visible yet, no bodies, no bones, no skulls, no vultures, no blood, no buildings, no green anywhere. Jesus is not in this frame.",
        "scene": (
            "One photograph, 24mm lens at f/8, hard high sun, deep haze in the "
            "distance, fine grain. THE CAMERA STANDS HIGH ON THE TRACK BEHIND THE "
            "TRAVELLER AND SHOOTS DOWN THE ROAD PAST HIS BACK: he is small in the "
            "lower middle of the frame, seen from directly behind and walking AWAY "
            "from the camera and downhill, his brown mantle and satchel plain against "
            "the pale dust, and no face is turned toward the lens anywhere in the "
            "picture. The gorge opens out in front of and above him — chalk-white and "
            "bone-grey limestone cliffs stacked in broken slabs, riddled with black "
            "shadowed clefts and overhangs, the ravine dropping away on the left into "
            "white rubble, the track threading along the flank and dropping steadily "
            "toward a hazed pale distance. He is the only living thing in the whole "
            "frame and he is very small in it. Vertical white glare, short black "
            "shadows, dust hanging in the air."
        ),
    },
    {
        "id": "v2-r020-b13", "out": "s13-robbers-were-what-he-found.jpeg", "seg": "n4 p1",
        "window": "51.862-53.642", "wide": True, "jesus": False, "ref": False,
        "locks": ["TRAVELLER", "ROBBERS", "JERICHO-ROAD"],
        "narration": "Robbers were exactly what he found.",
        "must_show": "exactly three ragged men coming fast down off the rocks above the track while the traveller, below them, has only just begun to turn — the instant before, not the violence itself.",
        "must_not_show": "NO blow landing, no blade touching a body, no wound, no blood, no man on the ground yet, no fourth robber, no faces on the lens.",
        "scene": (
            "One photograph, 35mm lens at f/4, 1/60th so the moving men smear "
            "slightly, hard high sun, dust in the air, fine grain. THE CAMERA IS DOWN "
            "ON THE TRACK BEHIND AND BELOW THE TRAVELLER AND SHOOTS UP PAST HIS "
            "SHOULDER: his back and the back of his head fill the near right of the "
            "frame, out of focus, and he has only just begun to turn, so no part of "
            "his face reaches the lens. Beyond and above him EXACTLY THREE ragged men "
            "and no fourth are coming fast down a slope of broken white limestone "
            "toward the road — sun-blackened, in filthy patched umber, faded rust and "
            "soot-grey wool with cloth wound over their heads and lower faces, one "
            "with a wooden staff, one with a length of twisted flax cord, one "
            "half-sliding on the loose rubble with an arm out for balance. They are "
            "each clearly separated on the slope and individually countable. All "
            "three are seen from the side or in three-quarter, moving ACROSS the "
            "frame and downward, none advancing into the camera and no face turned "
            "toward it. Vertical white glare, short hard shadows, a haze of kicked "
            "dust."
        ),
    },
    {
        "id": "v2-r020-b14", "out": "s14-half-dead-in-the-dust.jpeg", "seg": "n4 p2",
        "window": "53.642-59.314", "wide": False, "jesus": False, "ref": False,
        "locks": ["TRAVELLER", "JERICHO-ROAD"],
        "narration": ("They stripped him, beat him, and left him half dead in the "
                      "dust beside the road."),
        "must_show": "the aftermath and only the aftermath — the traveller lying on his side in the dust at the edge of the track, torn undertunic, dust and dried blood in his hair, barely conscious, his satchel and mantle gone.",
        "must_not_show": "NO robbers, no weapons, no violence, no open wounds, no pooled or running blood, no exposed body — the torn knee-length undertunic stays on him and covers him. No pupils on the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.8, hard high sun, fine grain. THE "
            "CAMERA IS ON THE GROUND AT THE EDGE OF THE TRACK, almost at dust level, "
            "shooting along the road so a foreground of pale stones and grit runs out "
            "of focus across the bottom of the frame. The traveller lies on his side "
            "in the dust just off the track, curled with his knees drawn up and one "
            "arm folded under his head — the same lean man of about thirty with dark "
            "hair at the jaw and a short dark beard, now in only his torn dust-brown "
            "knee-length undertunic, ripped open at the shoulder and grey with road "
            "dust, the cloth still covering him from shoulder to below the knee. Dust "
            "is caked on his cheek and forearms and dried dark blood is matted in the "
            "hair at his temple. His eyes are barely open, unfocused, aimed at the "
            "stones a hand's width in front of his face and out through the BOTTOM "
            "LEFT of the frame; he is not looking at anything and certainly not at "
            "the camera. He is the only person in the picture. The white vertical "
            "glare gives him almost no shadow to lie in, and the empty pale track and "
            "chalk cliffs behind him are soft and blown out."
        ),
    },
    {
        "id": "v2-r020-b15", "out": "s15-the-priest-crossed-over.jpeg", "seg": "n5 p1",
        "window": "59.314-64.204", "wide": True, "jesus": False, "ref": False,
        "locks": ["PRIEST", "TRAVELLER", "JERICHO-ROAD"],
        "narration": ("A priest came down that same road, saw the man, and crossed to "
                      "the far side."),
        "must_show": "the priest already over on the FAR edge of the track with the full width of the road empty between him and the man in the dust — and his FACE clearly readable, since this frame is his identity anchor. He has seen; he is walking on.",
        "must_not_show": "no cream, off-white, ivory or white robe on the priest — his robe is dove grey with deep blue borders. No temple, no altar, no Jerusalem skyline, no pupils on the lens.",
        "scene": (
            "One photograph, 50mm lens at f/4, hard high sun, fine grain. THE CAMERA "
            "IS LOW BESIDE THE BEATEN MAN AND SHOOTS ACROSS THE ROAD PAST HIM: his "
            "shoulder and dust-caked dark hair fill the near lower left corner, large "
            "and out of focus and seen from behind, and no part of his face reaches "
            "the lens. The entire width of the pale rubble track lies empty between "
            "him and the far edge, and on that far edge, sharp and lit full in the "
            "vertical sun, the priest walks on downhill — a tall upright well-fed man "
            "of fifty-five with a full square silver-grey beard and grey hair under a "
            "wound pale head-cloth, in a long fine DOVE-GREY linen robe with a wide "
            "deep-blue woven border and a grey-blue mantle over his left shoulder. He "
            "is caught in three-quarter as he passes, his body already turned "
            "downhill and away, his head turned back and DOWN toward the figure in "
            "the dust so his face is clearly visible and clearly seeing — his eyeline "
            "running across the frame and out through its LOWER LEFT corner, far off "
            "the camera axis. His mouth is set and his gathered mantle is held clear "
            "of the ground in one hand. Two figures only in the whole picture. Short "
            "black shadows straight down, white glare, dust."
        ),
    },
    {
        "id": "v2-r020-b16", "out": "s16-the-levite-also.jpeg", "seg": "n5 p2",
        "window": "64.204-69.535", "wide": False, "jesus": False, "ref": False,
        "locks": ["LEVITE", "JERICHO-ROAD"],
        "narration": "Then a temple assistant came, looked, and also crossed over.",
        "must_show": "the Levite's FACE mid-glance and mid-decision — he has looked, and the looking away is already happening. This frame is his identity anchor and his features must be plainly readable.",
        "must_not_show": "no cream or off-white cloth on him; he must NOT resemble the priest — he is younger, smaller, black-bearded, in dark olive. No pupils on the lens, no blood in frame.",
        "scene": (
            "One photograph, 85mm prime lens at f/2.2, hard high sun, fine grain. "
            "Close on the Levite from the chest up as he walks, turned three quarters "
            "toward the camera so his face is fully lit and fully readable — a "
            "slight, anxious man of about thirty-five, visibly younger and smaller "
            "than the priest, black hair cropped short, a close-trimmed black beard "
            "along the jaw and clean-shaven cheeks, in a plain DARK OLIVE-GREEN "
            "ankle-length tunic with a rust-brown sash and a rust-brown mantle "
            "gathered up in both hands against his chest. He is in the middle of the "
            "decision: his head has already begun to come back round to the front and "
            "his eyes are sliding down and away to his own right, toward something "
            "low at the edge of the road behind him, so his gaze leaves the frame "
            "through its LOWER RIGHT corner and nowhere near the lens. His jaw is "
            "tight and his shoulders are up. He is the only person in the picture. "
            "Vertical white glare puts a short hard shadow under his brow and his "
            "chin; behind him the chalk track and broken white cliffs go soft with "
            "the long lens and the heat haze."
        ),
    },
    {
        "id": "v2-r020-b17", "out": "s17-the-men-who-knew-the-law.jpeg", "seg": "n6 p1",
        "window": "69.535-73.155", "wide": True, "jesus": False, "ref": False,
        "locks": ["PRIEST", "LEVITE", "TRAVELLER", "JERICHO-ROAD"],
        "narration": ("These were the religious professionals, the men who knew the "
                      "law best."),
        "must_show": "both men — the grey priest and the olive Levite — on the road together in one frame, unmistakably the educated and respectable ones, with the beaten man small and unattended behind them.",
        "must_not_show": "no cream or off-white on either of them, no scrolls, no temple, no violence, and nobody looking into the lens.",
        "scene": (
            "One photograph, 50mm lens at f/5.6, hard high sun, fine grain. THE "
            "CAMERA STANDS ON THE TRACK BEHIND BOTH MEN AND SHOOTS DOWNHILL PAST "
            "THEIR BACKS: the priest and the Levite are seen from behind and slightly "
            "to the side, walking away from the camera down the descending road, and "
            "NOT ONE FACE IS TURNED TOWARD THE LENS. The priest is the taller and "
            "heavier of the two on the left, silver-grey hair and beard visible past "
            "his cheek, dove-grey linen robe with its deep-blue hem border and a "
            "grey-blue mantle; the Levite is the smaller, younger man on the right in "
            "his dark olive-green tunic and rust-brown mantle, hurrying a half pace "
            "ahead. Their clothes are clean, well woven and expensive against the "
            "dust, and both walk clear and unhurried on the open track. Far behind "
            "them, small and low at the extreme right edge of the frame and thrown "
            "out of focus, the dust-brown shape of the beaten man still lies where he "
            "was left. Vertical glare, short black shadows, white rock."
        ),
    },
    {
        "id": "v2-r020-b18", "out": "s18-unclean-for-the-temple.jpeg", "seg": "n6 p2",
        "window": "73.155-77.155", "wide": False, "jesus": False, "ref": False,
        "locks": ["PRIEST", "JERICHO-ROAD"],
        "narration": ("Maybe they feared a bloody body would make them unclean for "
                      "the temple."),
        "must_show": "the priest's careful hand gathering his clean grey hem up clear of the dust as he passes — the whole fear rendered as one small fastidious gesture.",
        "must_not_show": "no blood in the frame, no body in the frame, no temple, no face in focus, no cream or white cloth, nothing on the lens.",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, very shallow depth of field, "
            "hard high sun, fine grain. Tight and low on the priest's left hand and "
            "the hem of his robe as he walks past — a soft, clean, well-kept hand "
            "with the fingers hooked into a fistful of fine DOVE-GREY linen, lifting "
            "the deep-blue woven hem border a careful hand's width clear of the pale "
            "grit of the road, and the clean sandal and dust-free ankle stepping "
            "through beneath it. HIS SANDAL IS THE SIMPLEST FIRST-CENTURY KIND: a "
            "flat undyed leather sole with two or three plain leather thongs across "
            "the foot and one thong knotted around the ankle, the knot and the loose "
            "tail of the lace plainly visible. There is no buckle, no metal pin, no "
            "ring, no stud, no stitched strap end and no fastening of any kind "
            "anywhere on the foot, and no metal object appears anywhere in the "
            "picture. The hand and the hem are sharp; his body "
            "above, the grey-blue mantle and the white cliffs behind are thrown far "
            "out of focus, and NO FACE IS VISIBLE OR READABLE ANYWHERE IN THE "
            "PICTURE. Vertical white glare puts a hard little shadow under the "
            "gathered cloth and picks out every fibre of the linen weave and every "
            "grain of dust in the road below it. It is one complete natural hand with "
            "five fingers."
        ),
    },
    {
        "id": "v2-r020-b19", "out": "s19-they-kept-their-distance.jpeg", "seg": "n6 p3",
        "window": "77.155-80.880", "wide": True, "jesus": False, "ref": False,
        "locks": ["PRIEST", "LEVITE", "TRAVELLER", "JERICHO-ROAD"],
        "narration": "Either way, they kept their distance.",
        "must_show": "the distance itself as the subject — the man in the dust large and near, the two clean figures already small and far down the road, the empty track stretching between them.",
        "must_not_show": "nobody turning back, no hand reaching, no cream or white cloth, no faces toward the lens, no blood.",
        "scene": (
            "One photograph, 28mm lens at f/8, hard high sun, fine grain. THE CAMERA "
            "IS DOWN IN THE DUST JUST BEHIND THE BEATEN MAN AND SHOOTS ALONG THE ROAD "
            "OVER HIM: the curled dust-brown shape of his back and shoulder fills the "
            "near bottom left of the frame, seen from behind, no part of his face "
            "toward the lens. From there the empty pale rubble track runs away "
            "downhill through the white gorge, and far along it — small, sharp and "
            "already well past — the priest in dove grey and the Levite in dark olive "
            "walk on side by side, both seen from directly BEHIND and moving away "
            "from the camera, neither of them turning. The width of the road between "
            "the near shoulder and the far figures is empty pale stone and dust, and "
            "it is the largest thing in the picture. Vertical glare, short black "
            "shadows, chalk cliffs, no other living thing anywhere."
        ),
    },
    {
        "id": "v2-r020-b20", "out": "s20-then-a-samaritan-came.jpeg", "seg": "n7 p1",
        "window": "80.880-82.670", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "DONKEY", "JERICHO-ROAD"],
        "narration": "Then a Samaritan came down the road.",
        "must_show": "the Samaritan arriving on the road with his loaded donkey — a working foreigner in a striped rust-and-ochre mantle, instantly a different kind of man from the two who came before.",
        "must_not_show": "he has not seen the beaten man yet — no beaten man in this frame. No cream or off-white cloth, no pupils on the lens, no grey hair or old age on him.",
        "scene": (
            "One photograph, 70mm lens at f/2.8, hard high sun, dust hanging, fine "
            "grain. A medium shot from the side of the track as the Samaritan comes "
            "downhill into the frame from the right, walking, seen in three-quarter "
            "profile — a solid broad-shouldered man of about thirty-five, deeply "
            "sun-darkened, with a short dense BLACK beard, black hair and heavy black "
            "brows, in a travelling mantle woven in broad RUST-RED AND DARK OCHRE "
            "STRIPES over a dark brown tunic, a brown-and-black head-cloth bound with "
            "a twisted dark cord, and a wide leather belt with a small leather purse. "
            "He leads a small grey-brown pack donkey on a hand-twisted flax rope, its "
            "wooden pack-saddle and two woven baskets and a stoppered goatskin "
            "waterskin roped across its back. He is watching the road surface ahead "
            "and to his own left, so his eyes go forward and down and leave the frame "
            "through its LEFT edge, well off the camera axis. Vertical white glare, "
            "short shadows under him and the donkey, pale rubble underfoot and the "
            "chalk gorge soft behind."
        ),
    },
    {
        "id": "v2-r020-b21", "out": "s21-the-word-samaritan.jpeg", "seg": "n7 p2",
        "window": "82.670-86.390", "wide": True, "jesus": True, "ref": True,
        "locks": ["CROWD", "LAWYER", "TEACHING-PLACE"],
        "narration": ("And the crowd listening to Jesus was raised to despise "
                      "Samaritans."),
        "must_show": "BACK IN THE TEACHING PLACE: the crowd's faces at the word Samaritan — a stiffening, a sour look, two people glancing at each other, the scholar's jaw setting.",
        "must_not_show": "no shouting, no fists, no mob, no violence, no Jericho road, no cream or off-white cloth on anybody but Jesus, no pupils on the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.8, late afternoon, fine grain. THE "
            "CAMERA IS BEHIND JESUS AND SHOOTS OVER HIS SHOULDER INTO THE SEATED "
            "CROWD: the back of his head, his dark wavy hair to below the shoulders "
            "and one cream-robed shoulder fill the near left of the frame, large and "
            "out of focus, and his face is not visible and not toward the lens. "
            "Beyond him, sharp, six or seven seated listeners have all just reacted "
            "to a single word — a grey-bearded man's mouth pulling down at one "
            "corner, a woman's chin lifting away, two younger men turning their heads "
            "toward each other in the middle of a look, one man's eyes rolling "
            "sideways. At the right of the group the scholar of the law stands with "
            "his jaw set and his indigo-blue mantle gathered in one fist. Every gaze "
            "in the picture goes either to another person inside the frame or off "
            "through its left edge past the camera; nobody's pupils are on the lens. "
            "Their garments are rust brown, dark olive, umber, blue-grey and dusty "
            "indigo, and the only cream anywhere in the frame is Jesus's own robe at "
            "the near left edge. Low warm sun from the right."
        ),
    },
    {
        "id": "v2-r020-b22", "out": "s22-an-old-hatred.jpeg", "seg": "n7 p3",
        "window": "86.390-92.511", "wide": True, "jesus": False, "ref": False,
        "locks": ["JERICHO-ROAD"],
        "narration": ("Different blood, wrong worship, an old hatred hundreds of "
                      "years deep."),
        "must_show": "the geography of the grudge — two separate peaks holding two separate places of worship, seen across a wide empty hazed valley, with nothing at all connecting them.",
        "must_not_show": "no people at all in this frame, no domes, no minarets, no bell towers, no tiled or pitched roofs, no modern city, no crosses, no writing.",
        "scene": (
            "One photograph, 135mm lens at f/8, hard high sun, heavy heat haze "
            "compressing the distance, fine grain. A landscape with NO PEOPLE IN IT "
            "AT ALL, shot from a stony ridge whose near foreground of bare limestone "
            "and burnt thorn scrub runs out of focus across the bottom of the frame; "
            "the camera looks out from behind that ridge and away from it. Across a "
            "wide hazed empty valley two separate brown mountain summits rise, one to "
            "the left and one to the right, each carrying a small walled enclosure of "
            "the same pale dressed limestone as the hills — flat roofs, plain "
            "rectangular courts, low square blocks, hand-cut stone and nothing else. "
            "Between them there is nothing but empty air, layered haze and the dry "
            "valley floor: no road, no bridge, no path and no building joins them. "
            "Vertical white glare flattens both summits equally and the haze stacks "
            "them into pale receding bands."
        ),
    },
    {
        "id": "v2-r020-b23", "out": "s23-the-last-man-expected.jpeg", "seg": "n8",
        "window": "92.511-97.822", "wide": False, "jesus": True, "ref": True,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": ("A Samaritan was the last man in the world they expected to be "
                      "the hero of the story."),
        "must_show": "Jesus's face as he says it — completely steady, knowing exactly what he has just done to his listeners, with the scholar out of focus and rigid in the foreground.",
        "must_not_show": "no smirk, no triumph, no confrontation; no halo, glow or rim-light; no pupils on the lens.",
        "scene": (
            "One photograph, 85mm lens at f/2, late afternoon, fine grain. An "
            "OVER-THE-SHOULDER two-shot from behind and to the right of the standing "
            "scholar: his indigo-blue shoulder and the edge of his greying beard fill "
            "the near right of the frame, large and out of focus and turned away from "
            "the camera. Beyond him, sharp, Jesus is seated and looking up and to his "
            "own right directly at the scholar, so HIS GAZE HAS ITS TARGET INSIDE THE "
            "FRAME — on that out-of-focus indigo shoulder — and never reaches the "
            "lens. His expression is completely steady and unhurried, warm and "
            "unblinking, the face of a man who knows precisely what he has just said "
            "and is waiting without pressure for it to land. Warm low sun from the "
            "left crosses his cheekbone and the bridge of his nose; the light falls "
            "onto him and nothing comes off him, and there is no light around his "
            "head or along his shoulder. The hillside behind is a soft warm wash."
        ),
    },
    {
        "id": "v2-r020-b24", "out": "s24-moved-with-compassion.jpeg", "seg": "n9",
        "window": "97.822-103.550", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "JERICHO-ROAD"],
        "narration": ("He saw the beaten stranger. And the text says he was moved "
                      "with compassion."),
        "must_show": "the frame the whole video stands on — the Samaritan's FACE the instant he sees: not polite pity but a man visibly hit under the ribs by another man's condition. His features must be sharp and completely readable; this is his identity anchor.",
        "must_not_show": "no tears running, no theatrical horror, no hand clapped over the mouth, no pity-face; no cream or off-white cloth; no pupils on the lens; no grey hair, white beard or old age on him.",
        "scene": (
            "One photograph, 105mm prime lens at f/2, very shallow depth of field, "
            "hard high sun, fine grain. Very close on the Samaritan's face and "
            "shoulders alone, turned three quarters toward the camera and lit full so "
            "every feature reads — a solid, deeply sun-darkened man of about "
            "thirty-five with a short dense BLACK beard, black hair, heavy black "
            "brows and a broad blunt nose, the striped rust-red and dark ochre mantle "
            "just visible at his shoulder and the bound brown-and-black head-cloth "
            "above. He has stopped walking. His lips have come apart, his brows have "
            "pulled up and together in the middle, and the whole set of his jaw has "
            "gone loose — the involuntary face of a man who has just been hit "
            "somewhere under the ribs by what he is looking at. His eyes are wide and "
            "aimed DOWN and to his own left at something low on the ground, so his "
            "gaze exits through the LOWER LEFT of the frame and is nowhere near the "
            "lens. A hand has come halfway up into the bottom edge of the frame and "
            "stopped. Vertical white glare, a sheen of sweat and dust on his skin, "
            "the pale road behind him blown to a soft white blur."
        ),
    },
    {
        "id": "v2-r020-b25", "out": "s25-he-knelt-in-the-dirt.jpeg", "seg": "n10 p1",
        "window": "103.550-106.880", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "DONKEY", "JERICHO-ROAD"],
        "narration": ("He knelt down in the dirt beside a man his people were "
                      "supposed to hate."),
        "must_show": "both knees actually down in the dust of the road, the striped mantle dragging in the grit, his hands already going to the man — a man ruining his own clothes without noticing.",
        "must_not_show": "no blood, no open wound, no exposed body, no cream cloth, no faces toward the lens, nobody else on the road.",
        "scene": (
            "One photograph, 35mm lens at f/3.5, hard high sun, fine grain. THE "
            "CAMERA IS DOWN AT DUST LEVEL BEHIND THE SAMARITAN AND SHOOTS PAST HIS "
            "BACK: his striped rust-and-ochre mantle and his broad back and shoulders "
            "fill the near right of the frame, seen from behind, and his face is not "
            "toward the lens. BOTH HIS KNEES ARE ON THE GROUND in the pale grit, the "
            "trailing corner of the striped mantle already lying in the dust and the "
            "dirt already ground into the wool at his shins. THE SOLES OF HIS FEET "
            "TURNED UP BEHIND HIM ARE BARE BROWN SKIN, dusty and hard, or the flat "
            "dark undyed leather sole of a plain thong sandal — never a thick pale "
            "moulded sole, never a white or grey shoe, never a rubber tread, never "
            "any manufactured footwear. He is leaning in and "
            "both his hands are reaching down and forward. Beyond his shoulder, "
            "sharp, the beaten traveller lies curled on his side in his torn "
            "dust-brown knee-length undertunic, dust caked on his cheek and dried "
            "dark blood matted in the hair at his temple, his eyes barely open and "
            "aimed at the ground. Behind them both the small grey-brown donkey stands "
            "on the empty track with its rope reins hanging loose. The vertical glare "
            "is fierce, the shadows are short and black, and the road is otherwise "
            "completely empty."
        ),
    },
    {
        "id": "v2-r020-b26", "out": "s26-oil-and-wine.jpeg", "seg": "n10 p2a",
        "window": "106.880-109.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "JERICHO-ROAD"],
        "narration": "He cleaned and bound the wounds,",
        "must_show": "hands at work — a small clay oil flask tipped over a strip of clean linen, a goatskin wineskin on the ground beside it, the Samaritan's thick brown fingers winding the cloth around the traveller's forearm.",
        "must_not_show": "no open wound, no torn flesh, no running or pooled blood, no glass bottle, no metal bowl, no modern bandage roll or gauze; no faces on the lens.",
        "scene": (
            "One photograph, 100mm macro lens at f/2.8, very shallow depth of field, "
            "hard high sun, fine grain. Tight on four hands working in the dust. The "
            "Samaritan's are broad, brown, thick-fingered and filthy with road dust, "
            "and they are winding a narrow strip of coarse pale-fawn woven linen "
            "around the traveller's dust-caked forearm, one thumb holding the loose "
            "end down while the other hand draws the wrap around. A small stoppered "
            "clay oil flask, unglazed and hand-thrown, is tipped just above the cloth "
            "with a bead of oil running down its lip, and a goatskin wineskin lies "
            "open-mouthed on the grit beside them, wet and dark at its neck. The "
            "wrapped arm and the flask are sharp; the striped rust-and-ochre sleeve "
            "above and the dust-brown torn undertunic beyond are thrown far out of "
            "focus, and NO FACE IS VISIBLE ANYWHERE IN THE PICTURE. Vertical white "
            "glare picks out every fibre of the linen, the throwing rings on the clay "
            "and every grain of dust on the skin. Every hand in the frame is complete "
            "and natural with five fingers."
        ),
    },
    {
        "id": "v2-r020-b27", "out": "s27-on-his-own-animal.jpeg", "seg": "n10 p2b",
        "window": "109.800-113.771", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "DONKEY", "JERICHO-ROAD"],
        "narration": "lifted him onto his own animal, and walked beside him on foot.",
        "must_show": "the traveller riding, slumped forward over the donkey's neck and steadied by one of the Samaritan's hands, while the SAMARITAN WALKS ON HIS OWN FEET beside the animal — the owner on the ground, the stranger on the beast.",
        "must_not_show": "the Samaritan must NOT be riding and must not be up on the animal in any way. No second animal, no cart, no saddle with stirrups or metal fittings, no cream cloth, no faces on the lens.",
        "scene": (
            "One photograph, 35mm lens at f/4, late afternoon now, the light gone low "
            "and amber and coming from behind, long shadows, fine grain. THE CAMERA "
            "IS ON THE TRACK BEHIND THEM AND SHOOTS DOWNHILL PAST THEIR BACKS as they "
            "move away from it: no face is turned toward the lens anywhere in the "
            "frame. The small grey-brown donkey walks in the middle of the picture "
            "with the beaten traveller up on its back, slumped forward along its neck "
            "with both arms hanging down and his torn dust-brown undertunic and "
            "bandaged forearm plain against the animal's shaggy coat, the woven "
            "baskets and the goatskin waterskin roped behind him. THE SAMARITAN IS "
            "WALKING ON THE GROUND at the donkey's left flank, both his dusty "
            "sandalled feet clearly on the rubble of the road, his striped "
            "rust-and-ochre mantle swinging at his back, the flax rope rein in his "
            "right hand and his left hand laid flat on the traveller's back to hold "
            "him on. Their three long shadows stretch back toward the camera down the "
            "descending pale track; the chalk gorge is going warm and soft behind "
            "them."
        ),
    },
    # ================================================ THE INN — night, morning ===
    {
        "id": "v2-r020-b28", "out": "s28-through-the-night.jpeg", "seg": "n11 p1",
        "window": "113.771-116.511", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "TRAVELLER", "INN"],
        "narration": "He brought him to an inn and cared for him through the night.",
        "must_show": "night inside the inn, one clay lamp burning — the traveller asleep on a straw pallet on the mud-brick bench, the Samaritan sitting on the beaten-earth floor beside him, still awake, still there.",
        "must_not_show": "no glass, no lantern, no candle, no fireplace, no window glass, no bed frame, no chair; no cream or off-white cloth on either man; no pupils on the lens.",
        "scene": (
            "One photograph, 50mm lens wide open at f/1.8, very high ISO, heavy grain, "
            "almost no light. Inside the inn at night. The ONLY light in the frame is "
            "the bare wick of one shallow clay saucer oil lamp standing in a niche cut "
            "in the bare mud-plaster wall, and it throws a small warm circle and "
            "leaves everything past it in deep brown darkness. The traveller lies on a "
            "straw pallet on the low mud-brick bench along the wall, on his back under "
            "a coarse brown blanket, asleep, his bandaged forearm outside the blanket "
            "and the dried blood cleaned out of his hair. The Samaritan sits on the "
            "beaten-earth floor beside the bench with his back against the wall, one "
            "knee up, still in his striped rust-and-ochre mantle, awake — his head "
            "turned down toward the sleeping man so his face is in three-quarter and "
            "his gaze goes down and out through the BOTTOM LEFT of the frame, nowhere "
            "near the lens. Straw on the floor, a stacked clay jar and a hanging "
            "goatskin at the edge of the lamplight, and black darkness above. There "
            "are only two people in the picture, and every face in it is ordinary "
            "human skin that receives the lamplight and never emits light of its own."
        ),
    },
    {
        "id": "v2-r020-b29", "out": "s29-two-silver-coins.jpeg", "seg": "n11 p2a",
        "window": "116.511-120.600", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "INNKEEPER", "INN"],
        "narration": ("In the morning he pressed two silver coins into the "
                      "innkeeper's hand,"),
        "must_show": "morning in the inn doorway — the Samaritan pressing coins into the innkeeper's open palm and closing the man's fingers over them. The INNKEEPER'S FACE must be sharp and fully readable; this frame is his identity anchor.",
        "must_not_show": "no purse of many coins spilling, no coin stacks, no writing or numerals on the coins, no cream or off-white cloth on either man, no pupils on the lens.",
        "scene": (
            "One photograph, 50mm lens at f/2.2, early morning, thin level light "
            "coming in low from the east through the low doorway, fine grain. Two men "
            "from the chest up just inside the inn's plank door. The innkeeper is "
            "turned three quarters toward the camera and lit fully so his face reads "
            "completely — a heavy-set man of about fifty, balding on top with "
            "grey-streaked dark hair at the sides, a broad grizzled beard and a "
            "shrewd unhurried expression, in a dusty dark brown wool tunic with the "
            "sleeves pushed back and a scuffed leather apron. His right hand is open "
            "palm-up between them. The Samaritan stands in profile at the left edge, "
            "his striped rust-and-ochre mantle and bound brown-and-black head-cloth "
            "against the bright doorway, his own brown hand pressing down into the "
            "innkeeper's palm and folding the man's fingers closed over what is in "
            "it. Both men are looking DOWN at their two joined hands in the middle of "
            "the frame, so both eyelines have a target inside the picture and neither "
            "man's pupils are anywhere near the lens. Bare mud-plaster wall, beaten "
            "earth and straw underfoot, low morning light."
        ),
    },
    {
        "id": "v2-r020-b30", "out": "s30-about-two-days-wages.jpeg", "seg": "n11 p2b",
        "window": "120.600-124.880", "wide": False, "jesus": False, "ref": False,
        "locks": ["INNKEEPER", "INN"],
        "narration": "about two days wages, and said, take care of him.",
        "must_show": "EXACTLY TWO silver coins and no third, lying separated and individually countable in the innkeeper's opened brown palm.",
        "must_not_show": "not three coins, not a handful, not a heap, not a stack, not a purse; no writing, numerals, dates or lettering on either coin; no modern milled edge; no face in the frame.",
        "scene": (
            "One photograph, 100mm macro lens at f/4, early morning, low level light "
            "from the left, fine grain. Tight and straight down on the innkeeper's "
            "open right hand, a broad calloused working palm with dirt in the creases, "
            "held flat. TWO SILVER COINS LIE ON IT AND ONLY TWO — separated by a clear "
            "gap of bare skin, each one whole and individually countable, small "
            "hand-struck discs of tarnished silver, slightly irregular in outline and "
            "thickness, with worn soft unreadable relief on their faces and plain "
            "unmilled edges. There is no third coin anywhere in the frame, no stack, "
            "no heap and no purse. His dusty dark brown sleeve and the leather apron "
            "below run out of focus at the edges and NO FACE IS VISIBLE IN THE "
            "PICTURE. The low level morning light comes in from the left and rakes "
            "across the palm, putting a small hard shadow under each coin so the two "
            "of them are unmistakably separate objects."
        ),
    },
    {
        "id": "v2-r020-b31", "out": "s31-i-will-repay-thee.jpeg", "seg": "j35",
        "window": "124.880-131.639", "wide": False, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "INNKEEPER", "INN"],
        "narration": ("Take care of him; and whatsoever thou spendest more, when I "
                      "come again, I will repay thee."),
        "must_show": "the Samaritan giving his word in the doorway — one hand still on the door post, half turned back, saying the thing that binds him to a stranger's bill.",
        "must_not_show": "no written note, no tablet, no ledger, no contract, no handshake, no cream cloth, no pupils on the lens, no hinges or metalwork on the door.",
        "scene": (
            "One photograph, 50mm lens at f/2, early morning, fine grain. An "
            "OVER-THE-SHOULDER two-shot from behind the innkeeper: his broad dark "
            "brown shoulder, the strap of his leather apron and the grey-streaked "
            "back of his head fill the near right of the frame, large and out of "
            "focus, his back to the camera. Beyond him, sharp in the low doorway with "
            "the pale morning hillside behind him, the Samaritan has half turned back "
            "on his way out — one broad brown hand flat against the hewn timber door "
            "post, his body already angled outward, his striped rust-and-ochre mantle "
            "catching the level light from outside. He is speaking: his mouth is open "
            "on a word and his free hand has come up with two fingers extended in the "
            "plain gesture of a man giving his word. HIS EYES ARE ON THE INNKEEPER'S "
            "FACE INSIDE THE FRAME, on that out-of-focus shoulder and head to the "
            "right, so his gaze has a target in the picture and never reaches the "
            "lens. Bare mud-plaster, a plank door on wooden pins, beaten earth and "
            "straw."
        ),
    },
    {
        "id": "v2-r020-b32", "out": "s32-he-did-not-just-move-on.jpeg", "seg": "n12 p1-p2",
        "window": "131.639-137.349", "wide": True, "jesus": False, "ref": False,
        "locks": ["SAMARITAN", "DONKEY", "INN", "JERICHO-ROAD"],
        "narration": ("And whatever more it costs, when I come back, I will repay you "
                      "myself. He did not just help and move on."),
        "must_show": "the Samaritan leading his donkey away from the inn in the morning and looking BACK over his shoulder at the doorway — leaving, but not finished.",
        "must_not_show": "no farewell wave, no crowd, no other traveller, no cream cloth, no face turned to the lens, no sunset colours.",
        "scene": (
            "One photograph, 35mm lens at f/5.6, early morning, low level light from "
            "the east, long shadows, fine grain. THE CAMERA STANDS IN THE INN DOORWAY "
            "AND SHOOTS OUT AFTER HIM, so the Samaritan is seen from BEHIND as he "
            "walks away down the track with the donkey on its flax rope beside him — "
            "the striped rust-and-ochre mantle across his back, the empty woven "
            "baskets and the goatskin waterskin roped over the wooden pack-saddle, "
            "both of them moving away from the camera. He has turned his head back "
            "over his right shoulder toward the doorway, so his face is caught in "
            "sharp three-quarter from behind and his eyeline runs back past the "
            "camera and out through the frame's RIGHT edge, off the lens axis. The "
            "expression is unfinished business, not farewell. A dark out-of-focus "
            "edge of the doorway's hewn timber frames the near left and top of the "
            "picture. Beyond them the pale rubble track runs down into the bare "
            "chalk-and-ochre hills under a thin pale morning sky."
        ),
    },
    {
        "id": "v2-r020-b33", "out": "s33-he-tied-his-own-name-to-it.jpeg", "seg": "n12 p3",
        "window": "137.349-141.364", "wide": False, "jesus": False, "ref": False,
        "locks": ["INNKEEPER", "TRAVELLER", "INN"],
        "narration": "He tied his own name to a stranger's recovery.",
        "must_show": "the innkeeper standing over the sleeping traveller with the two coins still closed in his fist — a working man taking on somebody else's promise.",
        "must_not_show": "no coins on display, no counting, no ledger or writing, no cream cloth, no pupils on the lens, no glass or lantern.",
        "scene": (
            "One photograph, 50mm lens at f/2, early morning, one shaft of thin level "
            "light coming in from a small square unglazed window hole, fine grain. "
            "The innkeeper stands beside the low mud-brick bench looking down at the "
            "sleeping man — a heavy-set balding man of fifty with a broad grizzled "
            "beard, in his dusty dark brown tunic and scuffed leather apron, one "
            "shoulder catching the window light and the rest of him in brown shadow. "
            "His right FIST IS STILL CLOSED at his side around what was put into it, "
            "the knuckles tight and nothing visible in the hand. His head is bent and "
            "his eyes are down on the pallet in front of him, so his gaze exits the "
            "frame through its BOTTOM EDGE, far off the camera axis, and his "
            "expression is thoughtful and a little put-upon rather than warm. Below "
            "him, sharp in the foreground, the traveller sleeps on the straw pallet "
            "under the coarse brown blanket with his bandaged forearm across his "
            "chest and his face turned away toward the wall. Bare mud plaster, straw "
            "on beaten earth, a clay jar in the shadow. Only two people are in the "
            "picture."
        ),
    },
    # ================================================ BACK TO THE FRAME STORY ====
    {
        "id": "v2-r020-b34", "out": "s34-he-turned-it-back-on-him.jpeg", "seg": "n13",
        "window": "141.364-147.876", "wide": True, "jesus": True, "ref": True,
        "locks": ["LAWYER", "CROWD", "TEACHING-PLACE"],
        "narration": ("Then Jesus turned the scholar's own question back on him, and "
                      "asked which of the three men had been the neighbor."),
        "must_show": "the teaching place again in the same low afternoon sun — the story finished, Jesus looking up at the scholar who is still standing, and the whole crowd now turned to watch the scholar instead.",
        "must_not_show": "no Jericho road, no donkey, no cream or off-white cloth on anybody but Jesus, no halo or glow, nobody looking into the lens.",
        "scene": (
            "One photograph, 35mm lens at f/3.5, late afternoon, fine grain. THE "
            "CAMERA IS LOW AND OFF TO THE SIDE, BEHIND THE SEATED LISTENERS, AND "
            "SHOOTS ACROSS THE GROUP PAST THEIR BACKS AND SHOULDERS: two out-of-focus "
            "seated backs in rust brown and dusty indigo hold the near left of the "
            "frame and NOT ONE FACE IS TURNED TOWARD THE LENS. Jesus sits on the low "
            "limestone at the right of the picture, sharp, his forearms resting on "
            "his knees and his head tilted up toward the standing scholar; he has "
            "just asked something and is waiting. The scholar stands in the middle "
            "distance in his indigo-blue robe, seen in three-quarter from behind, one "
            "hand half lifted and stalled in the air. Every seated listener's head "
            "has turned away from Jesus and toward the scholar, so the whole picture's "
            "attention converges on the man who has to answer. Low warm sun from the "
            "right lays long shadows across the pale dust toward the camera; the "
            "light falls on Jesus and nothing comes off him."
        ),
    },
    {
        "id": "v2-r020-b35", "out": "s35-which-of-these-three.jpeg", "seg": "j1",
        "window": "147.876-153.721", "wide": False, "jesus": True, "ref": True,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": ("Which now of these three, thinkest thou, was neighbour unto "
                      "him that fell among the thieves?"),
        "must_show": "Jesus asking the question — his hand open and offered upward toward the scholar, his face patient and completely without triumph.",
        "must_not_show": "no counting on fingers, no three fingers held up, no accusation, no halo or glow or rim-light, no pupils on the lens.",
        "scene": (
            "One photograph, 85mm lens at f/2, late afternoon, fine grain. An "
            "OVER-THE-SHOULDER two-shot from behind and below the standing scholar: "
            "his indigo-blue shoulder and the underside of his greying dark beard "
            "fill the near left of the frame, large and out of focus, his back toward "
            "the camera. Beyond him, sharp, Jesus is seated and looking up at him — "
            "his right hand come up off his knee, open and turned palm-up and offered "
            "toward the scholar, his lips parted on the question, his eyebrows level "
            "and his face completely without triumph. HIS EYES ARE FIXED ON THE "
            "SCHOLAR'S FACE INSIDE THE FRAME, on that out-of-focus indigo shoulder at "
            "the left, so his gaze has a target in the picture and does not reach the "
            "lens. Low warm sun comes from behind the camera's right and models his "
            "cheek and beard; his cream robe takes the light and gives none back and "
            "there is no light around his head. The warm hillside behind is thrown to "
            "a soft blur."
        ),
    },
    {
        "id": "v2-r020-b36", "out": "s36-he-that-shewed-mercy.jpeg", "seg": "s37",
        "window": "153.721-156.901", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": "He that shewed mercy on him.",
        "must_show": "the scholar answering — the words coming out slowly and reluctantly, his eyes down, a man conceding something he did not want to concede.",
        "must_not_show": "no smile, no anger, no shouting; Jesus is not in this frame; no cream cloth; no pupils on the lens.",
        "scene": (
            "One photograph, 105mm lens at f/2, very shallow depth of field, late "
            "afternoon, fine grain. Close on the scholar of the law from the "
            "shoulders up, turned three quarters to his own left — forty-five, "
            "squared grey-shot dark beard, folded head-cloth, deep indigo-blue robe. "
            "He is answering, and it is costing him: his mouth is barely open and "
            "moving on a short reluctant phrase, his throat is tight, and his eyes "
            "have dropped away and down toward the ground in front of a man seated "
            "below him, so his gaze leaves the frame through its BOTTOM LEFT and is "
            "nowhere near the lens. His hands have come down and gone still at his "
            "sides. The certainty is completely gone out of his face. Low warm sun "
            "from the right rims the edge of his beard and the folds of the indigo "
            "mantle and leaves the near side of his face in soft shadow; behind him "
            "the crowd is an unreadable warm blur."
        ),
    },
    {
        "id": "v2-r020-b37", "out": "s37-could-not-say-the-word.jpeg", "seg": "n14 p1-p2",
        "window": "156.901-161.401", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "CROWD", "TEACHING-PLACE"],
        "narration": ("The scholar could not even say the word Samaritan. He "
                      "answered, the one who showed mercy."),
        "must_show": "the cost of the answer on his face and body — chin down, jaw working, a man who has just heard himself refuse to say a name out loud in front of everyone.",
        "must_not_show": "Jesus is not in this frame. No shame theatre, no covering the face, no tears; no cream cloth on anybody; no pupils on the lens.",
        "scene": (
            "One photograph, 70mm lens at f/2.2, late afternoon, fine grain. The "
            "scholar from the waist up, seen almost in full profile from his right "
            "side so his face is a clean lit edge against the soft background and no "
            "part of his gaze can reach the camera — his eyeline runs flat across the "
            "frame and out through its LEFT edge. His chin has come down toward his "
            "chest, his lips are pressed shut, and the muscle at the corner of his "
            "jaw is visibly working. One hand has come up and closed on the tassel at "
            "the corner of his indigo mantle and is holding it. Behind and below him, "
            "thrown well out of focus, two seated listeners in rust brown and dark "
            "olive have their heads turned up toward him and are watching, their "
            "faces soft and unreadable and turned away from the camera. Low warm sun "
            "from the right outlines his brow, his nose and the grey in his beard."
        ),
    },
    {
        "id": "v2-r020-b38", "out": "s38-he-flipped-the-question.jpeg", "seg": "n14 p3",
        "window": "161.401-163.801", "wide": False, "jesus": True, "ref": True,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": "Jesus had flipped the whole question.",
        "must_show": "Jesus close and still in the quiet beat after the answer — the argument is over and he has not raised his voice once.",
        "must_not_show": "no smile of victory, no raised hand, no gesture at all; no halo, glow or rim-light; no pupils on the lens; nobody else in focus.",
        "scene": (
            "One photograph, 105mm lens at f/2, extremely shallow depth of field, "
            "late afternoon, fine grain. AN OVER-THE-SHOULDER TWO-SHOT, NOT A "
            "PORTRAIT: the camera sits close behind and below the standing scholar's "
            "right shoulder, so his out-of-focus indigo-blue shoulder and the dark "
            "underside of his greying beard occupy the whole near RIGHT THIRD of the "
            "frame and his back is to the lens. Jesus is beyond that shoulder, "
            "seated, sharp, from the chest up and set well over to the LEFT of the "
            "frame. He is still and quiet in the beat after an answer he already knew "
            "was coming: his mouth closed and relaxed, no smile, no triumph, just "
            "steadiness and a warmth that does not press. HIS HEAD IS TURNED "
            "NOTICEABLY TO HIS OWN RIGHT, ACROSS THE FRAME, AND HIS EYES ARE FIXED ON "
            "THE SCHOLAR'S FACE INSIDE THE PICTURE — on that out-of-focus indigo "
            "shoulder at the right edge — so his eyeline runs sideways across the "
            "frame and the camera catches his face at an angle, in three-quarter, "
            "never square on and never down the lens axis. Low warm sun from the "
            "right crosses the bridge of his nose and the near cheekbone and leaves "
            "the far side of his face in soft shadow; the light lands on him and "
            "nothing at all comes off him, and there is nothing around his head or "
            "hair but ordinary air. Everything behind him is an unreadable warm wash "
            "of dust and olive green."
        ),
    },
    {
        "id": "v2-r020-b39", "out": "s39-which-of-them-acted-like-one.jpeg",
        "seg": "n14 p4",
        "window": "163.801-169.029", "wide": True, "jesus": True, "ref": True,
        "locks": ["LAWYER", "CROWD", "TEACHING-PLACE"],
        "narration": "Not who counts as my neighbor, but which of them acted like one.",
        "must_show": "the whole gathering holding still with the question turned inside out — Jesus seated and steady at the centre of everyone's attention, the scholar standing with nothing left to say.",
        "must_not_show": "no cream or off-white cloth on anybody except Jesus, no halo or glow, no posed line of people facing the camera, nobody's pupils on the lens.",
        "scene": (
            "One photograph, 35mm lens at f/4, late afternoon, fine grain. THE CAMERA "
            "STANDS BEHIND THE OUTERMOST SEATED LISTENERS AND SHOOTS PAST THEIR BACKS "
            "INTO THE GROUP: three out-of-focus seated backs and head-cloths in rust "
            "brown, umber and blue-grey fill the near foreground, and NOT ONE FACE IS "
            "TURNED TOWARD THE LENS. Beyond them the whole gathering is held still. "
            "Jesus sits on the low limestone slightly right of centre, sharp, hands "
            "loose on his knees, his head turned up toward the scholar; every seated "
            "person's head and eyeline in the picture converges either on Jesus or on "
            "the standing man, so the attention visibly gathers to those two and "
            "nobody in the frame is looking outward. The scholar stands to the left in "
            "his indigo-blue robe, seen in three-quarter from behind, his arms fallen "
            "to his sides. Low warm sun rakes in from the right and throws every long "
            "shadow across the pale dust toward the camera. The garments in the "
            "picture are rust brown, dark olive, umber, blue-grey and dusty indigo, "
            "and the only cream in the frame is Jesus's own robe."
        ),
    },
    {
        "id": "v2-r020-b40", "out": "s40-go-and-do-thou-likewise.jpeg", "seg": "j2",
        "window": "169.029-171.791", "wide": False, "jesus": True, "ref": True,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": "Go, and do thou likewise.",
        "must_show": "Jesus saying the last line — leaning forward off the stone toward the scholar, an open hand turned outward in the gesture of sending somebody off to go and do it.",
        "must_not_show": "no pointing finger, no command posture, no anger; no halo, glow or rim-light; no pupils on the lens.",
        "scene": (
            "One photograph, 85mm lens at f/2, late afternoon, fine grain. An "
            "OVER-THE-SHOULDER two-shot from behind and to the left of the standing "
            "scholar: his indigo-blue shoulder and mantle tassel fill the near left "
            "edge, large and out of focus, his back to the camera. Beyond him, sharp, "
            "Jesus has come forward off the limestone toward him — his weight on one "
            "forearm across his knee, his shoulders leaning in, his right hand open "
            "and turned outward and moving away from his own body in the plain "
            "gesture of sending a man off to go and do something. His mouth is open "
            "on the last word and his expression is warm and direct with no hardness "
            "in it. HIS EYES ARE ON THE SCHOLAR'S FACE INSIDE THE FRAME, on that "
            "out-of-focus indigo shoulder to the left, so his gaze has its target in "
            "the picture and never meets the lens. Low warm sun from the right; the "
            "light falls onto his cream robe and none comes off it, and there is "
            "nothing around his head but ordinary air."
        ),
    },
    {
        "id": "v2-r020-b41", "out": "s41-go-and-be-the-neighbor.jpeg", "seg": "n15 p1-p2",
        "window": "171.791-175.521", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAWYER", "TEACHING-PLACE"],
        "narration": ("Stop asking who you are allowed to walk past. Go, and be the "
                      "neighbor."),
        "must_show": "the scholar turning to leave — caught in the first step away, his face carrying something that has genuinely landed rather than been won off him.",
        "must_not_show": "Jesus is not in this frame. No storming off, no humiliation, no crowd jeering; no cream cloth; no pupils on the lens.",
        "scene": (
            "One photograph, 70mm lens at f/2, late afternoon, fine grain. The "
            "scholar of the law framed from the thighs up, caught mid-turn as he "
            "starts to walk away — his body already swung to his own left and moving "
            "ACROSS the frame from right to left, one sandalled foot lifting, the "
            "indigo-blue mantle swinging out behind him and his shoulders come down "
            "out of their earlier set. His head is still half turned back over his "
            "right shoulder so his lit face is caught in three-quarter, his eyes "
            "unfocused and travelling down and out through the frame's LOWER RIGHT "
            "corner, well past the camera. He is not angry and not humiliated; "
            "something has simply landed. Low warm sun from the right side rims his "
            "beard and the folds of the indigo wool and throws his long shadow out "
            "ahead of him across the pale dust. The crowd and the olive branches "
            "behind him are a soft unreadable warm blur and no face back there is "
            "turned toward the camera."
        ),
    },
    {
        "id": "v2-r020-b42", "out": "s42-the-road-goes-on.jpeg", "seg": "n15 p3-p4",
        "window": "175.521-180.035", "wide": True, "jesus": False, "ref": False,
        "locks": ["JERICHO-ROAD"],
        "narration": "That is how good he is. He will not even let you keep score.",
        "must_show": "the empty Jericho road itself in the last of the day — the place where the whole thing happened, quiet now, still running down and on, waiting for whoever comes along it next.",
        "must_not_show": "no people at all, no blood, no body, no donkey, no inn, no writing or symbol of any kind; not a red or purple sunset sky.",
        "scene": (
            "One photograph, 28mm lens at f/8, late afternoon, the sun low and warm "
            "and coming in from the right, long shadows reaching across the ground, "
            "fine grain. A landscape with NO PEOPLE IN IT AT ALL. The camera stands "
            "in the middle of the bare rubble track at knee height and looks along it "
            "away from the high ground behind, with the pale dust and loose limestone "
            "of the road running away from the lens into the picture; the track "
            "descends and bends out of sight around the flank of the chalk-white "
            "gorge on its way down. The broken cliffs on the right are warm ochre "
            "where the low light hits them and deep blue-shadowed in their clefts; "
            "the ravine falls away on the left into cool shadow; the hazed brown "
            "hills stack away into a clear pale sky that is warm and golden near the "
            "horizon and clean blue above, with no red, orange or purple in it. A "
            "little dust hangs in the low light. The road is empty and completely "
            "still."
        ),
    },
]
