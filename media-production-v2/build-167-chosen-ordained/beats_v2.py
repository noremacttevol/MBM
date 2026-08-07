#!/usr/bin/env python3
"""V2 beat map — row 167, build-167-chosen-ordained (John 15:16).

COVERAGE: 24 pictures over 117.94 s (card_start) = ~4.9 s/picture (matches the
library density set by rows 161-166; lesson 12 movie-coverage, every physical
idea its own frame, an action sequence a frame per action).

OPEN CAMERON COMPLAINT: none on file (`v2_outline.py 167` shows no prior
review). Fresh authoring — the job is the LEARNING/COST laws in the positive:
cover every beat, keep one locked band/one locked folk/one locked place each,
and hand the runner a plate-promote plan so the four recurring places do not
drift, WITHOUT spending an author credit.

SCRIPTURE FACT (John 15:16 KJV, the verse this row narrates), split across the
two red-letter beats:
  kv16a  "Ye have not chosen me, but I have chosen you, and ordained you,"
  kv16b  "that ye should go and bring forth fruit, and that your fruit should
          remain: that whatsoever ye shall ask of the Father in my name, he
          may give it you."

SPEAKER LAW (the row-39 lesson): John's gospel, RED-LETTER — Jesus is the one
speaking John 15:16. So kv16a and kv16b are the ONLY Jesus-voice beats and they
sit on Jesus's own face (jesus=True + ref=True, cream robe). Every n-segment is
the NARRATOR (light-blue scripture voice belongs to no one here — the narrator
frames the teaching). Jesus is ALSO embodied in the narrator beats that show HIM
choosing / calling / ordaining (b06-b08, b21-b22), because those depict the very
act the verse names — never for scale, always the ordinary-sized locked man.

ROW INTENT: milk that leans RESTORATION, kept strictly inside the Bible's own
frame and NEVER naming any church. The heart of the video is a man being CALLED
of God and ORDAINED by the laying on of hands — authority given from heaven
down, received as a gift, never seized as a badge. That is the priesthood
pattern shown through Jesus's own words and his own hands, without one word of
modern church vocabulary. The close hands the same call to the viewer.

HOW JESUS IS DEPICTED (lesson 8 + the Standing Laws): Jesus appears ONLY as the
locked V2 Jesus (LOCK v5 + REF), and only where the verse puts him — speaking
(b04, b05, b15, b16) and choosing/ordaining (b06, b07, b08, b21, b22). Only he
wears cream; ordinary-sized man, NEVER a giant (SCALE GATE, lesson 14); NO
halo/glow/rim-light and no light around his head. Where heaven is meant ("from
heaven down", "ask of the Father", "heaven would answer") it is warm light at
the frame's TOP EDGE, never a figure, face or form in the sky (the Father is
NEVER embodied).

THE ORDINATION SEQUENCE (lesson 12 — a key action gets a frame per action):
the calling/ordaining is covered as a real sequence, not one picture —
Jesus turning to choose the men (b04) -> laying hands to ordain (b05) ->
authority coming from above onto the ordained man (b06) -> singling ONE man out
and calling him by name (b07) -> both hands set on his head, set apart (b08) ->
the ordained man rising to go (b09). It returns at the study-gem summary as
call-by-name (b21) and gift-received-with-open-hands (b22).

MOVIE COVERAGE (lesson 12): the ONE establishing wide is b01 (the lakeshore of
ordinary life) and ONLY b01. Everything else is a single, an over-shoulder
two-shot, or an insert of hands / grain / a scroll. The disciples are always a
SMALL band of distinct real faces, never a crowd, and never the named Twelve
roster crowded in.

FOUR RECURRING PLACES, all NEW (no clean stash match kept the story's own warm
day / harvest-gold light arc, so they are authored as build-local prose locks
and the runner PROMOTES each from this build's first good NON-Jesus frame, per
lesson 11 — never promote a Jesus-bearing frame):
  LAKESHORE     promote b01, wire b02/b03/b23/b24  (bookend: ordinary work)
  TEACHING-HILL promote the first NON-Jesus hill frame b09, wire b10/b18/b19
                (b04-b08, b15, b16, b21, b22 are Jesus frames — they carry
                their own Jesus lock over the same place prose)
  VILLAGE-ROAD  promote b11, wire b13
  HARVEST-FIELD promote b12, wire b14/b17
Optional cross-video landscape plates the runner MAY reuse instead (pure
landscape, non-Jesus, on disk): TEACHING-HILL<-build-68 b10 (grassy slope),
LAKESHORE<-build-30 b03 (morning shore), HARVEST-FIELD<-build-46 b25 (gold
field), VILLAGE-ROAD<-build-110 b11 (village lane). Steps in QC.md.

TIME OF DAY (intentional, and defensible): the narration is thematic (nets,
water, roads, harvest brought home), not the literal Last-Supper night of the
discourse, and the V1 stills chose the same daytime thematic treatment. So the
whole row is warm natural DAY — ordinary morning on the shore, clear sun on the
teaching hill, harvest-gold in the field. No night, no lamplight (except the one
small study-insert b20, a tight interior detail, no place lock).
"""

# LOCKS: one entry per recurring person and per setting. Setting locks NEVER
# name a character. The shared JESUS lock + REF come from v2_prompt.py via the
# jesus/ref flags — never written here.
LOCKS = {
    "LAKESHORE": (
        "LAKESHORE LOCK: the same place in every frame — a wide first-century "
        "lakeshore in warm early-morning light, a strand of pale pebbles and "
        "sand meeting still pale water, ONE plain hewn-timber fishing boat drawn "
        "up on the stones, dark low hills across the far water, hand-knotted "
        "nets drying on the pebbles; soft low golden light coming off the water. "
        "The same shore, boat and far hills throughout — never a harbour wall, "
        "never a quay, never a modern dock, never any modern structure."
    ),
    "TEACHING-HILL": (
        "TEACHING-HILL LOCK: the same place in every frame — a broad open grassy "
        "hillside above the lake in warm clear daylight, dry summer grass and a "
        "few grey outcrops of stone, low scattered olive trees, the pale water "
        "and distant dun hills lying far below; soft warm sun. The same hill, "
        "grass and far water throughout — never a temple, never a palace, never "
        "a building, never any modern structure."
    ),
    "VILLAGE-ROAD": (
        "VILLAGE-ROAD LOCK: the same place in every frame — a worn dirt lane "
        "running into a small first-century village of pale flat-roofed "
        "mud-brick and dressed-stone houses, low dry-stone walls and a few olive "
        "and fig trees along the way, dun hills beyond; warm daylight. The same "
        "lane and the same village throughout — never a paved or modern road, "
        "never a signpost, never a wire or pole, never a modern building."
    ),
    "HARVEST-FIELD": (
        "HARVEST-FIELD LOCK: the same place in every frame — a first-century "
        "field of ripe standing barley gone deep gold under warm harvest-morning "
        "light, low dry-stone field walls, cut sheaves leaning together and a "
        "worn path along its edge, dun hills beyond. The same golden field and "
        "walls throughout — never a machine, never a fence of manufactured "
        "metal, never a modern structure."
    ),
    "DISCIPLES": (
        "DISCIPLES LOCK: the small band Jesus chooses and ordains — a handful of "
        "first-century working men of varied ages, distinct sun-browned faces, "
        "dark hair and beards of differing lengths, plain earth-toned wool of "
        "brown, rust, ochre, olive and undyed grey (never cream — only Jesus "
        "wears cream); ordinary, real, weathered men, NOT posed as a named "
        "roster, never twinned, never a cloned face, never a uniform crowd."
    ),
    "ORDINARY-FOLK": (
        "ORDINARY-FOLK LOCK: ordinary first-century working people going about "
        "unremarkable daily life — a fisherman, a water-carrier, a labourer, "
        "villagers of varied ages, distinct sun-browned faces, plain earth-toned "
        "wool and linen (never cream — only Jesus wears cream); real everyday "
        "people at plain work, never twinned, never a cloned face, never a "
        "uniform crowd."
    ),
}

REF = True

BEATS = [
    {
        "id": "v2-r167-b01", "out": "s01-ordinary-work-by-the-water.jpeg", "seg": "n1",
        "window": "0.280-5.200", "wide": True, "jesus": False, "ref": False,
        "locks": ["LAKESHORE", "ORDINARY-FOLK"],
        "narration": "The people God calls to his work rarely go looking for the honour.",
        "must_show": "the ONE establishing wide — the camera stands back on the pebbled shore behind two ordinary working men, shooting PAST their backs to the still lake and drawn-up boat; plain morning labour, nobody seeking honour, nobody aware of the lens.",
        "must_not_show": "no Jesus and no cream anywhere; not a posed line facing the camera; nobody grand or singled out; no halo or bright ring on anyone; no panel, border or text.",
        "scene": (
            "The film opens on unremarkable morning work: the camera stands a few "
            "steps back on the pebbled lakeshore BEHIND two ordinary fishermen "
            "and shoots PAST their backs and shoulders to the still pale water "
            "and the hewn-timber boat drawn up on the stones. One man is stooped "
            "over a net spread on the pebbles, the other wading shin-deep at the "
            "boat — plain men at plain work in the low golden light, not one face "
            "turned toward the lens, no one dreaming of honour. Every figure has "
            "two arms, two hands and one head, all of ordinary human height."
        ),
    },
    {
        "id": "v2-r167-b02", "out": "s02-mending-a-net.jpeg", "seg": "n1",
        "window": "5.200-10.300", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAKESHORE", "ORDINARY-FOLK"],
        "narration": "They are usually found doing something ordinary — mending a net,",
        "must_show": "an insert — a fisherman's weathered hands working a wooden netting needle through a torn fishing net across his knees, the knots and mesh close and clear; ordinary skilled work.",
        "must_not_show": "no Jesus and no cream; no modern nylon or monofilament — hand-knotted natural fibre; whole hands, five fingers; no face turned to the lens; no panel or text.",
        "scene": (
            "Close on ordinary work: a fisherman sits on the pebbles with a torn "
            "hand-knotted flax net drawn across his knees, his weathered brown "
            "hands drawing a carved wooden netting needle through the mesh and "
            "pulling a knot tight, his eyes down on the work and away from the "
            "camera. The low morning light rakes across the knots and the coarse "
            "twisted fibre. His hands are whole with five fingers each; nothing "
            "in the frame is modern."
        ),
    },
    {
        "id": "v2-r167-b03", "out": "s03-carrying-water.jpeg", "seg": "n1",
        "window": "10.300-15.355", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAKESHORE", "ORDINARY-FOLK"],
        "narration": (
            "carrying water, quietly living an unremarkable life, never dreaming "
            "of appointing themselves to anything."
        ),
        "must_show": "an ordinary woman carrying a fired-clay water jar up from the shore on her shoulder, seen from the side, quiet and unremarkable — plain daily life, no one seeking a place.",
        "must_not_show": "no Jesus and no cream; not posed to the lens — profile or three-quarter away; no modern vessel; whole hands; no panel or text.",
        "scene": (
            "Ordinary life carried on: a woman climbs the shore path from the "
            "water with a rounded fired-clay jar balanced on her shoulder, seen "
            "from the side so her gaze travels ahead up the path and never to the "
            "camera, her step even and unhurried. Behind her the boat and the "
            "still lake sit in the soft morning light. A plain earth-toned figure "
            "of ordinary height, both hands steadying the jar, one head; nothing "
            "modern anywhere."
        ),
    },
    {
        "id": "v2-r167-b04", "out": "s04-i-have-chosen-you.jpeg", "seg": "kv16a",
        "window": "15.355-18.700", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": "Ye have not chosen me, but I have chosen you,",
        "must_show": "SCRIPTURE-EXACT — an over-shoulder two-shot: Jesus turned toward the small band of disciples, one hand opening toward them as he chooses them; the choosing plainly runs from him to them, not from them to him.",
        "must_not_show": "no halo, glow or light around Jesus's head; Jesus ordinary-sized, never a giant; only he wears cream; the disciples NOT in cream; no faces posed to the lens; no panel or text.",
        "scene": (
            "The choosing shown in its true direction: on the grassy hillside in "
            "warm daylight the camera looks over the shoulders and backs of a "
            "small band of disciples to Jesus standing before them, his warm "
            "brown eyes moving across their faces and one open hand extended "
            "toward them as he chooses them out. He wears his plain cream wool "
            "robe; the disciples are distinct earth-toned men turned to him, seen "
            "from behind. His face carries no light around it; he is an "
            "ordinary-sized man with two hands and one head, the offered hand "
            "open, not grasping."
        ),
    },
    {
        "id": "v2-r167-b05", "out": "s05-and-ordained-you.jpeg", "seg": "kv16a",
        "window": "18.700-21.779", "wide": False, "jesus": True, "ref": True,
        "locks": ["DISCIPLES"],
        "narration": "and ordained you,",
        "must_show": "SCRIPTURE-EXACT — a tight two-shot of the ordaining act: Jesus laying both hands on the bowed head of a kneeling disciple, solemn and deliberate — set apart by the laying on of hands.",
        "must_not_show": "no halo or light around Jesus's head or the man's; ordinary-sized; only Jesus in cream; whole hands, no fused fingers; background soft and plain, no second unlocked figure at the edge; no panel or text.",
        "scene": (
            "The ordination itself, close and reverent: a disciple kneels with "
            "his head bowed and Jesus stands over him laying BOTH hands flat and "
            "steady on the crown of the man's head — the laying on of hands that "
            "sets a man apart. Jesus's face is grave and tender, tilted down "
            "toward the kneeling man, not toward the camera; his cream sleeves "
            "fall back from real hands with five fingers each. The warm daylight "
            "is even; nothing rings either head. Both are ordinary-sized men, the "
            "background soft grass with no one else crowding the frame."
        ),
    },
    {
        "id": "v2-r167-b06", "out": "s06-heaven-down-not-the-other-way.jpeg", "seg": "n2",
        "window": "21.779-26.400", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": (
            "Notice the direction of it. The choosing runs from heaven down to "
            "us, not the other way."
        ),
        "must_show": "the DIRECTION made visible — warm light spilling DOWN from the top of the frame onto Jesus and the ordained man below him, authority travelling heaven-to-man; Jesus's hand resting on the man, the man receiving.",
        "must_not_show": "no figure, face or form in the sky (the Father NEVER embodied) — only warm light at the top edge; no halo or ring around any head; ordinary-sized; only Jesus in cream; no panel or text.",
        "scene": (
            "The flow of it drawn from above downward: warm light comes down from "
            "beyond the top edge of the frame onto the hillside, falling first on "
            "Jesus and then, through his hand resting on the ordained man's "
            "shoulder, onto the man himself — the whole picture reading top to "
            "bottom, heaven to man, never the reverse. The light stays at the "
            "frame's upper edge and never becomes a shape, a face or a figure. "
            "Jesus in cream and the earth-toned disciple are both ordinary-sized, "
            "each with two hands and one head, nothing ringing either head."
        ),
    },
    {
        "id": "v2-r167-b07", "out": "s07-calls-them-by-name.jpeg", "seg": "n2",
        "window": "26.400-30.900", "wide": False, "jesus": True, "ref": True,
        "locks": ["DISCIPLES"],
        "narration": "He picks a person out, calls them by their own name,",
        "must_show": "Jesus singling ONE man out of the band — meeting that man's eyes, one hand reaching to him by name, the man turning in surprise that it is HIM being called; the others a little behind.",
        "must_not_show": "no halo or light around Jesus's head; ordinary-sized; only Jesus in cream; the called man plainly picked out from the rest; distinct faces; no face posed to the lens; no panel or text.",
        "scene": (
            "One man singled out by name: Jesus has turned from the small band to "
            "ONE disciple and fixed him with a warm, direct look, one hand "
            "reaching toward that man alone, as if speaking his own name — and "
            "the man has turned half toward Jesus in the surprise of being the "
            "one chosen, a hand rising to his own chest. The other disciples "
            "stand a step back, distinct and watching. Their eyes are on one "
            "another, not the lens. Jesus is an ordinary-sized man in cream; "
            "everyone has two hands and one head, nothing lighting Jesus's head."
        ),
    },
    {
        "id": "v2-r167-b08", "out": "s08-set-apart-with-authority.jpeg", "seg": "n2",
        "window": "30.900-35.227", "wide": False, "jesus": True, "ref": True,
        "locks": ["DISCIPLES"],
        "narration": (
            "and sets them apart with real authority for a work that is his to "
            "give."
        ),
        "must_show": "the setting-apart with authority — Jesus's both hands firm on the called man's head, the man kneeling solemn and steadied, the moment weighty and real; authority given, not taken.",
        "must_not_show": "no halo or ring of light around either head; ordinary-sized; only Jesus in cream; whole natural hands; no second unlocked figure at the edge; no invented symbol; no panel or text.",
        "scene": (
            "Authority conferred, shown as weight and stillness: the called "
            "disciple kneels upright and steady while Jesus lays both hands "
            "firmly on his head and holds them there, the man's face grave and "
            "accepting, the moment heavy with real commissioning. Jesus's brown "
            "eyes are down on the man; his cream robe falls plain; his hands are "
            "whole and deliberate. The warm daylight is even across both, nothing "
            "rings either head, both are ordinary-sized men, and the grass behind "
            "them is empty of any other figure."
        ),
    },
    {
        "id": "v2-r167-b09", "out": "s09-never-just-a-title.jpeg", "seg": "n3",
        "window": "35.227-39.500", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": "And a calling is never just a title to wear. It is a sending.",
        "must_show": "the ordained man RISING to his feet on the hill, plain and unadorned, ready to move — a calling that is not a badge worn but a task to go and do; no ornament, no throne, just a man getting up to go.",
        "must_not_show": "NO Jesus in this frame and no cream; no crown, robe of office, medal, badge or ornament of rank; nobody a giant; distinct face; no face posed to the lens; no panel or text.",
        "scene": (
            "The point that a calling is work, not decoration: the just-ordained "
            "disciple is rising from his knees on the grassy hillside, one hand "
            "pushing off the ground, his plain earth-toned wool unmarked by any "
            "ornament or badge of rank, his face set and ready — a man getting up "
            "to GO and do a thing, not to stand and be admired. A couple of the "
            "other disciples stand near, also plain. The warm sun is clear; every "
            "figure is ordinary-sized with two hands and one head, none turned to "
            "the lens."
        ),
    },
    {
        "id": "v2-r167-b10", "out": "s10-meant-to-go.jpeg", "seg": "n3",
        "window": "39.500-43.800", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": "Those he chose were meant to go —",
        "must_show": "the disciples turning from the hilltop to set out — seen from behind, faces already toward the descending path and the country beyond, a band putting themselves in motion to go.",
        "must_not_show": "NO Jesus and no cream; travel clearly AWAY from the lens; distinct backs, not twinned; nobody a giant; no modern path or structure; no panel or text.",
        "scene": (
            "Sent men in motion: the small band of disciples has turned from the "
            "crest of the teaching hill and is starting down the grassy slope "
            "with their backs to the camera, faces already toward the descending "
            "path and the dun country spread below — a people set going. The warm "
            "morning light is ahead of them. Each is a distinct earth-toned "
            "figure of ordinary height, two hands and one head, seen from behind, "
            "no face toward the lens."
        ),
    },
    {
        "id": "v2-r167-b11", "out": "s11-out-to-the-villages.jpeg", "seg": "n3",
        "window": "43.800-48.098", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE-ROAD", "DISCIPLES"],
        "narration": (
            "out to the roads and the villages, to actually do the thing they had "
            "been set apart to do."
        ),
        "must_show": "the disciples walking the dirt lane INTO a small village, seen from behind, going to the actual work among ordinary houses and people — the sending carried out.",
        "must_not_show": "NO Jesus and no cream; travel away from the lens toward the village; distinct backs; no paved or modern road, no signpost or wire; no panel or text.",
        "scene": (
            "The work reached: the band of disciples walks the worn dirt lane "
            "with their backs to the camera, entering a small first-century "
            "village of pale flat-roofed houses and low dry-stone walls, a "
            "villager or two visible at a doorway ahead — the sent men arriving "
            "to do the thing they were set apart for. Dust rises softly at their "
            "heels in the warm daylight. Ordinary-height earth-toned figures, two "
            "hands and one head each, seen from behind; nothing modern lines the "
            "lane."
        ),
    },
    {
        "id": "v2-r167-b12", "out": "s12-the-measure-is-fruit.jpeg", "seg": "n4",
        "window": "48.098-52.700", "wide": False, "jesus": False, "ref": False,
        "locks": ["HARVEST-FIELD"],
        "narration": "The measure of it would be simple and real: fruit.",
        "must_show": "an insert of ripe standing barley — full golden heads heavy and bending in the harvest-morning light, the plain honest measure of the work, real and countable grain.",
        "must_not_show": "no Jesus and no cream; no people needed; no modern machine or fence; no invented symbol; no panel, border or text.",
        "scene": (
            "The measure shown as plain grain: a close, low insert into a field "
            "of ripe barley, the heavy golden heads bending together on their "
            "stalks in the warm harvest-morning light, dust and chaff hanging "
            "gold in the air behind them — honest fruit, the simple real measure "
            "of the work. The low dry-stone field wall sits soft and out of focus "
            "beyond. Nothing modern is anywhere in the frame."
        ),
    },
    {
        "id": "v2-r167-b13", "out": "s13-people-lifted-and-gathered.jpeg", "seg": "n4",
        "window": "52.700-57.700", "wide": False, "jesus": False, "ref": False,
        "locks": ["VILLAGE-ROAD", "DISCIPLES", "ORDINARY-FOLK"],
        "narration": (
            "Not applause, not a position, but honest results — good work done, "
            "and people lifted and gathered in,"
        ),
        "must_show": "a disciple lifting an ordinary person up — a hand under the arm raising a weary villager to their feet in the village lane — real people helped and gathered, the true result of the calling.",
        "must_not_show": "no Jesus and no cream; not a crowd — a close helping two-shot; distinct faces; whole hands, natural contact; nobody a giant; no panel or text.",
        "scene": (
            "The result shown as a person helped: in the village lane a disciple "
            "has bent and slipped a steady hand under the arm of a weary, "
            "careworn villager, raising them up onto their feet, the villager's "
            "face lifting with relief — good work actually done, one person "
            "lifted and gathered in, not applause or rank. Both are distinct "
            "earth-toned people of ordinary height, hands whole and natural, one "
            "head each, neither looking at the lens, in warm daylight."
        ),
    },
    {
        "id": "v2-r167-b14", "out": "s14-harvest-brought-home.jpeg", "seg": "n4",
        "window": "57.700-62.731", "wide": False, "jesus": False, "ref": False,
        "locks": ["HARVEST-FIELD", "ORDINARY-FOLK"],
        "narration": "like a harvest brought home.",
        "must_show": "a labourer carrying a bound sheaf of golden barley on the shoulder along the field's edge, gathered grain being brought in — the harvest carried home.",
        "must_not_show": "no Jesus and no cream; no modern machine, baler or fence; whole hands; profile or from behind, not posed to the lens; no panel or text.",
        "scene": (
            "The fruit gathered and carried in: a labourer walks the worn path at "
            "the field's edge with a full bound sheaf of golden barley hoisted on "
            "one shoulder, seen from the side so the gaze travels ahead down the "
            "path, more cut sheaves leaning together behind in the gold light — a "
            "harvest being brought home. A plain earth-toned figure of ordinary "
            "height, both hands steadying the sheaf, one head; nothing modern in "
            "the field."
        ),
    },
    {
        "id": "v2-r167-b15", "out": "s15-bring-forth-fruit-remain.jpeg", "seg": "kv16b",
        "window": "62.731-68.600", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": (
            "that ye should go and bring forth fruit, and that your fruit should "
            "remain:"
        ),
        "must_show": "SCRIPTURE-EXACT — Jesus back on the hill speaking to the small band, one open hand gesturing outward toward the country and the harvest beyond; teaching them to go and bear fruit that lasts.",
        "must_not_show": "no halo or light around Jesus's head; ordinary-sized; only Jesus in cream; the disciples NOT in cream; no face posed to the lens; no panel or text.",
        "scene": (
            "Jesus names the purpose: on the grassy hillside in warm daylight he "
            "stands among the small band of disciples, his warm brown eyes on "
            "them and one open hand sweeping outward toward the dun country and "
            "the far golden fields — sending them to go and bring forth fruit "
            "that would last. The disciples are turned to him, distinct "
            "earth-toned men seen from the side and behind. Jesus is an "
            "ordinary-sized man in plain cream wool, his hand open and whole, "
            "nothing ringing his head."
        ),
    },
    {
        "id": "v2-r167-b16", "out": "s16-ask-of-the-father.jpeg", "seg": "kv16b",
        "window": "68.600-74.335", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": (
            "that whatsoever ye shall ask of the Father in my name, he may give "
            "it you."
        ),
        "must_show": "SCRIPTURE-EXACT — Jesus lifting one open hand toward the warm light at the top of the frame as he speaks of asking the Father in his name; the disciples watching; heaven present only as light above.",
        "must_not_show": "the Father NEVER embodied — no figure, face or form in the sky, only warm light at the top edge; no halo or ring around Jesus's head; ordinary-sized; only Jesus in cream; no panel or text.",
        "scene": (
            "The promise of answered prayer: Jesus stands among the disciples and "
            "lifts one open hand and his warm gaze toward the soft warm light "
            "spilling from beyond the top edge of the frame, teaching them that "
            "whatever they ask of the Father in his name would be given — the "
            "Father present only as that high warm light, never a shape or a face "
            "in the sky. The disciples look the same way, distinct earth-toned "
            "men. Jesus is an ordinary-sized man in cream, his lifted hand whole "
            "and open, nothing lighting his own head."
        ),
    },
    {
        "id": "v2-r167-b17", "out": "s17-a-harvest-that-lasts.jpeg", "seg": "n5",
        "window": "74.335-79.100", "wide": False, "jesus": False, "ref": False,
        "locks": ["HARVEST-FIELD"],
        "narration": (
            "And what fruit it was to be: not a flash that fades, but a harvest "
            "that lasts."
        ),
        "must_show": "gathered barley sheaves standing bound and stacked together at the field's edge — grain safely brought in and keeping, an enduring harvest rather than something quick that fades.",
        "must_not_show": "no Jesus and no cream; no people needed; no modern silo, machine or fence; no invented symbol; no panel or text.",
        "scene": (
            "Endurance shown as stored grain: several bound sheaves of golden "
            "barley stand leaned and stacked firmly together against the low "
            "dry-stone field wall in the warm light, solid and settled — a "
            "harvest safely gathered in and keeping, not a bright thing that "
            "flares and is gone. The gold of the standing field carries on soft "
            "behind them. Nothing modern is anywhere in the frame."
        ),
    },
    {
        "id": "v2-r167-b18", "out": "s18-backed-with-power.jpeg", "seg": "n5",
        "window": "79.100-83.900", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": "Better still, the calling came backed with power —",
        "must_show": "a disciple kneeling in prayer on the hillside, hands open and lifted, face turned up toward the warm light above — a called man drawing on real power beyond himself.",
        "must_not_show": "NO Jesus and no cream; no figure or face in the sky; no halo or ring around the man's head — only warm light at the top edge; whole hands; nobody a giant; no panel or text.",
        "scene": (
            "The calling shown as backed from beyond: a lone disciple kneels in "
            "the grass of the hillside, his open hands lifted a little and his "
            "weathered face turned up toward the soft warm light coming from "
            "above the top of the frame, praying — a called man reaching for the "
            "power promised him. The light stays high at the frame's edge and "
            "never becomes a figure. He is an ordinary earth-toned man of "
            "ordinary height, hands whole and open, one head, nothing ringing it."
        ),
    },
    {
        "id": "v2-r167-b19", "out": "s19-heaven-answers.jpeg", "seg": "n5",
        "window": "83.900-88.618", "wide": False, "jesus": False, "ref": False,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": (
            "so that what these called ones asked of heaven, in the proper way, "
            "heaven would answer and give."
        ),
        "must_show": "the answer — warm light from above coming down onto the still-kneeling praying disciple, his upturned face lit and eased, a prayer heard and answered from heaven.",
        "must_not_show": "the Father NEVER embodied — no figure or face in the sky, only warm light at the top edge; no halo or ring around the man's head; ordinary-sized; whole hands; no panel or text.",
        "scene": (
            "Heaven answering, shown as light received: the same disciple still "
            "kneels with his hands open, and now the warm light from beyond the "
            "top of the frame falls fuller across his upturned face and shoulders "
            "and open palms, his expression easing into having been heard — the "
            "asking of heaven answered and given. The source stays high at the "
            "frame's edge, never a shape or a face. An ordinary earth-toned man "
            "of ordinary height, hands whole, one head, no ring of light on it."
        ),
    },
    {
        "id": "v2-r167-b20", "out": "s20-the-quiet-study-gem.jpeg", "seg": "n6",
        "window": "88.618-93.300", "wide": False, "jesus": False, "ref": False,
        "locks": [],
        "narration": (
            "Here is the quiet study gem. You do not license yourself into God's "
            "service, and you do not have to."
        ),
        "must_show": "a quiet study insert — an open first-century scroll lit by a small clay oil lamp, a reader's hand resting on the lines, the room still; the moment of noticing the truth in careful reading.",
        "must_not_show": "no Jesus and no cream; no modern book, paper or print; NO legible modern letters or numerals on the scroll; a small clay oil lamp only, no candle or glass; no ring of light around anything; no panel, border or text overlay.",
        "scene": (
            "The turn to close reading: an insert looking down at an open "
            "first-century papyrus scroll spread on a plain wooden table, a small "
            "shallow clay oil lamp beside it throwing warm low light across the "
            "lines, and a reader's weathered hand resting quietly on the words as "
            "if pausing on something just understood. The room is still and dim "
            "around the lamp. The scroll bears only plain ancient ink strokes, "
            "nothing legible or modern; the hand is whole with five fingers."
        ),
    },
    {
        "id": "v2-r167-b21", "out": "s21-calls-of-his-own-choosing.jpeg", "seg": "n6",
        "window": "93.300-98.200", "wide": False, "jesus": True, "ref": True,
        "locks": ["TEACHING-HILL", "DISCIPLES"],
        "narration": "He calls of his own choosing, by name, and ordains for the work.",
        "must_show": "Jesus reaching out to call a single ordinary man by name — Jesus's open hand extended to him across the hill, the man turning toward the call, plainly chosen by Jesus and not putting himself forward.",
        "must_not_show": "no halo or light around Jesus's head; ordinary-sized; only Jesus in cream; the called man NOT in cream; the man clearly being called, not stepping up on his own; no face posed to the lens; no panel or text.",
        "scene": (
            "The calling restated as Jesus's own act: on the hillside Jesus "
            "reaches an open hand toward a single ordinary man standing a little "
            "apart, his warm gaze fixed on him as though speaking his name, and "
            "the man has turned toward the call with a hand half-lifted in the "
            "recognition of being chosen — plainly summoned, not pushing himself "
            "forward. Jesus is an ordinary-sized man in cream, the man earth-toned "
            "and distinct; both have two hands and one head, the offered hand "
            "open, nothing ringing Jesus's head, in warm daylight."
        ),
    },
    {
        "id": "v2-r167-b22", "out": "s22-a-gift-you-receive.jpeg", "seg": "n6",
        "window": "98.200-104.884", "wide": False, "jesus": True, "ref": True,
        "locks": ["DISCIPLES"],
        "narration": (
            "To be called of God is a gift you receive, not a badge you take."
        ),
        "must_show": "the called man kneeling with open, upturned, empty hands RECEIVING as Jesus lays hands to ordain him — the calling taken as a gift given from above, never seized or worn.",
        "must_not_show": "no halo or ring of light around either head; ordinary-sized; only Jesus in cream; the man's hands OPEN and empty (receiving), never grasping a badge or object; whole hands; no second unlocked figure at the edge; no panel or text.",
        "scene": (
            "A gift received, not seized: the called man kneels with his hands "
            "turned open and empty and lifted a little, palms up, receiving — "
            "while Jesus lays a steady hand on him to ordain him for the work. "
            "The man takes nothing for himself; the whole picture is of something "
            "being GIVEN downward into open hands. Jesus's face is warm above "
            "him, no light around it; his cream sleeve falls from a real hand. "
            "Both are ordinary-sized men with whole hands and one head each, the "
            "background soft and clear of any other figure."
        ),
    },
    {
        "id": "v2-r167-b23", "out": "s23-still-goes-out-by-name.jpeg", "seg": "n7",
        "window": "104.884-110.200", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAKESHORE", "ORDINARY-FOLK"],
        "narration": (
            "And that call still goes out, still by name, still to ordinary "
            "people who never went looking for it."
        ),
        "must_show": "back on the ordinary shore — a plain working person pausing at their task, half-turning as if they have just heard their own name on the morning air; the call reaching an ordinary life still.",
        "must_not_show": "no Jesus and no cream; not posed to the lens — the head turns off the camera axis; nobody grand; no halo on anyone; no modern object; no panel or text.",
        "scene": (
            "The bookend: on the same lakeshore where the film began, an ordinary "
            "working person has stopped over their task — a hand still on a "
            "beached net — and half-turned their head to the side and up, as "
            "though catching the sound of their own name carried on the still "
            "morning air. The gaze travels off past the camera, not into it. The "
            "boat and pale water sit behind in the low gold light. A plain "
            "earth-toned figure of ordinary height, whole hands, one head, "
            "nothing modern anywhere."
        ),
    },
    {
        "id": "v2-r167-b24", "out": "s24-will-you-look-up-and-answer.jpeg", "seg": "n7",
        "window": "110.200-117.943", "wide": False, "jesus": False, "ref": False,
        "locks": ["LAKESHORE", "ORDINARY-FOLK"],
        "narration": (
            "When heaven singles you out and calls you by your own name, will you "
            "look up, and answer?"
        ),
        "must_show": "the same ordinary person now standing straight and looking UP toward the warm light above the shore, face open and on the edge of answering — the invitation handed to the viewer, left hopeful and open.",
        "must_not_show": "no Jesus and no cream; no figure or face in the sky — only warm light at the top edge; no halo or ring around the person's head; ordinary-sized; not posed to the lens; no panel or text.",
        "scene": (
            "The question left open: the same ordinary person has straightened up "
            "from the work on the shore and lifted their face toward the soft "
            "warm light spilling from above the top of the frame, expression open "
            "and stirred, weight shifting as though about to answer — the call "
            "handed across to the one watching. The light stays high at the "
            "frame's edge and never becomes a figure or a face. A plain "
            "earth-toned person of ordinary height, whole hands, one head, "
            "nothing ringing it, the lake calm and gold behind."
        ),
    },
]


# === PLACE-PLATES (generated by v2_stash.py; edit via the tool, not by hand) ===
# Each token's plate is attached as a PLACE LOCK image to every beat whose
# `locks` name it. Plates live in PLACE-REF/ (gitignored art); PLACE-WIRING.json
# is the committed record — `v2_stash.py --wire <this build>` rebuilds the
# plates on any machine that has the source builds' stills.
#
# EMPTY BY DESIGN. All four recurring places are NEW to keep this story's own
# warm-day / harvest-gold light arc, so there is no plate to wire at author
# time. The runner PROMOTES each from this build's first good NON-Jesus frame
# (never a Jesus frame — lesson 11):
#   LAKESHORE     promote b01, wire b02/b03/b23/b24
#   TEACHING-HILL promote b09 (first NON-Jesus hill frame), wire b10/b18/b19
#                 (b04-b08, b15, b16, b21, b22 are Jesus frames — prose place)
#   VILLAGE-ROAD  promote b11, wire b13
#   HARVEST-FIELD promote b12, wire b14/b17
# Full steps + optional cross-video landscape plates in QC.md.
PLACE_REFS = {
}
# === end PLACE-PLATES ===
