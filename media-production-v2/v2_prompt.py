#!/usr/bin/env python3
"""v2_prompt.py — the V2 prompt assembler. Shared by every V2 build.

WHY THIS EXISTS
---------------
V2-KICKOFF requires STYLE-V2 and JESUS LOCK v4 to appear **byte-identical** in
every prompt, and every character's description to stay byte-identical across all
of a video's prompts. Hand-copying a 900-character block into twenty prompts is
exactly how drift got into V1. Here the blocks are written ONCE and assembled
mechanically, so byte-identity is a property of the code instead of a thing QC
has to keep catching.

A build supplies a `beats_v2.py` next to itself with:

    BEATS = [ {id, out, seg, window, wide, jesus, locks, scene, model}, ... ]
    LOCKS = { "WOMAN": "...", ... }        # locks local to that video

and this module turns each beat into the full prompt string.

Usage:
    python3 v2_prompt.py <build-dir> --dump          # write ASSEMBLED-PROMPTS.txt
    python3 v2_prompt.py <build-dir> --check         # run the v4 checklist (step D)
    python3 v2_prompt.py <build-dir> --gen [--only b03 b04]   # generate via Flow
"""
import argparse
import importlib.util
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOW_DRIVER = os.path.join(ROOT, "media-production", "flow_driver.py")
JESUS_REF = "media-production-v2/JESUS-V2-REF/jesus-v2-face.jpeg"

# ---------------------------------------------------------------- BLOCKS ----
# STYLE-V2 — byte-identical opener of EVERY image prompt (V2-KICKOFF).
STYLE_V2 = (
    "Cinematic biblical realism: a lifelike scene from first-century Judea, like a "
    "still frame from a reverent, masterfully photographed biblical film. Natural "
    "cinematic lighting, true depth of field, real physical scale. Realistic faces, "
    "eyes, hands and anatomy; real fabric weave, wood grain, stone, dust and skin "
    "texture. Historically credible clothing of rough-woven wool and linen in earth "
    "tones; authentic architecture and landscape. Emotionally warm, reverent, and "
    "spiritually serious. Not cartoon, not comic, not anime, not plastic CGI, not a "
    "painted illustration, not a copy of any painting or artist's style. No text, "
    "captions, borders, panels, watermarks, or modern objects anywhere in the image."
)

# Lessons distilled from Cameron's retained review complaints. This is included
# byte-identically in every prompt so a good scene description cannot accidentally
# omit the basic continuity and physical-reality rules.
QUALITY_LOCK = (
    "CONTINUITY AND PHYSICAL-REALITY LOCK: every recurring person keeps the same "
    "face, age, build, hair, beard, and clothing colours from shot to shot. People "
    "remain at believable human scale relative to one another and the setting. Every "
    "visible person has one coherent body with exactly two arms and two legs, complete "
    "natural hands and feet, and clear joints. Limbs, clothing, and bodies remain "
    "outside solid wood, stone, furniture, boats, and other people. Feet and knees "
    "make correct contact with ground, deck, furniture, or water exactly as the story "
    "requires. Gaze, travel direction, object placement, cause and effect, and the "
    "number of named people must match the narrated moment. ROUGH-DRAFT CONTINUITY "
    "LAW: when an earlier story frame is supplied as the first reference, treat its "
    "camera angle, blocking, character positions, action, direction of travel and "
    "major objects as the approved rough draft. Improve photographic realism and "
    "repair named defects without reinventing the composition or staging. Reject any "
    "image that breaks these rules."
)

# DEFECT LOCK — added 2026-08-01 (Claude worker 8) after the reroll rate held at
# ~30% across builds 05/06/07/08/09/10 at a flat $0.134/image, i.e. $2-3 of pure
# waste per video. The SAME four defect families caused nearly every reroll:
#   1. the subject looking into the lens        (rows 9 s01/s09/s22/s28/s31, row 10 s01/s04/s31/s38)
#   2. a stray unlocked figure at the frame edge, usually in CREAM, i.e. a second
#      unlocked Jesus                            (row 9 s14, row 10 s22 x2, s26, s31)
#   3. uncountable quantities                    (row 8, the ten coins)
#   4. recurring cast drifting off their sheets  (row 9 s21: short-haired John)
#
# The wording below is PORTED, not invented — each sentence is the phrasing that
# measurably fixed the defect in the QC.md of the build named above. The key
# lesson, learned the expensive way on row 10 s22 (a bare prohibition failed
# TWICE, the geometry fixed it in one pass): state the GEOMETRY — where the
# camera sits relative to the eyeline and which frame edge the gaze exits
# through — instead of only forbidding "looking at the camera".
DEFECT_LOCK = (
    "CANDID-FRAME LOCK: this is a photograph of something happening, not a posed "
    "portrait. NOBODY IN THE PICTURE LOOKS INTO THE LENS. Every person's gaze is "
    "aimed at another person, an object, or a point off the frame, and exits the "
    "picture through a named edge — above, below, left or right of the camera — so "
    "no one's pupils are ever centred on the lens. When a figure faces the camera "
    "the head is turned off the camera axis and the eyes travel clearly past it. "
    "No one acknowledges being photographed, poses, or presents themselves to the "
    "viewer. "
    "CAST-CLOSURE LOCK: the frame contains only the people the scene actually calls "
    "for — the named figures plus any background people the scene itself describes, "
    "and nobody else. In particular no unexplained extra body, shoulder, arm, head, "
    "hair, headscarf or back crowds into the EDGES of the picture, in the foreground "
    "or the background, in focus or out of focus, and no blurred stranger passes "
    "through the frame. NO CREAM OR OFF-WHITE CLOTH APPEARS ON "
    "ANYONE BUT JESUS anywhere in the frame, including out-of-focus edges — a pale "
    "shoulder at the edge of a shot reads as a second, unlocked Jesus and fails the "
    "picture. "
    "COUNT-AS-GEOMETRY LOCK: any quantity the narration names must be literally "
    "COUNTABLE in the picture — laid out separated and individually visible, never "
    "a vague handful, heap or crowd standing in for a number. If the story says a "
    "number, the viewer must be able to count that exact number of objects or "
    "people, and no extra ones. "
    "ANCHOR-RESTATEMENT LOCK: every recurring person carries their own locked "
    "description into THIS frame — face, age, build, hair length, beard state and "
    "garment colour exactly as locked, even when they are small, distant, "
    "out of focus, or seen from behind. No locked character is ever redrawn as a "
    "generic bystander and no two of them are given the same face."
)

# PERIOD-MATERIALS — promoted into the shared recipe 2026-08-01 (Claude worker 13) on
# row 19, the first V2 build whose second half lives in an open BOAT on a SHORE. Rows
# 16 and 18 already paid for the interior half of this lesson twice (glass kerosene
# lamps, a wrought-iron candelabra, a modern fixture) and each time the fix was pushed
# into ONE build's HOUSE lock, so the next new setting had no protection at all. The
# defect family is the same one every time and it is not "lighting" — it is that a
# NEW SETTING invents MANUFACTURED OBJECTS: machined boat fittings, nylon rope,
# monofilament net, moulded floats, a painted hull, a metal cooking grill. Stated
# POSITIVELY (what everything IS made of) rather than as a prohibition list, per the
# row-10/row-14 geometry lesson.
PERIOD_MATERIALS_LOCK = (
    "PERIOD-MATERIALS LOCK: every object in the frame is something a first-century "
    "household or working crew could make by hand. Wood is hewn, adzed and pegged; "
    "rope and cord are twisted natural flax or hemp fibre; nets and baskets are "
    "hand-knotted or woven from plant fibre; vessels, lamps and jars are fired clay; "
    "blades, nails and tools are hand-forged iron or bronze showing hammer marks; "
    "cloth is hand-woven wool or linen in dyes of that place and century. EVERY OPEN "
    "FLAME IN THE FRAME, near or far, sharp or blurred, is either a bare wick standing "
    "in a shallow clay oil lamp, a torch, or a fire of wood or charcoal directly open "
    "to the air. NOTHING IN THE PICTURE IS MANUFACTURED, MOULDED, MACHINED OR "
    "INDUSTRIAL: no plastic, nylon, monofilament, synthetic cord or foam; no glass of "
    "any kind, no glass chimney, globe, lantern or kerosene lamp; no candle, "
    "candlestick, candelabra or hanging fixture; no machined metal fitting, cleat, "
    "screw, bolt, hinge, buckle, zip, wire, chain-link or sheet metal; no painted, "
    "varnished, fibreglass or white-hulled boat; no engine, motor or propeller; no "
    "cooking grill, grate, tripod or pan; no printed, stencilled or repeating-pattern "
    "fabric; no rubber, no cardboard, no paper label, and no writing, lettering or "
    "numerals on any object — EXCEPT the two things that legitimately carry them in "
    "this world: a STRUCK COIN, which correctly bears a ruler's head in profile and a "
    "worn Greek or Latin rim legend (Jesus points at exactly this in Matthew 22:20, "
    "'Whose is this image and superscription?'), and a HAND-INKED HEBREW SCROLL or "
    "written bill, whose letters are hand-drawn brush strokes on parchment, never "
    "printed type. Neither is a defect; do not reroll a coin for carrying its legend. "
    "GARMENT-CONSTRUCTION LOCK: every garment is built the way a first-century loom "
    "builds one — a straight woven rectangle of cloth with a plain slit or round neck "
    "opening, straight unshaped sleeves, a selvedge or frayed hem, and a rope, cord or "
    "folded-cloth sash knotted at the waist. A mantle or shawl is one loose rectangle "
    "of cloth draped over the shoulders. NO GARMENT IS A MODERN DRESSING GOWN OR "
    "BATHROBE: no shawl collar, no lapel, no revers, no front placket, no buttons, "
    "hooks or fastenings, no set-in tailored shoulder, no cuffed sleeve, no patch "
    "pocket, no wide flat sash tied in a bow at the front, and no towelling, terry, "
    "fleece, velour or quilted fabric anywhere. "
    "SANDAL-CONSTRUCTION LOCK: every sandal and every foot covering in the frame "
    "is built the way a first-century one is, and it is stated positively — a "
    "FLAT sole of layered rawhide or thick leather, cut to the shape of the foot "
    "with no heel and no shaping, and plain undyed leather THONGS AND STRAPS that "
    "pass up through slits cut straight through that sole and are fastened by "
    "being KNOTTED, TIED, OR TUCKED BACK THROUGH THEMSELVES, the loose end left "
    "hanging. NO SANDAL, SHOE OR STRAP IN THIS PICTURE CARRIES A BUCKLE OF ANY "
    "KIND: no buckle, roller buckle, frame, pin, prong, tongue, eyelet, grommet, "
    "rivet, stud, snap, clasp, hook, ring or fitting of metal anywhere on any "
    "footwear, near or far, sharp or blurred; and no moulded or rubber sole, no "
    "heel, no welt, no stitched rand, no tread pattern, no lace, no boot, no shoe "
    "with an upper enclosing the foot, and no maker's stamp, lettering or logo. "
    "This clause exists because 'no buckle' was already written into this block "
    "as one word in a prohibition list and the model put a brass roller buckle on "
    "a servant's sandals anyway (row 35, the servant anchor) — the geometry of "
    "how the strap fastens has to be stated, not just the fitting forbidden. "
    "WOVEN-CLOTH LOCK: every piece of cloth in the frame is WOVEN ON A LOOM and "
    "shows it — a visible over-and-under grid of warp and weft threads, slightly "
    "irregular, with a flat matte surface. NO CLOTH IS KNITTED OR MACHINE-MADE: no "
    "knit stitch, no purl, no rib, no cable, no jersey, no seed stitch, no stretchy "
    "cuff or collar band, no felted, fleeced, brushed, napped or looped pile, and no "
    "sweater, jumper or sweatshirt texture anywhere, including at a rolled sleeve, a "
    "wrist, a hem or a blurred edge. A close macro shot of a sleeve must still read "
    "as coarse hand-woven wool or linen, never as knitwear."
)

# HAND-IRRIGATION — promoted into the shared recipe 2026-08-02 (row 26, the mustard
# seed, the first V2 build staged in a WALLED KITCHEN GARDEN). Rows 16/18 paid for
# interior lighting, row 19 for boat fittings, row 22 for city skylines; a garden's own
# anachronism is MODERN BLACK DRIP-IRRIGATION HOSE — thin dark tubing lying along the
# beds, present in 4 of the first 24 frames (b10 b11 b17 b21) and invisible until you
# crop in. Nothing in PERIOD-MATERIALS covers it, because it is not a lamp, a fitting or
# a garment — it is a LINE ON THE GROUND. Ported byte-for-byte from the row 26 GARDEN
# lock, where it killed all four in ONE pass. Stated POSITIVELY per the row-10 geometry
# lesson. Any build staged in a garden, orchard, vineyard or irrigated field names
# "HAND-IRRIGATION" in that beat's `locks` list before the first paid image.
HAND_IRRIGATION_LOCK = (
    "HAND-IRRIGATION LOCK: ALL the water in this cultivated ground moves by hand and by "
    "gravity alone. The ONLY things that carry water are shallow open channels scraped "
    "into the bare earth between the beds and rows, a stone-lined cistern or well, and "
    "fired-clay jars carried by hand. Along every bed, row and path the ground is BARE "
    "SOIL, unbroken, with nothing lying on it or running across it. There is NO tube, "
    "hose, pipe, line, cord, wire, cable, tape, stake or fitting of any kind lying along "
    "or across any bed, row, path or channel, in focus or out of focus, in the "
    "foreground or the background; nothing black, dark grey or glossy runs in a straight "
    "line anywhere on the ground; and there is no drip irrigation, no sprinkler, no "
    "spigot, no valve and no pump anywhere in the picture."
)

# HAND-TOOLS — promoted into the shared recipe 2026-08-02 (row 28, hidden treasure, the
# first V2 build whose STORY TURNS ON A DIGGING TOOL: "his spade struck something hard").
# Rows 16/18 paid for interior lighting, row 19 for boat fittings, row 22 for city
# skylines, row 26 for irrigation hose, row 27 for knitted fabric. A working scene's own
# anachronism is THE TOOL IN THE HAND, and PERIOD-MATERIALS does not reach it: it says
# tools are "hand-forged iron or bronze showing hammer marks", which a modern steel garden
# spade with a D-handle and a foot tread satisfies perfectly while still being an object
# from a garden centre. The tool is also the largest, sharpest, most central object in a
# digging frame, so it is the one thing a viewer cannot fail to see. Stated POSITIVELY
# (what the tool IS and how it is built) per the row-10 geometry lesson. Any build where
# somebody digs, chops, reaps, hoes or carries names "HAND-TOOLS" in that beat's `locks`
# list before the first paid image.
HAND_TOOLS_LOCK = (
    "HAND-TOOLS LOCK: every tool in this frame is a first-century hand tool and is "
    "built the way a village smith and a carpenter build one. A DIGGING TOOL is a "
    "MATTOCK: one straight rough-hewn wooden haft about an arm and a half long, "
    "unpainted and unvarnished, with a single heavy hand-forged iron blade socketed or "
    "wedged onto its head at an angle, the iron dark grey, uneven, pitted and showing "
    "hammer marks, its working edge bright and worn thin from use. A basket is "
    "hand-woven from split reed or willow; a sack is coarse dark goat-hair cloth; a "
    "water vessel is fired clay. THE TOOLS ARE NOT MODERN AND NOT MANUFACTURED: there "
    "is no steel garden spade or shovel, no flat pressed-steel blade, no D-handle, no "
    "T-handle, no moulded grip, no foot tread or step on the shoulder of any blade, no "
    "shaft of tubular metal or fibreglass, no painted or powder-coated tool, no "
    "stainless or chromed metal, no machine-milled edge, no rivets, screws, bolts, "
    "clamps, collars or ferrules of stamped metal, no wheelbarrow, no pitchfork of "
    "welded tines, and no printing, lettering, numerals or maker's stamp on any tool "
    "anywhere in the picture."
)

# ANCIENT-ROAD — promoted into the shared recipe 2026-08-02 (row 29, the pearl of great
# price, whose merchant "spent his whole life traveling"). Rows 16/18 paid for interior
# lighting, row 19 for boat fittings, row 22 for city skylines, row 26 for irrigation
# hose, row 27 for knitted fabric, row 28 for the tool in the hand. A ROAD's own
# anachronism is THE SURFACE AND THE THINGS THAT LINE IT, and nothing above reaches it:
# a metalled surface, a kerb, a painted line, a tyre rut, a telegraph or power pole, a
# wire strung between poles, a guardrail, a culvert, a signpost. PERIOD-MATERIALS bans
# manufactured OBJECTS, but a road surface is not an object — it is the ground, which is
# exactly why it slips through. Roads recur constantly across the 200 stories (row 09
# and row 20 both live on one), so this belongs in the shared file rather than in a
# ninth build-local copy. Stated POSITIVELY (what the way IS) per the row-10 geometry
# lesson. Any build with a road, track, way or caravan route names "ANCIENT-ROAD".
ANCIENT_ROAD_LOCK = (
    "ANCIENT-ROAD LOCK: the way underfoot is a first-century road and it is nothing but "
    "GROUND. Its surface is bare packed earth and pale dust worn hollow by feet and "
    "hooves, with bedrock breaking through in places, loose stones kicked to the sides, "
    "and at most rough irregular field stones laid unevenly by hand where it crosses "
    "wet ground. The road has NO built edge and NOTHING LINING IT: no asphalt, tarmac, "
    "concrete, gravel bed, cobbled setts or any laid regular paving; no kerb, gutter, "
    "verge strip, drain, grating or culvert pipe; no painted line, marking, arrow or "
    "lettering of any kind on the ground; no wheel rut of a pneumatic tyre and no tread "
    "pattern anywhere in the dust; no post, pole, mast, pylon, telegraph pole or power "
    "pole standing beside it; no wire, cable or line strung anywhere across or along it "
    "or against the sky; no fence, railing, guardrail, barrier, chain or gatepost of "
    "manufactured metal; no signpost, milestone board, notice or painted sign; and no "
    "vehicle of any kind but a hand-built wooden cart on hewn spoked wheels. The only "
    "things travelling it are people on foot, laden donkeys, and camels in a string."
)

# MARKET-TOWN — promoted into the shared recipe 2026-08-02 (row 29, whose merchant works
# a trading town's market). Row 22 paid for the CITY SKYLINE half of this lesson (minaret,
# bell tower, tiled roof) inside one build's own lock, so the next town had no protection.
# A MARKET's own anachronism is the STALL: a modern market renders folding trestle tables,
# steel or aluminium poles, striped or printed awning fabric, plastic crates and trays,
# and painted price boards — none of which PERIOD-MATERIALS names, because it is written
# about objects a household makes, not about market furniture. The SKYLINE half is folded
# in here too so a town never has to re-learn it. Stated POSITIVELY per the row-10 lesson.
# Any build staged in a town, market, street or quay names "MARKET-TOWN".
MARKET_TOWN_LOCK = (
    "MARKET-TOWN LOCK: this is a first-century Levantine trading town and every built "
    "thing in it is hand-made from the stone, mud brick, timber and cloth of that place. "
    "BUILDINGS are dressed limestone blocks or tan mud brick with FLAT roofs of poles and "
    "packed earth, plain rectangular door and window openings with no glass, and outside "
    "stone stairs climbing to the roofs. A STALL is a low bench of dry-laid stone or a "
    "plank of hewn wood on stone blocks, shaded by ONE rectangle of undyed dark goat-hair "
    "cloth slung from rough wooden poles lashed with twisted fibre cord; goods sit in "
    "hand-woven reed baskets, fired-clay bowls and jars, and folded squares of plain "
    "hand-woven wool. AGAINST THE SKY THERE IS ONLY FLAT ROOFLINE AND BARE HILL: no dome, "
    "no minaret, no bell tower, no spire, no campanile, no clock, no crenellated parapet, "
    "no pitched roof, no roof tile, no shingle, no chimney, no gable, no half-timbering, "
    "no Gothic arch or tracery, no column with a carved capital, no corrugated or sheet "
    "metal, no aerial, no wire and no cable. IN THE MARKET THERE IS no folding table, no "
    "trestle, no metal pole, tube or scaffold, no umbrella, no striped, printed, dyed-"
    "pattern or synthetic awning, no plastic sheet, crate, tray, bag or bottle, no "
    "cardboard, no painted board, price sign, placard or lettering anywhere, and no "
    "modern person, garment, footwear or object among the crowd."
)

# NIGHT-LAMPLIGHT — promoted into the shared recipe 2026-08-02 (row 31, the ten virgins,
# Matthew 25:1-13, the first V2 build whose WHOLE PARABLE happens in the dark and whose
# ONLY light source is the thing the story is about). Rows 16/18 paid for interior
# lighting, row 19 for boat fittings, row 22 for city skylines, row 26 for irrigation
# hose, row 27 for knitted fabric, row 28 for the tool in the hand, row 29 for the road
# and the market stall. A NIGHT scene's own anachronism is THE LIGHT ITSELF, and it
# arrives in two distinct ways that nothing above reaches:
#
#   1. THE FIXTURE. PERIOD-MATERIALS already says every open flame is "a bare wick
#      standing in a shallow clay oil lamp, a torch, or a fire of wood or charcoal" —
#      but that sentence is one clause inside a 400-word block about materials, and when
#      the lamp is the SUBJECT of the picture rather than set dressing the model reaches
#      for the iconic thing instead: a glass hurricane lantern, a candle, a wick floating
#      in a glass of oil, a metal ring handle. Stated at length and positively here.
#   2. THE HALO. This is the one that breaks a STANDING LAW rather than a period rule.
#      A flame carried near a face is the single most reliable way to get a bright ring
#      of light around a head — hair lit from behind into a glowing outline — which is
#      exactly the rim-light/halo the project forbids on every frame, and it arrives by
#      PHYSICS, not by the prompt asking for it. A prohibition does not beat physics.
#      What beats it is GEOMETRY, per the row-10/row-14 lesson: put the flame LOW and IN
#      FRONT of the person, below the chin and nearer the camera than the head, so the
#      light can only travel upward onto the front planes of the face and the top and
#      back of every head stay unlit. A light source is never placed behind a head.
#
# Any build staged at night, before dawn, or in an unlit interior names "NIGHT-LAMPLIGHT".
NIGHT_LAMPLIGHT_LOCK = (
    "NIGHT-LAMPLIGHT LOCK: it is genuinely NIGHT and the darkness is real. The sky is "
    "deep blue-black with stars in it, the land reads as shape and silhouette, and "
    "colour survives only where a flame actually reaches. There is NO sun, no sun disc, "
    "no sunrise, no sunset, no dawn, no dusk band, no orange or pink horizon, no warm "
    "glow along any skyline, no blue-hour brightness, and no unexplained ambient fill "
    "lighting the scene from nowhere. Away from the flames the picture falls to near "
    "black and detail is lost, exactly as it does at night. "
    "THE LAMPS ARE THE ONLY LIGHT AND THIS IS WHAT ONE IS: a SMALL HAND-HELD "
    "FIRST-CENTURY CLAY OIL LAMP — a shallow closed oval of plain fired terracotta "
    "small enough to sit in a cupped palm, with a round filling hole in its top and a "
    "pinched spout at one end, and ONE single small soft yellow-orange flame standing "
    "at that spout on a BARE FIBRE WICK, smoking faintly. It is carried in the hand or "
    "cupped in both hands. THERE IS NO OTHER KIND OF LIGHT ANYWHERE IN THE FRAME: no "
    "candle, wax, taper or candlestick; no glass of any kind, no chimney, globe, shade, "
    "hurricane lamp, storm lantern, kerosene lamp or oil lantern; no metal lamp, no "
    "hanging fixture, no bracket, no ring handle, no wick floating in a glass or bowl "
    "of liquid; no electric light, bulb, filament, flashlight, string light or lit "
    "window frame of modern glass; and no firelight or torch except where the scene "
    "itself names one. "
    "NO HEAD IS EVER HALOED, AND THE CURE IS WHERE THE FLAME STANDS: every lamp, torch "
    "or fire in this picture is LOW AND IN FRONT OF the person it lights — below the "
    "chin, at chest or waist height, and NEARER THE CAMERA THAN THAT PERSON'S HEAD — so "
    "its light can only travel UPWARD AND FORWARD onto the front planes of the face, "
    "catching the underside of the brow, the nose, the cheekbones and the chin, while "
    "the crown, the back of the head, the hair and the shoulders stay UNLIT AND DARK "
    "and simply merge into the night behind them. NO LIGHT SOURCE OF ANY KIND STANDS "
    "BEHIND, ABOVE OR BEYOND ANYONE'S HEAD. There is NO bright rim, edge, outline, "
    "contour line, ring, corona, aura, halo, nimbus or glowing separation around any "
    "head, hair, shoulder or body anywhere in the frame; no hair lit from behind into a "
    "bright fringe; no person outlined against a brighter background; and nobody emits, "
    "radiates or is haloed by light. Skin near a flame is warmly lit, never luminous, "
    "and never gives off light of its own."
)

# BACKGROUND-CAST — promoted into the shared recipe 2026-08-02 (row 32, the talents, whose
# trading beats are staged in a working town full of extras). The DEFECT_LOCK's
# CAST-CLOSURE clause already forbids cream or off-white cloth on anyone but Jesus "including
# out-of-focus edges", and row 31 paid for the same lesson again in its own locks — and BOTH
# times it was written as a PROHIBITION, which is exactly the shape of wording rows 10 and 14
# proved does not hold. Row 32's very first trading frame came back with a pale-robed man
# standing among the donkeys in the blurred background: not at an edge, not a stray shoulder,
# just an ordinary extra the model dressed in the first colour it reached for.
#
# The failure is not "cream" — it is that the background population is UNSPECIFIED. When a
# prompt describes only the named figures, every other body in the frame is invented free-hand,
# and pale linen is the default costume for a biblical crowd. What fixed it in ONE pass was
# stating the background POSITIVELY AND CAPPED: how many people may be back there, that they
# are a dark mass head to foot, and which light-toned things in the picture are legitimate
# (stone, dust, basketry, bare skin) so the model has somewhere lawful to put brightness.
# Ported byte-for-byte from the row 32 TRADE lock. Any build with populated background —
# a town, market, quay, road, courtyard, crowd or working yard — names "BACKGROUND-CAST".
BACKGROUND_CAST_LOCK = (
    "BACKGROUND-CAST LOCK: the background population of this picture is stated "
    "POSITIVELY AND IS CAPPED. At most THREE other people are ever visible behind "
    "the named figures of the scene, and every one of them is dressed head to foot "
    "in ONE SOLID DARK SATURATED EARTH COLOUR — DARK UMBER, CHARCOAL, DEEP RUST, "
    "DARK OLIVE, DEEP INDIGO or DEEP MAROON — so that every human shape in the "
    "background, in focus or out of focus, near or far, sharp or blurred, is a DARK "
    "MASS from edge to edge. NOT ONE PERSON IN THE BACKGROUND WEARS CREAM, "
    "OFF-WHITE, IVORY, BUFF, BEIGE, TAUPE, SAND, KHAKI, WHITE, PALE GREY OR ANY "
    "LIGHT-TONED CLOTH, DRAPE, MANTLE, SHAWL, TUNIC, SASH OR HEAD COVERING; no pale "
    "figure stands in any doorway, among any animals, along any wall or at any edge "
    "of the frame; and no blurred stranger passes through the picture. THE ONLY "
    "LIGHT-TONED THINGS ANYWHERE IN THE FRAME ARE STONE, DUST, PLASTER, REED "
    "BASKETRY, RAW TIMBER AND BARE SKIN — and, where the scene itself places him, "
    "Jesus's own wool robe."
)

# ANCIENT-PRISON — promoted into the shared recipe 2026-08-02 (row 33, the sheep and the
# goats, whose sixth work of mercy is "I was in prison, and ye came unto me"). Rows 16/18
# paid for interior lighting, row 19 for boat fittings, row 22 for city skylines, row 26
# for irrigation hose, row 27 for knitted fabric, row 28 for the tool in the hand, row 29
# for the road and the market stall, row 31 for night lamplight, row 32 for the background
# crowd. A PRISON's own anachronism is THE CELL ITSELF, and nothing above reaches it: the
# word "prison" is one of the most modern-loaded nouns in English and the model reaches
# straight for a Victorian or American jail — round machined steel bars in a welded grid,
# a hinged barred door with a lock plate, a bunk, a concrete floor, a corridor of cells.
# PERIOD-MATERIALS bans manufactured OBJECTS but a cell is ARCHITECTURE, which is exactly
# why it slips through, the same way a road surface does. A first-century holding place is
# a pit, a cistern or a vaulted undercroft below a house or fortress, closed by a heavy
# timber grille or a stone slab, and the prisoner is held by hand-forged iron on his own
# limbs rather than by an engineered cage. Stated POSITIVELY per the row-10 geometry
# lesson. Prison recurs across the 200 (John the Baptist, Peter, Paul, Barabbas), so it
# belongs here rather than in a tenth build-local copy. Any build with a prison, cell,
# dungeon, pit or a person in chains names "ANCIENT-PRISON".
ANCIENT_PRISON_LOCK = (
    "ANCIENT-PRISON LOCK: this holding place is first-century and it is CUT AND BUILT, "
    "not manufactured. It is a low vaulted undercroft of rough dressed limestone blocks "
    "and packed earth beneath a larger building, its walls damp, stained and hand-chiselled, "
    "its floor bare trodden earth and worn stone with a little dirty straw in one corner. "
    "The ONLY opening is a small squat rectangle in the stone closed by a grille of THICK "
    "SQUARE-CUT TIMBER BARS — split beams the thickness of a man's forearm, adzed flat, "
    "unpainted, set upright into hand-cut sockets in the stone and lashed across with "
    "twisted flax cord — with a heavy hand-forged iron ring and staple pinned into the "
    "stone beside it, the iron dark grey, uneven, pitted and showing hammer marks. A "
    "prisoner is held by a hand-forged iron shackle closed round one ankle or wrist and "
    "a few heavy hand-forged links pinned to the wall. THIS IS NOT A MODERN JAIL: there "
    "are no round machined steel bars, no welded or riveted grid, no bar spacing of "
    "identical milled rods, no hinged barred door, no lock plate, keyhole, padlock, bolt "
    "or latch of manufactured metal, no cell block, corridor or row of cells, no bench, "
    "bunk, cot, mattress or blanket, no concrete, brick, plaster render, tile or poured "
    "floor, no drain, grating or pipe, no window glass or shutter, and no number, letter, "
    "sign, scratch-mark tally or graffiti anywhere on the walls."
)

# GRANARY-BARN — promoted into the shared recipe 2026-08-02 (row 34, the rich fool,
# Luke 12:16-21, the first V2 build whose STORY IS A BUILDING: "I will pull down my
# barns, and build greater"). Rows 16/18 paid for interior lighting, row 19 for boat
# fittings, row 22 for city skylines, row 26 for irrigation hose, row 27 for knitted
# fabric, row 28 for the tool in the hand, row 29 for the road and the market stall,
# row 31 for night lamplight, row 32 for the background crowd, row 33 for the prison
# cell. A FARM STORE's own anachronism is THE BARN ITSELF, and nothing above reaches
# it, for the same reason a road surface and a prison cell slip through: a barn is
# ARCHITECTURE, not an object. "Barn" is also one of the most modern-loaded nouns in
# English — the model reaches straight for an American red-boarded barn with a pitched
# shingle roof and a hayloft door, or for a galvanised grain silo with a hopper and an
# auger. PERIOD-MATERIALS bans manufactured objects but says nothing about a BUILDING'S
# form, and its "wood is hewn, adzed and pegged" clause is satisfied perfectly by sawn
# dimensional lumber that has merely been distressed. A first-century Judean farm stores
# grain in squat mud-brick and field-stone bins, in rock-cut plastered pits, and in
# baskets, sacks and jars. Stated POSITIVELY per the row-10 geometry lesson. Barns,
# granaries, storehouses and threshing floors recur across the 200 (Joseph in Egypt, the
# wheat and the tares, the barn of Matthew 6:26), so this belongs here rather than in an
# eleventh build-local copy. Any build with a barn, granary, storehouse, silo, grain pit
# or farmyard names "GRANARY-BARN".
GRANARY_BARN_LOCK = (
    "GRANARY-AND-BARN LOCK: on a first-century Judean farm a BARN is built by hand out "
    "of the ground it stands on, and this is what one IS. A granary is a squat round or "
    "rectangular bin of sun-dried MUD BRICK and undressed field stone, plastered over "
    "with mud and chopped straw and weathered to a pale tan, standing about the height "
    "of a man and a half, with a low domed or flat roof of poles, brushwood and packed "
    "earth, ONE small square filling hatch in the top reached by a few mud steps, and "
    "ONE low square drawing door near the ground, which is EITHER simply an open dark "
    "square hole in the mud brick with nothing in it, OR is closed by ONE single flat "
    "slab of undressed limestone leaned and wedged against the opening and packed "
    "round with mud. A GRAIN BIN HAS NO DOOR THAT SWINGS: there is no planked or "
    "boarded door, no vertical boards, no cross-batten or ledge-and-brace, no frame, "
    "no jamb of sawn timber, no hinge, strap hinge, pintle, iron band, nail head, "
    "handle, ring, latch, hasp, bolt or padlock anywhere on any opening. Bigger stores are PITS cut down into the bedrock, plastered and "
    "stone-lined, closed with a flat stone lid. Where a roof is carried, it is carried on "
    "ROUGH HEWN TIMBER BEAMS with the bark still on parts of them, adzed flat only where "
    "they bear, pegged and lashed with twisted flax cord. Grain lies in loose HEAPS on a "
    "plastered earth floor and is moved in HAND-WOVEN REED BASKETS, coarse dark "
    "goat-hair sacks and fired-clay jars. THIS FARM IS NOT MODERN, NOT AMERICAN AND NOT "
    "INDUSTRIAL: there is no metal or concrete silo, grain bin, hopper, chute, auger, "
    "elevator, conveyor or ducting; no corrugated iron, tin, sheet metal, cladding, "
    "guttering or downpipe; no sawn plank, board, batten, weatherboard, dimensional "
    "lumber, plywood, pallet or nailed timber frame; no red-painted or boarded barn, no "
    "pitched or gabled roof, no shingle, tile or thatch, no hayloft, loft door, gambrel, "
    "cupola or weather vane; no glass window, hinged door, latch, hasp, bolt or padlock; "
    "no concrete, cinder block, red fired brick, cement render or poured floor; no wire, "
    "cable, chain, pipe, vent, fan, ladder of milled rungs or painted surface; no "
    "printed sack, label, stencil, lettering or numeral anywhere on anything; and no "
    "tractor, trailer, machine, engine or wheel of pneumatic rubber in the picture."
)

# BANQUET-HALL — promoted into the shared recipe 2026-08-02 (row 35, the great banquet,
# Luke 14:16-24, the first V2 build whose STORY IS A MEAL IN A HOUSE: "A certain man made
# a great supper, and bade many"). Rows 16/18 paid for interior lighting, row 19 for boat
# fittings, row 22 for city skylines, row 26 for irrigation hose, row 27 for knitted
# fabric, row 28 for the tool in the hand, row 29 for the road and the market stall, row
# 31 for night lamplight, row 32 for the background crowd, row 33 for the prison cell, row
# 34 for the barn. A FEAST's own anachronism is THE FURNITURE AND THE TABLEWARE, and
# nothing above reaches it, for the same reason a road surface, a prison cell and a barn
# slip through: a dining room is ARCHITECTURE AND FURNISHING, not an object a household
# "makes by hand" in the sense PERIOD-MATERIALS means.
#
# "Banquet", "feast", "supper" and "table" are among the most loaded nouns in English and
# every one of them pulls a MEDIEVAL OR VICTORIAN HALL: a long high trestle table with
# high-backed carved chairs down both sides, a white linen tablecloth, stemmed goblets,
# knives and forks laid out, tiered candelabra or a hanging chandelier, a whole roast on a
# silver charger. PERIOD-MATERIALS bans glass and machined metal, but it says nothing
# about a table's HEIGHT, about CHAIRS, or about the SHAPE of the room — and a first-
# century Judean supper has none of those things. Guests RECLINE on their left elbows on
# low couches or floor mats around three sides of a low table, leaving the fourth side
# open for serving; the food is flat bread, olives, lentils, figs, roast lamb and wine in
# fired clay. Stated POSITIVELY per the row-10 geometry lesson. Meals recur constantly
# across the 200 (Cana, Levi's feast, Simon's house, the prodigal's feast, the wedding
# garment, the last supper), so this belongs here rather than in a twelfth build-local
# copy. Any build with a supper, feast, banquet, dinner or table names "BANQUET-HALL".
BANQUET_HALL_LOCK = (
    "BANQUET-HALL LOCK: this is a well-off first-century JUDEAN household's dining "
    "room and the meal is eaten RECLINING, not sitting. THE ROOM: a plain rectangular "
    "chamber of dressed limestone and mud-plaster washed pale tan, its flat ceiling "
    "carried on ROUGH HEWN TIMBER BEAMS with the adze marks still on them, its floor "
    "worn flagstones or beaten plaster spread with hand-woven wool mats and rugs in "
    "deep madder, indigo and umber, its walls bare or hung with ONE plain woven "
    "hanging, and its openings plain rectangular gaps with NO GLASS, closed only by "
    "panels of dark woven cloth. THE TABLE IS LOW — knee high at most — a slab or "
    "several slabs of adzed timber on short hewn legs, arranged in a U with three "
    "sides occupied and the FOURTH SIDE LEFT OPEN so servants can reach in. THE "
    "DINERS RECLINE: each guest lies propped on his LEFT elbow on a low couch, "
    "bolster, folded mat or cushion of plain hand-woven wool, his feet away from the "
    "table and behind him, eating with the RIGHT HAND ONLY. THE FOOD AND VESSELS: "
    "flat rounds of barley and wheat bread laid straight on the wood, shallow "
    "fired-clay bowls and platters of olives, lentils, greens, figs, dates, almonds "
    "and roast lamb or kid, coarse-ground salt in a small clay dish, and wine in "
    "plain fired-clay jars, jugs and unstemmed clay cups. Hands are washed from a "
    "clay ewer over a clay basin. THIS IS NOT A MEDIEVAL, VICTORIAN, EUROPEAN OR "
    "MODERN DINING ROOM: there is NO chair, high-backed chair, carved chair, stool, "
    "bench, settle, throne or seat with a back or legs of turned wood; no tall or "
    "waist-high table, no trestle, no long refectory board, no head of the table; no "
    "tablecloth, table runner, napkin, doily, placemat or embroidered linen of any "
    "kind on the table; no glass, stemware, goblet, chalice, wine glass, decanter or "
    "carafe; no silver, pewter, brass, gold or any polished metal plate, charger, "
    "tureen, tray, ewer or serving dish; no knife, fork, spoon, cutlery, place "
    "setting or carving set laid out for a diner; no candle, candlestick, candelabra, "
    "chandelier, sconce or hanging lamp fixture of metal or glass — the only flame is "
    "a bare wick in a shallow fired-clay oil lamp standing on the table or on a stone "
    "ledge; no fireplace, mantel, hearth surround, wainscot, panelling, cornice, "
    "moulding, arch of dressed voussoirs, column with a carved capital, tiled floor, "
    "patterned mosaic border, curtain rail, tie-back, painted mural, framed picture, "
    "mirror or hanging tapestry with a woven scene in it; and no printed, stencilled "
    "or repeating-pattern cloth anywhere in the room."
)

# Shared SETTING locks a build opts into by name in a beat's `locks` list. Unlike the
# blocks above they are NOT appended to every prompt — a boat scene has no irrigation —
# but they live here so the next garden does not have to re-learn the lesson.
SHARED_SETTING_LOCKS = {
    "ANCIENT-PRISON": ANCIENT_PRISON_LOCK,
    "BANQUET-HALL": BANQUET_HALL_LOCK,
    "GRANARY-BARN": GRANARY_BARN_LOCK,
    "BACKGROUND-CAST": BACKGROUND_CAST_LOCK,
    "HAND-IRRIGATION": HAND_IRRIGATION_LOCK,
    "HAND-TOOLS": HAND_TOOLS_LOCK,
    "ANCIENT-ROAD": ANCIENT_ROAD_LOCK,
    "MARKET-TOWN": MARKET_TOWN_LOCK,
    "NIGHT-LAMPLIGHT": NIGHT_LAMPLIGHT_LOCK,
}

# JESUS LOCK v4 — byte-identical in every prompt where Jesus appears.
# JESUS LOCK v5 — Cameron, 2026-07-30. Supersedes v4 once a face candidate is picked.
#
# His order: *"we need to make Jesus look more like the prince of peace 1 and 2 in MBM
# folder for examples and to mix that with what we know he might look like to detere
# the people who think he had to be middle eastern and to make sure that he has the
# 'his eyes as like a flame of fire'"*
#
# THIS REVERSES v4's own hard line ("Never Caucasian, never pale"), which Cameron wrote
# on 2026-07-15 and rejected finished work over. It is his call and it is recorded here
# so no future session "corrects" it back.
#
# ON THE TWO REFERENCE PAINTINGS: `Prince of peace 1.jpg` and `Prince of peace 2 .jpg`
# are Akiane Kramarik's paintings — the second is signed and watermarked. They are NOT
# attached as generation refs and the model is never told to match her work, because
# this ships in an app and that would make ~3,000 derivative copies of a living
# artist's paintings. What IS taken from them is a description of the QUALITIES
# Cameron is pointing at, which gets the same look without copying the paintings:
# longer tousled mid-brown hair with warm golden lights (not blue-black), a warm
# fair-olive complexion, pale luminous GREEN eyes, a straight noble nose, and above
# all a gentle, peaceful, unguarded expression rather than a grim reconstruction.
#
# ON "EYES AS A FLAME OF FIRE" (Revelation 1:14): that verse describes the GLORIFIED
# Christ in vision, and the no-halo/no-glow law still binds every mortal-ministry
# scene. So the fire is IN the iris — pale green shot through with amber and gold, lit
# from within, arresting — and the eyes do NOT emit light onto the face or surroundings.
# Literal glowing eyes across ~3,000 street-level scenes would read as horror, not
# reverence, and would break the anti-glow law on every frame.
JESUS_LOCK_V5 = (
    "JESUS LOCK v5: the SAME man as the attached JESUS-V2-REF image — identical face, "
    "hair and beard in every picture: a MIDDLE EASTERN JEWISH man of the first century "
    "about thirty-three years old, born and weathered in the Judean sun. His skin is "
    "WARM OLIVE-BROWN, sun-darkened and richly toned — clearly Middle Eastern, never "
    "fair, never pale, never European-looking. Strong Semitic features: a prominent "
    "aquiline nose, deep-set eyes under strong dark brows, high cheekbones, a broad "
    "weathered brow. Long thick tousled wavy hair to below the shoulders in DARK BROWN "
    "with warm sun-bleached bronze lights through it. A full dark brown beard. His "
    "EYES ARE THE FEATURE OF HIS FACE: large and deep-set, a LUMINOUS INDETERMINATE "
    "COLOUR you cannot quite name — green and amber and gold at once, lit from within "
    "like a flame of fire, piercing and alive and arresting, holding whoever meets "
    "them. The eyes themselves cast NO light onto his skin or surroundings. His "
    "expression is gentle, peaceful and unguarded — kindness and quiet strength, "
    "never stern, never grim. One plain undyed off-white cream wool robe with a simple "
    "mantle and cloth sash (only he wears cream), leather sandals. No halo, no glow, "
    "no rim-light, no light coming off him. Never Caucasian, never pale, never "
    "blue-eyed, never blond. "
    "HE IS DRY unless the narrated physical conditions actually wet him — rain, "
    "spray, immersion, washing, or another explicit water contact. In a dry scene his "
    "robe, hair and beard have no water droplets, drips, streams, runnels or wet "
    "strands. When he walks on water he is on TOP of it and therefore not wet; when "
    "he rides inside a boat through a breaking-wave storm, the spray correctly soaks "
    "him."
)

JESUS_LOCK_V4 = (
    "JESUS LOCK v4: the SAME man as the attached JESUS-V2-REF image — identical face, "
    "hair and beard in every picture: a Middle Eastern Jewish man of about thirty-three, "
    "warm olive-brown skin, strong kind weathered features, shoulder-length dark "
    "brown-black wavy hair, a full dark beard, striking natural GREEN eyes, one plain "
    "undyed off-white cream wool robe with a simple mantle and cloth sash (only he wears "
    "cream), leather sandals. No halo, no glow, no rim-light. Never Caucasian, never "
    "pale, never blue-eyed, never blond."
)

# Forced-wide defense line — required after STYLE-V2 on any WIDE or multi-figure
# shot that has a ref attached (the ref-echo failure, FLOW-BUILD-PLAYBOOK).
WIDE_DEFENSE = (
    "WIDE FULL-LENGTH SCENE with MULTIPLE PEOPLE — never a portrait, never a close-up "
    "of one face; the camera far enough back that the named figures are visible head "
    "to sandals."
)

# WIDE-SHOT CAMERA GEOMETRY — promoted into the shared recipe 2026-08-01 from row 14
# (ten lepers), where 5 of 9 rerolls were this ONE failure: b01 b04 b05 b12 b26 all
# came back as a posed line of men facing the lens. The DEFECT_LOCK does NOT beat it,
# because the scene text says the figures "stand large in the near foreground" and the
# model resolves that phrasing as a group portrait. What fixed it in ONE pass every
# time was naming where the camera sits relative to the subjects' BACKS. The sentences
# below are PORTED byte-for-byte from the accepted row 14 prompts (b04, b19, b29) —
# nothing here is newly invented wording.
#
# Beat authors: this block is the floor, not a substitute. On any wide multi-figure
# beat you STILL state the camera-to-back geometry in the scene text itself
# ("THE CAMERA STANDS BEHIND <them> AND SHOOTS PAST THEM: their BACKS fill the near
# frame ... not one face is turned toward the lens"), and for travel beats name which
# way the backs face so the direction of travel cannot reverse. `--check` warns when a
# wide beat's scene never names the camera's position.
WIDE_GEOMETRY_LOCK = (
    "WIDE-SHOT CAMERA-GEOMETRY LOCK: this group is not arranged for the camera. The "
    "camera stands behind or beside the near figures and shoots PAST them, so the "
    "near figures are seen from behind, from the side, or in three-quarter from "
    "behind — never squared up to the lens, and NOT ONE FACE IS TURNED TOWARD THE "
    "LENS. The people are never lined up shoulder to shoulder presenting themselves "
    "to the viewer, and anyone walking or running is seen from the side or from "
    "directly behind, moving across the frame or away from it, never advancing into "
    "the camera."
)

# POSITIVE-INVENTORY — promoted 2026-08-01 from row 14 b08, where a SECOND, UNLOCKED
# JESUS (long loose hair, bare face, pale robe) appeared standing inside the line of
# ten lepers. Prohibitions had not stopped it; stating identity and headcount as an
# inventory of what IS in the frame fixed it in one pass. Ported from that prompt.
POSITIVE_INVENTORY_LOCK = (
    "POSITIVE-INVENTORY LOCK: identity and headcount are stated as what IS in the "
    "frame, not as what is forbidden. Every figure carries the garment colour, head "
    "covering and hair locked to him. When the narration names a number, exactly that "
    "many people stand in the frame and no additional one — ten men and no eleventh — "
    "each separated far enough to be counted individually."
)

# The identity half of the same lesson. Only added where Jesus is actually in the
# beat, so it can never pull him into a frame he does not belong in. Kept to the
# clause that is true in EVERY story — row 14 also added "the only man with long
# loose hair and an uncovered face", which was true there because the ten had their
# faces wrapped; that half stays a per-beat line, not a shared one.
JESUS_INVENTORY_LOCK = (
    "HE IS THE ONLY MAN IN CREAM ANYWHERE IN THE FRAME."
)

# Anti-panel clause — mandatory on every wide multi-figure still (Standing Law e).
# V1's wording said "ILLUSTRATION"; V2 is photographic, so the noun changes and
# nothing else does.
ANTI_PANEL = (
    "SINGLE UNIFIED PHOTOGRAPHIC FRAME, one scene edge to edge, NOT a grid, triptych, "
    "stacked panels or comic strip, no dividing lines, one picture only."
)

CLOSER = "One single continuous scene edge to edge, no border. 9:16 vertical."

# Recurring cast comes from the one canonical CHARACTER LAW source.  The old
# V2 dictionary described only four apostles and contradicted the approved
# sheets (for example: it gave clean-shaven John a beard and changed Andrew's
# locked olive-drab tunic to rust).  A group scene must never invent the other
# eight men as generic bearded fishermen.
def _canonical_cast_locks():
    path = os.path.join(
        ROOT, "media-production", "CHARACTERS", "character_refs.py"
    )
    spec = importlib.util.spec_from_file_location("mbm_character_refs", path)
    refs_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(refs_mod)

    key_to_slug = {
        "PETER": "peter",
        "ANDREW": "andrew",
        "JAMES-Z": "james",
        "JOHN": "john-beloved",
        "PHILIP": "philip",
        "BARTHOLOMEW": "bartholomew",
        "MATTHEW": "matthew",
        "THOMAS": "thomas",
        "JAMES-A": "james-son-of-alphaeus",
        "THADDAEUS": "thaddaeus",
        "SIMON-Z": "simon-the-zealot",
        "JUDAS-I": "judas-iscariot",
    }
    locks = {
        key: refs_mod.lock_text(slug) for key, slug in key_to_slug.items()
    }
    roster = " ".join(locks[key] for key in key_to_slug)
    locks["TWELVE-CANONICAL"] = (
        "TWELVE CANONICAL-CAST LOCK: the companions are exactly the Twelve in "
        "their approved gospel order. Every named man below keeps his own locked "
        "face, age, build, hair, beard state and tunic; no two are interchangeable, "
        "no face is cloned, and clean-shaven John never grows a beard. " + roster
    )
    return locks


CAST_LOCKS = _canonical_cast_locks()

# Words that mean the wrong Jesus. Any of these in a prompt fails the checklist.
DRIFT_WORDS = ["caucasian", "pale skin", "blue-eyed", "blue eyes", "blond", "blonde",
               "halo", "glow", "glowing", "rim-light", "rim light", "backlit halo"]


def load_beats(build_dir):
    path = os.path.join(build_dir, "beats_v2.py")
    if not os.path.isfile(path):
        raise SystemExit(f"no beats_v2.py in {build_dir}")
    spec = importlib.util.spec_from_file_location("beats_v2", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["beats_v2"] = mod
    spec.loader.exec_module(mod)
    return mod


def assemble(beat, local_locks):
    """Build the full prompt string for one beat."""
    parts = [STYLE_V2, QUALITY_LOCK, DEFECT_LOCK, POSITIVE_INVENTORY_LOCK,
             PERIOD_MATERIALS_LOCK]
    if beat.get("wide"):
        parts.append(WIDE_DEFENSE)
        parts.append(WIDE_GEOMETRY_LOCK)
    # ANTI-PANEL ON EVERY BEAT, not just wide ones (row 2, b18). It used to ride
    # along with the wide defense line, so tight shots got no panel protection —
    # and b18, a tight shot, came back with a landscape pasted in above the wall
    # like a second panel. A panel artifact is not a wide-shot problem.
    parts.append(ANTI_PANEL)
    for name in beat.get("locks", []):
        block = (local_locks.get(name) or CAST_LOCKS.get(name)
                 or SHARED_SETTING_LOCKS.get(name))
        if block is None:
            raise SystemExit(f"{beat['id']}: unknown lock {name!r}")
        parts.append(block)
    if beat.get("jesus"):
        # LOCK v5 is the live lock (Cameron picked face E, 2026-07-30).
        # This line said V4 while v5 sat unused above it, so every prompt
        # kept describing the OLD face and fought the new reference image.
        parts.append(JESUS_LOCK_V5)
        parts.append(JESUS_INVENTORY_LOCK)
    if beat.get("must_show"):
        parts.append("STORY MUST SHOW: " + beat["must_show"])
    if beat.get("must_not_show"):
        parts.append("HARD REJECTION CONDITIONS: " + beat["must_not_show"])
    parts.append(beat["scene"])
    parts.append(CLOSER)
    return " ".join(" ".join(p.split()) for p in parts)


def check(build_dir, mod):
    """Step D — the v4 checklist that replaces the retired v3 gate."""
    fails, warns = [], []
    for beat in mod.BEATS:
        p = assemble(beat, mod.LOCKS)
        low = p.lower()
        if not p.startswith(STYLE_V2):
            fails.append(f"{beat['id']}: prompt does not open with STYLE-V2")
        if beat.get("jesus"):
            if JESUS_LOCK_V5 not in p:
                fails.append(f"{beat['id']}: Jesus shot missing byte-identical LOCK v4")
            if not beat.get("ref"):
                fails.append(f"{beat['id']}: Jesus shot missing the REF line")
        for field in ("must_show", "must_not_show"):
            value = str(beat.get(field, "")).strip()
            if not value or "TODO" in value:
                fails.append(f"{beat['id']}: {field} is missing or unfinished")
        for w in DRIFT_WORDS:
            # Negative terms are lawful in must_not_show. Drift words in the scene
            # itself still fail because scene prose is what the model depicts.
            if w in beat["scene"].lower():
                fails.append(f"{beat['id']}: drift word {w!r} in the scene text")
        if "cream" in low:
            for line in beat["scene"].split(". "):
                ll = line.lower()
                if "cream" in ll and "jesus" not in ll and "he " not in ll \
                        and "his " not in ll and "only he" not in ll:
                    warns.append(f"{beat['id']}: check cream usage — {line.strip()[:70]}")
        if "NEGATIVE" in beat["scene"].upper() or "negative prompt" in low:
            fails.append(f"{beat['id']}: NEGATIVE-PROMPT list is banned in V2")
        if beat.get("wide") and ANTI_PANEL not in p:
            fails.append(f"{beat['id']}: wide shot missing the anti-panel clause")
        # Row 14 lesson: on a wide multi-figure beat the shared blocks are not enough —
        # the SCENE text itself has to say where the camera stands relative to the
        # subjects' backs, or the model composes a posed line facing the lens.
        if beat.get("wide"):
            scene_low = beat["scene"].lower()
            if not any(k in scene_low for k in ("camera", "lens", "shot on")) or not any(
                k in scene_low for k in ("behind", "past them", "backs", "from the side",
                                         "profile", "three-quarter", "away from the")
            ):
                warns.append(
                    f"{beat['id']}: wide beat does not state camera-to-back geometry "
                    "in its own scene text (row 14: 5 of 9 rerolls were this)"
                )
        # A char_ref that does not exist must fail HERE, not after a credit is spent.
        for cref in beat.get("char_refs", []):
            path = cref if os.path.isabs(cref) else os.path.join(build_dir, cref)
            if not os.path.isfile(path):
                fails.append(f"{beat['id']}: char_ref missing on disk: {cref}")
        rough_ref = beat.get("rough_ref")
        if rough_ref:
            path = rough_ref if os.path.isabs(rough_ref) \
                else os.path.join(build_dir, rough_ref)
            if not os.path.isfile(path):
                fails.append(f"{beat['id']}: rough_ref missing on disk: {rough_ref}")
    print(f"checked {len(mod.BEATS)} beats in {os.path.basename(build_dir)}")
    for w in warns:
        print(f"  WARN  {w}")
    for f in fails:
        print(f"  FAIL  {f}")
    if fails:
        sys.exit(1)
    print("  v4 checklist: PASS")


def dump(build_dir, mod):
    out = os.path.join(build_dir, "ASSEMBLED-PROMPTS.txt")
    with open(out, "w") as f:
        for beat in mod.BEATS:
            f.write(f"### {beat['id']}  ->  {beat['out']}\n")
            f.write(f"# window {beat['window']}  seg {beat['seg']}  "
                    f"model {beat.get('model', 'Nano Banana Pro')}"
                    f"{'  REF ' + JESUS_REF if beat.get('ref') else ''}"
                    f"{'  ROUGH-REF ' + beat['rough_ref'] if beat.get('rough_ref') else ''}"
                    f"{''.join('  CHAR-REF ' + c for c in beat.get('char_refs', []))}\n")
            f.write(assemble(beat, mod.LOCKS) + "\n\n")
    print(f"wrote {out} ({len(mod.BEATS)} prompts)")


def _below_2k(path):
    """True if a still is smaller than Flow's 2K (1536x2752) 9:16 download.

    Checked from the JPEG header directly so it works with no Pillow dependency and
    costs nothing. A `.size` marker beside the file (written by flow_driver when it
    falls back) counts too, in case a file is unreadable.
    """
    if os.path.exists(os.path.splitext(path)[0] + ".size"):
        return True
    try:
        with open(path, "rb") as fh:
            data = fh.read(200000)
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            m = data[i + 1]
            if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                     0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                w = int.from_bytes(data[i + 7:i + 9], "big")
                return w < 1536
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                i += 2
                continue
            i += 2 + int.from_bytes(data[i + 2:i + 4], "big")
    except Exception:
        return False
    return False


def gen(build_dir, mod, only, redo=False):
    assets = os.path.join(
        build_dir, getattr(mod, "OUTPUT_ASSET_DIR", "assets")
    )
    os.makedirs(assets, exist_ok=True)
    for beat in mod.BEATS:
        if only and beat["id"] not in only:
            continue
        dest = os.path.join(assets, beat["out"])
        if not redo and os.path.exists(dest) and os.path.getsize(dest) > 50000 \
                and not _below_2k(dest):
            print(f"= {beat['id']} already present, skipping")
            continue
        if os.path.exists(dest) and _below_2k(dest):
            # A 1K still counts as MISSING, not as done. flow_driver falls back to
            # the 1K original when Flow's upscaler is down and drops a .size marker
            # so "a later pass can re-pull it" — but no later pass existed, so 159
            # of the first 424 pictures (rows 10-13 entirely) sat at 768x1376,
            # BELOW the 1080x1920 delivery size. That is the exact upscaling the
            # anti-shimmer law forbids. Treating sub-2K as missing makes every
            # runner lap re-pull them automatically until they come back at 2K.
            print(f"~ {beat['id']} is BELOW 2K — re-pulling", flush=True)
        prompt = assemble(beat, mod.LOCKS)
        if redo and beat.get("redo_prompt"):
            prompt += (
                " CORRECTION PASS: Preserve every part of the supplied current "
                "production frame that is not explicitly changed below. "
                + beat["redo_prompt"]
            )
        cmd = [sys.executable, FLOW_DRIVER, "gen",
               "--size", "2K",
               "--model", beat.get("model", "Nano Banana Pro"),
               "--prompt", prompt,
               "--out", dest]
        # The prior still is the approved rough-draft composition.  Attach it
        # first so a realism rebuild improves the picture instead of inventing
        # unrelated blocking and boat mechanics.
        redo_source = beat.get("redo_source", "current") if redo else "rough"
        if redo and redo_source == "current" and os.path.isfile(dest):
            cmd += ["--ref", dest]
        elif redo_source == "rough" and beat.get("rough_ref"):
            path = beat["rough_ref"] if os.path.isabs(beat["rough_ref"]) \
                else os.path.join(build_dir, beat["rough_ref"])
            cmd += ["--ref", path]
        if beat.get("ref"):
            cmd += ["--ref", os.path.join(ROOT, JESUS_REF)]
        # Character locks by IMAGE (CAST-BIBLE principle). Text locks alone did NOT
        # hold the elder son across row 2 (s16/s17/s18 came back as three different
        # men), so a build may point each recurring character at an ACCEPTED still of
        # its own and every later shot of that character gets it attached.
        for cref in beat.get("char_refs", []):
            path = cref if os.path.isabs(cref) else os.path.join(build_dir, cref)
            if not os.path.isfile(path):
                raise SystemExit(f"{beat['id']}: char_ref not found: {path}")
            cmd += ["--ref", path]
        print(f"=== {beat['id']} -> {beat['out']} ===", flush=True)
        r = subprocess.run(cmd, cwd=ROOT)
        print(f"=== {beat['id']} exit={r.returncode} ===", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build_dir")
    ap.add_argument("--dump", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--gen", action="store_true")
    ap.add_argument(
        "--redo", action="store_true",
        help="regenerate selected existing outputs, using each beat's correction note",
    )
    ap.add_argument("--only", nargs="*", default=None)
    a = ap.parse_args()
    bdir = os.path.abspath(a.build_dir)
    mod = load_beats(bdir)
    if a.check or not (a.dump or a.gen):
        check(bdir, mod)
    if a.dump:
        dump(bdir, mod)
    if a.gen:
        check(bdir, mod)
        gen(bdir, mod, a.only, redo=a.redo)


if __name__ == "__main__":
    main()
